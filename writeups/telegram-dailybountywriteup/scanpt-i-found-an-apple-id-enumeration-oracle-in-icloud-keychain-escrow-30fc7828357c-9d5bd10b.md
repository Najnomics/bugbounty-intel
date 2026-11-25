# I found an Apple ID Enumeration Oracle in iCloud Keychain Escrow

- **Source URL:** https://medium.com/@scanpt/i-found-an-apple-id-enumeration-oracle-in-icloud-keychain-escrow-30fc7828357c
- **Fetched from:** https://medium.com/@scanpt/i-found-an-apple-id-enumeration-oracle-in-icloud-keychain-escrow-30fc7828357c?source=rss-fa9d9d9b24be------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14890 (id 14890)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Fábio Luís @scanpt / Sun, 30 Aug 2026 20:25:45 GMT

I was looking at escrowproxy.icloud.com when I noticed something odd about the way it handled failed authentication.

The service uses HTTP Basic Authentication, and the username can be a DSID. I started sending requests with deliberately incorrect passwords and comparing the responses.

I expected the usual generic authentication failure.

Instead, the response changed depending on the DSID I supplied.

A valid DSID with the wrong password returned one error.

A locked account returned another.

A DSID that didn’t exist returned something completely different.

That was the start of the bug.

After testing the behavior more systematically, I found that the same authentication flow could also be used with email addresses, making it possible to determine whether an email was associated with an Apple ID.

I reported the issue to Apple on March 29, 2026. Apple later fixed it in production and asked me to verify the fix.

The service I was testing was:

escrowproxy.icloud.com

One of the exposed API paths was:

/escrowproxy/api/get\_records

Authentication was performed using HTTP Basic Authentication.

The username could be a DSID, so I started testing how the service behaved when the identifier was valid but the password was deliberately wrong.

That was where things became interesting.

I tested three different DSID states using the same invalid password.

For an active account, the service returned:

Your Apple ID or password was entered incorrectly

For a locked account:

This Apple ID has been locked for security reasons

And for a DSID that didn’t exist:

unknown ds error code: -20946

So the behavior looked like this:

DSID

│

incorrect password

│

┌──────────┼──────────┐

│ │ │

▼ ▼ ▼

Active Locked Invalid

│ │ │

▼ ▼ ▼

"password" "locked" "-20946"

The password was wrong in every case.

The only thing I was changing was the identifier.

That meant the authentication response itself was revealing information about the account behind that identifier.

The next question was whether this was just inconsistent error handling or something reliable enough to classify account states.

I repeated the requests several times with delays between them.

The responses stayed consistent.

This effectively created a pre-authentication account-state oracle:

Input DSID

│

▼

escrowproxy

│

├── "Your Apple ID or password..."

│ ↓

│ Active account

│

├── "Apple ID has been locked..."

│ ↓

│ Locked account

│

└── "unknown ds error code: -20946"

↓

Invalid DSID

The interesting part wasn’t that authentication failed.

Authentication was supposed to fail.

The problem was that an external client could tell *why* it failed.

Some of the responses contained more than a user-facing error message.

I also saw strings such as:

Authentication failed for usrId:\<DSID>

authentication against ds failed

along with internal-looking status values including:

AccountDSLocked

Unauthenticated

Those distinctions made the oracle even easier to classify.

Instead of treating every failed login as the same event, the API was exposing different states from the backend authentication flow to the client.

At this point I had a reliable DSID oracle, but DSIDs are internal numeric identifiers.

I wanted to see what happened if the Basic Auth username wasn’t numeric.

So I tried email addresses.

The behavior was different depending on whether the address was associated with an Apple ID.

In my testing, addresses associated with Apple IDs returned:

AccountDSLocked

while addresses that were not associated with Apple IDs returned:

Unauthenticated

Conceptually:

Email address

│

▼

escrowproxy

│

authentication

│

┌─────────┴─────────┐

│ │

▼ ▼

Apple ID exists No Apple ID

│ │

▼ ▼

AccountDSLocked Unauthenticated

This was more useful from an enumeration perspective than the original DSID behavior.

Instead of needing an internal numeric identifier, the input could now be an ordinary email address.

