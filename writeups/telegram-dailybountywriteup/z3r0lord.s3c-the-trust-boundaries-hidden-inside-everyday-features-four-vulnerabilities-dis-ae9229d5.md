# The Trust Boundaries Hidden Inside Everyday Features

- **Source URL:** https://medium.com/@z3r0lord.s3c/the-trust-boundaries-hidden-inside-everyday-features-four-vulnerabilities-discovered-through-a19083572c5e
- **Fetched from:** https://medium.com/@z3r0lord.s3c/the-trust-boundaries-hidden-inside-everyday-features-four-vulnerabilities-discovered-through-a19083572c5e?source=rss-ade2a1eb2fd8------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14897 (id 14897)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** z3r0lord / Fri, 04 Sep 2026 04:09:33 GMT

**z3r0lord** | Security Researcher

Most security bugs don’t begin with exotic payloads, race conditions, or zero-days. They begin with a feature behaving exactly as designed right up until one small, almost boring observation reveals that some assumption baked into the stack was quietly wrong the entire time. Nobody throws a party for the bug that turns out to be interesting. The good ones are usually embarrassingly simple, which is exactly why nobody caught them first.

A rate limiter assumes its counters are scoped correctly. An AI assistant assumes a URL provided in a chat message is safe to fetch. An authentication layer assumes only trusted clients can send certain headers. A support chatbot assumes its system prompt is enough to enforce policy.

Every one of those assumptions sounds perfectly reasonable in a design review. Every one of them also turned out to be a load-bearing wall made entirely of good intentions.

