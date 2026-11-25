# P3 — Insecure Direct Object Reference (IDOR) in User Profile API

- **Source URL:** https://medium.com/@akashmotkar001/p3-insecure-direct-object-reference-idor-in-user-profile-api-fc105aea6765
- **Fetched from:** https://medium.com/@akashmotkar001/p3-insecure-direct-object-reference-idor-in-user-profile-api-fc105aea6765?source=rss-38c39a01cc6a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14976)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Akash motkar / Tue, 10 Nov 2026 06:23:08 GMT

**Severity:** Medium (P3)

**Vulnerability Type:** Broken Object-Level Authorization (BOLA / IDOR)

**CWE:** CWE-639 — Authorization Bypass Through User-Controlled Key

**OWASP:** API1:2023 — Broken Object Level Authorization

**Suggested CVSS v3.1:** 6.5 (context-dependent)

During security testing, an Insecure Direct Object Reference (IDOR) vulnerability was identified in the application’s user profile API.

The affected endpoint accepts a user-controlled identifier to retrieve profile information. However, the application does not properly verify whether the authenticated user is authorized to access the requested resource.

By modifying the identifier in the API request, an authenticated attacker may be able to access profile information belonging to another user without having the required permissions.

This indicates a lack of proper server-side object-level authorization checks.

The vulnerability is classified as Medium (P3) because it may allow unauthorized access to other users’ information, depending on the sensitivity and scope of the exposed data.

**Endpoint:** [https://target.example/api/v1/user/profile/{user\_id}](https://target.example/api/v1/user/profile/{user_id})

**HTTP Method:** GET

**Affected Functionality:** User Profile Retrieval API

The application returned another user’s profile information after the user identifier was modified.

Example request:

GET /api/v1/user/profile/1002 HTTP/1.1

Host: target.example

Authorization: Bearer \<ACCOUNT\_A\_TOKEN>

Accept: application/json

Example response:

```
{
  "status": "success",
  "user": {
    "id": 1002,
    "name": "Test User B",
    "email": "userb@example.com",
    "phone": "9876543210"
  }
}
```
The response demonstrates that Account A could retrieve Account B’s profile information without proper authorization.

The application should validate ownership and permissions before returning any user-specific information.

If Account A attempts to access Account B’s profile without authorization, the server should reject the request with an appropriate response, such as:

HTTP/1.1 403 Forbidden

Alternatively, the application may return 404 Not Found where resource-existence concealment is appropriate.

An attacker with a valid application account could potentially:

The actual impact depends on the sensitivity of the accessible information and the number of affected records.
