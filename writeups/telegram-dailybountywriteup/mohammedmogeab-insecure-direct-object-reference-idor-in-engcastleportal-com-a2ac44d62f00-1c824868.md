# Insecure Direct Object Reference (IDOR) in engcastleportal.com

- **Source URL:** https://medium.com/@mohammedmogeab/insecure-direct-object-reference-idor-in-engcastleportal-com-a2ac44d62f00?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251107080912/https://medium.com/@mohammedmogeab/insecure-direct-object-reference-idor-in-engcastleportal-com-a2ac44d62f00?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11672 (id 11672)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Insecure Direct Object Reference (IDOR) in engcastleportal.com

Hi, I’m **Mohammed Mogeab Ahmed Al-hajj**, a security researcher.

In this article, I’m sharing details of a **critical Insecure Direct Object Reference (IDOR)** vulnerability I discovered in [engcastleportal.com](https://web.archive.org/web/20251107080912/https://engcastleportal.com/).

## 1.Title

**Critical IDOR Vulnerability Allows Unauthorized Access to All Student Accounts**

this bug was fixed

## 2. Affected Domain

## 3. Vulnerability Type

- **Insecure Direct Object Reference (IDOR)**
- OWASP Top 10: **A01:2021 — Broken Access Control**
- CWE: **CWE-639 — Authorization Bypass Through User-Controlled Key**

## 4. Severity Level

**High (CVSS 3.1 Base Score: 6.5)**

*CVSS:3.1/*


## 5. Summary

An **Insecure Direct Object Reference (IDOR)** vulnerability exists in the `edit` profile endpoint of `https://engcastleportal.com`, which allows any authenticated student user to access and scrape **personally identifiable information (PII)** of other users by modifying the `user_id` in the URL path.

This serious oversight in access control allows attackers to **enumerate thousands of student records** including names, emails, phone numbers, and dates of birth without authorization.

## 6. Affected Endpoint and Parameters

- **Endpoint:** `GET /student/profile/{user_id}/edit`
- **Parameter Affected:** `user_id` (integer path parameter)
- **Authorization Missing:** No validation to ensure that `{user_id}` matches the authenticated user

## 7. Root Cause Analysis

The backend fails to enforce proper authorization logic for the `/student/profile/{user_id}/edit` route. The system **relies solely on the presence of an authenticated session** but does not verify whether the authenticated user has permission to view or edit the profile identified by `{user_id}`.

## 8. Steps to Reproduce

1. Log into a valid user account at [https://engcastleportal.com](https://web.archive.org/web/20251107080912/https://engcastleportal.com/)
2. Capture your session cookie (e.g., `engcastle_session`) using browser dev tools or a proxy like Burp Suite
3. Access the following endpoint by incrementing the `user_id`:

- `https://engcastleportal.com/student/profile/3501/edit https://engcastleportal.com/student/profile/3502/edit ..`

1. Each request will return the full profile form of other students:

- First Name
- Last Name
- Email Address
- Phone Number
- Date of Birth

look at this photo

## 9. Proof of Concept (PoC)

## Python Exploit Script

`i can't share code here`
## Example Output

```
{'user_id': 3501, 'first_name': 'Ayman', 'last_name': 'Saeed', 'email': 'ayman@example.com', 'date_of_birth': '2001-05-01', 'phone_number': '1234567890'}
{'user_id': 3502, 'first_name': 'Salma', 'last_name': 'Ali', 'email': 'salma@example.com', 'date_of_birth': '1999-12-12', 'phone_number': '0987654321'}
...
```
## 9–2. Critical Observation: Full Account Takeover via Email Enumeration and ID-Based Authentication

During further analysis, it was discovered that the platform’s authentication mechanism appears to be improperly tied to user identifiers — specifically the `user_id` and email address combination. Once a malicious actor gains access to another student's profile via the IDOR vulnerability, they are able to extract both the **email address** and potentially **infer or reset** the password associated with that account.

## Behavior Analysis

This behavior suggests that:

- The system may be relying on **predictable identifiers** (e.g., sequential `user_id` and publicly exposed emails) for account authentication.
- If a password reset flow is accessible and does **not enforce strict verification** (e.g., lacks email confirmation or token-based validation), it may allow an attacker to reset passwords for any user using only their email.
- Alternatively, if credentials are derived or loosely enforced (e.g., default passwords or `user_id`-based email/password logic), an attacker can **fully take over accounts at scale**.

## Impact: Full Account Takeover Across the Platform

Once emails are enumerated via the IDOR vulnerability, a malicious actor can:

- Log in as **any student user** by guessing, resetting, or exploiting a weak password scheme.
- Gain **persistent access** to the user’s private data and internal features.
- **Bypass all privacy and access controls** designed to isolate student data.

*This transforms the IDOR flaw from a simple information disclosure issue into a critical, system-wide account takeover vulnerability.*


## This Is the Most Severe Vulnerability Identified

- Combines **IDOR + Broken Authentication** to achieve **full user impersonation**
- Enables **horizontal privilege escalation** across all student accounts
- **Scalable** — can be automated via script to harvest and exploit user data platform-wide

## Urgent Remediation Actions Required

- Immediately **fix the IDOR** issue on the `/student/profile/{user_id}/edit` endpoint by enforcing **ownership checks**.
- Review and **harden authentication logic** to prevent email/ID-based account prediction or unauthorized resets.
- Implement **Multi-Factor Authentication (MFA)** and thoroughly audit all **password reset** and **login workflows**.
- Log and monitor for:
- Suspicious login attempts
- High-volume profile access
- Mass email enumeration activity

## Visual Reference

## 10. Impact

- Unauthorized access to **PII of all users**
- Enables **bulk data scraping** of thousands of users
- Can be used for:
- **Phishing attacks**
- **Identity theft**
- **Social engineering**
- **Credential stuffing**

## 11. Business Risk

This vulnerability directly threatens user privacy, organizational reputation, and regulatory compliance. If exploited, the exposure of student data can lead to:

- **Regulatory fines**
- **Reputational damage**
- **Breach notification requirements**
- **Loss of trust in the platform by students and stakeholders**

## 12. Suggested Remediation

1. Enforce strict **authorization checks** on all sensitive endpoints
2. Ensure users can only access their own profiles:

- Validate that `user_id` matches `session.user_id`

1. Replace sequential numeric IDs with **UUIDs** or opaque references
2. Implement **rate limiting**, **WAF**, and **CAPTCHA** to slow down automation
3. Log and alert on **abnormal access patterns**
4. Conduct regular **access control testing**

## 14. Tested Environment

- **Date of Testing:** August 1, 2025
- **User Role:** Authenticated student account
- **Tools Used:**
- Python 3.11
- httpx + BeautifulSoup
- Firefox 128.0
- Burp Suite
- Linux (Kali/Debian)

## 15. Additional Notes

- **CSRF tokens**, full HTML forms, and sensitive fields were exposed and could be submitted by a malicious actor, though not tested in this report.
- The vulnerability is scalable — full user base can be scraped with a basic script.
- No anti-bot, behavioral, or IP throttling mechanisms observed.

## 19. Conclusion

This report highlights a severe **Insecure Direct Object Reference (IDOR)** vulnerability affecting the `https://engcastleportal.com` student profile edit endpoint. The vulnerability allows any authenticated user to access and scrape sensitive personal information of all registered students, without authorization. This constitutes a direct violation of data privacy principles and introduces serious risks including mass data leakage, phishing, impersonation, and non-compliance with global privacy regulations such as GDPR and CCPA.

Immediate remediation is critical to protect users’ privacy and maintain trust. Proper authorization checks, use of non-predictable identifiers, and audit logging should be prioritized to prevent future exploitation.

## 20. Researcher Information

**Discovered and reported by: Mohammed Mogeab Ahmed Al-hajj**

Security Researcher | Ethical Hacker

You can reach me for follow-up, collaboration, or acknowledgments via:

- **X (formerly Twitter)**: [@MohammedMogeab](https://web.archive.org/web/20251107080912/https://x.com/MohammedMogeab)
- **GitHub**: [MohammedMogeab](https://web.archive.org/web/20251107080912/https://github.com/MohammedMogeab)
