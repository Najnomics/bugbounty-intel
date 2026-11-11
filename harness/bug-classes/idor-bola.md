# IDOR / BOLA (broken object-level authorization)

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/` and `writeups/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


## Detection signals
- Object references (ids, uuids, filenames) in requests that can be swapped across accounts.
- Sequential or predictable ids.
- A private record created by account A is readable/mutable by account B.

## Recon steps
- Stand up two researcher-owned accounts (A attacker, B victim) — his dual-lane model (Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md), Stage A, class `idor-x`).
- Catalog every object-reference parameter and the verbs each endpoint accepts.

## Method / requests seen in sources
- Two-account loop: create a private record as A, try to read and change it as B, share it with B then revoke, and retest after revoke (catches stale permissions). Source: [`posts/mdp_sec/2026-11-06-2118526280379343189.md`](../../posts/mdp_sec/2026-11-06-2118526280379343189.md).
- Sequential/predictable id walk and unauthenticated API access are separate Stage-B sweeps (Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md), classes `id-walk`, `unauth-access`).

## Tools
- Two browser profiles / sessions, Autorize-style cross-account replay, Burp Intruder for id walks.

## Automation (check spec)
```
for ep in object_endpoints:
  respA = request(ep, id=A_obj, session=A)
  respB = request(ep, id=A_obj, session=B)     # cross-account read
  if respB.ok and respB.body==respA.body: FLAG idor-read
  if mutate(ep, id=A_obj, session=B).ok: FLAG idor-write
  if sequential(id): enumerate nearby ids as B
  # revoke test
  share(A_obj, B); revoke(A_obj, B)
  if request(ep, id=A_obj, session=B).ok: FLAG stale-permission
```

## Related findings
- `harness/findings.jsonl` records with bug_class "IDOR" / access control.

