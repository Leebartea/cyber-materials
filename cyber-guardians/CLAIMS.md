# Cyber Guardians — claim ledger

Every rule-shaped assertion this course makes, with a status and the evidence
behind it. The guardrail gate (`tools/guardrail.py`) proves the course is
*structurally* sound — balanced fences, resolving cross-references, no dead
links. It cannot prove anything here is *true*. That is what this file is for.

- **Course file:** `cyber-guardians/cyber_guardians_app.html` (42 modules + 3 roadmaps)
- **Candidates extracted by:** `python3 tools/claims_extract.py guardians --json out.json`
- **Last pass:** 2026-09-11 (Batch 1 — standards and identifiers)

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
version, or software version. 478 candidate claims were extracted across all 45
module objects; 63 carry one of those identifier tags and collapse to the 34
distinct rules below.

**ATT&CK technique IDs are closed too — but not through `attack.mitre.org`.**
That host resolves to GitHub Pages (185.199.x.x), and every GitHub Pages address
is unreachable from the authoring connection: `curl`, `WebFetch` and the gate's
own reachability probe all fail while non-Pages hosts answer normally. A blocked
*page* is not an unavailable *source* — MITRE publishes the same data as STIX in
`mitre-attack/attack-stix-data`, and `raw.githubusercontent.com` is reachable.
All 32 distinct technique ids were validated against that bundle (row 35).

Not yet adjudicated — the next batches, in priority order:

| Batch | Class | Candidates | Why it matters |
|---|---|---|---|
| 2 | `rank` — "most common", "the first", "industry standard" | 182 | superlatives are the easiest thing to assert and the hardest to source |
| 3 | `quantity` — record counts, percentages, key sizes, costs | 54 | breach figures drift between retellings |
| 4 | `port` — port and protocol assignments | 51 | mostly IANA-settleable, low risk, high volume |
| 5 | `date` — "as of", "since", release years | 33 | rots by definition |
| 6 | `default` — "by default", "defaults to" | 22 | vendor defaults change silently between versions |
| 7 | `law` — GDPR/HIPAA/CFAA obligations and deadlines | 13 | wrong legal deadlines are the costliest error class here |
| 8 | `attribution` — "according to", "researchers found" | 5 | each needs the **primary** document, not the report quoting it |

(`attack` — 73 candidates, 32 distinct ids — is **closed** in Batch 1, row 35.)

## Batch 1 — standards and identifiers

