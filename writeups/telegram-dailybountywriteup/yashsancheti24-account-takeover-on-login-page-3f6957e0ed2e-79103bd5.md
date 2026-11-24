# Account Takeover on login page

- **Source URL:** https://medium.com/@yashsancheti24/account-takeover-on-login-page-3f6957e0ed2e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126143318/https://medium.com/@yashsancheti24/account-takeover-on-login-page-3f6957e0ed2e
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1911 (id 1911)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account Takeover on login page

Hi,

I found this a long time ago but sharing now. Hope you enjoy it!

They were encrypting data in hashes to prevent this bug but it was still easy to bypass it.

**Same steps can be used for email.**

My account no. — **xyz**

Victim’s account no.- **pqr**

**Steps to reproduce the bug** :-

1.First get the encrypted code of the **victim’s number** (**pqr**).

2.Now go to reset password page, enter your **account no**.(**xyz**) and send OTP to it. Now enter the OTP sent to **xyz**

and capture the request.

3.Paste the victim’s phone no. encrypted code on request and check the response and manipulate it to success

and then forward again.

4.Enter the new password and again capture the request and enter encrypted code of **victim’s** phone no. (**pqr**)

5.This lead me access the victim’s account.

POC Video: [https://www.youtube.com/watch?v=3-Cw-Nw0SY8](https://www.youtube.com/watch?v=3-Cw-Nw0SY8)
