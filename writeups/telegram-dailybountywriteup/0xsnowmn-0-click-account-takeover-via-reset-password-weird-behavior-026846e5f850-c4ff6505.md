# 0 Click Account Takeover Via reset password weird behavior

- **Source URL:** https://medium.com/@0xSnowmn/0-click-account-takeover-via-reset-password-weird-behavior-026846e5f850?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240603163835/https://medium.com/@0xSnowmn/0-click-account-takeover-via-reset-password-weird-behavior-026846e5f850
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5508 (id 5508)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
اللهم صلي على محمد

Snowman is Saying hi again with a new (weird) bug and a weird support team coz I had reported this bug in March 2023 because of the delay of the team I forgot about this bug totally, one week ago I was surprised when I found they responded about 3 months ago December 2023!

Anyway, let’s discuss how I found this bug

let’s assume our target gonna call it “target.com”, after the subdomain enum I decided to focus on the main app.

I opened my burp and started to interact with the app by doing the normal actions like creating something or deleting something to save the API requests to check it after that for any idor or any access control bugs.

started to check for any idor but unfortunately, it was secure.

I took a break and after I came back, I tried to check some data I got from my scripts like subdomains and screenshots but nothing interesting

I tried to read javascript files to check for any secrets or read the API requests but found nothing :(

The last thing I was checking was the reset password page so let’s dig into it i went to the reset password page and tried to enter my email address and reset it until here there is no problem

usually, I open the console and the local storage and cookie to check the data saved into it so I opened it and found some field called user\_email

and the value of it was my email I reset the password for it so I tried to change it to check if the value of the email in the page was taken from this local storage field and when I changed it changed in the page.

so I thought it might be trying to inject anything but after one minute I told myself even if I injected anything it’s self so I clicked on the button to resend the email with dead hope but guess what? I got the reset link for the victim mail to the new mail I put in the local storage!!!!!!!!!!!!!!!

So let’s reproduce the bug:

1. go to the reset password link and put the victim's mail
2. after the first link goes to the victim's mail open the console and change the user\_email to the attacker's mail
3. reload and resend the mail
4. open the attacker's mail and use the link to reset the victim's password

So let’s talk about this weird behavior :

the app when you make the reset password action returns the user data in some field called token in the local storage so when the user hits the resend email it should send the email to the email stored in that token but what the app does is get the email value from the user\_email and send it to the user id stored in the token.

Thanks for reading and don’t forget to pray for Palestine and always free Palestine.

Follow me on Twitter
