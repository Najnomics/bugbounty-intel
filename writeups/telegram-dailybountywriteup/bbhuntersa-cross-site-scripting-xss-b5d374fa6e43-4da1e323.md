# What is Cross-Site Scripting (XSS)?

- **Source URL:** https://medium.com/@bbhuntersa/cross-site-scripting-xss-b5d374fa6e43?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240603233042/https://medium.com/@bbhuntersa/cross-site-scripting-xss-b5d374fa6e43
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5672 (id 5672)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## Cross-Site Scripting (XSS)

# What is Cross-Site Scripting (XSS)?

## Cross-Site Scripting, commonly known as XSS, is a security vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. These malicious scripts can then perform various harmful activities, such as stealing sensitive data, session hijacking, and spreading malware. XSS attacks are prevalent and pose a significant threat to web application security.

# Types of XSS Attacks

## Stored XSS

In a Stored XSS attack, the malicious script is permanently stored on the target server, typically in a database. When a user visits the affected web page, the malicious script is executed, leading to potential data theft or unauthorized access. This type of XSS attack is particularly dangerous as it can affect multiple users who access the compromised web page.

## Reflected XSS

Reflected XSS attacks occur when the malicious script is embedded in the URL. When a user clicks on a malicious link containing the script, the script is executed, but it is not stored on the server. This type of XSS attack is often used in phishing campaigns and requires user interaction to execute the malicious script.

## DOM-based XSS

DOM-based XSS attacks exploit vulnerabilities in the Document Object Model (DOM) of the victim’s browser. The malicious script is executed as a result of modifying the DOM, and it runs within the context of the victim’s browser. This type of XSS attack is challenging to detect and mitigate, making it a preferred choice for attackers targeting modern web applications.

`<script>alert(1)</script>`
