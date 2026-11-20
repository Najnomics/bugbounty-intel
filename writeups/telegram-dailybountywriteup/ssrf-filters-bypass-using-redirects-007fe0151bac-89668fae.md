# SSRF Filters Bypass Using Redirects

- **Source URL:** https://osintteam.blog/ssrf-filters-bypass-using-redirects-007fe0151bac
- **Fetched from:** https://osintteam.blog/feed
- **Fetched:** 2026-11-20
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14992 (id 14992)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Read [this](https://hackerone.com/reports/3383079) and [this](https://hackerone.com/reports/381129) report. What similarities do you see? Both are SSRF vulnerabilities. Both had filters in place that were bypassed using redirects.

In this article, I’ll try to showcase this to you with the help of a lab that I vibe coded. I’ll showcase the technique on how you can reproduce this on your own and what makes this vulnerable at the code level.

Consider a web-app containing a parameter such as url . The url parameter is user controlled. Therefore, you enter a domain that you control and eventually end up getting a DNS/HTTP hit.

While this is enough to report when performing a pentest, however, this might not get you anywhere when doing bug bounty, as there is not much impact to show. So, what we should aim for is impact.

What people end up doing is first scan the internal network for IPs and then for ports. Mostly, folks rely on scanning ports on 127.0.0.1 . While, we won’t be covering the scanning part here, it’s a good thing to know for interviews.

Let’s assume that we know there’s another app running on port 5001 . At this point, we can just start with sending a request to the ?url=http://127.0.0.1:5001 . But wait, we end up getting an error message.

With mature SDLC, security is now inbuilt in most of the web apps before they are actually deployed.

Consider the code snippet below. localhost, 127.0.0.1 and ::1 are blocked. At this point, we could also have tried 0.0.0.0 and it would have worked, but we’ll ignore it for now.

Call it a mistake or a feature, what often developers do is turn on redirects. Someone might have thought that instead of sending a request to https://google.com (HTTPS endpoint), the user might send a request to http://google.com (HTTP endpoint), and the target HTTP endpoint would just return a 301 or 302, thus breaking the functionality of the application.

So, what we’ll be doing is exploiting this behavior of the application. We’ll be using something that redirects to 127.0.0.1:5001 when a request is made to the endpoint.

You can self host an endpoint and write a piece of code that redirects to 127.0.0.1:5001 . You could also use ngrok and other open source tools for the same purpose. But then, it would be a bunch of over-head.

For this, we’ll be leveraging tinyurls. We’ll set the domain to http://127.0.0.1:5001/admin and use the tinyurl link to get around the filter.

Using the tinyurl link results in us getting around the filter and getting access to the internal endpoint.

What could be more interesting is internal portals often do not have authentication or authorization in place. Also, if there’s MTLs in place, you get directly authenticated as the request originated from the vulnerable application itself.

Hope you enjoyed reading the article. Please consider subscribing and clapping for the article.

In case you are interested in CTF/THM/HTB writeups consider visiting my [YouTube](https://www.youtube.com/channel/UCnL50top2JtcuFVNdjDHiiw/) channel.

[SSRF Filters Bypass Using Redirects](https://osintteam.blog/ssrf-filters-bypass-using-redirects-007fe0151bac) was originally published in [OSINT Team](https://osintteam.blog) on Medium, where people are continuing the conversation by highlighting and responding to this story.
