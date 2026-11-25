# How I found a Zero-Click Account Tack over via password rest link

- **Source URL:** https://cyghost.medium.com/how-i-found-a-zero-click-account-tack-over-via-password-rest-link-9f4eafbc9009
- **Fetched from:** https://cyghost.medium.com/how-i-found-a-zero-click-account-tack-over-via-password-rest-link-9f4eafbc9009?source=rss-8116f81382d0------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14948 (id 14948)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** seif nasr / Wed, 14 Oct 2026 11:35:16 GMT

*How testing a password recovery workflow revealed a potential account takeover vulnerability.*

While exploring web application security, I decided to take a closer look at a password reset workflow.

Password recovery features are interesting targets for security researchers because they involve several security-sensitive elements: recovery tokens, account identifiers, and password changes. These elements must be correctly linked together on the server side.

I wanted to understand whether the application properly enforced that relationship.

I started by using the password recovery functionality with a test account under my control.

After receiving the recovery link and proceeding through the reset process, I inspected the HTTP requests involved in changing the password.

One detail caught my attention: the request included a parameter named Email.

This parameter appeared to identify the account associated with the password change.

That raised an important question: was the server independently verifying the account associated with the recovery token, or was it trusting the email address supplied in the request?

To investigate the behavior safely, I used two test accounts that I controlled.

I initiated the password recovery process for the first account and inspected the subsequent password change request.

I then examined how the Email parameter was handled by the application.

The key issue I wanted to verify was whether the recovery token was securely bound to the account whose password was being changed.

During testing, I observed that the application did not properly enforce this relationship.

The server accepted a password change request in which the account identifier did not correspond to the account associated with the original recovery operation.

A successful HTTP response alone would not have been enough to establish account takeover.

I therefore verified the resulting behavior using the test accounts under my control.

The password change affected the second test account, even though the recovery process had originally been initiated for the first account.

I then confirmed that the changed credentials could be used to authenticate to the second test account.

This demonstrated that the issue was more serious than an unexpected response or a simple input validation weakness: the password recovery workflow could allow one account’s recovery context to be used to change another account’s password.

The underlying security problem was a failure to enforce the relationship between the recovery token and the target account.

If the same behavior were exploitable against real users, an attacker could potentially take over an account without requiring the victim to interact with a recovery link.

The impact would depend on the affected account’s data, functionality, and privileges.

The behavior suggested insufficient server-side validation of the account identity during password recovery.

A secure implementation should:

Client-supplied parameters should never be sufficient on their own to determine which account receives a sensitive security operation.

This investigation reinforced an important lesson in web application security: a parameter’s presence in an HTTP request does not mean the server should trust it.

When testing authentication and recovery workflows, it is important to understand how the application links tokens, identities, and sensitive actions.

The real question is not simply whether a parameter can be changed. It is whether changing it breaks a security boundary — and whether that impact can be demonstrated safely.

*This write-up intentionally omits the affected organization, target, endpoints, complete requests, and other identifying information to protect the system and keep the discussion focused on the security lesson.*
