# Sign in with Apple JWT Bug

- **Source URL:** https://masimshahzad.medium.com/sign-in-with-apple-jwt-bug-account-takeover-case-ae9fd2061bf6
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14986 (id 14986)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Sign in with Apple JWT Bug: Any Email, Any Account

### How a $100,000 bug bounty finding let an identity provider sign tokens for email addresses nobody had proven they owned

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

An email address was the only thing an attacker needed. In April 2020, Bhavuk Jain found a [Sign in with Apple JWT bug](https://bhavukjain.com/blog/2020/05/30/zeroday-signin-with-apple/) that made Apple’s servers hand out validly signed identity tokens for whatever email was asked for. Any third-party app that trusted those tokens without extra checks was open to full account takeover, and Apple paid $100,000 for the report.

***Disclaimer:*** *Educational and defensive use only. Apple fixed this in 2020. Endpoints, request bodies and reproduction details are intentionally omitted.*

### Vulnerability Overview

- **Type:** Authentication bypass at the identity provider: identity token issued for an unverified, caller-chosen email claim
- **CWE (analytical mapping, not from the source):** CWE-287 (Improper Authentication), CWE-639 (Authorization Bypass Through User-Controlled Key)
- **CVE:** Not reported
- **Severity/CVSS:** Not reported. Bounty: $100,000 (Apple Security Bounty), source-reported

### How the Sign in with Apple JWT Bug Worked (high level)

Sign in with Apple behaves much like OpenID Connect. The user authenticates with Apple, chooses whether to share their real address or a private relay address, and Apple returns a signed JWT. The relying app checks the signature against Apple’s public keys and logs in whoever the email claim names.

The flaw sat in the step where Apple minted that token. According to the researcher, the email that ended up in the JWT could be supplied by the requester, and Apple did not confirm it belonged to the person who had just signed in. The token was genuine: correct issuer, correct signature, and a claim saying the email was verified. Only the identity inside it was wrong.

That is what makes this case uncomfortable. Every app that “validated the JWT properly” still accepted it, because the lie came from the trusted signer itself.

### Impact

Jain wrote that the bug could lead to full takeover of accounts on third-party apps using Sign in with Apple, even if the victim had no Apple ID, as long as the app had no additional safeguards. He named large adopters such as Dropbox, Spotify and Airbnb as examples of integrators, while noting they were not tested. Apple reviewed its logs and found no misuse or account compromise.

### Defending Against Sign in with Apple JWT Abuse (my own analysis)

**1. Key accounts on the stable subject, not the email.** Link a social login to iss + sub. Treat email as a mutable contact attribute.

**2. Never auto-merge on email alone.** If a federated email matches an existing password account, require the user to prove control of that account before linking.

**3. Validate every claim you depend on.** Check aud, exp, nonce and issuer, and bind the nonce to the browser session that started the login.

**4. Plan for a compromised provider.** Alert on new federated links and offer step-up checks for sensitive actions.

\# Pseudocode: federated login keyed on (issuer, subject)

def federated\_login(id\_token, session):

claims = verify\_jwt(id\_token, keys=apple\_jwks(),

issuer=APPLE\_ISS, audience=MY\_CLIENT\_ID)

if claims.nonce != session.pop("login\_nonce"):

raise AuthFailed("nonce mismatch")

link = links.find(issuer=claims.iss, subject=claims.sub)

if link:

return create\_session(link.user)

existing = users.find\_by\_email(claims.email)

if existing: # do not merge silently

return require\_proof\_of\_existing\_account(existing, claims)

return create\_session(users.create\_federated(claims.iss, claims.sub,

contact\_email=claims.email))

### Key Takeaways

- A valid signature proves who issued a token, not that its claims are true.
- Identify federated users by issuer and subject; email-based account merging is a takeover path.
- Build relying-party checks that still hold when the identity provider makes a mistake.

### Credit & Sources

Research by **Bhavuk Jain**: [Zero-day in Sign in with Apple](https://bhavukjain.com/blog/2020/05/30/zeroday-signin-with-apple/) (30 May 2020). Press context on the fix: [Ars Technica, 1 June 2020](https://arstechnica.com/information-technology/2020/06/apple-fixes-bug-that-could-have-given-hackers-unauthorized-to-user-accounts/). Facts come from those sources; analysis and code are original.

Next breakdown: the Facebook IDOR that could delete any photo album. Follow @masimshahzad for daily bug bounty breakdowns.
