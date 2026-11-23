# Server-Side Request Forgery (SSRF)

- **Source URL:** https://seclak07.medium.com/server-side-request-forgery-ssrf-detection-impact-and-defense-bypass-techniques-71787fe52db1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251231212350/https://seclak07.medium.com/server-side-request-forgery-ssrf-detection-impact-and-defense-bypass-techniques-71787fe52db1
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/12092 (id 12092)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Server-Side Request Forgery (SSRF): Detection, Impact, and Defense Bypass Techniques

Server-Side Request Forgery (SSRF) is a critical web application vulnerability that is frequently misunderstood but highly impactful when exploited. This article explains **what SSRF is**, **how to identify it**, and **how common defenses are bypassed in real-world scenarios**.

## What Is SSRF (Server-Side Request Forgery)?

SSRF stands for **Server-Side Request Forgery**. It is a vulnerability that allows an attacker to manipulate a web application into making **unauthorized or attacker-controlled HTTP requests** from the server itself.

Instead of the attacker directly accessing internal resources, the **server becomes the proxy**, issuing requests on the attacker’s behalf.

## Types of SSRF Vulnerabilities

SSRF vulnerabilities generally fall into two categories:

## 1. Regular (In-Band) SSRF

In this type, the server **returns the response** from the forged request directly to the attacker.

This makes exploitation easier, as the attacker can immediately see the output.

## 2. Blind SSRF

In Blind SSRF, the request is successfully triggered, but **no response is returned** to the attacker.

Detection usually requires **out-of-band techniques**, such as monitoring incoming requests on an external server.

## Impact of a Successful SSRF Attack

A successful SSRF vulnerability can have serious consequences, including:

- Access to unauthorized internal services
- Exposure of sensitive customer or organizational data
- Lateral movement into internal networks
- Retrieval of authentication tokens or credentials
- Access to cloud metadata services

Because the requests originate from the server itself, traditional network-level protections often fail to prevent SSRF exploitation.

## How to Identify Potential SSRF Vulnerabilities

SSRF vulnerabilities often appear in places where a web application **fetches or processes remote resources** based on user input.


**Common locations to look for SSRF include:**

## 1. Full URL Parameters

When an application accepts a complete URL as a parameter:

`?url=https://example.com/resource`
## 2. Hidden Form Fields

Applications may store URLs or hosts in hidden input fields, which are still attacker-controlled.

## 3. Partial URLs (Hostname Only)

Parameters that accept only a hostname or domain:

`?srv=filestorage.example.com`
## 4. URL Paths

Some applications only accept a file path, assuming the base URL is trusted:

`?file=/documents/report.pdf`
Some of these scenarios are easier to exploit than others, and **trial and error is often required** to determine whether SSRF is possible.

## Detecting Blind SSRF

When no response is reflected back to the user, **external interaction is required** to confirm exploitation.

Common tools and techniques include:

- External HTTP logging services (e.g., request bin–style tools)
- A self-hosted HTTP server
- Burp Suite Collaborator

If the server makes a request to your controlled endpoint, Blind SSRF is confirmed.

## Example: Identifying a Likely SSRF Endpoint

Based on simple observation, the following URL is **most likely vulnerable to SSRF**:

`https://website.thm/fetch-file.php?fname=242533.pdf&srv=filestorage.cloud.thm&port=8001`
This endpoint explicitly allows control over:

- Hostname
- Port
- Resource location

All of which are strong SSRF indicators.

## Defeating Common SSRF Defenses

Security-aware developers often implement validation mechanisms to reduce SSRF risk. These typically rely on **deny lists** or **allow lists**, both of which can be bypassed if poorly implemented.

## Deny List–Based Defenses

A deny list blocks specific domains, IP addresses, or patterns while allowing all others.

Commonly blocked targets include:

- `localhost`
- `127.0.0.1`
- Internal IP ranges

## Common Deny List Bypasses

Attackers may use alternative representations of localhost, such as:

- `0`
- `0.0.0.0`
- `127.1`
- `2130706433`
- `017700000001`
- `127.0.0.1.nip.io`

## Cloud Metadata Exploitation

In cloud environments, access to:

`169.254.169.254`
is often blocked, as it exposes instance metadata.

Attackers can bypass this by pointing a **custom DNS record** to the metadata IP address, effectively hiding it behind a legitimate-looking domain.

## Allow List–Based Defenses

An allow list denies all requests unless they match a specific pattern, such as:

`https://website.thm/`
## Allow List Bypass Example

An attacker can register a domain like:

`https://website.thm.attacker-domain.com`
If the validation only checks the prefix and not the actual hostname resolution, the request may be incorrectly allowed.

## Open Redirects as an SSRF Bypass Technique

If strict validation blocks direct SSRF attempts, attackers may leverage **open redirect vulnerabilities**.

Example:

`https://website.thm/link?url=https://attacker.com`
If an SSRF-prone endpoint only allows requests to `website.thm`, the attacker can:

1. Point the request to the open redirect endpoint
2. Let the server follow the redirect to the attacker-controlled domain

This effectively bypasses allow list restrictions.
