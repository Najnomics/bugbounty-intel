# Information Disclosure via Exposed Swagger Config

- **Source URL:** https://medium.com/@v01d19/information-disclosure-via-exposed-swagger-config-dafee40ab215
- **Fetched from:** https://medium.com/@v01d19/information-disclosure-via-exposed-swagger-config-dafee40ab215?source=rss-895dd646aed6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14956 (id 14956)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** v01d19 / Thu, 22 Oct 2026 19:31:20 GMT

If there’s one vulnerability class I have truly fallen in love with as a bug bounty hunter, it’s Information Disclosure. You don’t need complex exploits, a specific CVE, or even a single line of payload.

Sometimes, all it takes is some recon, navigating through the target, and letting your curiosity guide you. Just by playing around, that curiosity hands you a bug on a silver platter. That’s exactly what happened in this writeup.

The vulnerability was a security misconfiguration, allowing absolutely anyone to access the internal map of the entire server without needing any authentication at all.

As usual, I started with subdomain enumeration, but not just once. I did it on the same domain over and over until I found something that made me stop:

https://public.stage.ops.example.me/

I then started fuzzing the nested subdomain using ffuf until I uncovered this pretty endpoint :

https://public.stage.ops.example.me/api/v3/api-docs/swagger-config

And guess what, the endpoint is giving me response code 418 I’m a teapot

Focusing on the Host header, I asked myself what can I do with this response code? It’s not even a 403 that I can try to bypass.

I tried several things, but that one try that actually worked was in the Host header by replacing the first word with another, or even deleting the whole header and seeing what I caught:

now the real finding, you see this file that called :

/api/v3/api-docs/Internal%20APIs

we did it, by calling this endpoint :

and just like this i got a file contain the internal map for the whole server it contain things like :

Leaked Endpoints & Information

Admin Authentication Endpoints

/auth/admin/sso/code

/auth/admin/verification/validate

/auth/admin/verification/{email}

/auth/token/exchange/admin

API Key Management

/apiKey

/apiKey/active

/apiKey/{userId}/generateApiKey

/apiKey/{apiKeyId}

/apiKey/deactivateApiKey/{userId}

/apiKey/activateApiKey/{userId}

Jira Integration

/jira/internal/webhooks/worklog/created

/jira/internal/webhooks/worklog/updated

/jira/internal/webhooks/worklog/deleted

/jira/integration/webhooks/install

/jira/integration/webhooks/uninstall

System Settings

/system-settings

/system-settings/smtp-configuration

/system-settings/o-auth2-configuration

/system-settings/saml2-configuration

/system-settings/custom-emails

MongoDB Connectors:

exampleConnectorMongoDB

eventConnectorMongoDB

fileImportConnectorMongoDB

jobManagerMongoDB

quickbooksConnectorMongoDB

sharedConnectorMongoDB

webhookLogConnectorMongoDB

Redis Version: 7.2.4

Backend Service Version: 1.2333.0

and more than it it gave me exactly :

Total Internal API Endpoints: 756

OpenAPI Spec Size: 877 KB

Staging Dataset: 75,325 users

*The leaked OpenAPI specification was not just a list of endpoints; it was a complete architectural blueprint of the backend. It exposed:*

*Ultimately, this turned a standard Information Disclosure into a dangerous vulnerability that could allow an attacker to map the entire infrastructure and potentially pivot to the production environment.*

This issue is an example of a classic **Security Misconfiguration**. The vulnerability existed due to a combination of the following factors:

The fix is very simple:

This vulnerability showed me an important security lesson:

*Internal files should never be exposed to the public internet.*

Sometimes the most critical vulnerabilities are not complex exploits, They are simple misconfigurations hiding in plain sight waiting for you to catch.

Luckily, it wasn’t a duplicate, and I got paid for it.

Finally, keep hacking, keep breaking, and never stop
