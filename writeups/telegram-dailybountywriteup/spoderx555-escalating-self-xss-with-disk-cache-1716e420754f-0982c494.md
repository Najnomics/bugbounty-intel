# Escalating Self-XSS with Disk Cache

- **Source URL:** https://medium.com/@spoderx555/escalating-self-xss-with-disk-cache-1716e420754f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260505195732/https://medium.com/@spoderx555/escalating-self-xss-with-disk-cache-1716e420754f
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13482 (id 13482)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Escalating Self-XSS with Disk Cache

Hello everyone! I’m here to share my Self-XSS escalation write-up, one that took me multiple failed attempts before I finally cracked it with some much needed help. huge thanks to [**Jorian**](https://jorianwoltjer.com/) for helping me complete this exploit (check him out if you haven’t already phenomenal hacker).

## Initial Discovery

I found a Self-XSS vulnerability on the target application along with login/logout CSRF. After that, I attempted the following approaches:

### 1. Cookie Tossing

My first idea was to use the **cookie tossing** technique after forcing the victim to log out and log in to the attacker’s account, the Self-XSS executes, clearing the **HttpOnly** session cookie via a cookie-jar overflow, then setting the attacker’s session cookie with a **Path=/self-xss** attribute and redirecting to the log in page. This way, after the victim re-logs in (either immediately or sometime later), they wouldn’t notice the attacker’s session cookie, which would only be used for the Self-XSS path, while the victim’s session remains active on other endpoints.

Unfortunately, this didn’t work. The reason behind that is setting a **Path=** attribute causes the cookie to appear first in order, but the target server was reading the last cookie in the list.

This technique could also be applied from a subdomain XSS by using the **Domain=** cookie attribute, after the cookie-jar overflow, set the session cookie with **Domain=www.target.com** along with **Path=/self-xss**.

### 2. Stealing reflected session cookie

I then noticed the session cookie was being reflected on the page. My immediate thought was to open the victim’s page and trigger the Self-XSS on a separate tab to steal the session. However, I quickly ran into a wall: the Self-XSS page was using **Cross-Origin-Opener-PolicyCOOP: same-origin** the strictest option.

This setting ensures that the page shares a **Browser Context Group (BCG)** only with pages that are **same-origin** and have the same **COOP: same-origin** directive.

If it was **COOP: same-origin-allow-popups** or anything else, this approach would have worked, as it only requires both pages to be **same-origin** to share the **BCG**. And the sensitive page wasn’t setting the header at all.

### 3. The Winning Path

Running low on options, I reached out to Jorian and started discussing ideas.

Reading about the [**Cache Cache CTF Challenge**](https://mizu.re/post/heroctf-v6-writeups#cacheCache) and [**Poisoning top-level navigation with fetch()**](https://book.jorianwoltjer.com/web/client-side/caching#poisoning-top-level-navigation-with-fetch) gave me some inspiration.

An idea came to mind: I had a sensitive page with a reflected session, what if I could somehow cache the page under the victim’s session and after completing the chain, use the Self-XSS to somehow retrieve the cached page and exfiltrate it?

This is made possible by using: **fetch** with **force-cache**

After telling Jorian, he instantly came up with a solution.

### Disk Cache and fetch with force-cache

Opening the sensitive page on behalf of the victim result a disk cache. After performing the login/logout CSRF and triggering the Self-XSS, use **fetch** with the cache mode **force-cache**:

`fetch("/sensitive-page", { cache: "force-cache" });`
This forces the request to retrieve the cached response if one is present.

Sounds easy, right? Not so fast.

There’s a [**cross-site navigation bit**](https://source.chromium.org/chromium/chromium/src/+/main:net/http/http_cache.cc;l=760-765;drc=99249cf38aaf17aaed2443d2f8489595c982ac01) that gets set when navigating to the sensitive page. The fetch inside the Self-XSS won’t hit that cached response, because the cache key distinguishes between **cross-site navigation** and a **same-site fetch**.

**The fix:** Use a same-site client-side redirect gadget. By routing through:

`Attacker Page → Client-Side Gadget → Sensitive Page`
the navigation to the sensitive page becomes same-site, causing the cache keys to collide as intended.

This could have been simpler if there were an API endpoint leaking the session cookie, as that would eliminate the need for the client-side gadget entirely.

## Final Exploit Chain

1\. Tab A (attacker-controlled) opens Tab B (also attacker-controlled).

2. Tab A redirects through the client-side gadget to the sensitive page, making it a same-site navigation and caching the response.

3. Tab B performs the logout and login CSRF, then triggers the Self-XSS.

4. The Self-XSS executes:

`fetch("/sensitive-page", { cache: "force-cache" });`
This reads the cached response and then you can exfiltrates the victim session data.

## Mitigations

The following response headers would prevent this attack:

- [**Vary: Cookie**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Vary) ensures cached responses are scoped per cookie value.
- [**Cache-Control: no-store**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) prevents the response from being cached at all.
- [**Clear-Site-Data: “cache”**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Clear-Site-Data) can be used at login/logout requests to ensure the cache is cleared
