# Broken Authentication & 2FA Bybass ‘Business logic Error’

- **Source URL:** https://medium.com/@ghostxzx/broken-authentication-2fa-bybass-business-logic-error-ba24ee03a0d7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260519131328/https://medium.com/@ghostxzx/broken-authentication-2fa-bybass-business-logic-error-ba24ee03a0d7
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13467 (id 13467)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Broken Authentication & 2FA Bybass ‘Business logic Error’

Hi Hunter this is *mohammed yassin* ‘Ghostxz’ Again, Back with Bug in authentication flow let to business logic failure, 

The bug is sample but the impact can be high.

What The Bug? 

A brief explanation of the vulnerability: The vulnerability is classified as a Business Logic Error, and here the vulnerability allows modification to the account or access to it without authentication and bypassing two-factor authentication also.

How I Discover It? 

I did a little trick, I just changed the name in my profile and then picked up the request with Burp Suite, and then I enabled two-factor authentication and also logged out,

and then I sent the request that I had saved and the change in the profile actually worked without me being logged in on the site,

and even the two-factor authentication did not do its required job!

11111111111111111111111111111111111111111111111111111111111

ANd thats all ,thanks for reading 111111111111111111111
