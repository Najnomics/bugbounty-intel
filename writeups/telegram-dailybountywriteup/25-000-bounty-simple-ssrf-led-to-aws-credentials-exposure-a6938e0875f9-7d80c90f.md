# 25,000$ Bounty — Simple SSRF Led to AWS Credentials Exposure

- **Source URL:** https://cyberw1ng.medium.com/25-000-bounty-simple-ssrf-led-to-aws-credentials-exposure-a6938e0875f9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250228014848/https://cyberw1ng.medium.com/25-000-bounty-simple-ssrf-led-to-aws-credentials-exposure-a6938e0875f9
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8917 (id 8917)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# 25,000$ Bounty — Simple SSRF **Led to AWS Credentials Exposure**

## Exploiting SSRF in Analytics Reports to Gain AWS Access

# Timeline

- 📅 Reported: November 23, 2023
- ✅ Fixed: November 24, 2023
- 💰 Bounty: **$25,000**
- Severity: **Critical (9.8/10)**

# Introduction

Server Side Request Forgery (SSRF) is one of the most dangerous vulnerabilities in web applications, especially when it allows attackers to access **internal services** or **cloud metadata endpoints**.

Recently, a researcher found a **critical SSRF vulnerability** in an Analytics Reports feature that exposed **AWS credentials**, which could potentially allow full control over cloud services.

In this article, I’ll break down the vulnerability, how it was exploited, and how such attacks can be prevented.

# What is SSRF?

Server Side Request Forgery (SSRF) happens when an attacker tricks a web server into making requests to internal services or external systems.

# Types of SSRF Attacks:

1. **Basic SSRF** — The attacker forces a server to make a request to an unintended destination.
