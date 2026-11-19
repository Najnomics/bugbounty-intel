# When OAuth Works Correctly and Security Doesn’t

- **Source URL:** https://medium.com/@0xnexus0xfault0x/when-oauth-works-correctly-and-security-doesnt-a-bug-in-oauth-account-linking-7f24bfdf91f0
- **Fetched from:** https://web.archive.org/web/20261111042435/https://medium.com/@0xnexus0xfault0x/when-oauth-works-correctly-and-security-doesnt-a-bug-in-oauth-account-linking-7f24bfdf91f0
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14973 (id 14973)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **When OAuth Works Correctly and Security Doesn’t: A Bug in OAuth Account Linking**

*How a flaw in account linking lets an attacker attach their own Microsoft account to your profile, and why having a state parameter guarantees nothing.*

**Note.** At the request of the company’s security team, I’m not naming the platform or sharing screenshots or internal URLs. The report was submitted through the official channel. Status: fixed.

**TL;DR.** The account-linking callback accepted a state value that was never tied to the session that created it, and attached the external account to whoever was logged in when the callback arrived. That is a CSRF in account linking, and in my testing it led to account takeover. This is not a Microsoft bug: it is a flaw in how the application handles the result of external authorization.

## How It Started

I was looking for a bug bounty program and came across an interesting SaaS project that had its own program on a separate page. I started testing the site, and while looking at OAuth, I ran into an issue with the state query parameter.

What caught my attention wasn’t the Microsoft login itself, but a feature that people usually glance over: **linking a Microsoft account to an existing profile.**

## Login and Account Linking Are Not the Same Thing

From the outside, both flows look identical: the user goes to the provider, authenticates, and returns to the site. But the server has different jobs in each case.

- **Login.** Figure out whose external account has just been authenticated.
- **Account Linking.** Do the same, and also make sure the account is linked to the profile of the person who actually started the operation.

If that second check is weak, an external account can end up attached to the wrong profile. And since a linked provider often works as another way to sign in, this is no longer a minor misconfiguration. It’s a hole in authentication.

## How I Tested It

I created two test accounts, A (the attacker) and B (the victim), and worked through Burp Suite. I first studied the regular Microsoft login, then the linking flow. I looked at five things:

- which parameters are sent when OAuth starts;
- how state is generated and validated;
- where the session context is stored;
- how the callback is handled;
- what data the server uses to choose the account the external identity is added to.

At first glance everything looked fine: state was there, and the OAuth steps worked as expected. But I noticed a difference in how Login and Linking handle the user’s context.

## The Hypothesis

It’s not enough for state to simply exist and not be expired. It has to be tied to **the session that started the operation.** And when the callback arrives, the server should take the target account from the context saved at the start, not from whichever session happens to be active when the user returns.

My guess was that the platform checks whether a transaction is *valid*, but not *who it belongs to*.

## What the Problem Turned Out to Be

The hypothesis held up. There were two flaws working together:

- state was not strictly bound to the original session;
- when finishing the linking, the application relied on the current session rather than the context saved at the start.

As a result, the outcome of one linking operation was applied to a different account. This is a classic **CSRF in account linking.** The problem isn’t Microsoft OAuth. It’s how the application handles the result of external authorization.

## What the Attack Looks Like

Here is how I reproduced it between my two test accounts. Account A plays the attacker, account B plays the victim. The attack has two phases: in the first, the attacker only works with their own session; in the second, the victim comes into play.

## Phase 1: Preparation (attacker)

The attacker runs the normal linking flow with their own Microsoft account, but never lets the site process the final callback.

1. The attacker clicks the “Link Microsoft account” button on the site.
2. The site redirects them to Microsoft with its own state value (state\_attack in the figure).
3. The attacker authenticates with their Microsoft login and password.
4. Microsoft shows a page asking to confirm or deny linking the account to the website.
5. The attacker clicks “Agree”.
6. Microsoft redirects the browser to website/callback?code=…&state=state\_attack. The attacker catches this request in Burp Suite and does not follow the redirect, keeping code and state for later.

