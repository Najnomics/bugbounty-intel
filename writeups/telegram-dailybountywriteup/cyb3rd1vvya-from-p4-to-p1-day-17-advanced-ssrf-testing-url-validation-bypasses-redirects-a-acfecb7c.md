# From P4 to P1

- **Source URL:** https://medium.com/@cyb3rD1vvya/from-p4-to-p1-day-17-advanced-ssrf-testing-url-validation-bypasses-redirects-and-dns-rebinding-5f6d92dca0fa
- **Fetched from:** https://medium.com/feed/@cyb3rD1vvya
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14985 (id 14985)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Series:** From P4 to P1

**Day:** 17 of 30

**Topic:** Advanced Server-Side Request Forgery (SSRF) Testing

**Category:** Web Application Security | API Security

### 1. Introduction

In Day 10, we explored the fundamentals of Server-Side Request Forgery (SSRF), including URL-handling functionality, controlled callbacks, and basic validation.

But identifying a URL-fetching feature is only the beginning.

Modern applications often implement destination validation to prevent SSRF. They may use hostname allowlists, IP address restrictions, URL parsers, redirect controls, and network-level security policies.

However, these protections can fail when different components interpret the same URL differently.

Imagine an application that accepts URLs only from approved domains. The application validates the hostname, but its HTTP client interprets the destination differently or follows a redirect that was never checked.

This can create an opportunity to bypass the intended destination restrictions.

This is where **Advanced SSRF Testing** becomes important.

For bug bounty hunters, the goal is to understand how the entire URL-processing pipeline works, identify inconsistencies, and demonstrate whether an attacker can make the backend access an unauthorized destination.

Let’s explore the methodology.

### 2. Understanding Advanced SSRF

Advanced SSRF testing focuses on weaknesses in the security controls designed to restrict server-side requests.

Common areas include:

- URL parsing inconsistencies.
- Hostname validation weaknesses.
- Redirect handling.
- DNS resolution problems.
- DNS rebinding.
- IP address validation.
- URL scheme restrictions.
- Network egress controls.

Consider this simplified application:

User submits URL

|

v

Application validates hostname

|

v

HTTP client processes URL

|

v

Application follows redirects

|

v

Backend makes request

A secure implementation must validate the destination at every relevant stage, not just when the user initially submits the URL.

**Important:** Advanced SSRF is not about collecting unusual URL payloads. It is about understanding whether the application’s security boundary can actually be bypassed.

### 3. URL Parsing and Validation Inconsistencies

One common source of SSRF vulnerabilities is the difference between how two components interpret a URL.

An application may use one library to validate a URL and another library to make the actual request.

If their interpretations differ, the validation decision may not match the destination ultimately contacted.

### Example: URL Structure

Consider a standard URL:

https://example.org/path

It contains several components:

- Scheme: https
- Hostname: example.org
- Path: /path

The application should validate the parsed hostname and ensure the HTTP client connects to the same approved destination.

### What Should Researchers Investigate?

During authorized testing, review:

1. Which component parses the submitted URL?
2. Which component validates the hostname?
3. Does the HTTP client use the same interpretation?
4. Are credentials or unusual URL components handled safely?
5. Are hostname comparisons exact?
6. Are redirects independently validated?

### Common Validation Mistakes

**Substring matching**

A weak implementation might check whether a URL contains an approved hostname rather than comparing the parsed hostname against an exact allowlist.

**Incomplete hostname normalization**

Differences in case, trailing dots, internationalized domain names, or hostname normalization can produce inconsistent validation results.

**Confusing hostnames with paths**

A hostname appearing somewhere in a URL does not mean it is the actual destination.

**Trusting client-side validation**

Validation performed only in JavaScript does not protect server-side request functionality.

A secure implementation should parse URLs consistently and compare normalized destinations against an explicit allowlist.

### 4. Redirect-Based SSRF

Redirect handling is another important area of advanced SSRF research.

An application may validate the initial destination but fail to validate the destination returned by an HTTP redirect.

Consider this workflow:

Application

|

| Requests approved.example

v

Approved Website

|

| Returns HTTP 302

v

Redirect Destination

|

v

Backend follows redirect

If the application does not revalidate the redirect destination, its initial security check may become ineffective.

### How to Test Redirect Handling Safely

Use two researcher-controlled domains or endpoints.

For example:

- Endpoint A: An approved test destination.
- Endpoint B: A separate destination you control.

Configure Endpoint A to return a redirect to Endpoint B.

Then:

1. Submit Endpoint A through the application’s URL-fetching functionality.
2. Monitor both endpoints.
3. Observe whether the backend follows the redirect.
4. Review whether the application validates the second destination.
5. Record the resulting behavior.

This test demonstrates redirect handling without accessing internal infrastructure.

### What Should Developers Do?

