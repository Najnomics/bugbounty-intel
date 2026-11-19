# The Simple Bug That Led Me to My First Bounty (Account Takeover via Insecure Reusable Activation…

- **Source URL:** https://medium.com/@sudo_a7med/the-simple-bug-that-led-me-to-my-first-bounty-account-takeover-via-insecure-reusable-activation-918c1ea1a362?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260519120846/https://medium.com/@sudo_a7med/the-simple-bug-that-led-me-to-my-first-bounty-account-takeover-via-insecure-reusable-activation-918c1ea1a362
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11928 (id 11928)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Simple Bug That Led Me to My First Bounty (Account Takeover via Insecure Reusable Activation Link)

“بِسْمِ اللَّهِ، وَالْحَمْدُ لِلَّهِ، وَالصَّلَاةُ وَالسَّلَامُ عَلَى رَسُولِ اللَّهِ، اللَّهُمَّ عَلِّمْنَا مَا يَنْفَعُنَا، وَانْفَعْنَا بِمَا عَلَّمْتَنَا، وَزِدْنَا عِلْمًا”

اللهم انصر إخواننا المستضعفين في فلسطين والسودان وفي كل مكان

Hello Hackers! Back again, this is Sudo.

This write-up and the specific vulnerability are very different for me because this is the bug that landed me my first bounty!

Let’s dive right into the details.

The Discovery Phase

The vulnerability was quite simple initially, but it’s the kind of detail many people often overlook in application logic.

Let’s call the target website *\`target.com\`*.

When I created a new account, the application sent an Activation Link to my email to verify the account.

I clicked the link, and it immediately logged me into my account.

*Note: I spent some time understanding the site’s overall workflow, which took me a full day due to its size and the number of functions available. Understanding the Business Logic is crucial.*

The next day, I was ready to start testing. I created another account and received the activation link.

I clicked it, and I was logged in immediately.

My mind paused: “Why was I logged in directly? Shouldn’t the link’s sole purpose be account verification, not granting a session?”

## **Standard Security Practice: An activation link should ideally be single-use. Its job is to change the account state from “unverified” to “verified” and then it should expire immediately.**

### Confirming the Vulnerability:

I tried opening the exact same activation link again.

The Surprise: It logged me into my account again!

This was the vulnerability: Every time I opened the activation link, it granted me direct access to the account. The activation link was functioning as a persistent, passwordless session token.

I quickly wrote the report, highlighting that the link was reusable and automatically logged the user in.

One day later, the security team responded:

This response was a direct confirmation of the issue! The security team focused on the 48-hour expiration but ignored the core problem:

### Reusability: The link can be used more than once.

### Automatic Login: The link not only verifies but also authenticates the user.

These two factors combined transform a simple activation link into a 48-hour Account Takeover vulnerability!

Here is the summary of the follow-up I sent to clarify the security impact:

After my detailed follow-up explaining the real security impact, they reopened the report and set the status to Under Review.

Seven days later, the surprise came: The vulnerability was accepted, and I was rewarded!

It was truly an indescribable feeling, as it was my first-ever bug bounty payout.

### Technical Classification: This bug falls under a form of Broken Authentication or Broken Access Control, where a verification token is improperly used to establish a long-term, reusable user session.

I hope you found this write-up educational.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

The Takeaway:

Always focus on the Business Logic and how the application is supposed to work securely. Small details in the workflow often lead to critical bugs. If your report is initially rejected, don’t give up — clearly articulate the Impact and the exploitation scenario with logical, security-focused reasoning.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

Until next time — happy hacking!

You can follow my journey on bug bounty on X(Twitter), where I post daily updates: [https://x.com/sudo\_a7med](https://x.com/sudo_a7med) .
