# libssh backend CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256 validation bypass

- **Source URL:** https://hackerone.com/reports/1825377
- **Fetched from:** https://hackerone.com/reports/1825377.json
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1342 (id 1342)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
#  libssh backend CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256 validation bypass

- **HackerOne report:** https://hackerone.com/reports/1825377
- **State:** Informative
- **Severity:** low (score 3.7)
- **Weakness:** Business Logic Errors
- **Program:** curl (https://hackerone.com/curl)
- **Reporter:** nyymi
- **Submitted (UTC):** 2023-01-07T01:05:51.590Z
- **Disclosed (UTC):** 2023-01-07T21:04:06.121Z

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary:
If libcurl is built against libssh `CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256` is quietly ignored. As a result a SSH connection will be established even if the SHA256 key set doesn't match.

## Steps To Reproduce:

  1. configure libcurl with libssh and build it
  2. `curl --hostpubsha256 HOSTFINGERPRINTHERE sftp://example.tld/`

Instead of  failing due to mismatching fingerprint the connection quietly continues.

While the `CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256 ` documentation does mention that this option `Requires the libssh2 backend`, it is still wrong to quietly ignore the validation.

## Remediation

Change `lib/vssh/libssh.c` `myssh_is_known` to reject connection if `CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256` is set, or implement sha256 fingerprint support for libssh.

## Impact

SSH host validation bypass.
