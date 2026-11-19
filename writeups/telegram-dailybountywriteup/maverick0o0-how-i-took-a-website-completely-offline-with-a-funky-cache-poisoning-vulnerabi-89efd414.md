# How I Took a Website Completely Offline with a Funky Cache Poisoning Vulnerability (CPDOS)

- **Source URL:** https://medium.com/@Maverick0o0/how-i-took-a-website-completely-offline-with-a-funky-cache-poisoning-vulnerability-cpdos-220ac75d1cf3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905100246/https://medium.com/@Maverick0o0/how-i-took-a-website-completely-offline-with-a-funky-cache-poisoning-vulnerability-cpdos-220ac75d1cf3
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10042 (id 10042)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Took a Website Completely Offline with a Funky Cache Poisoning Vulnerability (CPDOS)

Hey everyone, Erfan here! In this write-up, I want to share a fun story about a cache poisoning vulnerability I found that led to a full-blown Denial of Service, knocking the entire site offline for all users.

If you want to get a deeper understanding of the mechanics behind this type of attack, I highly recommend checking out [**Zhero’s research**](https://zhero-web-sec.github.io/research-and-things/). It’s a goldmine of information.

### First Look: A Hardened Target

Let’s call our target `Target.com`. It was a private bug bounty, and it was clear that all the "low-hanging fruits" (the easy, common bugs) had already been picked. This meant I had to dig deeper and really get into the nitty-gritty details of the application.

I quickly noticed that the site was built on **Next.js** and was sitting behind a **CDN**. While poking around, I saw that certain paths and assets were being cached, like `/assets/images/` and a few high-traffic pages like the Home and Login pages. My first thought was to try for some classic Cache Deception to leak sensitive info, but I hit a dead end. Nothing seemed to work.

*A quick side note: Reading research and write-ups is great, but it’s useless if you don’t apply it in the real world. It’s like watching hours of swimming tutorials. You won’t actually learn to swim until you jump in the water.*


The CDN had some specific rules for caching content:

1. It cached specific paths, like `target.com/assets/images/anything`.
2. It cached popular pages (like `/login` and `/`) **but only if the response had a** **200 OK**
 **status code.**

### The “Aha!” Moment: Abusing a Next.js Header

This is where things got interesting. I started thinking about Next.js-specific headers and if I could use one to manipulate the response from the server.

A normal request to the login page would return the full HTML page, as you’d expect:

But, after some digging, I found a special header: **x-middleware-prefetch**. When I added this header to my request, the server’s response completely changed:

As you can see, instead of a login page, I just got back an empty JSON object (`{}`). The page was completely blank!

Here’s a **critical detail** that many researchers might miss, and it’s the key to the whole exploit: This trick **only worked over HTTP/1.1**. If I sent the same request with the `x-middleware-prefetch` header over HTTP/2, the login page loaded just fine. But with HTTP/1.1, I got the broken, empty response.


### The Exploit (Attempt #1)… and Failure

Okay, so the plan seemed simple now:

- Send a request to `/login` using HTTP/1.1.
- Add the `x-middleware-prefetch` header.
- The server responds with a `200 OK` and a blank page (`{}`).
- The CDN sees the `200 OK` and caches this broken response for everyone.
- **BOOM!** Site down.

…Except it didn’t work. The exploit failed. But why?

### The Plot Twist: It’s All in the Cookies

After a bit more digging, I realized that whenever I visited the site, the server set three cookies with seemingly random values:

```
Set-Cookie: CRSUG=bD79weyeCrs;
Set-Cookie: SUG=bD79weyeeUG;
Set-Cookie: BISUG=bD79weBeCrs;
```
This was the problem. The CDN wasn’t just caching one version of the login page; it was creating different cached versions based on the user’s cookies. This means my poisoned page was only cached for users who had the *exact same* cookie values as me. Since every new user got a new “random” set of cookies, my attack was useless against them.

### Digging Deeper: “Random” Isn’t Always Random

It was time to figure out just how “random” these cookies really were. I sent the initial request (the one that sets the cookies) over to **Burp Suite’s Sequencer** to analyze the values. And that’s when I found the final piece of the puzzle.

The cookie values weren’t random at all! They were being picked from a very small, predictable list.

- `SUG` cookie only ever had one of these **3** values: `['bD79weyeeUG', 'cIn9JugaP45', 'aT7dbxRwPwT']`
- `CRSUG`cookie only ever had one of these **2** values: `['aT7dbxRwCrs', 'bD79weyeCrs']`
- `BISUG` cookie only ever had one of these **2** values: `['aT7dbxBwCrs', 'bD79weBeCrs']`

This was the breakthrough! A new user visiting the site wouldn’t get a truly random cookie. They would be assigned one of a limited number of combinations.

A little bit of simple math tells us the total number of unique cookie combinations: `3 (SUG values) * 2 (CRSUG values) * 2 (BISUG values) = 12 possible combinations.`

So, any user visiting the site would have one of only **12 possible cookie sets**.

### The Final Exploit: Poisoning All 12 Caches

Now, the path to a full Denial of Service was crystal clear. If I could poison the cache for all 12 of those cookie combinations, then *every single new user* who visited the site would be served the broken page.

All I had to do was write a simple Python script that:

- Iterated through all 12 unique cookie combinations.
- For each combination, sent a request to the `/login` page.
- Included the `x-middleware-prefetch` header in each request and used HTTP/1.1.

The script ran, poisoning the cache for all 12 user “groups.” And just like that, any user trying to visit `Target.com` was greeted with a blank `{}` page. The site was effectively offline for everyone.

Perfect conclusion. Here it is, translated into the same friendly and encouraging tone for your write-up:

### Final Thoughts & Takeaway

Always try to apply the research and write-ups you read to real-world targets. If you hit what looks like a dead end, don’t give up immediately. What seems like a roadblock at first might just be a puzzle waiting to be solved. And remember, as we saw with the cookies in this case: **“Random” isn’t always random.** Keep digging!
