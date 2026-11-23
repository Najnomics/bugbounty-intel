# # I Found a Subdomain Takeover on Jio — But Got No Credit

- **Source URL:** https://medium.com/@cyberdivyanshu69/i-found-a-subdomain-takeover-on-jio-but-got-no-credit-c46222f8bf0a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250822111127/https://medium.com/@cyberdivyanshu69/i-found-a-subdomain-takeover-on-jio-but-got-no-credit-c46222f8bf0a
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10416 (id 10416)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
I Found a multiple Subdomain Takeover on Jio — But Got No Credit

In July 2025, while doing casual recon on major Indian telecom infrastructure, I stumbled upon a critical \*\*subdomain takeover vulnerability\*\* in Jio’s infrastructure. This issue allowed full control over a subdomain once it was unclaimed — a serious risk for phishing, data theft, and brand abuse.

---

\## 🕵️♂️ What I Found

\- ✅ A valid subdomain: \`jioacq.media.jio.com\`

- ⚠️ This subdomain was pointing to an \*\*unclaimed hosting service\*\*.

- 🧠 Tool Used: \`Subzy\` (by ProjectDiscovery) flagged it as vulnerable.

- 📡 DNS verification showed \`CNAME\` to a non-resolving domain.

- 🚨 This type of issue can lead to \*\*complete hijacking\*\* of subdomain content.

---

\## 📬 I Reported It to Jio

\- I responsibly disclosed the issue to Jio via email on \*\*July 27, 2025\*\*.

- I included all proof: scan outputs, DNS records, and screenshot evidence.

- But unfortunately, \*\*they silently fixed it without acknowledging my report.\*\*

---

\## 🤖 Tools I Used

\- \`Subfinder\` – for subdomain enumeration

- \`httpx\` – for live status check

- \`Subzy\` – for takeover detection

- \`dig\` – DNS CNAME verification

- \`Screenshot\` and timestamps for PoC

---

\## 🔐 Why This Matters

Subdomain takeovers are a well-known attack vector and can be used to:

- Host phishing pages

- Steal cookies/data from users

- Damage company reputation

- Mislead users with fake branding

By silently fixing it, Jio avoided public embarrassment — but also ignored ethical reporting.

---

\## 🖼️ Screenshots + Proof of Concept (PoC)

I have attached all evidence including:

- Subdomain vulnerability report

- DNS CNAME screenshot

- Tool output

- Gmail report with timestamp

- Confirmation of fix

---

📎 \*\*Full PoC + Evidence ZIP Download\*\*: 

👉 \[Click here to download\](https://github.com/DIVYANSHUBUG69/jio-subdomain-takeover.git)

---

\## 🧑💻 About Me

I'm a 19-year-old bug bounty hunter and student of Computer Science. I conduct all my recon and analysis \*\*using a mobile phone (Termux)\*\* — no PC required.

I believe ethical hackers deserve recognition when reporting real issues.

---

\## 💬 Want to Collaborate?

Reach out via LinkedIn or comment here. I'm open to connect with fellow bug hunters, devs, and security researchers.

---

\## 🔄 Timeline Summary

| Date | Event |

|------------|-------------------------------|

| July 27 | Bug found + reported to Jio |

| July 28-29 | Jio fixed silently |

| Aug 2-3 | Preparing public disclosure |

---

Thanks for reading. Please support ethical disclosure and give credit where it’s due.
