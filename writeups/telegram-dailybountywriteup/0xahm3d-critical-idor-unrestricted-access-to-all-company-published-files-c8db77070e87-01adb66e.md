# Critical IDOR

- **Source URL:** https://medium.com/@0xAhM3D/critical-idor-unrestricted-access-to-all-company-published-files-c8db77070e87?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501221007/https://medium.com/@0xAhM3D/critical-idor-unrestricted-access-to-all-company-published-files-c8db77070e87
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9089 (id 9089)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Critical IDOR: Unrestricted Access to All Company Published Files**

بسم الله والصلاة والسلام على رسول الله ﷺ❤️، اللهم علِّمنا ما ينفعنا، وانفعنا بما علَّمتنا، وزِدنا علمًا نافعًا

It is my the First Bug bounty writeup, feel free to send me feedback ❤️

## Whoami

First let me introduce myself, I am 0xAhM3D. I am a newly started bug hunter, and this is my first week on HackerOne.

However, I have already discovered over 20 vulnerabilities on the Open Bug Bounty platform.

## Intro

In this writeup, I will explain how I gained access to all of the company’s published files, It is one of the leading global gaming companies.

## Let’s Begin

The program scope was small. One of the subdomains was **api.target.com** — let’s call it **Target**. I enjoy testing APIs and doing manual testing, which was a perfect fit for this scenario. Manual testing is different from automated testing; it enhances creativity, reduces repetition, and, while it requires more effort, it is definitely worth it.

I discovered the bug much faster than I expected — within the first few hours of exploring URLs and reading the API documentation.

## Steps That Led Me to find the bug:

- After discovering this interesting subdomain, the first thing I did was crawl URLs using **Wayback Machine, VirusTotal, and AlienVault**. I searched for different API methods and looked for exposed API keys that could reveal potential vulnerabilities

**URLs Used for Crawling: Wayback Machine:** https://web.archive.org/cdx/search/cdx?url=api.target.com/\*&collapse=urlkey&output=text&fl=original


**AlienVault OTX:** https://otx.alienvault.com/api/v1/indicators/hostname/api.target.com/url\_list?limit=500

**VirusTotal:** https://www.virustotal.com/vtapi/v2/domain/report?apikey=YourApiKey&domain=api.target.com
This allowed me to gather valuable information about Target APIs, including different API methods and potential API key exposures.


- Surprisingly, I discovered exposed valid API keys, which was a great starting point.
— Only one of these API keys was valid.

- By analyzing Target’s public API documentation, I found: [http://api.target.com/ITargetWebAPIUtil/GetSupportedAPIList/v0001](http://api.target.com/ITargetWebAPIUtil/GetSupportedAPIList/v0001) This revealed multiple API methods
**ITargetRemoteStorage/GetPublishedFileDetails** was the one that caught my attention

- This API method requires three main parameters: 
**key=**
**itemcount=**
**publishedfileids[0]=**
- It took me a lot of time to craft a valid request, but eventually, I succeeded. I retrieved a valid **publishedfileids**
**Wayback Machine**, using historical API responses.
- Using an exposed API key and a valid **publishedfileid**
**Burp Suite**: https://api.target.com/ITargetRemoteStorage/GetPublishedFileDetails/v1?key= valid one&itemcount=1&publishedfileids\[0\]=3058373765

- The response contained a **file_url**
As soon as I accessed the**file\_url**, the file was automatically downloaded without any authentication or restrictions.

**Now comes the IDOR part —Changing IDs.**

- As noted earlier, the **publishedfileids**
**uint64**
**20 digits**.
- So, let’s **bruteforce** from **1** to **99,999,999,999,999,999,999** 😆🔥

Surprisingly, there was absolutely no rate limiting in place, allowing unrestricted and rapid enumeration of all published files.

- I brute-forced the **publishedfileids**
**Burp Intruder**. Now,
let’s filter the requests by**response length** to identify the valid ones.

**Downloading All Files:**

- For each valid **publishedfileid**
**file_url**
- By iterating over these, I was able to download **thousands of files** without any restrictions — including **private and unlisted ones**

## After reporting:

- I was informed that the bug was a duplicate

- This was one of the fastest bugs I have ever discovered
