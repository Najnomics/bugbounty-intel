# web cache deception on vdp program

- **Source URL:** https://medium.com/@Dorking1/web-cache-deception-on-private-program-eab62d869866?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250326185936/https://medium.com/@Dorking1/web-cache-deception-on-private-program-eab62d869866
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9174 (id 9174)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
hello everyone

we are back again with a new article. for those who dont’t know me, I’am dorking and i love the field of discovering vulnerablilities

so let’s give our target a name target.com

1. first, i logged in to the site.
2. then I went to the account

https://www.target.com/account

3\. I tried hello.php but to no avail

[https://www.target.com/accoun](https://www.target.com/account)t/hello.php

4\. I tried again, this time with hello.js and hello.json and the result was seccessful. the end stores personal information

[https://www.target.com/account/hello.js](https://www.target.com/account/hello.js)

https://www.target.com/account/hello.json

5.this way, the attacker will be able to stael the victim’s data when he opens the site

I hope you like this article.
