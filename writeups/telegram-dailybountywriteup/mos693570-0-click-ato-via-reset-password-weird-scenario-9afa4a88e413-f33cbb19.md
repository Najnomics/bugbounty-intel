# 0-Click ATO Via reset password weird scenario

- **Source URL:** https://medium.com/@mos693570/0-click-ato-via-reset-password-weird-scenario-9afa4a88e413?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241107174356/https://medium.com/@mos693570/0-click-ato-via-reset-password-weird-scenario-9afa4a88e413
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7720 (id 7720)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Introduction:

*EL\_Mo is saying hey again, Hello everyone! I’m Mo Salah, a beginner bug hunter with a passion for learning and exploring cybersecurity. Today, I’ll be discussing a recent discovery I made — a bug involving Zero Click Account Takeover, Let’s dive into the details!*

# Let’s get started:

*Let’s assume our target gonna call it “target.com”, I decided to focus on the main app. I opened my burp and started to interact with the app by doing the normal actions like creating something or deleting something to save the API requests to check it after that for any idor or any access control bugs. started to check for any idor but unfortunately, it was secure. The last thing I was checking was the reset password page so let’s dig into it*

*i went to the reset password page and tried to enter my email address and reset it until here there is no problem but when i request reset password link and open it, exist parameter called email in url, contain the email that requested the reset link.*

**Link: https://target.com/forget-password/token?email=attacker@gmail.com**


*so as everyone i change the value it to another email but Unfortunately the password not able to update and show error called “this token is not associated with this email , until here there is no problem I try a lot of known ways about reset password bugs but not nothing new.*

**Link: https://target.com/forget-password/token?email=victim@gmail.com**


*buuuuuuut i got idea* after four hours, so let’s explain it.

*I requested a password reset link for the victim's account and back again to request reset password link for my email. I received the reset link for my email and, before updating the password, changed the email to the victim's. To my surprise, the password updated successfully. I then went to the login page, entered the victim's email and new password, and successfully logged in.*

*So to make this scenario work, you must request a reset link for the victim beforehand.*

**let’s reproduce the bug:**


*Attacker account: attacker@acroins.com*

*Victim account: victim@gmail.com*

*1- Go to reset password function and write the victim(victim@gmail.com) email and request reset password link*

*2- Return to the reset password function, enter your email(attacker@acroins.com), and request a reset password link.*

*3-You will receive a reset link in your Gmail; click on it.*

*4-Change the email parameter in the URL to the victim’s email.*

*5- Change the password and confirm the update was successful.*

*6- Log in using the victim’s email and a new password.*

*let’s talk about this weird behavior :*


*The developer make mistake in token validation, he dos not check the token is valid for this user or not, i mean when attacker can request reset password link by victim email , and request reset link again by own email to take valid token and use it to change the password for victim*

*and so on the bug accepted and resolved in three days*

❤الحمد الله❤ i received a nice bounty

**Please let me know if there is anything more I can help with**

Follow me


*Thanks for reading and don’t forget to pray for Palestine and always free Palestine*
