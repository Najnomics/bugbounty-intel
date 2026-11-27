# JWT Security 101

- **Source URL:** https://medium.com/@mk2011sharma/jwt-security-101-how-to-defend-against-common-attacks-on-json-web-tokens-632fa09d8887?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230124064744/https://medium.com/@mk2011sharma/jwt-security-101-how-to-defend-against-common-attacks-on-json-web-tokens-632fa09d8887
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1366 (id 1366)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# JWT Security 101: How to defend against common attacks on JSON Web Tokens

JSON Web Tokens (JWT) are a popular way to represent claims securely between two parties. They are often used for authentication and authorization purposes in web applications and APIs. However, JWT-based systems can also be vulnerable to certain types of attacks if they are not properly implemented. Below attached image shows three components of jwt tokens such as Header, Payload and signature.

JWT has their own pros and cons and these were beautifully explained here by [Rahul Golwalkar](https://medium.com/u/9edd76024c0a?source=post_page-----632fa09d8887--------------------------------). Check it out to get in depth understanding of JWT as a session token alternative. Kudos to him for sharing detailed insight comparison.

**Methodology:**

I have used [this](https://github.com/ticarpi/jwt_tool/wiki/Attack-Methodology) methodology while testing for JWT Based vulnerabilities. Kudos to the guy who created the methodology.

**Attacks:**

Some common JWT-based attacks include:

1. Signature spoofing: An attacker can create a JWT with a modified payload and a valid signature, allowing them to gain unauthorized access. It will include attacks such as Accepting arbitrary signatures, Accepting tokens with no signatures etc.
2. Token replay: An attacker can intercept a JWT and reuse it multiple times, allowing them to bypass authentication and authorization controls. It will depend upon the session expiration configured in JWT.
3. Insecure JWT generation: An attacker can generate a JWT with weak or predictable signing keys or by using an algorithm that is known to be vulnerable.
4. JWT Brute force attack: An attacker uses an automated tool to guess the secret key that’s used to sign JWT, once the attacker guesses the secret key, he can then issue the token.
5. Algorithm evasion or confusion attack: An attacker may try to use JWT with an algorithm that the system does not support in order to bypass security checks.
6. JWT header parameter injections: An attacker can target the parameter such as jwk, kid, jku which are user controllable parameters to inject modified JWTs signed using your own arbitrary key rather than the server’s secret.

To mitigate JWT-based attacks, it’s important to use strong signing keys and algorithms, as well as using proper storage and transmission methods, such as HTTPS. Also, it’s crucial to implement rate limiting and blacklisting to detect and prevent token replay attacks. It’s also essential to verify that the JWT hasn’t been tampered with by validating the signature on the token before granting access, and include expiration time and make sure that it’s checked and respected on the server. Additionally, it’s essential to keep the systems up-to-date and ensure they are using the latest version of libraries that handle JWT. Make sure that apps are not vulnerable to path traversal or SQL injection via the kid header parameter.

**Additional defenses:**

- Always set an expiration date for any tokens that you issue.
- Avoid sending tokens in URL parameters where possible.
- Include the `aud` (audience) claim (or similar) to specify the intended recipient of the token. This prevents it from being used on different websites.
- Enable the issuing server to revoke tokens (on logout, for example).

**Labs where you can practice above mentioned attacks:**

Shoutout to Portswigger academy for creating such nice labs to practice. Practice labs are available on below mentioned link:

**Tools:**

Please let me know if you want detailed blog on the exploitation of each vulnerability.

You can reach out to me on:

LinkedIn: [https://www.linkedin.com/in/mkroot/](https://www.linkedin.com/in/mkroot/)

Twitter: [https://twitter.com/mk2011sharma](https://twitter.com/mk2011sharma)
