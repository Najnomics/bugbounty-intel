# How I Hacked 2FA for a $4,500 Bounty… in Just 24 Hours!

- **Source URL:** https://medium.com/@ibtissamhammadi1/how-i-hacked-2fa-for-a-4-500-bounty-in-just-24-hours-7f752a47c0c5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905093526/https://medium.com/@ibtissamhammadi1/how-i-hacked-2fa-for-a-4-500-bounty-in-just-24-hours-7f752a47c0c5
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9786 (id 9786)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# How I Hacked 2FA for a $4,500 Bounty… in Just 24 Hours!

## *(A Step-by-Step Bug Bounty Breakdown)*

**“The company said their 2FA was unbreakable. They were wrong — and I earned $4,500 in a single day.”**


Two-factor authentication (**2FA**) is supposed to be the *gold standard* for security. But what if I told you **a single misconfigured token** let me bypass it entirely?

This isn’t theory — it’s exactly how I **earned a $4,500 bug bounty** in under **24 hours**. And the scary part? **You could do it too.**

Here’s the full story, with **every technical detail** (and a few lessons I learned the hard way).

### Step 1: Finding the Flaw

The target was a **public** [**bug bounty program**](/tag/bug-bounty-program) (let’s call it [*redacted.com*](http://redacted.com)). Their login flow looked solid:

1. Enter **username/password**.
2. Get an **OTP (One-Time Password)** via SMS.
3. Submit OTP → access granted.

But when **the OTP screen loaded**, something felt *off*.

**“Why was a JWT token already generated *before* OTP verification?”**

I fired up **Burp Suite**, intercepted the request, and saw this:

```
POST /api/verify-otp HTTP/1.1  
Host: redacted.com  
Authorization: Bearer…
```
