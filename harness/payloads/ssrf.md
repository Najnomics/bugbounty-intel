# Payloads — ssrf

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. SSRF via localtest.me; open-redirect filter bypasses; CSRF token bypass by switching to GET
- Researcher: @zseano
- Post: https://x.com/zseano/status/1261995808553132032
- Sources: `posts/zseano/ARCHIVE.md`, `data/x_posts.jsonl`

```
SSRF: http://localtest.me ; open URL: /%255C and /%0d/ ; CSRF: change POST→GET to drop token requirement
```
