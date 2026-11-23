# Bypassing 2FA to Impersonate Users on Drugs.com

- **Source URL:** https://medium.com/@regan_temudo/bypassing-2fa-to-impersonate-users-on-drugs-com-66fb84b0491d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250513114036/https://medium.com/@regan_temudo/bypassing-2fa-to-impersonate-users-on-drugs-com-66fb84b0491d
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9078 (id 9078)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Bypassing 2FA to Impersonate Users on Drugs.com

2 min readMar 16, 2025

# Introduction

Hey Security Enthusiasts!

A serious authentication flaw was recently discovered on Drugs.com, allowing attackers to bypass Two-Factor Authentication (2FA) and impersonate legitimate users. This vulnerability exposed user accounts to takeover risks due to improper session handling and weak email verification.

# What Happened?

During security testing, researcher [(duk3\_](https://hackerone.com/duk3_?type=user)) found that Drugs.com did not properly verify email ownership during account changes. This enabled an attacker to hijack accounts without requiring 2FA re-authentication.

# Steps to ReproduceRegister an Account:

1. **Register an Account**

- Sign up on Drugs.com with an attacker-controlled email.
- Complete OTP verification and select “Trust this device for 1 month.”

**2. Change Email to Victim’s Email**

- Navigate to Account Details.
- Change the registered email to the victim’s email.
- Since the attacker’s session remains…
