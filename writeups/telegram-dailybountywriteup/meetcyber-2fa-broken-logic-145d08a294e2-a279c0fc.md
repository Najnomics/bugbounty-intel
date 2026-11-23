# 2FA Broken Logic

- **Source URL:** https://medium.com/meetcyber/2fa-broken-logic-145d08a294e2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251206140738/https://medium.com/meetcyber/2fa-broken-logic-145d08a294e2
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11705 (id 11705)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# 2FA Broken Logic

## **How a Simple Cookie Value Can Break 2FA**

**Disclaimer:**

The techniques described in this document are intended solely for ethical use and educational purposes. Unauthorized use of these methods outside approved environments is strictly prohibited, as it is illegal, unethical, and may lead to severe consequences.

It is crucial to act responsibly, comply with all applicable laws, and adhere to established ethical guidelines. Any activity that exploits security vulnerabilities or compromises the safety, privacy, or integrity of others is strictly forbidden.


## Table of Contents

## Summary of the Vulnerability

The lab demonstrates how a poorly designed two-factor authentication flow can be undermined by a single flaw in session handling.

After a user logs in with a valid username and password, the application sends a 2FA code to their email and stores a **verify=\<username>**
