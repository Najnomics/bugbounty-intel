# Email verification bypass due to race condition.

- **Source URL:** https://medium.com/@mohamed.yasser442200/email-verification-bypass-due-to-race-condition-8e4492313208?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241119062328/https://medium.com/@mohamed.yasser442200/email-verification-bypass-due-to-race-condition-8e4492313208
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6764 (id 6764)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
One day, I decided to hunt on a security services company’s public program with a limited scope.

In the past, I hesitated with public programs due to security concerns, but this time, I decided to trust myself and simply enjoy testing the program without worrying about finding vulnerabilities.

# **What is a bug?**

The site makes a security layer -> you should verify your email by sending token to your email (this happen also if you change your email), while editing my email, I performed Race Condition to bypass this verification layer.

# Detailed scenario:

I registered to the site and verified the email then I logged in.

First, I went to account setting and change my email, this message appeared to me

From this message, I got an idea to bypass this verification using Race condition. Because if the site just needs a valid verification URL and does not confirm that verification URL related to the email address, we can bypass it.

I intercepted change email request and send it to repeater

to test it we need to send the request at least 2 times so send it to the repeater again

In the first one add the email you want to take over

Add your own email in the second one.

then create group to be able to send the two requests in the same time

Now click the down arrow and choose *send group in parallel*

finally, send the two requests

Unexpected moment, the second email (spider4@gmail.com) has verification URL

I opened it and no error :)

and when I opened my dashboard I found that my email is ***admin@example.com —*** not my email — and It is verified.

I reported it and it triaged as P4.

But :(

This is the Security team’s response.
