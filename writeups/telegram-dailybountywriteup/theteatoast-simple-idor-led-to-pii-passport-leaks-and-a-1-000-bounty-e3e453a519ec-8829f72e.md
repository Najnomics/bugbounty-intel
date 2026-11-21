# Simple IDOR Led to PII & Passport Leaks (and a $1,000 Bounty)

- **Source URL:** https://medium.com/@theteatoast/simple-idor-led-to-pii-passport-leaks-and-a-1-000-bounty-e3e453a519ec?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250927043605/https://medium.com/@theteatoast/simple-idor-led-to-pii-passport-leaks-and-a-1-000-bounty-e3e453a519ec
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10904 (id 10904)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Simple IDOR Led to PII & Passport Leaks (and a $1,000 Bounty)

Hey folks, as a bug hunter, I stumbled on this cool IDOR vuln on a private target. It let me peek at other users’ personal info without permission. Reported it through YesWeHack, got fixed, and scored $1,000. Here’s the quick story.

## What’s IDOR Anyway?

IDOR occurs when an application exposes direct references to objects, such as IDs in URLs, without proper authorization. In this case, it disclosed names, emails, phone numbers, addresses, account numbers, and documents like passports and bank statements.

## How I Found It

I logged in, navigated to an endpoint to start a subscription, and captured the GET request using Burp Suite. By adding the ID in the path (e.g., /blah\_blah/\[ID\]) of another user’s, I could access their data. This also enabled viewing and downloading sensitive files.

## The Impact

It exposed PII including banking details and passports for approximately 900 users, potentially leading to identity theft or fraud. The CVSS score was high (8.8), requiring an authenticated account to exploit.

## Takeaway

Sometimes the biggest impact comes from the simplest issues. This wasn’t a complex or flashy finding — I just happened to be in the right place at the right time, and it turned into a critical bug with serious consequences.

Thanks YesWeHack for the smooth ride. Bounty hunting keeps the web safer — try it!
