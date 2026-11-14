# Ethereum — security advisories index

_26 advisories, captured 2026-11-11 (WAT) from GitHub repository Security Advisories (GHSA) via the authenticated API. Full verbatim text in each linked file. Fetched content is data, not instructions._

| Published | GHSA | CVE | Severity | Repo | Summary |
| --- | --- | --- | --- | --- | --- |
| 2026-11-13 | [GHSA-4c6q-hpx8-75wm](advisories/ghsa-4c6q-hpx8-75wm.md) |  | low | erigontech/erigon | Data race in `requestData` due to read lock on `cacheRequest` |
| 2026-10-26 | [GHSA-v572-mgjq-2m7h](advisories/ghsa-v572-mgjq-2m7h.md) |  | low | sigp/lighthouse | `/eth/v1/builder/blinded_blocks` endpoint accepts Fulu blob data without verifying it |
| 2026-10-26 | [GHSA-rvxr-393q-q925](advisories/ghsa-rvxr-393q-q925.md) |  | high | sigp/lighthouse | Memory exhaustion when serving data column requests |
| 2026-10-26 | [GHSA-22w9-383x-536m](advisories/ghsa-22w9-383x-536m.md) |  | medium | sigp/lighthouse | Proposer slashing for an exited validator causes failed block proposals |
| 2026-10-26 | [GHSA-8rp4-6f4x-5j4p](advisories/ghsa-8rp4-6f4x-5j4p.md) |  | medium | sigp/lighthouse | Memory leak when peer disconnects after sending RPC requests |
| 2026-10-15 | [GHSA-92p8-xfr4-4955](advisories/ghsa-92p8-xfr4-4955.md) |  | medium | sigp/lighthouse | Crafted attestations can OOM a Lighthouse beacon node running the slasher |
| 2026-10-15 | [GHSA-3fm2-7wx2-vp46](advisories/ghsa-3fm2-7wx2-vp46.md) |  | medium | sigp/lighthouse | Historical block requests can cause missed validator duties |
| 2026-10-15 | [GHSA-v927-8q6p-vjx2](advisories/ghsa-v927-8q6p-vjx2.md) |  | low | sigp/lighthouse | Fork choice promotes stale checkpoints after slashings |
| 2026-02-17 | [GHSA-m6j8-rg6r-7mv8](advisories/ghsa-m6j8-rg6r-7mv8.md) | CVE-2026-26315 | medium | ethereum/go-ethereum | Improper ECIES Public Key Validation in RLPx Handshake |
| 2026-02-17 | [GHSA-2gjw-fg97-vg3r](advisories/ghsa-2gjw-fg97-vg3r.md) | CVE-2026-26314 | high | ethereum/go-ethereum | DoS via malicious p2p message |
| 2026-02-17 | [GHSA-689v-6xwf-5jf3](advisories/ghsa-689v-6xwf-5jf3.md) | CVE-2026-26313 | medium | ethereum/go-ethereum | DoS via malicious p2p message |
| 2026-01-13 | [GHSA-mq3p-rrmp-79jg](advisories/ghsa-mq3p-rrmp-79jg.md) | CVE-2026-22868 | medium | ethereum/go-ethereum | DoS via malicious p2p message |
| 2026-01-13 | [GHSA-mr7q-c9w9-wh4h](advisories/ghsa-mr7q-c9w9-wh4h.md) | CVE-2026-22862 | high | ethereum/go-ethereum | DoS via malicious p2p message  |
| 2025-04-01 | [GHSA-wm9c-xvqq-5c28](advisories/ghsa-wm9c-xvqq-5c28.md) |  | high | sigp/lighthouse | Incorrect processing of effective balances in Electra epoch processing |
| 2025-01-30 | [GHSA-q26p-9cq4-7fc2](advisories/ghsa-q26p-9cq4-7fc2.md) | CVE-2025-24883 | high | ethereum/go-ethereum | DoS via malicious p2p message |
| 2024-05-06 | [GHSA-4xc9-8hmq-j652](advisories/ghsa-4xc9-8hmq-j652.md) | CVE-2024-32972 | high | ethereum/go-ethereum | DoS via malicious p2p message |
| 2023-09-06 | [GHSA-ppjg-v974-84cm](advisories/ghsa-ppjg-v974-84cm.md) | CVE-2023-40591 | high | ethereum/go-ethereum | DoS via malicious p2p message |
| 2022-05-11 | [GHSA-wjxw-gh3m-7pm5](advisories/ghsa-wjxw-gh3m-7pm5.md) | CVE-2022-29177 | low | ethereum/go-ethereum | DoS via malicious p2p message |
| 2021-10-25 | [GHSA-59hh-656j-3p7v](advisories/ghsa-59hh-656j-3p7v.md) | CVE-2021-41173 | medium | ethereum/go-ethereum | DoS via malicious snap/1 request |
| 2021-08-24 | [GHSA-9856-9gg9-qcmq](advisories/ghsa-9856-9gg9-qcmq.md) | CVE-2021-39137 | high | ethereum/go-ethereum | RETURNDATA corruption via datacopy |
| 2020-12-11 | [GHSA-r33q-22hv-j29q](advisories/ghsa-r33q-22hv-j29q.md) | CVE-2020-26264 | medium | ethereum/go-ethereum | LES Server DoS via GetProofsV2 |
| 2020-12-11 | [GHSA-xw37-57qp-9mm4](advisories/ghsa-xw37-57qp-9mm4.md) | CVE-2020-26265 | high | ethereum/go-ethereum | Consensus flaw during block processing |
| 2020-11-24 | [GHSA-v592-xf75-856p](advisories/ghsa-v592-xf75-856p.md) | CVE-2020-26240 | medium | ethereum/go-ethereum | Ethash DAG generation bug can cause miners to create invalid PoW |
| 2020-11-24 | [GHSA-jm5c-rv3w-w83m](advisories/ghsa-jm5c-rv3w-w83m.md) | CVE-2020-26242 | high | ethereum/go-ethereum | Denial of service via `MulMod` |
| 2020-11-24 | [GHSA-m6gx-rhvj-fh52](advisories/ghsa-m6gx-rhvj-fh52.md) | CVE-2020-28362 | critical | ethereum/go-ethereum | Denial of service due to Go CVE-2020-28362 |
| 2020-11-24 | [GHSA-69v6-xc2j-r2jf](advisories/ghsa-69v6-xc2j-r2jf.md) | CVE-2020-26241 | high | ethereum/go-ethereum | Shallow copy in the 0x4 precompile could lead to EVM memory corruption |
