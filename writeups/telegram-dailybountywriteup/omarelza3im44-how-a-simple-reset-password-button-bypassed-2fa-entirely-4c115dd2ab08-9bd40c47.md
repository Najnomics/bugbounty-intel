# How a Simple Reset Password Button Bypassed 2FA Entirely

- **Source URL:** https://medium.com/@omarelza3im44/how-a-simple-reset-password-button-bypassed-2fa-entirely-4c115dd2ab08
- **Fetched from:** https://medium.com/@omarelza3im44/how-a-simple-reset-password-button-bypassed-2fa-entirely-4c115dd2ab08?source=rss-9f0daf2ee15a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14893)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Omar Zaky / Tue, 01 Sep 2026 20:17:24 GMT

Ever had that moment where you find a bug so simple, you just sit back and laugh at how easy it was?

While testing a target recently, I bumped into a classic logic flaw that completely shattered the application’s 2FA protection. Unfortunately, someone beat me to it and the report was marked as **Duplicate** — but the trick itself is way too cool not to share.

Here is the story of how a password reset logic flaw let me walk right past 2FA without typing a single digit.

I was playing around with the login flow of the target application. Everything seemed standard:

So far, so good. The front door was locked tight. But what happens if we step side-ways instead of trying to push through the front door?

While staring at the 2FA prompt screen, I noticed a tiny, innocent-looking link at the bottom: **“Forgot Password?”**

Usually, if you click “Forgot Password” while trying to log in, it just sends an email link to reset your credentials. But I wondered: *How is the backend tracking my current state right now?*

So I decided to test it out:

And guess what? **I was fully logged in.** 🎉

No 2FA code. No OTP validation. Straight into the user’s account.

This is a classic **Business Logic & State Management Flaw**.

When you log in with a password, the application knows you got step 1 right, but it’s supposed to hold you in a temporary, unauthenticated state until you pass step 2 (2FA).

However, when I requested a password reset from that screen, the backend server got confused. Instead of keeping me in the pending state (or clearing my session altogether), triggering the reset flow caused the backend to incorrectly elevate my session status to “Fully Authenticated”.

In short: The server assumed that because I owned the email box to request a reset, I was good to go!

Logic flaws are everywhere, and they don’t always require complex payloads, Burp macros, or automated tools. Sometimes, all it takes is clicking a standard button at the wrong stage of an authentication flow.

Even though this report ended up as a **Duplicate** for me, finding these subtle state confusion bugs is always a great reminder: **Never trust the app’s state logic!**

Happy hunting, everyone! 🚀
