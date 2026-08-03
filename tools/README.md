# tools/

## `guardrail.py` — production-readiness gate

Run before every commit that touches course content, and in CI:

```bash
python3 tools/guardrail.py            # full check (includes URL reachability)
python3 tools/guardrail.py --no-net   # skip network checks
python3 tools/guardrail.py --json     # machine-readable
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

### The coverage ratchet

`COVERAGE_FLOOR` in the script is a **regression floor**, not a target. Coverage may
never drop below it. As the expected-output backfill lands, raise the floor to the new
measured value so progress can't be undone. `COVERAGE_TARGET` (95%) is what
"production grade" ultimately means for this gate.

Current state is deliberately `WARN`, not `PASS`: there are no known defects, but
coverage is still short of target.

### Deliberate non-failures

- **401/403/429/503** on a URL means a bot was refused or throttled, not that the link
  is dead. Hosts that refuse automation on every path (`openai.com`, `tryhackme.com`,
  `shodan.io`, …) are listed in `BOT_BLOCKED` and can only ever warn — verify by hand.
- **SSRF-bypass payloads** (`http://0x7f000001/`, `http://2130706433/`) and **reserved
  names** (`*.example`, `*.invalid`) are teaching artifacts. They are supposed not to
  resolve, and probing them would generate pointless outbound requests.

### Verifying the gate still bites

The gate is only worth having if it fails when it should. To confirm, reintroduce a
known defect and check for a non-zero exit:

```bash
cp cyber-guardians/cyber_guardians_app.html /tmp/cg.bak
# swap the correct hash for the old wrong one, then:
python3 tools/guardrail.py --no-net; echo "exit=$?"    # expect: FAIL … exit=1
cp /tmp/cg.bak cyber-guardians/cyber_guardians_app.html
```

### Authoring rule for expected output

When adding an expected-output block: **run the command and paste the real output**, or
derive it where the code fully determines it, or — for anything environment-dependent
(`dig`, cert dates, `wc -l` counts, docker image IDs, timestamps) — show the *shape*
with an explicit "yours will differ, here's what to look for" note.

**Never invent plausible-looking output.** A wrong expected output is worse than none:
it teaches the learner to distrust their own correct result. Three of the defects this
gate now guards were exactly that.
