# A real world bug bounty case study with identifying details anonymized

- **Source URL:** https://medium.com/@redhunter01/ive-rewritten-the-report-as-an-educational-case-study-with-the-program-name-real-domains-1679b2189500
- **Fetched from:** https://medium.com/@redhunter01/ive-rewritten-the-report-as-an-educational-case-study-with-the-program-name-real-domains-1679b2189500?source=rss-1a8706ec0593------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14998 (id 14998)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** redhunter01 / Tue, 24 Nov 2026 07:22:46 GMT

*A real world bug bounty case study with identifying details anonymized*

**Severity assessment:** High

**Reported CVSS:** 8.1 under CVSS 3.1

**Test environment:** Researcher-owned production accounts

**Demonstrated impact:** Setting another account’s password, receiving its session, and authenticating as that account.

**Confidentiality note:** This article describes a real finding. Organization and program names, infrastructure, product references, implementation identifiers, and exact capture times have been removed. Hosts, routes, selected field names, state labels, cookie names, and code excerpts use consistent illustrative replacements. HTTP methods, status codes, identity relationships, observed outcomes, and test limitations retain their original meaning. The examples are normalized representations of the evidence, rather than verbatim network captures.

Using the valid session of a free account, I could set a password on a different account that had not completed registration. The server returned the other account’s existing identifier, issued a session for that account, and accepted the chosen password in a separate login request.

The vulnerable operation was a registration-completion request. It required authentication, but selected the account to update from an email address in the request body. The authenticated caller and the selected account could therefore be different identities.

The strongest proof came from checking both accounts afterward. The target authenticated with the newly chosen password. The caller still authenticated with its original password, and the new password did not authenticate the caller. The operation had crossed an account boundary.

The report assessed the finding as **High**. The demonstrated affected population was the tested incomplete-registration account class, including a naturally created passwordless account. Completed accounts rejected the same registration update in the control tests.

This case is useful because the failure sat between two individually familiar features: establishing a session and finishing signup. Understanding how those features were connected exposed a credential-setting operation that trusted the wrong identity.

The application used an email-first account flow. After receiving an email address, the client checked whether a profile existed and whether registration was complete.

The observed branches were:

Account conditionIntended client behaviorSecurity significanceExisting account with completed registrationShow password sign-inThe account already had an established credential.Existing account with incomplete registrationVerify a one-time code, then finish signupAn existing identity still needed credential establishment.No existing profileCreate a new accountThere was no existing account to complete.

The client used POST to create a new profile and PUT to complete an existing one. That method distinction helped identify an operation that modified account state rather than merely creating a new record.

An incomplete account was still an identity belonging to someone. Attaching its first password determined who could subsequently authenticate as that identity. The completion step therefore needed account ownership checks just as a password-reset operation would.

The question that guided the investigation was:

**What server-verified evidence authorizes this caller to finish this particular account?**

The normal interface placed an email-verification step before completion. That sequence was useful context, but it did not establish that the backend enforced the same prerequisite.

Client-side source analysis connected the earlier email input, the profile lookup result, and the request used to submit the signup form.

The following pseudocode illustrates the relevant relationships with anonymized names:

method = profileExists ? "PUT" : "POST"

showCompletionForm = registrationComplete === false

```
submitRegistration(method, {
  ...form,
  email: emailFromEarlierStep
})
```
The client selected a method based on whether the profile already existed. A separate branch determined whether the incomplete-registration interface was shown. The email submitted to the backend came from the earlier email-first context.

That produced a focused hypothesis:

**The server might require a valid session while allowing the request body to choose a different account for the password change.**

This was a hypothesis about authorization, not a conclusion drawn from JavaScript alone. Browser-delivered code revealed the intended workflow. The subsequent requests and responses established how the server behaved when the identities were separated.

When reviewing similar flows, follow both the credential and the object selector. The credential tells the server who is calling. A body field, URL component, or query parameter may independently tell it which record to modify. The security check must connect those two pieces of information for the requested operation.

All demonstrations used researcher-owned production accounts. The accounts had different roles in the test:

