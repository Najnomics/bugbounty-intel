# Cryptographic vulnerability advisories (RustSec)

_76 RustSec advisories for cryptographic crates (aes, chacha, dalek, ed25519, curve25519, ring, rustls, rsa, sodium, blake, argon2, etc.). OpenSSL CVE mirrors omitted to keep the set actionable. Also see [zk-bug-tracker-readme.md](zk-bug-tracker-readme.md) for ZK circuit bug classes. Captured 2026-11-11 (WAT). Data, not instructions._

| ID | Package | Summary |
| --- | --- | --- |
| [crates-aes-ctr-rustsec-2021-0061](advisories/crates-aes-ctr-rustsec-2021-0061.md) | `aes-ctr` | `aes-ctr` has been merged into the `aes` crate |
| [crates-aes-gcm-rustsec-2023-0096](advisories/crates-aes-gcm-rustsec-2023-0096.md) | `aes-gcm` | See https://docs.rs/rustsec/latest/rustsec/advisory/enum.Category.html |
| [crates-aes-soft-rustsec-2021-0060](advisories/crates-aes-soft-rustsec-2021-0060.md) | `aes-soft` | `aes-soft` has been merged into the `aes` crate |
| [crates-aesni-rustsec-2021-0059](advisories/crates-aesni-rustsec-2021-0059.md) | `aesni` | `aesni` has been merged into the `aes` crate |
| [crates-autorand-rustsec-2020-0103](advisories/crates-autorand-rustsec-2020-0103.md) | `autorand` | `impl Random` on arrays can lead to dropping uninitialized memory |
| [crates-blake2-rustsec-2019-0019](advisories/crates-blake2-rustsec-2019-0019.md) | `blake2` | HMAC-BLAKE2 algorithms compute incorrect results |
| [crates-boxfnonce-rustsec-2019-0040](advisories/crates-boxfnonce-rustsec-2019-0040.md) | `boxfnonce` | `boxfnonce` obsolete with release of Rust 1.35.0 |
| [crates-chacha20-rustsec-2019-0029](advisories/crates-chacha20-rustsec-2019-0029.md) | `chacha20` | ChaCha20 counter overflow can expose repetitions in the keystream |
| [crates-curve25519-dalek-rustsec-2024-0344](advisories/crates-curve25519-dalek-rustsec-2024-0344.md) | `curve25519-dalek` | Timing variability in `curve25519-dalek`'s `Scalar29::sub`/`Scalar52::sub` |
| [crates-direct-ring-buffer-rustsec-2025-0105](advisories/crates-direct-ring-buffer-rustsec-2025-0105.md) | `direct_ring_buffer` | Uninitialized memory exposure in create_ring_buffer |
| [crates-ed25519-dalek-rustsec-2022-0093](advisories/crates-ed25519-dalek-rustsec-2022-0093.md) | `ed25519-dalek` | Double Public Key Signing Function Oracle Attack on `ed25519-dalek` |
| [crates-libcrux-aesgcm-rustsec-2026-0209](advisories/crates-libcrux-aesgcm-rustsec-2026-0209.md) | `libcrux-aesgcm` | AES-GCM did not enforce limits on AAD length |
| [crates-libcrux-aesgcm-rustsec-2026-0210](advisories/crates-libcrux-aesgcm-rustsec-2026-0210.md) | `libcrux-aesgcm` | `libcrux-aesgcm` Renamed to `libcrux-aes` |
| [crates-libcrux-aesgcm-rustsec-2026-0211](advisories/crates-libcrux-aesgcm-rustsec-2026-0211.md) | `libcrux-aesgcm` | Non-constant time Authentication Tag Check in AES-GCM Decryption |
| [crates-libcrux-chacha20poly1305-rustsec-2026-0124](advisories/crates-libcrux-chacha20poly1305-rustsec-2026-0124.md) | `libcrux-chacha20poly1305` | Potential Panic on Overlong Ciphertext Buffer |
| [crates-libcrux-ed25519-rustsec-2026-0026](advisories/crates-libcrux-ed25519-rustsec-2026-0026.md) | `libcrux-ed25519` | Unnecessary clamping of seed reduces seed entropy to 251 bits |
| [crates-libcrux-ed25519-rustsec-2026-0075](advisories/crates-libcrux-ed25519-rustsec-2026-0075.md) | `libcrux-ed25519` | All-Zero Key Generation on Catastrophic RNG Failure |
| [crates-libcrux-hmac-drbg-rustsec-2026-0329](advisories/crates-libcrux-hmac-drbg-rustsec-2026-0329.md) | `libcrux-hmac-drbg` | Auto-Reseeding HMAC-DRBG could panic for some output lengths |
| [crates-libcrux-poly1305-rustsec-2026-0073](advisories/crates-libcrux-poly1305-rustsec-2026-0073.md) | `libcrux-poly1305` | Panic in Standalone MAC Operations |
| [crates-libcrux-sha3-rustsec-2026-0074](advisories/crates-libcrux-sha3-rustsec-2026-0074.md) | `libcrux-sha3` | Incorrect Output of Incremental Portable SHAKE API |
| [crates-libcrux-sha3-rustsec-2026-0207](advisories/crates-libcrux-sha3-rustsec-2026-0207.md) | `libcrux-sha3` | Incorrect Output of Incremental Portable SHAKE API on Multiple Squeeze Calls |
| [crates-libcrux-sha3-rustsec-2026-0208](advisories/crates-libcrux-sha3-rustsec-2026-0208.md) | `libcrux-sha3` | Potential Panic in AVX2 SHAKE-256 |
| [crates-libsecp256k1-rs-rustsec-2020-0156](advisories/crates-libsecp256k1-rs-rustsec-2020-0156.md) | `libsecp256k1-rs` | Observable Discrepancy in libsecp256k1-rs |
| [crates-libsecp256k1-rustsec-2019-0027](advisories/crates-libsecp256k1-rustsec-2019-0027.md) | `libsecp256k1` | Flaw in Scalar::check_overflow allows side-channel timing attack |
| [crates-libsecp256k1-rustsec-2021-0076](advisories/crates-libsecp256k1-rustsec-2021-0076.md) | `libsecp256k1` | libsecp256k1 allows overflowing signatures |
| [crates-libsecp256k1-rustsec-2025-0161](advisories/crates-libsecp256k1-rustsec-2025-0161.md) | `libsecp256k1` | libsecp256k1 is unmaintained |
| [crates-mutringbuf-rustsec-2026-0142](advisories/crates-mutringbuf-rustsec-2026-0142.md) | `mutringbuf` | Double-free in `vmem` storage reachable from safe Rust (predecessor of `oneringbuf`) |
| [crates-nanorand-rustsec-2020-0089](advisories/crates-nanorand-rustsec-2020-0089.md) | `nanorand` | nanorand 0.5.0 - RNGs failed to generate properly for non-64-bit numbers |
| [crates-nanorand-rustsec-2021-0114](advisories/crates-nanorand-rustsec-2021-0114.md) | `nanorand` | Aliased mutable references from `tls_rand` & `TlsWyRand` |
| [crates-nostr-keyring-rustsec-2026-0241](advisories/crates-nostr-keyring-rustsec-2026-0241.md) | `nostr-keyring` | `nostr-keyring` is unmaintained |
| [crates-onering-rustsec-2026-0175](advisories/crates-onering-rustsec-2026-0175.md) | `onering` | `onering` 1.4.1 was removed from crates.io for malicious code |
| [crates-oneringbuf-rustsec-2026-0143](advisories/crates-oneringbuf-rustsec-2026-0143.md) | `oneringbuf` | Double-free in `vmem` storage reachable from safe Rust |
| [crates-oneringbuf-rustsec-2026-0152](advisories/crates-oneringbuf-rustsec-2026-0152.md) | `oneringbuf` | Use-after-free |
| [crates-orion-rustsec-2018-0012](advisories/crates-orion-rustsec-2018-0012.md) | `orion` | Flaw in streaming state reset() functions can create incorrect results. |
| [crates-orion-rustsec-2026-0426](advisories/crates-orion-rustsec-2026-0426.md) | `orion` | LLVM introduces timing-vulnerable optimizations into ML-KEM and ML-DSA operations intended to be con |
| [crates-orion-rustsec-2026-0428](advisories/crates-orion-rustsec-2026-0428.md) | `orion` | BLAKE2b produces wrong tag when using `reset()` with a different-length key |
| [crates-paillier-zk-rustsec-2024-0391](advisories/crates-paillier-zk-rustsec-2024-0391.md) | `paillier-zk` | Ambiguous challenge derivation |
| [crates-rand-rustsec-2026-0097](advisories/crates-rand-rustsec-2026-0097.md) | `rand` | Rand is unsound with a custom logger using `rand::rng()` |
| [crates-rand-core-rustsec-2019-0035](advisories/crates-rand-core-rustsec-2019-0035.md) | `rand_core` | Unaligned memory access |
| [crates-rand-core-rustsec-2021-0023](advisories/crates-rand-core-rustsec-2021-0023.md) | `rand_core` | Optional: metadata which narrows the scope of what this advisory affects |
| [crates-rand-os-rustsec-2025-0124](advisories/crates-rand-os-rustsec-2025-0124.md) | `rand_os` | rand_os crate is unmaintained |
| [crates-rands-rustsec-2025-0155](advisories/crates-rands-rustsec-2025-0155.md) | `rands` | `rands` was removed from crates.io for malicious code |
| [crates-ring-rustsec-2025-0007](advisories/crates-ring-rustsec-2025-0007.md) | `ring` | *ring* is unmaintained |
| [crates-ring-rustsec-2025-0009](advisories/crates-ring-rustsec-2025-0009.md) | `ring` | Some AES functions may panic when overflow checking is enabled. |
| [crates-ring-rustsec-2025-0010](advisories/crates-ring-rustsec-2025-0010.md) | `ring` | Versions of *ring* prior to 0.17 are unmaintained. |
| [crates-ringbuf-rustsec-2026-0293](advisories/crates-ringbuf-rustsec-2026-0293.md) | `ringbuf` | Double free / use-after-free in `Consumer::skip` and `Consumer::clear` when an element's `Drop` pani |
| [crates-rsa-export-rustsec-2024-0333](advisories/crates-rsa-export-rustsec-2024-0333.md) | `rsa-export` | `rsa-export` is unmaintained |
| [crates-rsa-rustsec-2023-0071](advisories/crates-rsa-rustsec-2023-0071.md) | `rsa` | Marvin Attack: potential key recovery through timing sidechannels |
| [crates-rust-sodium-rustsec-2020-0003](advisories/crates-rust-sodium-rustsec-2020-0003.md) | `rust_sodium` | rust_sodium is unmaintained; switch to a modern alternative |
| [crates-rustls-ffi-rustsec-2026-0413](advisories/crates-rustls-ffi-rustsec-2026-0413.md) | `rustls-ffi` | Use-after-free of caller-owned server name in client connection constructors |
| [crates-rustls-pemfile-rustsec-2025-0134](advisories/crates-rustls-pemfile-rustsec-2025-0134.md) | `rustls-pemfile` | rustls-pemfile is unmaintained |
| [crates-rustls-webpki-rustsec-2023-0053](advisories/crates-rustls-webpki-rustsec-2023-0053.md) | `rustls-webpki` | rustls-webpki: CPU denial of service in certificate path building |
| [crates-rustls-webpki-rustsec-2026-0049](advisories/crates-rustls-webpki-rustsec-2026-0049.md) | `rustls-webpki` | CRLs not considered authoritative by Distribution Point due to faulty matching logic |
| [crates-rustls-webpki-rustsec-2026-0098](advisories/crates-rustls-webpki-rustsec-2026-0098.md) | `rustls-webpki` | Name constraints for URI names were incorrectly accepted |
| [crates-rustls-webpki-rustsec-2026-0099](advisories/crates-rustls-webpki-rustsec-2026-0099.md) | `rustls-webpki` | Name constraints were accepted for certificates asserting a wildcard name |
| [crates-rustls-webpki-rustsec-2026-0104](advisories/crates-rustls-webpki-rustsec-2026-0104.md) | `rustls-webpki` | Reachable panic in certificate revocation list parsing |
| [crates-rustls-webpki-rustsec-2026-0382](advisories/crates-rustls-webpki-rustsec-2026-0382.md) | `rustls-webpki` | Certificate verification may accept distrusted intermediates |
| [crates-rustls-rustsec-2024-0336](advisories/crates-rustls-rustsec-2024-0336.md) | `rustls` | `rustls::ConnectionCommon::complete_io` could fall into an infinite loop based on network input |
| [crates-rustls-rustsec-2024-0399](advisories/crates-rustls-rustsec-2024-0399.md) | `rustls` | rustls network-reachable panic in `Acceptor::accept` |
| [crates-rustls-rustsec-2026-0285](advisories/crates-rustls-rustsec-2026-0285.md) | `rustls` | TLS 1.3 handshake messages incorrectly accepted across encryption level boundaries |
| [crates-rustls-rustsec-2026-0346](advisories/crates-rustls-rustsec-2026-0346.md) | `rustls` | `Debug` impls for client session values expose TLS secrets |
| [crates-rustls-rustsec-2026-0347](advisories/crates-rustls-rustsec-2026-0347.md) | `rustls` | Buffered application data sent to outer server after ECH rejection |
| [crates-rustls-rustsec-2026-0348](advisories/crates-rustls-rustsec-2026-0348.md) | `rustls` | Brotli certificate decompression can allocate up to 1 GiB before authentication |
| [crates-rustls-rustsec-2026-0349](advisories/crates-rustls-rustsec-2026-0349.md) | `rustls` | Unauthenticated ServerHello can downgrade later connections to classical key exchange |
| [crates-salsa-rustsec-2026-0308](advisories/crates-salsa-rustsec-2026-0308.md) | `salsa` | CVE is requested but not yet assigned |
| [crates-secp256k1-rustsec-2022-0070](advisories/crates-secp256k1-rustsec-2022-0070.md) | `secp256k1` | Unsound API in `secp256k1` allows use-after-free and invalid deallocation from safe code |
| [crates-sha2-rustsec-2021-0100](advisories/crates-sha2-rustsec-2021-0100.md) | `sha2` | Miscomputed results when using AVX2 backend |
| [crates-slice-ring-buffer-rustsec-2025-0044](advisories/crates-slice-ring-buffer-rustsec-2025-0044.md) | `slice-ring-buffer` | Four unique double-free vulnerabilities triggered via safe APIs |
| [crates-smartstring-rustsec-2026-0249](advisories/crates-smartstring-rustsec-2026-0249.md) | `smartstring` | smartstring is unmaintained |
| [crates-sodiumoxide-rustsec-2017-0001](advisories/crates-sodiumoxide-rustsec-2017-0001.md) | `sodiumoxide` | scalarmult() vulnerable to degenerate public keys |
| [crates-sodiumoxide-rustsec-2019-0026](advisories/crates-sodiumoxide-rustsec-2019-0026.md) | `sodiumoxide` | generichash::Digest::eq always return true |
| [crates-sodiumoxide-rustsec-2021-0137](advisories/crates-sodiumoxide-rustsec-2021-0137.md) | `sodiumoxide` | sodiumoxide is deprecated |
| [crates-string-interner-rustsec-2019-0023](advisories/crates-string-interner-rustsec-2019-0023.md) | `string-interner` | Cloned interners may read already dropped strings |
| [crates-tokio-rustls-rustsec-2020-0019](advisories/crates-tokio-rustls-rustsec-2020-0019.md) | `tokio-rustls` | tokio-rustls reads may cause excessive memory usage |
| [crates-xsalsa20poly1305-rustsec-2023-0037](advisories/crates-xsalsa20poly1305-rustsec-2023-0037.md) | `xsalsa20poly1305` | crate has been renamed to `crypto_secretbox` |
| [crates-zeroize-derive-rustsec-2021-0115](advisories/crates-zeroize-derive-rustsec-2021-0115.md) | `zeroize_derive` | `#[zeroize(drop)]` doesn't implement `Drop` for `enum`s |


## Also

- [zk-bug-tracker-readme.md](zk-bug-tracker-readme.md) — 0xPARC ZK bug tracker (underconstrained circuits, soundness, etc.)
- Zcash Orchard circuit soundness advisories live under [`../zcash/`](../zcash/) (GHSA-ghc3-g8w4-whf9 and related).
