# Thread completion pass (2026-11-11)

The earlier backfill was filtered on security keywords, so many threads by watched
researchers kept only the opener and lost the author's own follow-up replies. This pass
adds back the **author's own self-replies** in those conversations. Every added post is
verbatim X API v2 full-archive data. Nothing was summarised or paraphrased.

Method:
- **Candidate threads:** roots by watched accounts with `reply_count > 0` that are not
  replies to someone else. They were ranked into three tiers:
  - 0: explicit thread markers (🧵, `1/`, `(1/n)`, "thread", 👇) on an incomplete chain.
  - 1: two or more security keywords and more than 140 characters.
  - 2: one keyword.
- **Query shape:** `(from:A OR …) (to:A OR …) is:reply (conversation_id:… OR …)`, with up
  to 25 conversations per query. Each query is bounded from the earliest root to 30 days
  after the latest root.
- **Ingest rule:** a post is kept only when its conversation was in the batch and its author
  is the root's author. That keeps self-replies only and excludes third-party replies.
- **Missing conversation_id:** when the API omitted `conversation_id`, it was resolved
  through the `replied_to` chain. 848 existing posts were also re-linked this way, which
  merged threads that had been split.

Result: 1,727 self-reply posts added across 701 threads (231 API reads).
Posts from before 2017 returned no self-replies through `conversation_id` search.

Not done: the older `saxk` / `saxenism` keyword cursors listed in `backfill_status.md`.
Their original query strings were not recorded with the next_tokens, so they could not
be resumed exactly.
