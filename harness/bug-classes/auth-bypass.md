# Authentication / authorization bypass

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/` and `writeups/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


## Detection signals
- A protected path returns 403 or redirects to login, but the auth check and the router may parse the path differently (gate vs router disagreement).
- Tokens (JWT / session / reset) are accepted without the signature actually being verified.
- Pre-auth endpoints (login, activate, reset, verify) expose privileged actions.

## Recon steps
- Enumerate 403 / login-redirect paths and protected prefixes (`/admin`, `/api/internal`).
- Collect all tokens in use (cookies, Authorization headers, URL params) and their structure.
- Map pre-auth endpoints from the recon route map (Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md), class `preauth-bypass`).

## Payloads / requests seen in sources
- Path-normalization bypass: retry gated paths with `/./`, `//`, trailing dots, `%2e` — e.g. `GET /admin/./` passed an exact-match auth check then normalised to `/admin`. Source: [`posts/mdp_sec/2026-11-11-2120338219841544604.md`](../../posts/mdp_sec/2026-11-11-2120338219841544604.md).
- Token signature not verified: tamper claims and signature (strip, alter, `alg=none`, self-sign) and confirm acceptance ($8,000). Source: [`posts/mdp_sec/2026-11-05-2118435683329310786.md`](../../posts/mdp_sec/2026-11-05-2118435683329310786.md).
- API version bypass: replay each shape on `/v1`..`/vN`, unversioned, header and query variants, including write verbs; older versions often keep weaker authz. Source: Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md) (class `api-version`).

## Tools
- Burp/Caido + Param Miner (headers), `httpx`, a JWT editor, and his API-version replay logic (Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md)).

## Automation (check spec)
```
for path in protected_paths:
  for variant in [p, p+'/./', p+'//', p+'/%2e/', p+'.']:
    if status(variant) in (200,) and status(p) in (401,403,302): FLAG path-normalization-authz
for token in observed_tokens:
  if accepts(tamper(token, alg='none')) or accepts(strip_sig(token)): FLAG unverified-signature
for shape in api_shapes:
  for v in version_variants(shape):
    if authz(v) weaker-than authz(shape): FLAG api-version-authz
```

## Related findings
- See `harness/findings.jsonl` records with bug_class containing "Auth bypass" / "path normalisation".

