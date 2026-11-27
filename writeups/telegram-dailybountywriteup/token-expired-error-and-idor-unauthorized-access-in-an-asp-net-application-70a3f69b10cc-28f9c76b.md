# Token Expired Error and IDOR

- **Source URL:** https://hcibo.medium.com/token-expired-error-and-idor-unauthorized-access-in-an-asp-net-application-70a3f69b10cc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251020050441/https://hcibo.medium.com/token-expired-error-and-idor-unauthorized-access-in-an-asp-net-application-70a3f69b10cc
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11262 (id 11262)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **Token Expired Error and IDOR: Unauthorized Access in an ASP.NET Application**

Greetings to everyone from Châteldon…

— After a long time I was motivated to share a critical finding that excited me and to describe the process I followed during the time I discovered it. I hope sharing this vulnerability story will be useful to you as well.

As always, at the start of the week our project manager assigned tasks and set deadlines. Since I work in application security, I was given the web-based security testing scope at the beginning of the week.

First, I directly reviewed the scope and checked whether the provided URLs were functioning correctly. For this I used the scope review script I humbly developed: [https://github.com/HCIBO/Cyber-Security-IT/blob/main/scope\_review.py](https://github.com/HCIBO/Cyber-Security-IT/blob/main/scope_review.py.)


Then I selected one of the accessible targets and started the first sprint of the week. As I always do, I first identified which technology the application was built with. I discovered it was an “ASP” :) based website — something I will always dislike.

From that point on I integrated all my roadmap processes with the maddening Microsoft procedures, because ASP…
