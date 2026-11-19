# Linux Privilege Escalation [Part-1] | EJPT Notes

- **Source URL:** https://medium.com/@hrofficial62/linux-privilege-escalation-part-1-ejpt-notes-7f978d958888?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250314150709/https://medium.com/@hrofficial62/linux-privilege-escalation-part-1-ejpt-notes-7f978d958888
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9025 (id 9025)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

Linux Privilege Escalation Techniques (full tutorial) , In which how to gain root user access after gaining foothold.

Hi Hackers this is the important part of the penetration testing where you need root privilege when you have foothold of target. I will explain each and every techniques of Linux privilege escalation. Don’t forget to follow me here and get more tips and techniques of penetration testing.

## Why I write this article?

for a days ago ,I was exploiting a machine where I got a foothold by and I need to access the flag.txt file that only open when you have root privilege. but I had regular user privilege that’s why i did not access that flag.txt file. So i search how to get root access on the target then got the term privilege escalation that helps to gain higher privilege. I learned it and share my knowledge with you. if you wanna appreciate my efforts so give clap to this article. Privilege escalation is not a small part its big there are lot techniques to gain higher privilege so i am starting from basics what kind of information we need to gain higher privilege and how we gather that information form Linux machine. I am dividing this article in to few parts . this is the first part of privilege escalation where we learn some manual techniques to fetch information from Linux machine.
