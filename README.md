# Cyber Materials

Two self-paced cybersecurity curricula, each shipped as a self-contained, offline-first HTML reader — no build step, no server, no account. Open the file in any browser, on any device.

- **Cyber Guardians** (`cyber-guardians/cyber_guardians_curriculum.md`, `cyber-guardians/cyber_guardians_app.html`) — broad cybersecurity course, beginner to specialist, as an interactive React reader (progress tracking, quizzes, search).
- **Full-Stack AppSec** (`cyber-full stack/full_stack_appsec_curriculum.md`, `cyber-full stack/full_stack_appsec_app.html`) — a security path built specifically for full-stack web developers: every vulnerability is shown with annotated vulnerable-vs-secure code in **both Node.js and Python**, plus hands-on labs. Start with `cyber-full stack/START_HERE_appsec.md`. (A plain-HTML fallback reader with the same content is at `cyber-full stack/full_stack_appsec_app_static.html`.)

## How to use these files

Every `.html` reader in this repo is a single self-contained file — React/CSS/content are all inlined, with no build step, no server, and no internet connection required.

- **Open it directly:** double-click the file, or drag it onto an open browser window, or use your browser's File → Open. Any modern browser works (Chrome, Firefox, Safari, Edge).
- **Folder location doesn't matter.** None of these files link to each other or load anything relative to their location, so you can move, rename, or reorganize them freely — nothing will break.
- **Progress is saved locally in your browser** (via `localStorage`), tied to that exact file. If you move or rename a reader *after* you've started checking off progress in it, treat it as a fresh copy — the saved progress stays attached to the old file path/name, not the content. Avoid renaming a reader once you're partway through it.
- **Cross-device note:** since progress lives in the browser, not in the file, it doesn't automatically sync between devices. Copy the `.html` file to each device you study from; each copy tracks its own progress independently.

## Responsible use

This curriculum teaches real attack techniques — SQL injection, XSS, CSRF, SSRF, authentication bypass, and more — so you can recognize and defend against them. That knowledge is dual-use by nature, and the same rule applies throughout every lab in this course:

**Only test systems you own, or have explicit written permission to test.**

Allowed: your own local or deployed apps, intentionally-vulnerable training apps (OWASP Juice Shop, DVWA, WebGoat), PortSwigger Web Security Academy, TryHackMe/HackTheBox labs, and public bug bounty programs — only after reading the exact scope.

Not allowed: testing systems you don't own or don't have permission for, scanning third-party infrastructure, bypassing access controls "just to check," or touching real user data.

If you can't clearly state who gave you permission and what's in scope, stop.

This material is for education and authorized security testing only. It is provided as-is, with no warranty (see `LICENSE`); the author is not responsible for how it's used.

## License

MIT — see `LICENSE`.
