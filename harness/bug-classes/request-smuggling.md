# HTTP request smuggling / desync

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/` and `writeups/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


## Detection signals
- A front-end proxy and back-end disagree on request boundaries (CL.TE / TE.CL / CL.CL), or trust internal headers from outside.

## Method / requests seen in sources
- $300k came from a **trusted internal header accepted from outside** — brute-force hidden/internal headers (e.g. with Param Miner). Source: [`posts/albinowax/2026-11-04-2117935178278371560.md`](../../posts/albinowax/2026-11-04-2117935178278371560.md).
- SMTP dot-stuffing smuggling is a live variant. Source: [`posts/albinowax/`](../../posts/albinowax/) and techniques.md.
- Header injection (Host, X-Forwarded-*, CRLF) is a Stage-B sweep. Source: Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md) (class `header-inj`).

## Tools
- Burp HTTP Request Smuggler + Param Miner (James Kettle / PortSwigger research, [`writeups`/posts under garethheyes/albinowax]).

## Automation (check spec)
```
run smuggler probes (CL.TE/TE.CL) per host
for h in internal_header_wordlist: if behavior_changes(add_header(h)): FLAG trusted-internal-header
fuzz Host / X-Forwarded-* / CRLF
```

