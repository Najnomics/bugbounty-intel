# Breaking the Trust Boundary

- **Source URL:** https://medium.com/@romene.mohtadi.it/breaking-the-trust-boundary-a-mobile-security-assessment-of-a-healthcare-application-7adbdd2b7508
- **Fetched from:** https://medium.com/@romene.mohtadi.it/breaking-the-trust-boundary-a-mobile-security-assessment-of-a-healthcare-application-7adbdd2b7508?source=rss-0c8b34f211d5------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14928 (id 14928)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mohtadi Romene / Tue, 29 Sep 2026 21:12:14 GMT

***How a mobile security assessment uncovered authorization flaws, insecure authentication token storage, and sensitive medical data surviving logout.***

Healthcare applications operate in a particularly sensitive environment.

Unlike conventional mobile applications, they process information such as medical records, prescriptions, patient profiles, allergies, medical history, and other health-related information.

During a security assessment of a **healthcare mobile application**, I performed a mobile penetration test covering the Android application, backend APIs, authentication mechanisms, file storage, payment-related functionality, and the physician-facing web viewer.

The assessment followed the **OWASP Mobile Security Testing Guide (MSTG)** methodology and focused on identifying vulnerabilities across both the mobile client and the backend attack surface.

The assessment identified **8 security findings**, including:

The most significant findings involved:

The application is a mobile healthcare platform designed to allow users to centralize medical documents and patient information.

The application processes sensitive healthcare information and integrates several external services.

The main components identified during the assessment were:

The Android application was tested against the backend APIs, storage mechanisms, authentication flows and external integrations.

The assessment followed the **OWASP Mobile Security Testing Guide (MSTG)** methodology.

The testing environment included:

The objective was not only to identify vulnerabilities inside the mobile application, but also to determine whether security decisions were correctly enforced on the server side.

This distinction became particularly important during the assessment.

The tested attack surface included:

Two dedicated test accounts were created to perform cross-account and authorization testing.

No real user data was intentionally accessed or modified during the assessment.

**Severity: HIGH**

**CVSS: 8.1**

The first major vulnerability involved the application’s Premium authorization mechanism.

The application relied on a database field representing the Premium status of a user.

The problem was that this value could be modified through the backend API by an authenticated user.

The critical security issue was not simply that a database field was writable.

The deeper problem was that the application treated this field as a trusted authorization primitive.

A test account was initially configured as a non-Premium user.

The Premium field could then be modified through the REST API:

PATCH /rest/v1/notification\_preferences?id=eq.\<ROW\_ID>

Content-Type: application/json

```
{
  "is_premium": true
}
```
The API accepted the modification.

The response confirmed that the value had been changed:

The payment provider was then checked.

The account had:

```
{
  "entitlements": {},
  "subscriptions": {}
}
```
In other words:

**No active subscription existed.**

Nevertheless, the application considered the account Premium.

This allowed an authenticated user to access Premium functionality without purchasing a subscription.

According to the assessment, the affected functionality included:

The underlying issue was therefore an **authorization failure**, rather than a payment-provider compromise.

The attacker did not need to compromise the payment system.

They only needed to manipulate a client-accessible authorization state.

The root cause can be summarized as:

***Authorization was based on a mutable application state instead of a trusted server-side payment validation mechanism.***

This is a recurring pattern in mobile application security.

A mobile application should never be trusted to determine its own authorization level.

The assessment recommended several changes:

Users must not be able to arbitrarily modify their own Premium authorization state.

Premium-only backend operations should verify the subscription before executing privileged functionality.

Premium status should originate from the subscription system rather than from a client-controlled database field.

Subscription events such as:

should synchronize the authorization state securely.

**Severity: HIGH**

**CVSS: 7.8**

The second major finding involved local authentication storage.

The application stored Supabase authentication material, including:

inside Android SharedPreferences without encryption.

The assessment identified the following application storage location:

/data/data/\<application>/shared\_prefs/FlutterSharedPreferences.xml

