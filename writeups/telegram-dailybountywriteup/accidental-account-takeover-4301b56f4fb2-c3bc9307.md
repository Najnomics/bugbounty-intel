# Accidental Account takeover

- **Source URL:** https://infosecwriteups.com/accidental-account-takeover-4301b56f4fb2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221013050727/https://infosecwriteups.com/accidental-account-takeover-4301b56f4fb2
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/439 (id 439)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Accidental Account takeover

Hello Security Community,

Let’s start the writeup. I was testing a team management App. There are multiple roles and permission level functions. At the sign page there is an email address and password based authentication system. So i sign up with my Admin , manager and readonly accounts using firefox container.

Email verification with token look like this.

I copied this url from my mail box in chrome. I saw this token is uuid based and unguessable. I moved forward in the dashboard to check other functions. while testing the app. I tried to copy a link but somehow it didn’t work. I opened a private window and pasted that link but that copied link didn’t work so my clipboard already has an email verification link. i was in hurry i didn’t saw what i pasted and i clicked searched i saw dashboard of target app. I thought that token is for one time use but i am wrong. Then i searched that token in burp search function i got to know that its userID of user.

So i Started looking other users userID in responses of api. its team based app there is Users page i captured that request and in response i got userId of every user which are listed there.

i got access of every employee which are in my team.

To increase the severity i started looking this userID in other part of application. then i found out feedback page where multiple users and company employee commenting on each other feedback. GOLDMINE.

i takeover employee account for poc.

Goodbye until next time!
