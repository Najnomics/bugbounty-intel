# The JWT Bugs That Survive ‘We Use OAuth, So We’re Secure’

- **Source URL:** https://medium.com/@dhirenkumar/the-jwt-bugs-that-survive-we-use-oauth-so-were-secure-074436187cdc
- **Fetched from:** https://medium.com/feed/@dhirenkumar
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14973)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
#### Algorithm confusion, JWKS trust failures, and the cross-tenant mistakes I keep finding in production APIs

Every few months I get the same sentence in a kickoff call: *“Auth is solid we’re on OAuth 2.0 and OIDC, we use a managed identity provider, tokens are signed.”* And every few months I find a way to mint a token that the API happily accepts as an administrator of an account that isn’t mine.

The protocols aren’t the problem. OAuth 2.0 and OIDC are fine. The problem is that the spec ends where your code begins, and the most important security decision in the whole flow *do I trust this token?* gets made by a verification function somebody wrote on a Tuesday. That function is where I spend my time, and it’s where this article lives.

I’m going to walk through four failure modes I see over and over: JWT algorithm confusion, JWKS trust failures, issuer/audience sloppiness, and cross-tenant token validation. For each one I’ll show the vulnerable pattern, how to actually exploit it with tools you already have, and the fix that holds up. There’s a small vulnerable API so you can reproduce everything locally instead of taking my word for it.

A note up front, because it matters: the mainstream libraries have gotten good. PyJWT, recent jsonwebtoken, and friends now guard against several of these out of the box. That’s not a reason to skip the article it’s the reason these bugs have migrated into *custom verification wrappers* and *older pinned versions*, which is precisely where nobody is looking.

### Where verification actually happens

Draw the OIDC flow on a whiteboard and people point at the authorization server as “the secure part.” Correct, and irrelevant. The authorization server mints the token. The bug is almost always in the **resource server** your API when it receives that token and decides whether to believe it.

A token is three base64url segments: header, payload, signature. The header says which algorithm signed it and which key (alg, kid). The payload carries the claims (sub, iss, aud, exp, and whatever the IdP adds). Verification means: pick the right key, check the signature with the right algorithm, then check the claims actually apply to *you*.

Four questions decide whether that’s safe:

- Did I choose the algorithm, or did the attacker choose it for me in the header?
- Did I choose the key, or did the token tell me where to find one?
- Is this token from the issuer I expect?
- Is this token for *me*, and for *this tenant*?

Get any one of those wrong and the rest of your security model is decoration.

### A lab you can break

Generate a keypair the way a real IdP would:

bash

openssl genrsa -out private.pem 2048

openssl rsa -in private.pem -pubout -out public.pem

Here’s a deliberately sloppy resource server in Flask. It’s representative of real code not a strawman. Every mistake in it is one I’ve seen shipped.

python

import jwt

from flask import Flask, request, jsonify


app = Flask(\_\_name\_\_)

PUBLIC\_KEY = open("public.pem").read()

```
@app.get("/api/me")
def me():
    token = request.headers.get("Authorization", "").removeprefix("Bearer ").strip()
    try:
        # Three separate mistakes live on the next line.
        claims = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256", "HS256"])
    except jwt.PyJWTError as e:
        return jsonify(error=str(e)), 401
    return jsonify(claims)
```
```
@app.get("/api/admin")
def admin():
    token = request.headers.get("Authorization", "").removeprefix("Bearer ").strip()
    claims = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256", "HS256"])
    if claims.get("role") != "admin":
        return jsonify(error="forbidden"), 403
    return jsonify(secret="the crown jewels")
```
Point Burp at it, log in through your real flow to grab a legitimate Bearer token, and send it to /api/me in Repeater. Now we start taking it apart.

### 1. Algorithm confusion (RS256 → HS256)

The algorithms=\["RS256", "HS256"\] list is the kill shot, and it’s worth understanding *why* precisely.

