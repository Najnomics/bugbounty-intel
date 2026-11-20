# GHSA-25rm-9wvm-m38v — falcon-rust: Discrete-Gaussian sampler runs at 2^-33 precision, far below Falcon's requirement (reference KAT vectors no longer pass)

Source: GitHub Advisory Database (OSV). Published: 2026-11-20T00:17:04Z  Modified: 2026-11-20T00:17:04Z
Severity: MODERATE  CVSS_V3: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N  
Aliases: CVE-2026-77382
Fetched: 2026-11-20 (Africa/Lagos)

## Affected
- crates.io `falcon-rust` — ranges: [{"type": "ECOSYSTEM", "events": [{"introduced": "0"}, {"fixed": "0.2.0"}]}]

## Details

**Reporter:** Connor Webber
**Package:** `falcon-rust` (crates.io), repository `github.com/aszepieniec/falcon-rust`
**Affected:** v0.1.3 and the current `master` (HEAD `cfa1b35`). Regression introduced in commit `bf2cf00`.
**Component:** discrete-Gaussian sampler, `src/samplerz.rs` (`approx_exp`, `ber_exp`, `sampler_z`)
**Status:** Confirmed by source review and by empirical measurement of the crate's own compiled code.

## Summary

falcon-rust's discrete-Gaussian rejection sampler evaluates its `exp()` acceptance step at only 32 bits of fractional precision. Measured directly against the crate's own compiled code, `approx_exp` has a maximum relative error of 2^-33. For comparison, the Falcon reference implementation achieves about 2^-63, and the f64 code this crate replaced achieved about 2^-52. The current sampler is therefore roughly 2^19 (about 500,000x) less precise than the version it replaced, and about 2^30 less precise than the reference.

Falcon's security proof relies on the sampled signatures being statistically indistinguishable from an ideal discrete Gaussian, so the signature transcript leaks nothing about the secret trapdoor. That guarantee holds only when the sampler's relative error stays small enough, over the roughly 2^64 signature budget, to keep the Renyi divergence between the real and ideal distributions negligible. The precision the security analysis relies on is cited in the literature between roughly 2^-40 and 2^-46 (for example the FACCT and isochronous-sampling analyses). At 2^-33 the sampler is below every value in that range, roughly 128x to 4096x too coarse depending on which bound you take, so the precondition the proof depends on is not met.

There is a second, bound-independent piece of evidence that removes any ambiguity: the crate's sampler can no longer reproduce Falcon's known-answer test (KAT) vectors, which are the authoritative correctness oracle. Rather than restore the precision, the maintainers loosened their own test tolerance and noted that "rejection decisions may differ at the boundary." The regression is already visible in-tree; its security significance was simply not recognized.

Because the sampler's sigma is derived from the secret basis Gram-Schmidt norms, the resulting distribution deviation is secret-dependent. The `exp` function itself is public, but its inputs, and therefore the deviation, depend on secret quantities. This is the class of flaw that statistical and hidden-number-problem learning attacks on biased Gaussian samplers target.

The crate's own documentation describes this sampler as "side-channel-hardened" and notes that "the sampler defines the secret-key distribution, so getting it wrong weakens the cryptography," which is exactly the property this defect touches.

## Technical detail

Root location: `src/samplerz.rs`

* `FixedPoint64 = FixedPoint<i64>` with `FRAC_UNIT = 1 << 32`, i.e. 32 fractional bits (`src/fixed_point.rs`). The crate already defines `FixedPoint128` with 64 fractional bits, the correct-precision type, but the sampler uses `FixedPoint64`.
* `approx_exp` (`samplerz.rs:34`) evaluates the FACCT polynomial, whose coefficients are the correct 63-bit constants, but at line 59 it does `let z: u64 = (x.0 as u64) << 31;`. This takes the 32-bit-precision argument and zero-fills the low 31 bits into a 63-bit word, so the polynomial is evaluated at an argument quantized to 2^-32.
* `sampler_z` computes `dss = 0.5 * isigma^2` and `ccs = sigma_min * isigma` in this 32-bit type, where `sigma` is the per-leaf value derived from the secret basis Gram-Schmidt norms (ffSampling). The precision loss therefore lands on secret-dependent quantities.

Regression: commit `bf2cf00` ("Eliminate f64 from key generation via generic FixedPoint<T>") replaced the prior f64 sampler. `git show bf2cf00^:src/samplerz.rs` shows the old `fn approx_exp(x: f64, ccs: f64)` operating at 63-bit scale. The change landed before the 0.1.3 release. The maintainers then re-pinned their tests to the degraded output and loosened the tolerance, and the Falcon KAT vectors no longer pass.

