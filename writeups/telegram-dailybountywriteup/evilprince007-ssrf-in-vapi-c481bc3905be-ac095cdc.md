# SSRF in vAPI

- **Source URL:** https://medium.com/@evilprince007/ssrf-in-vapi-c481bc3905be?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142540/https://medium.com/@evilprince007/ssrf-in-vapi-c481bc3905be
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2482 (id 2482)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SSRF in vAPI

In this article, we are going to look at an easy but very critical and highly exploitable attack vector on API, which is Server Side Request Forgery (SSRF).

As usual assuming that the project (vAPI, Burpsuite, Postman) is installed and configured properly and everything is in good shape to start with.

- Definition:

In this attack, the target server is deceived into sending a resource request to either the attacker’s server or to DNS controlled by the attacker. This vulnerability has a significant impact and has its own category in the OWASP Top 10.

- Understanding the Scenario

**Enumeration** is the first step in successful hunting, so begin your hunt by discovering some probable API requests in vAPI, thus from the vapi home page, we didn’t find anything suspicious, but when we checked in postman, we discovered that there are some hidden API’s as well inside endpoint Arena.

So, after a little bit of exploring we actually found one useful request inside *ServerSurfer >> GetData* which might bevulnerable to SSRF.

- Attacking:

So, for confirmation, we tried substituting the initial resource request with a **loopback address** (127.0.0.1), but it did not succeed, indicating that it is not vulnerable to **loopback-ssrf**.

Then we tried substituting the address with simply google.com, and it worked, indicating that it is subject to SSRF and that we can see resources from google.com in response, indicating that it is vulnerable to **in-band** SSRF.

Mass Assignment in vAPI 

[https://medium.com/@evilprince007/mass-assignment-in-vapi-d1ff12340021](/@evilprince007/mass-assignment-in-vapi-d1ff12340021)
