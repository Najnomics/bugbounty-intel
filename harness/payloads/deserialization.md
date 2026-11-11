# Payloads — deserialization

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. CVE-2025-30406 ViewState RCE — fixed validation key across Shodan targets
- Researcher: @irsdl
- Post: https://x.com/irsdl/status/1911393741832679646
- Sources: `posts/irsdl/ARCHIVE.md`, `data/x_posts.jsonl`

```
ysoserial.net ViewState plugin + known/fixed validationkey
```

## 2. CVE-2020-0618 SSRS deserialization RCE — empty viewstate parameter required
- Researcher: @irsdl
- Post: https://x.com/irsdl/status/1228280144143540224
- Sources: `posts/irsdl/ARCHIVE.md`, `data/x_posts.jsonl`

```
Include empty viewstate parameter in the SSRS request
```
