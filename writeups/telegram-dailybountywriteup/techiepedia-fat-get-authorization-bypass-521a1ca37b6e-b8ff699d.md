# Fat GET Authorization Bypass

- **Source URL:** https://medium.com/techiepedia/fat-get-authorization-bypass-521a1ca37b6e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250505073146/https://medium.com/techiepedia/fat-get-authorization-bypass-521a1ca37b6e
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4572 (id 4572)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Fat GET Authorization Bypass

I was testing a SaaS web application that would generate reports with user data. There were several different reports for user roles and each client using the SaaS was also segregated from each other, as they should be.

Reports were generated with two-step process:

1. POST request with parameters to build the custom report, returns a report ID.

2. GET request with the report ID to download the server-generated PDF.

Attempting to access reports outside of your role or client space would result in a 403 error.

Just like everyone else in the world, I did try the bypass-403 tool to look for any quick bypasses.

No dice on low-hanging fruit.

I moved on to other places in the application and after some time came back to the reporting portion.

I had the POST request saved in my Burp Repeater and just manually built the GET request from the POST as I was too lazy to go capture the request naturally.
