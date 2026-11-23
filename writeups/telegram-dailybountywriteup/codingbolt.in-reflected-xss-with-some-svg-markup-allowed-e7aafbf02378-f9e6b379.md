# Reflected XSS with some SVG markup allowed

- **Source URL:** https://medium.com/@codingbolt.in/reflected-xss-with-some-svg-markup-allowed-e7aafbf02378?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250806040749/https://medium.com/@codingbolt.in/reflected-xss-with-some-svg-markup-allowed-e7aafbf02378
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7363 (id 7363)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **Reflected XSS with some SVG markup allowed**

reflected xss — svg markup allowed

Cross-Site Scripting (XSS) vulnerabilities have been haunting web applications for years, enabling attackers to inject malicious scripts that can be executed in a user’s browser. Among the most common variants, Reflected XSS is particularly dangerous because it leverages user inputs that are immediately reflected back into the web page without proper sanitization. A user simply clicks a crafted link, triggering malicious code execution.


We’ll focus on Reflected XSS in environments where most HTML tags are blocked, but some SVG markup is allowed. SVG (Scalable Vector Graphics) is a powerful image format used in modern web development, and it supports its own set of elements and attributes, which, if improperly handled, can be exploited to carry out XSS attacks.

**Why Allowing SVG is Risky?**

SVG might seem harmless at first glance — just a format for displaying vector graphics. However, SVG is more than just images. It supports a variety of elements that can embed JavaScript, event handlers, and other interactive features. When web applications allow SVG markup, they may inadvertently open up dangerous attack vectors that can lead to Reflected XSS vulnerabilities.

**Understanding Reflected XSS**
