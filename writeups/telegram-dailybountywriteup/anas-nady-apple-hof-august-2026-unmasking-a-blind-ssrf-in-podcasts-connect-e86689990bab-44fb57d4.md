# Apple HOF (August 2026)

- **Source URL:** https://medium.com/@anas-nady/apple-hof-august-2026-unmasking-a-blind-ssrf-in-podcasts-connect-e86689990bab
- **Fetched from:** https://medium.com/feed/@anas-nady
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14994 (id 14994)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*A step-by-step story of discovery, persistence, and securing the internal network.*

### 📝 Summary of Finding

During a routine security assessment of the **Apple Podcasts Connect** platform, a **Blind Server-Side Request Forgery (SSRF)** vulnerability was discovered. While the platform properly protected the primary “Add show with RSS Feed” endpoint, the alternative flow — “Add new show without RSS Feed” — contained a hidden weakness.

By manipulating the feedUrl parameter, it was possible to trick the server into making outbound HTTP requests to internal IP addresses. Although the server did not return the response body (making it "blind"), the vulnerability could be reliably exploited using a **time-based side-channel attack** to map internal network ports.

This report was successfully validated, patched, and acknowledged by the Apple Product Security team, earning a spot on the **Apple Security Hall of Fame**.

### 🪜 Steps to Reproduce

*(Note: Specific identifiers and UUIDs have been redacted for security.)*

1. Log in to the Podcasts Connect platform and navigate to the “Add a Show” section.
2. Select the secondary option: **“Add new show without RSS Feed”**.
3. Enter a dummy show name and proceed to the next step.
4. In the “More Options” section at the bottom, locate the **“Add RSS Feed”** field.
5. Intercept the PUT /podcasts/pcc/v1/shows/{uuid} request using a proxy tool (e.g., Burp Suite).
6. Modify the feedUrl parameter to point to a standard external URL (e.g., a public RSS feed). Observe a fast, normal response time (\~300ms).
7. Change the feedUrl to a localhost address with an open/filtered port (e.g., [http://127.0.0.1:80).](<http://127.0.0.1:80).>)
8. Send the request and observe the response time. It will significantly increase (e.g., >5,000ms) due to a connection timeout.
9. Change the feedUrl to a localhost address with a definitively closed port (e.g., [http://127.0.0.1:65535).](<http://127.0.0.1:65535).>)
10. Observe that the response time drops back to a fast state (\<1,000ms) due to an immediate “Connection Refused.”

### ⚠️ The Weakness

The core weakness lay in the **lack of strict outbound request validation** on the secondary show-creation endpoint.

While the primary RSS ingestion pipeline had robust SSRF protections (returning a 403 Forbidden), the alternative manual-entry flow failed to sanitize or restrict the feedUrl parameter. The backend service blindly attempted to fetch the provided URL. Because the response body was not reflected back to the user, the vulnerability was "blind." However, the application's error-handling and socket timeout behaviors created a measurable **time-based side-channel**, allowing an attacker to infer the state of internal ports based on response latency.

### 💥 Impact

Although this was a *Blind* SSRF, the impact was still significant:

- **Internal Network Port Scanning**: Attackers could map open, closed, or filtered ports on the local server (127.0.0.1) or other internal IP addresses.
- **Service Discovery**: By identifying open ports, an attacker could infer the presence of internal administrative dashboards, metadata services, or legacy applications.
- **Foundation for Further Attacks**: If combined with other vulnerabilities (e.g., a separate information disclosure or a misconfigured internal service), this SSRF could serve as a critical pivot point for deeper network compromise.

### 🛡️ Resolution

After initial skepticism, the researcher provided a clear, video-based Proof of Concept (PoC) demonstrating the exact millisecond discrepancies between open and closed ports.

The Apple Product Security team investigated and deployed a comprehensive fix:

1. **Input Validation**: The feedUrl parameter is now strictly validated against allowlists and blocked if it points to internal IP ranges (e.g., 127.0.0.0/8, 10.0.0.0/8, etc.).
2. **Uniform Error Handling**: Attempts to trigger the vulnerability now immediately return a 403 Forbidden response with an {"message": "access denied"} body.
3. **Response Time Normalization**: All rejected requests now resolve in under 400ms, completely eliminating the time-based side-channel.

### 🎯 Summary

This case highlights a classic security truth: **protecting one path is not enough if an alternate path is left unguarded**. What started as a minor inconsistency in response times evolved into a validated Blind SSRF report. Through persistent, professional collaboration and a well-crafted video PoC, the researcher helped the Apple Security Team identify and eliminate a subtle but dangerous flaw.

The successful remediation and subsequent acknowledgment on the **Apple Security Hall of Fame** stand as a testament to the value of thorough testing and constructive researcher-company partnerships. 🍏🔒✨

[Apple HOF (August 2026): Unmasking a Blind SSRF in Podcasts Connect](https://infosecwriteups.com/apple-hof-august-2026-unmasking-a-blind-ssrf-in-podcasts-connect-e86689990bab) was originally published in [InfoSec Write-ups](https://infosecwriteups.com) on Medium, where people are continuing the conversation by highlighting and responding to this story.
