# JaWT Scratchpad

- **Source URL:** https://medium.com/@affanhaxor/jawt-scratchpad-cylab-security-academy-write-up-jwt-secret-key-and-authentication-bypass-07966d6a7277
- **Fetched from:** https://medium.com/@affanhaxor/jawt-scratchpad-cylab-security-academy-write-up-jwt-secret-key-and-authentication-bypass-07966d6a7277?source=rss-a70f2c751bb6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14956)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Affanhaxor / Fri, 23 Oct 2026 05:50:14 GMT

**Author:** Affanhaxor

**Platform:** CyLab Security Academy

**Category:** Web Exploitation

**Topics:** JSON Web Tokens (JWT), HMAC-SHA256, Authentication Bypass

**Difficulty:** Medium

JSON Web Tokens (JWTs) are commonly used by web applications to maintain user sessions and verify identity. A JWT contains information about a user and a cryptographic signature that allows the server to verify whether the token has been modified.

However, JWT-based authentication can become vulnerable when an application uses a weak signing secret. If an attacker discovers that secret, they may be able to create a valid token containing a different user identity.

In this write-up, I will explain how I approached the **JaWT Scratchpad** challenge on CyLab Security Academy. The challenge demonstrates how a weak JWT signing secret can allow a user to forge a token and access an administrator’s scratchpad.

After opening the challenge, I found a web application called **JaWT**. The page described itself as an online scratchpad where users could write and save their thoughts.

The application explained that users needed to log in to access the scratchpad. It also mentioned that the administrator had a special scratchpad that ordinary users could not access.

This message provided an important clue: the application likely used the authenticated user’s identity to decide which scratchpad to display.

While exploring the page, I noticed a warning stating that users could not log in as the administrator because the admin account was special.

Instead of trying to bypass the restriction through the login form, I focused on understanding how the application identified an authenticated user.

Since JWTs were mentioned on the page, I suspected that the application might store session information in a token.

The application allowed users to register by entering a name. I registered with the username affan and accessed the scratchpad.

After successful registration, the page displayed a personalized greeting and provided a text area for writing notes.

This confirmed that the application associated the current session with a user identity.

Next, I opened the browser’s Developer Tools and navigated to the Application tab. Under Cookies, I found a cookie named jwt.

I copied the token for inspection. It appeared to contain three sections separated by periods, which is the standard structure of a signed JWT.

A typical signed JWT contains:

The cookie was particularly important because it appeared to hold the identity information used by the application.

I used a JWT decoding tool to inspect the token’s contents.

The decoded header contained:

```
{
  "alg": "HS256",
  "typ": "JWT"
}
```
The payload contained:

```
{
  "user": "affan"
}
```
The HS256 algorithm uses HMAC with SHA-256 to sign the token. The payload was readable because JWT encoding is not encryption; the signature is what protects the token against undetected modification.

The user claim was an important discovery. It suggested that the application used this claim to identify the logged-in user.

However, simply changing "user": "affan" to "user": "admin" would invalidate the existing signature. To create an accepted token, I needed to understand the signing secret.

The next step was to investigate whether the JWT’s signing secret was weak enough to recover through an offline dictionary attack.

I saved the relevant token data for analysis and used John the Ripper with the RockYou wordlist and the HMAC-SHA256 format.

The command shown in my screenshot was:

john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=HMAC-SHA256

John the Ripper tested candidate secrets from the wordlist against the captured signature. The output revealed the secret:

ilovepico

This demonstrated the risk of using a predictable signing secret. An HMAC signature is designed to be difficult to forge without the key, but a weak key can potentially be recovered by testing likely candidates offline.

Once I recovered the signing secret, I could generate a new token with the administrator identity in the payload.

The header remained:

The payload was changed to:

```
{
  "user": "admin"
}
```
Using the same HMAC-SHA256 algorithm and the recovered secret ilovepico, the token generator could produce a new signature for this payload.

This was the critical difference between merely editing a token and forging a valid signed token: the new token had to be signed with the correct secret.

After generating the token, I returned to the JaWT application and replaced the existing jwt cookie with the newly generated token.

I then refreshed the page so that the application would process the updated cookie.

The application recognized the identity in the new token and displayed the administrator’s scratchpad. This confirmed that the application trusted the signed user claim and that recovering the signing secret allowed the token to be forged.

The administrator’s scratchpad displayed the following flag:

`academy{jawt_was_just_what_you_thought_699fae22}`
This confirmed that the challenge had been completed successfully.

This challenge demonstrated several important security concepts:

Developers should follow these security practices when implementing JWT authentication:

**Use a strong, randomly generated signing secret.** Avoid predictable words, reused passwords, or secrets that can be found in public wordlists.

**Store secrets securely.** Keep signing keys in a suitable secret-management system or protected environment configuration rather than exposing them in source code.

**Verify every token correctly.** The server should validate the signature, enforce an explicitly allowed signing algorithm, and check relevant claims such as expiration and issuer.

**Enforce authorization on the server.** Sensitive access should not rely solely on a user-controlled identity claim. Administrative permissions should be verified against trusted server-side authorization data.

**Protect session tokens.** Use HTTPS and appropriate cookie settings, including HttpOnly, Secure, and a suitable SameSite policy.

**Rotate compromised keys.** If a signing secret is exposed or recovered, replace it and invalidate tokens signed with the compromised key as appropriate.

The JaWT Scratchpad challenge showed how a weak JWT signing secret can undermine an application’s authentication mechanism. By inspecting the browser cookie, decoding the JWT, recovering the weak secret, and generating a correctly signed token with a different user identity, I was able to access the administrator’s scratchpad.

The main lesson is that JWT security depends on more than the token format itself. Strong signing keys, correct signature verification, and server-side authorization checks are all essential for preventing token forgery and privilege escalation.

*This write-up is intended for educational use in the CyLab Security Academy lab environment. Test these techniques only on systems you own or are explicitly authorized to assess.*

**LinkedIn:** [https://www.linkedin.com/in/affanhaxor](https://www.linkedin.com/in/affanhaxor)

**Instagram:** [https://instagram.com/affan\_haxor](https://instagram.com/affan_haxor)

*Follow me for more CTF write-ups, web security labs, and AppSec content.*
