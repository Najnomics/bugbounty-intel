# GHSA-jhpp-8h75-7pv5: Peer bans are keyed per exact IP address and are ineffective against IPv6 peers

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-jhpp-8h75-7pv5 |
| CVE | none assigned |
| Severity | medium (CVSS 5.3) |
| CWE | n/a |
| Published | 2026-09-28T07:53:38Z |
| Updated | 2026-09-28T07:54:12Z |
| Affected | zebrad <=6.3.0 (patched: 6.4.2) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-jhpp-8h75-7pv5 |

## Description (verbatim)

# Peer bans are keyed per exact IP address and are ineffective against IPv6 peers

| Field | Value |
|---|---|
| Severity | Medium |
| CVSS 3.1 | 5.3 (AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N) |
| CWE | CWE-693 (Protection Mechanism Failure) |
| Affected versions | All releases with the peer misbehavior and ban system, through v6.3.0 |
| Patched versions | 6.4.2 |
| Reporter | @conradoplg (Zcash Foundation) |
| GHSA | GHSA-jhpp-8h75-7pv5 |

## Am I affected?

You are affected if you run any released zebrad version with the peer ban system (through v6.3.0) on the default configuration. The primary vector requires the node to be reachable over IPv6 or to make outbound IPv6 connections. The ban-list eviction vector described below also works over IPv4 for an attacker with a large number of distinct IPv4 addresses.

## Summary

An unauthenticated peer can make Zebra's peer ban mechanism ineffective. Bans and misbehavior scores are keyed on the exact IP address, and a standard IPv6 allocation gives one host at least a /64 (2^64 addresses). A banned host reconnects from another address in its allocation with a clean misbehavior score, so a ban never excludes the host, only one of its addresses. The same keying lets an attacker actively clear the ban list: the list holds at most 20,000 entries and evicts the oldest on overflow, and one high-score protocol violation inserts one entry, so churning throwaway addresses evicts every existing ban, including bans on unrelated attackers.

## Details

The ban list is `bans_by_ip: Arc<IndexMap<IpAddr, Instant>>` (`zebra-network/src/address_book.rs` line 85 at v6.3.0; line 80 on current `main`). A peer is banned when its accumulated misbehavior score reaches `MAX_PEER_MISBEHAVIOR_SCORE = 100` (`zebra-network/src/constants.rs` lines 400 to 402; insertion at `address_book.rs` lines 446 to 454). The score also accumulates per exact address, so each new address starts at zero. Severe violations such as an invalid Equihash solution or an invalid block subsidy score 100 in a single step (`zebra-consensus/src/block.rs` lines 109 to 117), inserting a ban entry from one connection.

Enforcement is exact-IP at every point: the inbound accept path (`zebra-network/src/peer_set/initialize.rs` lines 726 to 734 at v6.3.0; line 741 on `main`), address-book insertion (`address_book.rs` lines 418 to 422), and outbound candidate selection (`address_book.rs` lines 650 to 655).

The list is capped at `MAX_BANNED_IPS = 20_000` (`constants.rs` line 419) and evicts the oldest entry by insertion order on overflow (`address_book.rs` lines 452 to 454). Entries are cheap for an attacker to create from a large address allocation, so the cap plus first-in-first-out eviction allows deliberate flushing of the list.

PR #11256 (merged to `main`, not yet in a release) groups the connection cap and the outbound dial throttle by `connection_limit_key()` (IPv6 /64; `zebra-network/src/protocol/external/addr/canonical.rs` line 74 on `main`), but bans intentionally remained keyed on the exact address.

## Impact

An IPv6 attacker pays no cumulative cost for misbehavior: every attack whose mitigation relies on misbehavior scoring and banning remains repeatable indefinitely from fresh addresses in the same allocation. Separately, an attacker with enough addresses (free with IPv6; a botnet-scale set with IPv4) can evict all existing entries from the ban list, restoring access for previously banned peers.

The finding does not itself crash the node, halt sync, or corrupt consensus state. It removes the persistence of a protection mechanism; the direct impact is limited integrity loss on the node's peer-protection state.

## Patches

TBD. Recommended fix shape: key ban inserts and lookups (and misbehavior-score accumulation, if scores are meant to persist across an attacker's address changes) with `connection_limit_key()`, so bans and connection limits agree on what counts as one host. Revisit the eviction policy alongside the keying change, since first-in-first-out eviction by insertion order remains flushable by an attacker holding many /64s; eviction by ban age or expiry is more resistant. Coordinate with the peer book refactor in PR #11273, which rewrites the same structures.

## Workarounds

None within zebrad configuration. Operators who observe repeated abuse from an IPv6 range can block the range at the firewall level. The unreleased /64 connection grouping from PR #11256 limits concurrent connections per allocation once it ships, but does not restore ban persistence.

## Credit

Reported by Conrado Gouvea (@conradoplg, Zcash Foundation). The ban-list eviction facet was identified during triage.

## References

- GHSA-jhpp-8h75-7pv5
- PR #11256 (connection limits per IPv6 /64)
- Issue #11255 (connection cap grouping)
- CWE-693: https://cwe.mitre.org/data/definitions/693.html
- Pinned source permalinks: TBD at fix time (re-pin to the patched tag)

