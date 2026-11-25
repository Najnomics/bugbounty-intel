# From P4 to P1

- **Source URL:** https://medium.com/@cyb3rD1vvya/from-p4-to-p1-day-10-server-side-request-forgery-ssrf-finding-and-validating-server-side-c76e4c785bd2
- **Fetched from:** https://web.archive.org/web/20261106110833/https://medium.com/@cyb3rD1vvya/from-p4-to-p1-day-10-server-side-request-forgery-ssrf-finding-and-validating-server-side-c76e4c785bd2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14967 (id 14967)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From P4 to P1: Day 10 — Server-Side Request Forgery (SSRF): Finding and Validating Server-Side Request Vulnerabilities

**Series:** From P4 to P1

**Day:** 10 of 30

**Topic:** Server-Side Request Forgery (SSRF)

**Category:** Web Application Security | API Security

## 1. Introduction

Imagine a web application that allows users to enter a URL to fetch an image, generate a preview, import a document, or check whether a website is available.

You submit a URL, and the application’s backend makes a request to retrieve its content.

But what happens if the application accepts a URL pointing somewhere it was never intended to access?

This is where **Server-Side Request Forgery (SSRF)** comes into play.

SSRF occurs when an attacker can influence a server-side request made by an application, potentially causing the server to access internal services, restricted network resources, or unintended external destinations.

Unlike vulnerabilities that execute directly in a victim’s browser, SSRF abuses the trust and network access of the application’s backend.

For bug bounty hunters, SSRF can be particularly interesting because its impact depends on what the server can reach and what information or actions can be accessed through the vulnerable functionality.

## 2. What Is SSRF?

Server-Side Request Forgery is a vulnerability in which an application makes server-side requests using attacker-controlled or insufficiently validated input.

Consider this example:

An application provides an endpoint:

`POST /api/fetch-preview`

Request:

```
POST /api/fetch-preview HTTP/1.1
Host: example.com
Content-Type: application/json
```
```
{
  "url": "https://example.org"
}
```
The backend receives the URL and fetches its content.

If the application does not properly validate the destination, a user may be able to influence the server into requesting destinations outside the intended scope.

The key issue is not simply that a URL can be supplied. The issue is whether an attacker can make the server perform an unauthorized request and demonstrate a security impact.

## 3. How Does SSRF Work?

A typical SSRF flow looks like this:

1. An application accepts a URL or hostname from a user.
2. The backend processes the supplied value.
3. The backend makes an HTTP or other network request.
4. The response may be returned to the user, stored, or processed internally.
5. If destination restrictions are inadequate, the request may reach an unintended resource.

**Example architecture:**

```
Researcher
    |
    | Supplies a URL
    v
Web Application
    |
    | Backend makes request
    v
Internal / External Destination
    |
    | Response
    v
Web Application
    |
    v
Researcher
```
The security impact depends on the destination, the server’s network permissions, the response handling, and the application’s authentication boundaries.

## 4. Common Places to Look for SSRF

During an authorized assessment, pay attention to features that cause the backend to retrieve or process remote resources.

## A. URL Preview Features

Applications that generate website previews may fetch user-supplied URLs.

Examples:

- Link preview generators
- Social media URL previews
- Website metadata extractors

## B. Image and File Import

Look for functionality that imports remote content.

Examples:

- Import image from URL
- Upload from external link
- Remote document processing
- PDF conversion services

## C. Webhook Configuration

Webhook features may allow users to configure destinations where the application sends requests.

Check whether destination validation and authorization are properly enforced.

## D. PDF and Screenshot Generators

Some services render external URLs to generate screenshots, PDFs, or reports.

These features may make requests from the backend or a browser-rendering service.

## E. API Integrations

Look for API parameters such as:

```
{
  "url": "https://example.org",
  "callback_url": "https://example.org/callback",
  "image_url": "https://example.org/image.png",
  "webhook_url": "https://example.org/webhook"
}
```
These parameter names are only indicators. Their presence does not prove SSRF.

