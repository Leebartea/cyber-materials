#!/usr/bin/env python3
"""
guardrail.py — production-readiness check for the Cyber Materials courses.

Run from the repo root:

    python3 tools/guardrail.py                 # full check
    python3 tools/guardrail.py --no-net        # skip URL reachability (offline / CI without egress)
    python3 tools/guardrail.py --json          # machine-readable summary

Exit code 0 = production-grade gate PASSED, 1 = FAILED.

Every check here exists because a real defect got through. The comment above each
one names what it caught, so nobody deletes a check without knowing its cost.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import shutil
import subprocess
import socket
import sys
import tempfile
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSES = {
    "appsec": os.path.join(REPO, "cyber-full stack", "full_stack_appsec_app.html"),
    "guardians": os.path.join(REPO, "cyber-guardians", "cyber_guardians_app.html"),
    "scouts": os.path.join(REPO, "cyber-scouts", "cyber_scouts_app.html"),
}
# One claim ledger per course — what a source lookup settled, and when.
CLAIMS = {
    "appsec": os.path.join(REPO, "cyber-full stack", "CLAIMS.md"),
    "guardians": os.path.join(REPO, "cyber-guardians", "CLAIMS.md"),
    "scouts": os.path.join(REPO, "cyber-scouts", "CLAIMS.md"),
}

# ── thresholds ────────────────────────────────────────────────────────────────
# Ratchet: the expected-output coverage floor. Raise this as the backfill lands
# so coverage can never regress. Set to the current measured value.
COVERAGE_FLOOR = {"appsec": 95, "guardians_theory": 100, "guardians_lab": 100, "scouts_theory": 100, "scouts_lab": 100}
COVERAGE_TARGET = 95  # what "production grade" ultimately means for this gate

RESULT = {"pass": [], "fail": [], "warn": []}


def ok(check, detail=""):
    RESULT["pass"].append((check, detail))


def fail(check, detail):
    RESULT["fail"].append((check, detail))


def warn(check, detail):
    RESULT["warn"].append((check, detail))


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# ── 1. structural integrity ───────────────────────────────────────────────────
def check_parses(name, src):
    """Caught: nothing yet, but a stray </script> or unbalanced backtick inside a
    template literal silently truncates the whole app. Cheapest possible canary."""
    if not shutil.which("node"):
        warn(f"{name}: js-parse", "node not on PATH — skipped")
        return
    bad = []
    for i, body in enumerate(re.findall(r"<script[^>]*>([\s\S]*?)</script>", src)):
        if not body.strip():
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
            fh.write(body)
            tmp = fh.name
        r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
        os.unlink(tmp)
        if r.returncode:
            bad.append(f"script[{i}]: {(r.stderr.splitlines() or ['?'])[0]}")
    if bad:
        fail(f"{name}: js-parse", "; ".join(bad))
    else:
        ok(f"{name}: js-parse", "all <script> blocks parse")


def check_offline(name, src):
    """Caught: the courses must work with no network. A CDN <script src> would
    silently break every offline learner."""
    ext = re.findall(r'(?:src|href)="(https?://[^"]+)"', src)
    if ext:
        fail(f"{name}: offline", f"{len(ext)} external src/href: {sorted(set(ext))[:3]}")
    else:
        ok(f"{name}: offline", "0 external src/href refs")


def load_curriculum(name, src):
    """Extract the `const curriculum` object and eval it in node, so every other
    check runs against real data instead of regexes over HTML."""
    if not shutil.which("node"):
        return None
    i = src.index("const curriculum")
    tmpdir = tempfile.mkdtemp()
    out = os.path.join(tmpdir, "cur.js")
    for m in re.finditer(r"\n\};", src[i:]):
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(src[i : i + m.start() + 3] + "\nmodule.exports=curriculum;\n")
        if subprocess.run(["node", "--check", out], capture_output=True).returncode == 0:
            r = subprocess.run(
                ["node", "-e", f"process.stdout.write(JSON.stringify(require({out!r})))"],
                capture_output=True, text=True,
            )
            if r.returncode == 0:
                return json.loads(r.stdout)
    fail(f"{name}: curriculum-extract", "could not isolate/parse the curriculum object")
    return None


def module_texts(name, cur):
    """Yield (label, markdown) for every authored field, per course shape."""
    for m in cur.get("modules", []):
        label = f"{name} {m.get('num') or m.get('id')}"
        if name == "appsec":
            yield label, m.get("body") or ""
        else:
            yield label + "/theory", m.get("theory") or ""
            yield label + "/workbench", m.get("workbench") or ""
            lab = m.get("lab") or {}
            if isinstance(lab, dict) and lab.get("kind") == "paper":
                # A deliberately tool-free lab (risk register, ransomware tabletop):
                # `lab.mac` is markdown prose the app renders with <Prose>, not a script.
                # Wrapping it in a bash fence made it look like a terminal command and
                # tripped the prose-in-runnable-fence check for exactly the right reason.
                yield label + "/lab", lab.get("mac") or ""
            elif isinstance(lab, dict) and lab.get("mac"):
                # `lab.mac` stays one pristine copy-paste script; its expected result
                # lives in the sibling `lab.expected.mac` markdown, appended here so
                # an output fence there is credited to the lab's command block.
                exp = (lab.get("expected") or {}).get("mac") or ""
                yield label + "/lab", "```bash\n" + lab["mac"] + "\n```\n\n" + exp


# ── 2. authoring hygiene ──────────────────────────────────────────────────────
def check_fences_and_escapes(name, cur):
    """Caught: over-escaping (\\` rendering as a stray backslash) and unbalanced
    ``` fences, both of which swallow content silently. Real bugs in past passes."""
    bad_fence, bad_esc, bad_details = [], [], []
    for label, md in module_texts(name, cur):
        if not md.strip():
            continue
        if len(re.findall(r"^```", md, re.M)) % 2:
            bad_fence.append(label)
        if re.search(r"\\`", md) or re.search(r"\\\$\{", md):
            bad_esc.append(label)
        if md.count("<details>") != md.count("</details>") or md.count("<summary>") != md.count("</summary>"):
            bad_details.append(label)
    for tag, lst, msg in [
        ("fence-balance", bad_fence, "odd number of ``` fences"),
        ("escape-damage", bad_esc, "literal \\` or \\${ leaked into rendered text"),
        ("details-balance", bad_details, "unbalanced <details>/<summary>"),
    ]:
        if lst:
            fail(f"{name}: {tag}", f"{msg} in {lst[:5]}")
        else:
            ok(f"{name}: {tag}")


def check_renders(name, src, cur):
    """Caught: the `hr` bug — 154 literal '---' paragraphs across the AppSec course,
    because renderProse had no horizontal-rule handler. Runs the REAL renderer."""
    if not shutil.which("node"):
        warn(f"{name}: render", "node not on PATH — skipped")
        return
    i, j = src.index("function renderProse("), src.index("function renderInline(")
    tmpdir = tempfile.mkdtemp()
    rp = os.path.join(tmpdir, "rp.js")
    with open(rp, "w", encoding="utf-8") as fh:
        fh.write(src[i:j] + "\nmodule.exports=renderProse;\n")
    payload = os.path.join(tmpdir, "payload.json")
    with open(payload, "w", encoding="utf-8") as fh:
        json.dump([[l, m] for l, m in module_texts(name, cur) if m.strip()], fh)
    script = f"""
    const rp=require({rp!r}); const docs=require({payload!r});
    let literalHr=0, emptyCode=0, rawHeading=0; const where=[];
    const walk=(bs,l)=>(bs||[]).forEach(b=>{{
      if(b.type==='p'){{
        const c=String(b.content||'').trim();
        if(/^-{{3,}}$/.test(c)){{literalHr++; if(where.length<5)where.push(l+' [hr] ');}}
        if(/^#{{1,6}} /.test(c)){{rawHeading++; if(where.length<5)where.push(l+' [heading] '+c.slice(0,40));}}
      }}
      if(b.type==='code' && !String(b.content||'').trim()){{emptyCode++; if(where.length<5)where.push(l+' [empty-code]');}}
      if(b.inner) walk(b.inner,l);
    }});
    docs.forEach(([l,md])=>walk(rp(md),l));
    process.stdout.write(JSON.stringify({{literalHr,emptyCode,rawHeading,where}}));
    """
    r = subprocess.run(["node", "-e", script], capture_output=True, text=True)
    if r.returncode:
        fail(f"{name}: render", (r.stderr.splitlines() or ["?"])[0])
        return
    d = json.loads(r.stdout)
    problems = []
    if d["literalHr"]:
        problems.append(f"{d['literalHr']} literal '---' paragraphs (renderer missing hr handler?)")
    if d["rawHeading"]:
        problems.append(f"{d['rawHeading']} markdown headings rendering as plain text")
    if d["emptyCode"]:
        problems.append(f"{d['emptyCode']} empty code blocks")
    if problems:
        fail(f"{name}: render", "; ".join(problems) + f" — e.g. {d['where'][:3]}")
    else:
        ok(f"{name}: render", "no literal ---, no raw headings, no empty code blocks")


# ── 3. the expected-output gate (the core production-grade criterion) ─────────
#
# Every runnable block is classified into exactly one bucket. The buckets are
# deliberately narrow and mechanical so the number means the same thing to
# everyone who runs this, and so nothing is exempted by vibes.
#
#   fence     an output fence immediately follows  ..... THE documented convention
#   labelled  a bolded "**Expected observation:**" paragraph immediately follows
#   comment   a result comment sits inside the block ... weakest accepted form
#   gated     output fence lives in the next <details> Walkthrough (predict-first drill)
#   ---------------------------------------------------------------- exempt below
#   setup     every effective line is silent-on-success (mkdir/cd/install/...)
#   listing   the block is a file's contents (shebang), not commands to run
#   ---------------------------------------------------------------- counted as a gap
#   silent    a command that produces output, with no result shown anywhere
#
# Coverage = (fence + labelled + comment) / (total - exempt). Exempt blocks leave
# the denominator entirely rather than counting as free passes, and their count is
# printed so an exemption can never quietly grow.
RUNNABLE = {"bash", "sh", "shell", "zsh", "powershell", "console"}
OUTPUT_LANGS = {"", "text", "output", "out", "plain"}

# An inline result comment: "# root", "# => 3", "# prints 5". Requires an explicit
# result cue so an ordinary explanatory comment does not count as output.
RESULT_COMMENT = re.compile(
    r"(?m)^[^\n]*(?:#|//)[^\n]*(?:->|→|=>|\bprints?\b|\bshows?\b|you (?:should )?(?:see|get)|\boutputs?\b)"
)

# The labelled prose form, e.g. "**Expected observation:** Alice is gone".
# Anchored to the start of the text right after the block and required to be the
# bolded label the course actually uses. The previous version matched a bare
# "you see" anywhere in the following 450 chars, which passed `apt install` and
# `mkdir` blocks that show the learner nothing — a false pass, not coverage.
LABELLED_AFTER = re.compile(
    r"\A\s*(?:>\s*)?\*\*Expected (?:observation|output|result)s?[:.]?\*\*", re.I
)

# Commands that are silent on success. A block built only from these is exempt:
# inventing output for `mkdir` is noise, and the ledger's authoring rule 1 says so.
SILENT_CMDS = re.compile(
    r"^(?:sudo\s+)?(?:mkdir|cd|chmod|chown|touch|cp|mv|ln|export|set|unset|source|\.|"
    r"pushd|popd|rm|mkfifo|npm\s+(?:init|i|install|ci)|pnpm\s+(?:i|install)|yarn\s+(?:add|install)|"
    r"pip3?\s+install|python3?\s+-m\s+venv|brew\s+(?:install|tap)|apt(?:-get)?\s+install|"
    r"winget\s+install|go\s+install|cargo\s+install|pipx\s+install|git\s+clone)\b"
)

# The workbench drills are deliberately predict-first: "run this, write down what you
# expect, THEN open the walkthrough." For those, the output fence lives inside the next
# <details> Walkthrough rather than under the command — the learner is shown the result,
# just not before they have committed to a prediction. Counting those as a gap would push
# a future backfill into pasting the answer under the command and destroying the exercise.
# Kept deliberately tight: it must be the NEXT <details>, its summary must say
# walkthrough/answer/solution, it must actually contain an output fence, and no other
# runnable block may sit in between (so one walkthrough cannot cover a whole module).
DETAILS = re.compile(r"<details>\s*<summary>([^<]*)</summary>([\s\S]*?)</details>")
WALKTHROUGH = re.compile(r"walkthrough|answer|solution", re.I)


def gated_by_walkthrough(md, blocks, idx):
    b = blocks[idx]
    m = DETAILS.search(md, b["e"])
    if not m or not WALKTHROUGH.search(m.group(1)):
        return False
    if any(x["lang"] in RUNNABLE for x in blocks if b["e"] <= x["s"] < m.start()):
        return False
    return any(f["lang"] in OUTPUT_LANGS for f in fenced(m.group(2)))


# A line whose stdout is redirected into a file prints nothing to the terminal,
# whatever the command is: `cat > s.js <<'EOF'`, `printf ... > app.log`,
# `awk ... > out.txt`. Excludes `>&` (fd duplication) and `>(` (process substitution).
REDIRECT_TO_FILE = re.compile(r">>?\s*(?![&(])\S")


def fenced(md):
    out = []
    for m in re.finditer(r"```([^\n`]*)\n([\s\S]*?)```", md):
        out.append({"lang": m.group(1).strip().lower(), "code": m.group(2), "s": m.start(), "e": m.end()})
    return out


def effective_lines(code):
    """Command lines only: no comments, no blanks, and no heredoc payload — the
    body of `cat > f <<'EOF' ... EOF` is file content, not commands being run."""
    lines, in_heredoc, term = [], False, None
    for raw in code.split("\n"):
        line = raw.strip()
        if in_heredoc:
            if line == term:
                in_heredoc = False
            continue
        if not line or line.startswith("#"):
            continue
        m = re.search(r"<<-?\s*'?\"?([A-Za-z_][A-Za-z0-9_]*)'?\"?\s*$", line)
        if m:
            in_heredoc, term = True, m.group(1)
        lines.append(line)
    return lines


def classify(md, blocks, idx):
    """Return the bucket for blocks[idx]. Exactly one bucket applies.

    Order matters: the three 'shown' tests run FIRST, so a block that does show its
    result is never stolen by an exemption. (An earlier draft tested the shebang
    first and mis-filed a script that demonstrates quoting *and prints what it
    proves* as an exempt listing — undercounting real coverage.)
    """
    b = blocks[idx]
    code = b["code"]

    nxt = blocks[idx + 1] if idx + 1 < len(blocks) else None
    if nxt and nxt["lang"] in OUTPUT_LANGS and (nxt["s"] - b["e"]) < 600:
        return "fence"
    if LABELLED_AFTER.match(md[b["e"] : b["e"] + 300]):
        return "labelled"
    if RESULT_COMMENT.search(code):
        return "comment"
    if gated_by_walkthrough(md, blocks, idx):
        return "gated"

    lines = effective_lines(code)
    if not lines:
        # A runnable-tagged fence with nothing runnable in it: prose or, worse,
        # expected output authored as `#` comments instead of an output fence.
        return "prose_fence"
    if code.lstrip().startswith("#!"):
        # A file's contents. Its result belongs to the block that executes it.
        return "listing"
    if all(SILENT_CMDS.match(l) or REDIRECT_TO_FILE.search(l) for l in lines):
        return "setup"
    return "silent"


SHOWN = ("fence", "labelled", "comment", "gated")
EXEMPT = ("setup", "listing", "prose_fence")


def coverage(md):
    blocks = fenced(md)
    counts = {k: 0 for k in SHOWN + EXEMPT + ("silent",)}
    silent = []
    for idx, b in enumerate(blocks):
        if b["lang"] not in RUNNABLE:
            continue
        bucket = classify(md, blocks, idx)
        counts[bucket] += 1
        if bucket == "silent":
            first = next((l.strip() for l in b["code"].split("\n") if l.strip() and not l.strip().startswith("#")), "")
            silent.append(first[:60])
    return counts, silent


def check_coverage(name, cur):
    """Caught: the headline finding — most runnable command blocks showed the
    learner no expected result, so they had nothing to compare their terminal to."""
    buckets = {}
    for label, md in module_texts(name, cur):
        if not md.strip():
            continue
        # AppSec has one bucket; the module-shaped courses split theory from lab.
        # Keyed by course name — a lab in Scouts must never be graded against the
        # Guardians floor, or one course's regression hides behind the other's.
        key = "appsec" if name == "appsec" else f"{name}_{'lab' if label.endswith('/lab') else 'theory'}"
        counts, sil = coverage(md)
        b = buckets.setdefault(key, {"worst": [], **{k: 0 for k in SHOWN + EXEMPT + ("silent",)}})
        for k, v in counts.items():
            b[k] += v
        if counts["silent"]:
            b["worst"].append((counts["silent"], label, sil[:2]))
    for key, b in buckets.items():
        shown = sum(b[k] for k in SHOWN)
        graded = shown + b["silent"]
        if not graded:
            continue
        pct = round(shown / graded * 100)
        fence_pct = round(b["fence"] / graded * 100)
        floor = COVERAGE_FLOOR.get(key, 0)
        b["worst"].sort(reverse=True)
        worst = ", ".join(f"{l} ({n} silent)" for n, l, _ in b["worst"][:4])
        detail = (
            f"{shown}/{graded} = {pct}% (floor {floor}%, target {COVERAGE_TARGET}%) "
            f"[fence {b['fence']} · labelled {b['labelled']} · comment {b['comment']} "
            f"· gated {b['gated']} · exempt {sum(b[k] for k in EXEMPT)}]"
        )
        if pct < floor:
            fail(f"{key}: expected-output coverage", f"REGRESSED — {detail}; worst: {worst}")
        elif pct < COVERAGE_TARGET:
            warn(f"{key}: expected-output coverage", f"{detail} — below production target; worst: {worst}")
        else:
            ok(f"{key}: expected-output coverage", detail)
        # The convention is the output fence; the other two are tolerated legacy
        # forms. Surface the split so "coverage" can't be satisfied by comments alone.
        if fence_pct < pct - 25:
            warn(
                f"{key}: output-fence share",
                f"only {fence_pct}% of graded blocks use the documented output fence "
                f"(vs {pct}% counted as shown) — {b['comment']} rely on inline comments",
            )
        # A ```bash fence containing no runnable line is mis-tagged: it is prose, or
        # it is expected output written as `#` comments where an output fence belongs.
        if b["prose_fence"]:
            warn(
                f"{key}: prose in runnable fence",
                f"{b['prose_fence']} block(s) tagged runnable contain no command — "
                f"prose or output authored as comments; retag or convert to an output fence",
            )


# ── 4. known-bad content (regression guards for fixed defects) ────────────────
BANNED = [
    # (pattern, why it is banned, which finding it guards)
    # --- OWASP LLM Top 10: 2025 numbering superseded by the 2026 edition (Aug 2026).
    # Only LLM01/LLM02 kept their slots, so a pasted-back 2025 table row is silently
    # wrong rather than merely dated. Prose that cites the OLD id *with its year suffix*
    # (e.g. "System Prompt Leakage (LLM07:2025)") is deliberate and must not match.
    (r"\|\s*LLM03\s*\|\s*Supply Chain",
     "2025 numbering: Supply Chain is LLM04 in the 2026 edition", "LLM-2026"),
    (r"\|\s*LLM04\s*\|\s*Data and Model Poisoning",
     "2025 numbering: Data and Model Poisoning is LLM05 in the 2026 edition", "LLM-2026"),
    (r"\|\s*LLM05\s*\|\s*Improper Output Handling",
     "2025 numbering: Improper Output Handling is LLM10 in the 2026 edition", "LLM-2026"),
    (r"\|\s*LLM06\s*\|\s*Excessive Agency",
     "2025 numbering: Excessive Agency is LLM03 in the 2026 edition", "LLM-2026"),
    (r"\|\s*LLM07\s*\|\s*System Prompt Leakage",
     "2025 numbering + retired name: now LLM08 Hidden Context Exposure", "LLM-2026"),
    (r"\|\s*LLM08\s*\|\s*Vector",
     "2025 numbering: Vector/Embedding Weaknesses is LLM09 in the 2026 edition", "LLM-2026"),
    (r"\|\s*LLM09\s*\|\s*Misinformation",
     "2025 numbering: Misinformation is LLM07 in the 2026 edition", "LLM-2026"),
    (r"\|\s*LLM10\s*\|\s*Unbounded Consumption",
     "2025 numbering: Unbounded Consumption is LLM06 in the 2026 edition", "LLM-2026"),
    (r"9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08\s+data\.txt",
     "sha256 of 'test' presented as the hash of 'important data'", "A2"),
    (r"10-million-password-list-top-100000\.txt",
     "SecLists path that 404s — breaks the M6.1 cracking lab", "A1"),
    (r"osv-scanner/main/scripts/install\.sh",
     "osv-scanner install script that 404s", "A9"),
    (r"httpbin\.org",
     "httpbin is unreliable (503s, HEAD timeouts) — use a local server", "1.1 rewrite"),
    (r"still fires with the cookie on a top-level context",
     "wrong SameSite=Lax claim: a cross-site <img> is a sub-resource and IS blocked", "A4"),
    (r"approximately £25M",
     "Arup loss is ~US$25.6M, not £25M", "A7"),
    (r"an attacker remotely accessed the control system of the Oldsmar",
     "Oldsmar intrusion was never confirmed; FBI found no evidence", "A3"),
    (r"issuer=CN=DigiCert Global G2 TLS RSA SHA256 2020 CA1",
     "stale cert issuer for example.com (now Cloudflare)", "A6"),
    (r"^93\.184\.216\.34$",
     "stale example.com A record presented as expected dig output", "A5"),
    (r"\b60 modules across\b",
     "stale module count", "A10"),
    (r"echo '[^'\n]*\\\\n[^'\n]*'\s*>",
     "echo of a single-quoted string containing \\n redirected to a file: zsh's "
     "builtin echo expands \\n, bash's does not, so the file differs by shell", "A12"),
    (r"node\s+22-slim\s+a1b2c3d4e5f6",
     "invented IMAGE ID/size for node:22-slim presented as real docker images output", "A13"),
    (r"curl [^\n|]*(?:\s|\")\:[0-9]{2,5}/",
     "curl against a bare :PORT target — curl 8.x rejects it with "
     "'URL rejected: No host part in the URL'; write localhost:PORT", "A14"),
    (r"<\\\\/script>",
     "double-escaped closing script tag: renders a literal backslash into the "
     "command the learner runs (one \\ is correct inside the template literal)", "A15"),
    (r"dolevf/dvga(?![\s\S]{0,400}WEB_HOST)",
     "DVGA defaults WEB_HOST=127.0.0.1 and so binds the CONTAINER's loopback — "
     "-p 5013:5013 cannot reach it; pass -e WEB_HOST=0.0.0.0", "A16"),
    (r"bandit[^\n]*-ll[^\n]*hardcoded secrets",
     "bandit -ll reports medium+ only, and hardcoded-secret (B105) / assert (B101) "
     "findings are LOW — the flag silently filters out what the text promises", "A17"),
    (r"safety scan(?![\s\S]{0,700}(?:login|register|account))",
     "safety >=3 requires an account and prompts interactively, so it cannot run "
     "unattended — do not present it as a drop-in CVE feed", "A18"),
    (r"dependency-check-maven:check(?![\s\S]{0,600}nvdApiKey)",
     "dependency-check 13 aborts without an NVD API key (NoDataException: No "
     "documents exist) — it fails, it does not degrade", "A19"),
    (r"Semgrep flags[^\n]*concatenated SQL",
     "p/owasp-top-ten + p/javascript contain no Node SQLi taint rule that fires on "
     "pool.query(q) — verified: those two rulesets (and p/default) report only the "
     "eval, never line 9. The SQLi rule needs p/nodejsscan", "A21"),
    (r"npm install lodash@4\.17\.4\n(?![\s\S]{0,400}npm install express)",
     "the phase7-scanme app.js requires express and pg; installing only lodash leaves "
     "a 2-component dependency tree, so Module 7.2's SBOM demo has nothing to inventory "
     "and its 'dozens of components' claim is false", "A22"),
    (r"--format cyclonedx(?![\s\S]{0,1200}scanners vuln)",
     "trivy's cyclonedx output SILENTLY disables vulnerability scanning — the file is an "
     "inventory, not a scan result. Say so, and name --scanners vuln", "A23"),
    (r"bumping to \`?lodash@\^4\.17\.21",
     "4.17.21 is itself covered by newer lodash advisories (npm audit reports "
     "'lodash <=4.17.23'); the current fix is 4.18.x", "A24"),
    # NOTE the 4th element: an "acquitting" string. A plain lookahead was wrong here —
    # the required caveat can just as legitimately appear ABOVE the command (a YAML
    # comment on the step) as below it, and Python has no variable-width lookbehind.
    (r"safety check",
     "`safety check` prints a DEPRECATED banner (unsupported beyond 2024-06-01) and its "
     "replacement `safety scan` needs an interactive account login, so neither is a "
     "drop-in CI step — pip-audit is the one to depend on", "A25", "DEPRECATED"),
    (r"(?:listen\(|localhost:|127\.0\.0\.1:|-ti:|-i:|-p )(?:5000|7000)\b",
     "macOS AirPlay Receiver (ControlCenter) permanently binds ports 5000 and 7000, so a "
     "lab server there dies with EADDRINUSE and curl gets answered by AirTunes (a bare "
     "403 with Server: AirTunes/...). Verified on this machine. Use 5050/7010",
     "A26", "AirPlay"),  # acquits the note that TEACHES this, incl. `lsof -i:7000`
    (r"Secret +STRIPE_KEY +CRITICAL",
     "trivy's secret scanner reads FILE CONTENTS in layers, not image config metadata, so "
     "an ENV-planted key produces NO secret finding (verified: Secrets column reads '-'). "
     "docker history is what catches it", "A27"),
    (r"docker exec lab-good whoami(?![\s\S]{0,400}(?:not found|FAILS))",
     "distroless ships no shell and no coreutils, so `docker exec <distroless> whoami` "
     "fails with 'executable file not found in $PATH'. Verify the user from outside with "
     "docker inspect -f '{{.Config.User}}' or docker top", "A28"),
    (r"appsec-lab:hardened[^\n]*\n\s*Total: 0 ",
     "the distroless hardened image is NOT 0 CVEs — measured 6 (5 HIGH, 1 CRITICAL, all "
     "libssl3) vs 342 for node:22. Hardening is a ~98% reduction, not elimination", "A29"),
    (r"kindnet\\?`?\) does \*\*not enforce\*\*|kindnet\\?`?\) does not \*enforce\*",
     "stale: recent kindnet DOES enforce NetworkPolicy (verified kind v0.32.0 / "
     "kindnetd v20260528 / k8s v1.36.1 — attacker Pod goes 200 -> 000). Teach the A/B/A "
     "test instead of asserting either behaviour", "A30"),
    (r"kubesec scan default-deny\.yaml",
     "kubesec only scores WORKLOAD manifests; on a NetworkPolicy it returns 'could not "
     "find schema for NetworkPolicy' with score 0 — a passing-looking number for a scan "
     "that never happened. Point it at a Pod/Deployment",
     "A31", "could not find schema"),  # acquits the note that TEACHES this trap
    (r"kube-bench run --targets node(?![\s\S]{0,600}(?:version_mapping|on a node|kubectl run))",
     "kube-bench must run ON a Kubernetes node; on macOS it exits with 'unable to get "
     "benchmark version. error: config file is missing version_mapping section'. Run it "
     "in-cluster as a Pod with the hostPath mounts", "A32"),
    # A33: a truncated hash pasted as expected output must be as long as the slice() that
    # made it. 9.2's walkthrough showed the 12-char `ff8d9819fc0e` against the log written
    # by 9.1's `.slice(0, 8)` logger — and 40 failures against a 60-attempt burst. A learner
    # comparing terminals concludes their own correct run is wrong.
    (r"^\s*(?:#\s*)?\d+ +ff8d9819fc0e",
     "aggregation output showing the 12-char email_hash. 9.1's lab logger slices to 8, so "
     "its app.log aggregates to `ff8d9819`; only Build 1's logger.js emits 12", "A33",
     "slice(0, 12)"),   # acquits the Build 1 logger.js walkthrough, which really is 12
    (r"^\s*(?:#\s*)?40 +ff8d9819\b(?![\s\S]{0,200}logger\.js)",
     "9.1's lab burst is 60 attempts, so reusing its app.log aggregates to 60, not 40", "A33"),
    # A35: the com.apple.alf preferences domain no longer exists (verified absent on
    # macOS 26.5.1), so the firewall probe fails; routed through 2>/dev/null it printed
    # an EMPTY value into a posture report, which reads as a pass. Use socketfilterfw.
    (r"com\.apple\.alf",
     "the com.apple.alf defaults domain is gone on current macOS — the read fails and, "
     "silenced by 2>/dev/null, reports an empty firewall state that looks like a pass. "
     "Use /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate", "A35",
     "socketfilterfw"),  # acquits a passage that names the dead domain AND the fix
    # A36: same defect, same script — AutomaticCheckEnabled is absent from the
    # SoftwareUpdate plist on current macOS. `softwareupdate --schedule` is supported.
    (r"AutomaticCheckEnabled",
     "AutomaticCheckEnabled is no longer present in com.apple.SoftwareUpdate; the read "
     "returns nothing. Use `softwareupdate --schedule`", "A36"),
    # A34: neverssl.com accepts the TCP connection and then never answers — `nc` and
    # `curl` both hang and return nothing, so the "plaintext is readable" demo silently
    # produces no output and looks like the learner's own mistake. Same failure class as
    # httpbin (A?): a third-party host the lab's whole point depends on. example.com
    # serves plain HTTP on :80 without redirecting, and is IANA-reserved.
    (r"neverssl",
     "neverssl.com no longer responds (TCP connect succeeds, zero bytes returned) — the "
     "plaintext-vs-TLS demo silently shows nothing. Use example.com on port 80", "A34"),
    (r"hashcat -m 34000 -a 0 ~/argonhash\.txt",
     "hashcat v7 mode 34000 parses argon params as m,t,p but the node argon2 lib "
     "emits m,p,t — feeding the raw ~/argonhash.txt reports 0 cracked (not a crack); "
     "reorder to ~/argonhash.hc first", "A20"),
    # A37-A41 are the AppSec CLAIMS.md Batch 1 fixes. Every one of them was a
    # well-formed sentence naming a real standard, which is why nothing else in
    # this gate could see it; only a source lookup could. See
    # `cyber-full stack/CLAIMS.md` rows 4, 6, 7, 24, 31.
    (r"\bA\d{2}:2021\b",
     "superseded OWASP Top 10 edition numbering — the 2021 list was replaced by "
     "Top 10:2025 (purged at 173a31d; one survivor found in M10.1's capstone "
     "walkthrough at the Batch 1 claims pass). Cite A__:2025", "A37"),
    (r"\b14 chapters\b",
     "ASVS 5.0 has 17 chapters (V1 Encoding and Sanitization .. V17 WebRTC); 14 is "
     "the 4.0.3 count. Verified against the v5.0.0 flat JSON in OWASP/ASVS", "A38",
     # Acquit on the full phrase, not on a bare "4.0.3" — the edition number also
     # appears in neighbouring prose, and inside the 900-char window that was
     # enough to excuse a genuinely wrong "ASVS 5.0 has 14 chapters" sentence.
     "chapters of 4.0.3"),
    (r"\bV6 Session Management\b|\bV6\.2\.1\b",
     "ASVS V6 is Authentication in 5.0 and Stored Cryptography in 4.0.3 — Session "
     "Management is V7 (5.0) or V3 (4.0.3), and V6.2.1 exists in no edition. The "
     "CSPRNG session-token requirement is V7.2.3, and it is L1, not L2", "A39"),
    (r"Agentic Top 10",
     "no OWASP publication has that name. It is the `OWASP Top 10 for Agentic "
     "Applications` (GenAI Security Project, Dec 2025), numbered ASI01-ASI10 — and "
     "`excessive agency` belongs to the LLM list (LLM03:2026), not to it", "A40"),
    (r"CVE-2026-31789[^\n]*CRITICAL",
     "no vendor rates CVE-2026-31789 Critical — OpenSSL upstream and Red Hat rate it "
     "Low, SUSE `important`. A trivy fixture that inflates a real CVE's severity is "
     "the same defect class as inventing one", "A41"),
    # --- Batch 2 of the claim ledgers (rank claims). Unlike the Batch 1 defects,
    # every one of these is a fixed string, so a guard can hold it down.
    (r"most common full-stack language",
     "Node is a runtime, not a language, and the Intro says `pairing`. Stack "
     "Overflow 2025 ranks Node.js first among web technologies (48.7%) — the rank "
     "is fine, the noun was not (AppSec ledger row 34)", "A42"),
    (r"fastest-growing attack class",
     "A03:2025 Software Supply Chain Failures has the FEWEST occurrences in OWASP's "
     "collected data and placed on survey strength; the sourceable superlative is "
     "`highest debut in the list's history` (AppSec ledger row 35)", "A43"),
    (r"single most common cyberattack",
     "the rank inverted: DBIR 2026 puts vulnerability exploitation first at 31%, "
     "ahead of credential abuse and phishing. Teach the human-element share (62%), "
     "which does not depend on a ranking (Guardians ledger row 36)", "A44"),
    (r"TryHackMe\s+['\"]?Pro Hacker",
     "Pro Hacker is a HackTheBox rank (>45% of active content owned). TryHackMe "
     "uses 21 numbered levels, 0x1 Neophyte upward, and has no such rank "
     "(Guardians ledger row 37)", "A45"),
    (r"most common bug in real bug-bounty",
     "no published source ranks IDOR first; HackerOne's platform data puts XSS top. "
     "Hedged phrasing is fine — the unhedged #1 is the defect (Guardians row 38)", "A46"),
    (r"one of the largest DDoS attacks ever seen",
     "Dyn (2016) was the largest measured AT THE TIME; the record is now 31.4 Tbps "
     "(Q4 2025) and 1 Tbps+ attacks are routine. Bind a time-bound superlative in "
     "the sentence (Guardians ledger row 42)", "A47"),
    (r"launched a 1\.2 Tbps",
     "Dyn never confirmed a figure, reporting only `up to 50x normal` packet flow. "
     "1.2 Tbps is a third-party estimate and must be attributed as one "
     "(Guardians ledger row 42)", "A48"),
    # --- Batch 3 of the claim ledgers (quantity claims). Same property as Batch 2:
    # every defect is a fixed string, so a guard can hold it down.
    (r"trusted by 18,000\+ organi",
     "SolarWinds' own figure is FEWER than 18,000 customers *potentially affected* — "
     "the `+` inverts the bound — and it counts downloads of a trojanized build, not "
     "victims. SolarWinds puts the number actually compromised at fewer than 100 "
     "(Guardians ledger row 45)", "A49"),
    (r"settlement reached ~\$700M",
     "the FTC/CFPB/state settlement was *at least $575M*, rising to $700M only if the "
     "consumer fund ran short. $700M is the ceiling, not the amount paid "
     "(Guardians ledger row 46)", "A50"),
    (r"~\$1,649|the rebranded eLearnSecurity, ~\$200",
     "vendor exam prices rot: eJPT is $249 (not ~$200), PNPT $499 (not ~$400), OSCP+ "
     "$1,699 standalone (not ~$1,649), checked 2026-09-17. Date-bind the figures and "
     "say only the vendor's checkout is authoritative (Guardians ledger row 47)", "A51"),
    (r"flask-cors does exact-origin matching",
     "flask-cors matches with `re.match`, which anchors only at the START — a plain "
     "string origin also matches `https://app.example.com.evil.com`. It has no "
     "exact-match default; anchor the pattern yourself (AppSec ledger row 39)", "A52"),
    # Both branches negative-tested against the pre-fix file. The second needs the
    # `.{0,2}` because the course escapes its backticks (\`torch.load\`), so a
    # pattern written with bare backticks silently never matches.
    (r"torch\.load, which uses pickle|torch\.load.{0,2} uses pickle by default",
     "PyTorch 2.6 (Jan 2025) flipped `torch.load` to `weights_only=True`, a restricted "
     "unpickler that refuses the malicious file. Teach it as `weights_only=False` "
     "reaches pickle — mitigation, not repair (AppSec ledger row 40)", "A53"),
    (r"most Markdown renderers pass raw HTML through by default",
     "the renderers disagree and that is the lesson: `marked` and Python-Markdown pass "
     "raw HTML through, `markdown-it` ships `html: false`. Name them instead of "
     "generalising (AppSec ledger row 41)", "A54"),
    # --- Batch 4 of the claim ledgers (port claims in Guardians, quantity in
    # AppSec). Same property as Batches 2 and 3: every defect is a fixed string.
    # The `\*?` is load-bearing: the course writes `*named*` so the closing
    # asterisk abuts the word, and `.{0,3}` absorbs the escaped backtick (\`).
    # A first draft without both silently never matched — a dead guard scores
    # green forever, which is the exact failure this table exists to prevent.
    (r'named\*?\s+"?Elite"?\s+in\s+.{0,3}/etc/services',
     "`Elite` is nmap's own nmap-services name, not /etc/services. macOS "
     "/etc/services has no 31337 entry at all, and IANA assigns 31337/tcp to "
     "`eldim`. Three tables, three answers — that disagreement IS the lesson "
     "(Guardians ledger row 59)", "A55"),
    # WIDENED in Batch 5. The first version of this guard was the literal string
    # `60 known default username/password pairs`, copied from the one sentence
    # Batch 4 fixed — and a THIRD instance in the same module, worded `~60
    # **default username/password pairs**`, sat untouched and scored green for a
    # whole pass. A guard written from the wording of the instance you fixed only
    # ever proves that instance stayed fixed (Guardians ledger row 64).
    (r"\b~?60\b[^\n]{0,24}default username/password pairs",
     "Mirai's hardcoded table held 62 pairs, ten tried per host. It also scanned "
     "telnet on 2323 as well as 23, so a defence that names only 23 is incomplete "
     "(Guardians ledger rows 62, 64)", "A56"),
    (r"scrypt params in the OWASP ballpark",
     "OWASP lists no scrypt row with N=2^14 AND p=1 — its weakest fallback is "
     "N=2^14, r=8, p=5 and its minimum is N=2^17, r=8, p=1. A reduced benchmark "
     "setting must not be labelled as the standard's (AppSec ledger row 46)", "A57"),
    (r'body is exactly 6 bytes \(.{0,2}0\\+r\\+n\\+r\\+n',
     "`0\\r\\n\\r\\n` is FIVE bytes. The sixth byte counted by Content-Length: 6 is "
     "the `G`, and that byte is the entire CL.TE mechanism — dropping it makes the "
     "arithmetic unverifiable (AppSec ledger row 47)", "A58"),

    # --- Batch 5 of the claim ledgers (date claims in Guardians, law claims in
    # AppSec). The legal guards below are the highest-value entries in this table:
    # a wrong statutory deadline is the one class of error a learner can carry
    # into a real incident and cause harm with, and none of them is reachable by
    # any structural check.
    (r"median global dwell time[^\n]{0,60}was 10 days",
     "10 days is Mandiant's 2023 figure. The series went 16 (2022) -> 10 (2023) "
     "-> 11 (2024) -> 14 (2025, M-Trends 2026): the decade-long decline REVERSED. "
     "Never state a dwell-time number without its year (Guardians ledger row 65)",
     "A59"),
    (r"internally detected breaches it stretched much longer",
     "Inverted. Internal detection is the FAST path (9-day median); external "
     "notification is the slow one (25 days). The sentence taught the split "
     "backwards (Guardians ledger row 65)", "A60"),
    (r"Wombat/Proofpoint",
     "No such report exists: Wombat was absorbed into Proofpoint in 2018 and the "
     "State of the Phish report carries no AI-vs-human click-rate comparison. The "
     "2024 evidence pointed the OTHER way (Hoxhunt: AI still 10% behind human red "
     "teams in Nov 2024). The sourceable figure is Microsoft DDR 2025, 54% vs 12% "
     "(Guardians ledger row 66)", "A61"),
    (r"£\s?25M",
     "The Arup deepfake loss was HK$200M, about US$25.6M. Writing it as GBP "
     "converts the dollar figure into pounds and overstates it by ~25%; the "
     "reported number is HK$200M (Guardians ledger row 67)", "A62"),
    (r"personal use free",
     "Broadcom removed the personal-use restriction on 2024-11-11: Workstation "
     "and Fusion are free for commercial, educational AND personal use, and the "
     "paid Pro editions are no longer sold (Guardians ledger row 68)", "A63"),

    (r"HIPAA[^\n]{0,40}\b72[- ]hour",
     "HIPAA's Breach Notification Rule is 60 CALENDAR DAYS from discovery (45 CFR "
     "164.404-410), and a business associate has 60 days to tell the covered "
     "entity. The 72 hours is GDPR Art. 33, to a supervisory authority. Welding "
     "the two together is the most common compliance error in this course's "
     "subject area (AppSec ledger row 52)", "A64", "60 calendar days"),
    (r"[Ee]ncryption at rest and in transit \(both required",
     "Encryption is ADDRESSABLE under 45 CFR 164.312(a)(2)(iv) and (e)(2)(ii) - "
     "implement it or document an equivalent safeguard. The Jan 2025 NPRM would "
     "make it required but is still not final (OMB target 2027). Say `addressable, "
     "so encrypt anyway`, never `required` (AppSec ledger row 53)", "A65"),
    (r"six GDPR data subject rights",
     "GDPR Chapter III grants EIGHT rights (Arts. 15-22). `Six` is the number of "
     "LAWFUL BASES in Art. 6, which sits three paragraphs up the same page - and "
     "the table this tracker checks listed only five (AppSec ledger row 54)",
     "A66"),
    # WIDENED in Batch 6. This guard was written in Batch 5 from the AppSec
    # wording, which carried a comma: `EU residents, regardless of where`. The
    # Guardians course had the SAME error one comma away - `EU residents
    # regardless of where` - and this guard, which runs over every course in
    # COURSES, scored green over it for a full pass. Second time the ledger has
    # caught a guard cut to the shape of the one sentence it was born from
    # (cf. A56). The comma is now optional and `residents` may be `citizens`.
    (r"personal data of EU (?:residents|citizens),? regardless of where",
     "Art. 3(2) keys on data subjects `who are in the Union` - a location test, "
     "not residency or citizenship - and reaches a non-EU company only where it "
     "OFFERS goods/services to them or MONITORS their behaviour. Mere "
     "reachability from the EU is not enough (AppSec ledger row 55, Guardians "
     "ledger row 72)", "A67"),
    (r"PHI access[^\n]{0,40}retained for 6 years",
     "45 CFR 164.312(b) requires audit controls and sets NO retention period. The "
     "6 years is 164.316(b)(2), which covers DOCUMENTATION - your logging policy. "
     "Applying it to the log data is the conservative reading, not the text "
     "(AppSec ledger row 56)", "A68"),

    # --- Batch 6 of the claim ledgers (port claims in AppSec, law claims in
    # Guardians). The first four are one defect wearing four sentences: a
    # browser control was described at the wrong granularity, and a lab was
    # built on the description.
    (r"(?:port|:8000)[^\n]{0,80}DIFFERENT origin[^\n]{0,400}SameSite",
     "A second port makes a different ORIGIN, not a different SITE. SameSite is "
     "measured in sites - (scheme, registrable domain), no port - so "
     "localhost:8000 -> localhost:3000 is same-site and Lax does not fire. A "
     "CSRF lab that separates attacker from victim by port alone demonstrates "
     "the opposite of what it claims (AppSec ledger row 61)", "A69"),
    (r"SameSite=Lax\\?`? \(today's browser default\)",
     "Chrome/Edge apply Lax to an attribute-less cookie (Chrome 80, Feb 2020); "
     "Firefox never shipped it on release (bug 1617609, resolved without it) and "
     "Safari blocks third-party cookies instead. `The browser default` is one "
     "engine's behaviour, not the web's (AppSec ledger row 62)", "A70"),
    (r"SOP, CORS, cookie scope, CSP",
     "Cookie scope is NOT phrased against the origin triple. Cookies are scoped "
     "by domain and path and `do not provide isolation by port` "
     "(draft-ietf-httpbis-rfc6265bis-22 s8.5). Listing it beside SOP/CORS/CSP "
     "teaches that a second port isolates cookies, which is exactly the belief "
     "that breaks the 2.3 lab (AppSec ledger row 60)", "A71"),
    (r'"node server\.js"\s+Up \d',
     "`docker ps` COMMAND shows ENTRYPOINT+CMD truncated, and node:22-slim sets "
     "ENTRYPOINT [`docker-entrypoint.sh`], so the column reads "
     "`docker-entrypoint.s...`. The block also dropped the CREATED column, which "
     "docker ps always prints (AppSec ledger row 64)", "A72"),

    (r"the same packets are unauthorized access under the CFAA",
     "Overclaimed for a bare scan. US authority is one district case (Moulton v. "
     "VC3, N.D. Ga. 2000: no `damage`, no `access`); the UK convicted on far less "
     "(R v Cuthbert, 2005, s.1, no harm, no malicious motive). The honest "
     "teaching is that the answer differs by jurisdiction and you cannot know "
     "which applies before you send the packet (Guardians ledger row 75)", "A73"),
    (r"Cyber Resilience Act[^\n]{0,120}(?:applies|apply) from 11 Sep",
     "The CRA Art. 14 manufacturer reporting duty has been IN FORCE since "
     "2026-09-11; future tense is now stale. And 24h is only the EARLY WARNING "
     "in a 24/72/14 staircase - 72h notification, final report within 14 days of "
     "a fix (Guardians ledger row 74)", "A74"),
    (r"rights to know, delete, and opt out of the sale",
     "That is the 2018 CCPA list. CPRA added CORRECT, LIMIT use of sensitive "
     "personal information, and extended the opt-out to sale OR SHARING, all "
     "effective 2023-01-01. Naming CPRA while listing only the CCPA rights is "
     "three years stale (Guardians ledger row 73)", "A75"),
    (r"fines up to \*\*4% of global annual turnover\*\*",
     "Art. 83(5) is EUR 20 million OR 4% of global annual turnover, WHICHEVER IS "
     "HIGHER. Quoting only the percentage makes the ceiling look proportional to "
     "size; for a startup the EUR 20M is the binding figure (Guardians ledger "
     "row 72)", "A76"),

    # --- Batch 7 of the claim ledgers (`default` claims in Guardians, `date`
    # claims in AppSec). The Guardians defects share one shape: a vendor default
    # asserted as universal. A default is a property of ONE product at ONE
    # version, so a sentence of the form "X does Y by default" with no X named is
    # unfalsifiable and usually wrong for at least one X the learner will meet.
    (r"dev server that binds .{0,2}0\.0\.0\.0.{0,2} by default",
     "Dev servers disagree: `python3 -m http.server` and `next dev` bind every "
     "interface, Vite and Flask bind localhost and need `--host`. Name them. The "
     "durable lesson is that the printed banner is the address to CLICK, not the "
     "addresses bound - only `lsof` answers that (Guardians ledger row 78)", "A77"),
    (r"routers expose admin panel to WAN by default",
     "Backwards for retail gear: NETGEAR and TP-Link both document remote "
     "management as DISABLED by default. Real WAN-side admin exposure comes from "
     "ISP-supplied CPE, vendor cloud/app management, and stale manual changes "
     "(Guardians ledger row 79)", "A78"),
    (r'== listen\(5432, "0\.0\.0\.0"\)',
     "Node with no host arg binds `::` (IPv6 wildcard), not `0.0.0.0` - "
     "`server.address()` prints `::`. Reachability is the same on a dual-stack "
     "host, but a learner told to expect `0.0.0.0` will not find it "
     "(Guardians ledger row 80)", "A79"),
    (r"A fourth, \*\*HQC\*\*",
     "NIST calls HQC its FIFTH selected algorithm; the fourth is FN-DSA (Falcon), "
     "drafted as FIPS 206 and absent from the course. Same defect the Guardians "
     "ledger closed at its row 4, one course over (AppSec ledger row 67)", "A80"),
    (r"later revised to 167M\) password hashes",
     "The 2016 dump carried 117M email+password pairs; 167M is the record count "
     "including accounts with no password attached. 167M password HASHES is a "
     "figure nobody reported (AppSec ledger row 68)", "A81"),
    (r"This breached Apple, Microsoft, and dozens of others",
     "Alex Birsan's Feb 2021 research, every target inside a bug-bounty "
     "programme, $130k+ paid. Taught as an anonymous in-the-wild breach it loses "
     "the fact that the class was named by a PoC (AppSec ledger row 69)", "A82"),
    (r"a database with 143M SSNs",
     "143M was Equifax's FIRST count of people affected, revised to 147M; the "
     "FTC's SSN figure is 145.5M. The course quoted a superseded people-count as "
     "an SSN-count (AppSec ledger row 70)", "A83"),
    (r"Applications\*\* and an \*\*MCP Top 10\*\*",
     "The OWASP MCP Top 10 was not released in Dec 2025 and is not released now - "
     "its own roadmap puts it at Phase 3 of 5 (beta), entries `MCP01:2025`. Only "
     "the Agentic Top 10 (ASI01-ASI10) shipped (AppSec ledger row 71)", "A84"),
    (r"(?i)label+ed to (?:suggest|look like)[^.\n]{0,60}(?:did better|were picked up and opened)"
     r"|(?i:label+ed)[^.\n]{0,40}(?:did better than|more likely than|outperformed) unlabel+ed",
     "Tischer et al. (IEEE S&P 2016): NO drive design beat an unlabelled one, and "
     "return-address-labelled drives did WORSE (17/59 vs 27/60) because the finder "
     "had another way to reach the owner (Guardians ledger row 92)", "A85"),
    (r"(?i)(?:roughly|about|around|nearly) half[^.\n]{0,60}(?:find|return)[^.\n]{0,25}owner",
     "68% of USB-drop participants said they meant to return the drive; 'nearly "
     "half' is the paper's figure for those who opened the vacation photos FIRST. "
     "The two numbers describe opposite motives (Guardians ledger row 92)", "A86"),
    (r"(?i)\b1[34] (?:ATT&CK |enterprise )?tactics\b",
     "ATT&CK v19 (2026-04-28) has 15 enterprise tactics: TA0005 was renamed Stealth and "
     "TA0112 Defense Impairment was added (Guardians ledger row 96)", "A87"),
    (r"Defense Evasion",
     "TA0005 is 'Stealth' since ATT&CK v19; 'Defense Evasion' may appear only beside the "
     "new name, as history (Guardians ledger row 96)", "A88", "Stealth"),
    (r"(?i)\b(?:amcache|shimcache|appcompatcache)\b[^.\n]{0,80}\b(?:proves|confirms|shows|evidence of)\b[^.\n]{0,20}\bexecut",
     "Amcache/ShimCache show PRESENCE; on Windows 10/11 neither proves execution "
     "(Carvey 2024; Guardians ledger row 105)", "A89", "Presence is not execution"),
    (r"\bwindows\.malfind\b",
     "Volatility 3 2.28 moved malfind to windows.malware.malfind; the old name is a "
     "deprecated alias past its 2026-06-07 removal date (Guardians ledger row 109)", "A90"),
    # Raw-file scan: inside a template literal every backslash is doubled.
    (r"grep '(?:\\{1,2}\.){3}b'",
     "a Type filter of exactly '...b' drops birth rows that share their second with "
     "another time (m..b); match ',[m.][a.][c.]b,' (Guardians ledger Batch 10, fix 1)", "A91"),
    (r"(?i)\bno (?:file ?systems?|filesystems?) (?:records?|keeps?|stores?)\b[^.\n]{0,20}\bdeletion time",
     "false universal: ext4 keeps i_dtime and NTFS logs deletions in the USN journal; "
     "scope the claim to FAT (Guardians ledger row 118)", "A92"),
    (r"rstrip\(\s*[\"'] \(deleted\)",
     "str.rstrip strips a character SET ('failed' -> 'fail'); use removesuffix "
     "(Guardians ledger Batch 10, fix 3)", "A93"),
    (r"flags\s*=\s*int\.from_bytes\([^\n]*[\"']little[\"']",
     "FSEvents on-disk flags are read big-endian (FSEventsParser 4.1); little-endian "
     "never matches Removed 0x02000000 (Guardians ledger row 114)", "A94"),
    # The fetch line followed (after comment lines only) by anything but the delete.
    (r"(?m)^python3 fetch_isf\.py ntkrnlpa[^\n]*\n(?!(?:#[^\n]*\n)*find vol3 -name '[0-9A-F]+-\d+\.json\.xz' -print -delete)",
     "a typed symbol table fetched while Volatility's auto-generated STRIPPED table of the same "
     "name stays in the venv: which one loads is not deterministic, and a verbatim re-run "
     "printed nothing (Guardians ledger Batch 11, fix 1)", "A95"),
]


ACQUIT_WINDOW = 900  # chars either side of a hit in which an acquitting string may sit


def check_banned(name, src):
    hits = []
    for entry in BANNED:
        pat, why, fid = entry[:3]
        acquit = entry[3] if len(entry) > 3 else None
        for m in re.finditer(pat, src, re.M):
            if acquit and acquit in src[max(0, m.start() - ACQUIT_WINDOW) : m.end() + ACQUIT_WINDOW]:
                continue
            line = src[: m.start()].count("\n") + 1
            hits.append(f"{fid} @L{line}: {why}")
            break
    if hits:
        fail(f"{name}: known-bad content", "; ".join(hits))
    else:
        ok(f"{name}: known-bad content", f"{len(BANNED)} regression guards clear")


def check_rg_equivalence(name, src):
    """Caught: the course called `rg` and `grep -r` identical. They are not — rg
    skips hidden files and .gitignore'd paths, silently missing .env."""
    bad = []
    for m in re.finditer(r"[^\n]*\brg\b[^\n]*", src):
        line = m.group(0)
        claims_same = re.search(r"\bidentical\b|\bsame as\b|\bequivalent to\b", line, re.I)
        # A NEGATED claim ("not identical") is the correct teaching, and an ANALOGY
        # ("the find equivalent of rg vs grep") is not an equivalence claim at all.
        negated = re.search(r"\bnot\b[^\n]{0,12}(identical|same|equivalent)", line, re.I)
        if claims_same and not negated and "--hidden" not in line:
            bad.append(line.strip()[:80])
    if bad:
        warn(f"{name}: rg-vs-grep", f"claims rg/grep equivalence without --hidden: {bad[:2]}")
    else:
        ok(f"{name}: rg-vs-grep")


# ── 5. counts stay honest ─────────────────────────────────────────────────────
ATTACK_TABLE = os.path.join(REPO, "tools", "attack_ids_verified.json")


def check_attack_ids(name, src):
    """Every MITRE ATT&CK id taught must be one a claims pass actually verified.

    Like TOPIC_ANCHORS, the table is an authored assertion, not a derivation: no
    regex can know whether T1543 is a real technique or a typo for T1534. The
    table records what was checked against MITRE's STIX bundle and when, so a
    newly-added id fails the gate until someone verifies it too.

    Part B is the anti-rot half — an id in the table that no course mentions any
    more is dead weight and says so, exactly as the cross-reference anchors do.
    """
    if not os.path.exists(ATTACK_TABLE):
        fail(f"{name}: attack-ids", f"missing {ATTACK_TABLE}")
        return
    with open(ATTACK_TABLE, encoding="utf-8") as fh:
        table = json.load(fh)
    known = table.get("techniques", {})
    used = set(re.findall(r"\bT\d{4}(?:\.\d{3})?\b", src))
    if not used:
        ok(f"{name}: attack-ids", "course teaches no ATT&CK technique ids")
        return
    unverified = sorted(used - set(known))
    if unverified:
        fail(f"{name}: attack-ids",
             f"{len(unverified)} technique id(s) not in the verified table "
             f"({', '.join(unverified)}) — check them against MITRE's STIX bundle "
             f"and record the result in CLAIMS.md before teaching them")
        return
    ok(f"{name}: attack-ids",
       f"{len(used)} technique ids, all verified {table.get('_verified', '?')}")


def check_claims_ledger(name, src):
    """Every CVE the course teaches must be adjudicated in that course's CLAIMS.md.

    Same contract as check_attack_ids, one class along: no regex can tell whether
    CVE-2026-31789 is really CRITICAL, or whether CVE-2026-69246 exists at all.
    Only a lookup can, and the ledger is where a lookup is recorded. So the gate
    enforces the one thing it *can* see — that a lookup was written down — and a
    newly-taught CVE fails until someone adds its row.

    CVEs are the strictest identifier class the courses carry: each one is a
    single external fact (real / not revoked / that severity / that fixed
    version) sitting inside copy-pasteable scanner output a learner will trust.
    Both Batch 1 passes found a defect of exactly that shape.
    """
    ledger = CLAIMS.get(name)
    if not ledger or not os.path.exists(ledger):
        fail(f"{name}: claims-ledger", f"missing {ledger}")
        return
    with open(ledger, encoding="utf-8") as fh:
        text = fh.read()
    m = re.search(r"\*\*Last pass:\*\*\s*(\d{4}-\d{2}-\d{2})", text)
    if not m:
        fail(f"{name}: claims-ledger", f"{ledger} declares no `**Last pass:**` date")
        return
    used = sorted(set(re.findall(r"\bCVE-\d{4}-\d{4,7}\b", src)))
    missing = [c for c in used if c not in text]
    if missing:
        fail(f"{name}: claims-ledger",
             f"{len(missing)} CVE(s) taught but not adjudicated in {os.path.basename(ledger)} "
             f"({', '.join(missing)}) — verify each against NVD/GHSA and add a row "
             f"before teaching it")
        return
    # Count only the adjudicated rows, not the batch-plan table in Coverage that
    # precedes them — both are numbered markdown tables, so anchor on the Batch
    # headings. Every `## Batch N` section counts, or the total silently freezes
    # at Batch 1 while the ledger grows underneath it.
    batches = re.split(r"^## Batch \d+", text, flags=re.M)[1:]
    rows = sum(len(re.findall(r"^\| \d+ \| ", b.split("\n## ", 1)[0], re.M))
               for b in batches)
    # The row numbers are a single sequence across batches; a duplicate means a
    # batch was numbered from 1 again and two different claims share an id.
    nums = [int(n) for b in batches
            for n in re.findall(r"^\| (\d+) \| ", b.split("\n## ", 1)[0], re.M)]
    dupes = sorted({n for n in nums if nums.count(n) > 1})
    if dupes:
        fail(f"{name}: claims-ledger",
             f"duplicate row number(s) {dupes} in {ledger} — row ids must be a "
             f"single sequence across batches so a row can be cited unambiguously")
        return
    # `PENDING` is a legitimate state *during* a pass and a lie after it: a row
    # that says "not searched this pass" is an unverified claim still being
    # taught. Batch 2 closed with three of them and the gate stayed green, so
    # count them out loud — the ledger's own promise is that nothing ships
    # unadjudicated.
    pending = [n for b in batches
               for n in re.findall(r"^\| (\d+) \| .*?\| `PENDING` \|",
                                   b.split("\n## ", 1)[0], re.M)]
    if pending:
        warn(f"{name}: claims-ledger",
             f"row(s) {', '.join(pending)} in {os.path.basename(ledger)} are "
             f"`PENDING` — each is a claim the course still teaches and no one "
             f"has checked; close them or restate the claim so it needs no check")
        return
    ok(f"{name}: claims-ledger",
       f"{rows} adjudicated rows across {len(batches)} batches, 0 pending, last "
       f"pass {m.group(1)}; all {len(used)} taught CVEs covered")


def check_attack_table_rot(sources):
    """An entry no course uses any more is decoration; say so rather than carry it."""
    if not os.path.exists(ATTACK_TABLE):
        return
    with open(ATTACK_TABLE, encoding="utf-8") as fh:
        known = json.load(fh).get("techniques", {})
    seen = set()
    for src in sources:
        seen |= set(re.findall(r"\bT\d{4}(?:\.\d{3})?\b", src))
    stale = sorted(set(known) - seen)
    if stale:
        warn("attack-ids: table rot",
             f"{len(stale)} verified id(s) no longer taught anywhere ({', '.join(stale)}) — drop them")
    else:
        ok("attack-ids: table rot", f"all {len(known)} verified ids still in use")


def check_counts(name, src, cur):
    """Caught: 'ps60 modules' after the real count had drifted to 64."""
    mods = cur.get("modules", [])
    if name == "appsec":
        real = len([m for m in mods if (m.get("body") or "").strip() and m.get("id") != "m_intro"])
    else:
        real = len([m for m in mods if not str(m.get("id", "")).endswith("roadmap")])
    # Caught (2026-09): the count was stated four ways and only ONE of them matched a
    # pattern here, so three claims sat unchecked for the whole production sign-off.
    # A guard pinned to one phrasing of a claim is a guard pinned to an example.
    claimed = [int(x) for x in re.findall(r"\*\*(\d+) modules\b", src)] + \
              [int(x) for x in re.findall(r"All (\d+) modules\b", src)] + \
              [int(x) for x in re.findall(r"\*\*(\d+)-module\b", src)] + \
              [int(x) for x in re.findall(r"across (\d+) modules\b", src)] + \
              [int(x) for x in re.findall(r"for (\d+) modules\b", src)]
    wrong = [c for c in claimed if c != real]
    if wrong:
        fail(f"{name}: module-count", f"page claims {wrong}, actual is {real}")
    else:
        ok(f"{name}: module-count", f"{real} modules, claims consistent")


# ── 5b. cross-references resolve, and point at a module that covers the topic ─
#
# Caught: "Intelligence Gathering — OSINT and recon (Module 12)". Module 12 is Nmap:
# active scanning. It taught no OSINT at all, and the course had no OSINT module to
# point at. Every check above this one is closed over the repo's own text, so the
# sentence was self-consistent and the gate stayed green through a production sign-off.
#
# Part A (resolution) is mechanical: a pointer must name a module that exists.
# Part B (topic) cannot be: no regex over the corpus knows that Nmap is not OSINT.
# So the claim is AUTHORED here — an anchor says "this term belongs to these modules",
# and any sentence that names the term and also points at a module must point at one of
# them. That is a human assertion about ownership, which is exactly the thing a
# text-derived check can never supply. Part C keeps the anchors themselves honest.
#
# Adding an anchor is one line. Add one whenever a topic gets its own module, because
# that is precisely when older cross-references start pointing at the wrong place.
# Guardians writes both "M12" and "Module 12"; AppSec numbers its modules 7.2 / 7.5.4
# and never uses the bare-M shorthand — where a bare "M2" is the Apple silicon chip, not
# a cross-reference. One pattern for both would read the hardware as a dangling pointer.
MODULE_REF = {
    "guardians": re.compile(r"\b(?:M|Modules?\s+)(\d+(?:\.\d+)*)\b"),
    "appsec": re.compile(r"\bModules?\s+(\d+(?:\.\d+)*)\b"),
    # Scouts numbers S1.1 and always writes the dot, so "AWS S3" or "Level 1" can
    # never read as a pointer. Guardians modules are named "Cyber Guardians M11.7",
    # which this pattern does not match — a cross-course mention is not a pointer.
    "scouts": re.compile(r"\b(?:S|Modules?\s+S?)(\d+\.\d+(?:\.\d+)*)\b"),
}

TOPIC_ANCHORS = {
    "guardians": {
        "osint": ["M11.7"],
        "passive reconnaissance": ["M11.7"],
        "certificate transparency": ["M11.7"],
        "rdap": ["M11.7"],
        "nmap": ["M12", "M11.7"],          # M11.7 names it only as the active counterpart
        "wireshark": ["M13"],
        "burp": ["M20"],
        "att&ck": ["M18.5"],
        "zero trust": ["M16.5"],
        "chain of custody": ["M22"],
        "timestomp": ["M22.5"],
        "fsevents": ["M22.5"],
        "prefetch": ["M22.5"],
        "amcache": ["M22.5"],
        "mactime": ["M23.7"],
        "plaso": ["M23.7"],
        "super timeline": ["M23.7"],
        "volatility": ["M22.7", "M22"],
        "malfind": ["M22.7", "M22"],
        "memory forensics": ["M22.7", "M22"],
        "appinit_dlls": ["M22.7"],
    },
    "appsec": {
        # 0.5 introduces it hands-on from first principles; 3.2 is the deep dive.
        # Shared ownership is normal — an anchor that names only one is a false gate.
        "sql injection": ["3.2", "0.5"],
        "csrf": ["2.3"],
        "oauth": ["6.4"],
        "secrets management": ["8.1"],
    },
    "scouts": {
        # OSINT is the whole course; S1.1 is where the term is defined. Guardians
        # keeps its own "osint" -> M11.7 anchor: shared topic, one owner per course.
        "osint": ["S1.1"],
        "computer misuse act": ["S1.1"],
        "van buren": ["S1.1"],
        "hiq": ["S1.1"],
        "berkeley protocol": ["S1.1"],
        "collection record": ["S1.1"],
        "rdap": ["S1.2"],
        "bootstrap file": ["S1.2"],
        "registration data policy": ["S1.2"],
        "certificate transparency": ["S1.3"],
        "precertificate": ["S1.3"],
        "crt.sh": ["S1.3"],
    },
}

# Sentence-ish. Split only on terminal punctuation FOLLOWED BY SPACE, so that the "."
# inside a module number ("Module 0.5", "M11.7") never ends a sentence.
SENTENCE = re.compile(r"(?<=[.!?:])\s+|\n")

# Rows of an inventory — a table row, or a roadmap bullet naming a module — list many
# topics beside one module number without claiming any of them belongs to it.
# "- M13: Wireshark" is a title, not a cross-reference, and a tool list separated by
# middots is not a claim about anything. Anchors do not apply inside these.
INVENTORY = re.compile(r"^\s*(?:\||[-*]\s*M(?:odule)?s?\.?\s*\d)")

# How close a topic term must sit before the pointer to count as a claim ABOUT it. Two
# unrelated facts can share a long sentence; a claim and its pointer do not drift apart.
ANCHOR_WINDOW = 70

# The claim shape this check is a ratchet on: a topic, then a pointer offered as where
# that topic lives — "OSINT and recon (Module 12)", "certificate transparency — that is
# M11.7". A pointer in any other position ("you build the VM in Module 15; use
# scanme.nmap.org") is about sequencing, not coverage, and is deliberately not judged.
CLAIM_CUE = re.compile(r"(?:\(|\bthat is |\bsee |\bcovered in |\bcomes from |\bis in |\btaught in )$", re.I)


def module_numbers(cur):
    """Every module number a cross-reference may legitimately name, without its M.

    Guardians numbers as M12 / M11.5, AppSec as 7.2 — normalising to the bare number
    keeps one check honest about both, and picks up m0, whose `num` is "Intro".
    """
    nums = set()
    for m in cur.get("modules", []):
        n = (m.get("num") or "").lstrip("MmSs")
        if re.fullmatch(r"\d+(\.\d+)*", n):
            nums.add(n)
        i = str(m.get("id", ""))
        if re.fullmatch(r"m\d+([_-]\d+)?", i):
            nums.add(re.sub(r"[_-]", ".", i[1:]))
    return nums


def check_crossrefs(name, cur):
    valid = module_numbers(cur)
    anchors = {t: [o.lstrip("MmSs") for o in owners] for t, owners in TOPIC_ANCHORS.get(name, {}).items()}
    bag = {}
    for m in cur.get("modules", []):
        num = (m.get("num") or "").lstrip("MmSs")
        lab = m.get("lab") or {}
        bag[num] = (" ".join(
            str(m.get(k) or "") for k in ("title", "objective", "theory", "workbench")
        ) + " " + " ".join(
            str(v) for v in (lab.values() if isinstance(lab, dict) else []) if isinstance(v, str)
        )).lower()

    def resolves(n):
        # 7.5.4 is a module; 7.5 is the group it belongs to; 3.3.1 is a numbered section
        # inside module 3.3. All three are real destinations a reader can reach.
        return (n in valid
                or any(x.startswith(n + ".") for x in valid)
                or any(n.startswith(x + ".") for x in valid))

    ref = MODULE_REF[name]
    dangling, mispointed = [], []
    for label, md in module_texts(name, cur):
        for sent in SENTENCE.split(md):
            hits = list(ref.finditer(sent))
            if not hits:
                continue
            for m in hits:
                if not resolves(m.group(1)):
                    dangling.append(f"{label}: {m.group(0)} — {sent.strip()[:70]}")
            if INVENTORY.match(sent):
                continue
            low = sent.lower()
            for m in hits:
                if not CLAIM_CUE.search(sent[: m.start()]):
                    continue
                # A pointer claims the LAST topic before it. "SQL injection (Module 3.2)
                # → A05; IDOR/BOLA (Module 3.3)" must not read 3.3 as a claim about SQLi:
                # 3.2 already answered for it. So the window stops at the previous pointer.
                prev = max([h.end() for h in hits if h.end() <= m.start()] or [0])
                before = low[max(prev, m.start() - ANCHOR_WINDOW) : m.start()]
                for term, owners in anchors.items():
                    # A term inside a dotted or slashed token (scanme.nmap.org) is a
                    # hostname, not the subject of a claim.
                    if not re.search(r"(?<![\w.\-/])" + re.escape(term) + r"(?![\w.\-/])", before):
                        continue
                    if m.group(1) not in owners:
                        mispointed.append(
                            f"{label}: '{term}' -> {m.group(0)} (owned by {owners}) "
                            f"— {sent.strip()[:70]}"
                        )

    # Part C: an anchor is only worth having if its owning module really covers the term.
    rotted = [
        f"{term} -> M{o}" for term, owners in anchors.items() for o in owners
        if o not in bag or term not in bag[o]
    ]

    problems = []
    if dangling:
        problems.append(f"{len(dangling)} pointer(s) to a module that does not exist: {dangling[:3]}")
    if mispointed:
        problems.append(f"{len(mispointed)} topic claim(s) pointing at a module that does not teach it: {mispointed[:3]}")
    if rotted:
        problems.append(f"{len(rotted)} stale anchor(s) — the owning module no longer contains the term: {rotted[:3]}")
    if problems:
        fail(f"{name}: cross-references", "; ".join(problems))
    else:
        ok(f"{name}: cross-references", f"all (Module N) pointers resolve; {len(anchors)} topic anchors hold")


# ── 6. external URLs still resolve ────────────────────────────────────────────
SKIP_URL = re.compile(
    r"localhost|127\.0\.0\.1|example\.(com|org|net)|0\.0\.0\.0|169\.254|192\.168|10\.0\.|172\.16"
    r"|evil\.|acme|\.internal|yoursite|attacker|LAB|victim|app\.com|site/|internal|\$|<|>",
    re.I,
)
# SSRF-bypass payloads (decimal/hex/octal encodings of 127.0.0.1) and IPv6 loopback are
# teaching artifacts, not links. Probing them produces noise and, worse, outbound requests.
SSRF_PAYLOAD = re.compile(r"^https?://(0x[0-9a-f]+|\d{6,}|\[[0-9a-f:]*\]|0\d+)/?$", re.I)


# RFC 2606 / RFC 6761 reserved names plus the course's fictional phishing/C2 domains.
# These are supposed not to resolve — that is the point of using them in examples.
FICTIONAL = re.compile(r"\.(example|invalid|test|local)(\b|/)|apple-verification|evil-c2", re.I)

# badssl.com subdomains exist to present *deliberately invalid* TLS (expired certs,
# hostname mismatch). urllib rejects them at the handshake, which is the whole point of
# the lab that sends learners there — so the failure says nothing about whether the host
# is up. Probing them only produced a permanent "check by hand" warning nobody could clear.
BROKEN_TLS_DEMO = re.compile(r"\.badssl\.com", re.I)


def is_probeable(u: str) -> bool:
    if (
        SKIP_URL.search(u)
        or SSRF_PAYLOAD.match(u)
        or FICTIONAL.search(u)
        or BROKEN_TLS_DEMO.search(u)
    ):
        return False
    host = u.split("//", 1)[-1].split("/", 1)[0]
    return "." in host and len(host) > 3  # needs a real dotted hostname


GITHUB_PAGES_IPS = ("185.199.108.153", "185.199.109.153", "185.199.110.153", "185.199.111.153")


def _is_github_pages(url):
    """True if the host resolves to GitHub Pages (by address or CNAME)."""
    host = url.split("//", 1)[-1].split("/", 1)[0]
    try:
        infos = socket.getaddrinfo(host, None)
    except OSError:
        return False
    return any(i[4][0] in GITHUB_PAGES_IPS for i in infos)


def check_urls(sources):
    """Caught: two 404s that silently broke labs (A1, A9). Anything a learner is
    told to download or visit must still exist."""
    urls = set()
    for src in sources:
        for m in re.finditer(r"https?://[A-Za-z0-9._~:/?#\[\]@!$&*+,;=%-]+", src):
            u = m.group(0).rstrip(".,;:)]\\`'\"")
            # A URL immediately followed by a placeholder ("/host/<your-ip>", ".../$MY_IP")
            # is a template prefix, not a page. Probing the bare prefix is meaningless.
            if src[m.end() : m.end() + 1] in ("<", "$"):
                continue
            if is_probeable(u) and u.count("/") >= 2:
                urls.add(u)

    def probe(u):
        # An RDAP base URL (https://rdap.verisign.com/com/v1/) is a prefix: bare, it
        # answers 400/404 by design. RFC 9082 §3.1.6 defines "help" under every base,
        # so probe that instead — still a real liveness check, not an exemption.
        target = u + "help" if re.match(r"https://rdap\.[^/]+/(?:.*/)?$", u) else u
        req = urllib.request.Request(target, headers={"User-Agent": "cyber-materials-guardrail"})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return u, r.status
        except urllib.error.HTTPError as e:
            return u, e.code
        except Exception as e:  # DNS, TLS, timeout
            return u, f"ERR {type(e).__name__}"

    # 401/403/429 mean "a bot was refused or throttled", which a real browser would
    # not hit. Treating those as failures makes the gate cry wolf and get ignored.
    SOFT = {401, 403, 429, 503}
    # Hosts that refuse automation on EVERY path (verified by hand: openai.com returns
    # 403/404 to scripted requests for paths that load fine in a browser). Their status
    # carries no signal, so it can never be a failure — flag for manual review instead.
    BOT_BLOCKED = ("openai.com", "tryhackme.com", "hackthebox.com", "shodan.io", "virustotal.com")
    dead, soft = [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        for u, status in pool.map(probe, sorted(urls)):
            blocked = any(h in u for h in BOT_BLOCKED)
            if isinstance(status, int) and status >= 400:
                (soft if (status in SOFT or blocked) else dead).append(f"{status} {u}")
            elif isinstance(status, str):
                soft.append(f"{status} {u}")
    if dead:
        fail("urls: reachability", f"{len(dead)} DEAD of {len(urls)}: {dead[:4]}")
    elif soft:
        # Diagnosed 2026-09-11: a connection-level error on a GitHub Pages host is
        # almost always the *network path*, not a dead site — attack.mitre.org and
        # dfir.science both CNAME to Pages and both fail here, while non-Pages hosts
        # answer normally and pages.github.com itself is unreachable. Saying so stops
        # the next pass from re-running the same investigation.
        pages = [s for s in soft if s.startswith("ERR") and _is_github_pages(s.split(" ", 1)[-1])]
        hint = (f"; {len(pages)} of them are GitHub Pages hosts, which this network cannot "
                f"reach at all (verify from elsewhere, or use raw.githubusercontent.com)"
                if pages else "")
        warn("urls: reachability",
             f"{len(urls) - len(soft)}/{len(urls)} verified; {len(soft)} bot-blocked, "
             f"throttled or unroutable (check by hand){hint}: {soft[:3]}")
    else:
        ok("urls: reachability", f"all {len(urls)} external URLs resolve")


# ── main ──────────────────────────────────────────────────────────────────────
# ── 6. self-test ──────────────────────────────────────────────────────────────
# The coverage number is only trustworthy if `classify` is. These cases pin every
# bucket and every ordering decision, so a future tweak that quietly re-files a
# whole category (which an earlier draft of this file did) fails loudly instead.
SELF_TESTS = [
    ("fence: output fence right after",
     "```bash\nnode -v\n```\n```\nv22.12.0\n```", "fence"),
    ("fence: not counted when far away",
     "```bash\nnode -v\n```\n" + "x" * 700 + "\n```\nv22.12.0\n```", "silent"),
    ("labelled: bolded Expected observation",
     "```bash\ncurl -i localhost:3000\n```\n\n**Expected observation:** Alice is gone.", "labelled"),
    ("labelled: bare 'you see' prose is NOT coverage",
     "```bash\ncurl -i localhost:3000\n```\n\nSoon you see the result somewhere.", "silent"),
    ("comment: inline result arrow",
     "```bash\nwhoami   # -> root\n```", "comment"),
    ("comment: ordinary explanatory comment is not a result",
     "```bash\ncurl localhost   # talk to the server\n```", "silent"),
    ("setup: mkdir/cd only",
     "```bash\nmkdir -p ~/lab && cd ~/lab\n```", "setup"),
    ("setup: installs only",
     "```bash\nbrew install jq\nnpm install express\n```", "setup"),
    ("setup: one real command makes it NOT setup",
     "```bash\nmkdir -p ~/lab\njq --version\n```", "silent"),
    ("listing: shebang file contents",
     "```bash\n#!/usr/bin/env bash\ngrep -c ERROR app.log\n```", "listing"),
    ("listing: loses to a shown result (ordering)",
     "```bash\n#!/usr/bin/env bash\necho hi\n```\n```\nhi\n```", "fence"),
    # NB: these pad the gap past the 600-char `fence` window on purpose. A walkthrough
    # that sits close enough is already credited as `fence`; `gated` exists for the real
    # shape, where journal questions push the answer well past that window.
    ("gated: output fence inside the next Walkthrough details",
     "```bash\nnode rag.js\n```\n" + "Journal questions. " * 40 + "\n<details>\n<summary>"
     "Walkthrough — open after you've run it</summary>\n\n```\nretrieved [acme/d1]\n```\n"
     "</details>", "gated"),
    ("gated: NOT when a runnable block sits in between",
     "```bash\nnode rag.js\n```\n" + "Journal questions. " * 40 + "\n```bash\nnode other.js\n"
     "```\n<details>\n<summary>Walkthrough</summary>\n\n```\nout\n```\n</details>", "silent"),
    ("gated: NOT when the details holds no output fence",
     "```bash\nnode rag.js\n```\n" + "Journal questions. " * 40 + "\n<details>\n<summary>"
     "Walkthrough</summary>\n\nJust prose about why this matters.\n</details>", "silent"),
    ("gated: NOT for a Nudge/hint details",
     "```bash\nnode rag.js\n```\n" + "Journal questions. " * 40 + "\n<details>\n<summary>"
     "Nudge — open if stuck</summary>\n\n```\nhint\n```\n</details>", "silent"),
    ("prose_fence: comments only, nothing runnable",
     "```bash\n# first 3 bytes: 0x16 0x3 0x1\n# password readable? false\n```", "prose_fence"),
    ("heredoc payload is not a command",
     "```bash\nmkdir -p ~/lab && cd ~/lab\ncat > s.js <<'EOF'\nconsole.log(1);\nrm -rf /\nEOF\n```", "setup"),
    ("silent: a real command showing nothing",
     "```bash\nawk '{print $1}' access.log\n```", "silent"),
]


def self_test():
    bad = []
    for label, md, want in SELF_TESTS:
        blocks = fenced(md)
        got = classify(md, blocks, 0) if blocks else "(no block)"
        if got != want:
            bad.append(f"{label}: expected {want}, got {got}")
    print("\n\033[1mGUARDRAIL SELF-TEST — classify()\033[0m\n")
    for line in bad:
        print(f"  \033[31mFAIL\033[0m  {line}")
    if bad:
        print(f"\n  {len(SELF_TESTS) - len(bad)}/{len(SELF_TESTS)} passed\n")
        return 1
    print(f"  \033[32mPASS\033[0m  all {len(SELF_TESTS)} classifier cases\n")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-net", action="store_true", help="skip URL reachability")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--self-test", action="store_true", help="test classify() and exit")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    sources = []
    for name, path in COURSES.items():
        if not os.path.exists(path):
            fail(f"{name}: file", f"missing {path}")
            continue
        src = read(path)
        sources.append(src)
        check_parses(name, src)
        check_offline(name, src)
        check_banned(name, src)
        check_rg_equivalence(name, src)
        check_attack_ids(name, src)
        check_claims_ledger(name, src)
        cur = load_curriculum(name, src)
        if cur:
            check_counts(name, src, cur)
            check_crossrefs(name, cur)
            check_fences_and_escapes(name, cur)
            check_renders(name, src, cur)
            check_coverage(name, cur)

    check_attack_table_rot(sources)

    if not args.no_net:
        check_urls(sources)
    else:
        warn("urls: reachability", "skipped (--no-net)")

    if args.json:
        print(json.dumps({k: [{"check": c, "detail": d} for c, d in v] for k, v in RESULT.items()}, indent=2))
    else:
        print("\n\033[1mGUARDRAIL — Cyber Materials production-readiness\033[0m\n")
        for c, d in RESULT["pass"]:
            print(f"  \033[32mPASS\033[0m  {c}" + (f"  — {d}" if d else ""))
        for c, d in RESULT["warn"]:
            print(f"  \033[33mWARN\033[0m  {c}  — {d}")
        for c, d in RESULT["fail"]:
            print(f"  \033[31mFAIL\033[0m  {c}  — {d}")
        n_p, n_w, n_f = len(RESULT["pass"]), len(RESULT["warn"]), len(RESULT["fail"])
        print(f"\n  {n_p} passed · {n_w} warnings · {n_f} failures")
        if n_f:
            print("\n  \033[31mNOT production grade\033[0m — fix the failures above.\n")
        elif n_w:
            print("\n  \033[33mGate PASSED with warnings\033[0m — no defects; "
                  "read each warning above and decide whether it is worth clearing.\n")
        else:
            print("\n  \033[32mPRODUCTION GRADE\033[0m — all checks clean.\n")

    return 1 if RESULT["fail"] else 0


if __name__ == "__main__":
    sys.exit(main())
