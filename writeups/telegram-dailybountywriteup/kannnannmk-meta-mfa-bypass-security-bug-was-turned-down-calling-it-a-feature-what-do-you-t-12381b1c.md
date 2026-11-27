# Meta MFA bypass security bug was turned down, calling it a feature! What do you think?

- **Source URL:** https://medium.com/@kannnannmk/meta-mfa-bypass-security-bug-was-turned-down-calling-it-a-feature-what-do-you-think-9663e7c5a65e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240705045733/https://medium.com/@kannnannmk/meta-mfa-bypass-security-bug-was-turned-down-calling-it-a-feature-what-do-you-think-9663e7c5a65e
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6586 (id 6586)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Meta / Facebook MFA bypass security bug was turned down, calling it a feature! What do you think?

After a very long time, I was trying to login into my Facebook account,

1. I entered my username and password, but I was not able to login, there was a prompt asking me to enter the OTP that was sent to my WhatsApp number / Text message.
2. I am no more using that number and the WhatsApp number is invalid
3. So, now I tried to login into my Facebook account using **Google OAuth,** by using my gmail username as well as password. **This time again, I was prompted to enter OTP code sent to my WhatsApp number**

4\. Now, I am unable to login into my Facebook account by using my valid facebook login email / password, also by using Google OAuth

5\. Okay, now how to bypass this? I just logged in into my Gmail, and I saw a plenty of old messenger notifications

6\. I have opened one of the emails and it had two links , one to open the **messenger**, and other one to “**Go to profile**”, by clicking any of those, you will be redirected to a new page and prompted to enter username / password.

7\. Now enter your Facebook username and password, boom! you are now logged in, there **no WhatsApp OTP prompted**

I have reported this as an Authorization or MFA bypass vulnerability, but Meta Security have closed it and calling it as an intended functionality of the app.

I wanted to post this because, it didn’t make any sense to me on why that whatsapp OTP prompt was there during regular and Oauth login attempts, but why it was not promted if you login through your email link.

It was same login credentials that I was using during both scenarios, why it isn’t a security bug?

So please comment your opinions about this, is it a valid security bug or just a feature, because I am already able to bypass their **WhatsApp Verification** step, which was prompted during initial login as well as during **Google OAuth** login attempt
