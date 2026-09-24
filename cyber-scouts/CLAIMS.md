# Cyber Scouts — claim ledger

Every rule-shaped assertion this course makes, with a status and the evidence
behind it. The guardrail gate (`tools/guardrail.py`) proves the course is
*structurally* sound. It cannot prove anything here is *true*. That is what this
file is for.

Unlike the Guardians and AppSec ledgers, this one is **built as the course is
written, never retrofitted**: a module ships in the same commit as its batch, and
no claim enters the course before its row exists.

- **Course file:** `cyber-scouts/cyber_scouts_app.html` (intro + S1.1–S1.6 + 1 roadmap)
- **Candidates extracted by:** `python3 tools/claims_extract.py scouts --json out.json`
- **Last pass:** 2026-09-24 (Batch 6: S1.6 build pass, rows 88–105, 10 defects caught before publication, none shipped; Batch 5: S1.5 build pass, rows 70–87, 9 defects caught before publication, none shipped; Batch 4: S1.4 build pass, rows 53–69, 9 defects caught before publication, none shipped; Batch 3: S1.3 build pass, rows 36–52, 9 defects caught before publication, none shipped; Batch 2: S1.2 build pass, rows 17–35, 4 defects caught before publication, none shipped; Batch 1: S1.1, 16 rows)

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