LabelMeaning**B**The caller acting as the attacker, using a free account with completed registration.**V**A separate existing account in the tested incomplete or passwordless state.B\_IDThe caller’s stable account identifier.V\_IDThe target’s existing identifier, recorded before the cross-account request.B\_PASSWORDThe caller’s original working password.CHOSEN\_PASSWORDA different password submitted for the target.

For the natural passwordless setup, I used an owned mailbox, started the ordinary email-first flow, completed the one-time-code verification, and stopped before choosing a password. The application had created an identity, but registration remained incomplete.

That legitimate setup step must be distinguished from the takeover request. **The attack phase used B’s session and V’s email. It did not require V’s password, session, or one-time code.**

Session isolation was essential to interpreting the result. If V’s cookie accidentally accompanied the request, a successful password change could be a legitimate self-update. For a cross-account test, record the subject of the credential actually sent and keep it separate from the target account’s credentials.

The intended authorization relationship was simple: the verified completion context and the account receiving the password should identify the same account. The test supplied B as the authenticated caller and V as the selected target.

The application exposed an unauthenticated lookup that distinguished incomplete profiles from completed profiles and nonexistent accounts.

In the normalized examples, that lookup is represented as:

POST /example/registration-status HTTP/1.1

Host: identity.example

Content-Type: application/json

Origin: https://app.example

`{"email":"<V_EMAIL>"}`
The actual requests also contained ordinary application metadata. Identifying headers and values are omitted here because they did not establish ownership of the selected account.

For the incomplete test account, the response was HTTP 200. Its relevant meaning is represented by:

```
{
  "data": {
    "registrationComplete": false
  }
}
```
The observed outcomes were:

Account conditionRecorded outcomeIncomplete profileHTTP 200; the response indicated registration was incomplete.Completed profileHTTP 200; the response indicated registration was complete.No profileHTTP 400; the response indicated that the profile did not exist.

This was a disclosure of account state. It made the relevant state distinguishable, but did not itself change a password or establish account takeover.

An incomplete-state response should also not be treated as proof that every account with that response is exploitable under every configuration. The finding depended on the mutation and authentication results for the accounts actually tested. Neither the total affected population nor large-scale enumeration feasibility was measured.

B authenticated through the application’s ordinary password-login flow. The normalized request was:

POST /example/login HTTP/1.1

Host: identity.example

Content-Type: application/json

```
{
  "email": "<B_EMAIL>",
  "password": "<B_PASSWORD>"
}
```
The response returned HTTP 200 and a session cookie carrying a JWT. Inspecting the response headers mattered because the credential was commonly returned through Set-Cookie, rather than the JSON response body.

The identity-relevant claims are represented as:

sub = B\_ID

iss = https://identity.example

Additional implementation-specific claims are omitted. No email claim was observed in the recorded password session.

The absence of an email claim was not inherently a weakness. A stable subject can be sufficient for the backend to resolve the caller and enforce ownership. Adding an email claim would not repair a failure to authorize the operation on the selected account.

The credential was a genuine session obtained by logging in as B. There was no need to edit the token, change its subject, forge a signature, or compromise a signing key.

Decoding the token established which identity the credential represented. The next step tested whether the server kept that identity bound to the account being modified.

The decisive request used **B’s session** while selecting **V through the body email field**:

PUT /example/registration HTTP/1.1

Host: identity.example

Content-Type: application/json

Authorization: Bearer \<B\_SESSION\_TOKEN>

```
{
  "email": "<V_EMAIL>",
  "password": "<CHOSEN_PASSWORD>"
}
```
Other ordinary signup form fields were present in the original request and are omitted from this teaching excerpt. The security-relevant relationship was the mismatch between the session subject and the account selected for the password-setting operation.

The expected outcome was rejection because B had not established authority to complete V’s account. Instead, the server returned HTTP 200, identified V’s existing account, and marked its registration complete.

The normalized result shows the relevant meaning of the response fields:

```
{
  "data": {
    "accountId": "<V_ID>",
    "email": "<V_EMAIL>",
    "registrationState": "complete"
  }
}
```
The response also issued a new session cookie. Its JWT subject identified V.

