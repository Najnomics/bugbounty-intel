# Chaining low impact bugs leads to 0 click Mass ATO

- **Source URL:** https://medium.com/@haitamelkhorazmi/chaining-low-impact-bugs-leads-to-0-click-mass-ato-4e7016d22121?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142730/https://medium.com/@haitamelkhorazmi/chaining-low-impact-bugs-leads-to-0-click-mass-ato-4e7016d22121
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3790 (id 3790)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Chaining low impact bugs leads to 0 click Mass ATO

Bismillah Ar-rahman Ar-rahim

Hello everyone, I hope you’re doing well. This is my first writeup so if you don’t understand something, please let me know in order to fix it or improve it.

## Summary:

Today, i want to share with you an interesting finding and the lessons I learnt with : Chaining 3 bugs (1 medium + 2 none impact) leads to 0 click account takeover (high/critical).

For the web app, it’s a SaaS plateform for Web-hosting, you create an acccout and you buy domains to host your website.

We’ll simply call it **target.com**

So lets start:

### “Useless” IDOR:

The first bug is on the “Password change” feature : in order to change your password, you need the old and new password, and the URL was like this : **GET /api/v2/customers/change-password/”6\_digits\_id”.** This id was easy to brute-force since just the last 4 digits are variable, and the variation of ID is incremental ( x+1 ).

We can change other users’ passwords with this IDOR just by changing the ID to 6 random digits, but there is two problems : *1st one:* the authentication process needs email and password, so even if we change the password we don’t know the email of the victim, and he can easily reset his password. *the 2nd one :* we don’t know the “old” password in order to change it.

What’s the impact ? simple, it’s none. **BUT, I’ve written it down in my notes.**

### 2nd “useless” no rate-limit:

As I said, in order to change password, we need the old and new password, but I found out that there is no rate limit on this “change password” request. So you can send as many reqest as you want, you won’t be banned or blocked.

What’s the impact ? simple, it’s low or none. **BUT, I’ve written it down in my notes.**

### 3rd “game changing” IDOR:

It’s time for the main bug, I’ve found an 2nd IDOR that leaks other users’ PII including the most important thing which is **“Email”.** The URL was : **GET /api/orderbox/v2/reseller/customers/”6\_digits\_id”** and guess what ? It’s the same id in the 1st “useless” IDOR. So just by changing the id to a random id, I can have some customer’s informations including the email !

### The Ultimate Combo:

Let’s chain all this together :

- If we use the 3rd bug, we’ll have the victim’s email.
- Using the 1st bug, we can change the password for the same victim since it’s the same id.
- To bypass the “old” password problem, we will brute-force it using the 2nd bug (no rate limit on change password).

Chaining this bugs will lead to a 0 click Massive Accounts takeover.

## Lessons of the day:

- Never underestimate a bug, just write it down. maybe you’ll need it later
- Always try to chain bugs in order to escalate the impact.

I hope you’ve found this write-up useful and follow me on Twitter for more tips and write-ups !

[https://twitter.com/HaitamHayteex](https://twitter.com/HaitamHayteex)

Al Hamdoulillah
