# API Security Top 10 (2023)

- **Source URL:** https://medium.com/@fmn.flame/dvapi-a-step-by-step-walkthrough-of-the-owasp-api-security-top-10-2023-a62859e021f9
- **Fetched from:** https://medium.com/feed/@fmn.flame
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14985 (id 14985)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*A practical, step-by-step exploitation walkthrough of OWASP’s official DVAPI (Damn Vulnerable API) project — covering Broken Object Level Authorization, Broken Authentication, Broken Object Property Level Authorization, Unrestricted Resource Consumption, Broken Function Level Authorization, Unrestricted Access to Sensitive Business Flows, SSRF, Security Misconfiguration, Improper Inventory Management, and Unsafe Consumption of APIs.*

### Introduction

DVAPI is OWASP’s own “Damn Vulnerable API” — built specifically to map 1:1 onto the **OWASP API Security Top 10 (2023)** list. This post documents exactly how we exploited each of the ten categories against a local DVAPI instance:

192.168.0.180:3000  (also reachable as localhost:3000)

including the dead ends and recon steps that got us there, not just the final payloads.

**Tools used:** — **Caido** — proxy/intercept, Replay (hand-editing and resending requests), Automate (mass/brute-force requests) — **Postman** — DVAPI’s own collection, organized by User, Notes, Challenges, Scores, and Tickets - **jwt\_tool** — cracking the JWT signing secret and forging tokens - **dd** — generating an oversized file for the resource-consumption test - **Browser / DVAPI UI** — confirming real-world impact of SSRF and mass assignment visually (scoreboard, notes panel)

### API1:2023 — Broken Object Level Authorization

**How we solved it:**

We logged into DVAPI as our own low-privilege test account and opened Postman’s Notes > Get Note request, which calls GET /api/getNote?username=\<name>.

Sent as-is (with our own username), it correctly returned only our own note — so far, nothing unusual.

The interesting part was that username is a plain, client-controlled **query parameter**, not something derived from our session server-side. We simply swapped it:

GET /api/getNote?username=admin

No ownership check kicked in. The server returned admin's note directly to our unrelated, non-admin session:

`{ "status": "success", "note": "flag{bola_15_ev3rywh3r3}" }`
**Root cause:** notes are looked up purely by the client-supplied username, with no check that it matches the authenticated session.

**Fix:** derive “whose notes” from the session/token server-side, never from a client-supplied parameter — or at minimum verify session.user == requested.username before returning data.

### API2:2023 — Broken Authentication

**How we solved it:**

While poking at GET /api/profile with our normal session, we got curious what would happen if the JWT was *invalid* rather than just expired, so we flipped a character in the signature portion of our captured token and resent it.

Instead of a clean "unauthorized," the server threw back a full error object revealing it uses the standard jsonwebtoken Node library and HS256 signing — plus a bonus flag confirming this itself counts as a misconfiguration (more on that under API8 below):

`{ "err": { "name": "JsonWebTokenError", "message": "invalid signature" }, "message": "Sever Misconfiguration", "flag": "flag{St4cK_tR4c3_eRR0R}" }`
Knowing it’s HS256, we took a **legitimate, correctly-signed** token we’d captured earlier and ran jwt\_tool’s dictionary-cracking mode against it, pointing it at jwt\_tool’s bundled common-secrets wordlist:

jwt\_tool "\<captured\_jwt>" -C -d /home/path/jwt\_tool/jwt-common.txt

jwt\_tool cracked the signing secret in seconds: **secret123**.

With the real secret in hand, we used jwt\_tool's claim-injection mode to build a brand-new token claiming admin rights, properly re-signed so it would pass verification:

jwt\_tool "\<captured\_jwt>" -I -pc username -pv admin -pc isAdmin -pv 'true' -S hs256 -p "secret123"

We took the resulting forged JWT and sent it as our session token on GET /api/profile. The server verified the (correct) signature, trusted the forged isAdmin: true claim, and granted full access:

