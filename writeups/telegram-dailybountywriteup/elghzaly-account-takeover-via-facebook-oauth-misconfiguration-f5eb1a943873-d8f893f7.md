# Account Takeover via Facebook OAuth Misconfiguration

- **Source URL:** https://medium.com/@elghzaly/account-takeover-via-facebook-oauth-misconfiguration-f5eb1a943873?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250919194511/https://medium.com/@elghzaly/account-takeover-via-facebook-oauth-misconfiguration-f5eb1a943873
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9919 (id 9919)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account Takeover via Facebook OAuth Misconfiguration

Hey everyone, Today I’m excited to share a bug I discovered in a Bugcrowd VDP target involving **Facebook login** — and it led to **full account takeover** without any victim interaction. Grab your coffee and let’s dive in.

## **A quick word about oAuth**

OAuth is a widely-used authorization framework that allows third-party applications to grant limited access to user accounts without sharing credentials. It’s what enables you to “Log in with Facebook”, “Sign in with Google”, etc. While OAuth improves user experience and security, it introduces risks when developers assume identity data (like email) is trustworthy without additional validation.

Today, I’m sharing a Facebook OAuth misconfiguration that led to full account takeover without any victim interaction — exploited entirely from the frontend.

## **Finding the Flaw**

While reviewing the login page of the target application, I noticed the classic **“Login with Facebook”** option. This immediately piqued my interest — OAuth implementations often seem secure, but that surface hides a surprising number of edge cases and assumptions.

I clicked the button and authenticated via Facebook. As expected, Facebook presented the **“Edit Access”** screen, allowing me to customize the data shared with the target app.

I clicked **“Edit Access”** and unchecked the permission to share my **email address** with the application. Then I clicked **“Continue”** to finalize the login.

## Exploiting the Logic

Since the app didn’t receive my email from Facebook, it redirected me back and prompted me to **manually enter an email address**.

So, I typed in: `victim@example.com`

And… that was it. No verification, No confirmation email

The app **immediately logged me in as the victim**

**Steps to reproduce:**

1. Navigate to [example.com](http://example.com/) and initiate the login process using Facebook.

2. When prompted for permissions, deny access to your email address.

3. The site will then ask you to manually enter an email address.

4. Input the victim’s email, and you’ll be granted full access to their account — no password or verification required.

Thanks for reading!