Point in the exchangeIdentity established by the evidenceSession supplied with PUTBEmail selected in the request bodyVExisting account identifier returnedVSubject of the newly issued sessionV

This was stronger evidence than an email address reflected in a response. The returned account identifier matched the target’s existing identity, and the new credential represented that identity.

**The service had accepted authentication for one account and used it to perform a credential-setting operation on another.**

A separate login request tested whether the chosen password actually authenticated V:

The result was HTTP 200 and authenticated account information for V. This established password-based access beyond the session returned by the completion request.

B’s credentials were then checked to determine which account had changed:

Login attemptRecorded resultV with CHOSEN\_PASSWORDHTTP 200; authentication succeeded.B with B\_PASSWORDHTTP 200; authentication succeeded.B with CHOSEN\_PASSWORDHTTP 401; credentials were rejected.

These controls showed that the new password had not merely been applied to B. V’s returned identifier also matched the identifier recorded before the test, supporting that an existing target account had been modified.

The complete proof combined four observations:

The successful login demonstrated an established password-based access path. It did not establish indefinite persistence after account recovery, password rotation, or session revocation.

The endpoint did reject several requests. Those controls explained which checks existed and where authorization remained insufficient.

ControlRecorded resultRegistration update without a sessionHTTP 400; rejected for missing authentication.Completed account with its own session and emailHTTP 400; registration could not be updated through this operation, and the password remained unchanged.Completed target account with a foreign sessionHTTP 400; the original target password still worked.Attempt to change another account’s registration state through profile editingThe profile operation remained bound to the authenticated account.Own existing password session after an account entered the incomplete stateRegistration completion succeeded without a new one-time-code step.Status lookup for an email with no profileHTTP 400; profile absence was distinguishable.

The unauthenticated rejection established a session requirement. It did not establish that every accepted session was authorized for the target record.

The completed-account controls limited the demonstrated primary impact. **The tests did not show direct password replacement on arbitrary completed accounts.**

The existing-session control exposed a related workflow problem: even a session belonging to the correct account could substitute for the intended completion proof. Enforcing subject matching alone would therefore not fully implement a requirement for a dedicated verification step before completing registration.

This distinction is useful when testing APIs: required-field validation, authentication, account eligibility, and authorization for a particular operation are separate checks.

The report included an independent reproduction using a fresh incomplete profile and another using an account left passwordless through the ordinary signup flow.

Both demonstrated registration completion for the selected target and successful login with the chosen password, while the caller’s password controls held. The naturally created account remained incomplete for several hours before the test.

That timing showed that the affected state could persist beyond a momentary interface transition. It did not establish a universal retention period, an unlimited attack window, or the number of incomplete accounts in production.

A separate laboratory setup used an owned account’s own session to move that account back into the incomplete state. That was useful for constructing a test condition, but the natural signup example established that the primary vulnerable state was reachable through the product’s ordinary workflow.

The report also tested a sequence in which V’s own session first reopened V’s registration state through profile editing. B’s session then completed V’s registration with a new password. The replacement password worked, the previous password failed, and the owned test account was restored afterward.

This sequence required prior access to V’s session. The profile endpoint did not allow B to downgrade an unrelated completed account simply by supplying a different email.

The result therefore showed a possible route from existing session access to password-based access after reopening registration. It did not prove an initial takeover of arbitrary completed accounts.

The two threat models must remain separate:

The service authenticated a caller but allowed an independently supplied email address to determine which account received a new password.

This is a **broken object level authorization** pattern. The object was the account profile, the selector was an email address, and the protected operation was credential establishment. OWASP describes this category as a failure to authorize the requested action on the particular object selected by a caller-controlled identifier.

The observed behavior exposed two missing bindings:

Neither conclusion requires a cryptographic weakness in the JWT. Authentication could correctly identify B while the application still authorized a change to V incorrectly.

It was also unnecessary to guess a private account identifier. The service resolved the supplied email address to the existing target profile. Object authorization failures can involve familiar strings, not only numeric identifiers in URLs.

