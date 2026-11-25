# Finding “BAC - IDOR -PE” Within a Minute using Autorize Tool

- **Source URL:** https://medium.com/@Cyber_siva/finding-bac-idor-pe-within-a-minute-using-autorize-tool-5aad4f0b563f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012143958/https://medium.com/@Cyber_siva/finding-bac-idor-pe-within-a-minute-using-autorize-tool-5aad4f0b563f?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3560 (id 3560)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Finding “BAC - IDOR -PE” Within a Minute using Autorize Tool

--

Hello People,

I would like to say thanks to you all before I start the blog because I got a lot of views and responses for the “**Command Injection Vulnerability via File Upload**” If you are new to my blogs Just check my Profile and read the blogs.

Today we going to see one interesting tool in Burp that helps you to Find the “**Broken Access Control, IDOR, and Privilege Escalation**” Vulnerabilities within 5 Minutes by Browsing the application.

You don’t believe it, right? Let’s try my steps to find those vulnerabilities.

# What is Autorize?

Autorize is an automatic authorization enforcement detection extension for Burp Suite. It was written in Python by Barak Tawily, an application security expert. Autorize was designed to help security testers by performing automatic authorization tests. With the last release now Autorize also performs automatic authentication tests.

# Installation

1. Download Burp Suite (obviously): [http://portswigger.net/burp/download.html](https://web.archive.org/web/20231012143958/http://portswigger.net/burp/download.html)
2. Download Jython standalone JAR: [http://www.jython.org/download.html](https://web.archive.org/web/20231012143958/http://jython.org/download.html)
3. Open burp -> Extender -> Options -> Python Environment -> Select File -> Choose the Jython standalone JAR
4. Install Autorize from the BApp Store or follow these steps:
5. Download the Autorize.py file.
6. Open Burp -> Extender -> Extensions -> Add -> Choose Autorize.py file.
7. See the Autorize tab and enjoy automatic authorization detection :)

# How to use it?

1. After installation, the Autorize tab will be added to Burp.
2. Open the configuration tab (**Autorize -> Configuration**).
3. Get your **low-privileged user authorization token** header (Cookie / Authorization) and copy it into the textbox containing the text “**Insert injected header here**”. Note: Headers inserted here will be replaced if present or added if not.
4. Uncheck “**Check unauthenticated**” if the authentication test is not required (request without any cookies, to check for authentication enforcement in addition to authorization enforcement with the cookies of the low-privileged user)
5. Check “**Intercept requests from Repeater**” to also intercept the requests that are sent through the Repeater.
6. Click on “**Intercept is off**” to start intercepting the traffic in order to allow Autorize to check for authorization enforcement.
7. Open a browser and configure the proxy settings so the traffic will be passed to Burp.
8. Browse to the application you want to test with a **high privileged user.**
9. The Autorize table will show you the request’s URL and enforcement status.
10. It is possible to click on a specific URL and see the original/modified/unauthenticated request/response in order to investigate the differences.

# Authorization Enforcement Status:

# There are 3 enforcement statuses:

1. Bypassed! — Red color
2. Enforced! — Green color
3. Is enforced??? (please configure enforcement detector) — Yellow color

*Note: “Bypassed” means you can access that page directly with Low Privileged users and sometime that page will lead to PE vulnerability and it depends on the application.*


The first 2 statuses are clear, so I won’t elaborate on them.

The 3rd status means that Autorize cannot determine if authorization is enforced or not, so Autorize will ask you to configure a filter in the enforcement detector tabs. There are two different enforcement detector tabs, one for the detection of the enforcement of low-privileged requests and one for the detection of the enforcement of unauthenticated requests.

The enforcement detector filters will allow Autorize to detect authentication and authorization enforcement in the response of the server by content length or string (literal string or regex) in the message body, headers, or in the full request.

# For example:

if there is a request enforcement status that is detected as “**Authorization enforced???** (please configure enforcement detector)” it is possible to investigate the modified/original/unauthenticated response and see that the modified response body includes the string “You are not authorized to perform action”, so you can add a filter with the fingerprint value “You are not authorized to perform action”, so Autorize will look for this fingerprint and will automatically detect that authorization is enforced. It is possible to do the same by defining a content-length filter or fingerprint in headers.

Don’t Forget to “**Follow me”** for interesting blogs and share maximum.

Thanks for Reading and Happy Hacking…☺
