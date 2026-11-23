# JWT Attacks Explained

- **Source URL:** https://medium.com/@vigneshkumaroffsec/jwt-attacks-explained-how-json-web-tokens-get-forged-and-how-to-secure-them-b47eeb5ac00d
- **Fetched from:** https://medium.com/feed/@vigneshkumaroffsec
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14996 (id 14996)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*A JWT is only as trustworthy as its signature check — and that check is wrong more often than you’d think. Here are the ways JWTs get broken, how to test for each, and the fixes. Authorized testing only.*

By Vignesh Kumar | Security Researcher

JSON Web Tokens are everywhere — they’re how most modern APIs carry “this is who you are” between requests. The appeal is that they’re **self-contained**: the token itself holds your identity and permissions, signed by the server, so the server doesn’t have to look anything up. The risk is the same sentence: the token holds your permissions, and the *only* thing stopping you from editing them is one signature check. When that check is weak or missing, a user rewrites their own token to say admin and the whole thing falls over.

This guide walks through the main JWT attacks, how to test for them, and how to fix them — all for systems **you own or are explicitly authorized to test**.

### A JWT in 60 seconds

A JWT has three parts, separated by dots: header.payload.signature. The first two are just **base64url-encoded JSON** — readable by anyone.

- **Header** — metadata, crucially the alg (signing algorithm) and sometimes kid (key id).
- **Payload** — the *claims*: sub (subject/user), role, exp (expiry), iss (issuer), aud (audience), and whatever else the app adds.
- **Signature** — the header and payload signed with a secret (HMAC, e.g. HS256) or a private key (RSA/ECDSA, e.g. RS256). This is the only part that proves the token wasn’t tampered with.

Decode a JWT and you can read everything in it. The signature is what stops you from *changing* it and having it still accepted. Every attack below is a way to change the token and still get it accepted.

### Attack 1: The alg: none / unsigned token

The JWT spec includes an algorithm literally called none — "this token is unsigned." If a server accepts it, an attacker sets "alg": "none", edits the payload to say whatever they want ("role": "admin"), removes the signature entirely, and the server trusts it.

**Test:** change the header alg to none (and variants like None, NONE), tamper a claim, drop the signature, and send it. If it's accepted, the server isn't verifying at all.

**Fix:** never accept none. Explicitly reject unsigned tokens, and pin the expected algorithm server-side.

### Attack 2: Signature not verified

A surprising number of apps *decode* the JWT and read the claims but never actually *verify* the signature — or verify it in a way that’s easy to skip. Then any tampered token works, no tricks needed.

**Test:** change a claim (e.g. the user id or role), leave a syntactically valid but wrong signature, and send it. If the app acts on the changed claim, it isn’t verifying.

**Fix:** verify the signature on every request, before trusting a single claim, and fail closed if it doesn’t check out.

### Attack 3: Algorithm confusion (RS256 → HS256)

This is the clever one. With **RS256**, the server signs with a *private* key and verifies with the matching *public* key — and public keys are, by design, public. In **HS256**, the same secret both signs and verifies.

If a server naively picks the algorithm from the token’s header and passes “the key” to a verify function, an attacker can:

1. Take the server’s **public key** (often retrievable or leaked).
2. Change the header to HS256.
3. **Sign the tampered token using the public key as the HMAC secret.**

Now the server, trusting the header, verifies an HS256 token using the public key as the secret — which matches, because that’s exactly what the attacker signed with. Forged token accepted.

**Test:** obtain the public key, switch alg to HS256, re-sign with that key as the HMAC secret, send.

**Fix: pin the algorithm server-side** — never let the token’s header decide how it’s verified. Use a library that separates HMAC and RSA verification and configure the one you expect.

### Attack 4: Weak HMAC secret

If the app uses HS256 with a **guessable or short secret** (secret, password, a default from a tutorial), the signing key can be brute-forced offline. Once you have the secret, you can forge *any* token you like.

**Test:** take a valid token and run it through a cracking tool (hashcat, or jwt\_tool) against a wordlist. If the secret cracks, you own the signing key.

**Fix:** use a long, random, high-entropy secret (think 256 bits of randomness), stored securely — or use asymmetric keys (RS/ES) so there’s no shared secret to crack.

### Attack 5: Header injection via kid, jku, x5u

Some JWT headers tell the server *where to get the verification key*. If the server trusts them blindly, that’s an injection point.

- **kid (key id)** — often used to look up a key by name, from a file or database. A kid like ../../../dev/null can point the server at a predictable/empty "key" the attacker then signs with (path traversal); a kid plugged into a query can be **SQL injection**; one plugged into a command can be command injection.
- **jku / x5u (key-set URLs)** — tell the server to fetch the public key from a URL. If it isn't allow-listed, the attacker hosts their *own* key set, points jku at it, and signs with their own key — a combination of SSRF and key injection that forges valid tokens.

