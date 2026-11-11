# @xssdoctor

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/xssdoctor/`](../posts/xssdoctor/); full writeups under [`writeups/xssdoctor/`](../writeups/xssdoctor/).

| Field | Value |
| --- | --- |
| X | [@xssdoctor](https://x.com/xssdoctor) (user id 14862128, joined 2008-05-21) |
| Name (profile) | xssdoctor |
| Followers (11 Nov 2026) | 6125 |
| Bio (verbatim) | hacker and cardiologist… not necessarily in that order |
| Specialty | Web / OAuth |
| Platforms | HackerOne |
| Evidence of valid finds | Shared OAuth bug thread; FAAV Microsoft records writeup. |

## Key findings and analysis

### iOS OAuth client accepts any protocol in redirect_uri

- Post: https://x.com/xssdoctor/status/2105723370125881675 — verbatim: [`posts/xssdoctor/2026-10-01-2105723370125881675.md`](../posts/xssdoctor/2026-10-01-2105723370125881675.md)
- **Bug class:** OAuth redirect_uri validation → token theft / ATO
- **Root cause:** The iPhone app's OAuth client (a client_id different from the web app's) allowed any protocol in redirect_uri because iOS deep links use custom schemes; a malicious app could start the flow in Safari with the callback pointing at itself and receive the user's credentials.
- **How it was found:** Noticed an unfamiliar client_id in the OAuth flow, traced it to the iOS app, then tested redirect_uri protocols.
- **Takeaways:** Enumerate every client_id (web, iOS, Android, desktop) and test redirect_uri validation separately for each.

## All captured posts (verbatim files)

- 2026-10-01 — Found a cool bug today, thought i should share it. — [`posts/xssdoctor/2026-10-01-2105723370125881675.md`](../posts/xssdoctor/2026-10-01-2105723370125881675.md) · https://x.com/xssdoctor/status/2105723370125881675
- 2026-10-02 — One of my favorite hackers doing a research review for one of my other favorite hackers. Amazing video,mind bl — [`posts/xssdoctor/2026-10-02-2106083881502089446.md`](../posts/xssdoctor/2026-10-02-2106083881502089446.md) · https://x.com/xssdoctor/status/2106083881502089446
- 2026-09-25 — This guy is incredible! — [`posts/xssdoctor/2026-09-25-2103573395916939563.md`](../posts/xssdoctor/2026-09-25-2103573395916939563.md) · https://x.com/xssdoctor/status/2103573395916939563

## Writeups saved (full text)

- [`writeups/xssdoctor/faav-17-trillion-microsoft-records.md`](../writeups/xssdoctor/faav-17-trillion-microsoft-records.md)

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 3 finding(s). Full verbatim posts under `posts/xssdoctor/`._

- **iOS OAuth client accepts any protocol in redirect_uri** (`OAuth redirect_uri validation → token theft / ATO`)
  - post: https://x.com/xssdoctor/status/2105723370125881675
  - local: `posts/xssdoctor/2026-10-01-2105723370125881675.md`, `writeups/xssdoctor/faav-17-trillion-microsoft-records.md`
  - bounty: undisclosed
- **Deterministic prompt injection via client-side feedback loops** (`llm-prompt-injection`)
  - post: https://x.com/xssdoctor/status/2047385925819203936
  - local: `posts/xssdoctor/ARCHIVE.md`, `data/x_posts.jsonl`
- **faav-17-trillion-microsoft-records** (`xss`)
  - post: https://blog.faav.net/how-i-couldve-accessed-17-trillion-microsoft-records
  - local: `writeups/xssdoctor/faav-17-trillion-microsoft-records.md`
