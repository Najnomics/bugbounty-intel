# How I Found a Session Hijacking Bug That Could Lead to Account Takeover | by Samadhan Shimple

- **Source URL:** https://samadhanshimple.medium.com/how-i-found-a-session-hijacking-bug-that-could-lead-to-account-takeover-by-samadhan-shimple-99f63c58ca7f
- **Fetched from:** https://web.archive.org/web/20261009144315/https://samadhanshimple.medium.com/how-i-found-a-session-hijacking-bug-that-could-lead-to-account-takeover-by-samadhan-shimple-99f63c58ca7f
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14938 (id 14938)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How I Found a Session Hijacking Bug That Could Lead to Account Takeover | by [Samadhan Shimple](https://www.linkedin.com/in/samadhan-shimple/)

While testing a web application, I came across an interesting session-management issue involving the `PHPSESSID` cookie.

At first, it looked like a normal session cookie. However, during testing, I discovered that a valid session ID could be reused from another browser and the application would still treat the request as the authenticated victim.

This meant that if an attacker obtained a victim’s valid session ID, they could potentially impersonate that user and perform sensitive account actions.

Here’s how I found it.

### The Discovery

I started with two separate test accounts:

- **Account A — Attacker**
- **Account B — Victim**

I used different browsers for both accounts to make sure the sessions were completely separate.

I logged into **Account B** using Microsoft Edge and captured the `PHPSESSID` associated with the authenticated session.

Next, I switched to **Account A** in Firefox and navigated to the password-change functionality.

I intercepted the password-change request using Burp Suite.

The interesting part came when I replaced Account A’s `PHPSESSID` with the valid `PHPSESSID` belonging to Account B.

I then forwarded the modified request.

### What Happened?

The application accepted the victim’s session cookie without requiring any additional authentication or verification.

The request was processed in the context of **Account B**.

In my testing, I was able to observe victim-account information and successfully perform the password-change operation while operating from the attacker session.

In other words, the application appeared to rely almost entirely on the supplied `PHPSESSID` to determine the authenticated user.

This created a serious security boundary issue:

*Whoever possesses a valid session identifier may be able to act as the user associated with that session.*


### Reproduction Steps

The issue can be reproduced in a controlled testing environment as follows:

### 1. Create two accounts

Create two separate accounts:

- Attacker Account A
- Victim Account B

### 2. Authenticate as the victim

Log into Account B using a separate browser and capture the authenticated `PHPSESSID`.

### 3. Authenticate as the attacker

Log into Account A using another browser.

Navigate to the password-change functionality and intercept the request using Burp Suite.

### 4. Replace the session cookie

Modify the request by replacing Account A’s `PHPSESSID` with the valid `PHPSESSID` obtained from Account B.

Forward the request.

### 5. Observe the result

The application processes the request using Account B’s authenticated session.

The response indicates that the request was successfully executed against the victim account.

This demonstrates that possession of the victim’s session identifier is sufficient to impersonate that session.

### Why This Is Dangerous

Session cookies are effectively authentication credentials.

A properly designed application should ensure that a session is:

- Random and unpredictable.
- Properly protected.
- Bound to the authenticated session.
- Rotated when appropriate.
- Invalidated after logout.
- Protected against session fixation.
- Not exposed through application responses, URLs, logs, or client-side storage.

If an attacker obtains a valid authenticated session identifier, the attacker may not need the victim’s username or password.

In this case, the problem became especially serious because the hijacked session could be used to access a sensitive account-management function.

### Potential Impact

Depending on the privileges associated with the compromised session, an attacker could potentially:

- Access private account information.
- Perform actions as the victim.
- Modify account settings.
- Change the victim’s password.
- Lock the legitimate user out of their account.
- Access sensitive functionality available to the victim.
- Potentially escalate the attack if the compromised account has administrative privileges.

The password-change functionality makes this particularly concerning because successful exploitation could turn session compromise into persistent account takeover.

### Expected vs. Actual Behavior

### Expected Behavior

The application should properly protect authenticated sessions.

A session identifier belonging to one account should never be usable to authenticate as another account unless the request genuinely originates from that authenticated session.

Sensitive operations such as changing a password should also require appropriate authorization and, where appropriate, re-authentication or additional verification.

### Actual Behavior

Replacing the attacker’s `PHPSESSID` with the victim's valid `PHPSESSID` caused the application to treat the attacker-controlled request as the victim's authenticated session.

The password-change request was subsequently accepted.

### Security Classification

I would classify this issue primarily as a **session management / authentication failure** with potential **account takeover** impact.

Relevant classifications include:

- **OWASP Top 10 2021:** A07 — Identification and Authentication Failures
- **CWE-384:** Session Fixation
- **CWE-287:** Improper Authentication
- **CWE-522:** Insufficiently Protected Credentials
- **Bug bounty category:** Session Hijacking / Account Takeover

The exact CWE can depend on the underlying root cause. If the application allows an attacker to fix or force a victim into a known session, CWE-384 is particularly relevant. If the core issue is simply that possession of a stolen session token is enough to impersonate the user, the report may be better described as an authentication/session-management vulnerability.

### Recommended Fix

The application should review its complete session-management implementation.

Some important protections include:

1. Generate session identifiers using a cryptographically secure random mechanism.
2. Ensure session IDs are sufficiently long and unpredictable.
3. Rotate the session ID after authentication and important privilege changes.
4. Invalidate the previous session when appropriate.
5. Properly destroy sessions after logout.
6. Set appropriate cookie attributes such as `Secure`, `HttpOnly`, and an appropriate `SameSite` policy.
7. Avoid exposing session identifiers through URLs, logs, responses, or client-side JavaScript.
8. Implement appropriate session expiration and inactivity timeouts.
9. Require re-authentication or additional verification for highly sensitive operations such as password changes.
10. Review whether sessions should be revoked after password changes or other security-sensitive account events.

Most importantly, the application should ensure that authorization decisions are correctly tied to the authenticated session and that sensitive operations cannot be performed simply by supplying another user’s session identifier.

### Responsible Disclosure

I believe security research is most valuable when vulnerabilities are reported responsibly and the affected organization is given a reasonable opportunity to fix the issue.

This vulnerability was tested using controlled accounts and only the minimum actions necessary to verify the impact. No unrelated user accounts or data were intentionally accessed, modified, or disclosed.

After identifying the issue, the appropriate approach is to report it privately through the organization’s security or bug-bounty program, provide clear reproduction steps and evidence, and allow the security team sufficient time to investigate and remediate the vulnerability before publicly disclosing technical details.

For security researchers, a good rule is simple:

**Prove the vulnerability, minimize the impact, protect user data, and give the organization a fair opportunity to fix it.**

### Final Thoughts

This was a good reminder that sometimes the most interesting vulnerabilities aren’t complicated.

I didn’t need to find a sophisticated injection vulnerability or bypass a complex authentication mechanism. I simply tested how the application handled an authenticated session when the session identifier was changed.

The key lesson for me was:

**Never assume that a session cookie is “just a cookie.”**

A session identifier can effectively represent a user’s authentication state. If it can be obtained or abused, the consequences can be just as serious as exposing a password.

When testing web applications, I always recommend paying close attention to session behavior around login, logout, password changes, account recovery, privilege changes, and sensitive actions.

A small weakness in session management can sometimes turn into a complete account takeover.

*AI assistance: I used an AI-powered grammar and spelling checker to review this article. The ideas, research, technical analysis, and final content are my own.*

*Have questions or want to share your own workflow? Drop a comment below or connect with me on :*

🔗Linkdin: [https://www.linkedin.com/company/sam-shield/](https://www.linkedin.com/company/sam-shield/)

🔗Youtube: [https://www.youtube.com/@sam\_shield-w7l](https://www.linkedin.com/company/sam-shield/)

🔗Medium: [https://medium.com/@samadhanshimple](https://medium.com/@samadhanshimple)
