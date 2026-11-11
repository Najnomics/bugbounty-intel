# Ethereum — security advisories index

_34 advisories (go-ethereum GHSA + global Advisory DB). Solidity's 67 compiler bugs are in [solidity-compiler-bugs.md](solidity-compiler-bugs.md). Captured 2026-11-11 (WAT). Full verbatim text in each linked file. Data, not instructions._

| Published | File | CVE | Severity | Summary |
| --- | --- | --- | --- | --- |
| 2026-10-26 | [ghsa-v572-mgjq-2m7h.md](advisories/ghsa-v572-mgjq-2m7h.md) |  | low | GHSA-v572-mgjq-2m7h: `/eth/v1/builder/blinded_blocks` endpoint accepts Fulu blob data with |
| 2026-10-26 | [ghsa-rvxr-393q-q925.md](advisories/ghsa-rvxr-393q-q925.md) |  | high | GHSA-rvxr-393q-q925: Memory exhaustion when serving data column requests |
| 2026-10-26 | [ghsa-8rp4-6f4x-5j4p.md](advisories/ghsa-8rp4-6f4x-5j4p.md) |  | medium | GHSA-8rp4-6f4x-5j4p: Memory leak when peer disconnects after sending RPC requests |
| 2026-10-26 | [ghsa-22w9-383x-536m.md](advisories/ghsa-22w9-383x-536m.md) |  | medium | GHSA-22w9-383x-536m: Proposer slashing for an exited validator causes failed block proposa |
| 2026-10-15 | [ghsa-v927-8q6p-vjx2.md](advisories/ghsa-v927-8q6p-vjx2.md) |  | low | GHSA-v927-8q6p-vjx2: Fork choice promotes stale checkpoints after slashings |
| 2026-10-15 | [ghsa-92p8-xfr4-4955.md](advisories/ghsa-92p8-xfr4-4955.md) |  | medium | GHSA-92p8-xfr4-4955: Crafted attestations can OOM a Lighthouse beacon node running the sla |
| 2026-10-15 | [ghsa-3fm2-7wx2-vp46.md](advisories/ghsa-3fm2-7wx2-vp46.md) |  | medium | GHSA-3fm2-7wx2-vp46: Historical block requests can cause missed validator duties |
| 2026-02-17 | [ghsa-m6j8-rg6r-7mv8.md](advisories/ghsa-m6j8-rg6r-7mv8.md) | CVE-2026-26315 | medium | GHSA-m6j8-rg6r-7mv8: Improper ECIES Public Key Validation in RLPx Handshake |
| 2026-02-17 | [ghsa-689v-6xwf-5jf3.md](advisories/ghsa-689v-6xwf-5jf3.md) | CVE-2026-26313 | medium | GHSA-689v-6xwf-5jf3: DoS via malicious p2p message |
| 2026-02-17 | [ghsa-2gjw-fg97-vg3r.md](advisories/ghsa-2gjw-fg97-vg3r.md) | CVE-2026-26314 | high | GHSA-2gjw-fg97-vg3r: DoS via malicious p2p message |
| 2026-01-13 | [ghsa-mr7q-c9w9-wh4h.md](advisories/ghsa-mr7q-c9w9-wh4h.md) | CVE-2026-22862 | high | GHSA-mr7q-c9w9-wh4h: DoS via malicious p2p message |
| 2026-01-13 | [ghsa-mq3p-rrmp-79jg.md](advisories/ghsa-mq3p-rrmp-79jg.md) | CVE-2026-22868 | medium | GHSA-mq3p-rrmp-79jg: DoS via malicious p2p message |
| 2025-04-01 | [ghsa-wm9c-xvqq-5c28.md](advisories/ghsa-wm9c-xvqq-5c28.md) |  | high | GHSA-wm9c-xvqq-5c28: Incorrect processing of effective balances in Electra epoch processin |
| 2025-01-30 | [ghsa-q26p-9cq4-7fc2.md](advisories/ghsa-q26p-9cq4-7fc2.md) | CVE-2025-24883 | high | GHSA-q26p-9cq4-7fc2: DoS via malicious p2p message |
| 2024-05-06 | [ghsa-4xc9-8hmq-j652.md](advisories/ghsa-4xc9-8hmq-j652.md) | CVE-2024-32972 | high | GHSA-4xc9-8hmq-j652: DoS via malicious p2p message |
| 2023-10-18 | [ghsa-v9jh-j8px-98vq.md](advisories/ghsa-v9jh-j8px-98vq.md) | CVE-2023-42319 | high | GHSA-v9jh-j8px-98vq: go-ethereum vulnerable to denial of service via crafted GraphQL query |
| 2023-09-06 | [ghsa-ppjg-v974-84cm.md](advisories/ghsa-ppjg-v974-84cm.md) | CVE-2023-40591 | high | GHSA-ppjg-v974-84cm: DoS via malicious p2p message |
| 2022-08-06 | [ghsa-rqmg-hrg4-fm69.md](advisories/ghsa-rqmg-hrg4-fm69.md) | CVE-2022-37450 | medium | GHSA-rqmg-hrg4-fm69: Go Ethereum allows attackers to use manipulation of time-difference v |
| 2022-05-14 | [ghsa-p5gc-957x-gfw9.md](advisories/ghsa-p5gc-957x-gfw9.md) | CVE-2018-12018 | high | GHSA-p5gc-957x-gfw9: Go Ethereum LES protocol implementation vulnerable to Denial of Servi |
| 2022-05-11 | [ghsa-wjxw-gh3m-7pm5.md](advisories/ghsa-wjxw-gh3m-7pm5.md) | CVE-2022-29177 | low | GHSA-wjxw-gh3m-7pm5: DoS via malicious p2p message |
| 2022-03-18 | [ghsa-vrcc-g6vj-mh5w.md](advisories/ghsa-vrcc-g6vj-mh5w.md) | CVE-2021-42219 | high | GHSA-vrcc-g6vj-mh5w: Denial of service in go-ethereum |
| 2022-03-05 | [ghsa-vmf7-hmh6-vv57.md](advisories/ghsa-vmf7-hmh6-vv57.md) | CVE-2022-23328 | high | GHSA-vmf7-hmh6-vv57: Denial of Service in Go-Ethereum |
| 2022-03-05 | [ghsa-pvx3-gm3c-gmpr.md](advisories/ghsa-pvx3-gm3c-gmpr.md) | CVE-2022-23327 | high | GHSA-pvx3-gm3c-gmpr: Denial of Service in Go-Ethereum |
| 2021-11-23 | [ghsa-5m8f-chrv-7rw5.md](advisories/ghsa-5m8f-chrv-7rw5.md) | CVE-2021-43668 | medium | GHSA-5m8f-chrv-7rw5: Denial of Service in Go-Ethereum |
| 2021-10-25 | [ghsa-59hh-656j-3p7v.md](advisories/ghsa-59hh-656j-3p7v.md) | CVE-2021-41173 | medium | GHSA-59hh-656j-3p7v: DoS via malicious snap/1 request |
| 2021-08-24 | [ghsa-9856-9gg9-qcmq.md](advisories/ghsa-9856-9gg9-qcmq.md) | CVE-2021-39137 | high | GHSA-9856-9gg9-qcmq: RETURNDATA corruption via datacopy |
| 2021-06-29 | [ghsa-9h4h-8w5p-f28w.md](advisories/ghsa-9h4h-8w5p-f28w.md) | CVE-2018-19184 | high | GHSA-9h4h-8w5p-f28w: Go Ethereum Denial of Service |
| 2021-05-18 | [ghsa-qr2j-wrhx-4829.md](advisories/ghsa-qr2j-wrhx-4829.md) | CVE-2018-16733 | high | GHSA-qr2j-wrhx-4829: Go Ethereum Improper Input Validation |
| 2020-12-11 | [ghsa-xw37-57qp-9mm4.md](advisories/ghsa-xw37-57qp-9mm4.md) | CVE-2020-26265 | high | GHSA-xw37-57qp-9mm4: Consensus flaw during block processing |
| 2020-12-11 | [ghsa-r33q-22hv-j29q.md](advisories/ghsa-r33q-22hv-j29q.md) | CVE-2020-26264 | medium | GHSA-r33q-22hv-j29q: LES Server DoS via GetProofsV2 |
| 2020-11-24 | [ghsa-v592-xf75-856p.md](advisories/ghsa-v592-xf75-856p.md) | CVE-2020-26240 | medium | GHSA-v592-xf75-856p: Ethash DAG generation bug can cause miners to create invalid PoW |
| 2020-11-24 | [ghsa-m6gx-rhvj-fh52.md](advisories/ghsa-m6gx-rhvj-fh52.md) | CVE-2020-28362 | critical | GHSA-m6gx-rhvj-fh52: Denial of service due to Go CVE-2020-28362 |
| 2020-11-24 | [ghsa-jm5c-rv3w-w83m.md](advisories/ghsa-jm5c-rv3w-w83m.md) | CVE-2020-26242 | high | GHSA-jm5c-rv3w-w83m: Denial of service via `MulMod` |
| 2020-11-24 | [ghsa-69v6-xc2j-r2jf.md](advisories/ghsa-69v6-xc2j-r2jf.md) | CVE-2020-26241 | high | GHSA-69v6-xc2j-r2jf: Shallow copy in the 0x4 precompile could lead to EVM memory corruptio |


## Also in this folder

- [solidity-compiler-bugs.md](solidity-compiler-bugs.md) — 67 known Solidity compiler bugs (canonical `bugs.json`)
- [security-policy/](security-policy/) — go-ethereum and solidity SECURITY.md
