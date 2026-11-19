# A Beginner’s Guide to Testing for Server-Side Request Forgery (SSRF)

- **Source URL:** https://medium.com/@mcooter/a-beginners-guide-to-testing-for-server-side-request-forgery-ssrf-9a4b5e16fdd2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241213185122/https://medium.com/@mcooter/a-beginners-guide-to-testing-for-server-side-request-forgery-ssrf-9a4b5e16fdd2
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8168 (id 8168)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **A Beginner’s Guide to Testing for Server-Side Request Forgery (SSRF)**

In a few weeks, I’ll be taking the Offensive Security Web Assessor (OSWA) certification exam from Offensive Security. As part of my preparation, I’ve been diving deep into web vulnerabilities. One vulnerability on the exam and also something I see often in my day job as an application penetration tester, is Server-Side Request Forgery (SSRF). Writing about this vulnerability not only reinforces my understanding but also allows me to share insights with the community. Whether you’re a beginner or someone brushing up on SSRF, I am hoping you will find value in this guide.

# **What is SSRF?**

First off, what IS SSRF? Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to make a server perform unintended requests on their behalf.

These requests can target internal systems, external APIs, or even endpoints the attacker cannot directly access. The attacker’s goal is often to bypass network restrictions, access sensitive data, or escalate their attack.

Imagine a web app that fetches a profile picture from a URL. If the app doesn’t check the URL properly, an attacker could trick the server into fetching sensitive internal data, like [http://127.0.0.1/admin.](http://127.0.0.1/admin.)

# **What Are the Risks and Impact of SSRF?**

SSRF vulnerabilities can have severe consequences:

1. **Internal Network Access**: Attackers can access internal systems that are not exposed to the public, potentially compromising sensitive information or services.
2. **Sensitive Data Exposure**: SSRF can be used to access metadata endpoints in cloud environments (e.g., AWS’s [http://169.254.169.254/latest/meta-data/),](<http://169.254.169.254/latest/meta-data/),>) leading to the leakage of sensitive credentials.
3. **Port Scanning**: Attackers can use SSRF to identify open ports and services within the internal network.
4. **Code Execution**: In some cases, SSRF can be escalated to Remote Code Execution (RCE) if combined with other vulnerabilities.
5. **Denial of Service**: By abusing the server’s ability to make requests, attackers can perform DoS attacks against internal or external resources.

# **Detecting SSRF with Burp Suite and other tools**

Burp Suite is a powerful tool for detecting SSRF vulnerabilities. Here’s a step-by-step approach:

1. **Intercept Requests**:

- Configure Burp Proxy to intercept traffic between your browser and the web application.
- Look for parameters in the intercepted requests that accept URLs or user-controlled inputs, such as url, endpoint, callback, or redirect.

**2. Send to Repeater**:

- Right-click the identified request and send it to Burp Suite’s Repeater tool for manual testing.

**3. Insert Test Payloads**:

- Replace the parameter value with test URLs such as:
- [http://127.0.0.1](http://127.0.0.1) (internal loopback address)
- [http://169.254.169.254](http://169.254.169.254) (cloud metadata endpoint)
- A unique Burp Collaborator-generated URL
- Observe the server’s response for indications that the request was processed (e.g., specific error messages, timeouts, or redirects).

**4. Analyze Responses**:

- A successful SSRF may show a server response that includes content from the targeted resource, errors revealing server-side interactions, or an out-of-band interaction in the Collaborator client.

# **How to Test for SSRF**

Testing involves validating that the server processes and responds to crafted requests. Here are the steps to perform effective SSRF testing:

1. **Basic Testing**:

- Replace the parameter’s value with test URLs such as [http://example.com](http://example.com) to confirm that the server is making external requests.
- Monitor the server’s response for clues that it accessed the provided URL (e.g., status codes or headers).

**2. Out of band testing using Burp Collaborator, or a web server**:

- Generate a unique URL using Burp Collaborator and insert it into the parameter.

- Wait for an interaction notification from Collaborator, indicating the server accessed the URL.

If you do not have access to Burp, you can still test for out-of-band SSRF testing by spinning up a local web server, and using the IP address of the web server as the payload for the request(similiar to the Burp Collaborator example)

1. **Internal Scanning**:

- Test private IP ranges (127.0.0.1, 10.0.0.0/8, 192.168.0.0/16) to identify internal services the server can access.
- Example payloads:
- [http://127.0.0.1:80](http://127.0.0.1/)
- [http://192.168.1.1:8080](http://192.168.1.1:8080/)

**2. Headers Testing**:

- If URLs are not accepted directly, modify headers such as Host, X-Forwarded-Host, or Referer to include test payloads.
- Example: Add a header X-Forwarded-Host: 127.0.0.1.

**3. Time-Based Testing**:

- Use delayed responses (e.g., [http://example.com:8080?delay=10)](http://example.com:8080/?delay=10%29) to confirm if the server processes the request.
- Check for noticeable delays in the server’s response time.

**How to Exploit SSRF**

Exploitation takes testing a step further to achieve practical outcomes:

1. **Access Internal Services**:

- Use SSRF to reach internal admin panels, APIs, or other services behind a firewall.
- Example: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

**2. Cloud Metadata**:

- Exploit cloud environments by accessing metadata endpoints.
- Example: AWS metadata URL: [http://169.254.169.254/latest/meta-data/](http://169.254.169.254/latest/meta-data/)

**3. Port Scanning**:

- Use SSRF to identify open ports and services.
- Example payloads:
- [http://127.0.0.1:22](http://127.0.0.1:22/)
- [http://127.0.0.1:3306](http://127.0.0.1:3306/)

**4. Data Exfiltration**:

- Combine SSRF with other vulnerabilities to extract sensitive data, such as API keys or configuration files.

# **How to Remediate SSRF**

Preventing SSRF requires a combination of input validation and secure server configurations:

1. **Input Validation**:

- Validate and sanitize user input.
- Restrict input to a whitelist of safe URLs or domains.

**2. Network Segmentation**:

- Isolate sensitive internal resources from web-facing servers.

**3. Proper cloud service configuration** :

- Block access to cloud metadata endpoints unless explicitly required.
- Use Instance Metadata Service v2 (IMDSv2) in AWS for added security.

**4. Timeouts and Restrictions**:

- Set request timeouts and size limits.
- Restrict outbound requests to only necessary destinations.

It’s worth noting that while this guide covers the fundamentals of detecting and testing for SSRF vulnerabilities, there are several advanced techniques — such as alternate file protocols (FTP, Gopher), out-of-band (OOB) testing, SSRF bypasses, and other creative exploitation methods — that can uncover even more complex vulnerabilities. These techniques are important in comprehensive SSRF testing but fall outside the scope of this article. If there’s interest, I may dive deeper into these advanced topics in a future post.

Server-Side Request Forgery might sound intimidating at first, but with the right approach and tools, detecting, testing, and remediating SSRF becomes a straight forward process.

If you found this guide helpful, feel free to share it with others who are starting their journey into web application security. Happy Hunting!
