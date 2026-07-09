# 00 · Global-Standards Gap Audit — Index & Executive Summary

**Audit date:** 9 July 2026 · **Auditor role:** independent standards-benchmarking pass ("Fable")
**Scope:** both courses — `cyber-full stack/full_stack_appsec_app.html` (Full-Stack AppSec) and
`cyber-guardians/cyber_guardians_app.html` (Cyber Guardians) — benchmarked against the global set
of security standards, frameworks, and certification objectives an employer anywhere (US/EU/UK/APAC)
would check for.

This folder is a **blueprint for the Sonnet implementation session**, not a set of live edits. No
course files or git state were touched.

---

## The honest verdict, up front

**Both courses are in strong shape.** This is not a rescue job. The AppSec course in particular is,
against the current standards, an unusually complete and modern curriculum — its auth module is
NIST-aligned before I asked it to be, its LLM phase tracks the 2025 OWASP LLM Top 10, and its
supply-chain coverage (SLSA, SBOM, signing) is ahead of most professional training. Cyber Guardians
is broad and current on the technical, offensive, and defensive branches (MITRE ATT&CK, Zero Trust,
forensics, IR, malware, AI-driven attacks, IoT/OT).

The gaps that exist cluster into **three honest categories**, and I've resisted padding the list:

1. **One genuinely time-sensitive staleness** affecting *both* courses: they teach the **OWASP Top
   10 (2021)**, and the **2025 edition is now final** with two new categories and a reshuffle.
   Fix this first. *(Findings AS-1, CG-1.)*

2. **Missing standard *names* over content that already exists.** The courses often teach the right
   thing without citing the framework a graduate will be quizzed on by name — ASVS, STRIDE, NIST
   800-63B, CWE, SSDF, NICE, KEV/SSVC. These are low-effort, high-recognition adds: you're labeling
   existing strength, not authoring new labs. *(AS-2, AS-3, AS-4, AS-5, AS-9; CG-3, CG-5, CG-6.)*

