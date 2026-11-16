# Blind XSS To SSRF

- **Source URL:** https://akashc99.medium.com/blind-xss-to-ssrf-e2bc579976d?source=rss------bug_bounty-5
- **Fetched from:** https://akashc99.medium.com/feed
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 1553)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
During bug hunting in a private bug bounty program, I came across a feature within the application that allowed for the generation of PDF documents. Since the user input was reflected in the generated PDF documents, I decided to try injecting HTML and XSS payloads.

I used a well-known tool called XSSHunter, which allows us to find blind cross-site scripting vulnerabilities.To my surprise, my payload was immediately executed and I was able to retrieve the screenshot and the following details on XSSHunter.

Further investigation revealed that the payload had been executed on the file path

Gotenberg is an open-source API for converting HTML, Markdown, and Office documents to PDF. It uses a set of configurable rendering engines to convert the input document to a PDF file. The Gotenberg parser is the component of Gotenberg that takes the input document and converts it into a format that can be rendered by the engines.

Upon further testing, I discovered that the Gotenberg parser was vulnerable to server-side request forgery attacks. I was able to successfully execute a payload that included an iframe with the src set to “file:///etc/passwd”. This allowed me to view the contents of the “/etc/passwd” file.

This type of vulnerability allows an attacker to access sensitive files on a server by manipulating the file path in a way that allows them to traverse the file system. This can potentially lead to the exposure of sensitive information and even complete system compromise.

I immediately reported my findings to the security team, who classified the vulnerability as high. However, another security researcher had also reported the vulnerability at the same time. As a result, the team decided to split the bounty and I received $500.

The XSS Hunter has been deprecated and is no longer in use. A new version has been launched by Truffle Security, available at https://xsshunter.trufflesecurity.com.
