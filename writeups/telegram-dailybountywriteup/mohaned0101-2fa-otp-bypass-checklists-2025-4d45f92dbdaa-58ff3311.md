# 2fa, OTP bypass checklists 2025

- **Source URL:** https://medium.com/@mohaned0101/2fa-otp-bypass-checklists-2025-4d45f92dbdaa?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250821174944/https://medium.com/@mohaned0101/2fa-otp-bypass-checklists-2025-4d45f92dbdaa
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9657 (id 9657)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 2fa, OTP bypass checklists 2025

**Summary:**

This collection of 2FA bypass techniques has been gathered from various bug bounty write-ups, security research reports, and real-world examples. It showcases different methods attackers have used to bypass 2-factor authentication mechanisms across multiple applications.

1. Bypass via Removing Parameters

```
Original Request:
email=example.com&password=1234&token=vsa1adgnh
Bypass:
email=example.com&password=1234
```
2\. Lack of CSRF Protection on Disabling 2FA

```
Request:
GET /api/v1/mfaTurnOff HTTP/1.1  
Host: staging.example.com  
Cookie: some_imp_cookies  
User-Agent: browser  
Accept: application/json, text/plain, */*  
Origin: https://example.com
Bypass:
Generate a CSRF PoC for the request and send it to the victim.
 When the victim clicks the link, their 2FA will be disabled.
```
3\. Clickjacking

`Test if you can disable 2FA via clickjacking.`
4\. Direct Endpoint Access


Original URL:

https://example.com/2fa


Bypass:

https://example.com/home


Steps:

After login, change the URL directly to the homepage.
5\. Token Reuse

`Check if the same 2FA/OTP code can be reused multiple times.`
6\. Use Attacker’s OTP Code on Victim’s Account

`Request OTP for your account and reuse the same code on the victim’s account.`
7\. Brute Force Attacks

```
Check for lack of rate limiting on OTP requests.
Bypass techniques:
- Add spoofed IP headers:
 X-Forwarded: 127.0.0.1
 X-Forwarded-For: 127.0.0.1
 X-Forwarded-Host: 127.0.0.1
 X-Client-IP: 127.0.0.1
 X-Remote-IP: 127.0.0.1
 X-Remote-Addr: 127.0.0.1
 X-Host: 127.0.0.1
 X-Real-IP: 127.0.0.1
 X-HTTP-Method-Override: POST
 X-Original-URL: /mfa
 X-Originating-IP: 127.0.0.1
some time you need to add two headers  
- Change User-Agent
- Case sensitivity: `/OTP` vs `/OTp`
- HTTP method switch: GET, POST, PUT, PATCH, DELETE
- Modify route: `/OTP/.` or `/OTP/..`
- IP rotation using proxies
- Host header injection: `Host: 127.0.0.1`
- Cookie/session rotation after X requests
```
8\. Drop Request That Enforces 2FA


After login, the app makes:

GET /2FA HTTP/1.1


Bypass:

Drop this request entirely.
9\. Response Manipulation

```
Original Response:
403 Forbidden  
"login": false
Bypass:
200 OK  
"login": true
Modify the client-side response to simulate a successful login.
```
10\. Bypassing 2FA in Password Reset

`No rate limiting found on OTP validation during password reset.`
11\. Bypass via Valid Token in Response


The token is leaked in the login response.

Take the token and use it in further requests manually.
12\. Use Attacker’s 2FA Token on Victim

```
The server does not validate if the 2FA token belongs to the logged-in user.
Use your own token and attacker’s email in victim's session.
```
13\. Bypass by Not Accepting Cookie Policy

```
Steps:
1. Clear cache.
2. Visit video URL directly.
3. Login without accepting cookie policy.
Result: 2FA prompt is skipped.
```
14\. Change Number/Email to Victim’s

```
Intercept the request after entering OTP.  
Modify the email/number to that of the victim.
```
15\. JSON to Array Bypass

```
Original:
{
  "email": "victim@a.com"
}
Bypass:
{
  "email": [
    "victim@a.com",
    "attacker@a.com"
  ]
}
```
16\. Change Content-Type for Bypass

```
Original:
"user[email]": "victim@gmail.com"
Bypass:
"user": {
  "email": [
    "victim@gmail.com",
    "attacker@gmail.com"
  ]
}
```
- Use Burp Suite + Content-Type Converter extension.

17\. Change HTTP Method (POST → PUT)

`Change method from POST to PUT, PATCH, DELETE, or GET.`
18\. Bypass via Static OTP (e.g. `000000`)

``Try submitting OTP value as `000000`.``
19\. Inspect JS for OTP Value

```
Inspect the "Continue" button → see function: `checkOTP(event)`.  
Type it in browser console to reveal OTP in debugger.
```
20\. Source Code Inspection

21\. OTP Code Leak in Cookie

`OTP stored in a cookie` 22\. Bypass by Changing OTP Parameter to Boolean

```
Original:
"otp": "2211"
Bypass:
"otp": true
```
23\. Client-Side Bypass via CSS

```
Inspect the OTP popup → add `display: none;` in CSS.  
Now interact with the page behind the popup.
```
24\. session valid for one month

```
Steps:
1. Go to https://www.drugs.com/account/register/ and create an account using an email you own.
2. Complete OTP verification and select "Trust this device for 1 month". This gives you a valid session that does not require 2FA for one month.
3. Go to https://www.drugs.com/account/details/ and change the email to the victim's email (User B)
    - Now, the attacker has a valid session associated with User B's email for one month, bypassing 2FA.
4. Log out and log back in to confirm that the application doesn't prompt for OTP.
```
25\. Send a request after login

`after login send request to api that register for authy app or if you can send request that disable mfa`
Here all done. If you have a new bypass idea, share it in the comments.
