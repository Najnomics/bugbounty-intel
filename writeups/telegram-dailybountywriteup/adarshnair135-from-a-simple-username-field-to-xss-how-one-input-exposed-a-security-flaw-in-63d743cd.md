# From a Simple Username Field to XSS

- **Source URL:** https://medium.com/@adarshnair135/from-a-simple-username-field-to-xss-how-one-input-exposed-a-security-flaw-in-a-government-portal-c7183939ad60
- **Fetched from:** https://medium.com/feed/@adarshnair135
- **Fetched:** 2026-11-20
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14992 (id 14992)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
While performing web application security testing on a government portal, I came across an interesting behavior in its login functionality. What initially appeared to be an ordinary username field turned out to be an entry point for **Cross-Site Scripting (XSS)**.

No complex authentication bypass, advanced exploitation framework, or complicated payload was needed. A simple input field was enough to reveal a client-side security weakness.

### Where It Started

I started examining the login page and its input parameters. Like most authentication pages, the application contained two primary fields:

- Username
- Password

I began testing how the application handled unexpected input in the username parameter.Instead of simply accepting normal usernames, I tested whether the application properly validated and encoded special characters and HTML elements. That’s when things became interesting.

### The Unexpected Behavior

I submitted a XSS Payload in the username field, The request was sent to the application’s login processing endpoint:

POST /jsp/UserLogin.jsp

After examining the server response, I noticed that the submitted username value was reflected back into the HTML response without proper output encoding. The response contained the injected HTML/JavaScript content.

When the resulting page was rendered in the browser, a JavaScript alert dialog appeared.

### Remediation

To prevent similar vulnerabilities, developers should:

1. **Implement context-aware output encoding:** Properly HTML-encode user-controlled values before rendering them.
2. **Avoid unsafe HTML insertion:** Use safe templating mechanisms and avoid directly inserting untrusted data into HTML.
3. **Validate user input:** Apply appropriate server-side validation to username parameters.
4. **Implement Content Security Policy:** Deploy a restrictive CSP as an additional layer of protection.
5. **Perform security testing:** Include reflected and stored XSS testing in regular application security assessments.

Connect me on LinkedIn: linkedin.com/in/adarsh-s-nair-2300b9264/
