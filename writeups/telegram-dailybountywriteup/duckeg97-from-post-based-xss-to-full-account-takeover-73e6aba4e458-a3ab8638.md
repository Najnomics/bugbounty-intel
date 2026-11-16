# From POST-Based XSS to Full Account Takeover

- **Source URL:** https://medium.com/@duckeg97/from-post-based-xss-to-full-account-takeover-73e6aba4e458
- **Fetched from:** https://medium.com/feed/@duckeg97
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14962)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**بسم الله الرحمن الرحيم — وَمَا بِكُم مِّن نِّعْمَةٍ فَمِنَ اللَّهِ**

### collab with [Alharbe0](https://medium.com/@Alharbe0)

*A reflected XSS chained with authenticated account-management functionality.*

### Overview

During security testing of a web application (**Target**), I discovered a POST-based reflected XSS in:

POST /team/invite/accept

The endpoint reflected attacker-controlled POST parameters into its HTML response without proper output encoding. By delivering a crafted form, I was able to trigger JavaScript execution in the target’s origin.

The exploitation required addressing three challenges: WAF filtering, an existing Content Security Policy (CSP), and the application’s CSRF-token flow. The XSS could then be chained with authenticated account-management functionality, creating a path to account takeover.

### 1. WAF Evasion

The WAF initially interfered with the crafted payload. I represented the payload’s characters as HTML entities in the attacker-controlled form. The browser decoded those character references while parsing the form, allowing the resulting value to be submitted in the POST request.

This helped evade the WAF in the tested configuration. The underlying application issue was still **improper contextual output encoding**: the server reflected the submitted value into HTML without safely encoding it.

### 2. XSS PoC

The following proof of concept submits a crafted firstname value to the vulnerable endpoint. Replace target.example with the authorized test host and provide valid test values for any required fields.

\<!DOCTYPE html>

\<html lang="en">

\<body>

\<form action="https://target.example/team/invite/accept"

method="POST"

id="poc">

\<input name="firstname"

value="as"><img src=1 onerror="alert(1)"></svg> "">

\<input name="lastname" value="test">

\<input name="password" value="TEST\_VALUE">

\<input name="hash" value="VALID\_TEST\_HASH">

\</form>

\<script>

document.getElementById('poc').submit();

\</script>

\</body>

\</html>

The encoded firstname value is intended to demonstrate whether the reflected input can escape its original HTML context and trigger JavaScript execution. The alert(1) payload is non-destructive and serves only as an execution marker.

### 3. JavaScript Proof of Execution

For a separate JavaScript file, the following benign payload can be used to confirm execution. It does not read account data or modify the victim’s account.

```
(() => {
  console.log('XSS proof of execution on Target');
  document.title = 'XSS PoC executed';
  alert('XSS proof of execution');
})();
```
In the original test, the injected markup loaded JavaScript from external testing infrastructure. The target’s CSP did not prevent the demonstrated execution path in the tested configuration. This does not mean every CSP is bypassable; the effective directives and permitted script sources determine its protection.

### 4. Handling CSRF Token State

After confirming XSS, my initial attempt to change account information did not succeed because the application required the appropriate token state.

I used a hidden, same-origin iframe to load the internal page:

/account/user

After the page initialized, the script continued with the authenticated requests. This allowed the application’s page initialization and token-handling flow to run before the account modification request.

### 5. Chaining the XSS with Account Management

The application exposed authenticated user information through:

GET /dashboard/api/userinfo

The response contained the current user’s userId. Account updates were handled through the GraphQL endpoint:

POST /graphql

In the tested chain, the user ID was retrieved dynamically, and the account-management flow was used to change the email address. After verifying the new address through the controlled mailbox, the password-recovery process provided a path to account takeover.

The end-to-end chain was:

**POST-based XSS → WAF evasion → JavaScript execution despite the tested CSP → same-origin iframe for token initialization → retrieve user ID → change email → verify email → password recovery → account takeover.**

The account-changing JavaScript is intentionally not included in this public PoC; the HTML and JavaScript snippets above demonstrate the XSS without automating account modification or takeover.

### Impact

The issue went beyond reflected XSS. In the tested environment, the XSS could be chained with authenticated account-management functionality to change the victim’s email address and create a path to full account takeover. The victim’s user ID did not need to be known in advance because it was retrieved from the authenticated session.

### Conclusion

This finding shows how a POST-based reflected XSS can become much more serious when chained with authenticated application functionality. Entity encoding helped the test payload pass the WAF, the configured CSP did not stop the observed execution path, and a same-origin iframe allowed the application’s token initialization flow to run before the account update.

The primary fix is to prevent the original injection through proper output encoding, supported by a restrictive CSP and stronger controls for sensitive account changes.

**Disclosure note:** The target’s identity has been anonymized. Remove personal information, account identifiers, tokens, and other sensitive data from any screenshots or video before publication. Publish only in accordance with the applicable disclosure agreement.

### Responsible Disclosure

I reported the vulnerability through the appropriate security reporting channel.

**Under Review on 2026–09–15 17:07 Need More Info on 2026–09–30 13:32 Accepted on 2026–10–18 22:05**

Happy hunting! 🔐
