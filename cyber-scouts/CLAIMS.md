# Cyber Scouts — claim ledger

Every rule-shaped assertion this course makes, with a status and the evidence
behind it. The guardrail gate (`tools/guardrail.py`) proves the course is
*structurally* sound. It cannot prove anything here is *true*. That is what this
file is for.

Unlike the Guardians and AppSec ledgers, this one is **built as the course is
written, never retrofitted**: a module ships in the same commit as its batch, and
no claim enters the course before its row exists.

- **Course file:** `cyber-scouts/cyber_scouts_app.html` (intro + S1.1–S1.7 + S2.1–S2.7 + S3.1–S3.3 + 3 roadmaps)
- **Candidates extracted by:** `python3 tools/claims_extract.py scouts --json out.json`
- **Last pass:** 2026-09-29 (Batch 17: S3.3 build pass, rows 367–397, 10 defects caught before publication, none shipped; Batch 16: S3.2, rows 346–366; Batch 15: S3.1 build pass, rows 319–345, 14 defects caught before publication, none shipped; guard A111; Batch 14: S2.7 build pass, rows 292–318, 13 defects caught before publication, none shipped; Batch 13: S2.6 build pass, rows 264–291, 12 defects caught before publication, none shipped; Batch 12: S2.5 build pass, rows 238–263, 9 defects caught before publication, none shipped; Batch 11: S2.4 build pass, rows 206–237, 10 defects caught before publication, none shipped; Batch 10: S2.3 build pass, rows 178–205, 9 defects caught before publication, none shipped; Batch 9: S2.2 build pass, rows 147–177, 8 defects caught before publication, none shipped; Batch 8: S2.1 build pass, rows 122–146, 8 defects caught before publication, none shipped; Batch 7: S1.7 build pass, rows 106–121, 8 defects caught before publication, none shipped; Batch 6: S1.6 build pass, rows 88–105, 10 defects caught before publication, none shipped; Batch 5: S1.5 build pass, rows 70–87, 9 defects caught before publication, none shipped; Batch 4: S1.4 build pass, rows 53–69, 9 defects caught before publication, none shipped; Batch 3: S1.3 build pass, rows 36–52, 9 defects caught before publication, none shipped; Batch 2: S1.2 build pass, rows 17–35, 4 defects caught before publication, none shipped; Batch 1: S1.1, 16 rows)

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

## Batch 7 — S1.7 Capstone: the investigation report

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 106 | S1.7 | Berkeley Protocol ch. VII "Reporting on findings": para 210 six sections "unless there is a justifiable and articulated reason not to" — investigative objectives ("well-defined, articulable research questions"), methodology ("to enable replicability"), performed activities, underlying data and sources, gaps or uncertainties, results and recommendations; para 208 (a) accuracy incl. "an explanation of any redactions or gaps", (b) attribution "clearly distinguish" public content from investigators' judgement, (c) completeness "an indication of the completeness of the underlying data", (e) neutral language; footnote 168 recommends peer review | `SOURCED` | OHCHR PDF (`ohchr.org/sites/default/files/2024-01/OHCHR_BerkeleyProtocol.pdf`), text extracted with pdftotext and read, 2026-09-25 | stable |
| 107 | S1.7 | ICD 203 *Analytic Standards*: signed 2 January 2015 (Clapper), technical amendments since (one cites a 2022 DNI memo); tradecraft standards (1) source quality, (2) uncertainty incl. confidence based on "the quantity and quality of source material", (3) "clearly distinguish statements that convey underlying intelligence information" from "assumptions or judgments"; likelihood table 7 bands 01–05 / 05–20 / 20–45 / 45–55 / 55–80 / 80–95 / 95–99 % with the two rows of terms as taught; "strongly encouraged not to mix terms from different rows" without a disclaimer; "must not combine a confidence level and a degree of likelihood … in the same sentence" | `SOURCED` | `archive.dni.gov/files/documents/ICD/ICD-203.pdf` (dni.gov and odni.gov 301 there), text extracted and read, 2026-09-25 | on ODNI revision |
| 108 | S1.7 | PHIA *Explaining Uncertainty in UK Intelligence Assessment*, GOV.UK, published 24 March 2025: Remote Chance >0–≈5 %, Highly Unlikely ≈10–≈20, Unlikely ≈25–≈35, Realistic Possibility ≈40–<50, Likely or Probable ≈55–≈75, Highly Likely ≈80–≈90, Almost Certain ≈95–<100; analytical confidence "reflects the soundness and stability of the foundations on which the assessment of likelihood has been made"; High, Moderate or Low | `SOURCED` | raw GOV.UK HTML fetched with curl and decoded, 2026-09-25 (a summariser's reading was re-checked against it) | yearly |
| 109 | S1.7 | PHIA bands have gaps (nothing covers ≈5 % to ≈10 %); "likely" differs: ICD 55–80 % vs PHIA ≈55–≈75 % | `SOURCED` | follows arithmetically from rows 107–108. A search summary's "deliberately leave gaps" was **not** found in a page read, so the word "deliberate" was removed | with 107/108 |
| 110 | S1.7 | HIBP `?Domain=` "Filters the result set to only breaches against the domain specified"; searching addresses at a domain needs verified control (back-pointer row 72) | `SOURCED` | haveibeenpwned.com/API/v3, curl 2026-09-25 | 6 months |
| 111 | S1.7 lab | IANA "Example Domains" page: example.com "maintained for documentation purposes" (RFC 2606, RFC 6761), "not available for registration or transfer", "Last revised 2017-05-13"; footer: IANA functions "provided by Public Technical Identifiers, an affiliate of ICANN"; 6,639 bytes, SHA-256 `6fde51fc02d6…` identical across all runs | `EXECUTED` | item003, lab runs 2026-09-25 | stable |
| 112 | S1.7 lab | Verisign RDAP example.com: registration 1995-08-14T04:00:00Z; one entity, role `registrar`, handle 376, fn "RESERVED-Internet Assigned Numbers Authority"; nameservers ELLIOTT.NS.CLOUDFLARE.COM, HERA.NS.CLOUDFLARE.COM; 2,440 bytes; hash differs between runs (RDAP database timestamp, row 12) | `EXECUTED` | item001, lab + Drill 3 | volatile (nameservers, hash) |
| 113 | S1.7 lab | IANA registrar-ID CSV line `376,RESERVED-Internet Assigned Numbers Authority,Reserved,` (header `ID,Registrar Name,Status,RDAP Base URL`); 280,510 bytes | `EXECUTED` | item002 | volatile (file) · stable (row 376) |
| 114 | S1.7 lab | GLEIF exact legal name "Internet Corporation for Assigned Names and Numbers" → LEI 2549008HATEG8EESS568, ISSUED, jurisdiction US-CA; exact name "Public Technical Identifiers" → 0 records (a fuzzy-completion probe also returned none); the course draws no conclusion from the zero | `EXECUTED` | items 004–005 + one fuzzycompletions probe, 2026-09-25 | volatile |
| 115 | S1.7 lab | HIBP `breaches?Domain=example.com` → `[]`, SHA-256 `4f53cda18c2b…` (the two bytes `[]`) | `EXECUTED` | item006 | volatile |
| 116 | S1.7 | F2's two sources "agree" but are not independent: the registry repeats IANA's own registrar-ID assignment | `CONVENTION` | reasoning: item002 is IANA's registry of the IDs the registry cites, and the name strings are identical; stated as the course's reading, not a sourced fact | — |
| 117 | S1.7 | Nameservers show who answers DNS for a name, not who controls it | `CONVENTION` | DNS delegation vs registration are separate records (item001 lists both as separate fields); stated as course reasoning | — |
| 118 | S1.7 | Report Assessment "almost certain … (F1-F5)" + "Analytical confidence: high" with reasons | `CONVENTION` | analyst judgement on PHIA's scale, taught as a worked example of the two-sentence form (row 107) | — |
| 119 | S1.7 case | SSCI review of the October 2002 NIE *Iraq's Continuing Programs for Weapons of Mass Destruction*, published July 2004: Conclusion 1 quote incl. "a series of failures, particularly in analytic trade craft"; "has chemical and biological weapons" overstated, narrower support as taught; "did not have enough information to state with certainty that Iraq 'has' these weapons"; Conclusion 2 "portrayed what intelligence analysts thought and assessed as what they knew…"; Kent 1964 quote; Conclusion 4 "layering", tanker truck → transshipment → "as much as 500 metric tons of chemical agent"; mobile BW "largely from a single source to whom the Intelligence Community did not have direct access"; ballistic-missile assessments "reasonable" | `SOURCED` | globalsecurity.org mirror of the conclusions (`…/2004_rpt/iraq-wmd_intell_09jul2004_conclusions.htm`), raw HTML read 2026-09-25. Mirror, not senate.gov: re-check against the committee's own PDF | stable |
| 120 | S1.7 lab | Lab run 5× (3 bash, 2 zsh) plus the lab extracted from the built HTML, run in zsh from an empty HOME: six items, no FAILED, 7 findings / 9 citation checks PASS, seal verifies, all six evidence files OK. Wording guard tested with a changed role value. Windows variant **not run** (no PowerShell on this Mac; stated in the lab) | `EXECUTED` | lab runs + built-HTML round-trip (lab, windows, workbench, theory, linux, case, expected all MATCH) | stable |
| 121 | S1.7 Drills | D1: 3 FIX + sentence 4 passes by design; D2: no citation / not in log / hash differs / `UNKNOWN` exit 2; D3: item001 bytes CHANGED, items 002–006 same, facts behind F1–F4 SAME. Each drill run in bash and zsh with identical output | `EXECUTED` | drill runs 2026-09-25 | volatile (D3) |

Defects caught in the S1.7 build pass (none shipped):

- **The draft lab quoted IANA's page in F5 while its own check printed `0` matches.** The page wraps
  "They are not / available…" across lines and puts `<a>` tags inside the PTI sentence, so `grep -c`
  on raw HTML saw nothing, and the report quoted the page regardless. The lab now strips tags,
  joins lines, tests all three phrases, and stops if any is missing. Guard A99.
- **The draft report's hand-typed wording was unguarded.** "It names no registrant", the status
  "Reserved" and the ICANN LEI sentence would have stayed true-sounding if a source changed. One
  guard now stops the lab if any assumption fails. Tested by changing the role value.
- **The GLEIF shell variable ended in `…legalName%5D=`**, and the URL gate probed it as a URL (HTTP
  400, gate FAIL). It is now the real endpoint `…/lei-records`, and the filter is on each call.
- **The draft lab's `rm -f evidence/item*` would abort under zsh** (`nomatch`) on a first run with no
  evidence yet. Caught in review before the first run; the lab now removes and recreates the folder.
- **The draft verification step piped through `tail -3`**, hiding three of the six evidence checks.
- **Draft theory said "one claim per finding"** while F2 and F6 each carry two facts; called absence
  and agreement "the commonest overclaims" (unsourced); said addresses @example.com "belong to
  people" (overclaim); and called PHIA's gaps "deliberate" (from a search summary, row 109).
- **The draft case study said "every failure it named"** has a counterpart here. The committee's
  Conclusion 3 (group think) does not, so it now says "each failure described here".
- **Draft Challenge 2 compared F2 to "layering"**, which is about uncertainty not carried forward.
  F2's problem is single-source dependence, which the committee also found (mobile BW units).

## Batch 8 — S2.1 Web archives: page history, and what a capture proves (and the Level 2 shell)

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 122 | S2.1 | RFC 7089 (Memento, Dec 2013): a `Memento-Datetime` header "expresses the datetime of that state"; its presence "constitutes a promise that the resource state reflected in the response will no longer change"; the original URI is the target of a `Link` with `rel="original"` | `SOURCED` | rfc-editor.org/rfc/rfc7089.txt (Memento-Datetime section, text lines 372–386), curl 2026-09-25 | stable |
| 123 | S2.1 | CDX server README: `from`/`to` ranges "are inclusive", "same 1 to 14 digit format" `yyyyMMddhhmmss`; collapse note "only adjacent digest are collapsed, duplicates elsewhere in the cdx are not affected"; `limit=N` returns the first N; public fields urlkey, timestamp, original, mimetype, statuscode, digest, length | `SOURCED` | raw.githubusercontent.com internetarchive/wayback `wayback-cdx-server/README.md`, 2026-09-25 | yearly |
| 124 | S2.1 | WARC 1.1: `WARC-Payload-Digest` is a labelled-digest, example "a SHA-1 labelled Base32 ([RFC4648]) value"; "The payload of an application/http block is its 'entity-body' (specified in [RFC 2616])" | `SOURCED` | iipc/warc-specifications `specifications/warc-format/warc-1.1/index.md` via `gh api`, 2026-09-25 | stable |
| 125 | S2.1 | RFC 2616 §7.2.1: `entity-body := Content-Encoding( Content-Type( data ) )`, so a gzip-encoded response's payload is the compressed bytes | `SOURCED` | rfc-editor.org/rfc/rfc2616.txt line 2377 | stable |
| 126 | S2.1 | Internet Archive CDX-Writer: `new_style_checksum` returns the record's `WARC-Payload-Digest` minus `sha1:` (or base32 of the SHA-1 of the content when absent); field `S` = "compressed record size". IIPC CDX-2015 legend also lists "S compressed record size" | `SOURCED` | raw.githubusercontent.com internetarchive/CDX-Writer `cdx_writer.py` lines 443–459, 713; iipc/warc-specifications `cdx-format/cdx-2015/index.md` line 71 | stable |
| 127 | S2.1 | The CDX API's `length` is the compressed record size, not the page size: the 339-byte page has index lengths 481, 477, 476, 459; the 6,814-byte ICANN page has 1,792 | `EXECUTED` | row 126 names the field; lab item001 + `id_` byte counts, 2026-09-25 | stable |
| 128 | S2.1 | `id_` returns the stored bytes: base32 SHA-1 of the `id_` body equals the index digest for 20020120142510 (`HT2D…`), 20020328012821 and 20020604040806 (`UY3I…`), 20240101000832 (`JI6O…`), 20240101002738 (`WJM2…`) and 20140717152222 (`PDK2…`). No help.archive.org page documents `id_`; a search found only archive.org forum threads (post/1008502 "FAQ On 'id_' Wayback Toolbar Removal", post/1044859) and third-party guides | `EXECUTED` | lab, drills and case checks 2026-09-25; WebSearch 2026-09-25 for the documentation claim | yearly (documentation) |
| 129 | S2.1 lab | 2002 index for `url=example.com/`: 51 lines, all 200 text/html; 50 × `UY3I2DT2AMWAY6DECFCFYMT5ZOTFHUCH`, 1 × `HT2DYGA5UKZCPBSFVCV3JOBXGW2G5UUA`; originals `http://example.com:80/` and `http://www.example.com:80/` interleaved in 8 runs; 20020120142510 = ICANN "Reserved Domain Names", 20020604040806 = next capture of the same URL, "Example Web Page"; 20020328012821 = `www.`; window 2002-01-20T14:25:10Z → 2002-06-04T04:08:06Z; item001 SHA-256 `fb0f477a10e7…` identical in both runs | `EXECUTED` | lab runs 2026-09-25 (bash + zsh) | volatile (index may gain or lose captures) |
| 130 | S2.1 lab | `id_` responses carry `memento-datetime` equal to the 14-digit timestamp as an HTTP date in GMT, and a `Link` with `rel="original"`; the 2002 captures' `x-archive-src` names `.arc.gz` files (ARC, WARC's predecessor) | `EXECUTED` | item002–004 `.headers`; probe headers 2026-09-25 | stable |
| 131 | S2.1 Drill 1 | 2024 index (status 200, collapse=digest) lines `20240101000832 JI6O… 778` and `20240101002738 WJM2… 1334`; `id_` bodies 1,256 bytes plain and 648 bytes with `content-encoding: gzip`; gunzip gives the first body byte for byte. `curl --compressed` would decode before saving, so its hash cannot match (guard A100) | `EXECUTED` | 2024 CDX query + drill runs in bash and zsh, 2026-09-25 | stable |
| 132 | S2.1 Drill 1 | `3I42H3S6NNFQ2MSVX7XZKYAYSCX5QBYJ` is the base32 SHA-1 of zero bytes; the 2024 index filtered to status 200 contains lines with it; `id_` of 20240805072352 returned 0 bytes. The 2014 vk.com 302 captures carry the same digest | `EXECUTED` | `b32sha1 /dev/null`; 2024 query; Strelkov index | stable |
| 133 | S2.1 | help.archive.org "Using the Wayback Machine": missing sites because "automated crawlers were unaware of their existence", "password protected, blocked by robots.txt, or otherwise inaccessible", or owners "requested that their sites be excluded"; Save Page Now saves "a specific page one time" | `SOURCED` | help.archive.org/help/using-the-wayback-machine/, curl 2026-09-25 | yearly |
| 134 | S2.1 | Exclusion: email info@archive.org with the URL(s) and time period(s); "We do not make any guarantees beforehand about the outcome of a request" | `SOURCED` | help.archive.org/help/how-do-i-request-to-remove-something-from-archive-org/, curl 2026-09-25 | yearly |
| 135 | S2.1 | Mark Graham, "Robots.txt meant for search engines don't work well for web archives", blog.archive.org 17 April 2017 (author box: "Director of the Wayback Machine"): parked-domain robots.txt "has historically also removed the entire domain from view in the Wayback Machine"; complaints about "disappeared" sites "almost daily" | `SOURCED` | blog.archive.org 2017/04/17 post, curl 2026-09-25 | stable |
| 136 | S2.1 | No official published CDX rate limit (search found none). Staff reply relayed in edgi-govdata-archiving/wayback issue #137 (2023-11-01): /cdx "limited to an average of 60/min"; 429s beyond; "If 429s are ignored for more than a minute we block the IP at the firewall (no connection) for 1 hour", doubling on repeat. Taught as a relayed 2023 statement that may have changed | `SOURCED` | `gh api repos/edgi-govdata-archiving/wayback/issues/137`, 2026-09-25 | 6 months |
| 137 | S2.1 | "While this module was being built, the archive returned both" 429 and 503: availability API 429; CDX 503 "Temporarily Offline" and 504 on 2024–2026 windows; the 2002 query answered in 16–53 s | `EXECUTED` | build session 2026-09-25 | volatile |
| 138 | S2.1 | Save Page Now makes the archive request the live page (so the target receives a request) and stores the capture in the public archive | `CONVENTION` | follows from what SPN is (a capture of the live page on demand, row 133); not used in any lab | — |
| 139 | S2.1 | The crawler saw one response, from one place, logged out, at one time | `CONVENTION` | a capture is one HTTP response (rows 122, 124); stated as course reasoning | — |
| 140 | S2.1 case | Dutch Safety Board: 9N314M warhead launched by a Buk system detonated at "13.20 UTC"; "All 298 occupants were killed" | `SOURCED` | onderzoeksraad.nl press page (dated 22 October 2015), curl 2026-09-25 | stable |
| 141 | S2.1 case | Bellingcat, Aric Toler, "In Their Own Words", 16 July 2015: translation "In the area of Torez an AN-26 plane was just shot down…"; "Strelkov (Girkin) himself did not post this message; rather, some 'fans' of his posted the message from local information"; "It was taken down as soon as it was evident that a passenger plane, not an AN-26 transport plane, was shot down"; links web.archive.org/web/20140717152222/http://vk.com/strelkov_info | `SOURCED` | bellingcat.com raw HTML, curl 2026-09-25 | stable |
| 142 | S2.1 case | *The Interpreter*, "Russia Update: July 16, 2015", Catherine A. Fitzpatrick: "the group was in fact authorized to release Strelkov's statements (which indeed it was)"; "The stream of posts from Strelkovs' Dispatches on VK shown in the Wayback Machine at archive.org contain a post on the downing of a plane 13 minutes before the famous one". The "Strelkov reports" banner point is reported there as someone else's ("He also notes"), not hers, and the course does not use it (guard A101) | `SOURCED` | interpretermag.com raw HTML, curl 2026-09-25 | stable |
| 143 | S2.1 case | CDX `vk.com/strelkov_info` 2014-07-17: every capture before 15:22:22 is a 302 with digest `3I42…`; 20140717152222 is the first 200 (`PDK2M6YDLKW5UM6QATHVZGWKYM2252VD`, length 18497); `id_` body 76,429 bytes, SHA-1 matches, `charset=windows-1251`; text includes "17.07.2014 17:50 (мск) Сообщение от ополчения. "В районе Тореза только что сбили самолет Ан-26" | `EXECUTED` | one CDX query + one `id_` fetch, 2026-09-25 | stable |
| 144 | S2.1 Drill 2 | IANA tz database (Python `zoneinfo`): Europe/Moscow UTC+4 from 2011-03-27 to 2014-10-26 02:00 local, then UTC+3; 20140717152222 → 19:22:22+04:00 MSK; 17:50 MSK = 13:50 UTC; capture 2:02:22 after 13:20 UTC. (macOS `date` printed the right hour with a `+0300` label for the same instant, so the course uses `zoneinfo`.) `zoneinfo` needs Python 3.9+ | `EXECUTED` | zoneinfo transition scan + drill runs, bash and zsh | stable |
| 145 | S2.1 lab | Lab run twice (bash, zsh; fresh HOMEs): identical output, four requests logged 200, three MATCH. Drills 1–3 run in bash and zsh with identical output. Built HTML round-trip: lab, windows, workbench, theory, linux, case, expected all MATCH. Windows variant **not run** (no PowerShell on this Mac); its base32 routine was replayed in Python against three known digests | `EXECUTED` | runs 2026-09-25 | stable |
| 146 | S2.1 lab (Windows) | PowerShell 7's web cmdlets decode gzip automatically: `WebRequestSession.cs` sets `handler.AutomaticDecompression = DecompressionMethods.All` | `SOURCED` | PowerShell/PowerShell master `f8628c69f3` (2026-09-24), via `gh api` | yearly |

