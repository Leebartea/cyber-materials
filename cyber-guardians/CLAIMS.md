# Cyber Guardians — claim ledger

Every rule-shaped assertion this course makes, with a status and the evidence
behind it. The guardrail gate (`tools/guardrail.py`) proves the course is
*structurally* sound — balanced fences, resolving cross-references, no dead
links. It cannot prove anything here is *true*. That is what this file is for.

- **Course file:** `cyber-guardians/cyber_guardians_app.html` (42 modules + 3 roadmaps)
- **Candidates extracted by:** `python3 tools/claims_extract.py guardians --json out.json`
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
| 3 | `quantity` — record counts, percentages, key sizes, costs | 54 | breach figures drift between retellings |
| 4 | `port` — port and protocol assignments | 51 | mostly IANA-settleable, low risk, high volume |
| 5 | `date` — "as of", "since", release years | 33 | rots by definition |
| 6 | `default` — "by default", "defaults to" | 22 | vendor defaults change silently between versions |
| 7 | `law` — GDPR/HIPAA/CFAA obligations and deadlines | 13 | wrong legal deadlines are the costliest error class here |
| 8 | `attribution` — "according to", "researchers found" | 5 | each needs the **primary** document, not the report quoting it |

(`attack` — 73 candidates, 32 distinct ids — is **closed** in Batch 1, row 35.
`rank` — 182 candidates — is **closed** in Batch 2, rows 36–44.)

**How 182 `rank` candidates collapsed to 9 rules.** The regex fires on any
`the first` / `the only` / `top \d+` / `most common`, and in a teaching text
those are overwhelmingly *narrative*: "the first hop", "the only defence here",
"OWASP Top 10" as a title. Grouping the 182 by which trigger matched (70 `the
first`, 42 `the only`, 13 `top 10`, 20 `rank`, …) made the triage finite — the
`the first` / `the only` pile was cleared with one exclusion pattern for
narrative nouns, leaving 57 candidates carrying a real superlative, and those
collapse to the 9 rules below. **The claims that survive are the ones that name
a third party** — a platform, a report, a vendor ranking. A superlative about
the reader's own likely mistake cannot be sourced and should never be dressed
as a statistic (row 44).

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
| 23 | M1.5 | NIST SP 800-53 Rev 5 is the federal control catalogue CSF points to | `SOURCED` | closed 2026-09-16. **Rev 5 is still the current revision** — no Rev 6 exists. The patch release in force is **5.2.0 (27 August 2025)**, issued under EO 14306 and delivered through NIST's CPRT rather than as a new PDF; it adds SA-15(13), SA-24 and SI-02(07) and revises SI-07(12), with **no change to the SP 800-53B baselines**. The course names only the revision, never the patch level, which is the right granularity: patch releases now land continuously through CPRT, so any 5.x.y written into a lesson starts rotting the day it is typed | 2027-08 |
| 24 | M23.5 | ISO 22301:2019 is the BCMS standard; ISO 27001:2022 A.5.29/A.5.30 are the matching controls | `SOURCED` | 2019 (2nd ed.) current, no replacement edition. **Amd 1:2024** (Feb 2024) adds climate-change consideration to clauses 4.1/4.2 — worth a mention if the module is ever expanded | 2027-06 |
| 25 | M28 | NIST NICE Workforce Framework Components version | `FIXED` | course said **v2.0.0, March 2025** — two releases stale. Change log: v2.2.0 released **2026-04-28**, v2.1.0 2025-12-03, v2.0.0 2025-03-05, v1.0.0 2024-03-05. Updated to v2.2.0 (April 2026). The framework itself is still SP 800-181r1 (Nov 2020); only Components version | 2027-04 |
| 26 | M4 | Header field names are case-insensitive per RFC 5322 | `SOURCED` | closed 2026-09-16, and the route matters. RFC 5322 has **no declarative sentence** saying field names are case-insensitive; it inherits the property from **§1.2.2**, which specifies that a literal value in quotation marks is case-insensitive ("`A` for either uppercase or lowercase A"). Every field name in the grammar — `"From:"`, `"Date:"` — is such a literal, so `FROM:` is legal and the lab's `grep -i` is mandatory, exactly as M4 teaches. Cited as "per RFC 5322", which is correct; do not tighten it to a section number, because the obvious candidate (§3.6.8) says something different — that optional field names must not duplicate specified ones | 2028-01 |
| 27 | M11.7 | `0 .` is a null MX per RFC 7505 | `SOURCED` `EXECUTED` | RFC 7505 defines the null MX; the `dig` output in the module was run against `example.com` on 2026-09-11 | 2028-01 |
| 28 | M12, M16 | `192.0.2.0/24` is TEST-NET-1, reserved for documentation by RFC 5737 | `SOURCED` | RFC 5737 reserves 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24 | 2028-01 |
| 29 | M1.5, M14, M19 | Equifax: ~147M people, via unpatched Apache Struts CVE-2017-5638, patch public two months | `SOURCED` | FTC: 147M names/DOB, 145.5M SSNs; failure-to-patch is the FTC's own pleaded allegation | 2028-01 |
| 30 | M25 | Capital One: SSRF + IAM misconfiguration, ~$80M fine, perpetrator convicted | `SOURCED` | OCC NR-2020-101 (2020-08-06), $80M civil money penalty for cloud risk-assessment failures. **Nuance:** the OCC order cites the cloud-migration risk process, not the breach itself | 2028-01 |
| 31 | M19 | Log4Shell is CVE-2021-44228 (2021) | `SOURCED` | NVD; used consistently across theory, case study and the lab's fixture data | 2028-01 |
| 32 | M19 | CVE-2021-41773 is an Apache path-traversal finding a scanner reports | `SOURCED` | NVD; appears only inside simulated scanner output | 2028-01 |
| 33 | M11.5 | Shellshock is CVE-2014-6271 (2014) | `SOURCED` | NVD | 2028-01 |
| 34 | M0, M0.5, M19 | Tool banners in expected output: `git 2.45.2`, `nmap 7.95`, `hashcat 6.2.6`, `Docker 27.0.3`, `nuclei v3.3.7` | `EXECUTED` | transcripts from the authoring machine, not currency claims. The course never calls these "latest", and the labs are written so a different version still matches the described *shape* of the output | — |
| 35 | M18, M18.5, M23, M26, M27 | All 32 MITRE ATT&CK technique ids the course teaches are real, current, and paired with the right behaviour | `SOURCED` | validated against MITRE's own STIX bundle (`mitre-attack/attack-stix-data`, `enterprise-attack.json`, fetched 2026-09-11): every id resolves to an `attack-pattern`, **none deprecated, none revoked**, and each use matches the official technique. Four ids are used in shorthand without their official title — T1021.006 (as "WINRM / PowerShell remoting"), T1048 ("exfiltrated over an alt channel"), T1190 ("exploited web app to get a shell"), T1543 ("installed a launch-agent") — all describe the technique correctly, so this is style, not error. T1543 pairs a macOS launch-agent with the *parent* technique; the sub-technique T1543.001 Launch Agent is used correctly elsewhere | 2027-04 |

