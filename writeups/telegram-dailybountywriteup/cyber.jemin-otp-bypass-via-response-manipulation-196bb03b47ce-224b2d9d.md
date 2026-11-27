# OTP bypass via response manipulation

- **Source URL:** https://medium.com/@cyber.jemin/otp-bypass-via-response-manipulation-196bb03b47ce?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230613160440/https://medium.com/@cyber.jemin/otp-bypass-via-response-manipulation-196bb03b47ce
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2802 (id 2802)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello Hacker, I’m glad you’re back on my other blog. This time, I discovered my most recent finding on a private bug bounty programme. The vulnerability I discovered is the OTP bypass via response manipulation.

# What is OTP bypass via response manipulation

OTP (One-Time Password) bypass via response manipulation refers to a method where an attacker manipulates the response received during an authentication process to bypass the need for a valid OTP.

# Why it occurs

OTP bypass via response manipulation vulnerability can occur due to various factors, including Inadequate Response Validation, Lack of Integrity Checking,Insecure Communication Channels.

# Now Let’s look for vulnerability

I find out that the application requests an OTP in order to confirm the user’s identity when I browse through it. I first input the genuine OTP and evaluate the response. And I identify the application looking at the status code and user-id that we would receive after submitting an OTP. All we need to do is respond falsely to the real status and user-id.

## It’s time for practical

Create account on application.

Requesting OTP on mobile number.

Entering a random OTP and sending the request.

Captured request into Burp-suite with userId.

Response for wrong OTP.

Manipulated response with userId, status, and authId.

Successfully created account without using real OTP.

Thanks for reading!!

Keep Hacking!!
