# How i found xss in goverment website with one tools.

- **Source URL:** https://medium.com/@sulthanyluthfi/how-i-found-xss-in-goverment-website-with-one-tools-5dd5d431ed03?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241115093839/https://medium.com/@sulthanyluthfi/how-i-found-xss-in-goverment-website-with-one-tools-5dd5d431ed03
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7209 (id 7209)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
How i found xss in goverment website with one tools. XSS also cross site scripting is malicious script/code inject to trusted website. XSS can interact with the visitor’s browser without suspecting anything. When the script is executed, sensitive information such as passwords, credit card data, or other details that should be kept confidential can be accessed by the attacker.

I used xray tools to find the vurnerabilities. You can download in https://github.com/chaitin/xray/releases .

if you have downloaded it you must extract the file. After that you must find the website target. The syntax is :

./xray\_linux\_amd64 webscan — basic-crawler example@.com —plugins sqldet,xss,path-traversal — html-output example.html

— basic-crawler is simple script or tool used to browse and gather information from websites.

sqldet: This plugin is used for detecting SQL injection vulnerabilities.

xss: This plugin is used for detecting Cross-Site Scripting (XSS) vulnerabilities.

path-traversal: This plugin is used for detecting path traversal vulnerabilities, which occur when a web application allows users to access directories and files outside of the intended directory.

— html-output option is often used with command-line tools to specify that the output should be formatted as HTML.

I find the xss,after that click the url and inject the payload script to url.

tara i found the vulnerabilities.This vurnerabilites can impact:

1 . Data Theft: Session cookies or sensitive information can be stolen.

2\. Redirect to Malicious Site: Users are redirected to phishing sites.

3\. Web Page Modification: The web interface is altered to deceive users.

4\. Execution of Malicious Commands: Scripts can download malware.

5\. Admin Account Takeover: Full access to the site if an admin is targeted.

6\. Reputation Damage: Users lose trust in the website.

7\. Unauthorized Action Execution (CSRF): Attackers can change user data without permission.

This step for education. And i not responsibe.Follow me for more
