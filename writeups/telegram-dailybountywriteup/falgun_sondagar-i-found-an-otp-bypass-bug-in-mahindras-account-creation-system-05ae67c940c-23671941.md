# I Found an OTP Bypass Bug in Mahindra’s Account Creation System

- **Source URL:** https://medium.com/@Falgun_Sondagar/i-found-an-otp-bypass-bug-in-mahindras-account-creation-system-05ae67c940c6
- **Fetched from:** https://web.archive.org/web/20261001231235/https://medium.com/@Falgun_Sondagar/i-found-an-otp-bypass-bug-in-mahindras-account-creation-system-05ae67c940c6
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14929 (id 14929)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# I Found an OTP Bypass Bug in **Mahindra’s** Account Creation System

**By Falgun Sondagar**

## Introduction

Security research often starts with curiosity a simple “what happens if I try this?” moment. That’s exactly how this discovery began. While exploring the account creation flow on [**Mahindra’s international website**](https://auto.mahindra.com/), I noticed something in the OTP (One-Time Password) verification process that seemed… off. A few tests later, I had confirmed a critical authentication bypass vulnerability that allowed accounts to be created **without valid OTP verification**.

This is the story of that discovery, the frustrating silence that followed, and how responsible disclosure through [**CERT-In (Indian Computer Emergency Response Team)**](https://www.cert-in.org.in/) ultimately led to the issue being fixed.

## The Discovery

During routine testing of the account creation process on Mahindra’s platform, I focused on how the system handled OTP verification a step meant to confirm that the user genuinely owns the phone number or email being registered. This is a critical security control; if it can be bypassed, it undermines the entire authentication process, opening the door to fraudulent account creation, spam registrations, and potential abuse at scale.

After careful, methodical testing, I confirmed that the OTP verification step could be bypassed, allowing an account to be created successfully without ever entering the correct OTP.

I’ve intentionally kept the exact technical methodology out of this article. Given that this is an international platform with a large user base, publishing a step-by-step exploitation guide could put similar systems at risk if the same flaw exists elsewhere. If you’re a fellow security researcher or recruiter and want to understand my exact testing methodology, feel free to check my process and background on [**LinkedIn Post**](https://lnkd.in/p/dfBKjsNm) — I’m always open to discussing the technical details professionally, one-on-one.

## The Impact

An OTP bypass on an account creation flow isn’t just a minor glitch, it’s a serious security gap. Left unaddressed, it could have allowed:

- **Mass creation of unverified/fake accounts** on an international platform
- **Abuse of the registration system** for spam or automated attacks
- Undermining of **user trust** in the platform’s identity verification process
- Potential downstream risks if account creation is linked to other services (loyalty programs, dealer portals, service bookings, etc.)

For a company with the scale and global presence of Mahindra, a flaw like this in a customer-facing, international-facing system carries real business and reputational risk.

## Reporting the Vulnerability: A Frustrating Silence

Once I confirmed the vulnerability, I did what any responsible security researcher would do, I reported it directly to Mahindra.

Over the course of **more than a month**, I:

- Sent **multiple emails** detailing the vulnerability
- Reached out using **several different email addresses**, hoping to reach the right team

Despite these efforts, I received **no response whatsoever** no acknowledgment, no confirmation, not even an automated “we’ve received your report.” For a company operating an international digital platform, this silence was surprising and, frankly, concerning. Responsible disclosure only works when there’s a channel for researchers to be heard and in this case, that channel seemed to not exist.

## Escalating to CERT-In

After a month of unanswered emails, I made the decision to escalate the matter to **CERT-In**, India’s national nodal agency for responding to cybersecurity incidents. I submitted a detailed report of the vulnerability, including its potential impact, through their official reporting channel.

CERT-In registered the case under reference **CERTIn-75449726**, and to their credit, the process moved forward from there. Shortly after, **the vulnerability was fixed** on Mahindra’s website.

## Lessons Learned

This experience taught me a few important things about responsible disclosure:

1. **Direct reporting doesn’t always work** — even for large, international organizations, having a clear and responsive security contact channel is essential, and its absence can delay critical fixes.
2. **National CERTs matter** — CERT-In played a crucial role in bridging the gap between an independent researcher and a large corporation, ensuring the issue didn’t fall through the cracks.
3. **Persistence pays off** — a month of silence could have discouraged me from following through, but escalating through the right channel got the job done.
4. **Recognition shouldn’t be an afterthought** — while the vulnerability was fixed, formal acknowledgment (such as a Hall of Fame listing) from the company is still something I believe responsible researchers deserve, and I continue to follow up on this.

## Closing Thoughts

Finding and reporting this OTP bypass vulnerability was a reminder of why responsible disclosure matters not just for the researcher, but for the millions of users who trust platforms like Mahindra’s with their personal information every day. It’s also a reminder that security is a shared responsibility, and organizations especially those operating internationally need robust, responsive channels to work with the security community.

If you’re a security researcher, recruiter, or just curious about the technical details behind this discovery, feel free to connect with me on [**LinkedIn: Falgun Sondagar**](https://www.linkedin.com/in/falgun-sondagar) — I’m happy to discuss my methodology and findings further.

**X ( Twitter ):** [https://x.com/Falgun\_Sondagar](https://x.com/Falgun_Sondagar)

*Disclaimer: All testing was conducted responsibly and ethically, using my own accounts, with the sole intention of identifying and reporting the vulnerability for remediation. No user data was accessed, misused, or disclosed.*