`{ "status": "success", "message": "Broken Authentication", "flag": "flag{aBus1ng_w34K_s3cR3TTT}" }`
**Root cause:** a weak, dictionary-guessable JWT secret lets anyone forge arbitrarily-privileged tokens completely offline — no interaction with the server needed until the forged token is actually used.

**Fix:** use a long, high-entropy signing secret (or asymmetric RS256/ES256), rotate it periodically, and never leak internal stack traces that hint at the signing library/algorithm in use.

### API3:2023 — Broken Object Property Level Authorization

**How we solved it:**

We opened Postman’s User > Register request. The documented body only has username and password.

We'd already noticed (while browsing the public Scoreboard page) that user accounts carry a score value. That raised the question: is score settable by the client at registration, even though it's undocumented?

We tested it directly — registering a brand-new account named DarkKnight with an extra, undocumented top-level field added to the JSON body:

`{ "username": "DarkKnight", "password": "123456", "score": "100000000" }`
The server accepted it without any validation error:

`{ "status": "success", "message": "Registration successful" }`
We checked the Scoreboard page in the browser (and confirmed via GET /api/scores in Postman) — DarkKnight now sat at the very top with **100,000,000** points, dwarfing every legitimate score, and the scores response itself returned the flag:

`{ "username": "DarkKnight", "score": 100000000, ..., "flag": "flag{br0k3n_oBj3cT_Pr0p3rTy_L3v3L_Auth0RiS4Ti0N}" }`
**Root cause:** the registration endpoint exposes/accepts a sensitive property (score) that should only ever be set by server-side game logic, never by client input.

**Fix:** use explicit allow-lists per endpoint for which properties a client may set or read — privileged fields like scores, balances, or roles should never be client-writable.

### API4:2023 — Unrestricted Resource Consumption

**How we solved it:**

We checked the User > Upload ProfilePic request (POST /api/profile/upload) and noticed no documented file-size limit anywhere.

To test the theory, we generated a deliberately oversized 60 MB junk file on disk:

dd if=/dev/zero of=hacker.jpg bs=1M count=60

In Postman, we switched the upload request’s body to form-data, attached hacker.jpg as the file field, and hit Send.

The upload took about 24 seconds but completed with **no rejection whatsoever**, and the server even echoed the exact size back to us along with the flag:

`{ "message": "File uploaded successfully", "profilePic": "6af1da7483e59a4f7af49659.jpg", "size": "60.00 MB", "flag": "flag{file_size_is_important}" }`
**Root cause:** there’s no server-side (or reverse-proxy-level) cap on upload size, which in a real deployment opens the door to storage exhaustion / denial-of-service via repeated large uploads.

**Fix:** enforce strict file-size limits at both the application layer and the edge (reverse proxy / API gateway), and rate-limit the upload endpoint per user.

### API5:2023 — Broken Function Level Authorization

**How we solved it:**

Rather than guessing endpoints blindly, we sent an OPTIONS preflight request to a known user resource path, OPTIONS /api/user/Charlie (an existing seeded account), purely to see what HTTP methods the server itself claims to support there.

The response's Allow header told us far more than the UI or docs ever did:

Allow: GET, HEAD, DELETE

GET and HEAD are expected and documented. DELETE, however, is **never exposed anywhere in the UI or the Postman collection** — it's a hidden administrative function sitting on the exact same path a normal authenticated user can already reach for GET.

We tested it directly: using our own regular (non-admin) session's bearer token, we sent a live DELETE request against another account on the same path:

DELETE /api/user/DarkKnight

Authorization: Bearer \<our own, non-admin token>

The server didn’t reject it. It processed the deletion as if we were authorized to manage that account and handed back the flag:

`{ "status": "success", "message": "User deleted successfully", "flag": "flag{n0_fUncTi0N_L3v3L_aUtH???}" }`
**Root cause:** function-level checks (which *roles* may call which *HTTP methods*) aren’t enforced consistently across the same resource path. The exact same route that correctly requires nothing more than “logged in” for GET also accepts DELETE from that same low-privilege session — a normal user can delete *any* other account, not just their own.

