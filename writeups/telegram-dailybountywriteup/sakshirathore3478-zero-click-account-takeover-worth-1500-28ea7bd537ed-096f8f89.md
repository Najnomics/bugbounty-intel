# Zero-click account takeover worth 1500€

- **Source URL:** https://medium.com/@sakshirathore3478/zero-click-account-takeover-worth-1500-28ea7bd537ed?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260227183716/https://medium.com/@sakshirathore3478/zero-click-account-takeover-worth-1500-28ea7bd537ed
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/12864 (id 12864)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Zero-click account takeover worth 1500€

Hello Everyone, This is the method and steps I followed to uncover a vulnerability that resulted in getting me a bounty of 1500 Euros.

Also, This program doesn’t have any Official Bug Bounty Policy but they do reward for critical issues.

Apologies for the bad English.

I figured out this vulnerability after watching this awesome video from 

**Magn4** which you can check out too.


So, I was hunting on a website which was related to some medical stuff like something related to things that is required for making medicines and all. I went through the normal registration process, could not find anything there other than some low issues.

Then I analyzed their login flow, but nothing much there. Everything was secure.

In there User profile section, the settings were you cannot change anything there after registration except the email. I tried changing the email and got a link on the new email.

I sent the email change request to repeater and analyzed it. The email was being sent in the Json body with new email, country and some other parameters. I tried playing with it but got nothing.

After it, I analyzed the cookie of the request as there were so many parameters in it so I can just get a bit better understanding of the request.

There I used the Burp extension named request minimizer to remove the unnecessary cookies.

At the end I got this request for a successful execution.

okay so events cid and uuid were changing based on the actions we were performing (as much as I figured) but here the server was actually considering the Email that was in cookies value. As much as it sounds weird to me and others, It was the case.

Now let’s take 3 accounts.

*Victim@gmail.com*

*Attacker1@gmail.com*

*Attacker2@gmail.com*

1. I initiated an email change request from Attacker1@gmail.com to Attacker2@gmail.com.
2. I captured the request and changed the email value in the cookie from Attacker1@gmail.com to victim@gmail.com.
3. I got a link on my Attacker2@gmail.com inbox. I approved the email change request and It successfully changed from victim@gmail.com to Attacker2@gmail.com.
4. Now to login into the Victim account I simply have to request a password reset link which will obviously come to Attacker2@gmail.com from where I can just change the password and log into the victim’s account.

I reported it to them and they fixed it quickly and also awarded me with a 1500 Euro Bounty.

*(I have only the message on my mobile so bear with it but yeah these are the credentials for the Bounty)*

So that’s all I hope you like the writeup. Once again apologies for my bad English. See you all later. BBye!!!
