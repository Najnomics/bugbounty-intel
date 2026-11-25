# Security Write-Up

- **Source URL:** https://aboutal3b.medium.com/security-write-up-authentication-bypass-via-response-manipulation-on-email-change-feature-c8efbc15c0b1
- **Fetched from:** https://aboutal3b.medium.com/security-write-up-authentication-bypass-via-response-manipulation-on-email-change-feature-c8efbc15c0b1?source=rss-583bbeee9576------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14956 (id 14956)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Yousef / Thu, 22 Oct 2026 14:22:40 GMT

“وَمَا تَوْفِيقِي إِلَّا بِاللَّهِ ۚ عَلَيْهِ تَوَكَّلْتُ وَإِلَيْهِ أُنِيبُ”

Hey everyone! 👋

My name is Yousef Abdullah, and I’m a cybersecurity researcher. Welcome to my write-up! Today, I want to share a story about a cool logic vulnerability I recently discovered during a security assessment on **hollisterco.com**.

If you’re interested in web security, bug bounties, or just curious about how authentication and verification flows can break, this article is for you! So grab your favorite drink ☕, and let’s dive right in.

Imagine you want to update your registered email address on an online platform. To protect your account, the system requires you to enter a one-time password (OTP) sent to your new email to prove ownership.

Now, what if the application decides whether your code is correct based *solely* on a simple flag sent back in the HTTP response (like "success": false), and the front-end code blindly trusts whatever the response says? If an attacker enters a completely random or wrong code, intercepts that response packet, and flips the flag to "success": true, the application says, *"Ah, looks good!"* and updates the email without verifying anything.

This is a classic client-side logic flaw / authentication bypass (CWE-288 / CWE-602) where security controls are improperly enforced on the client side rather than securely validated on the server.

While testing hollisterco.com, I decided to inspect the account settings and the email update feature closely using Burp Suite. I wanted to see how the application handles OTP verification during sensitive account changes.

Here is how the vulnerability panned out:

```
{
  "errors": [
    {
      "message": "INVALID_OTP",
      "extensions": { "code": "UNAUTHENTICATED" }
    }
  ],
  "data": {
    "validateOtpForAccountChange": {
      "success": false,
      "errors": ["Invalid OTP code"]
    }
  }
}
```
**5. The Magic Trick (Response Manipulation):** Instead of letting the failure pass, I modified the response payload in Burp Suite to force a success state:

```
{
  "data": {
    "validateOtpForAccountChange": {
      "success": true,
      "errors": null,
      "__typename": "APIResponse"
    }
  }
}
```
**6. Bypass Successful:** I forwarded the modified response to the client browser, and boom! The application accepted the invalid OTP and successfully bypassed the verification step.

Why is this type of vulnerability dangerous?

If you are a developer or security engineer building modern web apps, here is how you can protect your application against this:

Logical vulnerabilities and response manipulation bugs are often missed by automated scanners because they require human creativity and a deep understanding of application workflows. Always remember to test how applications handle errors, responses, and state changes!

Thank you so much for reading! I hope you learned something new today. If you have any questions or feedback, feel free to connect with me!

**Author:** Yousef Abdullah

**Security Researcher**