- Disable automatic redirects when unnecessary.
- Validate every redirect destination.
- Restrict the number of redirects.
- Reject redirects to prohibited address ranges.
- Ensure the final connection uses the validated destination.

A redirect to another researcher-controlled endpoint demonstrates redirect following, not automatically an exploitable SSRF vulnerability.

### 5. DNS Rebinding

DNS rebinding is a technique that can exploit applications that validate a hostname at one point in time but resolve it again when making the actual connection.

The basic problem is a mismatch between DNS validation and connection-time resolution.

### Simplified Example

An application receives a hostname.

Step 1: Application resolves hostname.

|

v

Approved public address

|

v

Step 2: Application validates address.

|

v

Step 3: HTTP client resolves hostname again.

|

v

Different address

If the application does not bind its validation decision to the actual connection, a destination may change between validation and use.

This is related to a broader security issue known as **Time-of-Check to Time-of-Use (TOCTOU)**.

### What Should Bug Bounty Hunters Understand?

Investigate:

- Whether DNS is resolved more than once.
- Whether the application validates all returned IP addresses.
- Whether the HTTP client uses the validated address.
- Whether DNS results are cached.
- Whether the application revalidates destinations after redirects.

Only perform DNS rebinding experiments against explicitly authorized test environments or infrastructure you control.

### Recommended Protection

Applications should validate the resolved IP address and ensure the actual connection uses that validated address.

They should also account for DNS changes, redirects, IPv4 and IPv6, and connection reuse.

### 6. IP Address and Network Destination Validation

SSRF protections should not depend only on hostname allowlists.

Applications must also consider the actual IP address to which a request will connect.

### Important Address Categories

Address categorySecurity considerationLoopbackRefers to the local machinePrivate IPv4Used within private networksLink-localUsed for local network communicationIPv6 loopbackLocal IPv6 destinationIPv6 unique-localPrivate IPv6 addressingIPv4-mapped IPv6IPv4 address represented in IPv6 form

A secure implementation should reject prohibited address ranges according to its security policy.

### Common Mistakes

- Validating only IPv4 while ignoring IPv6.
- Checking the hostname but not the resolved IP.
- Validating one DNS answer but connecting to another.
- Allowing redirects to bypass address restrictions
- Failing to account for alternate address representations.

For bug bounty testing, begin by reviewing validation behavior in a controlled environment. Do not probe production internal services or cloud metadata endpoints unless explicitly permitted.

### 7. URL Scheme Restrictions

Applications may support multiple URL schemes depending on their implementation.

For example:

https://example.org

http://example.org

A URL-fetching feature designed to retrieve web pages should generally allow only the schemes it actually needs.

Accepting unnecessary schemes can introduce additional risks because different clients may handle them differently.

### Testing Approach

In an authorized environment:

1. Identify the schemes accepted by the application.
2. Test whether unsupported schemes are rejected.
3. Observe how the backend handles malformed or unexpected URLs.
4. Confirm whether the actual request is made by the server.
5. Document the behavior.

Do not assume that accepting an unusual scheme automatically creates an exploitable vulnerability.

### 8. Practical Advanced SSRF Testing Methodology

Here is a structured approach for bug bounty hunters.

### Step 1: Identify URL-Processing Functionality

Look for:

- Website previews.
- Remote image imports.
- PDF generators.
- Screenshot services.
- Webhook testing.
- Document import functionality.
- External API integrations.

Use Burp Suite to identify requests containing URL parameters.

### Step 2: Establish a Baseline

Submit a normal URL hosted on infrastructure you control.

Record:

- HTTP response.
- Request timing.
- DNS interaction.
- HTTP callback.
- Redirect behavior.
- Response content.

This establishes whether the backend processes the URL.

### Step 3: Understand Destination Validation

Determine whether the application uses:

- Exact hostname allowlists.
- IP address restrictions.
- URL scheme validation.
- DNS resolution checks.
- Redirect restrictions.

Do not assume a validation weakness just because the application returns an error.

### Step 4: Test Redirect Handling

Use controlled endpoints to determine whether the backend follows redirects and whether each destination is checked.

Record the initial request and all subsequent controlled interactions.

### Step 5: Review DNS Handling

Understand whether hostname validation and connection-time resolution are consistent.

Use only domains you control and authorized testing infrastructure.

### Step 6: Examine IPv4 and IPv6 Handling

Review whether the destination validation policy applies consistently to both address families.

Do not attempt to reach restricted production services.

### Step 7: Confirm the Impact

A strong finding should establish:

- The affected functionality.
- The intended destination restrictions.
- The validation weakness.
- The actual server-side behavior.
- The security impact demonstrated.

A controlled callback is useful evidence of server-side interaction, but it does not prove internal network access or sensitive information disclosure.

### 9. Common False Positives and Mistakes

Advanced SSRF testing can produce misleading results.

Avoid these mistakes:

**1. Treating every redirect as SSRF**

