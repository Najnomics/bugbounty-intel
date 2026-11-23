# Account Takeover (Same OTP)

- **Source URL:** https://medium.com/@raxomara/account-takeover-same-otp-81bfba35d9b3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241118084849/https://medium.com/@raxomara/account-takeover-same-otp-81bfba35d9b3
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7087 (id 7087)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello everyone

I hope you’re all doing well! Today, I want to share a fascinating account takeover vulnerability I recently discovered. Let’s dive into the details.

I was testing a secure website and found a login page where you first had to enter your phone number. An OTP (One-Time Password) would then be sent to your phone, which you had to enter to validate your login. If the OTP was correct, you’d successfully gain access to your account.

Pretty straightforward, right? But here’s where it gets interesting…

What would you do in this situation?

Are you thinking about brute-forcing the OTP to find the correct code?

Or maybe you’re considering whether the OTP might be leaked in the response when requesting it?

You’re wondering if you could bypass the OTP validation altogether by removing a relevant parameter and sneaking right into the account?

Nope… The vulnerability I discovered was even more intriguing than that!

Brute-forcing the OTP wasn’t an option because, after three failed attempts, the OTP would be invalidated. Plus, there was a rate limit on OTP validation requests.

None of the other tricks I mentioned earlier worked either, and even some that I didn’t mention fell flat. The login process seemed pretty secure. It looked like there was no vulnerability to be found, and that would be the end of this write-up.

Just kidding.

After a bunch of failed attempts and hitting dead ends, I decided to try something different, a race condition attack on the OTP generation process. That’s right, I exploited a race condition by sending OTPs to two different phone numbers, and… BOOOOOOOOOM!

I couldn’t believe it, but it worked. The same OTP was sent to both numbers!

I believe the OTP generation process was time-dependent, which is why we were able to exploit the race condition and send the same OTP to two different numbers.

Goodbye until the next write-up
