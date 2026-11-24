# HackTheBox — Web Attacks

- **Source URL:** https://medium.com/@harry.hphu/hackthebox-web-attacks-from-xxe-injection-to-advanced-local-file-disclosure-64d1bf5acdca?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240112050438/https://medium.com/@harry.hphu/hackthebox-web-attacks-from-xxe-injection-to-advanced-local-file-disclosure-64d1bf5acdca
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4552 (id 4552)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# HackTheBox — Web Attacks: From XXE Injection to Advanced Local File Disclosure

In my previous blog post, [HackTheBox — Web Attacks: From XXE Injection to Local File Disclosure](/@harry.hphu/hackthebox-web-attacks-xxe-injection-to-local-file-disclosure-c184b1ae4cbe), I went over how to use XXE Injection to read local files from the target machine. However, the technique used from the post is only applicable to web applications that use PHP. What happens if the target application does not use PHP? This blog post will go over another technique used to disclose local files.

To output data that does not conform to the XML format, we can wrap the content of the external file reference with a `CDATA` tag (e.g. `<![CDATA[ FILE_CONTENT ]]>`). This way, the XML parser would consider this part raw data, which may contain any type of data, including any special characters.

# Advanced Exfiltration with CDATA

## XML Parameter Entities

This is a special type of entity that starts with a `%` character and can only be used within the DTD (Document Type Definition). What's unique about parameter entities is that if we reference them from an external source (e.g., our own server), then all of them would be considered as external and can be joined, as follows:

`<!ENTITY joined "%begin;%file;%end;">`
We can store this in an `xxe.dtd` file that is hosted on attacking machine.

## Exploit the vulnerability

In Burp Suite, inject the XML entity payload that references to the `xxe.dtd` file hosted on attacking machine

From the above screenshot:

(1) — prepend the beginning of the CDATA tag

(2) — reference external file

(3) — append the end of the CDATA tag

(4) — reference our external DTD

(5) — reference the &joined; entity to print the file content

Once we send the request, we get the response on the right side, which displays the content of the requested file.

Using the same technique, we can obtain the flag in the `/flag.txt`

*HTB{3rr0r5\_c4n\_l34k\_d474}*
