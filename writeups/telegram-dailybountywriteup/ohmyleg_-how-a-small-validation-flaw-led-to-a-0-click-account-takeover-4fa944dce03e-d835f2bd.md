# How a Small Validation Flaw Led to a 0-Click Account Takeover

- **Source URL:** https://medium.com/@ohmyleg_/how-a-small-validation-flaw-led-to-a-0-click-account-takeover-4fa944dce03e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260519145311/https://medium.com/@ohmyleg_/how-a-small-validation-flaw-led-to-a-0-click-account-takeover-4fa944dce03e
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13379 (id 13379)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How a Small Validation Flaw Led to a 0-Click Account Takeover

Bug bounty hunting, for me, is mostly about understanding how applications handle authentication. Login, registration, password reset. Things that look normal on the surface often hide interesting behavior underneath.

In this case, everything started from something very small. At first, it did not look important. But after digging a bit deeper, it turned into a full account takeover without any interaction from the victim.

## **Getting Started**

The target had a pretty standard authentication setup:

- Email and password login
- Password reset protected by reCAPTCHA
- Google OAuth login

I started as usual by opening Burp Suite, intercepting requests, and observing how the application behaves under different conditions.

At first, nothing seemed unusual.

## Testing the Password Reset Flow

I began with the password reset feature. My goal was simple. I wanted to see how the system reacts when validation fails.

So I modified the request and corrupted the `recaptcha_token`

The server responded with an error, which was expected.

But in that same response, I noticed something I did not expect:

a `state_token` was still returned

That immediately caught my attention.

Normally, when validation fails, the system should not return any token that can be reused.

I decided to save that token and continue testing.

## Moving to the OAuth Flow

Next, I tested the Google OAuth login.

The flow was standard:

- Redirect to Google
- Authenticate
- Return to the application with a callback

In the callback request, I saw several parameters such as:

- `state_token`
- Registration-related parameters
- Email hint

At this point, I remembered the token I got earlier.

I started wondering if that token could be reused here.

## Combining the Flows

I initiated the OAuth login using my own account.

After authentication, I intercepted the callback request.

Then I tried something simple:

- Replaced the `state_token` with the one obtained from the password reset flow
- Adjusted the parameters to continue the registration flow
- Modified the email hint

There was no complex payload involved. Just a few parameter changes.

## Unexpected Behavior

The modified request did not immediately succeed. The application returned an error and asked me to restart the process.

So I clicked **Start over**.

This is where things got interesting.

I was redirected to a registration page.

And the email field was already filled.

Not with my email, but with the victim’s email


At that point, it became clear that the system was trusting the `state_token` to determine user context.

## Completing the Flow

From there, I continued as if it was a normal registration:

- Entered a password
- Submitted the form

There was no additional verification:

- No email confirmation
- No OTP
- No identity check

The process completed successfully.

And I was logged in as the victim.

## Impact

Without any interaction from the victim, without knowing their password, and without accessing their email, I was able to gain a valid session.

This qualifies as:

0-click Account Takeover


## **Why This Happened**

After analyzing the behavior, the issue came from a combination of problems:

- The password reset flow returned a valid `state_token` even when validation failed
- That token could be reused in another flow
- The OAuth flow did not properly validate whether the token matched the authenticated user
- The system relied on client-controlled parameters to determine identity

Individually, these issues might not seem critical.

But when combined, they led to a complete authentication bypass.

## Final Thoughts

This finding did not require advanced techniques.

It started from a simple observation:

a token returned when it should not have been


From there, everything slowly connected.

And what looked like a small issue turned into something much more impactful.
