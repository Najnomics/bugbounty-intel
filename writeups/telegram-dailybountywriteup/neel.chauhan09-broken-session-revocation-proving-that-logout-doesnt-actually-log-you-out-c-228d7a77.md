# Broken Session Revocation

- **Source URL:** https://medium.com/@neel.chauhan09/broken-session-revocation-proving-that-logout-doesnt-actually-log-you-out-c843047bf2b0
- **Fetched from:** https://medium.com/@neel.chauhan09/broken-session-revocation-proving-that-logout-doesnt-actually-log-you-out-c843047bf2b0?source=rss-dc15ab41b8c5------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14919 (id 14919)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Neel Chauhan / Sun, 20 Sep 2026 19:49:42 GMT

**CWE-613: Insufficient Session Expiration CWE-287: Improper Authentication CVSS 3.1: 8.1 (High)** — AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N

A logout button implies a contract: the token stops working, immediately, regardless of what it was before. Testing that contract is a capture-verify-revoke-replay exercise, four discrete steps, each one needed to actually prove or disprove the claim rather than just assume it.

I authenticated normally and grabbed the session cookie value straight out of Burp’s HTTP history:

Set-Cookie: session=eyJhbGciOiJIUzI1NiIs...; Max-Age=604800; HttpOnly; SameSite=Lax

A Max-Age of 604800 seconds is seven days. Long-lived by design, which makes the next steps matter a lot more.

Decoding the JWT payload (structurally, not breaking the signature, just base64-decoding the middle segment) showed the claim structure:

json

```
{
  "sid": "8eb1f788-...",
  "uid": "...",
  "role": "user",
  "email": "...",
  "twofa_pending": false,
  "iat": 1756000000,
  "exp": 1756604800
}
```
That structure is a strong hint about the architecture. A sid claim alongside exp suggests the backend is capable of tracking sessions server-side, the question is whether it actually checks that record on every request, or just trusts the signature and expiry.

GET /api/me HTTP/2

Cookie: session=\<captured token>

HTTP/2 200 OK

`{ "id": "...", "username": "test_user" }`
Baseline confirmed, working session, protected endpoint returns data.

POST /api/auth/logout HTTP/2

Cookie: session=\<captured token>

HTTP/2 200 OK

Set-Cookie: session=; Max-Age=0

The response clears the cookie client-side, Max-Age=0 tells the browser to delete it. Normal, expected behavior for a logout endpoint, from a browser's perspective.

This is the actual test. The browser’s copy is gone, but I still have the raw token value saved in Burp. If the token itself was invalidated server-side, replaying it should fail regardless of whether the browser still has it.

GET /api/me HTTP/2

Cookie: session=\<the SAME token captured in step 1, before logout>

Still 200. Still authenticated. Still returning the same user data. The token that was supposedly invalidated by logout is functionally identical to a live, active session.

I didn’t want to rely purely on my own replay test, so I checked whether the application exposed any internal session tracking I could use to independently corroborate the finding.

GET /api/sessions/audit HTTP/2

Cookie: session=\<same replayed token>

```
{
  "current_session": { "id": "8eb1f788-...", "is_active": false },
  "all_sessions": [
    { "id": "25b76b42-...", "is_active": false },
    { "id": "42bb9827-...", "is_active": true }
  ],
  "anomalies": [
    "Session ecSjJju0... was revoked (logout) but is still being honoured by the auth middleware."
  ]
}
```
The application’s own audit endpoint flags the exact discrepancy I’d already found manually: is\_active: false, meaning the backend does have a server-side record that correctly marks this session as revoked, but that record is evidently never consulted by the authentication middleware on incoming requests. The middleware is checking the JWT's signature and expiry only, and ignoring the is\_active flag that the rest of the system already maintains.

That’s the most useful kind of evidence to hand back to a dev team: not just “this is broken” but “you already built the fix, it’s just not wired into the auth check.”

On its own, this is a meaningful but contained gap. Where it becomes serious is in combination with anything that could expose a session token through some other channel, a reflected XSS vulnerability stealing document.cookie, a shared device, a proxy log, browser history sync. Normally, a user's best response to "I think my session might be compromised" is to log out. Here, that response accomplishes nothing. The stolen token remains fully valid for up to its entire seven-day lifetime, completely independent of how many times the legitimate user logs out in the meantime.
