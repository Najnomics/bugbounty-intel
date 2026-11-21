# The Complete Guide to PHP Functions That Can Cause Local File Inclusion (LFI) Vulnerabilities…

- **Source URL:** https://medium.com/@zoningxtr/the-complete-guide-to-php-functions-that-can-cause-local-file-inclusion-lfi-vulnerabilities-7e1115ece1ea?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905080922/https://medium.com/@zoningxtr/the-complete-guide-to-php-functions-that-can-cause-local-file-inclusion-lfi-vulnerabilities-7e1115ece1ea
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9875 (id 9875)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🔍🧠 The Complete Guide to PHP Functions That Can Cause Local File Inclusion (LFI) Vulnerabilities 🚨💣

*Explore the complete guide to PHP functions that can lead to Local File Inclusion (LFI) vulnerabilities 🚨💣. Learn which functions are risky, how attackers exploit them, and security best practices.*

D*isclaimer: This content is for educational purposes only. The author is not responsible for any use or misuse of the information provided. You are solely responsible for your actions. Always act ethically and ensure you have proper authorization.*

Local File Inclusion (LFI) vulnerabilities are among the most dangerous and common web application flaws — especially in **PHP-based websites**. If exploited, they can allow attackers to read sensitive files, gain remote code execution (RCE), or escalate privileges.

In this post, you’ll learn:

- 🧩 What causes LFI in PHP
- ⚙️ The **PHP functions most commonly associated** with LFI
- 🧪 Examples of vulnerable usage
- 🛡️ How to prevent each scenario effectively

## 📌 What is Local File Inclusion (LFI)?

LFI occurs when a web application uses **user-supplied input to build file paths**, which are then loaded or executed by the server. If that input is not properly validated, an attacker can manipulate it to access unintended files on the system.

## ⚠️ PHP Functions That Can Lead to LFI

Here are the most dangerous PHP functions that can result in LFI vulnerabilities:

## 1. `include()` / `include_once()`

🔁 Includes a file during runtime.

### ❌ Vulnerable Example:

`php````
<?php
$page = $_GET['page'];
include("pages/" . $page . ".php");
?>
```
### 🛡️ Mitigation:

Use a whitelist:

`php````
$allowed = ['home', 'about', 'contact'];
if (in_array($_GET['page'], $allowed)) {
    include("pages/" . $_GET['page'] . ".php");
}
```
- Sanitize and validate input.
- Avoid dynamic inclusion if possible.

## 2. `require()` / `require_once()`

🚨 Same behavior as `include()` but causes fatal error if file is missing.

### ❌ Vulnerable Example:

`php``require($_GET['template']);`
### 🛡️ Mitigation:

- Same strategies as `include()`
- Avoid dynamically building file paths

## 3. `file_get_contents()`

📥 Reads a file into a string.

### ❌ Vulnerable Example:

`php````
$file = $_GET['doc'];
echo file_get_contents("documents/" . $file);
```
### 🛡️ Mitigation:

`php````
$allowed_files = ['terms.txt', 'privacy.txt'];
if (in_array($_GET['doc'], $allowed_files)) {
    echo file_get_contents("documents/" . $_GET['doc']);
}
```
## 4. `fopen()`, `readfile()`, `file()`, `fpassthru()`, etc.

📂 Functions that handle file I/O can also be dangerous if user input is not validated.

### ❌ Vulnerable Example:

`php``$f = fopen($_GET['file'], "r");`
### 🛡️ Mitigation:

- Always validate file names
- Block directory traversal (`../`)
- Disable URL wrappers when not needed

## 5. `highlight_file()` / `show_source()`

🔍 Shows the source code of a file. Useful for debugging, but dangerous in production.

### ❌ Vulnerable Example:

`php``highlight_file($_GET['source']);`
### 🛡️ Mitigation:

- Remove such debug features in production
- Use static values or whitelist

## 💣 Exploitation Scenarios

## 🔓 Directory Traversal

`?page=../../../../etc/passwd`
## 🧪 LFI to RCE via Log Poisoning

Inject PHP code in a User-Agent:

`php``User-Agent: <?php system($_GET['cmd']); ?>`
Then access the log:

`bash``?page=../../../../var/log/apache2/access.log&cmd=id`
## 🚫 Common Mistakes That Lead to LFI

❗ Accepting raw input in file functions

❗ Not sanitizing input

❗ Assuming `.php` extension or path is safe

❗ Using `basename()` without validation

## 🛡️ General Mitigation Checklist ✅

## 🔐 PHP Config-Level Hardening

In `php.ini`:

`ini````
allow_url_include = Off
allow_url_fopen = Off
open_basedir = /var/www/html/
```
These settings **limit file inclusion** and access to specific directories.

## 🧠 Summary

## ✍️ Final Words

Local File Inclusion vulnerabilities are **easy to overlook but extremely dangerous**. By understanding the PHP functions that cause them, and how to secure them, you can significantly reduce your application’s risk.

🧠 Whether you’re a **bug bounty hunter**, **security analyst**, or **PHP developer**, mastering LFI gives you an edge in both attacking and defending systems.
