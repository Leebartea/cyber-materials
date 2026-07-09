# 01 · Full-Stack AppSec — Gap Findings & Drafted Fixes

Course file: `cyber-full stack/full_stack_appsec_app.html` (ground truth).
Module schema: `{ id, phaseId, num, title, objective, body, tracker[] }`; `body` is a markdown-ish
template literal rendered by the bespoke offline renderer. Drafted content below is written to drop
into `body` fields in the course's existing voice (Why-callout → 🎯 Concept → ⚔️ Hands-on with
ethics box → 🛡️ Defense with false-confidence traps → dual-language Node+Python → Knowledge check
→ ➡️ Next step). Escaping gotchas are flagged per finding.

**Headline:** This course is in **strong** shape. The one genuinely urgent finding is **AS-1** —
both the web and (in the other file) broad course still teach the **OWASP Top 10 2021** set, and
the **2025 edition is final** with two brand-new categories and a reshuffle. Everything else is
either a missing *standard name* over content that already exists (AS-2, AS-3, AS-4, AS-5), or a
genuine new-topic blind spot that the 2026 landscape now demands (AS-6 post-quantum, AS-7 EU
regulatory, AS-8 agentic AI).

Findings are ordered by priority.

---

## AppSec — Phase 4 (`m4_1`, `m4_2`, `m4_3`) + all A0x cross-references

