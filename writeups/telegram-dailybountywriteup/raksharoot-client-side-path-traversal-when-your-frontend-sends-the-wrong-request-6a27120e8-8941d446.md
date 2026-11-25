# Client-Side Path Traversal

- **Source URL:** https://medium.com/@raksharoot/client-side-path-traversal-when-your-frontend-sends-the-wrong-request-6a27120e8730
- **Fetched from:** https://medium.com/@raksharoot/client-side-path-traversal-when-your-frontend-sends-the-wrong-request-6a27120e8730?source=rss-4206d471b207------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14954)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Raksharoot / Tue, 20 Oct 2026 18:08:11 GMT

Disclaimer: Educational content only. Only test systems you own or have written permission to test. Use the Doyensec CSPT Playground for practice. Never test on live users without explicit authorization.

Server-side path traversal is old news. Everyone knows to sanitize ../ in file paths.

Client-side path traversal is the same bug, just moved one layer up, and most frontend developers have never heard of it.

***The idea:*** your SPA takes user-controlled input, concatenates it into a URL path, and sends an authenticated request. If that input contains dot segments like ../ , the browser normalizes the URL before dispatching it. The victim’s browser ends up hitting a completely different endpoint on the same origin with their cookies, their auth headers, their client certificate, everything attached.

That’s on-site request forgery. OSRF. CSPT.

Same request, different destination, victim’s credentials.

And it chains into everything.

Normal CSRF is cross-origin. The attacker’s page makes a request to the target, and the browser’s same-origin policy fights back. Defenses like CSRF tokens, *SameSite* cookies, and origin checks exist precisely because cross-origin requests are suspicious.

CSPT is same-origin. The request comes from the app itself. Cookies are attached automatically. *SameSite=Strict* doesn’t help. CSRF tokens are already in the request because the legitimate frontend code put them there.

The attacker doesn’t need to bypass any of that. They just need to control what path the frontend requests.

That’s the whole game.

Anywhere user-controlled data gets concatenated into a URL path.

***The common thread***: anything the user can influence ends up in a URL path.

The path goes somewhere. Where it lands determines what you can do with it.

The traversal only matters if the sink actually dispatches an authenticated request. A reflection into a *\<div>* isn’t a bug. A reflection into *fetch()* is.

This is the part that makes CSPT genuinely nasty.

Query parameters used as path segments can be parsed twice - first by *URLSearchParams*, then by the browser when *fetch* or XHR parses the constructed URL.

If you can encode *?* and *&* in the outer URL, the first parse returns them as literal characters inside one parameter. After interpolation, the second parse promotes them to actual query delimiters.

Here’s a real builder from a disclosed bug:

*Now Supply:*

The first parse gives you literal *?* and *&* inside teamId . After concatenation:

The browser normalizes the dot segments. The effective path is */api/v2/user*. The *x=x/invites/../* becomes query data, not a path to normalize.

If the client preserves a state-changing verb and the server accepts query parameters as update input, the victim’s browser fires:

That’s a request the frontend was never supposed to be able to make. And it’s authenticated with the victim’s session.

This is how you change someone’s email without ever touching their password.

CSPT by itself is a request you can retarget. The impact comes from what you retarget it to.

**CSPT → CSRF → account takeover**

Hijack authenticated *POST* , *PUT* , or *DELETE* calls by escaping the intended resource path and re-entering a sensitive endpoint. Password reset, payment approval, access revocation, primary email change.

One disclosed chain went all the way:

That’s account takeover, built from three bugs that individually would have been low severity.

**CSPT → cache deception → data leak**

This is the chain I find most impressive.

A frontend concatenates user-controlled input into an API path and attaches auth headers. Dot segments retarget the request to a different endpoint on the same origin, one that returns sensitive JSON.

If the CDN caches that endpoint without varying on auth headers, the victim’s authenticated response gets stored under a public cache key. Anyone who requests the same URL gets the victim’s data.

*The recipe:*

This is why static-file caching rules and authenticated API routes should never overlap.

*CSPT → open redirect → XSS or SSRF*

Traversal lands on an open redirect endpoint, which bounces to attacker infrastructure. That infrastructure serves malicious JS, or responds with SSRF-usable content.

The traversal gets you to the redirector. The redirector gets you to the attacker’s origin.

In 2025, Grafana had a CSPT in the frontend’s handling of */public/plugins//… paths*.

