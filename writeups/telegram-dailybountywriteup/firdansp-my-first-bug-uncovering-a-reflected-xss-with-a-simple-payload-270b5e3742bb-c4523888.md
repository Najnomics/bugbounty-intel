# My first Bug

- **Source URL:** https://medium.com/@firdansp/my-first-bug-uncovering-a-reflected-xss-with-a-simple-payload-270b5e3742bb?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240916060218/https://medium.com/@firdansp/my-first-bug-uncovering-a-reflected-xss-with-a-simple-payload-270b5e3742bb
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7182 (id 7182)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# My first Bug : Uncovering a Reflected XSS with a Simple Payload.

Hello everyone,

Introducing my name Firda Nurelia (on [Linkedin](https://www.linkedin.com/in/firdansp/)). Today, I’m excited to share with you my recent discovery of a Cross-Site Scripting (XSS) vulnerability that I stumbled upon in the subdomain of an application I was testing. If you’re into cybersecurity or just curious about how vulnerabilities are found, stick around!

## The Discovery

On August 15, 2024, while conducting a routine security review on the application at ***https://evil.com***. During this process, I used **subfinder** tools to discover subdomains and found one of interest: ***https://subdomain.evil.com.*** After identifying the subdomain, I registered an account and explored the application to search for potential vulnerabilities. My attention was drawn to a section labeled **“consultant”** that contained input fields which might be susceptible to XSS attacks.

## The Payload

I crafted and tested several payloads, eventually using this simple XSS payload:

`<img src="x" onerror="alert(document.cookie)">`
This payload is designed to trigger an alert box containing the document’s cookies when an image fails to load. Here’s how it works:

- The `src="x"` part of the payload refers to a nonexistent image, causing an error.
- The `onerror="alert(document.cookie)"` attribute triggers a JavaScript alert when the error occurs, displaying the cookies.

This payload is highly effective for detecting XSS vulnerabilities, as it provides immediate feedback (the alert box) when executed.

## The Testing Phase

I navigated to the input fields on the **“consultant”** page, focusing on fields labeled **“FieldOne”** and **“FieldTwo”.** After entering the following payload:

`<img src="x" onerror="alert(document.cookie)">`
I systematically input the payload into these fields, clicked “Simpan” (Save), and **BOOM!** To my surprise, an alert box popped up, displaying the document’s cookies. This confirmed that the application was vulnerable to **Reflected XSS.**

## How It Happened

During my initial exploration, I tested different input fields with a variety of XSS payloads. After multiple failed attempts, I realized that certain input fields were not properly sanitized. Specifically, when I submitted my payload into the **“consultant”** form fields, it was reflected back in the page without being escaped or validated, leading to the execution of my script.

This vulnerability occurred because the web application didn’t adequately filter or sanitize user inputs, making it possible to inject malicious JavaScript code.

## Impact

This vulnerability poses significant risks:

- **Cookie Theft:** Attackers could potentially steal session cookies and impersonate users.
- **Data Breach:** Sensitive user information could be accessed and misused.
- **Reputation Damage:** If users are targeted by such attacks, it could harm the application’s reputation and user trust.

## Remediation

To prevent XSS vulnerabilities, I recommend the following measures:

1. **Validate and Escape User Input:** Ensure that all user inputs are properly validated and escaped before rendering them on the webpage. This means any special characters should be converted to their safe equivalents (e.g., `<` to `<`).
2. **Implement a Content Security Policy (CSP):** Enforce a strict CSP to control which resources (scripts, styles, etc.) can be executed by the browser. This limits the ability of an attacker to inject and execute harmful scripts.
3. **Sanitize Output:** Use libraries such as [DOMPurify](https://github.com/cure53/DOMPurify) to clean and sanitize any user-generated content before displaying it on the website.
4. **Educate Developers:** Developers should be regularly trained on secure coding practices, including common web vulnerabilities such as XSS, and how to avoid introducing them into the codebase.

## References:

1. OWASP: Cross-Site Scripting (XSS)
2. Google Security Blog: XSS Prevention

## **Timeline**

*August 15, 2024 : Discovered the XSS Vulnerability and Report.*

*September 2, 2024 : Respond Team and Provide a Reward Certificate.*


## Conclusion

Finding this XSS vulnerability was both exciting and challenging. It serves as a reminder of the importance of thorough testing and input validation in web development. By addressing these vulnerabilities, we can ensure that web applications are more secure and less prone to attacks.

If you have any questions or want to share your own experiences with XSS or other vulnerabilities, feel free to leave a comment below. Thanks for reading!

So, what’s your first bug? Share it in the comments below!
