# P2 — Unauthenticated AI Agent Access via Cloudflare Turnstile CAPTCHA Bypass Leading to Internal…

- **Source URL:** https://medium.com/@akashmotkar001/p2-unauthenticated-ai-agent-access-via-cloudflare-turnstile-captcha-bypass-leading-to-internal-527ab9ca1ce5
- **Fetched from:** https://medium.com/@akashmotkar001/p2-unauthenticated-ai-agent-access-via-cloudflare-turnstile-captcha-bypass-leading-to-internal-527ab9ca1ce5?source=rss-38c39a01cc6a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14978 (id 14978)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Akash motkar / Wed, 11 Nov 2026 03:31:02 GMT

**Severity:** P2 — High

**Vulnerability Type:** CAPTCHA Bypass, Authentication Bypass, Sensitive Information Disclosure

**Bugcrowd Priority:** P2

**CVSS v3.1:** 5.3 (Medium — supplied base vector)

**CVSS Vector:** AV/AC/PR/UI/S/C/I/A

**CWE:**

**OWASP Classification:**

During the security assessment, a critical weakness was identified in a publicly accessible WebSocket-based AI Agent service that uses Cloudflare Turnstile CAPTCHA as an anti-automation and access-control mechanism.

The application implements a dedicated captcha\_verify WebSocket event intended to validate CAPTCHA tokens before granting access to protected AI-agent functionality.

Under normal operation, clients are expected to complete the Cloudflare Turnstile challenge and submit a valid token to the backend for server-side verification.

However, the backend does not properly validate the supplied CAPTCHA token. Instead, it accepts arbitrary token values and returns a successful verification response regardless of whether the submitted token is valid.

Testing confirmed that the server accepts:

In every tested scenario, the server returns a successful CAPTCHA verification response:

```
{
  "event": "captcha_result",
  "payload": {
    "success": true
  }
}
```
This behavior indicates that the application does not enforce effective server-side CAPTCHA verification through Cloudflare’s Siteverify API.

The security impact extends beyond bypassing an anti-automation mechanism.

Following successful CAPTCHA verification with an empty token, an unauthenticated external client can invoke a dedicated WebSocket event to retrieve the AI Agent’s complete internal system prompt.

The following request exposes the internal configuration:

```
{
  "event": "system_prompt",
  "action": "get"
}
```
The server responds with approximately 25,223 characters of internal system configuration.

The disclosed information includes:

The disclosure is particularly concerning because the system prompt explicitly instructs the AI Agent never to reveal its internal configuration, system instructions, or available tool names. Nevertheless, the dedicated WebSocket event exposes this information directly, bypassing the AI model’s conversational security guardrails.

The two weaknesses form a single reproducible attack chain:

**Unauthenticated WebSocket Connection → CAPTCHA Verification Bypass → Unauthorized Guest Access → Internal System Prompt Disclosure → Internal Tool Schema Exposure**

Consequently, an external attacker can bypass the intended security gate and retrieve sensitive internal AI-agent configuration without authenticating to an application account or completing a legitimate CAPTCHA challenge.

**Component:** AI Agent WebSocket Service

**Protocol:** WebSocket Secure (WSS)

**Endpoint:** /ws

**Affected Functionality:**

**Authentication Required:** No

**CAPTCHA Required:** No valid CAPTCHA token required due to the bypass.

Install the required dependencies:

sudo apt update

sudo apt install nodejs npm -y

sudo npm install -g wscat

Execute the following command, replacing the placeholder with the authorized affected hostname and the application’s required connection parameters:

wscat -c "wss://\<affected-host>/ws?app\_type=web&origin\_domain=\<configured-origin>&origin\_shop=\<configured-shop>"

The WebSocket connection is successfully established without providing authentication credentials.

The server returns a connection initialization response similar to:

```
{
  "event": "connection_established",
  "payload": {
    "status": "connected",
    "session_id": "<session-id>",
    "timestamp": "<timestamp>",
    "turnstile_site_key": "<site-key>"
  }
}
```
This confirms that an anonymous client can establish a WebSocket session and that the application expects a CAPTCHA verification step.

Keep the connection open for the remaining steps.

Before submitting any CAPTCHA verification event, send the following WebSocket message:

The server responds with an authentication-required error:

```
{
  "event": "error",
  "payload": {
    "type": "auth_required",
    "code": 403,
    "message": "Please sign in or continue as guest before using this feature."
  }
}
```
This confirms that the application enforces a restriction on the requested functionality before the CAPTCHA/guest-access verification step.

Submit the following WebSocket event:

```
{
  "event": "captcha_verify",
  "payload": {
    "token": ""
  }
}
```
The server responds:

The server has now accepted an empty CAPTCHA token as a successful verification.

No actual Cloudflare Turnstile challenge was completed.

To verify that the issue is not limited to empty-token handling, repeat the CAPTCHA verification event using different invalid token values.

**Test 1 — Arbitrary invalid token**

```
{
  "event": "captcha_verify",
  "payload": {
    "token": "AAAA-not-a-real-captcha-token"
  }
}
```
**Test 2 — Whitespace-only token**

```
{
  "event": "captcha_verify",
  "payload": {
    "token": " "
  }
}
```
**Test 3 — Missing token parameter**

```
{
  "event": "captcha_verify",
  "payload": {}
}
```
All tested variations return a successful verification response:

This demonstrates that the server does not distinguish between valid and invalid CAPTCHA tokens.

After receiving the successful CAPTCHA verification response, submit the following WebSocket event through the same connection:

Unlike the previous request, which returned an authentication-required error, the server now processes the request and returns the internal system prompt.

The response follows this structure:

```
{
  "event": "system_prompt",
  "payload": {
    "system_prompt": "You are an AI Agent, a virtual assistant built for customer support..."
  }
}
```
The returned system prompt contains approximately 25,223 characters of internal configuration.

This confirms that the CAPTCHA bypass enables unauthorized access to functionality that was previously restricted.

Review the returned system prompt and identify the internal tool definitions and operational instructions.

The disclosed tool catalogue includes:

list\_devices

get\_device\_capabilities

search\_feed

get\_location\_mode

change\_location\_mode

escalate\_to\_live\_agent

check\_order\_status

shopify\_get\_product\_details

shopify\_search\_products

shopify\_get\_active\_promotions

kb\_find\_kb\_article

read\_kb\_article

The system prompt also exposes internal security guardrails, including instructions prohibiting disclosure of:

Additionally, the disclosed configuration contains internal knowledge-base identifiers, customer-support workflows, order-related processes, and escalation conditions.

This information provides an external user with detailed insight into the internal architecture and operational behavior of the AI Agent.

Repeat the authorized testing procedure against the other affected production WebSocket environments.

The same CAPTCHA bypass and system-prompt disclosure behavior was observed across all three tested production zones.

This confirms that the issue is not isolated to a single deployment instance and indicates that the underlying verification weakness is present across multiple production environments.

The combined vulnerability creates a significant security weakness in the authentication and access-control mechanisms protecting the publicly accessible AI-agent service.

The impact includes:

**1. Complete CAPTCHA protection bypass**

An unauthenticated attacker can satisfy the CAPTCHA verification event without completing the actual Cloudflare Turnstile challenge.

This removes the intended anti-automation protection from the affected WebSocket functionality.

**2. Unauthorized disclosure of internal AI configuration**

An external user can retrieve the complete internal system prompt, exposing configuration and operational instructions that are intended to remain server-side.

**3. Exposure of internal AI tool architecture**

The disclosed tool definitions provide detailed insight into the AI Agent’s capabilities, including device management, video-feed search, customer-support escalation, and product-related operations.

This information could help attackers develop more targeted attacks against the exposed AI-agent functionality.

**4. Exposure of internal business workflows**

The system prompt reveals internal customer-support processes, knowledge-base identifiers, escalation conditions, and operational instructions.

This information may help attackers understand how the AI Agent processes customer requests and how its internal workflows are structured.

**5. Increased exposure to automated abuse**

Because arbitrary CAPTCHA tokens are accepted, automated clients can satisfy the verification step without solving a challenge.

This could facilitate scripted access to the AI-agent interface and increase exposure to automated abuse and unnecessary LLM resource consumption.

Actual cost amplification or service degradation was not measured during the assessment.

**6. Increased risk of subsequent AI-agent attacks**

Disclosure of internal tool definitions and guardrails provides attackers with information that could assist targeted prompt-injection, jailbreak, and tool-abuse research.

However, the disclosure alone does not establish that these subsequent attacks are successful.

**Important limitation:** Testing did not demonstrate unauthorized access to real customer devices, camera feeds, recordings, or account data. These impacts are not claimed as confirmed.

The primary root cause is insufficient server-side validation of Cloudflare Turnstile tokens.

The backend appears to accept the captcha\_verify event as sufficient proof of successful CAPTCHA completion without independently verifying the authenticity of the supplied token.

Additionally, the WebSocket protocol exposes a dedicated system\_prompt retrieval event to clients without enforcing appropriate authentication and authorization controls.

Internal system configuration should never be directly retrievable through a publicly accessible client-facing WebSocket event.

The combined weaknesses demonstrate failures in both CAPTCHA verification and authorization enforcement.

The following remediation measures are recommended:

**1. Implement proper server-side CAPTCHA validation**

Every submitted CAPTCHA token must be validated using Cloudflare’s official Siteverify API.

Reject empty, malformed, invalid, expired, and previously used tokens.

**2. Remove public system-prompt retrieval functionality**

The system\_prompt retrieval event should be removed from the publicly accessible WebSocket protocol.

System prompts should remain server-side configuration and must never be directly exposed to external clients.

**3. Enforce authentication and authorization**

Implement strict server-side authentication and authorization checks for all privileged WebSocket events.

Do not rely on a client-submitted CAPTCHA event as proof of authorization.

**4. Implement CAPTCHA token replay protection**

Ensure CAPTCHA tokens are validated for their expected hostname and action, have not expired, and cannot be reused.

**5. Introduce independent rate limiting**

Apply server-side rate limiting and anomaly detection to WebSocket connection attempts and sensitive application events.

**6. Protect internal AI configuration**

Avoid exposing internal tool schemas, operational instructions, knowledge-base identifiers, and sensitive business logic through client-accessible interfaces.

**7. Conduct a comprehensive WebSocket security review**

Review all WebSocket events to identify other functionality that may be accessible without proper authentication or authorization.

AttributeClassificationVulnerabilityUnauthenticated AI Agent Access via CAPTCHA BypassSeverityP2 — HighBugcrowd PriorityP2CVSS v3.15.3 (Medium, supplied vector)CWECWE-287, CWE-290, CWE-200, CWE-668, CWE-804OWASP LLMLLM07:2025 — System Prompt LeakageCategoryAuthentication Bypass / Sensitive Information DisclosureAttack VectorNetworkPrivileges RequiredNoneUser InteractionNoneStatusConfirmed
