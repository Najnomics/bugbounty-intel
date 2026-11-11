# Payloads — xss

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. XSS-challenge solution thread (10 parts)
- Researcher: @fransrosen
- Post: https://x.com/fransrosen/status/1828503460183941420
- Sources: `posts/fransrosen/2024-08-27-1828503460183941420.md`, `writeups/fransrosen/hackernotes-ep86-xcorrelation.md`

```
Send two query params: ?|targetUrl=<validated> and &targetUrl=javascript:... — one extraction validates, the other reaches location.href (regex [?|&] treats | literally)
```
