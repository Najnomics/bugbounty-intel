# OTP BYPASS IN REGISTRATION PAGE

- **Source URL:** https://medium.com/@ghostxzx/otp-bypass-in-registration-page-7fd0d07a431b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260306134252/https://medium.com/@ghostxzx/otp-bypass-in-registration-page-7fd0d07a431b
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/12901 (id 12901)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello everyone,

how are you? This is my first report about a web vulnerability 

I recently discovered on a website on the Hackeron platform.

Read till end❤


The vulnerability was identified as duplicate, 

but I’m happy with that outcome because it’s the first effective vulnerability 

I discovered that wasn’t marked as N/A.


First, I will explain what the vulnerability is,

how it was found, and where. I will also reproduce it with the same technical details,

### What is the OTP Bypass vulnerability?


An OTP bypass web bug is a security vulnerability where an attacker can circumvent 

the One-Time Password (OTP) verification 

process to gain unauthorized access to a user’s account or perform sensitive operations.

This is often due to improper implementation or logical flaws in the application’s authentication mechanism, 

rather than a flaw in the OTP concept itself.

In my case, the vulnerability wasn’t as severe as in the ATO case; 

it was on the registration page, for example, 

allowing you to register with someone else’s emails without their knowledge or permission.

This is indeed dangerous and can be classified as medium to high risk.

.

.

.

Now let me explain how I found it::


Ambition and persistence are the most important things for finding web vulnerabilities because discovering vulnerabilities is very tedious,

especially logic vulnerabilities. That day, I was unusually excited to discover vulnerabilities and said,

"I must discover a vulnerability today."

I chose a target, and right at the beginning, on the registration page,

and to my surprise, less than 10 minutes had passed.

## ٍSteps to Reproduction:

1.Create two email addresses, one for the hacker and the other for the target.

2.Register using the hacker email address officially; you will receive a code via email.

3.Now run Burp to capture the hacker email request.

4.Now copy the response in any note app keep it

5.Now try to register using target email .

6.Enter and wrong code and intersept the request and do introder ,

and now paste the hacker response in target response and forward the request.


..YOU NOW Bypass the otp

Thank you for reading to the end.
