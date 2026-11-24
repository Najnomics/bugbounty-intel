# My first P3 in bug crowd (cross site scripting ) xss

- **Source URL:** https://medium.com/@elsayedmohammed/my-first-p3-in-bug-crowd-cross-site-scripting-xss-1ed71773688?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230507222420/https://medium.com/@elsayedmohammed/my-first-p3-in-bug-crowd-cross-site-scripting-xss-1ed71773688
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2575 (id 2575)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# My first P3 in bug crowd (cross site scripting ) xss

Hi us ,

This is my first(P3) and last Bug Writeup this year. 😀

I am sharing with you my latest XSS finding.

- First i check if the search function can I write HTML code in it .

- I check if i can write payload but it is not work ..
- The specific endpoint had `url` a param that was vulnerable to Reflected XSS injection.

`target.com/Pages/search.aspx#k="><h1>test<h1>`
I try to write many payload but it is not work payload like :

**\<svg onload=alert(1)>**

**\<img src=x onerror=alert(1)>**

but try to write payload if i click or mouse over what is happen .

I try to write this payload but after i search about any thing .

`target.com/Pages/search.aspx#k=test"><img src=x onclick=alert("xss")>` it is work.
