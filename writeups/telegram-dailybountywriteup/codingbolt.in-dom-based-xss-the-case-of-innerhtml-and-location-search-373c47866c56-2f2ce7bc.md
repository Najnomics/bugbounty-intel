# DOM-based XSS

- **Source URL:** https://medium.com/@codingbolt.in/dom-based-xss-the-case-of-innerhtml-and-location-search-373c47866c56?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240921161116/https://medium.com/@codingbolt.in/dom-based-xss-the-case-of-innerhtml-and-location-search-373c47866c56
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7334 (id 7334)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# DOM-based XSS: The Case of \`innerHTML\` and \`location.search\`

Cross-Site Scripting (XSS) is a well-known web vulnerability that allows attackers to inject malicious scripts into web pages viewed by others. One particular variant, DOM-based XSS, occurs when the attack is based on changes in the Document Object Model (DOM) rather than server responses. This form of XSS can be tricky because it doesn’t involve server-side scripts — it’s all about how client-side JavaScript handles data.

**What’s DOM-based XSS?**

DOM-based XSS occurs when a web page’s JavaScript manipulates data in the DOM without properly validating or escaping it. In this case, the flaw lies in the JavaScript code itself, which takes input directly from the browser (often via the URL or form fields) and injects it into the page’s DOM.

**The Sink: \`innerHTML\`**

A sink in security terms is the function or process where untrusted data can lead to the execution of malicious code. One of the most commonly abused sinks in XSS attacks is \`innerHTML\`. It directly sets HTML content on the page, which can include \`\<script>\` tags and allow JavaScript execution. This makes it particularly dangerous if untrusted input is used to set its value.

*\<div id=”output”>\</div> \<script> var input = location.search; // Get data from URL document.getElementById(“output”).innerHTML = input; \</script>*

In the example above, the \`innerHTML\` sink is vulnerable because the value of \`location.search\` — which refers to the query string in the URL — is directly injected into the page without sanitization. If the query string contains malicious JavaScript, that code will be executed within the page’s context.

**The Source: \`location.search\`**

The \*\*source\*\* of an XSS vulnerability is the point where user input is introduced into the program. In this case, \`location.search\` serves as the source. This object contains everything after the \`?\` in the URL, and if user-controlled, it can be manipulated to inject malicious payloads.

For example, if the URL is:

*https://example.com/page?name=\<script>alert(1)\</script>*

The \`location.search\` part will be \`?name=\<script>alert(1)\</script>\`. When the script processes this untrusted data and assigns it to \`innerHTML\`, the browser interprets it as part of the DOM, resulting in a JavaScript alert:

*\<div id=”output”>\<script>alert(1)\</script>\</div>*

This is a typical DOM XSS attack: input from the URL is used to modify the DOM in a dangerous way, leading to script execution.

**How to Prevent This?**

Mitigating DOM-based XSS requires developers to be vigilant about how they handle user input. Below are some best practices to follow:

**1. Avoid Using \`innerHTML\`**

Where possible, avoid using \`innerHTML\` to directly set content. Instead, use safer alternatives like \`textContent\` or \`innerText\` that don’t allow HTML tags to be parsed:

*document.getElementById(“output”).textContent = input;*

This approach will render the text \`\<script>alert(1)\</script>\` literally, without executing it.

**2. Sanitize User Input**

If you absolutely need to work with HTML, make sure to sanitize input. There are libraries like DOMPurify that can strip harmful content from user inputs:

*var cleanInput = DOMPurify.sanitize(input); document.getElementById(“output”).innerHTML = cleanInput;*

**3. Validate Input Early**

It’s always good practice to validate and sanitize user input as soon as it’s received, ensuring that no malicious data gets processed by the application.

*function sanitizeURLParameter(param) { return param.replace(/\</g, “<”).replace(/>/g, “>”); } var safeInput = sanitizeURLParameter(input); document.getElementById(“output”).innerHTML = safeInput;*

DOM-based XSS, particularly involving \`innerHTML\` and \`location.search\`, is a common but dangerous vulnerability. As developers, we need to be aware of how we handle user input within the browser’s environment. By following best practices like using safer DOM manipulation methods and sanitizing input, we can reduce the risk of XSS attacks and keep our users safe.

Stay vigilant and always treat user input with caution!
