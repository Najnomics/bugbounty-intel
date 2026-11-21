# From Shodan to Securing Government Systems

- **Source URL:** https://medium.com/@eclipsedmarauder/from-shodan-to-securing-government-systems-bfla-stored-xss-write-up-ab3bfd4e703d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260412182335/https://medium.com/@eclipsedmarauder/from-shodan-to-securing-government-systems-bfla-stored-xss-write-up-ab3bfd4e703d
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10506 (id 10506)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From Shodan to Securing Government Systems: BFLA + Stored XSS Write-Up

This is a real security assessment case study. All sensitive details (IPs, domains, ports, and full malicious payloads) have been sanitized for responsible disclosure.


## 1. Background & Engagement

While conducting a **black-box security assessment**, I discovered a **publicly exposed API** belonging to a **Mauritanian government system**.

The discovery originated from **Shodan**, a search engine for internet-connected devices and services. Upon closer inspection, I uncovered a **critical vulnerability chain**:

- **BFLA (Broken Function Level Authorization)** — allowing unauthenticated API calls.
- **Stored XSS (Cross-Site Scripting)** — enabling arbitrary JavaScript execution in admin browsers.
- **CSP Misconfiguration** — making the XSS payload fully executable.
- **Logical DoS Potential** — through uncontrolled mass insertion of records.

I had the permission from the govern to try all this and report it.

## 2. Black-Box Methodology

This engagement followed a **black-box** approach:

- **No prior knowledge** of the infrastructure, source code, or credentials.
- Reconnaissance using only **OSINT** (Shodan, banner grabbing, public files).
- Exploitation purely from the **external attack surface**.

## 3. Discovery via Shodan

**Shodan** indexes banners, titles, SSL certificates, and responses from exposed services. By running queries such as:

```
http.title:"Swagger UI"
"JHipster" port:8080
hostname:"example.gov.com"
```
I located a host running a JHipster-based application with:

- An open API port accessible worldwide.
- SSL certificate data linked to a government domain.
- API endpoints visible to the internet.

## 4. Reconnaissance

The `/robots.txt` file exposed several sensitive API paths:

Most returned `401 Unauthorized`, indicating authentication via token was enforced — but not everywhere.

## 5. BFLA — Broken Function Level Authorization

Probing `/api/statuts` revealed:

- `GET /api/statuts` returned full records **without authentication**.
- `POST /api/statuts` created new records **without authentication**.

This matches **OWASP API Security Top 10 — API5:2019**:

*The server did not verify if the requester was authorized to perform the action.*


Here is the proof, you can see i have repeated creations or attacks, just for some checks:

**Impact:** Any unauthenticated user could inject data into the system.

## 6. Stored XSS Injection

The `nom` field in `statuts` accepted HTML/JS without sanitization.

I crafted a sanitized PoC:

When an authenticated administrator viewed the record list, the payload executed in their browser, enabling:

- Theft of the `jhi-authenticationToken` from `localStorage`.
- Execution of arbitrary actions as the admin.

## 7. CSP Misconfiguration Deep Dive

The API responses included a **Content-Security-Policy (CSP)** header:

```
default-src 'self';
script-src * data: 'unsafe-inline' 'unsafe-eval' blob:;
```
This rendered CSP ineffective:

1. `script-src *` allowed scripts from **any domain**, including attacker-controlled hosts.
2. `'unsafe-inline'` allowed inline event handlers (`onerror`) and `<script>` blocks.
3. `'unsafe-eval'` enabled dynamic code execution.

In effect:

- My inline `<img onerror=...>` payload executed without restriction.
- External scripts from my controlled server loaded successfully.

A properly restrictive CSP (`script-src 'self' 'nonce-...'`) could have blocked both.

## 8. Logical DoS Potential

Beyond XSS, the endpoint accepted:

- Null values.
- Unlimited submissions.
- No rate limiting.

This could be exploited to:

- Flood the database with junk entries.
- Crash the admin UI with hundreds of script-laden records.

## 9. Attack Chain Summary

1. **Exposure**: API indexed on Shodan.
2. **BFLA**: Anonymous creation and retrieval of records.
3. **Stored XSS**: Malicious payload persisted in backend.
4. **CSP Failure**: Payload executed in admin’s browser.
5. **Privilege Escalation**: Stolen session tokens enabled high-level access.
6. **Logical DoS**: Potential service degradation.

## Final Note

This case demonstrates how a **single overlooked endpoint** can compromise an entire system, and how proactive testing and responsible disclosure can lead to real-world security improvements.

Follow me for more, thanks!!
