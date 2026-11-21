# Google 2FA Bug

- **Source URL:** https://masimshahzad.medium.com/google-2fa-bug-the-login-that-outlived-the-password-54b41453325f
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14994 (id 14994)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

You change your password, sessions are wiped, and the attacker is out. Researcher Luke Berner found a Google 2FA bug where that was not true: a login parked on Google’s second-factor page stayed valid after the password changed, and still accepted a code after 2FA was switched off. Google confirmed the logic flaw, fixed it and paid a bounty.

***Disclaimer:*** *Educational and defensive use only. Google fixed this before the January 2019 write-up. Reproduction details are intentionally omitted.*

### Vulnerability Overview

- **Type:** Authentication logic flaw: a pending (password-verified, second-factor-pending) login state was not invalidated by password changes or 2FA changes, and its timeout could be renewed
- **CWE (analytical mapping, not from the source):** CWE-613 (Insufficient Session Expiration), CWE-287 (Improper Authentication)
- **CVE:** None (hosted service)
- **Severity/Bounty:** Not published. The researcher says Google awarded a bounty but does not state the amount

### How the Google 2FA Bug Worked (high level)

A modern login is a two-step state machine. Step one checks the password and creates a “pending” login. Step two checks the second factor and turns it into a real session.

Berner’s insight: 2FA was often added to login flows years later, by different teams. So what happens to the pending state when the account changes underneath it?

At Google, the answer was “nothing”. Changing the password terminated full sessions but not the pending one. Google said pending logins expired after about 20 minutes; Berner found that switching verification methods renewed that timer. He also found the second-factor page still accepted a valid code after 2FA had been turned off.

The realistic scenario: an attacker with a stolen password enables 2FA on the account, parks a login on the code page, then disables 2FA to stay quiet. The victim resets the password and feels safe. The parked login still completes.

### Business Impact

Password reset is the standard response to a compromised account; this bug made it a false recovery. Berner reports the same pattern at Microsoft login (closed as intended) and Instagram (called theoretical), while Cloudflare and Algolia fixed it.

### Fixing 2FA Login Bugs Like Google’s (my own analysis)

**1. Bind pending logins to the credential version.** Store a password epoch and 2FA config version with the pending state; any mismatch kills it.

**2. Use an absolute deadline.** Switching methods may refresh the UI, never the expiry.

**3. Re-check policy at the final step.** If the factor was removed, the old challenge is void.

\# Pseudocode: second step of login re-validates the account state

PENDING\_MAX\_AGE = 10 \* 60 # seconds, absolute, never extended

def complete\_second\_factor(pending\_id, code):

p = pending\_store.get(pending\_id)

if p is None or now() - p.created\_at > PENDING\_MAX\_AGE:

return fail()

user = load\_user(p.user\_id)

if (p.password\_epoch != user.password\_epoch # password changed since step 1

or p.mfa\_version != user.mfa\_version # 2FA enabled/disabled/rotated

or not user.mfa\_enabled):

pending\_store.delete(pending\_id)

return fail()

if not verify\_factor(user, code):

return fail()

pending\_store.delete(pending\_id) # single use

return create\_session(user)

# Test: start login, change password, submit valid code -> fail

### Key Takeaways

- Every intermediate auth state is a session. Inventory and revoke it.
- Timers that reset on user actions are not timeouts.
- Change account settings mid-flow in your tests.

### Credit & Sources

Research by **Luke Berner**: [How I abused 2FA to maintain persistence after a password change](https://medium.com/@lukeberner/how-i-abused-2fa-to-maintain-persistence-after-a-password-change-google-microsoft-instagram-7e3f455b71a1) (January 2019). Discovered via the [Awesome-Bugbounty-Writeups](https://github.com/devanshbatham/Awesome-Bugbounty-Writeups) index. Facts come from the researcher’s write-up; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
