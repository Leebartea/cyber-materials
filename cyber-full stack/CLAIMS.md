# Full-Stack AppSec — claim ledger

Every rule-shaped assertion this course makes, with a status and the evidence
behind it. The guardrail gate (`tools/guardrail.py`) proves the course is
*structurally* sound — balanced fences, resolving cross-references, no dead
links. It cannot prove anything here is *true*. That is what this file is for.

This is the sibling of `cyber-guardians/CLAIMS.md`; the status key, the batch
ordering and the "a row that can never be closed is a finding, not a to-do"
rule are the same in both, deliberately.

- **Course file:** `cyber-full stack/full_stack_appsec_app.html` (64 modules)
- **Candidates extracted by:** `python3 tools/claims_extract.py appsec --json out.json`
- **Last pass:** 2026-09-17 (Batch 5 — law claims, closed: no `PENDING` rows remain)

## How to use it

A second audit should be cheap. Re-read only:

1. rows whose **Re-check** date has passed,
2. rows still marked `PENDING`,
3. modules edited since the pass date above.

Everything else was settled by a source named in the row. Do not re-derive it.

## Status key

| Status | Means |
|---|---|
| `SOURCED` | an external authority was read this pass; the URL is in the row |
| `EXECUTED` | the claim is a command's behaviour and was **run**, output pasted into the course |
| `CORPUS` | confirmed against material the course itself cites |
| `PENDING` | standard and believed correct, not externally checked this pass; the row names the source to check |
| `CONVENTION` | terminal — **no source can settle it even in principle**; the course must state it as a convention and hedge it |
| `FIXED` | was wrong or overclaimed, corrected this pass |

`PENDING` means *a lookup is owed*. A row that can never be closed is a finding,
not a to-do — mark it `CONVENTION` and write the failed search into the row so a
later pass does not repeat it.

## Coverage

Batch 1 adjudicates the **standards-and-identifier** class: every claim naming a
CVE, CWE, ATT&CK technique, OWASP category, RFC, NIST SP/FIPS, ISO standard, PCI
version, or software version. 526 candidate claims were extracted across all 76
module objects; 85 carry one of those identifier tags and collapse to the 33
distinct rules below.

This course teaches **no ATT&CK technique ids** — the gate's `attack-ids` check
confirms it — so the STIX-bundle validation that Batch 1 of the Guardians ledger
had to perform has no counterpart here.

Not yet adjudicated — the next batches, in priority order:

| Batch | Class | Candidates | Why it matters |
|---|---|---|---|
| 6 | `port` — port and protocol assignments | 23 | mostly IANA-settleable, low risk, high volume — but read the Guardians ledger's Batch 4 first: 41 of its 48 were not assignments at all |
| 7 | `date` — "as of", "since", release years | 15 | rots by definition — and per the Guardians Batch 5, the date is rarely what rotted |
| 8 | `attribution` — "according to", "researchers found" | 1 | needs the **primary** document, not the report quoting it |

(`law` — 29 candidates — is **closed** in Batch 5, rows 52–57.)

## Batch 1 — standards and identifiers

