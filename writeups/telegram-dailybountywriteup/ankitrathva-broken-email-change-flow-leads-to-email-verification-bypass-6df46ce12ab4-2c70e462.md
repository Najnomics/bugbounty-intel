# Broken Email Change Flow leads to Email Verification Bypass

- **Source URL:** https://medium.com/@ankitrathva/broken-email-change-flow-leads-to-email-verification-bypass-6df46ce12ab4
- **Fetched from:** https://medium.com/@ankitrathva/broken-email-change-flow-leads-to-email-verification-bypass-6df46ce12ab4?source=rss-d479b91985ef------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14909 (id 14909)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ankit Rathva aka Gujarati Hacker / Sat, 12 Sep 2026 16:17:38 GMT

I am Ankit Rathva aka Gujarati Hacker and i am a student of MCA 2nd year, I am an ethical hacker and security researcher with a passion for finding logic, authorization, and data-integrity flaws in web applications. As a bug bounty hunter and red teamer, he combines hands-on testing, forensic analysis, and careful disclosure to help teams fix impactful issues while protecting users. He publishes clear, developer-friendly writeups and practical mitigation advice — connect to follow his work or collaborate on security research.

**Connect with me:** [https://linkedin.com/in/ankitrathva](https://linkedin.com/in/ankitrathva)

While testing an application’s account-management functionality, I came across an interesting flaw in the **email change and email verification flow**.

At first, the functionality appeared to work normally. However, after changing the account email multiple times in a short sequence, I noticed that the application was still sending the email-verification OTP to the **original email address** instead of the newly requested email address.

This created a serious trust-boundary issue.

By abusing this broken state, an attacker could potentially verify an email address without having access to that email’s inbox. In the worst-case scenario, this could lead to **account takeover of another user’s account, including a privileged administrator account**.

***Severity:*** *Critical*
***Vulnerability:*** *Broken Email Change Flow / Improper Email Verification*
***Impact:*** *Potential Account Takeover*

The important security property here is:

**The verification code must be bound to the exact email address that is currently being verified.**

For example:

Old Email: attacker@example.com

New Email: new@example.com

OTP → new@example.com

The problem I found was that this relationship was not properly maintained.

I started testing the email-change functionality using an account that I controlled.

The interesting behavior appeared when I performed multiple email changes in sequence.

The simplified flow looked like this:

Attacker Account

│

▼

Change Email → attacker2@example.com

│

▼

Change Email Again → victim@example.com

│

▼

Click "Verify Email"

│

▼

OTP sent to ORIGINAL email

│

▼

Attacker retrieves OTP

│

▼

Verification succeeds

The application was effectively treating the **old email address as the verification destination**, even though the account’s current pending email had already been changed.

For testing, I used only accounts and email addresses under my control.

I first logged into an account controlled by me.

Current Email:

attacker@example.com

I changed the account email to another attacker-controlled address:

attacker@example.com

↓

attacker2@example.com

Before completing the previous verification flow, I changed the email again to a third address used for testing:

attacker2@example.com

↓

victim@example.com

In a real-world attack scenario, the final address could potentially belong to another user.

I then clicked the application’s **Verify Email** option.

At this point, I expected the OTP to be sent to:

victim@example.com

However, the OTP was instead delivered to:

attacker@example.com

The original email address.

This was the key observation.

Depending on how the application’s authentication and recovery mechanisms are implemented, the vulnerability could allow:

The impact is especially serious when email addresses are used as a primary authentication or account-recovery identifier.

I reported this vulnerability to the affected company through its security reporting channel and provided a detailed proof of concept.

At the time of writing, **I have not yet received a response from the company**.

To avoid exposing users or enabling exploitation, I have intentionally omitted sensitive information such as the real target email address, application-specific endpoints, authentication data, OTP values, and other details that could facilitate attacks against the live system.

If the company provides additional information or confirms remediation, I may update this article accordingly.

This finding was a good reminder that **business logic and state-management vulnerabilities can be just as dangerous as traditional injection vulnerabilities**.

An application can have strong password hashing, secure OTP generation, and properly implemented authentication — but if the relationship between those components is broken, the entire security model can still fail.

When testing account-management functionality, I always recommend looking beyond individual requests.

**Status:** Reported to the vendor

**Vendor response:** No response at the time of publication

**Severity:** Critical

**Category:** Broken Authentication / Improper Email Verification / Account Takeover
