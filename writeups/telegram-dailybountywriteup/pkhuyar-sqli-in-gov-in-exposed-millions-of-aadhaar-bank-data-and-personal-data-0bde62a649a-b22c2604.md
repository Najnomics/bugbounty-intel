# SQLi in .gov.in Exposed Millions of Aadhaar, Bank Data and Personal Data

- **Source URL:** https://medium.com/@pkhuyar/sqli-in-gov-in-exposed-millions-of-aadhaar-bank-data-and-personal-data-0bde62a649aa?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905103718/https://medium.com/@pkhuyar/sqli-in-gov-in-exposed-millions-of-aadhaar-bank-data-and-personal-data-0bde62a649aa
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9547 (id 9547)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQLi in .gov.in Exposed Millions of Aadhaar, Bank Data and Personal Data

Hi, I’m Prashant Kamkar, a cybersecurity enthusiast, occasional bug bounty hunter, and automation enthusiast. I love building things that automate my work. This is the story of how I combined automation, some of the best hacking tools, and a bit of curiosity to uncover a critical SQL injection vulnerability in an Indian government website, with access to millions of records, names, phone numbers, Aadhaar numbers, passwords (in plain text), bank details, address and more.

I wasn’t actively hunting a specific target. I was testing my own automated bug bounty pipeline, a tool I’ve been building to integrate the best open-source recon and exploitation tools into a seamless workflow. I ran it on a random domain… and boom — a high-impact SQLi vulnerability on an Indian government website. Let me show you exactly how I built the toolchain, how it works, and how it led me to one of the most critical bugs I’ve ever reported.

I decided to simplify the chaos. I started building an automated recon and scanning pipeline that could run on my cloud server. The idea? One script to do it all — from subdomain enumeration to target classification.

### **Top Tools I Integrated**

I run this pipeline on my **cloud server**. It’s optimised, fast, and most importantly, silent when it needs to be. I pointed my automated script at **some government sites.** I noticed suspicious behaviour in URLs returned by `waybackurls` while testing the web apps..

I ran some tests using **SQLmap**: I found that one parameter is vulnerable to **boolean-based, time-based** and **UNION-based injection.** See the screenshot below for extracted user data.

While checking some other table, it contains an Aadhar number, bank account number, IFSC code and other sensitive information.

This was **P1-critical,** exposing the sensitive data of **millions of Indian citizens**. I immediately reported the vulnerability to: **rvdp@nciipc.gov.in***(Responsible Vulnerability Disclosure Program, Govt. of India).* They acknowledged the issue and began remediation.

The affected endpoint is leaking highly sensitive citizen data due to improper input sanitisation. Exposed information includes:

· Full names and email addresses

· Mobile numbers and Aadhaar numbers

· Bank account details and IFSC codes

· Passwords stored in plain text

This wasn’t a lucky shot. It was the result of. Building a smart automation system. Using the right tools together. Being curious and validating what others miss. Automation is powerful, but it only works when paired with an attacker’s mindset. If you’re a bug bounty hunter or security researcher, consider building your own pipeline. Even a simple recon script can lead to your next big find.

This was a real-world example of how a small input validation flaw on a .gov.in domain can snowball into a national-level data breach. We’re talking millions of Aadhaar numbers, bank details, plaintext passwords, and full citizen profiles exposed to anyone with a bit of time and the right tooling.

Under the **Digital Personal Data Protection (DPDP) Act, 2023,** this kind of incident is exactly what the law was made to prevent. The act holds both private and government entities accountable for careless data handling, and something like storing passwords in plain text or leaking Aadhaar numbers through SQLi could trigger fines up to ₹250 crore. **I’m not here to point fingers, but I do want to stress this.**

## Security basics still matter

Input sanitization, encrypted storage, proper access control — these aren’t optional. Especially when you’re handling citizen data at scale.

I didn’t find this bug because I was targeting a specific site. I found it because I built an automation system that treats every target seriously. And because curiosity still wins.

If you’re a hacker, build your tools.

If you’re an engineer, test your assumptions.

If you’re a government agency, encrypt your data. Please.

Thanks for reading. Stay curious. Hack responsibly.


If you like it please share and give claps to my post.

Prashant Kamkar
