# P2 Password Reset Token Not Invalidated After Successful Password Change

- **Source URL:** https://medium.com/@akashmotkar001/p2-password-reset-token-not-invalidated-after-successful-password-change-ad251de19a39
- **Fetched from:** https://medium.com/feed/@akashmotkar001
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14994 (id 14994)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Severity:** P2 — High (subject to validation)

**Vulnerability Type:** Authentication Weakness / Improper Session and Token Management

**CWE:**

- CWE-613 — Insufficient Session Expiration
- CWE-640 — Weak Password Recovery Mechanism for Forgotten Password
- CWE-287 — Improper Authentication

**OWASP:** A07:2025 — Authentication Failures

### 1. Description

The password recovery functionality may fail to invalidate a password-reset token after it has been successfully used to change an account password.

A password-reset token is intended to be a temporary, single-use credential that authorizes one password-reset operation. Once the password has been changed, the token should immediately become invalid.

If the application continues accepting the previously consumed token, an attacker who obtains that token may be able to reuse it to perform additional password changes.

Depending on the implementation, this could allow repeated unauthorized password modifications and potentially compromise the victim’s account.

The issue becomes particularly serious when reset tokens remain valid for an extended period or are not invalidated after successful password changes.

### 2. Affected Component

**Component:** Password Recovery / Reset Functionality

**HTTP Method:** POST

**Affected Functionality:** Password Reset API

**Authentication Required:** Possession of a valid password-reset token.

### 3. Steps to Reproduce

### Prerequisites

- Two controlled test accounts or one account with a repeatable password-reset workflow.
- Access to the associated test email inbox.
- Burp Suite.

### Step 1Request a password reset

Navigate to the application’s password recovery page and request a reset link for a controlled test account.

Retrieve the reset token from the email received.

### Step 2 Intercept the password reset request

Open the reset link and intercept the corresponding request using Burp Suite.

Example:

POST /api/v1/auth/reset-password HTTP/1.1

Host: \<application-host>

Content-Type: application/json

```
{
  "token": "<RESET_TOKEN>",
  "new_password": "TestPassword@123"
}
```
### Step 3 Complete the password reset

Forward the request and confirm that the application successfully changes the account password.

Record the response and retain the original reset token for testing.

### Step 4 Replay the consumed reset token

Send the same reset request again, using the previously consumed token but a different test password.

Example:

```
{
  "token": "<PREVIOUSLY_USED_RESET_TOKEN>",
  "new_password": "AnotherTestPassword@456"
}
```
### Step 5 Analyze the server response

Observe whether the application accepts the previously consumed token and returns a successful response.

### Step 6 Verify the behavior

Using the controlled test account, verify whether the second password change actually occurred.

A successful HTTP response alone is insufficient to confirm the vulnerability. The second password change must be demonstrated.

### 4. Security Impact

**Unauthorized Password Modification:** A previously consumed reset token may remain usable for additional password changes.

**Account Compromise:** An attacker possessing a valid reset token may be able to repeatedly modify the account password.

**Persistence of Unauthorized Access:** If the token remains valid after the legitimate user resets their password, the attacker may retain a password-reset capability.

**Loss of Account Control:** The legitimate account owner may lose control over their account if an attacker successfully reuses the token.

### 5. Root Cause Analysis

The likely root cause is inadequate lifecycle management of password-reset tokens.

The application may validate token authenticity and expiration without tracking whether the token has already been consumed.

A secure implementation must enforce single-use token semantics and invalidate the token atomically when the password-reset operation succeeds.

### 6. Remediation

1. Enforce single-use password-reset tokens.
2. Invalidate the reset token immediately after a successful password change.
3. Store token consumption state server-side.
4. Use cryptographically secure, unpredictable reset tokens.
5. Enforce short token expiration periods.
6. Invalidate outstanding reset tokens when a password is changed.
7. Ensure token validation and consumption occur atomically to prevent replay and race conditions.
8. Notify the account owner after a successful password change.
9. Log password-reset activity and monitor suspicious repeated attempts.

### 7. Classification

AttributeClassificationVulnerabilityPassword Reset Token ReplaySeverityP2 — High (conditional)CWECWE-613, CWE-640, CWE-287OWASPA07:2025 — Authentication FailuresAttack VectorNetworkPrivileges RequiredNone beyond possession of the tokenUser InteractionDepends on token acquisitionStatusIllustrative — Requires Validation
