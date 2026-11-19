# IDOR in Email Preference Management — Unauthenticated Access & Modification

- **Source URL:** https://medium.com/@dev_fr_/idor-in-email-preference-management-unauthenticated-access-modification-915a5f5c1fff?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260510203805/https://medium.com/@dev_fr_/idor-in-email-preference-management-unauthenticated-access-modification-915a5f5c1fff
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13521 (id 13521)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR in Email Preference Management — Unauthenticated Access & Modification

**Weakness**: Insecure Direct Object Reference (IDOR) 

**Severity**: Medium 

**Status**: Duplicate of a Triaged Report

### What Happened:

While testing a financial services platform, I found that the email preference system was protected by nothing more than a UUID token passed in the URL. No session. No authentication. Just a token.

Anyone who gets hold of a valid UUID can open that URL in a private browser and freely view or modify another user’s email preferences,including unsubscribing them from all communications.

### The Core Issue:

The platform assumes that knowing the UUID = being the owner. That’s the mistake.

UUIDs are designed for **unique identification**, not **authorization**. They never expire, they don’t invalidate after use, and they can leak through email forwarding, browser history, proxy logs, or even search engine indexing if the URLs aren’t properly blocked.

### Proof of Concept:

Open an incognito browser with no active session and visit:

https://\[REDACTED\]/email/preferences?token=a3f1c820-xxxx-xxxx-xxxx-1d9f6a2e8c47

The preferences page loads fully and all actions work — no login required.

To trigger an unsubscribe:

https://\[REDACTED\]/email/unsubscribe?token=a3f1c820-xxxx-xxxx-xxxx-1d9f6a2e8c47&type=email-marketing

Success message appears. Change is applied. Still no authentication.

### Impact:

An attacker can silently unsubscribe a target from all emails — including security alerts and account notifications — without the user ever knowing. It’s not account takeover, but suppressing security emails on a financial platform is a meaningful risk.

### Remediation:

\- Require an active authenticated session before allowing any preference changes.

- Replace permanent UUIDs with short-lived, signed tokens (HMAC or JWT with expiry).

- Block preference URLs from search engine indexing via \`robots.txt\` and \`X-Robots-Tag: noindex\`.

- Invalidate tokens after first use.

- Notify users via a separate channel when preferences are changed.

Reported: **November 2025** — Closed as duplicate of an earlier triaged submission.
