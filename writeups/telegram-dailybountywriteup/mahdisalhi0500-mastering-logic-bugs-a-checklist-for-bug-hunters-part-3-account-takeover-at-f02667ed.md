# Mastering Logic Bugs

- **Source URL:** https://medium.com/@mahdisalhi0500/mastering-logic-bugs-a-checklist-for-bug-hunters-part-3-account-takeover-ato-7af98ce87aa3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250405094946/https://medium.com/@mahdisalhi0500/mastering-logic-bugs-a-checklist-for-bug-hunters-part-3-account-takeover-ato-7af98ce87aa3
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9266 (id 9266)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Mastering Logic Bugs: A Checklist for Bug Hunters — Part 3: Account Takeover (ATO 💨💨)**

إِنَّ اللَّهَ وَمَلائِكَتَهُ يُصَلُّونَ عَلَى النَّبِيِّ يَا أَيُّهَا الَّذِينَ آمَنُوا صَلُّوا عَلَيْهِ وَسَلِّمُوا تَسْلِيمًا

## Salam Alaikum, guys! I’m so happy for the interaction. Thank you so much! you make my days allhmdlilih ❤

## Today i we gone dive into Account Takeover If you someone new in the palylist here the main ideas I’ll share some great tips for ATO. I’ve learned from other hunters and will provide the full resources for these tips…

# Let’s gooooooooooooooo…! 💢🔥

# **Account Takeover (ATO)**

- If the password reset request normally looks like this

“email”: “victim@gmail.com”)

“email”: \[“victim@gmail.com”, “your@gmail.com”\] \<- **list**

If the system sends a reset link to both emails, you might be able to take over the victim’s account by receiving their password reset link.

- Sign up with Oauth using Facebook and don’t share your email address with the website (with edit Access button on permission page) and if app ask you form email add victem mail \[[👊](https://hacktivator.medium.com/bugbounty-account-takeover-via-facebook-oauth-67b454696c0f)\]
- Make 2 Accounts Same in everything \[username and another things\] but with Different email ID >> [ATO😮](https://shahjerry33.medium.com/duplicate-registration-the-twinning-twins-883dfee59eaf)
- to bypass the verification section try to add company’s domain, like CaptinSharky[@company](http://twitter.com/company) \[like this[❤](</@0d-amr/account-takeover-how-i-gained-access-to-any-user-account-through-a-simple-registration-flaw-96f9f6bdc0ae)>)\]
- When I encountered the **“email already exists” error** while updating my email, I bypassed it by adding `%20` at the end (e.g., `your@email.com%20`) or changing the case (e.g., `your@email.Com`)…
- used X-Forwarded-Host to change the submits token to malicious domain \[[for example🙂](/bugbountywriteup/password-reset-token-leak-via-x-forwarded-host-4ed3e33dca31)\]
- test for “host” header if able for removing is able for ATO but if Host header will not work if it’s not ending with “ \[login.company.com\]([http://login.company.com/](http://login.company.com/))” try to add Host :([http://login.company.com.burpcollaboratorurl.com/](http://login.redacted.com.burpcollaboratorurl.com/)) [😮😮](/@deepanshudev369/interesting-story-of-an-account-takeover-vulnerability-140a45a058a3)
- Always test email verification links by clicking them in a different user’s session to check for improper session validation! \[[🥱](https://akashhamal0x01.medium.com/watch-out-the-links-account-takeover-32b9315390a7)\]
- HTML injection is very good for testing in \[[register pages🛠](/@mohamed.yasser442200/email-html-injection-with-a-simple-tip-aeab346fbefc)\]
- site:figma.com”[http://slack.com/invite](http://slack.com/invite)" OR “[http://slack.com/join](http://slack.com/join)" \<- open this for urlscan.io site can sometime get invtion link \[[😘](https://x.com/GodfatherOrwa/status/1879151844724806131)\]
- “CallBackUrl Parameters” you can face this param in diff funcs, but this is really impactful specially in the takeover scenarios By replacing host with malicious one it replies an err msg! The Q here, how developer checks for the host? \[[😍](https://x.com/SirBagoza/status/1872779097241518215)\]
- if a found Call backURLS ( ) but if when i change got 400
\_Here aresome of the payloads that i tried\_
but always try null byte character %00 in unicode is \u0000 \[[😜](/@0xold/null-byte-on-steroids-23f8104a25ec)\]

# OTP BYPASS

- Try to response manipulation with OTP\[…[💢](/@b.jaga17122001/otp-bypass-leads-to-full-account-takeover-ed90d062f758)\]
- opened the developer’s option and checked the storage mechanism for parameter like \*\*is\_otp\_enabled\*\* and manipulation \[[🏌️♂️](/@cyb3rmind/3-bug-bounty-series-otp-verification-bypass-468526b76720)\]
- in OTP Code try guest the fixed verification ( 111111 or 000000 ) … \[For example\]([😮😮😮](https://hackerone.com/reports/2588329)), in development, you might set a fixed OTP of \`123456\`, ask chat-gpt or manual guest
- leaked in response
- old OTP is still valid
- Integrity Issues -> use someones else OTP to open your account

# Coming soon inshallah :

🎥 **New Video Coming Soon, Inshallah!**

I’m working on a new video where I’ll explain a powerful technique to help you find bugs more easily and make your hunting process smoother.

📌 **Video Title:** Mastering Match and Replace in Burp Suite: A Step-by-Step Guide

If you’re interested in seeing new PoCs, bug bounty content, and videos, feel free to join my Telegram channel here:

👉 [https://t.me/CaptinSharky01](https://t.me/CaptinSharky01)

👉[https://x.com/SalhiMahdi72759](https://x.com/SalhiMahdi72759)

**Improper Access Control — Generic**

**mass assignment**

**OAuth Secret**

**tips form bug hunters**

**JavaScript Analysis**
