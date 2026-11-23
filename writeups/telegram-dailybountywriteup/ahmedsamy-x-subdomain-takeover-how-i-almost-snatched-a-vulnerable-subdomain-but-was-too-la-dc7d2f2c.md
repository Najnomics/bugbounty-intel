# Subdomain Takeover

- **Source URL:** https://medium.com/@AhmedSamy-X/subdomain-takeover-how-i-almost-snatched-a-vulnerable-subdomain-but-was-too-late-c-a2a0afe7b2d9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250305091559/https://medium.com/@AhmedSamy-X/subdomain-takeover-how-i-almost-snatched-a-vulnerable-subdomain-but-was-too-late-c-a2a0afe7b2d9
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8955 (id 8955)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Subdomain Takeover: How I Almost Snatched a Vulnerable Subdomain (But Was Too Late!)**

*Hello Hackers,*

*This is my first write-up since I started my journey in bug hunting, as I haven’t been keen on publishing my findings before.*

*Let’s take it step by step.*

*Step 1: Identifying Our Target*

*For this demonstration, we will use example.com as our target. I started in the usual way by selecting a program to work on and initiated the recon process to gather subdomains.*

*I used various sources to collect subdomains, including:*

*Web-based tools:*

*Security Trails*

*Shrewdeye*

*Subfinder C99*

*Command-line tools:*

`subfinder -d example.com -all - recursive -o subs.txt``echo example.com | assetfinder - subsonly >> subs.txt`
*Step 2: Filtering and Removing Duplicates*

*Once the subdomain enumeration was complete, the next step was to filter the results and remove duplicates using anew:*

`cat subs.txt | anew >> allsubs.txt`
*Step 3: Identifying Vulnerable Subdomains*

*Now comes a crucial part — checking which subdomains have expired and can be taken over. The primary tools for this task are Subzy and Subjack. Personally, I prefer Subzy.*

*To run Subzy:*

`subzy run - targets allsubs.txt - hide_fails - vauln`
*⚠ Warning: If you find an Akamai subdomain listed as vulnerable, it’s likely a false positive due to their firewall mechanisms. Akamai is one of the trickiest firewalls to bypass in such cases.*

*Step 4: Verifying the Vulnerability*

*Once we identify a potentially vulnerable subdomain, we need to check its CNAME record to determine the hosting provider and confirm if it can be taken over.*

*Run the following commands to extract CNAME records:*

`dig example.com``dig +short example.com``host example.com``nslookup example.com`
*In my case, I found that the subdomain pointed to:*

*ghs.googlehosted.com*

*This indicates that the subdomain was previously hosted on Google Sites.*

*Step 5: Confirming Takeover Feasibility*

*To ensure the subdomain is truly vulnerable, I accessed example.com in a browser, which returned a 404 Page Not Found error.*

*Step 6: Claiming the Subdomain*

*Since I confirmed the vulnerability, I went to sites.google.com, registered the subdomain, and completed the verification process. After receiving the verification email, I created a simple HTML page and published it, successfully taking over the subdomain.*

*Final Steps: Reporting the Bug*

*After completing all the steps, I submitted a detailed report, including all steps taken and a full Proof of Concept (PoC) video. Unfortunately, the response was “Duplicate” — someone had reported the vulnerability just two days before me!*

*Thank you for reading this far.*

*This is just the beginning — many more vulnerabilities are waiting to be uncovered. Stay tuned!🔥*