RS256 is asymmetric: the IdP signs with its **private** key, you verify with the **public** key. Public means public it’s sitting on the JWKS endpoint for anyone to read. HS256 is symmetric: the same secret both signs and verifies.

If the verifier accepts *both* algorithms and feeds the *same key material* into both paths, here’s the attack: I take the public key you handed the world, I flip the header to alg: HS256, and I HMAC-sign a token of my choosing using that public key as the secret. Your code reads HS256, grabs the public key, uses it as an HMAC secret and the signature checks out, because I used the exact same bytes to sign.

I decide the role claim. You verify my forgery against your own public key.

#### Doing it by hand

python

import jwt

pub = open("public.pem").read()

forged = jwt.encode({"sub": "attacker", "role": "admin"}, pub, algorithm="HS256")

print(forged)

Here’s the honest part, and you should put this in your own writeups too: **modern PyJWT will refuse that.** HMACAlgorithm.prepare\_key rejects any key containing PEM markers like -----BEGIN PUBLIC KEY----- and raises InvalidKeyError. That guard is good security it’s defense in depth doing its job.

So why does the bug still matter? Because the guard is (a) absent in older pinned versions you’ll find all over enterprise estates, (b) trivially sidestepped when the key reaches the HMAC path *without* PEM headers think a raw JWK, a DER blob, or a base64 string someone stored in config and simply not present in several other ecosystems, where historically jsonwebtoken and various Java/Go libraries would do exactly this if you didn’t pin the algorithm. The *mechanism* is identical everywhere; only the guardrails differ. When the key arrives as bare bytes, the forge above signs a token your server will trust.

#### Doing it in Burp

Install **JWT Editor** from the BApp Store. The flow for algorithm confusion when the public key is reachable (which, via JWKS, it usually is):

1. Pull the public key from the JWKS endpoint it’ll be a JWK with n and e.
2. Convert it to PEM. In JWT Editor: *New RSA Key*, paste the JWK, and it’ll render the PEM for you.
3. Base64-encode that PEM.
4. *New Symmetric Key* in JWT Editor, then replace the k value with your base64 PEM.
5. In Repeater, open the token in the JSON Web Token tab, edit the payload (role → admin), change alg to HS256, and *Sign* with your symmetric key.

The thing that will eat an hour of your life: **the exact byte representation of the public key.** Trailing newline or not. PEM PUBLIC KEY vs an X.509 cert wrapper. CRLF vs LF. The server used a specific serialization to load that key, and your HMAC secret has to match it byte-for-byte or the signature won’t verify and you’ll swear the bug isn’t real. It’s real. Try the variants.

#### The fix

Pin the algorithm. One algorithm. Never a list that mixes symmetric and asymmetric.

python

claims = jwt.decode(token, PUBLIC\_KEY, algorithms=\["RS256"\])

If you genuinely support more than one asymmetric algorithm, fine but a symmetric algorithm must never share a verification path with an asymmetric key. The cleanest rule I give teams: *the resource server, not the token, decides the algorithm.* The alg header is attacker-controlled input. Treat it like any other attacker-controlled input.

### 2. The free one: alg: none

While you’re in there, check for the original sin. Older libraries honored alg: none as “unsigned, and that’s fine,” which means anyone can strip the signature and self-assert any claim.

Take a valid token, set the header to {"alg":"none","typ":"JWT"}, keep your doctored payload, and leave the signature segment empty (the token ends with a trailing dot). If /api/me returns your claims, you’ve found a critical in about forty seconds.

Modern libraries reject none unless you explicitly opt in, so this is mostly a finding on legacy services and hand-rolled parsers. I still test it on every engagement because it costs nothing and it still hits more than it should.

### 3. JWKS trust failures: when the token picks the key

This is the category people under-test, and it’s my favorite, because the elegant version of the bug is *the token telling the server which key to trust.*

