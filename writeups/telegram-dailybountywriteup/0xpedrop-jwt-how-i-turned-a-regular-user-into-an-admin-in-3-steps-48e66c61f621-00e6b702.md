# JWT

- **Source URL:** https://medium.com/@0xpedrop/jwt-how-i-turned-a-regular-user-into-an-admin-in-3-steps-48e66c61f621?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905135214/https://medium.com/@0xpedrop/jwt-how-i-turned-a-regular-user-into-an-admin-in-3-steps-48e66c61f621
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9854 (id 9854)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# JWT: How I turned a Regular User into an Admin in 3 Steps

Imagine a regular user signing up for your application. They have basic permissions and can only view their own profile. Minutes later, without any action from the system, this same user becomes an administrator with full access to all data. How is this possible?

The culprit could be a single line of text that seemed harmless: a JSON Web Token (JWT). Although they are the backbone of many modern authentication systems, they carry a secret: if poorly implemented, they can become the main entry point for an attacker.

In this article, we will dissect this flaw in practice. I will guide you, step by step, showing how an attacker exploits a common vulnerability in JWTs and, most importantly, how you can shield your application against this type of attack.

### To Attack, First Understand the Victim

Before we break the system, we need to understand the basics of how a JWT works. Don’t worry, this will be quick and to the point.

## The Anatomy of a JWT

A JWT (JSON Web Token) is a standard used to securely exchange information between two parties. Think of it as a digital ID badge. When a user logs in, they receive this “badge” from the server. With each new request, they present the badge to prove who they are and what they are allowed to do.

This badge is a long string of text divided into three parts, separated by periods:

1. **Header:** The first part indicates the token’s type and, crucially, the encryption algorithm used to sign it (such as HS256). It is Base64Url encoded.
2. **Payload:** The second part contains the “claims,” which are the user’s data, such as name, ID, and their permission (`role`). It is also Base64Url encoded.
3. **Signature:** The third part is the most critical for security. It is a cryptographic signature that uses the Header, the Payload, and a secret key (known only by the server). The signature guarantees two things: that the data has not been altered (integrity) and that the badge is authentic (authenticity).

### The Standard Flow

As an attacker, it is essential to understand the normal flow to know where to interrupt it.

1. The user logs in with their credentials.
2. The server validates the credentials, creates a JWT, and sends it back to the user.
3. To access a protected route (e.g., `/my-profile`), the user sends the JWT in the request's HTTP header.
4. The server receives the JWT, verifies the signature to ensure it is valid and has not been tampered with, and then grants access.

## The Failure Point: When the Server’s Trust is Blind

We have established that the Signature is the JWT’s bodyguard, ensuring no one has tampered with the Payload’s content. The entire security relies on the server’s rigorous verification of this signature.

But… what if we could convince the server to simply *ignore* the bodyguard?


This is where the Achilles’ heel of many JWT implementations comes into play: an attack where we exploit the `alg` (algorithm) parameter within the Header itself.

### The `alg:none` Attack: The Attacker's Weapon

According to the official JWT specification, the `alg` parameter can optionally be set to `"none"`. The original intent was for scenarios where the token is already transmitted over a secure channel and its integrity is guaranteed by other means.

However, many JWT libraries, if not configured correctly, will accept this value without question. And it is this blind trust that the attacker exploits.

**The Vulnerable Server’s Flawed Logic**

When a server is misconfigured, it follows a dangerous flow:

1. It receives a token from the user.
2. It reads the **Header** to determine which algorithm to use for verification.
3. It finds `alg: "none"`.
4. **The fatal mistake:** Instead of rejecting an insecure algorithm, the server thinks, “Ah, the algorithm is ‘none’, so there’s no signature to verify.”
5. It completely skips the signature verification step and blindly trusts the data in the **Payload**.

### The Attacker’s 3-Step Plan

Knowing this flaw, the attacker’s plan becomes trivial:

1. **Obtain a Valid Token:** First, they register and log in as a regular user to receive a legitimate token (with `role: "user"`).
2. **Forge the Token:** They decode the token, change the **Header** to `{"alg": "none"}`, modify the **Payload** to `{"role": "admin"}`, and discard the original signature.
3. **Send the Forged Token:** They send this new, unsigned token to the server. The vulnerable server accepts it, and the attacker gains administrator access.

The theory seems simple and devastating, right?


Now, let’s stop imagining and get started. In the next section, we’ll run this attack step-by-step in our “Pwnned Corp” lab and watch the damage happen in real time.

## Getting Our Hands Dirty: Executing the Attack on “Pwnned Corp”

