# Account takeover without user interaction via the mail server

- **Source URL:** https://medium.com/@NiGHt.Hunter.101/account-takeover-without-user-interaction-via-the-mail-server-45d4f2e0eda7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221208082207/https://medium.com/@NiGHt.Hunter.101/account-takeover-without-user-interaction-via-the-mail-server-45d4f2e0eda7
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1034 (id 1034)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account takeover without user interaction via the mail server

Night Hunter is not a one-person night hunter is everyone who chose to hack for a reason, night hunters always thirsty for more and more, and as a night hunter, I will show you how I was able to hack and hunt anyone’s account.

I will mention our target as redacted.com and I will not write about the recon process cause many writeups are out there so no need to write again.

I was manually testing every single function and the reset password request got my attention cause it was the funniest request that I have ever seen

`{"mailID":"60334bab-d443-4681-0000-00000000000","to":["attacker@gmail.com"],"customData":{"email":"attacker@gmail.com","email_lang":"ar"}}`
- every message has a *mailID* and each time you request to reset your password a new mail ID will be generated
- the second parameter is the email that will receive the message
- the *customData* is some data that will be included in the message content

so if we can control who will receive the message that includes the reset password token we will be able to reset anyone’s password

and we can do that easily by just changing the second parameter to our email.

Steps to produce :

- Open the reset password page, type the victim’s email and press submit
- Intercept the request
- Change the email parameter to yours
- Check your inbox, click on the reset password link and you will be able to set a new password

in this way, I was able to take over anyone’s account by just knowing his email.

Now we can say that our hunt is done and we can survive for one more day!

contact: [nighthunter101@proton.me](mailto:nighthunter101@proton.me)

session id : 05412ea78f2ad19842cc41249e0cb8b4968a9a1e531205a79853ad1c5e234f7475