## Batch 3 — S1.3 Certificate Transparency

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 36 | S1.3 | RFC 6962 (June 2013) and RFC 9162 (December 2021, obsoletes 6962) are both **Experimental**; quote "The logs do not themselves prevent misissue, but they ensure that interested parties (particularly those named in certificates) can detect such misissuance." | `SOURCED` | rfc-editor.org .txt of both, headers + RFC 6962 §1 read 2026-09-24 | stable |
| 37 | S1.3 | Precertificate poison extension OID `1.3.6.1.4.1.11129.2.4.3` (critical); embedded SCT list OID `1.3.6.1.4.1.11129.2.4.2`; log ID = SHA-256 hash of the log's public key | `SOURCED` | RFC 6962 §3.1 and §3.2 text | stable |
| 38 | S1.3 | Chrome requires all publicly-trusted TLS certificates issued after **30 April 2018** to support CT to be recognised as valid | `SOURCED` | GoogleChrome/CertificateTransparency README.md (raw.githubusercontent.com; github.io unreachable from this network) | on Chrome policy change |
| 39 | S1.3 | Chrome embedded-SCT policy: ≤180 days → 2 SCTs, >180 days → 3, from distinct logs; ≥2 distinct operators; ≥1 log Qualified/Usable/ReadOnly at check; Retired-log SCT counts only if issued before the Retired timestamp | `SOURCED` | GoogleChrome/CertificateTransparency `ct_policy.md` "CT Compliant Certificates" section, read 2026-09-24 | on Chrome policy change |
| 40 | S1.3 | A certificate from an organisation's internal CA "has no reason to be in any log" | `CONVENTION` | Inference from row 39's scope ("all publicly-trusted TLS certificates"); no policy obliges a private CA to log. Worded as "no reason", not "never" | stable |
| 41 | S1.3 | crt.sh is run by Sectigo and is a search index over the logs, not a log | `SOURCED` | crt.sh footer "© Sectigo Limited 2015-2026"; github.com/crtsh org contact rob@sectigo.com (gh api, 2026-09-24); absent from Chrome's log list (row 45) | on ownership change |
| 42 | S1.3 lab | crt.sh answered **502** on the first request of the build and 200 on retry; `curl -f --retry 5 --retry-all-errors` turns a 502 into a retry | `EXECUTED` | Build runs 2026-09-24 (one 502 on `?q=`, one 502 then 404 on the homepage) | volatile by nature |
| 43 | S1.3 lab | `?q=example.com&output=json&exclude=expired`: 16 entries, 9 distinct serials (7 pairs, 2 singletons: serial `1000` from "AS207960 Test CA", and an issuer crt.sh reports as not found); 5 unique name strings (2 hostnames, 1 wildcard, 1 email, 1 non-hostname) | `EXECUTED` | Lab run 2026-09-24 12:13Z; file hash 41564f884e2f… stable across three runs within the hour | **volatile** — changes as certs issue/expire; course says so |
| 44 | S1.3 lab | crt.sh 22853391369 = precertificate (poison), 22853418213 = certificate (SCTs), both serial `531E16F0F28235B65CC7CD35A5F0710B`, 8 SANs (example.com/.edu/.net/.org ± www); crt.sh `name_value` showed only example.com + www.example.com; PEM hashes d893f69033dd… / 9c036575ad32… | `EXECUTED` | Lab run ×3, identical hashes each time; learner output must match exactly | stable (logged certs are immutable) |
| 45 | S1.3 lab | Final cert's SCTs → Google 'Argon2026h2' (usable), Sectigo 'Elephant2026h2' (usable), Let's Encrypt 'Oak2026h2' (**retired 2026-02-28T00:00:00Z**), all 2 Dec 2025 ~01:32:36 GMT; log list v92.1 published 2026-09-23T13:36:59Z | `EXECUTED` | Log IDs decoded by OpenSSL 3.6.3, base64-matched against gstatic `log_list.json` | on log list change |
| 46 | S1.3 | A log's `temporal_interval` is a window on certificate **expiry** ("certificates that expire (have a NotAfter date) between these dates"); hence "2026h2" names | `SOURCED` | gstatic `log_list_schema.json` description text | stable |
| 47 | S1.3 | A wildcard matches exactly one label (`mail.example.com`, not `a.b.example.com`); RFC 9525 (Nov 2023) obsoletes RFC 6125 | `SOURCED` | RFC 9525 §6.3 "can only match one label"; header "Obsoletes: 6125" | stable |
| 48 | S1.3 | Case study: 14 Sep 2015 ~19:20 GMT Thawte (Symantec) EV precert for google.com + www.google.com, not requested; found via CT (required for EV since 1 Jan 2015); in Google- and DigiCert-operated logs; valid one day; internal testing; announced 18 Sep. Symantec reported 23 test certs / 5 orgs; Google "a few minutes of work"; shared 6 Oct; 12 Oct Symantec +164 over 76 domains + 2,458 for never-registered domains; 28 Oct: CT required for Symantec from 1 Jun 2016 | `SOURCED` | security.googleblog.com 2015/09 "Improved Digital Certificate Security" and 2015/10 "Sustaining Digital Certificate Security", both read in full | stable |
| 49 | S1.3 | ATT&CK **T1596.003 Digital Certificates**, sub-technique of T1596, tactic TA0043 Reconnaissance | `SOURCED` | mitre/cti STIX object attack-pattern--0979abf9…, repo tip = v19.2 (2026-08-05, same release as `attack-stix-data`); not revoked/deprecated; added to `tools/attack_ids_verified.json` | per ATT&CK release |
| 50 | S1.3 Drill 2 | Cert 22853418213 valid 2 Dec 2025 00:00:00 → 2 Dec 2026 23:59:59 GMT (>180 days → 3 SCTs); 3 logs, 3 operators; Oak SCT predates its retirement → compliant | `EXECUTED` | `openssl x509 -startdate -enddate` + log-list `state`, run 2026-09-24, output in the drill | stable |
| 51 | S1.3 Drill 3 | 4 of the 9 serials issued by "Cloudflare TLS Issuing ECC/RSA CA 3", issuer O=**SSL Corporation** | `EXECUTED` | jq over the collected crt.sh JSON | volatile with row 43 |
| 52 | S1.3 lab | macOS `/usr/bin/openssl` is LibreSSL 3.3.6 and prints the CT OIDs without names or SCT decoding; Homebrew `openssl@3` decodes both and is a dependency of `python@3.12` (in the shared setup file); `brew --prefix` (no formula) is offline. Windows variant **not run** (stated in the lab) | `EXECUTED` | Both binaries run on the same PEMs; homebrew-core `Formula/p/python@3.12.rb` line 30 `depends_on "openssl@3"` | on macOS / formula change |

