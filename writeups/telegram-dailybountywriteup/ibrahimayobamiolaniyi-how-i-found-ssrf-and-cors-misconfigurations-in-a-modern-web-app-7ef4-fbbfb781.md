# How I Found SSRF and CORS Misconfigurations in a Modern Web App

- **Source URL:** https://medium.com/@ibrahimayobamiolaniyi/how-i-found-ssrf-and-cors-misconfigurations-in-a-modern-web-app-7ef44c3391d5?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@ibrahimayobamiolaniyi
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 13597)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Why browsers won’t save your backend API, and how I proved it during a manual penetration test.**

A lot of modern web applications operate on an illusion of security. Developers often rely on browser-level mechanisms to protect their APIs, assuming that if the frontend blocks a request, the backend is safe.

During my recent manual security assessment of the JobGuard application, I demonstrated exactly why that assumption is a critical vulnerability. By bypassing frontend restrictions entirely, I was able to interact directly with the backend API, eventually uncovering a severe Cross-Origin Resource Sharing (CORS) misconfiguration, alongside Server-Side Request Forgery (SSRF) and Insecure Direct Object Reference (IDOR) vulnerabilities.

Here is a breakdown of how I approached the architecture, what I found, and how the development team can fix it.

### The Setup: Mapping a Decoupled Architecture

Before firing any payloads, I needed to understand the application’s architecture. Using Burp Suite as an interception proxy, I passively mapped the environment and immediately noticed a decoupled structure:

- **The Presentation Layer:** Hosted on Vercel (https://job-guard-xj4y.vercel.app/).
- **The Core Backend API:** Hosted separately on Render (https://jobguard-api.onrender.com).

The frontend was actually well-configured. It enforced strict HTTPS communication via Strict-Transport-Security (HSTS) headers and handled invalid routing securely by returning generic 404 pages instead of leaking internal directory structures.

However, because the Render host managed all the core business logic, database interactions, and authentication, I knew that was my primary attack surface.

### The Breakthrough: When CORS Breaks the App (But Not the Attacker)

The most interesting finding came during the evaluation of the authentication flow. While attempting to log in, I noticed the mechanism was completely broken for legitimate users.

I intercepted the traffic and analyzed the browser’s OPTIONS preflight request to the backend API. The server returned a 204 No Content status, but the Access-Control-Allow-Origin header explicitly whitelisted an older, inactive domain (https://jobguard-mu.vercel.app) instead of the active production environment.

Because of this origin mismatch, modern browsers enforced a strict CORS policy and aborted the subsequent POST request containing the user credentials.

**Here is the critical security takeaway:** CORS is a browser-enforced mechanism, not a backend security control.

While legitimate users were locked out, an attacker using an interception proxy like Burp Suite or Postman isn’t bound by browser rules. I was able to effortlessly bypass the CORS restriction, interact directly with the /api/v1/auth/login endpoint, and continue my active testing against the API.

### Pushing Deeper: Uncovering SSRF and IDOR

Once I established direct communication with the backend API, I executed a series of manual injection tests. This led to the discovery of two high-severity flaws:

1. **Server-Side Request Forgery (SSRF):** I manipulated backend requests to force the server to interact with unintended internal resources, exposing internal network structures that should have been entirely isolated.
2. **Insecure Direct Object Reference (IDOR):** By analyzing the resource identifiers, I found predictable ID patterns. This lack of robust access control meant that, if exploited, an attacker could potentially access or manipulate data belonging to other users.

To make matters worse, my initial network reconnaissance using Nmap revealed 991 unnecessarily exposed ports on the backend infrastructure, providing an unnecessarily large attack surface.

### The Remediation Strategy

Finding vulnerabilities is only half the job; providing actionable fixes is the other. In the 38-page technical report I delivered to the development team, I outlined the following critical remediations:

#### 1. Fix the CORS Whitelist (and Don’t Rely on It for Security)

The immediate fix was to adjust the backend configuration to whitelist the active production domain (https://job-guard-xj4y.vercel.app). However, I emphasized that the /api/v1/auth/login route needed real, API-level defenses—specifically aggressive rate limiting and robust input validation to thwart automated brute-force attacks.

#### 2. Implement UUID v4

To eliminate the IDOR vulnerabilities, the backend needs to move away from predictable, sequential resource identifiers and implement universally unique identifiers (UUID v4), making it computationally infeasible for an attacker to guess valid resource IDs.

#### 3. Network Isolation

The backend architecture required immediate network isolation to mitigate the SSRF vulnerability, alongside strict firewall rules to close the 991 exposed ports identified during the Nmap scans.

### Conclusion

This assessment was a perfect reminder of why automated vulnerability scanners aren’t enough. An automated tool might have flagged the CORS error as a simple functional bug, but manual traffic analysis revealed it as a gateway to directly attacking an unprotected API.

If you are building decoupled applications, remember: your frontend is just a presentation layer. Your backend API must be built to defend itself.

*If you are interested in the raw data, HTTP request logs, and the full CVSS scoring of these vulnerabilities, you can check out the complete 38-page technical report on my GitHub here:* [https://github.com/Yung-IB/JobGuard-Penetration-Test](https://github.com/Yung-IB/JobGuard-Penetration-Test)
