# Give Gemini 4 Neon the bug nobody has reported yet

- **Source URL:** https://medium.com/@secops-vti/give-gemini-4-neon-the-bug-nobody-has-reported-yet-0408d05e3e20
- **Fetched from:** https://medium.com/feed/@secops-vti
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14996 (id 14996)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**An unreachable retry limit shows what a new benchmark can reveal about where Google’s model beats Claude Opus 5.5.**

OpenSearch once had a retry limit that could never be reached. When an operation failed, the code tried again, but the counter stayed at zero. As long as the failure persisted, the loop could run forever.

The fix was one line. The hard part was knowing which line, in an entire codebase, deserved a second look.

That bug appears in [SWE-sweep](https://swesweep.com/discoverability/), a benchmark that gives coding agents an unusually sparse assignment: *Here’s a repository. Find what’s broken and fix it.* There’s no ticket, filename, or stack trace. A repair counts only if it passes hidden tests and the project’s original test suite still passes. [swesweep.com](https://swesweep.com/)

This is where Google’s Gemini 4 Neon has an edge over Anthropic’s Claude Opus 5.5.

### The numbers

In [Google’s evaluation](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_neon_model_evaluation.pdf), Neon fixed 39.0% of the benchmark bugs in Google Antigravity. Opus fixed 10.1% in Claude Code.

The tools matter here. Antigravity lets Neon send several agents into different parts of a repository at once. But when Google put both models in the same simpler setup, Neon still led, 12.8% to 3.6%.

That gives an engineering team two reasons to pay attention. Neon kept its advantage with common tools, and the environment a team deploys can change how many repairs it gets. Even the best run left most known bugs unresolved.

### When someone has written the ticket

Now suppose the ticket exists, but the request is vague and the change crosses several files. [CursorBench](https://cursor.com/cursorbench) tests exactly that, using tasks drawn from real coding sessions.

Its most revealing comparison holds cost per task at the same reported level. At $6.54, Neon on High scored 63.7%. Opus on Extra High scored 56.7%. Neon also averaged 56 agent steps to Opus’s 95.

For a team working through a backlog of loosely specified changes, that seven-point gap is a reason to try Neon on tickets of its own.

### Where I’d use each

I’d give Neon the first pass on a pre-release bug hunt, or on a change whose scope the developer still has to discover.

I’d keep the choice open for terminal work, where Opus narrowly led Neon on Terminal-Bench 4.1, 65.8% to 65.2%.

The OpenSearch loop captures what makes the first assignment different. Once someone points to the counter, the patch is obvious. The work worth delegating starts before anyone knows to look there.
