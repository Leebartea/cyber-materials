# Mission Brief: Global-Standards Gap Audit & Expansion Blueprint

You are being brought in as a **third, independent role** on this project. Read this whole
document before touching anything — it is self-contained because you are starting cold.

## Who else is working on this repo (so you understand your lane)

- **The orchestrating Claude Code session ("Sonnet")** is the one who will actually *edit* the
  live course files. It runs on Anthropic's Sonnet model and does all implementation work.
- **`cyber-guardian-appsec-mentor`** is a specialized Opus subagent that session invokes for deep
  architectural/pedagogical judgment calls on this same curriculum.
- **You ("Fable")** are being run standalone in a separate terminal for this one task. Your job is
  **research and blueprint authorship only** — a global-standards benchmarking audit that produces
  a detailed, actionable expansion plan. You are explicitly **not** changing the project's
  workflow, and you are **not** to edit the live course files yourself. Your output is a set of
  new markdown documents that the Sonnet session will read afterward and use to implement changes
  with its own established (and hard-won — see "Known authoring gotchas" below) editing discipline.

Do not commit or push anything to git. Do not run destructive git commands. Just read source files,
research externally, and write your output files. Leave version control to the user.

## The project, in one paragraph

This repo holds two self-contained, offline, browser-based cybersecurity learning apps (no build
step, no CDN, no server — single HTML files with an inlined React 18 UMD runtime). One teaches
**application security for full-stack web developers**. The other teaches **cybersecurity broadly**
(networking, blue team, forensics, pentesting, cloud, AI security, career pathways — every branch,
not just web/AppSec). Both are actively studied by the repo owner, a full-stack developer learning
security. Your audit covers **both** courses.

## Exact file map (note the literal space in the folder name)

```
./ (repo root — note the literal space in "cyber-full stack")
├── cyber-full stack/
│   ├── full_stack_appsec_app.html            <- LIVE / CANONICAL interactive reader (React data-model). This is what the student actually studies from.
│   ├── full_stack_appsec_app_static.html      <- LEGACY fallback, git-ignored, superseded. Do not treat as a source of truth; only read it if you need to confirm something the live file is ambiguous about.
│   ├── full_stack_appsec_curriculum.md        <- authoring-source markdown, meant to be kept in parallel with the HTML but has drifted out of sync in places. Prefer the HTML as ground truth for current content.
│   ├── START_HERE_appsec.md                   <- student-facing course map / priority order
│   └── MY_SETUP_M2PRO.md                      <- personal hardware notes, gitignored, irrelevant to your task
├── cyber-guardians/
│   ├── cyber_guardians_app.html               <- LIVE / CANONICAL interactive reader for the broad course
│   ├── cyber_guardians_curriculum.md          <- authoring-source markdown, parallel-maintained, may drift
│   └── MY_SETUP_M2PRO.md                      <- irrelevant to your task
└── README.md
```

**Treat the two `*_app.html` files as ground truth for "what currently exists."** The `.md`
curriculum files are useful for readable context but have historically lagged behind the HTML.

## Current shape of each course (as of this audit — verify against the live files, don't trust this snapshot blindly for anything you plan to cite precisely)

### Full-Stack AppSec (`full_stack_appsec_app.html`)
Audience: a web developer becoming security-capable in their own stack. Web-first, not
general-security. 12 phases (`p0`–`p10`, plus `p7_5` for AI/LLM security), ~60 modules total
including 4 capstones. Phase list:

```
Phase 0  · Computer, Web, Code & Terminal Basics
Phase 1  · Web, Internet & CLI Foundations
Phase 2  · Secure JavaScript & Browser Security
Phase 3  · Backend, API & Database Security
Phase 4  · OWASP Top 10 & Web Exploitation Labs
Phase 5  · Burp Suite, ZAP & Professional Testing
Phase 6  · Authentication, Authorization & Sessions
Phase 7  · Secure SDLC, DevSecOps & Supply Chain
Phase 7.5· AI / LLM Application Security
Phase 8  · Cloud, Deployment & Production Security
Phase 9  · Logging, Monitoring & Incident Response
Phase 10 · Portfolio Capstones
```

Every module's `body` field follows an established **gold-standard pattern** — do not propose
deviating from it, propose new *content* that fills it:

