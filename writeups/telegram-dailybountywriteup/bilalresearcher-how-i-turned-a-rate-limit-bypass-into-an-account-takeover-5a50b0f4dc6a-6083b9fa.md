# How I Turned a Rate-Limit Bypass into an Account Takeover

- **Source URL:** https://medium.com/@bilalresearcher/how-i-turned-a-rate-limit-bypass-into-an-account-takeover-5a50b0f4dc6a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240829065144/https://medium.com/@bilalresearcher/how-i-turned-a-rate-limit-bypass-into-an-account-takeover-5a50b0f4dc6a
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7068 (id 7068)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Turned a Rate-Limit Bypass into an Account Takeover

Hello, fellow hunters!

In this blog post, I’ll walk you through how I discovered a rate-limit bypass vulnerability that led to an account takeover. Let’s dive into the details.

# The Beginning: Reconnaissance

As always, I started with the basics — reconnaissance. I performed the usual steps: subdomain enumeration, crawling URLs, looking for JavaScript leaks, and so on. It was a standard recon process, but this time, it didn’t yield any significant findings.

# Shifting Gears: Manual Testing

With no luck in recon, I decided to move on to manual testing, focusing on the registration and login pages. The login page was protected by rate-limit security measures, designed to block brute-force attacks after 20 incorrect attempts.

# The Discovery: Rate-Limit Bypass

Determined to find something, I tested various techniques to bypass the rate limit. To my surprise, one method worked! I was able to bypass the rate-limit protection and brute-force passwords indefinitely.

However, brute-forcing passwords is usually considered a low-severity issue (P4). Since I had successfully bypassed the rate limit, I knew the severity might increase to P3 (medium). But I wanted to take it further — I was curious if there were other features vulnerable to the same bypass.
