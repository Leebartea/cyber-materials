# tools/

## `guardrail.py` — production-readiness gate

Run before every commit that touches course content, and in CI:

```bash
python3 tools/guardrail.py            # full check (includes URL reachability)
python3 tools/guardrail.py --no-net   # skip network checks
python3 tools/guardrail.py --json     # machine-readable
python3 tools/guardrail.py --self-test  # test the coverage classifier itself
```

**Exit code 0 = gate passed, 1 = failed.** Warnings do not fail the gate; failures do.

### What it checks, and why each check exists

Every check was added because a real defect shipped past review. The comment above
each function in the script names the defect it guards.

| Check | Guards against |
|---|---|
| `js-parse` | A stray `</script>` or unbalanced backtick inside a template literal silently truncates the whole app |
| `offline` | A CDN `<script src>` would break every offline learner — the courses must work with no network |
| `known-bad content` | 10 regression guards on specific defects already fixed (wrong hash, 404'd lab URLs, the SameSite `<img>` error, the Oldsmar attribution, stale IPs/issuers, module-count drift, httpbin) |
| `module-count` | "60 modules" claimed while the real count had drifted to 64 |
| `fence-balance` / `escape-damage` / `details-balance` | Over-escaping (`\`` rendering as a stray backslash) and unbalanced fences swallow content silently |
| `render` | Runs the **real** `renderProse` over every module. Caught 154 literal `---` paragraphs (no `hr` handler) and a `## ` heading rendering as plain text (no `h2` handler) |
| `rg-vs-grep` | The course called `rg` and `grep -r` identical. They are not — `rg` skips hidden files and `.gitignore`'d paths, silently missing `.env` |
| `expected-output coverage` | The headline finding: most runnable command blocks showed the learner no expected result, so they had nothing to compare their terminal against |
| `urls: reachability` | Two 404s had silently broken labs (the M6.1 wordlist, the M7.1 osv-scanner installer) |

### How expected-output coverage is measured

Every runnable block lands in **exactly one** bucket. The buckets are narrow and
mechanical on purpose: the number has to mean the same thing to everyone who runs
this, and nothing may be exempted by judgement call.

| Bucket | Meaning | Counts as |
|---|---|---|
| `fence` | an output fence immediately follows — **the documented convention** | shown |
| `labelled` | a bolded `**Expected observation:**` paragraph immediately follows | shown |
| `comment` | a result comment inside the block (`# -> root`) — weakest accepted form | shown |
| `setup` | every effective line is silent on success (`mkdir`, installs, `> file`) | **exempt** |
| `listing` | the block is a file's contents (shebang); its result belongs to the block that runs it | **exempt** |
| `prose_fence` | tagged runnable but contains no command at all | **exempt**, and warned |
| `silent` | a command that produces output, with no result shown anywhere | **the gap** |

`coverage = (fence + labelled + comment) / (total − exempt)`. Exempt blocks leave the
denominator rather than counting as free passes, and the exempt total is printed on
every run so an exemption can never quietly grow.

Two sub-checks keep the headline number honest:

- **`output-fence share`** warns when a bucket's coverage rests mostly on inline
  comments rather than real output fences. This is what revealed that the Guardians
  `lab` panels had **zero** output fences — their whole score was `# comment` lines.
- **`prose in runnable fence`** warns when a ` ```bash ` fence holds no command. That
  is either prose mis-tagged as code, or expected output written as `#` comments where
  an output fence belongs.

Ordering matters and is asserted by the self-test: the three "shown" tests run before
any exemption, so a block that *does* show its result is never stolen by an exemption.

> Two heuristics were removed as **false passes**: a bare `you see` / `Result:` anywhere
> in the following 450 characters used to count as coverage, which passed `apt install`
> and `mkdir` blocks that show the learner nothing. Only the deliberate bolded label
> counts now.

### The coverage ratchet

`COVERAGE_FLOOR` in the script is a **regression floor**, not a target. Coverage may
never drop below it. As the expected-output backfill lands, raise the floor to the new
measured value so progress can't be undone. `COVERAGE_TARGET` (95%) is what
"production grade" ultimately means for this gate.

Current state is deliberately `WARN`, not `PASS`: there are no known defects, but
coverage is still short of target.

### The self-test

`--self-test` runs table-driven cases against `classify()` and exits non-zero on any
mismatch. The coverage number is only trustworthy if the classifier is, so **run it
after touching any classification logic**. It has already caught two real bugs in the
classifier itself: an ordering mistake that filed a result-showing script as an exempt
listing, and a `cat > file <<'EOF'` heredoc being graded as a gap when it is silent by
nature.

### Deliberate non-failures

- **401/403/429/503** on a URL means a bot was refused or throttled, not that the link
  is dead. Hosts that refuse automation on every path (`openai.com`, `tryhackme.com`,
  `shodan.io`, …) are listed in `BOT_BLOCKED` and can only ever warn — verify by hand.
- **SSRF-bypass payloads** (`http://0x7f000001/`, `http://2130706433/`) and **reserved
  names** (`*.example`, `*.invalid`) are teaching artifacts. They are supposed not to
  resolve, and probing them would generate pointless outbound requests.

### Verifying the gate still bites

The gate is only worth having if it fails when it should. Confirm both failure
classes — a content regression and a coverage regression:

```bash
# 1. content regression: put the wrong hash back (use the FULL 64-char hash —
#    swapping only its first characters will not match the guard, and you will
#    wrongly conclude the gate is broken)
cp cyber-guardians/cyber_guardians_app.html /tmp/cg.bak
python3 - <<'PY'
p="cyber-guardians/cyber_guardians_app.html"; s=open(p).read()
s=s.replace("d0eac8f61f9c7085dbb626bf1aef1d3c42afedbbd636b1487745ca7a4ce7d71e",
            "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",1)
open(p,"w").write(s)
PY
python3 tools/guardrail.py --no-net; echo "exit=$?"    # expect: FAIL A2 … exit=1
cp /tmp/cg.bak cyber-guardians/cyber_guardians_app.html

# 2. coverage regression: raise a floor above the measured value
#    expect: FAIL … REGRESSED … exit=1
```

### Authoring rule for expected output

When adding an expected-output block: **run the command and paste the real output**, or
derive it where the code fully determines it, or — for anything environment-dependent
(`dig`, cert dates, `wc -l` counts, docker image IDs, timestamps) — show the *shape*
with an explicit "yours will differ, here's what to look for" note.

**Never invent plausible-looking output.** A wrong expected output is worse than none:
it teaches the learner to distrust their own correct result. Three of the defects this
gate now guards were exactly that.