**Fix:** gate every HTTP method on a resource with its own explicit role/permission check; “authenticated” is not the same as “authorized to delete this resource.

### API6:2023 — Unrestricted Access to Sensitive Business Flows

**How we solved it:**

Browsing Postman’s Tickets folder, we found POST /api/addTicket — a support/entry-ticket submission endpoint. Submitting one manually worked exactly as expected, with no visible limit mentioned anywhere.

To test whether the *business flow itself* was rate-limited (as opposed to just the HTTP layer), we loaded the raw request into Caido's **Automate** panel, kept our normal authenticated session's cookie/token unchanged, set the payload to a static/null value, and configured it to generate **1,000 payloads**.

We ran it. All 1,000 requests fired back-to-back with no delay, and every single one came back 200 OK — no throttling, no CAPTCHA, no per-user cap kicked in at any point.

The final response confirmed what we'd just proven:

`{ "msg": "Unrestricted Access to Sensitive Business Flows", "flag": "flag{n0_r4t3_L1m1T?}" }`
**Root cause:** a business-critical flow (ticket/entry creation) can be automated and spammed at scale — in a real system this could mean raffle manipulation, inventory exhaustion, or spam at the business-logic layer, not just an infrastructure-level DoS.

**Fix:** apply business-flow-aware rate limiting (e.g., N tickets per user per hour), add CAPTCHA on repeated actions, and monitor for abnormal request velocity on sensitive flows specifically (not just overall traffic).

### API7:2023 — Server-Side Request Forgery (SSRF)

**How we solved it:**

We found the “Update Note With Link” feature on the DVAPI dashboard, backed by POST /api/addNoteWithLink — it takes a URL and fetches its content server-side to use as the note text.

