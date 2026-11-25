# Path Traversal and RCE in Online Compilers

- **Source URL:** https://medium.com/@amal_n47h/path-traversal-and-rce-in-online-compilers-454a446effca?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240614053255/https://medium.com/@amal_n47h/path-traversal-and-rce-in-online-compilers-454a446effca?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6391 (id 6391)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Path traversal**, also known as directory traversal, is a security vulnerability that allows an attacker to access files and directories stored outside the web root folder. By manipulating variables that reference files, attackers can navigate to parent directories and access restricted files.

**Remote Code Execution** (RCE) is a severe security vulnerability that allows an attacker to execute arbitrary code on a target system from a remote location. This can happen if an application improperly handles user inputs, enabling the attacker to inject malicious code that the server then executes.

Recently, while exploring an online JavaScript compiler, I discovered it accepts the `fs` (file system) module. Out of curiosity, I tried to read system files with a simple script:

function listFilesInDirectory() {

fs.readFile(‘/etc/passwd’, ‘utf8’, (e,data) => {

console.log(data)})}


It worked. I could read the contents of `/etc/passwd`.

I reported this security issue, but it turned out to be a duplicate, and the issue still wasn’t patched.

I then realized that many online compilers run in virtual environments, meaning this vulnerability might not be as critical as I initially thought. So, I set out to find a more impactful vulnerability such as RCE.

Unfortunately, I couldn’t find any RCE flaws in the JavaScript compilers I tested. So, I switched my focus to online Python compilers. I found that many of them allow importing the `os` module. I tried running arbitrary commands using this script:

import os 

print(os.popen(‘cat /etc/passwd).read())


This script successfully displayed the contents of `/etc/passwd`. I then tested it on various online Python compilers I found through a quick Google search. Surprisingly, 9 out of 11 compilers were vulnerable, and I was even able to get a reverse shell on those systems.

The widespread vulnerability across these platforms highlights a significant security concern that needs to be addressed. However, many companies don’t view this as a major security issue.
