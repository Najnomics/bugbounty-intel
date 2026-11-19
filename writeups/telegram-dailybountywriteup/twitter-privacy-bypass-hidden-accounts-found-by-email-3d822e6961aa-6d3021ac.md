# Twitter Privacy Bypass

- **Source URL:** https://masimshahzad.medium.com/twitter-privacy-bypass-hidden-accounts-found-by-email-3d822e6961aa
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14989 (id 14989)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How a login-flow duplicate check ignored discoverability settings and mapped phone numbers and emails to accounts, for a $5,040 bounty

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

You could switch off “let people find me by email or phone” and Twitter would still tell a stranger which account was yours. In January 2022, HackerOne researcher zhirinovskiy reported a [Twitter privacy bypass](https://hackerone.com/reports/1439026) in the Android login flow that returned an account’s ID for any submitted phone number or email, without authentication. Twitter resolved it and paid $5,040.

***Disclaimer:*** *Educational and defensive use only. This was fixed in 2022. Reproduction details are intentionally omitted.*

### Vulnerability Overview

- **Type:** Privacy-setting bypass and account enumeration via an unauthenticated login-flow step that disclosed the user ID linked to a phone number or email
- **HackerOne weakness (source-reported):** Improper Access Control — Generic
- **CWE (analytical mapping, not from the source):** CWE-284 (Improper Access Control), CWE-203 (Observable Discrepancy), CWE-359 (Exposure of Private Personal Information)
- **CVE:** Not reported
- **Severity/CVSS:** CVSS not reported. Severity rated High on HackerOne. Bounty: $5,040, source-reported

### How the Twitter Privacy Bypass Worked (high level)

Twitter’s discoverability setting is a promise: knowing someone’s email or phone number should not let you find their account. The login flow on one client did not keep it.

The Android client’s login is a multi-step “onboarding” flow. One step checks whether the identifier you typed belongs to an existing account, so the app can handle duplicates. That check ran before the user proved anything, using only the app’s guest-level credentials, and its response carried the matching account’s numeric user ID.

A user ID resolves to a public profile in one more lookup, so the gap between “this email exists” and “this email is @someone” was zero. The researcher found the discoverability preference was never consulted on this path, and that it even returned IDs for suspended accounts.

That is the recurring pattern: privacy rules enforced at the feature users see, not at the data layer every client path touches.

### Impact

One lookup is a privacy leak. Scripted lookups are a database. The report warns that anyone with basic scripting could link huge lists of phone numbers and emails to accounts, data valuable for spam, for selling, and for targeting celebrities and pseudonymous users. For anyone who relies on a separate identity for safety, unmasking is the whole harm.

### Fixing Twitter-Style Privacy Bypass in Login Flows (my own analysis)

**1. Enforce privacy at the lookup layer.** Every path that maps identifier to account should call one policy function.

**2. Pre-auth steps return decisions, not identities.** A login step needs “continue” or “try again”, never a user ID.

**3. Rate limit by identifier and client.** Bulk matching should cost real effort, not a loop.

**4. Watch for enumeration.** Alert on guest sessions trying many distinct identifiers.

\# Pseudocode: one guarded identifier lookup for every client path

def resolve\_identifier(identifier, requester):

account = accounts.find\_by\_email\_or\_phone(normalise(identifier))

if requester.is\_unauthenticated():

# Login needs a next step, not an identity.

limiter.hit(f"lookup:{requester.client\_id}", identifier) # count even misses

return NextStep("password") # identical whether or not account exists

if account is None or not account.discoverable\_by\_contact:

return NotFound() # same response whether hidden or absent

return Found(public\_handle(account))

\# Test: guest flow must never emit user IDs; hidden account == missing account in response

### Key Takeaways

- Privacy settings have to be enforced where data is fetched, not where it is displayed.
- Unauthenticated flow steps are an API surface; diff their responses for hidden and missing accounts.
- An internal ID is an identity when it resolves to a profile.

### Credit & Sources

Research by **zhirinovskiy** (HackerOne): [Discoverability by phone number/email restriction bypass, report #1439026](https://hackerone.com/reports/1439026) (reported 1 January 2022, disclosed 11 February 2022). Facts come from that report; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
