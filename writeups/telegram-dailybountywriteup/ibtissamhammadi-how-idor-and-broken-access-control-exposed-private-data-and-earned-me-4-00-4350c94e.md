# How IDOR and Broken Access Control Exposed Private Data and Earned Me $4,000 in 1 Day

- **Source URL:** https://medium.com/@ibtissamhammadi/how-idor-and-broken-access-control-exposed-private-data-and-earned-me-4-000-in-1-day-dd01a07e93e4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250310090820/https://medium.com/@ibtissamhammadi/how-idor-and-broken-access-control-exposed-private-data-and-earned-me-4-000-in-1-day-dd01a07e93e4?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8973 (id 8973)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **How IDOR and Broken Access Control Exposed Private Data and Earned Me $4,000 in 1 Day**

## *Discover how a simple security flaw turned into a $5,000 payout — and how you can do it too.*

It was just another ordinary day. I was sitting at my desk, sipping coffee, when I stumbled upon a **bug bounty program** for a small e-commerce platform. The platform promised rewards for finding security vulnerabilities, and I decided to give it a shot. Little did I know, within 24 hours, I’d uncover a critical flaw that would earn me **$4,000**.

This article is my story. It’s a **beginner-friendly guide** to finding **IDOR (Insecure Direct Object Reference)** and **Broken Access Control** vulnerabilities. By the end, you’ll know exactly how to spot these flaws and maybe even earn some money yourself.

# What Are IDOR and Broken Access Control?

**IDOR** and **Broken Access Control** are two of the most common vulnerabilities in web applications.

- **IDOR** happens when an application lets you access someone else’s data by tampering with an ID in the URL or request. For example, changing `user_id=123` to `user_id=124` might let you view another user’s private information.
- **Broken Access Control** occurs when an application fails to enforce…