Now the attacker holds a valid, unused callback URL tied to their own Microsoft account.

## Phase 2: Execution (victim)

7\. The attacker sends the victim the saved callback link, for example by email or on a web page.

## Get Nexus0xFault’s stories in your inbox

Join Medium for free to get updates from this writer.

8\. The victim, who is logged in to the platform, opens the link. The server sees a valid code and a state it recognizes, but never checks that this state was issued to a different session. It links the attacker’s Microsoft account to the victim’s profile.

9\. If the platform allows sign-in through a linked provider, the attacker logs in with “Sign in with Microsoft” and lands in the victim’s account.

## When It Works and When It Doesn’t

The result at step 8 depends on the victim’s state:

- **Victim not logged in:** the site returns a 401 error. Nothing is linked.
- **Victim logged in, no Microsoft account linked yet:** the attacker’s Microsoft account is linked. This is the vulnerable case.
- **Victim logged in, Microsoft account already linked:** the site returns an error and does not re-link.

Two practical notes. The callback is an ordinary top-level GET navigation, so it doesn’t matter that session cookies are SameSite=Lax: the browser still sends them. And the authorization code is short-lived, so in a realistic scenario the victim has to open the link soon after the attacker obtains it.

## Why the Standard Checks Didn’t Help

A state value can be present, have an expiration time, and pass validation. But if it isn’t tied to a specific session, it only protects against the most primitive forgeries.

Checking redirect\_uri and making the code single-use don’t help either: in this attack the code is valid, unused, and goes to the legitimate redirect\_uri. PKCE and state would stop it, but only if the verifier and the state are bound to the browser session that started the flow. Here they weren’t. The flaw isn’t in the protocol, it’s in the application’s logic.

## What This Means for Users

The impact depends on the platform’s architecture. On my test accounts, signing in with the attacker’s Microsoft account opened the victim’s account (step 9). In the worst case, this is what happens:

- someone else’s external account appears in your profile without your knowledge;
- you get an extra way to sign in that is controlled by another person;
- that access may survive a password change for as long as the link stays active.

If the platform allows sign-in through a linked provider, this amounts to **Account Takeover.** If it doesn’t, the impact is smaller, but an unwanted external identity in your profile is still a violation of the account’s integrity. That is why I confirmed the sign-in step in testing instead of assuming it.

## Testing Ethics

I ran all tests only on my own two accounts. No real users’ data was touched, and there was no mass exploitation. In my report, I described the issue, the affected scenario, the root cause, and recommendations.

## How to Fix It

- **Bind state to the session and the transaction.** Checking existence and expiration isn’t enough. Store it server-side together with the session and user that started the flow, and compare on callback. Do the same for the PKCE verifier.
- **Take the target account from server-side context** saved when linking starts, and reject the callback if the current session belongs to someone else.
- **Make the transaction single-use** and invalidate its data after processing.
- **Require re-authentication** before adding a new way to sign in.
- **Notify the account owner** about every new link.

## Checklist for Testing Account Linking

- Is the original user context preserved throughout the entire transaction?
- Can the authorization result be applied to a different account?
- Is state bound to a specific session? Is the PKCE verifier?
- How does the server determine the target account in the callback?
- How does the callback behave when the user is logged out, or already has this provider linked?
- Can one external identity be linked to two profiles? What happens if it’s already linked to someone else?
- Is identity confirmation required before adding a new way to sign in?
- Can you sign in through the linked provider?

A useful trick: compare Login and Account Linking. Differences between their implementations often reveal what you can’t see when you test only one flow.

## Conclusion

Interesting bugs don’t always hide in protocols. Sometimes OAuth works perfectly and every parameter is in place, yet a single business-logic mistake opens the way to someone else’s account.

Account Linking shouldn’t be treated as a secondary profile setting. It’s a critical security operation that changes how an account can be accessed. Developers should treat it as seriously as primary authentication, and pentesters should make it a mandatory part of their testing.
