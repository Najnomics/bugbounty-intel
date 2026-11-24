# Reflected XSS in BGMI

- **Source URL:** https://medium.com/@patil97/reflected-xss-in-bgmi-38ed48773981?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240107234751/https://medium.com/@patil97/reflected-xss-in-bgmi-38ed48773981
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4746 (id 4746)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
After PUBG Mobile was banned, it is making a comeback with a new name, BGMI. I visited the game’s website, and while randomly exploring the site, I looked at BGMI’s history tab and found URLs with different parameters. Luckily, one of the endpoint was a vulnerable to Reflected XSS.

Vulnerable URL: [https://www.battlegroundsmobileindia.com/news?p=](https://www.battlegroundsmobileindia.com/news?p=)

I just used simple Script XSS payload: [https://www.battlegroundsmobileindia.com/news?p=](https://www.battlegroundsmobileindia.com/news?p=)\</script>\<script>alert(1)\</script>

Now, the question is, where and how do you report it? Back then, I was a newbie (and still am). Unfortunately, Krafton, the company behind BGMI, didn’t have a Vulnerability Disclosure Policy. So, I reported the issue to their official email available on the same site, but I didn’t receive any response. After a few days, it was fixed, and I decided to make the POC public.
