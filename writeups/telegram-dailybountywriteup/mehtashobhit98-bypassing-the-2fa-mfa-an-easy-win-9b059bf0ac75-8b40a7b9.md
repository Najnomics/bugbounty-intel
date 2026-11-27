# Bypassing the 2FA /MFA — An Easy win

- **Source URL:** https://medium.com/@mehtashobhit98/bypassing-the-2fa-mfa-an-easy-win-9b059bf0ac75?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230417233715/https://medium.com/@mehtashobhit98/bypassing-the-2fa-mfa-an-easy-win-9b059bf0ac75
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2381 (id 2381)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bypassing the 2FA /MFA — An Easy win

Hello Readers, Today I am going to tell how was I was to bypass the 2FA protection for a product based company main login page. I hope this blog help you learn something new and apply to your bug hunting techniques.

I was hunting on a VDP called : [MathWorks](https://www.mathworks.com/company/aboutus/policies_statements/vulnerability-disclosure-policy.html) , This is a company which makes Matlab software.

In the program there was nothing special mentioned about the in scope and out scope so started with the Login page of the main website.

After spending some time with the application I figured out that they have put new feature of 2FA/MFA for their users for better security. I started to dig more into that functionality as it was a new thing that they have rolled out.

I started playing with 2FA/MFA thing and figured out that you can setup the 2FA/MFA in three ways :-

1. Using Google Authenticator App
2. Receiving code via text message on mobile
3. Receiving code via email on your registered mail id.

I choose the email method and setup my 2FA/MFA with the code I got on email and logged out.

Now When I login again I was asked the code which I received on my email and instead of putting right code, I thought of why not to brute this with random codes and check the behaviour of application. I immediately put the request in intruder and generated random 6 digit codes (check below screenshot)

The response I got was completely eye-opener. After 200+ request the application log you in without the actual right 2FA/MFA token.

So I was logged into my account by just hitting the random 6 digit codes for more than 200 times.

I reported that to the team and they were also surprised of this beahaviour. I was not awarded any bounty for this but I got an acknowledgement letter from The MathWorks (check it [here](https://www.linkedin.com/feed/update/urn:li:activity:6699200337196253184/))

Thank You Reading.