## Proof of concept (self-contained, reproducible)

Append the following module to `falcon-rust/src/samplerz.rs` and run:

`cargo test -p falcon-rust --release dump_approx_exp_precision -- --nocapture`

It calls the crate's own `approx_exp` and measures its maximum relative error against true `exp()` over the sampler's input domain `[0, ln 2]`.

```rust
#[cfg(test)]
mod prec_test {
    use super::*;
    #[test]
    fn dump_approx_exp_precision() {
        let n: u64 = 500000;
        let mut maxrel = 0.0f64;
        let two63 = 9223372036854775808.0f64; // 2^63
        for i in 0..=n {
            let x = (i as f64 / n as f64) * std::f64::consts::LN_2;
            let approx_u = approx_exp(FixedPoint64::from(x), FixedPoint64::ONE);
            let approx = approx_u as f64 / two63; // ~ exp(-x)
            let truev = (-x).exp();
            let rel = ((approx - truev) / truev).abs();
            if rel > maxrel { maxrel = rel; }
        }
        println!("MAXREL_APPROX_EXP={:.6e} log2={:.3}", maxrel, maxrel.log2());
        let req = 2f64.powi(-40);
        println!("FALCON_REQ_2^-40={:.3e}  RATIO_OVER_REQ={:.1}x", req, maxrel / req);
        let f64ref = 2f64.powi(-52);
        println!("F64_SAMPLER_2^-52={:.3e}  RATIO_OVER_F64={:.1}x", f64ref, maxrel / f64ref);
    }
}
```

Measured output (rustc 1.96.1, x86-64, release):

```
MAXREL_APPROX_EXP=1.164152e-10 log2=-33.000
FALCON_REQ_2^-40=9.095e-13  RATIO_OVER_REQ=128.0x
F64_SAMPLER_2^-52=2.220e-16  RATIO_OVER_F64=524287.3x
```

So the sampler is at 2^-33, about 128x coarser than even the loosest cited requirement (2^-40), and about 500,000x coarser than the f64 sampler this code replaced.

## Impact

The sampler's output distribution deviates from the specified discrete Gaussian by more than the security analysis allows, so the Renyi-divergence argument that guarantees the signature transcript hides the secret trapdoor no longer applies. Because the same sampler is used at key-generation time, the secret key itself is also drawn from a distribution that differs from the specified one. The deviation is secret-dependent, which is the property that statistical and hidden-number-problem learning attacks on biased Gaussian samplers exploit.

To be precise about scope (see Severity): this is a measured precision defect that voids the proof's precondition. It is not a demonstrated end-to-end key recovery.

## Severity (honest scoping)

Medium. This is a measured failure to meet the scheme's mandated sampler precision, which for a cryptographic library is a defect in its own right, because the security proof's precondition is provably not met and the reference KAT vectors fail. It is not a demonstrated key-recovery attack. Being coarser than the required bound invalidates the proof, but does not by itself establish a practical break. Showing recovery would require a full statistical-learning simulation over many signatures, and whether that is feasible within a realistic signature budget at a per-sample bias of 2^-33 is an open question. That uncertainty is why this is scoped as an unsoundness and proof-conformance defect rather than a claimed exploit. Suggested RUSTSEC classification: `informational = "unsound"` (cryptographic-soundness defect), or a Medium advisory.

## Fix

Perform `sampler_z`, `ber_exp`, and `approx_exp` at 53-bit precision (f64) or higher, or use the crate's existing `FixedPoint128` (64 fractional bits) throughout the acceptance-probability computation. Restore the Falcon reference KAT vectors as the test oracle instead of the loosened tolerance.

## Disclosure

Coordinated. Private notification to the maintainer first (this GitHub advisory), then RUSTSEC advisory-db. No public disclosure before maintainer contact.

## Note on tooling

Claude Opus (Anthropic's coding assistant) was used to help test the hypothesis, specifically to build the crate and measure `approx_exp` against high-precision `exp`, and to help prepare this report. The measurements above are deterministic and independently reproducible with the included test.

## References
- https://github.com/aszepieniec/falcon-rust/security/advisories/GHSA-25rm-9wvm-m38v
- https://nvd.nist.gov/vuln/detail/CVE-2026-77382
- https://github.com/aszepieniec/falcon-rust/commit/930d766256f9d67ec9b6d437557286cf47f042ca
- https://github.com/aszepieniec/falcon-rust/commit/bf2cf000e63a9803f7ab1a34f629a5a0e9c49cf6
- https://github.com/aszepieniec/falcon-rust
- https://github.com/aszepieniec/falcon-rust/releases/tag/v0.2.0
