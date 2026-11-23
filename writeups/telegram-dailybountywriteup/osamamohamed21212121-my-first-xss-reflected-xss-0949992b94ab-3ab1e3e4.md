# My first XSS

- **Source URL:** https://medium.com/@osamamohamed21212121/my-first-xss-reflected-xss-0949992b94ab?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250716122752/https://medium.com/@osamamohamed21212121/my-first-xss-reflected-xss-0949992b94ab
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7246 (id 7246)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# My first XSS: Reflected XSS

Hi, welcome back to another blog. In this blog, we’re going to know how I found my first XSS in the extrnal program. So, before starting, if you haven’t followed our medium account, do follow, guys. So without wasting time let’s get into the story of the XSS.

During testing, I tried to find an XSS vulnerability in each input, but nothing worked every time I tried. I completely lost hope in finding this vulnerability. However, after taking some time off, I returned and remembered that I can also inject XSS into the URL path of the website.”

BOOOOOOOOOOM :)

# Reflected XSS

`https://example.com/dashboard.php?user_id=111111`

I removed `?user_id=111111`

so the final form became like this

[https://example.com/dashborad.php/z%22%3E%3Cscript%3Ealert(%22osam\a\_mohamed%22)%3C/script%3E](<https://example.com/dashborad.php/z%22%3E%3Cscript%3Ealert(%22osam\\a_mohamed%22)%3C/script%3E>)


Done 

Thank you for watching.

“Don’t hesitate if you have any questions about anything.

I will leave my account for contact.

Follow me.”

*LinkedIn Profile :* 

[https://www.linkedin.com/in/osama-mohamed-b788b12b1/](https://www.linkedin.com/in/osama-mohamed-b788b12b1/)
