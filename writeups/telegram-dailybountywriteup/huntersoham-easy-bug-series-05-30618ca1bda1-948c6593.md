# Easy Bug Series | #05

- **Source URL:** https://medium.com/@huntersoham/easy-bug-series-05-30618ca1bda1
- **Fetched from:** https://systemweakness.com/easy-bug-series-05-30618ca1bda1?source=rss-c501c19c2da6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14929 (id 14929)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Soham D. Jadhav / Thu, 01 Oct 2026 04:31:05 GMT

Did You Really Log Out?

You Clicked Logout.

You closed the browser.

You think your sensitive data is gone.

But what if the browser still has it?

Let’s test something that is often overlooked:

**Browser Caching.**

Hello everyone 🙌

This is my 5th article of **The Easy Bug Series**, where i share my own security testing methodologies that can help beginners to get their first valid bug.

In today’s article, we’ll look at a small but interesting issue:

We usually test on the pages which the application properly protected.

But there is another question we should ask:

**What happens to those pages after logout?**

Let’s Find that…

**First, Login to your test account**

Start with an account that you use for testing.

Login to the application.

Go to the pages or endpoints where you can see any sensitive details like:

Now, refresh the page once and make sure it loads normally.

**Now, Logout**

Logout from your account

You would be redirected to the login page or home page.

At this point, everything looks normal. like nothing happened.

But don’t stop here.

**Press the browser back button.**

This is where the intresting part coming in…

**What happens Next?**

There are different possible behaviours.

**behaviour 1 — The page is not accessible**

You press back button.

The page asks you to login again.

This is an expected behaviour.

**behaviour 2 — The browser shows the old page**

You press the back button.

And suddenly you can see the previously visited authenticated pages.

Your account information is visible again

You may even go to the previously loaded pages.

Now we have something intresting to investigate.

**Check the Cache-Control Headers**

open the affected request in your browser’s developers tools or burpsuite.

Look at the response headers.

Specifically Look for this :

Cache-Control

For sensitive authenticated pages, applications should use appropriate cache-control directives to prevent sensitive content from being stored and resued by the browser.

For example, you may see something like this:

Cache-Control: no-store

or other appropriate directives depending on the application’s requirements.

if sensitive authenticated content is cached when it shouldn’t be, investigate further.

**Why Does This Matter?**

Imagine this situation:

You log into an application from a shared computer.

You open your account dashboard.

Then you logout.

the next person open the same browser and press back button.

if sensitive account information is still available from the browser cache, they may be able to see information from your previous session.

The actual impact depends on:

So don’t report it just because you see an old page after pressing back.

**What Should You Check?**

Whenever you are testing authenticated pages, try this first:

If sensitive authenticated content remains accessible from cache after logout, document the exact behaviour before reporting it.

Sometimes we ask:

**“Can I access this page while logged out?”**

But also ask:

**“Can my browser still remember it?”**

That’s it for **The Easy Bug Series | #05.**

What would you try to chain with improper cache-control? 👇

See you in the next one!

Find me here:

Happy Hunting! 🐞🔍

#BugBounty #WebSecurity #CyberSecurity #Pentesting #VAPT #BugBountyTips

[Easy Bug Series | #05](https://systemweakness.com/easy-bug-series-05-30618ca1bda1) was originally published in [System Weakness](https://systemweakness.com) on Medium, where people are continuing the conversation by highlighting and responding to this story.
