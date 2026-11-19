# A04

- **Source URL:** https://medium.com/@shrutishinde1319/a04-cryptographic-failures-owasp-top-10-2025-22f8091303d1
- **Fetched from:** https://medium.com/feed/@shrutishinde1319
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14989 (id 14989)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*Part 4 of my OWASP Top 10 (2025) series.*

If Someone sends his/her password to a server, how do we stop someone else from reading it? What if someone intercepts the request, steals stored data, or modifies information while it’s travelling?

This is where cryptography comes in.

Security relies on three important goals:

### What Is Encryption?

Encryption converts readable data (**plaintext**) into unreadable data (**ciphertext**) using an algorithm and a key. Decryption converts it back.

### What Is Hashing?

Hashing converts data into a fixed-length output called a **hash**. Unlike encryption, hashing is designed to be one-way you cannot simply decrypt a hash to recover the original data.

For example, SHA-256 always produces a 256-bit hash, regardless of the input size.

### What Is Salt?

Salt is random data added to a password before hashing. It ensures that two users with the same password don’t end up with identical password hashes.

This also makes precomputed rainbow-table attacks much less effective.

### Different Algorithms, Different Purposes

Now that we understand encryption, hashing, and salt, the next question is: **what actually makes these protections secure?**

The answer lies in the algorithms being used.

Different algorithms are designed for different purposes. Some protect data by encrypting it, some generate hashes, and others are specifically designed to store passwords securely.

Every algorithm has its own purpose, advantages, and limitations. The problem isn’t simply using an algorithm it’s using the wrong algorithm for the wrong purpose.

For example, SHA-256 is a strong hashing algorithm for many integrity-checking purposes, but using it directly to store passwords is a poor choice because attackers can test guesses very quickly.

Similarly, encryption is only as strong as its implementation and key management. Even a strong algorithm can fail if the encryption key is exposed or the application uses it incorrectly.

### Where Does the Risk Begin?

This is where cryptographic failures become interesting from a security perspective. A developer might use a strong algorithm but implement it incorrectly, store sensitive data without encryption, expose secret keys, or choose a hashing method that’s too fast for password storage.

The result? Sensitive information may become readable, passwords may be easier to crack, or data may be manipulated without proper detection.

### As a Pentester: What Should I Look For?

During testing, identify sensitive information that requires protection:

- Passwords and password hashes
- Authentication tokens and session cookies
- API keys and JWT secrets
- Personal and financial information
- Encryption keys and database credentials

Then investigate how the application protects them.

Check for:

- Plain HTTP instead of HTTPS
- Sensitive data exposed in API responses
- Cryptographic keys in source code or configuration files
- Weak encryption algorithms
- Poor password hashing practices
- Insecure JWT implementation
- Debug endpoints revealing sensitive information

For example, an API response containing:

```
{
  "username": "shruti",
  "password_hash": "5f4dcc3b5aa765d61d8327deb882cf99"
}
```
is a serious red flag. Even though the password is hashed, exposing password hashes unnecessarily creates an additional risk.

A hash isn’t the original password, but it doesn’t mean it’s harmless. If the hashing algorithm is weak, an attacker may be able to crack it and recover the original password.

As a pentester, the goal is not just to identify exposed data, but to understand how it is protected, whether that protection is strong enough, and what an attacker could do if it fails.

Thank You for Reading !
