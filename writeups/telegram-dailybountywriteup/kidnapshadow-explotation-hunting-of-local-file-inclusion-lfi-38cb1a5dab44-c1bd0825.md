# EXPLOTATION / HUNTING OF LOCAL FILE INCLUSION (LFI)

- **Source URL:** https://medium.com/@kidnapshadow/explotation-hunting-of-local-file-inclusion-lfi-38cb1a5dab44?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221231040913/https://medium.com/@kidnapshadow/explotation-hunting-of-local-file-inclusion-lfi-38cb1a5dab44
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/957 (id 957)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# EXPLOTATION / HUNTING OF LOCAL FILE INCLUSION (LFI)

— — — — — — — — — —— — — KIDNAPSHADOW — — — — — — — -— — — — — — — —

#1 What do You Means by Local File Inclusion (LFI) ?

— → LFI is a web vulnerability caused by mistakes made by a programmer of a website or web application. If an LFI vulnerability exists in a website or web application, an attacker can include malicious files that are later run by this website or web application.

#2 How Dangerous is LFI?

— → LFI can be dangerous, especially if combined with other vulnerabilities — for example, if the attacker is able to upload malicious files to the server. Even if the attacker cannot upload files, they can use the LFI vulnerability together with a directory traversal vulnerability to access sensitive information.

#3 How To Hunt Local File Inclusion (LFI) Bug

(i) you have to find a parameter that include some local file

example :- you can scan testphp.vulnweb.com

The following is an example of PHP code that is vulnerable to LFI.

```
/**
* Get the filename from a GET input
* Example - http://example.com/?file=filename.php
*/
$file = $_GET['file'];
```
```
/**
* Unsafely include the file
* Example - filename.php
*/
include('directory/' . $file);
```
In the above example, an attacker could make the following request. It tricks the application into executing a PHP script such as a web shell that the attacker managed to upload to the web server.

`http://example.com/?file=../../uploads/evil.php`
a) Open burp suite and spider your host and check parameter that include some file and document with extension pdf, php file, doc file and etc.

[http://example.com/?file=../../../../etc/passwd](http://example.com/?file=../../../../etc/passwd)

If you want to find local file inclusion (lfi) with automation with burpsuite

then you need a lfi payload

#4 How to detect LFI ?

The most efficient way to detect LFI is by using an automated vulnerability scanner. You can of course detect such vulnerabilities through manual penetration testing but it takes a lot more time and resources.

#5 How to avoid LFI?

To avoid LFI and many other vulnerabilities, never trust user input. If you need to include local files in your website or web application code, use a whitelist of allowed file names and locations. Make sure that none of these files can be replaced by the attacker using file upload functions.

Thank for reading the blog 💕❤

written by kidnapshadow

follow for more hacking related blog and also follow on youtube (kidnapshadow)
