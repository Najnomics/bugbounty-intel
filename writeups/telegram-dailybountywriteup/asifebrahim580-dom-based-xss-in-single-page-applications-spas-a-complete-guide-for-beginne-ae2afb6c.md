# DOM-Based XSS in Single Page Applications (SPAs)

- **Source URL:** https://medium.com/@asifebrahim580/dom-based-xss-in-single-page-applications-spas-a-complete-guide-for-beginners-bug-bounty-56d4e496a0a0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250907195258/https://medium.com/@asifebrahim580/dom-based-xss-in-single-page-applications-spas-a-complete-guide-for-beginners-bug-bounty-56d4e496a0a0
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9708 (id 9708)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🔥 DOM-Based XSS in Single Page Applications (SPAs): A Complete Guide for Beginners & Bug Bounty Hunters

### 📌 Introduction

DOM-Based Cross-Site Scripting (DOM XSS) is one of the stealthiest and most overlooked vulnerabilities in modern web apps — especially in Single Page Applications (SPAs) that rely heavily on JavaScript. As front-end frameworks like React, Angular, and Vue dominate the web, attackers have found new ways to exploit the DOM.

In this comprehensive guide, I’ll break down what DOM-based XSS is, how it works specifically in SPAs, real-world examples, detection methods, common payloads, and tools you can use as a beginner or aspiring bug bounty hunter.

### 🧠 What Is DOM-Based XSS?

DOM-Based XSS occurs when client-side JavaScript takes untrusted data (like from `window.location`, `document.referrer`, or `location.hash`) and dynamically injects it into the DOM without proper sanitization or encoding.

Unlike Reflected or Stored XSS, **DOM XSS does not involve the server directly** — the vulnerability lives entirely in the front-end JavaScript logic.

### **⚠️ Example:**

```
// Vulnerable SPA code
const name = new URLSearchParams(window.location.search).get('name');
document.getElementById('greeting').innerHTML = `Hello ${name}`;
```
If a user visits:

`https://example.com/?name=<img src=x onerror=alert(1)>`
The app renders:

`Hello <img src=x onerror=alert(1)>`
This leads to XSS execution directly in the browser.

### 🛠️ Why DOM XSS Is More Common in SPAs

Single Page Applications use client-side routing, dynamic DOM updates, and API-based data flows. That means:

- Inputs are often handled by JavaScript directly.
- URL fragments (`#`, `?`, etc.) are parsed on the client side.
- Frameworks may manipulate the DOM with dangerous APIs like `innerHTML`, `document.write()`, or `eval()`.

**Common vectors in SPAs:**

- `window.location.href`, `window.location.hash`, `document.URL`
- `innerHTML`, `outerHTML`, `insertAdjacentHTML()`
- `eval()`, `setTimeout(string)`, `Function()`

### 🎯 Where to Look: Common DOM Sinks & Sources

### 🧪 Real-World Example: jQuery DOM XSS in SPA

```
let payload = new URLSearchParams(location.search).get("xss");
$("#output").html(payload);
```
A user visiting:

`https://target.com/spa#/?xss=<img src=x onerror=alert('Hacked!')>`
Triggers DOM-based XSS, bypassing many traditional WAFs.

### 🕵️ How to Detect DOM-Based XSS in SPAs (Manual & Automated)

### Manual Testing:

1. **Check URL Parameters, Hashes, Fragments**: Try injecting test payloads into them.
2. **Use DevTools**: Monitor DOM changes and JavaScript execution via the “Sources” and “Console” tabs.
3. **Look for Dangerous DOM APIs**: Search for `innerHTML`, `document.write`, `eval`, etc.
4. **Analyze Frontend JavaScript**: Look for patterns where untrusted input is not sanitized.

### Common Payloads:

```
"><img src=x onerror=alert(1)>
<script>alert(1)</script>
<svg onload=alert(1)>
" onmouseover="alert(1)
```
### 🧬 Payload Variants for Bypassing Filters

Try obfuscation techniques:

```
<IMG SRC=JaVaScRiPt:alert(1)>
<svg><script>alert(1)</script></svg>
<iframe src="javascript:alert`1`">
<details open ontoggle=alert(1)>
<math href="javascript:alert(1)">
```
Framework-specific payloads (e.g., AngularJS):

`<iframe srcdoc="{{constructor.constructor('alert(1)')()}}">`
### 🔐 Real-World Bug Bounty Reports

- **Google**: Vulnerable due to dynamic DOM updates with unescaped input. Rewarded $5000.
- **Uber**: DOM XSS via location.hash used in client-side template rendering.
- **Twitter (legacy code)**: Allowed execution of JS from location fragments in their older SPA version.

### 👨💻 Final Thoughts

DOM-based XSS might seem tricky at first — but with SPAs dominating the modern web, understanding and hunting for these bugs is **essential** for any serious bug bounty hunter or web app pentester.

Keep experimenting with payloads, inspecting JS sources, and mastering tools like Burp and DOM Invader. The more you dive into SPAs and how they interact with the DOM, the better you’ll get at spotting these elusive but dangerous bugs.

💬 **Was this guide helpful? Drop a comment below or share your own experience finding DOM XSS in the wild!**

#xss #bugbounty #cybersecurity #websecurity #javascript #spa #pentesting #infosec
