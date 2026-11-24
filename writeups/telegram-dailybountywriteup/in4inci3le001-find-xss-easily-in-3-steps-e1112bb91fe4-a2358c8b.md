# Find XSS Easily in 3 steps

- **Source URL:** https://medium.com/@in4inci3le001/find-xss-easily-in-3-steps-e1112bb91fe4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250612144314/https://medium.com/@in4inci3le001/find-xss-easily-in-3-steps-e1112bb91fe4
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3035 (id 3035)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Find XSS Easily in 3 steps

Hello everyone and welcome back to the new write-up in this blog. I’m going to share with you some tips to easily find the reflective XSS bug in three steps, so let’s get started.

Let’s say I have a domain that is open to the public. Let’s call it example.com.

I visited this website and noticed a search option on multiple pages that were not on the navbar. So I was curious to check, and before getting blocked, let’s try HTML injection and see if it works.

sample payload \<h2>say hi\</h2>


and, as the above image shows, it works.

Let us now attempt injecting the script “>script>alert(“Say Hello”);/script>


and the result can be seen here

**Suggestions for consideration**

**\* Check for parameters  \* Do not directly enter any script tags; instead, start with HTML injection and then chain it to find other parameters.  \* Add the payloads together.**


That’s for now, I hope you enjoyed it and learned something today. see you back on another write-up until then happy hacking !
