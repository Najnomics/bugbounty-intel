# How to test for JWT attacks?

- **Source URL:** https://medium.com/@elsherifx00/how-to-test-for-jwt-attacks-513da89abe94?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221227013713/https://medium.com/@elsherifx00/how-to-test-for-jwt-attacks-513da89abe94
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1185 (id 1185)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How to test for JWT attacks?

Hi everyone in this blog I will try to summarize JWT attacks

We have 3 main solid points we will talk about 

**- What are JWTs? - What are JWT attacks? - Scenarios about JWT attacks**

Let’s get started !!

# **- What** are JWTs **?**

JSON web tokens (JWTs) are a standardized format for sending cryptographically signed JSON data between systems. Unlike with classic session tokens, all of the data that a server needs is stored client-side within the JWT itself.

A JWT consists of 3 parts: a **header**, a **payload**, and a **signature**. These are each separated by a dot. `xxxxx.yyyyy.zzzzz`

The **header** and **payload** parts of a JWT are just **base64url-encoded** JSON objects. In most cases, The data of header & payload can be easily read or modified by anyone with access to the token. Therefore, the security of any JWT-based mechanism is heavily reliant on the cryptographic **signature**.

To create the signature part you have to take *the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that.*

# **- What are JWT attacks?**

JWT attacks involve a user sending modified JWTs to the server in order to achieve a malicious goal.

# **- Scenarios about JWT attacks**

To summarize the idea we have one goal is to play with the signature. we can play with the signature via playing with the content of the signature (payload — “alg” of the header — header — secret — sign all of the mentioned). we have 7 scenarios in this blog & I’ll use the JWT Editor extension, to know more about it from [here](https://portswigger.net/web-security/jwt/working-with-jwts-in-burp-suite)

- ***The first scenario: (play with the payload only)***

Test for ***signature verification*** like changing *username value to administrator*


- ***the second scenario: (play with the payload & “alg” )***

Test for ***Accepting tokens with no signature*** via changing *the “alg” value to none & remove the signature*


```
{
    "alg": "none",
    "typ": "JWT"
}
```
- ***The third scenario:*** (play with the secret key)

Test for ***Brute-forcing secret keys using hashcat*** then *use the output & encode it* & click *New Symmetric Key and* Replace the generated value for the `k` property with the Base64-encoded secret.


`hashcat -a 0 -m 16500 <jwt> <wordlist>`
- ***The forth scenario: (play with the sign flow)***

Test for *Injecting self-signed JWTs via the* `jwk`***parameter*** via click *New RSA Key* & Generate `jwk`then *attack with Embedded JWK*


- ***The fifth scenario: (play with the header via external server)***

Test for ***Injecting self-signed JWTs via the jku parameter*** via click *New RSA Key &* Generate `jwk` then *Copy Public Key as JWK* & *paste it in external server body* as below

```
{
    "keys": [
    ]
}
```
*replace the current value* of the `kid`parameter with the `kid` of the JWK that you uploaded to the exploit server & Add a new `jku`parameter to the header of the JWT. *Set its value to the URL of your* `jwk`*Set on the exploit server.*

- ***The sixth scenario:***

Test for **Injecting self-signed JWTs via the kid parameter** via click *New Symmetric Key* & *Replace the generated value for the* `k` *property with a Base64-encoded null byte (AA==).*In the header of the JWT, change the value of the `kid`parameter to a path traversal sequence pointing to the /dev/null file: ../../../../../../../dev/null


- The seventh scenario:

Test for **Performing an algorithm confusion attack** via go to /jwks.json or /.well-known/jwks.json then *Copy the JWK object* from inside the keys array. Make sure that you don’t accidentally copy any characters from the surrounding array. then click *New RSA Key & paste the JWK that you just copied. then Copy Public Key as PEM* then Use the *Decoder* tab to Base64 encode this PEM key, then copy the resulting string then Click *New Symmetric Key* & *Replace the generated value for the k property with a Base64-encoded PEM that you just created*
