# IDOR — How I Leaked Data of 50k+ Users

- **Source URL:** https://medium.com/@YourFinalSin/idor-how-i-leaked-data-of-50k-users-bc44201e777a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250829003045/https://medium.com/@YourFinalSin/idor-how-i-leaked-data-of-50k-users-bc44201e777a
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6934 (id 6934)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR — How I was able to access PII of 50k+ Users

Hello everyone,

this is my first post ever on Medium, so the writing quality is probably going to improve in the next posts.

Let’s start.

The program I discovered an IDOR on is a public ecommerce type website with around 60k to 100k visitors a month and around 50k registered users. On programs like this, I usually start understanding how the application works and don’t bother about automated scanning.

So I registered an account on the application and started hacking.

First thing I wanted to find out how access control was implemented and how the application ties a session and it’s data to a specific account. So I checked all the requests in Burp and found an interesting endpoint /GetProfiledetails that displayed all the PII data of my account. There was also a cookie that was base64 encoded. Here is the full request and response

Decoding the base64 cookie answered my earlier question how access control was implemented. Every user account was identified mit it’s user ID and some other things over this base64 encoded cookie. See for yourself:

Now it was time to change that user ID to something like ‘509070’, base64 encode everything again and send the request. The request was processed by the server and I got access to the PII of another account! Brute forcing this user ID parameter showed I had access to about 50k users PII.

Here is a full PoC video of the IDOR:

I reported it and it was successfully triaged — Thank you for reading.
