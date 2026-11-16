# Crypto Primitives

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **76** (see `harness/findings.jsonl`)._

## Method / findings in sources

- **frost-core: refresh shares with smaller min_signers will reduce security of group** — ### Impact It was not clear that it is not possible to change `min_signers` (i.e. the threshold) with the refresh share functionality (`frost_core::keys::refresh` module). Using a smaller value would not decrease the threshold, and attempts to sign using a smaller threshold would fail. Additionally, after refreshing the shares with a smaller thresh Source: [`projects/zcash/advisories/ghsa-wgq8-vr6r-mqxm.md`](../../projects/zcash/advisories/ghsa-wgq8-vr6r-mqxm.md).
- **See https://docs.rs/rustsec/latest/rustsec/advisory/enum.Category.html** — As seen in the implementation of decrypt_in_place_detached for AES GCM, if the tag verification fails, an error is returned. Because the decryption of the ciphertext is done in place, the plaintext contents are now exposed via buffer. This should ideally not be the case - as noted in page 17 of NIST's publication Recommendation for Block Cipher Mod Source: [`projects/crypto/advisories/crates-aes-gcm-rustsec-2023-0096.md`](../../projects/crypto/advisories/crates-aes-gcm-rustsec-2023-0096.md).
- **Peer bans are keyed per exact IP address and are ineffective against IPv6 peers** — # Peer bans are keyed per exact IP address and are ineffective against IPv6 peers | Field | Value | |---|---| | Severity | Medium | | CVSS 3.1 | 5.3 (AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N) | | CWE | CWE-693 (Protection Mechanism Failure) | | Affected versions | All releases with the peer misbehavior and ban system, through v6.3.0 | | Patched versions Source: [`projects/zcash/advisories/ghsa-jhpp-8h75-7pv5.md`](../../projects/zcash/advisories/ghsa-jhpp-8h75-7pv5.md).
- **rustls-pemfile is unmaintained** — The rustls-pemfile crate is no longer maintained. The repository has been archived since August 2025, and users are encouraged to depend directly on the underlying PEM parsing code included in rustls-pki-types since 1.9.0. The latest version of rustls-pemfile is in fact a thin wrapper around the same code used in rustls-pki-types, so migrating shou Source: [`projects/crypto/advisories/crates-rustls-pemfile-rustsec-2025-0134.md`](../../projects/crypto/advisories/crates-rustls-pemfile-rustsec-2025-0134.md).
- **Unsound API in `secp256k1` allows use-after-free and invalid deallocation from safe code** — url = "https://github.com/rust-bitcoin/rust-secp256k1/issues/543" references = ["https://github.com/rust-bitcoin/rust-secp256k1/pull/548"] informational = "unsound" categories = ["memory-corruption"] keywords = ["use-after-free", "unsound-api", "invalid-free"] aliases = ["GHSA-969w-q74q-9j8v"] Source: [`projects/crypto/advisories/crates-secp256k1-rustsec-2022-0070.md`](../../projects/crypto/advisories/crates-secp256k1-rustsec-2022-0070.md).
- **Marvin Attack: potential key recovery through timing sidechannels** — Due to a non-constant-time implementation, information about the private key is leaked through timing information which is observable over the network. An attacker may be able to use that information to recover the key. Source: [`projects/crypto/advisories/crates-rsa-rustsec-2023-0071.md`](../../projects/crypto/advisories/crates-rsa-rustsec-2023-0071.md).
- **Optional: metadata which narrows the scope of what this advisory affects** — # Optional: metadata which narrows the scope of what this advisory affects [affected.functions] "rand_core::le::read_u32_into" = ["< 0.6.2, >= 0.6.0"] "rand_core::le::read_u64_into" = ["< 0.6.2, >= 0.6.0"] Source: [`projects/crypto/advisories/crates-rand-core-rustsec-2021-0023.md`](../../projects/crypto/advisories/crates-rand-core-rustsec-2021-0023.md).
- **Four unique double-free vulnerabilities triggered via safe APIs** — url = "https://github.com/LiquidityC/slice_ring_buffer/issues/12" categories = ["memory-corruption"] keywords = ["memory-safety", "double-free"] aliases = ["GHSA-7mcq-f592-pf7v"] Source: [`projects/crypto/advisories/crates-slice-ring-buffer-rustsec-2025-0044.md`](../../projects/crypto/advisories/crates-slice-ring-buffer-rustsec-2025-0044.md).
- **Incorrect Output of Incremental Portable SHAKE API** — [affected.functions] "libcrux_sha3::portable::incremental::Shake128Xof::squeeze" = [ "<= 0.0.7" ] "libcrux_sha3::portable::incremental::Shake256Xof::squeeze" = [ "<= 0.0.7" ] Source: [`projects/crypto/advisories/crates-libcrux-sha3-rustsec-2026-0074.md`](../../projects/crypto/advisories/crates-libcrux-sha3-rustsec-2026-0074.md).
- **generichash::Digest::eq always return true** — [affected.functions] "sodiumoxide::crypto::generichash::Digest::eq" = ["< 0.2.5, >= 0.2.0"] "sodiumoxide::crypto::generichash::Digest::ne" = ["< 0.2.5, >= 0.2.0"] Source: [`projects/crypto/advisories/crates-sodiumoxide-rustsec-2019-0026.md`](../../projects/crypto/advisories/crates-sodiumoxide-rustsec-2019-0026.md).
- **`rsa-export` is unmaintained** — This crate has been deprecated in favour of using the native support for exporting RSA keys into the standard PEM format. See [docs.rs documentation]. Source: [`projects/crypto/advisories/crates-rsa-export-rustsec-2024-0333.md`](../../projects/crypto/advisories/crates-rsa-export-rustsec-2024-0333.md).
- **Double free / use-after-free in `Consumer::skip` and `Consumer::clear` when an element's `Drop` panics** — [affected.functions] "ringbuf::traits::consumer::Consumer::skip" = ["< 0.5.2"] "ringbuf::traits::consumer::Consumer::clear" = ["< 0.5.2"] Source: [`projects/crypto/advisories/crates-ringbuf-rustsec-2026-0293.md`](../../projects/crypto/advisories/crates-ringbuf-rustsec-2026-0293.md).
- **smartstring is unmaintained** — The smartstring crate is unmaintained; all versions are affected. The GitHub repository was archived by the owner on 2026-05-03. Source: [`projects/crypto/advisories/crates-smartstring-rustsec-2026-0249.md`](../../projects/crypto/advisories/crates-smartstring-rustsec-2026-0249.md).
- **Ambiguous challenge derivation** — package = "paillier-zk" date = "2024-07-18" url = "https://github.com/dfns/paillier-zk/pull/49" categories = ["crypto-failure"] Source: [`projects/crypto/advisories/crates-paillier-zk-rustsec-2024-0391.md`](../../projects/crypto/advisories/crates-paillier-zk-rustsec-2024-0391.md).
- **Auto-Reseeding HMAC-DRBG could panic for some output lengths** — url = "https://github.com/celabshq/libcrux/pull/1558" cvss = "CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:N/VI:N/VA:H/SC:N/SI:N/SA:N" Source: [`projects/crypto/advisories/crates-libcrux-hmac-drbg-rustsec-2026-0329.md`](../../projects/crypto/advisories/crates-libcrux-hmac-drbg-rustsec-2026-0329.md).
- **Unaligned memory access** — [affected.functions] "rand_core::BlockRng::fill_bytes" = ["< 0.4.2"] "rand_core::BlockRng::next_u64" = ["< 0.4.2"] Source: [`projects/crypto/advisories/crates-rand-core-rustsec-2019-0035.md`](../../projects/crypto/advisories/crates-rand-core-rustsec-2019-0035.md).
- **BLAKE2b produces wrong tag when using `reset()` with a different-length key** — [affected.functions] "orion::hazardous::mac::blake2b::Blake2b::reset" = ["< 0.17.16", "< 0.18.1", ">= 0.12.0"] Source: [`projects/crypto/advisories/crates-orion-rustsec-2026-0428.md`](../../projects/crypto/advisories/crates-orion-rustsec-2026-0428.md).
- **rand_os crate is unmaintained** — The `rand_os` crate is deprecated and no longer actively maintained, as `OsRng` is now part of `rand_core`. Source: [`projects/crypto/advisories/crates-rand-os-rustsec-2025-0124.md`](../../projects/crypto/advisories/crates-rand-os-rustsec-2025-0124.md).

