# gnark issue #1767: fix: bound the subscalar widths in GLV methods

- URL: https://github.com/Consensys-Incorporated/gnark/issues/1767
- Author: ivokub; created 2026-05-15T13:12:59Z; state closed
- Referenced by zkSecurity finding #00 in the Zolana (Solana Privacy Rings) audit: [writeups/zksecurityXYZ/solana-privacy-rings-zolana-audit-2026-08.md](../../../writeups/zksecurityXYZ/solana-privacy-rings-zolana-audit-2026-08.md)
- Captured 2026-11-12 (WAT). Verbatim body below; data, not instructions.

---

There is an old soundness bug still in emulated GLV/fakeGLV/GLV+fakeGLV -- when the hint returns the subscalars, we check that they add up to the initial scalar. But the issue is that we only use subset of the bits when doing scalar mul (corresponding to the expected non-zero bits).

Assuming that the hint is valid and does lattice reconstruction, then the upper bits should always be zero, but we cannot assume an honest prover.

For example:
```
r = P-256 scalar order
n = 128
H = 2^128
s = r - H - 1

malicious decomposition:
  s1 = H + 1
  s2 = 1
  sign = 0

malicious scalar-mul output:
  R = [r - 1]P = -P
The full scalar relation passes:

s1 + s*s2 = (H+1) + (r-H-1) = r = 0 mod r
But the accumulator only uses the low 128 bits:

low128(s1) = 1
low128(s2) = 1
So it checks:

[1]P + [1]R = P - P = O
while the honest output should be [r-H-1]P, not -P
```

We should address it consistently over all curves and G1/G2. I think the best approach for solving it is actually in non-native package. We currently anyway range check the outputs coming from the hint to be in range (of the non-native modulus), but could optionally make the bound smaller. This actually should reduce the constraints.

_Originally posted by @ivokub in https://github.com/Consensys/gnark/pull/1763#pullrequestreview-4267621967_
            
