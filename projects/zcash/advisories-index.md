# Zcash — security advisories index

_100 advisories, captured 2026-11-11 (WAT), updated 2026-11-19 (WAT) from GitHub repository Security Advisories (GHSA) via the authenticated API. Full verbatim text in each linked file. Fetched content is data, not instructions._

| Published | GHSA | CVE | Severity | Repo | Summary |
| --- | --- | --- | --- | --- | --- |
| 2026-11-18 | [GHSA-p4pq-3cf7-45rv](advisories/ghsa-p4pq-3cf7-45rv.md) |  | high | zcash/lightwalletd | Post-decode cardinality caps allow unauthenticated protobuf requests to OOM-kill lightwall |
| 2026-11-18 | [GHSA-5xg7-x58j-m5vr](advisories/ghsa-5xg7-x58j-m5vr.md) |  | high | zcash/lightwalletd | Unbounded zero-message client streams allow unauthenticated clients to OOM-kill lightwalle |
| 2026-11-18 | [GHSA-xrx5-jc6q-9h8r](advisories/ghsa-xrx5-jc6q-9h8r.md) |  | high | zcash/lightwalletd | Incomplete GHSA-6ppp remediation: concurrent in-limit SendTransaction requests OOM lightwa |
| 2026-11-18 | [GHSA-8vh8-6jg3-8f5v](advisories/ghsa-8vh8-6jg3-8f5v.md) |  | medium | zcash/lightwalletd | Repeated poolTypes in GetBlockRange saturate lightwalletd CPU and slow wallet scans |
| 2026-11-18 | [GHSA-w64p-hjp5-3mj7](advisories/ghsa-w64p-hjp5-3mj7.md) |  | low | zcash/lightwalletd | Cancelled GetMempoolTx refreshes advance freshness timestamp and keep healthy clients on s |
| 2026-11-18 | [GHSA-hp3q-vfr4-v8m6](advisories/ghsa-hp3q-vfr4-v8m6.md) |  | high | zcash/lightwalletd | GetMempoolStream Global Mutex Held During Uncancellable RPC |
| 2026-11-18 | [GHSA-pp3p-5vmm-3cvw](advisories/ghsa-pp3p-5vmm-3cvw.md) |  | low | zcash/lightwalletd | Unchecked 32-byte slice-to-array conversion in `hash32.FromSlice` lets one unauthenticated |
| 2026-11-18 | [GHSA-pj5c-jx29-gmxr](advisories/ghsa-pj5c-jx29-gmxr.md) |  | medium | zcash/lightwalletd | A cancelled GetMempoolStream request hides new mempool transactions from every client unti |
| 2026-11-18 | [GHSA-jcrq-vv43-968c](advisories/ghsa-jcrq-vv43-968c.md) |  | low | zcash/lightwalletd | Unhandled slice index panic in `Block.GetHeight()` when a block contains zero transactions |
| 2026-11-18 | [GHSA-4wjx-vhhv-vc8c](advisories/ghsa-4wjx-vhhv-vc8c.md) |  | high | zcash/lightwalletd | Zero-message `GetTaddressBalanceStream` calls retain unbounded lightwalletd handlers and g |
| 2026-11-18 | [GHSA-w24w-x7vw-f2w8](advisories/ghsa-w24w-x7vw-f2w8.md) |  | medium | zcash/lightwalletd | Timeout-free metrics HTTP listener permits Slowloris descriptor exhaustion and denial of w |
| 2026-11-18 | [GHSA-j79f-98gc-33jw](advisories/ghsa-j79f-98gc-33jw.md) |  | medium | zcash/lightwalletd | lightwalletd metrics listener exposes command-line RPC passwords via `/debug/vars` |
| 2026-11-18 | [GHSA-gq9m-j9cv-6w9p](advisories/ghsa-gq9m-j9cv-6w9p.md) |  | high | zcash/lightwalletd | Five HTTP/2 denial-of-service issues in the `golang.org/x/net` dependency |
| 2026-11-18 | [GHSA-x943-ghgq-v675](advisories/ghsa-x943-ghgq-v675.md) |  | medium | zcash/lightwalletd | Public transparent-address lists repeatedly compile a constant regexp and degrade unrelate |
| 2026-11-18 | [GHSA-4q7w-cx94-55pc](advisories/ghsa-4q7w-cx94-55pc.md) |  | low | zcash/librustzcash | sighash computation has quadratic complexity |
| 2026-11-17 | [GHSA-2wx4-g5cf-32pf](advisories/ghsa-2wx4-g5cf-32pf.md) |  | medium | ZcashFoundation/zebra | Anchor Error Masks Halo2 Batch Poisoning and Evades Peer Scoring |
| 2026-11-17 | [GHSA-hvw5-x88g-2q8w](advisories/ghsa-hvw5-x88g-2q8w.md) |  | medium | ZcashFoundation/zebra | Checkpoint verifier admits and queues blocks by a coinbase height a peer can rewrite witho |
| 2026-11-17 | [GHSA-423j-2vj4-j5x4](advisories/ghsa-423j-2vj4-j5x4.md) |  | medium | ZcashFoundation/zebra | The mempool dispatches transactions above the standard sigop limit to script verification |
| 2026-11-17 | [GHSA-7jvw-68q7-xfh4](advisories/ghsa-7jvw-68q7-xfh4.md) |  | medium | ZcashFoundation/zebra | A forged block body queued in the state gets the next honest peer that serves the same blo |
| 2026-11-17 | [GHSA-8qxv-5f2c-452c](advisories/ghsa-8qxv-5f2c-452c.md) |  | high | ZcashFoundation/zebra | Unbounded retention of unverifiable blocks in the checkpoint and orphan queues |
| 2026-11-17 | [GHSA-vw2c-5w35-x5q6](advisories/ghsa-vw2c-5w35-x5q6.md) |  | high | ZcashFoundation/zebra | One already known hash anywhere past the first unknown hash in a FindBlocks answer aborts  |
| 2026-11-17 | [GHSA-hj54-2mfv-4xg8](advisories/ghsa-hj54-2mfv-4xg8.md) |  | high | ZcashFoundation/zebra | One-block balance-query amplification can OOM Zebra through public wallet requests |
| 2026-11-17 | [GHSA-g9rc-89v4-hhvf](advisories/ghsa-g9rc-89v4-hhvf.md) |  | high | ZcashFoundation/zebra | A single peer can stop initial sync indefinitely by serving blocks with a rewritten coinba |
| 2026-11-17 | [GHSA-m44m-9r8r-r64j](advisories/ghsa-m44m-9r8r-r64j.md) |  | high | ZcashFoundation/zebra | Permanent Checkpoint Sync Halt via Forged Child Block in `StateService::queue_and_commit_t |
| 2026-11-17 | [GHSA-j8gf-c4rj-6jv5](advisories/ghsa-j8gf-c4rj-6jv5.md) |  | high | ZcashFoundation/zebra | Transparent-output-dense blocks exhaust node memory through per-chain copies of the non-fi |
| 2026-10-27 | [GHSA-xq7v-jj38-pcwr](advisories/ghsa-xq7v-jj38-pcwr.md) |  | high | zcash/lightwalletd | Unauthenticated concurrent GetBlockRange streams can OOM-terminate lightwalletd |
| 2026-10-22 | [GHSA-7jp4-mq53-4cvq](advisories/ghsa-7jp4-mq53-4cvq.md) |  | high | ZcashFoundation/zebra | Mempool coinbase-maturity check does quadratic work per transaction, letting one peer pin  |
| 2026-10-22 | [GHSA-5h3r-fpmj-483w](advisories/ghsa-5h3r-fpmj-483w.md) |  | medium | ZcashFoundation/zebra | Lock-time mempool rejection bans honest peers that are one block ahead |
| 2026-10-22 | [GHSA-j4cw-58mj-7w6v](advisories/ghsa-j4cw-58mj-7w6v.md) |  | high | ZcashFoundation/zebra | Uncached ZIP-244 transparent sighash digests let one invalid transaction occupy the verifi |
| 2026-10-22 | [GHSA-jq45-ghw5-v37x](advisories/ghsa-jq45-ghw5-v37x.md) |  | high | ZcashFoundation/zebra | Transparent script verification failures are never scored, on the mempool, block-sync and  |
| 2026-10-22 | [GHSA-6v36-c42v-v98p](advisories/ghsa-6v36-c42v-v98p.md) |  | medium | ZcashFoundation/zebra | Peer disconnection during a blocked outbound send can abort zebrad |
| 2026-10-22 | [GHSA-2w9f-9wx8-f5c8](advisories/ghsa-2w9f-9wx8-f5c8.md) |  | high | ZcashFoundation/zebra | A sync restart during a failed checkpoint commit loses the verifier rewind and stalls chec |
| 2026-10-22 | [GHSA-9hq5-pfgc-cx5h](advisories/ghsa-9hq5-pfgc-cx5h.md) |  | high | ZcashFoundation/zebra | Forged checkpoint block body stalls initial sync until restart |
| 2026-09-28 | [GHSA-3c94-hf7p-g5mf](advisories/ghsa-3c94-hf7p-g5mf.md) |  | medium | ZcashFoundation/zebra | Same-hash block body forces full proof verification with no peer penalty |
| 2026-09-28 | [GHSA-4f6v-mj46-gxg3](advisories/ghsa-4f6v-mj46-gxg3.md) |  | low | ZcashFoundation/zebra | Coinbase scriptSig rewrite drops a gossiped block on the inbound path without penalizing t |
| 2026-09-28 | [GHSA-jhpp-8h75-7pv5](advisories/ghsa-jhpp-8h75-7pv5.md) |  | medium | ZcashFoundation/zebra | Peer bans are keyed per exact IP address and are ineffective against IPv6 peers |
| 2026-09-25 | [GHSA-h5rr-8pqv-grp9](advisories/ghsa-h5rr-8pqv-grp9.md) |  | high | ZcashFoundation/zebra | Unauthenticated peer can crash zebrad by sending a version 6 transaction whose consensus b |
| 2026-08-27 | [GHSA-932p-ww36-57vg](advisories/ghsa-932p-ww36-57vg.md) |  | medium | zcash/lightwalletd | Public `GetAddressUtxos` requests can overfetch backend UTXOs and degrade normal wallet re |
| 2026-08-17 | [GHSA-h8m8-844p-v3m9](advisories/ghsa-h8m8-844p-v3m9.md) |  | medium | ZcashFoundation/zebra | Valid one-hash FindBlocks response discarded, causing false close-to-tip status and a fals |
| 2026-08-17 | [GHSA-2p4c-3q4q-p463](advisories/ghsa-2p4c-3q4q-p463.md) |  | high | ZcashFoundation/zebra | Uncapped shielded verification cost lets peer-pushed V6 transactions stall block verificat |
| 2026-08-11 | [GHSA-8hh2-hrf2-cqf4](advisories/ghsa-8hh2-hrf2-cqf4.md) |  | medium | ZcashFoundation/zebra | Invalid gossiped blocks bypass peer misbehavior scoring |
| 2026-08-11 | [GHSA-qhr3-cvch-5fh2](advisories/ghsa-qhr3-cvch-5fh2.md) |  | medium | ZcashFoundation/zebra | Far-ahead FindBlocks hashes cause Zebra to ban honest peers that serve requested blocks |
| 2026-08-11 | [GHSA-g95h-hw6g-pvgv](advisories/ghsa-g95h-hw6g-pvgv.md) |  | high | ZcashFoundation/zebra | Coinbase scriptSig rewrite drops a required block during sync without penalizing the suppl |
| 2026-08-05 | [GHSA-m7j5-wvx3-qj6j](advisories/ghsa-m7j5-wvx3-qj6j.md) |  | low | zcash/lightwalletd | lightwalletd can serve old-fork and new-fork blocks in one live GetBlockRange response dur |
| 2026-07-31 | [GHSA-pwwg-h8q5-hq28](advisories/ghsa-pwwg-h8q5-hq28.md) |  | low | zcash/lightwalletd | lightwalletd cache can stitch old-fork and new-chain blocks after restart |
| 2026-07-30 | [GHSA-9p9r-mggr-8q9g](advisories/ghsa-9p9r-mggr-8q9g.md) |  | medium | zcash/lightwalletd | lightwalletd GetMempoolTx holds shared mempool mutex across client-controlled streaming se |
| 2026-07-30 | [GHSA-f9pw-q493-7qvh](advisories/ghsa-f9pw-q493-7qvh.md) |  | medium | zcash/lightwalletd | Deadlock and Uncontrolled Resource Consumption in github.com/zcash/lightwalletd |
| 2026-07-28 | [GHSA-9x94-88pq-6v7h](advisories/ghsa-9x94-88pq-6v7h.md) |  | high | zcash/lightwalletd | Lightwalletd cancelled block-range streams leak worker goroutines |
| 2026-07-28 | [GHSA-4x4j-5972-376r](advisories/ghsa-4x4j-5972-376r.md) |  | high | zcash/lightwalletd | lightwalletd GetMempoolTx can crash a targeted node when a mempool transaction disappears |
| 2026-07-28 | [GHSA-4hp3-3494-3f2m](advisories/ghsa-4hp3-3494-3f2m.md) |  | medium | zcash/lightwalletd | lightwalletd GetMempoolTx large exclude suffix lists amplify CPU and heap under the method |
| 2026-07-28 | [GHSA-6ppp-r2gc-9q6v](advisories/ghsa-6ppp-r2gc-9q6v.md) |  | high | zcash/lightwalletd | lightwalletd SendTransaction oversized raw transactions can OOM a targeted node before bac |
| 2026-07-28 | [GHSA-q2c2-hpp9-58hm](advisories/ghsa-q2c2-hpp9-58hm.md) |  | high | zcash/lightwalletd | lightwalletd GetTreeState oversized block hashes can OOM a targeted node before backend re |
| 2026-07-26 | [GHSA-x4m7-3gpp-xc36](advisories/ghsa-x4m7-3gpp-xc36.md) |  | high | zcash/lightwalletd | lightwalletd transparent-address gRPC resource-exhaustion DoS |
| 2026-07-22 | [GHSA-x93j-mj2f-q338](advisories/ghsa-x93j-mj2f-q338.md) |  | medium | ZcashFoundation/zebra | Poisoned blocks can delay download of valid blocks (SentHashes lockout on the KnownBlock p |
| 2026-07-19 | [GHSA-5h96-xw2v-jxgq](advisories/ghsa-5h96-xw2v-jxgq.md) |  | high | zcash/lightwalletd | Goroutine Leak in `GetBlockRange` |
| 2026-07-19 | [GHSA-qgw7-x3x7-p35x](advisories/ghsa-qgw7-x3x7-p35x.md) |  | high | zcash/zcash | Unpenalized remote DoS via malformed P2P tx/block messages |
| 2026-07-19 | [GHSA-ghc3-g8w4-whf9](advisories/ghsa-ghc3-g8w4-whf9.md) |  | critical | zcash/zcash | Orchard Action circuit soundness failure (under-constrained base in halo2_gadgets) enables |
| 2026-07-17 | [GHSA-95m2-vx53-v2jw](advisories/ghsa-95m2-vx53-v2jw.md) |  | low | ZcashFoundation/zebra | Block template omits header and transaction-count size, allowing oversized invalid blocks  |
| 2026-07-17 | [GHSA-g7c4-2w6c-cr3r](advisories/ghsa-g7c4-2w6c-cr3r.md) |  | medium | ZcashFoundation/zebra | Unattributed pushed-transaction verification failures allow sustained batch-verification p |
| 2026-07-17 | [GHSA-4g24-549m-hp75](advisories/ghsa-4g24-549m-hp75.md) |  | medium | ZcashFoundation/zebra | Quadratic transparent value check in block contextual verification |
| 2026-07-17 | [GHSA-8gxx-hc65-vv82](advisories/ghsa-8gxx-hc65-vv82.md) |  | medium | ZcashFoundation/zebra | Potential Chain Stall via stale `parent_error_map` |
| 2026-07-13 | [GHSA-qvwc-hc2r-82qv](advisories/ghsa-qvwc-hc2r-82qv.md) |  | medium | zcash/zcash | Incomplete fix for GHSA-rpcw-q5mr-gq35: NU5 block body poisoning via bad-blk-sigops |
| 2026-07-13 | [GHSA-382w-958v-m5jr](advisories/ghsa-382w-958v-m5jr.md) |  | medium | zcash/zcash | NU5+ block-body poisoning via the `bad-blk-length` rejection path |
| 2026-07-13 | [GHSA-2x4w-pxqw-58v9](advisories/ghsa-2x4w-pxqw-58v9.md) |  | low | zcash/zcash | Unbounded Orchard proofs can be used to impose large bandwidth and storage costs without p |
| 2026-07-13 | [GHSA-78pp-mc9g-g4mw](advisories/ghsa-78pp-mc9g-g4mw.md) |  | high | zcash/zcash | zcashd repeatedly persists the same invalid pool-delta block without caching it as invalid |
| 2026-07-13 | [GHSA-84j3-rw4c-gqmj](advisories/ghsa-84j3-rw4c-gqmj.md) |  | high | ZcashFoundation/zebra | Peer-Advertised Mempool Transactions Can Stall Tokio Workers via Synchronous Transparent S |
| 2026-07-03 | [GHSA-x6v8-c2xp-928m](advisories/ghsa-x6v8-c2xp-928m.md) |  | medium | ZcashFoundation/zebra | getblock verbosity 2 on a side-chain block panics the node via negative-confirmations u32  |
| 2026-07-03 | [GHSA-m9xx-8rcj-vmgp](advisories/ghsa-m9xx-8rcj-vmgp.md) |  | medium | ZcashFoundation/zebra | Direct P2P tx messages bypass per-peer mempool admission accounting |
| 2026-06-15 | [GHSA-ww9q-8r59-xv46](advisories/ghsa-ww9q-8r59-xv46.md) | CVE-2026-54496 | critical | ZcashFoundation/zebra | Missing copy constraint in halo2_gadgets variable-base scalar multiplication allows under- |
| 2026-06-01 | [GHSA-2prc-cj5x-4443](advisories/ghsa-2prc-cj5x-4443.md) |  | critical | ZcashFoundation/zebra | P2SH Sigop Undercount Not Correctly Fixed |
| 2026-05-29 | [GHSA-63wg-wjjj-7cp8](advisories/ghsa-63wg-wjjj-7cp8.md) | CVE-2026-52829 | high | ZcashFoundation/zebra | IPv4-Mapped Mempool Misbehavior Update Aborts Zebra Address Book |
| 2026-05-29 | [GHSA-hhm7-qrv5-h4r6](advisories/ghsa-hhm7-qrv5-h4r6.md) | CVE-2026-52739 | medium | ZcashFoundation/zebra | Repeated Non-Finalized Shielded Transaction Aborts Zebra Before Duplicate-Nullifier Reject |
| 2026-05-29 | [GHSA-w834-cf6p-9m9w](advisories/ghsa-w834-cf6p-9m9w.md) | CVE-2026-52738 | high | ZcashFoundation/zebra | Finalized address balance credit-first overflow on consensus-valid blocks |
| 2026-05-29 | [GHSA-gvjc-3w7c-92jx](advisories/ghsa-gvjc-3w7c-92jx.md) | CVE-2026-52737 | medium | ZcashFoundation/zebra | Sync restart poisoning from single unauthenticated peer via above-lookahead block |
| 2026-05-29 | [GHSA-4m69-67m6-prqp](advisories/ghsa-4m69-67m6-prqp.md) | CVE-2026-52736 | high | ZcashFoundation/zebra | Block suppression via NU5 same-header body poisoning of sent-hash cache |
| 2026-05-29 | [GHSA-h72h-ppcx-998p](advisories/ghsa-h72h-ppcx-998p.md) |  | medium | ZcashFoundation/zebra | Pre-handshake buffer capacity reservation based on attacker-claimed body length |
| 2026-05-29 | [GHSA-gf9r-m956-97qx](advisories/ghsa-gf9r-m956-97qx.md) | CVE-2026-52735 | critical | ZcashFoundation/zebra | Consensus divergence via P2SH sigop undercount in pure-Rust disabled-opcode parser |
| 2026-05-29 | [GHSA-65jj-fmw8-468q](advisories/ghsa-65jj-fmw8-468q.md) | CVE-2026-52734 | medium | ZcashFoundation/zebra | Unbounded memory leak in mempool download pipeline via timeout path cancel_handles retenti |
| 2026-05-29 | [GHSA-2gf8-q9rr-jq3h](advisories/ghsa-2gf8-q9rr-jq3h.md) | CVE-2026-52733 | medium | ZcashFoundation/zebra | Persistent on-disk corruption of Sapling/Orchard subtree roots after chain fork via pop_ti |
| 2026-05-29 | [GHSA-4fc2-h7jh-287c](advisories/ghsa-4fc2-h7jh-287c.md) | CVE-2026-52732 | medium | ZcashFoundation/zebra | Mempool transaction admission denial via single-peer inbound queue saturation |
| 2026-05-29 | [GHSA-c8w6-x74f-vmg3](advisories/ghsa-c8w6-x74f-vmg3.md) |  | medium | ZcashFoundation/zebra | Full node denial of service via crafted Sapling receiver in z_listunifiedreceivers |
| 2026-05-29 | [GHSA-443g-gwgp-49x4](advisories/ghsa-443g-gwgp-49x4.md) |  | low | ZcashFoundation/zebra | getblocks/getheaders locator CPU amplification via uncapped vector length |
| 2026-05-29 | [GHSA-qv2r-v3mx-f4pf](advisories/ghsa-qv2r-v3mx-f4pf.md) | CVE-2026-52731 | medium | ZcashFoundation/zebra | Full node denial of service via non-ASCII LongPollId in getblocktemplate |
| 2026-05-08 | [GHSA-3jg6-49c6-q99v](advisories/ghsa-3jg6-49c6-q99v.md) |  | medium | zcash/zcash | zcashd Normalizes Malformed V4 Sapling valueBalance Encodings That Zebra Rejects |
| 2026-05-08 | [GHSA-rpcw-q5mr-gq35](advisories/ghsa-rpcw-q5mr-gq35.md) |  | medium | zcash/zcash | Auth Data Body Poisoning in NU5+ Block Ingestion |
| 2026-05-08 | [GHSA-fqr9-fxpx-rfpf](advisories/ghsa-fqr9-fxpx-rfpf.md) |  | critical | zcash/zcash | zcashd ConnectBlock use-after-free: stack destruction order frees PrecomputedTransactionDa |
| 2026-05-05 | [GHSA-h9hm-m2xj-4rq9](advisories/ghsa-h9hm-m2xj-4rq9.md) | CVE-2026-44499 | critical | ZcashFoundation/zebra | Permanent Block Discovery Halt via Gossip Queue Saturation and Syncer Poisoning |
| 2026-05-04 | [GHSA-pvmv-cwg8-v6c8](advisories/ghsa-pvmv-cwg8-v6c8.md) |  | critical | ZcashFoundation/zebra | Zebra v4.4.0 still accepts V5 SIGHASH_SINGLE without a corresponding output |
| 2026-05-02 | [GHSA-cwfq-rfcr-8hmp](advisories/ghsa-cwfq-rfcr-8hmp.md) |  | critical | ZcashFoundation/zebra | Zebra Transparent SIGHASH_SINGLE Corresponding-Output Handling Diverges From zcashd |
| 2026-05-02 | [GHSA-gq4h-3grw-2rhv](advisories/ghsa-gq4h-3grw-2rhv.md) | CVE-2026-44497 | critical | ZcashFoundation/zebra | Consensus Divergence in Transparent Sighash Hash-Type Handling due to Stale Buffer |
| 2026-05-02 | [GHSA-438q-jx8f-cccv](advisories/ghsa-438q-jx8f-cccv.md) | CVE-2026-44500 | medium | ZcashFoundation/zebra | Allocation Amplification in Inbound Network Deserializers |
| 2026-05-02 | [GHSA-jv4h-j224-23cc](advisories/ghsa-jv4h-j224-23cc.md) | CVE-2026-44498 | critical | ZcashFoundation/zebra | Block Validator Undercounts Coinbase and P2SH Sigops |
| 2026-04-17 | [GHSA-8m29-fpq5-89jj](advisories/ghsa-8m29-fpq5-89jj.md) | CVE-2026-41583 | critical | ZcashFoundation/zebra | Consensus Divergence in Transparent Sighash Hash-Type Handling |
| 2026-04-17 | [GHSA-29x4-r6jv-ff4w](advisories/ghsa-29x4-r6jv-ff4w.md) |  | medium | ZcashFoundation/zebra | Denial of Service via Interrupted JSON-RPC Requests from Authenticated Clients |
| 2026-04-17 | [GHSA-452v-w3gx-72wg](advisories/ghsa-452v-w3gx-72wg.md) | CVE-2026-41584 | critical | ZcashFoundation/zebra | rk Identity Point Panic in Transaction Verification |
| 2026-04-17 | [GHSA-xr93-pcq3-pxf8](advisories/ghsa-xr93-pcq3-pxf8.md) | CVE-2026-40881 | medium | ZcashFoundation/zebra | addr/addrv2 Deserialization Resource Exhaustion |
| 2026-04-17 | [GHSA-xvj8-ph7x-65gf](advisories/ghsa-xvj8-ph7x-65gf.md) | CVE-2026-40880 | high | ZcashFoundation/zebra | Cached Mempool Verification Bypasses Consensus Rules for Ahead-of-Tip Blocks |
| 2026-03-27 | [GHSA-qp6f-w4r3-h8wg](advisories/ghsa-qp6f-w4r3-h8wg.md) | CVE-2026-34202 | critical | ZcashFoundation/zebra | CVE-2026-34202: Remote Denial of Service via Crafted V5 Transactions |
| 2026-03-27 | [GHSA-3vmh-33xr-9cqh](advisories/ghsa-3vmh-33xr-9cqh.md) | CVE-2026-34377 | high | ZcashFoundation/zebra | CVE-2026-34377: Consensus Failure via Crafted V5 Authorization Data |
| 2025-09-03 | [GHSA-wgq8-vr6r-mqxm](advisories/ghsa-wgq8-vr6r-mqxm.md) | CVE-2025-58359 | medium | ZcashFoundation/frost | frost-core: refresh shares with smaller min_signers will reduce security of group |
