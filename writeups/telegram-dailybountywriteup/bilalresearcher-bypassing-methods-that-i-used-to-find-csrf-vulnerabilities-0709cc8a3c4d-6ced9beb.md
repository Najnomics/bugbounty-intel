# Bypassing methods that I used to find CSRF vulnerabilities

- **Source URL:** https://medium.com/@bilalresearcher/bypassing-methods-that-i-used-to-find-csrf-vulnerabilities-0709cc8a3c4d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240829023228/https://medium.com/@bilalresearcher/bypassing-methods-that-i-used-to-find-csrf-vulnerabilities-0709cc8a3c4d
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7065 (id 7065)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bypassing methods that I used to find CSRF vulnerabilities

Hello folks,

This blog will expose some bypassing methods that I used to find CSRF vulnerabilities. Don’t use this informations for illegal purposes. Be Ethical!

Many frameworks have CSRF tokens built in, so often you can simply use your framework implementations. Besides Implementing CSRF tokens to ensure the authenticity of requests, another way of protecting against CSRF is with the SameSite cookies.

The Set-Cookie header allows you to use several optional flags to protect your user’s cookies, one of which is the SameSite flag. When the SameSite flag on a cookie is set to Strict, the client’s browser won’t send the cookie during cross-site requests:

*Set-Cookie: PHPSESSID=xxxxxxxxxx; Max-Age:86000; Secure; HttpOnly; SameSite=Strict.*


Using CSRF token in the header, Set Cookie flags, and Set Same-Origin, are used for preventing third-party site interactions related to vulnerabilities like CSRF, CORS and ClickJacking.

CSRF is very tough to find in current web technologies. Many security measures have been taken by companies to prevent CSRF attacks. Tradition CSRF not going to work nowadays. So CSRF is dead? nah. We have to know how to bypass the security measures that companies have. Let’s get into the bypassing methods.
