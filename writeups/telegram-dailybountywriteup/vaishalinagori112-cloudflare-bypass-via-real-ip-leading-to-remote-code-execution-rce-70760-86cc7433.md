# Cloudflare Bypass via Real IP Leading to Remote Code Execution (RCE)

- **Source URL:** https://medium.com/@vaishalinagori112/cloudflare-bypass-via-real-ip-leading-to-remote-code-execution-rce-7076015085df?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260510021032/https://medium.com/@vaishalinagori112/cloudflare-bypass-via-real-ip-leading-to-remote-code-execution-rce-7076015085df?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13525 (id 13525)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Cloudflare Bypass via Real IP Leading to Remote Code Execution (RCE)

## Introduction

Cloudflare is widely used to protect web applications against attacks such as XSS, SQL injection, and DDoS. It acts as a reverse proxy, filtering malicious traffic before it reaches the origin server.

But what if an attacker never goes through Cloudflare at all?

This blog walks through a real-world scenario where me and were able to bypassed Cloudflare protections via identifying and directly interacting with the origin server.

## Understanding the Protection Mechanism

When a website is behind Cloudflare:

- Traffic is routed through Cloudflare
- The real server IP is hidden
- Malicious payloads are filtered by WAF rules

This means attacking via the domain is often ineffective.

## Step 1: Initial Testing (Blocked by Cloudflare)

During testing, multiple payloads were attempted:

- XSS
- SQL Injection

All requests were blocked, confirming that Cloudflare WAF protections were active.

## Step 2: Reconnaissance — Identifying the Origin IP

The next step was to determine whether the origin server was truly hidden.

Using reconnaissance techniques such as Shodan , we identified a potential real IP address of the target server.

## Validating the Origin IP

To confirm whether the discovered IP belonged to the target:

- Enter the IP address along with the required port in the browser, and it redirects to the original website.

This confirmed that the IP was indeed the origin server.

## Step 3: Bypassing Cloudflare

Instead of interacting with the protected domain, we directly targeted the origin IP.

This completely bypassed Cloudflare protections, as requests no longer passed through its filtering layer.

## Step 4: Port Scanning & Service Discovery

An Nmap scan on the origin IP revealed an open port exposing an additional service.

This service turned out to be:

*A documentation portal not visible on the main application*


## Step 5: Default Credentials Exposure

Upon accessing the documentation portal:

- A login interface was present
- The portal accepted **default credentials**

Using these default credentials, we successfully gained access.

## Step 6: Post-Login Enumeration

After logging in, further exploration revealed:

- A file upload functionality within the portal

## Step 7: Exploiting File Upload

The upload feature lacked proper validation controls.

This allowed:

- Uploading a malicious PHP file
- Executing it on the server

## Step 8: Achieving Remote Code Execution

Once the file was uploaded:

- It was triggered through the browser
- A reverse shell connection was established

Result:

*Remote Code Execution (RCE) on the server*


## Root Cause Analysis

This was a chained exploitation involving multiple weaknesses:

1. Origin IP exposure
2. No restriction on direct access to origin server
3. Open port exposing internal service
4. Use of default credentials
5. Insecure file upload handling

## Key Takeaways

## 1. Cloudflare is Not Enough

It only protects traffic routed through it.

## 2. Restrict Origin Server Access

- Allow only Cloudflare IP ranges
- Block all direct public access

## 3. Never Use Default Credentials

- Always enforce credential changes
- Implement strong authentication policies

## 4. Minimize Attack Surface

- Do not expose internal services publicly
- Use proper network segmentation

## 5. Secure File Uploads

- Validate file types and content
- Disable execution permissions in upload directories

## 6. Never Assume Internal Means Safe

Never assume that an internal or less-visible portal is secure just because it’s not publicly linked. You never know when or how a data breach might occur. Even small misconfigurations or overlooked exposures can become entry points for attackers and eventually lead to a full compromise.

## Conclusion

This case highlights a critical reality:

*Security controls are only effective if they cannot be bypassed.*


Even with Cloudflare properly configured, exposing the origin server made the entire protection layer ineffective.

## Final Thoughts

Most breaches don’t happen because defenses fail — they happen because something was left exposed.

In this case, it wasn’t Cloudflare that was weak, it was everything around it.
