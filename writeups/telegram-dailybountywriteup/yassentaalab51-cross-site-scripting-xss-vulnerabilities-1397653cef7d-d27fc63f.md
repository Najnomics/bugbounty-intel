# Cross-Site Scripting (XSS) Vulnerabilities

- **Source URL:** https://medium.com/@yassentaalab51/cross-site-scripting-xss-vulnerabilities-1397653cef7d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240819113542/https://medium.com/@yassentaalab51/cross-site-scripting-xss-vulnerabilities-1397653cef7d
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6841 (id 6841)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Cross-Site Scripting (XSS) Vulnerabilities:

# بسم الله، والصلاة والسلام على رسول الله

# الحمد لله الذي عَلَّمَ بالقلم.. عَلَّمَ الإنسانَ ما لم يَعْلَم

# والصلاةُ والسلامُ على خيرِ مُعَلِّمي الناسِ الخير محمد أما بعد

# 1. Introduction

Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser-side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

In the OWASP Top 10 for both 2017 and 2021, XSS ranks high , reflecting its prevalence and impact.

# 2. How XSS Occurs

XSS vulnerabilities occur when data enters a web application from an untrusted source, most frequently a web request, and the data is included in dynamic content sent to a web user without being validated for malicious content. The malicious content, often in the form of JavaScript, HTML, Flash, or other executable code, can then execute in the user’s browser. This can result in transmitting private data, like cookies or session information, to the attacker, redirecting the victim to malicious content, or performing other harmful operations on the user’s machine under the guise of the vulnerable site.

# 3. Types of XSS

# Reflected XSS

Reflected XSS occurs when the injected script is reflected off the web server, such as in an error message, search result, or any other response that includes some or all of the input sent to the server as part of the request. Reflected attacks are typically delivered to victims via another route, such as an email message or a link on another website. When a user is tricked into clicking a malicious link, submitting a specially crafted form, or just browsing a malicious site, the injected code travels to the vulnerable website, which reflects the attack back to the user’s browser. The browser then executes the code because it came from a “trusted” server.

**Example:** Suppose a website has a search function that receives the user-supplied search term in a URL parameter:

`<https://insecure-website.com/search?term=gift>`
The application echoes the supplied search term in the response to this URL:

`<p>You searched for: gift</p>`
An attacker can construct an attack like this:

`<https://insecure-website.com/search?term=><script>alert("xss")</script>`
This URL results in the following response:

`<p>You searched for: <script>alert("xss")</script></p>`
If another user requests the attacker’s URL, the script supplied by the attacker will execute in the victim’s browser, in the context of their session with the application.

# Stored XSS

Stored XSS occurs when the injected script is permanently stored on the target servers, such as in a database, message forum, visitor log, or comment field. The victim retrieves the malicious script from the server when it requests the stored information. Stored XSS is also sometimes referred to as Persistent or Type-II XSS.

**Example:** Suppose a website allows users to submit comments on blog posts, which are displayed to other users. Users submit comments using an HTTP request like the following:

```
POST /post/comment HTTP/1.1
Host: vulnerable-website.com
Content-Length: 100
```
`postId=3&comment=This+post+was+extremely+helpful.&name=Carlos+Montoya&email=carlos%40normal-user.net`
After this comment has been submitted, any user who visits the blog post will receive the following within the application’s response:

`<p>This post was extremely helpful.</p>`
An attacker can submit a malicious comment like this:

`<script>/* Bad stuff here... */</script>`
Within the attacker’s request, this comment would be URL-encoded as:

`comment=%3Cscript%3E%2F*%2BBad%2Bstuff%2Bhere...%2B*%2F%3C%2Fscript%3E`
Any user who visits the blog post will now receive the following within the application’s response:

`<p><script>/* Bad stuff here... */</script></p>`
# DOM-based XSS

DOM-based XSS vulnerabilities usually arise when JavaScript takes data from an attacker-controllable source, such as the URL, and passes it to a sink that supports dynamic code execution, such as `eval()` or `innerHTML`. This enables attackers to execute malicious JavaScript, which typically allows them to hijack other users' accounts.

**Example:**

```
Select your language:
<select><script>
document.write("<OPTION value=1>"+decodeURIComponent(document.location.href.substring(document.location.href.indexOf("default=")+8))+"</OPTION>");
document.write("<OPTION value=2>English</OPTION>");
</script></select>
```
The page is invoked with a URL such as:

`<http://www.some.site/page.html?default=French>`
A DOM-based XSS attack against this page can be accomplished by sending the following URL to a victim:

`<http://www.some.site/page.html?default=><script>alert(document.cookie)</script>`
When the victim clicks on this link, the browser sends a request to `www.some.site`. The server responds with the page containing the above JavaScript code. The browser creates a DOM object for the page, in which the `document.location` object contains the string, including the attacker's payload. This payload manifests itself at the client-side script at runtime, when a flawed script accesses the DOM variable `document.location` and assumes it is not malicious.

For more details about XSS types, I recommend visiting the [OWASP Top 10](https://owasp.org/www-community/attacks/xss/).

# 4. Impact of XSS

The impact of XSS can range from moderate to severe, depending on the type:

- **Reflected and DOM XSS**: Moderate, as they can lead to session hijacking, data theft, or phishing.
- **Stored XSS**: Severe, as it can lead to remote code execution on the victim’s browser, allowing attackers to steal credentials, hijack sessions, or deliver malware.

# 5. Practical Steps to Detect XSS

1. **Identify the Framework**: Use tools like Wappalyzer extension to determine the technologies used.
2. **Find Parameters or Behaviors That Reflect User Input**: Look for input fields, URL parameters, or any user-generated content.
3. **Check for Security Measures**: Verify if input validation, output encoding, and security headers are implemented.
4. **Determine If XSS Is Possible**: Attempt to inject scripts and observe the application’s behavior.

# 6. Mitigation and Prevention

**Input Validation and Sanitization**

All user inputs should be validated and sanitized to remove or escape potentially harmful characters.

```
// Validate and sanitize user input
$input = $_POST['user_input'];
$sanitized_input = filter_var($input, FILTER_SANITIZE_STRING);
```
**Use of Security Headers**

HTTP headers like Content Security Policy (CSP) can significantly mitigate XSS attacks by restricting the sources from which scripts can be loaded.

```
// Content Security Policy (CSP) header
header("Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self';");
// X-Content-Type-Options header
header("X-Content-Type-Options: nosniff");
// X-XSS-Protection header
header("X-XSS-Protection: 1; mode=block");
```
**Output Encoding**

User inputs should be properly encoded before being displayed in the browser to prevent execution of malicious scripts.

```
// Encode output before rendering
$output = "<script>alert('XSS');</script>";
echo htmlspecialchars($output, ENT_QUOTES, 'UTF-8');
```
**Use of Security Libraries and Frameworks**

Using secure coding libraries and frameworks can help prevent XSS vulnerabilities by providing built-in security measures.g built-in security measures.

# 7. Resources and Practice

You can practice XSS detection and exploitation on platforms like:

For real-world scenarios, you can read this report on HackerOne: [XSS Report](https://hackerone.com/reports/881115).
