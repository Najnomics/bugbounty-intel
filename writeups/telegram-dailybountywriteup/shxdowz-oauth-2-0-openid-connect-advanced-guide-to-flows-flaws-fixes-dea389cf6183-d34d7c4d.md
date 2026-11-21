# OAuth 2.0 & OpenID Connect

- **Source URL:** https://medium.com/@shxdowz/oauth-2-0-openid-connect-advanced-guide-to-flows-flaws-fixes-dea389cf6183?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905164609/https://medium.com/@shxdowz/oauth-2-0-openid-connect-advanced-guide-to-flows-flaws-fixes-dea389cf6183
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9819 (id 9819)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# OAuth 2.0 & OpenID Connect: Advanced Guide to Flows, Flaws & Fixes

You see it everywhere: “Log in with Google,” “Sign in with GitHub,” “Allow App X to access your photos.” These familiar buttons, powering much of the modern web’s interoperability, are often driven by **OAuth 2.0**, the industry-standard framework for delegated authorization. Alongside it frequently runs **OpenID Connect (OIDC)**, an identity layer built on top of OAuth 2.0 to handle authentication.

The rise of APIs, mobile applications, Single Page Applications (SPAs), and microservices made sharing data between services essential, but doing so securely without sharing user passwords was a major challenge. OAuth 2.0 emerged as the solution, providing a standardized way for users to grant limited, controlled access to their data.

While incredibly powerful and enabling, OAuth 2.0’s flexibility and the complexity of its various flows make it a frequent source of security vulnerabilities when implemented incorrectly. Misconfigurations in grant types, improper validation of redirects, weak state parameters, or mishandling of tokens can lead to severe consequences like account takeovers, extensive data leakage, and privilege escalation.

This guide provides an advanced yet accessible deep dive into OAuth 2.0 and OIDC. We’ll explore the core concepts, dissect the different grant types (flows) in more detail, uncover common security pitfalls and exploitation techniques, and understand precisely how OIDC adds the identity layer. Whether you’re implementing, testing, or attacking OAuth flows, understanding these intricacies is crucial.

## What is OAuth? (It’s About Delegation, Not Just Login)

The most crucial concept to grasp is that **OAuth 2.0 is fundamentally an authorization framework, not an authentication protocol.** This distinction is vital for understanding its purpose and security implications.

- **Authentication:** Proving *who you are* (e.g., verifying identity via username/password, biometrics, hardware keys).
- **Authorization:** Determining *what you are allowed to do* or *what access you grant to others*, *after* you’ve been authenticated.

OAuth 2.0 allows a user (the **Resource Owner**) to grant a third-party application (the **Client**) limited access to their resources hosted on another server (the **Resource Server**), without sharing their primary credentials (like their password) for that server. This process of granting permission is mediated by an **Authorization Server**.

**The Hotel Key Card Analogy (Expanded):** Think of your password for a service (like Google) as the master key to your entire account — it opens every door. You wouldn’t hand this master key to a third-party hotel booking app just so it can check room availability or book a room for you. Instead, OAuth allows Google (acting as the Authorization Server) to issue a temporary, limited-access key card (an **Access Token**) to the booking app (Client) *after* you explicitly approve it via Google’s interface. This key card might only open the doors related to “viewing room availability” and “booking standard rooms” (these permissions are defined by **scopes**) for, say, the next hour. It doesn’t grant access to your email or settings, and it expires, protecting your master key.

**Key Roles:**

1. **Resource Owner (RO):** The end-user who owns the data/resource and grants permission.
2. **Client:** The application (e.g., web app, mobile app, SPA, CLI tool) requesting access to the Resource Owner’s data. Clients can be *confidential* (able to protect a secret, like a backend web server) or *public* (unable to protect a secret, like a browser-based SPA or mobile app).
3. **Authorization Server (AS):** The server trusted by the Resource Owner. It authenticates the RO, obtains their consent (authorization grant), and issues Access Tokens (and potentially Refresh Tokens) to the Client upon successful authorization.
4. **Resource Server (RS):** The server hosting the protected resources (e.g., an API for user data, photos, posts). It accepts and validates Access Tokens presented by the Client before granting access. (Often, the AS and RS are part of the same logical service, but they can be separate).

**Key Artifacts:**