We first tested it with a normal public URL (https://example.com/note.txt) just to confirm the server really does fetch server-side rather than client-side — it did; the note was populated with that page's content.

Suspecting the URL parameter had no allow-list, we loaded the request into Caido's **Automate** panel and swept a small list of internal/candidate targets through the url parameter (loopback addresses on various ports, internal service names, etc.) instead of manually guessing one at a time.

One of those internal targets returned a 200 OK with the note field populated directly with the flag, confirming the backend reached a resource it should never have been able to touch on our behalf:

`{ "status": "success", "message": "Successfully added a note", "note": "flag{55RF_c4n_wR3AK_h4v0c}" }`
**Root cause:** the server makes outbound requests to a URL fully controlled by the client, with no allow-list/deny-list stopping it from reaching internal hosts or local resources.

**Fix:** restrict this feature’s outbound requests to an explicit allow-list of external domains, block requests to private IP ranges/localhost/link-local metadata addresses, and disable dangerous URL schemes.

### API8:2023 — Security Misconfiguration

**How we solved it:**

This flag actually surfaced as a side effect of the API2 testing above: when we sent a request with a tampered/invalid-signature JWT to a protected endpoint, the server didn’t fail cleanly — it returned its **entire internal error object**, stack trace included:

```
{
  "status": "error",
  "err": {
    "name": "JsonWebTokenError",
    "message": "invalid signature",
    "stack": "JsonWebTokenError: invalid signature\n    at /app/node_modules/jsonwebtoken/verify.js:171:19\n    at module.exports [as verify] (/app/node_modules/jsonwebtoken/verify.js:97:14)\n    at exports.verifyToken (/app/controllers/auth.js:79:25)\n ..."
  },
  "message": "Sever Misconfiguration",
  "flag": "flag{St4cK_tR4c3_eRR0R}"
}
```
That one response leaks the exact Node.js module versions in use (jsonwebtoken), the internal file layout (/app/controllers/auth.js), and the full Express middleware call chain — all of it useful recon for chaining further attacks, and none of it something a production API should ever hand back to a client.

**Root cause:** the application runs with verbose/debug-level error handling rather than a production-safe configuration.

**Fix:** disable detailed stack traces outside local development, return generic error messages to clients, and log full details only server-side where they belong.

### API9:2023 — Improper Inventory Management

**How we solved it:**

Postman’s Challenges > All Challenges request documents a single accepted body: {"released": 1}, which returns the 11 publicly listed challenges.

On the hunch that a developer might have left an internal/QA toggle in the same handler, we tried swapping the key to something a backend team might realistically use while challenges are still being staged: {"unreleased": 1}.

The server didn't reject the unknown field — it returned a **12th challenge** that's never linked anywhere in the normal UI flow, flag baked right into its description text:

```
{
  "id": 12,
  "challengeName": "Challenge12",
  "shortDescription": "This is challenge12 flag{a553Ts_m4N4g3m3NT_g0n3_wR0ng}"
}
```
**Root cause:** an internal/staging parameter (unreleased) was left reachable in production on the same public endpoint, exposing inventory (here, a hidden challenge — in a real API this is just as easily an unreleased feature, a beta endpoint, or internal admin tooling) that should never be client-accessible.

**Fix:** maintain a strict API inventory and environment separation; internal-only parameters and routes should never ship to production, and if they must exist, they belong behind internal network access plus strong auth.

### API10:2023 — Unsafe Consumption of APIs

**How we solved it:**

The normal login flow (POST /api/login) expects {"username": "...", "password": "..."} as plain strings, submitted via the login form.

Instead of using the browser form, we crafted the request body by hand in Caido Replay and swapped the password value from a string into a MongoDB query **operator object**:

`{ "username": "admin", "password": { "$ne": 1 } }`
Because the backend passes this object straight into a MongoDB-style query filter (password: { $ne: 1 } — "password is not equal to the number 1"), and any real stored password hash is, in fact, not equal to 1, the condition evaluated to true for every account — authentication was bypassed entirely without knowing any real password:

`{ "status": "success", "message": "Authentication successful", "flag": "flag{eZ_n0SQLi_pWn}" }`
**Root cause:** the API “consumes” client-provided input structurally — trusting its *shape* as query logic rather than validating it as a plain value — a classic NoSQL injection enabled by unsafe trust in the type of incoming data, not just its content.

**Fix:** strictly type and sanitize every input field before it reaches a database query (reject non-string values for fields expected to be strings), and use parameterized/sanitized query builders instead of passing raw client objects into query operators.

### Summary Table

- **API1 — Broken Object Level Authorization** → flag{bola\_15\_ev3rywh3r3}
- **API2 — Broken Authentication** → flag{aBus1ng\_w34K\_s3cR3TTT}
- **API3 — Broken Object Property Level Authorization** → flag{br0k3n\_oBj3cT\_Pr0p3rTy\_L3v3L\_Auth0RiS4Ti0N}
- **API4 — Unrestricted Resource Consumption** → flag{file\_size\_is\_important}
- **API5 — Broken Function Level Authorization** → flag{n0\_fUncTi0N\_L3v3L\_aUtH???}
- **API6 — Unrestricted Access to Sensitive Business Flows** → flag{n0\_r4t3\_L1m1T?}
- **API7 — Server-Side Request Forgery** → flag{55RF\_c4n\_wR3AK\_h4v0c}
- **API8 — Security Misconfiguration** → flag{St4cK\_tR4c3\_eRR0R}
- **API9 — Improper Inventory Management** → flag{a553Ts\_m4N4g3m3NT\_g0n3\_wR0ng}
- **API10 — Unsafe Consumption of APIs** → flag{eZ\_n0SQLi\_pWn}

### Conclusion

DVAPI’s ten categories read like a checklist for “ways an API quietly trusts the client too much” — trusting a username parameter, a JWT signature, a registration field, a file size, an HTTP method, a request rate, a URL, an error handler’s verbosity, an internal flag, or a data type. None of these required exotic tooling; a proxy, a brute-forcer, and a JWT cracker covered nine of the ten categories. The lesson across almost every finding is the same: **validate on the server, not the client — and validate everything, not just the happy path.**

*Lab: DVAPI (OWASP Damn Vulnerable API) — all testing performed against a local, intentionally vulnerable instance for educational purposes only.*