| # | Module | Claim as taught | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 1 | ★, M1.5 | NIST CSF 2.0 is current; six functions; GOVERN added in 2.0 | `SOURCED` | CSF 2.0 released 2024-02-26; GOVERN is the added sixth function; still current | 2027-02 |
| 2 | ★ | Course is aligned to OWASP Top 10:2025, NIST CSF 2.0, SP 800-63B-4, 2025 CWE Top 25 | `SOURCED` | each component verified in rows 1, 5, 6, 12 | 2026-12 |
| 3 | ★ | Completing the course ≈ CompTIA Security+ level of knowledge | `CONVENTION` | no authority can certify an equivalence between a self-paced course and an exam; course states it as a self-assessment, not an accreditation | — |
| 4 | ★, M0 | `python3` v3.11+ / `git` v2.40+ are the required floors | `CONVENTION` | a floor the course chooses, not a fact about the tools | — |
| 5 | M3 | NIST SP 800-63B-4 (July 2025) is the password reference | `SOURCED` | final published 2025-07-31, superseding SP 800-63B; csrc.nist.gov/pubs/sp/800/63/b/4/final | 2027-07 |
| 6 | M5 | PCI DSS 4.0.1 is current; contractual, not statutory | `SOURCED` | v4.0.1 (June 2024) is current; v4.x are the only active versions | 2027-03 |
| 7 | M1.5, M6.5 | ISO/IEC 27001:2022 is the current ISMS certification standard | `SOURCED` | 2022 edition replaced 2013; 93 controls in 4 themes | 2027-06 |
| 8 | M6.5 | ISO/IEC 27001:2022 Annex A.7 "Physical controls" spans A.7.1–A.7.14 | `SOURCED` | Annex A themes: 37 organizational (5.x), 8 people (6.x), **14 physical (7.1–7.14)**, 34 technological (8.x) | 2027-06 |
| 9 | M1.5, M23.5 | CIS Controls v8.1 is current: 18 controls | `SOURCED` | v8.1 (June 2024) current, no v9; 18 controls, 153 safeguards, 3 IGs | 2027-01 |
| 10 | M23.5 | CIS Controls v8.1 Control 11 is "Data Recovery" | `SOURCED` | control list for v8/v8.1 | 2027-01 |
| 11 | M6.5 | CIS Controls v8.1 leaves physical security uncovered | `FIXED` | the course claimed "its scope note says so explicitly" — **no such verbatim scope statement exists**. Searched: CIS v8.1 landing page, SANS v8 poster commentary, CMMC-mapping analyses. The primary PDF mirror (`arklegaudit.gov/docs/cis_controls_guide.pdf`) fails TLS with a self-signed certificate, and cisecurity.org gates the download. What *is* supportable: v8.1 has no physical-security Safeguard, and CIS→CMMC mappings show facility access, visitor management and physical access logs as uncovered gaps. Reworded to that. Do not re-run this search — it has been run | — |
| 12 | ★ | The 2025 CWE Top 25 is the current edition | `SOURCED` | 2025 edition published Dec 2025 from 39,080 CVEs; cwe.mitre.org/top25/ | 2026-12 |
| 13 | M19 | Every CVE is tagged with a CWE; CWE-79 XSS, CWE-89 SQLi, CWE-352 CSRF | `SOURCED` | CWE catalogue; all three sit in the 2025 Top 25 (XSS #1, SQLi #2, CSRF #3) | 2026-12 |
| 14 | M11 | Command injection is OWASP **A05:2025 Injection** | `SOURCED` | Top 10:2025 — Injection fell from A03:2021 to A05:2025 | 2027-11 |
| 15 | M14, M19 | **A03:2025 Software Supply Chain Failures** is the Equifax category | `SOURCED` | new 2025 category expanding A06:2021 Vulnerable and Outdated Components | 2027-11 |
| 16 | M16 | **A09:2025 Security Logging and Alerting Failures** | `SOURCED` | held position 9; renamed from "Monitoring" to "Alerting" in 2025 | 2027-11 |
| 17 | M25 | SSRF is now filed under **A01:2025 Broken Access Control**, not its own number | `SOURCED` | A01 absorbed SSRF in the 2025 edition; CWE coverage grew 34→40 | 2027-11 |
| 18 | M10 | Aug 2024: NIST finalized FIPS 203 (ML-KEM), 204 (ML-DSA), 205 (SLH-DSA) | `SOURCED` | finalized 2024-08-13 | 2027-08 |
| 19 | M10 | HQC is a standardized post-quantum algorithm | `FIXED` | HQC was **selected** 2025-03-11 as a code-based backup KEM; its FIPS is still unpublished (expected ~FIPS 207, 2027). The course's "added as a backup" sat inside a sentence about algorithms NIST *finalized*, implying a standard that does not exist. Reworded to separate selected from standardized | 2027-03 |
| 20 | M16.5 | NIST published SP 800-207, Zero Trust Architecture, in 2020 | `SOURCED` | final published 2020-08-11; still final. Companion SP 800-207A now exists (cloud-native/multi-cloud) but does not supersede it | 2028-08 |
| 21 | M6.5 | NIST SP 800-88 defines Clear / Purge / Destroy | `FIXED` | the three levels are correct and unchanged, but the course cited **Rev 1**, which NIST **withdrew on 2025-09-26** when Rev 2 published. Updated to Rev 2 (Sept 2025), including what Rev 2 adds — sanitization *validation*. Other mentions in the module are version-agnostic and needed no change | 2028-09 |
| 22 | M23.5 | NIST SP 800-34 Rev 1 defines the BIA / RTO / RPO vocabulary | `SOURCED` | Rev 1 (2010, upd. 2010-11-11) is still Final; no Rev 2 draft posted | 2027-09 |
| 23 | M1.5 | NIST SP 800-53 Rev 5 is the federal control catalogue CSF points to | `PENDING` | Rev 5 is the current revision; confirm the patch release in force at csrc.nist.gov/pubs/sp/800/53/r5/upd1/final before the next pass | 2027-01 |
| 24 | M23.5 | ISO 22301:2019 is the BCMS standard; ISO 27001:2022 A.5.29/A.5.30 are the matching controls | `SOURCED` | 2019 (2nd ed.) current, no replacement edition. **Amd 1:2024** (Feb 2024) adds climate-change consideration to clauses 4.1/4.2 — worth a mention if the module is ever expanded | 2027-06 |
| 25 | M28 | NIST NICE Workforce Framework Components version | `FIXED` | course said **v2.0.0, March 2025** — two releases stale. Change log: v2.2.0 released **2026-04-28**, v2.1.0 2025-12-03, v2.0.0 2025-03-05, v1.0.0 2024-03-05. Updated to v2.2.0 (April 2026). The framework itself is still SP 800-181r1 (Nov 2020); only Components version | 2027-04 |
| 26 | M4 | Header field names are case-insensitive per RFC 5322 | `PENDING` | true of RFC 5322 §3.6; read the ABNF at rfc-editor.org/rfc/rfc5322 to close | 2028-01 |
| 27 | M11.7 | `0 .` is a null MX per RFC 7505 | `SOURCED` `EXECUTED` | RFC 7505 defines the null MX; the `dig` output in the module was run against `example.com` on 2026-09-11 | 2028-01 |
| 28 | M12, M16 | `192.0.2.0/24` is TEST-NET-1, reserved for documentation by RFC 5737 | `SOURCED` | RFC 5737 reserves 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24 | 2028-01 |
| 29 | M1.5, M14, M19 | Equifax: ~147M people, via unpatched Apache Struts CVE-2017-5638, patch public two months | `SOURCED` | FTC: 147M names/DOB, 145.5M SSNs; failure-to-patch is the FTC's own pleaded allegation | 2028-01 |
| 30 | M25 | Capital One: SSRF + IAM misconfiguration, ~$80M fine, perpetrator convicted | `SOURCED` | OCC NR-2020-101 (2020-08-06), $80M civil money penalty for cloud risk-assessment failures. **Nuance:** the OCC order cites the cloud-migration risk process, not the breach itself | 2028-01 |
| 31 | M19 | Log4Shell is CVE-2021-44228 (2021) | `SOURCED` | NVD; used consistently across theory, case study and the lab's fixture data | 2028-01 |
| 32 | M19 | CVE-2021-41773 is an Apache path-traversal finding a scanner reports | `SOURCED` | NVD; appears only inside simulated scanner output | 2028-01 |
| 33 | M11.5 | Shellshock is CVE-2014-6271 (2014) | `SOURCED` | NVD | 2028-01 |
| 34 | M0, M0.5, M19 | Tool banners in expected output: `git 2.45.2`, `nmap 7.95`, `hashcat 6.2.6`, `Docker 27.0.3`, `nuclei v3.3.7` | `EXECUTED` | transcripts from the authoring machine, not currency claims. The course never calls these "latest", and the labs are written so a different version still matches the described *shape* of the output | — |
| 35 | M18, M18.5, M23, M26, M27 | All 32 MITRE ATT&CK technique ids the course teaches are real, current, and paired with the right behaviour | `SOURCED` | validated against MITRE's own STIX bundle (`mitre-attack/attack-stix-data`, `enterprise-attack.json`, fetched 2026-09-11): every id resolves to an `attack-pattern`, **none deprecated, none revoked**, and each use matches the official technique. Four ids are used in shorthand without their official title — T1021.006 (as "WINRM / PowerShell remoting"), T1048 ("exfiltrated over an alt channel"), T1190 ("exploited web app to get a shell"), T1543 ("installed a launch-agent") — all describe the technique correctly, so this is style, not error. T1543 pairs a macOS launch-agent with the *parent* technique; the sub-technique T1543.001 Launch Agent is used correctly elsewhere | 2027-04 |

## Fixes applied in this pass

Four defects, all of the same family — a claim that was true when written and
quietly stopped being true, or was stated more strongly than the source supports:

1. **M28** — NICE Components v2.0.0 (March 2025) → **v2.2.0 (April 2026)**. Two releases stale.
2. **M6.5** — SP 800-88 **Rev 1** → **Rev 2**; Rev 1 has been withdrawn, so the course was citing a dead document. Added what Rev 2 changes.
3. **M6.5** — "CIS Controls v8.1 deliberately does not cover physical security — its scope note says so explicitly" → rewritten to the defensible version. No such scope note was found.
4. **M10** — HQC presented inside a list of finalized FIPS standards → now explicitly *selected, not yet standardized*.

None were reachable by the guardrail gate: every one of them is a
well-formed sentence pointing at a real standard.
