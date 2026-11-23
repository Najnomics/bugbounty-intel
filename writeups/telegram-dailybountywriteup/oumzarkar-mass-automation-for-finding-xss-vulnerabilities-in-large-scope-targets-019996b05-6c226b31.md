# Mass automation for finding XSS vulnerabilities in large scope targets

- **Source URL:** https://medium.com/@oumzarkar/mass-automation-for-finding-xss-vulnerabilities-in-large-scope-targets-019996b0515c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240603063132/https://medium.com/@oumzarkar/mass-automation-for-finding-xss-vulnerabilities-in-large-scope-targets-019996b0515c
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5799 (id 5799)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# *Mass automation for finding XSS vulnerabilities in large scope targets*

*Mass automation for finding vulnerabilities in large scope targets can be a esay getway to find multiple bugs on multiple websites faster and in less time. If you’ve been struggling to find bugs on platforms like HackerOne and want to explore alternative avenues, government websites under programs like NCIIPC RVDP can offer a wide scope for discovery.*

Here’s a refined strategy:

1. Discovering Target Domains: Utilize tools like Assetfinder to discover government domains. You can leverage pre-made lists available online for efficiency. For instance:

`assetfinder gov.in >> urls.txt`
Consider using curated lists from trusted sources, such as:

2\. Finding Live Hosts: After acquiring the target domains, determine which ones are live using tools like Httpx:

`httpx -l urls.txt`
This step ensures you focus your efforts on active websites, saving time and resources.

3\. Discovering Endpoints: Utilize tools like Katana to discover as many endpoints as possible within the live hosts:

`katana -u livehosts -o endpoints.txt`
This step helps in expanding your attack surface and increases the chances of discovering vulnerabilities.

4\. XSS Vulnerability Testing: Finally, employ XSS testing tools like XSS\_Vibes to scan the discovered endpoints for vulnerabilities. You can clone the tool from its GitHub repository:

`python3 main.py -f endpoints.txt -o vulnerabilities.txt -t 10`
This command initiates the XSS scanning process with a specified thread count for efficiency.

you can insert more payloads in payloads.json to improve its findings

5\. Reporting and Follow-Up:

I actually discovered simple XSS vulnerabilities in a government website using this strategy:

1. Reflected XSS

2\. DOM XSS

These vulnerabilities were reported, and they no longer exist. Additionally, I received an acknowledgment email from NCIIPC for finding these vulnerabilities.

# PS UPDATE :

I have made an Integration script that does all this in one go and utilizes maximum available resources to find xss vulnerabilities faster

[https://github.com/oumzarkar/MassXssAutomator.git](https://github.com/oumzarkar/MassXssAutomator)

This is a simple easy to use script that can help you to find bugs efficiently in large scope targets
