# Simple Subdomain Takeover

- **Source URL:** https://infosecwriteups.com/simple-subdomain-takeover-15129e19bbb4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240123103226/https://infosecwriteups.com/simple-subdomain-takeover-15129e19bbb4
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4866 (id 4866)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Simple Subdomain Takeover

--

Writeup about how I successfully took over the subdomain.

***Subdomain takeover*** is a type of vulnerability where an attacker can take control of a subdomain that is pointing to an external service that is no longer in use or misconfigured. This can lead to phishing, malware distribution, defacement, or other malicious activities.


Below are the steps that led to a successful subdomain takeover; BTW this was just the random target I felt to check out and they have no Bug Bounty program or a RVDP.

1. Checked the main domain for any low hanging bugs but did not find any.

2\. Next, I enumerated subdomains of the target domain. Subdomains can sometimes reveal hidden or forgotten functionalities that may be vulnerable. For example, test.example.com may be a testing environment that is not properly protected or updated.

3\. There were only few subdomains, so I started to give an initial look at every subdomain, like visiting the subdomain, checking the Whois, DNS records and other such passive data to find any misconfigurations related to domain. For example, if a subdomain has a different Whois information than the main domain, it may indicate that it is owned by a different person or entity. If a subdomain has a DNS record that is pointing to an external service or domain name, it may indicate that it is using a third-party service or hosting provider.

4\. On one subdomain, blog.target.com, I noticed something strange. While looking at the DNS records, I saw that it had a CNAME record pointing to xyz.netlify.app. However, when I visited blog.target.com in the browser, I got a “Site not found” error. This indicated that the subdomain might be vulnerable to subdomain takeover due to a dangling CNAME record.

5\. To confirm it is actually vulnerable to takeover, I hosted a proof-of-concept site on Netlify and tried to take over the subdomain. To my surprise, it worked! I was able to take over the subdomain and display my own content on it.

Stay safe, stay informed, and keep coming back for more empowering insights.

Thank You for reading. Knowledge is power, so keep gaining!!
