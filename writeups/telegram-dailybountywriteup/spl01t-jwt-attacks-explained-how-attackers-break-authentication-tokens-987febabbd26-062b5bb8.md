# JWT Attacks Explained

- **Source URL:** https://medium.com/@spl01t/jwt-attacks-explained-how-attackers-break-authentication-tokens-987febabbd26?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260706063309/https://medium.com/@spl01t/jwt-attacks-explained-how-attackers-break-authentication-tokens-987febabbd26
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14165 (id 14165)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# JWT Attacks Explained: How Attackers Break Authentication Tokens

*A practical walkthrough of the most common JWT vulnerabilities, based on what I learned from PortSwigger’s Web Security Academy*

JSON Web Tokens (JWTs) are everywhere. They sit behind the login flow of countless REST APIs, single-page apps, and microservices. They’re convenient, stateless, and easy to implement — which is exactly why they’re so often implemented *badly*.

In this post, I’ll break down how JWTs work, then walk through the main categories of attacks against them: weak secrets, algorithm confusion, the classic `none` algorithm bypass, and header injection tricks like `kid`, `jwk`, and `cty`. I'll also include the practical steps for testing each one with Burp Suite's **JWT Editor** extension.

This isn’t theoretical — these are real, well-documented attack techniques, and they still show up in production systems today.

## What is a JWT, Actually?

