# Uber Account Takeover

- **Source URL:** https://masimshahzad.medium.com/uber-account-takeover-the-api-that-handed-out-tokens-c12f52fb14fe
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14994 (id 14994)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### A $6,500 bug bounty report: a leaked user ID plus one API call that trusted it gave up any Uber rider, driver or Eats session

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

Two harmless-looking API responses added up to an Uber account takeover. In April 2019, researcher Anand Prakash showed Uber that a phone number or email was enough to get a user’s internal ID, and that ID was enough to get their live mobile session token. Uber fixed it within a week of the report and paid a $6,500 bounty.

***Disclaimer:*** *Educational and defensive use only. This was fixed in April 2019. Reproduction details are intentionally omitted.*

### Vulnerability Overview

- **Type:** Insecure direct object reference (IDOR) plus identifier leak in error messages, chained into session token disclosure and account takeover
- **CWE (analytical mapping, not from the source):** CWE-639 (Authorization Bypass Through User-Controlled Key), CWE-209 (Error Message Containing Sensitive Information), CWE-200 (Exposure of Sensitive Information)
- **CVE:** None (hosted service)
- **Severity/Bounty:** Rated High on HackerOne report #542340. Bounty: $6,500 (researcher’s write-up; the amount is not shown on the public report)

### How the Uber Account Takeover Worked (high level)

**Step one was a leak.** A partner-side API for adding drivers accepted a phone number or email. When the lookup failed, the error message echoed back the internal user UUID tied to that contact detail.

**Step two was the IDOR.** A separate endpoint, built to render a consent screen, took a user UUID straight from the request body and returned that user’s profile. Uber’s own disclosure summary says the response also carried the user’s mobile auth token. Nothing compared the UUID in the request with the session making it.

Neither bug was critical alone. Together, the second converted the first into a credential.

### Business Impact

With a victim’s mobile token, the researcher reports he could view ride history, request rides and see payment details on test accounts. Location history, saved addresses and driver information were exposed as well. For a ride-hailing platform that is physical-safety data, and the only input needed was a contact detail.

### Fixing Uber-Style IDOR and Token Leaks (my own analysis)

**1. Derive identity from the session.** If an endpoint serves “the current user”, it must never read a user ID from the request.

**2. Never return credentials in data responses.** Tokens are issued by the auth service at login, never by a profile or UI helper.

**3. Make errors boring.** “Not found” should not include the ID of the thing that was found.

**4. Treat UUIDs as public.** Unguessable is not authorized.

\# Pseudocode: profile endpoint that cannot be pointed at someone else

PUBLIC\_FIELDS = {"first\_name", "role", "locale"} # explicit allowlist

def consent\_screen\_details(request):

session = require\_session(request) # 401 if missing or expired

asked = request.body.get("user\_uuid")

if asked is not None and asked != session.user\_uuid:

audit\_log("uuid\_mismatch", session.user\_uuid)

return error(403, "forbidden") # no profile data, no ID echo

user = load\_user(session.user\_uuid) # identity from session only

return {k: user\[k\] for k in PUBLIC\_FIELDS} # tokens never serialized

# Test: session A requesting user\_uuid B -> 403 and the body has no "token" key

### Key Takeaways

- Two “low” bugs that share an identifier are one critical bug.
- An error message is an API response; review it like one.

### Credit & Sources

Research by **Anand Prakash** (AppSecure): [his write-up of the Uber account takeover](https://www.anandpraka.sh/2026/10/uber-account-takeover-vulnerability-bug-bounty.html) and [HackerOne report #542340](https://hackerone.com/reports/542340) (reported April 2019, disclosed September 2019), first published by the researcher in September 2019 [on HackerNoon](https://hackernoon.com/how-i-could-have-hacked-all-uber-accounts-rtzl3z72). Facts come from those sources; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
