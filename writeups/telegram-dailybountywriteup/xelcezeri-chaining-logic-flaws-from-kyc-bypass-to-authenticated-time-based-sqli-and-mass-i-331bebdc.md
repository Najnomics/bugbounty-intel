# Chaining Logic Flaws

- **Source URL:** https://medium.com/@xelcezeri/chaining-logic-flaws-from-kyc-bypass-to-authenticated-time-based-sqli-and-mass-idor-0425f362dad5?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@xelcezeri
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 13462)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### 1. Entry Point: Phone Verification (KYC) Bypass

The application enforces a mandatory phone verification step after registration at a specific gate. However, this was implemented as a weak client-side redirect.

- **Vulnerability:** Broken Access Control / Bypass.
- **Methodology:**

1. Register a new account.
2. Intercept the redirect to the verification endpoint.

**https://test.com/public/kyc-approval?customerId=X&redirect\_uri=/public/profile**

1. Manually modify the URL to the user profile path and stop the page load before the redirect triggers.

**https://test.com/public/profile**

To make it persistent, I used Burp’s rule to automatically swap the verification URL with the profile URL in every outgoing request.

- **Result:** Full access to the authenticated user dashboard without completing the required KYC process.

### 2. Deep Dive: Authenticated Time-Based SQL Injection

Once the KYC gate was bypassed, I analyzed the authenticated API traffic. An endpoint used for managing records caught my attention due to its parameter handling.

- **Target Endpoint:** POST [https://api.\[REDACTED\].com/api/case](https://api.[REDACTED].com/api/case)
- **Vulnerable Parameter:** …Id
- **Payload:** 'XOR(if(now()=sysdate(),sleep(4),0))XOR'Z
- **Observation:** The server responded with a consistent 4-second delay, confirming that the backend was executing the injected SQL command.

### 3. Expanding the Attack Surface: Double IDOR (Create & Delete)

The lack of proper authorization checks extended to object-level references, allowing for complete manipulation of other users’ data.

#### A. Unauthorized Record Creation

- **Vulnerability:** IDOR in the owner identification parameter.

**Exploit:** By modifying the ....Id in the POST /api/case request (e.g., from my ID to a victim’s ID), I could create or update records on behalf of any user.

#### B. Unauthorized Record Deletion

- **Vulnerability:** IDOR in the delete endpoint.

**Exploit:**

1. Intercept the delete request: POST /api/case/\[ID\]/delete.
2. Change the object ID to a victim’s ID.

- **Result:** The system deleted the victim’s record without verifying if the authenticated user was the actual owner.

### Stay Connected

- **X (Twitter):** [@xelcezeri](https://x.com/xelcezeri)
- [**LinkedIn:** Samet Yiğit](https://www.linkedin.com/in/xsametyigit/)
