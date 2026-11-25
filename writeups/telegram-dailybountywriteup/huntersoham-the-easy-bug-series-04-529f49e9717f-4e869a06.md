# The Easy Bug Series | #04

- **Source URL:** https://medium.com/@huntersoham/the-easy-bug-series-04-529f49e9717f
- **Fetched from:** https://medium.com/@huntersoham/the-easy-bug-series-04-529f49e9717f?source=rss-c501c19c2da6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14927 (id 14927)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Soham D. Jadhav / Tue, 29 Sep 2026 04:31:04 GMT

Is Your 2FA Really Protecting Your Account?

You Enabled 2fa.

You have your password.

You have your authenticator app.

Everything looks secure.

But is it? Let’s test this function.

Hello everyone 🙌

This is my 4th article of my series i hope you are enjoying this articles. Where i share my own methodologies while hunting on a targets, which helps beginners to find their first valid bug.

In today’s article, we’ll look at a small security issue that is often overlooked:

**What happens when a user tries to disable 2fa?**

We normally think about testing whether 2fa works during login.

but there is another question we should ask:

**What happens when we remove it ?**

Let’s find out.

First, Enable 2fa

start with an account that you used for testing.

Go to :

Account settings → Security → 2fa

Enable 2fa and complete the setup.

Make sure that 2fa is enabled successfully.

You should see somthing similar to :

Two-Factor Authentication: Enabled

\[ Disable 2FA \]

Now comes the interesting part.

Try to Disable 2fa

click: Disable 2fa

Don’n immediately assume that everything is secure.

look carefully at what happens next.

The application may ask you for something like:

Current password / Enter 2fa code / Please re-authenticate

This means the application is asking for verification while disabling 2fa which is an important security control.

But sometimes…

you click disable 2fa and it is immediately disabled.

No password asked…

No otp….

No re-authentication…

Just : 2fa enabled → disable 2fa → 2fa disabled

This is where our testing becomes intresting.

**Why Does This Matter?**

2fa is an additional security layer on an account.

if an attacker anyhow gets access to an active session and can disable 2fa without any additional verification, they may be able to remove an important security control from the account.

the impact depends on the application’s session and authentication behaviour.

**What Should You Check?**

Whenever you find a 2FA disable option, simply check:

\[ \] Is password required?

\[ \] Is OTP required?

\[ \] Is re-authentication required?

\[ \] Can 2FA be disabled directly?

\[ \] What happens to the existing session after disabling 2FA?

If 2FA can be disabled directly, retest it once or twice and verify the actual impact before reporting it.

**Don’t report it only because the password wasn’t requested.**

**Final Thoughts**

This is very simple security check, but it’s easy to overlook.

Whenever you see a sensitive endpoint or security testing, don’t just reply on it works or not:

Ask Yourself:

**Can this security control be removed without proper verification?**

That’s it for **The Easy Bug Series | #04**.

If you found this useful, **let’s connect and keep hunting together.**

**And One last question for you**

If you come at the end of this article you should think about this:

**If you find this vulnerability**, **what other vulnerability would you try to chain it with?**

Drop your answer in the comments. 👇

See you in the next one!

**Find me here:**

Happy Hunting! 🐞🔍

#BugBounty #WebSecurity #CyberSecurity #Pentesting #VAPT #BugBountyTips
