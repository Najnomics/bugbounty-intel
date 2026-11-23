# Logical 2FA Bypass via Missing clientId Parameter in Profile Update Endpoint

- **Source URL:** https://medium.com/@mhmodgm54/logical-2fa-bypass-via-missing-clientid-parameter-in-profile-update-endpoint-3f054bc651d6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250830035202/https://medium.com/@mhmodgm54/logical-2fa-bypass-via-missing-clientid-parameter-in-profile-update-endpoint-3f054bc651d6
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10517 (id 10517)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Logical 2FA Bypass via Missing** **clientId** **Parameter in Profile Update Endpoint**

## Introduction

This write-up describes a logical vulnerability that allowed me to bypass the Two-Factor Authentication (2FA) mechanism in a web application.

The application enforced 2FA verification for **every** modification request, including actions like updating an email, uploading a photo, or changing profile information. However, a missing parameter check in the request led to a complete bypass

## Discovery Process

### Normal Flow for Any Update

1. When a user attempts to update any profile detail, a **2FA prompt** appears
2. The system sends a **One-Time Password (OTP)** to the user’s email
3. The user enters the OTP in the prompt
4. If correct, the server responds with a **special verification token** (different from the original OTP) which is valid for **one specific request**

```
Content-Disposition: form-data; name="verification_code"
xxxxxxx
```
This value is then used to authorize the update request

## Example of an Email Update Request

For example, updating the email sends a request like:

`PUT /api/me/email?clientId=BASE64_value`
The `clientId` value was **constant** across requests even in different account Initially, I suspected it might refer to a gateway

## Initial Bypass Attempts (Failed)

- **IDOR on** **clientId**
**:** Tried modifying it, but it was constant and changes caused the request to fail
- **Token Reuse:** Used the verification token from a successful email update to perform other actions (e.g., updating the name) — failed
- **Rate Limit Testing:** Attempted brute force/rate limit testing on both the OTP and post-2FA token — blocked with `429 Too Many Requests`. The token also expired after 5 minutes
- **Cross-Account Token Use:** Tried using a token from another account’s email change — failed

## The Successful Bypass

When I **removed the clientId parameter entirely**, the request unexpectedly succeeded **without triggering the 2FA flow**

`PUT /api/me/email`
**Result:** The server allowed the update with no OTP verification required

### This meant I could

- Update **any profile field** without providing OTP
- Completely bypass the 2FA enforcement logic for all profile modification endpoints

## End

i wish you benefit from this simple write-up

*أن رجلا جاء إلى رسول الله صلى الله عليه وسلم فقال : ( يا رسول الله ! أيُّ الناس أحبُّ إلى الله ؟ فقال : أحبُّ الناس إلى الله أنفعهم للناس…)*
