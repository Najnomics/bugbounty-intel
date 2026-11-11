# LLM prompt injection / agent abuse

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **1** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Treat client-visible model feedback as an oracle that can stabilize injection payloads. (from xssdoctor). Source: [`posts/xssdoctor/ARCHIVE.md`](../../posts/xssdoctor/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Method / findings in sources

- **Deterministic prompt injection via client-side feedback loops** — Technique to make prompt injection more deterministic using client-side feedback loops. Writeup at blog.starstrike.ai. Source: [`posts/xssdoctor/ARCHIVE.md`](../../posts/xssdoctor/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Automation (check spec)

```
# Checks derived from 1 documented finding(s) in findings.jsonl for class=llm-prompt-injection
# note: Treat client-visible model feedback as an oracle that can stabilize injection payloads.
```
