# Instagram Account Takeover

- **Source URL:** https://masimshahzad.medium.com/instagram-account-takeover-racing-the-6-digit-code-e34bcf8a1407
- **Fetched from:** https://masimshahzad.medium.com/instagram-account-takeover-racing-the-6-digit-code-e34bcf8a1407?source=rss-440524433a10------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14998 (id 14998)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Muhammad Asim Shahzad / Tue, 24 Nov 2026 04:56:54 GMT

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

A six-digit code was the only thing standing between an attacker and an Instagram account takeover. In 2019, Laxman Muthiyah showed that Instagram’s mobile password-recovery flow throttled guesses per source but never capped guesses per code, so parallel requests from many IP addresses could cover the whole code space. Facebook fixed it and paid $30,000.

***Disclaimer:*** *Educational and defensive use only. This was patched in 2019. Reproduction details are intentionally omitted.*

The web reset flow used links and held up. The mobile flow sent a six-digit code by SMS instead. Six digits is one million possibilities, and each code stayed valid for 10 minutes.

There was a rate limit. In the researcher’s first test, roughly a quarter of a 1,000-request burst got through and the rest were throttled. But two things were missing. Throttled sources were slowed, never blocked. And the limit was keyed to the source, not to the code being guessed.

So the attack became arithmetic. He reports about 200 guesses per IP before throttling. Send them concurrently from many addresses and no single source ever trips the limit. In his test, 1,000 machines sent 200,000 guesses, a fifth of the code space, inside the window. His estimate for a full attack: about 5,000 IPs and roughly $150 of cloud compute.

A working attack meant full takeover of any account with a phone number on file; the victim would only see an SMS they never requested. Private messages, creator income and brand accounts were all exposed.

Facebook first could not reproduce it; a proof-of-concept video of 200,000 accepted requests changed that.

**1. Budget guesses per code, not per IP.** Attackers can rent IPs, not extra attempts.

**2. Count before you compare.** The attempt counter must be incremented atomically and committed before checking the guess, or parallel requests all read “0 attempts so far”.

**3. Cap code issuance per account.** Otherwise each fresh code is a fresh budget.

\# Pseudocode: the guess budget belongs to the code, not to the caller's IP

MAX\_TRIES = 5

def verify\_recovery\_code(account\_id, submitted, request):

rec = recovery\_codes.get\_active(account\_id) # one live code per account

if rec is None or rec.expires\_at \< now():

return reject("code\_invalid")

tries = recovery\_codes.increment\_attempts(rec.id) # atomic UPDATE ... RETURNING, committed now

if tries > MAX\_TRIES:

recovery\_codes.revoke(rec.id) # burn it; a new code must be requested

alert("recovery\_bruteforce", account\_id, request.ip)

return reject("code\_invalid")

if not constant\_time\_equals(rec.code\_hash, hash\_code(submitted)):

return reject("code\_invalid") # the failed attempt is already counted

if not recovery\_codes.consume\_once(rec.id): # compare-and-set: single use

return reject("code\_invalid")

return issue\_reset\_session(account\_id)

# Issuance cap: N codes/account/day keeps odds near N\*5 in a million

# Test: 1,000 parallel guesses from 1,000 IPs -> at most 5 compared, then code revoked

Found by **Laxman Muthiyah**. Primary source: his write-up [How I Could Have Hacked Any Instagram Account](https://thezerohack.com/hack-any-instagram) (The Zero Hack; the page now shows a later update date): flow, rate-limit observations, test scale, cost estimate and $30,000 reward. Date context: [SecurityWeek, 15 July 2019](https://www.securityweek.com/instagram-account-takeover-vulnerability-earns-hacker-30000/). Facts come from those sources; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
