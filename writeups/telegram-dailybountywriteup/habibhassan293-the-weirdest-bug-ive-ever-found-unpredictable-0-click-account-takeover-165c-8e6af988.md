# The Weirdest Bug I’ve Ever Found — Unpredictable 0-Click Account Takeover

- **Source URL:** https://medium.com/@habibhassan293/the-weirdest-bug-ive-ever-found-unpredictable-0-click-account-takeover-165c54fa81c7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251127095656/https://medium.com/@habibhassan293/the-weirdest-bug-ive-ever-found-unpredictable-0-click-account-takeover-165c54fa81c7
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11686 (id 11686)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Weirdest Bug I’ve Ever Found — Unpredictable 0-Click Account Takeover

I was testing on \[REDACTED\] for about 1–2 days. Back then, I had zero methodology — no recon, no planning, just straight into hunting like a typical beginner.

One thing I’ve learned that’s absolutely crucial in bug bounty: **test everything**. Even the stuff that seems completely useless. Because sometimes those “useless” things turn out to be impactful, as you’re about to see.

## The Discovery

So I was messing around with the forgot password functionality. Nothing special, just another forgot password endpoint. There were two parameters: `email` and `redirect_uri`.

I tried everything I could think of:

- Host header injection
- Sending requests with no email
- Parameter pollution
- null bytes

Absolutely nothing worked.

At this point, I was pretty hopeless. But I thought, “you know what, let me just test for open redirect.” And here’s the thing — it was a POST request, so even if there WAS an open redirect, it wouldn’t really count as vuln since its POST.

But I modified the `redirect_uri` anyway.

**And suddenly, I was logged into the victim’s account.**

I honestly thought it was a glitch. Like, what? I didn’t even understand what just happened. So I just… forgot about it and moved on.

## The Realization

Two days later, I came back to test the forgot password again (Alhamdullilah for second chances).

Kept trying different attacks on the email parameter — nothing. Then I modified the `redirect_uri` again, and AGAIN - logged into the account. Again.

I tested it multiple times. Every single time, just by modifying the `redirect_uri` parameter, I gained full access to the victim's account. No password reset. No email confirmation. Nothing.

## What Was Actually Happening

Here’s what I think was happening in the backend (and this is just a guess):

When you send a faulty `redirect_uri`, the server - for some absolutely bizarre reason - **fixes your current session token to be the victim's session token**.

the reason i think that? My own session token didn’t even change. It stayed exactly the same, but now it had access to the victim’s account. It’s like the server just… switched the permissions on my existing session.

**Impact:**

- Full account compromise of any user

## Lessons Learned

1. **TEST EVERYTHING.** Even the things that seem pointless. That “useless” open redirect test turned into a HIGH ATO.

Alhamdullilah forever for his grace.
