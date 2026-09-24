# Cyber Scouts — claim ledger

Every rule-shaped assertion this course makes, with a status and the evidence
behind it. The guardrail gate (`tools/guardrail.py`) proves the course is
*structurally* sound. It cannot prove anything here is *true*. That is what this
file is for.

Unlike the Guardians and AppSec ledgers, this one is **built as the course is
written, never retrofitted**: a module ships in the same commit as its batch, and
no claim enters the course before its row exists.

- **Course file:** `cyber-scouts/cyber_scouts_app.html` (intro + S1.1 + 1 roadmap)
- **Candidates extracted by:** `python3 tools/claims_extract.py scouts --json out.json`
- **Last pass:** 2026-09-24 (Batch 1: S1.1 build pass, 16 rows, 3 defects caught before publication, none shipped)

## How to use it

Re-read only rows whose **Re-check** date has passed, rows marked `PENDING`, and
modules edited since the pass date above. Everything else was settled by the
source named in the row.

## Status key

| Status | Means |
|---|---|
| `SOURCED` | an external authority was read this pass; the source is in the row |
| `EXECUTED` | the claim is a command's behaviour and was **run**; output pasted into the course |
| `PENDING` | believed correct, not externally checked this pass; the row names the source to check |
| `CONVENTION` | no source can settle it; the course states it as a convention |
| `FIXED` | was wrong or overclaimed in a draft, corrected before or during this pass |

## Batch 1 — S1.1 Lawful by Design (and the intro)

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 1 | S1.1 | Computer Misuse Act 1990 s.1(1): offence = causing a computer to perform a function with intent to secure access, access unauthorised, and knowing it; max on indictment (E&W) **2 years** (s.1(3)(c)) | `SOURCED` | legislation.gov.uk/ukpga/1990/18/section/1 (current revised text) | 2027-09 or on any CMA reform bill |
| 2 | S1.1 | CFAA = 18 U.S.C. § 1030 ("without authorization" / "exceeds authorized access"). *Van Buren v. United States*: decided **3 June 2021**, **6–3**, majority by **Barrett**; quote "gates-up-or-down inquiry—one either can or cannot access a computer system"; exceeding authorised access = reaching off-limits files, folders, databases | `SOURCED` | law.cornell.edu/supremecourt/text/19-783 (opinion text) | stable |
| 3 | S1.1 | *hiQ v. LinkedIn*: 9th Cir. **April 2022** (31 F.4th 1180) affirmed injunction; serious questions whether scraping public data is "without authorization" | `SOURCED` | law.justia.com 9th Cir. No. 17-16783, 2022-04-18; Wikipedia summary | stable |
| 4 | S1.1 | hiQ later found in breach of User Agreement (Nov 2022 ruling); used fake accounts for logged-in pages; **Dec 2022** stipulated consent judgment **$500,000** + permanent injunction to stop scraping and destroy data/code | `SOURCED` | Proskauer New Media & Technology Law blog 2022-12-08 (read: $500,000, filed 2022-12-06, fake accounts); Privacy World 2022-12; Morgan Lewis 2022-12 | stable |
| 5 | S1.1 | GDPR Art. 14 = information where data not obtained from the data subject; 14(3)(a) **one month**; 14(5)(b) "impossible or would involve a disproportionate effort" / "seriously impair" exemption | `SOURCED` | gdpr-info.eu/art-14-gdpr (Regulation text) | stable |
| 6 | S1.1 | "Public availability is not a lawful basis" under UK/EU GDPR: processing publicly available personal data still needs an Art. 6 basis | `CONVENTION` | Follows from Art. 6(1) (lawful only if at least one basis applies; none is "publicly available"). Stated as the course's reading of the Regulation, with a not-legal-advice note | on UK DUAA changes |
| 7 | S1.1 | Berkeley Protocol: published **December 2020** (launched 1 Dec, dated 2 Dec) by **OHCHR + Human Rights Center, UC Berkeley School of Law**; UN symbol HR/PUB/20/2 (UN edition catalogued 2022) | `SOURCED` | ohchr.org launch statement 2020-12; humanrights.berkeley.edu publication page; digitallibrary.un.org/record/3973652 | stable |
| 8 | S1.1 | Protocol's six phases: online inquiries, preliminary assessment, collection, preservation, verification, investigative analysis | `SOURCED` | Protocol PDF, ch. VI contents (pp. 53 ff.), text extracted and read | stable |
| 9 | S1.1 | Methodological principles "at a minimum, accuracy, data minimization, data preservation and security by design"; collection data = collector, machine IP, virtual identity, time stamp, clock synced to NTP; hash at point of collection "has not been modified since the time of collection" | `SOURCED` | Protocol PDF, principles summary and ch. VI.C (g)–(h), quoted from extracted text | stable |
| 10 | S1.1, intro | example.com / .net / .org reserved by IANA for documentation | `SOURCED` | RFC 2606 §3 (rfc-editor.org) | stable |
| 11 | S1.1 | Case study: Reddit named Sunil Tripathi (missing since mid-March 2013) after the 15 April 2013 bombing; family froze Facebook page; Martin apologised privately 19 Apr, publicly 22 Apr ("fueled online witch hunts and dangerous speculation"); body found 23 Apr, identified 25 Apr; subreddit ban for Navy Yard search Sept 2013 | `SOURCED` | NBC News (Reddit apology); Al Jazeera 2013-04-23; WBUR 2013-04-25; TechCrunch (Navy Yard ban). Manner of death deliberately omitted (young audience) | stable |
| 12 | S1.1 lab | Verisign RDAP response for example.com embeds "last update of RDAP database"; two fetches can hash differently (seen: 07:27 vs ~07:28) or identically (seen: same run, seconds apart); file size 2,440 bytes | `EXECUTED` | Lab run 2026-09-24; both outcomes observed; size from `ls -l`; expected block says "may or may not match" | on RDAP profile change |
| 13 | S1.1, intro | `shasum -a 256` of the two `printf` lines (31138c47… / a844aa1f…) and of `/dev/null` (e3b0c442…b855) | `EXECUTED` | Run 2026-09-24; deterministic, learner output must match exactly | stable |
| 14 | S1.1 | ATT&CK TA0043 Reconnaissance; T1593, T1589 | `SOURCED` | `tools/attack_ids_verified.json` (STIX-verified, Guardians Batch 1 row 35) | per ATT&CK release |
| 15 | S1.1 | "Personal data" = any information relating to an identified or identifiable **living** person | `SOURCED` | GDPR Art. 4(1) ("natural person") + Recital 27 ("does not apply to the personal data of deceased persons"), gdpr-info.eu | stable |
| 16 | S1.1 | "SHA-256 is the standard choice today" for evidence hashing | `CONVENTION` | Berkeley Protocol deliberately names no algorithm ("evaluate which hash to use based on the currently accepted standard"); stated as current practice, not a rule | on SHA-2 deprecation guidance |

## Defects caught before publication

- **Draft theory showed an invented hash output** with a "do not trust this" note
  — a documented result that cannot happen, the exact shape the gate always
  scores green. Replaced with the real deterministic output (row 13).
- **Raw `sntp` output prints the machine's local timezone offset.** The lab now
  prints only the clock offset, so no location detail enters the course.
- **A challenge answer said hiQ "paid" $500,000.** The sources record a
  stipulated consent *judgment*, not a payment (hiQ was by then defunct).
  Restated as "ended with a $500,000 consent judgment against it" (row 4).
