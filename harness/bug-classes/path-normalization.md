# Path Normalization

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **3** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Always test ACL/proxy vs backend parser differentials with encoded and special-character path variants. (from 0xacb). Source: [`posts/0xacb/ARCHIVE.md`](../../posts/0xacb/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Method / findings in sources

- **Nginx ACL vs backend parser inconsistencies — forbidden routes become accessible** — Nginx normalizes paths before ACL; backends (Node/PHP/Flask/Spring) decode again differently. Prefixing with ;/@/%00, over-encoding, or inserting special chars can bypass Nginx location deny while backend routes to /admin. Examples: Node ignores \xa0/\x09/\x0c; Flask strips \x85; Spring ignores \x09/; PHP-FPM /admin.php/index.php; AWS WAF line-fold Source: [`posts/0xacb/ARCHIVE.md`](../../posts/0xacb/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **higher-bug-bounties-wont-stop-hacks** — Although projects can always choose to go above and beyond, it is well understood today that there are three key steps to crypto security: write tests to ensure that basic mistakes are caught during development, use audits and contests to conduct a comprehensive review prior to deployment, and set up a bug bounty program to incentivize and reward r Source: [`writeups/samczsun/higher-bug-bounties-wont-stop-hacks.md`](../../writeups/samczsun/higher-bug-bounties-wont-stop-hacks.md).
- **How I Chained RCE Via Dependencies Confusion to LFI** — Hii Everyone I’m Suryesh a Bug Bounty Hunter. In this write-up/blog i’ll explained about Dependencies Confusion attack and how i chained it into LFI. So, everything i’ll keep it very simple because i know there are lot of beginners who facing problem to understand this vulnerability. Please forgot to any grammatical error. So, Let’s Start Source: [`writeups/Suryesh_92/how-i-chained-rce-via-dependencies-to-lfi.md`](../../writeups/Suryesh_92/how-i-chained-rce-via-dependencies-to-lfi.md).

## Payloads / requests seen in sources

- `/;admin ; /admin%2f..%2f ; /admin\xa0 (Node) ; /admin\x85 (Flask) ; /admin; or /admin\x09 (Spring) ; /admin.php/index.php (PHP-FPM)` — Nginx ACL vs backend parser inconsistencies — forbidden routes become accessible. Source: [`posts/0xacb/ARCHIVE.md`](../../posts/0xacb/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

See also [`../payloads/path-normalization.md`](../payloads/path-normalization.md) when present.

## Automation (check spec)

```
# Checks derived from 3 documented finding(s) in findings.jsonl for class=path-normalization
# try: /;admin ; /admin%2f..%2f ; /admin\xa0 (Node) ; /admin\x85 (Flask) ; /admin; or /admin\x09 (Spring) ; /admin.php/index.php (PHP-FPM)
```

## Prior harness notes (retained)

_Retained from earlier curated harness file; still cites local sources._

## Detection signals
- Auth/gate matches the raw path; the router normalises afterwards.

## Payloads seen in sources
- `/./`, `//`, trailing dots, `%2e` on any 403/login-gated path. `/admin/./` → bypass. Source: [`posts/mdp_sec/2026-11-11-2120338219841544604.md`](../../posts/mdp_sec/2026-11-11-2120338219841544604.md). Also `path-bypass` Stage-B class in Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md).
- Path traversal / LFI is its own Stage-B class (not demoted). Source: Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md) (`lfi`).

## Automation (check spec)
```
for p in gated_paths:
  for variant in dot_segment_and_encoding_variants(p):
    if status(variant)==200 and status(p) in (401,403,302): FLAG path-authz-bypass
```
