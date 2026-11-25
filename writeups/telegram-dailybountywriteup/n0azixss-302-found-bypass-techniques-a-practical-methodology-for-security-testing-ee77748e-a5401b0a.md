# 302 Found & Bypass Techniques

- **Source URL:** https://medium.com/@N0aziXss/302-found-bypass-techniques-a-practical-methodology-for-security-testing-ee77748ecf6d
- **Fetched from:** https://medium.com/@N0aziXss/302-found-bypass-techniques-a-practical-methodology-for-security-testing-ee77748ecf6d?source=rss-ef3c608c2595------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14923 (id 14923)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** N0aziXss / Fri, 25 Sep 2026 02:34:29 GMT

Systematic Approach to Identifying Redirect Misconfigurations and Control Flow Vulnerabilities

By N0aziXss | Security Researcher | HackerOne & BugCrowd Validated

HTTP 302 is one of the most common response codes on the web. It signals a temporary redirect — “the resource you want is over there.” Developers use it for login flows, URL normalization, and post-action navigation.

But here’s what most people miss: A 302 response is not just a navigation instruction. It is a complete HTTP message with a status code, headers, and a body. If the server sends a 302 but continues executing sensitive backend logic, that logic may leak into the response body. Browsers follow the redirect and hide it. Tools like Burp Suite show the truth.

A redirect is a navigation signal.

It is NOT an access control mechanism.

Treating it as one creates vulnerabilities.

✓ Understanding 302 and its role in access control

✓ Vulnerability map: how misconfigured redirects become exploits

✓ Systematic testing methodology

✓ Bypass techniques (observation-based, not code-based)

✓ Remediation and prevention

**Disclaimer:** This article is for educational and authorized security testing only. Do not test systems without explicit permission.

HTTP 302 Found

- Semantics: "The resource is temporarily located elsewhere"

- Requires: Location header with target URL

- Client behavior: Follows Location automatically

- Server behavior: Should stop processing after sending redirect

❌ WRONG: "If I send a 302, the request is over."

✅ RIGHT: "Sending a 302 does not terminate server-side execution."

In many frameworks, code after a redirect call continues to run unless

explicitly stopped. This is the foundation of several vulnerability classes.

"302 Forbidden" is not a standard HTTP status code.

It appears when:

- A WAF or proxy returns a 302 redirect to a block page

- An application redirects unauthenticated users to login

- A misconfigured server redirects to an error page

The presence of "302" in logs where "403" is expected is a red flag.

It often indicates that access control is enforced by redirect,

not by termination of processing.

┌─────────────────────────────────────────────────────────────────────┐

│ REDIRECT VULNERABILITY MAP │

└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────┐

│ Misconfigured 302 │

└──────────┬──────────┘

│

┌──────────────────────┼──────────────────────┐

│ │ │

▼ ▼ ▼

┌───────────────┐ ┌───────────────┐ ┌───────────────┐

│ Execution │ │ Open Redirect │ │ SSRF via │

│ After │ │ │ │ Redirect │

│ Redirect │ │ │ │ │

└───────┬───────┘ └───────┬───────┘ └───────┬───────┘

│ │ │

▼ ▼ ▼

┌───────────────┐ ┌───────────────┐ ┌───────────────┐

│ Auth Bypass │ │ Phishing │ │ Internal │

│ Data Leakage │ │ Token Theft │ │ Network │

│ │ │ │ │ Access │

└───────────────┘ └───────────────┘ └───────────────┘

Definition:

Server sends a 302 redirect, but continues executing sensitive code

and writes protected content into the response body.

Root Cause:

- Missing return/exit after redirect call

- Incorrect assumption that redirect stops execution

- Framework-specific behavior (PHP header(), etc.)

Impact:

- Full authentication bypass

- Sensitive data exposure

- Admin panel access without credentials

A PHP application checks if a user is logged in. If not, it sends a 302 redirect to the login page. However, the code after the redirect continues to run and outputs the full dashboard HTML. An attacker using curl or Burp Suite can read the response body — which contains the protected content — even though the status code says 302.

Definition:

Application accepts user-controlled input as a redirect target

without proper validation.

Common Parameters:

redirect, redirect\_to, return, return\_to, next, goto, url, target, dest

Impact:

- Phishing from trusted domain

- OAuth/SSO token theft

- Bypass of URL-based security controls

**OWASP Classification:** Unvalidated Redirects and Forwards (formerly A10, now part of Broken Access Control).

