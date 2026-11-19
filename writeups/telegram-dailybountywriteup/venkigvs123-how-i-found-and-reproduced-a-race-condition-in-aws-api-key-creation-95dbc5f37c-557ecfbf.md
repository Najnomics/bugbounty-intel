# How I Found and Reproduced a Race Condition in AWS API Key Creation

- **Source URL:** https://medium.com/@venkigvs123/how-i-found-and-reproduced-a-race-condition-in-aws-api-key-creation-95dbc5f37c90?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905081507/https://medium.com/@venkigvs123/how-i-found-and-reproduced-a-race-condition-in-aws-api-key-creation-95dbc5f37c90
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9697 (id 9697)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Found and Reproduced a Race Condition in AWS API Key Creation

\## Introduction

Hello, world!

In this blog, I’ll share how I discovered and responsibly disclosed a race condition that allowed bypassing the API key creation limit for a single AWS account. This wasn’t “hacking AWS,” but rather identifying a timing issue related to API key generation.

— -

\## Blog Structure

\- What is a Race Condition?

\- What Made Me Find This Vulnerability?

\- How I Reproduced This Vulnerability

\- Steps to Reproduce

\- How You Can Find Race Condition Vulnerabilities

\- How to Protect Yourself

\- Conclusion

— -

\## What is a Race Condition?

A \*\*race condition\*\* is a software error that occurs when the order of operations is not properly managed, leading to unexpected behavior. It often happens when multiple concurrent actions access shared resources without proper synchronization.

In this case, AWS enforces a restriction allowing each IAM user to create a maximum of two API keys. Due to a race condition, I was able to bypass this limit.

— -

\## What Made Me Find This Vulnerability?

Before exploring vulnerabilities, I follow a simple rule: \*\*Look for “you can’t” and try turning it into “I can.”\*\*

While testing another private bug bounty program, I noticed an option to integrate with AWS using API keys. During the setup process, I hit this error:

\`\`\`

Sender LimitExceeded: Cannot exceed quota for AccessKeysPerUser: 2

\`\`\`

My hacker instincts kicked in — could this be vulnerable to a race condition?

— -

\## How I Reproduced This Vulnerability

Armed with Burp Suite and curiosity, I began testing on my own AWS account.

\### Steps to Reproduce

1\. Log into AWS Console: \`https://us-east-1.console.aws.amazon.com/\`

2\. Navigate to IAM → Users → Select a user → Security Credentials.

3\. Ensure the user already has two API keys (the maximum allowed).

4\. Reproduction process:

\- Delete all existing API keys.

\- Intercept the \*\*CreateAccessKey\*\* request using Burp Suite.

\- Send the request to the Repeater tab.

\- Duplicate the request three times.

\- Group and send the requests using “Send group in parallel (last group sync)”.

\- All three requests succeeded, bypassing the 2-key limit.

5\. Refresh the AWS Console — three API keys were created instead of two.

\> ⚠ \*\*Disclaimer\*\*: Only test these techniques in accounts you own or within authorized scope. Refer to \[AWS security testing guidelines\](https://aws.amazon.com/security/penetration-testing/) before testing.

— -

\## How You Can Find Race Condition Vulnerabilities

Race conditions tend to exist where there are system-imposed limits or restrictions. Here’s how to spot them:

1\. Look for messages like \*“You cannot create more than X.”\*

2\. Identify if the action can be triggered concurrently.

3\. Use Burp Suite or custom scripts to send parallel requests.

4\. Observe how the system handles those requests.

— -

\## How to Protect Yourself

If you manage systems with enforced limits, here are some protection strategies:

\- Ensure limits are checked server-side with proper locking.

\- Use atomic operations or synchronization techniques.

\- Monitor API key creation with \*\*ListAccessKeys\*\* or the IAM Console.

\- Enforce regular audits and key rotation.

— -

\## Conclusion

Race conditions are often overlooked, yet powerful vulnerabilities. If you’re testing or developing secure systems, always challenge assumptions about concurrency and limits.

And the next time something says \*“You can’t”\* — just remember: \*\*Think carefully, test responsibly, and act ethically.\*\*
