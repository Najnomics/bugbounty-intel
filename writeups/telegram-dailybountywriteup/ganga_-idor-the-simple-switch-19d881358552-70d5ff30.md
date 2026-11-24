# IDOR

- **Source URL:** https://medium.com/@ganga_/idor-the-simple-switch-19d881358552?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240304083901/https://medium.com/@ganga_/idor-the-simple-switch-19d881358552
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5362 (id 5362)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Greetings, fellow cybersecurity enthusiasts! Allow me to introduce myself: I’m Ganga Manivannan, a passionate security researcher. In this write-up, I’m excited to share with you an interesting discovery:

I quickly jump into the finding. Let’s start with the target; I can’t disclose the name of the target, so let’s call it app.redacted.com. Here, users can create accounts using either email/password or Google OAuth. I started by creating an account using the email/password method. Afterward, I navigated to the profile settings page.

There, I discovered an interesting feature: the ability to connect a Google account and subsequently enable or disable Google authentication.


Excited to delve deeper, I fired up the Burp Suite and began analyzing the requests. Using Burp Suite’s history feature, I meticulously examined each request.

I found an interesting endpoint while enabling and disabling Google authentication by clicking the *configure* option, where the user ID was present both in the URL and request body.

*You guessed right!!*

I quickly created another account (i.e., a victim account) and captured the ID. I attempted to replace the attacker’s ID with the victim’s, thinking that I could enable/disable my Google account in the victim’s account, effectively connecting my Google account to theirs. However, my efforts were unsuccessful, resulting in a ‘403 Forbidden’ response.

After some time, I thought, ‘Why not switch up the email ID?’ So, I modified the ‘id’ and ‘summary’ values to the victim’s email ID, and BOOM!! Now, I got the result.

However, after switching up the email ID and achieving the desired result, I needed to confirm the vulnerability of linking another user’s Google account to my own account. To do that, I made one change: I switched the request method from POST to GET. I received the response containing the victim’s email address.

Thank You :)

I hope you’ve learned something and enjoyed my write-up. If you have any questions about this finding or bug bounty, feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/ganga-manivannan-0546941a8) through direct message. I’m always here to help!