- **Access Token:** A credential, often an opaque string or a structured format like a JSON Web Token (JWT), used by the Client to make authenticated requests to the Resource Server. Represents the specific permissions (scopes) granted by the user. Usually short-lived (minutes to hours).
- **Refresh Token:** A credential used by the Client to obtain *new* Access Tokens from the Authorization Server *without* requiring the user to go through the full login and consent flow again. Usually long-lived (days, months, or until revoked) and must be stored securely by the client. Crucial for maintaining user sessions over time.
- **Scope:** Strings that define the specific permissions the Client is requesting (e.g., `profile`, `email`, `read_calendar`, `write_posts`). The user consents to these scopes, and the issued Access Token is typically bound to them. Follows the principle of least privilege.

## How OAuth 2.0 Works: The Authorization Code Grant (+PKCE)

OAuth 2.0 defines several “grant types” or flows for obtaining tokens, tailored to different client types and scenarios. The most common, secure, and recommended flow for web applications and native/mobile apps is the **Authorization Code Grant**, which today should *always* be implemented with the **PKCE (Proof Key for Code Exchange)** extension (RFC 7636).

Here’s the typical flow, step-by-step:

1. **Initiation (Client -> AS via User’s Browser):** The Client application needs access. It constructs a URL pointing to the Authorization Server’s `/authorization` endpoint and redirects the User's browser there. This URL includes critical query parameters:

- `response_type=code`: Signals the Authorization Code flow.
- `client_id`: Public identifier for the Client application (pre-registered with the AS).
- `redirect_uri`: The specific URL on the Client application where the AS should redirect the user back *after* authorization. **(Critical security point! Must be pre-registered and validated strictly).**
- `scope`: One or more space-separated strings indicating the requested permissions (e.g., `openid profile email read_calendar`).
- `state`: A randomly generated, unpredictable, opaque value created by the Client and stored temporarily (e.g., in the user's session). Used to prevent Cross-Site Request Forgery (CSRF) by ensuring the callback originates from the user's initiated flow. **(Critical security point!)**
- `code_challenge` (PKCE): A value derived from a secret (`code_verifier`) generated by the Client. Typically `BASE64URL-ENCODE(SHA256(code_verifier))`.
- `code_challenge_method` (PKCE): Specifies the hash method used (usually `S256` for SHA256).

1. **User Authentication & Consent (User \<-> AS):** The Authorization Server receives the request. If the user isn’t already logged into the AS, it prompts them to log in. Then, it displays a consent screen showing the Client application’s name and the requested `scopes`, asking the user to approve or deny the request.
2. **Authorization Code Grant (AS -> Client via User’s Browser):** If the User approves, the Authorization Server generates a short-lived, single-use **Authorization Code**. It then redirects the User’s browser back to the `redirect_uri` provided by the Client in step 1, appending the code and the original state value: [https://client.example.com/callback?code=SplxlOBeZQQYbYS6WxSbIA&state=xyz123](https://client.example.com/callback?code=SplxlOBeZQQYbYS6WxSbIA&state=xyz123)
3. **Code-for-Token Exchange (Client Backend \<-> AS Backend):**

- The Client’s backend server receives the request at its `/callback` endpoint. It immediately **validates** the received `state` parameter against the value it stored for that user's session before step 1. If they don't match or the state is missing, the request is rejected as a potential CSRF attack.
- If the state matches, the Client’s backend makes a **secure, direct POST request** (server-to-server) to the Authorization Server’s `/token` endpoint. This request is typically authenticated using the Client's `client_id` and `client_secret` (for confidential clients) in an `Authorization` header (e.g., Basic Auth). The request body includes:
- `grant_type=authorization_code`
- `code`: The authorization code received in step 3.
- `redirect_uri`: The *same* redirect URI used in step 1 (for validation).
- `code_verifier` (PKCE): The original secret string generated by the Client in step 1.

**Token Issuance (AS Backend -> Client Backend):** The Authorization Server:

- Authenticates the Client (using client secret if applicable).
- Verifies the received `code` is valid, hasn't expired, and wasn't already used.
- Validates that the `redirect_uri` in the token request matches the one used when the `code` was issued.
- **Performs the PKCE verification:** It hashes the received `code_verifier` using the `code_challenge_method` stored from step 1 and compares the result to the `code_challenge` stored from step 1. If they match, it proves the client exchanging the code is the same one that initiated the flow. **This prevents attackers who might intercept the code (e.g., via malware, browser history) from exchanging it for tokens.**
- If all checks pass, the AS revokes the authorization code and responds with a JSON payload containing:
- `access_token`: The bearer token.
- `token_type`: Typically `Bearer`.
- `expires_in`: Lifetime of the Access Token (seconds).
- `refresh_token` (Optional, but common): The Refresh Token.
- `id_token` (If `openid` scope was requested - see OIDC section).

**API Access (Client -> Resource Server):** The Client securely stores the received tokens. It can now use the `access_token` to make requests to the Resource Server (API) on behalf of the user. It typically includes the token in the `Authorization` header: `Authorization: Bearer <access_token>` The Resource Server receives this request, extracts the token, and validates it (e.g., by checking its signature and claims if it's a JWT, or by calling an introspection endpoint on the Authorization Server). If valid and possessing the required scopes for the requested API endpoint, the Resource Server processes the request.

## Deep Dive: Other OAuth 2.0 Grant Types

While Authorization Code + PKCE is the modern standard for user-facing applications, understanding other grant types helps recognize legacy systems or specific use cases:

- **Implicit Grant (Legacy/Discouraged):**
- `response_type=token` (or `token id_token` for OIDC).
- **Why it existed:** Designed for early SPAs executed entirely in the browser, which couldn’t securely store a `client_secret` to perform the backend code-for-token exchange.
- **Flow:** Simpler flow where the AS returns the `access_token` (and `id_token`) directly in the redirect URI's *fragment identifier* (`#`), e.g., `https://client.com/callback#access_token=ABC...&state=xyz`. The client-side script extracts the token from the fragment.
- **Why it’s bad:**
- Token Exposure: The token lives in the browser’s URL bar, potentially gets logged in browser history, web server logs (via Referer headers on subsequent requests), and is accessible to malicious browser extensions or scripts (if XSS exists).
- No Refresh Tokens: Typically, refresh tokens are not issued in this flow, requiring more frequent user re-authentication.
- Less Secure: Doesn’t benefit from the backend validation step or PKCE.
- **Current Status: Deprecated** by the OAuth 2.1 draft and security best practices. SPAs and mobile apps should use Authorization Code + PKCE.
- **Resource Owner Password Credentials Grant (ROPC — Legacy/Discouraged):**
- `grant_type=password`.
- **Why it existed:** To migrate legacy applications using direct username/password logins to OAuth infrastructure without changing the user experience immediately.
- **Flow:** The Client application itself collects the user’s `username` and `password` and sends them directly to the AS's `/token` endpoint along with its own client credentials.
- **Why it’s bad:**
- Breaks Delegation Principle: Requires the user to trust the *client application* with their actual password for the resource server, completely undermining OAuth’s core benefit.
- Increased Attack Surface: Exposes user credentials to the client application, making it a high-value target. Limits the AS’s ability to implement stronger authentication methods (like MFA, WebAuthn).
- **Current Status: Deprecated** and strongly discouraged. Only ever considered acceptable for absolutely trusted first-party applications where redirect-based flows are impossible, but even then, alternatives are preferred.
- **Client Credentials Grant:**
- `grant_type=client_credentials`.
- **Flow:** Used for non-interactive, machine-to-machine (M2M) communication. The Client application authenticates itself directly with the AS using its pre-registered `client_id` and `client_secret` (or other secure methods like JWT assertions or mTLS). The AS issues an Access Token representing the *client's own authority*, not a user's.
- **Use Case:** Backend microservices calling each other, API clients performing automated tasks on their own behalf. No user involved.
- **Device Authorization Grant (RFC 8628):**
- Designed for input-constrained devices (smart TVs, IoT devices) where direct browser interaction is difficult.
- **Flow (Simplified):** Device shows user a code & URL -> User visits URL on phone/PC, logs in, enters code -> Device polls AS -> AS issues tokens to device once user approves.
- **Refresh Tokens:**
- **Purpose:** Allow clients to obtain new Access Tokens when the current one expires without forcing the user to log in again. Essential for smooth user experience.
- **Flow:** Client sends its `refresh_token` (along with client credentials for confidential clients) to the AS's `/token` endpoint with `grant_type=refresh_token`. AS validates the refresh token and issues a new `access_token` (and potentially a *new* `refresh_token` - see rotation).
- **Security:** Refresh tokens are powerful and long-lived. They MUST be stored securely by the client (e.g., encrypted in a backend database, secure storage on mobile). Implement **Refresh Token Rotation:** issue a new refresh token with each refresh and invalidate the old one immediately to detect and mitigate token theft.

## OpenID Connect (OIDC): Authentication on Top of OAuth 2.0

As established, OAuth 2.0 handles *authorization*. It doesn’t tell the Client application *who* the authenticated user is in a standardized, verifiable way. **OpenID Connect (OIDC)** fills this gap.

OIDC is a simple identity layer built directly on top of OAuth 2.0. It doesn’t replace OAuth; it extends it. When a Client needs to authenticate a user (log them in), it performs a standard OAuth 2.0 flow (like Authorization Code) but includes the specific scope `openid`.

This triggers OIDC behavior:

1. **openid**
2. **ID Token:** The Authorization Server (now also acting as an OpenID Provider) includes an **ID Token** in the response from the token endpoint, alongside the `access_token`.
3. **ID Token (JWT):** This is a JSON Web Token (JWT) signed by the Authorization Server. It contains claims (key-value pairs) about the authentication event and the user. **Crucially, the Client MUST validate the ID Token’s signature and claims.** Standard claims include:

- `iss`: Issuer Identifier (URL of the AS).
- `sub`: Subject Identifier (a stable identifier for the user at the issuer).
- `aud`: Audience (Client ID of the application the token is intended for).
- `exp`: Expiration time.
- `iat`: Issued at time.
- `nonce` (Optional but recommended): A value included in the initial authorization request and reflected in the ID Token, used to mitigate replay attacks.
- Other profile claims (`name`, `email`, `picture`, etc.) can be included if corresponding scopes (`profile`, `email`) were requested.

1. **UserInfo Endpoint:** OIDC defines a standard API endpoint (`/userinfo`) at the AS. The Client can make a GET or POST request to this endpoint using the obtained `access_token` to retrieve additional user profile claims that might not be included in the ID Token for brevity.

In essence, OIDC uses OAuth 2.0’s secure flows to transmit verifiable identity information. “Log in with Google” is typically an OIDC flow using Google as the OpenID Provider.

## Exploiting OAuth 2.0 & OIDC Implementations (Bug Hunter’s Focus) 🎯

The complexity of these flows creates numerous opportunities for error. Here’s where to focus your hunting:

**Insecure redirect\_uri Handling:**

- **The Core Problem:** The AS sends sensitive `code` or `token` values to this URI. If an attacker can control where this redirect goes, they win.
- **Attack Vectors:**
- *Missing Validation:* AS doesn’t check the `redirect_uri` against a pre-registered list. Attacker provides `redirect_uri=https://evil.com`.
- *Partial String Matching:* Check only `startsWith("<https://trusted.com>")`. Attacker uses `redirect_uri=https://trusted.com.evil.com`.
- *Path/Query Parameter Confusion:* Check allows any path/query on trusted domain. Attacker uses `redirect_uri=https://trusted.com/login?redirect=//evil.com` or `redirect_uri=https://trusted.com/callback#evil.com` (fragment abuse).
- *Path Traversal:* `redirect_uri=https://trusted.com/callback/../resource?path=../attacker/` if server resolves relative paths insecurely.
- *Subdomain Takeover:* `redirect_uri=https://dev.trusted.com/callback` where `dev.trusted.com`'s DNS is unclaimed. Attacker registers it.
- **Testing:** Fuzz the `redirect_uri` parameter mercilessly. Use common path traversal, open redirect payloads, different protocols (`javascript:`), domain variations. Use an interaction service (Burp Collaborator, Interactsh) as the target URI to detect callbacks. Check all registered URIs for takeover potential.
- **Mitigation: Strict exact string matching** against a pre-registered URI whitelist is the gold standard.

**Improper state Parameter Handling (CSRF on Consent):**

- **The Core Problem:** An attacker forces a victim’s browser to initiate an OAuth flow without their knowledge. Without `state` validation, the attacker might authorize their own malicious client or link their service account to the victim's client profile.
- **Attack Vectors:** Missing `state` parameter entirely; using a static or predictable `state`; failing to validate the returned `state` against the user's session on callback.
- **Testing:** Initiate a legitimate flow, capture the authorization URL. Remove/change the `state` parameter and send it to an authenticated victim's browser (e.g., via an image tag `src`). Does the flow complete successfully? Replay the callback URL (`/callback?code=...&state=DIFFERENT`) - does the application accept it?
- **Mitigation:** Generate a unique, high-entropy, unpredictable `state` value for each flow initiation, bind it to the user's session, and strictly validate its return on the callback.

**Authorization Code Interception / Leakage:**

- **The Core Problem:** Stealing the short-lived `code` allows exchanging it for long-lived tokens (if PKCE is not used/enforced).
- **Attack Vectors:**
- `Referer` Header Leak: If the `redirect_uri` page loads third-party resources (images, scripts, analytics), the full callback URL including the `code` might leak via the `Referer` header.
- Browser History: Code visible in URL bar/history.
- Insecure Transport (HTTP): `code` sent over plaintext.
- Malicious Browser Extensions / Platform Vulns: Code exfiltrated via other means.
- Log Files: Server logs recording the full callback URL.
- **Testing:** Check network requests originating from the callback page for `Referer` headers containing the code. Examine browser history. Ensure HTTPS. Check server logs if possible.
- **Mitigation: PKCE is the primary defense.** It cryptographically binds the code exchange to the initiating client. Use short lifetimes for codes (e.g., 60 seconds).

**Access Token Leakage:**

- **The Core Problem:** Leaked Access Tokens grant direct API access.
- **Attack Vectors:**
- Implicit Grant (`#` fragment): Browser history, `Referer` leaks (less common from fragments but possible via JS), XSS can read `window.location.hash`.
- Insecure Storage: Storing tokens in `localStorage`, `sessionStorage` (accessible to XSS), non-`HttpOnly` cookies.
- Proxy/Server Logs: If tokens are passed in query parameters or logged insecurely.
- Leaked via other Vulns: Exposed via SSRF, XXE, Directory Traversal, Debug endpoints.
- **Testing:** Check browser history/storage after Implicit flows. Look for tokens in proxy logs. Use XSS payloads to steal from storage.
- **Mitigation:** Avoid Implicit Grant. Store tokens securely (backend session, `HttpOnly` cookies, secure mobile storage). Sanitize logs. Implement robust CSP. Use short token lifetimes.

**Scope Misconfiguration / Escalation:**

- **The Core Problem:** Client gains more permissions than intended or authorized.
- **Attack Vectors:** AS allows client to request scopes not pre-registered; Client requests broad default scopes; User tricked by misleading consent screen (UI Redressing); Flaws allowing modification of approved scopes post-consent.
- **Testing:** Check the initial `/authorization` request - what scopes are requested by default? Try adding other known/guessed scopes (`admin`, `write`, `delete`, internal scopes). Carefully examine the consent screen. Test API endpoints to see if permissions exceed granted scopes.
- **Mitigation:** AS should enforce pre-registered scopes. Clients should request minimum necessary scopes (least privilege). Clear and accurate consent screens.

**OIDC Specific Flaws (ID Token Validation):**

- **The Core Problem:** The Client (Relying Party) trusts the ID Token without proper validation, allowing identity spoofing or session manipulation.
- **Attack Vectors:**
- Signature Stripping/Modification: Exploiting libraries that accept `alg:none` in the JWT header, bypassing signature checks entirely.
- Weak Signature Key / Key Leakage: Allowing attackers to forge valid signatures.
- Ignoring Claims: Failing to validate `iss` (is it from the expected provider?), `aud` (is this token *for me*?), `exp` (is it expired?), `nonce` (does it match the one I sent in the request to prevent replay?).
- **Testing:** Capture ID Tokens. Decode using [jwt.io](http://jwt.io/) or libraries. Check header/payload. Try changing `alg` to `none` and removing signature. Modify claims (`sub`, `iss`, `aud`, `exp`) and see if the client still accepts the token (requires re-signing if `alg!=none`). Check if `nonce` validation is performed.
- **Mitigation:** Use vetted OIDC/JWT libraries. Perform *all* required validations: signature (using correct public key), `iss`, `aud`, `exp`, `iat`, `nonce`.

**Refresh Token Vulnerabilities:**

- **Problem:** Compromise of a refresh token grants long-term access.
- **Flaws:** Issuing refresh tokens to public clients without rotation; insecure storage; non-expiring refresh tokens; leakage via logs or other vulns.
- **Testing:** Identify where/how refresh tokens are stored. Check for rotation mechanisms (does using one invalidate it and issue a new one?). Look for leakage points.
- **Mitigation:** Secure storage is paramount. Implement refresh token rotation. Provide mechanisms for users/admins to revoke tokens.

## Conclusion: Complexity Breeds Opportunity

OAuth 2.0 and OpenID Connect are powerful, indispensable standards for modern application security and interoperability. However, their inherent flexibility and the multitude of possible interactions across different roles, servers, and clients create significant opportunities for subtle and severe errors during implementation.

For developers, a deep understanding of the chosen grant types’ security implications, rigorous validation of all external inputs (especially `redirect_uri` and `state`), the mandatory use of PKCE for public clients, correct JWT validation for OIDC, and secure token handling throughout the lifecycle are non-negotiable.

For bug bounty hunters and security testers, these complex, stateful flows provide fertile ground. Methodically testing each step — from the initial redirect and consent screen to the callback handling, code exchange, token storage, and API usage — focusing on redirects, state management, token handling, scope enforcement, and OIDC validation, will often uncover high-impact flaws that automated scanners miss. Always remember the core principle: trust is established via authentication, but authorization must be explicitly verified at every single stage where access to a resource or function is granted.
