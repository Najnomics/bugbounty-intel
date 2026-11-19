# Starbucks Path Traversal

- **Source URL:** https://masimshahzad.medium.com/starbucks-path-traversal-nearly-100m-customer-records-d64e803acab8
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14989 (id 14989)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How one user-controlled path segment in a backend-for-frontend proxy reached an internal search service, for a $4,000 bounty

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

One path segment the browser was allowed to set turned a gift-card checkout into a view of nearly 100 million customer accounts. In 2020, Sam Curry reported a [Starbucks path traversal](https://samcurry.net/hacking-starbucks) where a proxy API forwarded user input into an internal host, exposing names, emails, phone numbers and addresses. Starbucks patched it the next day and paid $4,000.

***Disclaimer:*** *Educational and defensive use only. This was fixed in 2020. Reproduction details are intentionally omitted.*

### Vulnerability Overview

- **Type:** Path traversal in a server-side proxy (“secondary context” request), leading to broken access control on an internal API and mass data exposure
- **CWE (analytical mapping, not from the source):** CWE-22 (Path Traversal), CWE-441 (Unintended Proxy or Intermediary), CWE-284 (Improper Access Control)
- **CVE:** Not reported
- **Severity/CVSS:** Not reported. Bounty: $4,000, source-reported

### How the Starbucks Path Traversal Worked (high level)

The Starbucks web app used a “backend for frontend” layer: browser calls hit a proxy on the public host, which fetched the real data from an internal service the browser never talks to directly.

Most proxied calls were fixed routes. The interesting one took an item ID from the URL and dropped it into the internal request path. That is the whole bug class: if user input becomes part of a path on a second, hidden server, traversal sequences start walking that server’s directory tree instead of the public one.

A WAF blocked the obvious pattern, but a backslash-based variant slipped past. Error codes did the mapping: the JSON “not found” style proved requests were reaching the internal API, and a switch to “bad request” marked its root. From there, Curry and Justin Gardner enumerated top-level services. One was a search API over production accounts and addresses, which the researcher identifies as a Microsoft Graph instance. A count query returned nearly 100 million records, and filter parameters could target a single user.

### Impact

Anyone with a browser could have pulled names, emails, phone numbers and addresses for close to 100 million customers, with no special account. The researchers also listed internal services for loyalty, cards, rewards and billing that they did not test. Data at this scale is phishing and fraud fuel.

### Preventing Starbucks-Style Proxy Path Traversal (my own analysis)

**1. Never build internal paths from raw input.** Validate IDs against a strict format, then URL-encode them as a single segment.

**2. Normalise, then allow-list.** Resolve the final internal path and reject anything outside the route you meant to call.

**3. Give the proxy a narrow identity.** Internal services should enforce per-user authorisation, not trust “came from the BFF”.

**4. Don’t lean on the WAF.** Traversal has too many encodings.

\# Pseudocode: safe internal routing from a BFF proxy

import re

from urllib.parse import quote

```
ITEM_ID = re.compile(r"^[A-Za-z0-9-]{8,64}$")
ALLOWED_PREFIX = "/stream/v1/users/{uid}/items/"
```
def proxy\_get\_item(session, item\_id):

if not ITEM\_ID.fullmatch(item\_id): # rejects dots, slashes, backslashes

return Fail(400)

prefix = ALLOWED\_PREFIX.format(uid=session.user\_id)

path = prefix + quote(item\_id, safe="") # one encoded segment, never a path

if not normalise(path).startswith(prefix): # defence in depth

return Fail(400)

# Internal service re-checks that the item belongs to session.user\_id

return internal.get(path, on\_behalf\_of=session.user\_id)

\# Test: IDs containing ../, ..\, %2e%2e or %5c must return 400 and never reach internal.get

### Key Takeaways

- A proxy that forwards user input is a second attack surface; test the hidden server, not just the visible one.
- Different error shapes leak where your request landed, which makes internal mapping easy.
- Internal APIs need authorisation too. “Only the BFF can reach it” fails the first time the BFF can be steered.

### Credit & Sources

Research by **Sam Curry**, with Justin Gardner and Noah Pearson credited: [Hacking Starbucks and Accessing Nearly 100 Million Customer Records](https://samcurry.net/hacking-starbucks) (June 2020). Facts come from that source; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
