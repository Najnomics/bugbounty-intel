# Bypassing URL Validation with IPv6

- **Source URL:** https://medium.com/@muhammedmoslaam/bypassing-url-validation-with-ipv6-an-ssrf-story-9e5998c5d4af
- **Fetched from:** https://medium.com/@muhammedmoslaam/bypassing-url-validation-with-ipv6-an-ssrf-story-9e5998c5d4af?source=rss-057c42d4629c------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14970)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** MuhammedMoslaam / Thu, 05 Nov 2026 23:19:26 GMT

*How IPv6 representations bypassed an IPv4-focused webhook URL validator, exposing a potential path to internal services.*

During a security assessment, I discovered that a webhook URL validator blocked IPv4 loopback and metadata addresses but accepted their IPv6 equivalents.

By testing IPv6 loopback (\[::1\]), IPv4-mapped IPv6, and NAT64 representations, I identified a validation bypass.

I confirmed that webhook creation accepted these addresses and that the backend performed outbound HTTP requests through an external callback server.

However, internal response retrieval could not be demonstrated because the platform did not expose webhook delivery logs or response information.

The application exposed an authenticated API endpoint for creating webhooks:

POST /api/v1/webhooks?teamId=\<teamId>

Content-Type: application/json

{

"url": "\<attacker-controlled-url>",

"events": \["project.created"\]

}

The application enforced a public-URL-only policy, rejecting loopback, link-local, and cloud metadata addresses.2. Testing IPv4 Loopback

I started with the standard IPv4 loopback address:

```
{
  "url": "http://127.0.0.1:80/",
  "events": ["project.created"]
}
```
**Response:**

400 Bad Request

```
{
  "error": {
    "code": "validation_error",
    "message": "Webhook URL should be a public URL."
  }
}
```
Other tested addresses and representations, including 169.254.169.254, localhost, and decimal/hexadecimal/octal IPv4 formats, were also rejected.

Next, I tested the IPv6 loopback equivalent:

```
{
  "url": "http://[::1]:80/",
  "events": ["project.created"]
}
```
200 OK

The webhook was successfully created, and the application returned a secret token.

The difference was clear:

I continued testing alternative IPv6 representations:

\[::1\] — Accepted

\[::ffff:127.0.0.1\] — Accepted

\[::ffff:169.254.169.254\] — Accepted

\[64:ff9b::7f00:1\] — Accepted

These results indicated that the validator was not properly normalizing and checking IPv6 destinations.

To verify webhook execution, I configured a webhook using an external callback domain under my control.

I then triggered the project.created event by creating a project:

POST /api/v9/projects?teamId=\<teamId>

Content-Type: application/json

{

"name": "ssrf-confirm-new-collab",

"framework": "nextjs"

}

After triggering the event, the callback service recorded DNS lookups and HTTP requests originating from the application’s infrastructure.

This confirmed that the backend performed outbound HTTP requests when webhook events were triggered.

I investigated whether internal response data could be retrieved through the webhook functionality.

However, the platform did not expose delivery logs, HTTP response codes, or response bodies. Several possible delivery endpoints also returned 404 Not Found.

As a result, I could not demonstrate successful internal response retrieval or data exfiltration.

**Confirmed findings:**

**Not demonstrated:**

The vulnerability creates an SSRF attack surface that could potentially expose internal infrastructure.

An authenticated user could configure webhook destinations that bypassed the application’s IPv4-focused validation.

The actual impact depends on backend network access and whether requests to internal destinations are successfully executed.

This assessment demonstrates how incomplete IPv6 handling can undermine URL validation and introduce an SSRF vulnerability.

The key lesson is that URL validation must account for all IP address representations, not just IPv4.

**Good security research is about proving what actually happened, not claiming impact that cannot be demonstrated.**

Don’t forget to follow me on [www.linkedin.com/in/muhammed-moslaam](http://www.linkedin.com/in/muhammed-moslaam)