Definition:

Server uses the Host header to construct redirect URLs

without validation.

Attack Vector:

Attacker sends request with modified Host header

Server responds with 302 to attacker-controlled domain

Impact:

- Password reset link hijacking

- Cache poisoning

- Phishing

Definition:

SSRF protection validates only the initial URL.

When the server follows a 302 redirect, the new target is not validated.

Attack Vector:

1. Attacker supplies URL to their own server

2. Server validates it (external, safe)

3. Attacker's server returns 302 to internal address

4. Server follows redirect to internal network

Impact:

- Access to internal services

- Cloud metadata exposure

- Full internal network mapping

Definition:

A 302 response with attacker-controlled Location header

gets cached and served to other users.

Attack Vector:

1. Attacker triggers 302 with malicious Location

2. Response is cached

3. Other users receive the cached redirect

Impact:

- Mass phishing

- Token theft

- Session hijacking

\# Identify redirect behavior in the application

1. Browse the application normally

2. Note every 3xx response (301, 302, 303, 307, 308)

3. Record the endpoint, parameters, and Location target

Tools to observe:

- Browser DevTools (Network tab)

- Burp Suite (Proxy history)

- curl with -v flag

- OWASP ZAP

What to look for:

- Login/Logout redirects

- Password reset flows

- Post-action navigation

- URL normalization (e.g., adding trailing slash)

- HTTP to HTTPS redirects

\# Non-intrusive EAR testing

1. Identify a protected endpoint (e.g., /admin, /dashboard)

2. Request it WITHOUT authentication

3. Observe the response

Key indicators of EAR:

- Status code is 302

- Location header points to login page

- BUT response body is non-empty and contains protected content

Verification:

- Compare response size for authenticated vs unauthenticated

- If unauthenticated response body contains sensitive strings,

EAR is confirmed

Example observation:

HTTP/1.1 302 Found

Location: /login

Content-Length: 15432

\[Response body contains full dashboard HTML\]

**Note:** This is observation-based testing. You are reading what the server sends. No exploitation tools are required.

\# Systematic open redirect testing

1. Identify redirect parameters:

- URL parameters (redirect=, next=, return=)

- Form fields

- Headers (Referer, Host)

2. Test with external URLs:

- redirect=https://example.com

- redirect=//example.com

- redirect=///example.com

3. Document behavior:

- Does the server redirect externally?

- Is there validation? (blocked? filtered?)

- What bypass techniques work?

\- URL encoding: %2F%2Fexample.com

- Double encoding: %252F%252Fexample.com

- Backslash: \\example.com

- Userinfo: https://example.com@attacker.com

- Subdomain: https://attacker.com.example.com

- Fragment: https://example.com#attacker.com

\# Test if Host header influences redirects

1. Send request with modified Host header:

Host: attacker.com

2. Observe 302 Location:

- Does it point to attacker.com?

- Is the Host reflected in the redirect?

3. Test variations:

- X-Forwarded-Host

- X-Forwarded-Server

- Forwarded header

4. Document which headers are trusted

\# Test if SSRF protection follows redirects

1. Identify URL-fetching functionality:

- Image import from URL

- Webhook configuration

- Document conversion

- URL preview generation

2. Supply a URL to a server you control

3. Return a 302 redirect to an internal address

4. Observe if the internal address is fetched

Note: This requires an external server you control.

Do not attempt against production systems without authorization.

The "bypass" for EAR is not an exploit - it is simply not following

the redirect.

Browsers follow redirects automatically and hide the response body.

Non-browser clients (curl, Burp, Python requests) show the full response.

Observation approach:

- Use curl -v to see headers AND body

- Use Burp Repeater to inspect raw response

- Compare authenticated vs unauthenticated response sizes

The vulnerability exists when the server returns sensitive content

alongside the 302. The "bypass" is reading it.

\# Common validation bypass techniques

1. Protocol-relative URLs:

//attacker.com

2. Backslash injection:

\\attacker.com

\/attacker.com

3. @ symbol abuse:

https://trusted.com@attacker.com

4. Subdomain confusion:

https://attacker.com.trusted.com

https://trusted.com.attacker.com

5. URL encoding:

%2F%2Fattacker.com

%5C%5Cattacker.com

6. Whitespace/control characters:

%09attacker.com

%0d%0a//attacker.com

7. Trusted domain in path:

https://attacker.com/trusted.com

https://attacker.com?trusted.com

\# When Host header is validated

