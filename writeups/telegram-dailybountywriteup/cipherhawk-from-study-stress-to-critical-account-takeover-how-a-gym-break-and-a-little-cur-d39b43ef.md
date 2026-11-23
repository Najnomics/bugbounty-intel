# From Study Stress to Critical Account Takeover

- **Source URL:** https://medium.com/@CipherHawk/from-study-stress-to-critical-account-takeover-how-a-gym-break-and-a-little-curiosity-uncovered-a-d15cfc2e142b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250503174030/https://medium.com/@CipherHawk/from-study-stress-to-critical-account-takeover-how-a-gym-break-and-a-little-curiosity-uncovered-a-d15cfc2e142b
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7698 (id 7698)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From Study Stress to Critical Account Takeover: How a Gym Break and a Little Curiosity Uncovered a Major Vulnerability

Today had been one of those nonstop days. Between work and study, it felt like my brain had reached maximum capacity. So when a friend pinged me, suggesting a quick bug hunt, I almost laughed it off. I was ready to call it a day! But I knew I needed a break from it all — so I hit the gym to clear my mind.

An hour later, recharged and back home, I thought, “**Why not?**” I called my friend, and within minutes, we were diving into the target app. It was an account management platform, and we both knew the reset password functionality could hold potential.

The plan was simple: explore the password reset flow and see if any unusual behavior popped up. But what happened next was anything but expected.

## Step 1: Testing the Password Reset — A Surprising 403 Response

We got into testing different scenarios, and I honed in on what the password reset response looked like. I clicked “**Reset Password**” and was met with an unexpected message saying, “**Email and password combination are invalid**.” This piqued my curiosity, so I switched over to Burp Suite, intercepting the response to inspect it closely.

There it was: a \`**403 Forbidden**\` status code.

At this point, my friend, watching my screen, suggested, “Why not try flipping that to \`**200 OK**\` and see what happens?” I liked the idea; it had a certain mad-scientist appeal to it lol. So I went ahead and edited the status code, changing the \`403 Forbidden\` to \`200 OK\`.

I forwarded the modified response, waited a second, and…\*\***boom**! Password successfully changed.\*\* Both of us went silent for a moment as we processed what just happened. We had just landed a **critical** vulnerability in about **12 minutes**.

## Step 2: The Big Idea — Testing Email Change for Full Account Takeover

We were still buzzing from the discovery when an even bigger idea popped into my mind. I thought, “**Wait**…if we can manipulate the response to reset the password, what if we could change the email too?” It was a moment of suspense. My friend liked the idea, I liked the idea — **even my Burp Suite seemed to like the idea.** This was the moment to test if we could turn this into a full account takeover.

So I intercepted the request to change the account’s email address, modified the response from \`403\` to \`200 OK\` once more, and let it through. \*\***BOOM!**\*\* **Full account control** was ours, with the email now changed for future resets. This was the jackpot — complete account takeover potential.

## Step-by-Step Process Breakdown: How We Pulled It Off

Let’s break it down for anyone looking to learn from this journey. Here’s how we managed the account takeover:

1\. *Start with Password Reset*: Go to the password reset functionality and trigger a password reset attempt. Make note of any messages or errors returned.

2. *Intercept the Response*: Use Burp Suite to intercept the response coming back from the server.

3. *Check the Status Code*: Look at the HTTP status code in the response. In this case, it was \`403 Forbidden\`.

4. *Manipulate the Status*: Change the \`403 Forbidden\` status code to \`200 OK\` and forward the modified response.

5. *Confirm Password Reset*: If the password is reset successfully, you’ve bypassed the intended security checks.

6. *Test Email Change for Full Takeover*: Next, repeat the steps above, intercepting the request to change the email address. Change the response status to \`200 OK\` and confirm if the email change is accepted, enabling full account takeover.

## Reflections — The Value of a Good Break and a Curious Mind

It’s funny how sometimes the best results come when you least expect them. After a long day, I wasn’t sure I’d find anything. But that gym break and a little curiosity turned into a major win. With a little back-and-forth brainstorming and quick tests, we went from “**Maybe this will work**” to a **critical** finding in no time.

The biggest takeaway? Never underestimate the power of a fresh perspective and an open mind. When you’re feeling stuck or doubting yourself, sometimes all it takes is one good idea, a friend to bounce it off, and maybe a little help from Burp Suite.