## Batch 4 — S1.4 People and Organisations

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 53 | S1.4 | An LEI is a 20-character code defined by ISO 17442; GLEIF publishes LEI data free of charge | `SOURCED` | gleif.org "ISO 17442: The Global Standard" / "Introducing the LEI" pages, 2026-09-24 | stable |
| 54 | S1.4 | SEC fair access: declare a User-Agent in the form "Sample Company Name AdminContact@<sample company domain>.com"; max 10 requests/second | `SOURCED` | sec.gov "Accessing EDGAR Data", read 2026-09-24 | 6 months |
| 55 | S1.4 | GDPR Art. 5(1)(c): "adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed ('data minimisation')"; UK GDPR same text | `SOURCED` | legislation.gov.uk/eur/2016/679/article/5, read 2026-09-24 | stable |
| 56 | S1.4 Step 1, Drill 1 | GLEIF legal-name search "Apple Inc.": 24 records, 15 jurisdictions, exactly one with that legal name (`HWUPKR0MPOU8FGXBT394`); LEI ISSUED 6 / LAPSED 18; entity status ACTIVE 24; the four names quoted are in the result | `EXECUTED` | lab + Drill 1 run 3×, 2026-09-24 | volatile |
| 57 | S1.4 Step 2 | LEI record: legal address "C/O C T Corporation System, 330 N. Brand Blvd, Suite 700, Glendale"; HQ "One Apple Park Way, Cupertino"; registeredAt `RA000598` as `806592`; `FULLY_CORROBORATED`, validatedAt `RA000598`; created 1977-01-03. `RA000598` = Secretary of State (California), "Business Entity Records" | `EXECUTED` | lab; GLEIF `/registration-authorities/RA000598` | volatile |
| 58 | S1.4 Step 3 | 20 ultimate children, all relationships `IS_ULTIMATELY_CONSOLIDATED_BY` and `ENTITY_SUPPLIED_ONLY`; RR-CDF 2.1 definition quoted verbatim ("significant reliance on the information that a submitter provided due to the unavailability of corroborating information"); the type means full accounting consolidation | `SOURCED` | lab; gleif.org Level 2 RR-CDF 2.1 format page, read 2026-09-24 | volatile (counts) |
| 59 | S1.4 Step 3 | Ultimate-parent exception reason `NATURAL_PERSONS`; ExceptionReason = "a single reason provided by the legal entity"; NATURAL_PERSONS = "the entity is controlled by a natural person(s) without any intermediate legal entity" | `SOURCED` | lab; gleif.org Level 2 Reporting Exceptions 2.1 format page, read 2026-09-24 | volatile (reason) |
| 60 | S1.4 Step 4 | SEC CIK 0000320193: "Apple Inc.", stateOfIncorporation CA, business address ONE APPLE PARK WAY, CUPERTINO; formerNames APPLE INC (2007-01-10→2019-08-05), APPLE COMPUTER INC (1994-01-26→2007-01-04), APPLE COMPUTER INC/ FA | `EXECUTED` | data.sec.gov submissions JSON, lab | volatile |
| 61 | S1.4 Step 4 | Reg S-K Item 601(b)(21)(i) requires the subsidiaries list; (ii) omission text quoted verbatim | `SOURCED` | eCFR versioner, 17 CFR 229.601 as of 2026-08-01 | stable |
| 62 | S1.4 Step 4 | 10-K accession 0000320193-25-000079, filed 2025-10-31; Exhibit 21.1 names 19 subsidiaries and invokes 601(b)(21)(ii); 9 of 19 match GLEIF ultimate children by exact normalised string; `애플코리아 유한회사` has transliterated name APPLE KOREA LIMITED | `EXECUTED` | lab | stable (filing) · volatile (GLEIF side) |
| 63 | S1.4 Step 5 | Exhibit 31 = "Rule 13a-14(a)/15d-14(a) Certifications" (Item 601(b)(31)); Exhibit 31.1 opens "I, Timothy D. Cook, certify" and is signed "Date: October 31, 2025 … Chief Executive Officer" | `SOURCED` | eCFR 229.601; exhibit text extracted by the lab | stable |
| 64 | S1.4 | ATT&CK T1591 Gather Victim Org Information (.002 Business Relationships, .004 Identify Roles), T1589 Gather Victim Identity Information (.003 Employee Names), all reconnaissance | `SOURCED` | mitre/cti attack-pattern objects at the v19.2 tip, 2026-09-24; added to `tools/attack_ids_verified.json` | each ATT&CK release |
| 65 | S1.4 case | Brewer: John Vincent Cable Services Ltd (2013), "former Business Secretary Vince Cable MP", dissolved by Companies House; Cleverly Clogs Ltd (2016) naming Baroness Neville-Rolfe, James Cleverly MP, invented "Ibrahim Aman"; s.1112 Companies Act 2006; guilty plea, Redditch Magistrates' Court, 15 March 2018; £1,602 fine, £10,462.50 costs, £160 surcharge; announced 23 March 2018 as the first such prosecution | `SOURCED` | gov.uk press release "UK's first ever successful prosecution for false company information", read 2026-09-24 | stable |
| 66 | S1.4 case | ECCT Act 2023: identity verification a legal requirement for directors and PSCs from 18 November 2025, 12-month transition for existing directors | `SOURCED` | gov.uk news 5 August 2025, read 2026-09-24 | stable |
| 67 | S1.4 Drill 1 | LAPSED = "An LEI registration that has not been renewed by the NextRenewalDate and is not known by public sources to have ceased operation" (course quotes the first clause) | `SOURCED` | gleif.org LEI-CDF 3.1 format page, read 2026-09-24 | stable |
| 68 | S1.4 Drill 2 | With `transliteratedOtherNames`, 11 of 19 match; 8 unmatched; Apple Japan合同会社 / "Apple Japan LLC", form 7QQ0, `RA000412` `0111-03-003992`; 19 + 20 − 11 = 28 (27 if Japan is one entity) | `EXECUTED` | Drill 2 extracted from the built HTML and run | volatile |
| 69 | S1.4 lab | Both exhibit hashes (`2a65f37b1dc3…`, `a80ced0d3b73…`) identical across 3 runs; an EDGAR amendment is a new submission with its own accession number, and SEC post-acceptance corrections exist (hence "should not", not "will not"). Windows variant **not run** (stated in the lab) | `EXECUTED` | three lab runs; sec.gov EDGAR PDS dissemination spec (search) | stable |

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
- **S1.3 lab: `brew --prefix openssl@3` hits the network.** On a connection that
  cannot reach formulae.brew.sh it failed, left `$OSSL` empty, and the two-way
  classifier then labelled **both** entries "CERTIFICATE (carries SCTs)", a
  confident wrong answer. Now `$(brew --prefix)/opt/openssl@3` (offline), a
  missing-binary warning, and a three-way classifier whose fallback is `UNKNOWN`.
