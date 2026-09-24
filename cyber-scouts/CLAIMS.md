# Cyber Scouts — claim ledger

Every rule-shaped assertion this course makes, with a status and the evidence
behind it. The guardrail gate (`tools/guardrail.py`) proves the course is
*structurally* sound. It cannot prove anything here is *true*. That is what this
file is for.

Unlike the Guardians and AppSec ledgers, this one is **built as the course is
written, never retrofitted**: a module ships in the same commit as its batch, and
no claim enters the course before its row exists.

- **Course file:** `cyber-scouts/cyber_scouts_app.html` (intro + S1.1–S1.2 + 1 roadmap)
- **Candidates extracted by:** `python3 tools/claims_extract.py scouts --json out.json`
- **Last pass:** 2026-09-24 (Batch 2: S1.2 build pass, rows 17–35, 4 defects caught before publication, none shipped; Batch 1: S1.1, 16 rows)

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

## Batch 2 — S1.2 Registration Data (RDAP)

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 17 | S1.2 | RDAP RFCs: 7480 HTTP usage, 7481 security (both Mar 2015, Internet Standard); 9082 query, 9083 JSON responses (both Jun 2021, Internet Standard); 9224 bootstrap (Apr 2022, obsoletes 7484); 9537 redacted fields (Mar 2024, Proposed Standard); WHOIS = RFC 3912 (Sep 2004) | `SOURCED` | rfc-editor.org `rfcNNNN.json` metadata, read 2026-09-24 (title, date, status, obsoleted_by) | on any new RDAP RFC |
| 18 | S1.2 | From **28 Jan 2025** gTLD registries/registrars no longer required to provide WHOIS/web WHOIS, "except for .com, .name, and .post"; RDAP became the definitive source | `SOURCED` | ICANN RDAP FAQs page (quoted verbatim); ICANN announcement "Launching RDAP; Sunsetting WHOIS" 2025-01-27 | on RA/RAA amendment |
| 19 | S1.2 | 2023 global amendments require every gTLD registrar to provide RDAP for all domains it sponsors | `SOURCED` | ICANN "2023 Global Amendments" page / RDAP FAQs (search summary of icann.org pages, 2026-09-24) | on RA/RAA amendment |
| 20 | S1.2 | Temporary Specification adopted by ICANN Board **17 May 2018**; GDPR applies from **25 May 2018**; Registration Data Policy effective **21 Aug 2025** (replaced the Interim Policy); quote "MUST NOT include the value of the data element … and MUST indicate that the value is redacted", subject to Consent to Publish | `SOURCED` | icann.org Registration Data Policy page (effective-date and redaction text quoted); ICANN announcement 2025-08-21; GDPR Art. 99(2) | on RDP revision (last revised 2026-05-12, Rec 18) |
| 21 | S1.2 | RDRS / registrar disclosure process is the route for non-public data; not used by the course | `SOURCED` | ICANN RDAP sunset announcement (2025-01-27) names RDRS and registrar contact | on RDRS change |
| 22 | S1.2 | Five RIRs (AFRINIC, APNIC, ARIN, LACNIC, RIPE NCC) | `EXECUTED` | Distinct HTTPS servers in IANA `ipv4.json` + `asn.json`, 2026-09-24: exactly five, one per RIR | stable |
| 23 | S1.2 | Bootstrap file layout (`services` = [[keys],[urls]]); `.com`→Verisign, `.org`→PIR, `.uk`→Nominet, `.fr`, `.au` present; `.de`, `.jp`, `.io` absent; DNS file published 2026-09-16 covered **1,202 of 1,438** root TLDs (unique, case-folded) | `EXECUTED` | `data.iana.org/rdap/dns.json` vs `data.iana.org/TLD/tlds-alpha-by-domain.txt`, `comm` count 2026-09-24 | quarterly — volatile |
| 24 | S1.2 | example.com: registered 1995-08-14, registrar handle 376 "RESERVED-Internet Assigned Numbers Authority", statuses client delete/transfer/update prohibited, expiry 2027-08-13, Cloudflare NS, delegationSigned true. example.org: registered 1995-08-31, registrar 376 "ICANN", `redacted` conformance with one removal of "Registry Domain ID" at `$.handle` | `EXECUTED` | Lab + Drill 2 run 2026-09-24; output pasted | per re-run (records change) |
| 25 | S1.2 | IANA Registrar ID 376 status *Reserved*, no RDAP server; 3,330 of 4,504 registrar records carry an RDAP server | `EXECUTED` | `iana.org/assignments/registrar-ids/registrar-ids.xml`, 2026-09-24 | stable (376); counts volatile, not in course |
| 26 | S1.2 | 192.0.2.1 → ARIN via `192.0.0.0/8`; `NET-192-0-2-0-1`, TEST-NET-1, registrant IANA, documentation remark. AS64496 absent from ASN bootstrap; ARIN returns AS64496, 64496–64511, IANA-RSVD, RFC 5398 remark | `EXECUTED` | Lab run 2026-09-24; RFC 5737 / RFC 5398 (rfc-editor.org metadata) | stable |
| 27 | S1.2 | ARIN names `198.51.100.0/24` (`NET-198-51-100-0-1`) **TEST-NET-1**; RFC 5737 names it **TEST-NET-2** | `EXECUTED` | ARIN RDAP 2026-09-24 + RFC 5737 §3 text | on ARIN record change |
| 28 | S1.2 | RFC 5731 §2.3: "client"-prefixed statuses set by client (registrar), "server" by server (registry); RFC 8056 maps EPP to RDAP status (Jan 2017) | `SOURCED` | RFC 5731 text (quoted); RFC 8056 metadata | stable |
| 29 | S1.2 | crDate = "date and time of domain object creation"; trDate = "most recent successful domain-object transfer" → registration date is not acquisition date | `SOURCED` | RFC 5731 §3.1.2 text | stable |
| 30 | S1.2 | RFC 9537 methods: removal, empty value, partial value, replacement value | `SOURCED` | RFC 9537 §3.1–3.4 headings | stable |
| 31 | S1.2 | RFC 7480 §5.3: empty result set → 404 (Not Found) | `SOURCED` | RFC 7480 text | stable |
| 32 | S1.2 | RFC 9082 §3.1.6 help path under every base URL (used by the gate's RDAP probe) | `SOURCED` | RFC 9082 text; all five base URLs in the course returned 200 on `help` | stable |
| 33 | S1.2 | An IP record names the block holder (usually a network operator), not who used an address at a moment | `CONVENTION` | Follows from what RIR records contain (allocation/assignment, not usage logs); stated as a reading, not a rule | stable |
| 34 | S1.2 | ATT&CK T1596 Search Open Technical Databases; TA0043 | `SOURCED` | `tools/attack_ids_verified.json` (T1596 present; sub-technique T1596.002 **not** in the verified file, so the course cites only T1596) | per ATT&CK release |
| 35 | S1.2 | Case study: WannaCry 12 May 2017, NHS among victims; Hutchins (MalwareTech, 22) found an unregistered kill-switch domain, registered it (~$10.69) as routine tracking **without knowing** it was a kill switch; later variants' domains also sinkholed | `SOURCED` | TechCrunch 2019-07-08 ("would often take control of unregistered domains"); Cloudflare Learning + SecurityWeek ($10.69); Wikipedia "WannaCry ransomware attack" (began Fri 12 May 2017; NHS England/Scotland; cites "a 22yo who blocked"; 14 May variant with second kill switch registered by Matt Suiche). Arrest/prosecution deliberately omitted (not relevant to the lesson) | stable |

## Defects caught before publication

- **Draft theory showed an invented hash output** with a "do not trust this" note
  — a documented result that cannot happen, the exact shape the gate always
  scores green. Replaced with the real deterministic output (row 13).
- **Raw `sntp` output prints the machine's local timezone offset.** The lab now
  prints only the clock offset, so no location detail enters the course.
- **A challenge answer said hiQ "paid" $500,000.** The sources record a
  stipulated consent *judgment*, not a payment (hiQ was by then defunct).
  Restated as "ended with a $500,000 consent judgment against it" (row 4).
- **S1.2 draft expected-output block had placeholder timestamps and hashes**
  typed by hand. Replaced with the verbatim output of a real run of the exact lab
  string (round-trip checked: rendered `lab.mac` == the script that was run).
- **S1.2 case study draft said "that afternoon" and "British"** — neither was
  verified this pass. Both removed; age (22) kept — Wikipedia's cited headline gives it.
- **S1.2 Drill 1 walkthrough assumed ARIN names 198.51.100.0/24 "TEST-NET-2"** (the
  RFC 5737 name). Running it showed ARIN labels it "TEST-NET-1". Now taught as a
  second instance of "join on handles and ranges, not names" (row 27).
- **Gate false-fail on RDAP base URLs** (400/404 bare, by design). The URL check now
  probes `<base>help` (RFC 9082 §3.1.6) — a real liveness check, not an exemption.