A JSON Web Token is a standard (defined in [RFC 7519](https://www.rfc-editor.org/rfc/rfc7519)) for securely transmitting data between two parties as a JSON object. JWTs are most commonly used for **authentication and authorization**, typically sent in an HTTP header like this:

`Authorization: Bearer <token>`
A JWT is made of **three parts**, separated by dots, each base64url-encoded:

`header.payload.signature`
## 1. Header

The header describes the token itself — which algorithm was used to sign it, and what type of token it is:

```
{
 “alg”: “RS256”,
 “typ”: “JWT”
}
```
The `alg` field is the one that matters most from an attacker's perspective. The two algorithms you'll run into most often are:

- **HS256** — symmetric. One secret key is used to both sign and verify the token.
- **RS256** — asymmetric. A private key signs the token; a public key verifies it.

## 2. Payload

The payload carries the actual data — referred to as **claims**:

```
{
  "id": "110",
  "name": "John Smith",
  "admin": false
}
```
## 3. Signature

The signature is computed over the header and payload using the chosen algorithm and key. Its job is to guarantee the token hasn’t been tampered with — *if*, and only if, the server’s verification logic is implemented correctly. That “if” is where almost every JWT vulnerability lives.

With that foundation in place, let’s look at how each piece can be abused.

## Algorithm-Specific Attacks

## HS256: Cracking a Weak Secret

Because HS256 uses a single shared secret for signing and verifying, an attacker who guesses or brute-forces that secret can forge any token they want.

This is usually tested offline with **hashcat**:

`hashcat -a 0 -m 16500 <token> <wordlist.txt>`
If the secret turns out to be something weak — `secret123`, `changeme`, the company name, etc. — the attacker now owns the signing key. From here, they can modify any claim (e.g., flip `"admin": false` to `"admin": true`) and re-sign the token so it still validates.

**In Burp Suite, using the JWT Editor extension:**

1. Base64-encode the cracked secret.
2. Open the **JWT Editor Keys** tab and click **New Symmetric Key**.
3. Click **Generate**, then replace the `k` value with your base64-encoded secret.
4. Modify the payload claims as desired.
5. Sign the token using that key.

## RS256: Algorithm Confusion

RS256’s main weakness isn’t the algorithm itself — it’s **algorithm confusion**: tricking the server into verifying a token with the wrong type of key.

The idea: many JWT libraries decide *how* to verify a signature based on the `alg` header — a value the attacker fully controls. If a server expects RS256 but blindly trusts the `alg` field, an attacker can switch it to HS256 and sign the token using the server's own **public key** as if it were an HMAC secret. Since the public key is, well, public, the server ends up "verifying" a forged token against a secret the attacker already knows.

**Steps to construct this attack:**

1. Obtain the server’s public key — often exposed at `/.well-known/jwks.json` or `/jwks.json`.
2. Convert the key from JWK format to PEM (most JWT tooling, including Burp’s JWT Editor, can do this for you).
3. Change the `alg` header to `HS256`.
4. Sign the token using the public key (in PEM form) as the HMAC secret.

**No public key available?** If the server doesn’t expose its public key directly, you may still be able to reconstruct it mathematically from two valid RS256 tokens using PortSwigger’s `sig2n` tool:


`docker run --rm -it portswigger/sig2n <token1> <token2>`
## General JWT Attacks (Algorithm-Agnostic)

The following techniques aren’t tied to HS256 or RS256 specifically — they exploit weaknesses in how servers parse and trust the JWT *structure* itself.

## 1. The `none` Algorithm Attack

The JWT spec technically allows an algorithm value of `none`, meaning the token isn't signed at all. Some libraries, if not configured carefully, will happily accept this.

To exploit it:

- Change the `alg` value to `none`.
- Remove the signature portion of the token entirely — **but keep the trailing dot** (`header.payload.`).

Some implementations filter for the literal string `none`, so it's worth trying case variations to bypass weak filtering: `None`, `NONE`, `nOnE`, and so on.

## 2. Header Injection Attacks

The JWS specification defines several optional header parameters beyond `alg` — and "optional" doesn't mean "safe to ignore." A few of these can be abused directly.

### `jwk` — Embedded JSON Web Key

Some servers will use a public key embedded directly in the token’s own header (`jwk`) to verify that same token's signature — meaning the attacker can supply *their own* key pair and self-sign a token the server will trust.

**Using JWT Editor in Burp Suite:**

1. With the extension loaded, go to the **JWT Editor Keys** tab in Burp’s main tab bar.
2. Generate a new RSA key.
3. Send a request containing a JWT to Burp Repeater.
4. In the message editor, switch to the **JSON Web Token** tab and modify the payload as needed.
5. Click **Attack**, then select **Embedded JWK**, and choose the RSA key you just generated.
6. Send the request and observe the server’s response.

### `kid` — Key ID Injection

The `kid` header tells the server which key to use for verification — often by looking up a file path or a database record. If that lookup isn't sanitized, it's a direct line to **path traversal** or **SQL injection**.

Path traversal example, pointing the key lookup at a predictable empty file so the signature check effectively passes against an empty string:

```
{
  "kid": "../../../../../../../dev/null",
  "typ": "JWT",
  "alg": "HS256"
}
```
SQL injection is also worth testing if `kid` is used to query a key store — a payload like `kid": "nonexistent' UNION SELECT 'attacker_known_secret"` (adjusted to the actual query structure) can return a key the attacker controls.

### `cty` and `x5u` — Other Header Parameters Worth Trying

- **cty**
`application/x-java-serialized-object`) or **XXE** (`application/xml`), depending on how the application processes the payload afterward.
- **x5u**

## Key Takeaways

JWT vulnerabilities almost never come from a flaw in JSON Web Tokens as a standard — they come from **implementation mistakes**: trusting attacker-controlled header fields, accepting weak secrets, or skipping proper algorithm enforcement.

If you’re building or reviewing systems that rely on JWTs, the defensive checklist looks roughly like this:

- **Enforce the expected algorithm explicitly** server-side — never let the token’s own `alg` header dictate verification behavior.
- **Use strong, random secrets** for HS256 (256 bits of entropy, not a dictionary word).
- **Reject** **none**
 **and any unexpected algorithm** outright.
- **Validate or disable** **jwk**
**,** **jku**
**, and** **x5u**
- **Sanitize** **kid**
- **Set short expiration times** and validate `exp`, `nbf`, and `iat` claims properly.

JWTs are a powerful tool when implemented carefully — and a wide open door when they’re not. Most of the attacks above take only minutes to test with Burp Suite’s JWT Editor extension, which makes them an excellent first stop in any API security assessment.

*If you want hands-on practice with these exact attacks, PortSwigger’s Web Security Academy has a full set of free labs covering JWT vulnerabilities end to end.*
