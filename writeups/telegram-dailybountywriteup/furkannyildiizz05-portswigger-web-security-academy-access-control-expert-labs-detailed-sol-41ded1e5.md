# PortSwigger Web Security Academy Access Control Expert Labs Detailed Solution Series

- **Source URL:** https://medium.com/@furkannyildiizz05/portswigger-web-security-academy-access-control-expert-labs-detailed-solution-series-d5fbbbd7bdbb
- **Fetched from:** https://medium.com/@furkannyildiizz05/portswigger-web-security-academy-access-control-expert-labs-detailed-solution-series-d5fbbbd7bdbb?source=rss-53768bce8ff1------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14949 (id 14949)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Furkannyildiizz / Thu, 15 Oct 2026 14:31:33 GMT

[🇹🇷 Türkçe okumak için tıklayın:](https://medium.com/@furkannyildiizz05/portswigger-web-security-academy-erisim-kontrolu-uzman-lablari-detayli-cozum-serisi-cb967a8d4fc9?sharedUserId=furkannyildiizz05)

Introduction

We have completed 4 expert-level labs from the Access Control module in the PortSwigger Web Security Academy. In this article, we examine how authorization architectures in web applications can fail, the logic behind these vulnerabilities, and step-by-step solution processes in detail.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

Lab 1: URL-Based Access Control Can Be Circumscribed (X-Original-URL)

Definition and Logic:

In modern web architectures, incoming requests are first handled by a front-end system (Reverse Proxy / WAF). This front-end blocks direct external access to sensitive paths like /admin due to security policies. However, if the back-end application supports special HTTP headers like X-Original-URL to track the original path of requests, this security control can be bypassed. While the front-end approves a harmless root request (/), the back-end processes the /admin address specified in the header.

Step-by-Step Solution Process:

1. Directly trying to browse to /admin via the browser results in a front-end block (403 Forbidden).

2. The request is sent to Burp Suite Repeater. The path in the request line is changed to root (/), and the header \`X-Original-URL: /invalid\` is added. Receiving a “not found” response proves that the back-end system processes this header.

3. The header value is updated to \`X-Original-URL: /admin\`. This allows the front-end to pass the request assuming it is safe, while the back-end serves the admin panel.

4. To delete the target user carlos, the header value is modified to \`X-Original-URL: /admin/delete?username=carlos\` and the request is sent to complete the lab.

Lab 2: Method-Based Access Control Can Be Circumscribed

Definition and Logic:

In some web applications, authorization controls implemented for sensitive actions (privilege escalation, user deletion, etc.) are incorrectly tied only to specific HTTP methods (e.g., POST requests only). The developer fails to account for whether the same action could be performed via GET or another method. An unauthorized user can bypass this protection by changing their session cookie and manipulating the request method.

Step-by-Step Solution Process:

1. Log in with the administrator account, escalate a user’s privileges, and locate the resulting request via Burp Suite HTTP History to send it to Repeater.

2. Log out of the admin session and log in with a normal user account.

3. In the Repeater request, replace the administrator session cookie with the normal user’s session cookie.

4. Change the request method from POST to GET using the “Change request method” feature. Since the security filter only checks POST requests, the GET request reaches the back-end unchecked, elevating the normal user to administrator status.

Lab 3: Multi-Step Process with No Access Control on One Step

Definition and Logic:

Critical actions like user authorization or role changes may consist of multiple steps (e.g., confirmation screen and execution screen). In some applications, developers place security checks only on the first step (permission to reach the confirmation screen) but forget to re-verify the user’s privileges on the final execution step. In this case, an attacker can directly trigger the second-step request to perform unauthorized actions.

Step-by-Step Solution Process:

1. Log in with the admin account, perform a user promotion, capture the final multi-step confirmation request in Burp Suite, and send it to Repeater.

2. Log out of the admin session, log in with the normal user account, and copy the normal user’s session cookie value.

3. Replace the session cookie inside the Repeater request with the normal user’s cookie.

4. Adjust the target username inside the request and trigger the final step directly. Since the server does not check privileges at the final result step, the normal user is successfully promoted to administrator.

Lab 4: Referer-Based Access Control

Definition and Logic:

Some web applications rely blindly on the Referer header sent by the browser — which specifies the originating page of the request — instead of secure session cookies to verify whether a sensitive request comes from an authorized source. An attacker can trick the server by writing the admin panel address into the Referer header while sending a request; the server approves the action purely based on the Referer header, regardless of whether the session owner is a normal user.

Step-by-Step Solution Process:

1. Log in with the admin account, promote a user, and send the resulting request to Burp Suite Repeater.

2. Log out and log in with the normal user account, then copy the normal user’s session cookie.

3. Replace the session cookie in the Repeater request with the normal user’s cookie.

4. Ensure the Referer value among the request headers points to the admin panel path. When the request is sent, the server trusts the Referer header instead of checking cookies, successfully elevating the normal user’s privileges.
