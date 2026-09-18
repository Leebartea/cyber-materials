# Cyber Guardians — claim ledger

Every rule-shaped assertion this course makes, with a status and the evidence
behind it. The guardrail gate (`tools/guardrail.py`) proves the course is
*structurally* sound — balanced fences, resolving cross-references, no dead
links. It cannot prove anything here is *true*. That is what this file is for.

- **Course file:** `cyber-guardians/cyber_guardians_app.html` (42 modules + 3 roadmaps)
- **Candidates extracted by:** `python3 tools/claims_extract.py guardians --json out.json`
- **Last pass:** 2026-09-18 (Batch 6 — law claims, closed: no `PENDING` rows remain)

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
| 7 | `default` — "by default", "defaults to" | 22 | vendor defaults change silently between versions — but they fail *visibly*, at a terminal, which is why `law` was promoted ahead of this |
| 8 | `attribution` — "according to", "researchers found" | 5 | each needs the **primary** document, not the report quoting it |

(`attack` — 73 candidates, 32 distinct ids — is **closed** in Batch 1, row 35.
`rank` — 182 candidates — is **closed** in Batch 2, rows 36–44.
`quantity` — 55 candidates — is **closed** in Batch 3, rows 45–58.
`port` — 51 candidates, 48 distinct — is **closed** in Batch 4, rows 59–63.
`date` — 34 candidates — is **closed** in Batch 5, rows 64–71.
`law` — 13 candidates — is **closed** in Batch 6, rows 72–77, **pulled forward**
from its scheduled slot at Batch 7; see that batch's opening for why.)

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

## Batch 3 — quantity claims

55 `quantity` candidates. The triage splits cleanly in two, and the split is
the batch's main finding. **Most of the class is not a claim at all:** 30 of the
55 are byte counts, buffer sizes and digests inside the course's own labs — `15
bytes, not 14`, `at most 63 bytes + NUL`, `64 bytes from 192.168.56.20`. Those
are `EXECUTED` arithmetic about code printed on the same screen; no external
lookup can confirm or refute them and none is owed. The remaining **14 rules
below all share one property: each names a third party** — a breach victim, a
regulator, a vendor's price list. That is the same line Batch 2 drew for
superlatives (row 44), arrived at independently from a different tag, which is
some evidence it is the right line.

| # | Module | Claim as taught | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 45 | M16.5 | SolarWinds Orion was "a product trusted by 18,000+ organizations" | `FIXED` | **A ceiling quoted as a count, with the bound inverted.** SolarWinds' own security advisory says "we've currently identified **less than 18,000** customers **potentially affected**" — so the `+` points the wrong way, and the figure counts *downloads of a trojanized build*, not victims. The company puts the number **actually compromised at fewer than 100**: SUNBURST slept up to two weeks, fingerprinted for sandboxes, and was activated selectively, so most recipients were never entered. Orion's total customer base is ~33,000, which is the number "trusted by" actually wanted. Rewritten to name the ceiling as a ceiling and state the <100 figure, because the 18,000-victim retelling overstates the breach by more than two orders of magnitude. | 2028-01 |
| 46 | M14 | The Equifax "settlement reached ~$700M" | `FIXED` | **The ceiling reported as the amount.** The FTC's own press release is titled *"Equifax to Pay $575 Million"*: the global FTC/CFPB/50-state settlement was **at least $575M**, of which $300M is the consumer fund, $175M to 48 states + DC + PR, and $100M a CFPB civil penalty. The **$700M is a conditional maximum** — Equifax adds up to $125M more only if the initial consumer fund proves insufficient. Same defect shape as row 45, found in the same pass: a range's upper end, stated as a fact. | 2028-01 |
| 47 | M28 | Cert roadmap prices: eJPT ~$200, PNPT ~$400, OSCP+ ~$1,649 | `FIXED` | **All three stale, all three low** — verified 2026-09-17: PNPT is **$499** direct from `certifications.tcm-sec.com/pnpt/` (voucher + free retake + 12 months of training); eJPT is **$249** standalone (INE's certification page no longer prints a price, so this rests on converging 2026-dated secondary sources, not the vendor — recorded as the weaker citation it is); OSCP+ standalone is **$1,699** (bundle $1,749, Learn One $2,749/yr, retake $249). Fix follows the row 42 pattern: the figures are kept but **date-bound in the sentence**, the vendor's checkout is named as the only authority, and the durable teaching point — a few hundred dollars vs a few thousand — is stated separately so the lesson survives the next price rise. | 2027-09 |
| 48 | M25.5 | Oldsmar: lye setpoint moved ~100 ppm → 11,100 ppm on 5 Feb 2021, via internet-reachable TeamViewer with a shared password | `SOURCED` | **Checked because it is the single most retold OT "attack" in any curriculum, and the course already handles it correctly** — in all three places it teaches both halves: the reported intrusion *and* that a four-month FBI investigation could not confirm one, that no perpetrator was identified, and that in 2023 former city manager Al Braithwaite said publicly there was no evidence of outside access and the change was most likely an employee mis-clicking. One wording note for the next pass, not worth a change now: the FBI's actual statement is narrower than the course's "could not confirm any intrusion" — Tampa Field Office said it "was not able to confirm that this incident was initiated by a **targeted cyber intrusion**". Two loose ends also stay open: Pinellas County Sheriff's Office still calls its case active, and Dragos reported a watering-hole site targeting Florida water utilities that was accessed from an Oldsmar browser the same day, never definitively linked. | 2028-01 |
| 49 | M11.7 | Ubiquiti BEC: 14 wire transfers over 17 days from a Hong Kong subsidiary totalling $46.7M; FBI told the CEO on 5 June 2015; $39.1M charge | `SOURCED` | every figure exact against the company's own SEC filings. 10-K FY2015: **$46.7M** transferred from the Hong Kong subsidiary; the initial spoofed email reached finance **19 May 2015**; **14 transfers over the next 17 days** to Russia, China, Hungary and Poland; **5 June 2015** the FBI's San Francisco office emailed CEO Robert Pera. **$8.1M recovered** by 30 June 2015 → a **$39.1M charge** in Q4 FY2015, with $6.8M under injunction and $31.8M still pursued. The course's "only a fraction was ever recovered" is exactly right at 17%. | 2028-01 |
| 50 | M23 | Maersk/NotPetya destroyed ~49,000 laptops and 4,000 servers, June 2017 | `SOURCED` | true, but the sentence **splices two different Maersk accounts** and it is worth knowing which is which. Chairman Jim Hagemann Snabe at Davos (Jan 2018): "4,000 new servers, **45,000** new PCs, 2,500 applications… over 10 days". CTIO Adam Banks (Gartner Risk Summit 2019): "all end-user devices, including **49,000 laptops**… were destroyed", all rebuilt by week four. So 49,000 (Banks, destroyed) and 4,000 (Snabe, reinstalled) are each sourced and not contradictory — they are simply from different tellings, which is why the two laptop figures differ by 4,000. Left as written, with the `~` doing the work. Damages $250–300M per Snabe. | 2028-01 |
| 51 | M25 | Capital One: SSRF → EC2 metadata → IAM role → ~100 million customer records from S3 | `SOURCED` | ~**100M in the US plus ~6M in Canada**, ~106M application records total; the course says "~100 million customer records", which is the US figure and the one usually quoted. Chain confirmed: SSRF in a ModSecurity WAF → IMDS → over-permissioned WAF role → S3. Access occurred 22–23 March 2019, undetected until a GitHub Gist tip on 19 July. AWS's answer was **IMDSv2** (session token via `PUT` + custom header), which is why most SSRF cannot reach metadata today — worth a sentence if M25 is ever expanded. | 2028-01 |
| 52 | M16 | Target: HVAC vendor Fazio Mechanical phished → vendor network → POS malware → 40 million payment cards | `SOURCED` | **40M** card accounts (27 Nov – 15 Dec 2013), plus **70M** customers' names/addresses — the course cites only the 40M card figure, which is the one its sentence is about. Fazio Mechanical (Sharpsburg, PA) credentials, stolen by phishing, first used **15 Nov 2013**. The course avoids the usual error here and should keep avoiding it: **the HVAC system itself was not hacked** — Fazio's access was for electronic billing, contract submission and project management, not remote climate control. | 2028-01 |
| 53 | M3 | LinkedIn 2012: ~6.5M unsalted SHA-1 hashes, ~90% cracked within days; a 2016 follow-up revealed the real scope was 117 million accounts | `SOURCED` | 6 June 2012, ~**6.5M** hashes posted; unsalted SHA-1 confirmed by LeakedSource's later analysis of the full set. **May 2016**: 117M account records surfaced for sale (the "Peace" dumps, alongside Myspace 360M and Tumblr 65M) and **LinkedIn confirmed** the expanded scope, forcing a second reset. The ~90% figure is the contemporaneous press consensus for the 6.5M subset rather than a single audited count — it is hedged with `~` and stays that way. | 2028-01 |
| 54 | M5 | Cambridge Analytica: data on 87 million users from ~270,000 quiz takers; FTC settlement $5 billion, then a record | `SOURCED` | **87M** is Facebook's own upper estimate; **~270,000** installed Kogan's *This Is Your Digital Life* (a few sources say ~305,000 — the course's `~` covers the spread). FTC penalty **$5B**, July 2019, a 3-2 vote, plus a 20-year order and an independent privacy committee. UK ICO fined **£500,000**, its statutory maximum — and specifically under the **Data Protection Act 1998**, because the conduct predated GDPR. The course already says exactly that, which is the part most retellings get wrong. | 2028-01 |
| 55 | M25.5 | Stuxnet physically destroyed ~1,000 centrifuges | `SOURCED` | the figure traces to one place: Albright, Brannan & Walrond, *Did Stuxnet Take Out 1,000 Centrifuges at the Natanz Enrichment Plant?* (ISIS, 22 Dec 2010), which **infers** ~1,000 IR-1s removed from IAEA data against ~10,000 installed. It is an estimate, not a confirmed count — Iran never published one — and later analysts have said ~2,000. The `~` is therefore load-bearing; keep it, and never write this number without it. | 2028-01 |
| 56 | M25.5 | Ukraine grid 2015/2016: blackouts affecting 230,000 customers, BlackEnergy and Industroyer | `SOURCED` | **23 Dec 2015**, three regional oblenergos, outages of 1–6 hours. Two figures circulate and both are defensible: **230,000** (the common count, and what the course uses) and **~225,000** (DHS/CISA alert IR-ALERT-H-16-056-01). Primary analysis is the E-ISAC/SANS report of 18 March 2016 (Lee, Assante, Conway): BlackEnergy 3 for access, operators' HMIs driven by hand, KillDisk to destroy evidence, and a telephone denial-of-service against the call centre. Industroyer belongs to **2016**, not 2015, and the course's next sentence already separates them correctly. | 2028-01 |
| 57 | M4 | Twitter 2020: vishing of employees, accounts of Obama/Biden/Musk/Apple/Uber hijacked, ~$118,000 stolen in minutes | `SOURCED` | Hillsborough County State Attorney Andrew Warren: **12.86 BTC from ~360 people, $117,440** at the time — "~$118,000" is that figure rounded and is how the state's own office stated it. 15 July 2020, 45 accounts posted. Graham Ivan Clark was **17 when charged**, arrested 31 July 2020, pleaded guilty to 30 felonies and took **3 years in a juvenile facility plus 3 years' probation** under Florida's Youthful Offender Act — so the course's "arrested within weeks and received real prison time" holds. | 2028-01 |
| 58 | M0.5, M1, M10, M12, M13, M15, M21, M22 | ~30 byte counts, buffer sizes, key lengths and digests inside the labs — `15 bytes, not 14`, `32 bytes from env`, `at most 63 bytes + NUL`, `buf is 16 bytes`, `the SHA-256 of those exact 50 bytes` | `EXECUTED` | **Deliberately not individual rows.** Each is arithmetic about code printed on the same screen, verifiable by running the lab and by no other means; there is no authority to cite and nothing to re-check. Recording them separately would pad the ledger while lowering its signal. The rule: a `quantity` is a claim only when it describes **something outside the course**. | — |

## Batch 4 — port and protocol assignments

51 `port` candidates, 48 distinct. The batch was expected to be the dull one —
"mostly IANA-settleable, low risk, high volume" is what the Batch 1 table
predicted — and the prediction was wrong in an instructive way.

**41 of the 48 are not assignments at all.** They are scan output, `tcpdump`
filters, ephemeral source ports in synthetic log lines, and tunnel examples:
`22/tcp open ssh`, `sudo tcpdump -i lo0 -A 'tcp port 8080'`, `from 203.0.113.44
port 51222`. Those are `EXECUTED` — the port number is an input to a command
printed on the same screen, and no registry can confirm or refute it. The 7 rules
below are the ones that assert something about the **world**: what a number is
named, who named it, and whether a name means anything.

**The finding: a port name is three different facts wearing one label.** IANA's
registry, the OS's `/etc/services`, and nmap's `nmap-services` are three separate
tables maintained by three separate parties, and they disagree — routinely, not
exceptionally. The course had already reached the right *conclusion* ("that tells
you nothing") while citing the wrong *table*, which is the most dangerous shape a
claim can have: correct advice resting on a checkable falsehood, so the reader
who verifies it loses trust in the advice.

| # | Where | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 59 | M12 | Port 31337 is named "Elite" in `/etc/services` | `FIXED` | **wrong table, and the right answer is better teaching.** `Elite` is nmap's name, from `nmap-services` (verified by execution: `grep -w 31337/tcp /opt/homebrew/share/nmap/nmap-services` → `Elite 31337/tcp 0.000163`, nmap 7.99). macOS `/etc/services` has **no 31337 entry** (`grep 31337 /etc/services` → rc=1, 13,926 lines). IANA's registry assigns 31337/tcp+udp to **`eldim`** ("a secure file upload proxy") — confirmed in the 15,404-line CSV at `iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv`. nmap's own comment on the line *names eldim*, so nmap knows it is overriding IANA. Rewritten so the three-way disagreement is the lesson, with both verification commands printed for the reader | 2027-09 |
| 60 | M9, M12, M15, M17 | Scan-output service names: `3000/tcp ppp`, `9929/tcp nping-echo`, `8080/tcp http`, `5432/tcp postgresql`, `3306/tcp mysql`, `22/tcp ssh`, `80/tcp http` | `EXECUTED` | all match `nmap-services` as shipped in nmap 7.99, which is what produces these columns. Two diverge from IANA and **that divergence is correct output, not a defect**: 3000/tcp is `ppp` to nmap but `hbci`/`remoteware-cl` to IANA; 8080/tcp is `http-proxy` to nmap but `http-alt` to IANA. M17's `8080/tcp open http Jetty` is `-sV` output, where probe-derived service identity overrides the table — also correct | 2027-09 |
| 61 | M0.5, M2, M13, M25.5 | Well-known assignments the course teaches as fact: 80 HTTP, 443 HTTPS/TLS, 22 SSH, 23 Telnet, 445 SMB, 1900 SSDP/UPnP, 3306 MySQL, 5432 PostgreSQL | `SOURCED` | all confirmed against the IANA CSV above: `http,80,tcp`; `https,443,tcp,http protocol over TLS/SSL`; `ssh,22,tcp` [RFC4251]; `telnet,23,tcp` [RFC854]; `microsoft-ds,445,tcp`; `ssdp,1900,udp`; `mysql,3306,tcp`; `postgresql,5432,tcp`. The course calls 1900 "UPnP", IANA calls it SSDP — SSDP is the discovery protocol UPnP uses on that port, so the course's usage is the common one and is not a defect | 2027-09 |
| 62 | M25.5 | Mirai scanned "Telnet on port 23" using "60 known default username/password pairs" | `FIXED` | two drifts in one sentence. The credential table held **62** pairs, with **ten** tried per host — the figure consistently reported from the released source and the USENIX Security '17 analysis *Understanding the Mirai Botnet* (Antonakakis et al., pp. 1093–1110). And Mirai scanned telnet on **23 and 2323**; a defence paragraph that says "firewall management ports" while naming only 23 leaves the port people actually forget. Both corrected, and the module's own scan lab updated to `-p 23,2323` so the lab and the prose agree | 2027-09 |
| 63 | M6, M12 | Binding a port below 1024 requires privilege; there are only 65,535 ports, so a "secret" high port is not a secret | `CORPUS` | both hold as taught. The privileged-port boundary is real on macOS and Linux (the course already names the standard escapes — bind-then-drop, or let nginx/systemd hold the port), and 65,535 is simply the 16-bit range. The M12 example port **47821 is genuinely unassigned** — absent from the IANA CSV and `unknown` in `nmap-services` — so the "nobody will guess it" scenario is not accidentally naming a registered service | 2029-09 |

## Batch 5 — date claims

34 `date` candidates. The tag was predicted to "rot by definition" and it does,
but not in the way the prediction implied. **A stale date is rarely the defect.**
Almost every year in this course is a *historical anchor* — Morris in 1988, WEP
broken in 2001, Stuxnet found in 2010, Maersk in June 2017 — and a historical
anchor cannot rot; it is either right or it was always wrong, and all of them are
right (row 69).

The five defects are all the other shape: **a date attached to a moving
measurement.** A dwell-time median, a phishing click rate, a software licence, a
loss figure quoted in the wrong currency. The `date` regex found them because
the sentence said "in 2024" — but what had gone stale was never the year, it was
the number sitting next to it, and in two cases the underlying *trend had
reversed* while the course stood still. That is the same defect Batch 2 found in
the `rank` class (row 36), which suggests the two tags are pointing at one
failure mode from different angles: **a claim that names a year is usually a
claim about a series, and a series has a direction.**

| # | Where | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 64 | M25.5 | Mirai tried "~60 default username/password pairs" — **a third instance Batch 4 missed** | `FIXED` | **The batch's most uncomfortable finding: the previous pass's own guard was written too narrow to catch its own defect.** Batch 4 (row 62) corrected Mirai's credential table from 60 to **62** pairs in two places and wrote guard `A56` as the literal string `60 known default username/password pairs` — the exact wording of the sentence it had just fixed. A **third** instance in the same module, worded `~60 **default username/password pairs**`, was never touched, and the gate scored green over it for a full pass. Fixed here to 62 pairs / ten per host, and the same sentence also gained the `23 and 2323` correction it had missed. `A56` is **widened** to `~?60[^\n]{0,24}default username/password pairs`, which fires on both wordings | 2027-09 |
| 65 | M18.5 | "In 2023-2024 data, the median global dwell time was 10 days, down from 16 the previous year, but for internally detected breaches it stretched much longer" | `FIXED` | **Two errors in one sentence, and the second is the worse one.** (1) *Stale, and the trend has since reversed.* 10 days is Mandiant's **2023** figure (M-Trends 2024), correctly paired with 16 for 2022 — but the series continued **11 days (2024)** and **14 days (2025)**, published in M-Trends 2026 from 500,000+ hours of investigations. The decade-long decline the sentence was teaching **ended and turned**, driven by long-running espionage and DPRK IT-worker intrusions at a 122-day median. (2) *Inverted.* Internally detected breaches have the **shortest** dwell time — **9 days** — and externally notified ones the longest at **25**; the whole 2025 rise came from the external bucket. The course had the split exactly backwards while using it to make a point about detection maturity. Rewritten with the full series, each figure year-bound, and the split stated in the right direction | 2027-04 |
| 66 | M24.5 | "In 2024, Wombat/Proofpoint reported that AI-generated phishing had a click rate 70%+ higher than manually written campaigns" | `FIXED` | **A statistic attributed to a report that does not exist, stating a result the 2024 evidence contradicted.** Wombat Security was absorbed into Proofpoint in 2018 and the brand retired; Proofpoint's *State of the Phish* carries no AI-vs-human click-rate comparison, and no "70%" figure traces anywhere. Worse, through 2024 the measurements ran the **other way**: IBM X-Force Red (2023) got **14%** for a human phish against **11%** for AI, and Hoxhunt's running comparison had AI still **10% behind** elite red teams in November 2024, only crossing over to **+24%** in March 2025. The sourceable modern figure is **Microsoft's Digital Defense Report 2025 — 54% click rate on AI-crafted lures vs 12% manually written**. Rewritten to give the crossover as a dated sequence, name both real sources, and state the durable point separately: the grammar-and-greeting tells have stopped being evidence, whatever the percentage | 2027-10 |
| 67 | M24.5 | The Arup deepfake fraud "cost £25M" (case-study title, workbench goal, workbench answer) | `FIXED` | **A currency conversion that never happened.** The loss was **HK$200 million ≈ US$25.6M** — 15 transfers across five Hong Kong accounts, January 2024, reported by Hong Kong police in February and tied to Arup by CNN in May. Three of the four passages wrote the US-dollar magnitude with a **pound** sign, which re-labels the figure and overstates it by about a quarter (HK$200M is roughly £20M). The one passage that was right — the case-study `body` — already said `HK$200M (approximately US$25.6M)`, so the course **contradicted itself across four passages about the same incident**. All now give HK$200M with the USD equivalent, and the answer carries a note to write the figure in the currency it was reported in. Guard `A62` bans a bare `£25M` outright | 2028-01 |
| 68 | ★ Intro | VM setup table: VMware Fusion/Workstation are "free — personal use" (3 rows) | `FIXED` | **A licence claim that expanded under the course.** Broadcom made Workstation Pro and Fusion Pro free for *personal* use in May 2024 — which is what the table recorded — and then on **11 November 2024** removed the restriction entirely: commercial, educational and personal use are all free, and the paid Pro editions **are no longer sold at all**. The stale version is not merely out of date, it tells a learner planning to use the course at work that they need a purchase they cannot make. Corrected in all three rows, with the version floor that actually gates it (**Workstation 17.5.2 / Fusion 13.5.2**), and a note on why the wording matters. Same family as row 47's exam prices: a vendor fact the course cannot control, so it is now **date-bound in the sentence** | 2027-11 |
| 69 | M13.5, M18.5, M21, M22, M23.5, M24, M16.5 | Historical anchors: WEP broken **2001**; ATT&CK begun by MITRE in **2013**; Morris worm **Nov 1988** and the `gets()`/`fingerd` overflow; "true in **1996**" (Aleph One, *Smashing the Stack*, Phrack 49); BTK taunting police "for 30 years"; Code Spaces' AWS console ransom **June 2014**; Stuxnet discovered **2010**; Zero Trust "died at SolarWinds… since 2020" | `SOURCED` | all confirmed, none can rot. WEP's break is the Fluhrer–Mantin–Shamir attack of 2001; ATT&CK started in 2013 as the FMX project and went public in 2015, so "built… starting in 2013" is right; Morris was released 2 Nov 1988 by a Cornell graduate student and `fingerd`'s `gets()` was one of its vectors; Aleph One's paper is Phrack 49 (Nov 1996), which is the naïve-overwrite era the module contrasts with PAC/ASLR/DEP. BTK: first murders Jan 1974, arrested 25 Feb 2005 on floppy-disk metadata — 31 years, so "30 years" is the correct round number and the `for` is doing the hedging. **The rule this row sets: a date that fixes an event in the past is not a rot risk and does not need a re-check column.** Only dates attached to a measurement do | — |
| 70 | M28, M25.5, M24.5 | Relative-present dates: "a path that actually works **in 2025**"; "a router bought in 2015 still listening in **2025**"; "which in **2024** most organisations had not yet implemented" | `CONVENTION` | terminal, and the finding is that **these are the only `date` claims with no correct form.** Each names the year the sentence was *written* as though it were the year it is *read*; none is checkable, because no authority publishes "what works for a career-changer this year". They are kept because the alternative — deleting the year — makes them vaguer, not truer. The rule: a relative-present date is a **timestamp on the author, not a claim about the world**, and must never be given a statistic to carry. The moment one does, it becomes row 66 | — |
| 71 | — | The 14 `date` candidates already adjudicated in Batches 1–4 | `CORPUS` | **Do not re-derive these.** CSF 2.0 released Feb 2024 (row 1); SP 800-63B-4 July 2025 (5); HQC selected March 2025 (19); SP 800-207 published 2020 (20); NICE Components v2.2.0 April 2026 (25); LinkedIn 2012 (53); Ubiquiti May 2015 (49); SolarWinds 2020 (45); Maersk June 2017 (50); Oldsmar Feb 2021 and the 2023 retraction (48); Twitter July 2020 (57); Mirai 2016 and the 30 Tbps floor (42, 62); the OWASP 2025 refresh (14–17); the Agentic Top 10 of Dec 2025 (AppSec ledger row 24). Listed here only so a later pass grepping for `date` can see they are closed rather than untouched | — |

## Batch 6 — law and regulatory claims

**Pulled forward out of turn.** The Batch 1 table scheduled `default` (22
candidates) as Batch 6 and `law` (13) as Batch 7. `law` was promoted because it
is the only tag in either ledger with **no cheap-dismissal rule**. Every other
class has one: a `port` that is a scan fixture is `EXECUTED` on sight, a `rank`
about the reader's own likely mistake is dismissed by row 44, a `date` that fixes
a past event cannot rot (row 69). There is no equivalent move for a statute. A
legal claim is either checked against the instrument or it is unadjudicated, and
13 candidates is the smallest this class will ever be — so the cheapest moment to
read it carefully is now, while it is small, rather than after the OSINT and
forensics work adds more. `default` moves to Batch 7 and loses nothing by waiting;
a vendor default that drifts fails visibly, at a terminal, in front of the learner.

**All 13 are real claims.** Unlike `port` or `quantity`, a law cannot be mentioned
incidentally — you do not write "GDPR" as a fixture. They collapse to the 6 rules
below, and **five of the six needed work**, the highest defect density of any
batch in either ledger.

**The finding: the errors cluster in the *scope* of a law, never its headline
number.** Every deadline in this course was already right — GDPR's 72 hours, and
the M23 sentence that names PCI/DORA/HIPAA as running "their own" clocks, which
is precisely the hedge that stopped this course from acquiring the fabricated
"HIPAA 72-hour rule" the AppSec course did (AppSec row 52). What was wrong was
always the sentence *around* the number: **who** a law reaches (row 72), **which**
rights it grants (73), **when** it starts applying (74), and **whether** an act is
actually the offence the course says it is (75). That is a more dangerous shape
than a wrong number, because a wrong deadline is falsifiable in one search
whereas a wrong scope reads as fluent background and is repeated by the learner
as settled fact. The rule this batch sets: **a legal claim's verb is the risky
part, not its figure** — "covers", "grants", "applies from", "is unauthorized
access" each smuggle a scope decision that the instrument itself states narrowly.

| # | Where | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 72 | M5 | **GDPR** "covers personal data of EU residents regardless of where the company is based"; "fines up to **4% of global annual turnover**" | `FIXED` | **the same defect the AppSec course was fixed for in Batch 5, sitting in this course untouched — and a guard written that pass should have caught it.** See the meta-finding below; the substance is AppSec row 55's. Art. 3(1) covers a controller **established in the Union** for everything it processes anywhere; Art. 3(2) reaches a non-EU controller only where processing relates to **offering goods or services to** data subjects "**who are in the Union**", or **monitoring their behaviour** there. It is a *location* test applied per processing activity, and the EDPB's Guidelines 3/2018 state that the targeting criterion "is not limited by the citizenship, residence or other type of legal status" of the data subject — so an American tourist in Berlin can be in scope and an EU citizen living in Toronto is not. "Regardless of where the company is based" states the conclusion while deleting the condition that produces it. Separately, the fine ceiling was given as the percentage alone: Art. 83(5) is **€20 000 000 or 4% of total worldwide annual turnover, whichever is higher**, and for a small company the €20M is the binding figure — quoting only the percentage makes the ceiling sound proportional to size, which is the opposite of the article's design. Both halves rewritten, with the two Art. 3 doors named separately. Guards `A67` (widened), `A76` | 2028-09 |
| 73 | M5 | **CCPA/CPRA** "grants California consumers rights to know, delete, and opt out of the sale of their data" | `FIXED` | a 2018 rights list flying a 2023 name. The bullet says "CCPA/**CPRA**" and then enumerates only the rights the original CCPA granted. CPRA took effect **1 January 2023** and added the right to **correct** inaccurate personal information and the right to **limit** the use and disclosure of *sensitive* personal information, and extended the opt-out from "sale" to "**sale or sharing**" (California Privacy Protection Agency, consumer-rights FAQ, read this pass — the agency lists six rights: know, delete, correct, opt out, limit, and non-discrimination). "Sharing" is a term of art meaning disclosure for cross-context behavioural advertising, and it exists precisely because companies argued ad-targeting was not a "sale" — so a list that stops at "sale" reproduces the loophole CPRA was written to close. Rewritten with all of them, the 2023 date attached, and the sale-vs-sharing distinction explained rather than listed. Guard `A75` | 2028-01 |
| 74 | M5, M23 | The **EU Cyber Resilience Act** "gives you **24 hours** to report an actively-exploited vulnerability … (applies from 11 Sep 2026)", in two modules | `FIXED` | **stale by six days at the moment of the pass, and incomplete in the same breath.** The manufacturer reporting obligations **came into force on 11 September 2026** — this pass ran on 18 September — so a parenthetical written as a forward-looking heads-up now misdescribes live law, and a learner reading "applies from" as "not yet" would be wrong about their own employer's duty. The deadline was also one third of the obligation: Art. 14 runs a **24 / 72 / 14** staircase — early warning within 24h of awareness, fuller notification within 72h, final report within 14 days of a corrective measure being available — all to the coordinating CSIRT and ENISA through the single reporting platform, which then shares it with the CSIRTs of every member state where the product was made available (European Commission, *CRA reporting obligations*, `digital-strategy.ec.europa.eu/en/policies/cra-reporting`, read this pass; obligations for open-source stewards start 11 Dec 2027, with the rest of the regulation). Corrected in both modules, with the operational point the staircase exists to make: the 24h item is **not** an investigation report and the CRA expressly permits progressive disclosure, so the skill is making a defensible early call while forensics are still moving. The AppSec course carried the identical pair of errors and was fixed in the same pass (AppSec row 66). **This is the first row in either ledger to rot between batches rather than between passes** — Batch 5 closed on 2026-09-17 and this sentence was correct then | 2027-12 |
| 75 | M15 | "Against a public site the same packets are **unauthorized access under the CFAA**, the UK Computer Misuse Act, and equivalents worldwide" | `FIXED` | **right advice, overclaimed authority — the Batch 4 shape (row 59), now in its most consequential form.** The module's conclusion is correct and nothing about it changed: do not point these tools at machines you do not own. But the sentence asserts a settled criminal characterisation for "the same packets", and those packets include the module's own Nmap scan, for which the law is genuinely unsettled *and differs by jurisdiction*. **US:** the only real authority on scanning is *Moulton v. VC3*, No. 1:00-CV-434-TWT (N.D. Ga. 2000), which rejected a CFAA claim on two grounds — the scan caused no "damage", the court holding that damage "must be an impairment to the integrity and availability of the network", and it "did not grant … access". That is one district-court decision, fact-bound, and it leaves fifty state computer-crime statutes with broader definitions of "access" untouched. **UK:** the opposite result on far less conduct — in *R v Cuthbert* (2005) a security consultant who typed `../../../` into the address bar of a tsunami-appeal donation site was convicted under **s.1** despite causing no harm (BT confirmed its Solaris server was unaffected) and despite the Crown accepting he had no malicious motive, because s.1 has no damage threshold and asks only whether he *intended* to secure access he was not authorised to have; he was fined £400 plus £600 costs and lost his job. Rewritten to give both cases and to state the real lesson, which is **sharper than the blanket it replaces**: your exposure for an identical packet depends on which country's server answered, and you cannot find out which rule applies until after you have sent it — so authorization is the only thing that removes the question. Guard `A73` | 2028-09 |
| 76 | M11.7, M15 | "Reading a public record is lawful. **Access without authorisation is not.** That is the line the US **CFAA** and the UK **Computer Misuse Act 1990 (s.1)** actually draw" | `SOURCED` | correct, and **strengthened rather than corrected** — the one law row that needed no repair. CMA 1990 s.1 is indeed "Unauthorised access to computer material", and its elements are causing a computer to perform a function with intent to secure unauthorised access, plus knowledge that the access is unauthorised — which is why the module's "'the data was public' is not a defence" holds. On the US side the line the sentence describes was confirmed by the Supreme Court after the module was written: *Van Buren v. United States*, 593 U.S. 374 (2021), decided 3 June 2021 6–3 per Barrett J., held that a police sergeant who ran a licence-plate lookup he was authorised to run, in exchange for a bribe, did **not** "exceed authorized access" — the statute poses a "gates-up-or-down" question about whether information was off-limits to you, not whether your purpose was proper. That is the module's line exactly, and it is now cited there, with a pointer to row 75 noting that the same clarity does not extend to *scanning*. Note the asymmetry this creates and keep it: **M11.7 states the rule carefully and M15 stated it as a blanket**, and the course now uses the pair as a teaching contrast rather than contradicting itself across two modules | 2029-06 |
| 77 | M5, M21, M23, M24.5, M28, M11.7 | The remaining law mentions: GDPR 72 hours; HIPAA scope; PCI DSS 4.0.1 as contractual not statutory; SOC 2 as an audit report not a law; Morris as the first CFAA conviction; the Cambridge Analytica fines; pasting regulated data into a public AI service as a possible GDPR/HIPAA violation; ToS breach as civil not criminal; GDPR applying to public personal data on an OSINT engagement | `SOURCED` `CORPUS` | **all correct as written; one enriched.** GDPR's 72 hours is Art. 33(1), stated to the supervisory authority — correct in both modules, and M23's "PCI, DORA, and HIPAA each run their own" is the hedge that kept this course clear of the fabricated "HIPAA 72-hour rule" found in the AppSec course (AppSec row 52); do not let a later edit "helpfully" fill in that number. HIPAA covering "hospitals, insurers, and their vendors" is covered entities plus business associates — right. PCI DSS as contractual and SOC 2 as an audit report are both correctly *excluded* from being laws, which is the distinction most compliance summaries blur. Morris: convicted January 1990, the first conviction under the CFAA of 1986 — right. M24.5's data rule is correctly hedged with "**can** itself be a compliance violation", which is the accurate modal: disclosing PHI to a vendor without a BAA, or personal data without an Art. 28 processor agreement, is a violation independent of misuse. M11.7's "ToS breach is not in itself a crime" is right and is the line *Van Buren* reinforces. **Enriched, not fixed:** the Cambridge Analytica case study said "the UK ICO and US FTC both fined Facebook (the FTC settlement alone was $5 billion)" — true, but it gave no figure for the ICO, leaving the "predates GDPR" clause as an unbacked assertion. The ICO's penalty was **£500,000**, settled in October 2019 with no admission of liability, and that number is **the statutory maximum available under the Data Protection Act 1998** — the conduct predated GDPR's 25 May 2018 application, so the regulator was capped regardless of what it found. Added, with the point it unlocks: an old fine quoted as evidence that a regulator was toothless is often evidence that the regulator was capped | 2028-09 |

## Fixes applied in this pass

**Batch 6 (2026-09-18) — five defects in six rules, the highest density of any batch.**

1. **M5** — GDPR scope given as "**EU residents** regardless of where the company
   is based". Art. 3 is a *location* test plus, for non-EU controllers, a
   targeting or monitoring condition. Rewritten with both doors named.
2. **M5** — GDPR fines given as "4% of global annual turnover", omitting the
   "**€20 million or** … whichever is higher" half that binds a small company.
3. **M5** — CCPA/**CPRA** named while listing only the 2018 CCPA rights. Added
   correct, limit-sensitive-PI, and opt-out of sale **or sharing**, effective
   2023-01-01.
4. **M5, M23** — the CRA reported as "24 hours (applies from 11 Sep 2026)". It is
   **24 / 72 / 14** and it has been in force since 11 Sep 2026 — stale by six days
   at the moment of this pass.
5. **M15** — "the same packets are unauthorized access under the CFAA" stated as
   settled law. Replaced with *Moulton* (US, 2000) and *Cuthbert* (UK, 2005) and
   the lesson that the answer differs by jurisdiction and cannot be known in
   advance. **M11.7** gained *Van Buren* (2021) as the authority for the careful
   version of the same line.
6. **M5** — Cambridge Analytica: added the ICO's £500,000 and that it was the DPA
   1998 statutory maximum, which is what makes the "predates GDPR" clause mean
   something.

**The meta-finding: a guard from the previous batch was live over this file and
scored green on the defect it was written for.** Batch 5 fixed the GDPR
territorial-scope error in the AppSec course and wrote guard `A67` from that
course's wording — `personal data of EU residents, regardless of where`. This
course carried the same error with **no comma**, and `check_banned` runs over
every course in `COURSES`, so the guard was aimed at this file for a full pass and
missed by one character. `A67` is now `EU (?:residents|citizens),? regardless of
where`.

This is the **second** time a batch has caught a guard cut to the exact shape of
the single sentence it was born from — `A56` was the first (row 64), and that one
missed a sibling instance in the *same* module. Two incidents, one mechanism, so
it is now a rule rather than an anecdote: **a guard must be tested against the
text it was written from *and* against the sibling course before the pass closes.**
A defect worth guarding in one course is, in a two-course repository built by one
author, usually present in both. Every guard added this pass was checked in both
directions — it fires on the pre-fix wording and is clear on the post-fix
wording — and that check is now part of the batch procedure rather than a thing
that happened to be done.

**Batch 5 (2026-09-17) — five defects, and one of them is a hole in the previous pass's gate.**

1. **M25.5** — a **third** "~60 default username/password pairs" that Batch 4 never
   saw, because Batch 4 wrote its regression guard from the exact wording of the
   sentence it had just fixed. The guard was green, the defect was live, and the
   two facts were consistent with each other for a full pass.
2. **M18.5** — Mandiant dwell time given as 10 days "down from 16", two editions
   stale and describing a decline that has since **reversed** (11 in 2024, 14 in
   2025) — plus the internal/external detection split stated **backwards**.
3. **M24.5** — an AI-phishing click rate attributed to a **report that does not
   exist** (`Wombat/Proofpoint`), asserting for 2024 a result that 2024's actual
   measurements contradicted.
4. **M24.5** — the Arup loss written as **£25M** in three passages while a fourth
   passage in the same module correctly said HK$200M ≈ US$25.6M.
5. **★ Intro** — VMware "free for personal use", a restriction Broadcom deleted on
   11 Nov 2024, in a setup table a learner acts on before anything else.

**The shape worth carrying forward: a guard written from the fix is not a guard
against the defect.** Row 64 is the first time this ledger's own machinery failed
rather than the course. `A56` was negative-tested in Batch 4 and it *did* fire —
on the one sentence it was copied from. Testing a guard against the file you just
edited proves only that the guard matches your edit. **The test that matters is
whether the pattern describes the error or the instance**, and the cheap way to
force that question is to write the pattern before looking at how the sentence
happens to be worded, then grep the whole course for near-misses. Every Batch 5
guard was written that way, and `A56` is widened accordingly.

The second finding is a triage rule, and it is the inverse of the ones Batches 3
and 4 produced. Those found that most candidates in their class were not claims
at all. Here, most candidates *are* claims — but **the claim is almost never the
date** (rows 69, 70). A year pinned to a past event is inert. A year pinned to a
measurement is a claim about a **series**, and a series has a direction that can
reverse without any of its published numbers becoming wrong. Rows 65 and 66 are
both that: no figure in either sentence was ever false, and both sentences taught
the opposite of what is now true.

All five defects are fixed strings, so all five carry guards — `A59`–`A63`, plus
the widened `A56`. Each was verified firing against the pre-fix file and clear on
the fixed one.

**Batch 4 (2026-09-17) — two defects, both "right conclusion, wrong authority".**

1. **M12** — "port 31337 is *named* `Elite` in `/etc/services`". It is named that
   in **nmap's** table; `/etc/services` has no such entry and IANA assigns the port
   to `eldim`. The conclusion the sentence was supporting ("that tells you
   nothing") was already correct — so the fix strengthens it: the course now
   names all three tables, shows they disagree, and prints the two commands that
   prove it.
2. **M25.5** — Mirai's credential table given as **60** pairs (it is **62**, ten
   tried per host) and its telnet scanning given as port **23** alone (it also
   scanned **2323**). The second half mattered more than the first: the module's
   defence advice said "firewall management ports" while naming only one of them,
   and the module's own lab scanned only `-p 23`. Prose and lab now both say
   `23,2323`.

**The shape worth carrying forward: correct advice resting on a false citation.**
Neither defect changed what the reader should *do*. Both would have been caught
by the first reader who ran the check the sentence invited — and that reader
would then have had good reason to doubt the surrounding, correct, material. A
claim in a teaching text is load-bearing even when the conclusion above it is
sound; **verifiability is the product, not just accuracy.** When a row asserts
that a name lives in a named file, the row must record *which* file was read.

The second finding is a triage rule, matching Batch 3's: **most `port` candidates
are not claims.** 41 of 48 were command inputs and scan output — `EXECUTED`, with
no registry to cite (row 60). A port number is only checkable when the sentence
asserts what it is *called* or what it is *for*, not when it is an argument.

Both defects are fixed strings, so both carry guards — `A55` and `A56` — each
negative-tested in both directions. `A55` needed two repairs before it fired:
the course writes `*named*`, so the closing asterisk abuts the word, and the
escaped backtick (`\``) sits between "in" and the path. The first draft matched
nothing and would have scored green forever, which is precisely the dead-guard
failure this table exists to prevent.

