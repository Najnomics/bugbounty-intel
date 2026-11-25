# IDOR Chained To Missing Ratelimiting Leaded To ATO of Any User Account

- **Source URL:** https://d0natel00.medium.com/idor-chained-to-missing-ratelimiting-leaded-to-ato-of-any-user-account-338d9f22aed2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260519130951/https://d0natel00.medium.com/idor-chained-to-missing-ratelimiting-leaded-to-ato-of-any-user-account-338d9f22aed2?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13399 (id 13399)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR Chained To Missing Ratelimiting Leaded To ATO of Any User Account

Hello Friend, When I Was Bored and Doing Testing on One of the VDP Programs Which I Recommend This To You If You Want To Practice or Bored Like Me or Gain Reputation ! , I Found an **IDOR on Changing Password Function Which the APP Let the Use Try a Lot of Passwords on Current Password in Case He Forgot it So They Leaved This Without Ratelimiting Enforced on It (By Design They Trusted That this Only Happens on The Legit User Session). That is Good Until Now, Except if This Was Chained To IDOR That Can make The Attacker Able To Bruteforce Another User’s Password Without Getting Blocked and Change It .**

**Normal Change Password** POST Request is Like That :

```
{
  "currentCredential": "<LEGIT-OWNER-PASSWORD>",
  "credential": "<CHANGEPASSWORD>",
  "confirmCredential": "<CHANGEPASSWORD-CONF>",
  "username": "",
  "emailAddress": "<LEGIT-OWNER-EMAIL>"
}
```
Tip: When the Change Password Function Doesn’t Require the User to Write His Current Password That Can Lead To CSRF Attacks


**With Unlimited Attempts When He Trying To Guess (We Will Bruteforce) The Current Password Credential (By Design), Which The Developer Trusted That The User Only Can Change His Own Account Password . But, I Just Spoofed the Email and username And Wrote the True Password of The Victim Test Account . Then, I Tried to Login With the Old Credential and It Didn’t Pass Me Until I Wrote The New Credential (Password) Which We Used in the IDOR !**

```
{
  "currentCredential": "<BRUTE>",
  "credential": "<CHANGEPASSWORD>",
  "confirmCredential": "<CHANGEPASSWORD-CONF>",
  "username": "<SPOOFED-USERNAME-TARGET>",
  "emailAddress": "<SPOOFED-EMAIL-TARGET>"
}
```
I Tried to Simulate the Attack and Put a Test Password Like `Password123` For Example, In Real Situation Attacks the Attacker Have Unlimited Attempts So He Can Bruteforce As Much as He Want. I Just Bruteforced 500 Passwords For Confirmation on the Bug To The Triage

Without This IDOR (Instant Lockout After \~10–30 Attempts) :

### Combined To Email and Userenumeration :

**That Make the Attacker Able To Validate That There is Existing User and Email . That’s Useful Like in this App Case Because If You Changed the Email To None Existing Address It will Respond Like Just the Current Password is Wrong. So, When You Report Bugs From that Stuff It’s Recommended To Include UserEnumeration Vulnerabilities To Make the Report Even More Powerful**

You Can Spot User enumeration :

- Registration
- Change Email
- Login
- Send Messages (If Found Such a Feature)
- Password Reset/Forgot Functions
- Timing (Advanced)
- Api ID Endpoints (Which Are Suspicious For IDORS)
- Public Profiles (Sometimes)
- Status Codes

Another Techniques …

After This, I Reported the Bug Instantly To The Program !

Thanks, To The Team They Responded Very Quickly After I Reported in About \~1 Minutes !

I Hope You Got any Useful Idea From this Short Write-up .

Goodbye .
