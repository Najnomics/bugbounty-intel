# Top 50+ XSS Bug Bounty Writeups | Cross-Site Scripting(XSS) Attacks Reports

- **Source URL:** https://medium.com/@proseizala/top-50-xss-bug-bounty-writeups-cross-site-scripting-xss-attacks-reports-700332ed6c87?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240718092720/https://medium.com/@proseizala/top-50-xss-bug-bounty-writeups-cross-site-scripting-xss-attacks-reports-700332ed6c87
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6732 (id 6732)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Top 50+ XSS Bug Bounty Writeups | Cross-Site Scripting(XSS) Attacks Reports

# Playlist Of All Bug Bounty POC : [https://www.youtube.com/playlist?list=PLIudDZbGJAYIhueHWRYndIYrANiC5adXj](https://www.youtube.com/playlist?list=PLIudDZbGJAYIhueHWRYndIYrANiC5adXj)

# What is XSS attack?

**Cross-Site Scripting (XSS)** attacks are a type of injection, where malicious contents are injected into in any case harmless, and confided-in sites. XSS attacks happen when an attacker utilizes a web application to send noxious/malicious code, by and large as program-side content, to an alternate end client.

In the event that the casualty client has restricted admittance inside the application, the attacker could possibly oversee the application’s all’s usefulness and information.

# How many types of XSS attacks?

- Reflected XSS ( Non-Persistent or Type 1)
- Stored XSS ( Persistent or Type 2)
- DOM-Based XSS ( Type-0)

# What is reflected XSS attack?

**Reflected XSS** happens when client input is quickly returned by a web application in a mistake message, output, or whatever other reaction that incorporates some or all of the information given by the client as a part of the request, without that information being made protected to deliver in the program, and without forever putting away the client gave information.

The attacker’s payload must be a part of the request that is sent to the web server. It is then reflected back so that the HTTP reaction incorporates the payload from the HTTP demand.

# What is stored XSS attack?

An attacker utilizes **Stored XSS** to inject pernicious/malicious code (that is payload), most frequently JavaScript code, into the objective application.

**Stored XSS** for the most part happens when client input is put away on the objective server, for example, in a data set, in a message gathering, guest log, remark field, and so on. And afterward, a casualty can recover the stored data information from the web application without that information being made protected to deliver in the program.

# What is DOM-Based XSS attack?

**DOM-based XSS** is a high-level XSS attacks. It is possible to assume that the web application’s client-side contents compose information given by the client to the ***Document Object Model (DOM)***.

If the data are incorrectly taken care of, an attacker can inject a payload, which will be put away as a component of the DOM and executed when the information is read back from the DOM.

A **DOM-based XSS attack** is much of the time a client-side assault and the malicious payload is never shipped off the server.

# How to find XSS vulnerability on a website?

Here’s a general process you can follow when conducting an XSS test on a web application: 1. Identify potential input fields on the web application, such as forms, search bars, and URL parameters.

2\. Attempt to inject known XSS payloads into the fields. A payload is a piece of code inserted into the input field and executed by the victim’s browser.

3\. Monitor the application’s response to the payloads, looking for evidence of successful injection, such as the payload being reflected back in the page or an alert box being displayed.

4\. If you successfully identify a vulnerability, report it to the website’s administrator or security team, along with a detailed description of the issue and how it can be exploited.

5\. The website’s team will then fix the issue and you can then verify the fix. It’s important to note that this process should only be done with explicit permission from the website owner or administrator, and any testing should be done in a controlled environment to avoid causing harm to users. Also, it’s important to note that XSS is not the only security vulnerability to consider when testing web applications. Other common types of vulnerabilities include SQL injection, cross-site request forgery (CSRF), and insecure session management.