Defects caught in the S2.1 build pass (none shipped):

- **The first reading of the index was the tempting one.** Comparing the first two 2002 lines
  "dated" the change to 28 March, but line 2 is `www.example.com`. It became the lab's lesson: the
  lab picks captures by rule for one original URL and prints the wrong claim beside the right one.
- **A WebFetch summary gave Fitzpatrick someone else's argument** (the "Strelkov reports" banner).
  The raw page attributes it with "He also notes". Rewritten from the raw HTML (row 142, guard A101).
- **Draft drill 3 showed an invented digest** for the tampered file, which is a documented result
  that cannot happen. Replaced with the output of the actual run.
- **"16 captures" of the empty digest** came from a `collapse=digest` query, which counts runs,
  not captures. The number was removed.
- **The expected output said an error page "can arrive with a status that looks fine."** Only 503
  and 504 were ever seen. Reworded to what the check actually does.
- **Unsourced wording removed:** "the largest public web archive", CDX-Writer "builds these
  indexes", retroactive loss "on a large scale", "separatist commander", and "still divides
  careful people".
- **`curl -f` keeps an earlier file when a retry fails** (a stale 503 page was read as a new
  result). The lab deletes any non-200 body and starts from an empty `evidence/`.
- **The Windows comment said PowerShell "may" decode gzip.** The source says it always does (row 146).

