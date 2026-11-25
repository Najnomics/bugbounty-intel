# Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes…

- **Source URL:** https://medium.com/@codingbolt.in/stored-xss-into-onclick-event-with-angle-brackets-and-double-quotes-html-encoded-and-single-quotes-9af43308602b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501125606/https://medium.com/@codingbolt.in/stored-xss-into-onclick-event-with-angle-brackets-and-double-quotes-html-encoded-and-single-quotes-9af43308602b?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7372 (id 7372)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **Stored XSS into** `onclick` **event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped**

Cross-Site Scripting (XSS) is one of the most dangerous and widely exploited vulnerabilities in modern web applications. Among the many forms of XSS, Stored XSS is particularly severe because malicious scripts are persistently stored on a server and executed whenever unsuspecting users visit the compromised page. One subtle yet impactful form of Stored XSS occurs when user input is reflected into JavaScript event handlers — such as the \`onclick\` attribute — without proper encoding.

This article explores how Stored XSS can be exploited in the context of the \`onclick\` event, even when angle brackets (\`\<\`, \`>\`), double quotes (\`”\`), and backslashes are encoded or escaped. It also provides best practices for mitigating these risks.

**Stored XSS in a Nutshell**

Stored XSS (also called persistent XSS) occurs when malicious user input is stored on the server and then reflected back into web pages viewed by others. Unlike Reflected XSS, where the malicious payload is delivered via a URL and only affects the victim who clicks the link, Stored XSS poses a greater risk because it can affect multiple users and persist over time.
