# Easy SQLI in just 30 minutes

- **Source URL:** https://medium.com/@mohammed01550038865/easy-sqli-in-just-30-minutes-0296038bb473?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250902123446/https://medium.com/@mohammed01550038865/easy-sqli-in-just-30-minutes-0296038bb473
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8145 (id 8145)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Easy SQLI in just 30 minutes

Hello All,

Today, I’ll share one of my findings on **Bugcrowd**. I will refer to the target as mytarget.com.


**Introduction:**

*SQL Injection (SQLi) is one of the most dangerous vulnerabilities affecting web applications. This write-up details my experience discovering and responsibly reporting an SQLi vulnerability in a government web application .*

**How I Started the Testing:**

*You might think that I started with Recon, and you’re right. However, if you ask many researchers how they try to discover hidden parameters, most will tell you they use tools like waybackurls, arjun, or paramspider. Those are great methods, but I want to highlight that some parameters can’t be discovered using these tools alone.*

### *So, what’s the additional method I suggest? Here it is: open your target normally, enable traffic interception in Burp Suite, and start browsing through links and pages. Afterward, review the Burp history for potential parameters.*

*Using this method, I discovered the vulnerable parameter that led to my finding.*

## 1. Discovering

While exploring mytarget.com, I came across an interesting endpoint:

`http://mytarget.com/?pageID=licensees&reportID=3003&sort=full_name`.
