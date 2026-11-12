# GHSA-wvx7-39qj-2g9v: Line-separator characters can silently change literal values and types

| Field | Value |
| --- | --- |
| Repo | vyperlang/vyper |
| GHSA | GHSA-wvx7-39qj-2g9v |
| CVE | CVE-2026-114116 |
| Severity | low |
| CWE | n/a |
| Published | 2026-10-06T09:04:44Z |
| Updated | 2026-11-04T11:32:21Z |
| Affected | vyper >= 0.1.0b1, < 0.1.0b17 (patched: 0.1.0b17); vyper >= 0.4.1 |
| Credits | DELENE-TCHIO-ROMUALD |
| Advisory URL | https://github.com/vyperlang/vyper/security/advisories/GHSA-wvx7-39qj-2g9v |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

# Line-separator characters can silently change literal values and types

## Summary

Vyper's inconsistent handling of line separators can make numeric literals compile with incorrect values or types and bypass literal validation. Trigger characters shift source lookups to earlier text, with cumulative displacement when multiple characters occur. Crafted source can therefore compile to behavior different from what its literal expressions show, without a compiler warning.

## Details

In `vyper/ast/parse.py`, the source-line table uses `str.splitlines(keepends=True)`, which recognizes eight additional line separators that the Python parser does not count as newlines: `U+000B`, `U+000C`, `U+001C`, `U+001D`, `U+001E`, `U+0085`, `U+2028` and `U+2029`.

Each trigger adds an extra split, cumulatively redirecting source lookups to earlier lines; lookups immediately after a trigger can also shift within a line. `visit_Num` uses this incorrect text to classify numeric literals, reconstruct hexadecimal, binary and decimal values, and validate literal widths. Plain integers can therefore become hexadecimal or binary literals, and invalid literals can be accepted. Strings and `x""` hex-string literals retain their parser-provided values.

All eight characters can trigger the issue in comments or docstrings. The five ASCII characters also work in strings and byte literals; form feed additionally works as indentation whitespace.

Diagnostics, AST output and default-value metadata can also reflect incorrect source text.

## Proof of concept

The source declares `TREASURY` as `0x…dEaD`, but Vyper uses `0x…c0Ffee11` from the comment immediately above it. The two addresses start in the same column; a form-feed character in the first comment causes the incorrect lookup.

Run this Python script with an affected Vyper installation. Python converts `\x0c` into the actual form-feed byte in the Vyper source:

```python
import vyper

source = """# \x0c
#                             0x00000000000000000000000000000000c0Ffee11
TREASURY: constant(address) = 0x000000000000000000000000000000000000dEaD

@external
@view
def treasury() -> address:
    return TREASURY
"""

clean = source.replace("\x0c", "")

# The getter's runtime bytecode matches an explicitly substituted contract.
substituted = clean.replace(
    "0x000000000000000000000000000000000000dEaD",
    "0x00000000000000000000000000000000c0Ffee11",
)
def runtime(code):
    return vyper.compile_code(code, output_formats=["bytecode_runtime"])["bytecode_runtime"]

assert runtime(source) == runtime(substituted)
assert runtime(source) != runtime(clean)
```

Both assertions pass: the compiled getter matches the substituted-address contract and differs from the intended-address contract.

## Impact

An attacker able to contribute source code can hide a trigger in comments, docstrings, strings, byte literals or form-feed indentation to change an address, selector, byte sequence, integer or decimal constant. Depending on how the literal is used, this can redirect funds or alter contract behavior. Exploitation requires crafted source to be accepted and compiled. The reported scan found none of the eight trigger characters in 45,774 deployed-contract and repository source files across all compiler versions; this finding is limited to the scanned dataset.

## Affected versions

- **0.4.1 through 0.5.0b1** are affected. The issue is also unpatched on the inspected `master` checkout (`17e925db`).
- **0.1.0b17 through 0.4.0** are unaffected.
- **0.1.0b1 through 0.1.0b16** have a related manifestation: decimal and binary values can change; hexadecimal values retain their parsed value, but their type and checksum validation can change. The address PoC above is not applicable to these versions.

## Remediation

Build source offsets using the same newline rules as the parser, and apply consistent handling to diagnostics. Until a fix is available, reject the eight characters in source files before compilation. Previously compiled contracts require assessment and, where affected, recompilation and redeployment or an upgrade.

