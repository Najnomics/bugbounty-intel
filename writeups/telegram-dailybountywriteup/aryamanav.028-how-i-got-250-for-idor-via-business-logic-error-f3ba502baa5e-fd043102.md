# How I got $250 for IDOR via Business Logic Error

- **Source URL:** https://medium.com/@aryamanav.028/how-i-got-250-for-idor-via-business-logic-error-f3ba502baa5e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240913102420/https://medium.com/@aryamanav.028/how-i-got-250-for-idor-via-business-logic-error-f3ba502baa5e
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6058 (id 6058)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **How I got $250 for IDOR via Business Logic Error**

Hello everyone👋

I hope you all are doing well. This write-up focuses on how I recently got my first bounty from a Bugcrowd program.

After struggling with lots of duplicates from the last two years (also not being consistent😅), I finally got a bounty of $250 for IDOR which I luckily found through a small bug or you can simply say a business logic error.

Now let’s begin✌️

*Reconnaissance:*

Firstly, I started by getting familiar with the web application and its workflow. Eventually, I explored how the target website is involved in handling transactions of funds with the help of user wallet IDs.

The web application was running in a **sandbox environment,** provided with some funds into the dummy account for testing purposes.


There were different feature tabs, for example, checking account balances, creating virtual accounts, and obviously making transactions. So I created two accounts for testing purposes and started looking for any endpoints containing parameters that might be vulnerable to IDOR.

A user can simply make transactions by searching another user’s wallet id. While searching, the user can enter the wallet id (which looks something like this **ewallet**\_random\_string

*Attacking phase:*

While pentesting, I didn’t find any potential parameters leading to IDOR but after spending days I found something worth checking. I noticed that in my profile name, there is an extra space added at the end by the web application every time I change it. As soon as I removed that extra space I was able to see two new options which allowed me to download `Account Statement` and `Proof of account`files. So now, what’s the next step?

I captured the requests in Burpsuite for these two endpoints and analyzed the parameters being passed in the POST body:

I found that my e-wallet id was being sent in both requests, so I just replaced that with one of the user’s e-wallet id obtained from the search results earlier. And guess what? I got a 200 OK response from the server, and the files were downloaded successfully!!

However, the downloaded file or template did not show the victim’s account balances, so the triage team changed the severity from **P3** to **P4**. But they decided to reward with a bounty as the server gave the **200 response code,** which it shouldn’t have for both endpoints.

*Techniques to find IDORs:*

1. First, look for endpoints containing parameters with unique IDs or strings as values (whichever is applicable).
2. Always create two accounts for testing purposes: one for the attacker and one for the victim. This ensures better clarity and a strong proof of concept (PoC).
3. Capture the requests having such parameters in Burpsuite.
4. Then try replacing the value of the unique id or string with the victim’s one.
5. Observe the behavior of the web application in terms of status codes to analyze potential vulnerabilities.

So, this is all about this writeup. I hope you find this useful and it has added some valuable insights to your knowledge. Also, this is my first write-up, so any suggestions would be appreciated.

Thanks for reading!!

Happy Hacking✌️

**Profile Links:**

**LinkedIn**: *https://www.linkedin.com/in/manav-arya-2ab3a11a5/*

**Twitter**: *https://twitter.com/manavarya28*
