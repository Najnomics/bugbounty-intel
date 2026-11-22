# JWT [JSON WEB TOKENS] [ ALGORITHM CONFUSION ATTACK] (0x03)

- **Source URL:** https://infosecwriteups.com/jwt-json-web-tokens-algorithm-confusion-attack-0x03-3b1e3ab6030e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230529075539/https://infosecwriteups.com/jwt-json-web-tokens-algorithm-confusion-attack-0x03-3b1e3ab6030e
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2288 (id 2288)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# [JWT \[JSON WEB TOKENS\] \[ ALGORITHM CONFUSION ATTACK\] (0x03)](https://medium.com/bugbountywriteup/jwt-json-web-tokens-explanation-exploitation-0x02-cea23008314f?source=user_profile---------0----------------------------)

--

Hi! My name is Hashar Mujahid. I am a security researcher and a penetration tester. This blog is part 3 of the comprehensive exploitation of JSON web tokens. I recommend you read the first part and 2nd of this series as well.

Part 1:

Part 2:

In the previous series of JSON web tokens, we discuss all the attack possibilities. Let's now discuss Algorithm confusion attacks in JSON web tokens.

## **WHAT ARE ALGORITHM CONFUSION ATTACKS?**

Algorithm confusion attacks are also known as key confusion attacks. In this scenario, the attacker is able to validate a JWT signed with a different algorithm rather than the intended or implemented algorithm in the backend.

This allows an attacker to forge a valid JWT without signing it with the server’s side secret key.

**FOR EXAMPLE:**

Let’s consider a Web server that has an RSA algorithm for validating the JWT token. But the attacker forged his own jwt using the HMAC algorithm The server will skip the checking for the valid algorithm and accept this new forged token as valid token.

Now let’s discuss the main causes of

# How do algorithm confusion vulnerabilities arise?

Algorithm confusion attacks in JWTs can arise through a number of different vectors, including:

1. Vulnerable libraries or frameworks: If the code or libraries used to create or validate JWTs are vulnerable to attacks, an attacker may be able to modify the algorithm used to sign the token.
2. Insecure token generation: If the code used to generate JWTs does not validate or sanitize input properly, an attacker may be able to inject their own algorithm into the token header.

The typical code function that is use to verify the token in vulnerable jwt libraries might look something like this.

```
def verify(token, secretOrPublicKey):
    algorithm = jwt.get_unverified_header(token).get("alg")
    if algorithm == "RS256":
        # Use the provided key as an RSA public key
        decoded_token = jwt.decode(token, secretOrPublicKey, algorithms=["RS256"])
        return decoded_token
    elif algorithm == "HS256":
        # Use the provided key as an HMAC secret key
        decoded_token = jwt.decode(token, secretOrPublicKey, algorithms=["HS256"])
        return decoded_token
```
We can see the verify function takes 2 inputs a JWT and a Publickey or secret. It first checks the algorithm type and then proceeds to verify.

**BUT IF**

The attacker forges his own JWT signed with the public key as a secret using the HMAC algorithm the code will now skip the RS256 and run the code block in HS256. Which will treat the public key as a valid secret and verify the token.

The code that is vulnerable written on the backend could look similar to this.

```
import jwt
public_key = "-----BEGIN PUBLIC KEY-----\n<public-key-of-server>\n-----END PUBLIC KEY-----\n"
token = request.cookies.get("session")
# The following generic verify() method assumes an algorithm-agnostic approach
def verify(token, secretOrPublicKey):
    decoded_token = jwt.decode(token, secretOrPublicKey, algorithms=["RS256", "HS256"])===> HERE LIES THE PROBLEM
    return decoded_token
verified_token = verify(token, public_key)
```
We can see the `algorithms=[RSA256 , HS256]` makes the code vulnerable because when the verify function will be called it will then treat the server key as an HS256 secret.

Now let’s discuss how we can perform this attack.

# STEPS TO PERFORM ALGORITHM CONFUSION ATTACK.

**Step 1: Finding the Sever Public Key:**

By reading the above example this can be easily deduced that we need to have a public key to the server. This path of the public key could be found during fuzzing or reviewing the web traffic. Some common paths are also worth checking like `/jwks.json` or `/.well-known/jwks.json.`

**Step 2: Converting it to a suitable format.**

To perform an algorithm confusion attack, the attacker needs to sign the JWT with a key that matches the server’s local copy used to verify the signature. This copy may be stored in a different format than the one provided by the server. The attacker can convert the server’s JWK-format public key to the necessary format using tools like the JWT Editor extension in Burp

**Step 3: Temper your JWT**

Now just temper the values in the payload section like setting the username to admin and also setting the alg type to HS256.

After that, you just need to sign your jwt using the public key as a secret.

Let’s solve a lab to get a better hang of this.

This lab uses a JWT-based mechanism for handling sessions. It uses a robust RSA key pair to sign and verify tokens. However, due to implementation flaws, this mechanism is vulnerable to algorithm confusion attacks.

To solve the lab, first obtain the server’s public key. This is exposed via a standard endpoint. Use this key to sign a modified session token that gives you access to the admin panel at `/admin`, then delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

**SOLUTION:**

Let’s Repeat the steps.

Retrieve the PUBLIC KEY:

The public key can be found in /jwks.json.

Convert it to a suitable format:

To convert the key follow these steps:

To convert the server’s JWK-format public key to the necessary format, use the JWT Editor extension in Burp. After loading the extension, go to the JWT Editor Keys tab in the main tab bar. Then, create a new RSA key by pasting the JWK obtained earlier and selecting the PEM radio button. Copy the resulting PEM key and base64-encode it in the Decoder tab. Next, create a new symmetric key in the JWT Editor Keys tab by clicking Generate and replacing the generated value for the k parameter with the base64-encoded PEM key. Finally, save the key.

Step 3:

Now just sign this with the key we converted

After signing the token send the request.

Now just delete the user named Carlos.

We can see we were able to successfully exploit the algorithm confusion vulnerability.

Follow me for more to read more content related to WEB Pentesting Bug Bounty and API pen-testing.

Hope you all enjoyed this blog as much as i enjoyed writing it. See you all in the next blog till then Happy Hacking ❤.