```
"Why this matters" callout
### 🎯 Concept — root cause explained, terms defined in-place
### ⚔️ Hands-on — ethics/scope box, then a real reproducible attack lab (localhost / own machine only)
### 🛡️ Defense — the fix, plus a "false-confidence traps" list (common wrong beliefs that feel safe but aren't)
A dual-language section — every module with code shows BOTH Node.js/Express AND Python/Flask
  versions of the vulnerable-then-fixed code, annotated with WHY, not just what
### Knowledge check — 4-6 questions in a collapsible <details> with answers
➡️ Next step — one-sentence bridge to the following module
```

Module object schema (JS, inlined as static data — this is a splice-into-HTML architecture, not
JSX source): `{ id, phaseId, num, title, objective, body, tracker[] }`. `body` is a giant template
literal of markdown-ish text rendered by a bespoke offline renderer.

### Cyber Guardians (`cyber_guardians_app.html`)
Audience: broad — anyone from "curious beginner" to someone aiming at a security career, covering
networking, OS hardening, cryptography, Linux, Nmap/Wireshark/Burp, OWASP Top 10, blue team,
zero trust, ethical hacking methodology, MITRE ATT&CK, vuln assessment, forensics, incident
response, malware analysis, AI-powered attacks/defenses, cloud & mobile security, IoT/critical
infrastructure, scripting, red-vs-blue, career pathways & certifications, graduation capstone.
3 levels (Recruit / Operator / Specialist), 35 modules (`m0`–`m29`, several `_5`-suffixed
insertions like `m16_5`, `m18_5`, `m24_5`, `m25_5` from recent expansions), each paired with a
real-world breach case study (Colonial Pipeline, SolarWinds, Log4Shell, Equifax, Stuxnet, etc.).

Module object schema (**stricter than AppSec's — this renderer only supports a defined markdown
subset and only consumes specific named fields; do not invent new ones, they will be silently
ignored**):
```
{ id, level, num, title,
  objective,                                  // -> <p>
  theory: `...markdown...`,                   // supports #/##/###/#### headings, -/1. lists,
                                                //   tables, blockquotes, inline <details>, ```lang
                                                //   code fences (bash/powershell/js/python/sql),
                                                //   **bold**, *italic*, `code`, [text](url)
  lab: { mac: `...`, windows: `...`, linux: `...` },   // OS-tabbed hands-on lab
  caseStudy: { title, body },
  challenges: [ { q, a } ],                    // "Try It Yourself" with reveal
  quiz: [ "q1", "q2", ... ],
  tracker: [ "item1", ... ] }
