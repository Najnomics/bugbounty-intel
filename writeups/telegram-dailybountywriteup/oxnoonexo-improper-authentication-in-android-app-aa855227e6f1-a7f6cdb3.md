# Improper Authentication in Android App

- **Source URL:** https://medium.com/@oXnoOneXo/improper-authentication-in-android-app-aa855227e6f1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230311181557/https://medium.com/@oXnoOneXo/improper-authentication-in-android-app-aa855227e6f1
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1965 (id 1965)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Improper Authentication in Android App**

\[+\] **Hello friend, This article will be about a simple Improper Authentication vulnerability that allowed me to bypass the lockout behavior of the application on the users’ accounts. The program was providing several accounts with different roles, One of them was Shipper role. I tried to sign into the app and the login request was a Basic Authentication. When i was trying to login i was facing the following pop-up**:

**The request was like**:

```
POST /hub/login HTTP/1.1
Host: api.stage.target.com
Authorization: Basic ZGFzaGlwcGVyXzE5QHRhcmdldC5jb206TGV0bWVpbjEyM0AK
Da-Source: app.android
Content-Type: application/json
Content-Length: 0
Accept-Encoding: gzip, deflate
User-Agent: okhttp/4.9.1
Connection: close
```
**The server returned the JWT of the account and the refresh-token including some fields but the most important field was verified, It was assigned with a *null* value like here**:

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: null
Cache-Control: no-cache
Content-Type: application/json; charset=utf-8
Date: Fri, 06 Jan 2023 17:15:20 GMT
Set-Cookie: hub-token=#DATA
Set-Cookie: refresh-token=#DATA
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Vary: accept-encoding,Origin
X-Frame-Options: DENY
X-Xss-Protection: 1; mode=block
Content-Length: 2620
Connection: Close
{--SNIP--,"verified":null,--SNIP--}
```
**When i tried to login with the other accounts using the android application there were no problems but i noticed the *verified* field in the returned response was *true*, So i tried to do edit the returned response of shipper(disabled)account request by changing the *null=>true* and i managed to login successfully and the MainActivity opened**:

**Thank you for reading, I hope if it was kinda helpful and see you soon❤.**

**Linkedin**: [https://www.linkedin.com/in/abd-elmonsef-sobhy-58542a1a7/](https://www.linkedin.com/in/abd-elmonsef-sobhy-58542a1a7/)

**Facebook**: [https://www.facebook.com/0xno0nex0](https://www.facebook.com/0xno0nex0)
