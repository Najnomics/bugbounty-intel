# Bypassing Rate Limit Protection to Account Takeover

- **Source URL:** https://medium.com/@sohailahmed0x0/bypassing-rate-limit-protection-to-account-takeover-fe44598fc1df?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250131185835/https://medium.com/@sohailahmed0x0/bypassing-rate-limit-protection-to-account-takeover-fe44598fc1df
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8585 (id 8585)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bypassing Rate Limit Protection to Account Takeover

In this blog, I will share my finding in which I was able to bypass Rate Limit Protection on the Login page and was also able to show a valid POC for Account Takeover.

**Rate limit vulnerabilities** are security weaknesses that occur when a system or service doesn’t properly enforce limits on how many requests a user or system can make in a given time period. Essentially, these vulnerabilities arise when the system allows excessive requests from the same source or allows the rate of requests to exceed what is typical or safe.

How was I able to find this vulnerability?

I found this vulnerability on the Login page.

- First entered my testing account credentials.

- Captured this request using Burp Suite and sent it to Burp Intruder. Using Burp Intruder, I wanted to find if this endpoint is vulnerable to Brute Force Attack. I selected the password field because I knew that my email is correct. Tried around 50 random passwords and found out that the application was blocking me by giving 429: Too Many Requests Error. I thought that the application is secure.

- There are some methods which I saw somewhere bypassing Rate Limit Protection.

I used random headers to try and bypass the Rate Limit Protection. Luckily, I was able to bypass the Rate Limit protection using X-Forwarded-For Header.

After finding this out, I got back and tried another trick which I learned from solving **PortSwigger Labs**.

Burp Intruder has different “**Attack Types**”

The default attack type is “**Sniper**”, 2nd is “**Battering Ram**”, 3rd is “**Pitchfork**” and 4th is “**Cluster Bomb**”.

Battering Ram will use the payloads which you give them on Multiple added parameters.

Pitchfork will use different payloads for different selected parameters.

Cluster Bomb will allow you to perform complex, multi-position attacks. It is particularly useful when you need to send multiple payloads at different positions in a single request and want to test the combination of various inputs at those positions.

In my case, I used Pitchfork Attack.

This is how I was able to find a Rate Limit Bypass on the Login page which can also lead to Account Takeover as well.

I hope that my blog was helpful. Good luck hunting :)
