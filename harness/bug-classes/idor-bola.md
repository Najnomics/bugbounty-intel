# Idor Bola

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **3** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Password-reset endpoints that echo or accept other users' identifiers are enum+ATO primitives. (from RootxRavi). Source: [`posts/RootxRavi/ARCHIVE.md`](../../posts/RootxRavi/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Classic IDOR still yields ATO on high-profile targets. (from galnagli). Source: [`posts/galnagli/ARCHIVE.md`](../../posts/galnagli/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- A repeatable A/B access-control loop; the revoke step catches stale-permission bugs. (from mdp_sec). Source: [`posts/mdp_sec/2026-11-06-2118526280379343189.md`](../../posts/mdp_sec/2026-11-06-2118526280379343189.md), [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md), [`writeups/mdp_sec/mdpsec-home.md`](../../writeups/mdp_sec/mdpsec-home.md).

## Method / findings in sources

- **IDOR on forgot-password → mass username/email enumeration (3-digit bounty)** — Forgot-password flow on developer account yielded password-reset link pattern enabling IDOR mass username/email enumeration. Source: [`posts/RootxRavi/ARCHIVE.md`](../../posts/RootxRavi/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **DoD website IDOR → account takeover (blog writeup)** — IDOR discovered on a USA DoD website enabling account takeover. Blog with takeaways for new hunters. Source: [`posts/galnagli/ARCHIVE.md`](../../posts/galnagli/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Two-account IDOR/BAC testing checklist** — N/A – methodology post. Source: [`posts/mdp_sec/2026-11-06-2118526280379343189.md`](../../posts/mdp_sec/2026-11-06-2118526280379343189.md), [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md), [`writeups/mdp_sec/mdpsec-home.md`](../../writeups/mdp_sec/mdpsec-home.md).

## Automation (check spec)

```
# Checks derived from 3 documented finding(s) in findings.jsonl for class=idor-bola
# note: Password-reset endpoints that echo or accept other users' identifiers are enum+ATO primitives.
# note: Classic IDOR still yields ATO on high-profile targets.
# note: A repeatable A/B access-control loop; the revoke step catches stale-permission bugs.
```

## Prior harness notes (retained)

_Retained from earlier curated harness file; still cites local sources._

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
