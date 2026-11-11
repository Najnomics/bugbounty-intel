# Business logic / mass assignment / workflow abuse

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **2** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Check every token-issuing path for MFA enforcement; grab credentials before a security boundary goes up and reuse after. (from infinitelogins). Source: [`posts/infinitelogins/2026-10-28-2115429533738262954.md`](../../posts/infinitelogins/2026-10-28-2115429533738262954.md).
- Liabilities/collateral accounting that can be reset are double-count primitives. (from ChainLight_io). Source: [`posts/ChainLight_io/ARCHIVE.md`](../../posts/ChainLight_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Method / findings in sources

- **Free-trial → platform superadmin via mass assignment + MFA-skipping auto-login ($5,000)** — PUT /api/admin/{my-user-id} accepted writing admin_permissions including superadmin with no prior-admin check. Escalation triggered MFA on normal login, but a previously-minted auto-login/device key still issued a session with no MFA. Superadmin token could read any user's data across orgs (sequential IDs). Source: [`posts/infinitelogins/2026-10-28-2115429533738262954.md`](../../posts/infinitelogins/2026-10-28-2115429533738262954.md).
- **Orion $645K — token liability resettable, enabling over-withdrawal** — Poor management of token liability that should be set only once; liability could be reset by another function, allowing withdraw of more tokens than staked (double-counted collateral / flawed staking business logic). Source: [`posts/ChainLight_io/ARCHIVE.md`](../../posts/ChainLight_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Payloads / requests seen in sources

- `PUT /api/admin/{my-user-id} {"admin_permissions":"0000000f"}; POST /autologin/devices {"access_key":"{my-key}"}; GET /api/users/{any-user-id}` — Free-trial → platform superadmin via mass assignment + MFA-skipping auto-login ($5,000). Source: [`posts/infinitelogins/2026-10-28-2115429533738262954.md`](../../posts/infinitelogins/2026-10-28-2115429533738262954.md).

See also [`../payloads/business-logic.md`](../payloads/business-logic.md) when present.

## Automation (check spec)

```
# Checks derived from 2 documented finding(s) in findings.jsonl for class=business-logic
# try: PUT /api/admin/{my-user-id} {"admin_permissions":"0000000f"}; POST /autologin/devices {"access_key":"{my-key}"}; GET /api/users/{any-user-id}
# note: Liabilities/collateral accounting that can be reset are double-count primitives.
```
