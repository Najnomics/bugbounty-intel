# Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and…

- **Source URL:** https://medium.com/@codingbolt.in/reflected-xss-into-a-javascript-string-with-angle-brackets-and-double-quotes-html-encoded-and-e1ad9b482189?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240929070629/https://medium.com/@codingbolt.in/reflected-xss-into-a-javascript-string-with-angle-brackets-and-double-quotes-html-encoded-and-e1ad9b482189
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7371 (id 7371)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped**

Cross-Site Scripting (XSS) remains one of the most notorious and prevalent web vulnerabilities. While many developers are familiar with basic XSS vectors, understanding how to prevent XSS in complex contexts like JavaScript strings is trickier. The issue becomes even more delicate when user input is reflected into JavaScript strings, where angle brackets (\`\<\`, \`>\`), double quotes (\`”\`), and single quotes (\`’\`) must be carefully handled and encoded.

In this article, we will explore how Reflected XSS can be exploited in JavaScript strings, even when some encoding measures are in place, and discuss best practices for mitigating such attacks.

Reflected XSS occurs when a web application takes user-supplied input and reflects it back into the web page without proper validation or sanitization, allowing attackers to inject malicious code that is executed in the context of the user’s browser.

The most common mistake happens when this user input is embedded in JavaScript strings, particularly when developers incorrectly assume that partial encoding of characters like angle brackets (\`\<\`, \`>\`), double quotes (\`”\`), and single quotes (\`’\`) is sufficient to prevent attacks.