| # | Module | Claim as taught | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 1 | ★ | Course is aligned to OWASP Top 10:2025, ASVS 5.0, NIST SP 800-63B-4, 2025 CWE Top 25 | `SOURCED` | each component verified in rows 2, 5, 12, 14 | 2026-12 |
| 2 | ★, M4.1 | The 2025 edition is the current OWASP Top 10; A01 Broken Access Control, A02 Security Misconfiguration, A03 Software Supply Chain Failures, A05 Injection, A09 Security Logging & Alerting Failures, A10 Mishandling of Exceptional Conditions | `SOURCED` | owasp.org/Top10/2025/ — announced Nov 2025 at Global AppSec DC, final Jan 2026. A02 rose from A05:2021; A03 and A10 are the two new categories; A09 renamed Monitoring→Alerting; A01 absorbed SSRF and now names BOLA/BFLA explicitly | 2027-11 |
| 3 | M4.1 | A10:2025 Mishandling of Exceptional Conditions is "the genuinely new category" — fail-open error paths | `SOURCED` | A10 is new in 2025 and spans 24 CWEs covering improper error handling, logical errors and failing open. A03 is also new, so the course's "genuinely new" is a teaching emphasis, not an exclusivity claim; both are named as new at L10829 | 2027-11 |
| 4 | M10.1 | An IDOR walkthrough is filed as API1:2023 BOLA / A01 Broken Access Control | `FIXED` | API1:2023 is current (the 2023 edition is the live OWASP API Security Top 10; no later edition). The paired web category read **A01:2021** — a survivor of the 2021-numbering purge, correct in letter (A01 is Broken Access Control in both editions) but citing a superseded edition. Changed to **A01:2025**, which is also the edition that explicitly names BOLA | 2027-11 |
| 5 | ★, M4.1 | OWASP ASVS 5.0 (May 2025) is ~350 testable requirements at three levels | `SOURCED` | released 30 May 2025 at Global AppSec EU Barcelona; the v5.0.0 flat JSON in `OWASP/ASVS` holds **345** requirements, so "~350" stands | 2027-05 |
| 6 | M4.1 | ASVS 5.0 has **14** chapters | `FIXED` | 14 is the **4.0.3** chapter count. The v5.0.0 tag has **17** (V1 Encoding and Sanitization … V17 WebRTC), counted from the released flat JSON. Corrected to 17 in both the theory text and the knowledge-check answer, and the answer now warns that requirement numbers are not portable between editions | 2027-05 |
| 7 | M4.1 | "ASVS V6 Session Management — V6.2.1, session tokens are generated with a CSPRNG" | `FIXED` | this cites a chapter/requirement that exists in **neither** edition: in 5.0, V6 is Authentication and V7 is Session Management; in 4.0.3, V6 was Stored Cryptography and V3 was Session Management. The real requirement is **V7.2.3** — "Verify that if reference tokens are used to represent user sessions, they are unique and generated using a cryptographically secure pseudo-random number generator (CSPRNG)" — and it is **L1**, not L2, so the surrounding "read its L2 requirements" was also rewritten | 2027-05 |
| 8 | M4.1 | ASVS L1 is the outside-testable baseline, L2 the target for apps handling meaningful data, L3 high-assurance | `SOURCED` | the levels are cumulative; L1 is the minimum and is largely verifiable without source access, L2 is the level procurement questionnaires implicitly mean, L3 is for catastrophic-breach applications. 5.0 softened but did not drop the "L1 is checkable from outside" framing, so the course's phrasing holds | 2027-05 |
| 9 | M2.2 | CWE-79 is XSS and is #1 on the 2025 CWE Top 25 | `CORPUS` | cwe.mitre.org/top25/ — same source that closed row 13 of the Guardians ledger this pass | 2026-12 |
| 10 | M3.2 | CWE-89 is SQL Injection and is #2 on the 2025 CWE Top 25 | `CORPUS` | as row 9 | 2026-12 |
| 11 | M2.3 | CWE-352 is CSRF and is #3 on the 2025 CWE Top 25 | `CORPUS` | as row 9 | 2026-12 |
| 12 | ★, M4.1 | The 2025 CWE Top 25 is the current edition; CWE-78, CWE-22, CWE-434, CWE-862 and the memory-safety trio CWE-787/125/416 follow the top three | `SOURCED` | 2025 edition published Dec 2025 from 39,080 CVEs | 2026-12 |
| 13 | M3.4, M8.3, M10.1 | CWE-434 unrestricted upload; CWE-918 SSRF; CWE-639 authorization bypass through user-controlled key; CWE-862 missing authorization | `CORPUS` | CWE catalogue; each is used for the weakness it names | 2028-01 |
| 14 | M6.1 | NIST SP 800-63B-4 (July 2025) forbids composition rules and forced rotation, requires a breached-password check | `CORPUS` | final published 2025-07-31, superseding SP 800-63B; the prohibition on composition rules and scheduled rotation and the blocklist requirement are §3.1.1.2 of that document. Closed as row 5 of the Guardians ledger from the same source | 2027-07 |
| 15 | M7.1 | NIST SSDF is SP 800-218; its four practice groups are PO / PS / PW / RV | `SOURCED` | csrc.nist.gov/pubs/sp/800/218/final — SSDF v1.1, Feb 2022: Prepare the Organization, Protect the Software, Produce Well-Secured Software, Respond to Vulnerabilities. A companion **SP 800-218A** (generative-AI profile) exists and does not supersede it | 2027-02 |
| 16 | M1.2 | Aug 2024: NIST finalized FIPS 203 (ML-KEM), 204 (ML-DSA), 205 (SLH-DSA) | `CORPUS` | finalized 2024-08-13; identical claim closed as row 18 of the Guardians ledger. This course does **not** repeat that ledger's HQC defect — it makes no HQC claim | 2027-08 |
| 17 | M7.3 | PCI DSS 4.0.1 is current, and all requirements — including MFA for every CDE access and a 12-character password minimum — have been mandatory since 31 Mar 2025 | `SOURCED` | v4.0.1 replaced v4.0 on 2024-12-31 and added/removed no requirements; 51 of the 64 new v4.x requirements were future-dated to 2025-03-31, among them 8.4.2 (MFA for all CDE access, not just admin) and 8.3.6 (12-character minimum). **Watch:** a next version entered RFC in mid-2026, so this row will move | 2027-03 |
| 18 | M7.3 | ISO/IEC 27001:2022 is the current ISMS standard and the international counterpart to a US SOC 2 report | `CORPUS` | 2022 edition replaced 2013; closed as row 7 of the Guardians ledger | 2027-06 |
| 19 | M7.5.8 | ISO/IEC 42001 is the international AI management system standard | `SOURCED` | ISO/IEC 42001:2023, *Information technology — Artificial intelligence — Management system*, published 2023-12-18; still the current and only edition | 2027-12 |
| 20 | M7.3 | EU CRA: in force 10 Dec 2024; reporting obligations from 11 Sep 2026; full requirements 11 Dec 2027; 24-hour notice to ENISA/CSIRT for an actively exploited vulnerability | `SOURCED` | Article 14 became applicable **2026-09-11** — the day of this pass — via the CRA Single Reporting Platform, which routes one filing to the lead CSIRT and ENISA simultaneously; full application 2027-12-11 stands. The 24-hour clock is the *early warning*; a full notification is due at 72 hours and a final report at 14 days, which the course does not yet mention (incomplete, not wrong) | 2027-12 |
| 21 | M7.3 | DORA applies since 17 Jan 2025 to the EU financial sector and its ICT providers; five pillars | `SOURCED` | application date 2025-01-17; pillars are ICT risk management, incident reporting, resilience testing, third-party risk, information sharing | 2028-01 |
| 22 | M7.3 | NIS2 has applied since national transposition, deadline Oct 2024 | `SOURCED` | transposition deadline 2024-10-17. The course already hedges with "since national transposition", which is the correct hedge — member-state transposition is uneven | 2028-01 |
| 23 | M7.5.1 | The OWASP LLM Top 10 runs LLM01:2026 … LLM10:2026, and System Prompt Leakage (LLM07:2025) became Hidden Context Exposure (LLM08:2026) | `CORPUS` | adopted course-wide at commit `c2b354d`; the gate's known-bad table guards the superseded 2025 ordering | 2027-11 |
| 24 | M7.5.8 | "The OWASP Agentic Top 10" names excessive agency, tool/description poisoning, memory poisoning, cross-agent impersonation and cascading failures | `FIXED` | **no list by that name exists.** OWASP's GenAI Security Project published **OWASP Top 10 for Agentic Applications** on 2025-12-09, numbered **ASI01–ASI10** (Agentic Security Initiative): ASI01 Agent Goal Hijack, ASI02 Tool Misuse, ASI03 Identity & Privilege Abuse, ASI04 Agentic Supply Chain Vulnerabilities, ASI05 Unexpected Code Execution, ASI06 Memory & Context Poisoning, ASI07 Insecure Inter-Agent Communication, ASI08 Cascading Failures, ASI09 Human-Agent Trust Exploitation, ASI10 Rogue Agents. The taught bullets were all real risks but were attributed to the wrong publication, and **"excessive agency" is not an ASI entry at all** — it is LLM03:2026 from the LLM list, distributed in the agentic list across ASI03 and ASI10. Retitled, each bullet mapped to its ASI id, the four unmentioned entries added, and the tracker rewritten to ask for ASI ids. The same project also publishes a broader T01–T17 threat taxonomy, which is why "the OWASP agentic list" is ambiguous and the ids are now mandatory in the text | 2027-12 |
| 25 | M1.5, M7.2 | SLSA v1.2 (Nov 2025) is current and promoted the Source track alongside the Build track | `SOURCED` | slsa.dev/blog/2025/11/announce-slsa-v1.2 — approved by the steering committee 2025-11-12 after RC1 (June 2025) and RC2; the Source track is the headline addition and defines SLSA_SOURCE_LEVEL_0–3; backwards compatible with v1.1 | 2027-11 |
| 26 | M1.5, M7.1 | The pinned GitHub Action SHAs really are the tags the comments claim | `EXECUTED` | `git ls-remote --tags` against each upstream, 2026-09-11: `actions/checkout@11bd7190…` = v4.2.2, `actions/checkout@b4ffde65…` = v4.1.1, `actions/setup-node@60edb5dd…` = v4.0.2, `actions/setup-python@0a5c6159…` = v5.0.0, `google/osv-scanner-action@9a498708…` = v2.3.8. All five exact. This matters more than most rows: these lines are copy-pasted into a learner's CI | 2027-09 |
| 27 | M7.1, M7.2 | lodash scanner fixture: CVE-2019-10744 CRITICAL fixed in 4.17.12; CVE-2018-16487 HIGH fixed ≥4.17.11; CVE-2021-23337 HIGH fixed in 4.17.21 | `SOURCED` | GHSA-jf85-cpcp-j695 rates CVE-2019-10744 Critical (CVSS 9.1) with lodash patched at 4.17.12 — exactly the fixture. CVE-2018-16487 (GHSA-4xc9-xhrj-v574) scores 5.3 on NVD but **High** on GitHub's own rating, which is the severity trivy shows for npm packages, so HIGH is right for this output; CVE-2021-23337 (GHSA-35jh-r3h4-6jhm) is CVSS 7.2 HIGH, fixed 4.17.21 | 2028-01 |
| 28 | M7.1 | Flask fixture: flask 2.0.0 is CVE-2023-30861, which pip-audit calls PYSEC-2023-62 and safety calls PyUp 55261 | `SOURCED` | CVE-2023-30861 / GHSA-m2qf-hxjv-5gpq, CVSS 7.5, fixed in 2.2.5 and 2.3.2 — so 2.0.0 is in range. PYSEC-2023-62 is the confirmed PyPI-advisory alias. The teaching point (three tools, three identifier namespaces for one bug) is the reason this fixture must stay exact | 2028-01 |
| 29 | M3.5 | Ruby fixture: rack 2.2.3 is CVE-2022-30123 / GHSA-wq4h-7r42-5hrr, Critical, fixed at `>= 2.2.3.1` | `SOURCED` | RubySec + GitHub Advisory: CVSS 10.0 Critical (CWE-150), safe constraints `~> 2.0.9, >= 2.0.9.1`, `~> 2.1.4, >= 2.1.4.1`, `>= 2.2.3.1` — the fixture's solution string is verbatim correct | 2028-01 |
| 30 | M3.5 | PHP fixture: guzzlehttp/guzzle CVE-2026-69246 / GHSA-v5mv-p594-2x33, high, affects `>=8.0.0,<8.0.1` and `<7.15.2` | `SOURCED` | real and recent — a noncanonical-host bypass of host-based checks (CWE-180/436/918/941), published 2026-07-26, reported 2026-08-03. Affected ranges match the fixture exactly | 2028-01 |
| 31 | M8.4 | Distroless trivy fixture: `libssl3` has 6 findings, CVE-2026-31789 **CRITICAL** and CVE-2026-28387 HIGH, fixed in `3.0.19-1~deb12u2` | `FIXED` | both CVEs and the Debian fixed version are exactly right — the Debian security tracker shows both closed for bookworm by `3.0.19-1~deb12u2` under DSA-6201-1. **The CRITICAL is not.** OpenSSL upstream rates CVE-2026-31789 (32-bit hex-conversion overflow, needs a >1 GB certificate) **Low**; Red Hat rates it low; SUSE's "important" is the ceiling anyone gives it. No source supports Critical. Changed to HIGH — and the total line from `6 (HIGH: 5, CRITICAL: 1)` to `6 (HIGH: 6)` — plus a sentence on why scanner severity is an opinion, since CVE-2026-28387 is Low upstream and 8.1 HIGH at NVD. That disagreement now reinforces the module's own three-scanners-three-totals lesson instead of quietly contradicting it | 2028-01 |
| 32 | M7.2 | Equifax's root cause was an unpatched Apache Struts2 RCE, CVE-2017-5638, whose patch had been available two months | `CORPUS` | NVD; the two-month patch gap is the FTC's own pleaded allegation. Closed as row 29 of the Guardians ledger from the same sources — this course repeats the claim in M7.2's supply-chain narrative but makes no victim-count claim alongside it | 2028-01 |
| 33 | M0.4 | Node older than v20.19 / v22.7 rejects `import` in a plain `.js` file | `SOURCED` | automatic module-syntax detection (`detect-module`, nodejs/node#53619) was unflagged in **v22.7.0** and backported to **v20.19.0** alongside the `require(esm)` unflagging (nodejs/node#56927). Both boundary versions in the course are the exact release that changed the behaviour | 2028-01 |

## Batch 2 — rank and superlative claims

284 `rank` candidates (the extractor's original estimate of 275 was low by 9),
triaged the same way as the Guardians pass: group by which trigger fired, clear
the narrative `the first` / `the only` / `top 10`-as-a-title pile, and the 41
survivors carrying a real superlative collapse to the 5 rules below.

| # | Module | Claim as taught | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 34 | ★, M3.5 | Node/Express is "the most common full-stack **language**" | `FIXED` | Two faults in one sentence. **Node is a runtime, not a language** — and the course's own Intro says "the most common full-stack *pairing*", so the two passages contradicted each other. The underlying rank is fine: Stack Overflow's 2025 survey (n=23,678 on this question, fielded 29 May–23 Jun 2025) puts **Node.js first among web technologies at 48.7%**, ahead of React at 44.7%; Express is a separate, smaller entry. Harmonised to the Intro's wording. | 2027-07 |
| 35 | M4.1 | Software Supply Chain Failures is "the fastest-growing attack class" | `FIXED` | **OWASP's own data points the other way.** A03:2025 maps only 5 CWEs and has the *fewest* occurrences in the collected data — its #3 placement came from the community survey, not from CVE volume. The sourceable superlative is that **#3 is the highest debut in the list's history**, and the text now says that instead, with the basis named. | 2027-11 |
| 36 | M0.4, M3.3, M6.5 | Broken access control / BOLA / IDOR are "the most common" API and application vulnerabilities | `SOURCED` | Defensible **as written, because every instance is hedged** — "one of the most common serious bugs", "the most common API vulnerabilities are…". Broken Access Control is A01:2025, and improper access control ranked 2nd in HackerOne's 2020 Top 10. Contrast Guardians row 38, where the same idea was asserted as an unhedged #1 and was wrong: the defect there was the certainty, not the topic. | 2027-11 |
| 37 | M4.1 | OWASP Top 10:2025 — A03 Software Supply Chain Failures promoted from the old components entry; new A10 Mishandling of Exceptional Conditions; SSRF no longer its own entry | `SOURCED` | All three confirmed this pass. The 2025 edition was announced November 2025 at OWASP Global AppSec in Washington DC and finalised January 2026, built from 175,000+ CVEs with 248 CWEs mapped; A10 carries 24 CWEs; SSRF was absorbed into Broken Access Control after earning its own 2021 slot on survey strength alone. | 2027-11 |
| 38 | M0.1, M0.7, M1.3, M1.7, M8.1, M10.3 | The "single most common &lt;mistake&gt;" teaching idiom — misreading silent success, the dropped `sort` before `uniq`, an unescaped `.` in a regex, the committed `.env`, the stale process on the port | `CONVENTION` | Same ruling as Guardians row 44: no telemetry ranks the mistakes learners make, so no lookup can settle these even in principle. Keep the idiom, never attach a number or a named source to it. | — |

## Batch 3 — default-behaviour claims

65 `default` candidates. The split mirrors the Guardians `quantity` pass: roughly
half are **advice in the imperative** — "deny by default", "default to host-only
cookies", "default to no `sudo`" — which are pedagogy, not assertions about the
world, and no lookup applies. The rest assert **what some third party's software
does when you do not configure it**, and those are among the most perishable
claims a security course can make: a default is a decision a maintainer can
reverse in a point release, and when they reverse it for *security* reasons the
course's lesson can invert overnight. That is exactly what row 40 is.

| # | Module | Claim as taught | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 39 | M2.4 | "flask-cors does exact-origin matching by default" — only a *regex* `origins` value needs anchoring | `FIXED` | **The most serious defect found in any batch so far: the course promised a safety property the library does not have, in the exact place a reader would rely on it.** flask-cors matches with `re.match(pattern, origin)`, and `re.match` anchors only at the **start** of the string — it never requires the pattern to consume the whole thing. So a plain allow-list string `"https://app.example.com"` **also matches** `https://app.example.com.evil.com` and `https://app.example.com:8080`, and the matched origin is reflected straight back in `Access-Control-Allow-Origin`. The warning was aimed only at the regex case while the default case had the identical hole. This is the same root cause as the 2024 flask-cors CVE cluster on path matching (CVE-2024-6839 regex-specificity ordering, CVE-2024-6866 case-insensitive paths, CVE-2024-6844 `unquote_plus`), all of which come from `try_match` being reused where exactness was assumed. Rewritten to say it plainly and to anchor every pattern, regex or not. | 2027-03 |
| 40 | M7.5.4, M3.9 | "`torch.load` uses pickle by default", so loading an untrusted `.pt` is arbitrary code execution | `FIXED` | **A security default that flipped under the course — in the safe direction, which is why nothing complained.** **PyTorch 2.6, 29 January 2025**, made `weights_only=True` the default (deprecation warnings ran from 2.4; PR #137602). With it, `torch.load` uses a restricted unpickler that can only rebuild tensors and basic types, so a malicious `.pt` raises `UnpicklingError` instead of executing. Three passages asserted the old default and one code sample demonstrated it. Rewritten as **mitigation, not repair**, and the nuance is now the better lesson: the expressive path is one keyword argument away, old checkpoints fail loudly under the new default so `weights_only=False` is among the most-pasted workarounds on the internet, `add_safe_globals` widens the allowlist back, pre-2.6 PyTorch is still widely deployed, and a `weights_only=True` RCE bypass was itself reported and fixed in 2.6. The lab is unaffected — it uses `pickle` directly, which is unchanged. | 2027-01 |
| 41 | M7.5.3 | "most Markdown renderers pass raw HTML through by default" | `FIXED` | **Defensible as a majority claim and useless as advice, because the renderers disagree and the reader has exactly one.** `marked` passes raw HTML through and has not sanitized since v5 — a deliberate separation-of-concerns stance, with `DOMPurify.sanitize(marked.parse(...))` as the documented pipeline. Python-Markdown likewise does not sanitize and says so explicitly (the old `safe_mode` is deprecated). But `markdown-it` — the most widely embedded of the three — ships **`html: false`** and advertises "safe by default". Replaced the generalisation with the three named behaviours, which is what a reader can act on. | 2027-06 |
| 42 | M8.4 | "Every Pod runs with a service account that can, by default, call the Kubernetes API" | `FIXED` | true but **overstated in the direction that matters**, and the overstatement is the common one. The token is mounted by the ServiceAccount admission controller at `/var/run/secrets/kubernetes.io/serviceaccount` unless `automountServiceAccountToken: false` (a projected, auto-rotating TokenRequest token since v1.22), and it does authenticate to the API server — but under stock RBAC the namespace's `default` account has **no permissions beyond the API-discovery endpoints granted to every authenticated principal**. So "can call the API" is true of authentication and nearly false of authorization. Rewritten to name the two real risks instead: an unnecessary **cluster identity** in every container, and the fact that binding one convenient Role to `default` silently promotes every Pod in the namespace. | 2027-06 |
| 43 | M3.5 | "dependency-check 13 aborts with no NVD API key" — the transcript and the stack trace | `SOURCED` `EXECUTED` | the transcript is accurate and reproduces, but the *reason* was missing and it changes what the reader should expect. An NVD API key has been **strongly recommended and never required** since 9.0.0 moved from the data feed to the NVD API; older versions warned and then crawled (~1.5 req/s without a key vs 5–10+ with one). The hard abort is a **13.0.0 regression** — [dependency-check#8715](https://github.com/dependency-check/DependencyCheck/issues/8715): the key now defaults to an empty string rather than null, and the client rejects a zero-length key (`Invalid API Key, length of 0 too short to provided a masked partial key`, exactly as the transcript shows). Annotated as a regression so the module does not read as wrong when a patched 13.x restores the warning. Note the repo moved: `jeremylong/DependencyCheck` was archived 2025-09-27. | 2027-03 |
| 44 | M2.2, M3.5 | Jinja2 auto-escapes by default | `SOURCED` | **checked because it is the classic trap and the course is on the right side of it.** Jinja2's own `Environment` defaults to `autoescape=False`; it is **Flask** that turns it on, for `.html`/`.htm`/`.xml`/`.xhtml` templates rendered through `render_template`. Every instance in the course either says "in Flask" or is inside a Flask example, and M3.5 states the mechanism explicitly (`autoescape=True` or `render_template`). No change. Keep the Flask qualifier attached if this text is ever edited — unqualified, it is false. | 2028-01 |
| 45 | M0.6, M0.7, M1.3, M1.7, M3.2, M6.1, M7.2, M9.1 | Tool and library defaults: macOS `zsh` / Linux `bash`; `rg` and `fd` skipping hidden and `.gitignore`d files; `awk` splitting on whitespace; a pipeline's exit code being the last command's; BRE vs ERE metacharacters; zsh not word-splitting unquoted parameters; containers running as root; Express `X-Powered-By`; ORMs parameterizing; `argon2-cffi` defaulting to Argon2id; `ignore-scripts`; Python `logging` emitting free text | `SOURCED` `EXECUTED` | ~20 claims, all confirmed and all **demonstrated on screen in the module that makes them** — the course shows `rg` skipping `.env`, shows the root shell in the container, shows the `X-Powered-By` header in the response. They are grouped rather than split into rows because each is settled by running the lab, they are stable across versions, and individually they would trade the ledger's signal for length. The one to re-check first if any is ever disputed is "containers run as root by default", since M8.4's entire hardening section is built on it. | 2028-01 |

## Deliberately not rows

- **Tool version banners** (`git version 2.55.0`, `Docker version 28.3.3`, `Nmap 7.99`, `vite v8.2.1`, `kind v0.32.0`, `k8s v1.36.1`, `Node v24.17.0`) are `EXECUTED` transcripts from the authoring machine, not currency claims. The course never calls them "latest", and M0.0 makes the inconsistency of version banners its actual teaching point. Same treatment as row 34 of the Guardians ledger.
- **`4.17.4`, `flask 2.0.0`, `rack 2.2.3`** are the *deliberately vulnerable* fixture versions. They are inputs to a demo, not assertions that anyone should run them.

## Batch 4 — quantity claims

39 `quantity` candidates. The Guardians `quantity` pass (its Batch 3) found that
most of the class was `EXECUTED` lab arithmetic and that only claims naming a
**third party** were checkable. That rule held here too — but it let through the
two defects below, and understanding why is the point of this batch.

**A quantity can be false without naming anyone.** Both defects are numbers about
the course's *own* material: the byte count of a request body it prints on the
same screen, and the parameters of a hash it tells you to run. Neither names an
outside party, so the Batch 3 triage rule would have filed both as `EXECUTED` and
moved on. They are still wrong, and they are worse than an outdated statistic,
because the reader is invited to reproduce them.

**Refined rule: `EXECUTED` is a status you earn by running it, not a status you
assign by looking at it.** 24 of the 39 candidates really are self-evident
arithmetic. The other 15 assert something a command would settle — and a claim
nobody actually ran is `PENDING` wearing an `EXECUTED` label. Every row below was
run on this machine (Node v22.12.0, M2 Pro) before it was written.

| # | Where | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 46 | M6.1 | The scrypt benchmark uses "params in the OWASP ballpark": `{ N: 16384, r: 8, p: 1 }` | `FIXED` | **OWASP lists no such row.** The Password Storage Cheat Sheet gives scrypt as `N=2^17 (128 MiB), r=8, p=1` (minimum) with fallbacks `2^16/r8/p2`, `2^15/r8/p3`, `2^14/r8/p5`, `2^13/r8/p10`. Every listed config with `N=2^14` carries **`p=5`**; with `p=1` the setting sits below the weakest row OWASP publishes, so "the OWASP ballpark" claimed an endorsement that does not exist. The reduction is nonetheless *correct for a benchmark*, for two executed reasons: Node's `scryptSync` defaults `maxmem` to 32 MiB, so `N=2^17` raises `error:030000AC … memory limit exceeded` unless `maxmem` is passed (verified: it succeeds in 258 ms at `maxmem: 268435456`); and `p=5` measures **6 hashes/sec** here, below the "tens to low hundreds" band the lab's own *Done when* requires. Rewritten to say plainly that it is a reduced benchmark setting, name both real OWASP rows, and give the production line | 2027-09 |
| 47 | M3.10 | "the body is exactly 6 bytes (`0\r\n\r\n`)" — the CL.TE request-smuggling lab | `FIXED` | **off by one, on the byte that is the entire exploit.** `0\r\n\r\n` is five bytes. The sixth byte counted by `Content-Length: 6` is the `G` of `GPOST` — which is *why* the `G` is there, and why the back-end's leftover begins `POST /admin`. Verified by running the lab's own code: front-end ends request 1 at byte **98**, back-end at **97**, leftover `"GPOST /admin HTTP/1.1\r\nHost: shop.example\r\n\r\n"`, and the six CL-counted bytes print as `"0\r\n\r\nG"`. The code and its documented output were always right; two prose restatements of it were wrong, in the one place a reader checks the arithmetic by hand | 2028-09 |
| 48 | M6.1 | bcrypt silently ignores input past **72 bytes**, historically truncating at a NUL; the safe pepper is `bcrypt(base64(HMAC-SHA256(pepper, password)))` | `SOURCED` | holds. OWASP Password Storage Cheat Sheet: "bcrypt has a maximum length input length of 72 bytes", with null bytes truncating at the first occurrence. The recommended construction is sound — a SHA-256 HMAC is 32 bytes, base64 of which is 44 characters, comfortably under 72. One wording note carried, not a defect: the course says the *digest* "fits under 72 bytes" when it is the base64 *encoding* that is fed to bcrypt; both are under 72, so the advice is unaffected | 2027-09 |
| 49 | M6.1 | SHA-256 runs at ~2.5M guesses/sec vs a slow hash's few hundred; the gap is ~10,000–50,000× | `EXECUTED` | re-measured on this machine rather than trusted: SHA-256 **1,444,466/sec**, scrypt `N=2^14,r=8,p=1` **35/sec**, ratio **~41,270×** — inside the course's stated band, and the walkthrough's illustrative `~1,000,000/sec ÷ ~22/sec → ~45,000×` is arithmetically sound. The band, not the point estimate, is what the course teaches, and the band survives on 2026 hardware | 2027-09 |
| 50 | M7.1, M7.2, M7.5.x | "1,000+ transitive packages", "1,400 npm packages", the `$99,999.99` refund, "62 percent margin", the "50,000-word essay" | `CONVENTION` | terminal — no source settles these and none should be sought. The dependency counts are order-of-magnitude illustrations the reader verifies locally (`npm ls --all`), and the rest are **fixtures inside the course's own scenarios**: an invented refund amount, an invented margin in a prompt-injection document, an invented abusive request. A fixture is not a claim about the world, and dressing one in a citation would be worse than leaving it plain | — |
| 51 | M7.2 | Equifax (2017) disclosed a breach of **147 million** records | `CORPUS` | 147 million is the FTC's figure for the 2017 Equifax breach and is the one the course already uses. The adjacent *settlement* figure was the Guardians ledger's Batch 3 defect (its row 46, `$700M` ceiling quoted as the amount paid) — that is a different number in a different course, and this one is unaffected | 2028-09 |

## Batch 5 — law and regulatory-deadline claims

29 `law` candidates, and this batch earns the priority the Batch 1 table gave it:
**four of the five defects are in one module (M7.3), and two of them are wrong
statutory deadlines.** Every other class in these ledgers fails safe — a stale
port name or an over-strong superlative makes the course *look* wrong to a reader
who checks. A wrong breach-notification deadline is different in kind: it is the
one error a learner can carry out of the course and cause real harm with, in a
room where nobody has time to check.

The candidate distribution is unusual too. Unlike `quantity` or `port`, where
most hits were the course's own fixtures, **essentially all 29 are real claims** —
you cannot mention GDPR incidentally. What made the triage finite was that 19 of
the 29 land in M7.3, the compliance module, so the batch is one careful reading of
one module plus a sweep of the incidental mentions elsewhere (row 57).

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 52 | M7.3 | Tracker: "Knows the **HIPAA 72-hour breach notification rule** (it applies to GDPR too) and what triggers it" | `FIXED` | **The worst defect found in any batch of either ledger: a fabricated statutory deadline, in the line the learner uses to certify themselves competent.** There is no 72-hour rule in HIPAA. The Breach Notification Rule (45 CFR 164.404–410) gives **60 calendar days from discovery** to notify individuals; HHS is notified contemporaneously at 500+ individuals and annually (within 60 days of year-end) below that; and a **business associate — which is what a developer building on PHI *is* — has 60 days to notify the covered entity**. The 72 hours is **GDPR Article 33**, to a data-protection supervisory authority, and the parenthetical "(it applies to GDPR too)" has the direction of the borrowing exactly backwards. The module's own theory states GDPR's 72 hours correctly two screens earlier, so the tracker **contradicted the text it was checking**. Fixed by adding the real rule to the HIPAA section — with the three traps that make 60 days tighter than it sounds (the clock starts at constructive *discovery*, not at the end of forensics; the BA's 60 and the covered entity's 60 can stack, which is why a sane BAA negotiates 5–15 days; many US state statutes are shorter and are not preempted) — and rewriting the tracker to ask the learner to keep **three** clocks apart, HIPAA 60 days / GDPR 72 hours / CRA 24 hours, with what triggers each. Guard `A64` bans the two being welded together | 2028-01 |
| 53 | M7.3 | HIPAA technical safeguards: "Encryption at rest and in transit (**both required**, unlike GDPR where it's 'appropriate measures')" | `FIXED` | **False, and the contrast it draws is backwards.** Encryption is an **addressable** implementation specification under **45 CFR 164.312(a)(2)(iv)** (at rest) and **164.312(e)(2)(ii)** (in transit) — you implement it, or you document why it is not reasonable and what equivalent safeguard you used. Addressable is *not* optional, but it is a risk-based standard, which makes it much closer to GDPR Art. 32's "appropriate measures" than the sentence's "unlike GDPR" allows. The January 2025 NPRM would delete the required/addressable distinction and make encryption and MFA flatly mandatory — but it is **still not final**: comments closed 7 Mar 2025, the May 2026 target slipped, and OMB now targets **2027**, with compliance 180 days after an effective date 60 days after publication. Rewritten to give the real status, keep the practical advice (encrypt — almost no alternative is defensible), and add the reason the distinction is worth knowing: telling an auditor the regulation *requires* it advertises that you have not read it. **Watch this row** — it is the one in this ledger most likely to flip to `required` | 2027-07 |
| 54 | M7.3 | Tracker: "Can name the **six** GDPR data subject rights"; the table it checks lists **five** | `FIXED` | **Three numbers, no two of which agree.** GDPR Chapter III grants **eight** rights, Articles 15–22: access, rectification, erasure, restriction of processing, portability, objection, the right not to be subject to solely automated decisions, and (Arts. 13–14) the right to be informed. The table listed five. The tracker asked for six. **Six is the number of lawful bases in Article 6** — which the module states correctly in a bold heading *three paragraphs above*, so the wrong number was almost certainly captured from the nearest bold number on the same page. This is the guard-on-an-example failure in reverse: the tracker is the artefact a learner self-certifies against, and it asked for a count that matched neither the law nor the course. Fixed by naming all eight, splitting them into the five that become API endpoints and the three that do not (Art. 18 restriction — in practice a `processing_restricted` flag the jobs honour; Art. 22 automated decisions; Arts. 13–14 the privacy notice), and warning about the Article 6 confusion by name. Guard `A66` | 2028-01 |
| 55 | M7.3 | "GDPR applies to any system that processes personal data of **EU residents**, regardless of where your company is located" | `FIXED` | **Two imprecisions, and the second one tells a reader they are in scope when they may not be.** (1) Article 3(2) keys on data subjects "**who are in the Union**" — a *location* test. Residency and citizenship are irrelevant: it reaches an American tourist in Rome and does not reach an EU citizen living in Toronto. (2) "regardless of where your company is located" is true only *conditionally*: for a controller with no EU establishment, Art. 3(2) applies where the processing relates to **offering goods or services to** people in the Union, or **monitoring their behaviour** there. Mere reachability of a website from the EU is expressly not enough — the EDPB's Guidelines 3/2018 targeting criterion looks for evidence the controller **envisaged** EU users (EU-language checkout, euro pricing, EU delivery, EU-targeted advertising), and it is assessed **per processing activity, not per company**, so one business can be partly in scope. Rewritten to the location test plus the targeting criterion with the concrete signals. Guard `A67` | 2028-01 |
| 56 | M7.3 | HIPAA: "Audit logs of all PHI access (who, what, when) — **retained for 6 years**" | `FIXED` | true as practice, mis-cited as text — the milder sibling of the Guardians Batch 4 finding (right advice, wrong authority). **45 CFR 164.312(b)** requires audit controls and specifies **no retention period at all** — no format, no fields, no duration. The familiar six years is **164.316(b)(2)**, which covers *documentation*: policies, procedures, assessments, retained six years from creation or last effective date. Your *logging policy* is unambiguously in scope; applying the same six years to the log **data** is the conservative industry reading, not the regulation, and most compliance vendors flatten the distinction without saying so. Left at six years — it is the right operational answer, and state law or a litigation hold can push it further — but the sentence now says which provision each half comes from. A developer who cites 164.312(b) for a six-year retention requirement will be corrected by the first auditor who reads it | 2028-01 |
| 57 | M7.3, M7.5.5, M7.5.7, M7.5.8, M9.1, M9.3, M4.1 | The remaining 24 `law` mentions: CRA 24h / NIS2 / DORA / PCI; GDPR erasure applied to vector stores and embeddings; "GDPR 72h" in the incident-response phases; GDPR/CCPA data minimisation in logging | `SOURCED` `CORPUS` | **all correct as written, and four were already closed in Batch 1** — CRA in force 10 Dec 2024 with reporting from 11 Sep 2026 and full application 11 Dec 2027, 24h early warning to ENISA/CSIRT (row 20); DORA since 17 Jan 2025, five pillars (21); NIS2 transposition deadline Oct 2024, already correctly hedged as "since national transposition" (22); PCI DSS 4.0.1 with the 31 Mar 2025 future-dated requirements (17). Checked fresh this pass: every standalone "GDPR 72 hours" in M9.1/M9.3 names the supervisory authority and the personal-data-breach trigger, so none of them has the row 52 defect. The **M7.5.5 embeddings point is the strongest legal reasoning in the course and needed no change** — that deleting a source row does not delete its embedding is a live erasure problem, and that embeddings are not reliable anonymisation because inversion can partially reconstruct the source is the correct and non-obvious reading. M7.5.7/M7.5.8 on pasting customer data into AI assistants correctly separate "not trained on" from "not stored". The one incompleteness carried forward, not a defect: the CRA's 24h is only the **early warning** — a full notification is due at 72 hours and a final report at 14 days, which the module still does not mention (noted in row 20, unchanged) | 2027-12 |

## Fixes applied in this pass

**Batch 5 (2026-09-17) — five defects, four of them in one module, two of them wrong deadlines.**

1. **M7.3 tracker** — a **"HIPAA 72-hour breach notification rule" that does not
   exist**. HIPAA is 60 calendar days from discovery; 72 hours is GDPR's, and the
   parenthetical "(it applies to GDPR too)" reversed the borrowing. The module's
   own theory said GDPR's 72 hours correctly two screens earlier.
2. **M7.3** — HIPAA encryption at rest and in transit called "**both required**".
   It is **addressable** (164.312(a)(2)(iv), (e)(2)(ii)); the rule that would make
   it required is a January 2025 NPRM still not final, now targeted at 2027.
3. **M7.3 tracker** — "the **six** GDPR data subject rights", checking a table that
   listed **five**, for a law that grants **eight**. Six is the number of *lawful
   bases* in Article 6, three paragraphs up the same page.
4. **M7.3** — GDPR scope given as "**EU residents**, regardless of where your company
   is located". Art. 3(2) is a location test, and reaches a non-EU company only
   through the targeting or monitoring criterion.
5. **M7.3** — PHI audit logs "retained for 6 years" cited to the audit-controls
   rule, which sets no retention period; the six years is the *documentation* rule.

**The shape worth carrying forward: the tracker is not documentation, it is the
claim the learner will repeat.** Two of these five (rows 52, 54) are in `tracker`
strings, and both **contradicted the module's own theory text** — the correct
GDPR deadline and the correct rights table were on screen, unchanged, while the
self-assessment line asked for something else. A defect in prose misleads a reader
once; a defect in a tracker is the sentence they rehearse until they believe it,
and it is the last thing they read before marking the module complete. **Audit
`tracker`, `quiz` and `challenges` strings on their own pass**, against the theory
rather than against the world — an internal contradiction is the cheapest defect
in these courses to find and, per the standing note that a green gate proves
structure and never truth, one of the few that a purely internal check *can*
catch.

The second finding is about the class itself. Legal claims have no `EXECUTED`
escape hatch and no fixture exemption — the triage rules that let Batches 3 and 4
dismiss most of their candidates (a byte count is arithmetic; a port number is an
argument) have **no analogue here**. You cannot mention GDPR illustratively. That
makes `law` the most expensive tag per candidate and the one where "we'll get to
it" is least defensible, which is why the Guardians ledger's own 13 remaining
`law` candidates (its Batch 7) should be pulled forward.

All five defects are fixed strings, so all five carry guards — `A64`–`A68`. `A64`
carries an acquittal on `60 calendar days`, because the corrected text
deliberately names both deadlines in one sentence in order to keep them apart.

**Batch 4 (2026-09-17) — two defects, both about the course's own arithmetic.**

1. **M6.1** — `{ N: 16384, r: 8, p: 1 }` labelled "params in the OWASP ballpark".
   OWASP publishes no scrypt row with `N=2^14` and `p=1`; its weakest fallback is
   `p=5` and its minimum is `N=2^17, r=8, p=1`. The parameters stay (Node's 32 MiB
   `maxmem` default and the lab's own timing band both require the reduction) but
   the label goes: the lab now states it is a deliberately reduced benchmark
   setting, names both real OWASP rows, and gives the production line to copy.
2. **M3.10** — "the body is exactly 6 bytes (`0\r\n\r\n`)". That string is five
   bytes; the sixth is the `G`, which is the whole CL.TE mechanism. Fixed in the
   JS comment and the walkthrough. The lab code and its printed offsets (98 / 97)
   were correct throughout and were re-run to confirm it.

**The shape worth carrying forward: `EXECUTED` claimed, not earned.** Both
defects sat in material the previous pass would have classed as self-evident lab
arithmetic — no third party named, therefore nothing to look up. But a number
about code the reader is *told to run* is the most falsifiable kind there is, and
the most damaging to get wrong, because verification is the assignment. Batch 3's
triage rule ("a quantity is checkable only when it describes something outside
the course") is **too coarse** and is superseded here: a quantity is checkable
whenever a command settles it, inside or out. The cheap discipline that follows —
run it, paste the output, then write the row — is what caught both.

Both defects are fixed strings, so both carry guards — `A57` and `A58` — each
negative-tested against the pre-fix text and clear against the fixed file.

**Batch 3 (2026-09-17) — four defects, and this is the batch that justifies the ledger.**

1. **M2.4** — "flask-cors does exact-origin matching by default." **It does not.** It
   matches with `re.match`, which anchors only at the start, so a plain allow-list
   string `https://app.example.com` also matches `https://app.example.com.evil.com`
   — and the course's only warning was aimed at the *regex* case, while the default
   case had the identical hole. The single most serious defect found in any batch:
   not a stale number but **a promised safety property the library never had**,
   stated in the exact place a reader would lean on it.
2. **M7.5.4 / M3.9** — "`torch.load` uses pickle by default." **PyTorch 2.6
   (29 Jan 2025)** flipped the default to `weights_only=True`. Rewritten as
   mitigation-not-repair.
3. **M7.5.3** — "most Markdown renderers pass raw HTML through by default."
   True of `marked` and Python-Markdown, false of `markdown-it` (`html: false`).
   Replaced with the three named behaviours, which is what a reader can act on.
4. **M8.4** — "every Pod runs with a service account that **can call the Kubernetes
   API**." True of authentication, nearly false of authorization: the `default`
   account has no permissions beyond API discovery. Rewritten to the two real
   risks — an unnecessary cluster identity in every container, and `default`
   silently promoting every Pod the moment someone binds a Role to it.

**A default is the most perishable claim a security course can make.** It is a
decision a maintainer can reverse in a point release, and row 40 is the sharp
case: PyTorch changed its default *for security*, so the course's warning became
overstated — the failure was silent precisely because the world got safer. A
rotted warning is as much a defect as a rotted reassurance, and it is far harder
to notice, because nothing breaks and no learner complains.

**A guard is only worth what its negative test proves.** `A53` was first written
with bare backticks, so one of its two branches silently matched nothing —
the course escapes its backticks (`` \` ``). Testing each branch separately
exposed it, and the repaired guard immediately found **a fourth `torch.load`
passage the manual pass had missed.** Test every alternation branch on its own;
an `|` is a place for a guard to half-die without saying so.

All four defects are fixed strings, so all four carry guards — `A52`, `A53`,
`A54` here, with the Kubernetes rewrite covered by the surrounding prose rather
than a pattern, since its defect was an overstatement rather than a fixed phrase.

**Batch 2 (2026-09-12) — two defects.**

1. **M3.5** — "the most common full-stack *language*" for a runtime, contradicting the course's own Intro two thousand lines earlier. A ledger pass catches this class precisely because it reads the same claim in every place it is made; neither passage looks wrong alone.
2. **M4.1** — "the fastest-growing attack class" for the category that has the *fewest* data occurrences in the edition being described. The claim was not just unsourced, it ran against the source it was summarising.

Both are fixed strings, so both now carry a regression guard in
`tools/guardrail.py` — `A42` and `A43` — each verified by running it against the
pre-fix file, where it fires, as well as against the fixed one, where it is
clear. See the Guardians ledger for the five guards this batch added there.

**Batch 1 (2026-09-11) — four defects.** Three are the same family as the Guardians pass — a claim that was
true when written, or stated more strongly than any source supports — and one is
a citation to a document that does not exist:

1. **M4.1** — ASVS "14 chapters" → **17**. 14 is the 4.0.3 count carried forward under the 5.0 label.
2. **M4.1** — "ASVS V6 Session Management / V6.2.1" → **V7 / V7.2.3**. The cited requirement number existed in no edition, and its real counterpart is L1, not the L2 the sentence claimed to be reading.
3. **M7.5.8** — "the OWASP Agentic Top 10" → **OWASP Top 10 for Agentic Applications**, with ASI01–ASI10 ids. The old name pointed at no publication, and one of the five taught "entries" belongs to a different list entirely.
4. **M8.4** — CVE-2026-31789 relabelled **CRITICAL → HIGH** in the trivy fixture. No vendor rates it Critical; upstream rates it Low.

Plus one edition correction: **M10.1**'s `A01:2021` → `A01:2025`, the last survivor
of the 2021-numbering purge at `173a31d`.

None were reachable by the guardrail gate before this pass: every one of them is
a well-formed sentence pointing at a real standard. Each now has a regression
guard in `tools/guardrail.py`'s known-bad table (A37–A41), so they cannot
silently return.
