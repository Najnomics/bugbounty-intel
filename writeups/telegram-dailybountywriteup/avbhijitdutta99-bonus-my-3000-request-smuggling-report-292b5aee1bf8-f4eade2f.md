# Bonus — My $3000 request smuggling report

- **Source URL:** https://medium.com/@avbhijitdutta99/bonus-my-3000-request-smuggling-report-292b5aee1bf8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126141753/https://medium.com/@avbhijitdutta99/bonus-my-3000-request-smuggling-report-292b5aee1bf8
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4168 (id 4168)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Bonus — My $3000 request smuggling report

Hi everyone, today I want to share one of my request smuggling report which I performed and how I managed to do that on one of the bug bounty program. I have detailed the way I exploited the bug. So let the drumroll begin…

Let’s start with the basics. Ruleset Engines are a vital component of its security infrastructure, designed to help protect web applications from various forms of threats. This engine enables administrators to define rules that specify how incoming HTTP requests should be processed. It is often used to enforce security policies, transform request data, and mitigate various types of attacks.

There is a use of *Hexadecimal Escape Sequences;* it is Ruleset Engine’s feature that allows the use of hexadecimal escape sequences in string manipulation functions, particularly in the context of the `concat()` function. Hexadecimal escape sequences are character representations in a hexadecimal format (e.g., \x0d\x0a) and are typically used to represent special characters in URLs.

This feature, while designed to offer flexibility and functionality for rule creation, can inadvertently open the door to security vulnerabilities if not used cautiously. In this context, it enabled attackers(me) to manipulate the processing of HTTP requests in a manner that could potentially compromise security.
