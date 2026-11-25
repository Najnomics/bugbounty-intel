# 3 Cases of DOM XSS in Bug Bounty

- **Source URL:** https://medium.com/@kerstan/3-cases-of-dom-xss-in-bug-bounty-0744003f0b2b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105161733/https://medium.com/@kerstan/3-cases-of-dom-xss-in-bug-bounty-0744003f0b2b?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4724 (id 4724)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Subscribed to:** [https://medium.com/@kerstan](https://web.archive.org/web/20240105161733/https://medium.com/@kerstan)

Hi guys, I am Kerstan. Today, I will share you how find DOM XSS in bug bounty from three cases. So, let’s get started.

# What is the Dom XSS?

DOM XSS（Document Object Model Cross-Site Scripting）is a type of cross-site scripting attack that exploits the DOM (Document Object Model) in web pages to inject malicious scripts and execute them in the user’s browser. Attackers manipulate the DOM structure of a webpage to insert malicious scripts, which are then executed in the user’s browser when they visit the webpage. This can lead to security issues such as information disclosure and session hijacking.

Let’s start by learning from the following simple case.

```
var url = window.location.href;
        var newUrl = 'DjamLanding.aspx';
        var splitString = url.split('?url=');
        if (splitString.length > 1) {
            newUrl = splitString[1];
            window.top.location.href = newUrl;
        }
        else {
            // New Url With NO query string
            alert('NO query string');
        }
        window.top.location.href = newUrl;
```
This is a very simple case, with the following JavaScript code logic:

1\. Split the URL parameter using *?url=*

2. Redirect to the specified URL.


Therefore, you can directly add a payload to the `?url=` parameter.

Payload: [https://vulntest.com/xss?url=javascript:alert(1)](https://web.archive.org/web/20240105161733/https://vulntest.com/xss?url=javascript%3Aalert%281%29)

That’s great that you already have a basic understanding of DOM XSS. Now, let’s dive deeper into DOM XSS by learning from the following case. Let’s get started!

# Case 1 The application is retrieving the parameter.

First, let’s consider the example `https://vulntest.com/xss?sca_message=xxxx`. Typically, web applications retrieve specific parameter values from the URL and then write them into the page. So, the key point here is whether we can inject our payload while the application is retrieving the parameter.

Let’s start by learning from the following simple code.

```
var getUrlParameter = function getUrlParameter(sParam) {
        var sPageURL =…
```
