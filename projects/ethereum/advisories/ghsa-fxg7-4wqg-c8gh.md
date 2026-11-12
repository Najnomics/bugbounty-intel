# GHSA-fxg7-4wqg-c8gh: `create_from_blueprint` offset validation bypass through unsigned wraparound

| Field | Value |
| --- | --- |
| Repo | vyperlang/vyper |
| GHSA | GHSA-fxg7-4wqg-c8gh |
| CVE | none assigned |
| Severity | low |
| CWE | CWE-681, CWE-697 |
| Published | 2026-10-06T08:45:22Z |
| Updated | 2026-10-06T08:45:22Z |
| Affected | vyper >= 0.3.4 |
| Credits | n/a |
| Advisory URL | https://github.com/vyperlang/vyper/security/advisories/GHSA-fxg7-4wqg-c8gh |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

## Summary

Vyper's `create_from_blueprint` can deploy a contract with empty runtime bytecode instead of reverting when supplied with an invalid `code_offset`. Contracts that allow attackers to control this parameter are affected.

## Details

The builtin computes the remaining blueprint code size using EVM subtraction, then validates the result with a signed comparison:

```python
codesize = ["sub", ["extcodesize", target], code_offset]
check_codesize = ["assert", ["sgt", codesize, 0]]
```

Because `code_offset` is a `uint256`, subtraction can wrap modulo `2^256` and produce a small positive result that passes the check.

For example, given a blueprint with 200 bytes of code:

```text
code_offset = 2^256 - 1
codesize    = 200 - (2^256 - 1) mod 2^256 = 201
sgt(201, 0) = true
```

`EXTCODECOPY` then reads beyond the blueprint's code and fills the destination with zeros. The resulting initcode begins with `STOP`, so contract creation succeeds and returns an address with no runtime code. The oversized source offset does not itself cause excessive gas consumption.

## Impact

An attacker who controls `code_offset` can cause a factory to deploy empty contracts instead of the intended blueprint instances. Depending on the application, this can disrupt initialization, violate assumptions about deployed contracts, or leave ETH and tokens sent to those addresses inaccessible.

The common pattern using a fixed, valid offset such as `code_offset=3` is unaffected by this bypass.

## Remediation

Validate **`code_offset < extcodesize(target)` using an unsigned comparison before subtraction**. Checking only the wrapped result, even with an unsigned comparison, does not prevent the bypass.

As a workaround, use a fixed, valid offset or explicitly enforce this bound before calling `create_from_blueprint`.

