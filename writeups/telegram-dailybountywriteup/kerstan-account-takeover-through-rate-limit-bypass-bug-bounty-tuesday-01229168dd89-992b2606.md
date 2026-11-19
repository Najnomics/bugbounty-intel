# Account Takeover Through Rate-Limit Bypass — Bug Bounty Tuesday

- **Source URL:** https://medium.com/@kerstan/account-takeover-through-rate-limit-bypass-bug-bounty-tuesday-01229168dd89?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240831160931/https://medium.com/@kerstan/account-takeover-through-rate-limit-bypass-bug-bounty-tuesday-01229168dd89
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5536 (id 5536)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Account Takeover Through Rate-Limit Bypass — Bug Bounty Tuesday**

**Subscribed to:** [https://medium.com/@kerstan](/@kerstan)

Hello everyone, I’m Kerstan.

Today is Bug bounty Tuesday, I will share with you how to use rate-limit bypass account takeover.

So, let’s dive right in.

In a private bug bounty program, when a password reset was initiated, users were asked to enter a six-digit numeric code sent to their email for verification.

To deter brute-force attacks, the application set up rate-limit protection, limiting the number of requests users could make within a specific time frame. If this limit was exceeded, the system would return a 429 Too Many Requests error message.

However, the rate-limit protection was bypassed by adding two X-Forwarded-For: IP headers.

```
POST /reset HTTP/2
Host:example.com
X-Forwarded-For:1.1.1.1
X-Forwarded-For:2.2.2.2
```
By changing the IP address in the second X-Forwarded-For header, it became possible to bypass the rate limit and attempt multiple codes until the correct one was located.

Exploiting this vulnerability made it possible to take over any account within the application without authorization.

**Resources:**
