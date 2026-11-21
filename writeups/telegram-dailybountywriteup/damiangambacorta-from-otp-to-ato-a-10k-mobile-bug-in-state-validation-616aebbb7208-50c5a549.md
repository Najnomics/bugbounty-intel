# From OTP to ATO

- **Source URL:** https://medium.com/@damiangambacorta/from-otp-to-ato-a-10k-mobile-bug-in-state-validation-616aebbb7208?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905191753/https://medium.com/@damiangambacorta/from-otp-to-ato-a-10k-mobile-bug-in-state-validation-616aebbb7208
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9751 (id 9751)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From OTP to ATO: A $10K Mobile Bug in State Validation

Account takeovers (ATO) usually rely on social engineering or password reuse. But what if you could bypass the entire login flow just by modifying the response of a mobile app?

In this write-up, I’ll show how I discovered a broken state management system that allowed me to change the password of any user — **without ever completing OTP verification**. With just an email address and a Burp Suite match-and-replace rule, I gained full access to any account.

The vulnerability was acknowledged as critical due to its impact and trivial exploitability.

The app has SSL pinning, so bypassing it was the first step. I recommend this post: [https://medium.com/@neelamsoni/ssl-bypassing-without-using-jailbroken-ios-device-and-burpsuit-447f4fd3c210](/@neelamsoni/ssl-bypassing-without-using-jailbroken-ios-device-and-burpsuit-447f4fd3c210)

## Vulnerability Overview

- **Affected app**: Event Registration APP
- **Core issue**: Lack of server-side state validation between critical flows
- **Key exploitation point**: Manipulating JSON responses to bypass OTP and trigger password reset and login views
- **Tools used**: Burp Suite (match & replace), scripting, manual testing.

## Vulnerability Summary

The mobile app exposed two major logic flaws:

1. **Password reset flow accepted an OTP ‘key’ without verifying it server-side.**
2. **Login from a new device triggered an OTP, but the response could be manipulated to bypass verification entirely.**

Combined, these flaws allowed:

- Changing the password of any user using only their email
- Logging into any account without OTP validation
- Full account takeover (ATO) without ever touching the user’s phone

## Discovery & Initial Analysis

While testing the app, I triggered a password reset and started monitoring requests. I noticed the following:

- A `key` value was returned from the endpoint `/api/otp/sendAuthCode`
- This `key`, combined with the user's email and a new password, was submitted to `/api/login/findPasswordSave`

Here’s the kicker: **there was no server-side verification of whether the OTP had actually been entered.**

If I had a valid `key`, I could change the password of the user. The client (mobile app) was solely responsible for showing the OTP page, not enforcing it.

## A Closer Look: Burp Match & Replace

I realized that instead of doing any scripting, I could intercept and modify the app’s responses directly using Burp Suite. Here’s how I used **Match & Replace** rules to trick the app:

1. Replace `"needLogin":true` with `"needLogin":false`
2. Replace error messages like `"errorCode":"otp.code.error"` with `"errorCode":""`
3. Inject fake `loginOtpToken` and `key` values

**With these modifications, the app displayed the password reset screen *as if* the OTP was verified.**

I could then submit a new password and change the victim’s account credentials.

Classic vulnerability when the last step assumes that if reached to that point, everything worked before.

## Full Account Takeover (ATO)

Once the password was changed, the login flow presented another problem: **device ID validation.**

When logging in from a new device, the app would normally send an OTP to the phone number and not allow the access to the APP, unless completed. This was part of the challenge to make it FULL ATO.

As with the previous case, I analyzed the standard flow and realized that I could:

- Modify the device ID manually in requests
- Replace OTP enforcement responses to simulate success

**Result: I could log in with any valid email + encrypted password combo, using my own device ID, and the backend happily gave me a session.**

## Impact

- Mass account takeover with **just an email address**
- No need for password knowledge or OTP interception
- No real device fingerprinting or validation in place
- Trivial automation potential

This was classified as **Critical** by the program, as it affected all users and required zero user interaction.

*The issue was complex and took several hours to fully reproduce. In cases where multiple steps are involved, I always create a script — usually in Python or Bash — to make the triager’s job easier. It’s important to remember that triagers are people too; they may not be deeply familiar with every asset, so providing a clear proof of concept or an automated script can significantly streamline the triage process.*

*That said, I don’t recommend investing time in building a script until the report has been validated as new and not a duplicate — this helps avoid unnecessary effort on PoCs that might end up being discarded.*

## Technical Explanation: Trusting Previous States Is a Security Flaw

The application had multiple broken access control and logic flaws:

- **No server-side enforcement** of OTP validation state
- **State decisions made entirely on client-side responses**
- **Device ID was trusted without validation**

Many applications rely on a multi-step process — like password resets, email verification, or multi-factor authentication — where each step depends on the successful completion of the previous one. A common but dangerous mistake is to **assume that if the user has reached a certain step, they must have correctly completed the previous ones.**

This is known as **trusting client-side state** or **state-based trust**, and it introduces a serious security flaw.

**Why it’s vulnerable:**

- The client (browser, mobile app) controls what state to display, but **attackers can intercept and manipulate traffic**, skipping steps or injecting fake data.
- If the backend doesn’t strictly validate whether the correct flow was followed, an attacker can **bypass security checks** like OTPs, email verification, or device validation.
- In essence, the server trusts that “if you’re here, you must’ve done what you were supposed to before” — which is not always true.

## Conclusion

This bug is a perfect reminder that not all vulnerabilities are about complex exploits — sometimes it’s the simple things, like trusting the client, that lead to the most damage.

With a few tweaks in Burp and an understanding of how the app handled states, I was able to go from email-only knowledge to full account access.

If you’re developing mobile flows with OTP, password resets, or device validation: **double-check who your backend trusts.**

**Bounty?** 10k bounty was awarded for this critical Bug!

## Work With Us

At **OliveX**, we don’t just identify vulnerabilities — **we help you fix them**.

From deep logic flaws to API abuse and mobile security, our approach combines real-world attacker techniques with actionable remediation support. If you’re looking to strengthen your app’s security posture, let’s talk.

📩 Contact us at [www.olivex.io](https://www.olivex.io/) / hello@olivex.io

**Written by** [**@g4mb4**](https://www.linkedin.com/in/dgambacorta/) — Top 5 HackerOne researcher in Argentina and founder of OliveX.
