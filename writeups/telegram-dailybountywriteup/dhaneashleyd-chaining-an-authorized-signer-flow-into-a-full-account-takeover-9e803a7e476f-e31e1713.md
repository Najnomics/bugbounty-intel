# Chaining an Authorized Signer Flow Into a Full Account Takeover

- **Source URL:** https://medium.com/@dhaneashleyd/chaining-an-authorized-signer-flow-into-a-full-account-takeover-9e803a7e476f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251231114139/https://medium.com/@dhaneashleyd/chaining-an-authorized-signer-flow-into-a-full-account-takeover-9e803a7e476f
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/12020 (id 12020)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Chaining an Authorized Signer Flow Into a Full Account Takeover

All glory to God, who grants wisdom and understanding. The following write-up documents security weaknesses identified during responsible research.

Hello, my name is Dhane Ashley Diabajo (pseudo\_), a bug bounty hunter from the Philippines. This write-up shares my experience uncovering a series of security flaws during authorized testing of a U.S.-based financial services web application, with the goal of responsibly reporting and improving its security posture.

## Background

During my initial review of the application, I focused on account security and profile management features. One of the first things I noticed was that sensitive profile changes—such as updating a phone number—were protected by multiple layers of verification. These included a one-time passcode sent to the phone number, facial verification, and government-issued document checks.

At first glance, these controls appeared strong and well-designed. As someone who frequently tests fintech applications, this aligned with what I would expect from a platform handling highly sensitive financial and identity data.

However, experience has taught me that security issues often don’t lie in the obvious or well-protected paths, but rather in alternate workflows that interact with the same data.

That curiosity led me to explore other areas of the application.

## The Authorized Signer Feature

While reviewing the student loan application process, I came across the feature that allows users to add an authorized signer. The purpose of this feature is reasonable—many applicants rely on co-signers—but what stood out immediately was how little information was required to add one.

The application only requested the signer’s name and email address.

This raised a simple but important question in my mind:

What happens if the name and email entered belong to an existing user account?

To answer this, I decided to test the scenario using another account that I personally controlled.

## Unexpected PII Disclosure

After adding my other account as an authorized signer, I inspected the backend GraphQL responses associated with the loan application. What I saw was unexpected and concerning.

The response returned extensive sensitive information associated with the signer’s account—far beyond what should be necessary for a loan application flow.

The exposed data included:

- Full name

- Business name (if applicable)

- Residential address

- Income details

- Employment information

- Education information

- Last four digits of the Social Security number

- Last four digits of the phone number

At this point, it was clear that the authorized signer workflow was not properly isolating or restricting access to sensitive user data. This alone represented a significant PII disclosure issue.

Unauthorized Profile Updates

Curious about how deep this issue went, I continued testing the same workflow. I noticed that during the loan application process, I could modify certain details associated with the authorized signer.

Specifically, I was able to update:

- Address

- Phone number

- Income information

I submitted the application to see whether these changes were isolated to the loan context or merely temporary.

To my surprise, after submission, the changes were reflected directly in the signer’s main account profile. No notification was sent, no verification was required, and no approval was requested from the signer.

This meant that a process originally designed for loan applications could be abused to silently update another user’s core profile data, effectively bypassing the document and identity verification controls enforced elsewhere in the application.

Chaining the Issue Into a 2FA Bypass

At this stage, I wanted to understand whether this flaw could be chained with other security features—specifically two-factor authentication (2FA).

The application supports SMS-based 2FA, where login verification codes are sent to the phone number on file. I enabled SMS-based 2FA on the target account and then repeated the authorized signer workflow from a separate account.

The steps were straightforward:

1. Log into a secondary account

2. Initiate a student loan application

3. Add the target account as an authorized signer

4. Modify the signer’s phone number during the application process

5. Submit the application

Once the application was submitted, the target account’s phone number had been updated. When I attempted to log in to the target account, the 2FA verification code was sent to the phone number I controlled.

At that moment, the impact became very clear: if an attacker had the victim’s credentials, this flaw would allow full account takeover despite 2FA being enabled.

## Bypassing KYC and Identity Verification Controls

The application explicitly states that certain identity attributes cannot be changed directly through the profile interface. For changes involving legal name, date of birth, citizenship, or Social Security number, users are instructed to contact customer service and provide official documentation.

Wanting to validate whether this policy was truly enforced across all workflows, I tested the authorized signer submission more deeply. By intercepting and modifying the GraphQL request associated with the signer flow, I was able to alter the following fields:

- Legal name

- Date of birth

- Citizenship

- Social Security number

After submitting the modified request, I logged back into the target account to confirm the result.

All changes were applied successfully. They persisted after logging out and back in, and no document verification, manual review, or additional checks were triggered.

This confirmed a direct bypass of identity verification and KYC controls through an unintended backend pathway.

Impact

By abusing the authorized signer workflow, an authenticated user could:

- Access another user’s highly sensitive PII

- Modify core identity and financial information without consent

- Bypass document verification and KYC requirements

- Chain the issue into a two-factor authentication bypass

- Achieve full account takeover under realistic conditions

All of these issues stem from insufficient authorization checks and broken trust boundaries within backend application logic.

Final Thoughts

This research reinforced a recurring lesson in application security: even when individual features are well protected, overlooked alternate workflows can completely undermine those protections.

Security controls must be enforced consistently across every path that interacts with sensitive data. Otherwise, attackers will always look for—and find—the weakest link.

I hope this write-up helps highlight the importance of holistic security testing, especially in applications that handle financial and identity-critical data.
