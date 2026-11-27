# 2500$ From Login Bypassed & MFA Using a Race Condition + JWT Leak

- **Source URL:** https://medium.com/@syedshorox27/25000-from-login-bypassed-mfa-using-a-race-condition-jwt-leak-6139fcc22573?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@syedshorox27
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 10230)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How I Bypassed Login & MFA Using a Race Condition + JWT Leak

*What happens when you race 50+ login requests at once? Sometimes, magic.*

Hey hackers 👋 — this post is a fun deep dive into a critical authentication vulnerability I discovered during a recent security test. It combines one of my favorite web bugs (race condition) with a juicy JWT leak and ends in full account takeover — even with MFA enabled. Yep. Let’s get into it.

### 🧪 The Setup: Good Login Security (At First Glance)

So I was testing this app’s login page. Pretty standard stuff: enter your email and password, and if you’re lucky (and legit), it shoots back a JWT and asks for a 6-digit OTP (Multi-Factor Authentication). Simple, right?

To their credit, the devs had implemented account lockout — after 5–6 incorrect login attempts, the account would lock for 10 minutes. Nice!

But of course… I had other plans. 😈

### 🎯 Target: Beat the Lockout With Speed (Race Condition)

I figured if I could send multiple login attempts simultaneously, I might be able to squeeze a correct password in before the lockout logic kicks in.

### So I did this:

- Created a list of password attempts (including the correct one 😉)
- Loaded up **50+ requests** in **Burp Repeater**
- Launched them all at once like a packet flood

And guess what?

*💥* ***BOOM*** *— The server sent back a* ***valid JWT****, even though it should’ve locked me out.*

So the lockout check wasn’t atomic. The race was won by the correct password before the server tallied up the failures.

### 🔓 The Surprise: JWT Had a Hidden Auth Code 👀

Now here’s where it gets spicy.

The JWT looked something like this:

```
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "scope":"read",
  "token_type":"AuthCode",
  "expires_in":900
}
```
Wait… what’s authCode? 🤔

After decoding the JWT, I saw what the authCode is and wondered why it’s included there.

So I thought:

*What if I submit* ***any random OTP*** *with this valid JWT?*

I tried it… and…

*✅* ***It worked.*** *I was logged in.*

OTP **bypassed |** MFA **defeated |** Account **compromised**.

### 💡 Why This Happens

- Login and lockout logic wasn’t atomic (race won by correct password)
- JWT was issued **before** verifying OTP
- OTP validation was too trusting — the authCode leaked in JWT gave away the answer

### 🔥 The Impact

- Full login and MFA bypass
- No CAPTCHA or throttling to stop race
- Accounts **without MFA enabled** would be 100% compromised
- Even MFA-protected accounts could be broken into by abusing the leaked authCode

### ✅ Final Thoughts

This was one of those bugs that just *shouldn’t happen*. But it does — and when it does, it’s awesome (and terrifying).

Security isn’t just about blocking bad input — it’s also about handling timing, trust, and sequencing properly.

I responsibly reported the bug, got it patched, and now I’m sharing it with you.

Stay curious, stay ethical, and keep breaking things (safely).

Happy hacking! 🐱💻

#bugbounty #websecurity #jwt #racecondition #mfa #infosec #cybersecurity #redteam
