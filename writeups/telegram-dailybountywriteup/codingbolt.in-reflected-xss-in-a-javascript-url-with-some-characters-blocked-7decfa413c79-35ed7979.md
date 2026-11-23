# Reflected XSS in a JavaScript URL with some characters blocked

- **Source URL:** https://medium.com/@codingbolt.in/reflected-xss-in-a-javascript-url-with-some-characters-blocked-7decfa413c79?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501121444/https://medium.com/@codingbolt.in/reflected-xss-in-a-javascript-url-with-some-characters-blocked-7decfa413c79
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7382 (id 7382)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **Reflected XSS in a JavaScript URL with some characters blocked**

## XSS

In the world of web security, Reflected Cross-Site Scripting (XSS) is one of the most notorious and widely abused vulnerabilities. While many web applications enforce stringent character restrictions to defend against XSS attacks, experienced attackers continue to find innovative ways to exploit them.


We will focus on a specific variant: exploiting Reflected XSS through a JavaScript URL when certain characters are blocked.


# **Reflected XSS: A Recap**

Before diving into the nuances of bypassing filters, let’s quickly revisit the basics of reflected XSS. Reflected XSS occurs when an attacker inputs malicious code (usually in the form of a URL parameter) that is reflected back in a page response and executed in the victim’s browser. This form of XSS is typically triggered when a user clicks a malicious link or submits a form with injected script tags.

**A typical XSS payload might look like this:**

`<script>alert('XSS');</script>`
However, in our scenario, let’s assume that certain characters, such as \`\<\`, \`>\`, \`”\` or \`’\`, are blocked by input validation or content filtering mechanisms, making…
