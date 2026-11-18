# P3 — Insecure Direct Object Reference (IDOR) in User Profile API

- **Source URL:** https://medium.com/@akashmotkar001/p3-insecure-direct-object-reference-idor-in-user-profile-api-fc105aea6765
- **Fetched from:** https://medium.com/feed/@akashmotkar001
- **Fetched:** 2026-11-18
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14976)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Severity:** Medium (P3)

**Vulnerability Type:** Broken Object-Level Authorization (BOLA / IDOR)

**CWE:** CWE-639 — Authorization Bypass Through User-Controlled Key

**OWASP:** API1:2023 — Broken Object Level Authorization

**Suggested CVSS v3.1:** 6.5 (context-dependent)

### Description

During security testing, an Insecure Direct Object Reference (IDOR) vulnerability was identified in the application’s user profile API.

The affected endpoint accepts a user-controlled identifier to retrieve profile information. However, the application does not properly verify whether the authenticated user is authorized to access the requested resource.

By modifying the identifier in the API request, an authenticated attacker may be able to access profile information belonging to another user without having the required permissions.

This indicates a lack of proper server-side object-level authorization checks.

The vulnerability is classified as Medium (P3) because it may allow unauthorized access to other users’ information, depending on the sensitivity and scope of the exposed data.

### Affected Component

**Endpoint:** [https://target.example/api/v1/user/profile/{user\_id}](https://target.example/api/v1/user/profile/{user_id})

**HTTP Method:** GET

**Affected Functionality:** User Profile Retrieval API

### Steps to Reproduce

1. Log in to the application using a valid test account (Account A).
2. Navigate to the user profile section.
3. Intercept the profile API request using Burp Suite.
4. Send the intercepted request to Burp Suite Repeater.
5. Identify the user identifier in the request URL or parameters.
6. Replace the original user identifier with another valid test account’s identifier (Account B).
7. Forward the modified request to the server.
8. Examine the HTTP response.
9. Verify whether the application returns Account B’s profile information while the request is authenticated as Account A.
10. Repeat the test with accounts you control to confirm the authorization weakness.

### Observed Result

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

### Expected Result

The application should validate ownership and permissions before returning any user-specific information.

If Account A attempts to access Account B’s profile without authorization, the server should reject the request with an appropriate response, such as:

HTTP/1.1 403 Forbidden

Alternatively, the application may return 404 Not Found where resource-existence concealment is appropriate.

### Security Impact

An attacker with a valid application account could potentially:

- Access other users’ profile information.
- Retrieve personal information not intended for them.
- Enumerate user identifiers to identify additional accessible records.
- Collect information that could support targeted phishing or social engineering.
- Combine the vulnerability with other weaknesses to facilitate further attacks.

The actual impact depends on the sensitivity of the accessible information and the number of affected records.

### Remediation

1. Implement server-side object-level authorization checks on every API request.
2. Verify that the authenticated user has permission to access the requested resource.
3. Never rely exclusively on user-supplied object identifiers.
4. Apply ownership validation before retrieving or modifying user records.
5. Implement role-based access control where applicable.
6. Review all API endpoints that accept user IDs, account IDs, document IDs, or other object references.
7. Add automated authorization tests covering cross-user access attempts.
8. Log and monitor suspicious attempts to access resources belonging to other users.
