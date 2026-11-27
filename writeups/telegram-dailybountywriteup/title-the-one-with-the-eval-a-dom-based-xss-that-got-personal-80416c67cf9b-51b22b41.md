# Title

- **Source URL:** https://mosstafa.medium.com/title-the-one-with-the-eval-a-dom-based-xss-that-got-personal-80416c67cf9b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250822055221/https://mosstafa.medium.com/title-the-one-with-the-eval-a-dom-based-xss-that-got-personal-80416c67cf9b
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10345 (id 10345)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **The One with the** **eval()** **— A DOM-Based XSS That Got Personal**

# “I just can’t get you out of my head…”

That line was meant for a JavaScript file.

Specifically: `ajax-cart.js` on a Shopify store.

It was late. Screens dimmed. **27** tabs open. **7** were JavaScript files. Tabs piling. My recon engine hummed. That’s when I saw it — the kind of negligence you don’t just find; it finds you:

```
var token = new URLSearchParams(window.location.search).get("cart_token");
eval(token);
```
That’s not just sloppy — that’s dangerous by design.

# 📦 Context: Recon Rituals & Birthday Revelations

My ritual’s simple: monitor every exposed Shopify store, harvest every `.js` file, and hunt for the one line no one should write.

And that day? My birthday.

H**BD** to me**(Mosstafa)**

Most people get cake. I got a ticking time bomb in code.

The file? `ajax-cart.js`. Harmless name. Hidden venom.

So I tore it open. Line by line. And there it was:

```
let token = new URLSearchParams(window.location.search).get("cart_token");
eval(token);
```
No filtering. No protection. No excuse.

This wasn’t just vulnerable — it was begging to be exploited.

And suddenly, I wasn’t thinking about the bug anymore. I was thinking about her.

She always said, “You overanalyze everything.”

**Maybe. But if I didn’t, I wouldn’t have found this**.

**I didn’t forget her birthday like she thought I did—she just didn’t notice**

Same with this vulnerability.

It was always there. Waiting. Like I was.

# 🕳️ The Bug: DOM-Based XSS via Unfiltered `eval()`

Let’s break it down:

File: `ajax-cart.js`


- Flow:
- Extracts `cart_token` from URL
- Passes it directly to `eval()`
- Problem: No sanitization, no verification

```
let token = new URLSearchParams(window.location.search).get("cart_token");
eval(token);
```
This is textbook DOM XSS — lethal and instant.

# 🎯 Proof of Concept

Basic alert? Easy:

`https://target.myshopify.com/?cart_token=alert(document.domain)`
More poetic?

`https://target.myshopify.com/?cart_token=document.body.innerHTML='<h1>I just can\'t get you out of my head.</h1>'`
Or dramatic:

`https://target.myshopify.com/?cart_token=document.write('<div style="font-size:2em;">You trusted me with this. And now it's too late.</div>')`
No backend. No auth. No challenge.

Just raw power — in the wrong hands.

# 🔥 Real-World Impact

DOM XSS isn’t theory — it’s practice.

If cookies are accessible, then:

- Session hijack
- Admin account takeover
- Silent customer skimming

If abused in phishing:

- Injected login prompts
- Malicious redirect chains
- Fake checkout forms

If admin clicks? Game over.

All from a URL.

# 🛠️ Remediation: Burn the `eval()`

# What to do:

- Remove `eval()` entirely
- Sanitize and validate all URL params
- Implement CSP with `script-src 'self'`

# Replace with:

```
try {
  let safe = JSON.parse(token);
  // use safe object logic
} catch (e) {
  console.error('Invalid token input');
}
```
But honestly?

Don’t even trust URL input unless you control both ends.

# 🧠 Why It Mattered

This bug wasn’t the most complex.

It wasn’t buried in **2009** lines.

It was right there.

Like memories you try to forget, but can’t.

*This bug reminded me why I hunt. Why I dig through noise. Why I still feel things I don’t talk about.*


When I talked to my friend about this and told him every thing

he told me “you are probably in love with security”.

And I was like :

**I absofuckinglutely Love S**.

The Security. The Silence. The Script. And maybe Shopify as a target

# ✅ TL;DR

- Vulnerability: DOM-Based XSS
- Location: `ajax-cart.js`
- Input: `cart_token` parameter from URL
- Flaw: Direct use of `eval()`
- Impact: Full JS execution in browser
- Exploit: No auth, no filters, 1-click payloads
- Fix: Remove `eval()` + validate inputs

Written by Mostafa Ghanem🎱 🫵🏻— code breaker, boundary pusher, and someone who found a bug… and a bit of himself in it.


🎂 **HBD** — to the bug that broke the silence.

🧠 **16** stores down. **And this one? Unforgettable.**
