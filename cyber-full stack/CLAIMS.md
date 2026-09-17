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
- **Last pass:** 2026-09-16 (Batch 2 — rank and superlative claims, closed: no `PENDING` rows remain)

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
| 3 | `default` — "by default", "defaults to" | 65 | vendor defaults change silently between versions; this course's are mostly Express/Node/Docker behaviours a test can settle |
| 4 | `quantity` — record counts, percentages, key sizes, costs | 39 | breach figures drift between retellings |
| 5 | `law` — GDPR/CRA/DORA/NIS2 obligations and deadlines | 29 | wrong legal deadlines are the costliest error class here |
| 6 | `port` — port and protocol assignments | 23 | mostly IANA-settleable, low risk, high volume |
| 7 | `date` — "as of", "since", release years | 15 | rots by definition |
| 8 | `attribution` — "according to", "researchers found" | 1 | needs the **primary** document, not the report quoting it |

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

## Deliberately not rows

- **Tool version banners** (`git version 2.55.0`, `Docker version 28.3.3`, `Nmap 7.99`, `vite v8.2.1`, `kind v0.32.0`, `k8s v1.36.1`, `Node v24.17.0`) are `EXECUTED` transcripts from the authoring machine, not currency claims. The course never calls them "latest", and M0.0 makes the inconsistency of version banners its actual teaching point. Same treatment as row 34 of the Guardians ledger.
- **`4.17.4`, `flask 2.0.0`, `rack 2.2.3`** are the *deliberately vulnerable* fixture versions. They are inputs to a demo, not assertions that anyone should run them.

## Fixes applied in this pass

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
