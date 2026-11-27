# The PDF Trojan Horse

- **Source URL:** https://uchihamrx.medium.com/the-pdf-trojan-horse-leveraging-html-injection-for-ssrf-and-internal-resource-access-fbf69efcb33d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260719064308/https://uchihamrx.medium.com/the-pdf-trojan-horse-leveraging-html-injection-for-ssrf-and-internal-resource-access-fbf69efcb33d
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6607 (id 6607)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The PDF Trojan Horse: Leveraging HTML Injection for SSRF and Internal Resource Access

.بِسْم اللَّه الرَّحْمن الرَّحِيم . . اللَّهمَّ صَلِّ وَسلَّم وبارك على نَبِينَا مُحمَّد

In the name of God, the most gracious, the most merciful.

May Allah’s blessings and peace be upon our Prophet Muhammad.

Before we begin, I offer my prayers for my brothers in Palestine and Sudan, asking Allah to grant them unwavering strength and ultimate victory.

## Introduction

In this writeup, I will detail the discovery of a critical SSRF vulnerability I found in a private Bug Bounty Program. This article explores how a low-severity bug like HTML injection (HTMLi) can be exploited via PDF generation to achieve SSRF, leading to access to AWS metadata and internal resources.

### **Discovery of HTML Injection:**

The web app is designed for company management, catering to both users and clients. Each user gets a unique subdomain to manage their company, such as `hacker.target.com`. After creating an account, I used the app like a normal user to gather information about its features. Once I had a good understanding, I started with the profile section. In the fields for username and company name, I tested a basic HTML payload like `'"><h1>Mrx</h1>` to see if it would execute. It worked, and the HTML injection payload executed successfully.

This initially perceived as low-severity, Let’s try to make it more impactful.

### **SSRF via PDF Generation Attack:**

During my exploration, I found a feature generating monthly PDFs containing statistical data. My mind lit up with the idea of launching an SSRF attack via PDF generation. You can learn more about this attack by checking out these [slides](https://docs.google.com/presentation/d/1JdIjHHPsFSgLbaJcHmMkE904jmwPM4xdhEuwhy2ebvo/htmlpresent).

I generated the PDF with the HTMLi payload and found that the HTMLi persisted in the PDF rendering. I realized the potential for SSRF exploitation.

To validate this I replaced the HTMLi payload with an iframe payload pointing to a Burp Collaborator (`<iframe src="http://Burp-Collaborator"></iframe>`). Upon generating the PDF, I successfully received callbacks, confirming SSRF feasibility.

### **Exploiting SSRF:**

To escalate the exploit, I attempted to access local resources by embedding `<iframe src="http://127.0.0.1"></iframe>` and regenerating the PDF. This action granted access to internal portals, demonstrating the exploitability of the SSRF vulnerability. Knowing the Target utilized AWS services, I targeted AWS metadata endpoints (`<iframe src="http://169.254.169.254/latest/meta-data"></iframe>`). Upon regenerating the PDF with modified payloads. and Boom! We got it!

Let's proceed to access AWS credentials.(`<iframe src="http://169.254.169.254/2021-07-15/meta-data/identity-credentials/ec2/security-credentials/ec2-instance"></iframe>`). Upon regenerating the PDF with modified payloads. and I successfully accessed AWS credentials.

I’ve submitted the report to the program. They acknowledged its severity as critical and rewarded me.

Thank you for taking the time to read, and I hope it proves beneficial to you.
