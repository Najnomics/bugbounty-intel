# XSS Attacks Explained

- **Source URL:** https://medium.com/@vigneshkumaroffsec/xss-attacks-explained-the-types-the-contexts-and-how-to-find-them-65f73849da5e
- **Fetched from:** https://medium.com/feed/@vigneshkumaroffsec
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/15000 (id 15000)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*Get your JavaScript to run in someone else’s browser and you can act as them — steal their session, their data, their account. Here’s how XSS works, its types, the contexts that decide the payload, and the fixes. Authorized testing only.*

By Vignesh Kumar | Security Researcher

Cross-Site Scripting is the bug that keeps topping web vulnerability lists, two decades after it was named — because it’s simple, everywhere, and high-impact. The idea: you get a web app to include *your* JavaScript in a page, and when another user loads that page, your script runs **in their browser, in the app’s context.** From there you can read their session, act as them, and take over their account.

This guide covers what XSS is, its three types, the contexts that decide which payload works, how to find it, and the fixes — all for systems **you own or are explicitly authorized to test.**

### What XSS actually is

A web page is HTML and JavaScript. When an app takes something you typed — a comment, a search term, a profile field — and drops it into a page *without properly encoding it*, your input stops being data and becomes part of the page’s code. Add \<script> (or an event handler, or a javascript: URL) and the browser runs it.

The critical consequence: that script runs with the **victim’s** session and the **app’s** origin. It can read cookies (if not HttpOnly), make authenticated requests as the victim, read the page, log keystrokes, and exfiltrate data — anything the user could do, your script can do, silently.

### The three types of XSS

- **Reflected XSS.** Your payload is in the request (a URL parameter, a form field) and the server reflects it straight back into the response. It fires when a victim opens a crafted link. One victim per link, but trivial to deliver via phishing.
- **Stored XSS.** Your payload is **saved** by the app — in a comment, a profile, a support ticket, a product review — and runs for **everyone** who views that content. The most dangerous type: no link needed, and it can hit admins and spread like a worm.
- **DOM-based XSS.** The vulnerability is entirely in the **client-side JavaScript** — the server never sees the payload. Unsafe JS takes a value from a *source* (like location.hash) and writes it to a dangerous *sink* (like innerHTML or eval), executing it in the browser.

Knowing the type tells you how to deliver and confirm it; knowing the *context* tells you what payload to use.

### Context is everything

The same input lands in different places in the page, and each place needs a different payload. This is the part beginners miss. Where does your input appear?

