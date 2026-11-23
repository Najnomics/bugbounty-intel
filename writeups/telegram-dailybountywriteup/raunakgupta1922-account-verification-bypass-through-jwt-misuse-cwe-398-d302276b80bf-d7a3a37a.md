# Account Verification Bypass through JWT Misuse & CWE-347

- **Source URL:** https://medium.com/@RaunakGupta1922/account-verification-bypass-through-jwt-misuse-cwe-398-d302276b80bf?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250906073657/https://medium.com/@RaunakGupta1922/account-verification-bypass-through-jwt-misuse-cwe-398-d302276b80bf
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10641 (id 10641)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account Verification Bypass through JWT Misuse & CWE-347

## My Introduction

Hiyya, I am Raunak Gupta, a Security Researcher and Bug Bounty Hunter for fun and profit.

All sensitive data is blurred due to privacy reasons.


## Target Overview

Redacted is a platform that provides blog articles, tutorials, and resources for developers. Users can create accounts to interact with content, such as posting comments. To maintain authenticity, the platform requires users to verify their email before gaining full access to certain features.

## Now Main Story

While testing the platform, I noticed that unverified users couldn’t post comments and were asked to verify their email first.

I decided to analyze the **JWT tokens** issued during registration.

- The unverified account’s JWT had a few extra claims compared to the verified one.

- After clicking the official verification link, I noticed its structure:

`https://example.com/auth/verify-email/<JWT_TOKEN>`
This gave me an idea: what if the verification endpoint accepted *any* valid session JWT?

So, I created a new account, intercepted an authenticated request (like a page refresh), copied the **session JWT**, and pasted it into the verification URL:

`https://example.com/auth/verify-email/<SESSION_JWT>`
Boom, the account got verified instantly, without ever needing to open the verification email.

This completely bypassed the intended email ownership check.

I will add poc video link as soon as bug will fixed

## Connect with me

LinkedIn: [https://www.linkedin.com/in/raunak-gupta-772408255/](https://www.linkedin.com/in/raunak-gupta-772408255/)

My Discord server: [https://discord.gg/8SSx5Ma9ve](https://discord.gg/8SSx5Ma9ve)

My YouTube Channel: [https://www.youtube.com/@BiscuitSecurity/featured](https://www.youtube.com/@BiscuitSecurity/featured)
