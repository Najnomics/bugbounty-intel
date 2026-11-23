# Reflected XSS into HTML context with most tags and attributes blocked

- **Source URL:** https://medium.com/@codingbolt.in/reflected-xss-into-html-context-with-most-tags-and-attributes-blocked-0bb80ac37064?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250502033620/https://medium.com/@codingbolt.in/reflected-xss-into-html-context-with-most-tags-and-attributes-blocked-0bb80ac37064
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7362 (id 7362)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **Reflected XSS into HTML context with most tags and attributes blocked**

Reflected Cross-Site Scripting (XSS) attacks exploit vulnerabilities in web applications by reflecting malicious inputs back to a user via unsanitized data. Unlike stored XSS, reflected XSS does not persist on the server; instead, it relies on user interaction, often via a specially crafted link. Despite the lack of persistence, reflected XSS can be incredibly dangerous, especially when developers attempt to block certain HTML tags and attributes but leave small gaps for attackers to exploit.

In this article, we’ll explore how attackers bypass restrictions designed to block XSS in the HTML context, where most tags and attributes are blocked, and demonstrate how creative payloads can still lead to successful exploitation.

**How Reflected XSS Works**

The core idea behind reflected XSS is simple: the attacker supplies data to the server, which is then immediately reflected back to the user’s browser in a vulnerable way, typically without proper sanitization. For example, an attacker might embed malicious JavaScript in a query string, form input, or URL, tricking the web application into rendering the code in the victim’s browser.

But what if the application blocks most common HTML tags and attributes, such as \`\<script>\`, \`\<img>\`, or \`onload\`? Attackers must…
