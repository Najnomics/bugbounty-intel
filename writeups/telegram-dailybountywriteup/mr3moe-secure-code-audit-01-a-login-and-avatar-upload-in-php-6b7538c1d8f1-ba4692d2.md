# Secure Code Audit 01

- **Source URL:** https://medium.com/@Mr3Moe/secure-code-audit-01-a-login-and-avatar-upload-in-php-6b7538c1d8f1
- **Fetched from:** https://medium.com/@Mr3Moe/secure-code-audit-01-a-login-and-avatar-upload-in-php-6b7538c1d8f1?source=rss-3866ea38ddcc------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14976 (id 14976)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mr3Moe / Tue, 10 Nov 2026 01:24:00 GMT

This PHP file has security bugs. By the end of this post you will know how to spot every one of them, how an attacker would use it, and how to fix it.

Welcome to **Secure Code Audit**, a series where we read real-looking code like an attacker does. Each post follows the same steps:

Try to find the bugs yourself before you read the audit. Count how many you find, then compare.

The target is account.php, a small page from a community forum. It does three jobs:

The line numbers on the left are added for this post. They are not part of the code.

01  \<?php

02 session\_start();

03 $conn = mysqli\_connect("localhost", "root", "root123", "forum");

04

05 if (isset($\_POST\['login'\])) {

06 $user = $\_POST\['username'\];

07 $pass = md5($\_POST\['password'\]);

08 $sql = "SELECT \* FROM users WHERE username = '$user' AND password = '$pass'";

09 $res = mysqli\_query($conn, $sql) or die(mysqli\_error($conn));

10 if (mysqli\_num\_rows($res) > 0) {

11 $\_SESSION\['user'\] = $user;

12 echo "Welcome back, " . $user;

13 } else {

14 echo "Login failed for " . $\_POST\['username'\];

15 }

16 }

17

18 if (isset($\_FILES\['avatar'\]) && isset($\_SESSION\['user'\])) {

19 $name = $\_FILES\['avatar'\]\['name'\];

20 move\_uploaded\_file($\_FILES\['avatar'\]\['tmp\_name'\], "uploads/" . $name);

21 echo "Avatar saved: \<img src='uploads/$name'>";

22 }

23

24 if (isset($\_GET\['view'\])) {

25 include("pages/" . $\_GET\['view'\]);

26 }

Stop here and make your own list before reading on.

The most dangerous bugs are on lines 8, 20 and 25: each one alone can take over the app. We go in order from top to bottom.

The password sits in the source code, and the app connects as root, the most powerful database user.

**Attack:** Anyone who reads the source (a leaked Git repo, a account.php.bak backup, or the file-read bug on line 25) gets the password.

**Impact:** Full control of every database on the server, not just the forum.

MD5 is fast and unsalted. Two users with the same password get the same hash.

**Attack:** If the users table leaks (see line 8), the hashes crack with a GPU and a wordlist. Common passwords fall in seconds.

**Impact:** Plain-text passwords, which users often reuse elsewhere.

$user comes straight from the request and is pasted into the SQL string. The attacker can close the quote and write their own SQL. Send this username with any password:

admin'-- -

The query becomes ... WHERE username = 'admin'-- -' AND password = '...'. Everything after -- is a comment, so the password check disappears.

**Impact:** Log in as any user with no password. With UNION SELECT, dump the whole database.

or die(mysqli\_error($conn)) prints the raw database error to the page.

**Attack:** The attacker breaks the query on purpose and reads the error to learn table and column names. This makes the line 8 injection much faster.

**Impact:** Leaks the database structure and helps every other attack.

Both lines echo the username back to the page with no encoding. Line 14 echoes it even when login fails, so no account is needed.

This is reflected from a POST, so the attacker cannot just send a link. Delivery works like this:

This works because there is no CSRF token and no SameSite cookie to block the cross-site POST.

**Impact:** Run script in the victim’s browser on this site steal their session cookie or phish them. Rated Medium because POST delivery is harder than a plain GET link.

move\_uploaded\_file saves the file under its original name, into a web folder, with no check on type or extension. The name comes straight from the attacker.

**Attack:** Upload a file named shell.php holding \<?php system($\_GET\['c'\]); ?>. Then run it one of two ways:

The name is also unchecked for ../, so the file can be written outside the uploads folder.

**Impact:** Remote code execution the attacker runs commands on the server. This is the worst bug in the file.

$\_GET\['view'\] is passed to include() with no check. PHP runs whatever file it points to.

**Attack**: Request ../../..//etc/passwd to read system files, or combine with the line 20 upload: ?view=../uploads/shell.php to run the uploaded shell even if the uploads folder blocks direct PHP.

**Impact:** Read any file on the server (including the line 3 password), or run attacker-controlled code.
