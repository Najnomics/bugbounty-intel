# IDOR leads to Account Takeover with JWT Week Screet

- **Source URL:** https://aryasec.medium.com/idor-leads-to-account-takeover-with-jwt-week-screet-3a6395973b27?source=rss------bug_bounty-5
- **Fetched from:** https://aryasec.medium.com/feed
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 4177)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello everyone, introducing my name Tengku Arya Saputra (Follow my [Linkedin](https://www.linkedin.com/in/tengku-arya-saputra-3b5031224/)) on this occasion I will tell you how I found a security hole with a very critical vulnerability level, initially I found IDOR but I escalated more and got an account takeover vulnerability.

At first I tried to register an account, and log in to the application, at first I didn’t think about trying to analyze the token, and continued looking for other vulnerabilities, after 2 days I tried to analyze the system it turned out that here I tried the jwt token which made me interested in trying to membrutefoce screet whether this is default or not

And here I can see that the jwt token is stored in the cookie, and you can see that the response shows the profile of the user, if I manage to find the screet of jwt I can do IDOR, how can I do it? I visit [jwt.io](https://jwt.io/) to try to decrypt the token.

You can see that when it is decrypted I get data in the form of json, where there is a user\_id, if the screet is successfully penetrated I can change the user\_id to someone else’s user\_id.

You can see that the signature is invalid, and in the red box there is a screet that I haven’t filled in.

how can I find out the screet ? I use john the ripper tools

Initially I created a jwt file, where the contents of the file are the tokens that you have copied

And bingo! I got what I was looking for, which is a screet that this app sets by default for its token screet, let’s continue!

I can see that the signature changed to valid which means I am successful and free to change the user\_id as I please…

let’s try to put the token on burpsuite

I changed the user\_id from **1368129** to **1368128**.

bingo! I got the IDOR vulnerability via JWT Week Screet!

and how can I takeover the account? Here I remember that the login application only uses their mobile number and pin, I can use IDOR to take the victim’s mobile number.

and I went straight to the login page

I immediately entered the victim’s cell phone number

How can I find out the pin? Here I have a problem with the pin number, but I see an anomaly that when I do forget the pin. I get a paramater that makes me interested in changing it, see below.

in the picture above I am suspicious of the paramater because logically the otp code will be sent based on what the user enters in the username, but here the server provides a POST request on the server that can be edited by anyone, here I am trying to change the victim’s number to mine.

and bingo! I get the otp code, just change the cellphone number using the paramater available, then I will enter the otp code into the account.

and it worked!!! I was directed to enter a new PIN! …

I managed to enter the victim’s account by trying to takeover the account.

**Timeline**

*Report —* October *15, 2023*

*Change To Triaged —* October 17*, 2023*

*Respond Team —* October 18*, 2023*

*Reward Bounty via Mobile Banking $$ — 19* October*, 2023*

*Resolved — 19* October*, 2023*