## Prior harness notes (retained)

_Retained from earlier curated harness file; still cites local sources._

## Detection signals
- Nonce / IV reuse in AES-GCM, ChaCha20-Poly1305, or ECDSA/Ed25519.
- Weak or predictable RNG seeding.
- Padding-oracle-shaped APIs (error distinguishes padding vs MAC).
- Signature malleability (ECDSA s-value, Ed25519 cofactor).
- Missing point validation / bad curves / twist attacks.
- Timing-variable comparisons on secrets (`subtle` / constant-time failures).
- ZK: underconstrained signals, missing range/boolean constraints, verifier free/replay branches.

## Sources (full text)
- [`projects/crypto/advisories-index.md`](../../projects/crypto/advisories-index.md) — 76 RustSec crypto advisories (aes-gcm, chacha20, curve25519-dalek, ed25519-dalek, ring, rustls, rsa, blake2, argon2, …).
- [`projects/crypto/zk-bug-tracker-readme.md`](../../projects/crypto/zk-bug-tracker-readme.md) — 0xPARC ZK bug tracker.
- Zcash Orchard underconstrained circuit: [`projects/zcash/advisories/ghsa-ghc3-g8w4-whf9.md`](../../projects/zcash/advisories/ghsa-ghc3-g8w4-whf9.md).
- Harness ZK/TEE classes: [`zk-circuits.md`](zk-circuits.md), [`tee-attestation.md`](tee-attestation.md).

## Automation (check spec)
```
for crate in crypto_deps:
  if rustsec_advisory(crate): FLAG
scan for AES-GCM/ChaCha with caller-supplied nonce reused across messages
scan ECDSA for missing low-s / nonce determinism (RFC 6979)
for circuit_signal: if not fully_constrained: FLAG underconstrained
```

- 2026-11-16: see [2026-11-16 check-specs](2026-11-16-mcp-open-data-rpc-tracer-logs.md)