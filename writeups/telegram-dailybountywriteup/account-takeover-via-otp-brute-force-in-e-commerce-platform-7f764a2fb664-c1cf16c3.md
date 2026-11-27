# Account Takeover via OTP Brute Force in E-commerce Platform .

- **Source URL:** https://waleedosamaeg.medium.com/account-takeover-via-otp-brute-force-in-e-commerce-platform-7f764a2fb664?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905103642/https://waleedosamaeg.medium.com/account-takeover-via-otp-brute-force-in-e-commerce-platform-7f764a2fb664
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10114 (id 10114)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account Takeover via OTP Brute Force in E-commerce Platform .

## ⚡ Quick Overview

Here’s a quick breakdown of what went down:

- 🔍 **Target:** E-commerce website with OTP-based password reset
- 🔐 **Vulnerability:** weak protection on OTP verification endpoint ( rate limit via ip blocking, no lockout, no CAPTCHA)
- 🛠️ **Attack Method:** Bruteforced the 4-digit OTP using python Script
- 💥 **Impact:** Full account takeover without needing the victim’s password
- 🧯 **Fix Suggestions:** Implement rate limiting, add CAPTCHA, use time-based OTPs with session binding

In short:

The site trusted the OTP too much…

And I was like: **“Challenge accepted.”** 😈

## Introduction

**Hello again, my hacker friends 👾**

Back at it with a brand new hacking adventure!

This time, I stumbled upon a juicy vulnerability in an e-commerce website — and things got *real* interesting 😏

In this writeup, I’ll walk you through how I **bypassed the rate limiting mechanism**, **brute-forced the OTP** used in the *reset password* function, and eventually pulled off a full **account takeover** like it was nothing.

Grab your Burp and your popcorn — let’s dive in!

While testing a popular e-commerce website for one of the biggest pharmacy chains in my country 💊, I came across the classic **“Forgot Password”** function.

Here’s how it worked:

1. You enter a phone number 📱
2. The backend checks if it exists in the database
3. If it does, an OTP gets sent via SMS 🔐

Naturally, I thought:

**“Hmm… what if I just guess the OTP?”** 👀

So I gave it a shot — started brute-forcing some random 4-digit codes.

But after just 10 wrong attempts, **boom! My IP got banned… but only for a short nap 💤**

That’s when I knew:

**“We’re close. It’s weak, but not impossible.”**

After a bit of trial and error (and a whole lot of 403s 😅), I started noticing a pattern…

🔁 The backend was allowing **only 10 OTP attempts per IP**,

⏲️ Then it would **block the IP for 30 seconds**,

💣 And if you exceeded **5000 total requests**, you’d get a **permanent ban** (RIP to my old IP).

While analyzing the requests (check the screenshot below 📸), I noticed something interesting — 

The OTP API endpoint had **zero protection**:

- No CAPTCHA
- No CSRF tokens
- Just a wide-open gate waiting for someone to knock (or kick it down 🚪)

So I had an idea 💡

“What if the frontend/load balancer uses headers like `X-Forwarded-For` or `X-IP-Host` to detect my IP?"

```
X-Forwarded-For: 1.1.1.1 
X-IP-Host: 1.1.1.1 
X-Real-IP: 1.1.1.1
```
…but sadly, **none of them worked** 💔

That’s when it hit me — the server was getting my real IP using good old:

`$_SERVER['REMOTE_ADDR']`
In short:

**They weren’t reading headers. They were reading reality.** 😅

After a bit of digging and some good ol’ hacker instinct 🕵️♂️, I finally found a way around the IP blocking system…

**Enter: the Tor network.** 🧅✨

Instead of sending requests from my real IP, I started routing them through Tor — which basically gave me a **fresh new IP** every time I needed one.

Here’s the idea:

1. Send OTP brute-force attempts through Tor
2. When the server responds with something like:

`{"message" :"...." ,"code" : "429"}`
1. I simply switch to a new Tor identity
2. Continue the brute-force from a new IP like nothing happened 😎

Just like that, I broke free from the 10-request prison, and turned **“Try again later”** into **“Let me try forever”**

Of course, to pull this off, I had to set things up properly.

First step?

✅ **Install the Tor Expert Bundle** (not the browser — the actual service) from the official [Tor Project](https://www.torproject.org/) website.

This gives you access to the **Tor daemon**, which runs in the background and lets your scripts route traffic through the Tor network without launching the full browser.

Once installed and configured, I was able to:

- Connect my script to the Tor SOCKS proxy
- Programmatically **rotate identities (change IPs)** whenever I hit the rate limit
- Keep the brute-force going like a ghost 🕴️ in the machine

Basically, with Tor up and running, I had unlimited lives… and the OTP endpoint had no idea what hit it.

Next up — automation time! 🤖🐍

To make life easier (and faster), I wrote a Python script to:

- Brute-force the OTP code
- Detect when the correct OTP was accepted
- Then immediately **reset the password** function will be executed with the new password i passed .

Basically, all I had to do was:

1. Ask for otpCode of certain phoneNumber
2. Let the script handle the rest 💅

Here’s a simplified version of how it worked:

Sure, using the Tor network isn’t exactly fast — 

It’s more like… the turtle of the internet 🐢💨

But hey, **slow and steady still pwns the race** 😎

After about **an hour of brute-forcing through Tor**, I finally got a hit — 

💥 **Valid OTP found!**

At this point, it was game over:

- I could **reset the password of any account**,
- All I needed was the victim’s **phone number** 📱
- No need for passwords, emails, or access to the victim’s device

But then I had a darker thought 💭

“If I can get the phone number of one of the **admin users** — like a branch manager or staff member — 

I could easily take over their account too…”

And guess what?

I discovered that the admin panel lives at a sweet little subdomain:

👉 **admin.target.com**

With access to an admin account, the possibilities just expanded:

- Full control of orders, users, products
- Potential access to sensitive data
- And maybe even RCE if they have file upload features 👀
