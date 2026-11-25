# Hunting for IDOR and BAC Vulnerabilities in B2B Applications with Burp Suite’s Authorize Extension

- **Source URL:** https://thexssrat.medium.com/hunting-for-idor-and-bac-vulnerabilities-in-b2b-applications-with-burp-suites-authorize-extension-597877b53d94?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501112537/https://thexssrat.medium.com/hunting-for-idor-and-bac-vulnerabilities-in-b2b-applications-with-burp-suites-authorize-extension-597877b53d94?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7724 (id 7724)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **Hunting for IDOR and BAC Vulnerabilities in B2B Applications with Burp Suite’s Authorize Extension**

In today’s fast-paced world of agile development and B2B (business-to-business) applications, security professionals and bug bounty hunters alike are constantly on the lookout for vulnerabilities. Two prominent types are Insecure Direct Object References (IDOR) and Broken Access Control (BAC). These vulnerabilities can be game-changers when uncovered, especially given the criticality of B2B systems which often contain sensitive data or core business functions.

This article will guide you through using Burp Suite’s Authorize extension to identify these vulnerabilities, with practical examples and tips on effective testing techniques. With agile release cycles and frequent updates, even if the team has secured 99.4% of the endpoints, there’s always a chance to find that obscure feature or hidden parameter that opens the door to privilege escalation or unauthorized access.

# Overview of IDOR and BAC

# What is IDOR?

Insecure Direct Object References (IDOR) occur when an application allows users to access objects, like records or files, directly through a reference without proper access control checks. If a user has direct access to objects they shouldn’t, it can lead to unauthorized data…
