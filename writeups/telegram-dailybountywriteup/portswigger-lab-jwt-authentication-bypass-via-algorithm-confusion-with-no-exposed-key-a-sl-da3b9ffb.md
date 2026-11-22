# Portswigger Lab

- **Source URL:** https://infosecwriteups.com/portswigger-lab-jwt-authentication-bypass-via-algorithm-confusion-with-no-exposed-key-a-slightly-e28602b6ef70?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221215121553/https://infosecwriteups.com/portswigger-lab-jwt-authentication-bypass-via-algorithm-confusion-with-no-exposed-key-a-slightly-e28602b6ef70
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1075 (id 1075)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Portswigger Lab: JWT authentication bypass via algorithm confusion with no exposed key, a slightly different walkthrough

## , or how I learned the importance of RTFM yet again

I mean, to be perfectly honest, this article started as a huge complaint in my head while I was working on solving [the lab in question](https://portswigger.net/web-security/jwt/algorithm-confusion/lab-jwt-authentication-bypass-via-algorithm-confusion-with-no-exposed-key), but in the end it turned out I was in the wrong. So, here’s a different walkthrough compared to the community walkthroughs under the solutions of this lab. And, if you consider yourself not as smart at times…
