# 2FA Bypass

- **Source URL:** https://medium.com/@cybersekler/2fa-bypass-how-not-to-implement-two-factor-authentication-8351647ad8dc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105165410/https://medium.com/@cybersekler/2fa-bypass-how-not-to-implement-two-factor-authentication-8351647ad8dc
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4279 (id 4279)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 2FA Bypass: How not to implement two-factor authentication

--

Two-factor authentication (2FA) is an important security measure that helps protect against unauthorized access to accounts and systems. It requires a user to provide not just a password, but also a second form of authentication, such as a one-time code sent to a phone or email, or a biometric verification.

While 2FA is an effective way to increase the security of accounts and systems, it is possible that an attacker could try to bypass it using several methods. One such method is social engineering, which involves manipulating people into divulging sensitive information or taking actions that compromise security.

An example of using social engineering to bypass 2FA occurred in the Uber hack of 2022. The attacker sent numerous 2FA notifications to the victim and eventually convinced them to accept the request and grant access.

Today’s blog will discuss a 2FA bypass attack that was poorly implemented and lacked additional security measures, making it easy to bypass with a brute force attack.

# How I did do it?

While performing a pentest on the authentication system of a web application, I noticed that the 2FA code sent via email did not expire after a significant amount of time. I was able to use a code that had been generated a day earlier, which was the first red flag. This prompted me to investigate further, as it is common for one issue to indicate the presence of others.

I tested for the lockout threshold to see if I would be blocked after a certain number of attempts. I started with 3 consecutive tries and then increased to 5, but I was still able to try more codes. I then launched a brute-force attack using Burp Intruder with 10 requests, but I still wasn’t locked out, indicating that there was no lockout policy in place.

Next, I tested to see if there was any rate limiting implemented by sending 50, 100, and then 150 consecutive requests. Again, I was able to send more requests without any indication of rate limiting being implemented.

At this point, I started looking into the randomness of the codes being generated and noticed that the numbers were close to each other, indicating that the randomness was not sufficient and the codes could be easily brute-forced. I then launched an attack by sending an invalid code and captured the request using Burp, as shown in the redacted screenshots below.

Although the issue has since been resolved, the screenshots have been redacted for privacy reasons.

The previously received codes indicated that the correct code should be in the 3000 range. However, I decided to start the brute force attack from zero to demonstrate the danger of a weak 2FA implementation.

The screenshot below shows that the brute force was successful and I have highlighted the correct code, as well as the differences in the responses to other requests. This confirms that the code was indeed correct, and I was able to successfully log in.

As I mentioned before the issue has been resolved and proper two-factor authentication along with other security measures has been implemented. It is a positive sign that 2FA was already in place for this web application, as it demonstrates a commitment to security that is not always present in other web applications I have tested in the past that did not even offer 2FA as an option.

Hope you enjoyed this short demonstration. Stay curious and see you next time.
