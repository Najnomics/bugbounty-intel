# Stored XSS into anchor href attribute with double quotes HTML-encoded

- **Source URL:** https://medium.com/@codingbolt.in/stored-xss-into-anchor-href-attribute-with-double-quotes-html-encoded-9f384d27aa95?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240923181201/https://medium.com/@codingbolt.in/stored-xss-into-anchor-href-attribute-with-double-quotes-html-encoded-9f384d27aa95?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7352 (id 7352)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Stored XSS into anchor** `href` **attribute with double quotes HTML-encoded**

Cross-Site Scripting (XSS) is one of the most dangerous vulnerabilities in web applications. While XSS typically involves injecting malicious scripts into HTML, it can become even more subtle and effective when targeting specific HTML attributes, such as the \`href\` attribute of anchor tags (\`\<a>\`). A particularly sophisticated vector of attack occurs when the quotes inside the \`href\` attribute are HTML-encoded twice, making detection and exploitation challenging. In this article, we will delve into how stored XSS in an \`href\` attribute with double-encoded quotes can be used maliciously and how to mitigate it.

**What is Stored XSS?**

Stored XSS (also known as persistent XSS) occurs when a malicious payload is stored on a server and later executed in the context of a victim’s browser when they view the compromised content. Unlike reflected XSS, where the payload is delivered via a URL, stored XSS is more dangerous as it affects multiple users without their direct interaction.

**The Role of the \`href\` Attribute in XSS**

The \`href\` attribute in an anchor tag is used to specify the URL a user is directed to when they click the link. Normally, it should only accept well-formed URLs such as ***\`https://example.com\`***. However, if an attacker can inject JavaScript code into the \`href\`, they can execute malicious scripts when a user clicks the link.

A basic XSS injection into the \`href\` attribute looks like this:

*\<a href=”javascript:alert(1)”>Click me\</a>*

However, many modern web applications sanitize their inputs, converting dangerous characters like quotes (\`”\`, \`’\`) into HTML entities such as \`"\` or \`"\`, which makes direct injection harder.

**Double HTML-Encoded Quotes and Bypassing Filters**

To prevent XSS, developers often encode user inputs before rendering them. For example, if an attacker attempts to inject the following payload:

*\<a href=”javascript:alert(1)”>Click me\</a>*

The application may encode it to:

*\<a href=”javascript:alert(1)”>Click me\</a>*

But what if the application encodes the quotes twice? Here’s what happens:

\- A single quote \`”\` becomes \`"\` in HTML encoding.

- When double-encoded, it becomes \`&quot;\`.

An attacker can exploit this behavior by injecting payloads that are expected to be double-encoded. Consider the following scenario:

\- The user input is sanitized, and quotes are converted to HTML entities.

- However, due to a logic flaw, these quotes are encoded twice, introducing an attack vector.

An example payload might look like this when injected:

*\<a href=”http://example.com/?q=search&quot;javascript:alert(1)&quot;">Click me\</a>*

Upon first encoding, this payload might look harmless. However, once rendered in the user’s browser, the browser decodes the \`&\` entities back to \`&\`, leading to this:

*\<a href=”http://example.com/?q=search"e;javascript:alert(1)"e;">Click me\</a>*

Now the payload is successfully injected and can be used to trigger malicious JavaScript, like \`javascript:alert(1)\`.

**Exploitation Example: Crafting the Payload**

Assume you are working with an application that sanitizes input twice and places user input within the \`href\` attribute. The challenge is to bypass the double-encoded quotes. An attacker can craft a payload like this:

1\. Inject a string with encoded quotes:

 *&quot;javascript:alert(1)&quot;*

2\. Once decoded by the browser, it becomes:

 *“javascript:alert(1)”*

3\. If placed inside an \`href\` attribute, this payload can now execute JavaScript when the user clicks the link.

**Crafting a Working Exploit**

Let’s assume we want to inject a payload into the \`href\` attribute. Here’s an attack scenario:

1\. Input into the web form:

 *"javascript:alert(1)"*

2\. This becomes double-encoded by the web application:

 *&quot;javascript:alert(1)&quot;*

3\. In the browser, this is decoded back to:

 *“javascript:alert(1)”*

Now, when a user clicks on the link, it will trigger the \`alert(1)\` JavaScript execution, demonstrating the XSS.

**Mitigations and Best Practices**

To prevent such XSS attacks, it is essential to follow strict security practices:

1\. Proper Input Validation: Ensure that user inputs are validated on both the client and server side. Never trust user input.


2. Context-Aware Escaping: Escaping user input differently based on the context. For example, when user input is included in an HTML attribute, ensure that it is properly HTML-encoded. In this case, double encoding might be a bug, so ensure encoding happens only once.

3\. Avoid JavaScript in \`href\`: Ideally, avoid using \`javascript:\` in \`href\` attributes. Use event handlers like \`onclick\` instead, with proper validation.

4\. Content Security Policy (CSP): Implementing CSP headers can prevent XSS attacks by controlling which scripts are allowed to run in the browser.

5\. Use Trusted Libraries: Use well-established libraries or frameworks that automatically handle input sanitization and encoding, reducing the chances of such vulnerabilities.

6\. Regular Security Audits: Applications should undergo regular security testing, including static analysis, dynamic analysis, and manual penetration testing to identify and fix potential XSS vulnerabilities.

Stored XSS in an \`href\` attribute, especially when combined with double-encoded quotes, is a sophisticated attack vector that can evade traditional input sanitization mechanisms. Understanding how encoding works and how different contexts interpret inputs is crucial in building secure applications. By following best practices in input validation, output encoding, and secure coding practices, you can significantly reduce the risk of XSS vulnerabilities in your applications.
