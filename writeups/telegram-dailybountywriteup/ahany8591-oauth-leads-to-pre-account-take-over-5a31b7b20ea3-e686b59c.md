# OAuth leads to pre account take over

- **Source URL:** https://medium.com/@ahany8591/oauth-leads-to-pre-account-take-over-5a31b7b20ea3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142428/https://medium.com/@ahany8591/oauth-leads-to-pre-account-take-over-5a31b7b20ea3
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3937 (id 3937)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# OAuth leads to pre account take over

In this writup i will share with you how i could make use of OAuth Misconfiguration to takever an account:

A pre-account takeover occurs when an attacker creates a user account using one signup method and the victim creates another account using a different signup method using the same email address. Because the email addresses are the same, the application connects the two accounts. when the app is unable to validate email addresses.

## **POC:**

Lets say that there is an email has facebook account called example@email.com that belongs to victim

1-first i register as normal registeration with that {**example@email.com**} and give it password say {**123456**}

2-second i register via facebook feature with the same email {**example@email.com**}

3- when i register with facebook method it didn’t ask for password for the account

4-both methods redirect me to the same account and here it is,

5-when i log out and sign in again with the same password of first method {123456} it succeded!!

so i manage to create an account using only mail address and when the victim verifies the account i will be able to manage it

so briefly i can say i can pre account takeover if i register before the victim do if i have its email address only!!

Unfortunately, The program says its a Dublicate,

Always remember to keep trying untill you reach, **Happy Hacking**