## 5. Practical SSRF Testing Methodology

Always test only within the program’s authorized scope. Prefer a researcher-controlled domain or an approved interaction endpoint.

## Step 1: Identify URL-Handling Parameters

Browse the application and identify features that accept URLs.

Use Burp Suite to intercept the relevant requests.

Example:

```
POST /api/import HTTP/1.1
Host: target.example
Content-Type: application/json
```
```
{
  "image_url": "https://researcher-controlled.example/test.png"
}
```
## Step 2: Establish a Baseline

Submit a normal, publicly accessible URL that you control.

Observe:

- Does the application make a server-side request?
- Does your controlled endpoint receive a request?
- What HTTP method is used?
- Are headers or other metadata forwarded?
- Does the application return fetched content?

A request appearing in your browser is not proof of SSRF. Confirm that the request originates from the application’s backend or its processing infrastructure.

## Step 3: Use a Controlled Interaction Endpoint

Use a domain or callback service you own or are explicitly authorized to use.

For example:

`https://researcher-controlled.example/ssrf-test`
Monitor incoming DNS and HTTP interactions.

A callback can help establish that the application or its backend attempted to resolve or access the supplied destination.

However, DNS-only interaction does not automatically prove that an HTTP request was completed or that sensitive resources were accessed.

## Step 4: Check Destination Validation

In an authorized test environment, assess whether the application restricts destinations appropriately.

Review:

- Whether only expected URL schemes are accepted.
- Whether destination hostnames are allowlisted.
- Whether resolved IP addresses are checked.
- Whether private, loopback, link-local, and other restricted address ranges are blocked.
- Whether redirects are revalidated.
- Whether DNS resolution and the actual connection are protected against rebinding.

Do not probe cloud metadata endpoints, internal production services, or other sensitive destinations unless the program explicitly authorizes those tests.

## Step 5: Evaluate the Actual Impact

A strong SSRF report should explain what the attacker can achieve.

## Get cyb3rD1vvy@’s stories in your inbox

Join Medium for free to get updates from this writer.

Potential impacts include:

- Access to restricted internal services.
- Exposure of sensitive information.
- Unauthorized interaction with internal APIs.
- Access to cloud instance metadata, where explicitly authorized and safely demonstrated.
- Server-side actions against destinations that trust internal network requests

A URL parameter accepting arbitrary input is not sufficient evidence of a vulnerability.

## 6. Types of SSRF

## A. Basic SSRF

The application makes a server-side request to a destination controlled by the user, and the response is visible or otherwise observable.

## B. Blind SSRF

The application makes a server-side request, but the response is not returned to the user.

Researchers may identify it through controlled DNS or HTTP callbacks.

## C. Second-Order SSRF

The application stores a supplied URL and processes it later.

For example, a user submits a URL while configuring an integration, but the backend fetches it during a scheduled job.

## D. Redirect-Based SSRF

The application follows redirects from an initially accepted URL.

If redirect destinations are not validated, a seemingly safe URL may lead the backend to an unintended destination.

## 7. Common SSRF Testing Mistakes

Not every suspicious response is SSRF.

Avoid these mistakes:

**1. Treating every URL parameter as vulnerable**

A URL field may be processed entirely by the browser. Verify server-side behavior.

**2. Relying only on response differences**

A different status code or response time does not independently prove SSRF.

**3. Ignoring redirects**

A destination may appear safe initially but redirect elsewhere. Test redirect handling only with controlled destinations.

**4. Confusing DNS interaction with full SSRF impact**

DNS resolution is useful evidence, but it does not prove that the backend successfully fetched sensitive content.

**5. Claiming cloud metadata exposure without proof**

Never report metadata access based only on the possibility that a server runs in a cloud environment.

**6. Testing outside program authorization**

