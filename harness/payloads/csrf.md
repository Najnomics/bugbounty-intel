# Payloads — csrf

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. CSRF token leaked via search form URL + sandboxed-iframe baseURI theft
- Researcher: @garethheyes
- Post: https://x.com/garethheyes/status/1834985571422245055
- Sources: `posts/garethheyes/ARCHIVE.md`, `data/x_posts.jsonl`

```
Steal CSRF token from document.baseURI even inside sandboxed iframe after reflecting token into URL
```
