# OAuth Misconfiguration Pre-Account Takeover

- **Source URL:** https://medium.com/h7w/oauth-misconfiguration-pre-account-takeover-535beb8d1987?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251013025434/https://medium.com/h7w/oauth-misconfiguration-pre-account-takeover-535beb8d1987
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7793 (id 7793)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Easy P1/P2 -OAuth Misconfiguration Pre-Account Takeover

Read For Free — [https://nexguardians.com/oauth-misconfiguration-pre-account-takeover/](https://nexguardians.com/oauth-misconfiguration-pre-account-takeover/)

Check out my previous articles on P4 bugs — [Part 1](https://nexguardians.com/p4-bugs-and-their-poc-steps-part-1/) , [Part 2](https://nexguardians.com/p4-bug-and-their-poc-steps-part-2/), [Part 3](https://nexguardians.com/p4-bugs-and-their-poc-steps-part-3/), [Part 4](https://nexguardians.com/p4-bugs-and-their-poc-steps-part-4/), [Part 5](https://nexguardians.com/p4-bugs-and-their-poc-steps-part-5/), [Part 6](https://nexguardians.com/p4-bugs-and-their-poc-steps-part-6/)

Hi everyone, I am socalledhacker, i am a security researcher , penetration tester, certified ethical hacker and a web3 noob. In past months, I have discover lots of bugs but in today’s article we are going to discuss about OAuth Misconfiguration Pre-Account Takeover, which i discover recently so without further delay let’s start….

## OAuth Misconfiguration Pre-Account Takeover

I discovered lots of OAuth misconfiguration pre-account takeover bug in past and this is only the bug I found the most, in almost every program that i hunt on which has login feature via Oauth, i got OAuth misconfiguration pre-account takeover because Oauth function is not easy to implement securely so developers always do mistake in configuration which is the cause of this bug and it is also complex to implement.

So lets talk about how to find/test this bug, let’s say you have a target which has login function via Oauth, now create an account using your email address and then a verification link will send to you email address, don’t verify that.
