# Account Takeover via password reset functionality.

- **Source URL:** https://medium.com/@genius0x1/account-takeover-via-password-reset-functionality-8d4b12c05a2a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230626195605/https://medium.com/@genius0x1/account-takeover-via-password-reset-functionality-8d4b12c05a2a
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3000 (id 3000)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hey hackers, I hope you are doing well.

I am Ahmed AbdElsalam and this is a new write up

i will take about IDOR leads to account takeover

**Frst we want to know what is insecure Direct Object References (IDOR) ?**

This is a type of access control vulnerability that arises when an application uses user-supplied input to access objects directly without any filters.

**and What is an account takeover vulnerability?**

This vulnerability allows the attacker to gain unauthorized and full access to the victim’s account by exploiting the authentication flaw in the application.

ok lets start

I tried to reset my password , so i clicked on **Forget Your Password ?**

then i received a mail contains a link to reset the password.

i opened the link and found that i must write a new password and new password confirm so i wrote them and intercepted the request with burp suite

i noticed that user id is included in the request so i tried to manipulate this id

i have already another account so i get this account id and put this id in the request and i found this

response is ok, so i went to check if The password of the other account changed successfully

and **YES** I found that the password changed successfully so i can get access to any account with its id only.

thanks for your time.
