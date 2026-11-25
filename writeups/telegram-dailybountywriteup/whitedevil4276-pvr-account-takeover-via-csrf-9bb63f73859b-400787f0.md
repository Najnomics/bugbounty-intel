# PVR Account Takeover via CSRF

- **Source URL:** https://medium.com/@whitedevil4276/pvr-account-takeover-via-csrf-9bb63f73859b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221211061244/https://medium.com/@whitedevil4276/pvr-account-takeover-via-csrf-9bb63f73859b?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/51 (id 51)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# PVR Account Takeover via CSRF

Hi all

I found a responsible disclosure program through google dork which is insecure from the CSRF attack, there was no CSRF token exist while updating the record.

For the individuals who don’t know about CSRF, it is a web application attack where an attacker stunts or powers the client to present his malicious request which the client isn’t proposed.

In a straightforward manner, if a server isn’t approving a request sent from the client, the attacker can create a malicious request and stunt the client to tap on it which will result in a modification in users’ accounts like password or email.

Let start with POC

- First, create an account as an attacker and fill all the form check your info in the Account Detail.

- Change the email and capture the request, then created a CSRF Exploit.

The CSRF Exploit looks like as given below. I have replaced the email value to anyemail@\*\*\*\*\*\*\*\*.com and submitted a request the victim’s account.

In the following stage, I just forward the above request and vola! My exploit worked, so by this exploit, I changed my email to the victim’s email and by using the forgot password method to retrieve the password reset link to my email and I have full control over the victim’s account.

Hope you find this useful, I tried my best to explain. Please share so that others can learn from it.

Thank You.
