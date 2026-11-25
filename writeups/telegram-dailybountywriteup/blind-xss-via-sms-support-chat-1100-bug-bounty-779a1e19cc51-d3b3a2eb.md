# Blind XSS via SMS Support Chat — $1100 Bug Bounty!

- **Source URL:** https://chevonphillip.medium.com/blind-xss-via-sms-support-chat-1100-bug-bounty-779a1e19cc51?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230410230632/https://chevonphillip.medium.com/blind-xss-via-sms-support-chat-1100-bug-bounty-779a1e19cc51?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2245 (id 2245)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Blind XSS via SMS Support Chat — $1100 Bug Bounty!

Hello Hunters, This is a quick write-up on how my blind XSS payload executed within an internal support portal via an SMS support chat.

This company (example.com) had a support site allowing users to submit a support ticket. You can create a support ticket in three ways:

1. Email Support
2. Phone Call Support
3. Text messages SMS support

**Option 3** stood out to me, and I decided to play around with this option. After a few minutes of creating a ticket, I decided to make another ticket, but this time injecting my blind XSS payload within the SMS message, which turned into a live SMS text between the support agent and myself.

Long Story Short…My payload got triggered after our chat ended with an internal note which also leaked the first and last name of the support agent and more.

Here is a redirected version of the PoC:

# Takeaways:

Always try your blind XSS payloads in areas that are not likely to expect one, like a support SMS chat.

I hope you like this short write-up. If you want to see more, please follow me here and on Twitter. [https://twitter.com/ChevonPhillip](https://web.archive.org/web/20230410230632/https://twitter.com/ChevonPhillip)
