# 29

- **Source URL:** https://hackerone.com/reports/3971518
- **Fetched from:** https://hackerone.com/reports/3971518.json
- **Fetched:** 2026-11-13
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14906 (id 14906)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 29: CURLOPT_ISSUERCERT accepts a different-key certificate when issuer metadata collides

- **HackerOne report:** https://hackerone.com/reports/3971518
- **State:** Informative
- **Severity:** none
- **Weakness:** None
- **Program:** curl (https://hackerone.com/curl)
- **Reporter:** giant_anteater
- **Submitted (UTC):** 2026-08-26T15:42:35.268Z
- **Disclosed (UTC):** 2026-09-08T08:01:00.034Z
- **Attachments (filenames only; expiring CDN URLs omitted):** reproduce.sh (application/x-sh); client.c (text/x-csrc); Dockerfile (application/octet-stream); run.sh (application/x-sh)

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary

`ossl_check_issuer()` in `lib/vtls/openssl.c` uses `X509_check_issued()` to implement `CURLOPT_ISSUERCERT`. This OpenSSL function checks metadata (subject/issuer names, key identifiers, algorithm compatibility, key usage) but does **not** verify the certificate's cryptographic signature. A certificate with matching subject DN and Subject Key Identifier but a completely different public key passes the check.

The documentation at `docs/libcurl/opts/CURLOPT_ISSUERCERT.md` states the option verifies the issuer is "indeed the one associated with the certificate" and can "enforce that the peer certificate is from a specific branch of the tree." The implementation does not cryptographically enforce this.

The same pattern exists in the GnuTLS backend (`gnutls_x509_crt_check_issuer()` at `lib/vtls/gtls.c:1815`).

## Root cause

```c
// lib/vtls/openssl.c — ossl_check_issuer()
if(X509_check_issued(issuer, server_cert) != X509_V_OK) {
```

Per OpenSSL docs ([X509_check_issued](https://docs.openssl.org/master/man3/X509_check_issued/)): this checks whether a certificate was "apparently issued" by another — it explicitly does not verify the signature. Normal chain verification runs independently beforehand (line 4828) and does not require the configured issuer to appear in the verified chain.

## Reproduction

Expected vs actual output:

The PoC builds two independent CA branches. Both intermediates share the same subject (`CN=Colliding Intermediate`) and the same hardcoded SKID, but use different RSA keys. The leaf is signed by the real intermediate (trusted root). The decoy intermediate (untrusted root) is passed as `CURLOPT_ISSUERCERT`.

- **Expected:** `CURLE_SSL_ISSUER_ERROR` (83) — the configured issuer did not sign the leaf.
- **Actual:** `CURLE_OK` (0) — the transfer succeeds.

Controls confirm the check is active: changing the decoy's subject or SKID correctly returns error 83. Direct `openssl verify` of the leaf against the decoy's key fails with "certificate signature failure."

## Impact

This bypasses the PKI branch restriction that `CURLOPT_ISSUERCERT` is documented to enforce. It does **not** bypass normal CA verification or hostname verification. Exploitation requires the attacker to already control another CA hierarchy trusted by the application and have authority to issue for the target hostname, which significantly limits practical impact. I believe Low severity is appropriate.
