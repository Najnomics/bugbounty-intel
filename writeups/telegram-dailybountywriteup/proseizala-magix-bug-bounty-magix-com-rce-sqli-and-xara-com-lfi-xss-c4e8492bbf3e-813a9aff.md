# Magix Bug Bounty

- **Source URL:** https://medium.com/@proseizala/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss-c4e8492bbf3e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240717100934/https://medium.com/@proseizala/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss-c4e8492bbf3e?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6653 (id 6653)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Magix Bug Bounty: magix.com (RCE, SQLi) and xara.com (LFI, XSS)

# Learn More About Cyber Security , Hacking And Get Your First Certificate For Free On : [https://alison.com/tag/it-security?utm\_source=alison\_user&utm\_medium=affiliates&utm\_campaign=40731788](https://web.archive.org/web/20240717100934/https://alison.com/tag/it-security?utm_source=alison_user&utm_medium=affiliates&utm_campaign=40731788)

lets get started :

The German Magix Software GmbH rewarded me with a [Hall of Fame](https://web.archive.org/web/20240717100934/http://research.magix.com/) listing and a free Magix Music Maker 2014 Premium license for my reports of several serious security issues in the online infrastructures of magix.com and xara.com, which could be used to break both sites entirely:

At this point, I’d like to thank the Magix Security Team for their really fast and always transparent responses and the good coordination process as a whole. This is a perfect example of how the communication between the bug bounty operator and the researcher can satisfy both parties. The fixes for the critical vulnerabilities (RCE, SQLi, LFI) were implemented quite fast within only a few days after my initial report **(!)**, the fix for the XSS took a bit longer, but it’s still acceptable for a medium-severity issue.

Bug Bounty programs are always a great challenge and sometimes you’re rewarded with pretty cool stuff and great references like this — now here’s a short write-up about the discovered vulnerabilities, which already have been fixed by Magix.

# Remote Code Execution on europe.magix.com

This is the most dangerous flaw, I’ve found while working on this bug bounty program. I’ve discovered a script, that allows an attacker to upload zip files via a HTTP POST request. The script accepts any zip file, renames it to some temporary name and finally extracts the .zip file to a worker directory without checking if the zip file contains a valid file. Additionally, the extracted contents were accessible via www — I think the problem is quite obvious.

To prove the exploitability to Magix, I wrote a short Python script. The following snippet shows how the quite handy Python ZipFile function can be used to dynamically generate a zip file in memory. The .zip file contains one single file named “/tmp/test.php” with a custom PHP payload.

#!/usr/bin/python

**import** zipfile

**from** *StringIO* **import** StringIO

**import** zlib

inMemoryFile = StringIO()

zipFile = zipfile.ZipFile(inMemoryFile, ‘w’, zipfile.ZIP\_DEFLATED)

zipFile.writestr(‘./tmp/test.php’, ‘\<?php echo \”www.rcesecurity.com\"; ?>’)

zipFile.close()

In case of Magix, the target script echoes some additional (and hazardous) debugging output after POSTing an arbitrary zip file: looks like Magix missed to deactivate this output — without this I wouldn’t have probably found this flaw 🙂

Since the debugging output also discloses the full-path of the extracted file, this leads to a nice RCE condition:

Now imagine an attacker who’d upload some malicious C99…

# SQL Injection on europe.magix.com

This vulnerability is more or less based on the same condition like the previously described RCE flaw. If the zip file contains a specially prepared .ini file, the same script, that is responsible for the RCE flaw, uses the .ini values unfiletered in a SQL query:

# Local File Inclusion on downloadsv9.xara.com

A local file inclusion could become as dangerous as a RCE flaw, because an attacker may read sensitive system files like /etc/passwd:

…and if you’ve got a lazy sysadmin who likes to chmod 777 on files and directories, even more might by revealed 😉

# Cross-Site Scripting on downloadsv9.xara.com

OK — I promised not to write about a XSS in detail anymore, so I’ll leave you with the PoC screenshot:

A real happy day for bug bounty hunters and Magix!
