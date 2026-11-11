# CSRF / cookie tossing / SameSite gaps

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **1** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- document.baseURI leaks full URL including query tokens from sandboxed iframes. (from garethheyes). Source: [`posts/garethheyes/ARCHIVE.md`](../../posts/garethheyes/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Method / findings in sources

- **CSRF token leaked via search form URL + sandboxed-iframe baseURI theft** — CSRF token placed in search form leaked to URL; used a tag to execute JS and stole token via document.baseURI, which leaks URL even from a sandboxed iframe. Found in Hackvertor, fixed. Source: [`posts/garethheyes/ARCHIVE.md`](../../posts/garethheyes/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Payloads / requests seen in sources

- `Steal CSRF token from document.baseURI even inside sandboxed iframe after reflecting token into URL` — CSRF token leaked via search form URL + sandboxed-iframe baseURI theft. Source: [`posts/garethheyes/ARCHIVE.md`](../../posts/garethheyes/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

See also [`../payloads/csrf.md`](../payloads/csrf.md) when present.

## Automation (check spec)

```
# Checks derived from 1 documented finding(s) in findings.jsonl for class=csrf
# try: Steal CSRF token from document.baseURI even inside sandboxed iframe after reflecting token into URL
```
