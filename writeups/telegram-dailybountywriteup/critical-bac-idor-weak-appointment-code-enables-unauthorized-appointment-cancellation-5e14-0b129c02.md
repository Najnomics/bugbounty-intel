# Critical BAC

- **Source URL:** https://kjulius.medium.com/critical-bac-idor-weak-appointment-code-enables-unauthorized-appointment-cancellation-5e145ced50ca
- **Fetched from:** https://kjulius.medium.com/feed
- **Fetched:** 2026-11-18
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14938)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Critical BAC: IDOR + Weak Appointment Code Enables Unauthorized Appointment Cancellation, Modification and PII Disclosure.

While testing a public-facing pre-complaint system, I discovered a **critical Broken Access Control (BAC)** issue involving appointment management.

The system sends users a 6-character appointment code in their confirmation email, following a pattern similar to:

CGXXXX

The CG prefix was static across my test appointments, leaving only four variable characters. The remaining characters were uppercase letters and digits, resulting in an effective keyspace of:

**3⁶⁴ = 1,679,616 combinations**

However, the bigger issue wasn’t simply the code’s entropy.

### The Authorization Problem.

The appointment-management functionality relied on the appointment code as the authorization mechanism.

The backend exposed functionality equivalent to:

```
GET /api/<redacted>/appointments/{code}
DELETE /api/<redacted>/appointments/{code}
```
No authenticated session or additional ownership verification was required.

More importantly, providing a **valid appointment code returned the personal information associated with that appointment**, including:

- First and last name
- Telephone number
- Email address
- Street/address
- ZIP/postal code

This turned the issue from simply an appointment-management flaw into a potential **PII disclosure vulnerability** as well.

An attacker who obtains or successfully guesses a valid appointment code could potentially retrieve sensitive information belonging to another citizen and then use the same code to interact with their appointment.

### Impact.

The vulnerability affected **confidentiality, integrity,** and **availability**.

***Confidentiality.***
A valid appointment code could expose personally identifiable information belonging to the appointment owner, including their name, phone number, email, street address, date of birth, etc.

***Integrity.***
The modification functionality could allow unauthorized changes to appointment details.

***Availability.***
The cancellation functionality could allow an unauthorized party to cancel another citizen’s appointment.

For a police-related service, this could have real-world consequences for people attending appointments concerning theft, fraud, property damage, insurance claims, evidence collection, and other time-sensitive matters.

### Recommended Fix.

The appointment code should **not be the sole authorization mechanism**.

The application should:

1. Require ownership verification through the email associated with the appointment.
2. Use high-entropy, unpredictable appointment tokens without static prefixes.
3. Implement strong server-side rate limiting and lockouts.
4. Use short-lived, signed or single-use authorization tokens for sensitive actions.
5. Avoid returning sensitive PII unless the requester has been properly authenticated and authorized.
6. Monitor repeated failed appointment-code attempts for enumeration activity.

### Final Takeaway.

This finding was eventually marked as a **duplicate**, with a ***CVSS:3.1AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H 9.8(Critical)*** but it highlighted an important security principle:

***Knowing an object’s identifier should never automatically grant access to its data or control over it.***

The core issue wasn’t just the weak appointment code. It was the combination of **predictable identification, unauthorized PII disclosure, and missing authorization controls**.

That combination makes Broken Access Control particularly dangerous when the underlying records contain sensitive personal information and control real-world services.

I hope you enjoyed the write-up and learned something useful from it. Thanks for reading, and I’ll see you in the next one. Until then, stay blessed! 🙏🌾

[https://x.com/ethical\_h4ck3r\_](https://x.com/ethical_h4ck3r_)

[Critical BAC: IDOR + Weak Appointment Code Enables Unauthorized Appointment Cancellation…](https://infosecwriteups.com/critical-bac-idor-weak-appointment-code-enables-unauthorized-appointment-cancellation-5e145ced50ca) was originally published in [InfoSec Write-ups](https://infosecwriteups.com) on Medium, where people are continuing the conversation by highlighting and responding to this story.
