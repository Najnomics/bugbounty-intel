# Stripe Auth Bypass

- **Source URL:** https://masimshahzad.medium.com/stripe-auth-bypass-lockout-screen-case-study-09a82a954377
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-18
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14987 (id 14987)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Stripe Auth Bypass: The Lockout Screen That Wasn’t

### A 2017 bug bounty report shows why a re-authentication wall drawn in the browser is not a security control

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

A locked screen still let someone add a new admin. In 2017, Jon Bottarini reported a [Stripe auth bypass](https://www.jonbottarini.com/2017/04/03/inspect-element-leads-to-stripe-account-lockout-authentication-bypass/) where a dashboard that had timed out and demanded a password still accepted a request to invite an administrator. Stripe confirmed a back-end check had been accidentally removed for that action, fixed it shortly after the report, and paid $500.

***Disclaimer:*** *Educational and defensive use only. This was fixed in 2017. Reproduction details are intentionally omitted.*

### Vulnerability Overview

- **Type:** Authentication bypass: re-authentication requirement enforced in the UI but missing on the server for one sensitive action
- **CWE (analytical mapping, not from the source):** CWE-602 (Client-Side Enforcement of Server-Side Security), CWE-306 (Missing Authentication for Critical Function)
- **CVE:** Not reported
- **Severity/CVSS:** Not reported. Bounty: $500, source-reported

### How the Stripe Auth Bypass Worked (high level)

Stripe’s dashboard locks after a period of inactivity. The session cookie still exists, but the user must re-enter their password before doing anything. That design protects an unattended, logged-in laptop.

The lockout was visible as an overlay with disabled controls. The researcher noticed that “disabled” was largely a presentation choice: by changing the page in the browser’s developer tools, he could reach parts of the dashboard behind the overlay. Most actions were still refused by the server. Inviting a new team member was not.

Stripe later explained that its back end normally enforces the re-authentication check and that this one action had lost it by accident. The UI looked locked, and for nearly everything the server agreed. One gap was enough.

### Impact

The precondition is physical or local access to a browser where the victim had been signed in, so this is not a remote attack. Within that scope it is serious: inviting yourself as an administrator turns a few unattended minutes into durable access to a payments account that survives the victim logging out. The researcher noted that webhook changes were blocked, which shows the control existed but was applied unevenly.

### Fixing Stripe-Style Auth Bypass Server-Side (my own analysis)

**1. Treat the UI as a hint, never the gate.** Hidden, greyed-out and disabled controls are convenience. The server must reject the request on its own.

**2. Enforce re-auth as default-deny middleware.** Mark sensitive routes in one place and fail closed, so a new or refactored endpoint cannot silently skip the check.

**3. Test the negative path.** Add automated tests proving every privileged action fails while a session is locked or stale.

**4. Watch privilege changes.** Notify existing owners when an admin is invited and require the invitee to verify.

\# Pseudocode: fail-closed re-authentication for sensitive actions

SENSITIVE = {"team.invite", "team.role\_change", "payout.update",

"webhook.update", "api\_key.create"}

def handle(request, action):

s = sessions.get(request.session\_id)

if s is None:

raise Unauthorized()

if s.idle\_seconds() > IDLE\_LIMIT:

s.mark\_locked()

if action in SENSITIVE or s.is\_locked():

if not s.recent\_reauth(within\_seconds=300):

raise ReauthRequired() # enforced here, not in the UI

return dispatch(action, request, s)

# CI test: every sensitive action must fail on a locked session

def test\_locked\_session\_blocks\_sensitive\_actions():

for action in SENSITIVE:

assert call(action, session=locked\_session()).status == 401

### Key Takeaways

- If the server does not enforce it, it is not a control; it is decoration.
- Centralized, deny-by-default checks survive refactors better than per-endpoint code.
- Low bounties can still teach high-value lessons about uneven enforcement.

### Credit & Sources

Research by **Jon Bottarini**: [Inspect Element leads to Stripe Account Lockout Authentication Bypass](https://www.jonbottarini.com/2017/04/03/inspect-element-leads-to-stripe-account-lockout-authentication-bypass/) (3 April 2017, published with Stripe’s permission). Facts come from that source; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
