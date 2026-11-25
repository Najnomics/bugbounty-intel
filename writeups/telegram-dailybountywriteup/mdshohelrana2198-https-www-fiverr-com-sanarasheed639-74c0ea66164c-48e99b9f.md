# 🐛 Bug Bounty Writeup

- **Source URL:** https://medium.com/@mdshohelrana2198/https-www-fiverr-com-sanarasheed639-74c0ea66164c
- **Fetched from:** https://medium.com/@mdshohelrana2198/https-www-fiverr-com-sanarasheed639-74c0ea66164c?source=rss-1c87222dbc8d------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14962 (id 14962)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Shohel Rana / Tue, 27 Oct 2026 21:16:17 GMT

A practical, step-by-step overview for people starting out in web application penetration testing. For use only in authorized pentests or bug bounty programs with explicit scope.

Introduction

SQL Injection (SQLi) remains one of the most critical vulnerabilities in the OWASP Top 10. When a Web Application Firewall (WAF) is in place, automated scanners often get blocked — but understanding the manual methodology lets you work through the logic and find legitimate bypasses. Here’s the process broken down for beginners.

Step 1: Reconnaissance & Parameter Identification

Map every input point in the target app — URL parameters, form fields, headers (User-Agent, X-Forwarded-For), cookies, JSON body.

Use Burp Suite to capture and map the full traffic.

Check whether a WAF is present: fingerprint it with a tool like wafw00f, or send a simple test payload and observe the response (403 errors, captchas, generic block pages are common signs).

Step 2: Vulnerability Detection

Try breaking the query with a single quote (’), double quote, or backslash and see if it triggers an error.

Boolean-based test: compare the response for id=1 AND 1=1 vs id=1 AND 1=2.

Time-based test: check if a delay-inducing condition causes the response to actually slow down.

This stage tells you whether an injection point exists and how aggressively the WAF is filtering.

Step 3: Understanding WAF Behavior (Filter Fingerprinting)

Before attempting any bypass, figure out what the WAF is actually blocking:

Specific keywords (UNION, SELECT, OR, AND)?

Pattern/regex-based (e.g., keyword followed by a space)?

Case-sensitive or case-insensitive matching?

Is there a payload length limit?

Send small, isolated test payloads (one keyword at a time) to identify the exact blocking rule — this is the most important step in the entire process.

Step 4: Common Bypass Technique Categories

These are concept-level categories documented in general security literature and the OWASP Testing Guide:

Case manipulation — altering keyword casing to slip past case-sensitive regex filters.

Whitespace/comment substitution — replacing spaces with inline comments or alternate whitespace characters.

Encoding — URL encoding, double encoding, or Unicode encoding to obfuscate the payload so the WAF can’t pattern-match the raw string.

Logical operator alternatives — using equivalent logical/comparison expressions instead of standard OR/AND.

Function/keyword splitting — breaking up keywords using inline comments.

HTTP Parameter Pollution (HPP) — sending the same parameter multiple times so the backend and WAF parse it differently.

Oversized/buffer tricks — padding requests with large dummy data to exceed a WAF’s inspection limits.

Note: I’m intentionally not providing ready-to-use payload strings here. Every WAF (Cloudflare, ModSecurity, AWS WAF, Akamai, etc.) uses a different rule set — a generic payload that works on one will fail on another. In a real engagement, you craft target-specific payloads based on what you learned in Step 3.

Step 5: Data Extraction (in an authorized test)

Once a bypass succeeds:

Identify the database version, current user, and database name.

Determine column count (using ORDER BY or UNION-based techniques).

Enumerate tables/columns via information\_schema (if the DBMS supports it).

Keep sensitive data access to the minimum needed for proof-of-concept.

Step 6: Handling Blind SQLi

WAFs often suppress error messages, pushing you into blind territory:

Boolean-based blind: look for distinct response patterns between true/false conditions.

Time-based blind: confirm using delay-based conditions.

Out-of-band (OOB): DNS exfiltration techniques, if internal interaction is possible.

Step 7: Documentation & Reporting

Save every payload, request/response pair, and timestamp (Burp’s history is useful here).

Clearly show the client what the WAF blocked vs. what got through.

Include remediation advice: parameterized queries, input validation, WAF rule tuning, least-privilege DB accounts.

Step 8: Prevention Recommendations (for your client report)

Mandate prepared statements / parameterized queries.

Audit raw query fragments even in ORM-based codebases.

Treat the WAF as one layer in a defense-in-depth strategy, not the sole protection.

Regular dependency and DB permission audits.

Legal/Ethical Note

This methodology applies only within a written, authorized pentest engagement or bug bounty scope. Testing systems without permission or outside of scope is illegal under international law.