3. **Genuine new-topic blind spots the 2026 landscape now demands.** Post-quantum crypto (standards
   finalized, government migration deadlines set), EU software regulation (the **Cyber Resilience
   Act's** reporting duties start **11 Sep 2026** — this month), agentic AI security, and — for
   Cyber Guardians specifically — a **governance/GRC spine** (no NIST CSF, no risk-management
   vocabulary, no privacy law). *(AS-6, AS-7, AS-8; CG-2, CG-4, CG-7.)*

**If Cyber Guardians has one structural weakness, it's the governance axis.** It teaches security
*doing* superbly and security *deciding* barely at all — which is exactly the half the management-
track certs (Security+ GRC domain, CISSP Domain 1) test and the half a career-oriented graduate
needs. That's finding **CG-2**, the highest-value single addition in this audit.

Nothing here requires new schema fields or renderer changes; all drafts fit the existing contracts.

---

## How to use these files

- **`03-standards-crosswalk.md`** — the matrix. Every standard/cert → covering module(s) by `id` →
  Meets/Partial/Gap → finding pointer. Start here to see the whole landscape at a glance; it was
  also my gap-finding tool, so it's the fastest way to sanity-check that nothing was missed.
- **`01-appsec-fullstack-gaps.md`** — findings `AS-1`…`AS-9` for the AppSec course, each with exact
  integration point and drop-in drafted content in the course's gold-standard pattern.
- **`02-cyber-guardians-gaps.md`** — findings `CG-1`…`CG-9` for the broad course, drafted for its
  stricter `theory`/`lab`/`caseStudy`/`challenges`/`quiz`/`tracker` field contract.
- **This file** — summary, priority order, standards-checked list with versions.

Findings are labeled **Blind spot / Shallow / Stale / Nice-to-have**. Where content was too large
to fully draft in one pass, it's marked **"OUTLINE ONLY — needs a full authoring pass."** Fully
drafted findings are ready to adapt into a `body`/`theory` field with only voice-matching and the
flagged escaping.

---

## Recommended implementation order (highest value first)

| # | Finding | Course | Severity | Effort | Why this order |
|---|---|---|---|---|---|
| 1 | **AS-1 / CG-1** OWASP Top 10 → 2025 | both | Stale | Med (course-wide relabel) | Time-sensitive; the only thing that reads as "a year behind" today. Do both together. |
| 2 | **CG-2** NIST CSF 2.0 + risk mgmt module | Guardians | Blind spot | Med-High (new module) | Closes the single biggest structural gap; becomes the spine other modules reference. |
| 3 | **AS-6 / CG-7** Post-quantum crypto | both | Blind spot | Low-Med | Fully drafted; timely (FIPS finalized, 2030/2035 deadlines); zero current coverage. |
| 4 | **AS-7** EU CRA/NIS2/DORA + PCI 4.0.1 | AppSec | Stale/Blind | Low | CRA reporting starts 11 Sep 2026; fully drafted; closes the main US-centric blind spot. |
| 5 | **AS-2** ASVS 5.0 + STRIDE naming | AppSec | Blind spot | Low | Fully drafted; names existing strength; huge interview-recognition payoff. |
| 6 | **AS-3 / CG-6** NIST 800-63B-4 citation | both | Shallow | Low | Fully drafted; adds the standard's name + 2 current rules to already-strong auth content. |
| 7 | **CG-3** NICE Framework in careers | Guardians | Partial | Low | Fully drafted; brief flagged it explicitly; adds CREST for the global goal. |
| 8 | **AS-4 / CG-5** CWE / CWE Top 25 + KEV/SSVC | both | Shallow | Low | Fully drafted; cheap vocabulary add over existing CVE/CVSS work. |
| 9 | **CG-4** Privacy law breadth (GDPR et al.) | Guardians | Gap | Low-Med | Outline; closes "GDPR: 0 hits" in a global course. |
| 10 | **AS-5** NIST SSDF / SAMM / SLSA version | AppSec | Shallow | Low-Med | Outline; framing over existing Phase 7 content. |
| 11 | **AS-8 / CG-9** Agentic AI & MCP security | both | Nice-to-have | Med | Outline; forward-looking; AppSec gets the full module, Guardians the awareness version. |
| 12 | **AS-9 / CG-8** API Top 10 (2023) / MASVS naming | both | Nice-to-have | Trivial | One-sentence standard-naming adds. |

**Batching suggestion:** items 5–8 and 12 are all "name the standard over existing content" —
low-risk prose edits that can be done in one focused pass. Items 2, 9, and 11 are the ones that need
real authoring time.

---

## Standards / frameworks / certs checked (with current version + date, web-verified July 2026)

**Web/App/API** — OWASP Top 10:2025 (final, Nov 2025); OWASP API Security Top 10 (2023); OWASP LLM
Top 10 (2025) + Agentic Top 10 (Dec 2025) + MCP Top 10; OWASP ASVS 5.0.0 (30 May 2025); OWASP MASVS
2.1.0 (18 Jan 2024) / MASTG; OWASP SAMM 2.0; OWASP Cheat Sheets / WSTG.

**Governance/risk** — NIST CSF 2.0 (26 Feb 2024, adds Govern); NIST SP 800-53 Rev 5; NIST SP
800-63B-4 (31 Jul 2025); NIST SP 800-218 SSDF v1.1; NIST NICE Components v2.0.0 (5 Mar 2025,
SP 800-181r1); ISO/IEC 27001:2022 & 27002:2022 (2013 edition retired 31 Oct 2025); ISO/IEC
27017/27018; CIS Controls v8.1 + Benchmarks.

**Threat/adversary** — MITRE ATT&CK v19 (Apr 2026); MITRE D3FEND 1.3.0 (Dec 2025); CWE Top 25
(2025 list, 11 Dec 2025); STRIDE / PASTA / attack trees.

**Certifications** — CompTIA Security+ SY0-701 (SY0-801 preview ~Oct 2026), Network+ N10-009, CySA+
CS0-003, PenTest+ PT0-003; (ISC)² CISSP (8 domains), SSCP; EC-Council CEH v13; GIAC GSEC/GWEB/GPEN/
GCIH; OffSec OSCP+/OSWA/OSWE; PortSwigger BSCP; CREST CRT/CPSA (+ OSCP equivalency route); INE
Security eWPT/eCPPT (fka eLearnSecurity).

**Cloud/supply chain** — AWS Well-Architected Security Pillar; Microsoft Cloud Security Benchmark v1
(v2 in preview); Google Cloud Security Foundations; CIS Kubernetes Benchmark / CNCF; SLSA v1.2
(Nov 2025); SBOM CycloneDX/SPDX; OpenSSF Scorecard.

**Privacy/compliance** — GDPR; CCPA/CPRA; PCI DSS 4.0.1 (all reqs mandatory since 31 Mar 2025);
HIPAA; SOC 2; EU NIS2, Cyber Resilience Act (reporting 11 Sep 2026; main obligations 11 Dec 2027),
DORA (applies since 17 Jan 2025); ISO/IEC 42001 & EU AI Act (breadth).

**Cross-cutting modern** — NIST FIPS 203/204/205 post-quantum (final Aug 2024; HQC added Mar 2025;
US migration EO deprecate-by-2030/disallow-by-2035); vulnerability prioritization via CVSS + EPSS
v4 (Mar 2025) + CISA KEV + SSVC.

Full source URLs are listed at the foot of `03-standards-crosswalk.md`.

---

## Methodology (so findings are auditable)

1. **Coverage map.** Extracted every phase/module `id` and `title` from both live HTML files, then
   ran ~200 keyword probes (standard names, cert names, technique terms) across both files to
   measure presence *and* depth (hit counts), and read the specific modules that any finding
   depends on so integration points cite real, current content.
2. **Version research.** Web-verified the current (2026) edition/date of every standard and cert
   above, because training data lags and a superseded version number would undermine the audit.
   Every version claim in these files is traceable to a named source.
3. **Crosswalk.** Built `03-standards-crosswalk.md` as both a deliverable and the gap-finding tool —
   Meets/Partial/Gap per standard, which surfaced the findings.
4. **Findings + drafts.** Wrote each finding to the required format with drafted content in the
   course's own voice, flagging every `</script>` / backtick / `${}` splice gotcha for the
   implementer.
5. **This summary last**, once the actual shape of the findings was known — including saying plainly
   that both courses are already strong and that the real list is short. No findings were
   manufactured to look thorough.

---

## What I deliberately did **not** flag

- **Tool ARM64/M-series compatibility** — out of scope (tracked separately).
- **UI/UX, broken anchors, HTML rendering** — out of scope unless hiding content (none did).
- **Formatting inconsistencies between the two courses** that don't map to a standards gap — an
  implementation concern, not a standards one.
- **Depth beyond a course's stated audience** — e.g. Cyber Guardians isn't a compliance course, so
  privacy law is drafted at *recognition* breadth, not practitioner depth. Same for the AppSec
  course on general blue-team/forensics (correctly Cyber Guardians' territory).
- **Things already strong** — auth (AppSec), ATT&CK/Zero Trust/forensics/IR (Guardians), supply
  chain and SBOM (AppSec), email auth SPF/DKIM/DMARC (Guardians). These meet or exceed their
  standards and need nothing.