Redirect following may be intended functionality. The issue is whether it bypasses a security restriction.

**2. Confusing DNS resolution with an HTTP request**

A DNS callback proves a resolution event, not necessarily a completed HTTP connection.

**3. Assuming hostname validation is always bypassable**

Some applications correctly normalize and validate destinations.

**4. Ignoring the actual connection destination**

A validation response is not enough. Understand where the backend really connects.

**5. Reporting URL parser differences without impact**

Different parsing behavior is a weakness only when it causes a security boundary to fail.

**6. Claiming internal access without evidence**

Do not claim access to private services or metadata endpoints based on speculation.

**7. Testing outside program authorization**

Do not use production internal addresses, sensitive services, or third-party infrastructure without explicit permission.

### 10. Example Vulnerability Report

### Title

SSRF Protection Bypass Through Unvalidated Redirect Destination in URL Preview Functionality

**Severity:** Depends on demonstrated impact.

**Category:** Server-Side Request Forgery / Improper Destination Validation

**CWE:** CWE-918 — Server-Side Request Forgery (SSRF)

**Related CWE:** CWE-367 — Time-of-check Time-of-use (TOCTOU) Race Condition

**OWASP Mapping:** OWASP Top 10:2021 — A10: Server-Side Request Forgery (SSRF)

### Description

During the security assessment, a potential SSRF protection bypass was identified in the application’s URL preview functionality.

The application validates the initial user-supplied URL but appears to follow HTTP redirects without consistently validating the resulting destination.

Testing with researcher-controlled endpoints demonstrated that the backend followed a redirect from the initially submitted destination to a second destination.

This behavior suggests that redirect destination validation may be incomplete.

The application should enforce destination restrictions for every request in the redirect chain.

### Steps to Reproduce

1. Access the authorized URL preview functionality.
2. Configure a researcher-controlled endpoint as the initial destination.
3. Configure the endpoint to redirect to a second researcher-controlled destination.
4. Submit the initial URL to the application.
5. Monitor both endpoints for incoming interactions.
6. Record whether the backend follows the redirect.
7. Review whether the application applies destination validation to the second URL.

### Impact

If redirect destinations are not properly validated, an attacker may be able to bypass the application’s intended destination restrictions.

Depending on the backend’s network access and the affected functionality, this may allow requests to unintended resources.

The severity depends on the actual destinations reachable and the impact demonstrated.

### Remediation

- Validate the initial URL using a trusted parser.
- Enforce exact hostname allowlists.
- Resolve and validate all destination IP addresses.
- Revalidate every redirect destination.
- Restrict unnecessary URL schemes.
- Apply connection-time IP validation.
- Protect against DNS rebinding.
- Disable automatic redirects where appropriate.
- Apply network-level egress restrictions.
- Avoid exposing sensitive response content.

**Reporting note:** This example should only be used when the application demonstrably fails to enforce its destination policy. A redirect between two controlled domains alone does not establish a security impact.

### 11. Developer Checklist: Preventing Advanced SSRF

- Use a trusted and consistent URL parser.
- Enforce exact hostname allowlists.
- Normalize and validate hostnames.
- Restrict unnecessary URL schemes.
- Resolve and validate IPv4 and IPv6 addresses.
- Bind validation to the actual connection destination.
- Revalidate every redirect.
- Protect against DNS rebinding.
- Disable automatic redirects where possible.
- Apply outbound network restrictions.
- Limit request timeouts and response sizes.
- Monitor unusual outbound requests.

### 12. Useful Tools for Advanced SSRF Research

ToolPurposeBurp SuiteIntercept and modify URL-handling requestsBurp RepeaterManually validate destination behaviorInteractshDetect controlled DNS and HTTP interactionscurlInspect redirects and HTTP responsesDNS utilitiesReview hostname resolutionPythonBuild controlled test endpointsBurp CollaboratorCorrelate out-of-band interactions

Use tools only against authorized targets and infrastructure you control.

### 13. Final Thoughts

Advanced SSRF testing is about understanding the complete journey of a URL through an application.

A hostname may pass validation, but that does not guarantee the final network connection is safe.

A redirect may appear harmless, but its destination may not have been checked.

A DNS lookup may be valid initially, but the connection-time address may differ.

For bug bounty hunters, the important skills are understanding URL parsing, destination validation, redirects, DNS behavior, and network boundaries.

Remember:

**SSRF protection must validate where the server actually connects, not just the URL submitted by the user.**

A strong report should demonstrate the validation weakness, reproduce the behavior safely, and explain the actual impact without making unsupported claims.

### Tomorrow: Day 18 — HTTP Request Smuggling

Next, we will explore how inconsistent HTTP request parsing between front-end and back-end servers can create request boundary confusion, security control bypasses, and unexpected application behavior.

**From P4 to P1 — Keep learning. Keep testing. Keep reporting responsibly.**