## Batch 9 — S2.2 Network ownership: who holds an address, who routes it, who authorised it

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 147 | S2.2 | RFC 1930: an AS is "a connected group of one or more IP prefixes run by one or more network operators which has a SINGLE and CLEARLY DEFINED routing policy" | `SOURCED` | rfc-editor.org/rfc/rfc1930.txt line 134, curl 2026-09-25 | stable |
| 148 | S2.2 | AS path lists the newest hop first; the last AS is the origin | `SOURCED` | RFC 4271 §5.1.2: a speaker "prepends its own AS number as the last element of the sequence (put it in the leftmost position" (lines 1408–1409) | stable |
| 149 | S2.2 | Longest prefix wins: RIPE NCC calls it "the longest prefix match rule"; Cloudflare explains 1.1.1.1/32 as the "longest match" | `SOURCED` | ripe.net YouTube case study (17 Mar 2008); blog.cloudflare.com 1.1.1.1 incident post, curl 2026-09-25 | stable |
| 150 | S2.2 | RIS docs: "Currently dumps are created every 8 hours, and updates are created every 5 minutes"; archive URL `data.ris.ripe.net/rrcXX/YYYY.MM/TYPE.YYYYMMDD.HHmm.gz`; RRC00 Amsterdam listed as "multihop", scope "global" | `SOURCED` | ris.ripe.net/docs/mrt/ and /docs/route-collectors/, curl 2026-09-25 | yearly |
| 151 | S2.2 | RIPEstat network-info "returns the containing prefix and announcing ASN of a given IP address, based on information from RIPE RIS" | `SOURCED` | stat.ripe.net/docs/data-api/api-endpoints/network-info, curl 2026-09-25 | yearly |
| 152 | S2.2 | RIPEstat rules of usage: "No limit on the amount of requests but please register if you plan to regularly do more than 1000 requests/day"; "limits the usage to 8 concurrent … requests coming from one IP address"; `sourceapp` "alphanumeric values with no whitespace", hyphens and underscores allowed | `SOURCED` | stat.ripe.net/docs/data-api/ripestat-data-api, curl 2026-09-25 | yearly |
| 153 | S2.2 | routing-history docs: `min_peers` default 10, "Excludes low-visibility/localized announcements"; `full_peers_seeing` = "number of RIS full-feed peers that saw this route"; `latest_max_ff_peers` = maximum full-table peers per IP version. `time_granularity` is **not** documented; the course reports it only as an observed field (row 163) | `SOURCED` | stat.ripe.net/docs/data-api/api-endpoints/routing-history, curl 2026-09-25 | yearly |
| 154 | S2.2 | rpki-validation labels: `valid`; `invalid_asn` (covering ROA "but a different ASN"); `invalid_length` ("prefix length is greater than the ROA's maximum length"); `unknown` ("no ROA found") | `SOURCED` | stat.ripe.net/docs/data-api/api-endpoints/rpki-validation, curl 2026-09-25 | yearly |
| 155 | S2.2 | RFC 6811 states: NotFound "No VRP Covers the Route Prefix"; Valid "At least one VRP Matches the Route Prefix"; Invalid "At least one VRP Covers the Route Prefix, but no VRP Matches it" | `SOURCED` | rfc-editor.org/rfc/rfc6811.txt lines 246–251 | stable |
| 156 | S2.2 | RFC 9582 (May 2024, obsoletes 6482): maxLength "specifies the maximum length of the IP address prefix that the AS is authorized to advertise" | `SOURCED` | rfc-editor.org/rfc/rfc9582.txt line 286 | stable |
| 157 | S2.2 | RFC 7908 (June 2016): "A route leak is the propagation of routing announcement(s) beyond their intended scope" | `SOURCED` | rfc-editor.org/rfc/rfc7908.txt line 143 | stable |
| 158 | S2.2 | IANA: `001/8,APNIC,2010-01` (ALLOCATED); AS `13312-15359,Assigned by ARIN` | `SOURCED` | iana.org ipv4-address-space.csv and as-numbers-1.csv, curl 2026-09-25 | stable |
| 159 | S2.2 lab | network-info 1.1.1.1 → prefix `1.1.1.0/24`, asns `["13335"]` | `EXECUTED` | lab item001, 2026-09-25 | volatile |
| 160 | S2.2 lab | APNIC RDAP ip/1.1.1.1: `1.1.1.0-1.1.1.255`, name `APNIC-LABS`, registrant `APNIC Research and Development` (ORG-ARAD1-AP), remarks include "Routed globally by AS13335/Cloudflare" and "Research prefix for APNIC Labs", registration `2011-08-10T23:12:35Z` | `EXECUTED` | lab item002, 2026-09-25 | yearly |
| 161 | S2.2 lab | ARIN RDAP autnum/13335: name `CLOUDFLARENET`, registrant `Cloudflare, Inc.`, registration `2010-07-14T18:35:57-04:00` (= 22:35:57 UTC) | `EXECUTED` | lab item003, 2026-09-25 | yearly |
| 162 | S2.2 lab | rpki-validation AS13335 / 1.1.1.0/24 → `valid`, one ROA AS13335 1.1.1.0/24 max_length 24 | `EXECUTED` | lab item004, 2026-09-25 | volatile |
| 163 | S2.2 lab | routing-history 1.1.1.0/24, 2000-08-01 → 2026-09-01: `time_granularity` 1036800 (12 days); other prefixes 0.0.0.0/1, 0.0.0.0/3, 1.0.0.0/8, 1.1.0.0/16, 1.1.1.0/30, 1.1.1.1/32; 33 origins of the exact /24 before AS13335's first bucket (2018-03-14T00:00:00), 14 of them in buckets starting before 2010-01-01; `latest_max_ff_peers` v4 330 | `EXECUTED` | lab item005 + jq, 2026-09-25 | stable (fixed window) |
| 164 | S2.2 lab | Hashes differ run to run: RIPEstat replies carry `query_id`/`server_id`/`process_time`; APNIC and ARIN RDAP returned one entity's roles as `technical, administrative` then `administrative, technical` a minute apart | `EXECUTED` | `jq -S` diff of two runs' evidence, 2026-09-25 | volatile |
| 165 | S2.2 lab | Lab run in bash and zsh (fresh HOMEs): identical output apart from hashes; five requests logged 200. Built HTML round trip: lab, windows, workbench, theory, linux, case, expected all MATCH; lab extracted from the HTML re-run in zsh: SAME. Windows variant **not run** (no PowerShell on this Mac) | `EXECUTED` | 2026-09-25 | — |
| 166 | S2.2 lab (Windows) | `ConvertFrom-Json -DateKind` (values Default, Local, Utc, Offset, String) "was introduced in PowerShell 7.5" | `SOURCED` | MicrosoftDocs/PowerShell-Docs `reference/7.5/…/ConvertFrom-Json.md` lines 175–188, raw.githubusercontent.com 2026-09-25 | yearly |
| 167 | S2.2 Drill 1 | routing-history 1.1.1.0/24, 2018-03-01 → 2018-04-30: `time_granularity` 28800 (8 h); AS13335 first bucket `2018-03-20T08:00:00`, full_peers_seeing 162.0; with `min_peers=0` AS28191 appears, bucket `2018-03-31T16:00:00`, 4 peers | `EXECUTED` | drill run in bash and zsh, identical, 2026-09-25 | stable |
| 168 | S2.2 Drill 2 | routing-history 208.65.153.0/24, 2008-02-24 → 2008-02-25T12:00, `min_peers=0`: exact prefix only AS36561 from 2008-02-25T00:00:00, no AS17557 (also absent over 20–28 Feb). RRC00 `updates.20080224.1845.gz` 22,498 bytes, SHA-256 `cc893c9c3b9431c2…`: 27 announcements of the /24, 18:47:57–18:49:19, every path ending `3491 17557`. RRC00's `bview` files for that day are stamped 07:59, 15:59, 23:59; the course labels "a history built from snapshots can miss it" as inference | `EXECUTED` | drill run in bash and zsh; directory listing data.ris.ripe.net/rrc00/2008.02/, 2026-09-25 | stable |
| 169 | S2.2 Drill 2 | RIPE NCC, "YouTube Hijacking: A RIPE NCC RIS case study", 17 Mar 2008: AS17557 starts announcing 208.65.153.0/24 at 18:47 UTC; YouTube /24 at 20:07, /25s at 20:18; AS3491 withdraws at 21:01; "When a routing event is still fresh, it's likely that the associated prefix announcement hasn't yet been included in an RIS RIB dump" | `SOURCED` | ripe.net/about-us/news/youtube-hijacking-a-ripe-ncc-ris-case-study/, curl 2026-09-25 | stable |
| 170 | S2.2 Drill 2 | RFC 6396: BGP4MP is type 16; subtypes 1 BGP4MP_MESSAGE, 4 BGP4MP_MESSAGE_AS4 | `SOURCED` | rfc-editor.org/rfc/rfc6396.txt lines 314, 687–688 | stable |
| 171 | S2.2 Drill 3 | bgp-updates `meta/availability` declares 2024-01-01 onward; yet 1.1.1.0/24 returns 0 for 12-hour windows on 2024-01-02, 06-01, 06-26, 06-27 and 06-28 (and 18:00–22:00 on 06-27), but 114 on 03-01, 88 on 07-01, 737 on 2026-09-01 00–12; 8.8.8.0/24 returns 0 on 2024-06-27 18–22 and 29 on 2026-09-01 00–12; 192.0.2.0/24 returns 0 on 2026-09-01 00–12. RRC00 `updates.20240627.1850.gz` exists (6,407,407 bytes). Checker: bad prefix → UNKNOWN exit 2; missing args → exit 64; runs under dash | `EXECUTED` | drill runs in bash, zsh, dash, 2026-09-25 | volatile |
| 172 | S2.2 case | Cloudflare, "Cloudflare 1.1.1.1 incident on June 27, 2024", Bryton Herdes, Mingwei Zhang, Tanner Ryan, 4 July 2024: "a mix of BGP … hijacking and a route leak"; 18:51 AS267613 "begins announcing 1.1.1.1/32…"; 18:52 AS262504 leaks 1.1.1.0/24 to AS1031 with path "1031 262504 267613 13335"; 18:52 a tier 1 accepts the /32 as RTBH, "causing blackholed traffic for all the tier 1's customers"; 02:28 (28 June) AS262504 "fully resolves the route leak"; "over 300 networks in 70 countries", "less than 1% of users in the UK and Germany"; ROA "only signed for origin AS13335 (Cloudflare) with a maximum prefix length of /24"; AS398465 and AS13760 reported the /32 to route-views collectors; BMP data; "historically misappropriated"; "erroneously leaked"; "routes to the nearest data center via BGP anycast". No statement of intent for the hijack (text searched for intent/malicious/deliberate) | `SOURCED` | blog.cloudflare.com/cloudflare-1111-incident-on-june-27-2024/, curl 2026-09-25 | stable |
| 173 | S2.2 case | rpki-validation today: AS267613 / 1.1.1.1/32 → `invalid_length`; AS13335 / 1.1.1.1/32 → `invalid_length`; AS13335 / 1.1.1.0/24 → `valid` | `EXECUTED` | three RIPEstat queries, 2026-09-25 | volatile |
| 174 | S2.2 | 192.0.2.0/24 is TEST-NET-1 and 203.0.113.0/24 a documentation range (RFC 5737) | `SOURCED` | as Batch 2 (S1.2) | stable |
| 175 | S2.2 | Any network can announce any prefix; BGP itself checks nothing, so an origin is a claim | `CONVENTION` | course reasoning; it is the problem RPKI/ROV exists to address (rows 155, 172) | — |
| 176 | S2.2 | ping, traceroute and port scans send packets to the target and through networks in between, so they are active and out of scope | `CONVENTION` | S1.1's passive/active line applied | — |
| 177 | S2.2 challenge | Hosting providers rent addresses to customers; an address may be a compromised machine or a proxy | `CONVENTION` | general practice, stated as reasoning, no statistic | — |

Defects caught in the S2.2 build pass (none shipped):

- **The first case-study plan could not work.** The YouTube 2008 hijack was to be shown from
  RIPEstat, but `bgp-updates` only holds data from 2024, and `routing-history` does not show
  AS17557 at all, even with `min_peers=0`. That absence became Drill 2's lesson, with the raw RIS file.
- **The 2024 incident was to be shown from `bgp-updates`.** RIPEstat returns zero for all of June
  2024 despite declaring coverage. That became Drill 3 and guard A102.
- **Windows `Collect` printed its status line to the output stream** while also returning the
  parsed JSON, so `$ni = Collect …` would have held an array. Fixed with `Write-Host` (guard A103).
- **`ConvertFrom-Json` turns date strings into DateTime**, so the Windows lab would have printed
  dates unlike the records. It now uses `-DateKind String` (PowerShell 7.5+, row 166).
- **The MRT reader used a backslash inside an f-string**, a syntax error before Python 3.12 (this
  Mac has 3.11). Rewritten with `%` formatting.
- **Unsourced wording removed:** route collectors "announce nothing back"; RRC00 "peers with
  networks anywhere"; the RIS archive "does not change old files".
- **"14 origins before IANA allocated 1.0.0.0/8"** counted buckets, not dates, against a month-level
  allocation date. Reworded to "buckets that began before January 2010".
- **Case draft said Cloudflare "calls the leak 'erroneous'"** and "every window tried in June 2024"
  for two prefixes. Now the exact phrase ("erroneously leaked"), and per-prefix counts (row 171).