Let’s apply the theory in our test lab: the “Pwnned Corp” application. Our objective is clear: start as the user `0xPedrop` and end with full administrator access.

### Step 1: Obtaining the Initial Token (The Regular User’s Badge)

First, we act like a normal user. We access the application and log in. We are greeted by our dashboard with limited permissions.

Upon trying to access the Admin panel, we are met with a warning notification:

Access denied. You do not have administrator permission.


Our browser has received and stored a JWT that identifies us. Using the browser’s Developer Tools (F12), in the “Application” -> “Local Storage” tab, we find our digital badge:

This token is perfectly valid and signed by the server. For now.

### Step 2: The Forgery (Tampering with the Badge)

Now for the fun part. We copy the token above and take it to an online tool like `jwt.io` to modify it.

We make two crucial changes:

- **In the Header:** We change the `alg` value from `"HS256"` to `"none"`. We are telling the server not to worry about the signature.
- **In the Payload:** We change the `role` value from `"user"` to `"admin"`. We are promoting ourselves to administrators.

The tool returns a new token. Notice that it lacks the third part (the signature).

**The result of our forgery:**

`eyJhbGciOiAibm9uZSIsICJ0eXAiOiAiSldUIn0.eyJ1c3VhcmlvIjoiMHhQZWRyb3AiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NDkzMDYxMTgsImV4cCI6MTc0OTMwOTcxOH0.`
### Step 3: The Breach (Accessing as an Administrator)

With our new token, we return to the application. Again, using the Developer Tools, we go to Local Storage, delete the old token, and paste our forged token in its place.

Now, the moment of truth. We simply reload the page (F5).

The result is immediate. The application reads our forged token, and since there is no signature verification, it trusts the data in the Payload. The “Access Admin Panel” button is now enabled. Upon clicking it, access is granted.

Done. We went from a regular user to an administrator in three steps, by exploiting a single flawed line of configuration on the server.

**Important Note: Real-World Attacks** *In our lab, we manipulated Local Storage to simplify the demonstration. In a real-world scenario, an attacker would typically intercept the HTTP request (using tools like Burp Suite or OWASP ZAP) to swap the legitimate JWT with the forged one before the request reaches the server.*

The example shown was just one of many possible attacks, such as Header parameter injections.

## Defense Guide: How to Shield Your Application From This Attack

We saw how easy it is to exploit this flaw. The good news is that defending against it is even simpler, as long as you follow best practices when verifying tokens.

Here are the golden rules:

1. **NEVER Trust the** **alg**
 **Sent by the Client:**
The root cause of our attack was the server blindly trusting the `alg: "none"` sent by the attacker. The fix is simple: when verifying the token, your code must **ignore** what the token says and **enforce** the algorithm you expect.

Example of a fix in our `server`: Instead of letting the library choose, we force the use of `HS256`.

```
jwt.verify(token, SEGREDO, { algorithms: ['HS256'] }, (err, usuario) => {
    if (err) {
        return res.status(403).send('Token inválido ou adulterado.');
    }
    req.usuario = usuario;
    next();
});
```
By passing the `{ algorithms: ['HS256'] }` option, the `jsonwebtoken` library will immediately throw an error if it receives a token that is not signed with `HS256`, blocking the `alg:none` attack at its source.

**2. Use Strong and Secure Secrets** In our lab, we used a weak secret (`'my-super-weak-secret-123'`). In production, an attacker could try to guess your secret with brute-force attacks. Always use a long, complex, and random string, and store it securely as an environment variable, never directly in the code.

- ❌ **Bad:** `'password123'`
- ✅ **Good:** `'d5b2a7e4-2f8c-4d1e-9a0f-8b6c2c1e7a9b-_VERY_RANDOM_STRING_HERE'`

**3. Validate Essential Claims** Besides the signature, always check the payload’s `claims`, such as the expiration date (`exp`), to ensure the token isn't old and being reused. Most libraries do this by default, but it's good to confirm.

## Conclusion: Power Demands Care

We navigated the complete journey together: from a seemingly secure system, through the exploitation of a subtle flaw, to the shielding of our application. What we’ve learned is that powerful tools like JWTs are not inherently secure or insecure — their robustness depends entirely on our diligence as developers.

Implementing authentication correctly, never trusting client-sent data without cryptographic verification, and following best practices are not just recommendations; they are the foundation of a secure and trustworthy application.

I hope this practical guide has demystified the `alg:none` attack and, more importantly, has given you the confidence to defend against it.

*Thank you for reading!*

*Follow me for more articles on security. Leave a comment if you have any questions or suggestions.*
