# WebSec — CSRF/XSRF (Cross-Site Request Forgery)

- **Source URL:** https://medium.com/@meryemddalgali/websec-csrf-xsrf-cross-site-request-forgery-6c048c6323d1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250120110500/https://medium.com/@meryemddalgali/websec-csrf-xsrf-cross-site-request-forgery-6c048c6323d1
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7090 (id 7090)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# WebSec — CSRF/XSRF (Cross-Site Request Forgery)

## What is CSRF and how does it occur?

Cross-Site Request Forgery (CSRF) is the manipulation of the user by the attacker. This manipulation process takes place with various phishing methods. Thus, the target site, where the user completes the authentication process, can perform various activities against the victim’s request by using the user’s cookies (such as transferring money from his account, changing his e-mail address and password). First of all, before analyzing the vulnerability in detail, let’s talk about the basics.

**Cookie:** HTTP is a stateless protocol. Stateless means that it does not keep state information. This means that after the request-response cycle, the next request does not keep any information about what happened in the previous request. Cookies came into our lives at this point. In this way, session information can be tracked on the server side by processing through cookies without taking user information at every request made.

Most web applications perform authentication based on the user’s sessions. After the authentication process is completed, the browser stores a session cookie. The browser then sends the cookie to the registered domain with each request to make the session process easier.

The risk inherent in this mechanism is that cookies are added to the requests sent to the application in systems where the source and how they are sent are not controlled. CSRF vulnerability occurs when necessary precautions are not taken.

## Identifying CSRF

Cross-Site Request Forgery (CSRF) vulnerabilities in the most basic form arise when a malicious actor can trick the victim’s browser into performing an action. However, not every action (API endpoint or method) is vulnerable. Certain conditions have to be met before we can consider a specific endpoint or app route to be vulnerable to CSRF. Let’s take a look at it in detail.

To ensure an API endpoint or app route is susceptible to Cross-Site Request Forgery (CSRF), three main conditions must align:

1. **Privileged Action Requirement:** The target endpoint must perform an action that alters data on behalf of the user. This could involve modifying, adding, or deleting data. Publicly accessible endpoints, such as contact forms, are generally not protected against CSRF, but exploiting them often yields no significant impact.
2. **Session ID with Appropriate SameSite Policy:** For CSRF to be viable, the session ID must be stored in a cookie with the SameSite attribute set to either “None” or “Lax.” If the policy is set to “Strict,” the browser will block the cookie from being sent in cross-origin requests, preventing the attack. Endpoints requiring non-standard headers for authentication are typically safe from CSRF since credentials won’t be forwarded automatically. Exceptions exist when HTTP Basic Authentication or client certificates are in use, as these methods ensure credentials are included in each request.
3. **Absence of Unpredictable Values:** The request should not include any values or tokens that an attacker cannot predict. Developers often implement anti-CSRF tokens in state-changing requests to mitigate this risk. However, vulnerabilities can arise if these tokens are improperly validated or lack randomness.

These conditions create the foundation for CSRF vulnerabilities. Understanding and addressing them is key to protecting your application.

## CSRF Exploitation

Method 1


Sending an HTTP GET request should never cause any data to change. However, some web applications use GET instead of POST, which is suitable for data-change situations.

`GET /transfer?amount=1000&targetaccount=user`
Since this request is from a user who is authenticated in the application, the attacker can manipulate the URL at this point. He can use phishing methods to get the target user who has completed the authentication process to make this request.

For example, the attacker will redirect the victim to his site with a phishing attack and parse the manipulated request in the \<img> tag in the user’s browser (during the parse process, the browser will add cookies to the request), so that the manipulated request will be made by the victim.

`<img src="http://example.com/transfer?amount=999999&targetaccount=hackeraccount">`
Method 2


On a site where no measures are taken against CSRF attack, the admin user can add users with a post request.

As seen in the image below, the attacker uses the payload to get the administrator to add a new user on the target site.

When the victim opens the malicious link sent by the attacker, the attacker’s account will be added.

## Roadmap

I’ve created a roadmap that you can use while testing. I hope it will be useful :)

## Vulnerability Prevention

## SameSite Cookies

Since the behavior of browsers adding cookies causes security problems, the SameSite cookie was created to provide control over cookies. In this definition, we instruct in which cases the cookie can be added in requests triggered from different sources. These definitions:

- Strict: Does not add cookies to requests made from other sources.
- Lax: Does not send cookies to normal cross-site requests, but sends them when a user is navigating to the source site (i.e. following a link). (GET request)
- None: Adds cookies to every request.

Although most modern browsers set SameSite by default (Lax) for all cookies, it should still be set manually in the web application. SameSite alone is not a sufficient measure.

## Anti-CSRF Tokens

Anti CSRF tokens give the user’s browser a token that the browser must then send back. This token must be unique and HTTP requests should only occur after the token has been verified.

In the vulnerability examples above, there was no check on outgoing requests. But now the web server’s token is placed in a session cookie that is sent to the browser after login. Form submissions then contain a hidden field containing the token. If the correct token implementation is done, the CSRF vulnerability is eliminated.
