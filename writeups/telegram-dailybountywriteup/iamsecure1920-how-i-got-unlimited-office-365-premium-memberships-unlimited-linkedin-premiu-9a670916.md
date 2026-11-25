# How I Got Unlimited Office 365 Premium Memberships & Unlimited LinkedIn Premium Vouchers

- **Source URL:** https://medium.com/@iamsecure1920/how-i-got-unlimited-office-365-premium-memberships-unlimited-linkedin-premium-vouchers-42ca4231e2af
- **Fetched from:** https://medium.com/@iamsecure1920/how-i-got-unlimited-office-365-premium-memberships-unlimited-linkedin-premium-vouchers-42ca4231e2af?source=rss-56bdc22de10------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14940 (id 14940)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** iamsecure1920 (Sai Krishna Sobila ) / Fri, 09 Oct 2026 00:58:33 GMT

The story of a tiny “+” that broke the gate — and what it taught me about identity, rate limits, and responsible disclosure.

A quick note before we dive in: This vulnerability has been fixed. I reported it to Microsoft, waited roughly five months after the fix, and I’m sharing it now for educational purposes. Please don’t try this on live systems. Responsible disclosure keeps the ecosystem healthy.

The Bug That Whispered

Security bugs don’t always announce themselves with crashing servers or dramatic zero-days. Sometimes they whisper. Mine whispered with a plus sign.

I was poking around the Microsoft 365 Education signup flow. Nothing fancy. Just a researcher with a .edu email and a curious mind. I entered test@redacted.edu, verified it, and watched a 12-month free subscription light up. Normal enough.

Then I wondered: What if I add a plus tag?

Most email providers treat test+1@redacted.edu as the same inbox as test@redacted.edu. It’s a feature, not a bug. It’s called sub-addressing. Gmail does it. Outlook does it. Plenty of university mail systems do it. It’s handy for filtering newsletters, sorting receipts, and generally keeping your digital life from becoming a landfill.

So I tried test+1@redacted.edu.

The verification email landed in test@redacted.edu. I clicked. Another trial activated.

Then I tried test+2@redacted.edu.

Same inbox. Another trial.

The gate wasn’t locked. It was just pretending.

One Inbox, Infinite Identities

Here’s the heart of it: Microsoft’s signup flow was treating test+1@redacted.edu and test+2@redacted.edu as two different people. My inbox knew better. Every verification email arrived in the same place. Every account was mine. Every trial was mine.

The system was checking the string, not the identity.

That’s the gap. That’s where the vulnerability lived.

What is sub-addressing?

According to RFC 5322 and RFC 5233, the local part of an email address can contain a “+ tag” that many providers ignore when delivering mail. So:

test@redacted.edu → main inbox

test+1@redacted.edu → same inbox

test+2@redacted.edu → same inbox

test+anything@redacted.edu → same inbox

It’s a beautiful feature. It’s also a landmine if your identity system doesn’t canonicalize addresses before enforcing rate limits.

Microsoft’s didn’t.

Reproduction Steps

Prerequisites:

A valid .edu email address with sub-addressing support. In this write-up, the main email is test@redacted.edu.

Step 1: The First Crack

Go to the Microsoft 365 Education offer page.

Sign in with an existing Microsoft account or create a new one.

On the payment setup page, enter test+1@redacted.edu.

Complete the payment method setup. No charge is required for the trial.

Check the inbox at test@redacted.edu for the verification email.

Click the verification link.

Return to the payment page and click Continue.

Result: A 12-month free subscription is activated for test+1@redacted.edu.

Step 2: The Repeatable Bypass

Sign out or open an incognito window.

Repeat Step 1 using test+2@redacted.edu.

The verification email arrives in the same inbox: test@redacted.edu.

Verify and complete signup.

Result: A second 12-month free subscription is activated on the same email infrastructure.

Repeat with +3, +4, +5… The well never runs dry.

Root Cause: The Missing Canonicalization

The Microsoft Account identity system failed to canonicalize email addresses according to RFC 5322/5233 sub-addressing conventions before enforcing account creation rate limits. In plain English: it didn’t strip the +tag before asking, “Have I seen this identity before?”

Intended security control: One account per unique identity (email address).

Bypass mechanism: Sub-addressing aliases treated as distinct identities.

Result: Rate-limiting bypass enabling unlimited automated account provisioning.

It’s a classic case of string matching masquerading as identity verification. The system saw test+1 and test+2 as strangers. The inbox saw them as the same person wearing different hats.

Why This Matters More Than Free Trials

It’s tempting to shrug and say, “So what? Free trials.” But the impact reaches further than a few extra months of Microsoft 365.

Scenario 1: Service Abuse

Automated account creation can abuse OneDrive storage, Teams resources, or API quotas. The resource exhaustion is spread across multiple “identities” that resolve to a single actor. Detection becomes a nightmare. Mitigation becomes a game of whack-a-mole.

Scenario 2: The Ripple Effect — Cross-Product Entitlements

Here’s where it gets even more interesting. Each bypassed account didn’t just unlock Microsoft 365. It triggered a cascade of cross-product entitlement provisioning. That included a 12-month LinkedIn Premium Career subscription, delivered through Microsoft Store infrastructure.

Think about that. One plus sign didn’t just get you Office apps. It pulled in LinkedIn Premium. It expanded the resource impact across multiple Microsoft services, all tied to a single email inbox. The attacker could manage everything from one place. Centralized coordination. Distributed abuse. A single point of control for a sprawling network of entitlements.

This violates the CIA triad in two directions:

Availability: Resource exhaustion across shared services.

Integrity: Business rule enforcement is undermined. The “one account per identity” control becomes a polite suggestion.

**The Fix**

Microsoft addressed the issue after my report. The signup flow now properly canonicalizes email addresses before enforcing rate limits and account creation controls. Sub-addressed aliases are recognized as belonging to the same underlying identity. The gate is closed.

I waited about five months after the fix before writing this. That’s Coordinated Vulnerability Disclosure in action. The bug is dead. The lesson lives.

**Timeline**

Date Event

\[Feb 7,2026\] Vulnerability reported to Microsoft

\[Mar 16, 2026\] Microsoft released a fix

September 2026 Public disclosure via Medium

**Lessons Learned**

Email is not identity. It’s a string.

If you treat it as identity, you must canonicalize it first. Otherwise, you’re building security on quicksand.

RFC features are double-edged swords.

Sub-addressing is useful. It’s also a bypass waiting to happen if your rate limits don’t understand it.

Rate limits must be identity-aware.

Throttling by raw email string is not enough. You need to throttle by the actual human or mailbox behind the string.

Cross-product entitlements amplify impact.

One bug can ripple across an entire ecosystem. Always consider what else gets provisioned when an account is created.

Responsible disclosure works.

Report it. Wait. Then teach. Everyone wins.

Thank You, Microsoft

Thanks to the MSRC team for taking the report seriously and fixing it. This isn’t a story about dunking on Microsoft. It’s a story about how even small gaps in identity logic can open surprisingly wide doors.

To my fellow researchers: keep pulling threads. Sometimes the smallest thread unravels the biggest knot. But do it responsibly. Report. Wait. Then share what you learned.

And to developers: the next time you write a rate limiter, ask yourself one question.

Are you checking the string, or are you checking the identity?

**About the Researcher**

Sai Krishna Sobila is a security researcher focused on identity systems, access control, and web application security. This research was conducted independently and reported responsibly to Microsoft.

This article is for educational purposes only. The vulnerability described has been fixed. Do not attempt to exploit similar behavior against any system without explicit authorization.