```
Dual-language (Node.js + Python) vulnerable/secure code lives *inside* `theory` as fenced code
blocks (there is no separate `codeExamples` field — the renderer ignores one if you invent it).
Same gold-standard pattern as AppSec: naive/vulnerable approach → why it fails → fix, with pitfalls
and quiz answers, but organized as Theory → Lab → Case Study → Try It Yourself → Quiz → Tracker.

### Known authoring gotchas (for your awareness — you're not editing HTML, but your drafted content will be, so write with these in mind)
- A literal `</script>` inside any example payload (XSS/CSRF demos, etc.) will terminate the real
  `<script>` element early when spliced into the HTML. When you draft example payloads that contain
  a closing script tag, note in your blueprint that it needs the `<\/script>` escape treatment —
  you don't have to escape it yourself in the blueprint prose, just flag it so Sonnet doesn't miss it.
- Cyber Guardians' `theory` field is a JS template literal — backticks and `${...}` inside any code
  you draft for it will need escaping on the implementation side. Again: flag, don't fix yourself.

## Your mission

**Benchmark the full content of both courses against the widest reasonable set of global,
recognized security standards, frameworks, and certification bodies — the ones an employer
anywhere in the world would actually check for — and produce a detailed blueprint of every
gap, blind spot, and expansion opportunity, with a drafted fix for each wherever you can
reasonably draft one.**

The goal: a graduate of these two courses should be able to walk into an AppSec engineer role, a
SOC analyst role, a pentest role, or a GRC-adjacent role **anywhere** — US, EU, UK, APAC — and have
the vocabulary, mental models, and hands-on reflexes that role expects, with nothing that reads as
a regional or dated blind spot.

### Standards / frameworks / certifications to benchmark against

Research current (2026) editions/versions where you're not certain — your training data may lag,
and citing a superseded version number undermines the whole point of this audit. Cite your sources
inline (name + version + date) for every standard you reference, so Sonnet can spot-check later.

**Web/App/API security**
- OWASP Top 10 (Web) — confirm current edition
- OWASP API Security Top 10
- OWASP Top 10 for LLM Applications
- OWASP ASVS (Application Security Verification Standard)
- OWASP MASVS / MASTG (Mobile)
- OWASP SAMM (Software Assurance Maturity Model)
- OWASP Testing Guide + Cheat Sheet Series (spot-check a few high-value cheat sheets against course depth)

**Governance / risk / architecture**
- NIST Cybersecurity Framework (CSF)
- NIST SP 800-53 (security controls)
- NIST SP 800-63B (digital identity, auth strength)
- NIST SP 800-218 (Secure Software Development Framework)
- NIST NICE Workforce Framework (role/competency mapping — useful for the Career Pathways module)
- ISO/IEC 27001 / 27002 (ISMS), 27017/27018 (cloud/privacy extensions)
- CIS Controls (current version) + relevant CIS Benchmarks

**Threat modeling / adversary knowledge**
- MITRE ATT&CK (and D3FEND for defensive mapping)
- CWE Top 25 Most Dangerous Software Weaknesses
- STRIDE / PASTA threat-modeling methodologies (check whether either course teaches a formal
  threat-modeling framework at all — this is a plausible blind spot)

**Certification exam objectives (map course coverage against these directly — this is the clearest
"would this graduate pass X" test)**
- CompTIA Security+, Network+, CySA+, PenTest+
- (ISC)² CISSP (domains only — full depth isn't realistic, but check for *coverage gaps* at the
  domain level, e.g. physical security, BC/DR, GRC) and SSCP
- EC-Council CEH
- GIAC/SANS: GSEC, GWEB, GPEN, GCIH (the AppSec course already references GWEB/eWPT/OSWA/BSCP
  badges — verify those are still accurately described and check for others worth adding)
- Offensive Security OSCP, OSWA, OSWE
- CREST CRT (UK/EU-recognized — important for the "anywhere" goal, not just US-centric certs)
- INE/eLearnSecurity eWPT, eCPPT

**Cloud-specific**
- AWS Well-Architected Framework — Security Pillar
- Microsoft/Azure Security Benchmark
- Google Cloud Security Foundations
- Kubernetes/CNCF security best practices (both courses touch containers/K8s — check depth)

**Supply chain / DevSecOps**
- SLSA (Supply-chain Levels for Software Artifacts)
- SBOM standards (CycloneDX, SPDX) — course already mentions CycloneDX, verify still current
- OpenSSF Scorecard

**Privacy / compliance (breadth, not depth — these courses aren't compliance courses, but a
"global" graduate should recognize the vocabulary and know when to escalate to a specialist)**
- GDPR (EU), CCPA/CPRA (California), PCI-DSS (current version), HIPAA (US health), SOC 2,
  and note explicitly if the course is US-centric anywhere it doesn't need to be

### What counts as a "blind spot" for this audit
- A topic a named standard/cert/employer would expect that **doesn't exist anywhere** in either
  course.
- A topic that exists but is shallower than the standard it maps to (e.g., mentions a concept in
  passing where the standard treats it as a core competency).
- Content that reads as outdated relative to the current (2026) threat landscape or current
  standard versions — call these out explicitly with what changed and since when.
- Regional/US-centric framing where a global framing would cost little and add real value.
- Structural gaps between the two courses' rigor — e.g., if AppSec is missing a layer (quiz,
  case-study) the broad course has, or vice versa, and that gap maps to a real pedagogical loss
  (not just a formatting inconsistency — that's implementation's problem, not yours, unless it
  blocks a standards-mapping goal).

### What is explicitly OUT of scope for you
- Tool ARM64/M-series-Mac compatibility notes — already tracked separately, not your concern.
- UI/UX bugs, broken anchors, HTML rendering issues — not your concern unless a bug is actively
  hiding content from a standards-coverage standpoint.
- Anything that would require inventing new module schema fields or changing the renderer/format.
  Work within the existing field contracts described above.
- Editing the live `.html`/`.md` files yourself.

## Deliverable: output location and structure

Create a new folder at the repo root: `global-standards-blueprint/`. Write these files:

```
global-standards-blueprint/
├── 00-INDEX.md                    <- start here: executive summary, methodology, standards
│                                      checked (with versions/dates/sources), overall verdict per
│                                      course, how to use the other files, priority order for
│                                      Sonnet to work through the findings
├── 01-appsec-fullstack-gaps.md    <- full findings for the AppSec course
├── 02-cyber-guardians-gaps.md     <- full findings for the broad course
└── 03-standards-crosswalk.md      <- a matrix: standard/cert -> which module(s) currently cover
                                      it (by exact id/title) -> coverage verdict (Meets / Partial /
                                      Gap) -> pointer to the relevant finding entry