In other words, the endpoint could be used as an email-to-Apple-ID existence oracle.

Once I had confirmed the behavior, I checked whether it was specific to get\_records.

I found nine relevant API endpoints on the service:

The same general differential authentication behavior was present across the endpoints I tested.

I also wanted to see whether repeated requests would trigger throttling.

I sent 50 sequential requests.

The result was:

50 requests

50 × HTTP 401

0 × HTTP 429

0 × HTTP 403

I didn’t observe any throttling during that test.

This doesn’t prove that the service had no rate limiting under every condition, but it showed that the oracle remained usable across repeated sequential requests without being blocked during my testing.

The basic behavior could be reproduced with curl and base64.

For example:

curl -sk -X POST \

-H "Content-Type: application/x-apple-plist" \

-H "Authorization: Basic $(echo -n 'DSID:WrongPassword' | base64)" \

-d '\<?xml version="1.0" encoding="UTF-8"?>

\<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"

"http://www.apple.com/DTDs/PropertyList-1.0.dtd">

\<plist version="1.0">

\<dict>

\<key>c\</key>

\<string>g\</string>

\</dict>

\</plist>' \

"https://escrowproxy.icloud.com/escrowproxy/api/get\_records"

The password stays invalid.

Changing only the identifier was enough to produce the different authentication responses.

I also wrote a small PoC script while testing the issue. The original report covered:

This wasn’t an account takeover.

There was no authentication bypass and the vulnerability didn’t provide access to an Apple account.

The issue was the information exposed *before* successful authentication.

For DSIDs, an attacker could distinguish between:

DSID → active / locked / invalid

For email addresses, the behavior could be used to infer:

email → associated with Apple ID / not associated

That information can be useful as a building block for more targeted attacks.

For example, confirming that a particular email address is associated with an Apple ID makes Apple-specific phishing more targeted.

Similarly, distinguishing active accounts from invalid identifiers gives an attacker information that should not normally be available without authentication.

The important distinction is that this was an enumeration and account-state disclosure issue, not an account takeover vulnerability.

From an unauthenticated client’s perspective, these states shouldn’t be distinguishable.

Whether the identifier belongs to:

the external response should be the same.

Something as simple as:

Authentication failed

would remove the oracle.

The backend can still know exactly why authentication failed. The client doesn’t need to.

Apple subsequently updated the production service.

I re-tested the affected cases on July 2, 2026.

After the fix, the authentication scenarios I had previously been able to distinguish all returned the same response:

errorCode: -3001

errorMessage: Authentication failed

HTTP 401

I tested:

The previous differential responses were gone.

I also verified the behavior across the affected endpoints I had tested originally.

The oracle was no longer observable.

On July 7, Apple Product Security confirmed my verification of the fix. Apple later added **Fábio Luís (@scanpt)** to its Web Server Security Acknowledgements for July 2026.

**Apple Security Acknowledgement:**

Fábio Luís (@scanpt) — July 2026

[https://support.apple.com/pt-pt/102774](https://support.apple.com/pt-pt/102774)

**March 29, 2026**

Reported the vulnerability to Apple.

**July 2, 2026**

Re-tested the production service and confirmed that the differential authentication behavior had been fixed.

**July 7, 2026**

Apple Product Security confirmed my verification of the fix.

**July 2026**

Apple published my credit as **Fábio Luís (@scanpt)** in its Web Server Security Acknowledgements.

**August 2026**

Public disclosure.

This bug started with something that didn’t look particularly interesting: an authentication endpoint returning different error messages.

Any one of those responses on its own probably wouldn’t have caught my attention for long.

The interesting part appeared when I put the responses next to each other.

Different identifier

↓

Different backend state

↓

Different authentication error

↓

Account enumeration

Once the DSID behavior was clear, trying email addresses was the obvious next step — and that turned the same issue into an Apple ID existence oracle using ordinary email addresses.

The fix was simple from the outside.

Don’t expose the underlying account state.

After Apple’s update, all of the cases I tested collapsed into the same generic authentication failure, which is exactly what I would have expected from the service originally.

Sometimes the useful signal isn’t in a successful response.

It’s in the differences between the failures.

**Researcher: Fábio Luís @scanpt**
