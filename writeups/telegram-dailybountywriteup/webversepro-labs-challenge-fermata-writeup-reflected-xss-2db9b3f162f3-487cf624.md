# WebVersePro Labs — Challenge

- **Source URL:** https://zor0ark.medium.com/webversepro-labs-challenge-fermata-writeup-reflected-xss-2db9b3f162f3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260423215253/https://zor0ark.medium.com/webversepro-labs-challenge-fermata-writeup-reflected-xss-2db9b3f162f3
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13365 (id 13365)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# WebVersePro Labs — Challenge: Fermata Writeup (Reflected XSS)

**OBJECTIVE:** To identify the injection point, break out of an HTML comment block, and execute arbitrary JavaScript to retrieve the challenge flag.

**VULNERABILITY:** Reflected Cross-Site Scripting (XSS) via HTML Comment Breakout


### **Challenge Scenario**

*Fermata connects clients with piano tuners. An old debug line left over from development drops the booking reference into an HTML comment so ops can scan View Source for bad IDs. It never occurred to anyone that comments are just text — not a fence.*

### Challenge Objective

A piano-tuner booking site still has a debug comment baked into production. It echoes your input — right into an HTML comment.


## Initial Discovery

I started by inspecting the booking reference system. After submitting a booking, I noticed the reference number was passed directly through the URL as a GET parameter: `?ref=[REF-ID]`.

Looking at the page source, I saw exactly what the scenario described. The backend was taking my `ref` parameter and echoing it straight into the DOM without any sanitization, placing it inside a comment block on line 25: `<!-- debug:booking-ref FM-2026-F14AC3 -->`

I knew immediately that all I had to do was close that comment prematurely and inject my own script tags.

## Hitting a Wall (My Mistakes)

I crafted my payload: `--><script>alert(1)</script>`. I fired it off, and I saw the `alert(1)` popup perfectly. I even saw the remaining `-->` render as plain text on the page, proving my comment breakout was successful. However, the flag wasn't showing up.

I initially went down a massive rabbit hole thinking this was a blind XSS scenario. Because the challenge mentioned “someone from the office emails within 24 hours,” I assumed there was a headless “Ops Bot” that I needed to target. I spent time intercepting the initial `POST /book` request, trying to inject my payload directly into the `date` parameter hoping the server would save it and force a bot to visit my poisoned link.

That wasn’t the issue at all. I was over-engineering a pure Reflected XSS challenge.

## The Workaround

The issue wasn’t my payload; it was my browser’s privacy settings. I was testing the challenge in Firefox, and I noticed a background script called `poll.js` running on the page, along with requests to a `__csp-report` endpoint.

The CTF platform validates the solve by using a Content-Security-Policy in “Report-Only” mode. When my XSS fires, my browser sends a telemetry report to the server. The server checks the session cookie on that report, matches it to my account, and tells `poll.js` to drop the flag on my screen.

However, Firefox’s Enhanced Tracking Protection was aggressively stripping my session cookies from those automated background reports. The server was getting my report, but it was completely anonymous. I dropped the shields in Firefox, but ultimately just fired up Chromium on my Kali machine, pasted the exact same URL:

`?ref=--%3E%3Cscript%3Ealert(1)%3C%2Fscript%3E`
Because Chromium natively attached the SameSite cookies to the CSP report, the server immediately recognized my session, and `poll.js` printed the flag directly to the screen.

After clicking ‘OK’, the page refresh again and displays the flag.

## **My Technical Takeaways**

**Why the payload works (Code Vulnerability Analysis)**

The application blindly trusts user input from the `ref` parameter. It reflects this input directly into the HTML template without escaping control characters like `<` and `>`. By prepending my payload with `-->`, the browser parsed that as the end of the developer's `<!--` comment block. This dropped the rest of my input—the `<script>` tag—directly into the active DOM, forcing the browser to execute it as valid code.

**Why this happened (Infrastructure Insight)**

From an infrastructure perspective, this challenge taught me a lot about how modern CTF platforms validate client-side attacks. Relying on `__csp-report` telemetry is a smart way to verify XSS, but it is highly susceptible to modern browser privacy features. When exploiting client-side bugs, the browser's default security postures (like cookie stripping or strict tracking protection) can silently break an otherwise flawless exploit chain.

**How I would patch it**

I would fix this by implementing strict output encoding. Before reflecting the `ref` parameter into the HTML template, the backend must convert all special characters into their corresponding HTML entities. Specifically, `<` should become `<` and `>` should become `>`. If properly encoded, my payload would render safely as a literal string inside the comment: `<!-- debug:booking-ref --><script>alert(1)</script> -->`, completely neutralizing the context breakout.