**Batch 3 (2026-09-17) — three defects, and two of them are the same bug.**

1. **M16.5** — SolarWinds "trusted by **18,000+** organizations". The vendor's own
   number is *fewer than* 18,000 **potentially affected**, and it counts downloads
   of a trojanized build; **fewer than 100** customers were actually compromised.
2. **M14** — the Equifax "settlement **reached** ~$700M". It was **at least $575M**;
   $700M is a conditional ceiling that applies only if the consumer fund runs short.
3. **M28** — three vendor exam prices, every one stale and every one low: eJPT
   $200→**$249**, PNPT $400→**$499**, OSCP+ $1,649→**$1,699**. Fixed the row 42 way:
   figures kept but **date-bound in the sentence**, the vendor's checkout named as
   the only authority, and the durable point (hundreds vs thousands) stated
   separately so it survives the next rise.

**The shape worth carrying forward: a ceiling quoted as a count.** Rows 45 and 46
are the same defect on unrelated subjects, found in the same pass — a published
range's *upper* bound repeated as though it were the measured value, in one case
with a `+` appended that reverses the bound's direction. A number that arrives
with "up to", "fewer than", or "as many as" attached is not the same number once
those words are dropped, and the drop is invisible at the sentence level. When a
`quantity` row cites a bound, **the row must record which end of the range it is.**

The second finding is a triage rule rather than a defect: **most `quantity`
candidates are not claims.** 30 of 55 were byte counts inside the course's own
labs — `EXECUTED` arithmetic with no authority to cite. A quantity is only
checkable when it describes something **outside** the course (row 58). That is
the same boundary Batch 2 found for superlatives (row 44), reached from a
different tag, which is mild evidence it generalises.

All three defects are fixed strings, so all three carry guards — `A49`, `A50`,
`A51` — each verified firing against the pre-fix file and clear against the fixed
one.

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
