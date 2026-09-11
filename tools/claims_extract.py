#!/usr/bin/env python3
"""claims_extract.py — harvest candidate falsifiable claims from a course reader.

This is step 1 of the CLAIMS.md workflow. It does *not* decide truth; it finds
the sentences that assert something a source or a command could settle, so the
ledger author reviews a few hundred candidates instead of re-reading 13k lines.

Everything it looks for is rot-prone or checkable: standard identifiers, version
numbers, dates, ranks, ports, RFCs, quantities, and the English shapes that
signal an external claim ("as of", "the most widely used", "by default").

Usage:
    python3 tools/claims_extract.py guardians            # all modules
    python3 tools/claims_extract.py guardians m1 m1_5    # only these
    python3 tools/claims_extract.py guardians --list     # module inventory
    python3 tools/claims_extract.py appsec --json out.json
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

COURSES = {
    "guardians": ROOT / "cyber-guardians" / "cyber_guardians_app.html",
    "appsec": ROOT / "cyber-full stack" / "full_stack_appsec_app.html",
}

# Fields of a module object whose prose can carry a claim. Mirrors the search
# blob the readers themselves build, so nothing teachable is skipped.
TEXT_FIELDS = (
    "objective", "theory", "workbench", "caseStudy", "quiz", "challenges",
    "tracker", "lab", "expected", "why", "q", "a", "body", "answer", "steps",
)

# (tag, pattern). Tags group the review: identifier rot, version rot, and the
# softer rhetorical claims that need a source but name no id.
PATTERNS = [
    ("cve", r"\bCVE-\d{4}-\d{4,7}\b"),
    ("cwe", r"\bCWE-\d{1,4}\b"),
    ("attack", r"\bT\d{4}(?:\.\d{3})?\b"),
    ("owasp", r"\b(?:A|API|LLM|M)\d{2}:\d{4}\b"),
    ("rfc", r"\bRFC\s?\d{3,5}\b"),
    ("nist", r"\bSP\s?800-\d+[A-Za-z0-9-]*\b|\bNIST CSF\s?\d\.\d\b|\bFIPS\s?\d{3}-?\d?\b"),
    ("iso", r"\bISO(?:/IEC)?\s?\d{4,5}(?::\d{4})?\b"),
    ("pci", r"\bPCI[- ]DSS\s?v?\d(?:\.\d)*\b"),
    ("version", r"\b(?:v|version )\d+(?:\.\d+){1,2}\b"),
    ("date", r"\b(?:as of|since|in|released|published|updated|retired|deprecated)\s+(?:\w+\s+)?(?:19|20)\d{2}\b"),
    ("rank", r"\b(?:ranks?|ranked|#\d|number one|top \d+|most common|most widely|the largest|the first|the only|the fastest|industry standard)\b"),
    ("quantity", r"\b\d{1,3}(?:,\d{3})+\b|\b\d+(?:\.\d+)?\s?(?:%|percent|million|billion|bits?|bytes|rounds|iterations)\b"),
    ("port", r"\bport \d{1,5}\b|\b\d{2,5}/(?:tcp|udp)\b"),
    ("default", r"\bby default\b|\bdefaults? to\b|\bout of the box\b"),
    ("law", r"\bGDPR\b|\bHIPAA\b|\bCCPA\b|\bSOX\b|\bDMCA\b|\bComputer Fraud and Abuse Act\b|\bCFAA\b|\b\d{1,3} (?:hours|days) to (?:notify|report)\b"),
    ("attribution", r"\baccording to\b|\bresearchers? (?:at|found)\b|\breport(?:ed|s) that\b|\bstudy (?:found|showed)\b"),
]
COMPILED = [(tag, re.compile(p, re.I)) for tag, p in PATTERNS]

# Sentence split: terminal punctuation followed by whitespace only, so that
# "Module 0.5", "v5.1.1" and "192.168.1.1" survive intact.
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")

# Markdown / template noise stripped before a sentence is shown for review.
NOISE = re.compile(r"^[\s>*\-|#`]+|[`*]+$")


def module_blocks(path):
    """Yield (id, num, title, [(lineno, text)]) for each module object."""
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "modules: [")
    except StopIteration:
        sys.exit(f"no `modules: [` array found in {path.name}")
    end = next((i for i, l in enumerate(lines) if "const SKILL_LEVELS" in l), len(lines))

    cur = None
    for i in range(start, end):
        line = lines[i]
        m = re.match(r'\s*id: "([^"]+)"', line)
        if m:
            if cur:
                yield cur
            cur = {"id": m.group(1), "num": "", "title": "", "lines": []}
            continue
        if cur is None:
            continue
        for key in ("num", "title"):
            k = re.match(r'\s*%s: "([^"]*)"' % key, line)
            if k and not cur[key]:
                cur[key] = k.group(1)
        cur["lines"].append((i + 1, line))
    if cur:
        yield cur


def candidates(block):
    """Return [(lineno, [tags], sentence)] for claim-bearing sentences."""
    out, seen = [], set()
    for lineno, raw in block["lines"]:
        # Skip pure code/config lines: they are EXECUTED evidence, not claims.
        stripped = raw.strip()
        if not stripped or stripped in ("`,", "},", "],", "{", "}"):
            continue
        for sent in SENT_SPLIT.split(stripped):
            tags = sorted({tag for tag, rx in COMPILED if rx.search(sent)})
            if not tags:
                continue
            text = NOISE.sub("", sent).strip()
            if len(text) < 12:
                continue
            key = text.lower()
            if key in seen:
                continue
            seen.add(key)
            out.append((lineno, tags, text))
    return out


def main():
    args = [a for a in sys.argv[1:]]
    if not args or args[0] not in COURSES:
        sys.exit(f"usage: claims_extract.py <{'|'.join(COURSES)}> [module_id ...] [--list] [--json PATH]")
    course = args.pop(0)
    want_list = "--list" in args
    json_path = None
    if "--json" in args:
        j = args.index("--json")
        json_path = args[j + 1]
        del args[j:j + 2]
    only = {a for a in args if not a.startswith("--")}

    blocks = list(module_blocks(COURSES[course]))
    if want_list:
        for b in blocks:
            print(f'{b["id"]:<12} {b["num"]:<6} {b["title"]}')
        print(f"\n{len(blocks)} module objects")
        return

    payload, total = [], 0
    for b in blocks:
        if only and b["id"] not in only:
            continue
        cands = candidates(b)
        total += len(cands)
        payload.append({"id": b["id"], "num": b["num"], "title": b["title"],
                        "candidates": [{"line": l, "tags": t, "text": s} for l, t, s in cands]})
        if not json_path:
            print(f'\n=== {b["id"]}  ({b["num"]}) {b["title"]} — {len(cands)} candidates')
            for l, t, s in cands:
                print(f'  {l:>6}  [{",".join(t)}] {s}')

    if json_path:
        Path(json_path).write_text(json.dumps(payload, indent=1), encoding="utf-8")
    print(f"\n{total} candidate claims across {len(payload)} modules", file=sys.stderr)


if __name__ == "__main__":
    main()