A healthy setup is boring: the resource server has a **pre-configured, allowlisted JWKS URL**, fetches the IdP’s public keys, caches them, and matches the token’s kid against that set. The token supplies an identifier; the server supplies the keys.

The bugs show up when a developer gets clever about key resolution. Three patterns:

**jku header injection.** The jku header is a URL pointing to a JWK Set. If verification code reads jku from the token and fetches keys from it, I point it at a JWKS I host, sign with my own private key, and your server fetches my public key and validates my forgery. I supplied the token, the key, *and* the trust.

**Embedded jwk header.** Same idea, lazier. The jwk header can carry a public key inline. If the verifier honors it, I embed my own public key, sign with my matching private key, done. JWT Editor has an *Embedded JWK* attack that automates exactly this one click.

**kid abuse.** The kid is attacker-controlled text that often gets used to *locate* a key. I’ve seen it concatenated into a filesystem path (../../dev/null → empty key → HMAC with an empty secret), interpolated into a SQL lookup (now it’s also an injection point), and used to select from a key store without checking the key actually belongs to the expected issuer.

Here’s the honest framing again: PyJWT’s PyJWKClient does *not* read jku or honor embedded jwk by default you hand it the JWKS URL and it ignores what the token wants. So when you find these, you’ve almost always found a **custom resolver** the clever wrapper someone wrote to “make multi-issuer support easier.” That wrapper is the richest target in the codebase. If a verification function is complex enough that I can’t understand it in one read, I assume it’s exploitable until proven otherwise.

#### The fix

The key source is configuration, never input.

- JWKS URL(s) are allowlisted server-side. The token never influences where keys come from.
- Strip or ignore jku, x5u, and embedded jwk entirely. Don’t fetch, don’t parse.
- Use kid only to *select* from keys you already trust, and bind the selection to the expected issuer. Never let kid touch a filesystem, a query, or a shell.
- Cache JWKS and handle rotation with a bounded refresh, so a kid miss triggers a controlled re-fetch not an attacker-triggered fetch of arbitrary URLs.

### 4. Issuer and audience: the confused deputy

Signature valid, algorithm pinned, key trusted and still a bypass, because a correctly signed token isn’t automatically a token meant for *you*.

Picture one IdP serving two APIs: orders-api and billing-api. A user authenticates and gets a token with aud: orders-api. Both tokens are signed by the same IdP with the same key, so both verify cleanly everywhere. If billing-api checks the signature but not the aud claim, I take my legitimately-issued orders token and replay it against billing. The signature is real. The audience is wrong. Billing doesn’t look, so billing gets played. That’s the confused deputy, and it’s endemic in microservice estates that share an IdP.

The iss version is the same disease: if you don’t verify the issuer, any token your library can validate including ones from an entirely different IdP you happen to also trust a key for walks in.

#### The fix

Verify every claim that scopes the token, and make the library enforce it rather than checking by hand afterward:

python

claims = jwt.decode(

token,

key,

algorithms=\["RS256"\],

issuer="https://issuer.example.com/",

audience="billing-api",

options={"require": \["exp", "iss", "aud", "sub"\]},

)

Require exp and actually honor it. Require iss and match it exactly. Require aud and match *your* identifier. “We validate the signature” is half a sentence. The other half is “and the token was minted for this service by the issuer we expect.”

### 5. Cross-tenant validation: the one that compromises other people’s accounts

This is the headline, because it’s the one that turns “I can forge a token” into “I can read tenant B’s data while logged in as tenant A.”

Multi-tenant B2B SaaS almost always shares an identity provider across tenants. Same IdP, same signing keys, different organizations. Which means a token from tenant A is, cryptographically, a perfectly valid token the question is whether your API checks that it belongs to the tenant it’s being used against.

Two concrete versions:

**The “any tenant” issuer bug.** This is the classic Azure AD / Entra ID multi-tenant mistake. An app validates that the token is signed by Microsoft and came from login.microsoftonline.com, and stops there. But the /common endpoint issues tokens for *every* Microsoft tenant on earth. If you don’t validate the specific tenant the tid claim and the tenant-specific issuerthen any user in any Microsoft tenant can authenticate to your app as a valid user. Microsoft’s own guidance is blunt about this: multi-tenant apps must validate the issuer and the tenant ID against an allowlist, not just trust the shared signer.

**The tenant-context mismatch.** The app figures out the tenant from the request a subdomain (acme.app.com), a path, a headerand separately validates the token against the global signing key. If nothing ties the *token’s* tenant to the *request’s* tenant, I log in legitimately to my own tenant, grab my valid token, and send it to tenantvictim.app.com. My signature is real. My tid says tenant A. The host says tenant B. The server never compares them, so it serves tenant B’s data under my tenant A identity.

I find this one by authenticating to an account I control, then replaying that token against a tenant I don’t, varying the subdomain/path/header while keeping my own valid token. When it returns someone else’s data, it’s game over, and it’s usually a clean critical because it’s an authentication-and-authorization bypass at the tenant boundary.

#### The fix

The tenant boundary has to be enforced *inside* verification, not alongside it:

- Validate the issuer against a **specific-tenant** issuer (or an explicit allowlist of tenant issuers), never a wildcard.
- Validate the tenant claim (tid, org\_id, or whatever your IdP calls it) against an allowlist of tenants you actually serve.
- **Bind the token’s tenant to the request’s tenant.** If the token says tenant A and the request targets tenant B, reject it before any data access. This single check kills the whole class.
- Treat per-tenant isolation as a security control, not a UI convenience. The database query scope and the token’s tenant must be the same tenant, enforced server-side.

### How I actually test this on an engagement

When I land on an API using bearer JWTs, the sequence is boring on purpose:

First, read the token. Decode header and payload (jwt\_tool, JWT Editor, or three lines of Python). Note alg, kid, iss, aud, exp, and any tenant claim. The header tells me which attacks are even on the table.

Then, find the public key. JWKS endpoint, OIDC discovery doc at /.well-known/openid-configuration, sometimes embedded in a client bundle. If I have the public key, algorithm confusion is live.

Then I run the cheap checks in order: alg: none; strip the signature; flip to HS256 and sign with the public key (trying the byte-representation variants); embedded jwk; jku pointed at my own host; kid path and injection payloads. Each is minutes of work.

Then the claim logic: drop aud, swap iss, extend exp, and the big one replay a token I legitimately own against a tenant I don’t.

And if I can get eyes on the source, I read the verification function first, before anything else. Fifteen minutes with the actual jwt.decode call and its wrapper tells me more than an hour of black-box poking. I’m looking for one thing: *who chose the algorithm and the key the server, or the token?* If the answer is “the token,” I already know how the report ends.

### The remediation that actually holds

Strip away the specifics and it’s four rules, applied together:

The server decides the algorithm. Pin it explicitly, never mix symmetric and asymmetric in one verification path, and treat the alg header as untrusted input.

The server decides the key. JWKS URLs are allowlisted configuration; jku, x5u, and embedded jwk are ignored; kid only selects from keys you already trust and never touches a path, query, or shell.

The server checks that the token is for it. Require and validate iss, aud, and exp through the library, not with hand-rolled checks after the fact.

The server checks that the token is for *this* tenant. Validate the tenant claim against an allowlist and bind it to the tenant the request is actually operating on.

None of this is exotic. It’s the difference between calling a verification function and *understanding* one. OAuth and OIDC gave us a solid protocol. Whether your API is secure comes down to a few dozen lines that decide what to trust and those lines are written by people, which means they’re worth reading, and worth breaking in a lab before someone breaks them in production.

If you only change one thing after reading this: go find your jwt.decode call and check whether the algorithm is pinned. I’ll wait.