Do not access internal systems, credentials, metadata services, or third-party infrastructure without explicit permission.

## 8. Example Vulnerability Report

## Title

Server-Side Request Forgery (SSRF) in the Remote Image Import Functionality

**Severity:** Depends on demonstrated impact

**Category:** Server-Side Request Forgery

**CWE:** CWE-918 — Server-Side Request Forgery (SSRF)

**OWASP Mapping:** OWASP Top 10:2021 — A10: Server-Side Request Forgery (SSRF)

## Description

During the security assessment, a potential Server-Side Request Forgery vulnerability was identified in the remote image import functionality.

The application accepts a user-controlled URL and processes it through a backend request. Testing with a researcher-controlled endpoint confirmed that the application initiated a request from its server-side infrastructure.

The destination validation controls should be reviewed to ensure that requests are restricted to authorized destinations and cannot be redirected to internal or otherwise restricted resources.

## Steps to Reproduce

1. Log in to the authorized test application if authentication is required.
2. Navigate to the remote image import functionality.
3. Intercept the request using Burp Suite.
4. Supply a URL hosted on a researcher-controlled domain.
5. Submit the request.
6. Monitor the controlled endpoint for incoming DNS or HTTP interactions.
7. Record the evidence demonstrating the server-side request.

## Impact

If destination restrictions can be bypassed, an attacker may be able to cause the backend to interact with unintended network resources.

Depending on the server’s network access and the application’s response handling, this could lead to internal service exposure, sensitive information disclosure, or unauthorized interactions with internal systems.

## Remediation

- Enforce a strict allowlist of permitted destinations.
- Permit only necessary URL schemes, preferably HTTPS where appropriate.
- Resolve hostnames and validate all resulting IP addresses.
- Block loopback, private, link-local, and other restricted address ranges.
- Revalidate every redirect destination.
- Protect against DNS rebinding and time-of-check/time-of-use issues by validating the address actually used for the connection.
- Use network-level egress restrictions.
- Avoid returning raw internal responses to users.
- Apply authentication and authorization checks to URL-fetching functionality.

**Note:** Adjust the report’s impact and severity to match the evidence actually obtained. A controlled callback alone may demonstrate server-side interaction, but does not establish access to internal resources.

## 9. Developer Checklist: Preventing SSRF

Developers should review the following controls:

- Validate and allowlist destination hostnames.
- Restrict URL schemes.
- Resolve and validate IP addresses before connecting.
- Block private, loopback, and link-local destinations.
- Revalidate redirect destinations.
- Protect against DNS rebinding.
- Apply outbound network restrictions.
- Use safe HTTP client configurations.
- Avoid exposing internal response data.
- Log and monitor suspicious outbound requests.

## 10. Useful Tools for SSRF Research

ToolPurposeBurp SuiteIntercept and modify HTTP requestsInteractshDetect controlled DNS and HTTP interactionscurlValidate HTTP behavior against controlled endpointsOWASP ZAPAssist with web application testingDNS toolsInspect hostname resolutionBrowser Developer ToolsUnderstand client-side request behavior

Use these tools only against authorized targets and controlled destinations.

## 11. Final Thoughts

SSRF is not simply about changing a URL parameter.

The real skill is understanding how an application makes outbound requests, what destinations it trusts, how redirects are handled, and what the backend can access.

For bug bounty hunters, the difference between a weak SSRF observation and a strong vulnerability report is **demonstrated impact**.

Always establish the server-side request, validate the security boundary, and document the impact without accessing resources beyond your authorization.

Remember: A convincing report is built on evidence, not assumptions.

## Tomorrow: Day 11 — XML External Entity (XXE) Injection

Next, we will explore how unsafe XML parsing can expose local files, trigger unintended server-side requests, and create serious security risks.

**From P4 to P1 — Keep learning. Keep testing. Keep reporting responsibly.**

Follow along for the next part of the series.:)