**Standard(s)/cert(s) this closes a gap for:** OWASP Top 10:2025 (final, released Nov 2025 —
https://owasp.org/Top10/2025/). Also feeds CWE Top 25 (2025), and every job-description/audit that
now references the 2025 list.
**Severity:** Stale (exists but outdated) — **highest priority in the course.**
**Integration point:** Phase 4 is the anchor, but A0x labels are threaded through the *entire*
course (grep found A01–A10 references in Phases 2, 3, 4, 6, 8). This is a **course-wide relabel +
two new-category inserts**, not a single-module edit. Update: `m4_1` (the "Top 10 as threat-model
lens" table), `m4_2` (lab mapping), `m4_3` (reporting), and every inline `A0x` mention elsewhere.

**Why this is a gap:** The course teaches the **2021** category set (confirmed: `m4_2` maps
"A01 Access Control / A02 Crypto / A03 Injection …", the 2021 ordering). OWASP Top 10:2025 is now
final and changed materially:

- **A01:2025 Broken Access Control** (still #1; **SSRF from 2021's A10 folded into A01**)
- **A02:2025 Security Misconfiguration** (up from #5)
- **A03:2025 Software Supply Chain Failures** — **NEW**, expanded from 2021's "Vulnerable & Outdated Components"
- **A04:2025 Cryptographic Failures**
- **A05:2025 Injection**
- **A06:2025 Insecure Design**
- **A07:2025 Authentication Failures**
- **A08:2025 Software or Data Integrity Failures**
- **A09:2025 Security Logging and Alerting Failures** (note: "Alerting", not just "Monitoring")
- **A10:2025 Mishandling of Exceptional Conditions** — **NEW** (error/exception handling, fail-open logic)

A graduate who walks into an interview describing "the 2021 Top 10" now reads as a year behind. The
good news: the course *already teaches* the content behind both new categories — supply chain is
`m7_2`/`m1-5`, and exceptional-condition/fail-open handling is touched in `m3_1` and `m9_x`. This is
mostly a **relabel-and-cross-reference** job, plus one new short subsection for A10.

**Drafted content:**

Replacement for the `m4_1` category table (drop-in for the 🎯 Concept section):

```markdown
### 🎯 Concept: the OWASP Top 10 (2025 edition) in developer terms

OWASP refreshed the Top 10 in 2025. Two things changed that you must know by name:

- **Supply chain got its own category (A03:2025).** In 2021 this was a narrow "vulnerable and
  outdated components." In 2025 it's **Software Supply Chain Failures** — dependencies, build
  systems, CI/CD, and the artifacts you ship. This is the fastest-growing attack class (SolarWinds,
  xz-utils, npm typosquats). You cover the defenses in Phase 7 — now you have the label for them.
- **A new A10:2025 — Mishandling of Exceptional Conditions.** When your error handling fails
  *open* (a try/catch that swallows an authz check, a default that grants instead of denies, a
  timeout that skips validation), the exception becomes the vulnerability. This is why "fail
  closed" is a security rule, not just a reliability one.

| 2025 rank | Category | The developer question to ask every feature |
|---|---|---|
| A01 | Broken Access Control (now includes **SSRF**) | Can user A reach user B's object? Can the server be tricked into making requests for the attacker? |
| A02 | Security Misconfiguration | Are defaults hardened? Debug off? Headers set? Buckets private? |
| A03 | **Software Supply Chain Failures** | Do I know every dependency and build input, and can I prove they weren't tampered with? |
| A04 | Cryptographic Failures | Is sensitive data encrypted correctly in transit and at rest, with modern algorithms? |
| A05 | Injection | Does any user input reach an interpreter (SQL, shell, HTML, template) unparameterized? |
| A06 | Insecure Design | Did we threat-model this feature before building it? |
| A07 | Authentication Failures | Can identity be forged, brute-forced, or bypassed? |
| A08 | Software or Data Integrity Failures | Are updates, deserialization, and CI/CD steps integrity-verified? |
| A09 | Security Logging and **Alerting** Failures | Would we detect this attack, and would anyone be alerted? |
| A10 | **Mishandling of Exceptional Conditions** | When something fails, does it fail *closed*? |

> **Migration note for your notes/journal:** if you learned the 2021 list, the two you need to
> re-anchor are **A03 (supply chain, promoted)** and **A10 (exceptional conditions, new)**, and
> remember **SSRF is no longer its own number — it lives under A01 now.**
```

New short subsection to add to `m4_1` (or as a labeled callout in `m3_1`) for the genuinely new
A10 concept, since it's the one topic the course doesn't already cover under another name:

```markdown
### ⚔️ Hands-on: make an app fail *open*, then fail *closed* (A10:2025)

> **Ethics & scope:** your own localhost Express/Flask app only. This is a logic demo, not an
> attack on anything you don't own.

Fail-open bug: an authorization middleware that grants access when its own check throws.

Node/Express — the trap:
```js
// VULNERABLE: if getRole() throws (DB blip, cache miss), the catch lets the request through
async function requireAdmin(req, res, next) {
  try {
    const role = await getRole(req.user.id);
    if (role === 'admin') return next();
    return res.status(403).end();
  } catch (e) {
    return next();            // FAIL-OPEN: an exception becomes an authz bypass (A10 -> A01)
  }
}
```
```js
// FIXED: any exception denies. Fail closed, always.
async function requireAdmin(req, res, next) {
  try {
    const role = await getRole(req.user.id);
    return role === 'admin' ? next() : res.status(403).end();
  } catch (e) {
    req.log?.error({ err: e }, 'authz check failed');
    return res.status(503).end();   // deny + alert (A09), never proceed
  }
}
```

**False-confidence traps:**
- "The catch is just for resilience, it can't be a security bug." An exception path that skips a
  control *is* the control's bypass. Every catch around a security decision must deny.
- "It only throws on rare infra errors." Attackers *cause* those errors (connection exhaustion,
  malformed input that trips the parser) precisely to reach the fail-open branch.
```

**Flags for the implementer:** none for scripts here. When you relabel A0x mentions course-wide,
grep for the literal strings `A01`–`A10` and `2021` to catch every cross-reference; several live
outside Phase 4. No `</script>` or backtick issues in this draft.

---

## AppSec — NEW subsection in `m4_1` (id: `m4_1`) + course-level framing

**Standard(s)/cert(s) this closes a gap for:** OWASP ASVS 5.0.0 (30 May 2025, 14 chapters, L1/L2/L3
— https://asvs.dev/); STRIDE threat modeling (Microsoft/Shostack); feeds GWEB, CISSP Domain 3/8.
**Severity:** Blind spot (ASVS is never named anywhere; no *formal* threat-modeling methodology).
**Integration point:** Two small additions. (1) A new "Verifying your work against a standard —
ASVS" callout at the end of `m4_1`, and referenced again from the capstone `m10_1`. (2) A named
threat-modeling method (STRIDE) added to `m4_1`'s existing "four questions" concept, since the
course already does Shostack's four-question frame but never gives it or STRIDE a name.

**Why this is a gap:** The course teaches excellent *ad hoc* verification and a Shostack-style
four-question threat model (`m4_1`), but never names **ASVS** — the OWASP standard that turns "is
my app secure?" into a checklist with verifiable requirements at three assurance levels. Any AppSec
engineer role expects the candidate to say "we target ASVS L2." Similarly, the course teaches
threat modeling as a mindset but never gives a **named methodology** (STRIDE / PASTA / attack
trees). ASVS 5.0 and SAMM both expect a named method. This is a small, high-leverage add: the
content exists, it just needs the vocabulary.

**Drafted content:**

```markdown
### 🎯 Concept: naming what you already do — STRIDE and ASVS

You've been threat-modeling with four questions (what are we building / what can go wrong / what
do we do / did we check). The industry gives the "what can go wrong" step a named checklist:
**STRIDE**. For each trust boundary, walk the six letters:

| STRIDE | Threat | The property it violates | Example in your stack |
|---|---|---|---|
| **S** | Spoofing | Authentication | Forged JWT, session fixation |
| **T** | Tampering | Integrity | Modifying a price in a request, mass assignment |
| **R** | Repudiation | Non-repudiation | No audit log, so "it wasn't me" can't be disproved |
| **I** | Information disclosure | Confidentiality | IDOR leaking another user's record, verbose errors |
| **D** | Denial of service | Availability | Unbounded query, no rate limit (ties to LLM cost DoS) |
| **E** | Elevation of privilege | Authorization | BFLA, path to admin, container escape |

STRIDE gives you a *systematic* way to not miss a category — it maps almost one-to-one onto the
OWASP Top 10 you just learned.

**Then: how do you know you're *done*?** That's **OWASP ASVS 5.0** (Application Security
Verification Standard, released May 2025). ASVS is a list of ~350 concrete, testable requirements
organized into 14 chapters (auth, session, access control, validation, crypto, etc.) at three
levels:

- **L1** — the baseline every app should meet; testable from outside (black-box).
- **L2** — the standard target for most apps handling meaningful data (**aim here**).
- **L3** — high-assurance (payments, health, critical infrastructure).

**How to use it as a developer:** pick a chapter (say, ASVS V6 Session Management), read its L2
requirements, and turn each into a test. "V6.2.1 — session tokens are generated with a CSPRNG" is
something you can *verify*, not just hope for. When someone asks "how secure is this app?", "it
meets ASVS L2, here's the checklist" is a far stronger answer than "we followed best practices."

> **Career note:** "We target ASVS L2 and threat-model with STRIDE" is a sentence that signals
> maturity in an AppSec interview anywhere in the world. Both are vendor-neutral, globally
> recognized, and free.
```

Add to the `m10_1` capstone tracker:
```markdown
- [ ] Map the secured app against OWASP ASVS 5.0 L2 for at least 3 chapters (Auth, Session,
      Access Control); note which requirements you meet and which you consciously don't.
```

**Flags for the implementer:** none. Pure prose + a markdown table. No escaping issues.

---

## AppSec — `m6_1` Password Storage / `m6_2` Sessions / `m6_6` WebAuthn

**Standard(s)/cert(s) this closes a gap for:** NIST SP 800-63B-4 Digital Identity Guidelines
(final 31 Jul 2025 — https://csrc.nist.gov/pubs/sp/800/63/b/4/final). Feeds Security+, CISSP,
GWEB.
**Severity:** Shallow (strong practice, missing the standard's name and two current rules).
**Integration point:** A short "What NIST 800-63B-4 actually requires" callout inside `m6_1`,
after the Argon2id deep-dive (which is already excellent), plus one row in the false-confidence
traps.

**Why this is a gap:** `m6_1` is one of the strongest modules in the course — Argon2id, memory-
hardness, pepper via HMAC, the whole thing is right. But it **never cites NIST SP 800-63B**, which
is *the* globally referenced authority a graduate will be asked about by name. It also omits two
specific, currently-testable 800-63B-4 rules: the **15-character minimum when a password is the
only factor**, and the **"screen against breached-password lists"** requirement (the course teaches
strength but not the breach-corpus check). Adding the citation turns "good practice" into "provably
standards-aligned."

**Drafted content:**

```markdown
### 🎯 Concept: what NIST SP 800-63B-4 actually requires (and what it now forbids)

Everything above (Argon2id, per-user salt, pepper) is the *how*. **NIST SP 800-63B-4** (the July
2025 revision of the US digital-identity standard, and the reference the rest of the world cites
too) is the *what* — the rules an auditor checks. The current, sometimes-surprising requirements:

- **Length over complexity.** Minimum **15 characters when the password is the only
  authenticator** (8+ when it's one factor inside MFA). Support at least **64 characters**, allow
  **spaces and all printable Unicode**. A long passphrase beats a short `P@ssw0rd!`.
- **No composition rules.** 800-63B-4 says you **shall not** require "1 upper, 1 number, 1 symbol."
  Those rules push users toward predictable patterns and add little entropy.
- **No forced periodic rotation.** Do **not** expire passwords on a schedule. Force a change
  **only on evidence of compromise**. (Rotation theater is now an explicit anti-pattern.)
- **Screen against breach corpora.** On set/change, reject passwords found in known-breached lists
  (e.g. a local copy of Have I Been Pwned's k-anonymity range API set, or an offline bloom filter).
  This is a *requirement*, not a nice-to-have — and it's the one most homegrown auth systems miss.
- **No password hints, no knowledge-based "security questions."**

**Map it to what you built:** your Argon2id storage satisfies the *verifier* requirements; the
list above is the *policy* layer you enforce at registration and password-change time.
```

Add to the module's false-confidence traps list:
```markdown
- "We enforce complexity rules, so our passwords are strong." NIST 800-63B-4 explicitly tells you
  to *drop* composition rules and instead enforce length + a breached-password screen. Complexity
  rules are now considered harmful.
- "We rotate passwords every 90 days for safety." 800-63B-4 forbids scheduled rotation absent
  evidence of compromise — it drives weaker, incrementing passwords (`Spring2026!` -> `Summer2026!`).
```

**Flags for the implementer:** none. Prose + list. No code fences with backticks-in-backticks. If
you add a small breach-screen code example, note the HIBP range API is an *online* call — keep the
course's offline-lab ethos by demoing the k-anonymity hash prefix locally.

---

## AppSec — NEW cross-cutting callout, anchored in `m4_1` and reused in `m9_2`

**Standard(s)/cert(s) this closes a gap for:** CWE (Common Weakness Enumeration) & CWE Top 25 2025
(11 Dec 2025 — https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html). Feeds CVSS/CVE
workflows, Security+, CySA+, every scanner output.
**Severity:** Shallow/Blind spot — CWE is never referenced despite heavy CVE/CVSS use.
**Integration point:** One short "OWASP names risk *classes*; CWE names the *specific weakness*"
callout in `m4_1`, plus adding CWE IDs to the existing vulnerability modules (a one-line
`**CWE:** CWE-79 (XSS)` tag under each vuln's Concept heading).

**Why this is a gap:** Every real vulnerability report, scanner finding (Semgrep, CodeQL, Snyk),
and CVE is tagged with a **CWE ID**, and the **CWE Top 25** is a distinct industry list from the
OWASP Top 10 (2025's #1 CWE is **CWE-79 XSS**, then **CWE-89 SQLi**, then **CWE-352 CSRF**). The
course teaches all these weaknesses deeply but never gives students the CWE vocabulary to map their
knowledge onto tool output and CVE records. Cheap to fix, high recognition value.

**Drafted content:**

```markdown
### 🎯 Concept: OWASP is the risk, CWE is the weakness

Two lists, different jobs:
- **OWASP Top 10** = broad *risk categories* for awareness (A01–A10).
- **CWE (Common Weakness Enumeration)** = a precise catalog of *specific* software weaknesses,
  each with an ID. When Semgrep or CodeQL flags your code, when a CVE is filed, when a bug-bounty
  triager rates your report — they speak **CWE**.

The **CWE Top 25 (2025)** is the industry's "most dangerous weaknesses" list. Its top three are
weaknesses you already know cold:

1. **CWE-79** — Cross-Site Scripting (Phase 2)
2. **CWE-89** — SQL Injection (Phase 3)
3. **CWE-352** — Cross-Site Request Forgery (Phase 2)

…followed by CWE-78 (OS command injection), CWE-22 (path traversal), CWE-434 (unrestricted upload,
your Phase 3 file-upload module), CWE-862 (missing authorization), and memory-safety weaknesses
(CWE-787/125/416) that matter when you touch native code or WASM. Learn to say "that's a CWE-89"
— it's the lingua franca of scanners and disclosure.
```

Then a one-line tag under each existing vuln module's Concept (mechanical):
```markdown
**CWE:** CWE-79 (Improper Neutralization of Input During Web Page Generation)   <!-- m2-2 XSS -->
**CWE:** CWE-89 (SQL Injection)                                                 <!-- m3_2 -->
**CWE:** CWE-352 (Cross-Site Request Forgery)                                    <!-- m2-3 -->
**CWE:** CWE-434 (Unrestricted Upload of File with Dangerous Type)               <!-- m3_4 -->
**CWE:** CWE-918 (Server-Side Request Forgery)                                   <!-- m8_3 -->
**CWE:** CWE-611 (XXE) / CWE-502 (Insecure Deserialization)                      <!-- where relevant -->
```

**Flags for the implementer:** none. Tags are plain text. The HTML comments above are just to help
you place them — don't paste the comments into `body`.

---

## AppSec — `m7_1` Secure SDLC / `m7_2` Supply Chain

**Standard(s)/cert(s) this closes a gap for:** NIST SP 800-218 SSDF v1.1
(https://csrc.nist.gov/pubs/sp/800/218/final); OWASP SAMM 2.0; SLSA v1.2 (Nov 2025); OpenSSF
Scorecard. Feeds US federal software-attestation requirements.
**Severity:** Shallow — the practices are taught; the framework names (SSDF, SAMM) and a SLSA
version bump are missing.
**Integration point:** A "The SSDF — the framework auditors use" callout in `m7_1` after the
existing shift-left concept; a one-line SLSA version note in `m1-5`/`m7_2`; a mention of OpenSSF
Scorecard in `m7_2`.

**Why this is a gap:** `m7_1` teaches shift-left and a secure SDLC beautifully but never names
**NIST SSDF (SP 800-218)** — the framework the US government now requires software producers to
attest to, and the one that maps directly to the CI/CD security work in `m7_2`. SLSA is taught
(good) but may cite v1.0; current is **v1.2** (Nov 2025, which promoted the Source track). Adding
SSDF's four practice groups (PO/PS/PW/RV) gives the whole phase a recognized spine.

**Drafted content:** OUTLINE ONLY — needs a full authoring pass (the content it maps to already
exists across Phase 7, so this is framing + a mapping table, not new labs):

- **Concept callout — "Meet the SSDF (NIST SP 800-218)."** Explain it's the US federal baseline for
  secure software development and what its four practice groups mean, then map each to work the
  student already did:
  - **PO — Prepare the Organization** (security requirements, roles) → `m4_1` threat modeling
  - **PS — Protect the Software** (protect code/releases, integrity) → `m7_2` signing, SLSA, SBOM
  - **PW — Produce Well-Secured Software** (secure design, review, testing) → Phases 2–5, `m7_1` SAST/DAST
  - **RV — Respond to Vulnerabilities** (find, remediate, disclose) → `m9_x`, `m7_2` dependency mgmt
- **One-liner:** "When a customer or the US government asks for a 'secure development attestation,'
  they mean SSDF. You've done the work — now you know its name."
- **SLSA version note:** update any "SLSA v1.0" reference to **v1.2 (Nov 2025)**; add one sentence
  that v1.2 promoted the **Source track** (tamper-evident source history) alongside the Build track
  levels L0–L3.
- **OpenSSF Scorecard mention:** one line in `m7_2` — an automated tool that scores a repo's supply
  chain hygiene (branch protection, signed releases, pinned deps, no dangerous workflows); pairs
  with SLSA as the "how healthy is this dependency?" check before you add it.
- **Optional SAMM one-liner:** name OWASP SAMM 2.0 as the *maturity* counterpart to SSDF for teams.

**Flags for the implementer:** none — framing prose and a mapping table. No payloads.

---

## AppSec — `m1-2` (DNS/TLS) + `m8_2` (production crypto) — NEW subsection

**Standard(s)/cert(s) this closes a gap for:** NIST FIPS 203 (ML-KEM), 204 (ML-DSA), 205 (SLH-DSA)
finalized Aug 2024; HQC selected Mar 2025; US Executive Order setting **2030** (key establishment)
/ **2031** (signatures) federal migration deadlines, quantum-vulnerable algorithms **deprecated by
2030, disallowed by 2035**. Sources: https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards
**Severity:** Blind spot — **zero** post-quantum coverage in either course; now a board-level topic.
**Integration point:** New subsection in `m1-2` (right after the TLS handshake explanation) titled
"Crypto-agility and the post-quantum transition," ~cross-referenced from `m8_2`.

**Why this is a gap:** FIPS 203/204/205 are finalized standards, browsers and TLS libraries now
ship **hybrid post-quantum key exchange (X25519MLKEM768)** by default, and the "harvest now,
decrypt later" threat means data encrypted today with RSA/ECDH is already at risk. A full-stack dev
in 2026 needs to (a) understand crypto-agility as a design property and (b) recognize the migration
is underway, not theoretical. This is the highest-value *new-topic* add for the AppSec course.

**Drafted content:**

```markdown
### 🎯 Concept: crypto-agility and the post-quantum transition

Everything you rely on for confidentiality online — TLS key exchange (ECDH), digital signatures
(RSA/ECDSA) — rests on math a large **quantum computer** could break. That computer doesn't exist
yet at scale, but two facts make this your problem *now*:

1. **Harvest now, decrypt later.** Adversaries are recording encrypted traffic today to decrypt
   once quantum hardware arrives. Anything with a long confidentiality lifetime (health records,
   state secrets, your users' data) is already exposed to a future break.
2. **The standards are done.** In August 2024 NIST finalized the first post-quantum algorithms:
   **FIPS 203 (ML-KEM**, key encapsulation, formerly Kyber**)**, **FIPS 204 (ML-DSA**, signatures,
   formerly Dilithium**)**, and **FIPS 205 (SLH-DSA**, hash-based signatures**)**. A fourth,
   **HQC**, was selected in March 2025 as a backup KEM. This is no longer research — it's a
   migration project with government deadlines (US federal: key establishment by **2030**,
   classical algorithms **disallowed by 2035**).

**What this means for you as a developer — crypto-agility.** You almost never implement crypto
yourself (good — don't). Your job is to make sure your systems can *swap algorithms without a
rewrite*:
- Don't hard-code cipher choices or key sizes across your codebase; centralize them behind config.
- Keep TLS libraries current — modern TLS 1.3 stacks already negotiate **hybrid** key exchange
  (**X25519MLKEM768**: classical + post-quantum together, so you're safe if either holds).
- Inventory where you use asymmetric crypto (TLS, JWT signing, code signing, SSH) — that inventory
  *is* your migration plan.

You don't need to become a cryptographer. You need to (1) not block the transition with brittle,
hard-coded crypto, and (2) be able to say what "post-quantum" and "crypto-agility" mean when a
security review asks.
```

```markdown
### ⚔️ Hands-on: see hybrid post-quantum TLS in your own connection

> **Ethics & scope:** you're inspecting the TLS handshake your *own* browser/client negotiates with
> a public site that already serves it. Reading a public cert/handshake is passive and fine.

```bash
# Modern OpenSSL (3.5+) lists post-quantum / hybrid groups it supports:
openssl list -tls-groups | grep -i mlkem    # look for X25519MLKEM768

# Negotiate against a site with PQC enabled and see the group actually used:
openssl s_client -connect www.cloudflare.com:443 -groups X25519MLKEM768 </dev/null 2>/dev/null \
  | grep -i -E "Negotiated|group|cipher"
```
If your OpenSSL is older than 3.5 it won't offer ML-KEM groups — that itself is the lesson:
**crypto-agility means keeping the library current is a security control, not just maintenance.**
```

**False-confidence traps:**
```markdown
- "Quantum computers don't exist, so this is years away." Harvest-now-decrypt-later means the
  clock started when you first sent the data, not when the quantum computer boots.
- "TLS 1.3 is modern, so I'm covered." TLS 1.3 with *classical-only* groups is still quantum-
  vulnerable. You need the library version that offers hybrid ML-KEM groups.
- "We'll swap the algorithm when we need to." Only if your code is crypto-agile. Hard-coded curve
  names and key sizes scattered across a codebase turn a config change into a multi-quarter project.
```

**Flags for the implementer:** the bash block uses `<` and `>` redirects and a `2>/dev/null` — no
`</script>` sequences, safe to splice. No template-literal backticks inside (this is the AppSec
renderer, not the Guardians one). Verify the `openssl s_client` example still negotiates a hybrid
group at authoring time (the specific default group name evolves — X25519MLKEM768 is current as of
July 2026).

---

## AppSec — `m7_3` Compliance & Privacy Engineering

**Standard(s)/cert(s) this closes a gap for:** EU Cyber Resilience Act (in force 10 Dec 2024;
**reporting obligations apply 11 Sep 2026**; main obligations 11 Dec 2027 —
https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act); NIS2; DORA (applies since
17 Jan 2025); PCI DSS 4.0.1 (current, all reqs mandatory since 31 Mar 2025). Also ISO/IEC 27001:2022.
**Severity:** Stale/Blind spot — `m7_3` is strong on GDPR/PCI/SOC2/HIPAA but has **no EU
software-product regulation** (CRA/NIS2/DORA), and its PCI reference should confirm 4.0.1.
**Integration point:** New "EU software regulation you'll actually be asked about" subsection in
`m7_3` after the GDPR section; a one-line PCI version confirmation; a one-line ISO 27001 name-drop.

**Why this is a gap:** The course's compliance module is genuinely good but **US-centric on the
non-GDPR side**. For the stated "employable anywhere" goal, the biggest miss is the **EU Cyber
Resilience Act**, which for the first time imposes security obligations and **24-hour
actively-exploited-vulnerability reporting** on *any manufacturer of software with digital
elements* — i.e. potentially the student's own product, not just their employer's compliance team.
Its reporting phase starts **11 September 2026** (weeks after this audit's date). NIS2 and DORA
round out the EU picture. This is exactly the "regional blind spot" the brief asks to close.

**Drafted content:**

```markdown
### 🇪🇺 EU software regulation — the CRA, NIS2, and DORA

GDPR is about *personal data*. A newer wave of EU law is about *the software itself* and
*operational resilience* — and as a developer whose product might ship into the EU, the Cyber
Resilience Act can land on **you**, not just your legal team.

**Cyber Resilience Act (CRA) — the big one for product developers.** The CRA sets mandatory
security requirements for "products with digital elements" (basically any connected software or
hardware) sold in the EU. Key facts:
- In force since **10 Dec 2024**. **Vulnerability & incident reporting obligations apply from
  11 Sep 2026**; the full requirements from **11 Dec 2027**.
- If a vulnerability in your product is being **actively exploited**, you must notify ENISA and the
  relevant national CSIRT within **24 hours** of becoming aware. (Compare GDPR's 72-hour *data-
  breach* clock — different trigger, different regulator, tighter deadline.)
- It expects **secure-by-design** development, an **SBOM**, timely security updates for a defined
  support period, and no shipping with known-exploitable vulnerabilities. Everything you learned in
  Phase 7 (SBOM, dependency management, signed releases) is how you *comply* with the CRA.

**NIS2 Directive.** Raises baseline cybersecurity and incident-reporting duties for "essential" and
"important" entities across many sectors (energy, transport, health, digital infrastructure,
managed service providers). If your employer is in scope, expect risk-management measures, supply-
chain security duties, and 24h/72h incident reporting. Applicable across the EU since national
transposition (deadline was Oct 2024).

**DORA (Digital Operational Resilience Act).** Applies since **17 Jan 2025** to the EU financial
sector (and their ICT providers). Five pillars: ICT risk management, incident reporting,
resilience testing, third-party (ICT vendor) risk, and information sharing. If you build fintech or
sell software *to* a bank in the EU, DORA flows down to you contractually.

> **The one-sentence takeaway:** GDPR asks "did you protect the data?"; the CRA asks "did you build
> and maintain the product securely, and do you report exploited holes within 24 hours?" A globally
> employable developer knows both exist and which regulator each answers to.
```

Small edits in the same module:
```markdown
- Confirm the PCI reference reads **PCI DSS 4.0.1** — the only valid version since 31 Dec 2024,
  with *all* requirements (including MFA for all CDE access and 12-character passwords) mandatory
  since 31 Mar 2025. (The module currently cites "PCI DSS 6.4," which is a *requirement number*,
  not the version — make sure the version is stated as 4.0.1 somewhere in the section.)
- Add one line naming **ISO/IEC 27001:2022** as the international ISMS certification an employer
  outside the US is most likely to hold (the 2013→2022 transition closed 31 Oct 2025, so 27001:2022
  is now the only current edition).
```

**Flags for the implementer:** none — prose only, no payloads or code fences with special chars.

---

## AppSec — Phase 7.5 (`m7_5_1`…`m7_5_6`) — extend for agentic AI

**Standard(s)/cert(s) this closes a gap for:** OWASP Top 10 for LLM Applications (2025) — already
covered; **OWASP Top 10 for Agentic Applications (Dec 2025)** and **MCP Top 10** —
https://genai.owasp.org/. Also ISO/IEC 42001 (AI management) & EU AI Act (breadth mention).
**Severity:** Nice-to-have expansion (the LLM phase is strong and current; agentic is the new frontier).
**Integration point:** New module `m7_5_7` "Agentic AI & Tool-Use Security (MCP, autonomous
agents)" inserted after `m7_5_6`, or a large subsection appended to `m7_5_3` (Output Handling and
Tool Safety), which is the natural home.

**Why this is a gap:** Phase 7.5 is genuinely current on the **LLM** Top 10, but the field moved:
in Dec 2025 OWASP released a distinct **Top 10 for Agentic Applications** plus an **MCP (Model
Context Protocol) Top 10**, because autonomous agents that call tools introduce risk classes the
LLM list doesn't cover — excessive agency, tool/skill poisoning, multi-agent trust, persistent-
state poisoning, and confused-deputy attacks via MCP servers. Since this student is a developer
likely wiring LLMs into apps with tool-calling, this is the highest-value *forward-looking* add.

**Drafted content:** OUTLINE ONLY — needs a full authoring pass:

- **🎯 Concept:** the shift from "LLM answers a question" to "agent takes actions." New risk axis =
  **agency**: the more an agent can *do* (call APIs, run code, spend money, touch other agents), the
  more an injection or a poisoned tool description costs you. Introduce the OWASP Agentic Top 10
  themes: excessive agency, tool misuse, memory/state poisoning, identity & impersonation across
  agents, and cascading multi-agent failures.
- **MCP-specific:** Model Context Protocol lets agents connect to tool servers. Threats: a
  malicious/compromised MCP server (supply-chain, ties back to A03:2025), **tool-description
  injection** (the tool's own metadata carries a prompt-injection payload — "confused deputy"),
  over-broad tool scopes, and unauthenticated tool servers. Defense: least-privilege tool scopes,
  human-in-the-loop for high-impact actions, allow-listing MCP servers, treating tool output as
  untrusted input (ties to `m7_5_3`).
- **⚔️ Hands-on:** build a tiny local agent (Node or Python) with two tools — a safe `readFile` and
  a dangerous `runShell` — and show how a prompt-injected document convinces the agent to call
  `runShell`. Then add the fix: an approval gate + scoped tools + output sanitization. Localhost
  only, no external calls.
- **🛡️ Defense + false-confidence traps:** "the model is smart enough to refuse" (injection defeats
  refusal), "read-only tools are safe" (SSRF/exfil via a read tool), "it's just my internal agent"
  (internal agents get the widest scopes and least review).
- **Breadth mention:** name **ISO/IEC 42001** (AI management system) and the **EU AI Act** as the
  governance frameworks a security-aware AI developer should recognize (risk tiers, transparency
  duties) — one paragraph, not a deep dive.
- **Dual-language:** Node + Python agent-with-tools snippets (vulnerable tool-calling loop → gated
  version).

**Flags for the implementer:** **This module's example payloads will contain prompt-injection
strings and possibly a `runShell` demo — if any example includes an HTML/script payload, apply the
`<\/script>` escape.** The agent code is dual-language template-literal code in the AppSec
renderer (backticks only need escaping in the *Guardians* renderer, but if you reuse this content
in Guardians `m24_5`, escape backticks and `${}` there). Keep the shell-tool demo clearly fenced as
localhost-only.

---

## AppSec — `m3_3` API Security — name the 2023 standard explicitly (minor)

**Standard(s)/cert(s):** OWASP API Security Top 10 — 2023 edition
(https://owasp.org/API-Security/editions/2023/). **Severity:** Nice-to-have. **Integration point:**
one sentence in `m3_3`'s Concept.
**Why:** `m3_3` teaches IDOR/BOLA, mass assignment, and GraphQL — exactly the 2023 API Top 10
content — but doesn't name the list or its 2023 restructure (Broken Object Property Level
Authorization, **BOPLA**, merged the old Excessive Data Exposure + Mass Assignment). Add: "These map
to the **OWASP API Security Top 10 (2023)** — API1 BOLA, API3 BOPLA (which merged mass assignment
and excessive data exposure), API5 BFLA. Know these by their `APIn` labels; API pentests are scoped
against them." **Flags:** none.