**Test:** probe kid for traversal/SQLi, and set jku/x5u to a URL you control to see if the server fetches keys from it.

**Fix:** treat these headers as untrusted input — validate/allow-list kid values, never build file paths or queries from them unsanitized, and allow-list the exact hosts jku/x5u may use (or don't support them at all).

### Attack 6: Sensitive data in the payload

The payload is **base64, not encryption**. Anyone with the token can read it. Yet teams put emails, internal IDs, roles, even API keys in there, assuming it’s opaque. It isn’t.

**Test:** decode the payload and read it. Anything sensitive in there is already exposed to the token holder.

**Fix:** put nothing secret in a JWT payload. If the content must be confidential, use an encrypted token (JWE) — but usually the answer is simply to keep secrets out.

### Attack 7: Missing expiry, no revocation, replay

Because JWTs are self-contained, the server usually can’t “log one out.” If a token has **no exp or a very long one**, a stolen token works indefinitely. With **no jti/nonce**, the same token can be **replayed**.

**Test:** check exp (is it absent or far in the future?); try reusing an old token after "logout"; replay a captured token.

**Fix:** short-lived access tokens with refresh tokens; validate exp and nbf strictly; maintain a revocation mechanism (short TTL plus a denylist for emergencies); include and check jti where replay matters.

### How to test JWTs, in practice

The workflow for any target JWT:

1. **Decode** the header and payload (jwt.io, or jwt\_tool). Read what's in them.
2. **Tamper and resend** with no clever signature — does the app verify at all?
3. **Try alg: none** and its casings.
4. **Try algorithm confusion** (RS256 → HS256 with the public key).
5. **Crack the secret** if it’s HS256.
6. **Probe kid/jku/x5u** for injection and SSRF.
7. **Check claims** — exp, iss, aud — and test replay and logout.

**jwt\_tool** and Burp’s **JWT Editor** extension automate most of this. Only ever against tokens from accounts and targets you’re authorized to test.

### The fixes, together

Almost every JWT vulnerability comes down to a handful of rules:

- **Always verify the signature**, before trusting any claim, and **fail closed**.
- **Pin the algorithm server-side.** Never let the token’s alg header choose how it's verified — this single rule kills alg: none and algorithm confusion.
- **Use strong keys** — a high-entropy HMAC secret, or asymmetric keys with proper key management.
- **Validate every claim** — exp, nbf, iss, aud — not just the signature.
- **Treat kid, jku, x5u as untrusted** — allow-list, don't interpolate.
- **Keep secrets out of the payload.**
- **Keep tokens short-lived**, with refresh and a revocation path.
- Use a **well-maintained library** configured strictly, rather than hand-rolling verification.

### Common Mistakes to Avoid

- Testing tokens or targets you aren’t authorized to assess.
- Reading JWT claims without verifying the signature (on the defense side, the cardinal sin).
- Letting the token’s alg header decide the verification algorithm.
- Accepting alg: none or its variant casings.
- Using a short, guessable, or tutorial-default HMAC secret.
- Building file paths or SQL from kid, or fetching keys from an unrestricted jku.
- Putting sensitive data in the payload because it “looks encoded.”
- No expiry, no revocation, no replay protection.

### A Quick JWT Security Checklist

- Every request verifies the signature before trusting claims, and fails closed.
- The algorithm is pinned server-side; the header’s alg is never trusted to choose it.
- alg: none (all casings) is rejected.
- HMAC secrets are long and random, or asymmetric keys are used with proper management.
- kid, jku, x5u are validated/allow-listed and never interpolated into paths or queries.
- exp, nbf, iss, aud are all validated.
- No sensitive data lives in the payload.
- Tokens are short-lived with refresh tokens and a revocation path; replay is handled where it matters.
- A maintained JWT library is used and configured strictly.

### Final Thoughts

JWTs fail in a specific, teachable way: the token hands the user their own permissions, and the entire security model rests on one correct signature verification. Get that verification right — verify always, pin the algorithm, use strong keys, validate the claims — and almost every attack on this page disappears. Get it subtly wrong — trust the header, accept none, reuse the public key as a secret — and a user simply edits their token into an admin's.

If you build or test with JWTs, do one thing this week: take a token from your own test account, change one claim, strip or weaken the signature, and send it. If the server notices, your verification is sound. If it doesn’t, you’ve just found the gap — and you know exactly which rule closes it.

### About me

I’m Vignesh Kumar, a security researcher working across application security, DevSecOps, cloud security, and vulnerability research.

I share practical findings from security assessments and responsible disclosures to help improve the security of real-world systems.

*The techniques in this article are described for defending and testing systems you own or are authorized to assess.*
