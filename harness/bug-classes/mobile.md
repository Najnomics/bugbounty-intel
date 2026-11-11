# Mobile (deeplinks, webviews, content providers, thick client)

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **4** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Attack the mobile app; pinning/root checks are obstacles, not scope boundaries. (from Rhynorater). Source: [`posts/Rhynorater/ARCHIVE.md`](../../posts/Rhynorater/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- — (from _bagipro). Source: [`posts/_bagipro/2026-02-25-2026798826871247233.md`](../../posts/_bagipro/2026-02-25-2026798826871247233.md), [`writeups/_bagipro/oversecured-samsung-vulnerabilities-readme.md`](../../writeups/_bagipro/oversecured-samsung-vulnerabilities-readme.md).
- — (from _bagipro). Source: [`posts/_bagipro/2025-08-01-1951318010444005529.md`](../../posts/_bagipro/2025-08-01-1951318010444005529.md), [`writeups/_bagipro/oversecured-samsung-vulnerabilities-readme.md`](../../writeups/_bagipro/oversecured-samsung-vulnerabilities-readme.md).

## Method / findings in sources

- **8 high-impact IDORs + SSRF after bypassing SSL pinning, APK hash verify, root detection** — After bypassing SSL cert pinning, apk hash verification, and root detection, found 8 high-impact vulns — all IDORs and SSRF. Source: [`posts/Rhynorater/ARCHIVE.md`](../../posts/Rhynorater/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Content-provider attack via system apps** — See thread (3 of 4 parts captured). Source: [`posts/_bagipro/2026-02-25-2026798826871247233.md`](../../posts/_bagipro/2026-02-25-2026798826871247233.md), [`writeups/_bagipro/oversecured-samsung-vulnerabilities-readme.md`](../../writeups/_bagipro/oversecured-samsung-vulnerabilities-readme.md).
- **Android Uri host-validation bypass** — See thread. Source: [`posts/_bagipro/2025-08-01-1951318010444005529.md`](../../posts/_bagipro/2025-08-01-1951318010444005529.md), [`writeups/_bagipro/oversecured-samsung-vulnerabilities-readme.md`](../../writeups/_bagipro/oversecured-samsung-vulnerabilities-readme.md).
- **oversecured-samsung-vulnerabilities-readme** — Oversecured is a leading mobile security provider specializing in detecting vulnerabilities in Android and iOS apps. Source: [`writeups/_bagipro/oversecured-samsung-vulnerabilities-readme.md`](../../writeups/_bagipro/oversecured-samsung-vulnerabilities-readme.md).

## Automation (check spec)

```
# Checks derived from 4 documented finding(s) in findings.jsonl for class=mobile
# note: Attack the mobile app; pinning/root checks are obstacles, not scope boundaries.
# note: —
# note: —
```