Over the course of a single research season, I filed four vulnerability reports three against [**HackerSavanna’s own platform**](https://www.hackersavanna.com/), one against a private program triaged through [**HackerSavanna’s**](https://www.hackersavanna.com/) disclosure ecosystem. Different targets, different bug classes, wildly different severities. But peel back the technical detail on any of them and you find the same small crack underneath: a trust boundary nobody was actually enforcing, just quietly assuming someone else already had.

That’s the part that should be a little terrifying, and honestly a little exciting, for anyone thinking about getting into this. You don’t need a zero-day. You don’t need a research lab. You need to be the one person willing to send the request twice once the normal way, once with a single thing changed and actually read what comes back instead of assuming it matches what you expected. Most people skim past the small stuff.

And at every step, HackerSavanna made that worth doing: real triage from people who read what you send them, communication instead of a support-ticket black hole, and remediation that actually shipped instead of sitting in a backlog forever. Three of these four findings ended up publicly disclosed through [SavannaHub .](https://www.hackersavanna.com/)

If you’ve been sitting on the sidelines wondering whether bug hunting is “for other people” it isn’t. It’s for whoever notices the small thing. Go find yours.

The findings below are presented in the order they were discovered……………..

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

**Target:** Private program (redacted as “wantam”) **Reward:** KSh 8,000 (Report #63)

This finding began with an ordinary authentication test. An unauthenticated request correctly returned 401 Unauthorized. Adding a single custom header changed everything:

X-Wantam-Platform: wantam

No token. No cookie. No session. The response suddenly contained a fully authenticated user context. Further testing confirmed this wasn’t limited to informational endpoints state-changing functionality that should have required authentication accepted requests solely because the header was present.

The bypass alone was serious. What made the finding significantly more impactful was what that access exposed next.

One accessible endpoint triggered internal scanning operations. Because the scanner executed requests from within the platform’s own environment, it effectively became an SSRF primitive. Initial testing showed obvious inputs like 127.0.0.1 were correctly blocked but alternative representations were never normalized before validation. The hex-encoded equivalent, 0x7f000001, bypassed the filter entirely. The resulting scan output resolved to localhost and returned backend-specific headers that were never observable through the public edge infrastructure confirming the request had genuinely reached the internal network.

Further testing showed cloud metadata endpoints and additional internal addresses were reachable through the same mechanism.

A separate, unrelated issue surfaced during the same assessment: newly registered users were automatically placed into the organization’s live operational tenant rather than an isolated one exposing internal source code within minutes of account creation.

**Root Cause**

**Security Impact**

**Remediation** The header-based bypass was removed, validation logic was moved to occur after resolution rather than on the raw string, and tenant assignment was corrected. The full chain was retested and confirmed fixed.

**Target:** HackerSavanna AI Assistant **Reference:** Publicly disclosed via SavannaHub r/REF:[https://www.hackersavanna.com/savannahub/66](https://www.hackersavanna.com/savannahub/66)

Rate limiting is one of the most common defensive controls on modern applications. Done correctly, it prevents abuse while preserving availability for legitimate users. The AI Assistant implemented such a control but the limit wasn’t scoped to the user.

After sending several normal messages in quick succession, the assistant began returning a generic error instead of a response. Alongside the error was an internal throttling identifier an implementation detail that immediately raised questions about how the limiter was actually being tracked.

The critical observation came from testing a second account. A completely unrelated account, authenticated in a separate session with no prior interaction history, received the exact same error on its very first request. At that point the problem became clear: the limiter wasn’t tracking individual users. It was tracking the feature itself.

In practice, any researcher could exhaust the shared quota and temporarily deny access to every other researcher on the platform. To affected users, the behavior was indistinguishable from a backend outage making it harder to even recognize, let alone report.

**Remediation** HackerSavanna rescoped the limiter to key requests against the authenticated user rather than a shared counter. Verified fixed, then publicly disclosed.

Modern AI assistants frequently offer URL summarization. Under the hood, that means the application accepts untrusted user input and performs outbound requests on the user’s behalf a classic setting for trust boundaries to break down.

Testing began with a URL hosted under my own infrastructure. When the assistant was instructed to summarize the page, an out-of-band listener immediately recorded an inbound request originating from HackerSavanna’s environment, confirming server-side fetching was taking place.

The next step was straightforward: replace the external URL with an internal address. Instead of a summary, the application returned an unhandled server exception complete with stack traces, filesystem paths, and internal identifiers. Additional malformed payloads produced the same category of failure.

At first glance, this looked like SSRF. During triage, HackerSavanna’s team conducted a deeper review and determined that the infrastructure assumptions behind the original SSRF theory didn’t hold for their deployment a correction that turned out to matter. What remained consistently reproducible, and ultimately formed the final classification, was a prompt-driven denial-of-service condition capable of crashing the assistant’s rendering pipeline while exposing internal implementation details in the process.

**Remediation** Patched and publicly disclosed as a prompt-injection-driven DoS rather than the originally reported SSRF a useful reminder that accurate classification matters as much as finding the bug itself.

**Target:** HackerSavanna Support Assistant **Reference:** SavannaHub Disclosure #74

The support assistant explicitly advertised itself as limited to bug bounty hunting, report writing, platform guidance, and research onboarding. That restriction existed entirely inside the model’s instructions no server-side enforcement layer backed it.

After a short conversational detour and one deliberately vague follow-up, the assistant stopped applying the restriction entirely. Requests with no relation to bug bounty research were answered normally, with no acknowledgment they fell outside its stated purpose.

Unlike the previous three findings, this wasn’t a confidentiality or integrity issue the impact was operational. An assistant budgeted, tuned, and deployed for a specific function could be redirected into general-purpose use simply by steering the conversation off-topic.

**Remediation** Scope validation was moved into application logic rather than relying solely on model instructions. No longer reproducible after remediation.

Different systems, different technologies but all four failed for essentially the same reason. A security control existed. The application trusted that the control was being enforced. The enforcement lived in the wrong place.

The rate limiter trusted a global counter. The AI assistant trusted input it hadn’t validated. The authentication layer trusted a user-controlled header. The support assistant trusted a system prompt to behave like an access-control mechanism.

In every case, the feature worked exactly as intended until the assumption behind it was questioned. None of these required custom tooling or exploitation frameworks. Most began with nothing more than a browser, a proxy, and a single modified request.

One reason for documenting these together: they’re a reminder that impactful vulnerabilities are often found through curiosity rather than complexity. A second browser session. A modified header. A different URL representation. A vague follow-up question. Small changes reveal hidden assumptions, and hidden assumptions are where trust boundaries fail.

All four reports were triaged, remediated, and verified. Three were publicly disclosed through [**HackerSavanna’s SavannaHub**](https://www.hackersavanna.com/), turning them into case studies for the wider community rather than letting them quietly disappear behind a changelog entry. Credit to the HackerSavanna team for engaging constructively throughout, and for choosing transparency by publishing findings once they were fixed.

**The best bugs aren’t always buried deep inside code. Sometimes they’re hiding behind the features everyone uses every day.**
