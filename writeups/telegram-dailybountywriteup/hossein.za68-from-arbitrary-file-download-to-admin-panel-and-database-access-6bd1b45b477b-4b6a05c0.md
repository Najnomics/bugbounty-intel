# From Arbitrary File Download to Admin Panel and Database Access

- **Source URL:** https://medium.com/@hossein.za68/from-arbitrary-file-download-to-admin-panel-and-database-access-6bd1b45b477b
- **Fetched from:** https://medium.com/@hossein.za68/from-arbitrary-file-download-to-admin-panel-and-database-access-6bd1b45b477b?source=rss-30dc26eb393c------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14917 (id 14917)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Hossein Zarei / Fri, 18 Sep 2026 19:12:21 GMT

A while ago, I was browsing the source code of different GitHub projects while looking into some frameworks and services. By chance, I came across a website that immediately caught my attention.

The first thing I noticed was that the site appeared to be vulnerable to **Arbitrary File Download / Arbitrary Local File Read**.

For example, the following endpoint was used to download some PDF files containing guides and course materials:

https://target.com/download.php?file=\*.pdf

However, when I supplied the name of a PHP file to the same parameter, the application would return the actual PHP file for download instead of executing it.

For example:

https://target.com/download.php?file=download.php

The website also had an admin login panel:

https://target.com/admin/auth.php

So naturally, I wanted to see whether this file could also be retrieved through the same vulnerability.

I tried:

https://target.com/download.php?file=auth.php

And the file was downloaded successfully.

That’s where things started to get interesting.

After downloading the file, I started going through its source code. In one part of the code, I found a temporary login mechanism where the username and password were stored directly in the source code in **cleartext**.

The sensitive values have been redacted in the screenshot below:

I used one of the credentials and was able to log in to the admin panel.

At this point, the attack chain had already moved beyond a simple file download:

Arbitrary File Download

↓

Source Code Disclosure

↓

Credential Disclosure

↓

Admin Panel Access

The first thing that came to mind after getting access to the admin panel was testing its **File Upload** functionality.

There were several upload features throughout the panel, including PDF and image uploads.

I decided to start with the **Upload PDFs** section.

For the initial test, I used a very simple PHP shell:

\<?php system($\_GET\['c'\]); ?>

Interestingly, there didn’t seem to be any effective file-extension validation in place, and the PHP file was uploaded successfully.

Finding the upload path was also relatively easy because I already had access to the application’s source code, which revealed where uploaded files were being stored.

The uploaded file was accessible at a path similar to:

https://target.com/admin/uploads/shell.php?c=id

At this point, I expected to be able to execute an operating system command through the c parameter and achieve **OS Command Execution / RCE**.

However, the command didn’t produce any output.

To understand what was preventing command execution, I uploaded a simple PHP file containing phpinfo() and checked the PHP configuration.

It turned out that a number of potentially dangerous PHP functions had been disabled in the environment, which prevented my initial approach from working.

So the direct path to OS Command Execution wasn’t available in the way I initially expected.

But that didn’t mean the attack chain had to stop there.

I had previously read about situations where PHP-based file-management functionality could still be useful in environments where direct command execution through functions such as system(),shell\_exec() and etc was restricted.

Instead of focusing entirely on OS Command Execution, I decided to try a different approach using a **standalone PHP file manager**.

For this, I looked at projects such as **TinyFileManager**.

The idea was simple: if I could upload a full-featured file manager through the existing file-upload functionality, I could potentially use its file-management capabilities to further explore the environment without relying directly on system() or similar command-execution functions.

I uploaded one of the source-code files through the same PDF upload functionality.

The file was uploaded successfully and executed without any issues. I was then presented with the TinyFileManager login page.

The file manager could be accessed using the default credentials provided in the tool’s own source code. The actual credentials are not included in this public write-up.

After logging in, TinyFileManager was running normally and provided functionality such as viewing and managing files, deleting files, and accessing other files within the directories available to it.

At this point, even without obtaining direct OS Command RCE, I had gained a significant amount of access to the server’s file environment.

While continuing to review the application’s source code, I came across another file named db.php.

Since the original arbitrary file download vulnerability was still available, I downloaded that file as well.

The db.php file contained the credentials used by the application to connect to its database.

This gave me another important attack path:

Arbitrary File Download

↓

Source Code Disclosure

↓

db.php 

↓

Database Credential Disclosure

↓

Database Access

At this point, a standalone PHP database-management tool such as [**Adminer**](https://www.adminer.org/en/editor/) could also be used.

After uploading the PHP file and supplying the database username and password obtained from db.php, it was possible to connect to the database and perform various database-management operations, including creating a backup/dump of the database.

So even without relying on direct OS Command Execution, the original vulnerability had now led to:

It’s worth pointing out that the File Manager and Database Credential paths can also be considered separate branches of the attack chain.

In other words, reaching OS Command RCE wasn’t necessarily required to demonstrate significant impact.

One of the things I found particularly interesting during this assessment was that **getting RCE isn’t always the only way to increase the impact of a File Upload vulnerability.**

Sometimes a direct approach to command execution won’t work because of server configuration, application restrictions, or something like PHP’s disable\_functions.

That doesn’t necessarily mean the vulnerability becomes useless.

By looking at the application more carefully and thinking about what other capabilities are available, you may find alternative paths such as:

In this case, the entire chain started with a relatively simple **Arbitrary File Download** vulnerability. By reviewing the exposed source code and following the access paths it revealed, I was able to reach sensitive credentials, the admin panel, server-side file management, and database access.

For me, this was an important reminder:

***RCE isn’t always the goal. What matters is understanding what you can do with the access you’ve already gained and what other paths that access may open up.***

The issue was responsibly disclosed, and all sensitive information related to the target has been redacted from this write-up.
