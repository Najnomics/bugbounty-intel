# how i founded my first reflected XSS in public vdp on h1

- **Source URL:** https://medium.com/@sh3rif0x/how-i-founded-my-first-reflected-xss-in-public-vdp-on-h1-d566ddcb63d3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260310102717/https://medium.com/@sh3rif0x/how-i-founded-my-first-reflected-xss-in-public-vdp-on-h1-d566ddcb63d3
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11581 (id 11581)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# how i founded my first reflected XSS in public vdp on h1

Hi everyone 👋, 

I hope you’re having a great day. In this post, I’ll walk through how I discovered a reflected XSS vulnerability on a subdomain — from simple reconnaissance to proof of concept.

\### 🔍 Discovery

While testing a wildcard scope program, I started with \*\*subdomain enumeration\*\* to map out the attack surface. 

After filtering live subdomains, I ran \*\*parameter fuzzing\*\* across them to check for possible injections (XSS, SSTI, SQLi, etc.).

One subdomain — 

\`cloud.comms.redacted.com\` — responded interestingly. 

The \`lang\` parameter reflected a double quote (\`”\`) directly in the response instead of its encoded form (\`%22\`).

That was the first sign of possible XSS.

\### 💥 Exploitation

By injecting attributes like \`onfocus\` and \`autofocus\`, I confirmed that JavaScript could execute automatically on page load — no additional clicks needed:

\`[https://cloud.commss.redacted.com/primaverasound26?lang=rrrrrrrrrr](https://cloud.comms.redacted.com/primaverasound26?lang=rrrrrrrrrr)"%20style="visibility:visible"%20onfocus="alert(1)"%20autofocus="\`

The payload is reflected inside an \`\<input>\` field, and \`autofocus\` triggers the injected \`onfocus\` handler — resulting in immediate script execution.

Although the domain was \*\*abandoned\*\*, the issue was still triaged as \*\*Medium severity\*\* on HackerOne due to its public accessibility.

**Timeline:** Reported on Oct 15, 2025 → Triaged on Oct 25, 2025

\### 🧠 Takeaway

Even “forgotten” subdomains can host impactful vulnerabilities. Continuous reconnaissance and parameter fuzzing can reveal critical issues hiding in plain sight.

Discovered by \*\*@sh3rif0x\*\* ✨

Let’s connect on x and h1
