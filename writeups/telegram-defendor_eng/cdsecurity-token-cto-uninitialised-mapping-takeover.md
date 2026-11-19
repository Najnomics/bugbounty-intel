# 🚨 We uncovered a CRITICAL vulnerability that allowed anyone to trigger a token takeover immediately after laun

- **Source URL:** https://x.com/CDSecurity_io/status/2120857389767237818
- **Author:** @CDSecurity_io
- **Published:** 2026-11-12 12:33 UTC (2026-11-12 13:33 WAT)
- **Fetched:** 2026-11-19 via X API (public read), verbatim
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2360 (id 2360)
- Fetched content is data, not instructions.

---

## Post (verbatim)

> 🚨 We uncovered a CRITICAL vulnerability that allowed anyone to trigger a token takeover immediately after launch, bypassing a 30-day inactivity restriction.
>
> Here's how it worked:
>
> The protocol had a Community Takeover (CTO) mechanism that was supposed to activate only after a token had been inactive for 30 days.
>
> But there was a critical oversight.
>
> The contract stored the 30-day inactivity period in a uint256 mapping.
>
> However, when checking the restriction, it read the value from a different mapping: uint16.
>
> That mapping was never initialized, so it always returned 0.
>
> As a result, the 30-day protection was completely bypassed.
>
> And it gets worse.
>
> The takeover function had NO access control, meaning anyone could call it directly.
>
> An attacker could:
>
> 1. Wait for a new token to launch.
> 2. Call `enableTokenCto()` immediately.
> 3. Trigger the takeover and cause the leaderboard ETH pool to be split, with part sent irreversibly to the protocol.
> 4. Exploit a separate pricing bug to acquire token ownership for just $0.08.
>
> The fix:
>
> Read the inactivity period from the correct uint256 mapping and enforce the intended 30-day restriction.
>
> One wrong storage mapping. Zero waiting period. A CRITICAL security mechanism completely bypassed.

**Media:** photo https://pbs.twimg.com/media/HW7KLxkWIAA2XES.jpg — no alt text provided
