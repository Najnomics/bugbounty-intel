# How I accessed WAF Bypass for Stored XSS Smart Idea

- **Source URL:** https://medium.com/@yossefmohamedsalah2001/how-i-accessed-waf-bypass-for-stored-xss-smart-idea-708082fcfa79?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250730052143/https://medium.com/@yossefmohamedsalah2001/how-i-accessed-waf-bypass-for-stored-xss-smart-idea-708082fcfa79?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10351 (id 10351)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I accessed WAF Bypass for Stored XSS Smart Idea 💡

Stored XSS vulnerabilities can earn you **$500 to $7500** in bug bounty programs, depending on the scope and impact.

But WAFs (Web Application Firewalls) often stand in your way…

**💡 The Trick: Confuse the WAF**

Many WAFs rely on parsing headers and interpreting content type to determine if an incoming request is malicious. You can sometimes **bypass these protections** with a straightforward trick:

Add a custom or malformed Content-Type header to your request:

Content-Type: any\_random\_text’

This might:

- Trick the WAF into ignoring payload analysis.
- Allow your XSS payload to reach the backend.
- Store it in the application.
- Trigger it later on a victim’s browser.

# 🔥 Real Example

Let’s say your payload gets blocked:

`<script>alert('XSS')</script>`
You can bypass it by:

1. Sending it as part of a POST request.
2. Adding a misleading header:

`Content-Type: text/plain'`
Or by encoding:

`<img src=x onerror=eval(atob('YWxlcnQoJ1hTUycp'))>`
# 🔍 Why This Works

Some WAFs only scan payloads when the `Content-Type` is set to known values like `application/json` or `application/x-www-form-urlencoded`. If you alter the header:

- The WAF may **skip or mishandle the parsing**.
- But the backend application **still processes** the request.

# When It Works

✅ Works on:

- Poorly configured WAFs
- Homegrown WAF solutions
- Legacy or unpatched rulesets

❌ Won’t work on:

- Advanced behavior-based firewalls
- Solutions with content inspection at deeper layers
- Modern ML/AI-based detection

# **Summary ✨**

# 🛡️ WAF Bypass via Custom `Content-Type` Header for Stored XSS Payloads 💥

# 🎯 Target: Bypass WAF to Trigger Stored XSS

Web Application Firewalls (WAFs) are designed to block malicious input, including common XSS payloads. But with clever tricks, you can **slip payloads past WAF filters**, especially **Stored XSS**, which is highly rewarding in bug bounty programs.

One powerful yet simple bypass method involves **modifying the Content-Type header** of your HTTP request.
