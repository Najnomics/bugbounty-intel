# Bug classes from the 19 Nov 2026 run (NGINX HTTP/2 RCE, `<selectedcontent>` XSS, ERC-4626 accounting drains, uninitialised-mapping CTO, ABCpdf LFR, KZG limbs)

Sources are verbatim in the repo; this file is the harness-oriented digest. Items marked *(inference)* go beyond what the source states.

## 1. NGINX HTTP/2 memory corruption (CVE-2026-123007 / CVE-2026-123633) + 3 more nginx CVEs ("NGINX2Shell / NGINX2Root")
- Sources: Wiz [`writeups/albinowax/wiz-nginx-http2-rce-cve-2026-123633-123007.md`](../../writeups/albinowax/wiz-nginx-http2-rce-cve-2026-123633-123007.md); Xint [`writeups/farazsth98/xint-nginx2root-remote-code-execution.md`](../../writeups/farazsth98/xint-nginx2root-remote-code-execution.md); posts [`albinowax`](../../posts/albinowax/2026-11-18-2123100309065199643.md), [`farazsth98`](../../posts/farazsth98/2026-11-18-2123073555340615910.md), [`0xacb`](../../posts/0xacb/2026-11-18-2123073966890008693.md), [`S1r1u5_`](../../posts/S1r1u5_/2026-11-19-2123270208744001691.md).
- CVE-2026-123007: HTTP/2 flow-control accounting → invalid memory copy; HTTP/2 enabled is enough (static file serving); 1.9.5–1.31.8. CVE-2026-123633: HTTP/2 UAF when proxying to upstream under low connection slots; 1.19.7–1.31.8. Xint also lists CVE-2026-123634 (resolver + request-derived `proxy_pass` + `mirror` with `mirror_request_body off`), CVE-2026-121810 (HTTP/3 to upstream), CVE-2026-113425 (mail proxy `auth_http`). Fix: 1.31.9; disabling HTTP/2 blocks only the two HTTP/2 CVEs.
- Harness: fingerprint nginx version + ALPN `h2` on in-scope hosts → flag candidates (report as outdated/vulnerable only if program accepts version-based reports; do not attempt memory-corruption exploitation without explicit permission). @albinowax: teams turning off HTTP/2 → re-run request-smuggling (CL.TE/TE.CL, H2→H1 downgrade) scans on hosts whose ALPN changed. @S1r1u5_: exploitation needs per-target grooming; not sprayable.

## 2. XSS in `innerHTML` without `=` via `<selectedcontent>` (Masato Kinugawa / PortSwigger)
- Source: [`writeups/garethheyes/portswigger-xss-innerhtml-without-equals.md`](../../writeups/garethheyes/portswigger-xss-innerhtml-without-equals.md).
- Payload: `<select><selectedcontent></selectedcontent><option><svg><script>alert(1)<\/script>` — cloned `<script>` executes (Safari; Chrome before 153). Use when the sink is `innerHTML` and `=`/event handlers are filtered; also test sanitizers that allow `select`/`option`/`selectedcontent`/`svg` (cf. DOMPurify GHSA-87xg-pxx2-7hvx). Verify in WebKit, not only Chromium.

## 3. ERC-4626 share-price manipulation via temporarily excluded assets (K3 Capital sBOLD, ~$3.43M)
- Source: [`writeups/telegram-defendor_eng/exvulsec-k3-capital-sbold-vault-drain-liquity-self-liquidation.md`](../../writeups/telegram-defendor_eng/exvulsec-k3-capital-sbold-vault-drain-liquity-self-liquidation.md).
- `totalAssets()` excluded unswapped Stability-Pool collateral below a 7,500 BOLD threshold; attacker self-liquidated Liquity V2 troves (flash-loaned wstETH) to move accounted BOLD into excluded collateral → share price dips → mint cheap shares → `swap()` restores assets → redeem. Invariant: any user-triggerable state change must not move `totalAssets()` without matching share changes; flag thresholds/exclusions in `totalAssets()`.

## 4. Two mappings, one check — uninitialised-mapping CTO takeover (CDSecurity)
- Source: [`writeups/telegram-defendor_eng/cdsecurity-token-cto-uninitialised-mapping-takeover.md`](../../writeups/telegram-defendor_eng/cdsecurity-token-cto-uninitialised-mapping-takeover.md).
- 30-day inactivity stored in a `uint256` mapping but read from a different `uint16` mapping (never written → 0) → takeover right after launch. Harness: for each `require` on a mapping read, confirm the same mapping is written somewhere (write/read set diff via Slither).

## 5. Bridge key rotation / admin proxy upgrade drains (Blockaid via defendor_eng)
- Gonka bridge: attacker rotated the epoch BLS group key, then drained reserves and minted unbacked WGNK (~$1.05M at time of post) — [`writeup`](../../writeups/telegram-defendor_eng/blockaid-gonka-bridge-bls-group-key-rotation-drain.md). Check who can rotate validator/group keys and whether rotation is itself verified by the previous key set.
- Reental (Polygon): admin upgraded aToken proxies to a drainable implementation (~$454k) — [`writeup`](../../writeups/telegram-defendor_eng/blockaid-reental-polygon-atoken-proxy-upgrade-drain.md). Centralisation/upgrade-authority risk.

## 6. HTML-to-PDF renderer local file read (H1 #4191812, Essity)
- Source: [`hackerone/reports/2026/4191812.md`](../../hackerone/reports/2026/4191812.md). Unauthenticated ABCpdf/Gecko HTML→PDF endpoint renders attacker HTML; `<iframe src="file:///C:/Windows/win.ini">` embedded in the PDF. Harness: find `*Pdf*`/`.asmx` render endpoints, inject iframe/`file:///` and check the PDF text.

## 7. CSRF on management console deleting integration credentials (H1 #3882740, GitHub Enterprise Server, CVE-2026-110288)
- Source: [`hackerone/reports/2026/3882740.md`](../../hackerone/reports/2026/3882740.md). Test destructive admin-console actions (integration credential delete) for missing CSRF protection.

## 8. Non-canonical limb encodings in generated verifiers (snark-verifier GHSA-265x-v3qf-ff6p / CVE-2026-61618)
- Source: [`projects/crypto/advisories/ghsa-265x-v3qf-ff6p.md`](../../projects/crypto/advisories/ghsa-265x-v3qf-ff6p.md). KZG accumulator coordinates reconstructed from public-instance limbs without per-limb bound checks → multiple encodings of one point. Check every limb < bound before reconstruction in Solidity/EVM verifiers.

## 9. Fix review (Bluethroat Labs / @saxenism, Zcash)
- [`posts/saxenism/2026-11-18-2123003101548556624.md`](../../posts/saxenism/2026-11-18-2123003101548556624.md), [`posts/saxenism/2026-11-18-2122996063590334928.md`](../../posts/saxenism/2026-11-18-2122996063590334928.md); advisories under [`projects/zcash/advisories/`](../../projects/zcash/advisories/). Re-test the *impact state* of every disclosed fix, not the original PoC path.
