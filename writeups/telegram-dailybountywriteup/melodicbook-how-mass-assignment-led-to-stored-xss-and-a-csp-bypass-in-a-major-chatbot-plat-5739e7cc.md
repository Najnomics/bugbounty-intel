# How mass-assignment led to stored-XSS and a CSP bypass in a major chatbot platform

- **Source URL:** https://medium.com/@melodicbook/how-mass-assignment-led-to-stored-xss-and-a-csp-bypass-in-a-major-chatbot-platform-3c6569d7c9e9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142413/https://medium.com/@melodicbook/how-mass-assignment-led-to-stored-xss-and-a-csp-bypass-in-a-major-chatbot-platform-3c6569d7c9e9?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11255 (id 11255)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# How mass-assignment led to stored-XSS and a CSP bypass in a major chatbot platform

By Sami Mirov — Security Researcher

Short summary: In recent research I discovered a high-impact vulnerability class in a widely used chatbot vendor. The root cause was unsafe mass-assignment: the platform merged incoming JSON into server models without allow-listing fields. That, combined with inconsistent sanitization and a permissive Content-Security-Policy, allowed persisted HTML to be stored and later render in customer websites and internal agent consoles. **About 500 customer instances were affected**. This article explains the issue, why mass-assignment is particularly dangerous in embedded widgets, safe proof-of-concept practices, remediation steps, and defensive code patterns.

**A single convenience pattern, platform-wide blast radius**

Developers love convenience: mapping request bodies directly to model objects is fast, flexible, and common in many frameworks. But that convenience commonly known as mass-assignment becomes dangerous when the application exposes fields that should be immutable or server-controlled. In the chatbot platform I examined, client JSON was merged into persisted models (for example using Object.assign(model, req.body) or ORM update(req.body) convenience methods). Attackers could set fields like html, markup, or domKey that were later rendered into the DOM. Even with some sanitization and a CSP in place, encoded inputs and decoding steps in the rendering pipeline allowed persistent HTML to slip…
