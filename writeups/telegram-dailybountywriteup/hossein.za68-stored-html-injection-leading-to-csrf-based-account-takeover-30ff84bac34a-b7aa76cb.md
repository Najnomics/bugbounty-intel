# Stored HTML Injection leading to CSRF-based Account Takeover

- **Source URL:** https://medium.com/@hossein.za68/stored-html-injection-leading-to-csrf-based-account-takeover-30ff84bac34a?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@hossein.za68
- **Fetched:** 2026-11-18
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14119)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hi everyone 👋

Recently, during a private bug bounty program in my country, I discovered a critical issue in a blog subdomain of a web application that led to **Account Takeover (ATO)**.

The vulnerability was a combination of:

- Stored HTML Injection in comment functionality
- CSRF protection failure on a sensitive endpoint
- Misconfigured SameSite cookie behavior
- Unsafe HTTP method handling on a state-changing action

When chained together, these issues allowed any authenticated user (including administrators) to have their email address silently changed after interacting with a malicious comment.

This ultimately enabled a full account takeover via password reset.

### Application Overview

The target was a subscription-based platform providing torrent-to-direct-download conversion services, built using the **Drupal framework**.

A blog subdomain (e.g. blog.target.com) was used for announcements, discounts, and public posts.

Users were allowed to:

- View blog posts
- Leave comments under posts
- Interact with content without moderation

### Key observations:

- Comments were **auto-published immediately**
- No admin approval was required
- HTML filtering was partially implemented but incomplete

### Initial Finding: Stored HTML Injection

During testing, I noticed that the comment section was not properly sanitizing HTML input.

The following restrictions were observed:

- \<script> tags were filtered
- Most JavaScript event handlers (onerror, onload, onclick, etc.) were blocked
- However, certain HTML tags were still allowed:
- \<img>
- \<a>

This resulted in a **Stored HTML Injection vulnerability**, rather than full XSS execution.

Although JavaScript execution was not possible, HTML-based payload delivery was still feasible.

### Sensitive Functionality: Email Change Endpoint

While analyzing account settings, I intercepted the request responsible for changing the user’s email address using Burp Suite.

Key findings:

- The request used the **POST method**
- No **CSRF token** was present
- Authentication relied solely on **session cookies**

This immediately indicated a missing CSRF protection mechanism.

### SameSite Cookie Behavior Analysis

Response headers showed that no explicit SameSite attribute was set for the session cookie.

A captured response confirmed this behavior:

In modern browsers (Chrome, Edge, Firefox), when SameSite is not explicitly defined, it is treated as:

***SameSite=Lax (default behavior)***

### What SameSite=Lax actually means

Under this configuration:

- Cookies are sent on **same-site requests**
- Cookies are also sent on **top-level navigations (GET-based navigations)**
- Cookies are NOT sent on subresource requests such as:
- \<img>
- \<iframe>
- fetch / AJAX

This is an important browser-level CSRF mitigation mechanism, not a simple GET/POST restriction.

### Abuse of \<a> Tag for CSRF Triggering

A key part of this exploit was abusing the behavior of the \<a> tag.

Unlike \<img> or \<iframe>, the \<a> tag triggers a:

***Top-level navigation in the browser***

This means:

- The browser fully navigates to the target URL
- The request is treated as a legitimate user action
- Session cookies are included under SameSite=Lax rules

### Impact

This transforms the attack into a:

***User-initiated navigation-based CSRF***

Meaning user interaction (click) is required to trigger the state-changing request.

### HTTP Method Handling Issue (GET vs POST Behavior)

The email change functionality was originally designed using a POST-based form:

\<form action="/my-panel/change-email" method="POST">

\<input name="email">

\</form>

However, backend behavior was not strictly enforcing HTTP methods.

In PHP, the following implementation was observed:

$email = $\_REQUEST\['email'\];

This means:

- Both GET and POST requests are accepted
- Cookie data may also be included depending on context

If instead the code had been:

$email = $\_POST\['email'\];

Then only POST requests would be accepted.

### Root cause

The vulnerability was not simply method switching.

Rather:

*The endpoint was designed to accept state-changing input without strict HTTP method enforcement.*

### Root Cause Summary

This issue was the result of multiple security failures combined:

1. Missing CSRF protection (no anti-CSRF token)
2. Weak HTTP method validation on a sensitive endpoint
3. Stored HTML Injection enabling payload delivery

### Exploitation Payload

The final payload injected into the comment section was:

\<a href="https://target.com/my-panel/change-email?email=evil@gmail.com">

Click here to see screenshot

\</a>

To make the attack more realistic, the payload was embedded in a social engineering context:

Hi guys, I have a problem. Please check my screenshot:

\<a href="https://target.com/my-panel/change-email?email=evil@gmail.com">

Click here to see screenshot

\</a>

### Impact

Once a victim clicked the malicious link:

- Their email address was silently changed to an attacker-controlled value
- The attacker could then initiate a password reset flow
- This led to **full Account Takeover (ATO)**

### Conclusion

This vulnerability demonstrates how multiple medium-severity issues can be chained into a critical impact:

- Stored HTML Injection alone was not exploitable for XSS
- CSRF protection was missing
- HTTP method enforcement was weak
- Browser security mechanisms (SameSite=Lax) were insufficient due to navigation-based abuse

Individually, each issue may seem limited in severity — but combined, they resulted in full account compromise.

To provide a clearer understanding of the vulnerability workflow, I have included a schematic diagram at the end of this article.
