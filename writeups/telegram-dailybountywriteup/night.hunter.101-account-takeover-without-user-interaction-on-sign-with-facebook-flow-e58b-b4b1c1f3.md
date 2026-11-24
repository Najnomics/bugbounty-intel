# Account takeover without user interaction on sign with Facebook flow

- **Source URL:** https://medium.com/@NiGHt.Hunter.101/account-takeover-without-user-interaction-on-sign-with-facebook-flow-e58bf47cb2b7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221209101711/https://medium.com/@NiGHt.Hunter.101/account-takeover-without-user-interaction-on-sign-with-facebook-flow-e58bf47cb2b7
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1021 (id 1021)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account takeover without user interaction on sign with Facebook flow

Night Hunter is not a one-person night hunter is everyone who chose to hack for a reason, night hunters always thirsty for more and more, and as a night hunter, I will show you how I was able to hack and hunt anyone’s account.

I will mention our target as redacted.com and I will not write about the recon process cause many writeups are out there so no need to write again.

most of the hackers just neglect the Facebook and google buttons while testing, but on this site, I was manually testing every single function.

at the first, I fired up burp suite, clicked on sign-in with Facebook, kept my eye on all the requests that were sent from my browser to the server, and as on I found that the developer did a very bad mistake

My information was sent in this request email, profile picture, and name so before reading the response I knew it was a bug cause they will need to validate one of these fields to let me in.

yeah, it’s me of course replacing the email parameter to my second account email.

as you can see in the response the account name, id, and email were changed from mine to the victim's, and the cookies were leaked in the response so now I can use the cookie to log into the victim account and I will be able to take over anyone’s account by just knowing his email.

Now we can say that our hunt is done and we can survive for one more day!

contact: [nighthunter101@proton.me](mailto:nighthunter101@proton.me)

session id : 05412ea78f2ad19842cc41249e0cb8b4968a9a1e531205a79853ad1c5e234f7475
