# How to Find Subdomain Takeover in Bug Hunting

- **Source URL:** https://medium.com/@vipulsonule71/how-to-find-subdomain-takeover-in-bug-hunting-33aed8f43c27?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250406162505/https://medium.com/@vipulsonule71/how-to-find-subdomain-takeover-in-bug-hunting-33aed8f43c27
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9037 (id 9037)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# 🔍 How to Find Subdomain Takeover in Bug Hunting 🚀

**🔍 How to Find Subdomain Takeover in Bug Hunting 🚀**

Subdomain takeover is a critical security vulnerability that occurs when an attacker takes control of an orphaned or misconfigured subdomain. Bug bounty hunters often look for such weaknesses to report and earn rewards. In this blog, we’ll explore how to identify and exploit subdomain takeovers efficiently.

**📌 What is Subdomain Takeover?**

A **subdomain takeover** happens when a subdomain of a website points to an external service (e.g., AWS, GitHub, Heroku) that is no longer in use, allowing attackers to claim it.

**🎯 Step-by-Step Guide to Finding Subdomain Takeovers**

**1️⃣ Gather Subdomains**

Use tools like:

🔹 **Amass** — amass enum -d target.com

🔹 **Subfinder** — subfinder -d target.com

🔹 **Assetfinder** — assetfinder — subs-only target.com

**2️⃣ Check for Dead DNS Records**

Once you have a list of subdomains, check if they resolve to an unclaimed service. Tools like dig, host, and nslookup help:

dig CNAME subdomain.target.com

host subdomain.target.com

If the subdomain points to a third-party service but the service is no longer active, it might be vulnerable.

**3️⃣ Verify with HTTP Response**

Send an HTTP request using curl or httpx:

curl -I [http://subdomain.target.com](http://subdomain.target.com/)

httpx -u subdomain.target.com

Look for error messages like:

❌ *“No such bucket”* (AWS S3)

❌ *“There isn’t a GitHub Pages site here”*

❌ *“Heroku | No such app”*

**4️⃣ Attempt to Claim the Subdomain**

If the external service allows you to create a new resource with the same name, you can confirm the takeover. However, **never perform actual takeovers on live targets unless permitted by the bug bounty policy.**

**🔥 Best Tools for Subdomain Takeover**

🔹 **Subjack** — Automates subdomain takeover detection

🔹 **Takeover** — Finds vulnerable subdomains

🔹 **Nuclei** — Has predefined templates for takeover scanning
