# XSS on The MOST Popular Movie Ticket website.

- **Source URL:** https://medium.com/@tarang.parmar/xss-on-most-popular-entertaining-website-2fbf5a88df0f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20261011053813/https://medium.com/@tarang.parmar/xss-on-most-popular-entertaining-website-2fbf5a88df0f
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1738 (id 1738)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# WAF Bypass + XSS on The MOST Popular Movie Ticket website.

Hi all,

This is the first time I was writing this blog, so I will let you know the story of how I got the XSS on one of the popular entertaining websites.

so here is how to begin,

I just start my normal day and from social media from one of my friends I came to know that REDACTED.com is giving some free credit points when you find vulnerability on it and that you can use to purchase movie tickets, popcorn for the special one 😉, etc etc.

so I simply open the website and tried to look for vulnerable points, but after looking for 2 hours I was not able to get any of those, then…

I found one option for a DONATION campaign,

I thought let’s try it out here, so I logged in and try to donate 1 RS (INR) on the website, first, I thought let’s try it out.

Step 1: try to understand how the application is processing the request and how it’s serving the response. basically, the application takes the amount and asks you to pay it using Paytm and once the payment is done it will redirect you to the main website simple 🙂.

Step 2: try to inject payload in the values like name, email, refcode, bankid, POSTURL, etc.

Step 3: I tried everything but nothing works, but but but …

instead of modifying the request from the Main website to paytm I changed my approach and start modifying the request which is coming from paytm to the main website, and I got one request which had a parameter “**strException**” which I was able to inject the ***“>*** in it without getting encoded in the response.

so i start with the Master payload \<script>Alert(1)\</script>, and it got **BLOCKED BY CLOUDFLARE**.😐 “NICEEEEEEEEEE !!!”

## Get Tarang Parmar’s stories in your inbox

Join Medium for free to get updates from this writer.

so I start searching all the different types of payloads on Google for available bypass for Cloudflare and guess what Cloudflare is also doing the same 🥲, mostly possible payloads are already patched/Blocked.

so I moved to our website [https://bugbountytip.tech](https://bugbountytip.tech) , and start searching “Cloudflare bypass” and it gives me this… “NOICE”

so i took this : **\<svg onload=alert("1")>**


I thought this also get blocked as usual, but it was bypassed in the waf and I was able to inject without any blockage I thought might be it will not work as it looks (but it was a VALID payload), now the fun part now you need to balance it with the request so by changing the payload: (**somebody: but How ?**)

Request Code: \<input type=”hidden” name=”strException” value=”**\<Value>**”>


first I try to apply the value directly in the code andddddd

Modified Code: \<input type=”hidden” name=”strException” value=”\<svg onload=alert("1")>”>


and it didn’t work. 🤔, so I changed a little bit more..

Modified Code: \<input type=”hidden” name=”strException” value=”**”>**\<svg onload=alert("1")>**\<”**”>


now, I add “> in the beginning and “\< at the end which separate the code from the code and it FINALLY WORKS !!🤩

lesson learned: never lose hope 😉