## Batch 10 — S2.3 Passive DNS: what a name used to resolve to, and what a sighting proves

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 178 | S2.3 | Passive DNS was described by Florian Weimer, "Passive DNS replication", 17th Annual FIRST Conference, 2005 | `SOURCED` | draft-dulaunoy-dnsop-passive-dns-cof-13 §1 (ietf.org/archive/id), curl 2026-09-28 | stable |
| 179 | S2.3 | Sensors capture "cache fill" responses (authoritative → recursive), so they never see the client; the method is "intended to minimize the privacy implications to users" | `SOURCED` | COF draft -13 §1 | stable |
| 180 | S2.3 | Authoritative servers "may serve different answers to different query addresses" (RFC 7871 client subnet) | `SOURCED` | COF draft -13 §1 | stable |
| 181 | S2.3 | COF is an Internet-Draft, revision 13, intended Informational, ISE stream, state Expired ("Expires: 28 February 2025"); never an RFC | `SOURCED` | datatracker API doc + state/2 ("Expired"), and the -13 text header, 2026-09-28 | 2027-03 |
| 182 | S2.3 | COF mandatory fields rrname, rrtype, rdata, time_first, time_last; time_first = "the first time that the record / unique tuple (rrname, rrtype, rdata) has been seen by the passive DNS", UTC Unix seconds | `SOURCED` | COF draft -13 §3.3, §3.3.4–3.3.5 | stable |
| 183 | S2.3 | COF count = "how many authoritative DNS answers were received at the Passive DNS server's collectors" (optional field) | `SOURCED` | COF draft -13 §3.4.1 | stable |
| 184 | S2.3, challenge | "a snapshot-in-time answer"; clients should not "assume that answers will be identical across multiple Passive DNS servers" | `SOURCED` | COF draft -13 §2 | stable |
| 185 | S2.3 | A shorter TTL means more refetches and so a higher count, whatever the traffic | `CONVENTION` | reasoning from row 183 and DNS caching; no statistic claimed | — |
| 186 | S2.3 | Filtering or misbehaving resolvers hand out answers the real servers never gave, and some reach passive DNS databases | `CONVENTION` | reasoning; illustrated, not proven, by the lab's 127.0.0.1 and count-1 rows (row 193). COF §2 names the bailiwick filter as one protection | — |
| 187 | S2.3 | RFC 5952 §4.1: leading zeros in an IPv6 field "MUST be suppressed" | `SOURCED` | rfc-editor.org/rfc/rfc5952.txt lines 523–527, curl 2026-09-28 | stable |
| 188 | S2.3 | mnemonic is a security company headquartered in Oslo | `SOURCED` | mnemonic.io footer "Oslo (HQ)", curl 2026-09-28 | 2027-09 |
| 189 | S2.3 | mnemonic public API: no key needed; "10 requests per minute, and 1000 requests per day"; TLP white only; HTTP 402 `resource.limit.exceeded` with `millisUntilResourcesAvailable`; public `limit` capped at 1000 (412 above) | `SOURCED` | www.docs.mnemonic.no/api/services/pdns/01-public_api.html, curl 2026-09-28 (docs.mnemonic.no without www 404s) | 2027-03 |
| 190 | S2.3 | mnemonic docs: records carry firstSeenTimestamp/lastSeenTimestamp; createdTimestamp and lastUpdatedTimestamp "always returns 0"; results sorted by lastSeenTimestamp; COF at /pdns/v3/cof/. Neither the public nor the private API page mentions `flags` or `partialResult` (grep: 0 hits each) | `SOURCED` | same page + 02-private_api.html, curl 2026-09-28 | 2027-03 |
| 191 | S2.3 lab | Unfiltered JSON for example.com: count 997, 994 rows flagged partialResult, all with firstSeenTimestamp 0, 17 IPv6 answers typed "a". The same records by `rrType`, or from COF, carry correct types and real times (filtered AAAA: flags [], firstSeen populated) | `EXECUTED` | lab item002 + rrType=aaaa query, 2026-09-28 | volatile |
| 192 | S2.3 lab | 21 A rows for example.com: 93.184.216.119 (2013-07-30→2014-12-10, 490); 93.184.216.34 (2017-01-29→2024-04-18, 334652); 93.184.215.14 (2024-04-18→2025-01-14); 23.x/96.7.x from 2025-01-15; 104.x/172.66.x from 2025-12-16; last 23.x sighting 20:03, first 104.x 18:37 on 2025-12-16 | `EXECUTED` | lab item001 (COF), three runs 2026-09-28; closed rows identical, open rows move | volatile |
| 193 | S2.3 lab | Single sightings 74.117.222.18, 210.211.113.133, 103.74.119.182 (count 1); 127.0.0.1 count 12, 2019-04-30→2021-03-23; total A answers 979633; no A row between 2014-12-10 and 2017-01-29 | `EXECUTED` | lab item001, 2026-09-28 | volatile |
| 194 | S2.3 lab | Google Public DNS JSON `Status` 0 = NOERROR; live A 104.20.23.154 + 172.66.147.243 = the newest COF pair | `SOURCED` / `EXECUTED` | developers.google.com/speed/public-dns/docs/doh/json, curl 2026-09-28; lab item003 | volatile |
| 195 | S2.3 lab | RDAP today: 93.184.216.0/24 EDGECAST-NETBLK-03 (RIPE, registered 2012-06-22); 23.192.0.0–23.223.255.255 AKAMAI (ARIN, 2013-07-12); 104.16.0.0–104.31.255.255 CLOUDFLARENET (ARIN, 2014-03-28). 96.7.128.x and 172.66.x were not looked up, and the course does not name their holders | `EXECUTED` | lab items 004–006, 2026-09-28 | volatile |
| 196 | S2.3 lab | IANA: 93/8 RIPE NCC; 23/8 and 104/8 ARIN | `SOURCED` | iana.org ipv4-address-space, as fetched for S2.2 (2026-09-25) | stable |
| 197 | S2.3 lab | Reverse 23.215.0.136: 7 names; example.com present; 4 under akamai.net; 2 others (not printed). 93.184.216.34: count 1000 | `EXECUTED` | lab items 007–008, 2026-09-28 | volatile |
| 198 | S2.3 Drill 1 | 17 AAAA records = 16 addresses; 2606:2800:021f:cb07:6820:80da:af6b:8b2c and 2606:2800:21f:… are one; merged 2024-04-19 09:04 → 2025-01-14 15:55, 1578 answers | `EXECUTED` | wb1, bash and zsh identical, 2026-09-28 | volatile |
| 199 | S2.3 Drill 2 | By type: a+aaaa 38, cname 515, ptr 993 (sum 1546) vs unfiltered 997; all 515 cname and 993 ptr rows have answer = example.com, 1 cname query under an IANA example name; 93.184.216.34 at offset 1000 → 0 rows | `EXECUTED` | wb2 + per-type pulls, 2026-09-28 | volatile |
| 200 | S2.3 Drill 3 | COF grading 35 SEEN OVER TIME + 3 SINGLE SIGHTING; JSON view 38 UNKNOWN; without the UNKNOWN branch 35 UNDER A DAY + 3 SINGLE; 93.184.216.34 createdTimestamp − COF time_first = 248,397 s | `EXECUTED` | wb3 + one-off comparison script, 2026-09-28 | volatile |
| 201 | S2.3 case | Krebs, "A Deep Dive on the Recent Widespread DNS Hijacking Attacks", KrebsOnSecurity, 18 Feb 2019: US government and security companies warned; "suspected Iranian hackers"; Talos write-up 27 Nov 2018 dubbed "DNSpionage"; CrowdStrike addresses run "through both Farsight Security and SecurityTrails"; "more than 50 Middle Eastern companies and government agencies"; mail.gov.ae; 139.59.134[.]216 "home to just seven different domains over the years", two only in Dec 2018; ns0.idm.net.lb at 194.126.10[.]18 "From early 2014 until December 2018", changed Dec. 18, 2018; sa1.dnsnode.net and fork.sth.dnsnode.net (Netnod, "a major global DNS provider based in Sweden"); certificates "sometimes weeks, sometimes just days or hours" later, Comodo/Let's Encrypt, visible at crt.sh; Netnod CEO confirmed hijacks after attackers gained access to registrar accounts (Krebs's paraphrase); Woodcock: four attacks, tools on "roughly one hour"; PCH "no fewer than three monitoring systems", none alerted (Krebs's paraphrase) | `SOURCED` | krebsonsecurity.com/2019/02/a-deep-dive-on-the-recent-widespread-dns-hijacking-attacks/, raw HTML curl 2026-09-28, datetime 2019-02-18T09:50:05-05:00 | stable |
| 202 | S2.3 | example.com and the .example TLD are reserved for documentation (RFC 2606); 198.51.100.0/24 is a documentation range (RFC 5737) | `SOURCED` | as rows 10 and 174 | stable |
| 203 | S2.3 | Querying a domain's authoritative servers directly lands in the log of whoever runs them; asking a public resolver lands in the resolver's | `CONVENTION` | S1.1's whose-log test applied | — |
| 204 | S2.3 | A forgotten record pointing to an address you gave up is how subdomain takeovers begin | `CONVENTION` | general practice, stated without a statistic | — |
| 205 | S2.3 | Windows variant not run (no pwsh on the build Mac); it says so in its header | `CONVENTION` | as S1.7–S2.2 | — |

Defects caught in the S2.3 build pass (none shipped):

- **The first plan dated records from mnemonic's JSON `firstSeenTimestamp`.** Every unfiltered row
  had it as 0, flagged `partialResult`, a flag the documentation never mentions. The lab now dates from COF,
  and Drill 3 grades JSON rows UNKNOWN (guard A104 blocks code that reads `createdTimestamp` instead).
- **The lab set `PDNS=https://api.mnemonic.no/pdns/v3`**, a bare base that 404s under the URL gate.
  Every request now spells out its full endpoint.
- **"127.0.0.1 … in a history of hundreds of thousands"** was hand-typed around extracted values.
  Now computed: 12 of 979,633. A draft "never from its servers" was unprovable and removed.
- **Case draft said "several governments"** warned; Krebs says the US government (guard A105).
- **Case draft put Krebs's paraphrases in the mouths of Netnod's CEO and PCH's Woodcock** as quotes.
  Now attributed to Krebs; only "roughly one hour" and "no fewer than three monitoring systems" are quoted (A105).
- **Drill 3 draft said a grader without UNKNOWN gives `UNDER A DAY` "38 times over".** Run, it is 35
  plus 3 single sightings. Its "24 seconds" example belonged to a different record from the one named. Replaced
  with the measured 248,397 s for 93.184.216.34.
- **Theory said the lab shows "hundreds of strangers'" CNAME/PTR records.** The lab never fetches them.
  Now points to Drill 2's measured counts. "Norwegian" became "headquartered in Oslo", the wording the site uses.
- **Expected-output notes named the Akamai and Cloudflare eras from one RDAP lookup each.** Now "the 23.x
  addresses (in the block registered today as AKAMAI)"; 96.7.x and 172.66.x holders are not claimed. "Byte-identical
  mnemonic replies" was scoped to runs minutes apart after a later run's COF hash changed.
- **Theory said old and new answers overlap "because cached answers live on until they expire".** The
  lab's overlap is about 90 minutes against 300-second TTLs, so caching alone cannot be asserted as the
  reason. Now names two possible causes and says the record does not tell you which.

## Batch 11 — S2.4 Document metadata: what a file says about who made it, and what that proves

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 206 | S2.4 | A .docx is a zip of XML parts; `docProps/core.xml` holds creator, lastModifiedBy, revision, created, modified; `docProps/app.xml` holds Application, AppVersion, TotalTime, Company, Template | `EXECUTED` | lab steps 4–5 on five pinned versions, 2026-09-28 | stable |
| 207 | S2.4 | creator = "an entity primarily responsible for making the content"; lastModifiedBy = "the user who performed the last modification. The identification is environment-specific. Examples include a name, email address, or employee ID." | `SOURCED` | python-docx docs, dev/analysis/features/coreprops (curl 2026-09-28) | stable |
| 208 | S2.4 | revision "might indicate the number of saves or revisions, provided the application updates it after each revision" | `SOURCED` | python-docx coreprops page | stable |
| 209 | S2.4 | TotalTime = "Total Edit Time Metadata Element"; w:rsid = "Single Session Revision Save ID" | `SOURCED` | learn.microsoft.com Open XML SDK class pages ExtendedProperties.TotalTime, Wordprocessing.Rsid | stable |
| 210 | S2.4 | PDF information dictionary fields title, author, subject, creator, producer, creation date, modification date; "All the following could be None!" | `SOURCED` | pypdf 6.19.0 docs, user/metadata | stable |
| 211 | S2.4 | PDF Creator = the program that made the original of a converted file; Producer = the program that converted it to PDF | `SOURCED` | pypdf docs, DocumentInformation.creator / .producer | stable |
| 212 | S2.4 | PDF dates are written `D:YYYYMMDDHHmmSS` plus an offset with apostrophes, e.g. `-05'00'` | `SOURCED` | pypdf user/metadata "Writing metadata" example | stable |
| 213 | S2.4, challenge | Incremental update: "the original document is written first and new/modified content is appended" | `SOURCED` | pypdf docs, PdfWriter `incremental` parameter. pdfa.org forensics pages 403 to scripts here: not used | stable |
| 214 | S2.4 | A PDF can hold the same facts again in XMP, and nothing forces the two copies to agree | `CONVENTION` | pypdf reads both (row 210 page); agreement is not a format requirement stated anywhere read | — |
| 215 | S2.4 | W3C date-time: TZD = "Z or +hh:mm or -hh:mm" | `SOURCED` | w3.org/TR/NOTE-datetime | stable |
| 216 | S2.4 | ZIP entry time: "standard MS-DOS format", "year values relative to 1980 and 2 second precision" | `SOURCED` | PKWARE APPNOTE.TXT 6.3.10 (rev. 1 Nov 2022) §4.4.6 | stable |
| 217 | S2.4 | Python zipfile: the central-directory timestamp is "interpreted as representing local time"; the format "does not support timestamps before 1980" | `SOURCED` | docs.python.org/3/library/zipfile | stable |
| 218 | S2.4, Drill 3 | A zip time of 1980-01-01 00:00 is the format's lowest valid value: read it as "no time recorded" | `CONVENTION` | derived from row 216; Word-era v1 and v2 hold it for every part | — |
| 219 | S2.4 | git takes author and committer dates from GIT_AUTHOR_DATE / GIT_COMMITTER_DATE when set | `SOURCED` | git-scm.com/docs/git-commit, COMMIT INFORMATION | stable |
| 220 | S2.4 | python-docx is MIT-licensed; default.docx was first committed with author date 2013-08-15 | `SOURCED` | GitHub API repos/python-openxml/python-docx (license MIT); lab item001 | stable |
| 221 | S2.4 | Eight commits touch docx/templates/default.docx up to 80740f2c; four show a committer date later than the author date; e75d056a authored 2013-08-15, committed 2013-12-21 | `EXECUTED` | lab step 3 | stable (pinned sha) |
| 222 | S2.4 | v1–v3 share one creator (not a personal name, an organisation label), v2–v3 add a personal lastModifiedBy; v4 (commit 215ecebacc, "tmpl: change core props author to python-docx") sets creator python-docx and empties lastModifiedBy | `EXECUTED` | lab step 5; values printed only as pseudonyms/labels | stable |
| 223 | S2.4 | created moves from 2013-08-14T00:12Z (v1) to 2013-12-23T23:15Z (v2 onward) | `EXECUTED` | lab step 5 | stable |
| 224 | S2.4, Drill 1 | v2→v3: only word/document.xml differs (zip time 2013-12-31 23:26:02), modified unchanged; v4→v5: core.xml bytes differ with identical values, settings.xml loses `w:percent="203"` | `EXECUTED` | lab step 5, Drill 1 | stable |
| 225 | S2.4 | docProps/thumbnail.jpeg has identical bytes in all five versions | `EXECUTED` | per-part SHA-256 96367138dc44… across v1–v5 | stable |
| 226 | S2.4 | All five versions name Microsoft Macintosh Word 14.0000 in app.xml | `EXECUTED` | lab step 5 | stable |
| 227 | S2.4 | The forged copy: new file SHA-256, identical document.xml SHA-256 and zip times | `EXECUTED` | lab step 6 | stable |
| 228 | S2.4, Drill 3 | Commit Date headers: 629cadb2, 215eceba, 90fc91c7 at −0800; e75d056a, d563fa4a at −0700. In the committer's zone v4 and v5 were packed 2.2 and 10.1 min before commit; v3 22 h | `EXECUTED` | github.com/…/commit/<sha>.patch headers, Drill 3 | stable |
| 229 | S2.4, Drill 2 | A plain-hash tag of a name can be confirmed by anyone who guesses the name; an HMAC tag cannot be tested without the key | `EXECUTED` | Drill 2 (guess = the name the lab itself wrote) | — |
| 230 | S2.4 | GitHub primary rate limit for unauthenticated REST requests: 60 an hour | `SOURCED` | docs.github.com rate-limits-for-the-rest-api | 2027-03 |
| 231 | S2.4 | Document Inspector: File → Info → Check for Issues → Inspect Document (Word for Windows); run it "on a copy of your original document, because it is not always possible to restore the data…"; "some information that the Document Inspector cannot remove" | `SOURCED` | support.microsoft.com "Remove hidden data and personal information by inspecting documents…" | 2027-03 |
| 232 | S2.4 case | Rangwala (casi list, 5 Feb 2003): dossier "released last Thursday" (30 January 2003), downloadable Word version; "the bulk of the 19-page document (pp.6-16) is directly copied without acknowledgement" from al-Marashi's Sept 2002 MERIA article; the misplaced-comma example; Gause and Boyne also copied | `SOURCED` | casi.org.uk/discuss/2003/msg00457.html (raw HTML) | stable |
| 233 | S2.4 case | Rangwala lists four names "in Word > Properties" | `SOURCED` | row 232 source | stable |
| 234 | S2.4 case | Smith, 30 June 2003: ten-entry revision log (users and paths as tabled, names replaced by roles); `A:` saves; hearings in the week of 23 June 2003; "One reporter quickly identified the four individuals"; cic22 glossed as "Communications Information Centre" | `SOURCED` | Wayback 20030703054403id_ of computerbytesman.com/privacy/blair.htm (live page 404; dfir.com.br copy now empty) | stable |
| 235 | S2.4 case | Smith: "PDF files do not contain revision logs or hidden author information" is quoted as a claim that fails | `SOURCED` | row 234 quote; contradicted by rows 210 and 213 | stable |
| 236 | S2.4 | Officials in the case, and personal names in the lab files, appear as roles or pseudonyms only | `CONVENTION` | course practice since S1.4 | — |
| 237 | S2.4 | Windows variant not run (no pwsh on the build Mac); it says so in its header | `CONVENTION` | as S1.7–S2.3 | — |

Defects caught in the S2.4 build pass (none shipped):

- **Drill 1's first comparison read tags and text only.** It scored v4→v5 `settings.xml` "same values"
  though `w:percent="203"` was gone. Now compares attributes too; guard A106 blocks the attribute-blind form.
- **The pseudonymiser hid the product name "python-docx"** along with personal names, so the finding read
  "became person#…". Now an analyst-checked `LABELS` set prints product names; everything else stays a tag.
- **The clock column floored to whole days**, printing "0 days later" for a 7-minute gap. Now hours under two days.
- **"A later save rewrote 'created'"** and **"the Word-saved v1 and v2"** asserted mechanisms the files do
  not show. Now "something rewrote 'created' in between" and "the 1980 pattern of v1 and v2".
- **Theory said "two" commits had a later committer date** (four do), and that `modified` sat "hours" before
  the commit for v1 and v2 (v2's gap is 7 minutes). A "usually leaves it alone" about zip editors had no source.
- **Unsourced quantifiers** "many organisations", "many PDFs", "often set once, when the software is
  installed" became statements of what can happen.
- **Case draft called `cic22` a "machine account"/"shared account"**, credited the floppy link to the Foreign
  Affairs Committee (Smith says "hearings"), and had Smith "ending" on the PDF claim (it is near the end).
- **Workbench named −0800 as "US Pacific winter time"**: one zone with that offset, not a location.
- **PowerShell `"{0}" -f x / 10`** parses as (string / 10). Parenthesised. (Windows variant still not run.)
- Gate: OOXML namespace URIs (host has no DNS record) were probed as links; that one host is now skipped,
  purl.org and w3.org namespace URIs are still probed. A `revision log` anchor was dropped: the term lives only
  in the case study, which the stale-anchor check does not read.

## Batch 12 — S2.5 Image and video verification: is this picture what the post says it is?

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 238 | S2.5 | dHash: shrink to 9×8, grey, compare each pixel with its right neighbour, 64 bits; described by Neal Krawetz, "Kind of Like That", 21 January 2013, crediting the "difference hash" idea to David Oftedal | `SOURCED` | hackerfactor.com/blog archives/529 (raw HTML, 2026-09-28) | stable |
| 239 | S2.5 | "A value of 0 indicates the same hash and likely a similar picture. A value greater than 10 is likely a different image, and a value between 1 and 10 is potentially a variation." | `SOURCED` | row 238 page | stable |
| 240 | S2.5 | Bit = 1 where a pixel is darker than its right neighbour, as Krawetz's own convention ("a \"1\" to indicate that P[x] < P[x+1]") | `SOURCED` | row 238 page; lab `pic.py` uses the same | stable |
| 241 | S2.5 | Distances from the original (sips, build Mac): thumbnail 2, night control 31, viral (mirrored, 95%) 38, viral mirrored back 5 | `EXECUTED` | lab step 6, bash and zsh identical, three runs | 2027-03 (Commons may re-make thumbnails) |
| 242 | S2.5, Drill 2 | Centre crops of the thumbnail: 98% → 3, 95% → 6, 90% → 11, 85% → 14, 80% → 15, 70% → 25, 60% → 29, 50% → 38 | `EXECUTED` | Drill 2, bash and zsh identical | 2027-03 |
| 243 | S2.5 | The original carries Exif: Apple iPhone 8, DateTimeOriginal 2018:08:26 09:42:06, no OffsetTimeOriginal, a GPS block. Commons' 960 px thumbnail has no APP segments at all | `EXECUTED` | lab step 5 (`pic.py` reads the bytes) | 2027-03 |
| 244 | S2.5, Drill 1 | `sips -f horizontal` on the original keeps make, model, time and GPSImgDirection 75.2 on a mirror image (new SHA-256; dHash distance 38) | `EXECUTED` | Drill 1, bash and zsh identical | stable |
| 245 | S2.5 | MediaWiki imageinfo `sha1`: "Adds SHA-1 hash for the file." | `SOURCED` | mediawiki.org/wiki/API:Imageinfo (curl) | stable |
| 246 | S2.5 | item002 SHA-1 c6bac702d583… and item006 SHA-1 febdab7ba0a5… equal the API's values; API `url` fields end in `?utm_…` tracking tags | `EXECUTED` | lab step 3 | stable |
| 247 | S2.5 | Commons upload timestamps: LONDON_BRIDGE.jpg 2018-10-06T06:34:05Z; Tower_Bridge_MVI_1768.webm 2017-01-07T19:13:00Z; 2,914 calendar days from the first to 2026-09-28 | `EXECUTED` | lab steps 7–8 | stable |
| 248 | S2.5 | Matroska DateUTC: "The date and time that the Segment was created by the muxing application or library" (optional); MuxingApp and WritingApp minOccurs 1 | `SOURCED` | rfc-editor.org RFC 9559 §5.1.2.11–14 (txt) | stable |
| 249 | S2.5 | EBML Date: signed nanoseconds from 2001-01-01T00:00:00 UTC; a zero-length Date means that instant | `SOURCED` | RFC 8794 §7.6 (txt) | stable |
| 250 | S2.5 | QuickTime mvhd creation time: "seconds since midnight, January 1, 1904, preferably using coordinated universal time (UTC)" | `SOURCED` | developer.apple.com QTFF movie_header_atom/creation_time (docs JSON; HTML needs JavaScript) | stable |
| 251 | S2.5 | `©swr`: "Name and version number of the software (or hardware) that generated this movie" | `SOURCED` | developer.apple.com QTFF user_data_atoms (docs JSON) | stable |
| 252 | S2.5 | `Lavf` + version is FFmpeg libavformat's ident string (`LIBAVFORMAT_IDENT "Lavf" AV_STRINGIFY(LIBAVFORMAT_VERSION)`) | `SOURCED` | FFmpeg libavformat/version.h, master via raw.githubusercontent.com | stable |
| 253 | S2.5 | item006 (WebM): MuxingApp = WritingApp = Lavf54.20.4, no DateUTC. item007 (.mov conversion): `©swr` Lavf59.27.100, mvhd version 0, creation time 0 | `EXECUTED` | lab step 8 (EBML walker, box walker; no byte search) | stable |
| 254 | S2.5 | `qlmanage -t` gives the same frame bytes on two grabs of item007 | `EXECUTED` | lab step 8 | stable (per macOS version) |
| 255 | S2.5 | C2PA FAQ: "While C2PA Manifests are typically embedded in the asset, they can be separated." and "The core C2PA Content Credentials specification does not support attribution of content to individuals or organizations" | `SOURCED` | c2pa.org/faqs (raw HTML) | 2027-03 |
| 256 | S2.5 | No C2PA specification version is named: spec.c2pa.org does not route from the build network, and a search summary is a lead, not a source | `CONVENTION` | curl 000, WebFetch failed | — |
| 257 | S2.5 | `sips -g all` prints make, model, software and a creation time, but no GPS | `EXECUTED` | on item002 | stable |
| 258 | S2.5, Linux | Pillow 11.3.0 variant (LANCZOS to 9×8, "L" grey): thumbnail 0, control 26, viral 38, mirrored back 5; same verdicts as sips | `EXECUTED` | the linux.txt code run on macOS | stable |
| 259 | S2.5 case | BBC social media editor, 29 May 2012: picture up "for about 90 minutes", "first spotted as it circulated on Twitter", the "veracity … disclaimer … should have been better … we apologise" passage; photographer "works for Getty Images"; "almost a decade earlier" | `SOURCED` | bbc.co.uk/blogs/theeditors/2012/05/houla_massacre_picture_mistake.html (raw HTML) | stable |
| 260 | S2.5 case | BBC caption "This image – which cannot be independently verified – is believed to show the bodies of children in Houla awaiting burial."; credit "Photo From Activist"; Di Lauro to the Telegraph: "I almost felt off from my chair" | `SOURCED` | poynter.org, Craig Silverman, 28 May 2012 (raw HTML). The Telegraph returns 402 to scripts: quoted via Poynter, and said so | stable |
| 261 | S2.5 case | Di Lauro's blog, 9 June 2012: text says taken "on March 27, 2003"; caption on the same page says "Al Musayyib, Iraq – May 27, 2003"; bodies moved from a mass grave to a school to be identified; story "Iraq, the Aftermath of Saddam" | `SOURCED` | marcodilauro.com blog post (raw HTML). Not resolved: no third source read | stable |
| 262 | S2.5 case | BBC official by role only; photographer named as credited author of the picture and statements | `CONVENTION` | as S2.4 | — |
| 263 | S2.5 | Windows variant not run (no pwsh on the build Mac); it says so in its header and skips the frame step | `CONVENTION` | as S1.7–S2.4 | — |

Defects caught in the S2.5 build pass (none shipped):

- **zsh broke the lab twice.** A jq path written with a variable followed directly by `[0]` is an array
  subscript in zsh, and `set --` on an unquoted variable does not split there. Both ran in bash, and both
  stopped in zsh. Guards A107 and A108.
- **An EBML Date of zero length would have crashed** the WebM reader (RFC 8794 allows it). It now reads it as 2001-01-01.
- **The clock grader said 2,913 days** where the lab said 2,914: a timedelta floors across the time of day.
  Both now count calendar dates.
- **The first finding said the post's picture "is a mirrored, trimmed copy".** That is known only because
  the lab made the copy. The finding now says "within 5 bits … if it is that photo", and to confirm by eye.
- **Case draft over-reached.** It had "his agency's archive", "some outlets argued" (pages not read),
  "readers saw the picture more than the words", "an earlier copy existed to be found" (not in any source
  read), "credited to 'an activist'" (the credit read "Photo From Activist"), and "both from the
  photographer's own pages" (one page).
- **Unsourced quantifiers** "Most false pictures", "Most pictures … have none", "Many apps remove location"
  and "almost any video a platform touches" became statements of what can happen.
- **PowerShell:** a uint64 XOR cast to int64 overflows; int64 keys never match int32 lookups in a hashtable;
  a one-element list returned from a function unrolls; ConvertFrom-Json turns timestamps into local dates.
  All four were fixed on reading. The variant is still not run.
- **The API's thumbnail size is not the file's.** With `iiurlwidth=640`, Commons returned
  `thumbwidth: 640` and a URL that served a 960-pixel file. The lab asks for 960 and measures what arrives.
- **Case chosen against:** the 2015 error-level-analysis dispute over MH17 satellite images. The only
  pages that could be read were one party's advocacy, too contested to pin quotes to.

## Batch 13 — S2.6 Usernames and accounts: whose account is this, and who says so?

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 264 | S2.6 | GitHub: "After changing your username, your old username becomes available for anyone else to claim." | `SOURCED` | docs.github.com … /changing-your-github-username (curl, 2026-09-28) | 2027-03 |
| 265 | S2.6 | WhatsMyName rule file pinned at commit 062bcfe48df7… (2026-09-16, "Add MAX public handle checks (#1073)"): 717 rules, SHA-256 507d2f8aa5b1…, licence CC BY-SA 4.0 | `EXECUTED` | lab step 3; `gh api repos/WebBreacher/WhatsMyName/commits/062bcfe…`; file's own `license` field | stable (pinned) |
| 266 | S2.6 | WMN README: "started as a personal fix for a real frustration: existing username checkers were full of false positives"; CONTRIBUTING defines e_code / e_string / m_code / m_string as quoted in the theory table and asks for strings that are "truly unique" | `SOURCED` | README.md and CONTRIBUTING.md at the pinned commit (raw) | stable (pinned) |
| 267 | S2.6 | Sherlock ("Hunt down social media accounts by username across social networks") and Maigret ("Collect a dossier on a person by username …") are username checkers | `SOURCED` | `gh api repos/sherlock-project/sherlock`, `repos/soxoj/maigret` descriptions | stable |
| 268 | S2.6 | Rules as pinned: GitHub (User) 200+`"id":` / 404+`"status": "404"`; GitLab 200+`"id":` / 200+`[]`; Codeberg 200+`"id":` / 404+`user redirect does not exist`; Mastodon API 200+`display_name` / 404+`"accounts":[]` | `EXECUTED` | lab step 3 | stable (pinned) |
| 269 | S2.6 | Codeberg: forgejo 200 FOUND; control 404 MISSING. GitLab: gitlab 200 FOUND; control 200 `[]` MISSING | `EXECUTED` | lab step 4, bash and zsh identical | 2027-03 |
| 270 | S2.6 | GitHub's 404 body comes in two layouts, spaced (`"status": "404"`) and compact (`"status":"404"`), alternating across repeated requests for the same URL with the same User-Agent (15 requests, 5 UAs); the rule says UNKNOWN for the compact one | `EXECUTED` | build probes 2026-09-28; lab step 4 gave UNKNOWN in both shells | 2027-03 (layout may settle) |
| 271 | S2.6 | mastodon.social `/api/v2/search?q=<control>` returns HTTP 200 with a different account (not an exact match); a query with no hits returns 200 `{"accounts":[],…}`. The endpoint never returned 404, so the rule's MISSING branch cannot fire | `EXECUTED` | lab step 4 (reply hashed and deleted); build probe with a nonsense query | 2027-03 |
| 272 | S2.6 | GitHub `eff` → login EFF, type User, id 955524, created 2011-08-03, no eff.org link; `EFForg` → Organization, id 2120271, created 2012-08-09, blog https://www.eff.org/ | `EXECUTED` | lab step 5 | stable |
| 273 | S2.6 | eff.org home page: one `rel="me"` link, to https://mastodon.social/@eff; no link to github.com/EFForg (the GitHub org page links to eff.org) | `EXECUTED` | lab step 6; build fetch of github.com/EFForg | 2027-03 (site redesigns) |
| 274 | S2.6 | mastodon.social @eff: id 41055, created 2017-04-04, Website field → https://www.eff.org, verified_at 2023-11-02T21:28:54.864+00:00 | `EXECUTED` | lab step 7 | 2027-03 (re-verification moves verified_at) |
| 275 | S2.6 | Mastodon docs: "Mastodon checks if that link resolves to a web page that links back to your Mastodon profile with a special rel=me attribute. If so, you get a verification checkmark" | `SOURCED` | docs.joinmastodon.org/user/profile/ (curl); verified_at field listed at /entities/Account/ | stable |
| 276 | S2.6 | AT Protocol handle spec: `_atproto` TXT record with prefix `did=`; HTTPS `/.well-known/atproto-did`; "The link between handle and DID must be confirmed bidirectionally, otherwise anybody could create handle aliases for third-party accounts." | `SOURCED` | atproto.com/specs/handle (curl) | stable |
| 277 | S2.6 | `_atproto.eff.org` TXT = did=did:plc:lr36xv2l64jwtnyoaqem6z2z; DID document alsoKnownAs `at://eff.org` | `EXECUTED` | lab step 8 | stable |
| 278 | S2.6 | PLC audit log for that DID: 3 operations — 2023-04-25 and 2023-11-10 at://eff.bsky.social, 2024-02-08 at://eff.org | `EXECUTED` | lab step 8 | stable (closed history) |
| 279 | S2.6 | did:plc spec: audit-log timestamps "could be cross-verified against network traffic or other information to de-anonymize account holders" | `SOURCED` | web.plc.directory/spec/v0.1/did-plc (curl; page says v0.3.0, December 2025) | stable |
| 280 | S2.6 | `api.github.com/user/583231` → login octocat | `EXECUTED` | lab step 9 | stable |
| 281 | S2.6 | GitHub unauthenticated REST limit: `x-ratelimit-limit: 60` per hour; exhausted during the build, which turned Drill 3's EFForg line UNKNOWN on the zsh run | `EXECUTED` | response headers 2026-09-28; wb3 zsh run | 2027-03 |
| 282 | S2.6, Drill 1 | Saved compact reply: text rule UNKNOWN, parsed MISSING; spaced layout: both MISSING; octocat parsed FOUND; a rate-limit reply parsed UNKNOWN | `EXECUTED` | Drill 1, bash and zsh identical | stable |
| 283 | S2.6, Drill 2 | octocat: GitHub FOUND, GitLab MISSING, Codeberg MISSING; all three controls MISSING | `EXECUTED` | Drill 2, bash and zsh identical | 2027-03 (anyone may register octocat) |
| 284 | S2.6, Drill 3 | @eff↔www.eff.org TWO-WAY; @eff↔github.com/EFForg NONE; EFForg↔www.eff.org ONE-WAY (account's claim only); Bluesky eff.org TWO-WAY; example.com NONE (no `_atproto` TXT, well-known 404) | `EXECUTED` | Drill 3 (see row 281 for the UNKNOWN run) | 2027-03 |
| 285 | S2.6 case | NYT, Nathaniel Popper, 25 Dec 2015, web title "The Unsung Tax Agent Who Put a Face on the Silk Road": Alford "a young special agent with the Internal Revenue Service assigned to work with the D.E.A."; Google advanced search by date range; "the last weekend of May 2013"; post "just before Silk Road had gone online, in early 2011"; "suggested that altoid might have inside knowledge"; email post "apparently deleted — but … preserved in the response of another user"; "the first of many striking parallels"; "wasn't able to get the surveillance and the subpoenas he wanted"; "more than three months to gather enough evidence …"; home "a few hundred feet" from the cafe; Frosty line (Times paraphrase from "two people briefed"); apprehended "at a public library in San Francisco" | `SOURCED` | web.archive.org/web/20151225215838id_/…nytimes.com/2015/12/27/business/dealbook/the-unsung-tax-agent-who-put-a-face-on-the-silk-road.html (raw HTML; live page 403s scripts). Wikipedia cites the print title "The Tax Sleuth Who Took Down a Drug Lord" | stable |
| 286 | S2.6 case | Bitcointalk "A Heroin Store" thread: altoid, 29 January 2011, "Has anyone seen Silk Road yet? It's kind of like an anonymous amazon.com." | `SOURCED` | bitcointalk.org/index.php?topic=175.msg42670 (raw HTML, 2026-09-28) | stable |
| 287 | S2.6 case | "IT pro needed for venture backed bitcoin startup", altoid (OP), 11 October 2011: the email address is in altoid's own opening post, live (2026-09-28) and in the Wayback capture 20111127165405; no "Quote from: altoid" on the live page. Conflicts with the NYT's "deleted … preserved in another user's response" — taught as a discrepancy, not resolved | `EXECUTED` | bitcointalk.org/index.php?topic=47811.0 live + `id_` capture (CDX lists 20111127165405 and 20140406212357) | stable |
| 288 | S2.6 case | Convicted on all counts (NYT headline dated FEB. 4, 2015); sentenced to life (NYT headline dated MAY 29, 2015); arrest in October 2013 (NYT says Oct. 2; not narrowed further in the course) | `SOURCED` | row 285 page (related-coverage headlines and body) | stable |
| 289 | S2.6 case | 21 January 2025: Trump "signed a full and unconditional pardon" (Truth Social post quoted by CNBC) | `SOURCED` | cnbc.com/2025/01/21/trump-pardons-silk-road-ross-ulbricht-.html (raw HTML) | stable |
| 290 | S2.6 | Ethics conventions: the email address in the case is not reproduced; lab replies that name people (GitHub eff, the control search) are hashed into the log and deleted, and only ownership fields are printed; drills practise on the student's own usernames | `CONVENTION` | module text and lab | — |
| 291 | S2.6 | Linux variant (sha256sum for shasum) executed on macOS via /sbin/sha256sum; Windows variant not run (no pwsh on the build Mac) and says so | `EXECUTED` / `CONVENTION` | lab_linux.sh run | — |

Defects caught in the S2.6 build pass (none shipped):

- **A shared rule file had two broken rules out of the four tested.** The Mastodon API rule reads a fuzzy
  search as an existence check and reported a name nobody holds as FOUND; the GitHub rule matches one of two
  reply layouts. Found only because every rule was run against a control name. Both are now the lesson.
- **Drill 3's first Bluesky check read `dig` output without its exit status**, so a resolver failure would
  have printed NONE. It now answers UNKNOWN. Guard A110.
- **Case draft put the Times's paraphrase in Tarbell's mouth** ("Tarbell explained that 'Frosty was …'").
  The Times reports it from two people briefed on the call. Guard A109.
- **Case draft used the headline Wikipedia cites** (the print title). The archived page's own title is
  "The Unsung Tax Agent Who Put a Face on the Silk Road".
- **Case draft said Alford searched "for the earliest mentions of Silk Road"** and that the post came
  "before the site was widely known": neither is in the article. Replaced with its words.
- **Case draft quoted "anonymous Amazon.com"** from the Times; the forum post reads "amazon.com".
- **Theory draft said EFForg "has held EFF's repositories since 2012"** — not checked. Now: an Organization
  account created in 2012 whose profile names the foundation, so "probably".
- **Lab header said "nineteen requests"**: it makes sixteen and one DNS lookup.
- **GitHub's hourly limit ran out during the build.** The drill's UNKNOWN path caught it; the lesson went
  into Drill 3's text.
- **The lab's own DNS step had the Drill 3 defect.** `DID=$(dig … | sed …)` dropped dig's exit status, and a
  transient resolver failure during the Linux-variant run stopped the lab with "no _atproto TXT record".
  The lab now keeps the exit status, logs it, and says UNKNOWN for a failed lookup. A110 now also flags
  a shell variable assigned from `$(dig … |`.
- **A no-answer request (HTTP 000) made `shasum` fail on a missing file** before the STOP line. `collect`
  now logs NONE as the hash and tells you to run the lab again. Two such drops happened in one build run.
- **The URL gate probed Drill 2's `…/users/{}` template as a real URL** (Codeberg 404). The drill now uses
  `<name>` placeholders, which the gate already skips.

## Batch 14 — S2.7 Capstone 2: a multi-source pivot report, and how strong each link is

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 292 | S2.7 | eff.org A 173.239.79.200; www.eff.org CNAME eff.map.fastly.net → 151.101.{0,64,128,192}.201; certbot.org and atlasofsurveillance.org (www CNAME apex) on the same four addresses | `EXECUTED` | lab item001, three runs 2026-09-28 | 2027-03 |
| 293 | S2.7 | 173.239.79.200 in 173.239.64.0/20, AS32354 ("UNWIRED - Unwired"); 151.101.0.201 in AS54113 ("FASTLY - Fastly, Inc."); example.com's 104.20.23.154 in 104.20.16.0/20, AS13335 ("CLOUDFLARENET - Cloudflare, Inc.") | `EXECUTED` | lab items 010–011; RIPEstat network-info + as-overview (curl 2026-09-28) | 2027-03 |
| 294 | S2.7 | Fastly is a content delivery network | `SOURCED` | fastly.com/products/cdn page title "Fastly CDN \| Content Delivery Network" (curl 2026-09-28) | stable |
| 295 | S2.7 | Public Interest Registry operates .org | `SOURCED` | iana.org/domains/root/db/org.html (curl 2026-09-28) | stable |
| 296 | S2.7 | PIR RDAP: eff.org registered 1990-10-10, certbot.org 2016-03-16, atlasofsurveillance.org 2020-04-15; all three list ns1/ns2/ns4.eff.org; each record's only entity is the registrar (handle 81), no registrant | `EXECUTED` | lab items 004–006; `jq '[.entities[] \| {roles, handle}]'` | 2027-03 |
| 297 | S2.7 | IANA registrar ID 81 = "Gandi SAS", Accredited | `SOURCED` | iana.org registrar-ids-1.csv (curl 2026-09-28) | 2027-09 |
| 298 | S2.7 | Asked with +norec, ns1.eff.org answers eff.org, certbot.org and atlasofsurveillance.org SOA with aa, and example.com with REFUSED (no aa); ns2 and ns4 behave the same (Drill 2) | `EXECUTED` | lab item003; Drill 2 run, bash and zsh | 2027-03 |
| 299 | S2.7 | RFC 1035 §4.1.1: AA "specifies that the responding name server is an authority for the domain name in question section"; RCODE 5 "Refused - The name server refuses to perform the specified operation for policy reasons." | `SOURCED` | rfc-editor.org/rfc/rfc1035.txt (curl 2026-09-28) | stable |
| 300 | S2.7 | RFC 9499 quotes RFC 1912 §2.8's lame-delegation definition ("…a nameserver is delegated responsibility for providing nameservice for a zone (via NS records) but is not performing nameservice for that zone…"), notes the term has drifted to other flaws, and says it "should be considered historic" | `SOURCED` | rfc-editor.org/rfc/rfc9499.txt (curl 2026-09-28) | stable |
| 301 | S2.7 | mnemonic pDNS, eff.org A: 69.50.232.52 2012-08-17→2013-11-14, 69.50.232.54 2016-04-30→2018-04-25, 198.100.177.181 2018-05-02→2018-11-27, 173.239.79.196 2018-11-28→2025-06-10, 173.239.79.200 2026-04-16→(open) | `EXECUTED` | lab item007 | closed rows stable; open row moves |
| 302 | S2.7 | mnemonic pDNS on 151.101.0.201: 8 names (certbot.org/.com/.net/.info, atlasofsurveillance.org, onlinecensorship.org, securityeducationcompanion.org, eff.map.fastly.net); same 8 on .128/.192.201; certbot.org last seen 2024-09-24; atlas only 2026-09-03; eff.map.fastly.net until 2024-10-25; onlinecensorship.org 2023-05-25→2024-03-20 | `EXECUTED` | lab item008; probes of the other three addresses | open rows move |
| 303 | S2.7 | Control: example.com's 104.20.23.154 seen with 29 names under 14 registered domains, 2 of them example.com's | `EXECUTED` | lab item009 (build run) | moves |
| 304 | S2.7 | Wayback CDX first captures: certbot.org 20170520113943 HTTP 301; atlasofsurveillance.org 20200713191852 HTTP 200 | `EXECUTED` | lab items 012–013 | stable (history) |
| 305 | S2.7 | atlasofsurveillance.org home page: "Atlas of Surveillance is a project of the Electronic Frontier Foundation" | `EXECUTED` | lab item014 | 2027-03 |
| 306 | S2.7 | certbot.org answers HTTP 301 → https://certbot.eff.org/ | `EXECUTED` | curl -w redirect_url 2026-09-28 (probe; not a lab item — the theory cites the archived 301s) | 2027-03 |
| 307 | S2.7 | dig 9.10.6: exits 9 when no server replies (192.0.2.1); one @server applies to every query on the line; with +comments each reply's HEADER and flags lines come before its QUESTION line, and the EDNS line also contains "flags:" | `EXECUTED` | runs on the build Mac; the lab's aa() is written for this layout | stable |
| 308 | S2.7 | GNU date: `-r file` = `--reference=file` ("Display the date and time of the last modification of file"); BSD/macOS date: `-r seconds`. The lab uses jq `todate` instead | `SOURCED` | gnu.org coreutils manual, Options for date; `man date` on macOS | stable |
| 309 | S2.7 | PHIA "highly likely" ≈80–≈90 %; likelihood and confidence in separate sentences | `SOURCED` | follows rows 108–109 and 118 (S1.7) | per rows 108–109 |
| 310 | S2.7 | WSL: `wsl --install` in an administrator PowerShell, then restart; installs Ubuntu by default; needs Windows 10 version 2004 (Build 19041) or later, or Windows 11 | `SOURCED` | learn.microsoft.com/en-us/windows/wsl/install (ms.date 2025-06-09, fetched 2026-09-28) | 2027-03 |
| 311 | S2.7 | Case: DHS/DOJ release 15 Feb 2011 announced "the execution of seizure warrants against 10 domain names of websites engaged in the advertisement and distribution of child pornography" under "Operation Protect Our Children", "a new joint operation"; it names no domains and does not mention mooo.com | `SOURCED` | dhs.gov/news/2011/02/15/joint-dhs-doj-operation-protect-our-children-seizes-website-domains-involved (raw HTML, curl 2026-09-28; 0 hits for "mooo") | stable |
| 312 | S2.7 | Case: TorrentFreak, 16 Feb 2011 (Ernesto Van der Sar): "the most popular shared domain at afraid.org"; "a massive 84,000 subdomains were wrongfully seized"; "contacted the domain registries to point the domains in question to a server that hosts the warning message"; "somewhere in this process a mistake was made"; FreeDNS: "Freedns.afraid.org has never allowed this type of abuse of its DNS service."; "on Sunday the domain seizure was reverted"; "it took another 3 days before the images disappeared completely"; "personal sites and sites of small businesses" | `SOURCED` | torrentfreak.com/u-s-government-shuts-down-84000-websites-by-mistake-110216/ (raw HTML) | stable |
| 313 | S2.7 | Case: The Register, 18 Feb 2011 (Dan Goodin): "as many as 84,000"; "suspended at the registrar level"; "By Sunday evening, mooo.com was restored"; "silenced for 72 hours" | `SOURCED` | theregister.com/security/2011/02/18/unprecedented-domain-seizure-shutters-84000-sites/1038665 (raw HTML) | stable |
| 314 | S2.7 | Case: NBC News credits TorrentFreak ("the TorrentFreak blog reported") and dates it "Late on Friday (Feb. 11)"; Techdirt, 16 Feb 2011: "point it at whatever machine is actually hosting your content" | `SOURCED` | nbcnews.com/id/wbna41649634; techdirt.com/2011/02/16/did-homeland-security-seize-then-unseize-dynamic-dns-domain/ (raw HTML) | stable |
| 315 | S2.7 | ICE's later "inadvertently seized" statement is deliberately NOT taught: its source (Dark Reading) returns 403 to scripts and WebFetch, has no Wayback capture, and only Wikipedia repeats it | `CONVENTION` | the case says it is left out and why | re-try if Dark Reading becomes readable |
| 316 | S2.7 | example.org lists Cloudflare nameservers (Drill 2's NONE case); example.com also uses Cloudflare nameservers (S1.7) | `EXECUTED` | Drill 2 run; `dig NS example.com` 2026-09-28 | 2027-03 |
| 317 | S2.7 | Ethics conventions: organisations' domains only; no person, email address or account; officials by role only; journalists named only as authors of cited pieces; unfollowed leads listed, not queried | `CONVENTION` | module text and scope.txt | — |
| 318 | S2.7 | Lab (3 DNS lookups + 11 requests) and all three drills run in bash and zsh with identical output; Linux variant (sha256sum) run on macOS via /sbin/sha256sum, identical; Windows = WSL route, not run natively (no pwsh, aa-flag reporting of Windows DNS tools unverified) and says so | `EXECUTED` / `CONVENTION` | out_bash / out_zsh / out_linux diffs | — |

Defects caught in the S2.7 build pass (none shipped):

- **The first draft tagged F4 (the registry's nameserver list) STRONG, and `check_report.sh` passed it.** Anyone
  can list any nameserver; only F5 shows the server's side. Now F4 is ONE-WAY, the story is the module's "what
  the check does not prove" lesson, and Drill 1 is a tag auditor that catches it. No gate guard can: the tag's
  correctness is a reading of the evidence.
- **The authoritative-answer parser read the wrong reply.** `dig +comments` prints each reply's header before
  its question line, so an awk that started at the question took the *next* reply's status; the EDNS line
  also contains "flags:". Now it remembers the last header and prints at the question.
- **`case` inside `$( … )` broke bash** (an unbalanced `)`); the loop was also `for n in $CO`, which zsh does
  not split. Replaced with `tr | grep -vxE`. A108 was not extended to `for x in $var`: that form is correct
  inside the `#!/bin/bash` check_report.sh heredocs (S1.7, S2.7), so a regex would flag good code. The
  bash-and-zsh double run is the check.
- **`date -u -r SECONDS` is BSD-only**; on GNU `-r` names a reference file. The lab now uses jq `todate`, so
  the Linux variant differs only by sha256sum.
- **Drill 2's first rule required the candidate's nameservers to equal eff.org's set.** The rule is "every
  listed nameserver sits inside the origin's domain"; fixed.
- **Case draft attributed NBC's story "via TechNewsDaily"** — not on the page. NBC credits TorrentFreak.
- **Case draft said the 84,000 figures "appear to trace back to FreeDNS"** — neither article says where the
  number came from. Replaced with exactly that.
- **ICE's "inadvertently seized" quote** could not be pinned to a readable page; left out, and the case says so.
- **Theory draft called the control's 14 registered domains "unrelated"** (and a challenge said "nearly all
  unrelated"); only the count was checked. Now counts only.
- **Workbench draft said "millions of other domains" use Cloudflare's nameservers** — not checked. Now:
  example.com does (S1.7), along with many unrelated domains.
- **Theory draft said a domain "has been registered continuously since" its RDAP registration date** — the
  record does not show continuity of holder. Now: when the registry says this registration began.
- **Level 2's roadmap promised "a second case folder that grows one module at a time"**; every L2 module
  uses its own `~/scouts-case/s2_N` folder. The line now says so.
- **This ledger's header was stale since Batch 11** (course-file line said S2.1–S2.3; Last pass began at
  Batch 11). Updated with Batches 12–14.

## Batch 15 — S3.1 Source grading and competing hypotheses (opens Level 3)

Level 3 list agreed 2026-09-28: the user delegated the choice ("recommend … global standard"); benchmarked
against the Berkeley Protocol's Chapter VI and SANS SEC587's published syllabus. Sock puppets, dark-web
markets, password cracking and facial recognition were left out as incompatible with the course's passive,
lawful-first stance. Planned rows carry `—`, not numbers.

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 319 | S3.1 | JDP 2-00 (4th Edition) is dated August 2023, UK MOD; para 3.40 calls the NATO Intelligence Grading System "sometimes referred to as the 'Admiralty Code'"; Table 3.1 gives A–F reliability and 1–6 credibility with the labels the module prints | `SOURCED` | assets.publishing.service.gov.uk JDP_2_00_Ed_4_web.pdf, pdftotext (2026-09-28), pp. 59–60 | 2028-09 |
| 320 | S3.1 | JDP 2-00 para 3.40: B5 / E1 examples; "The two ratings do not need to 'match'"; F6 "does not render the information useless"; gradings "should be reviewed as further intelligence is acquired" | `SOURCED` | same PDF, para 3.40 and 3.40a | 2028-09 |
| 321 | S3.1 | JDP 2-00 para 3.39a (reliability of organisational sources "largely depend[s] on the reporting history…"), 3.39b (credibility "usually best assessed by corroborating…"; internal check for content "factually incorrect or logically implausible"; circular reporting), 3.39c ("Reliability and credibility must be evaluated separately…") | `SOURCED` | same PDF, para 3.39 | 2028-09 |
| 322 | S3.1 | JDP 2-00 footnote 53 (to para 3.51) defines circular reporting in the words quoted | `SOURCED` | same PDF, para 3.51 fn 53 | 2028-09 |
| 323 | S3.1 | JDP 2-00 para 3.33: SATs "compel users to actively think…"; names anchoring, confirmation bias, groupthink | `SOURCED` | same PDF, para 3.33a–b | 2028-09 |
| 324 | S3.1 | NATO's JADL copy of AJP-2.1 was not used: 403 to curl. The grading table is cited from JDP 2-00, which reproduces it | `CONVENTION` | jadl.act.nato.int … AJP21.pdf → HTTP 403 (2026-09-28) | — |
| 325 | S3.1 | College of Policing APP "Intelligence report": first published 24 August 2015, updated 26 January 2022; three source gradings (reliable — "competence and veracity" tests; untested; not reliable); A–E information grades with the quoted wording; handling codes P and C; corroboration must be "independent and not from the same original source"; refers to intelligence "graded under the 5x5x5 system" | `SOURCED` | live page 403s to curl and WebFetch; read via Wayback `20240707145422id_` (2026-09-28) | 2027-09 |
| 326 | S3.1 | The APP page does not number the three source grades; the module names them and does not claim 1/2/3 | `CONVENTION` | same capture; secondary sources (Substack, Blockint) number them, not relied on | 2027-09 |
| 327 | S3.1 | Old 5x5x5 system graded the source with letters, "A – ALWAYS RELIABLE" | `SOURCED` | library.college.police.uk/docs/APPref/how-to-complete-5x5x5-form.pdf, pdftotext (2026-09-28) | stable |
| 328 | S3.1 | Heuer, *Psychology of Intelligence Analysis*, CIA Center for the Study of Intelligence, 1999; Chapter 8 ACH; the eight steps as paraphrased; high-temperature analogy; "fewest minuses" (quoted with the original's "hypotheses … is"); "You, not the matrix, must make the decision. The matrix serves only as an aid to thinking and analysis" | `SOURCED` | archive.org PsychologyOfIntelligenceAnalysis/Psychology_of_Intelligence.pdf, pdftotext (2026-09-28), pp. 95–104 | stable |
| 329 | S3.1 | Berkeley Protocol Chapter VI sections A–F = online inquiries, preliminary assessment, collection, preservation, verification, investigative analysis; paras 176–182 (verification; source analysis: provenance, credibility, independence and impartiality, specificity, attenuation) with the quoted phrases; bias sentence in Principles | `SOURCED` | ohchr.org …/OHCHR_BerkeleyProtocol.pdf, pdftotext -raw (2026-09-28) | stable |
| 330 | S3.1 | Theory draft called the six parts a "cycle"; the Protocol lists them as sections and says "investigation cycle" only in passing — now "sets out the investigation process in six parts" | `FIXED` | same PDF | — |
| 331 | S3.1 | RIPEstat routing-history for 129.134.30.0/23, 3–6 Oct 2021: only origin AS32934; 129.134.30.0/24 and 129.134.31.0/24 seen by 341/342 peers before and 0 in the 2021-10-04 16:00–23:59 bin; the /23 at 31; covering 129.134.0.0/17 at 341 throughout | `EXECUTED` | lab item001, three runs 2026-09-28 (zsh, bash, rendered copy) | historical data; stable |
| 332 | S3.1 | RIPEstat bgp-updates returns 0 updates for these prefixes in October 2021 — the lab uses routing-history (8-hour bins) instead | `EXECUTED` | curl stat.ripe.net bgp-updates (2026-09-28) | 2027-09 |
| 333 | S3.1 | RIPEstat replies carry `time`, `server_id`, `process_time`, so item001's hash changes every run | `EXECUTED` | jq on item001 | stable |
| 334 | S3.1 | mnemonic pDNS: a.ns.facebook.com A 129.134.30.12 first seen 2020-03-05, last seen 2026-09-13 (open row); 69.171.239.12 2017-01-29 → 2020-03-06 | `EXECUTED` | lab item002 | closed row stable; open row moves |
| 335 | S3.1 | Cloudflare post (datePublished 2021-10-04T21:08:52Z): "around 15:40 UTC … a peak of routing changes"; 1.1.1.1 unavailable ~15:50 → 21:20 UTC; renewed BGP ~21:00, peak 21:17; "other Facebook IP addresses remained routed"; lines at 15:51 and 15:58 exist only in today's version | `EXECUTED` | lab items 003 (Wayback 20211004220101) and 004 (live) | item004 live: 2027-03 |
| 336 | S3.1 | Cloudflare's post said "as of 22:28 UTC" in captures from 21:39:41 to 22:05:40 UTC; "21:28" from 22:18:50; no "as of" sentence at 21:17:40 and 21:29:21 | `EXECUTED` | Drill 1 binary search over 221 CDX captures, run as written 2026-09-28 | stable |
| 337 | S3.1 | Facebook engineering post (2021-10-05, Wayback 20211005173240): command "unintentionally took down all the connections in our backbone network"; DNS servers "withdraw those BGP advertisements"; "not by malicious activity" | `EXECUTED` | lab item005 | stable |
| 338 | S3.1 | Kentik (Wayback 20211004220908): traffic "virtually disappeared at 15:39 UTC", from NetFlow data | `EXECUTED` | lab item006 | stable |
| 339 | S3.1 | Wikipedia "2021 Facebook outage" revision 1319969338 (2025-11-02T00:20:01Z): "Cloudflare reported that at 15:39 UTC…" cites only the Cloudflare post; the cause sentence cites engineering.fb.com | `EXECUTED` | lab item007 | pinned revision; stable |
| 340 | S3.1 | Same revision gives recovery as BGP ~21:50 / DNS 22:05 UTC in one paragraph and BGP before 21:00 / resolvable 21:05 UTC in another; Drill 2 finds neither 22:05 nor 21:05 on the cited pages (21:50 has no "UTC" after it, so the drill does not test it); 22:45 not on the cited BBC capture, which states no time zone | `EXECUTED` | Drill 2 run as written; BBC capture 20211004225712 grepped for BST/GMT/UTC/ET (none) | pinned; stable |
| 341 | S3.1 | Grade letters are based on this course's own history with each source (B for RIPEstat and mnemonic, F for first use) | `CONVENTION` | STANAG-style F = no track record; JDP 3.39a reporting history | — |
| 342 | S3.1 | The ACH marks (C/I/N) for C1–C7 against H1–H4 are the module's judgement, with each reason in the matrix row and the theory | `CONVENTION` | judgement, shown so it can be challenged | — |
| 343 | S3.1 | WMD Commission "Report to the President, March 31, 2005": every quotation in the case (Curveball fabricator; three other sources "thought to have corroborated"; second source recanted Oct 2003, never recalled; INC source fabrication notice May 2002, reused July 2002; fourth source single report; WINPAC analyst vs DO group chief; "damning comment"; recall requirement; May 2004 recall) | `SOURCED` | georgewbush-whitehouse.archives.gov/wmd/text/report.html (2026-09-28), each quotation string-matched by script | stable |
| 344 | S3.1 | The `sha256sum` variant produces identical facts and checks | `EXECUTED` | run with macOS's own `/sbin/sha256sum`; Docker daemon not running, so not run on a Linux distribution | 2027-03 |
| 345 | S3.1 | Windows route is WSL; no native PowerShell port was run | `CONVENTION` | as S2.7 | — |

Defects caught in the S3.1 build pass (none shipped):

- **`check_report.sh` matched `F[0-9]*`, which matches the bare "F" in "Facebook's"**, and failed a correct
  report ("cites F, which is not a finding"). Now `F[0-9][0-9]*`.
- **The Wikipedia API call asked only for `content`**, so `revid` was missing and the facts step crashed.
  Now `rvprop=ids|timestamp|content`.
- **`datetime.utcfromtimestamp`** (deprecated since 3.12) replaced with `fromtimestamp(…, timezone.utc)`.
- **Drill 2 put a backslash inside an f-string's `{…}`** — a SyntaxError before Python 3.12, and Level 2
  promises 3.9. Rewritten; **guard A111** now catches the shape in every course (0 existing hits).
- **Drill 1's first fetch crashed on gzip-encoded Wayback captures**; `--compressed` added.
- **Drill outputs were drafted before the drills ran.** Two blocks were wrong (Drill 2's last paragraph,
  Drill 3's `tail -2` lines). All three are now pasted from runs of the extracted code blocks.
- **Theory draft said the APP "replaced" 5x5x5**; the page only calls 5x5x5 gradings historic. Reworded.
- **Heuer quotation ended "aid to thinking."** — the sentence continues "and analysis". Restored.
- **Case draft put "was never recalled or corrected" in quotation marks**; the report's words are "Nor, for
  that matter, was the report ever recalled or corrected." Now paraphrased without quotes.
- **Case draft quoted two hypotheses that were the module's own phrasing**; now italic, not quoted.
- **Case draft called the objector "the chief of the group handling the case"**; the report says a group chief
  "responsible for the liaison country's region" in the Directorate of Operations.
- **Quiz asked why a non-diagnostic item is "worth having" in the matrix**, against Heuer's step 4 (delete
  it). Quiz and theory now say what step 4 says.
- **Theory draft called Cloudflare "new to this course"**; S2.7 uses a Cloudflare address as its control.
  Now "not used as a source".
- **The lab had no STOP when a statement the grades rely on vanished from a source**; added.

## Batch 16 — S3.2 Preservation and tool validation: is the capture what the tool says it is?

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 346 | S3.2 | WARC/1.0 = ISO 28500:2009, WARC/1.1 = ISO 28500:2017; IIPC publishes the text of both | `SOURCED` | IIPC warc-specifications (2026-09-28) | 2028-09 |
| 347 | S3.2 | WARC borrows "entity-body" from RFC 2616; RFC 2616: entity-body "is obtained from the message-body by decoding any Transfer-Encoding"; IIPC issue 22 (2015–2017) kept "entity-body" for WARC/1.1 | `SOURCED` | RFC 2616 §7.2; IIPC warc-specifications issue 22 | stable |
| 348 | S3.2 | 2023 public thread, Internet Archive crawler/Wayback maintainer: "Payload-Digest is computed after decoding Transfer-Encoding, but before removing Content-Encoding"; the Archive recalculates the digest at indexing and does not use the WARC's | `SOURCED` | thread read 2026-09-28; quotation string-matched | stable |
| 349 | S3.2 | Forensic Science Regulator statutory Code of Practice v2, England and Wales, in force 2 October 2025; para 24.1.2 validation definition incl. "fit for the specific purpose intended"; binding on forensic units, not on the learner | `SOURCED` | gov.uk Code of Practice PDF (2026-09-28) | 2027-09 |
| 350 | S3.2 | RFC 3161 (2001) Time-Stamp Protocol; query/reply content types `application/timestamp-query` / `-reply` | `SOURCED` | rfc-editor.org RFC 3161 | stable |
| 351 | S3.2 | Berkeley Protocol paras 168–170: keep evidentiary and working copies apart | `SOURCED` | OHCHR Berkeley Protocol PDF (as row 329) | stable |
| 352 | S3.2 | Wget 1.25.0 writes `WARC/1.0` records | `EXECUTED` | lab facts step, `head -1` of each record | 2027-03 |
| 353 | S3.2 | Known-answer test: 1,400-byte body served plain / gzip / chunked / chunked-gzip; expected payload digests XXHBHIW4… (identity) and 2FAV3TQB… (gzip), written before Wget runs; checker validated 4/4 against them first | `EXECUTED` | lab, bash + zsh + sha256sum variant, identical output (2026-09-29) | stable |
| 354 | S3.2 | Wget 1.25.0: block digests 4/4 PASS, payload digests 2/4 PASS; fails on /chunked and /chunked-gzip — the stored payload digest is over the still-chunked bytes, against the WARC/1.0 and 1.1 definition | `EXECUTED` | lab, three runs identical | re-run on each new Wget |
| 355 | S3.2 | Both real captures (IANA example-domains, RFC 2606) were served chunked; stored payload digest DIFFERS on both, block ok; so were all four pages tried during the build | `EXECUTED` | lab items 001–002 | 2027-03 |
| 356 | S3.2 | Drill 1: Internet Archive CDX digests for rfc2606.txt match the checker's recomputed digest; Wget's stored digest appears nowhere in the list | `EXECUTED` | Drill 1 run as written | stable (RFC unchanged since 1999) |
| 357 | S3.2 | Drill 2 measures the Mac clock against the TSA reply's `Time stamp:` field, bounded by the before/after local reads | `EXECUTED` | Drill 2 run as written; output pasted | — |
| 358 | S3.2 | Drill 3: a script-inserted sentence is visible in the browser and absent from Wget's `--page-requisites` WARC | `EXECUTED` | Drill 3 run as written; Chrome part 2 macOS-only, Linux prints "skip part 2" | 2027-03 |
| 359 | S3.2 | freetsa.org/tsr returns a verifiable RFC 3161 reply for a SHA-256-only query; `openssl ts -verify` with its published cacert.pem/tsa.crt passes; changing one letter makes the block digest check fail | `EXECUTED` | lab seal step + tamper step | 2027-03 |
| 360 | S3.2 | Case: Casey Anthony trial 2011; March 2008 Firefox history in Mork; NetAnalysis (first police report, Aug 2008) showed 1 visit to the chloroform page on sci-spot.com; CacheBack showed 84 | `SOURCED` | Digital Detective post 11 July 2011; NYT 19 July 2011 as republished by NBC News | stable |
| 361 | S3.2 | Wilson (NetAnalysis developer) post 11 July 2011: first heard of the discrepancy ~9 June 2011; account attributed to him, not stated as fact | `SOURCED` | Digital Detective post | stable |
| 362 | S3.2 | NYT 19 July 2011: Bradley (CacheBack designer, testified) now said 1 visit not 84, after redesigning; said neither tool decoded the whole file; said his findings were not presented to the jury — attributed to him | `SOURCED` | NYT via NBC | stable |
| 363 | S3.2 | ABA Journal 21 July 2011: State Attorney press release — Bradley contacted prosecutors 23 June; discrepancy discussed 27 June; both sides agreed on one visit; a later report went to a wrong email address; Bradley's lawyer disputed "erroneous media reports"; jury acquitted 5 July | `SOURCED` | two ABA Journal reports | stable |
| 364 | S3.2 | Who knew what and when is disputed; the module gives both sides and does not settle it | `CONVENTION` | — | — |
| 365 | S3.2 | Windows route is WSL; no native PowerShell port was run | `CONVENTION` | as S2.7 / S3.1 | — |
| 366 | S3.2 | Guardrail probes RFC 3161 TSA endpoints by POSTing the SHA-256-of-empty query and requiring `application/timestamp-reply`; a GET gets 403 and proves nothing | `EXECUTED` | `tools/guardrail.py` TSA_ENDPOINTS; freetsa.org/tsr verified in gate run | — |

Defects caught in the S3.2 build pass (none shipped):

- **The seal broke itself.** It covered the collection log, and the timestamp entry was then appended to that
  log. The timestamp record now goes in its own file.
- **The Last-Modified regex was case-sensitive** and missed IANA's lowercase `last-modified` header.
- **A literal `</script>` in Drill 3 ended the app's script block.** The builder now escapes it.
- **Case draft said the jury "was never told"**; that is Bradley's claim to the Times, now attributed to him.
- **Case draft said "June and July 2011"**; the trial began earlier. Now "2011".
- **Case draft missed Bradley's point that both tools were incomplete** (neither decoded the whole file,
  though NetAnalysis got this record right). Added.
- **Guardrail GET-probed freetsa.org/tsr and got 403**; now a real POSTed query (row 366).

## Batch 17 — S3.3 Public ledgers: what the chain proves, what it only repeats, and where tracing stops

Moved ahead of "internet-wide scan data" at the user's request (2026-09-29); the L3 list is otherwise unchanged.

| # | Module | Claim | Status | Evidence | Re-check |
|---|---|---|---|---|---|
| 367 | S3.3 | ERC-20 marks `name()`, `symbol()`, `decimals()` OPTIONAL: "interfaces and other contracts MUST NOT expect these values to be present"; `Transfer(address indexed _from, address indexed _to, uint256 _value)` | `SOURCED` | ethereum/ERCs `ERCS/erc-20.md` (raw, 2026-09-29) | stable |
| 368 | S3.3 | Tether's own page lists `0xdAC17F958D2ee523a2206206994597C13D831ec7` for Ethereum | `EXECUTED` | lab item001 (tether.to/en/supported-protocols/) | 2027-03 |
| 369 | S3.3 | Blockscout's first search page for USDT: 30 tokens with symbol USDT, 29 not the issuer's, 28 named "Tether USD"; most-"held" lookalike 0x5620…50f7 with 128,698 | `EXECUTED` | lab item002; counts drift, expected output says so | volatile |
| 370 | S3.3 | Node: the issuer's contract and 0x417D…A154 both return name "Tether USD", symbol "USDT", decimals 6 | `EXECUTED` | lab items 003–004 | 2027-03 |
| 371 | S3.3 | Drill 1: 0x417D…A154 is not on Tether's page; created 2025-12-30; Tether's contract created 2017-11-28 | `EXECUTED` | Drill 1 run as written, bash + zsh identical | stable |
| 372 | S3.3 | 2024 poisoning: victim's key signed 0.05 ETH (native) to 0xd9a1b0b1…853a91 at 09:14:47 UTC 3 May 2024 (tx 0xb18ab131…) | `EXECUTED` | lab item005 (node) + Blockscout | stable |
| 373 | S3.3 | Tx 0x9147d74e… (09:17:35 UTC) was signed by 0x517d…1db2, not the victim; it emitted 16 Transfer events naming 16 different senders; the victim's: token 0x7393…262e, to 0xd9a1c378…3a91, raw 50000 | `EXECUTED` | lab items 006–007 (node receipt) | stable |
| 374 | S3.3 | Token 0x7393…262e: name "Ether", symbol "ETH", decimals 6 | `EXECUTED` | lab item008 (node) | stable |
| 375 | S3.3 | Intended vs lookalike: first 4 and last 6 hex digits identical; 27 of 40 differ | `EXECUTED` | lab item005 + item007 | stable |
| 376 | S3.3 | Loss: victim's key signed transfer() on WBTC contract 0x2260…c599 to the lookalike, raw 115528802767 (1,155.288 WBTC) at 10:31:35 UTC, 74 min after the fake transfer | `EXECUTED` | lab item009 (node); timestamp via Blockscout | stable |
| 377 | S3.3 | Chainalysis (23 Oct 2024): scammer "returned the original $68 million in ETH on May 9th"; 82,031 addresses seeded | `SOURCED` | chainalysis.com/blog/address-poisoning-scam/ raw HTML | stable |
| 378 | S3.3 | Bybit theft tx 0x46deef0f… block 21895238, 14:13:35 UTC, execTransaction (0x6a761202), operation=1, to 0x9622…7242, inner transfer(0xbdd077…9516, 0) | `EXECUTED` | lab items 011 (node raw decode) + 012 (explorer decode) agree | stable |
| 379 | S3.3 | Safe v1.3.0: `enum Operation {Call, DelegateCall}`; proxy: singleton "always needs to be first declared variable", fallback `sload(0)` | `SOURCED` | safe-global/safe-smart-account v1.3.0 Enum.sol, GnosisSafeProxy.sol (raw) | stable |
| 380 | S3.3 | Bybit Safe storage slot 0 today = 0xbdd077f651ebe7f7b3ce16fe5f2b025be2969516 | `EXECUTED` | lab item013 (node, latest) | 2027-03 |
| 381 | S3.3 | sweepETH tx 0xb61413c4… at 14:16:11 UTC paid 401,346.768858404671846374 ETH from the Safe to 0x4766…86e2; state-changes agree | `EXECUTED` | lab item014; Drill 2 | stable |
| 382 | S3.3 | 0x4766…86e2: 62 outgoing txs; 40 distinct addresses paid exactly 10,000 ETH; 39 on FBI list, 0x36ed…e4cb not; 0x4766 itself not listed | `EXECUTED` | lab items 010, 015–016 | re-check if IC3 edits the PSA |
| 383 | S3.3 | FBI PSA I-022625-PSA (26 Feb 2025): North Korea / "TraderTraitor", ~$1.5B, on or about 21 Feb 2025; 51 ETH addresses "holding or have held assets from the theft"; "dispersed across thousands of addresses on multiple blockchains" | `SOURCED` | ic3.gov/psa/2025/psa250226 raw HTML (item010) | 2027-03 |
| 384 | S3.3 | Drill 3: 0x36ed…e4cb sent 2 × 5,000 ETH to 0x4571…900a on 22 Feb 2025; neither listed; 0x4571's first page: 50 txs to 41 addresses | `EXECUTED` | Drill 3 run as written; count by direct query | stable |
| 385 | S3.3 | Drill 2: Blockscout v2 internal-transactions answered 0, 2 and no reply for the same sweep within minutes; v1 txlistinternal answered 1; v1 also returned HTTP 429 for several minutes after heavy build use | `EXECUTED` | Drill 2 bash + zsh runs pasted; lab log rows | volatile |
| 386 | S3.3 | Arkham announced ZachXBT submitted "definitive proof" of Lazarus at 19:09 UTC 21 Feb 2025 (Arkham's bounty) | `SOURCED` | crypto.news 22 Feb 2025 and cryptoninjas 22 Feb 2025, both quoting Arkham's post | stable |
| 387 | S3.3 | Sygnia (16 Mar 2025): dev macOS workstation compromised 4 Feb "likely through social engineering"; AWS 5–17 Feb; S3 JS modified 19 Feb with activation condition for one Bybit cold wallet; malicious code removed two minutes after the tx; Mandiant confirmed attribution (per Safe's X post); Docker project in ~/Downloads | `SOURCED` | sygnia.co/blog/sygnia-investigation-bybit-hack/ raw HTML | stable |
| 388 | S3.3 | Etherscan labels 0x4766…86e2 "Bybit Exploiter 1" | `SOURCED` | etherscan.io address page title (2026-09-29) | 2027-03 |
| 389 | S3.3 | Bitget: unauthorized transfers from some hot wallets detected 18:31 UTC 24 Sep 2026; $351.6M; CEO: "compromised a critical backend system…spoof transaction data…"; "Private key compromise has been ruled out" | `SOURCED` | CoinDesk 25 Sep 2026 raw HTML | re-read when independent reports land |
| 390 | S3.3 | Bitget CEO: "Based on IP behavior patterns and on-chain analysis, the attack method…is highly consistent with known patterns of North Korean hacker organizations" | `SOURCED` | The Hacker News (2026/09) raw HTML | as row 389 |
| 391 | S3.3 | Whitepaper §10: "Some linking is still unavoidable with multi-input transactions, which necessarily reveal that their inputs were owned by the same owner." | `SOURCED` | nakamotoinstitute.org/library/bitcoin/ HTML (bitcoin.org PDF unreadable here) | stable |
| 392 | S3.3 | Bitcoin Wiki Privacy: "One of the purposes of CoinJoin is to break this heuristic" | `SOURCED` | en.bitcoin.it/wiki/Privacy raw HTML | stable |
| 393 | S3.3 | IC3 I-081325-PSA (13 Aug 2025) updates I-062424-PSA on fictitious law firms; "The US Government does not request payment for law enforcement services provided." | `SOURCED` | ic3.gov/PSA/2025/PSA250813 raw HTML | stable |
| 394 | S3.3 | Fake-token swap in theory is a composite of a common pattern, not a named case | `CONVENTION` | labelled as such in the text | — |
| 395 | S3.3 | Lab stops one hop from addresses named in case documents; victim and intended recipient truncated; lookalike shown in full | `CONVENTION` | scope.txt, lab header | — |
| 396 | S3.3 | Lab, bash + zsh + sha256sum variant: identical checker output; RFC 3161 seal verifies | `EXECUTED` | four full runs 2026-09-29 | 2027-03 |
| 397 | S3.3 | Windows route is WSL; no native PowerShell port was run | `CONVENTION` | as S3.2 | — |

Defects caught in the S3.3 build pass (none shipped):

- **A WebFetch summary invented a claim.** It said Chainalysis described the poisoning as "not fake tokens". The raw page says no such thing, and the ledger shows a fake "ETH" token (row 373). Only raw text is pinned.
- **An explorer said "0 internal transactions" for a 401,346 ETH sweep**, and the first checker silently dropped the line. The lab now tests content, retries across two interfaces, and prints UNKNOWN (row 385).
- **The collection-log FAILED check read every row**, so a retried-then-successful capture stopped the lab. The last row per item now decides.
- **The inner-call decoder read the bytes argument's length word as its selector.** It now follows the ABI offset.
- **The FBI's attribution was first graded B2.** Under S3.1's rule (the course's own history with the source), a first-use source is F; now F3.
- **The bare explorer base `…/api/v2` failed the URL gate (400).** The variable is now the host.
- **A stale background run overwrote a sealed evidence file**; the seal reported it `FAILED`. The case was rerun clean.
- **Case draft said "hot and warm wallets" for Bitget's 18:31 detection**; CoinDesk says "some exchange hot wallets". Fixed.
- **Case draft cited BleepingComputer for the Bitget attribution quote**, which returned 403 to a raw fetch; re-pinned to The Hacker News raw HTML.
- **"The address the sweep paid" was first described as outside the FBI list's remit**; it held stolen ether, which is what the list describes. Now stated as a gap without a reason.
