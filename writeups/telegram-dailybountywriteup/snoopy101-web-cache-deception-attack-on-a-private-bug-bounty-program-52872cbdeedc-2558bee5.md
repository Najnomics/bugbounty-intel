# Web Cache Deception Attack on a private bug bounty program

- **Source URL:** https://medium.com/@snoopy101/web-cache-deception-attack-on-a-private-bug-bounty-program-52872cbdeedc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260309085946/https://medium.com/@snoopy101/web-cache-deception-attack-on-a-private-bug-bounty-program-52872cbdeedc
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1866 (id 1866)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Web Cache Deception Attack on a private bug bounty program

**Hi incredible hackers!**

I’m about to tell you the story of one of the coolest bugs I’ve found on a private program which got duplicate, unfortunately.

I was like:

Anyway I love hacking and as one of my heroes says: “Bounty/money is just a bonus”

Back to the vulnerability.

Web Cache Deception:

The scope of the program is truly small which just contains the main website (www.target.tld) and the API subdomain (api.target.tld).

I was looking at my profile page on the main website and I refreshed the page and looked at my Burp’s history page and I realized that the profile information were shown on this API endpoint.

I looked at the response and that ‘**Server-Timing: cdn-cache; desc=MISS**’ caught my eyes.

Now I had to test for 2 beautiful bugs:

1. Cache Poisoning Attack
2. Cache Deception Attack

Although I literally tried everything, it seems that the website isn’t vulnerable to the first bug.

So I went for the second vulnerability and I put ‘.css’ at the end of the URL.

Damn! I was still able to see my information, so I checked the ‘**Server-Timing**’ response header, immediately.

So now I just needed to send [https://www.target.tld/api/users/WHATEVER/current/full.css](https://www.target.tld/api/users/WHATEVER/current/full.css) to the victim for cache to be hit and open the link on my own browser before the cache expired to see the victim’s information. **Pretty easy right?**

**Unfortunately no.** It wasn’t that easy and the cache was expired so fast that I couldn’t see the information. In order to exploit the vulnerability I had to find a way to send multiple requests to the endpoint from victim’s behalf.

## The scenario

1. The victim visits hacker’s website
2. The hacker’s website sends several requests to the [https://www.target.tld/api/users/WHATEVER/current/full.css](https://www.target.tld/api/users/WHATEVER/current/full.css) in order to poison the cache.
3. The hacker opens the link on his browser and the victim’s information is shown.

## PoC:

*Note that the Chrome browser is the victim and the Firefox browser is the hacker:*
