# Web Security Short Series — XXE

- **Source URL:** https://medium.com/@frankyyano/web-security-short-series-xxe-64492ed1d893?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240605203138/https://medium.com/@frankyyano/web-security-short-series-xxe-64492ed1d893
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5646 (id 5646)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**XXE is the attack to XML** parser where weakly configured XML parser, trusts the XML input coming from the client and parses the external entities back to the response. Which may lead to exfiltration of data.

XXE can also lead to SSRF in poorly configured web application servers.

XML external entity injection (XXE) basically allows an attacker to interfere with an application’s processing of XML data.

An attacker could essentially be able to view files on the application server filesystem, and even interact with any back-end or other connected external systems.

All an attacker has to do is inject a system command within the vulnerable XML code block.

In some situations, with the correct payload, an attacker can upload a malicious reverse shell payload on the target, and obtain a system level shell, creating persistence on the server.

The below illustration shows an XXE attack flow to read files on the target system.

**What are the types of XXE attacks?**

1. **Exploiting XXE to retrieve files** — Files are displayed in an application’s response. The below payload would retrieve the /etc/passwd file from the server.

2\. **Exploiting XXE to perform SSRF attacks**.

3. **Exploiting blind XXE exfiltrate data out-of-band**. Since external entities can reference resources on other servers, we can use entities to access other servers in a *server-side request forgery* (SSRF) attack or as a means to exfiltrate data back to a server we control.

When an application parses this type of external entity, it will send a GET request to the specified URL. This is typically how SSRF works, and can give an attacker access to private enpoints in the network.

4\. **Exploiting blind XXE to retrieve data via error messages**. An attacker can trigger a parsing error message containing sensitive data.

More reading and Labs:

I hope you enjoy this piece!
