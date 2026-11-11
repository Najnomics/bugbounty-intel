# Payloads — smart-contract

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. Rounding-down precision loss → repeated 1-wei mint leaching free tokens
- Researcher: @DevDacian
- Post: https://x.com/DevDacian/status/1724351803846975607
- Sources: `posts/DevDacian/ARCHIVE.md`, `data/x_posts.jsonl`

```
Repeatedly mint 1 wei when share calculation rounds down to zero
```
