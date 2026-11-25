# When an Old Password Reset Token Still Worked

- **Source URL:** https://medium.com/@sanjivanidobhal05/when-an-old-password-reset-token-still-worked-27700d63d767
- **Fetched from:** https://medium.com/@sanjivanidobhal05/when-an-old-password-reset-token-still-worked-27700d63d767?source=rss-10cd7e4b4fb2------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14893 (id 14893)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Sanjivani Dobhal / Wed, 02 Sep 2026 03:31:00 GMT

While testing a web application, I decided to look beyond the usual password-reset checks.

Instead of asking:

***“Can I reset the password?”***

I asked:

***“What happens to an old reset token after the password is changed?***

That simple question led me to an interesting authentication issue.

When you click **“Forgot Password”**, the application usually generates a temporary token or code and sends it to your email.

Think of it as a temporary key that allows you to reset your password.

Ideally, these tokens should have a controlled lifecycle — including proper expiration and invalidation when they are no longer supposed to be usable.

I generated a password reset token but intentionally didn’t use it.

Then I:

The application still accepted the previously generated reset token.

Reset Token Generated

↓

Password Changed Normally

↓

Old Token Replayed

↓

Token Still Accepted ❗

This was the behavior that caught my attention.

A password-reset token is a sensitive authentication credential.

If an old token remains usable when it should have been invalidated, someone who obtains that token may potentially use it to reset the account password again.

The important lesson for me was that security testing isn’t always about finding a vulnerable endpoint.

Sometimes the interesting bugs appear when **two individually normal features interact in an unexpected way.**

I used **Burp Suite Repeater** to replay the previously generated reset request after changing the account password.

This allowed me to test whether the application’s authentication state had actually changed or whether the old reset credential was still being accepted.

After reproducing the behavior, I responsibly reported it to the security team with:

The security team responded that the issue was **already known**, so my report was marked as a duplicate and was not eligible for a bounty.

Although it was a duplicate, it was still a valuable learning experience.

This finding taught me three important things:

**1. Test workflows, not just endpoints.**

Don’t stop at “Does this feature work?”

Ask:

***“What happens when I combine this feature with another feature?”***

**2. Think about token lifecycles.**

Ask when a token is:

**3. Manual testing matters.**

Logic-based issues can be difficult for automated tools to identify because they often depend on the **sequence of actions and application state**.

This was one of my early experiences with real-world web application security testing.

The report may have been a duplicate, but the process taught me how to analyze authentication workflows, use Burp Suite for manual testing, reproduce an issue, and report it responsibly.

For me, security research is not just about getting a bounty.

It’s about asking better questions.

***“What happens if I do this… after I do that?”***

That’s where interesting bugs can hide. 🔐

**#CyberSecurity #BugBounty #WebSecurity #VAPT #SecurityResearch #BurpSuite #EthicalHacking #Authentication #ResponsibleDisclosure**
