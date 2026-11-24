# Github Repository Exposed the Sensitive Data to Admin Account Takeover

- **Source URL:** https://medium.com/@bishnu.kumar200231/github-repository-exposed-the-sensitive-data-to-admin-account-takeover-5c9e0a6a37f1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251127071420/https://medium.com/@bishnu.kumar200231/github-repository-exposed-the-sensitive-data-to-admin-account-takeover-5c9e0a6a37f1
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2138 (id 2138)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Github Repository Exposed the Sensitive Data to Admin Account Takeover

**WhoAmI**: Penetration Tester, Bug Bounty Hunter, Security Consultant

Introduction:- I found the senstive data like admin id and password and takeover the account succesfully

Here how i did it: we know that github is huge space for programmer and developer so i decide to do github dorking here is command

target.com “client\_secret” or target.com password

after some time of research i have not find anything senstive but but but never ever give up in bug bounty so i try to

to find github repository of company and after some time research i found one repository which one contain a credentials 

So i jump into the credentilas repository and some code review i found the seceret which one id and password of admin

now time to validate the credentils but i was false so once again i have decided to review the code and i found the login link of amin page

booommmm i got redirected and successfully login the account and access the all customer data

**Reporting:**- i have reported on hackerone and after 1 days it was triggred by hackerone and they give me some bounty

**Conclusion**: Always do recon and try to find some senstive on github dorking and most important while doing dorking on github always try to understand the target

and try do max time mannual dorking just because automated tool missed lot’s of thing
