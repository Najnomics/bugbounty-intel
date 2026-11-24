# XSS Cheatsheet

- **Source URL:** https://medium.com/@r0ckysah/xss-cheatsheet-a49e5cc16fbd?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230313123002/https://medium.com/@r0ckysah/xss-cheatsheet-a49e5cc16fbd
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1985 (id 1985)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS Cheatsheet

Cross-site scripting (XSS) attacks are a common type of web application security vulnerability. These attacks occur when an attacker injects malicious code into a web page viewed by other users. This can result in stolen user data, malware downloads, and other malicious activities. In this article, we’ll provide a comprehensive XSS cheatsheet to help you protect your web application against these attacks.

# XSS Cheatsheet Categories

1. Basic XSS Test Without Filter Evasion: This category includes basic test cases that can be used to test a web application for XSS vulnerabilities without filter evasion. Some examples of basic test cases include input validation bypass, attribute injection, form input injection, URL parameter injection, and cookie injection.
2. Advanced XSS Test With Filter Evasion: This category includes more advanced test cases that can be used to test a web application for XSS vulnerabilities with filter evasion. Some examples of advanced test cases include encoding evasion, HTML tag evasion, script tag evasion, and image tag evasion.
3. XSS Payloads: This category includes a list of XSS payloads that can be used to test a web application for XSS vulnerabilities. Some examples of XSS payloads include simple payloads, alert payloads, cookie stealing payloads, and redirection payloads.
4. Prevention Techniques: This category includes a list of prevention techniques that can be used to protect a web application against XSS attacks. Some examples of prevention techniques include input validation, output encoding, cookie security, and using a Content Security Policy (CSP).

# [XSS Cheatsheet](https://www.codelivly.com/complete-xss-cheatsheet/) Examples

To give you an idea of what’s included in the XSS cheatsheet, here are some examples of basic XSS test cases:

1. Input validation bypass:

- Submit a script tag as input and check if it is rendered as HTML on the page.
- Submit a JavaScript function as input and check if it is executed on the page.
- Submit an HTML tag as input and check if it is rendered as HTML on the page.

1. Attribute injection:

- Submit a script tag as input in an attribute such as `src`, `href`, `onerror`, `onclick`, etc. and check if it is executed on the page.
- Submit an HTML tag as input in an attribute such as `style`, `data`, `title`, etc. and check if it is rendered as HTML on the page.

1. Form input injection:

- Submit a script tag as input in a form field such as `input`, `textarea`, `select`, etc. and check if it is executed on the page.
- Submit an HTML tag as input in a form field such as `input`, `textarea`, `select`, etc. and check if it is rendered as HTML on the page.

1. URL parameter injection:

- Append a script tag to a URL parameter and check if it is executed on the page.
- Append an HTML tag to a URL parameter and check if it is rendered as HTML on the page.

1. Cookie injection:

- Set a cookie with a script tag and check if it is executed on the page.
- Set a cookie with an HTML tag and check if it is rendered as HTML on the page.

# XSS Prevention

Techniques Now that you have an idea of what’s included in the XSS cheatsheet, let’s take a closer look at some prevention techniques you can use to protect your web application against XSS attacks:

1. Input validation: Validate user input to ensure that it meets the expected format and content. This can help prevent malicious code from being injected into your web application.
2. Output encoding: Encode user input before displaying it on the page. This can help prevent malicious code from being executed by the browser.
3. Cookie security : Secure your cookies by using the `HttpOnly` and `Secure` flags. The `HttpOnly` flag prevents JavaScript from accessing cookies, while the `Secure` flag ensures that cookies are only transmitted over HTTPS.
4. Content Security Policy (CSP): Implement a Content Security Policy (CSP) to restrict the types of content that can be loaded on your web page. This can help prevent XSS attacks by blocking the execution of malicious scripts.

# Conclusion

XSS attacks can have serious consequences for web applications and their users. However, by following the prevention techniques outlined in our XSS cheatsheet, you can significantly reduce the risk of XSS vulnerabilities. Remember to always validate user input, encode output, secure your cookies, and use a Content Security Policy to protect against XSS attacks.

With the help of this XSS cheatsheet, you can easily identify and prevent XSS vulnerabilities in your web application. By incorporating these prevention techniques into your web development process, you can protect your users’ data and maintain the security of your web application.
