# How My Very First Bug Bounty Finding Leaked 12,000+ Enterprise Product Records

- **Source URL:** https://medium.com/@0zidmaaz/how-my-very-first-bug-bounty-finding-leaked-12-000-enterprise-product-records-18e1e4d93cdd
- **Fetched from:** https://medium.com/@0zidmaaz/how-my-very-first-bug-bounty-finding-leaked-12-000-enterprise-product-records-18e1e4d93cdd?source=rss-bebf50ad9b53------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14899 (id 14899)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Zidmaaz / Sat, 05 Sep 2026 18:36:15 GMT

How My Very First Bug Bounty Finding ***Leaked 12,000+*** Enterprise Product Records

Every bug bounty hunter remembers their first real finding. That nervous excitement when you send a payload, followed by the heart-pounding realization: “Wait, did that actually just work?”

This is the story of how a quick late-night recon session on a random target led me to discover a critical flaw (CWE-862) exposing full Read and Write access to over 12,000 enterprise product records across 5 countries.

Here is how I stumbled into it, proved the impact responsibly, and earned my very first bounty.

The “Maintenance Mode” Illusion

It all started on a quiet evening while I was enumerating subdomains for a target program. I came across a domain-let’s call it content-craft.redacted-target.com.

When I loaded the page in my browser, I was greeted by a sleek, generic landing page: “***Site Under Maintenance***.”

Normally, a beginner might close the tab and move on. But a core rule of bug bounty is to never trust what the frontend tells you. Web pages might be under maintenance, but underlying backend APIs are often wide open, running silently in the background.

I popped open my browser developer tools and intercepted a few requests. The application was running on Laravel, and more importantly, the backend API endpoints were completely active.

The “Wait, What?” Moment

While testing standard authentication workflows, I tried hitting their registration endpoint (***/api/register***).

Usually, modern applications demand email verification, a CAPTCHA, or an invite code. I fired off a simple curl request to create a test account, half expecting it to fail:

Bash

curl -X POST -H “Content-Type: application/json” \

-d ‘{“name”:”Test User”,”email”:”[mytest@example.com](mailto:mytest@example.com)”,”password”:”RedactedPass123!”,”c\_password”:”RedactedPass123!”}’ \

“[https://content-craft.redacted-target.com/api/register](https://content-craft.redacted-target.com/api/register)"

**To my surprise**, the server immediately responded with a **200** OK status and handed me a shiny valid Bearer Token:

JSON

{

“success”: true,

“data”: {

“token”: “REDACTED\_BEARER\_TOKEN”,

“name”: “Test User”

},

“message”: “User registered successfully”

}

No email verification. No admin approval. Just a brand-new, valid authentication token created in less than two seconds.

Digging Deeper: Reading 12,000+ Records

Having a token was great, but I needed to see what an authenticated “regular” user could actually do. I attached the bearer token to a GET request aimed at their internal product catalog endpoint:

Bash

curl -H “Authorization: Bearer REDACTED\_BEARER\_TOKEN” \

-H “Accept: application/json” \

“[https://content-craft.redacted-target.com/api/products](https://content-craft.redacted-target.com/api/products)"

The response screen lit up with JSON data. Product titles, vendor part numbers, localized specs in Danish, Swedish, English, Finnish, and Norwegian-it was all right there.

I noticed the API was paginated, returning 50 items per page. I pushed the page parameter to see how far the rabbit hole went:

Bash

curl -H “Authorization: Bearer REDACTED\_BEARER\_TOKEN” \

“[https://content-craft.redacted-target.com/api/products?page=244](https://content-craft.redacted-target.com/api/products?page=244)"

Page 244 returned the final 35 items. Doing quick math: 243 pages × 50 items + 35 = 12,185 products. An arbitrary user on the internet had just gained total visibility over their entire enterprise inventory catalog.

Testing the Integrity (The Risk of Mass Destruction)

Reading data was bad enough, but could a standard user modify or delete records?

To prove business impact without breaking anything, I selected a single test product ID and sent a minor PUT update request to change its title to “SECURITY-RESEARCH-TEST”.

Bash

curl -X PUT \

-H “Authorization: Bearer REDACTED\_BEARER\_TOKEN” \

-H “Content-Type: application/json” \

-d ‘{“name”:”SECURITY-RESEARCH-TEST”}’ \

“[https://content-craft.redacted-target.com/api/products/\[REDACTED\_ID](https://content-craft.redacted-target.com/api/products/[REDACTED_ID)\]"

The response came back instantly: “message”: “Product updated successfully”.

My heart skipped a beat. A malicious actor could easily write a simple script to overwrite or wipe all 12,000+ records in a matter of minutes, completely sabotaging the platform’s product management pipeline.

(And yes, I immediately sent another PUT request to revert the title back to its original state right after taking my screenshot!)
