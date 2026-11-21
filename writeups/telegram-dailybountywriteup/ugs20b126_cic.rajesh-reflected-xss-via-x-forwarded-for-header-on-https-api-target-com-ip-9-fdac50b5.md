# reflected xss via x forwarded for header on https api target com ip 96642a4a49ed

- **Source URL:** https://medium.com/@ugs20b126_cic.rajesh/reflected-xss-via-x-forwarded-for-header-on-https-api-target-com-ip-96642a4a49ed?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250716122103/https://medium.com/@ugs20b126_cic.rajesh/reflected-xss-via-x-forwarded-for-header-on-https-api-target-com-ip-96642a4a49ed
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9210 (id 9210)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS via X-Forwarded-For Header on [https://api.target.com/ip](https://api.target.com/ip)

Hi, Today I will discuss about how I found this bug in a target. A clean and simple one.

Yesterday night I did fuzzing on [https://api.target.com](https://api.target.com), and found a endpoint called /ip, which was returning my ip address. I strongly fixed that I should find some bug at this endpoint. So I checked for cors misconfiguration, but didn’t found any. So I left it, for that day.

So today I again came with a mindset that, I should find some bug at this endpoint. So this is the method I followed.

I captured that request and sent it to intruder. ( burp shortcut, **ctrl+I** and later **ctrl+shift+I** ). Here I right clicked and did active scan.

I got this result.

So now I started tinkering with the **X-Forwarded-For** header and I observed that, what ever I enter, it was reflecting in the response as it is. So without wasting my time and energy I did this. I sent this request containing X-Forwarded-For header and added this value as insertion point. Now right click → Scan defined insertion point → open scan launcher.

See the below image for better understanding.

And after few minutes I got this, Reflected XSS.

**Takeaways**: Learning Burpsuite is very very important. Burpsuite is really a great tool. You should try to master it.

Anyways I forgot to mention, here I was using some custom configuration scan profiles. You can learn from here [https://mrrootsec.vercel.app/blog/burpsuite-custom-scan-profiles](https://mrrootsec.vercel.app/blog/burpsuite-custom-scan-profiles). Shout out to [Saqlain bro](https://x.com/_mohd_saqlain) for the article.

I hope you learned something. Bye !!!

Similar H1 Disclosed reports: 

[https://hackerone.com/reports/882220](https://hackerone.com/reports/882220)

[https://hackerone.com/reports/1392935](https://hackerone.com/reports/1392935)

[https://hackerone.com/reports/297203](https://hackerone.com/reports/297203)

#bugbounty
