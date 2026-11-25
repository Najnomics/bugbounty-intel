# IDOR via Weak JWT Validation Leading to Unauthorized Data Access

- **Source URL:** https://medium.com/@0xMo7areb/idor-via-weak-jwt-validation-leading-to-unauthorized-data-access-e8d641750099?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260519132749/https://medium.com/@0xMo7areb/idor-via-weak-jwt-validation-leading-to-unauthorized-data-access-e8d641750099?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13437 (id 13437)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR via Weak JWT Validation Leading to Unauthorized Data Access

*الحمد لله الذي عَلَّمَ بالقلم.. عَلَّمَ الإنسانَ ما لم يَعْلَم والصلاةُ والسلامُ على خيرِ مُعَلِّمي الناسِ الخير محمد أما بعد*

## Let’s Dive into Today’s Bug

Today’s bug is a classic IDOR found on a private HackerOne program — one modified field in a JWT, **and every user profile on the platform becomes yours to read**. No special tools, no complex exploit chain — just a number change and a broken trust assumption.

## Overview

I discovered an IDOR (Insecure Direct Object Reference) vulnerability in the following endpoint:

`GET /user-profile/profile`
The application uses the `user_id` inside the JWT to determine which user profile to return.

However, this value is not validated on the server side.

## How It Works

After authentication, the server issues a JWT like:

```
{
  "user_id": 26452623
}
```
When requesting the profile endpoint, the backend reads this `user_id` and directly fetches the corresponding user data.

The issue is that this value is **trusted without verification**, even though it can be modified by the client.

## Exploitation

1. **Intercept the request:**

```
GET /user-profile/profile
Authorization: Bearer <JWT>
```
and this is **response** with my profile data

I noticed the `user_id`in the request— and I’m guessing the same thought popped into your mind right away :) 

**so, let’s to test for IDOR ☠️**

2\. Modify **user\_id :**for example make

**”user\_id”: 1**

**Result:**

The server returns the profile data of the modified user ID without any vaildation on the **token or Authorization.**

**Repeating this process with different IDs allows access to multiple user profiles.**

## Impact

- Any authenticated user can access other users’ profiles
- Exposure of user data such as:
- Education details
- Institution information
- Job and profile metadata
- The issue can be automated to enumerate users and extract data at scale
- Increases risk of targeted phishing and social engineering

## Root Cause

The application relies on a client-controlled value (`user_id` in JWT) without enforcing object-level authorization checks.

## Fix

- Ensure users can only access their own profile
- Validate ownership on the server side
- Do not rely on JWT claims for authorization decisions
- Implement proper object-level authorization (BOLA protection)

## Takeaway

*Never trust client-controlled data for access control decisions.*


A single unchecked value in a token can expose the entire user base.

## Report Status

This report was marked as a **duplicate**, as the same issue had already been submitted approximately **3 hours earlier**.

I had actually discovered the vulnerability **a day before submitting**, but delayed reporting while attempting to chain it with other issues for greater impact.

Ultimately, the vulnerability was already reported by another researcher — *Alhamdulillah*, it was a good learning experience and a reminder of how fast-paced bug bounty programs can be.

**Let’s Connect: x account || linkedin account**


D*on’t forget to follow me on this medium account :)*

*“سُبْحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ ، أَشْهَدُ أَنْ لا إِلَهَ إِلا أَنْتَ ، أَسْتَغْفِرُكَ وَأَتُوبُ إِلَيْكَ”*
