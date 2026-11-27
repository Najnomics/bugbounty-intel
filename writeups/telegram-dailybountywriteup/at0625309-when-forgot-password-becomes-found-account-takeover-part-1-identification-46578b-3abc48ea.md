# When ‘Forgot Password’ Becomes ‘Found Account Takeover’ — Part 1

- **Source URL:** https://medium.com/@at0625309/when-forgot-password-becomes-found-account-takeover-part-1-identification-46578b0afbc2
- **Fetched from:** https://medium.com/feed/@at0625309
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/15000 (id 15000)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Enter your email, get a link, set a new password. That’s all “Forgot Password” looks like from the outside.

But every reset flow quietly answers three questions, and each one is a place where account takeover can hide:

1. Identification — whose account is being reset?

2. Token generation — what proves this reset request is legitimate?

3. Token delivery — who actually receives the reset link?

**A small note: This is more or less the checklist I’ve put together while exploring password reset testing. Thought I’d share it here in case it helps someone else too, especially those just getting started. Hopefully, it saves you a few rabbit holes along the way!**

I’ve split my password reset testing notes into three parts to keep things easier to follow. This one starts with identification — figuring out whose account we’re actually resetting. If the app gets identification wrong, nothing downstream can save it — a perfectly random token sent to the wrong person is still a takeover.

All testing below assumes accounts you own and a program whose scope allows it.

*1. Enumeration: the app tells you who exists*

The reset form is often the easiest place to learn whether an email is registered. Apps leak this in three layers — check all three, because fixing one doesn’t fix the others.

Layer 1 — the UI. “Reset link sent” for one email, “No account found” for another. Obvious, and usually already reported.

Layer 2 — the API. The page shows a generic “If an account exists…” message, but the JSON behind it doesn’t:

// registered


HTTP/1.1 200 OK

{“status”: “success”, “message”: “Request processed”}

// unregistered

HTTP/1.1 200 OK

{“status”: “error”, “message”: “User does not exist”}

Same status code, different body. In Burp, send both requests to Comparer and diff status, headers, body, length and redirects.

Layer 3 — timing. Identical responses can still differ in time, because a real account triggers extra work (token creation, sending an email). Send 20–30 requests for each identifier and compare averages. One slow response proves nothing; a consistent gap does.

Severity check: enumeration is information disclosure, not takeover. Many programs mark it informative unless the platform is sensitive (health, dating, finance) or you can chain it.

*2. Parameter manipulation: who does the backend actually trust?*

Many reset endpoints take more than just email in the body. The question is whether the backend independently validates each parameter, or just trusts whatever the client sends.

HTTP Parameter Pollution (HPP). Send the email field twice, or as an array, and see which account the backend acts on — and who the link actually gets mailed to.

email=victim@mail.com&email=attacker@mail.com

{“email”: \[“victim@mail.com”, “attacker@mail.com”\]}

This isn’t theoretical. A GitLab report (HackerOne #2293343) showed that sending the email field as an array caused the reset link to go to both the victim’s and the attacker’s inboxes — letting the attacker complete the reset with no interaction from the victim. A similar bug in ReadMe’s reset flow worked the same way: a duplicated email parameter made both addresses receive the link, so the attacker could take over using their own copy.

Also worth trying: a CRLF-style injection to append a second recipient (email=victim@mail.com%0A%0Dcc:attacker@mail.com), and swapping email for a user\_id or similar identifier the frontend never exposes but the API still accepts.

Testing approach (two accounts you control):

1. Capture a normal reset request in Burp.

2. Duplicate the identifier field, as a repeated param and as a JSON array.

3. Check where the email actually lands — not just what the API responds with.

4. Try conflicting identifiers (email of account A + user\_id of account B) and see which one wins.

The goal is to map the server’s real lookup logic, not just throw payloads at it.

*3. Normalization, Unicode, and multi-tenant collisions*

Case, spaces, encoding. Test whether Researcher@Example.com, a trailing space, or URL-encoded characters resolve to the same account as the plain registered email — and whether registration, login, and password reset all normalize the same way. A mismatch between flows (login is case-insensitive, reset is case-sensitive) is itself a bug worth flagging.

Unicode normalization — a real-world account takeover pattern.

GitHub disclosed a password reset vulnerability in 2016 involving Unicode characters in email addresses. Its lookup process could normalize an attacker-supplied address to match another user’s account, while the reset token was delivered to the submitted address.

Django experienced a related issue, tracked as CVE-2019–19844. A crafted Unicode email address could match an existing user’s email after case transformation, allowing the reset token to be sent to the submitted address instead of the registered one.

A more recent example is Weblate’s CVE-2026–134838, published in November 2026, which involved Unicode case-insensitive email matching in its password reset flow.

**The pattern to test for: does the app perform its lookup using a normalized identifier but deliver the reset link using the raw, attacker-controlled value?** If those two steps use different values, that’s where account takeover can happen.

Multi-tenant apps. If the same email can exist under two different organizations, check whether the tenant/org ID is something the client supplies and the server trusts blindly. Initiate a reset from each tenant with accounts you control, compare the requests, and try swapping the tenant identifier to see if it changes which account gets resolved.

**4. Rate limiting, and what actually makes a report**

Even an app that doesn’t leak account existence directly should still throttle reset requests. Check whether the limit is per-IP, per-identifier, or both, and whether it can be bypassed by rotating identifiers or source IPs. Weak limits don’t cause takeover by themselves, but they turn a slow manual enumeration into an automatable one — and can enable reset-request flooding against real users.

**Identification-stage checklist**

**Area → What to check**

Enumeration → UI message, API body, response timing

Normalization → Case, whitespace, encoding, Unicode

Parameter trust → HPP, arrays, CRLF injection, alternate identifiers

Multi-tenant → Client-supplied tenant/org ID

Rate limiting → Per-IP vs per-identifier, bypass via rotation

What makes it a strong report

A working exploit needs all of: the exact behavior, the security boundary it violates, reproducible steps on accounts you control, and the concrete impact (not just “a parameter can be modified”). “I can see the response differs” is a weak enumeration report; “here’s the reset link landing in both inboxes, with a screen recording” is a strong takeover report.

At this point, the password hasn’t even been touched, and things are already going wrong.

Imagine what happens when we get to the token.

In Part 2, we’ll look at what happens after identification — how reset tokens are generated, what makes them predictable, and why a token that looks random isn’t necessarily secure.

Because apparently, generating a password reset link is also an opportunity to make questionable security decisions.
