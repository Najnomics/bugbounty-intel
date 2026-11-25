# Reflected XSS protected by very strict CSP, with dangling markup attack

- **Source URL:** https://medium.com/@codingbolt.in/reflected-xss-protected-by-very-strict-csp-with-dangling-markup-attack-029d16b86163?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250507005943/https://medium.com/@codingbolt.in/reflected-xss-protected-by-very-strict-csp-with-dangling-markup-attack-029d16b86163?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7384 (id 7384)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **Reflected XSS protected by very strict CSP, with dangling markup attack**

Cross-Site Scripting (XSS) remains one of the most dangerous vulnerabilities on the web, even as security standards such as Content Security Policy (CSP) aim to reduce the risks. However, even with a very strict CSP in place, attackers have found clever ways to bypass these protections. One such method is the dangling markup attack.

In this article, we’ll delve into how a Reflected XSS attack can still be executed in a web application fortified by a strict CSP using the dangling markup attack. We’ll cover the basics of strict CSPs, why they matter, and how the dangling markup technique manipulates the browser’s rendering engine to inject malicious payloads.

**What is Reflected XSS?**

Reflected XSS is a form of Cross-Site Scripting where an attacker injects malicious code that gets reflected back to the user by the web server, typically via URL parameters. This code is then executed in the victim’s browser when they click a specially crafted malicious link. The attacker aims to hijack sessions, steal credentials, or run arbitrary scripts within the victim’s browser.

A typical Reflected XSS attack might look like this:

*https://example.com/?search=\<script>alert(1)\</script>*
