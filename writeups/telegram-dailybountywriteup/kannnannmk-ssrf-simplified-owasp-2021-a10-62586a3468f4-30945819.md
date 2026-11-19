# SSRF Simplified (OWASP 2021-A10)

- **Source URL:** https://medium.com/@kannnannmk/ssrf-simplified-owasp-2021-a10-62586a3468f4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501122412/https://medium.com/@kannnannmk/ssrf-simplified-owasp-2021-a10-62586a3468f4
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7383 (id 7383)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SSRF Simplified (OWASP 2021-A10)

SSRF is Server Side Request Forgery — By exploiting the vulnerabilities within internal server through external interface of a web or APIs.

How this can be exploited,

1. Sending Malicious request to the internal server from the vulnerable URL parameter or API parameter (GET or POST)
2. The malicious request contains the parameter added with a payload that represents the internal server location along with URI schema
3. Example: [http://localhost:80/file.txt,](http://localhost:80/file.txt,) [http://127.0.0.1/../../etc/passwd](http://127.0.0.1/../../etc/passwd), ftp://anonymous:anonymous@localhost:21/file.txt
4. This can provide you the content of the file either in the response or download the file if its through web browser

**Port Scanning:**

You can either create a malicious script to run a port scan on the server or by using Burp Suite Intruder to identify open ports within the vulnerable web server using SSRF attack

SSRF Port Scanning Sample Script [Attack-Automation-Scripts/SSRF-Port-Scan.py at main · kannnannmk/Attack-Automation-Scripts (github.com)](https://github.com/kannnannmk/Attack-Automation-Scripts/blob/main/SSRF-Port-Scan.py)

or you can use Burp Intruder module

This is one of the OWASP top 10 (A10) 2021,

**Prevention**:

There is no single step remediation applicable for SSRF just like SQL injection or XSS or any other vulnerability

1\. Removing unused URL schemas file://, SSH://, dict://, ftp://, gopher://, etc

2\. Ensure that URL parameters that may cause SSRF (Img\_url, consumeURL, etc) are only available for users with low privileged permissions in the server

3\. Proper authorization checks to be performed if the user wants to access sensitive data or configuration files (like password files, configuration files, etc) in the server via URL parameters

4\. Using IP address validator libraries to ensure there is no forged IP address in the request and only allow requests from trusted internal IP address sources (whitelisting), with input validation to prevent encoded / modified payloads containing special characters, like below

http://0000::1/

5\. Validate domain name and allow the requests only from trusted domains, using the DNS Resolver libraries available based on programming languages

6\. Implementing rate-limiting to prevent large number requests from randomly generated IP addresses trying to bypass filters

7\. Enabling server configurations that prevent port-scanning, to prevent SSRF based port scanning attacks.
