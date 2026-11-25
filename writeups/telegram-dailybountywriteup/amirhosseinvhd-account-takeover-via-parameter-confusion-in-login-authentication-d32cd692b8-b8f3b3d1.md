# Account Takeover via Parameter Confusion in Login Authentication

- **Source URL:** https://medium.com/@amirhosseinvhd/account-takeover-via-parameter-confusion-in-login-authentication-d32cd692b8db
- **Fetched from:** https://medium.com/@amirhosseinvhd/account-takeover-via-parameter-confusion-in-login-authentication-d32cd692b8db?source=rss-49b9687d34b0------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14884)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** theemi / Thu, 27 Aug 2026 10:44:54 GMT

One day, while testing an application, I came across a relatively simple login flow.

The application allowed users to authenticate using either their **phone number or email address**. The initial request accepted one of these identifiers and generated a dynamically created “nonce”.

After submitting the OTP, the application used the previously generated “nonce” together with the OTP to verify the authentication attempt. If the verification was successful, the server returned an authentication token.

At first glance, the authentication flow appeared to be straightforward:

**The Initial Login Request**

The first request in the authentication flow accepts a phone number or email address and generates a “nonce”. The “nonce” is a GUID that is bound to the generated OTP and is later used during the OTP verification step.

**Figure 1 — Login request containing the mobile number and generated “nonce”**

After receiving the OTP, the application sends a second request containing the “nonce” and OTP.

If the verification succeeds, the server returns an authentication token.

**Figure 2 — OTP and “nonce” verification request returning the authentication token**

At this point, everything looked normal.

**Looking for Something Interesting**

I had already gone through the usual authentication test cases and covered the expected attack surface. At first glance, the login flow looked fairly straightforward, and there didn’t seem to be much room for anything particularly interesting.

But then, **boom!**

Something caught my attention.

The verification request appeared to rely solely on the “nonce” and OTP, without carrying the authentication identifier itself. That small detail immediately raised a more interesting question: **what exactly was the “nonce” bound to?**

If the “nonce” was only associated with the OTP, rather than being strictly tied to the identifier that initiated the authentication flow, there might be a way to cross the boundary between different authentication identifiers.

So I decided to test a rather unconventional idea:

**What if I could generate the same “nonce” for two different phone numbers?**

If successful, this could potentially allow me to confuse the authentication flow and make the server associate an OTP verification with the wrong account.

I spent quite some time trying to achieve a “nonce” collision between two different phone numbers.

Unfortunately, it didn’t work.

After several attempts, I realized that this approach probably wasn’t going anywhere.

Then, another idea came to mind.

**The Turning Point**

The application supported two different login identifiers:

Under normal circumstances, the user was expected to provide **one identifier at a time**.

So I decided to break away from the intended flow and send both parameters together.

Instead of:

mobile → Login → “nonce”

or:

email → Login → “nonce”

I tried:

mobile + email → Login → “nonce”

**Figure 3 — Sending both mobile and email parameters in the same request and receiving the OTP on the mobile number**

The application responded in an interesting way.

The OTP was sent to the **phone number**.

At first, I thought the idea had failed.

But then I noticed something important.

I had added the phone number as the **second parameter** in the JSON body.

That made me think about how the backend was handling these two identifiers.

So I removed the phone number and sent the same email address again, this time as the only identifier.

And then…

**Boom!**

It worked.

The application generated the **exact same “nonce” again**.

**Figure 4 — Sending the email alone and receiving the previously generated “nonce” again**

This was the first major breakthrough.

The application had generated the same “nonce” for the authentication flow involving the different login parameters.

At this point, I had a new hypothesis:

**If the same “nonce” could be reproduced, could the OTP generated in the previous flow also be reused?**

**Testing the OTP**

Before attempting anything against another account, I wanted to validate the behavior using identifiers that I controlled.

I already had an OTP generated through the mobile-based flow.

I then tested whether that same OTP could be used with the email-based flow associated with the same authentication state.

**Figure 5 — Reusing the OTP obtained through the mobile flow with the email-based flow**

The OTP was accepted.

This was the second major breakthrough.

The “nonce” and OTP were not being strictly bound to a single login identifier.

The authentication flow could therefore be represented as:

At this point, I had confirmed the behavior using accounts and identifiers that I controlled.

The next step was to determine whether the same weakness could affect another user’s account.

**Exploiting the Issue**

With the behavior confirmed, the final step was to reproduce the same flow using the target account’s identifier.

The application allowed the authentication request to be constructed using both mobile and email, while generating a “nonce” that was not uniquely bound to a single identifier.

Once the appropriate “nonce” and OTP were available, I sent them to the verification endpoint.

**Figure 6 — Sending the OTP and “nonce” to the verification endpoint and receiving the victim’s authentication token**

The server accepted the verification request and returned a valid authentication token associated with the target account.

I then used the returned token to authenticate to the application.

The token was valid, and I was fully authenticated as the victim.

At this point, the impact was no longer theoretical.

**I had successfully achieved a full Account Takeover.**

**Root Cause**

The root cause of the vulnerability was the way the application generated and associated the “nonce” with the login identifiers.

The application supported two different authentication identifiers:

mobile

However, when both parameters were supplied, the application generated a single “nonce” that could be associated with both authentication contexts.

Conceptually, the vulnerable behavior looked like this:

The critical issue was that the “nonce” was not uniquely bound to **one specific authentication identifier and one authentication attempt**.

The application’s intended behavior was to accept either an email address or a phone number for a login attempt. However, the backend allowed both identifiers to participate in the same authentication flow.

As a result, the same authentication state could be reproduced across the email and mobile login parameters.

Because the subsequent verification endpoint relied on the “nonce” and OTP, this parameter confusion ultimately allowed the authentication flow to be manipulated and resulted in the issuance of a valid authentication token for another user’s account.

**Impact**

This vulnerability allowed an unauthenticated attacker to bypass the intended authentication flow and obtain a valid authentication token for another user’s account.

The impact included:

The issue was therefore not merely a parameter-validation problem. The vulnerable parameter handling directly affected the application’s authentication boundary and allowed an attacker to authenticate as another user.

**Attack Flow**

The complete attack chain can be summarized as follows:
