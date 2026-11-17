# From Subtle IDOR to Full Account Takeover (Including Admin Access)

- **Source URL:** https://medium.com/@amitdutta6026/from-subtle-idor-to-full-account-takeover-including-admin-access-43b468c5542b?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@amitdutta6026
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 12337)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Note :**The website name isn’t disclosed, and all user details are blurred in black-and-white images.

**Lets get started……..**

So few days back in an weekend I was having coffee and feeling bored , so I thought to hack something for fun (The website was into my bucket list ) and it turned into the discovery of a subtle yet critical security flaw in a website .

I registered a new account on the website and started to dig into it and I found nothing interesting into it and it was a quite small web application with limited scope so I thought to create another account to look for broken access control vulnerabilities.

This is the web application. It proudly displays “Secure Login” and “Protected.”

Jokes aside, here’s what I found.

During the new account registration process, I observed that immediately after signup the application triggers an endpoint such as:

[https://redacted/php?intr=SA8920980&msg=4&id=11380](https://redacted/php?intr=SA89209808&msg=4&id=1138020)71

Now , I changed the [id=11380](https://redacted/php?intr=SA89209808&msg=4&id=1138020)71 into [id=11380](https://redacted/php?intr=SA89209808&msg=4&id=1138020)72 .

And **Bingo**, I got another users username and password .

Now , lets try to login into this account

And I have successfully logged in into another users account and observe that I can access every private information of another user like **Name, Email , Phone number and even bank details**( I haven’t shown the bank details to maintain privacy).

Now , I targeted the Admin and thought to change the id into "id=1" in the same endpoint [https://redacted/php?intr=SA8920980&msg=4&id=1](https://redacted/php?intr=SA89209808&msg=4&id=1138020)and I easily got access into Admin’s credentials in a single shot .

That was easy ……………

Please follow for more security write-ups .
