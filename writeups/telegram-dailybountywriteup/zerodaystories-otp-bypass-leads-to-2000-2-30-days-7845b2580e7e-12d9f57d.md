# OTP Bypass Leads to $2000 (2/30 DAYS)

- **Source URL:** https://medium.com/@zerodaystories/otp-bypass-leads-to-2000-2-30-days-7845b2580e7e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250908112503/https://medium.com/@zerodaystories/otp-bypass-leads-to-2000-2-30-days-7845b2580e7e
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8340 (id 8340)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# OTP Bypass Leads to $2000 (2/30 DAYS)

## **Hi Bug Bounty Hunters!**

I’m a security researcher, and I’ve taken on the challenge of explaining one bug bounty report every day for the next 30 days — **30 days, 30 reports**!

Here’s the second one: OTP Bypass Allows Any Phone Number Takeover

## How a Researcher Found a Critical Bug in \*\*\*\*\*

A fellow researcher found a critical bug in the \*\*\*\*\* app, a popular ride-sharing service with millions of users. The issue was in the OTP (One-Time Password) verification process when updating phone numbers. Let’s dive into how it was discovered.

## The Bug: OTP Bypass in Phone Number Update

When users try to change their phone number, they should get a 4-digit OTP for verification. But here’s the flaw: the app accepts “0000” as a valid OTP, bypassing verification altogether.

Here’s how the bug was found:

1. Open \*\*\*\*\* app and go to account settings.
2. Choose to update your phone number.
3. Enter a new phone number.
4. When prompted for the OTP, enter “0000.”
5. Done! The phone number changes without verification.
