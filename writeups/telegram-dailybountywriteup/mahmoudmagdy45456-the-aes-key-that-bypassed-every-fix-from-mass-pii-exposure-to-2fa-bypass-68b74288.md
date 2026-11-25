# The AES Key That Bypassed Every Fix

- **Source URL:** https://medium.com/@mahmoudmagdy45456/the-aes-key-that-bypassed-every-fix-from-mass-pii-exposure-to-2fa-bypass-8143c9326f34
- **Fetched from:** https://medium.com/@mahmoudmagdy45456/the-aes-key-that-bypassed-every-fix-from-mass-pii-exposure-to-2fa-bypass-8143c9326f34?source=rss-65fcf9c19d05------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14931)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mahmoud Magdy / Fri, 02 Oct 2026 19:35:41 GMT

Sometimes you find a random secret in JavaScript and the first question should be:

**“What is this actually used for?”**

That’s exactly what happened here.

While testing the application, I was looking through the publicly accessible JavaScript files.

I found this:

REACT\_APP\_AES\_KEY = "\<REDACTED>"

The key was inside the frontend JavaScript.

At this point, I didn’t know its purpose.

So I didn’t want to assume that simply finding an AES key meant there was a vulnerability.

I wanted to know:

***What is this key actually used for?***

I had previously reported several vulnerabilities on the same application : [https://medium.com/@mahmoudmagdy45456/how-i-landed-5-bounties-on-the-same-platform-c8d910b5f4cd](https://medium.com/@mahmoudmagdy45456/how-i-landed-5-bounties-on-the-same-platform-c8d910b5f4cd)

For example:

GET /api/proxy-service/companies?tenantCode=PIL&companyRegistrationNumber=1

and:

GET /api/proxy-service/reference-data/USER\_ROLE?tenantCode=PIL

GET /api/proxy-service/admin/bl/companies

These APIs were returning sensitive information without the proper access controls.

The company fixed those issues.

But as part of the fix, they changed how the API responses were handled.

Instead of restricting access to the APIs properly, they started **encrypting the API responses** so the returned data was no longer directly readable.

So when I found the AES key, I immediately thought:

***Could this be the key they introduced to protect the API responses after my previous reports?***

That was the first thing I wanted to test.

I took one of the encrypted API responses and wrote a small script that used the exposed AES key to decrypt it.

The idea was very simple:

Get encrypted API response

↓

Use exposed AES key

↓

Decrypt response

↓

Read original JSON

```
const crypto = require("crypto");
const key = Buffer.from("<AES-KEY>");
const data = Buffer.from("<encrypted_response>", "base64");
const iv = data.slice(0, 12);
const encrypted = data.slice(12);
const tag = encrypted.slice(-16);
const text = encrypted.slice(0, -16);
const decipher = crypto.createDecipheriv("aes-256-gcm", key, iv);
decipher.setAuthTag(tag);
let decrypted = decipher.update(text, null, "utf8");
decrypted += decipher.final("utf8");
console.log(decrypted);
```
I didn’t need to break AES.

I didn’t need to guess the key.

The key was already sitting inside the frontend.

After implementing the same AES-GCM logic used by the application, I tested it against a real API response.

And…

**It worked.**

The encrypted response was successfully decrypted.

This was the moment the finding became much more interesting.

The application had fixed my previous reports.

They had introduced encryption to prevent someone from simply reading the API responses.

But the encryption key was available to anyone who could download the JavaScript.

And the decrypted responses contained sensitive information such as company and contact data.

So the issue wasn’t just:

***There is an AES key in JavaScript.***

The important part was:

***The exposed key allowed me to defeat the encryption that had been introduced as part of the security fix.***

After confirming that the key worked against the API responses, I started looking for other places where the same encryption was used.

That’s when I found something much more interesting.

The application also used encrypted data during the **2FA verification flow**.

I captured the encrypted verification response and decrypted it using the same key.

After decryption, I found a value similar to:

mahmoudmagdy45456@gmail.com:null:1776557237487:N

The important part was the last value:

N

It represented the verification state.

At this point, I wanted to see whether the server actually validated this value properly.

So I changed:

to:

Y

The value became:

mahmoudmagdy45456@gmail.com:null:1776557237487:Y

Then I re-encrypted the modified value using the same AES key.

```
const crypto = require("crypto");
const key = Buffer.from("<AES-KEY>");
const plaintext = "<Decrypted modified Verification Response>";
// Generate random IV (12 bytes for GCM)
const iv = crypto.randomBytes(12);
try {
    const cipher = crypto.createCipheriv("aes-256-gcm", key, iv);
    let encrypted = cipher.update(plaintext, "utf8");
    encrypted = Buffer.concat([encrypted, cipher.final()]);
    const tag = cipher.getAuthTag();
    // Combine: IV + ciphertext + tag
    const result = Buffer.concat([iv, encrypted, tag]).toString("base64");
    console.log(result);
} catch (err) {
    console.error("❌ Error:", err.message);
}
```
So my process was:

Original encrypted response

↓

Decrypt using exposed key

↓

Change N → Y

↓

Encrypt again using the same key

↓

Send modified response

I sent the modified value back to the application.

And it worked.

The server accepted the modified encrypted response as valid.

without completing the actual verification step.

That demonstrated a **2FA bypass**.

**The chain looked like this:**

Original API vulnerabilities

↓

Fixed

↓

API responses encrypted

↓

AES key exposed in JavaScript

↓

Key extracted

↓

API responses decrypted

↓

Same key found in 2FA flow

↓

N changed to Y

↓

Response re-encrypted

↓

2FA bypass

That’s what made the finding much more interesting than simply finding a hardcoded secret.

If you find a secret in frontend JavaScript, don’t immediately assume you know the impact.

First ask:

***What is this secret used for?***

In my case, I found the key first.

Then I remembered the previous fixes.

Then I realized:

***They had started encrypting the API responses.***

That gave me a direction.

I built a small script using the exposed key.

The encrypted API response decrypted successfully.

Then I followed the key further and found that it was also involved in the 2FA flow.

Changing:

N → Y

and re-encrypting the response was enough to make the server accept the verification state.

So one exposed key ended up bypassing **the protection that had been introduced after the original vulnerabilities were fixed**, and it also led to a demonstrated 2FA bypass.

**LinkedIn:**

[https://www.linkedin.com/in/mahmoud-magdy-0a8078269/](https://www.linkedin.com/in/mahmoud-magdy-0a8078269/)

**Email:**

[mahmoudmagdy45456@gmail.com](mailto:mahmoudmagdy45456@gmail.com)

**Thanks for reading, and stay safe out there 🛡️**
