# From Simple Restriction Bypass to Internal Privilege Escalation to High Impact IDOR

- **Source URL:** https://medium.com/@Alharbe0/from-simple-restriction-bypass-to-internal-privilege-escalation-to-high-impact-idor-e7b8366ac70d?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@Alharbe0
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 10514)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Introduction

A few weeks ago, while hunting on an external bug bounty program, I came across a fascinating case of **IDOR (Insecure Direct Object Reference)** that allowed me to modify other users’ accounts across **three interconnected web applications** — without any interaction from the victim. This bug was not just a one-off; I later found the same vulnerability in multiple other bounty programs.

Here’s the full story of how I discovered it, the thought process behind each step, and how it escalated from a harmless bypass to a cross-application account manipulation bug.

### Background

The target consisted of **three web applications** tightly linked together. Creating an account on one app automatically created accounts on the other two. The apps were used for **project management, team collaboration, and time tracking**, with multiple user roles and different privilege levels.

Users could edit only certain profile fields (e.g., bio, public info) within each app. **Sensitive fields like email and name were locked** and could only be updated via a **central account management system**.

### Initial Discovery — Local Restriction Bypass

While testing **App #1**, I edited my bio and capture the request with burp. the request going to /users/me endpoint. In the request body, I noticed a name parameter containing my account’s name.

PUT /users/me HTTP/2

Host: test.com

Accept: application/json, text/plain, \*/\*

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate, br

Content-Type: application/json

Content-Length: 251

Sec-Fetch-Dest: empty

Sec-Fetch-Mode: cors

Sec-Fetch-Site: same-site

Priority: u=0

Te: trailers

{"name":"researcher","email":"test@test.test","title":"wwww","phone":null,"mobilePhone":null,"languageTag":"en-US","timeZone":null,"location":null,"birthDay":null,"workAnniversary":null,"photoBackgroundColor":"green-dark","customFields":{}}

Out of curiosity, I modified the name parameter and sent the request.

Surprisingly, my account name was updated—**bypassing the restriction** that prevented editing it outside the central account system.

At this point, it seemed like a minor bug with no real security impact since I could only modify my own account.

### Other Ways To Modify

Next, I wondered what would happen if I changed the request path from:

PUT /users/me

to:

`PUT /users/{my_account_id}`
It worked! My account updated successfully.

Naturally, I replacing my account ID with another user’s ID — but it failed, returning an error:

`{"status":"FORBIDDEN","message":"Cannot update another user.","errorLabel":"FORBIDDEN","errorCode":0000000}`
### Testing with Other Accounts in My Company

I tried modifying another user’s account **within my own company**.

Success — I could edit their account details.

I tried to modify an account from a **low-privilege account**, it failed. But from an **admin or owner account**, I could edit other users admins’ or even the owner’s details.

So the admin can modify user accounts and the owner account.

At this stage, the impact seemed limited to **internal privilege escalation** (low severity).

### Attempting To Modify Accounts Of Another Companys

After more brainstorming, I remembered that we can inviting an existing user from another company to our company

After sending the invitation to a user in another company and before he accepts the invitation, I can edit his account the same way I edit my company accounts.

This meant I could:

1. Invite a victim’s email to my company.
2. Capture their **user ID** from the API response (no interaction required).
3. Modify his account in the same way.:

`PATCH /users/{victim_id}`
Successfully update the victim’s account — **without accepting the invitation**.

And since all three apps shared the same account system, **the changes reflected across all of them instantly**.

### Impact

- An attacker can modify any account in the three applications by knowing the victim’s email address.

### Conclusion

What started as a small “Bypass a simple restriction” bypass turned into a **cross-application IDOR vulnerability** .

After reporting it responsibly, the issue was fixed, and I was rewarded. Even more interestingly, I later found **the exact same bug pattern** in other bug bounty programs — proving how common (yet dangerous) this flaw can be.
