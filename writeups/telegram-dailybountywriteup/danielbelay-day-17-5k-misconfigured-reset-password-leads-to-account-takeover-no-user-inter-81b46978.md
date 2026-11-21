# Day 17

- **Source URL:** https://medium.com/@danielbelay/day-17-5k-misconfigured-reset-password-leads-to-account-takeover-no-user-interaction-ato-4d378e995fc2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250827192814/https://medium.com/@danielbelay/day-17-5k-misconfigured-reset-password-leads-to-account-takeover-no-user-interaction-ato-4d378e995fc2
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8860 (id 8860)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Day 17: \[$5K\] Misconfigured Reset Password Leads to Account Takeover (No User Interaction ATO)

*By Aditya Sharma*

*Published on Aug 24, 2021–4 min read*

## Introduction

Hello folks! I hope you’re all staying safe and healthy. Today, this write-up shares an **account takeover (ATO) vulnerability** discovered in a **public program on HackerOne**. The target was one of the leading **online adult entertainment platforms**.

This was an interesting **server misconfiguration** that allowed the researcher to take over **any user account** without any interaction from the victim. The vulnerability was found **within 5–10 minutes**, and the researcher was rewarded with a **$5,000 bounty**! 🚀

## Summary of the Vulnerability

While testing the platform’s **affiliate registration page**, the researcher found a **misconfigured password reset functionality** that leaked **password reset tokens** in API responses. By exploiting this, it was possible to **reset the password of any valid user**, leading to a full account takeover.

## Technical Details & Exploitation

## Initial Testing

1. The researcher started by testing **login, signup, and password reset functionalities**.
2. An **OAuth misconfiguration** was discovered, leading to **open redirection**, but it wasn’t critical enough.
3. While testing the **forgot password feature**, it was observed that the application sent a **reset token link** — which seemed normal.

## Finding the Vulnerability

Since the application relied on **AJAX requests**, the researcher examined the **XHR (XMLHttpRequest) responses**.

- When a user clicked **“Forgot Password”**, no visible page reload occurred.
- Instead, a **password reset token was generated in the background.**
- By inspecting the **API calls in the page source**, the following endpoint was found:

`https://company.com/api/REDACTED/resetPasswordToken/`
This API responded with a **leaked reset token**, exposing it to an attacker! 😲

## Exploiting the Misconfiguration

By intercepting the **password reset request**, the researcher found another vulnerable endpoint:

`https://company.com/api/REDACTED/resetPassword/<username>`
The server’s response contained:

```
{
    "id": 11077,
    "token": "4PjLzn7fyLU<Redacted>f1h1P2F",
    "stamp": 1628796031082,
    "username": "test13337"
}
```
💡 **The mistake?**

👉 The **reset token was leaked in the API response** for any **valid username**.

## Full Account Takeover

With the leaked token, crafting a **password reset link** was easy:

`https://www.company.com/#/changePassword/<username>/<token>`
By replacing `<username>` and `<token>` from the API response, the researcher could **reset any user’s password**, completely **taking over their account**!

## Impact

✅ **No user interaction needed**

✅ **Could reset passwords for any user (even admins)**

✅ **Potential for financial fraud (redirecting payments to an attacker’s crypto wallet)**

## Reporting & Bounty

The researcher immediately reported the issue. The security team **validated and triaged** it within **10 minutes**, and a **$5,000 bounty** was awarded the same day.

## Timeline:

- **Issue Found:** Aug 16, 2021 (9:30 PM IST)
- **Issue Reported:** Aug 16, 2021 (10:00 PM IST)
- **Issue Triaged:** Aug 16, 2021 (10:10 PM IST)
- **Bounty Awarded:** Aug 16, 2021 (10:30 PM IST) — 💰 **$5,000**

## Final Thoughts

🚀 **Lessons Learned:**

🔹 Always check API responses for sensitive data leaks.

🔹 AJAX-based applications may hide critical vulnerabilities.

🔹 Think outside the box and **inspect every request/response carefully**.

Hope you enjoyed this write-up! **Stay creative & keep hunting!** 🔥