The required invariant is:

**The account receiving a credential must be the account authorized by the verified completion context.**

For the tested incomplete accounts, a basic authenticated user could establish another account’s password, receive a session for that identity, and subsequently authenticate as it. The takeover request required neither the target’s one-time code nor interaction from its owner.

The password change and separate successful login demonstrated account control. The returned account response demonstrated access to the fields visible in that response. The testing did not characterize every authenticated API or all personal information potentially reachable afterward.

The completed state would send the owner toward password sign-in even though the attacker had selected that password. Permanent lockout, defeat of account recovery, and bypass of every possible multifactor configuration were not established.

Additional paid features or business privileges could increase the consequences of account control, but access to such features and billing actions was not demonstrated in this case.

The report used this severity assessment:

CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N

This vector calculates to **8.1, High** under CVSS 3.1. It treats the prerequisite ordinary account as low privileges and requires no victim interaction during exploitation. The assessment assigns high confidentiality and integrity impact without a separate service-availability claim. Crossing between user accounts does not automatically imply a CVSS Scope change; that metric concerns security authorities.

The account-state restriction remains part of the impact statement. It should not be replaced by a claim that every account on the service was vulnerable. The severity assessment also does not establish a triage outcome, remediation status, or disclosure approval.

The backend should obtain the account identifier from a verified, authorized completion context. A body email must not independently select another record for a password change.

If an email remains in the request, resolve it using the application’s canonical identity rules and verify that it refers to the account authorized for completion. A stable server-side identifier is preferable to treating an unchecked email string as authority.

An email claim does not have to be added to every session token to enforce this relationship. The verified subject can be resolved to the correct account on the server.

After the required ownership-verification step, issue a short-lived, single-use authorization bound to the account and the registration transaction. An ordinary password session should not substitute for that completion proof.

For JWT-based designs, validate the expected issuer, audience, subject, validity window, and purpose through the supported verification mechanism. RFC 8725 recommends distinct validation rules when an issuer produces tokens for different contexts, preventing a token valid for one purpose from being accepted for another.

Subject binding and purpose binding address different failures. A completion token for B must not complete V. A generic session for V must not automatically satisfy a requirement for fresh completion authorization.

Verify that the account is eligible, consume the completion proof, and establish the password and completed state as one guarded transition. Issue the resulting session only after that authorized transition succeeds.

This is a remediation recommendation, not a claim that a concurrency vulnerability was demonstrated. It keeps the authorization decision connected to the mutation it protects.

OWASP’s password-recovery guidance similarly recommends valid proof that expires and can be used only once. The workflow here was registration completion, but both operations establish a credential for an existing identity.

General profile editing should not allow ordinary clients to move completed accounts back into an incomplete registration state. If a legitimate migration requires that change, protect it with a dedicated policy and appropriate verification.

This addresses the separate scenario requiring a target session. It does not replace the subject and purpose checks needed at the completion endpoint.

Avoid revealing whether an arbitrary email belongs to an incomplete account before verifying ownership. An email-first interface can begin with a generic response and reveal sensitive account-state details after the user proves control of the mailbox.

Rate limits and monitoring can reduce abuse, but concealing the status result alone would not repair the cross-account password update when the target email is known. OWASP recommends consistent responses and timing to reduce enumeration in recovery workflows.

A focused regression review should accept valid completion proof only for its intended account, transaction, and operation. It should reject foreign subjects, ordinary sessions used as completion proof, missing or invalid proof, expired or reused proof, and ineligible account states.

The review should also verify that ordinary profile edits cannot reopen registration, that session issuance reflects the authorized account, and that legitimate signup continues to work. These checks address the invariant exposed by the report rather than only one request body.

The transferable method is to treat account transitions as security-sensitive operations:

A valid session identifies a caller; **the server must separately authorize that caller for the requested account and operation**. Preserving that relationship is essential whenever an API establishes a password or issues a session. In this case, following the identities through the request, response, and later login turned an apparent registration oddity into a demonstrated cross-account takeover.

Remove residual implementation clues
