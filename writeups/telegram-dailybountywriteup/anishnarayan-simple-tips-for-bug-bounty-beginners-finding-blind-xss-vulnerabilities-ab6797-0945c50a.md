# Simple Tips for Bug Bounty Beginners

- **Source URL:** https://medium.com/@anishnarayan/simple-tips-for-bug-bounty-beginners-finding-blind-xss-vulnerabilities-ab67977ff756?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260210015509/https://medium.com/@anishnarayan/simple-tips-for-bug-bounty-beginners-finding-blind-xss-vulnerabilities-ab67977ff756
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5803 (id 5803)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Simple Tips for Bug Bounty Beginners: Finding Blind XSS Vulnerabilities

Among various vulnerabilities found in websites, Blind Cross-Site Scripting (XSS) is a significant threat that can quietly damage the security of web applications. But with the right knowledge and tools, we can successfully address Blind XSS and ensure the safety of our online systems.

**Understanding Blind XSS: The Silent Threat**

Blind XSS, also known as Persistent XSS or second-order XSS, happens secretively, executing payloads within web applications internally. Unlike reflected XSS, where payloads are immediately executed upon input, Blind XSS could remain dormant for a while before getting triggered. These payloads are stored within the application’s web server or other repositories and take their time before execution. It could take as little as 5 minutes or as long as 8 months for the XSS to get executed.

Stored XSS and Reflected XSS have a lot in common and the payloads can be used interchangeably but this is not the case with Blind XSS.

**Unveiling Blind XSS**

To begin with, we require certain URLs to test for Blind XSS which we can do using the following one-liner:

waybackurls site.com | grep “=” | qsreplace ‘“>\<script>confirm(1)\</script>’ | while read host do ; do curl — silent — path-as-is —…
