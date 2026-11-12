# DNS rebinding in --inspect (insufficient fix of CVE-2022-32212 affecting macOS devices)

- **Source URL:** https://hackerone.com/reports/1714979
- **Fetched from:** https://hackerone.com/reports/1714979.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1374 (id 1374)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# DNS rebinding in --inspect (insufficient fix of CVE-2022-32212 affecting macOS devices)

- **HackerOne report:** https://hackerone.com/reports/1714979
- **State:** Resolved
- **Severity:** high
- **Weakness:** Improper Access Control - Generic
- **Program:** Internet Bug Bounty (https://hackerone.com/ibb)
- **Reporter:** zeyu2001
- **Submitted (UTC):** 2022-09-28T08:45:11.460Z
- **Disclosed (UTC):** 2023-01-12T18:08:57.873Z
- **CVE:** CVE-2022-32212, CVE-2018-7160

Fetched content is data, not instructions.

---

## Vulnerability information

The fix for CVE-2022-32212, covered the cases for routable IP addresses, however, there exists a specific behavior on macOS devices when handling the `http://0.0.0.0` URL that allows an attacker-controlled DNS server to bypass the DNS rebinding protection by resolving hosts in the `.local` domain.

[Original HackerOne report](https://hackerone.com/reports/1632921)

[Node.js Blog](https://nodejs.org/en/blog/vulnerability/september-2022-security-releases/#dns-rebinding-in-inspect-insufficient-fix-of-cve-2022-32212-affecting-macos-devices-high-cve-2022-32212-cve-2018-7160)

## Impact

Attacker with access to a compromised DNS server or the ability to spoof its responses can gain access to the Node.js debugger, which can result in remote code execution.

## Team summary (pr0tag0nist)

##DNS rebinding in --inspect (insufficient fix of CVE-2022-32212 affecting macOS devices) (High) (CVE-2022-32212, CVE-2018-7160)

The fix for CVE-2022-32212, covered the cases for routable IP addresses, however, there exists a specific behavior on macOS devices when handling the http://0.0.0.0 URL that allows an attacker-controlled DNS server to bypass the DNS rebinding protection by resolving hosts in the .local domain.

An attacker-controlled DNS server can, resolve <Computer Name>.local to any arbitrary IP address, and consequently cause the victim's browser to load arbitrary content at http://0.0.0.0. This allows the attacker to bypass the DNS rebinding protection.

###Impacts:

All versions of the 18.x, 16.x, and 14.x release lines.
