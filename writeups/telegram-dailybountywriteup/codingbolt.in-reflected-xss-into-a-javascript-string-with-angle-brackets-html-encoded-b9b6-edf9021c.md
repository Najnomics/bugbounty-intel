# Reflected XSS into a JavaScript string with angle brackets HTML encoded

- **Source URL:** https://medium.com/@codingbolt.in/reflected-xss-into-a-javascript-string-with-angle-brackets-html-encoded-b9b60f4b2823?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240924031026/https://medium.com/@codingbolt.in/reflected-xss-into-a-javascript-string-with-angle-brackets-html-encoded-b9b60f4b2823
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7353 (id 7353)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Reflected XSS into a JavaScript string with angle brackets HTML encoded**

Reflected Cross-Site Scripting (XSS) attacks are one of the most common and dangerous web application vulnerabilities. They occur when an attacker tricks a web application into echoing user input back onto a webpage without proper sanitization or encoding. One interesting attack vector is when user input is reflected inside JavaScript strings, and the angle brackets (\`\<\`, \`>\`) are HTML-encoded, giving the attacker an opportunity to bypass weak security mechanisms and inject malicious code.

In this article, we’ll explore how reflected XSS can occur in JavaScript strings, the role of angle bracket encoding, and how attackers can exploit it to run unauthorized scripts. We’ll also look at effective mitigation strategies to defend against these attacks.

**Understanding Reflected XSS**

Reflected XSS happens when malicious input is sent to a vulnerable web application and is immediately reflected back to the user without being properly handled. This attack usually takes place through a URL or form submission where a user’s input is directly reflected into the HTML or JavaScript of a webpage.

In the context of JavaScript, this becomes dangerous when user input is injected directly into a script block or as part of a JavaScript string. If the input isn’t correctly sanitized or escaped, an attacker can craft a payload that breaks out of the string and inserts malicious JavaScript.

**The Role of Angle Brackets in XSS**

Angle brackets (\`\<\`, \`>\`) are crucial in web-based attacks because they are key components of HTML tags, such as \`\<script>\`. Most developers understand the need to escape or encode these characters to prevent direct HTML injection. For instance:

*\`\<\` is typically encoded as \`<*

*\` \`>\` is typically encoded as \`>\`*

While encoding these characters prevents HTML tag injection, it may not always be sufficient when user input is reflected inside JavaScript code, particularly in strings. Even with angle brackets encoded, an attacker may still be able to break out of the intended JavaScript context and inject executable code.

**A Typical Reflected XSS Scenario in JavaScript Strings**

Let’s look at an example where an attacker can exploit reflected XSS with encoded angle brackets in a JavaScript string.

Imagine the following code on a web page, where user input is reflected inside a JavaScript string:

*\<script> var userName = “User: \<?php echo htmlspecialchars($\_GET\[‘name’\]); ?>”; alert(userName); \</script>*

The PHP function \`htmlspecialchars()\` is being used to encode special characters, including angle brackets. If an attacker tries to inject something like \`\<script>alert(1)\</script>\`, the angle brackets will be encoded as \`<\` and \`>\`, preventing the direct execution of an HTML tag.

So, the reflected value might look like:

*var userName = “User: <script>alert(1)</script>”;*

This would safely render the string without executing the script. However, encoding angle brackets alone is not enough to fully mitigate XSS attacks in JavaScript.

**Breaking Out of the JavaScript String Context**

While angle brackets are encoded, an attacker may still inject characters that allow them to break out of the JavaScript string. For example, consider what happens if the input contains a quote or backslash that isn’t properly escaped:

Attacker input:

*“; alert(‘XSS’); //*

In this case, the input will be reflected as:

*var userName = “User: “; alert(‘XSS’); //”;*

This would result in:

1\. The first part of the string being closed by the injected quote (\`”\`).

2. The \`alert(‘XSS’)\` function being executed immediately afterward.

3. The remainder of the original string being commented out with \`//\`.

Even though the angle brackets are encoded, the attacker has successfully escaped the string context and executed JavaScript. The core issue here is improper handling of the quotes and backslashes used in the input, not the angle brackets.

**Exploiting the Vulnerability**

Here’s how an attacker could craft a working reflected XSS payload:

1\. Understand the context: In this case, the input is being inserted inside a JavaScript string, meaning quotes and backslashes are critical.

2. Craft a payload: The attacker injects a payload that closes the current string, executes their code, and comments out the remainder of the script.


Payload:

*“; alert(‘Hacked!’); //*

This breaks out of the JavaScript string, injects an alert box, and comments out the remaining portion of the original script, making it harmless.

The result:

*\<script> var userName = “User: “; alert(‘Hacked!’); //”; alert(userName); \</script>*

The malicious JavaScript code is successfully injected and executed when the user visits the page with the crafted URL:

*http://vulnerable-site.com/?name=%22%3B%20alert%28%27Hacked%21%27%29%3B%20//*

**Why HTML-Encoding Angle Brackets Alone is Not Enough**

The key takeaway here is that encoding special characters like angle brackets only addresses part of the problem. XSS attacks in JavaScript strings typically rely on breaking out of the string itself using quotes, slashes, or other special characters. Encoded angle brackets prevent tag injection (\`\<script>\`), but they do not stop an attacker from injecting code into the string by manipulating how the browser interprets quotes or other control characters.

Thus, encoding only angle brackets without properly escaping quotes and slashes leaves the application vulnerable to XSS attacks.

**Defending Against Reflected XSS in JavaScript Strings**

To effectively defend against reflected XSS in JavaScript, especially within string contexts, follow these best practices:

1\. Use Proper Escaping for JavaScript: When inserting user-controlled data into JavaScript code, you need to escape not just angle brackets, but also quotes, backslashes, and other potentially dangerous characters. Most languages offer libraries or functions for this purpose. For example:

— In PHP, use \`json\_encode()\` to safely escape and encode data for JavaScript.

— In Python, use \`json.dumps()\` for the same purpose.

Example:

*var userName = “User: \<?php echo json\_encode($\_GET\[‘name’\]); ?>”;*

2\. Validate User Input: Always validate user input on both the client and server side. Ensure that inputs conform to expected formats (e.g., letters, numbers) and reject inputs containing potentially harmful characters.

3\. Context-Aware Output Encoding: Use encoding mechanisms tailored to the context where the data is used. In HTML, use \`htmlspecialchars()\`, but in JavaScript contexts, ensure proper escaping or encoding for JavaScript strings.

4\. Content Security Policy (CSP): A well-implemented Content Security Policy (CSP) can mitigate XSS attacks by restricting which scripts can be executed on a page. CSP won’t prevent XSS, but it can limit its impact.

5\. Regular Security Audits: Perform regular security audits and code reviews to identify and address XSS vulnerabilities. Use automated tools and manual penetration testing to test for XSS flaws in various contexts.

Reflected XSS attacks that target JavaScript strings are a powerful technique for attackers, especially when developers rely on simple HTML encoding of special characters like angle brackets. While encoding \`<\` and \`>\` may prevent basic script tag injection, it is not enough to prevent attackers from escaping JavaScript strings and injecting malicious code. Proper escaping, input validation, and security practices are necessary to defend against this attack vector effectively.

By understanding the nature of reflected XSS and the nuances of encoding within JavaScript, developers can build more secure applications and better protect their users from these dangerous exploits.
