# 02 · Cyber Guardians — Gap Findings & Drafted Fixes

Course file: `cyber-guardians/cyber_guardians_app.html` (ground truth).
Module schema (**strict — the renderer only consumes these named fields**):
`{ id, level, num, title, objective, theory, lab:{mac,windows,linux}, caseStudy:{title,body},
challenges:[{q,a}], quiz:[...], tracker:[...] }`. Dual-language code lives *inside* `theory` as
fenced blocks. Drafted content below is written for these fields.

**⚠️ Escaping reminder that applies to EVERY drafted `theory` block below:** `theory` is a JS
template literal — any backtick `` ` `` or `${...}` inside code you paste must be escaped
(`` \` `` and `\${`) on the implementation side, and any `</script>` inside a payload needs the
`<\/script>` treatment. Each finding re-flags the specific spots.

**Headline:** Cyber Guardians is **broad and strong** on the technical/offensive/defensive
branches (ATT&CK, Zero Trust, forensics, IR, malware, AI attacks, IoT/OT). Its real gaps are on the
**governance / risk / compliance** axis — the things a SOC-analyst-to-manager track and the CISSP/
Security+ "management" domains expect. The biggest single miss is that the course has **no named
governance framework** (NIST CSF 2.0 is absent), and, surprisingly for a global course, **no
privacy-law coverage at all** (GDPR: 0 hits). It also shares the AppSec course's **stale OWASP Top
10 (2021)** and **zero post-quantum** gaps.

Findings ordered by priority.

---

## Cyber Guardians — `m14` OWASP Top 10 — Web Security

**Standard(s)/cert(s) this closes a gap for:** OWASP Top 10:2025 (final, Nov 2025 —
https://owasp.org/Top10/2025/). Feeds Security+, CySA+, CEH.
**Severity:** Stale.
**Integration point:** Rewrite `m14`'s `theory` category table (currently labeled "OWASP Top 10
(2021)" with the 2021 `A01…A10` rows) to the 2025 set; update the `quiz` and `challenges` if they
name 2021 categories.

**Why this is a gap:** `m14` explicitly presents the **2021** list (confirmed: the theory table
reads `A01 Broken Access Control … A10 SSRF` with the header "OWASP Top 10 (2021)"). The 2025
edition is final and moved things: **Security Misconfiguration → A02**, **Software Supply Chain
Failures → new A03**, **SSRF folded into A01**, and **Mishandling of Exceptional Conditions → new
A10**. Same fix as AppSec finding AS-1 — see that entry for the full replacement table; this course
needs the shorter, awareness-level version below.

**Drafted content** (replacement `theory` table for `m14`):

```markdown
## The OWASP Top 10 (2025 edition)

OWASP refreshed the list in 2025. If you learned the 2021 version, note the two structural changes:
**supply-chain attacks got their own category (A03)**, and a new **A10** covers software that fails
*open* when an error hits. **SSRF** is no longer its own entry — it now lives under **A01**.

| 2025 | Category | One-line meaning | Example |
|---|---|---|---|
| A01 | Broken Access Control (incl. SSRF) | Users reach data/actions they shouldn't | IDOR: `/account/123` → change to `124` |
| A02 | Security Misconfiguration | Insecure defaults, exposed panels, verbose errors | Default admin creds, open S3 bucket |
| A03 | **Software Supply Chain Failures** | A dependency/build/CI step is compromised | Malicious npm package, SolarWinds |
| A04 | Cryptographic Failures | Weak/missing encryption of sensitive data | MD5 passwords, plaintext HTTP |
| A05 | Injection | Untrusted input becomes code/query | `admin' OR '1'='1`, XSS |
| A06 | Insecure Design | The flaw is in the design, not a bug | Password reset with no expiry |
| A07 | Authentication Failures | Identity can be forged or brute-forced | No lockout, weak session IDs |
| A08 | Software or Data Integrity Failures | Unverified updates/deserialization | Unsigned auto-update |
| A09 | Security Logging & **Alerting** Failures | Attacks go unseen and unalerted | 200-day dwell time, no central logs |
| A10 | **Mishandling of Exceptional Conditions** | Error paths fail *open* | A `catch` that skips an authz check |
```

**Flags for the implementer:** the payload cells contain `admin' OR '1'='1` and `/account/124` —
plain strings, no `</script>`, but if the surrounding row already had escaping, preserve it. No
backticks inside the table.

---

## Cyber Guardians — NEW MODULE (governance spine) — insert as `m1_5` "Security Governance, Risk & the NIST CSF"

**Standard(s)/cert(s) this closes a gap for:** NIST Cybersecurity Framework (CSF) 2.0 (26 Feb 2024,
adds the **Govern** function — https://www.nist.gov/cyberframework); NIST SP 800-53 Rev 5 (control
catalog); ISO/IEC 27001:2022 (ISMS); CIS Controls v8.1. Feeds **CISSP Domain 1 (Security & Risk
Management)**, **Security+ Domain 5 (Governance, Risk & Compliance)**, CySA+, GRC-analyst roles.
**Severity:** Blind spot — the world's most-cited governance framework and formal risk management
are absent from a broad course that otherwise reaches management-track certs.
**Integration point:** New early module inserted as **`m1_5`** (Recruit level, between `m1` CIA
Triad and `m2` How the Internet Works), so the CSF's five/six functions become the mental scaffold
the rest of the course hangs on. Cross-reference it from `m16` (Blue Team = Detect/Respond),
`m23` (IR = Respond/Recover), `m18_5` (threat hunting = Detect).

**Why this is a gap:** The course teaches Detect/Respond/Recover *activities* superbly (blue team,
IR, forensics) but never gives them the **framework spine** every employer, auditor, and management-
track cert uses to organize them: the **NIST CSF**. CSF 2.0 (Feb 2024) is a landmark update that
added a sixth function, **Govern**, precisely because organizations kept doing the technical work
without the governance layer. A "curious beginner to security career" course that omits CSF, risk
registers, and the concept of an ISMS leaves a graduate unable to speak the language of a GRC
interview or the Security+ GRC domain. This is the single highest-value structural add for Guardians.

**Drafted content:**

`objective`:
```
Every technical skill in this course fits into a bigger picture that employers, auditors, and
regulators share: a governance framework. This module gives you that map — the NIST Cybersecurity
Framework 2.0 and the basics of risk management — so you can explain not just *how* to defend a
system, but *how an organization decides what to defend and proves it did.*
```

`theory` (abridged to the load-bearing parts — expand code/examples to course length in authoring):
```markdown
## Why frameworks exist

You can know Nmap, Wireshark, and Burp cold and still fail a job interview that asks "how would you
build a security *program*?" Individual skills defend a host. A **framework** organizes those
skills so an organization can decide what matters, assign responsibility, and *prove* to a customer
or regulator that it's handling risk. The one you must know by name is the **NIST Cybersecurity
Framework (CSF) 2.0** — released February 2024, used worldwide, and free.

## The six CSF 2.0 functions

CSF 1.1 had five functions. **CSF 2.0 added GOVERN** — a signal that leadership, policy, and risk
decisions are part of security, not separate from it.

| Function | Question it answers | Where you see it in this course |
|---|---|---|
| **GOVERN** (new in 2.0) | Who decides, what's our risk appetite, what are the policies? | This module, `m28` careers |
| **IDENTIFY** | What do we have and what could go wrong? | Asset inventory, `m19` vuln assessment, threat modeling |
| **PROTECT** | How do we prevent harm? | `m6` OS hardening, `m16_5` Zero Trust, crypto (`m10`) |
| **DETECT** | How do we notice an attack? | `m16` blue team, `m18_5` ATT&CK/threat hunting, SIEM |
| **RESPOND** | What do we do during an incident? | `m23` incident response |
| **RECOVER** | How do we get back to normal? | Backups, BC/DR (see `m23`) |

When someone describes their SOC as "we're strong on Detect and Respond but weak on Govern," they
mean this. Memorize the six — it's the spine of Security+ Domain 5 and CISSP Domain 1.

## Risk management — the vocabulary

Security is applied risk management. The core terms:

- **Asset** — something of value (data, a server, a reputation).
- **Threat** — something that could cause harm (ransomware crew, insider, flood).
- **Vulnerability** — a weakness a threat can exploit (unpatched CVE, weak password policy).
- **Risk** — the *combination*: likelihood × impact. `Risk = Threat × Vulnerability × Impact`.
- **Risk appetite** — how much risk leadership will accept before spending to reduce it.

**The four risk treatments** (know these four words):
1. **Mitigate** — reduce it (patch, add MFA).
2. **Transfer** — shift it (cyber insurance, outsource).
3. **Avoid** — stop doing the risky thing.
4. **Accept** — acknowledge and monitor (when the fix costs more than the risk).

A **risk register** is the living document where each risk is logged with its owner, likelihood,
impact, treatment, and status. Being able to say "I'd log that in the risk register as
high-likelihood/high-impact and recommend mitigation" is a GRC-analyst answer.

## Frameworks you should be able to name (breadth, not depth)

- **NIST CSF 2.0** — the flexible outcome-based framework above.
- **NIST SP 800-53 Rev 5** — the giant US federal *control catalog* CSF points to.
- **ISO/IEC 27001:2022** — the *international* certification for an Information Security Management
  System (ISMS). When a non-US company says "we're ISO 27001 certified," this is it. (The 2013
  edition retired 31 Oct 2025 — 27001:2022 is the only current version.)
- **CIS Controls v8.1** — 18 prioritized, prescriptive controls; the fastest practical starting
  point for a small org ("do these 18 things in order").
- **MITRE ATT&CK / D3FEND** — adversary behaviors (you meet ATT&CK in `m18_5`) and their defensive
  countermeasures.

You don't need to memorize all of 800-53. You need to know *which framework answers which question*
so you can navigate a real security program — and pass the GRC section of every foundational cert.
```

`lab` (governance is paper-based; make the "lab" a real deliverable, OS-agnostic but keep the three
keys populated):
```
mac/windows/linux (same task): Build a mini risk register for your own lab from Module 8's
personal security audit. In a spreadsheet, list 5 risks (e.g. "reused password on old account"),
score each Likelihood (1-5) × Impact (1-5), pick a treatment (mitigate/transfer/avoid/accept), and
assign yourself as owner. Then tag each risk to a CSF function (Identify/Protect/Detect/…). This is
exactly what a GRC analyst produces on day one.
```

`caseStudy`:
```
title: "Equifax (2017) — a governance failure, not just a technical one"
body: The Equifax breach (147M records) is usually told as "they didn't patch Apache Struts
(CVE-2017-5638)." True — but the deeper failure was GOVERN and IDENTIFY: no accurate asset
inventory (they didn't know where Struts ran), an expired scanning certificate that silently
disabled detection, and no clear ownership for acting on the patch alert. A CSF lens shows the
breach touched every function: Identify (unknown assets), Protect (unpatched), Detect (blind
scanner), Respond (delayed disclosure), Govern (no accountable owner). Technical patching was one
missing control among five failed functions — which is exactly why frameworks exist.
```

`challenges`:
```
{ q: "Your company can't afford to fully fix a low-likelihood, low-impact risk this quarter. Which
     of the four risk treatments applies, and what must you still do?",
  a: "Accept — but formally: document it in the risk register with an owner and a review date, and
     get leadership sign-off on accepting it. 'Accept' is a decision, not ignoring it." }
{ q: "A vendor says 'we're ISO 27001 certified.' What does that actually tell you?",
  a: "That they run a certified Information Security Management System audited against ISO/IEC
     27001:2022 — a governance/process assurance, not a guarantee any specific control is perfect.
     It's the international counterpart to a US SOC 2 report." }
```

`quiz`:
```
"Name the six functions of NIST CSF 2.0 and which one was newly added in the 2.0 release.",
"Write the risk equation and define each term.",
"List the four risk treatment options with an example of each.",
"What is a risk register and what does each entry contain?",
"Which framework is the international ISMS certification, and what is its current version year?"
```

`tracker`:
```
"I can name all six NIST CSF 2.0 functions and place any course topic under one",
"I built a 5-row risk register with likelihood × impact scoring",
"I can explain the four risk treatments with examples",
"I can distinguish NIST CSF, 800-53, ISO 27001, and CIS Controls by what each is for"
```

**Flags for the implementer:** the `theory` contains the string `` `Risk = Threat × Vulnerability
× Impact` `` — that's an inline-code span using backticks, so **escape those backticks** (`` \` ``)
when placing into the template literal. The risk equation also appears un-fenced in the risk
section; keep it consistent. No `</script>` payloads. No `${}` sequences.

---

## Cyber Guardians — `m28` Career Pathways & Certifications

**Standard(s)/cert(s) this closes a gap for:** NIST NICE Workforce Framework, Components v2.0.0
(5 Mar 2025; SP 800-181r1 — https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/nice-framework-current-versions);
plus cert-currency corrections (CompTIA PenTest+ PT0-003, Security+ SY0-801 on the horizon; OffSec
OSCP→**OSCP+**; **CREST CRT/CPSA** for UK/EU; INE Security rebrand of eLearnSecurity).
**Severity:** Partial — strong cert map, but **no NICE role/competency framework** (the brief flags
this explicitly) and a few cert-currency items.
**Integration point:** New "Map yourself to the NICE Framework" subsection in `m28`'s `theory`
after the existing cert map; update the cert-badge/currency mentions; add CREST for the "employable
anywhere" goal.

**Why this is a gap:** `m28` gives an excellent *certification* map but no **role/competency**
framework. The **NIST NICE Framework** is the standard vocabulary (used by employers and,
increasingly, job postings globally) for cybersecurity **work roles**, tasks, and the Knowledge/
Skills that map to them. A career module that lists certs but can't map the student to a NICE work
role (e.g. "Cyber Defense Analyst," "Vulnerability Assessment Analyst," "Secure Software
Developer") is missing the connective tissue between "what I studied" and "what job title to apply
for." Also, for the global goal, the module has **no UK/EU-recognized pentest cert (CREST)**.

**Drafted content:**

New `theory` subsection:
```markdown
## Mapping yourself to real job roles — the NICE Framework

Certifications prove skills; the **NIST NICE Workforce Framework** (Components v2.0.0, March 2025)
names the **jobs** those skills add up to. Employers worldwide describe openings in NICE terms, so
knowing your target **work role** turns "I know security stuff" into "I'm targeting the Cyber
Defense Analyst role." A few roles this course prepares you for:

| NICE work role | What they do | Course modules that build it | Certs that signal it |
|---|---|---|---|
| **Cyber Defense Analyst** (SOC analyst) | Monitor, detect, triage alerts | `m16`, `m18_5`, `m19`, `m23` | Security+, CySA+ |
| **Vulnerability Assessment Analyst** | Find & prioritize weaknesses | `m12`, `m19`, `m20` | PenTest+, eJPT |
| **Penetration Tester** | Authorized offensive testing | `m15`, `m18`, `m20`, `m21` | OSCP+, PenTest+, CEH, **CREST CRT** |
| **Incident Responder** | Contain & recover from attacks | `m23`, `m24`, `m22` (forensics) | GCIH, CySA+ |
| **Secure Software Developer** | Build security into code | the AppSec course | GWEB, OSWA/OSWE, BSCP |

**How to use NICE:** pick the work role you want, read its NICE Task/Knowledge/Skill statements
(free on the NIST NICE site), and treat any gap as your study plan. It's the bridge from this
course to a specific job title recruiters search for.
```

Cert-currency corrections (edit the existing badge/mentions):
```markdown
- OSCP is now issued as **OSCP+** (OffSec added the "+" with the exam refresh); mention both.
- Add **CompTIA PenTest+ (PT0-003)** as the vendor-neutral offensive badge, and note **Security+
  SY0-801** is expected ~late 2026 (SY0-701 remains current and valid for 3 years from test date).
- Add **CREST CRT / CPSA** as the **UK/EU-recognized** penetration-testing path — important for the
  "employable anywhere" goal. Note the OffSec→CREST equivalency route (OSCP/OSCP+ + CPSA → CRT),
  and that CRT-by-equivalency can't be used for UK Government CHECK work (which needs the CREST exam
  directly). This is the single most useful non-US cert to name.
- Note that **eLearnSecurity is now "INE Security"** — the eJPT/eWPT/eCPPT certs are current under
  that brand; update any "eLearnSecurity" label.
```

**Flags for the implementer:** the work-role table has no backticks or payloads. If you keep the
existing cert-badge JSX array elsewhere in the file, the CREST/PenTest+ additions go there as new
`{ name, full, org }` objects — no escaping issues.

---

## Cyber Guardians — NEW subsection in `m28` (or `m5`) + `m23` — Privacy law & compliance breadth

**Standard(s)/cert(s) this closes a gap for:** GDPR (EU); CCPA/CPRA (California); PCI DSS 4.0.1;
HIPAA; SOC 2; EU CRA/NIS2/DORA (breadth). Feeds Security+ GRC domain, CISSP Domain 1, and the
course's own privacy module `m5`.
**Severity:** Gap — **GDPR has 0 hits in the entire course**; a broad, globally-aimed security
course has essentially no data-protection-law vocabulary.
**Integration point:** Extend the existing privacy module **`m5` (Privacy & Safe Browsing)** with a
"The laws that protect data" subsection, and add one paragraph to `m23` (IR) on breach-notification
clocks. Keeps it in the existing privacy home rather than a new module.

**Why this is a gap:** `m5` teaches personal privacy hygiene (tracking, safe browsing) but nothing
about the **regulatory** side — the laws a security professional is expected to recognize and know
when to escalate. For a course whose stated goal is employability *anywhere*, the absence of **GDPR**
(the de-facto global baseline) is the notable miss. This is breadth, not depth — one subsection.

**Drafted content:** OUTLINE ONLY — needs a full authoring pass into `m5.theory`:

- **🎯 The laws you must recognize by name** (short table): **GDPR** (EU — personal data, 72h breach
  notice to regulator, data-subject rights, fines up to 4% global turnover), **CCPA/CPRA**
  (California — consumer data rights), **HIPAA** (US health data), **PCI DSS 4.0.1** (card data —
  contractual, not a law), **SOC 2** (US trust-services audit report). One line each on *what data*
  and *who enforces*.
- **Breach-notification clocks** (the practical thing an incident responder needs): GDPR **72 hours**
  to the supervisory authority; **CRA 24 hours** for actively-exploited product vulnerabilities
  (applies from 11 Sep 2026); PCI/DORA/HIPAA each have their own — the lesson is "know which clock
  starts, and that the IR playbook must include a *legal notification* step." Add this paragraph to
  `m23`'s theory too.
- **"When to escalate"** framing: a broad security analyst isn't a privacy lawyer, but must
  recognize when an incident triggers a legal obligation and loop in the right people fast.
- **caseStudy tie-in:** the existing `m5` Cambridge Analytica case is a perfect anchor — extend its
  body with the GDPR/regulatory aftermath (record fines, the regulatory response that followed).
- **One quiz item:** "An EU user's data is breached. How long do you have to notify the regulator,
  and under which law?" (72 hours, GDPR.)

**Flags for the implementer:** prose only, no payloads/backticks expected.

---

## Cyber Guardians — `m19` Vulnerability Assessment

**Standard(s)/cert(s) this closes a gap for:** CWE Top 25 (2025 — https://cwe.mitre.org/top25/);
CISA **KEV** catalog & **SSVC** decision model; EPSS v4 (Mar 2025). Feeds CySA+, PenTest+.
**Severity:** Shallow — `m19` teaches CVSS+EPSS+risk triage well but omits **KEV** and **SSVC** and
never mentions **CWE**.
**Integration point:** Extend `m19.theory`'s prioritization section (which already contrasts
CVSS-only vs risk-based) with a KEV/SSVC paragraph, and add a one-line CWE definition.

**Why this is a gap:** `m19` is genuinely good — it already teaches *not* to "fix highest CVSS
first" and factors in EPSS and exposure. But modern vuln management has two more must-know inputs
the module misses: **CISA's KEV (Known Exploited Vulnerabilities) catalog** — the authoritative
"this is being exploited *right now*, patch it regardless of score" list — and **SSVC**
(Stakeholder-Specific Vulnerability Categorization), the decision-tree model CISA promotes over raw
scores. And since the module works with CVEs, it should name **CWE** (the weakness type behind each
CVE). Small, high-value additions to an already-strong module.

**Drafted content** (append to `m19.theory`):
```markdown
### Two more inputs the pros use: KEV and SSVC

CVSS tells you *how bad* a vuln is in theory; EPSS tells you *how likely* it is to be exploited
soon. Two more, both free and authoritative:

- **CISA KEV (Known Exploited Vulnerabilities) catalog.** A curated list of CVEs **confirmed
  exploited in the wild**. Rule of thumb: **if it's on KEV, it jumps the queue** — real-world
  exploitation beats any theoretical score. US federal agencies are *required* to patch KEV entries
  on a deadline; treat it the same way. Check it at cisa.gov/kev.
- **SSVC (Stakeholder-Specific Vulnerability Categorization).** Instead of a single number, SSVC is
  a **decision tree**: Is it being exploited (KEV)? Is the system exposed? What's the mission
  impact? It outputs an *action* — Track / Track* / Attend / Act — which is what you actually need.
  CISA promotes SSVC precisely because "CVSS 9.8" isn't a decision, it's a data point.

**The modern triage stack:** start from your scan, then rank by **KEV (exploited?) → EPSS
(likely?) → exposure → asset value**, using CVSS as one input, not the verdict. That's the answer
that lands in a CySA+ interview.

### Naming the weakness: CWE

Every CVE is tagged with a **CWE (Common Weakness Enumeration)** — the *type* of flaw (CWE-79 XSS,
CWE-89 SQLi, CWE-352 CSRF). The **CWE Top 25 (2025)** is the "most dangerous weaknesses" list, led
by XSS, SQLi, and CSRF. When you report a finding, cite its CWE — it's how scanners, CVEs, and
triagers all speak.
```

Add one `quiz` item: `"A CVE has a CVSS of 6.1 but appears on the CISA KEV catalog. Do you patch it
before a 9.8 that isn't on KEV? Why?"` (Yes — KEV means confirmed active exploitation; real-world
risk outranks theoretical severity.)

**Flags for the implementer:** the CWE codes (`CWE-79`) and `Track*` contain no backticks needing
escape; `cisa.gov/kev` is plain text. No `</script>`.

---

## Cyber Guardians — `m3` Passwords, Hashing & MFA

**Standard(s)/cert(s):** NIST SP 800-63B-4 (31 Jul 2025 —
https://csrc.nist.gov/pubs/sp/800/63/b/4/final). **Severity:** Partial — teaches hashing/MFA but
doesn't cite 800-63B or its current rules. **Integration point:** short callout in `m3.theory`.
**Why:** `m3` covers hashing and MFA but should name the global reference standard and its
current, sometimes-counterintuitive rules (15-char minimum single-factor, **no** composition rules,
**no** forced rotation, **screen against breached-password lists**). Mirrors AppSec finding AS-3 —
use the abbreviated version.

**Drafted content** (append to `m3.theory`):
```markdown
### What NIST SP 800-63B-4 actually says (2025)

The global reference for password rules is **NIST SP 800-63B-4** (July 2025). Its current guidance
surprises people:
- **Length beats complexity:** ≥15 characters when a password is the *only* factor; support 64+ and
  allow spaces/Unicode.
- **Drop composition rules** ("1 upper/1 number/1 symbol") — they push users to predictable patterns.
- **No scheduled rotation** — change only on evidence of compromise.
- **Screen new passwords against breach lists** (e.g. Have I Been Pwned) and reject matches.
So the old "change your complex password every 90 days" advice is now an *anti-pattern* by the
standard's own words.
```

Add a `quiz` item: `"According to NIST SP 800-63B-4, name two common password practices that are
now discouraged."` (Forced periodic rotation; mandatory composition/complexity rules.)

**Flags for the implementer:** prose + list, no backticks/payloads.

---

## Cyber Guardians — `m10` Cryptography Essentials — post-quantum subsection

**Standard(s)/cert(s):** NIST FIPS 203/204/205 (Aug 2024), HQC selected Mar 2025, US PQC migration
EO (2030/2035). **Severity:** Blind spot (0 post-quantum hits). **Integration point:** new
subsection in `m10.theory` after the TLS/AES material.
**Why:** `m10` covers AES-GCM and TLS well but has no post-quantum awareness. With standards
finalized and government migration deadlines set (deprecate by 2030, disallow by 2035), a broad
security course should give graduates the vocabulary. Mirrors AppSec finding AS-6 at awareness depth.

**Drafted content** (append to `m10.theory`):
```markdown
### The quantum threat and post-quantum cryptography

The encryption protecting the internet (RSA, ECDH key exchange, ECDSA signatures) relies on math a
large **quantum computer** could break. It doesn't exist at scale yet, but **"harvest now, decrypt
later"** means adversaries record encrypted data today to crack later — so long-lived secrets are
already at risk.

The response is real and standardized. In **August 2024** NIST finalized the first post-quantum
algorithms: **FIPS 203 (ML-KEM)** for key exchange, **FIPS 204 (ML-DSA)** and **FIPS 205 (SLH-DSA)**
for signatures (**HQC** was added as a backup in March 2025). Governments have set deadlines to
retire classical algorithms (US: deprecate by **2030**, disallow by **2035**), and modern TLS 1.3
already negotiates **hybrid** key exchange (classical + ML-KEM together).

**What a defender needs to know:** you won't implement these, but you should (1) recognize the terms
ML-KEM / post-quantum / crypto-agility, (2) understand that keeping crypto libraries current is a
security control because it's how the hybrid algorithms reach you, and (3) know the migration is a
live project, not science fiction.
```

Add a `quiz` item: `"What does 'harvest now, decrypt later' mean, and why does it make post-quantum
migration urgent even before quantum computers are practical?"`

**Flags for the implementer:** `ML-KEM` etc. are plain text; no backtick spans or `${}` in this
draft — safe for the template literal.

---

## Cyber Guardians — `m24_5` AI-Powered Attacks & Defenses — agentic AI (nice-to-have)

**Standard(s)/cert(s):** OWASP Top 10 for LLM Applications (2025) & Agentic Applications (Dec 2025)
+ MCP Top 10 — https://genai.owasp.org/. **Severity:** Nice-to-have expansion. **Integration
point:** extend `m24_5.theory` with an "autonomous agents" subsection.
**Why:** `m24_5` is current on AI *attacks* (deepfakes, AI-assisted phishing — the Arup £25M case
is excellent) but predates the **agentic** wave. A short subsection on autonomous-agent risk
(excessive agency, tool/MCP poisoning, confused-deputy) keeps the broad course's AI module abreast
of the 2026 landscape. See AppSec finding AS-8 for the fuller treatment; here it's awareness-level.

**Drafted content:** OUTLINE ONLY — needs a full authoring pass:
- One paragraph defining **agentic AI** (LLMs that *take actions* via tools) and why autonomy is a
  new risk axis beyond prompt injection.
- Name the OWASP **Agentic Top 10** themes (excessive agency, tool misuse, memory poisoning,
  multi-agent trust) and the **MCP Top 10** (malicious tool servers, tool-description injection).
- Defensive one-liner: least-privilege tool scopes, human-in-the-loop for high-impact actions,
  treat tool output as untrusted, allow-list MCP servers.
- Tie to the existing `m24_5` deepfake case: as agents gain the ability to *act*, an AI-driven
  social-engineering attack can move from "convince a human" to "drive an over-privileged agent."

**Flags for the implementer:** if the drafted agentic example includes a prompt-injection payload
with a `</script>` or code with backticks/`${}`, **escape both** for the `theory` template literal.

---

## Cyber Guardians — `m25` Cloud & Mobile Security — MASVS naming (nice-to-have)

**Standard(s)/cert(s):** OWASP MASVS 2.1.0 (18 Jan 2024) / MASTG. **Severity:** Nice-to-have.
**Integration point:** one sentence in `m25.theory`'s mobile section.
**Why:** `m25` covers mobile security generally but doesn't name the **OWASP MASVS** (Mobile
Application Security Verification Standard) — the mobile counterpart to ASVS, and the standard a
mobile-security role expects. Add: "For mobile specifically, the standard is **OWASP MASVS 2.1.0**
(with the **MASTG** testing guide) — it covers storage, crypto, auth, network, platform
interaction, code quality, resilience, and (added in 2.1) **privacy**. If you go into mobile
security, MASVS is your ASVS." **Flags:** none — one sentence, no code.