The tokens were stored in plaintext.

A refresh token could be extracted from the application storage in the tested environment.

The token could then be replayed against the authentication service to obtain a new access token.

A refresh token is not just another application preference.

It represents the ability to obtain new authentication credentials.

If an attacker obtains a valid refresh token, they may be able to establish a new authenticated session without knowing the victim’s password.

For a healthcare application, this can potentially lead to access to sensitive medical information.

The application treated standard local preferences as a secure storage mechanism for authentication secrets.

This violates an important mobile security principle:

***Sensitive authentication material should not be stored in plaintext application preferences.***

The assessment recommended:

For Flutter applications, sensitive authentication material should be stored using a secure storage mechanism backed by Android Keystore.

For example:

final storage = FlutterSecureStorage();

await storage.write(

key: 'refresh\_token',

value: refreshToken,

);

The exact implementation should follow the application’s authentication architecture and threat model.

Additional recommendations included:

**Severity: HIGH**

**CVSS: 7.2**

The third High-severity vulnerability was related to local medical-data persistence.

Medical exports generated by the application remained on the device after logout or account switching.

During testing, files belonging to different test accounts were found simultaneously in the application’s local storage.

Consider a shared device.

User A logs into the application and accesses medical documents.

The application generates local exports.

User A logs out.

User B subsequently logs into the same device.

If User A’s medical exports remain locally accessible, User B may potentially recover information belonging to the previous account.

This creates a significant privacy boundary failure.

The exported data could contain information such as:

For a healthcare application, this information requires strong local-data protection.

The problem is therefore not only storage encryption.

It is also **data lifecycle management**.

If an export is only required for display or temporary processing, it should be deleted immediately after use.

Logout should invalidate the local security context and remove sensitive cached data belonging to the previous account.

If medical information must remain on the device, it should be protected using an appropriate encryption mechanism and secure key management.

**Severity: MEDIUM**

**CVSS: 5.3**

The signup API returned different response structures depending on whether an email address was already registered.

This behavior could allow an unauthenticated attacker to determine whether an account exists.

The issue becomes more sensitive in a healthcare context because knowledge that a person uses a particular healthcare service can itself reveal potentially sensitive information.

The signup endpoint should return a consistent response regardless of account existence.

HTTP 200

Generic response

The application should avoid exposing whether a particular email address is already registered.

**Severity: LOW**

**CVSS: 3.1**

Several backend operations returned raw technical errors to the client.

Examples included errors revealing:

While these messages do not necessarily result in direct compromise, they provide useful information about the backend implementation.

Technical errors should be:

Client → Generic error

Server → Detailed technical logs

Users should receive a controlled message such as:

An unexpected error occurred.

while detailed database information remains available exclusively through server-side logging.

**Severity: LOW**

**CVSS: 3.5**

The medical-document upload mechanism relied on the declared Content-Type when processing PDF files.

During testing, a file that was not actually a PDF could be stored while being declared as a PDF.

This demonstrates why checking only the HTTP MIME type is insufficient.

The backend should validate the actual file content.

A robust implementation should inspect the file’s **magic bytes** before accepting it.

Validation should occur server-side before the file reaches permanent storage.

**Severity: LOW**

**CVSS: 2.8**

Medical files stored in the application’s storage infrastructure did not consistently specify:

Content-Disposition: attachment

Depending on the browser or WebView behavior, a document could potentially be rendered inline instead of being treated strictly as a downloadable file.

For sensitive medical documents, the server should explicitly configure an appropriate response header, for example:

Content-Disposition: attachment;

filename="document.pdf"

The exact configuration should match the application’s intended document-delivery behavior.

**Severity: INFORMATIONAL**

A test-oriented backend endpoint remained accessible in the production environment.

The endpoint was associated with testing a Premium/WhatsApp-related functionality.

Production environments should not expose unnecessary testing functionality.

Test endpoints should either be:

A simple rule is:

***If an endpoint is not required by production users, it should not be exposed to production users.***

A penetration test should not only document vulnerabilities.

It should also identify security mechanisms that successfully resisted testing.

Several important controls were found to be correctly implemented.

Supabase RLS was correctly implemented on critical tables, including:

No cross-user medical-data leakage was identified during the assessment.

PostgREST parameterization and the existing WAF controls prevented the tested SQL injection attempts.

The physician viewer correctly escaped HTML through React/JSX rendering.

Stored XSS payloads tested during the assessment were rendered as inert text.

Authentication endpoints returned:

429 Too Many Requests

when rate limits were exceeded.

This provided protection against brute-force attempts and large-scale email abuse.

The medical-sharing mechanism verified profile ownership before generating sharing tokens.

A user could not simply request a sharing token for another patient’s profile.

Sharing restrictions were also enforced server-side.

The server respected the categories and permissions associated with generated sharing links.

Sharing tokens were stored as SHA-256 hashes rather than plaintext values.

The physician viewer used a Next.js Server Component to validate sharing tokens server-side.

The sharing token was not exposed to client-side JavaScript.

Storage-level authorization correctly prevented authenticated users from directly accessing another user’s medical documents.

The most interesting aspect of this assessment was not any individual vulnerability.

It was the concept of **trust boundaries**.

A mobile application contains many values that look authoritative:

is\_premium = true

user\_id = ...

authenticated = true

role = doctor

document\_owner = ...

But values inside a mobile application should never automatically be considered trustworthy.

The client is controlled by the user.

A determined attacker can:

Therefore:

***The client should request authorization, not define authorization.***

This principle explains why the Premium vulnerability was possible.

The application trusted a value that should have been derived from a trusted backend/payment source.

Another important lesson from this assessment is that mobile security cannot be reduced to static analysis.

A secure mobile application requires several layers:

A vulnerability at any trust boundary can undermine the overall security model.

Static analysis can reveal insecure storage.

Dynamic testing can reveal authorization failures.

API testing can reveal backend weaknesses.

Filesystem analysis can reveal sensitive-data persistence.

A professional mobile assessment therefore requires all of these perspectives.

Based on the assessment, the remediation roadmap was organized as follows:

The three P1 findings represented the most immediate risks identified during the assessment.

This assessment demonstrated an important principle of mobile application security:

**A strong architecture can still contain dangerous trust-boundary failures.**

The application already had several effective security mechanisms:

However, three High-severity vulnerabilities demonstrated weaknesses in other parts of the security model:

Premium status should never depend on a client-modifiable value.

A refresh token stored in plaintext can become a direct path to session compromise.

Logging out is not enough if sensitive medical data remains on the device.

The assessment of this healthcare mobile application revealed a combination of strong security controls and several significant weaknesses.

The most important findings were not exotic attacks.

They were failures to properly enforce **trust boundaries**:

Client-controlled state

≠

Trusted authorization

Local storage

≠

Secure secret storage

Logout

≠

Automatic data destruction

These principles are particularly important for healthcare applications because the impact of a security failure extends beyond technical compromise.

It can affect the confidentiality of highly sensitive personal information.

From a mobile pentesting perspective, the assessment reinforced a simple rule:

***Never trust what the client tells you. Verify it at the boundary where trust actually matters.***

This write-up has been intentionally anonymized.

The application name, client identity, production domains, identifiers, credentials, tokens, and other potentially sensitive information have been removed.

The objective of this publication is to share **security methodology, technical lessons, vulnerability patterns, and remediation strategies** without exposing the assessed organization’s confidential information.

All testing described in this article was performed within an authorized security assessment scope.

**Mobile Security**

**Backend & API Testing**

**Focus Areas**

The most valuable finding in a penetration test is not always the vulnerability with the highest CVSS score.

Sometimes, it is the security assumption behind it.

**If the client can change it, don’t trust it.**

**If the device can expose it, protect it.**

**If the data is sensitive, define its entire lifecycle.**
