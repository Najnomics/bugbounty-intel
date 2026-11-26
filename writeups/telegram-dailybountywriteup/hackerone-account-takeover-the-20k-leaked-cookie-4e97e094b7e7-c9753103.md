# HackerOne Account Takeover: The $20K Leaked Cookie

- **Source URL:** https://masimshahzad.medium.com/hackerone-account-takeover-the-20k-leaked-cookie-4e97e094b7e7
- **Fetched:** 2026-11-26
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14999)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Muhammad Asim Shahzad / Wed, 25 Nov 2026 05:06:33 GMT

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

No exploit, no phishing, no brute force: the bug bounty platform handed over the key itself. In November 2019, hacker haxta4ok00 reported a HackerOne account takeover after a HackerOne security analyst accidentally posted a valid session cookie in a report thread. The cookie worked from anywhere, exposing customer reports. HackerOne revoked it and paid $20,000.

***Disclaimer:*** *Educational and defensive use only. This was fixed in 2019. Reproduction details are intentionally omitted.*

HackerOne triages reports to its own bug bounty program. An analyst could not reproduce a submission and replied with the steps they had tried, including part of a cURL command copied from the browser console. That snippet still carried their session cookie.

The analyst had signed in through multi-factor single sign-on, but the cookie was the product of that login. Whoever held it skipped SSO and MFA entirely.

HackerOne’s own analysis is candid: sessions were not tied to where they were created. That was a known, accepted risk, because many users work over mobile networks and proxies. Twenty minutes after the cookie appeared, the hacker reported that it worked.

The session reached reports from the programs that analyst supported, including a pre-screening inbox, so vulnerability details from multiple customers were exposed. Affected customers were notified.

The report arrived on a Sunday, when Slack alerts were unreliable. It took two hours to triage, and the cookie was revoked three minutes after triage began. HackerOne’s minimum for high severity was $7,500; it chose to treat the case as critical given the data at risk.

**1. Catch secrets before they post.** HackerOne added detection and redaction of tokens in comments.

**2. Bind privileged sessions.** Short term, HackerOne pinned staff sessions to the sign-in IP; longer term, device binding.

**3. Shrink the blast radius.** Least-privilege analyst access, and page someone for critical reports.

\# Pseudocode: block secrets in comments, and reject replayed staff sessions

SECRET\_PATTERNS = \[COOKIE\_HEADER, BEARER\_TOKEN, CLOUD\_ACCESS\_KEY\]

def submit\_comment(author, report, text, confirmed=False):

hits = \[p.name for p in SECRET\_PATTERNS if p.search(text)\]

if hits and not confirmed:

return ask\_to\_redact(hits, preview=redact(text)) # nothing is stored yet

return comments.save(report.id, author.id, text)

def load\_session(cookie, request):

s = sessions.get(cookie)

if s is None or s.expired():

return anonymous()

if s.privileged and not device\_proof\_valid(request, s.device\_key\_id):

sessions.revoke(s.id) # revoke first, then alert

alert("staff\_session\_replay", s.user\_id, request.ip)

return anonymous()

return s

# Test: replay a staff cookie from a second browser -> session revoked, alert fired

Reported by **haxta4ok00** (HackerOne). Primary source: [HackerOne report #745324, Account takeover via leaked session cookie](https://hackerone.com/reports/745324), disclosed 3 December 2019, including HackerOne’s incident report: timeline, root cause, data exposure, preventive measures, severity and $20,000 bounty. Facts come from that source; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