```

If a single course's findings file would be unreasonably huge, you may split it further (e.g.
`01a-appsec-web-owasp.md`, `01b-appsec-cloud-devsecops.md`) — just keep `00-INDEX.md` as the map
to everything, and keep filenames self-describing.

### Format for every individual finding (in the `01-*` / `02-*` files)

Use this exact structure per finding so Sonnet can implement mechanically without re-deriving your
reasoning:

```markdown
## [Course] — [existing module id/title, or "NEW MODULE"]

**Standard(s)/cert(s) this closes a gap for:** name + version/date + source
**Severity:** Blind spot (nothing exists) | Shallow (exists but thin) | Stale (exists but outdated) | Nice-to-have expansion
**Integration point:** exact location — e.g. "new subsection in Module 2.2 (id: m2-2), inserted
  after the 🛡️ Defense section, before the dual-language code section" or "new module, insert as
  m8_5 between [existing module] and [existing module]" or "extend the existing Career Pathways
  module (m28) with a new subsection on X"

**Why this is a gap:** 2-4 sentences, concrete, cites the standard's actual requirement.

**Drafted content:**
[Full gold-standard-pattern draft, ready to adapt into the module's body/theory field — Concept /
Attack-with-ethics-box / Defense / dual-language Node+Python code / pitfalls / knowledge-check
questions, matching the course's existing voice and depth. If genuinely too large to fully draft
in one pass, write a detailed outline instead AND label it clearly: "OUTLINE ONLY — needs a full
authoring pass" so it isn't mistaken for finished content.]

**Flags for the implementer:** any `</script>`-in-payload, backtick/`${}`-escaping, or other
mechanical gotchas your drafted content will trigger when spliced in.
```

### Quality bar
- Every claim about what a standard requires must be traceable to a real, named, current source —
  don't paraphrase from memory if you're not confident it's still accurate; verify.
- Every finding must be **actionable without further research** by whoever implements it — exact
  location, exact standard, drafted content or a genuinely useful outline, not vague suggestions
  like "could add more on cloud security."
- Prioritize breadth-with-real-depth over exhaustiveness-for-its-own-sake: a handful of
  well-drafted, high-value closes of genuine blind spots beats fifty superficial "consider adding"
  notes.
- Don't duplicate what's already strong. Read enough of both live HTML files first (they're large —
  several thousand lines each; use search/grep for section titles rather than reading linearly) to
  know what's already covered before flagging something as missing.

## Suggested working order

1. Read `START_HERE_appsec.md` and skim both `*_app.html` files' module/phase title lists (grep for
   `title:` and `name:` inside the `curriculum`/`modules` JS objects — much faster than reading
   sequentially) to build an accurate map of current coverage.
2. Research current versions/requirements of the standards list above; note anything that's shifted
   since a training-data cutoff might suggest.
3. Build the crosswalk matrix (`03-standards-crosswalk.md`) — this is your own gap-finding tool as
   much as a deliverable.
4. Write the findings files, drafting content as you go.
5. Write `00-INDEX.md` last, once you know what you actually found, with an honest executive
   summary — including saying so plainly if a course is already in strong shape against most
   standards and only has a handful of real gaps. Don't manufacture findings to look thorough.

Take the time this deserves — this is meant to be a genuinely deep audit, not a quick pass.
