# OAuth and JWT Attacks

- **Source URL:** https://medium.com/cloud-security/oauth-and-jwt-attacks-3840fe2a113f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501113855/https://medium.com/cloud-security/oauth-and-jwt-attacks-3840fe2a113f?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9076 (id 9076)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# OAuth, OpenID, and JWT Attacks

## How do I hack thee? Let me count the ways…

\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~

⚙️ Check out my series on *Automating Cybersecurity Metrics. The Code.*

🔒 Related Stories: *Appsec | Secure Code | Data Breaches | Pentesting | Bug Bounties*

💻 Free Content on *Jobs in Cybersecurity |* ✉️ Sign up for the *Email List*

\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~

I find so many authentication and authorization errors on penetration tests that I wanted to review what information is out there in case I’ve missed anything and summarize it in a post for myself and others. I’m focusing on OAUTH and JWTs in this post since they are so prevalent. Cookies, local storage, and other forms of authentication and authorization lead to many other types of attacks and vulnerabilities not included here.

## Client confusion

Before I even start I’m going to remind everyone including myself that Client in OAuth terms does not always refer to the user’s device or the user’s browser. It can refer to the Client Application or Client Server that wants access to some data on Resource Server and the user is authorizing that data.
