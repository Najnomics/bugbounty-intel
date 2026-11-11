# OAuth / OIDC / SAML / SIWE

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/` and `writeups/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


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

