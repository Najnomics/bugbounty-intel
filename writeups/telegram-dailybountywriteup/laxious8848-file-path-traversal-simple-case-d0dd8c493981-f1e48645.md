# File path traversal, simple case

- **Source URL:** https://medium.com/@Laxious8848/file-path-traversal-simple-case-d0dd8c493981?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241121210940/https://medium.com/@Laxious8848/file-path-traversal-simple-case-d0dd8c493981
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7934 (id 7934)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Local File Inclusion (LFI)** is a type of **vulnerability** in web applications that allows an attacker to trick the application into including files from the local file system on the server. This vulnerability typically arises due to improper input validation in file inclusion mechanisms.

This is the First LFI labs which we have to solve. I will manually test it. First turn on the Foxy proxy and burpsuite. But you dont need to on the intercept.

Use the sitemap not the intercept and on the top left side you will see the sitemap filter. Just go into it and add images and apply it. And you will see something like /image?filename=66.jpg. You can see anything not just 66.jpg. I am just taking it as example. And just right click and send this request to the repeater.

After remove the 66.jpg and add ../../../etc/passwd. You might be thinking why the hell this dude will write something so weird alien like. But Trust me this thing is going to work and i will explain it too. So we are telling it to get out of the directories, and execute /etc/passwd on behalf of us. The image should be stored in something like /var/www/images/. And it will just ends up with the root directory and /etc/passwd might be stored in it. And send it to and lets see the response.

And Our lab is solved…..
