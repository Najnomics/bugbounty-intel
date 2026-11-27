# Power of CSRF

- **Source URL:** https://medium.com/@hillrane24/power-of-csrf-43b736c74280?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905162526/https://medium.com/@hillrane24/power-of-csrf-43b736c74280
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5836 (id 5836)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Power of CSRF

Hello People, My name is Nikhil Rane and I am a Bug bounty hunter from India. This is my second blog of my methodology and exploitations of vulnerabilities. This is bit unique way of bypassing the verification process of mobile number and email, So lets start.

I discovered a public program where there was a sign up page. It was just like a normal account creation process where i was asked to verify my mobile number as well as my email address (I did not verify my email). I tried some manipulation technique to bypass mobile verification process but i was not able to do it. So i created my account and went to edit profile page i tried some manipulating process still same.

To change email as well as mobile number verification is asked in the form of OTP, so my main focus was to bypass the mobile OTP as it is the primary source of authentication. I spent almost 30 to 45 minutes finding write up as well as some unique way to bypass verification — but i didn't found anything interesting.

So just for curiosity i intercepted the edit profile traffic just to look what i can do, but i did found something interesting.

I saw that i am getting phone number as well as email parameter in the intercepted traffic, I got confidence that i can find something interesting. I changed the mobile number in the request section and sent the request forward but nothing happened. So after analyzing the request i saw there is no CSRF protection, so i just generated the CSRF POC.

CSRF is an attack in which attacker capture the the action request like updating, deleting and changing of profile credentials or activity of the account followed by generating HTML code. Saving that request in the HTML file and sending it to victim. The victim click on the file unknowing executing the action request made by attacker. If the execution is successful the data or credentials will be changed of victims account. But here in my attacking scenario i did self attack on my own account, usually it is tested on the victim side. My moto was to bypass the verification so i executed this file on my own browser.

I changed the mobile number and email address to some other or say to victims phone and email, clicked on the option “test in browser” and Opened file on my own browser tab just to get the success message.

So, the thing is i am able to bypass the email as well as mobile verification as the main authentication was mobile OTP. So this was my unique finding of bypassing the authentication process and OTP verification which i did back in past. The mitigation was done by adding CSRF token and by encrypting the input field upon capturing the edit profile request .

Now the catch is i did not try to link it with account take over. As i was new to the Bug bounty hunting i was not knowing the concept of chaining the attacks. But still this was my best finding back then. I could have simply send CSRF file to victim followed by victim download and execute the file in the browser. Victims account credentials might get change which can lead to ATO(Account take over). Once the credentials are changed we can ask for forget password link or OTP which will be on our changed number or email. This is just a scenario, which i could have tested back.

I hope you enjoy reading, Peace out :)
