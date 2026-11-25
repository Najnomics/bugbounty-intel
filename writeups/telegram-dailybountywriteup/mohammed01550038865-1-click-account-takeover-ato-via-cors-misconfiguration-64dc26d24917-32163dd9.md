# 1-Click Account Takeover (ATO) via CORS Misconfiguration

- **Source URL:** https://medium.com/@mohammed01550038865/1-click-account-takeover-ato-via-cors-misconfiguration-64dc26d24917?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251007104057/https://medium.com/@mohammed01550038865/1-click-account-takeover-ato-via-cors-misconfiguration-64dc26d24917?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8130 (id 8130)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **1-Click Account Takeover (ATO) via CORS Misconfiguration**

Hello All, 

*Today, I will share an important write-up I found on a private bug bounty on Bugcrowd.  I will refer to my victim target as mytarget.com*.


**Initial Discovery:**

*While testing, I navigated to the login page and noticed a redirect to the following endpoint:*

`https://mytarget.com/sign-in?callbackUrl=//mytarget.com`
*Anyone observing this endpoint might think to test for an open redirect vulnerability. I did exactly that.*

**Open Redirect:**

*I tested using the following payload:*

`https://mytarget.com/sign-in?callbackUrl=////////evil.com`
*After logging in, I was redirected to \`evil.com\`. This confirmed the open redirect vulnerability, which is generally categorized as P4 (low impact).*

**Escalating to Reflected XSS:**

*After that, I thought if it was possible to escalate it to XSS. I started testing with this basic payload:*

*https://myterget.com/sign-in?callbackUrl=javascript:alert(1)//*
*and it worked! I could see*

*alert(1)*
*. Now, this is*

***RXSS P3 (medium impact)***

*.*

**Escalating Further to P2:**

*I thought about how to escalate this to P2. I started looking at the Burp history and began fuzzing. After 30 minutes, I found this endpoint: /api/auth/session. When I visited it, I saw that it includes the access token of the current user. Now I thought,* 

***Can I use CORS***…
