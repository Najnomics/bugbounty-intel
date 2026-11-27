# Server-side request forgery (SSRF) in Web App Penetration Testing | 2023

- **Source URL:** https://cyberw1ng.medium.com/server-side-request-forgery-ssrf-in-web-app-penetration-testing-2023-f33d2188c4e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241210091525/https://cyberw1ng.medium.com/server-side-request-forgery-ssrf-in-web-app-penetration-testing-2023-f33d2188c4e
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3972 (id 3972)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Server-side request forgery (SSRF) in Web App Penetration Testing | 2023

## Understanding the Concept of SSRF in Web Application Penetration Testing for Bug Bounty | Karthikeyan Nagaraj

# What is SSRF?

Server-side request forgery is a web security vulnerability that allows an attacker to cause the server-side application to make requests to an unintended location.

In a typical SSRF attack, the attacker might cause the server to make a connection to internal-only services within the organization’s infrastructure. In other cases, they may be able to force the server to connect to arbitrary external systems. This could leak sensitive data, such as authorization credentials.

# What is the impact of SSRF attacks?

A successful SSRF attack can often result in unauthorized actions or access to data within the organization. This can be in the vulnerable application, or on other back-end systems that the application can communicate with. In some situations, the SSRF vulnerability might allow an attacker to perform arbitrary command execution.

An SSRF exploit that causes connections to external third-party systems might result in malicious onward attacks. these can appear to…