## Batch 2 — rank and superlative claims

| # | Module | Claim as taught | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 36 | M4 | "The single most common cyberattack is not a Hollywood-style technical hack — it's psychological" | `FIXED` | **The rank flipped.** Verizon DBIR 2026 (22,000+ breaches, 145 countries, Nov 2024–Oct 2025): exploitation of vulnerabilities is the #1 initial access vector at **31%**, up from 20% — the first time in the report's 19-year history that credential theft lost the top spot. Credential abuse 13% (16% adjusting for the new pretexting vector), phishing 16%. The defensible figure is the one that does not depend on a ranking: a **human element is present in 62% of breaches**. Objective rewritten to that. | 2027-05 |
| 37 | M28 | "a TryHackMe 'Pro Hacker' rank" (4 sites) | `FIXED` | **Pro Hacker is a HackTheBox rank, not a TryHackMe one.** HTB names 7 ranks by share of *active* content owned — Noob, Script Kiddie (>5%), Hacker (>20%), Pro Hacker (>45%), Elite Hacker (>70%), Guru (>90%), Omniscient (100%). TryHackMe uses 21 numbered **levels**, 0x1 Neophyte through 0x15 GRANDMASTER; "Pro Hacker" appears nowhere in that ladder. Reattributed to HTB and the two ladders are now distinguished where both are named. | 2027-09 |
| 38 | M20 | "IDOR … is the single most common bug in real bug-bounty reports" | `FIXED` | **No published source ranks IDOR first.** HackerOne's platform data (78,042 valid issues across 1,300+ customer programs) puts **XSS** top for bug bounty; IDOR placed **8th** in the 2019 Top 10 edition, and the broader "improper access control" was 2nd in 2020. Rewritten to say XSS holds the top spot and IDOR is among the most consistently rewarded. | 2027-10 |
| 39 | M1.5, M23.5 | CIS Controls v8.1 = 18 controls; "the fastest practical starting point for a small org" | `SOURCED` + `CONVENTION` | count re-confirmed this pass — v8.1 (June 2024) has **18 controls, 153 safeguards, 3 IGs** (IG1 = 56), unchanged from v8; duplicate of Batch 1 row 9 and still true. The *superlative* is a pedagogical judgement no authority settles, and is stated as advice, not as a finding. | 2027-01 |
| 40 | M1 | Colonial Pipeline was "the largest refined-fuel pipeline on the US East Coast" | `SOURCED` | true, and **stated more weakly than the evidence allows** — Colonial is the largest refined-products pipeline in the United States, not merely on the East Coast. EIA: ~5,500 miles, **2.5 million b/d**, 29 refineries to 267 terminals, Houston to New York Harbor, routinely at or near capacity. The only comparable East Coast link is the Products (SE) / Plantation line at **720,000 b/d** — about a third the size, so the rank is not close. Left as written: understating a rank is not a defect, and the module's point is the outage's blast radius, not the league table. | 2028-01 |
| 41 | M13.5 | TJX was "the largest retail breach of its era" | `SOURCED` | confirmed, and the hedge is doing real work. TJX's own SEC filing put it at **45.7 million** records — the largest breach on record at the time, passing CardSystems Solutions (~40 million, 2005) — and it held that place until Albert Gonzalez's **Heartland** indictment in August 2009 named **130 million** cards. Gonzalez ran both. The course's "later estimates ran higher" matches the October 2007 court filings, which put TJX nearer 94 million. So "of its era" is exactly right: drop the hedge and the sentence becomes false. | 2028-01 |
| 42 | M25.5 | Mirai/Dyn was "one of the largest DDoS attacks ever seen" | `FIXED` | **A superlative that rotted by an order of magnitude.** Dyn was the largest attack measured in 2016; the record is now **31.4 Tbps** (Cloudflare, Q4 2025), and Cloudflare alone mitigated **935 attacks above 1 Tbps in H1 2026** — the tier Dyn was estimated to sit in is now routine. Rewritten to "the largest DDoS attack measured up to that point", with the growth since stated as a floor ("passed 30 Tbps in late 2025") so it cannot rot the same way: records only move one direction. The neighbouring **1.2 Tbps** figure was a second defect — it is a third-party estimate **Dyn explicitly declined to confirm**, reporting only "up to 50x normal" packet flow; now attributed as an estimate. The "hundreds of thousands" of devices is correct and now carries its source: Antonakakis et al., *Understanding the Mirai Botnet* (USENIX Security '17), measured a **600,000** peak in late November 2016. | 2028-01 |
| 43 | M21 | Missing bounds checks "have caused the largest incidents in computing history" | `CONVENTION` | no register ranks incidents by root cause, so no source can settle it even in principle. Left standing: it is hedged, it is the consensus reading of Morris/Heartbleed/EternalBlue, and the sentence's actual load-bearing claim (that this is why the industry is moving to memory-safe languages) is separately supported. | — |
| 44 | ★, M2, M9, M15, M20, M26 | The "single most common &lt;mistake&gt;" teaching idiom — the Homebrew PATH slip, the expired cert, binding to `0.0.0.0`, the loopback false pass, the hand-rolled proxy hang, secret-scanner noise | `CONVENTION` | **Six instances, all deliberately kept.** No telemetry exists that ranks the mistakes learners make, so no lookup can settle any of them. They are defensible *because* they are framed as classroom experience rather than as findings. The rule this batch sets: **keep the idiom, never attach a number or a named source to it** — the moment one carries a statistic it becomes a row like 36. | — |

## Fixes applied in this pass

**Batch 2 (2026-09-12, closed 2026-09-16) — four defects, all rank claims about a third party.**

1. **M4** — a superlative that *inverted* while the course sat still: the 2026 DBIR moved vulnerability exploitation past credentials and phishing into first place. Replaced with the human-element share, which carries the module's point without depending on a ranking.
2. **M28** — a rank name attached to the wrong platform, in four places including a quiz answer. The pedagogy also improved by being right: an HTB rank really is evidence of *current* practice, because it is computed from active content only.
3. **M20** — an unhedged "#1" where the platform's own data names a different bug. The neighbouring AppSec course makes the same claim *hedged* and is fine (AppSec row 36) — the defect is the certainty, not the topic.
4. **M25.5** — "one of the largest DDoS attacks ever seen" for an attack the record has since passed by more than 25×, plus a headline 1.2 Tbps figure the victim never confirmed. Rewritten to "measured up to that point", and the growth since is stated as a floor, because a floor on a monotonic record cannot rot. This is the fix pattern the batch is worth keeping: **when a superlative is time-bound, bind it in the sentence** rather than leaving the reader to date it.

Unlike Batch 1, **every Batch 2 defect is a fixed string**, so each now carries a
regression guard in `tools/guardrail.py` — `A44`, `A45`, `A46`, `A47`, `A48` here
and `A42`, `A43` in the AppSec course. Each guard was verified by running it
against the pre-fix file: all seven fire there and are clear on the fixed text.
A guard that has never been shown to fire is not a guard.

Closing the batch also meant clearing two rows Batch 1 had left `PENDING` (23,
26) and three this batch opened (40, 41, 42) — all five are now adjudicated, and the
gate warns on any `PENDING` row so a batch cannot be declared closed over one
again.

**Batch 1 (2026-09-11) — four defects,** all of the same family — a claim that was true when written and
quietly stopped being true, or was stated more strongly than the source supports:

1. **M28** — NICE Components v2.0.0 (March 2025) → **v2.2.0 (April 2026)**. Two releases stale.
2. **M6.5** — SP 800-88 **Rev 1** → **Rev 2**; Rev 1 has been withdrawn, so the course was citing a dead document. Added what Rev 2 changes.
3. **M6.5** — "CIS Controls v8.1 deliberately does not cover physical security — its scope note says so explicitly" → rewritten to the defensible version. No such scope note was found.
4. **M10** — HQC presented inside a list of finalized FIPS standards → now explicitly *selected, not yet standardized*.

None were reachable by the guardrail gate: every one of them is a
well-formed sentence pointing at a real standard.
