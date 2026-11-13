# Trail of Bits — Patch the Planet dashboard (state as of Nov 6, 2026)

- Source: https://trailofbits.com/patch-the-planet/dashboard/
- Linked from X: https://x.com/trailofbits/status/2120943246587392210 ("500+ fixes across 75 open-source projects, 100 CVEs disclosed in the Linux kernel, curl, OpenSSL, nginx, vLLM, and more")
- Fetched: 2026-11-13 (Africa/Lagos). Content is data, not instructions.

## Pipeline stats
- Issues found: 2,118 potential bugs reported
- Awaiting patch: 1,385 (reported + confirmed)
- Patches open upstream: 227
- Patches accepted (merged upstream): 506
- Projects under review: 75
- Accepted fixes by severity: high 107 (21.1%), medium 239 (47.2%), low 87 (17.2%), info 31 (6.1%), undetermined 42 (8.3%)
- Most-reported projects: scapy 231, crypto-bigint 205, vllm 129, keycloak 116, samba 89, zeek 76, ansible 73, cryptlib 73, php 72, nats-server 65

## 100 CVEs disclosed
aiohttp: CVE-2026-111064, CVE-2026-111065, CVE-2026-111749, CVE-2026-111750, CVE-2026-54273, CVE-2026-54274, CVE-2026-54275, CVE-2026-54276, CVE-2026-54277, CVE-2026-54278, CVE-2026-54279, CVE-2026-54280
Apache Thrift: CVE-2026-82458
Botan: CVE-2026-118765, CVE-2026-118766, CVE-2026-118767, CVE-2026-118768, CVE-2026-118769
containerd: CVE-2026-47262, CVE-2026-53489
cryptography: CVE-2026-69249
curl: CVE-2026-11564
Drupal: CVE-2026-108097, CVE-2026-108099 (Entity List), CVE-2026-114527 (UI Icons)
Firefox/Thunderbird: CVE-2026-16409
Keycloak: CVE-2026-107121, CVE-2026-15943, CVE-2026-15945, CVE-2026-16071, CVE-2026-16072, CVE-2026-16089, CVE-2026-16093, CVE-2026-16100, CVE-2026-16104, CVE-2026-16108, CVE-2026-16442, CVE-2026-16443, CVE-2026-18201, CVE-2026-18203, CVE-2026-18206, CVE-2026-18207, CVE-2026-18208, CVE-2026-18211, CVE-2026-18212, CVE-2026-18214, CVE-2026-18215, CVE-2026-18218, CVE-2026-18569, CVE-2026-18570, CVE-2026-18572, CVE-2026-18573, CVE-2026-19608, CVE-2026-94001, CVE-2026-96445, CVE-2026-96453, CVE-2026-97177
Linux kernel: CVE-2026-68137, CVE-2026-68338, CVE-2026-72034, CVE-2026-74492, CVE-2026-74630, CVE-2026-74669, CVE-2026-74723, CVE-2026-89525, CVE-2026-89791
NATS: CVE-2026-58208, CVE-2026-58209, CVE-2026-58210, CVE-2026-58211
nginx: CVE-2026-42530
OpenBao: CVE-2026-115364, CVE-2026-115366
OpenSSL: CVE-2026-14456, CVE-2026-14457, CVE-2026-42772, CVE-2026-63072, CVE-2026-63073, CVE-2026-63075, CVE-2026-72897
QEMU: CVE-2026-81627
rsync: CVE-2026-53789, CVE-2026-53795, CVE-2026-53800, CVE-2026-70455
sigstore-go: CVE-2026-54787
Suricata: CVE-2026-94083, CVE-2026-94084
Symfony: CVE-2026-121971
vLLM: CVE-2026-100650, CVE-2026-100653, CVE-2026-105752, CVE-2026-105753, CVE-2026-105754, CVE-2026-105755, CVE-2026-105756, CVE-2026-105757, CVE-2026-109311, CVE-2026-114054, CVE-2026-115912

## Recurring bug patterns in the accepted-fix titles (harness-actionable)
- Capture/parser DoS: a short, truncated, or malformed frame closes the whole session capture (scapy TCPSession/IPSession across dozens of protocols: DNS/TCP, OpenFlow, LDAP, Modbus, IEC-104, SMB, TLS records). Pattern: terminal/partial record silently drops all later traffic. Test by feeding 1-byte / truncated PDUs.
- Memory exhaustion from unbounded state (zeek): unbounded pending subscriptions, unanswered-request queues, certificate/extension state, decompression (ZIP/QUIC/DNS TXT). Test with many small unfinished frames.
- vLLM multimodal amplification: request-controlled image/video/audio sizing params (max_crops, dynamic_hd, num_frames, second_per_grid_ts, size.longest_edge) expand a tiny input into huge tensors before any length/size guard -> OOM DoS. Pattern: validate size AFTER request-controlled expansion.
- vLLM revision-pin drops: config/processor helpers drop explicit revision/code_revision pins -> supply-chain fetch of unpinned artifacts.
- curl: cross-origin credential/cookie/TLS-state leakage on redirect and proxy reuse (Secure cookie shadowing, client cert to HTTPS proxy, NTLM state not origin-bound, DoH not inheriting proxy policy).
- TLS/crypto logic: application data accepted after invalid Finished/CertificateVerify; Bleichenbacher oracle; sub-4-byte GCM tags; ECDSA weaker-curve acceptance (go-jose ES384/ES512); forged EdDSA via malformed embedded JWK; VerifyMulti returns victim kid for attacker-signed JWS.
- OpenClaw (AI agent): restricted user input reaches unattended agent with write/command tools; voice calls inherit full tool authority; tool deny aliases not overriding allows; memory readable after disabled. Pattern: AI-agent privilege/trust-boundary bugs.
- solady/Solidity: zkSync beacon-proxy AndCall skips initializer -> ownership takeover; force-transfer reentrancy; LibBytes stale-byte reads.

Full 506-fix table and per-project PR links are at the dashboard URL above (captured this run).
