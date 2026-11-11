# @Assass1nmarcos — Aditya Sharma

- X: [https://x.com/Assass1nmarcos](https://x.com/Assass1nmarcos) (id `1021768127896477696`, account created 24 Jul 2018)
- Display name: Aditya sharma
- Bio (Nov 2026): Cyber security researcher; HoF claim for Google, Microsoft, Apple, Meta, Adobe, Oneplus
- Site: [adityasec.in](https://adityasec.in/) — also lists Intel, Sony, Dell, Mastercard, Philips, Nokia, AT&T, Okta, HubSpot among recognized disclosures; Senior Cyber Security Consultant at REOFT Technologies; GitHub `assassin-marcos`
- HackerOne: [assassin_marcos](https://hackerone.com/assassin_marcos?type=user) — 148 vulnerabilities found, 76 thanks, ~92nd rank / 1522 reputation, 10-month streak, joined Sep 2016 (profile fetched Nov 2026)
- Medium: [assassin-marcos.medium.com](https://assassin-marcos.medium.com/)
- Platforms: HackerOne (primary in 2026 posts), also Bugcrowd
- Focus: Web, API, cloud, VAPT / offensive security

**Caution on 2026 payout screenshots.** On 20 Oct 2026 15:25 WAT he posted a $6,421 HackerOne bounty and wrote "Yes these are edited and fake ;)". Treat that particular amount as a joke/edited image, not as a finding. Earlier October payout posts were not labeled fake in the post text; they remain unverified beyond the public claim.

## Findings with technical detail

### 1. Password-reset token returned in the API response (account takeover, no user interaction)

- **Title:** Misconfigured reset password leads to account takeover
- **Platform / program:** HackerOne public program (target not named; described as a well-known adult-entertainment platform). Domain was out of scope on the public program; he was invited to the private program after submitting.
- **Severity:** Critical (author's description)
- **Bounty:** $5,000 (publicly stated)
- **Bug class:** Account takeover / sensitive token disclosure in a password-reset API
- **Root cause:** A forgot-password flow used an AJAX/API call. The response to a reset request for a valid username included the reset token and username in JSON, so a third party could build the change-password URL without reading the victim's email.
- **How it was found:** Ordinary login/signup and the email-based reset looked normal (and there was a separate OAuth open redirect). He then viewed page source / XHR traffic, replayed the reset API, and noticed the token in the response. Found in about 5–10 minutes once on that page.
- **PoC:** Disclosed in the writeup; the full verbatim text is now stored in this repo under `posts/` (see the post file linked from this researcher index).
- **Takeaways:** Always inspect the **response body** of forgot-password and token-issuance endpoints, not just whether an email is sent. Tokens must not be echoed back to the requester. Adjacent auth pages (affiliates, older SPAs) are worth more than yet another login form.
- **Sources:** [Medium writeup](https://assassin-marcos.medium.com/5k-misconfigured-reset-password-that-leads-to-account-takeover-no-user-interaction-ato-e6a36b8ef183) (24 Aug 2021). Timeline in the post: found 16 Aug 2021, triaged in 10 minutes, paid $5,000, fixed the next morning.

### 2. Admin-panel takeover via leaked forgot-password token plus documented reset API

- **Title:** Breaking the Barrier: Admin Panel Takeover Worth $3500
- **Platform / program:** Bugcrowd private program (target undisclosed)
- **Severity:** Not formally labeled in the republished writeup; impact was admin-panel access
- **Bounty:** $3,500 (publicly stated)
- **Bug class:** Password-reset token leak + auth bypass / admin takeover
- **Root cause:** Subdomain enumeration found an admin host. Directory enumeration on the admin "manage" area found a forgot-password page. Submitting a username caused the reset token to appear in the response. The remaining puzzle was how to *use* the token; reading the application's API documentation surfaced the reset endpoint and the `passwordConfirm` parameter, which accepted the leaked token and set a new admin password.
- **How it was found:** Collaboration with Rajesh Ranjan (who invited him onto the program). Recon: subdomain enum → admin login → directory fuzzing → forgot-password testing → API docs.
- **PoC:** Disclosed in the writeup; the full verbatim text is now stored in this repo under `posts/` (see the post file linked from this researcher index).
- **Takeaways:** Fuzz directories behind admin logins; forgot-password on admin panels is high-value. When a token leaks, go read official API docs instead of guessing the consumer. Program patched within an hour of submission.
- **Sources:** Republished at [Bug Bounty Directory](https://www.bugbountydirectory.com/blogs/breaking-the-barrier-admin-panel-takeover-worth-3500) (13 Aug 2024), originally on Medium.

### 3. Source-path disclosure from a missing Host header

- **Title:** Don't underestimate the errors — they can provide a good bounty
- **Platform / program:** Mamba bug bounty (`mamba.ru`)
- **Severity:** Information disclosure (path disclosure)
- **Bounty:** $200 (publicly stated)
- **Bug class:** Misconfigured error handling / information disclosure
- **Root cause:** After trying XSS and Host-header injection on a chat-bot subdomain, removing the Host header produced a 401 error that included a sensitive source-code path, instead of a generic 400.
- **How it was found:** Subdomain recon, then testing an uninteresting-looking bot-chat host and iterating on errors.
- **PoC:** Screenshots in the writeup (path redacted); the full verbatim text is now stored in this repo under `posts/` (see the post file linked from this researcher index).
- **Takeaways:** Weird error behavior is in-scope intel. Unexpected status codes and stack/path leaks on "dummy" subdomains are still reportable.
- **Sources:** [Medium writeup](https://assassin-marcos.medium.com/dont-underestimates-the-errors-they-can-provide-good-bounty-d437ecca6596) (7 Jun 2019). Reported 22 May 2019, rewarded 23 May 2019.

## 2026 payout posts (details undisclosed)

These are evidence of ongoing activity only. Bug class, program, and method were not stated, except as noted.

- $12,500 HackerOne — 15 Oct 2026 16:47 WAT — [post](https://x.com/Assass1nmarcos/status/2110759502081675582)
- $6,000 HackerOne — 12 Oct 2026 20:30 WAT — [post](https://x.com/Assass1nmarcos/status/2109728544893120639)
- $7,200 HackerOne — 12 Oct 2026 20:23 WAT — [post](https://x.com/Assass1nmarcos/status/2109726553705959685)
- $8,000 Bugcrowd and $4,950 HackerOne, thanks @ThisIsDK999 — 2 Oct 2026 18:06 WAT — [post](https://x.com/Assass1nmarcos/status/2106068361662922971)
- $10,000 HackerOne, with @bug_vs_me and @ThisIsDK999 — 1 Oct 2026 22:14 WAT — [post](https://x.com/Assass1nmarcos/status/2105768256917389365)
- $5,000 HackerOne — 30 Mar 2026 17:04 WAT — [post](https://x.com/Assass1nmarcos/status/2038648576335884461)
- $6,421 HackerOne — 20 Oct 2026 15:25 WAT — **author said the images were edited and fake** — [post](https://x.com/Assass1nmarcos/status/2112550747087024581)

## Other notes

On 8 Jul 2026 he publicly disputed a HackerOne triage that marked a claimed in-scope P1 BOLA on a large cybersecurity firm's API as informative / "subdomain takeover, out of scope." That disagreement is not independent confirmation of the bug. [Thread start](https://x.com/Assass1nmarcos/status/2074871162035986895).
