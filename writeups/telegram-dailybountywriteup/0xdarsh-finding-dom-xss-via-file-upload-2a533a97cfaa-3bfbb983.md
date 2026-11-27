# Finding DOM XSS via File Upload

- **Source URL:** https://medium.com/@0Xdarsh/finding-dom-xss-via-file-upload-2a533a97cfaa?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@0Xdarsh
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 7490)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
As a pentester or bug hunter, discovering vulnerabilities in web applications can be both challenging and rewarding. One common vector that deserves attention is DOM-based Cross-Site Scripting (DOM XSS). we’ll dive into a specific case involving the Dropify file upload library, highlighting how a seemingly innocuous feature can be exploited.

**Understanding DOM XSS:**DOM XSS occurs when client-side scripts modify the Document Object Model (DOM) in a way that allows attackers to inject malicious scripts. Unlike traditional XSS, where server-side processing is involved, DOM XSS exploits vulnerabilities directly in the browser.

**The Vulnerability: Dropify’s Filename Handling**Dropify is a popular jQuery plugin used for file uploads, often integrated into web applications for its sleek interface and functionality. However, a crucial line in its code can introduce a DOM XSS vulnerability:

*this.filenameWrapper.children(“.dropify-filename inner”).html(this.file.name);*

In this line, the plugin dynamically sets the inner HTML of an element based on the uploaded file’s name. If this name isn’t properly sanitized, an attacker can exploit it to execute arbitrary JavaScript.

**The Exploit: Uploading a Malicious File**

To exploit this vulnerability, follow these steps:

Craft the Payload: Choose a filename that includes a malicious script. For example:

*\<img src=x onerror=alert(‘XSS’)>*

By embedding this payload in an image file’s name, it can be executed when the file is uploaded.

Upload the File: Using the file upload feature in the application, upload the crafted file. Since the Dropify plugin directly injects the filename into the HTML without escaping it, the script will be executed when the file name is displayed.

Trigger the XSS: Once the file is uploaded and the application attempts to display the filename, the injected script will execute.

**Impact of the Vulnerability:**The potential impact of this vulnerability can be severe. An attacker could execute scripts in the context of the user’s session, manipulate the DOM, or redirect users to malicious sites. The risk increases significantly in applications handling sensitive data or user authentication.

**Mitigating the Risk:**

To prevent DOM XSS vulnerabilities like this one, developers should implement the following best practices:

Sanitize Input: Always sanitize and escape user input, especially when incorporating it into the DOM. Use libraries that handle sanitization for you.

- Use Text Instead of HTML: Instead of using .html(), consider using .text() to set text content safely, as it doesn’t interpret HTML tags.
- Content Security Policy (CSP): Implement a strong CSP to limit the execution of scripts and mitigate the risk of XSS attacks.
- Regular Security Audits: Regularly audit your code and third-party libraries for vulnerabilities. Stay updated with security patches and community advisories.

*Stay vigilant, and happy hunting!*
