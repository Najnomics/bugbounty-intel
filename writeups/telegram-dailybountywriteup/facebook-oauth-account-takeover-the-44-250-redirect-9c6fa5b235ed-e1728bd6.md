# Facebook OAuth Account Takeover

- **Source URL:** https://masimshahzad.medium.com/facebook-oauth-account-takeover-the-44-250-redirect-9c6fa5b235ed
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14989 (id 14989)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How a trusted Oculus login endpoint stopped guarding its redirects after a migration and let a first-party access token walk out the door

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

A login endpoint Facebook trusted was quietly rebuilt, and the token-leak protection it used to have did not survive the move. In 2022, Youssef Sammouda showed a [Facebook OAuth account takeover](https://ysamm.com/uncategorized/2023/01/29/account-takeover-of-facebook-oculus-accounts-due-to-first-party-access_token-stealing.html) where the Oculus app’s first-party access token could be steered through a redirect chain to an attacker. Meta fixed it in September 2022 and paid $44,250, including bonuses.

***Disclaimer:*** *Educational and defensive use only. This was fixed in 2022. Reproduction details are intentionally omitted.*

### Vulnerability Overview

- **Type:** OAuth access token theft via an allowed redirect URI that forwarded to attacker-influenced destinations (redirect chain plus open redirect), leading to account takeover
- **CWE (analytical mapping, not from the source):** CWE-601 (Open Redirect), CWE-522 (Insufficiently Protected Credentials), CWE-352 (CSRF, for the login-CSRF setup step)
- **CVE:** Not reported
- **Severity/CVSS:** Not reported. Bounty: $44,250 including BountyCon bonuses and a Highest Impact Report bonus, source-reported

### How the Facebook OAuth Account Takeover Worked (high level)

Oculus users could log in with Facebook. Facebook’s OAuth configuration for the Oculus app listed an Oculus login endpoint as a valid redirect URI, so Facebook would hand tokens to it.

Then Oculus moved login to Meta accounts. The endpoint now bounced users through the Meta login service and back, and finally forwarded them to a “next” URL taken from its own query string, which could be any Oculus subdomain.

The old version did that final hop in JavaScript, which kept the token from following. The new one redirected directly. With the implicit flow, the token sits in the URL fragment, and browsers carry fragments across redirects. So the token rode every hop.

The last link: an Oculus subdomain that forwarded to a third-party service with an open redirect, so the token landed on a page the researcher controlled. Setup needed the victim logged in to Facebook, plus a login CSRF to place them in the right Meta state. The researcher notes the open redirect was not fully disclosed because it was still not completely fixed.

### Impact

A first-party token is not a limited third-party grant. It belongs to an app Facebook treats as its own, and the researcher states it could be used to access the victim’s Facebook and Oculus accounts. The victim only had to be logged in to Facebook and land on the attacker’s flow; the five-figure bounty reflects how little else was required.

### Preventing Facebook-Style OAuth Token Theft (my own analysis)

**1. Register exact redirect URIs.** Never an endpoint that forwards to a caller-supplied URL.

**2. Use code flow with PKCE.** Fragment tokens follow redirects; codes bound to a verifier are useless when stolen.

**3. Re-review OAuth trust after migrations.** A login rewrite changes what an allowed URI does.

**4. Restrict post-login “next” targets.** Allow-list paths, and clear the fragment on every onward hop.

\# Pseudocode: post-login redirect that never forwards credentials

from urllib.parse import urlsplit

SAFE\_NEXT\_PATHS = {"/", "/account", "/store"} # same-origin paths only

def finish\_login(request, session):

session.establish\_from(request) # consume code server-side

nxt = request.query.get("next", "/")

parts = urlsplit(nxt)

if parts.scheme or parts.netloc or parts.path not in SAFE\_NEXT\_PATHS:

nxt = "/" # no cross-host or subdomain hops

# Browsers keep the old #fragment on redirects unless Location sets one,

# so end with an explicit empty fragment to drop any token.

return Redirect(urlsplit(nxt).path + "#", headers={"Referrer-Policy": "no-referrer"})

# Test: next=https://any.sub.example/... must land on "/" with no token in URL or Referer

### Key Takeaways

- An allowed redirect URI is only as safe as every redirect it can trigger.
- Migrations silently remove defences; re-test token flows after any login rebuild.
- Implicit-flow tokens in fragments are a liability; move first-party apps to code flow with PKCE.

### Credit & Sources

Research by **Youssef Sammouda (sam0)**: [Account takeover of Facebook/Oculus accounts due to First-Party access\_token stealing](https://ysamm.com/uncategorized/2023/01/29/account-takeover-of-facebook-oculus-accounts-due-to-first-party-access_token-stealing.html) (published January 2023). Facts come from that source; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
