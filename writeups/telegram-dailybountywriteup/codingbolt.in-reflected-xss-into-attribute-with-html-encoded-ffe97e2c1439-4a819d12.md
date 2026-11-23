# Reflected XSS into Attribute with HTML-Encoded

- **Source URL:** https://medium.com/@codingbolt.in/reflected-xss-into-attribute-with-html-encoded-ffe97e2c1439?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240921170804/https://medium.com/@codingbolt.in/reflected-xss-into-attribute-with-html-encoded-ffe97e2c1439
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7338 (id 7338)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS into Attribute with HTML-Encoded

When it comes to web vulnerabilities, Cross-Site Scripting (XSS) stands out as one of the most prevalent and dangerous threats. XSS allows attackers to inject malicious scripts into web pages that unsuspecting users view, potentially leading to session hijacking, data theft, or worse. One specific variant is Reflected XSS, which occurs when an attacker can insert malicious input that is immediately “reflected” back to the user. In this article, we’ll dive deep into a unique form of reflected XSS — where the attack is injected into an HTML attribute, and angle brackets (\`\<\`, \`>\`) are encoded.

We’ll cover how this vulnerability works, its risks, and how to mitigate it effectively.

**What Is Reflected XSS?**

Before diving into the specifics, let’s review \*\*Reflected XSS\*\*. This type of XSS occurs when user input is taken from the browser (often from the URL, form data, or query string), processed by the server, and then immediately reflected back in the response. If this input is not properly sanitized, it can allow an attacker to inject harmful scripts that are executed within the user’s browser.

**Example of Reflected XSS**

Imagine a website that displays a user’s name by taking input from the URL’s query string:

*https://example.com/?name=John*

The server takes the \`name\` parameter from the URL and reflects it back into the page:

*\<p>Welcome, John!\</p>*

If the website does not sanitize this input, an attacker could craft a malicious URL like:

*https://example.com/?name=\<script>alert(1)\</script>*

The server reflects this input directly into the page:

*\<p>Welcome, \<script>alert(1)\</script>!\</p>*

This causes the browser to execute the injected script, leading to a successful XSS attack.

**Reflected XSS into an Attribute with HTML-Encoded Angle Brackets**

Now, let’s talk about a more subtle variant of reflected XSS: when the malicious payload is inserted into an \*\*HTML attribute\*\*, and the angle brackets are \*\*HTML-encoded\*\* (i.e., \`”\<”\` becomes \`<\` and \`”>”\` becomes \`>\`).

**Understanding Attribute Injection**

Consider a website that allows users to enter their favorite color via the URL query string, and it dynamically changes the background color of a specific element:

*\<a href=”#” id=”colorLink” title=”Your favorite color is blue!”>Click me\</a> \<script> var color = new URLSearchParams(window.location.search).get(‘color’); document.getElementById(“colorLink”).setAttribute(“title”, “Your favorite color is “ + color + “!”); \</script>*

If an attacker injects the following payload in the URL:

*https://example.com/?color=red*

It works as intended:

*\<a href=”#” id=”colorLink” title=”Your favorite color is red!”>Click me\</a>*

But what if an attacker tries something more malicious, like injecting a script?

*https://example.com/?color=">\<img src=x onerror=alert(1)>*

The website might HTML-encode the angle brackets to prevent XSS:

*\<a href=”#” id=”colorLink” title=”Your favorite color is "><img src=x onerror=alert(1)>”>Click me\</a>*

At first glance, it looks safe because the angle brackets (\`\<\`, \`>\`) are encoded. However, this is where things get tricky. While encoding the angle brackets might prevent direct execution of a script within the page’s content, it \*\*does not necessarily prevent XSS within an attribute context\*\*.

**Why HTML-Encoded Attributes Can Still Be Vulnerable**

In this case, the attribute (\`title\`) remains vulnerable because the browser will still interpret the double quotes (\`”\`) as ending the \`title\` attribute value. Once the browser closes the attribute, it will interpret the rest of the input (\`>\<img src=x onerror=alert(1)>\`) as a new HTML element. This allows the attacker to inject a malicious image tag with an \`onerror\` event handler, which executes JavaScript.

Here’s what happens:

*\<a href=”#” id=”colorLink” title=”Your favorite color is “>\<img src=x onerror=alert(1)>\</a>*

The browser interprets this as a valid HTML tag and executes the \`onerror\` event, triggering the XSS attack.

**How to Mitigate This Vulnerability**

Now that we understand how reflected XSS in an attribute with HTML-encoded angle brackets works, let’s focus on how to prevent it. This vulnerability can be subtle, but the good news is that effective defenses exist.

**1. Attribute Value Encoding**

One of the most reliable ways to prevent XSS in HTML attributes is to \*\*properly encode all special characters\*\* before inserting them into an attribute. This means not just encoding \`\<\` and \`>\`, but also double quotes (\`”\`) and single quotes (\`’\`), which are used to delineate attribute values.

In JavaScript, this can be done manually:

*function encodeAttribute(input) { return input.replace(/”/g, ‘"’).replace(/’/g, ‘'’).replace(/\</g, ‘<’).replace(/>/g, ‘>’); }*

*var color = new URLSearchParams(window.location.search).get(‘color’); var safeColor = encodeAttribute(color); document.getElementById(“colorLink”).setAttribute(“title”, “Your favorite color is “ + safeColor + “!”);*

By properly encoding these characters, you ensure that user input will be treated as literal text, not executable code.

**2. Use Safe JavaScript Methods**

When setting attributes using JavaScript, always use methods like \`textContent\` or \`setAttribute\` rather than directly manipulating the DOM via \`innerHTML\`. These methods help ensure that user input is treated as text rather than HTML or JavaScript.

For instance, using \`textContent\` would make this code inherently safe:

*var color = new URLSearchParams(window.location.search).get(‘color’); document.getElementById(“colorLink”).textContent = “Your favorite color is “ + color;*

In this case, even if an attacker injects a script, it will be rendered as plain text, not executable code.

**3. Validate User Input**

Another crucial step is to validate all user inputs before reflecting them on the page. If you expect the user to provide a color, ensure that the input is actually a valid color. For example:

*var validColors = \[“red”, “blue”, “green”, “yellow”\]; var color = new URLSearchParams(window.location.search).get(‘color’);*

*if (validColors.includes(color)) { document.getElementById(“colorLink”).setAttribute(“title”, “Your favorite color is “ + color + “!”); } else { alert(“Invalid color!”); }*

By using a whitelist of accepted values, you can completely eliminate the possibility of an XSS attack through this vector.

4\. Content Security Policy (CSP)

Implementing a \*\*Content Security Policy (CSP)\*\* is an excellent additional layer of defense. CSP is a browser feature that allows you to specify which sources are allowed to execute JavaScript on your site. Even if an attacker manages to inject malicious JavaScript, a properly configured CSP can prevent it from running.

Here’s a basic example of a CSP header:

*Content-Security-Policy: script-src ‘self’;*

This ensures that only scripts from your own domain (\`self\`) are allowed to execute, blocking any inline or external scripts injected by an attacker.

Reflected XSS into an attribute with HTML-encoded angle brackets is a subtle but dangerous attack that can bypass simple encoding measures. When user input is reflected into HTML attributes without proper encoding and validation, attackers can exploit this to inject and execute malicious scripts.

**To mitigate this risk:**

\- Always properly encode special characters when inserting user input into attributes.

- Use safe methods like \`setAttribute\` or \`textContent\` instead of manipulating the DOM directly.

- Validate user inputs rigorously, especially if they are reflected into the DOM.

- Implement a Content Security Policy (CSP) to block unauthorized scripts.

By following these best practices, you can effectively prevent XSS attacks and ensure the security of your web application.
