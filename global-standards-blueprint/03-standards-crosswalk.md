# 03 · Standards & Certification Crosswalk

This is the gap-finding matrix. For each standard/framework/cert, it names the module(s) that
currently cover it (by exact `id` — the ids you'll edit in the `*_app.html` files), gives a
coverage verdict, and points to the finding that closes any gap.

**Verdict key**
- **Meets** — coverage is at or above what the standard/cert would expect of a graduate.
- **Partial** — the concept exists but is thinner than the standard treats it, is cited without
  the standard's name/version, or lives in the wrong course only.
- **Gap** — nothing meaningful exists in either course.

**Finding pointers** — `AS-n` = finding in `01-appsec-fullstack-gaps.md`; `CG-n` = finding in
`02-cyber-guardians-gaps.md`. "—" means no action needed.

**Course id key** — `AS` = Full-Stack AppSec (`full_stack_appsec_app.html`); `CG` = Cyber
Guardians (`cyber_guardians_app.html`).

All version/date facts below were web-verified July 2026; sources are listed at the bottom.

---

## Web / App / API security

| Standard (current version, date) | AppSec coverage | Guardians coverage | Verdict | Finding |
|---|---|---|---|---|
| **OWASP Top 10 — Web, 2025 edition** (final, Nov 2025) | `m4_1`, `m4_2`, `m4_3` + threaded throughout — but mapped to the **2021** category set/numbering | `m14` — mapped to **2021** (`A01…A10` 2021 table, "OWASP Top 10 (2021)") | **Partial (Stale)** — both courses teach the 2021 list; 2025 reshuffled and added two new categories | AS-1, CG-1 |
| **OWASP API Security Top 10 — 2023 edition** | `m3_3` (IDOR/BOLA, mass assignment, GraphQL) | `m20` (BOLA/IDOR case study) | **Meets** (AS) / **Partial** (CG) | AS-9 (nice-to-have: name BOPLA/2023 explicitly) |
| **OWASP Top 10 for LLM Applications — 2025** | `m7_5_1`…`m7_5_6` (whole Phase 7.5) | `m24_5` (AI attacks/defenses) | **Meets** (AS) / **Partial** (CG) | AS-8 (add agentic/MCP), CG-9 |
| **OWASP Top 10 for Agentic Applications (Dec 2025) + MCP Top 10** | none — LLM phase predates agentic list | none | **Gap** | AS-8 |
| **OWASP ASVS 5.0.0** (30 May 2025, 14 chapters, L1–L3) | none — ASVS never named; content informally aligns | none | **Gap** — no verification-standard framing anywhere | AS-2 |
| **OWASP MASVS 2.1.0 / MASTG** (18 Jan 2024) | none (out of AppSec's web scope) | `m25` (mobile security, general) | **Partial** (CG) / N/A (AS) | CG-8 (nice-to-have) |
| **OWASP SAMM 2.0** (maturity model) | `m7_1` teaches shift-left/SDLC but not SAMM/maturity levels | none | **Partial** | AS-5 (fold into SSDF finding) |
| **OWASP Cheat Sheet Series / Testing Guide (WSTG)** | Heavily reflected (XSS, CSRF, CORS, upload, JWT, session cheat sheets all mirrored) | Reflected in `m14`, `m20` | **Meets** | — |

## Governance / risk / architecture

| Standard (current version, date) | AppSec coverage | Guardians coverage | Verdict | Finding |
|---|---|---|---|---|
| **NIST CSF 2.0** (26 Feb 2024; adds **Govern** function) | none by name | none by name — no Identify/Protect/Detect/Respond/Recover spine | **Gap** — the single most-cited global governance framework is absent | CG-2 |
| **NIST SP 800-53 Rev 5** (control catalog) | none | none | **Gap** (breadth only) | CG-2 (mention) |
| **NIST SP 800-63B-4** (digital identity/auth, 31 Jul 2025) | `m6_1`, `m6_2`, `m6_6` — technically aligned (Argon2id, passkeys) but **never cites 800-63B**; missing the 15-char single-factor minimum framing | `m3` (passwords/MFA) — no 800-63 citation | **Partial** — strong practice, missing the standard's name + a couple of current rules | AS-3, CG-6 |
| **NIST SP 800-218 (SSDF v1.1)** (secure software dev framework) | `m7_1` teaches secure SDLC/shift-left but not SSDF/PW-PS-PO tasks | none | **Partial** | AS-5 |
| **NIST NICE Workforce Framework, Components v2.0.0** (5 Mar 2025; SP 800-181r1) | `m_intro`/career framing only | `m28` Career Pathways — strong cert map, **no NICE work-role/competency mapping** | **Partial** | CG-3 |
| **ISO/IEC 27001:2022 / 27002:2022** (ISMS; 2013→2022 transition closed 31 Oct 2025) | `m7_3` names SOC 2/GDPR/PCI/HIPAA, not ISO 27001 | one passing mention | **Partial/Gap** | CG-4, AS-7 (mention) |
| **ISO/IEC 27017 / 27018** (cloud / PII in cloud) | none | none | **Gap** (breadth) | AS-7 (mention) |
| **CIS Controls v8.1 + CIS Benchmarks** | Hardening taught (`m8_2`) but not mapped to CIS | `m6` OS hardening, not mapped to CIS | **Partial** | CG-2 (mention), CG-4 |

## Threat modeling / adversary knowledge

| Standard (current version, date) | AppSec coverage | Guardians coverage | Verdict | Finding |
|---|---|---|---|---|
| **MITRE ATT&CK v19** (Apr 2026) | none | `m18_5` (ATT&CK & threat hunting) — strong | **Gap** (AS) / **Meets** (CG) | AS-6 (nice-to-have) |
| **MITRE D3FEND 1.3.0** (Dec 2025) | none | none by name (defensive content exists, unmapped) | **Gap** (breadth) | CG-2 (mention) |
| **CWE Top 25 (2025 list, 11 Dec 2025)** | none — CWE never referenced | none | **Gap** — no CWE vocabulary despite CVE/CVSS coverage | AS-4, CG-5 |
| **STRIDE / PASTA / attack trees (formal threat modeling)** | `m4_1` "four questions" (Shostack-style) but **no named methodology** | none | **Partial** (AS) / **Gap** (CG) | AS-2 (STRIDE), CG-2 (mention) |

## Certifications (does a graduate map to the exam objectives?)

| Cert (current exam version) | AppSec | Guardians | Verdict | Finding |
|---|---|---|---|---|
| **CompTIA Security+ SY0-701** (SY0-801 preview ~Oct 2026) | partial (web slice) | `m28` badge + broad coverage | **Meets** (CG) | CG-3 (note SY0-801 horizon) |
| **CompTIA Network+ N10-009** | n/a | `m2`,`m9` + badge | **Meets** (CG) | — |
| **CompTIA CySA+ CS0-003** | partial | `m16`,`m18_5`,`m19` + badge | **Meets** (CG) | — |
| **CompTIA PenTest+ PT0-003** | partial | `m15`,`m18`,`m20`,`m21` | **Partial** | CG-3 (add badge) |
| **(ISC)² CISSP** (8 domains) | partial (Domain 8 slice) | broad, but **Domain-level gaps**: Security & Risk Mgmt (GRC), BC/DR, physical security | **Partial** | CG-2, CG-4, CG-7 |
| **(ISC)² SSCP** | partial | broad match | **Partial** | CG-2 |
| **EC-Council CEH v13** | partial | `m18`,`m20`,`m21` + badge (v13) | **Meets** (CG) | — |
| **GIAC GWEB / GSEC / GPEN / GCIH** | GWEB badge (AS) | GCIH-adjacent (`m23`) | **Partial** | AS verify badges accurate — OK |
| **OffSec OSCP+ / OSWA / OSWE** | OSWA badge (AS) | OSCP/OSWE mentioned | **Meets** (badge scope) | note OSCP→**OSCP+** rename |
| **PortSwigger BSCP** | badge + required track (`m4_3`,`m10_2`) | mentioned | **Meets** (AS) | — |
| **CREST CRT / CPSA (UK/EU)** | none | none | **Gap** — "anywhere" goal wants a UK/EU-recognized cert named | CG-3 |
| **INE eWPT / eCPPT (fka eLearnSecurity)** | eWPT badge (AS) | eJPT mentioned | **Meets** | note "INE Security" rebrand |

## Cloud / containers / supply chain

| Standard (current version, date) | AppSec | Guardians | Verdict | Finding |
|---|---|---|---|---|
| **AWS Well-Architected — Security Pillar** | `m8_3` (IAM, SSRF-to-metadata) — strong, not named as WAF pillar | `m25` (Capital One SSRF case) | **Meets/Partial** | AS-7 (mention) |
| **Microsoft Cloud Security Benchmark v1 (v2 preview)** | none by name | none | **Gap** (breadth) | AS-7 (mention) |
| **CIS Kubernetes Benchmark / CNCF, Pod Security** | `m8_4` (K8s security, NetworkPolicy, Pod Security) — solid | brief | **Meets** (AS) | — |
| **SLSA v1.2** (Nov 2025; Build L0–L3 + Source track) | `m1-5`, `m7_2` — SLSA taught (levels may cite 1.0) | none | **Meets** (AS, minor version note) | AS-5 (version note) |
| **SBOM — CycloneDX / SPDX** | `m7_2` — both named | passing | **Meets** (AS) | — |
| **OpenSSF Scorecard** | none by name | none | **Gap** (small) | AS-5 |

## Privacy / compliance (breadth)

| Standard (current version, date) | AppSec | Guardians | Verdict | Finding |
|---|---|---|---|---|
| **GDPR (EU)** | `m7_3` — solid (72h breach, DSAR, lawful bases) | **none** (0 hits) | **Meets** (AS) / **Gap** (CG) | CG-4 |
| **CCPA/CPRA (California)** | `m7_3` mentions CCPA | none | **Partial** | CG-4 (mention) |
| **PCI DSS 4.0.1** (only valid version since 31 Dec 2024; all reqs mandatory since 31 Mar 2025) | `m7_3` — cites "PCI DSS 6.4"; should confirm **4.0.1** current & MFA/12-char rules | passing | **Partial** | AS-7 |
| **HIPAA / SOC 2** | `m7_3` — solid | passing | **Meets** (AS) | — |
| **EU NIS2 / Cyber Resilience Act / DORA** | none (CRA especially relevant — **reporting obligations apply 11 Sep 2026**) | none | **Gap** — a global software producer must know CRA's 24h exploited-vuln reporting | AS-7 |
| **ISO/IEC 42001 (AI management) & EU AI Act** | Phase 7.5 is technical; governance not named | `m24_5` technical only | **Gap** (small, breadth) | AS-8 (mention) |

## Cross-cutting modern topics

| Topic (why it matters now) | AppSec | Guardians | Verdict | Finding |
|---|---|---|---|---|
| **Post-quantum crypto / crypto-agility** (FIPS 203/204/205 final Aug 2024; HQC selected Mar 2025; US EO 2030/2035 migration deadlines) | none (`m1-2` TLS, no PQC) | none (`m10` crypto, no PQC) | **Gap** — 0 hits both courses; now a board-level topic | AS-6, CG-7 |
| **Vulnerability prioritization: CVSS + EPSS + CISA KEV/SSVC** | `m9_2` CVSS mention only | `m19` — CVSS+EPSS+risk triage, **no KEV/SSVC** | **Partial** | CG-5 |
| **Formal GRC: risk register, risk appetite, treatment** | none | GRC mentioned x2, no method | **Gap** | CG-2 |
| **Business continuity / disaster recovery / backups (3-2-1)** | `m9_3` IR only | `m23` IR; backups mentioned, no BC/DR method | **Partial/Gap** | CG-7 |
| **Physical & environmental security** | n/a | none | **Gap** (CISSP domain) | CG-7 (mention) |

---

## Sources (web-verified July 2026)

- OWASP Top 10:2025 — https://owasp.org/Top10/2025/ (final, Nov 2025)
- OWASP API Security Top 10 (2023) — https://owasp.org/API-Security/editions/2023/
- OWASP Top 10 for LLM Applications (2025) & Agentic Apps (Dec 2025) — https://genai.owasp.org/
- OWASP ASVS 5.0.0 (30 May 2025) — https://github.com/OWASP/ASVS , https://asvs.dev/
- OWASP MASVS 2.1.0 (18 Jan 2024) — https://mas.owasp.org/
- OWASP SAMM 2.0 — https://owaspsamm.org/
- NIST CSF 2.0 (26 Feb 2024) — https://www.nist.gov/cyberframework
- NIST SP 800-63B-4 (31 Jul 2025) — https://csrc.nist.gov/pubs/sp/800/63/b/4/final
- NIST SP 800-218 SSDF v1.1 — https://csrc.nist.gov/pubs/sp/800/218/final
- NIST NICE Framework Components v2.0.0 (5 Mar 2025; SP 800-181r1) — https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/nice-framework-current-versions
- ISO/IEC 27001:2022 (2013→2022 transition closed 31 Oct 2025)
- CIS Controls v8.1 — https://www.cisecurity.org/controls
- MITRE ATT&CK v19 (Apr 2026) — https://attack.mitre.org/resources/versions/ ; D3FEND 1.3.0 (Dec 2025) — https://d3fend.mitre.org/changelog/
- CWE Top 25 (2025 list, 11 Dec 2025) — https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html
- CompTIA SY0-701 (SY0-801 preview ~Oct 2026), N10-009, CS0-003, PT0-003 — CompTIA
- EC-Council CEH v13; OffSec OSCP+/OSWA/OSWE; PortSwigger BSCP; INE Security eWPT/eCPPT (fka eLearnSecurity)
- CREST CRT/CPSA + OSCP equivalency — https://www.crest-approved.org/
- SLSA v1.2 (Nov 2025) — https://slsa.dev/ ; SBOM CycloneDX/SPDX ; OpenSSF Scorecard
- PCI DSS 4.0.1 (mandatory since 31 Mar 2025) — https://www.pcisecuritystandards.org/
- EU CRA (reporting 11 Sep 2026; main obligations 11 Dec 2027), NIS2, DORA (applies since 17 Jan 2025) — https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- NIST FIPS 203/204/205 (Aug 2024), HQC selected Mar 2025, US PQC migration EO (2030/2035) — https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards
- EPSS v4 (Mar 2025); CISA KEV catalog — https://www.first.org/epss/ , https://www.cisa.gov/known-exploited-vulnerabilities-catalog
