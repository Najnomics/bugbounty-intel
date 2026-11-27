# Exposing an OAuth Token Weakness in Amazon’s Mobile App

- **Source URL:** https://clawshea.medium.com/exposing-an-oauth-token-weakness-in-amazons-mobile-app-a-responsible-disclosure-journey-3b967ab8134f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905211213/https://clawshea.medium.com/exposing-an-oauth-token-weakness-in-amazons-mobile-app-a-responsible-disclosure-journey-3b967ab8134f
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9912 (id 9912)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Exposing an OAuth Token Weakness in Amazon’s Mobile App: A Responsible Disclosure Journey

## How a Simple Burp Suite Interception Revealed Serious Risks in Token Handling and User PII Exposure

Cybersecurity isn’t just a profession — it’s a mindset. Sometimes, the most profound flaws are hidden in plain sight, waiting for a watchful eye to uncover them. This is the story of how I responsibly discovered a critical vulnerability in Amazon’s OAuth 2.0 token flow using only my own device, and the steps I took to test, validate, and report it.

1. **The Setup — Testing on My Own Amazon Fire Tablet:**

As part of my ongoing device pentesting series, I focused on Amazon’s MAPClientLib traffic from a Fire Tablet running Android 5.1.1. Using Burp Suite Community Edition and a MitM certificate installed on my device, I began capturing HTTPS traffic during app interactions.

**2. The First Sign — Replaying the Refresh Token:**

Within the traffic logs, I noticed a refresh token used in the `/auth/token` endpoint. I replayed the exact same POST request after 48 hours with Burp Repeater. To my surprise, it still responded with an HTTP 200 OK and issued a new access token. This indicated the refresh token had not expired and lacked session binding.

In the Repeater — I was able to use the same token well after 48 hours, June 12th; The original request was from June 8th, as you can see in the image above:

As you can see, the token is still valid and I got an OK response with a new access token.

**3. Metadata Manipulation: Does Amazon Validate Device Identity?**

Next, I altered individual fields inside the `device_metadata` JSON of the original request:

- Changed the MAC address
- Faked the device serial number
- Nullified the Android ID
- Randomized the app name

The response remained unchanged: a valid access token was returned each time. The metadata appeared completely unvalidated.

**4. The Curl Test: Pulling PII Outside the App:**

Armed with the new access token, I ran the following in my Kali terminal:

```
curl -X GET https://api.amazon.com/user/profile \
     -H "Authorization: Bearer <ACCESS_TOKEN>"
```
This returned my full user profile, including my name, email address, and user ID. This proved the token was functional even outside the app, without any device/session/IP binding:

**5. Findings Summary:**

- **Refresh Token Replayable:** A token captured days earlier still functioned.
- **Device Metadata Ignored:** Spoofed and missing fields did not affect token issuance.
- **Token Not Bound to Device:** Tokens worked from unrelated clients (e.g., curl).
- **PII Exposure Risk:** Profile data was exposed with minimal friction.

**6. The Responsible Path — Reporting to Amazon:**

I compiled all my findings, included screenshots, curl outputs, and a full timeline, then submitted the vulnerability through Amazon’s official disclosure program. This included a detailed breakdown of attack surface, risk level (Critical for PII exposure), and CVSS-like reasoning for severity.

**7. Reflection:**

**What This Means for Developers** OAuth 2.0 is powerful, but without proper session binding, token rotation, and metadata validation, it becomes a risk vector. This case shows why **defense-in-depth** is more than a buzzword.

**8. Recommendations**

- Implement refresh token rotation
- Validate `device_metadata` server-side
- Shorten token TTLs
- Bind tokens to client sessions (DPoP, MTLS, etc.)

## **Conclusion**

This journey started with curiosity and ended with a deeper understanding of how even trusted systems can carry latent weaknesses. As developers and security researchers, our job is to shine a light — responsibly, transparently, and always with the intention to protect.

\*\*Master the basics of Networking, binary numbers and subnetting [*here*](https://www.amazon.com/Mastering-Binary-Numbers-Subnetting-Comprehensive-ebook/dp/B0D9R7W257/ref=sr_1_1?crid=35ER42MZ1JBVX&dib=eyJ2IjoiMSJ9.bA49KtFND_e_g4qEhuThUy6wYnlFK_u_4e47WKHBLIN9C2yOhWoJ05NzWoepuFKqjXwODkXzI9Y8YehP47GlW4-oeR7uL0-my7RPRfpeZtJbxXursiJGNl2bdlJbuhi1.X8_fsw514v0Ga_efGuxQyc20PsyITfGBRD5lfSGi8J4&dib_tag=se&keywords=mastering+binary+numbers&qid=1743178076&sprefix=mastering+binary+numbers%2Caps%2C185&sr=8-1&irclickid=zwTzT42m2xyPW6HVA0VoJw1jUks3bn3xy1hRTc0&ref=dmm_asc_ir_4061861_zwTzT42m2xyPW6HVA0VoJw1jUks3bn3xy1hRTc0&irgwc=1).\*\*
