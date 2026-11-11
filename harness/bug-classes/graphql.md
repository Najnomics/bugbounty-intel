# GraphQL (authz, batching, introspection)

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **1** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Always probe GraphQL unauthenticated — authz on mutations/queries is frequently missing. (from Assass1nmarcos). Source: [`posts/Assass1nmarcos/ARCHIVE.md`](../../posts/Assass1nmarcos/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Method / findings in sources

- **Unauthenticated GraphQL PII dump (limited disclosure)** — Without logging in, GraphQL functionality dumped PII. Tip: never skip GraphQL. Source: [`posts/Assass1nmarcos/ARCHIVE.md`](../../posts/Assass1nmarcos/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Automation (check spec)

```
# Checks derived from 1 documented finding(s) in findings.jsonl for class=graphql
# note: Always probe GraphQL unauthenticated — authz on mutations/queries is frequently missing.
```
