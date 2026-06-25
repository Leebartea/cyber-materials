# Cyber Materials

Two self-paced cybersecurity curricula, each shipped as a self-contained, offline-first HTML reader — no build step, no server, no account. Open the file in any browser, on any device.

- **Cyber Guardians** (`cyber_guardians_curriculum.md`, `cyber_guardians_app.html`) — broad cybersecurity course, beginner to specialist, as an interactive React reader (progress tracking, quizzes, search).
- **Full-Stack AppSec** (`cyber-full stack/full_stack_appsec_curriculum.md`, `full_stack_appsec_app.html`) — a security path built specifically for full-stack web developers: every vulnerability is shown with annotated vulnerable-vs-secure code in **both Node.js and Python**, plus hands-on labs scoped to Apple Silicon. Start with `cyber-full stack/START_HERE_appsec.md`. (A plain-HTML fallback reader with the same content is at `full_stack_appsec_app_static.html`.)

## Responsible use

This curriculum teaches real attack techniques — SQL injection, XSS, CSRF, SSRF, authentication bypass, and more — so you can recognize and defend against them. That knowledge is dual-use by nature, and the same rule applies throughout every lab in this course:

**Only test systems you own, or have explicit written permission to test.**

Allowed: your own local or deployed apps, intentionally-vulnerable training apps (OWASP Juice Shop, DVWA, WebGoat), PortSwigger Web Security Academy, TryHackMe/HackTheBox labs, and public bug bounty programs — only after reading the exact scope.

Not allowed: testing systems you don't own or don't have permission for, scanning third-party infrastructure, bypassing access controls "just to check," or touching real user data.

If you can't clearly state who gave you permission and what's in scope, stop.

This material is for education and authorized security testing only. It is provided as-is, with no warranty (see `LICENSE`); the author is not responsible for how it's used.

## License

MIT — see `LICENSE`.
