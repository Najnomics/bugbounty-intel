# Apple Auth Bypass

- **Source URL:** https://masimshahzad.medium.com/apple-auth-bypass-one-default-password-for-every-user-b6767b7edfa8
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/15000 (id 15000)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Sam Curry’s team found an Apple educator forum where every applicant shared one hidden password, then reached the admin console

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

Apple users signed in with their Apple ID, yet the forum quietly gave every applicant the same password. That single design choice turned into an Apple auth bypass on the Apple Distinguished Educators site, found in 2020 by Sam Curry’s five-person team. Chained with a path trick into the admin console, it led to code execution on the server.

***Disclaimer:*** *Educational and defensive use only. Apple fixed and retested these issues in 2020. Values, requests and reproduction steps are intentionally omitted.*

### Vulnerability Overview

- **Type:** Authentication bypass via a shared default credential on SSO-provisioned accounts, plus an authorization bypass on the admin path
- **CWE (analytical mapping):** CWE-1392 (Use of Default Credentials), CWE-288 (Authentication Bypass Using an Alternate Path), CWE-647 (Non-Canonical URL Paths for Authorization Decisions)
- **CVE:** None
- **Bounty:** Not stated per bug. By 8 October 2020 the team had received 32 Apple payments totalling $288,500 across their findings

### How the Apple Auth Bypass Happened (high level)

Apple Distinguished Educators was an invitation-only forum built on Jive, a product that normally uses usernames and passwords. Apple added custom middleware so people could sign in with their Apple account instead, and newcomers filled in an application for moderators to approve.

The application form carried a hidden password field. Its value was the same for every applicant, and it was stored against the new account. Nobody was meant to use it, because everyone was supposed to arrive through Apple sign-in.

But Jive’s own username-and-password login still existed. The team tried short usernames with the shared value and within minutes were logged in as an approved member. From the user list, they moved to administrator accounts.

The admin console seemed restricted, likely by network location. A variant of the admin path, with an extra character the access rule did not recognise but the application still routed, got them in. After trying a few admin accounts they reached the core administrator, whose built-in features allow code execution.

### Business Impact

The team reported they could have run commands on the ade.apple.com server, reached the internal LDAP service that manages user accounts, and reached most of Apple’s internal network. One forgotten login path turned a community site into a foothold.

This was one of 55 findings (11 rated critical by the team) between July and October 2020. Apple usually fixed issues within one to two business days, some in hours.

### Fixing Apple-Style Default Password Flaws (my own analysis)

**1. SSO accounts get no password.** Store none, so no shared secret can exist.

**2. Close the alternate door.** Disable local login for federated users, and rate-limit what remains.

**3. Authorize the canonical path.** Normalise once, then check and route that same path.

\# Pseudocode: SSO-only accounts have no password; admin checks use the routed path

def provision\_from\_sso(profile):

return users.create(username=profile.username, email=profile.email,

password\_hash=None, auth\_source="sso") # ignore any form password

def password\_login(username, password, ip):

if not limiter.allow(("login", ip, username)):

return deny("rate\_limited")

u = users.get(username)

if u is None or u.auth\_source != "local" or u.password\_hash is None:

verify\_dummy\_hash(password) # same timing for every refusal

return deny()

return allow(u) if verify\_hash(password, u.password\_hash) else deny()

def handle(request, user):

path = canonicalize(request.raw\_path) # strip ;params, decode once, resolve dots

if path.startswith("/admin") and not (user and user.is\_admin and admin\_network(request)):

return deny()

return router.dispatch(path, request) # dispatch exactly what was checked

# Test: admin path variants with ;params or encoding -> denied for every non-admin

### Key Takeaways

- A password nobody is supposed to know is still a password. If it is shared, it is public.
- Bolting SSO onto a product does not remove the product’s original login; it just hides it.
- Path-based access rules must see the same path the router sees.

### Credit & Sources

Found by **Sam Curry, Brett Buerhaus, Ben Sadeghipour, Samuel Erb and Tanner Barnes**. Primary source: [We Hacked Apple for 3 Months: Here’s What We Found](https://samcurry.net/hacking-apple), 7 October 2020, published with Apple’s permission. Corroboration: [Ars Technica](https://arstechnica.com/information-technology/2020/10/white-hat-hackers-who-had-control-of-internal-apple-network-get-288000-reward/) and [The Register](https://www.theregister.com/security/2020/10/10/five-bag-300000-in-bug-bounties-after-finding-55-security-holes-in-apples-web-apps-it-infrastructure/1517534). Facts come from those sources; analysis and code are original.

Next breakdown: the header that knocked GitHub repos offline for logged-out visitors. Follow @masimshahzad for daily bug bounty breakdowns.
