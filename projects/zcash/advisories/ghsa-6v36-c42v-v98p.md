# GHSA-6v36-c42v-v98p: Peer disconnection during a blocked outbound send can abort zebrad

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-6v36-c42v-v98p |
| CVE | none assigned |
| Severity | medium (CVSS 5.9) |
| CWE | n/a |
| Published | 2026-10-22T12:27:28Z |
| Updated | 2026-10-22T12:30:53Z |
| Affected | zebrad < 7.0.0 (patched: 7.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-6v36-c42v-v98p |

## Description (verbatim)

# Peer disconnection during a blocked outbound send can abort zebrad

| Field | Value |
|---|---|
| Severity | Medium |
| CWE | CWE-617 (Reachable Assertion); CWE-362 (Race Condition) |
| Affected versions | zebrad < 7.0.0 |
| Patched versions | zebrad 7.0.0 |
| Reporter | [@SphereDonout](https://github.com/SphereDonout);  [@professorsolderin](https://github.com/professorsolderin), Trail of Bits (independent rediscoveries)|

## Am I affected?

You are affected if all of the following hold:

- You run zebrad 6.4.2 or earlier, or 7.0.0-rc.0.
- You run a release build (the default for published binaries and Docker images), which aborts the process on panic.
- Your node accepts or makes P2P connections to untrusted peers (the default).

The confirmed trigger applies while the node is syncing (more than 1,000 blocks behind the network tip). Other peer-disconnection paths that could reach the same window were not ruled out, so treat every node running an affected version as exposed. Upgrading to 7.0.0 removes the defect on every path.

## Summary

A peer connected to zebrad can, under specific timing, cause the node process to abort. When the peer set disconnects a peer while zebrad is still waiting to write a message to that peer's socket, an internal response handle is dropped without being resolved, and an assertion fires. Release builds use `panic = "abort"`, so the whole process exits. A malicious peer that completes a normal handshake, returns empty replies to block-discovery requests, and stops reading from its socket can create the conditions for this. No consensus, funds, or on-disk state impact is involved; the node recovers on restart.

## Details

Each outbound request to a peer carries a `MustUseClientResponseSender`. Its `Drop` implementation asserts that it was either used or canceled, and only skips the check during global shutdown ([`zebra-network/src/peer/client.rs:323-335`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-network/src/peer/client.rs#L323-L335)). This is a plain `assert!`, so it is active in release builds, and the release profile sets `panic = "abort"` ([`Cargo.toml:311-312`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/Cargo.toml#L311-L312)).

`Connection::handle_client_request` moves the sender into a local variable, then awaits `peer_tx.send(...)` for the request's wire message. Only after the send completes does it store the sender in `State::AwaitingResponse` ([`zebra-network/src/peer/connection.rs:1168-1179`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-network/src/peer/connection.rs#L1168-L1179)). The send is bounded by `REQUEST_TIMEOUT` ([`zebra-network/src/peer/connection/peer_tx.rs:28-33`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-network/src/peer/connection/peer_tx.rs#L28-L33)), and a timeout or send error resolves the sender correctly. Cancellation does not: if the connection task is aborted while the send is pending, the local sender is dropped unresolved. `Connection::shutdown` resolves only a sender already held in `AwaitingResponse` ([`zebra-network/src/peer/connection.rs:1781-1795`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-network/src/peer/connection.rs#L1781-L1795)).

Dropping a `Client` aborts its connection task ([`zebra-network/src/peer/client.rs:589-601`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-network/src/peer/client.rs#L589-L601), [`684-696`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-network/src/peer/client.rs#L684-L696)). While syncing, the peer set counts empty or missing `FindBlocks`/`FindHeaders` replies as stalls ([`zebra-network/src/peer_set/set.rs:174-183`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-network/src/peer_set/set.rs#L174-L183)) and removes a peer after three consecutive stalls ([`zebra-network/src/peer_set/stall_tracker.rs:18`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-network/src/peer_set/stall_tracker.rs#L18), [`set.rs:825-865`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-network/src/peer_set/set.rs#L825-L865)). If that removal happens while the peer's connection is blocked writing to a socket the peer has stopped reading, the assertion fires.

The defect is in the connection's request lifecycle, not in the stall tracker. Any path that drops a `Client` while its connection is suspended in an outbound send has the same effect. The same code has been present in every zebrad release.

## Impact

A successful trigger terminates the zebrad process. The node stops syncing, relaying, and serving RPC until it is restarted. Repeating the trigger can prolong the outage of an individual node. The attacker needs no credentials, only an ordinary post-handshake P2P connection.

Scope limits: exploitation depends on timing (a pending socket write overlapping a peer disconnection), and the confirmed trigger applies only while the node is syncing. There is no consensus, funds, privacy, or persistent state impact.

## Patches

Fixed in zebrad 7.0.0. The connection now owns the response sender for the whole of the send (`Connection::sending_request_tx`), and `Connection::shutdown`, which runs when the connection is dropped, resolves it with an error if the task was cancelled mid-send. A regression test covers cancellation during a parked send. Upgrade to 7.0.0 or later.

## Workarounds

There is no configuration option that removes the trigger. Running zebrad under a process supervisor with automatic restart (for example systemd `Restart=on-failure`, or a container restart policy) limits the outage if the process aborts.

## Credit

Reported by [@SphereDonout](https://github.com/SphereDonout), and independently by [@professorsolderin](https://github.com/professorsolderin).

## References

- [CWE-617: Reachable Assertion](https://cwe.mitre.org/data/definitions/617.html)
- [CWE-362: Race Condition](https://cwe.mitre.org/data/definitions/362.html)
- [Zebra 7.0.0 release notes](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/CHANGELOG.md)
- [`zebra-network/src/peer/client.rs` at v6.4.2](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-network/src/peer/client.rs)
- [`zebra-network/src/peer/connection.rs` at v6.4.2](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-network/src/peer/connection.rs)
- [`zebra-network/src/peer/connection.rs` at v7.0.0 (fix)](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-network/src/peer/connection.rs)

