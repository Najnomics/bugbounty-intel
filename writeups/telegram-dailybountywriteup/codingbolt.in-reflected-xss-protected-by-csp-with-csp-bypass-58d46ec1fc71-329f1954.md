# Reflected XSS protected by CSP, with CSP bypass

- **Source URL:** https://medium.com/@codingbolt.in/reflected-xss-protected-by-csp-with-csp-bypass-58d46ec1fc71?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240926182419/https://medium.com/@codingbolt.in/reflected-xss-protected-by-csp-with-csp-bypass-58d46ec1fc71?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7385 (id 7385)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Reflected XSS protected by CSP, with CSP bypass**

Cross-Site Scripting (XSS) is one of the most persistent and dangerous web vulnerabilities. Even with modern defenses like Content Security Policy (CSP), attackers find creative ways to bypass security measures and exploit reflected XSS vulnerabilities. In this article, we explore how attackers can bypass a strong CSP to execute a Reflected XSS attack and offer guidance on how developers can bolster their defenses.

**What is Reflected XSS?**

Reflected XSS occurs when user input is reflected back from the server without proper validation or sanitization, allowing an attacker to inject malicious JavaScript code. When a victim clicks a malicious link or submits input, the reflected payload is executed within the user’s browser, granting the attacker access to sensitive information or control over the victim’s session.

**A typical reflected XSS attack looks like this:**

*https://example.com/search?q=\<script>alert('XSS')\</script>*

Without any protection, the web server reflects this input directly into the page, and the malicious script is executed in the victim’s browser.

*Content Security Policy (CSP): The First Line of Defense*

CSP is a browser security mechanism designed to prevent various types of attacks, including XSS, by controlling which resources (scripts, styles, images, etc.) can be loaded and executed on a webpage. For instance, a strict CSP could look like this:
