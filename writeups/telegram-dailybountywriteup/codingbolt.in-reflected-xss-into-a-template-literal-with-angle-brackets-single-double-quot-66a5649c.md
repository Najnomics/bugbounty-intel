# Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and…

- **Source URL:** https://medium.com/@codingbolt.in/reflected-xss-into-a-template-literal-with-angle-brackets-single-double-quotes-backslash-and-5acbbd9f2631?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250505111335/https://medium.com/@codingbolt.in/reflected-xss-into-a-template-literal-with-angle-brackets-single-double-quotes-backslash-and-5acbbd9f2631
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7373 (id 7373)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped**

Cross-Site Scripting (XSS) remains a critical security vulnerability in web applications, and attackers often exploit flaws in how user input is handled and reflected back into pages. While modern JavaScript introduces new features such as template literals, these features come with their own unique challenges in preventing XSS attacks. Template literals, with their ability to embed variables and multi-line strings, can become an attractive target for attackers if user input is not properly sanitized.

This article explores how Reflected XSS can manifest in template literals when user input is injected without proper encoding. We will focus on Unicode escaping for special characters, such as angle brackets (\`\<\`, \`>\`), single quotes (\`’\`), double quotes (\`”\`), backslashes (\`\\\`), and backticks (\`\` \` \`\`), to prevent malicious code execution.

**What is Reflected XSS?**

Reflected XSS occurs when a web application takes user-supplied input and reflects it back into the page without proper validation or escaping. This allows attackers to inject malicious scripts into a web page, which are then executed in the victim’s browser.
