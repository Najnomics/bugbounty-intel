# Finding Cross-Site Scripting (XSS) vulnerabilities in Bug bounty program

- **Source URL:** https://medium.com/@curiouskhanna/finding-cross-site-scripting-xss-vulnerabilities-in-bug-bounty-program-2a40bef4c8d7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250720143119/https://medium.com/@curiouskhanna/finding-cross-site-scripting-xss-vulnerabilities-in-bug-bounty-program-2a40bef4c8d7
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7667 (id 7667)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Finding Cross-Site Scripting (XSS) vulnerabilities in Bug bounty program

2 min readOct 25, 2024

Finding XSS in Bug bounty program can be hard at first, so I have wrote some things together to do have a roadmap whenever doing bug bounty.

## 1. Input Vectors:

- **URL Parameters:** These are parts of the URL that can be manipulated. For example, `http://example.com/page?name=John` — test by injecting scripts into `name`.
- **Form Inputs:** Fields where users enter data, such as login forms, search bars, and comments.
- **HTTP Headers:** Headers like `User-Agent` or `Referer` can sometimes be manipulated to execute scripts.
- **Cookies:** If cookies are improperly handled, they might be another vector for XSS.

## 2. Payloads:

- **Basic Payloads:** Start with simple scripts like `<script>alert('XSS')</script>`.
- **Advanced Payloads:** Use variations to bypass filters, such as `"><script>alert('XSS')</script>` or `SRC=javascript:alert('XSS')`.
- **Polyglots:** These are payloads that can execute in multiple contexts, e.g., `"><img src=x onerror=alert(1)>`.

## 3. Bypassing Filters:

- **Encoding:** Use HTML entity encoding (e.g., `<script>`) or URL encoding (`%3Cscript%3E`).
- **Nested Encoding:** Double or triple encode to bypass simple filters.
- **Case Variations:** Change the case of tags or attributes, e.g., `<ScRipT>`.

## 4. Testing Strategies:

- **Fuzzing:** Input random data into fields to see how the application processes it.
- **Contextual Testing:** Understand the context (HTML, JavaScript, CSS) where your input is reflected and craft your scripts accordingly.
- **DOM Analysis:** Use browser developer tools to inspect the Document Object Model (DOM) and identify client-side vulnerabilities.

## 5. Tools and Automation:

- **Burp Suite:** A comprehensive tool that allows for manual and automated testing of web applications.
- **OWASP ZAP:** An open-source web application security scanner.
- **XSSer:** A tool specifically designed to find XSS vulnerabilities.
- **Browser Extensions:** Extensions like “XSS Rays” for Chrome can help in manual testing.

## 6. Reporting:

- **Detailed Reports:** Provide step-by-step details, including the exact payload used, screenshots, and how the vulnerability can be reproduced.
- **Impact Explanation:** Explain the potential impact of the vulnerability, such as data theft or session hijacking.
- **Mitigation Suggestions:** Offer guidance on how to fix the vulnerability, like input validation and output encoding.

# Best Practices and Ethics

- **Stay Legal:** Only test applications that are part of a bug bounty program and have given explicit permission.
- **Continuous Learning:** The cybersecurity field evolves rapidly, so keep learning about new techniques and vulnerabilities.
- **Engage with the Community:** Join forums, attend workshops, and participate in Capture The Flag (CTF) competitions to improve your skills.
