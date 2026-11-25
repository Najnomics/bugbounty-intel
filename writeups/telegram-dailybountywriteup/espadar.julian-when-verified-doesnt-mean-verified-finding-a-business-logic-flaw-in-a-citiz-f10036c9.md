# When Verified Doesn’t Mean Verified

- **Source URL:** https://medium.com/@espadar.julian/when-verified-doesnt-mean-verified-finding-a-business-logic-flaw-in-a-citizen-data-platform-fc91a3e12dfe
- **Fetched from:** https://medium.com/@espadar.julian/when-verified-doesnt-mean-verified-finding-a-business-logic-flaw-in-a-citizen-data-platform-fc91a3e12dfe?source=rss-8064117de3f2------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14901 (id 14901)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** julichaan / Mon, 07 Sep 2026 20:02:12 GMT

Most vulnerability research focuses on breaking authentication, bypassing authorization, or exploiting technical weaknesses such as SQL injection and XSS.

Sometimes, however, the most interesting findings emerge when an application behaves exactly as designed.

This was one of those cases.

During a security assessment of a public-facing platform, I discovered a business logic flaw that allowed authenticated users to create and store entirely fictitious identity-related information inside a trusted data repository used to pre-fill official forms and administrative procedures.

There was no privilege escalation.

No account takeover.

No access to another user’s data.

Yet the platform would happily accept fabricated information, mark it as owned by the user, and treat it as legitimate throughout the application workflow.

The platform maintained a collection of structured user records.

These records represented various categories of personal and organizational information, including:

The purpose of these records was convenience.

Instead of requiring users to repeatedly enter the same information, the platform stored it centrally and automatically used it to pre-fill future forms and requests.

At first glance, this seemed perfectly reasonable.

The problem appeared when I started examining how those records were created.

The application exposed a generic API endpoint responsible for creating and updating these records.

The request structure was surprisingly simple:

```
{
  "recordType": "<type identifier>",
  "content": {
    "...": "..."
  }
}
```
Different record types represented different categories of information.

For example:

What immediately caught my attention was that the API appeared to accept whatever values the client submitted.

There was no evidence of server-side verification.

No validation against authoritative sources.

No confirmation that the information actually existed.

To verify the behavior, I created several records containing entirely fictitious information.

The values were intentionally chosen to avoid matching real-world entities.

Examples included:

The goal was simple:

Could the system distinguish legitimate information from completely invented data?

The answer was no.

Every submission returned a successful response.

More interestingly, the API indicated that ownership validation had succeeded.

A simplified response looked like this:

```
{
  "id": "...",
  "content": {
    "...": "..."
  },
  "ownershipValid": true
}
```
The platform accepted the data without question.

At this point, one might argue that accepting user-provided information is normal.

Many applications allow users to store arbitrary profile data.

The more significant issue emerged after reloading the profile.

The fabricated records were no longer just temporary inputs.

They had become first-class records inside the platform.

The information appeared throughout the user interface exactly like legitimate records.

The system treated them as active profile data.

Some were automatically selected for form pre-filling workflows.

In other words, the platform was not merely storing user assertions.

It was operationalizing them.

Among all tested record types, vehicle information stood out.

The application allowed users to create records describing vehicles and mark them for future form usage.

The submitted values were never checked against any authoritative source.

As a result, entirely fictitious vehicles could become part of the user’s profile and be presented in future administrative workflows.

The issue wasn’t whether the platform would ultimately approve a request based on that information.

The issue was that the platform had already assigned a level of trust to data that had never been validated.

Once false information enters a trusted workflow, downstream systems and human operators may reasonably assume that some verification has already occurred.

The same behavior affected business-related data.

Users could create records describing:

Again, the platform performed no meaningful verification.

Any well-formed value appeared acceptable.

From a security perspective, this effectively transformed verified identity fields into self-asserted claims.

The distinction is important.

Identity data often exists specifically because it establishes eligibility, authority, or ownership.

If validation never occurs, those assurances disappear.

The vulnerability illustrates an important security principle:

Validation and authorization are not the same thing.

The platform correctly verified that users could modify their own records.

What it failed to verify was whether those records represented reality.

As a result, the system blurred the distinction between:

When those two categories become indistinguishable, trust begins to leak into downstream processes.

Caseworkers, partner systems, automated workflows, and other consumers of the data may assume a level of authenticity that does not actually exist.

Some vulnerabilities are easy to explain because they involve obvious technical failures.

This wasn’t one of them.

The API worked.

Authentication worked.

Authorization worked.

Input filtering worked.

The flaw existed because the platform implicitly trusted information that had never been validated.

Security is often thought of as preventing attackers from accessing data they shouldn’t have.

Equally important is preventing systems from trusting data they shouldn’t.

In this case, the most valuable lesson wasn’t about breaking access controls.

It was about understanding how easily trust can be manufactured when validation is missing.
