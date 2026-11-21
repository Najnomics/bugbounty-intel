# Account Takeover Based on Deep Understanding of the Target

- **Source URL:** https://medium.com/@Maverick0o0/account-takeover-based-on-deep-understanding-of-the-target-9c02b8af88fa?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250702074647/https://medium.com/@Maverick0o0/account-takeover-based-on-deep-understanding-of-the-target-9c02b8af88fa
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9359 (id 9359)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account Takeover Based on Deep Understanding of the Target

Hi there! Maverick here, and in this write-up, I’ll walk you through an interesting account takeover scenario.

First of all, our target has been active in the bug bounty scene for several years, with very few new features added recently. So, how come nobody has reported this account takeover vulnerability until now? What’s so special about it?

It all boils down to a deeper understanding of the target and detailed analysis. Sometimes, hidden features might exist that aren’t obvious at first glance.

The vulnerability was discovered in the password reset functionality. Here’s how the normal flow works: The user enters their mobile number or email address, receives an OTP code, and after entering it, they can reset their password.

Sounds pretty straightforward, right? But there’s a subtle difference in the OTP flow for emails and mobile numbers.

For mobile numbers, there’s a rate limit. If you send more than three consecutive OTP requests, your IP gets temporarily blocked. Additionally, the developer implemented a second layer of rate limiting as a custom security measure.

The second rate limit kicks in if a user sends more than five OTP requests to a mobile number, activating a “Reverse Confirmation” process.

But what exactly is “Reverse Confirmation”? Normally, you receive an OTP on your device and enter it on the website. In Reverse Confirmation mode, however, the backend sends an OTP to your phone, and you must text this OTP from the phone number you want to reset the password for, to a specific number provided by the system.

During this process, every second, a GET request is sent to the endpoint **isPhoneConfirmed?phone=xxx** to check if the phone number has been confirmed.

Once confirmed, you’re redirected to the next step, where you can reset the account password by sending specific parameters to the endpoint **/api/v1/users/recovery**.

Important note: The CSRF token is not validated on the server side, and when using Reverse Confirmation, the parameter “code” uses four hashtags (#) instead of the real OTP, and you can only submit this request once. **The critical point here is, if an attacker sends this request before the victim, they can set any desired password for the victim’s account.**


We’ve identified a unique feature and an ambiguous scenario, but how can we exploit it effectively to perform an account takeover?

First, we activate Reverse Confirmation for the victim’s account by sending at least six OTP requests to their mobile number.

Next, we must force the victim to reset their password. (At this point, Reverse Confirmation is active, and the victim must text the backend-generated OTP to a specific number.) This step typically requires social engineering or interaction with the victim, significantly influencing our CVSS score. However, upon deeper analysis of the target, I found a defense mechanism that allows me to lock the user’s account, forcing them to reset their password.

As the victim texts the OTP to the designated number, we continuously send requests to the endpoint **isPhoneConfirmed?phone={target\_phone}**, checking when the victim confirms their number. As soon as it’s confirmed, we immediately send a password reset request with the victim’s number to the endpoint **/api/v1/users/recovery**.

(Due to the rate limit on the password reset endpoint, we first verify phone confirmation through **isPhoneConfirmed** before sending the password reset request.)


To automate the entire process, I wrote a Python exploit script that only requires the victim’s mobile number and handles all the following steps:

1. Locks the user’s account.
2. Activates Reverse Confirmation.
3. Forces the user to reset their password.
4. Constantly checks if the victim has confirmed their phone number.
5. Immediately resets the password once the victim confirms their phone number. (Since this operation can only be performed once, the exploit must act faster than the victim.)

# Conclusion

The deeper we dive into our targets and uncover more hidden features, the higher the chance of discovering severe vulnerabilities. Additionally, chaining seemingly harmless bugs or those with low CVSS scores can often lead to identifying critical or high-severity vulnerabilities.
