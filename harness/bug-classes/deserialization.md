# Deserialization (ViewState, Java, pickle, etc.)

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **3** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Scan for static machine keys; ViewState deser is still point-and-shoot when keys leak. (from irsdl). Source: [`posts/irsdl/ARCHIVE.md`](../../posts/irsdl/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Deser exploits often need a specific empty/default field — read the request shape carefully. (from irsdl). Source: [`posts/irsdl/ARCHIVE.md`](../../posts/irsdl/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Workflow/automation engines that eval expressions are high-value RCE surfaces. (from irsdl). Source: [`posts/irsdl/ARCHIVE.md`](../../posts/irsdl/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Method / findings in sources

- **CVE-2025-30406 ViewState RCE — fixed validation key across Shodan targets** — Exploitable with ysoserial.net ViewState plugin. Fixed validationkey across almost all Shodan targets (tested via badsecrets/crapsecrets). CISA KEV. Source: [`posts/irsdl/ARCHIVE.md`](../../posts/irsdl/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **CVE-2020-0618 SSRS deserialization RCE — empty viewstate parameter required** — Deserialization RCE in SQL Server Reporting Services. Trickiest bit: an empty viewstate parameter is needed in the request for the exploit to work. Source: [`posts/irsdl/ARCHIVE.md`](../../posts/irsdl/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **SharePoint Workflow protection bypass → RCE (2018)** — RCE in SharePoint by bypassing Workflow protection mechanisms. Full story + PDF on soroush.me. Source: [`posts/irsdl/ARCHIVE.md`](../../posts/irsdl/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Payloads / requests seen in sources

- `ysoserial.net ViewState plugin + known/fixed validationkey` — CVE-2025-30406 ViewState RCE — fixed validation key across Shodan targets. Source: [`posts/irsdl/ARCHIVE.md`](../../posts/irsdl/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- `Include empty viewstate parameter in the SSRS request` — CVE-2020-0618 SSRS deserialization RCE — empty viewstate parameter required. Source: [`posts/irsdl/ARCHIVE.md`](../../posts/irsdl/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

See also [`../payloads/deserialization.md`](../payloads/deserialization.md) when present.

## Automation (check spec)

```
# Checks derived from 3 documented finding(s) in findings.jsonl for class=deserialization
# try: ysoserial.net ViewState plugin + known/fixed validationkey
# try: Include empty viewstate parameter in the SSRS request
# note: Workflow/automation engines that eval expressions are high-value RCE surfaces.
```
