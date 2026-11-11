# @infinitelogins — Harley Kimball

- X: [https://x.com/infinitelogins](https://x.com/infinitelogins) (id `1197730077078720512`, created 22 Nov 2019)
- Bio (Nov 2026): Researcher Strategy & Live Hacking @ HackerOne; community cultivator; bug bounty hunter; co-founder @BugBountyDEFCON; founder of Disclosed
- Location listed: Portland, OR
- Newsletter: [getdisclosed.com](https://getdisclosed.com)
- Platforms: HackerOne (employee and hunter). Program names in the 2026 writeup posts were not disclosed.
- Focus: Web/API authentication, mass assignment, SQLi, recon process; weekly curation of other people's disclosures

The most technically detailed **web** writeups in this entire pass are his long X posts from Oct–Nov 2026. Below is a summary; the complete request-level text of every post is stored verbatim under `posts/infinitelogins/`.

He also posted that he finished top 5 in the US on HackerOne for a quarter (3 Jul 2026, [post](https://x.com/infinitelogins/status/2073099379712671799)) and, after ~6 weeks building an autonomous bounty system, was top 60 on H1 over 90 days and top 5 in the US (13 Apr 2026, [post](https://x.com/infinitelogins/status/2043552103076094169)).

## Findings with technical detail

### 1. Unauthenticated account takeover via leaked auto-login keys — $5,000

- **Title:** Critical unauthenticated account takeover (any customer, no password)
- **Platform / program:** Undisclosed
- **Severity:** Critical (author)
- **Bounty:** $5,000
- **Bug class:** Account takeover / broken authentication / wildcard injection in a secret lookup
- **Root cause (conceptually):** The product used unattended devices, so accounts had an "auto login key" that *was* the credential: presenting the key issued a session, with no password. That design is reasonable until a key leaks. The lookup endpoints used a SQL `LIKE`-style match on the key, so a wildcard character returned many rows instead of a single record, including enough data to obtain a victim's real key. There was no rate limit, so the customer table could be iterated. The device-registration endpoint then did what it was designed to do: trade a valid key for a session. The victim was not notified of the new device.
- **How found:** He mapped the device auto-login design, then tested whether secret-lookup endpoints were exact-match or pattern-match, then chained lookup → key resolve → device login.
- **PoC:** Described in the post; the full verbatim text is now stored in this repo under `posts/` (see the post file linked from this researcher index).
- **Takeaways:**
  - Any endpoint that *looks up a secret* is a candidate for wildcard / pattern-injection. If a metacharacter returns more than one record, you may be able to enumerate the table.
  - "This credential is only for devices" does not make leakage safe.
  - Missing rate limits turn a single-account leak into a platform-wide takeover.
- **Source:** 4 Nov 2026 15:04 WAT — [post](https://x.com/infinitelogins/status/2117981403161764138)

### 2. Mass assignment to superadmin, then MFA bypass via the device auto-login path — $5,000

- **Title:** Privilege escalation from a new free-trial account to platform superadmin
- **Platform / program:** Undisclosed (same product family as finding 1: it also had an auto-login / unattended-device flow)
- **Severity:** Critical (author)
- **Bounty:** $5,000
- **Bug class:** Mass assignment, MFA bypass, broken tenant isolation
- **Root cause (conceptually):** A PUT endpoint let a user write their own `admin_permissions` field, including a superadmin flag, with no check that they were already an admin. Becoming admin triggered MFA on the normal login path, and self-enrollment was disabled, which looked like a dead end. A separate auto-login / device flow issued session tokens **without MFA**, because devices have no human to complete a challenge. He generated a device key *before* escalating, then used that flow after the escalation so the new superadmin session skipped MFA. User IDs were sequential, and a superadmin token could read users in other organizations.
- **How found:** Tested mass assignment on profile/admin fields as a brand-new trial user; when MFA blocked the obvious login, he asked whether every token-issuing path enforced MFA.
- **PoC:** Described in the post; the full verbatim text is now stored in this repo under `posts/` (see the post file linked from this researcher index).
- **Takeaways:**
  - Bind mass-assignment allowlists tightly; permission fields must not be user-writable.
  - When MFA is added, audit **every** session-issuing path (device pairing, API keys, "magic" login, mobile clients).
  - Grab a long-lived credential *before* a new security boundary appears, then see if it still works after.
  - Sequential IDs plus broken tenant checks turn one privileged session into a platform data leak.
- **Source:** 28 Oct 2026 14:04 WAT — [post](https://x.com/infinitelogins/status/2115429533738262954)

### 3. Unauthenticated BigQuery SQL injection, WAF bypass, error-based extraction — $4,000

- **Title:** Critical unauthenticated SQL injection
- **Platform / program:** Undisclosed
- **Severity:** Critical (author)
- **Bounty:** $4,000
- **Bug class:** SQL injection, WAF bypass, verbose error leakage
- **Root cause (conceptually):** A public analytics API concatenated user input into BigQuery SQL. A simple quote produced a 500 whose error text identified BigQuery. The WAF blocked common keywords (`UNION`, `SELECT`, `AND`, `OR`, and some dynamic-SQL keywords) but missed BigQuery-specific scripting and encoding tricks, so he could still build a true/false oracle. Verbose 500s were then used as an **output channel**: the database was induced to put query results in the error message, which the API returned, so extraction did not have to be character-by-character. He could enumerate metadata and read customer and operational records, including fields another API had redacted.
- **How found:** Probe a public JSON API for error-based injection; fingerprint the dialect from the error; map WAF denials against that dialect's lesser-known features.
- **PoC:** Dialect-specific bypasses are in the post; the full verbatim text is now stored in this repo under `posts/` (see the post file linked from this researcher index).
- **Takeaways:**
  - Don't stop because a WAF blocks textbook payloads. Learn the **actual database dialect**.
  - A 500 is sometimes an output channel, not just a crash.
  - Never return raw database errors to unauthenticated clients.
- **Source:** 14 Oct 2026 14:02 WAT — [post](https://x.com/infinitelogins/status/2110355630133322159)

### 4. Multi-layer auth bypass (gateway vs backend path parsing) — $10,000

- **Title:** Critical auth bypass leading to mass PII exfiltration
- **Platform / program:** Undisclosed
- **Severity:** Critical (author)
- **Bounty:** $10,000 (he attributed the amount to the scale of PII)
- **Bug class:** Authentication bypass / parser differential / trusted-client header trust
- **Root cause (conceptually):** An employee API sat behind three checks: JWT auth at the gateway, backend path validation, and a trusted-client header. The gateway skipped JWT auth for paths that looked like static files (a `.json` suffix). The backend still wanted a clean identifier, so he needed a request that looked like a static file at the gateway but parsed as a normal id behind it (a fragment-style encoding difference). The last gate was only a client header, which is not a secret. Different layers interpreted the same URL differently.
- **How found:** Mapped each security check independently, then looked for disagreements between gateway and backend URL parsing.
- **PoC:** Exact request shaping is in the post; the full verbatim text is now stored in this repo under `posts/` (see the post file linked from this researcher index).
- **Takeaways:** When several layers share a request, **map every check** and test whether the gateway, proxy, and backend parse the path the same way. Suffix-based "static asset" exceptions are a classic auth bypass. Headers that merely name the client (`WEBAPP`, etc.) are not authentication.
- **Source:** 8 Oct 2026 14:01 WAT — [post](https://x.com/infinitelogins/status/2108181015885685018)

### 5. First bug-bounty SQLi, later paid maximum critical

- **Platform / program:** Undisclosed
- **Severity:** Maximum critical (author, 14 May 2026)
- **Bounty:** "max crit bounty" — dollar amount not stated
- **Bug class:** SQL injection
- **Method:** Only "after escalating for hours today." This may or may not be the same issue as finding 3 (the $4,000 writeup came in October and describes a $4,000 bounty, so they should be treated as **separate claims** unless he later ties them together).
- **Sources:** 10 May 2026 00:36 WAT [found](https://x.com/infinitelogins/status/2053257780895920586); 14 May 2026 15:27 WAT [paid](https://x.com/infinitelogins/status/2054931668570685494)

## Recon workflow tip

**30 Oct 2026 19:31 WAT:** Store recon in a real database (he suggested free Supabase, including MCP) rather than scattered text files: endpoints, parameters, headers, request/response shapes, related services. The payoff is being able to ask an agent questions against prior recon ("what other parameters have we seen on this endpoint?"). [post](https://x.com/infinitelogins/status/2116236446147240443)

## Curated, not his bugs

Disclosed regularly summarizes other researchers' work. Useful pointers from the 19 Oct 2026 issue ([post](https://x.com/infinitelogins/status/2112170733228966180), [getdisclosed.com](https://getdisclosed.com)) included Paulos Yibelo's PwnEscape, a Google DevSite pickle/RCE chain by Simon Koeck ($90k), brutecat on Google GFile ($100k), SLCyberSec's AEM Cloud pre-auth RCE chain, and wunderwuzzi23's trailing-dot Copilot bypass. Those belong to the named authors; see [researchers.md](../researchers.md) watch list.

On 19 Feb 2026 he also highlighted @spaceraccoon's project that watches GitHub commit diffs for vulnerability patches before CVEs are public — useful for variant hunting. [post](https://x.com/infinitelogins/status/2024484231062114553)
