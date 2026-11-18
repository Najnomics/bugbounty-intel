# P2 Broken Access Control Allowing Unauthorized Account Email Modification and Account Takeover

- **Source URL:** https://medium.com/@akashmotkar001/p2-broken-access-control-allowing-unauthorized-account-email-modification-and-account-takeover-dea75b86edf1
- **Fetched from:** https://medium.com/feed/@akashmotkar001
- **Fetched:** 2026-11-18
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14987 (id 14987)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Severity:** P2 — High

**Vulnerability Type:** Broken Access Control / Account Takeover

**Bugcrowd VRT:** Broken Access Control → Privilege Escalation / Account Takeover

**CWE:**

- CWE-639 — Authorization Bypass Through User-Controlled Key
- CWE-862 — Missing Authorization
- CWE-284 — Improper Access Control

**OWASP:** A01:2025 — Broken Access Control

**Suggested CVSS v3.1:** 8.1 (High), subject to the actual attack prerequisites and impact.

### 1. Description

During security testing, a potential broken access control vulnerability was identified in an application’s account management functionality.

The application allows authenticated users to update account information, including their registered email address. However, the backend does not properly validate whether the authenticated user is authorized to modify the targeted account.

An attacker with a valid low-privileged account may be able to manipulate user-identification parameters in account update requests and modify the email address associated with another user’s account.

If the application accepts the unauthorized modification without requiring ownership verification or re-authentication, an attacker could potentially replace a victim’s registered email address with an attacker-controlled address.

This could compromise the integrity of the victim’s account and potentially enable account takeover through subsequent password-reset or email-verification workflows.

The vulnerability represents a significant authorization failure because sensitive account-management operations are not adequately restricted to the legitimate account owner.

### 2. Affected Component

**Component:** User Account Management API

**HTTP Method:** POST / PUT / PATCH (depending on implementation)

**Affected Functionality:** Account Email Modification

**Authentication Required:** Yes, valid attacker account.

**Authorization Required:** Ownership of the targeted account.

### 3. Steps to Reproduce

### Prerequisites

- Two authorized test accounts.
- Burp Suite Professional or Community.
- A browser with an authenticated application session.

### Step 1Authenticate using Account A

Log in to the application using a valid test account controlled by the tester.

Navigate to the account settings or profile management section.

### Step 2 Intercept the email modification request

Change the registered email address of Account A and intercept the corresponding HTTP request using Burp Suite.

Example:

POST /api/v1/account/update HTTP/1.1

Host: \<application-host>

Authorization: Bearer \<ACCOUNT\_A\_TOKEN>

Content-Type: application/json

```
{
  "user_id": "1001",
  "email": "attacker@example.com"
}
```
### Step 3 Identify user-controlled account parameters

Inspect the intercepted request and identify parameters responsible for selecting the account being modified.

In this example, the application uses the user\_id parameter to identify the target account.

### Step 4 Modify the target account identifier

Replace Account A’s identifier with the identifier of another authorized test account (Account B).

Example:

```
{
  "user_id": "1002",
  "email": "attacker@example.com"
}
```
Keep the authenticated session associated with Account A.

### Step 5 Submit the modified request

Forward the modified request to the application server.

Observe whether the server accepts the modification and returns a successful response.

### Step 6 Verify unauthorized account modification

Using the separately controlled Account B, verify whether its registered email address has been modified.

If the application accepts the modification without verifying account ownership, the broken access control vulnerability is confirmed.

### Step 7 Evaluate account takeover impact safely

In an authorized test environment, determine whether changing the registered email address affects account recovery or authentication workflows.

Do not attempt to access another person’s account. Use only controlled test accounts to validate the potential account takeover impact.

### 4. Security Impact

The vulnerability may have significant consequences for application users.

**1. Unauthorized Account Modification**

An attacker may modify sensitive account information belonging to another user without appropriate authorization.

**2. Account Takeover Risk**

If the email modification changes the account’s recovery destination without independent verification, an attacker may potentially gain control over subsequent password-reset workflows.

**3. Loss of Account Integrity**

Legitimate users may lose control over their registered account information and recovery settings.

**4. Unauthorized Access to Account Resources**

Successful account takeover could expose information and functionality available to the compromised account.

**5. Business and Reputational Impact**

Unauthorized account modifications and potential account compromise could undermine user trust and create additional incident-response and recovery costs.

### 5. Root Cause Analysis

The root cause is insufficient server-side authorization validation during sensitive account-management operations.

The backend appears to rely on a user-controlled account identifier without adequately verifying that the authenticated user owns the targeted account.

Sensitive operations such as email modification must be authorized using the authenticated server-side identity rather than trusting identifiers supplied by the client.

### 6. Remediation

1. Derive the account identity from the authenticated server-side session rather than trusting user-controlled identifiers.
2. Enforce object-level authorization checks on every account-management request.
3. Require ownership verification before changing registered email addresses.
4. Send a verification link to the new email address before applying the change.
5. Require re-authentication for sensitive account-management operations.
6. Notify the existing registered email address when account recovery information changes.
7. Invalidate relevant sessions or recovery tokens when appropriate.
8. Implement automated authorization tests to prevent cross-account modification vulnerabilities.

### 7. Classification

AttributeClassificationVulnerabilityUnauthorized Account Email ModificationSeverityP2 — HighBugcrowd PriorityP2CWECWE-639, CWE-862, CWE-284OWASPA01:2025 — Broken Access ControlCategoryAccount Takeover / Broken Access ControlAttack VectorNetworkPrivileges RequiredLowUser InteractionNoneStatusIllustrative — Requires Validation
