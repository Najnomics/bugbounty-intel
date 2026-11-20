# 🐛 Bug Bounty Writeup

- **Source URL:** https://masimshahzad.medium.com/slack-http-request-smuggling-stealing-session-cookies-c88efca5294c
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-20
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14992 (id 14992)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How one space character in a header let two servers disagree about where a request ended, and turned that into Slack account takeover

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

Two servers read the same request and disagreed about where it ended. In November 2019, Evan Custodio (defparam) reported [Slack HTTP request smuggling](https://hackerone.com/reports/737140) on a Slack asset that let him hijack other customers’ requests in flight and collect their session cookies. Slack reproduced it, shipped a fix and paid a bounty within 24 hours.

***Disclaimer:*** *Educational and defensive use only. This was fixed in 2019. Reproduction details are intentionally omitted.*

### Vulnerability Overview

- **Type:** HTTP request smuggling (CL.TE desync) chained with a backend redirect that carried session cookies, leading to session hijacking
- **CWE (analytical mapping, not from the source):** CWE-444 (Inconsistent Interpretation of HTTP Requests), CWE-601 (Open Redirect)
- **CVE:** Not reported
- **Severity/CVSS:** HackerOne severity: Critical; no CVSS score published. Bounty amount: not publicly listed on the report

### How the Slack HTTP Request Smuggling Worked (high level)

A request body’s length can be declared two ways: Content-Length, or chunked Transfer-Encoding. When both appear, the standard says Transfer-Encoding wins.

The researcher found a malformed Transfer-Encoding header, with a stray space before the colon, that the front-end server ignored and the back-end server honoured. The front end measured the request by Content-Length; the back end read it as chunked. The leftover bytes stayed on the shared back-end connection and were glued to the front of the next customer’s request.

That prefix rewrote the victim’s request into one that made the back end answer with a redirect to an external host. The victim’s browser followed it, and Slack’s session cookie travelled with the request into a server the researcher controlled. Every request on that poisoned connection was a potential victim, chosen by timing, not by targeting.

### Impact

A stolen Slack session cookie is a logged-in session: messages, files and channels of whatever workspace the victim belonged to. The researcher argued an attacker could automate this into mass account takeover. Slack paused public disclosure until its investigation concluded, and a redacted summary was disclosed in March 2020.

### Preventing Slack-Style Request Smuggling (my own analysis)

**1. Reject ambiguity at the edge.** A request with both length headers, or a malformed header name, gets a 400 and a closed connection.

**2. Normalize, then forward.** The proxy should rebuild requests in canonical form, not pass raw header bytes through.

**3. Prefer HTTP/2 end to end** or don’t reuse back-end connections across users for sensitive hosts.

**4. Harden the second bug.** The researcher himself recommended reviewing back-end redirects: never build an absolute Location from the request line.

\# Pseudocode: edge filter that refuses to guess where a request ends

import re

HEADER\_NAME = re.compile(r"^\[!#$%&'\*+.^\_\`|\~0-9A-Za-z-\]+$") # RFC 9110 token

def check\_framing(raw\_headers):

names = \[n for n, \_ in raw\_headers\]

if any(not HEADER\_NAME.match(n) for n in names): # "Transfer-Encoding " fails

return reject(400, close=True)

lower = \[n.lower() for n in names\]

has\_te, has\_cl = "transfer-encoding" in lower, "content-length" in lower

if has\_te and has\_cl:

return reject(400, close=True) # never pick a winner

if has\_te and header(raw\_headers, "transfer-encoding").strip().lower() != "chunked":

return reject(400, close=True)

return forward\_canonical(raw\_headers) # re-serialized, not raw

### Key Takeaways

- Smuggling is a disagreement bug: test the front end and back end as a pair.
- Desync alone is noisy; the redirect gadget made it critical. Fix both.
- Fast triage matters: report to fix and bounty took under a day.

### Credit & Sources

Research by **Evan Custodio (defparam)**: [HackerOne report #737140, Slack](https://hackerone.com/reports/737140) (submitted November 2019, disclosed March 2020). Facts come from that source; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
