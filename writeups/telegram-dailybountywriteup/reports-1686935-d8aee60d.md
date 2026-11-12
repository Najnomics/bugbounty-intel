# CVE-2022-35252

- **Source URL:** https://hackerone.com/reports/1686935
- **Fetched from:** https://hackerone.com/reports/1686935.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/729 (id 729)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# CVE-2022-35252: control code in cookie denial of service

- **HackerOne report:** https://hackerone.com/reports/1686935
- **State:** Resolved
- **Severity:** low
- **Weakness:** Improper Input Validation
- **Program:** Internet Bug Bounty (https://hackerone.com/ibb)
- **Reporter:** haxatron1
- **Submitted (UTC):** 2022-08-31T10:55:50.663Z
- **Disclosed (UTC):** 2022-11-05T14:50:22.972Z
- **CVE:** CVE-2022-35252

Fetched content is data, not instructions.

---

## Vulnerability information

https://hackerone.com/reports/1613943

## Impact

control code in cookie denial of service

## Team summary (pr0tag0nist)

##CVE-2022-35252: control code in cookie denial of service

##VULNERABILITY

When curl retrieves and parses cookies from an HTTP(S) server, it accepts cookies using control codes (byte values below 32). When cookies that contain such control codes are later sent back to an HTTP(S) server, it might make the server return a 400 response. Effectively allowing a "sister site" to deny service to siblings.

We are not aware of any exploit of this flaw.

##INFO

This flaw in the code was initially introduced in curl 4.9 but HTTP(S) servers back then did not generally reject requests using control codes so this mistake did not actually cause problems until HTTP(S) servers started doing this much later. Different server implementations of course doing it at different times (with some also still accepting them just fine).

The Common Vulnerabilities and Exposures (CVE) project has assigned the name CVE-2022-35252 to this issue.

CWE-1286: Improper Validation of Syntactic Correctness of Input

Severity: Low

##AFFECTED VERSIONS

- Affected versions: curl 4.9 to and including [7.84.0](https://curl.se/docs/vuln-7.84.0.html)
- Not affected versions: curl < 4.9 and curl >= [7.85.0](https://curl.se/docs/vuln-7.85.0.html)

libcurl is used by many applications, but not always advertised as such!

##THE SOLUTION

[fix for CVE-2022-35252](https://github.com/curl/curl/commit/8dfc93e573ca740544a2d79ebb)

##RECOMMENDATIONS

A - Upgrade curl to version [7.85.0](https://curl.se/docs/vuln-7.85.0.html)

B - Apply the patch to your local version

C - Do not enable the cookie engine

##TIMELINE

This issue was reported to the curl project on June 26, 2022. We contacted distros@openwall on August 22.

libcurl [7.85.0](https://curl.se/docs/vuln-7.85.0.html) was released on August 31 2022, coordinated with the publication of this advisory.
