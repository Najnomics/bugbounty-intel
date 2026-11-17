# Oauth

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **2** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Client ID says which app asked; it must never grant admin capability. Authn ≠ authz. (from mdp_sec). Source: [`posts/mdp_sec/2026-09-03-2095462761111388207.md`](../../posts/mdp_sec/2026-09-03-2095462761111388207.md).
- OAuth redirect/state issues remain top-paid at LHEs. (from galnagli). Source: [`posts/galnagli/ARCHIVE.md`](../../posts/galnagli/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Method / findings in sources

- **Public OAuth client ID treated as authority — free account R/W production billing catalog ($2,500)** — A public OAuth client let any free self-registered account read and write the production billing catalog. Backend treated client identity as authority and forgot to verify user authorization. Submitted Critical, triaged High, paid $2,500. Source: [`posts/mdp_sec/2026-09-03-2095462761111388207.md`](../../posts/mdp_sec/2026-09-03-2095462761111388207.md).
- **$20,000 OAuth bug (live hacking event) — lab replica with NahamSec/HackingHub** — OAuth bug discovered at a live hacking event worth $20,000; lab replica and walkthrough published with NahamSec & hackinghub. Source: [`posts/galnagli/ARCHIVE.md`](../../posts/galnagli/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Payloads / requests seen in sources

- `Use public OAuth client_id as a free user against production billing catalog endpoints` — Public OAuth client ID treated as authority — free account R/W production billing catalog ($2,500). Source: [`posts/mdp_sec/2026-09-03-2095462761111388207.md`](../../posts/mdp_sec/2026-09-03-2095462761111388207.md).

See also [`../payloads/oauth.md`](../payloads/oauth.md) when present.

## Automation (check spec)

```
# Checks derived from 2 documented finding(s) in findings.jsonl for class=oauth
# try: Use public OAuth client_id as a free user against production billing catalog endpoints
# note: OAuth redirect/state issues remain top-paid at LHEs.
```

## Prior harness notes (retained)

_Retained from earlier curated harness file; still cites local sources._

## Detection signals
- Multiple client_ids (web vs mobile vs desktop) with different redirect_uri validation.
- Custom URL schemes accepted as redirect targets (mobile deep links).
- state/nonce reuse, code reuse, postMessage token leakage, SIWE signature replay / chain-id confusion.

## Payloads seen in sources
- Enumerate every client_id; an iOS client accepted any protocol in redirect_uri, so a malicious app registering that scheme captured the token (ATO). Source: [`posts/xssdoctor/2026-10-01-2105723370125881675.md`](../../posts/xssdoctor/2026-10-01-2105723370125881675.md).
- OAuth/OIDC/SAML (redirect_uri, state, code reuse, binding, postMessage leakage) and SIWE/wallet (nonce reuse, signature replay, chain-id) are Stage-A classes. Source: Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md) (`oauth`, `siwe`).

## Automation (check spec)
```
for cid in enumerate_client_ids():
  test redirect_uri: foreign host, custom scheme, open-redirect chain, path append
for flow: reuse(state); reuse(code); check postMessage targetOrigin
for siwe: replay(signature); reuse(nonce); swap(chain_id)
```

- 2026-11-17: see [2026-11-17 check-specs](2026-11-17-ai-tool-idor-oauth-scheme-roles-module.md)