- **S1.3 lab: awk `/Timestamp/` also matched "Signed Certificate Timestamp:"** and
  printed junk SCT rows. Anchored to `^ *Timestamp :`.
- **S1.3 lab: an `exit` guard** would have closed the learner's Terminal when pasted.
  Replaced by a warning.
- **S1.3 case study: a search summary said Symantec admitted "187 test
  certificates".** Google's post gives 23, then 164 more. The course uses the post's
  figures (row 48).
- **S1.3 draft overclaims, caught on re-read:** a singleton entry called "not a
  public CA's certificate" (unverified; now "open it before counting it"); "the
  domain had certificates long before this one" (not in collected evidence; now
  cites S1.2's 1995 registry date); "a wildcard tells you subdomains are in use"
  and "any single name under" (now RFC 9525's one-label rule, row 47).
- **S1.3 Drill 2 shipped commands without output** — the coverage gate caught it
  (scouts_theory 4/5); the real output is now in the walkthrough.
- **S1.4 Step 1 draft characterised search hits** ("a restaurant franchisee, a
  Montessori school, a real-estate trust") from their names alone. Now it quotes
  the legal names and says no more.
- **S1.4 theory said the LEI issuer "checked" the entity record against its
  register.** The record shows `validatedAt RA000598`; the course now says exactly
  that.
- **S1.4 case study draft carried three details from secondary coverage**: a letter
  to Vince Cable, a Companies House warning, and Brewer's motive. None is in the
  gov.uk release. All three removed (row 65).
- **S1.4 case-study lesson "two real ministers"** — James Cleverly's 2016 office was
  not checked. Now "three real politicians".
- **S1.4 lab: certification date never printed.** EDGAR encodes the colon as
  `&#58;`, so `Date:` never matched. Found by running the lab, not by reading it.
- **S1.4 Windows lab used `$args`**, a PowerShell automatic variable, as a splat
  name; and `"$G?filter"` would parse as a variable named `G?`. Renamed to `$p`
  and braced as `${G}`.
- **Gate FAIL: 3 ATT&CK ids not in the verified table.** Verified from mitre/cti
  (row 64) and added. The gate did its job.
- **Gate FAIL: `https://api.gleif.org/api/v1` DEAD (404).** A bare base URL in the
  lab. The base is now `…/api/v1/lei-records`, a real endpoint (200), and the lab was
  re-run from the built HTML with identical output and hashes.
- **Pronouns for the named officer** in a challenge and Drill 3 replaced with
  neutral wording or the name.

## Batch 5 — S1.5 Breach Exposure

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 70 | S1.5 | DPA 2018 s.170(1): offence to "knowingly or recklessly" obtain or disclose personal data without the controller's consent, or retain it after so obtaining; s.170(2)–(3) defences (crime, enactment/court, public interest, reasonable belief, special purposes/journalism) | `SOURCED` | legislation.gov.uk s.170 XML, read 2026-09-24 | stable |
| 71 | S1.5 | Using a leaked credential to log in is unauthorised access under CMA 1990 s.1 (back-pointer to S1.1's statement of s.1) | `SOURCED` | S1.1 row set (Batch 1); course text line "Section 1 of the Computer Misuse Act 1990" | stable |
| 72 | S1.5 | HIBP API v3: User-Agent required, missing one → HTTP 403; email search (`breachedAccount`) needs an `hibp-api-key`; domain search needs verified control ("organisations must first add the domain to their dashboard and verify that they control it"), unverified → 403; verification by DNS or email; Pwned Passwords needs no authorisation | `SOURCED` | haveibeenpwned.com/API/v3, read 2026-09-24 | 6 months |
| 73 | S1.5 | Breach-model definitions quoted for IsVerified, IsFabricated (incl. "still contains legitimate email addresses"), IsSpamList, IsSensitive, BreachDate ("not always accurate … Use this attribute as a guide only"); the IsVerified entry reads "Indicates that the breach is considered unverified" (a documentation slip; data shows true = verified: Adobe true, Zoosk false) | `SOURCED` | haveibeenpwned.com/API/v3 breach model, read 2026-09-24; lab data | 6 months |
| 74 | S1.5 Step 1 | Catalogue 1038 breaches; not verified 42, fabricated 3, spam lists 16, malware 9, stealer logs 6, sensitive 94; fabricated = JustDate, Paytm, Zoosk with dates and counts as printed | `EXECUTED` | lab, 4 runs (bash, zsh, built-HTML extract) | volatile |
| 75 | S1.5 Step 1 | Paytm: IsFabricated true **and** IsVerified true; description "did not originate from Paytm"; 3,395,101 addresses; flag combinations 40/2/16/1 (Drill 1) | `EXECUTED` | breaches.json; Drill 1 run from the built HTML | volatile |
| 76 | S1.5 Step 2 | Adobe: BreachDate 2013-10-04, AddedDate 2013-12-04, PwnCount 152445165, classes Email addresses/Password hints/Passwords/Usernames, verified; description "disclosed much about the passwords" | `EXECUTED` | `/breach/Adobe`, lab | stable |
| 77 | S1.5 Step 2 · Drill 2 | Gap AddedDate−BreachDate: 168 ≤ 7 days, median 134, 362 > 1 year, max 5201 (RSBoards 2011-12-26 → 2026-03-23); 42 breach dates on 1 January (≈15× the ≈2.8 expected by chance) | `EXECUTED` | Drill 2 run from the built HTML | volatile |
| 78 | S1.5 Step 3 | `?Domain=adobe.com` returns 1 breach (Adobe) | `EXECUTED` | lab | volatile |
| 79 | S1.5 Step 4 | Range API: first 5 chars of SHA-1 (or NTLM) hash, not case-sensitive; SHA-1(`P@ssw0rd`) = 21BD12DC183F740EE76F27B78EB39C8AD972A757; prefix 21BD1 held 1925 real suffixes; suffix count 6,421,042; 16⁵ = 1,048,576 prefixes; other ranges 00000/FFFFF/5BAA6 held ~2509/2047/1978 lines | `EXECUTED` | lab + direct probes 2026-09-24; API v3 docs | volatile (counts) · stable (hash) |
| 80 | S1.5 Step 4 | Padding: `Add-Padding: true` adds random zero-count rows ("Padded entries always have a password count of 0"); docs still say "between 800 and 1,000"; live: 51–193 padding rows, totals 1976–2118 over 7 requests; Hunt 2020-03-04 post: example ranges 523/528 rows, numbers chosen to give "a heap of buffer to expand the total volume" | `SOURCED` + `EXECUTED` | API v3 docs; troyhunt.com "Enhancing Pwned Passwords Privacy with Padding" (datePublished 2020-03-04); 7 live requests | 6 months |
| 81 | S1.5 | ATT&CK T1589.001 Credentials (reconnaissance), T1110.004 Credential Stuffing (credential access); neither revoked nor deprecated | `SOURCED` | mitre/cti attack-pattern objects at the v19.2 tip (`8543c5b05b`), 2026-09-24; added to `tools/attack_ids_verified.json` | each ATT&CK release |
| 82 | S1.5 case | Hunt, "Here's how I verify data breaches", 6 May 2016: 57,554,881 rows email:password; "makes it very hard to verify"; 88k "badoo" vs 6.4k "zoosk" addresses; 93k `$HEX[...]` passwords, "yet another anomaly"; subscribers "approaching 400k verified", those denying membership also denied the password; Zoosk: "None of the full user records in the sample data set was a direct match to a Zoosk user"; ZDNet story "One of the biggest hacks happened last year, but nobody noticed" the same day | `SOURCED` | troyhunt.com post, raw HTML read 2026-09-24 | stable |
| 83 | S1.5 case | `$HEX[73c5826f6e65637a6e696b69]` decodes to "słoneczniki" (ł is non-ASCII). The draft's claim that this is "how password-cracking tools write out" such passwords was **removed**: its source (hashcat FAQ) could not be read from this connection | `EXECUTED` | `xxd -r -p` | stable |
| 84 | S1.5 case | HIBP Zoosk record: fabricated, not verified, BreachDate 2011-01-01, AddedDate 2017-02-08, 52,578,183 addresses, "In approximately 2011"; "during extensive verification in May 2016 no evidence could be found" | `EXECUTED` | breaches.json | stable |
| 85 | S1.5 Drill 3 | `pwcheck` works identically in bash and zsh; empty input refused; failed request (dead proxy) → UNKNOWN, exit 2; `P@ssw0rd` → seen 6421042 times; non-breached test string → not found | `EXECUTED` | Drill 3 block run exactly as written, both shells | stable |
| 86 | S1.5 | "The only address you should ever check is your own" and "no dumps, no pastes, no combolists, no forums" are course rules, not law | `CONVENTION` | course rule (S1.1 practice targets) | — |
| 87 | S1.5 lab | Lab run 4× (bash, zsh, built-HTML extract); SHA-1, prefix, Adobe record and fabricated list identical each time; `range` evidence hash differs every run by design (padding). Windows variant **not run** (stated in the lab) | `EXECUTED` | four lab runs | stable |

Defects caught in the S1.5 build pass (none shipped):

- **Draft Drill 3 checked the empty string in bash.** The zsh-style `read "PW?…"` fell
  back to bash's form only after consuming the line, so SHA-1("") (`DA39A…`) was
  looked up and a count printed. Found by running it; fixed with a shell test and an
  empty-input guard.
- **Draft Drill 3 printed the count twice** (`${N:+…}${N:-…}` both expand when N is set).
- **Draft Drill 3 had no failure path**: a failed `curl` read as "not found". Now UNKNOWN.
- **A scratch catalogue count was wrong** (`A|length, (B|length)` without grouping); the
  lab's own figures were right. It never reached the course.
- **Case draft attributed `$HEX[...]` to cracking tools** without a readable source. Removed (row 83).
- **"57,554,881 rows became 52,578,183 addresses"** implied a derivation nobody showed.
  Now two separately attributed counts.
- **Challenge used `example-client.com`**, a registrable name. Now `client.example` (RFC 2606).
- **Gate FAIL: `https://api.pwnedpasswords.com/range/` DEAD (400).** Not a dead link: the
  gate skipped `…/$VAR` templates but not the escaped `…/\${…}` form a template literal
  stores. The gate now treats `\$` as a placeholder too; only that one prefix left the probe set (85 → 84).
- **Theory's padding quote cut Hunt's sentence mid-clause.** Replaced with a complete quoted phrase.

## Batch 6 — S1.6 Geospatial

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 88 | S1.6 | Protection from Harassment Act 1997 s.2A: stalking offence = course of conduct in breach of s.1(1) that amounts to stalking; s.2A(3) examples include "monitoring the use by a person of the internet, email or any other form of electronic communication" and "watching or spying on a person"; extent E+W; inserted by Protection of Freedoms Act 2012 s.111(1), in force 25.11.2012 | `SOURCED` | legislation.gov.uk/ukpga/1997/40/section/2A, read 2026-09-24 ("Latest available (Revised)") | on amendment |
| 89 | S1.6 | "Never geolocate a photo of a person, or of anywhere a person lives, and never work out who took a photo or where they live"; "photos of public places, published by their authors for reuse" only | `CONVENTION` | course rule (S1.1 practice targets) | — |
| 90 | S1.6 | Wikimedia User-Agent policy asks for contact information (email, website or wiki user); generic format `<client>/<version> (<contact>) …`; scripts without an informative UA "may be blocked without notice" (HTTP 403) | `SOURCED` | foundation.wikimedia.org Policy:Wikimedia_Foundation_User-Agent_Policy, read 2026-09-24 | yearly |
| 91 | S1.6 lab | `upload.wikimedia.org` answers the exact UA `CyberScoutsLab/1.0 (you@example.com)` with HTTP 403 ("Please honor our robot policy"); `(student@school.invalid)`, `(a@example.org)`, `(you@example)`, no contact, a real-looking webmail address all 200. The lab refuses to start while `CONTACT` is the placeholder | `EXECUTED` | six curl probes, 2026-09-24 | volatile — Wikimedia may change its blocklist |
| 92 | S1.6 lab | Commons `File:LONDON_BRIDGE.jpg`: SHA-1 `c6bac702d58366bca4915ee5b970461f12929cec`, 399,534 bytes, CC BY-SA 4.0, uploader Accord14, uploaded 2018-10-06; description "The famous London Tower Bridge along the Thames River"; category *Remote views of Tower Bridge*; no people categories; downloaded file's SHA-1 matches the API | `EXECUTED` | Commons API `imageinfo` + `categories`; image content not viewed by the author (description and categories only) | stable while the SHA-1 holds |
| 93 | S1.6 lab | EXIF: Apple iPhone 8, software 11.4.1; 51° 30' 26.74" N, 0° 4' 41.09" W; GPSHPositioningError 10 m; GPSImgDirectionRef True North, GPSImgDirection 75.18820225; no GPSMapDatum; no OffsetTimeOriginal; DateTimeOriginal 2018:08:26 09:42:06; GPSDateTime 2018:08:26 08:42:06Z; 20 tags matching `*gps*` | `EXECUTED` | ExifTool 13.59 (tarball SHA-256 `668ea3ac…fd65a` = exiftool.org checksums-13.59.txt) | stable |
| 94 | S1.6 Step 3 | `exiftool -n -GPS:GPSLongitude` = `0.0780805555555556` (unsigned); `-Composite:GPSLongitude` = `-0.0780805555555556`; Composite GPSLatitude/Longitude `Require` GPS:GPSLatitude + GPS:GPSLatitudeRef | `EXECUTED` | lab run; `lib/Image/ExifTool/GPS.pm` Composite table | stable |
| 95 | S1.6 Steps 3–4, Drill 1 | Sign error = 0.156° ≈ 10.8 km at 51.51° N ("about 11 km"); per-decimal-place table (111,320 m/deg × cos lat): 4 dp ≈ 11.13 m N–S / 6.93 m E–W; 6 dp ≈ 0.1 m; hand DMS→decimal equals Composite to 10 places | `EXECUTED` | Drill 1 run in bash and zsh; python cross-check | stable |
| 96 | S1.6 Step 2, 5 | Exif (CIPA DC-008 English translation, 2019 = Exif 2.32): GPSTimeStamp "Indicates the time as UTC"; OffsetTimeOriginal = offset from UTC "including daylight saving time", "±HH:MM"; revision history "2.31 July 2016 … Added three time offset tags"; GPSMapDatum "strongly recommended" when GPS Info is recorded; GPSHPositioningError "horizontal positioning errors in meters"; GPSImgDirection 0.00–359.99; Ref T = true, M = magnetic (ExifTool GPS.pm) | `SOURCED` | cipa.jp DC-X008-Translation-2019-E.pdf, text extracted and read 2026-09-24 | on new Exif edition |
| 97 | S1.6 Step 5, Drill 2 | Europe/London 2018: GMT→BST 2018-03-25, BST→GMT 2018-10-28; 2018-08-26 08:42:06 UTC = 09:42:06 BST (UTC+0100); clocks differ by exactly 60 min | `EXECUTED` | macOS tz database via `TZ=Europe/London date`; Drill 2 in bash and zsh | stable |
| 98 | S1.6 Step 6 | Wikidata P625: Q83125 Tower Bridge 51.5055556, −0.0752778; Q130206 London Bridge 51.5080556, −0.0877778. From the camera: Tower Bridge bearing 137.0°, 285 m; London Bridge 275.9°, 675 m (awk in lab = independent python haversine) | `EXECUTED` | `wbgetclaims` + lab awk + python | re-check if either item's P625 is edited |
| 99 | S1.6 Step 6 | Heading 75.19° vs bearing 137.0° to the subject's recorded point = ~62° discrepancy; the course names no cause ("a sensor reading … sometimes wrong") | `EXECUTED` | rows 93 + 98 | stable |
| 100 | S1.6 Step 7, Drill 3 | `exiftool -all= -o` copy has 0 `*gps*` tags (original 20). A copy with location only in `XMP-exif:GPSLatitude/Longitude` has no Composite:GPSLatitude but does have `GPSPosition` (51.5074 -0.0781) | `EXECUTED` | lab + Drill 3 | stable |
| 101 | S1.6 | ATT&CK T1591.001 Determine Physical Locations (sub-technique of T1591 Gather Victim Org Information, reconnaissance); not revoked or deprecated | `SOURCED` | mitre/cti `attack-pattern--ed730f20-0e44-48b9-85f8-0e2adeb76867` at tip `8543c5b05b` (= ATT&CK v19.2 Enterprise; attack-stix-data latest release v19.2); added to `tools/attack_ids_verified.json` | each ATT&CK release |
| 102 | S1.6 case | 3 Dec 2012: Vice photo of McAfee (with Vice's editor-in-chief) kept its EXIF; iPhone 4S; 15.658167, −88.992167; @simplenomad pointed it out; McAfee a "fugitive" (headline). 4 Dec: Ranchon Mary resort; McAfee first said the metadata was "manipulated", later removed that post; quotes "Vice Magazine reporters are indeed with me in Guatemala. Yesterday was chaotic due to the accidental release of my exact co-ordinates." and "I am in Guatemala and will be meeting with Guatemalan officials this morning."; Vice removed the metadata and re-posted | `SOURCED` | Graham Cluley, 3 Dec 2012; Scientific American / TechNewsDaily, 4 Dec 2012; both read 2026-09-24 via a summarising fetch. DMS lead 15°39'29.4"N 88°59'31.8"W converts exactly to Cluley's decimals. NPR's page timed out and is not relied on | stable |
| 103 | S1.6 lab | Install names: `brew install exiftool` (homebrew-core `Formula/e/exiftool.rb`); `winget install OliverBetz.ExifTool` (winget-pkgs manifests up to 13.59); Debian/Ubuntu `libimage-exiftool-perl` (sources.debian.org) | `SOURCED` | gh api + sources.debian.org API, 2026-09-24 | yearly |
| 104 | S1.6 Drills | Drills 1–3 run exactly as written in bash and zsh; outputs byte-identical; Drill 3: photo → HAS GPS exit 1, XMP-only → HAS GPS exit 1, stripped → NO GPS exit 0, text renamed `.jpg` → UNKNOWN exit 2, missing file → UNKNOWN exit 2, exiftool absent → UNKNOWN | `EXECUTED` | drill runs, 2026-09-24 | stable |
| 105 | S1.6 lab | Lab run 5× (3 bash, 2 zsh) with `CONTACT` set; everything above the log identical; `photo` SHA-256 `49e94c07bf33…` and `record` `df48d5c41c76…` stable across runs; placeholder guard exits before any request. Windows variant **not run** (stated in the lab) | `EXECUTED` | five lab runs + built-HTML round-trip (lab, windows, workbench, theory, case, expected all MATCH) | stable |

Defects caught in the S1.6 build pass (none shipped):

- **The lab's first run failed at the download** with a bare `FAILED: photo`: Wikimedia refuses the
  `you@example.com` placeholder (row 91). The lab now stops before any request and says why.
- **Draft Drill 1 printed a positive longitude with no error.** Unqualified `-GPSLongitude` returned
  the Composite value with a trailing `W`, and `tr -d "deg'\""` also deleted the `e` in "West", so the
  Ref test never matched. Now `-c "%d %d %.4f"` on explicit `GPS:` tags. Guard A96.
- **Draft Drill 2 printed London time as UTC**: `date -u` applies to output as well as input.
  Now parses both clocks to epoch seconds with `TZ=UTC` and formats with `TZ=Europe/London date -r`.
- **Draft Drill 3 said `NO GPS` about a text file** — the two-way-classifier shape again. MIME-type
  check added; non-images are UNKNOWN.
- **Draft Drill 3 said `NO GPS` about an XMP-only file**: `Composite:GPSLatitude` is built from the
  EXIF GPS block only (row 94). Now `GPSPosition`. Guard A97.
- **Draft lab counted only `-gps:all` in the stripped copy**, which cannot see XMP. Now counts every
  `*gps*` tag in any group, original and copy. Guard A98.
- **Draft theory said the photo "shows" the bridge**, but the author could not view the image. Now
  "is described as showing", pinned to the Commons description (row 92).
- **Draft theory asserted causes it had not sourced**: a compass "thrown off by metal", "almost always
  WGS 84", a title "the kind of mistake visitors make". All reworded to what the evidence supports.
- **Draft case study said McAfee was in Belize before**, and counted the resort name as corroboration.
  Neither was in a page read; and a resort named *from* the coordinates is not independent of them.
- **Draft Challenge 1 said "practising once is not a crime"**, which leans on the course-of-conduct
  threshold in s.7 — not read this pass. Removed.
