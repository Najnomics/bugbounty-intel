# OAuth Misconfiguration Leads To Pre-Account Takeover(snapchat)

- **Source URL:** https://medium.com/@a7med.ctf/oauth-misconfiguration-leads-to-pre-account-takeover-snapchat-129b118661f6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250916165832/https://medium.com/@a7med.ctf/oauth-misconfiguration-leads-to-pre-account-takeover-snapchat-129b118661f6
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4459 (id 4459)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# OAuth Misconfiguration Leads To Pre-Account Takeover(snapchat)

Hi guys, my name is Ahmed Mahmoud. I am a bug hunter. I will share my latest finding, which is an OAuth Misconfiguration that Leads To Pre-Account Takeover. I will share two scenarios, one of which is in a domain belonging to Snapchat.

First What is OAuth?

OAuth is an open-standard authorization protocol or framework that provides applications the ability for “secure designated access.” For example, you can tell Facebook that it’s OK for ESPN.com to access your profile or post updates to your timeline without having to give ESPN your Facebook password. This minimizes risk in a major way: In the event ESPN suffers a breach, your Facebook password remains safe.

OAuth doesn’t share password data but instead uses authorization tokens to prove an identity between consumers and service providers. OAuth is an authentication protocol that allows you to approve one application interacting with another on your behalf without giving away your password.

So now let’s start. I found a domain belonging to Snapchat which has a login page for login and signup. On this page, you can login or signup with Google or GitHub.

How to test account take over ?

First method:

1-sign up with victim email with normal way email and password and logout

2-with same email go and sign up with google account

3-Now if it let you login with same account you did you have pre account take over

That what i founded in domain belong to snap chat but after make step one you need to verfiy email but when victim sign up with google it will him login to account and verfiy it

Second method:

1-sign up with google account and logout

2-Try sign up with same email

3-Now it will may be link you with exist accout so you will have account take over

Second scenario in privat program on bugcrowd i tried second method but i have two differents account with same email one (login with google account) second (login with username and password)but first method work again with me.

For questions:
