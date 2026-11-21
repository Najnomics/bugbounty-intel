# From Pre-Account Takeover to Full Account Takeover using Google OAuth

- **Source URL:** https://medium.com/@sudo_a7med/from-pre-account-takeover-to-full-account-takeover-using-google-oauth-38b42268ce31?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250823233745/https://medium.com/@sudo_a7med/from-pre-account-takeover-to-full-account-takeover-using-google-oauth-38b42268ce31
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10500 (id 10500)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From Pre-Account Takeover to Full Account Takeover using Google OAuth

“بِسْمِ اللَّهِ، وَالْحَمْدُ لِلَّهِ، وَالصَّلَاةُ وَالسَّلَامُ عَلَى رَسُولِ اللَّهِ، اللَّهُمَّ عَلِّمْنَا مَا يَنْفَعُنَا، وَانْفَعْنَا بِمَا عَلَّمْتَنَا، وَزِدْنَا عِلْمًا”

اللهم انصرنا إخواننا المستضعفين في فلسطين وفي كل مكان

Hello Hackers,

Ahmed here again. Luckily, it hasn’t been too long since we last met. Today I’ve got two vulnerabilities to share — though, according to Bugcrowd’s triage, they were “the same thing.” Let’s not waste time and dive right into the scenarios.

## **First Scenario**

When I first created an account on the program, I noticed there was no email verification. The account was created instantly, and I was logged in right away. I took note of it and thought, *I’ll check it out later.*

After two days of hunting on the program without much luck, I revisited the login function. This time, I saw I could log in via the **Google OAuth**, which would automatically create an account and send a password setup link to the registered email.

I started thinking *What if I signed up with the victim’s email, and then later the victim signed up via Google OAuth? Would my session still be active?*

**Time to test**

I registered an account with the victim’s email, filled in the required details (name, password, etc.), and logged in.

Then, from another browser, I clicked ***Sign in with Google OAuth*** using the victim’s actual Google account. This redirected me to the account I had initially created in step one, but it also sent a password setup link to the victim’s email. I set a new password for the account.

But when i open the first browser i still login the account!

I assumed that once my session expired, I’d lose access — especially since changing the password would require knowing the current one. I tried the password I originally set but got incorrect password. After several attempts, I realized I couldn’t create a backdoor to login the account again , so I wrote up the report and sent it to Bugcrowd.

But unfortunately, it was marked as a duplicate

## Second Scenario

A few days later, I was back to studying when I came across a new scenario that I could test on this target. Since I always keep a TXT file with all the accounts I create on each target — in case I return to hunt on the same target later

When I tried logging in to one of these accounts, the password was incorrect. No problem — maybe I changed it while hunting and forgot to update the file. I quickly logged in via Google OAuth, and it worked.

Then, using another browser, I logged in with **a completely different Google account** and to my surprise, **I was logged into the same account!**

Thinking I may have accidentally clicked the same Google account, I logged out and retried but no, even with a different Google email, it still went into the same account.

**My adrenaline started rushing, and I thought: *it looks like we have a vulnerability here* how was the same account linked to two different Google OAuth accounts?so i start reviewing my past test cases**

After reviewing my past test cases for over an hour, I figured it out:

1- Log in with your own Google account

2- Change the account’s email to the victim’s email (the victim hasn’t created an account yet).

3- When the victim later signs up via Google OAuth, he will be redirected to the account I created and changed the email for to the victim’s email.

4- The victim sets their own password from the link sent to them.

After that, I tried logging into the site using the same Google OAuth account I had originally used to create the account before changing it to the victim’s email

**And to my surprise**, it logged me into the victim’s account even after the password had been changed!

*Now, I could still log in using my original Google account — and it would take me straight into the victim’s account. I had a persistent backdoor with full control.*

I wrote up the report and submitted it to Bugcrowd

After a few hours, I got this

So, are the two vulnerabilities the same?**Absolutely not.**

This was exactly what I tried explaining to Bugcrowd’s triage but here’s what they told me:

Alhamdulillah anyway.

That’s all for today. Hopefully, next time I’ll be back with a write-up about an accepted vulnerability (Insha’Allah).

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — - — — —

Thanks for reading. I hope this helped or inspired you in some way.

Until next time — happy hacking!

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — - — — — 

You can follow my journey to my first bounty on X(Twitter), where I post daily updates: [https://x.com/sudo\_a7med](https://x.com/sudo_a7med) .
