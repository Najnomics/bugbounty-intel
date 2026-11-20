# GitLab Account Takeover

- **Source URL:** https://masimshahzad.medium.com/gitlab-account-takeover-one-reset-email-two-inboxes-e553d8cdac3b
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-20
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14992 (id 14992)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How a $35,000 bug bounty report turned GitLab’s password reset form into a CVSS 10 account takeover by accepting a list where it expected one email

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

A password reset form asked for one email address and quietly accepted many. In December 2023, a researcher known as asterion04 reported a [GitLab account takeover](https://hackerone.com/reports/2293343) where the reset link for a victim’s account was also delivered to an inbox the attacker controlled. GitLab rated it Critical (CVSS 10.0), assigned CVE-2023–7028 and paid a $35,000 bounty.

***Disclaimer:*** *Educational and defensive use only. This was fixed in January 2024. Reproduction details are intentionally omitted.*

### Vulnerability Overview

- **Type:** Password reset poisoning through parameter type confusion (array accepted where a single email was expected), leading to account takeover
- **CWE (analytical mapping, not from the source):** CWE-640 (Weak Password Recovery Mechanism), CWE-20 (Improper Input Validation)
- **CVE:** CVE-2023–7028
- **Severity/CVSS:** Critical, CVSS 3.1 base score 10.0 (GitLab advisory). Bounty: $35,000 (HackerOne report)

### How the GitLab Account Takeover Worked (high level)

In GitLab 16.1, released in May 2023, a change let users reset their password through a secondary email address. GitLab’s advisory says the bug sat in the email verification step of that new path.

The reset endpoint took the email from the request body. The researcher found it would also accept that field as a list. Submit the victim’s address alongside one more, and GitLab matched the victim’s account but mailed the reset link to every address in the list, including the unverified one.

No click from the victim, no phishing, no prior access. Knowing an account’s email was enough. By the 11 January 2024 advisory GitLab.com was already patched, and self-managed versions 16.1 through 16.7 got backported fixes.

### Impact

Anyone could take over any GitLab account whose email they knew, including administrators of self-managed instances, which hold source code, CI secrets and deploy keys. GitLab notes one real limit: with two-factor authentication enabled, the password could still be reset, but the attacker could not log in. It reported no detected abuse on GitLab-managed platforms.

### Fixing GitLab-Style Password Reset Bugs (my own analysis)

**1. Pin parameter types.** If a field is one email, reject anything that is not exactly one string, before any lookup.

**2. Send only to addresses the server already trusts.** The recipient comes from the account record, never from the request.

**3. Test the shape, not just the value.** Arrays, nested objects and duplicate keys belong in every auth test suite.

**4. Treat reset as a login.** Require 2FA after a reset and alert the user on every reset request.

\# Pseudocode: password reset that never mails a caller-chosen address

def request\_reset(params):

email = params.get("email")

if not isinstance(email, str): # list, dict, None -> reject

return generic\_ok() # same response either way

user = find\_user\_by\_verified\_email(email.strip().lower())

if user is None:

return generic\_ok()

token = issue\_reset\_token(user) # single use, short expiry

send\_reset\_mail(user.email\_matching(email), token) # stored, verified address only

return generic\_ok()

\# Test: email=\["victim@x", "other@y"\] must send zero mails to other@y

### Key Takeaways

- A reset flow is only as safe as the place it takes the recipient from.
- Frameworks happily parse arrays; validate type before meaning.
- New convenience paths (secondary emails) need the same security review as the original flow.

### Credit & Sources

Research by **asterion04**: [HackerOne report #2293343](https://hackerone.com/reports/2293343) (disclosed February 2025) and the [GitLab critical security release advisory](https://about.gitlab.com/releases/2024/01/11/critical-security-release-gitlab-16-7-2-released/) (January 2024). Facts come from those sources; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
