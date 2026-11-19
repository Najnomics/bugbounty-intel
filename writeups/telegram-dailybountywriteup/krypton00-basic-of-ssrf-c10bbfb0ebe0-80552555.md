# Basic of SSRF

- **Source URL:** https://medium.com/@Krypton00/basic-of-ssrf-c10bbfb0ebe0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142200/https://medium.com/@Krypton00/basic-of-ssrf-c10bbfb0ebe0
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3609 (id 3609)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Basic of SSRF

Hello There,

This is Sahil \[Krypton\] Who’s Cyber Security learner.

I am writing This blog to put my understanding on one of the Web application server side vulnerability hope so you will find it will.

(I am not content writer or creator so Kindly understand the mistakes )

So When I started my learning in web Appsec I start learning as per the below points mentioned:-

What is SSRF

Types of SSRF 

How to find and exploit SSRF

Exploit using url schemas accepted 

Bypasses of SSRF 

Impact of SSRF

My methodology

SSRF:-

SSRF stands for Server-Side Request Forgery. It’s a web vulnerability that allows attackers to manipulate the server into making unauthorized requests to internal or external resources. Here’s some information about

1\. Types of SSRF:

— Basic SSRF: The attacker directly manipulates the URL or parameter to trigger requests.

— Blind SSRF: The attacker doesn’t receive direct responses, making it harder to exploit.

— Time-Based SSRF: The attacker uses time delays to infer the success of requests.

— DNS Rebinding SSRF: The attacker abuses DNS resolution to bypass restrictions.

2\. How to find and exploit SSRF:

— Manual Testing: Manually inspect the application for URLs or parameters vulnerable to SSRF.

— Automated Scanning: Use SSRF-specific scanning tools to identify potential vulnerabilities.

— Exploitation: Modify the URL or parameter to access internal resources or sensitive data.

3\. Exploit using protocols accepted:

— HTTP/HTTPS: Access other web applications and services.

— File: Read local files from the server.

— gopher: Communicate with Gopher servers.

— ftp: Access files on FTP servers.

— dict: Query dictionary servers.

— ldap: Access LDAP servers.

4\. Bypass techniques for SSRF:

— IP Whitelisting: Attackers can bypass SSRF by using IP addresses instead of domain names.

— URL Encoding: Malicious URLs may be encoded to avoid detection.

— Firewall Evasion: Use techniques like DNS rebinding to bypass firewalls.

5\. Impact of SSRF:

— Unauthorized Data Access: Attackers can access sensitive information stored on internal systems.

— Service Disruption: SSRF attacks can disrupt internal services or even the application itself.

— Security Bypass: By accessing internal APIs, attackers might bypass authentication mechanisms

.Scan the network for hosts,Port scan internal machines and fingerprint internal services,

collect instance metadata,

bypass access controls

leak confidential data