1. Add port: Host: trusted.com:8080

2. Use IPv6: Host: \[::1\]

3. Case variation: Host: TRUSTED.COM

4. Trailing dot: Host: trusted.com.

5. Multiple Host headers

6. X-Forwarded-Host fallback

\# Using multiple redirects to bypass validation

Step 1: Trusted endpoint that redirects to user input

Step 2: Your input redirects to external

Step 3: External redirects to final target

This bypasses validation that only checks the first hop.

❌ VULNERABLE:

if (!authenticated) {

header("Location: /login");

// code continues…

}

output\_sensitive\_data();

✅ FIXED:

if (!authenticated) {

header("Location: /login");

exit; // or return, or die

}

output\_sensitive\_data();

**Rule:** After any redirect, immediately terminate execution.

✅ DO:

• Validate redirect targets against an allowlist

• Use relative paths only: /dashboard, /profile

• Store redirect targets server-side with indirect references

• Reject any URL containing "://" or starting with "//"

❌ DON'T:

• Accept full URLs from user input

• Use blacklists (always bypassable)

• Trust URL encoding

• Rely on client-side validation

**OWASP Guidance:** Parameters must be validated before sending 302 HTTP code. The server should maintain a relation of authorized redirections (e.g., in a database).

✅ DO:

• Disable automatic redirect following

• Validate every hop in a redirect chain

• Use a separate, isolated network for URL fetching

• Implement DNS pinning

❌ DON'T:

• Validate only the initial URL

• Trust Location headers blindly

• Allow arbitrary redirect targets

\# Defense in depth

Content-Security-Policy:

default-src 'self';

frame-ancestors 'none';

form-action 'self';

Strict-Transport-Security: max-age=31536000; includeSubDomains

X-Frame-Options: DENY

X-Content-Type-Options: nosniff

Referrer-Policy: strict-origin-when-cross-origin

□ Identify all 3xx responses in the application

□ Test for EAR: request protected endpoints without auth

- Check response body for sensitive content

- Compare authenticated vs unauthenticated response sizes

□ Test for open redirect:

- Parameter-based (redirect=, next=, return=)

- Header-based (Host, Referer)

- Form-based

□ Test Host header injection:

- Modify Host header, observe Location

- Test X-Forwarded-Host, Forwarded

□ Test SSRF via redirect:

- Identify URL-fetching features

- Test redirect following behavior

□ Test cache poisoning:

- Check if 302 responses are cached

- Manipulate Location header

□ Test OAuth/SSO redirect\_uri:

- Unsupported response\_type

- Validation bypass attempts

□ Document all findings with:

- Request/response evidence

- Risk rating

- Remediation guidance

┌─────────────────────────────────────────────────────┐

│ PHASE 1: RECON │

│ • Map all redirect endpoints │

│ • Identify parameters and headers │

│ • Understand redirect flow │

└─────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────┐

│PHASE 2: EAR TESTING │

│ • Request protected pages without auth │

│ • Inspect response body │

│ • Compare response sizes │

└─────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────┐

│ PHASE 3: OPEN REDIRECT │

│ • Test redirect parameters │

│ • Try bypass techniques │

│ • Document validation behavior │

└─────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────┐

│ PHASE 4: HEADER INJECTION │

│ • Test Host header │

│ • Test forwarded headers │

│ • Observe Location reflection │

└─────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────┐

│ PHASE 5: SSRF CHAINS │

│ • Identify URL-fetching features │

│ • Test redirect following │

│ • Document bypasses │

└─────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────┐

│ PHASE 6: DOCUMENTATION │

│ • Clear reproduction steps │

│ • Risk assessment │

│ • Remediation guidance │

└─────────────────────────────────────────────────────┘

1\. A 302 is not an access control - it's a navigation signal

2. Always inspect the response body, not just the status code

3. Test both browser and non-browser clients

4. Follow redirect chains - every hop is a potential bypass

5. Document behavior, not just presence of redirects

1\. After redirect, immediately terminate execution

2. Never trust user input for redirect targets

3. Validate every hop in a redirect chain

4. Use allowlists, not blocklists

5. Treat Host header as untrusted input

**A redirect says “go there.” It does not say “stop here.”**

**The gap between those two statements is where vulnerabilities live.**

**Understand the gap. Test the gap. Close the gap.**

N0aziXss is an experienced security researcher specializing in web application security and bug bounty hunting, with multiple validated discoveries across various platforms.
