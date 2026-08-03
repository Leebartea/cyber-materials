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
import sys
import tempfile
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSES = {
    "appsec": os.path.join(REPO, "cyber-full stack", "full_stack_appsec_app.html"),
    "guardians": os.path.join(REPO, "cyber-guardians", "cyber_guardians_app.html"),
}

# ── thresholds ────────────────────────────────────────────────────────────────
# Ratchet: the expected-output coverage floor. Raise this as the backfill lands
# so coverage can never regress. Set to the current measured value.
COVERAGE_FLOOR = {"appsec": 40, "guardians_theory": 40, "guardians_lab": 45}
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
            if isinstance(lab, dict) and lab.get("mac"):
                yield label + "/lab", "```bash\n" + lab["mac"] + "\n```"


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
RUNNABLE = {"bash", "sh", "shell", "zsh", "powershell", "console"}
OUTPUT_LANGS = {"", "text", "output", "out", "plain"}
RESULT_COMMENT = re.compile(
    r"(?m)^[^\n]*(?:#|//)[^\n]*(?:->|→|=>|\bprints?\b|\bshows?\b|you (?:should )?(?:see|get)|\boutputs?\b)"
)
PROSE_AFTER = re.compile(
    r"Expected (?:observation|output|result)|You (?:should )?see|You'?ll see|prints?:|Result:", re.I
)


def fenced(md):
    out = []
    for m in re.finditer(r"```([^\n`]*)\n([\s\S]*?)```", md):
        out.append({"lang": m.group(1).strip().lower(), "code": m.group(2), "s": m.start(), "e": m.end()})
    return out


def coverage(md):
    """A runnable block 'shows a result' if an output fence follows it, or it carries
    a result comment, or prose right after states the expected output."""
    blocks = fenced(md)
    shown = total = 0
    silent = []
    for idx, b in enumerate(blocks):
        if b["lang"] not in RUNNABLE:
            continue
        total += 1
        nxt = blocks[idx + 1] if idx + 1 < len(blocks) else None
        has_fence = nxt and nxt["lang"] in OUTPUT_LANGS and (nxt["s"] - b["e"]) < 600
        if has_fence or RESULT_COMMENT.search(b["code"]) or PROSE_AFTER.search(md[b["e"] : b["e"] + 450]):
            shown += 1
        else:
            first = next((l.strip() for l in b["code"].split("\n") if l.strip() and not l.strip().startswith("#")), "")
            silent.append(first[:60])
    return shown, total, silent


def check_coverage(name, cur):
    """Caught: the headline finding — 65% of runnable command blocks showed the
    learner no expected result, so they had nothing to compare their terminal to."""
    buckets = {}
    for label, md in module_texts(name, cur):
        if not md.strip():
            continue
        key = "guardians_lab" if label.endswith("/lab") else ("guardians_theory" if name == "guardians" else "appsec")
        s, t, sil = coverage(md)
        b = buckets.setdefault(key, {"shown": 0, "total": 0, "worst": []})
        b["shown"] += s
        b["total"] += t
        if t - s:
            b["worst"].append((t - s, label, sil[:2]))
    for key, b in buckets.items():
        if not b["total"]:
            continue
        pct = round(b["shown"] / b["total"] * 100)
        floor = COVERAGE_FLOOR.get(key, 0)
        b["worst"].sort(reverse=True)
        worst = ", ".join(f"{l} ({n} silent)" for n, l, _ in b["worst"][:4])
        detail = f"{b['shown']}/{b['total']} = {pct}% (floor {floor}%, target {COVERAGE_TARGET}%)"
        if pct < floor:
            fail(f"{key}: expected-output coverage", f"REGRESSED — {detail}; worst: {worst}")
        elif pct < COVERAGE_TARGET:
            warn(f"{key}: expected-output coverage", f"{detail} — below production target; worst: {worst}")
        else:
            ok(f"{key}: expected-output coverage", detail)


# ── 4. known-bad content (regression guards for fixed defects) ────────────────
BANNED = [
    # (pattern, why it is banned, which finding it guards)
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
]


def check_banned(name, src):
    hits = []
    for pat, why, fid in BANNED:
        for m in re.finditer(pat, src, re.M):
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
def check_counts(name, src, cur):
    """Caught: 'ps60 modules' after the real count had drifted to 64."""
    mods = cur.get("modules", [])
    if name == "appsec":
        real = len([m for m in mods if (m.get("body") or "").strip() and m.get("id") != "m_intro"])
    else:
        real = len([m for m in mods if not str(m.get("id", "")).endswith("roadmap")])
    claimed = [int(x) for x in re.findall(r"\*\*(\d+) modules\b", src)] + \
              [int(x) for x in re.findall(r"All (\d+) modules\b", src)]
    wrong = [c for c in claimed if c != real]
    if wrong:
        fail(f"{name}: module-count", f"page claims {wrong}, actual is {real}")
    else:
        ok(f"{name}: module-count", f"{real} modules, claims consistent")


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


def is_probeable(u: str) -> bool:
    if SKIP_URL.search(u) or SSRF_PAYLOAD.match(u) or FICTIONAL.search(u):
        return False
    host = u.split("//", 1)[-1].split("/", 1)[0]
    return "." in host and len(host) > 3  # needs a real dotted hostname


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
        req = urllib.request.Request(u, headers={"User-Agent": "cyber-materials-guardrail"})
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
        warn("urls: reachability",
             f"{len(urls) - len(soft)}/{len(urls)} verified; {len(soft)} bot-blocked or "
             f"throttled (check by hand): {soft[:3]}")
    else:
        ok("urls: reachability", f"all {len(urls)} external URLs resolve")


# ── main ──────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-net", action="store_true", help="skip URL reachability")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

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
        cur = load_curriculum(name, src)
        if cur:
            check_counts(name, src, cur)
            check_fences_and_escapes(name, cur)
            check_renders(name, src, cur)
            check_coverage(name, cur)

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
            print("\n  \033[33mGate PASSED with warnings\033[0m — no defects, but "
                  "expected-output coverage is still below the production target.\n")
        else:
            print("\n  \033[32mPRODUCTION GRADE\033[0m — all checks clean.\n")

    return 1 if RESULT["fail"] else 0


if __name__ == "__main__":
    sys.exit(main())