- **HTML body** — between tags. A classic \<script> or \<img src=x onerror=...> works.
- **HTML attribute** — inside value="...". You first break out of the attribute (">), then inject.
- **JavaScript context** — inside a \<script> block or an inline handler. You break out of the string/statement ('; or \</script>) and write JS directly.
- **URL context** — inside an href/src. A javascript: URL can execute.
- **CSS / other** — rarer, but style contexts have their own injection paths.

Figuring out the context — and what characters are and aren’t encoded there — is the whole craft. The payload that fires in an HTML body does nothing inside a JS string, and vice versa.

### Where XSS hides

Anywhere user input reaches the page:

- **Search boxes** that echo “results for: *your term*.”
- **Comments, reviews, posts, messages** (stored).
- **Profile fields** — name, bio, website, location.
- **URL parameters** reflected into the page (reflected/DOM).
- **Error messages** that echo the bad input.
- **HTTP headers** reflected into pages (Referer, User-Agent).
- **File names** shown in an upload list.
- **Markdown / rich text / SVG** that renders HTML.
- **JSON data** rendered into the DOM by client-side JS (prime DOM-XSS territory).

### How to find and test XSS

**1. Inject a unique probe.** Put a harmless, searchable marker into every input — something like xss7391 — and find everywhere it appears in the response or the DOM.

**2. Identify the context.** For each reflection, look at *where* it landed: HTML body, an attribute, a script block, a URL. That decides your payload.

**3. Test whether special characters survive.** Try the characters you’d need to break out — \< > " ' / — and see which are encoded. If \< becomes <, that context is encoding HTML; if it passes through raw, it's injectable.

**4. Build a context-appropriate proof.** Start with a benign, unmistakable proof of execution rather than anything harmful — the point is to *demonstrate* script runs, not to attack users:

HTML body:        \<img src=x onerror=alert(document.domain)>

Attribute: ">\<img src=x onerror=alert(document.domain)>

JS string: ';alert(document.domain)//

URL: javascript:alert(document.domain)

alert(document.domain) is the convention because it proves execution *and* the origin it runs in — enough for a report, without touching anyone's data.

**5. For stored XSS**, inject the payload, then load the page as another test account to confirm it fires for other users. For **DOM XSS**, trace the JavaScript from source (location, document.referrer, postMessage) to sink (innerHTML, document.write, eval, setAttribute) in the browser's dev tools.

**6. Report it** with the exact input, the URL/page, the context, a benign proof-of-execution payload, the realistic impact (session/account takeover), and the fix. Only on systems you’re authorized to test, and never with a payload that touches real users’ data.

### The impact (why it’s rated high)

- **Session/cookie theft** → account takeover (unless cookies are HttpOnly).
- **Acting as the victim** — making authenticated requests, changing their settings, stealing their CSRF token.
- **Credential capture** — a fake login prompt injected into a trusted page.
- **Worming** — stored XSS that re-injects itself spreads across users.

### The fix

- **Context-aware output encoding** — the core fix. Encode user data for the *exact* context it’s placed in (HTML, attribute, JS, URL). Modern frameworks (React, Angular, Vue) auto-escape by default — don’t override that with dangerouslySetInnerHTML / v-html on untrusted data.
- **A Content Security Policy (CSP)** — a strong CSP (no inline script, nonces/hashes, tight script-src) turns many XSS bugs from "account takeover" into "nothing happens." Defense in depth, not a substitute for encoding.
- **HttpOnly cookies** — so even successful XSS can't read the session cookie.
- **Sanitize HTML you must render** — if users submit rich text, run it through a vetted sanitizer like **DOMPurify**; never build it by hand.
- **Avoid dangerous sinks** — no innerHTML, document.write, or eval on untrusted data; use textContent and safe DOM APIs.
- **Validate input** as a secondary layer — but output encoding is what actually stops XSS, not input filters (which get bypassed).

### Common Mistakes to Avoid

- Testing against systems or users you aren’t authorized to assess.
- Testing one payload everywhere instead of matching the payload to the context.
- Only checking the HTML response and missing DOM-based XSS in the JavaScript.
- Assuming a WAF or input filter is the fix — both get bypassed; encoding is the fix.
- Rendering user HTML/markdown/SVG without a sanitizer.
- Using innerHTML/dangerouslySetInnerHTML/v-html on untrusted data.
- Forgetting HttpOnly on session cookies, turning XSS straight into session theft.
- Using a real user’s data in a proof — alert(document.domain) proves it without harm.

### A Quick XSS Checklist

- You’re testing only inputs and targets you’re authorized to assess.
- Every user input is traced to where it appears in the response and the DOM.
- The injection context (HTML/attribute/JS/URL) is identified for each reflection.
- Payloads are context-appropriate, and proof is benign (alert(document.domain)).
- Stored cases are confirmed from a second account; DOM cases traced source → sink.
- On the fix: output is context-encoded; the framework’s auto-escaping isn’t bypassed.
- A strong CSP is in place; session cookies are HttpOnly.
- Any rendered rich text/HTML goes through a vetted sanitizer; dangerous sinks are avoided.

### Final Thoughts

XSS persists because every app takes user input and shows it to users, and the gap between “data” and “code” is one missing encode wide. The fix isn’t exotic: encode output for its context, add a CSP, mark cookies HttpOnly, and sanitize anything you deliberately render as HTML. The craft of *finding* it is all about context — the same character that's harmless in one place is a running script in another.

If you build or test web apps, do one thing this week: pick any field that shows your input back to you, drop in ">\<img src=x onerror=alert(document.domain)>, and see what the browser does. If a box pops, you've found the gap between data and code — and you know exactly which encode closes it.

### About me

I’m Vignesh Kumar, a security researcher working across application security, DevSecOps, cloud security, and vulnerability research.

I share practical findings from security assessments and responsible disclosures to help improve the security of real-world systems.

*The techniques in this article are described for defending and testing systems you own or are authorized to assess.*
