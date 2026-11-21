# Sensitive Data Exposure + Public Recon = Instant Account Takeover

- **Source URL:** https://medium.com/@GERRR4Y/sensitive-data-exposure-public-recon-instant-account-takeover-97c2ae752720?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250911185457/https://medium.com/@GERRR4Y/sensitive-data-exposure-public-recon-instant-account-takeover-97c2ae752720
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9430 (id 9430)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Sensitive Data Exposure + Public Recon = Instant Account Takeover🔻

“بسم الله و الصلاة و السلام على رسول الله الحمد لله الذي علم بالقلم علم الإنسان ما لم يعلم و الصلاة و السلام على خير معلم الناس الخير محمد”

🔻دعواتنا دائمًا لأهلنا في غزة، اللهم كن لهم عونًا ونصيرًا، وافرغ عليهم صبرًا وعزيمة.

## Introduction

While conducting a passive reconnaissance exercise on target.com, I discovered publicly accessible URLs containing **login credentials** for a real user account. Using only publicly available OSINT tools — no brute force, no internal access — I was able to **log into the account**, access **sensitive personal data** (name, phone number, address, login history,email), and effectively perform an **Account Takeover (ATO)** with zero friction.

This all started as part of a routine recon on target.com, a trading platform, caught my attention. I used an open-source tool to automate the collection of indexed URLs and started analyzing the responses manually.

*For full transparency, the tool I used is publicly available on GitHub:* 

[*https://github.com/killua889/otx-url.git*](https://github.com/killua889/otx-url.git)

This tool scrapes URLs indexed by threat intel platforms (like AlienVault OTX), which often capture exposed endpoints during past scans or incident reports. While inspecting the returned URLs, I found a login**URL** in the following format:

[https://app.target.com/ :](https://deriv.com/signup:email@example.com:SomePassword123)example[@](https://deriv.com/signup:email@example.com:SomePassword123)gmail[.com:Password123](https://deriv.com/signup:email@example.com:SomePassword123)

This immediately raised red flags .

## Exploitation

I took a cautious approach — I tested the credentials against the platform’s login page (app.target.com). To my surprise, I was **immediately logged in**. No CAPTCHA. No MFA challenge. Just a direct login using leaked credentials.

Once inside the account, I was able to access:

- Full name
- Phone number
- API key
- Address
- Date of Birth
- Account settings
- login history
- Internal support/chat interface
- connected Apps, etc….

There were no signs of the account being a test or sandbox account. While it had no financial transactions yet, the personal data alone qualifies as **sensitive information** under most security and compliance standards.

## **Why This Write-up Still Matters:**

Even though the report was marked as a duplicate, I believe the **scenario is highly valuable** for other researchers — especially those focusing on **recon and open-source intelligence**.

This case shows how minimal effort using public tools can lead to impactful discoveries. No internal access. No advanced exploitation. Just recon and analysis.

Please share your feedback with me!

And let’s connect on Twitter: [X \ آية أيمن 🇵🇸 (@GERR4Y)](https://x.com/GERR4Y)
