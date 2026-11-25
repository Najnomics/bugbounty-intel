# Password Reset Tokens That Never Die

- **Source URL:** https://medium.com/@neel.chauhan09/password-reset-tokens-that-never-die-testing-invalidation-not-just-generation-7cb0aa5718be
- **Fetched from:** https://medium.com/@neel.chauhan09/password-reset-tokens-that-never-die-testing-invalidation-not-just-generation-7cb0aa5718be?source=rss-dc15ab41b8c5------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14919 (id 14919)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Neel Chauhan / Sun, 20 Sep 2026 19:50:08 GMT

**CWE-640: Weak Password Recovery Mechanism CWE-613: Insufficient Session Expiration CVSS 3.1: 7.4 (High)** — AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N

Most testing of a forgot-password flow stops at “does the token work.” A more complete test asks a second question: once a token has done its job, or been superseded by a newer one, does it actually stop working? That’s a token *invalidation* question, and it needs its own dedicated test sequence, generating multiple tokens deliberately and tracking which ones should logically be dead.

There are two invalidation behaviors a well-built system should enforce, and I tested both:

POST /api/auth/forgot-password HTTP/2

Content-Type: application/json

`{"email":"<test-account>"}`
HTTP/2 200 OK

```
{
  "ok": true,
  "reset_link": "https://<target>/reset-password?token=<TOKEN_A>"
}
```
I saved TOKEN\_A and deliberately did nothing else with it, simulating a real-world scenario where a user requests a reset, gets distracted, and never clicks the link.

```
{
  "ok": true,
  "reset_link": "https://<target>/reset-password?token=<TOKEN_B>"
}
```
Two live tokens now exist for the same account, at least in theory. A correctly implemented system should already have invalidated TOKEN\_A the moment TOKEN\_B was issued.

POST /api/auth/reset-password HTTP/2

Content-Type: application/json

`{"token":"<TOKEN_B>","password":"NewPass_1!"}``{ "ok": true, "message": "Password reset successful." }`
Password successfully changed. From the perspective of anyone watching only the happy path, everything looks correct and complete right here.

This is the step that most functional QA testing would never think to run, because from a pure feature-correctness standpoint, the reset flow already “worked” in step 3.

`{"token":"<TOKEN_A>","password":"NewPass_2!"}`
TOKEN\_A still worked. Generated before TOKEN\_B, never used by anyone, and the account's password had already been successfully changed via a completely different token in the meantime, and it still went ahead and reset the password a second time. Neither of the two invalidation behaviors I was testing for was actually implemented.

Every reset token has some expiration window, but that’s a separate control from invalidation-on-use, and it doesn’t substitute for it. A token sitting untouched in an old email, a shared inbox, synced browser history, or a proxy log doesn’t become safer just because a newer link was issued afterward, or because the account owner already reset their password through a different link. It remains a fully functional credential for the account, for as long as its raw expiry window allows, entirely disconnected from anything the account owner has done since.

I noted a scoping caveat directly in the writeup: I observed what appeared to be an unusually long token validity window, informally around a year, during testing, but did not independently confirm that through an explicit server-side expiration test, so I did not report it as a standalone confirmed finding. The token non-invalidation issue stands on its own regardless of what the exact expiry turns out to be, being precise about what was and wasn’t independently verified is part of writing a report that holds up under scrutiny.

Any token exposed through some other channel, whether that’s a phishing attempt, a compromised mailbox, or a separate disclosure vulnerability, inherits this same weakness: it doesn’t die when a new one is issued, and it doesn’t die when the account’s password actually changes. That turns a single leaked token into a standing, long-term access risk rather than a narrow, time-boxed one.
