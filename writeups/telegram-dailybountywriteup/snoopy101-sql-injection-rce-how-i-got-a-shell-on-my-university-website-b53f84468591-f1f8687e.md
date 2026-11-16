# SQL Injection + RCE | How I got a shell on my university website

- **Source URL:** https://medium.com/@snoopy101/sql-injection-rce-how-i-got-a-shell-on-my-university-website-b53f84468591?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@snoopy101
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 1775)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hi wonderful hackers.

I’m gonna tell you the story of an easy Blind SQL injection which led to RCE. I do not really spend my time on hacking non-bug bounty websites like my university and I found this vulnerability coincidentally.

I was doing my stuff on the website like a good student, and suddenly I realized that some data were fetching through an API.

So I fired up my Burp (or it was already up I don’t remember) and sent these Blind SQL payloads with intruder on battering ram mode.

' or sleep(5)#--

' or sleep(5)='

;waitfor delay '0:0:5'--

') or sleep(5)='

**Result:**

*The “;waitfor delay '0:0:5'--” payload worked*

Dear database sleep 5 seconds:

*Look in the bottom right corner of the page*

Sleep 10 seconds:

After that I did the exactly same thing that you are thinking right now.

I gave the URL to the amazing tool [sqlmap](https://github.com/sqlmapproject/sqlmap), and I was able to see the whole Database

#### Honestly the database was fairly huge, and I wasn’t interested in breaching the whole database. Also, I already had everything: usernames, passwords, backups, addresses, phone numbers, E-mails, …

### RCE

The process of getting a shell was pretty easy too. I just needed to use sqlmap shell commands:

First I used this command

sqlmap -u "https://snoopy-college.tld/api/v1/StudentSomething?parameter1=9999" -H "Cookie: uni-cookie=MY-COOKIE-HERE"  --random-agent --os-cmd whoami

sqlmap response:

Cool. For the last move I ran this command :

sqlmap -u "https://snoopy-college.tld/api/v1/StudentSomething?parameter1=9999" -H "Cookie: uni-cookie=MY-COOKIE-HERE"  --random-agent --os-shell

#### **And got the sqlmap shell**

Although I had access to literally everything, I didn’t do anything malicious. I just ran some basic commands and saw all files on the server.

A black-hat hacker could’ve abused this to:

- Deface the website
- Shutdown the server/website
- Extract all the files on the server (using FTP server or something else)
- Delete all the files and directories
- You tell me :)

After those basic commands I simply closed my terminal.

A couple of days later I told this to the university, and they fixed it right away.

Thank you for your attention and feel free to leave a ***comment*** if you have any question!

[SQL Injection + RCE | How I got a shell on my university website](https://systemweakness.com/sql-injection-rce-how-i-got-a-shell-on-my-university-website-b53f84468591) was originally published in [System Weakness](https://systemweakness.com) on Medium, where people are continuing the conversation by highlighting and responding to this story.
