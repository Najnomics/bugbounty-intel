# Remote code Execution

- **Source URL:** https://medium.com/@roshiniyathakula/remote-code-execution-9b2e9f26963d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241003173006/https://medium.com/@roshiniyathakula/remote-code-execution-9b2e9f26963d
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7419 (id 7419)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Remote code Execution

Hi✋, I’m Roshini, a passionate cybersecurity researcher dedicated to uncovering the latest in digital security. I focus on identifying vulnerabilities and developing strategies to enhance protection. In this blog, I’ll share my knowledge and experiences to help defend against cyber threats. Join me as we navigate the evolving challenges of safeguarding our digital world!

**What is Remote Code Execution (RCE)?**

Remote Code Execution (RCE) through file upload occurs when an attacker uploads a malicious file, such as a script, to a vulnerable server. Once uploaded, the file gets executed, allowing the attacker to run arbitrary code on the server. This usually happens due to poor validation or sanitization of file inputs, including allowing dangerous extensions like .php or .exe. Once attackers gain control, they can escalate privileges, exploit further vulnerabilities, or even take control of the entire server. Mitigations include validating file types, storing files outside the webroot, and disabling execution permissions in upload directories.

**Impact:**

The consequences of RCE via file upload can be devastating. Attackers can seize complete control of the server, resulting in data theft, defacement, or deletion of key files. They can escalate privileges, install malware, or set up backdoors for future access. A compromised server can also be used to attack other systems, disrupt services, or steal sensitive data, leading to financial, reputational, and operational damage to the organization.

**Practical Demonstration:**

***Step 1:*** Write a malicious JSP code and upload it to the server.

***Step 2:*** Access the file and run the WHOAMI command to verify the server’s response.

Step 3: Start an ncat listener in AWS.

Step 4: Send a PowerShell command to obtain a reverse shell. Once done, we can control the application server.

**Mitigation:**

To prevent RCE through file uploads, follow these best practices:

➢Enforce strict file type validation by checking both MIME types and file extensions.

➢Store uploaded files outside the webroot and disable execution permissions in the upload directory.

➢Use secure file naming conventions, generating random names instead of relying on user input.

➢Sanitize all inputs and remove potentially dangerous content.

➢Implement server-side security measures such as web application firewalls (WAFs) and intrusion detection systems (IDS).

**References:**

[https://www.baeldung.com/cs/rce-security](https://www.baeldung.com/cs/rce-security)

I hope you all understand what is RCE and how does it works and how to mitigate. Stay tuned on my next coming blog. Don’t forget to share read follow.

Bye🙋♀️……………See you guys in next blog.

Happy reading……….!!!
