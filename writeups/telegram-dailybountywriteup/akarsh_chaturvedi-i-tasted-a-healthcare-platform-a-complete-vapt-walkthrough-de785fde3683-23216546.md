# Breaking Down a Healthcare Web Application

- **Source URL:** https://medium.com/@Akarsh_Chaturvedi/i-tasted-a-healthcare-platform-a-complete-vapt-walkthrough-de785fde3683
- **Fetched from:** https://medium.com/@Akarsh_Chaturvedi/i-tasted-a-healthcare-platform-a-complete-vapt-walkthrough-de785fde3683?source=rss-42087a213b30------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14901 (id 14901)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Akarsh_¢haturvedi / Mon, 07 Sep 2026 18:08:40 GMT

Healthcare platforms hold some of the most sensitive data imaginable patient records, medical histories, and personal identifiable information (PII). So when I set out to perform a *Vulnerability Assessment & Penetration Test (VAPT)* on a healthcare web application, my goal was clear: *find every weakness before a real attacker does.*

In this post, I’ll walk you through my complete methodology from reconnaissance to exploitation the exact tools I used, the vulnerabilities I discovered (including a Critical XSS and an unrestricted file upload), and what developers can do to fix them.

1\. Introduction & Scope

2\. Methodology & Approach

3\. Tools Used

4\. Step-by-Step Testing Process

5\. Findings & Vulnerabilities

6\. Impact Analysis

7\. Recommendations

8\. Conclusion

**Objective:** To conduct a comprehensive Vulnerability Assessment and Penetration Test (VAPT) on a healthcare platform to identify security weaknesses that could be exploited by malicious actors.

**Scope:**

· Web application security testing

· Input validation vulnerabilities

· File upload security

· Configuration security

· Information disclosure

**Timeline:** \~5 hours total — Reconnaissance: 1 hour · Active Testing: 3 hours · Documentation: 1 hour

I followed a structured, industry-standard methodology to ensure nothing was missed:

VAPT METHODOLOGY

─────────────────────────────────────────

1. Reconnaissance

↓

2. Information Gathering

↓

3. Vulnerability Identification

↓

4. Exploitation / POC Testing

↓

5. Documentation & Reporting

↓

6. Recommendations

Frameworks referenced throughout:

· OWASP Top 10 (2021) — primary vulnerability reference

· WSTG (Web Security Testing Guide) — testing procedures

· PTES (Penetration Testing Execution Standard) — methodology

**Environment:** Kali Linux on VirtualBox — a complete penetration testing distribution.

1\. DNS Lookup

nslookup healthcare-..\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*.


2. Technology Detection

whatweb [https://healthc](https://healthcare-plus-vulnerable.vercel.app)…………………….


3. Connectivity Test

ping -c 5 healthca.\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*.app

**Output:**

❯ Server: G………\*\*..

❯ IP: 216.1\*0.\*\*.\*

❯ Technology: HTML5, JavaScript

❯ Email: info@h\*\*\*\*\*\*\*\*\*\*\*.\*\*\*

**What I discovered:**

· ✅ Server is hosted on ………..

· ✅ Site uses HTML5 & JavaScript

· ✅ Business email exposed: info@h\*\*\*\*\*\*\*\*\*\*\*.\*\*\*
