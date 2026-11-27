# Introduction to JWT

- **Source URL:** https://medium.com/@chanpreetkaur2005/introduction-to-jwt-f69162b59c24?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240819193209/https://medium.com/@chanpreetkaur2005/introduction-to-jwt-f69162b59c24
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6950 (id 6950)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Introduction to JWT

# **Introduction**

In web development and modern authentication, keeping data secure is very important. Developers need strong methods to ensure data stays safe and users are properly authenticated. JSON Web Tokens (JWT) have become a popular and secure way to handle authentication and share information. In this blog post, we’ll explain what JWT is, how it works, its benefits, and some tips for using it effectively.

# What is JSON Web Token (JWT)?

A JSON Web Token (JWT) is a compact and self-contained way of securely transmitting information between parties as a JSON object. JWTs are commonly used for authentication and information exchange in web applications.

# **Structure Of JWT**

A JWT consists of three parts separated by periods (.), which are base64url-encoded strings:

- **Header**: The header typically consists of two parts: the type of the token (which is JWT) and the signing algorithm being used, such as HMAC SHA256 or RSA.
- **Payload**: The payload contains the claims, which are statements about an entity (usually the user) and additional data.
- **Signature**: To create the signature, you take the encoded header, the encoded payload, a secret, and the algorithm specified in the header, and sign that. The signature is used to verify that the sender of the JWT is who it says it is and that the message wasn’t changed along the way.

# **Working Of JWT**

A JSON Web Token (JWT) is a lightweight, self-contained method for securely transmitting information between parties. It is made up of three parts: the header, payload, and signature. The header specifies the token type (JWT) and the signing algorithm (e.g., HMAC SHA256 or RSA). The payload contains the claims, which are pieces of information about the user or other data. The signature is created by encoding the header and payload with a secret key or private key, ensuring that the token is authentic and hasn’t been altered.

When a user logs in, the server generates a JWT with relevant user details and sends it back to the client. The client then includes this JWT in the authorization header of subsequent HTTP requests. Upon receiving the JWT, the server verifies the token by decoding it and checking the signature to confirm its validity. It also validates the claims, such as expiration time or issuer, to ensure the token’s authenticity. If the token is valid, the server processes the request and grants access based on the information within the JWT. This process allows secure, stateless authentication and efficient data exchange in web applications.

# How Do Vulnerabilities to JWT Attacks Arise?

While JWTs are secure in theory, their implementation can introduce vulnerabilities. Common issues arise when the signature verification process is flawed or improperly configured. These vulnerabilities allow attackers to forge tokens or bypass authentication mechanisms entirely.

**Exploiting Flawed JWT Signature Verification**

JWTs rely on a signature to verify the authenticity of the token. If the signature verification is flawed, attackers can exploit this weakness in several ways:

Accepting Arbitrary Signatures


Some implementations may incorrectly accept any signature, which allows attackers to craft tokens with arbitrary signatures that the server accepts as valid.

**Example Payload:**

```
#Header
{
  "alg": "HS256",
  "typ": "JWT"
}
#Payload
{
  "username": "admin"
}
```
**JWT Token :** eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV\_adQssw5c

In this example, if the server does not properly verify the signature, an attacker could create a token with an arbitrary signature and potentially gain unauthorized access.

Accepting Tokens with No Signature


Some JWT implementations may allow tokens without a signature (when the algorithm is set to ‘none’). This effectively turns the JWT into an unsigned, unverified data blob, which can be easily manipulated by attackers.

**Example Payload**

```
#Header
{
  "alg": "none",
  "typ": "JWT"
}
#Payload
{
  "username": "admin"
}
```
**Example Token:** eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VybmFtZSI6ImFkbWluIn0.

In this scenario, the token has no signature, and if the server is configured to accept this, the attacker could modify the payload to impersonate any user.

# Conclusion

JWTs are powerful tools for authentication and data exchange, but they must be implemented with care. Understanding and mitigating vulnerabilities, such as accepting arbitrary signatures or tokens with no signature, is crucial to maintaining the security of your systems. By adhering to best practices in JWT implementation and ensuring robust signature verification, you can protect your applications from these common yet dangerous exploits.
