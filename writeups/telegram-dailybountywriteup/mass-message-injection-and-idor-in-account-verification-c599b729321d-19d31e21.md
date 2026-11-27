# Mass Message Injection and IDOR in Account Verification

- **Source URL:** https://kingcoolvikas.medium.com/mass-message-injection-and-idor-in-account-verification-c599b729321d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260707110446/https://kingcoolvikas.medium.com/mass-message-injection-and-idor-in-account-verification-c599b729321d
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9865 (id 9865)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Mass Message Injection and IDOR in Account Verification

Hello everyone,

I hope you’re doing well. Today, I’m sharing a detailed write-up about two impactful vulnerabilities I discovered on the same program — both affecting user trust and core account verification functionality.

This particular bug bounty program has a narrow scope with only 2–3 domains in scope. Given that, I decided to deep-dive into the main application, which led me to uncover the following two bugs:

## Bug 1: Mass Message Injection — Sending Malicious Links to All Customers

When creating an account on the platform and proceeding to purchase an item, the checkout process requires account verification. During this ID verification step, users are given two options:

1. **Upload ID directly via the website**, or
2. **Choose to receive a secure upload link via SMS** (by entering their mobile number).

At first glance, the feature appeared secure. I explored the verification flow without using any tools, just to understand the UX logic. Once I had a clear picture, I started intercepting the traffic with **Burp Suite** and noticed a key request:

`POST /api/v1/verification/send-sms`
This request contained two parameters:

- `"to_phone_number"`: the recipient’s mobile number
- `"url"`: the link used to upload ID documents

I tested what would happen if I modified both parameters — by inserting **my own malicious URL** and setting the phone number to another user’s. Upon sending the modified request, I received a **200 OK**, and the link was successfully delivered to the victim’s phone.

Interestingly, the platform uses a URL shortener to send these links (likely due to long URLs), which made it even easier to obfuscate the malicious link. As a result, this vulnerability can be abused to **mass-deliver phishing or malicious payloads** to all customers, given only their phone numbers.

## Bug 2: IDOR — Unauthorized ID Verification Submission on Other Accounts

Now, let’s look at the second bug.

As mentioned earlier, the platform shortens the document upload links using a predictable pattern. I observed that the shortened links followed an **ascending, predictable sequence**:

```
https://example.com/aa  
https://example.com/ab  
https://example.com/ac  
...
```
This sequential nature meant that I could **enumerate** a large number of existing shortened URLs. Many of them were still active and led directly to document submission pages for other users’ ID verifications.

This introduced a serious **IDOR (Insecure Direct Object Reference)** vulnerability — I could upload ID documents on behalf of other users, effectively hijacking their identity verification process. This could:

- Prevent legitimate users from verifying their accounts
- Be abused at scale, affecting a large portion of the user base

## Conclusion

Both bugs demonstrate a serious lack of input validation and access control:

- The **first bug** allows attackers to **send arbitrary, potentially malicious links** to any user via SMS — enabling large-scale phishing or social engineering attacks.
- The **second bug** allows an attacker to **interfere with critical account verification**, possibly locking users out or misusing the verification pipeline.

Thanks for reading. I hope this write-up helps others understand how small oversights in logic and authorization can lead to major security issues.
