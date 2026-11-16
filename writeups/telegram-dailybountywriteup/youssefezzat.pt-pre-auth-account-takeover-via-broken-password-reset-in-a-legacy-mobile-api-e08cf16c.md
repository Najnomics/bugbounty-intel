# Pre-Auth Account Takeover via Broken Password Reset in a Legacy Mobile API

- **Source URL:** https://medium.com/@youssefezzat.pt/pre-auth-account-takeover-via-broken-password-reset-in-a-legacy-mobile-api-f1b0b63dc1a6
- **Fetched from:** https://medium.com/feed/@youssefezzat.pt
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14985 (id 14985)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**By Youssef Ezzat**

### Introduction

I was doing recon on a private bug bounty program when I noticed the target had a legacy mobile API still exposed to the internet. Most people would scroll past it. I didn’t.

After mapping the WSDL and testing a few operations, I found something that stopped me: the password reset flow was completely broken. Not “missing rate limiting” broken. Not “weak token” broken. I mean the server would reset any account’s password with just an email address — no token, no old password, no inbox access required.

This is the write-up for that finding: a pre-authentication account takeover that earned a **Critical (9.3)** severity rating and was patched within hours of disclosure.

### Background — What Is This API?

Many large consumer apps have layers built over years. The modern web or mobile app talks to a clean REST or GraphQL layer, but behind it, there’s often an older service that still runs: untouched, forgotten, exposed.

This target had exactly that. A legacy SOAP service with **206 operations** in the WSDL — from account creation and login, to payment tokens and order history. No authentication required to discover or call these operations. It was essentially a full account management API open to anyone who knew the endpoint.

The two operations that matter for this finding:

- **ForgotPassword** — triggers a reset and (critically) returns the reset URL directly in the SOAP response
- **ResetForgottenPassword** — accepts an email address and a new password, and changes the password

Sounds fine on paper. The devil is in the details.

### The Bug — Broken Password Reset

There are two separate issues that together make this Critical:

**Issue 1: The reset token is leaked in the API response**

When you call ForgotPassword, the server is supposed to send a reset link to the user's email. Instead, it also returns the full reset URL — including the secret token — directly in the SOAP response body. Any unauthenticated caller can see the token without touching the victim's inbox.

**Issue 2: ResetForgottenPassword ignores the token entirely**

This is the bigger one. When you call ResetForgottenPassword, you'd expect it to validate the token from step 1. It doesn't. It accepts **just an email address and a new password** and immediately changes the account's password. No token. No old password. No session. Nothing.

The token is both leaked *and* unenforced. You don’t even need issue 1 to exploit this. Issue 2 alone is a complete account takeover.

### Proof of Concept — The Full Attack Chain

All requests go to the SOAP endpoint. I created a synthetic test account first, then ran the full chain against it.

**Step 1: Create a test account (attacker-controlled)**

SOAPAction: CreateGenericAccount

EmailAddress: victim@example.com

Password: OldPass!111

Response: ACCOUNT\_CREATED\_SUCCESSFULLY / 200

**Step 2: Confirm baseline login works**

SOAPAction: LoginV3

EmailAddress: victim@example.com

Password: OldPass!111

Response: OK / 200 — AID returned, PII confirmed

**Step 3: Call ResetForgottenPassword — no token, no old password**

SOAPAction: ResetForgottenPassword

EmailAddress: victim@example.com

NewPassword: NewPass!222

Response: OK / 200

That’s it. No token. No validation. The password changed.

**Step 4: Old password is dead**

LoginV3 with OldPass!111 → EMAIL\_PASSWORD\_INCORRECT / 400

**Step 5: New password logs in and returns PII**

LoginV3 with NewPass!222 → OK / 200

Returns: AID, EmailAddress, FirstName, LastName, PhoneNumber

Account taken over. No inbox access. No user interaction. Zero.

### Impact

The impact here is straightforward and severe.

Any account in the legacy mobile system could be taken over by anyone who knows (or can guess) the email address. The mobile app had over 10 million downloads on Google Play, meaning millions of real user accounts were potentially at risk.

After login, the WSDL contract shows access to:

- Full PII (name, email, phone)
- Payment tokens and billing addresses
- Order history and order details
- Ability to change email and password
- Account deletion

The web account system (FusionAuth) was separate and unaffected — this was scoped to the legacy mobile credential store only. Still, for a service with millions of users, that’s more than enough.

### Remediation

The program patched this quickly. Here’s what a proper fix looks like:

1. **Enforce a valid reset token in ResetForgottenPassword** — it should be single-use, high-entropy, and time-limited (e.g. 15 minutes). Reject any request without a valid token.
2. **Never return the reset URL in the API response** — deliver it only to the user’s verified email address. Returning it in the SOAP body defeats the entire purpose of a reset flow.
3. **Invalidate all active sessions** after a password change.
4. **Add rate limiting and alerting** on reset and password-change operations.
5. **Audit historical logs** — if the endpoint was exposed, assume the reset tokens in those logs may have been read. Invalidate any still-valid tokens.

In the interim, the program deployed a WAF block at Cloudflare while the backend fix was finalized. That’s a clean, fast incident response.

### Key Takeaways

**Don’t ignore legacy APIs.** Most bug hunters focus on the modern REST/GraphQL surface. Legacy SOAP services that handle real user data are often overlooked — and undertested.

**Map the WSDL before you test.** The full operation list tells you exactly what the server can do. ResetForgottenPassword being there at all was the first signal.

**Test the full reset flow, not just the happy path.** The question isn’t just “does it send an email” — it’s “what does the API return, and what does it validate?”

**Critical findings come from connecting two weak points.** Issue 1 alone (token leaked in response) might be Medium. Issue 2 alone (token not enforced) is already Critical. Together, they tell a complete story and make the report undeniable.

Thanks for reading. If you have questions, feel free to reach out.

— **Youssef Ezzat**
