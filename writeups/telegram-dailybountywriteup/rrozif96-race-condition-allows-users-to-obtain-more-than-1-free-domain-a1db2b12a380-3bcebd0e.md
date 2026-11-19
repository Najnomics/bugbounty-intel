# Race Condition Allows Users to Obtain More Than 1 Free Domain

- **Source URL:** https://medium.com/@rrozif96/race-condition-allows-users-to-obtain-more-than-1-free-domain-a1db2b12a380?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260426120941/https://medium.com/@rrozif96/race-condition-allows-users-to-obtain-more-than-1-free-domain-a1db2b12a380
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13366 (id 13366)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Race Condition Allows Users to Obtain More Than 1 Free Domain

*Disclaimer: This is a report from someone else that I am studying, not my own finding. (Source: Automattic | Report #2616045 — Race condition on add 1 free domain | HackerOne)*

**Affected Platform:**

[wordpress.com](https://wordpress.com/) (related to Gravatar service)

**Brief Description**

When a platform offers free accounts, they typically limit certain features (e.g., only 1 free domain claim per account). If a race condition flaw exists, a user can exploit it to bypass these limits and obtain more than they should.

In this case, a user with a free [WordPress.com](https://wordpress.com/) account (via Gravatar) could obtain more than 1 free domain by sending multiple parallel requests during the domain claim transaction process.

**Steps to Reproduce (relaxed style):**

1. Create a free account on Gravatar.
2. Log in to that account, then select the free domain claim menu (usually in the profile section — hidden menu, intentionally redacted as █████).
3. After clicking, you will be redirected to a [WordPress.com](https://wordpress.com/) URL like:
4. `https://wordpress.com/start/domain-for-gravatar/domain-only?search=yes&new=(your gravatar domain name)`
5. Continue the process until you reach the checkout page (even though it’s free, there is still a transaction process).
6. Reach this endpoint:
7. `public-api.wordpress.com/rest/v1.1/me/transactions? ██████`
8. Prepare a group of requests (using Burp Suite or similar tools), then duplicate that request 1–15 times.
9. Change the “meta” parameter in each request to a different name (e.g., “meta1”, “meta2”, etc.).
10. Send all requests simultaneously / in parallel.
11. Result: More than 1 free domain will be obtained (even though only 1 per account is intended).

Full PoC details are in the attached files (screenshots, video, or request/response logs).

**Impact:**

A malicious user could obtain more than 1 free domain on [WordPress.com](https://wordpress.com/), which should not be possible on a free account. This harms the platform because of:

- Abuse of resources (free domains)
- Potential illegal resale
- Bypassing feature limitation systems

**Remediation Recommendations:**

- Use a locking mechanism (e.g., row-level lock or Redis lock) during the domain claim process.
- Ensure transactions are atomic so only one request succeeds.
- Use an anti-replay token (e.g., a single-use nonce).
- Limit request frequency per user in a short time window (rate limiting).

**Reference:**

CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization (‘Race Condition’)

Hope this helps for learning purposes.
