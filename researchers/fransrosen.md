# @fransrosen

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/fransrosen/`](../posts/fransrosen/); full writeups under [`writeups/fransrosen/`](../writeups/fransrosen/).

| Field | Value |
| --- | --- |
| X | [@fransrosen](https://x.com/fransrosen) (user id 80555140, joined 2009-10-07) |
| Name (profile) | Frans Rosén |
| Followers (11 Nov 2026) | 44173 |
| Bio (verbatim) | Co-founder of @centrahq/@detectify/@poweredbyingrid. I do not advertise doing hacking services, do not trust the ones telling you I do. |
| Specialty | Web (XSS, OAuth, postMessage) |
| Platforms | HackerOne (4x MVH per post) |
| Evidence of valid finds | 4th MVH at H1-0131; x-correlation/JSON-injection research (writeups/fransrosen/hackernotes-ep86-xcorrelation.md). |

## Key findings and analysis

### XSS-challenge solution thread (10 parts)

- Post: https://x.com/fransrosen/status/1828503460183941420 — verbatim: [`posts/fransrosen/2024-08-27-1828503460183941420.md`](../posts/fransrosen/2024-08-27-1828503460183941420.md)
- **Bug class:** XSS via double query-param extraction
- **Root cause:** The page parsed the query twice with different logic; a regex char class `[?|&]` (pipe treated literally) let a crafted parameter be picked up by one parser but not the other.
- **How it was found:** Reading the client-side parameter extraction code.
- **Takeaways:** Look for differential parsing of the same URL; regex char-class mistakes are common.

## All captured posts (verbatim files)

- 2024-09-04 — Here's my x-correlation/json-injection research also in writing, thank you @ctbbpodcast! — [`posts/fransrosen/2024-09-04-1831348652930949616.md`](../posts/fransrosen/2024-09-04-1831348652930949616.md) · https://x.com/fransrosen/status/1831348652930949616
- 2024-09-24 — I just won my 4th MVH at @Hacker0x01 H1-0131 in Scotland! 🤯 So sad I could not attend in person, been some cra — [`posts/fransrosen/2024-09-24-1838679292189848033.md`](../posts/fransrosen/2024-09-24-1838679292189848033.md) · https://x.com/fransrosen/status/1838679292189848033
- 2024-08-27 — Here's the solution for the XSS-challenge from last week. — [`posts/fransrosen/2024-08-27-1828503460183941420.md`](../posts/fransrosen/2024-08-27-1828503460183941420.md) · https://x.com/fransrosen/status/1828503460183941420

## Writeups saved (full text)

- [`writeups/fransrosen/hackernotes-ep86-xcorrelation.md`](../writeups/fransrosen/hackernotes-ep86-xcorrelation.md)
