# 750$ in 5 Minutes - XXE to LFI

- **Source URL:** https://skramthu.medium.com/750-in-5-minutes-xxe-to-lfi-897bca9c304c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240924030931/https://skramthu.medium.com/750-in-5-minutes-xxe-to-lfi-897bca9c304c?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7351 (id 7351)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello everyone! Welcome back to my blog. It took me just 5 minutes to find this and 1 hour to triage it. This has been my quickest discovery and bounty!

I received a private invite from one of the programs. I checked the scope and noticed that it had a wildcard scope. I ran Subfinder and Httpx to collect more subdomains, and I also used DNS brute-forcing and vhost discovery tools to enumerate a large number of subdomains.

If you want more subdomains, simply run Subfinder again with the subdomains it generated. Use the commands below to create a good list of subdomains:

`subfinder -d domain.com -silent -all | httpx -p 80,443,8443 | tee subs.txt``subfinder -dL subs.txt -all -silent | httpx -p 80,443,8443 | tee moresubs.txt`
After enumerating all the subdomains, I ran a CVE scan in Nuclei using the command below:

`nuclei -l subs.txt -tags cve,exposure,panel -es low,info -rl 60 -nmhe` Within 5 minutes of time i got a CVE !

At first, I thought it might be a false positive, but later I checked for the proof of concept (PoC) for that particular CVE on GitHub and found an exploit.

I checked the CVE against the affected domain and found a Local File Inclusion (LFI) vulnerability.

I immediately reported the finding and, after one hour, received a message with the triage results and bounty information.

Clap if you learned something! Follow me for more blogs like this, and connect with me on LinkedIn.

[https://www.linkedin.com/in/ramthullaguduru](https://web.archive.org/web/20240924030931/https://www.linkedin.com/in/ramthullaguduru)

Bye for now!