**The attack chain:** CSPT + open redirect → load an attacker-controlled plugin module → XSS in the victim’s browser.

What made this one notable:

*A schematic path looked like:*

Exact normalization and plugin-ID requirements varied by release, but the concept was consistent: traversal escapes the plugin directory, the open redirect sends the browser to attacker infrastructure, the module loads as if it came from Grafana.

With the optional Grafana Image Renderer installed, the same path manipulation became a full-read SSRF instead.

**Fixed in:** 10.4.18+security-01, 11.2.9+security-01, 11.3.6+security-01, 11.4.4+security-01, 11.5.4+security-01, and 12.0.0+security-01.

Passive discovery with Burp

The CSPT Burp extension is the most useful tool here. It parses your proxy history, clusters parameters that end up reflected inside other requests’ paths, and can reissue proof-of-concept URLs with canary tokens.

Load the JAR, set Source Scope to client parameters ( *id* , *slug* , etc.), and set Sink Methods to *GET, POST, DELETE*. The extension highlights dangerous request builders. You can export all suspect sources with embedded canaries and validate them in bulk.

Also watch for double-URL-decoding while browsing. Patterns like */api/%252e%252e/* that get normalized by the frontend before hitting the network are easy to miss without an automated scanner. They often show up as base64-encoded JSON bodies referencing route state.

Drop this in DevTools and interact with the UI:

Add similar wrappers around *XMLHttpRequest.prototype.open*, *history.pushState*, and *frameworkspecific* routers like next/router.

Watching for *init.credentials === “include”* narrows it down fast, those are the requests carrying session cookies.

If the app stores routing hints in IndexedDB or localStorage, edit those entries with traversal payloads and reload. The mutated state often gets reinjected into requests during hydration, before any UI validation runs.

When you see an unexpected request in the Network panel, click it and look at the Initiator stack. It tells you exactly which code built the URL.

Compare the URL string immediately before dispatch with the path and query shown in the Network panel. A URL constructor alone is not a defense — *new URL()* deliberately resolves dot segments. The bug is that the app concatenated untrusted input before the constructor normalized it.

Spin up the Doyensec CSPT Playground with *docker compose up* and practice chaining traversal → CSRF → stored XSS without touching a real target.

Reproducing the target’s router structure locally makes it easier to craft shareable PoCs and to know which payloads will work before you try them on the live app.

Maintain a list of dot-segment variations that worked:

When a new sink appears mid-engagement, you’ll want that list ready.

Not exhaustive, but this is the order I go in:

CSPT is a same-origin request forgery that bypasses every defense designed for cross-origin attacks.

No CSRF token bypass needed. No *SameSite* bypass needed. The request is already authenticated because the frontend made it.

The bug is that the frontend trusts input it shouldn’t, and the browser normalizes the URL before dispatch, so the destination is whatever the attacker chose.

**The fix is boring:** validate each identifier against its expected grammar, reject path and query delimiters before concatenation, and allowlist the final method and normalized pathname. Not a *URL* constructor, actual grammar validation.

**The exploit is creative:** chain CSPT into CSRF, cache deception, open redirect, or XSS. Each chain step is a small bug. Together they’re account takeover.

Test in the playground. Instrument the sink. Follow the initiator stack. And when you find a traversal, don’t stop, ask what endpoint the attacker would want to hit. That’s where the impact lives.

That’s Part-10. Read the whole series in order: [Web Pentesting: A Complete Guide](https://medium.com/@raksharoot/list/web-pentesting-a-complete-guide-ad31d529002a).
