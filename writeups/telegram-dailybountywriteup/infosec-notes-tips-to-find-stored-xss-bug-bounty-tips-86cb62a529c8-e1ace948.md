# Tips to find Stored XSS [Bug_Bounty_Tips]

- **Source URL:** https://medium.com/infosec-notes/tips-to-find-stored-xss-bug-bounty-tips-86cb62a529c8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250114130914/https://medium.com/infosec-notes/tips-to-find-stored-xss-bug-bounty-tips-86cb62a529c8?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8478 (id 8478)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Tips to find Stored XSS \[Bug\_Bounty\_Tips\]

## Intro

Hi Bug Bounty hunter , Welcome back to my another article. Today I would like to share some simple and quick ways to find stored XSS vulnerability as well as I provide some ***HackerOne*** reports that help you to find Store Cross site scripting. In the end I mentioned trick to find Stored XSS

Stored Cross site scripting occurs when an application receives user-input data and save it that data comes with http response of application and renders on the page. For example, one blog page contains comment section where user comment below the post and that comments are rendered on the page. What if Instead of normal comment we try to inject \<script>alert(document.domain)\</script> javascript payload if this comment section is vulnerable then it will executed. so there is a stored XSS vulnerability.

Lets take a some references of stored Cross site Scripting


## *Report :* [*#485748*](https://web.archive.org/web/20250114130914/https://hackerone.com/reports/485748)

# $700 Bounty for Stored XSS Report

This vulnerability found in Reports section. Where user create and submit network reports. when we create and submit this report in , it renders on the page.

Now try to exploit this :

During making reports he entered this payload

`"><img src=x onerror=alert(document.domain)>`
