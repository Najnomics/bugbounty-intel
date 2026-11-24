# Booking.com OAuth Account Takeover in Three Small Gaps

- **Source URL:** https://masimshahzad.medium.com/booking-com-oauth-account-takeover-in-three-small-gaps-373036855acc
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14997 (id 14997)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Booking.com OAuth Account Takeover in Three Small Gaps

### Salt Labs chained a loose redirect path, an open redirect and a client-supplied URI into one-click Booking.com and Kayak takeover

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

One link on a legitimate facebook.com URL was enough for a Booking.com OAuth account takeover. Salt Labs researcher Aviad Carmel chained three minor-looking gaps to open any account that used “Log in with Facebook”, plus its linked Kayak login. Booking.com fixed them within weeks of the December 2022 report.

***Disclaimer:*** *Educational and defensive use only. Booking.com remediated these issues before the March 2023 publication. Reproduction details are intentionally omitted.*

### Vulnerability Overview

- **Type:** OAuth code theft via a loose redirect URI and an open redirect, completed by a client-controlled exchange URI; result: account takeover
- **CWE (analytical mapping, not from the source):** CWE-601 (URL Redirection to Untrusted Site), CWE-346 (Origin Validation Error), CWE-472 (External Control of Assumed-Immutable Web Parameter)
- **CVE:** None (hosted service)
- **Severity/Bounty:** Not reported

### How the Booking.com OAuth Account Takeover Worked (high level)

**Gap one: redirects registered by origin, not path.** Facebook only enforced that the code returned to Booking’s account domain. Any path there was accepted.

**Gap two: an open redirect on that domain.** A settings flow read its next destination from inside its state parameter, with no allowlist. Aim the OAuth redirect at that flow, request a response mode that puts the code in the URL fragment, and the browser carries the victim’s code to an outside site.

**Gap three: the client chose the exchange URI.** A stolen code alone failed: Facebook requires the exchange to repeat the original redirect URI, and the website sent a fixed one. The Android app’s login request, however, carried a result URI the backend used for the exchange. Supplying the malicious link’s URI made Facebook accept the code.

### Business Impact

The attacker got the victim’s session: personal data, booking history, reservations, and the power to act as them, including cancelling bookings. The login also worked on Kayak. Accounts created with Google were exposed too, because Booking matched the Facebook email to the existing account. The victim only clicked a trusted-domain link.

### Fixing Booking.com-Style OAuth Flaws (my own analysis)

**1. Register exact redirect URIs.** Origin matching turns any redirect into a leak.

**2. Keep the exchange redirect URI on the server,** for web and mobile alike.

**3. Allowlist post-login destinations** as relative paths, never inside a client-editable state blob.

**4. Bind codes to the starting session** with single-use state and PKCE where supported.

\# Pseudocode: an OAuth callback where the client never chooses the redirect URI

REDIRECT\_URI = "https://account.example.com/oauth/callback/facebook" # exact match at the IdP

def finish\_login(session, request):

expected = session.pop("oauth\_state", None) # single use, consumed even on failure

verifier = session.pop("pkce\_verifier", None)

if expected is None or not constant\_time\_eq(request.state, expected):

return error(400, "invalid\_state")

tokens = idp\_exchange(code=request.code,

redirect\_uri=REDIRECT\_URI, # server constant; ignore client URIs

code\_verifier=verifier)

return login\_as(verified\_identity(tokens))

def safe\_next(path):

ok = path.startswith("/") and not path.startswith("//") and "\\" not in path

return path if ok else "/"

# Test: a code injected into another session's flow fails the PKCE check

# Test: safe\_next("https://evil.example") and safe\_next("//evil.example") -> "/"

### Key Takeaways

- Three “low” OAuth findings made one critical.
- Mobile clients are OAuth attack surface; review what their requests let a user set.
- Linking accounts by email makes every login method as weak as the weakest.

### Credit & Sources

Research by **Aviad Carmel** (Salt Labs, Salt Security): [Traveling with OAuth: Account Takeover on Booking.com](https://salt.security/blog/traveling-with-oauth-account-takeover-on-booking-com) (2 March 2023), including Booking.com’s statement; report date from [SecurityWeek](https://www.securityweek.com/critical-vulnerabilities-allowed-booking-com-account-takeover/). Facts come from those sources; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
