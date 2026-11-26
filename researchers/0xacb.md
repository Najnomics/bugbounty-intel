# @0xacb

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/0xacb/`](../posts/0xacb/); full writeups under [`writeups/0xacb/`](../writeups/0xacb/).

| Field | Value |
| --- | --- |
| X | [@0xacb](https://x.com/0xacb) (user id 1320338581, joined 2013-04-01) |
| Name (profile) | André Baptista |
| Followers (11 Nov 2026) | 20307 |
| Bio (verbatim) | Hacker grinding for L1gh7 and Fr33dφm, straight outta the cosmic realm. Co-founder @ethiack |
| Specialty | Web |
| Platforms | HackerOne; co-founder Ethiack |
| Evidence of valid finds | sshole reproduction; AI RCEssion writeup. |

## Key findings and analysis

### sshole (CVE-2026-123158) reproduction

- Post: https://x.com/0xacb/status/2118387414527832065 — verbatim: [`posts/0xacb/2026-11-05-2118387414527832065.md`](../posts/0xacb/2026-11-05-2118387414527832065.md)
- **Bug class:** Auth bypass
- **Root cause:** See post.
- **How it was found:** —
- **Takeaways:** —

## All captured posts (verbatim files)

- 2026-10-27 — Attackers often exploit new vulnerabilities before defenders can react, sometimes before the vulnerability eve — [`posts/0xacb/2026-10-27-2115033525975986327.md`](../posts/0xacb/2026-10-27-2115033525975986327.md) · https://x.com/0xacb/status/2115033525975986327
- 2026-11-03 — I was reading a blog on the "AI RCEssion" today, and it captures what happened during October: AI isn't creati — [`posts/0xacb/2026-11-03-2117647871285584365.md`](../posts/0xacb/2026-11-03-2117647871285584365.md) · https://x.com/0xacb/status/2117647871285584365
- 2026-11-05 — Just reproduced sshole (CVE-2026-123158), beautifully simple bug by @kultekin — [`posts/0xacb/2026-11-05-2118387414527832065.md`](../posts/0xacb/2026-11-05-2118387414527832065.md) · https://x.com/0xacb/status/2118387414527832065
- 2026-10-20 — We’re continuously reversing the emerging 0days that matter most, sometimes before they get a CVE, and publish — [`posts/0xacb/2026-10-20-2112556367739257001.md`](../posts/0xacb/2026-10-20-2112556367739257001.md) · https://x.com/0xacb/status/2112556367739257001
- 2026-11-02 — This @bishopfox tool is next level! 🚀 — [`posts/0xacb/2026-11-02-2117156243588497749.md`](../posts/0xacb/2026-11-02-2117156243588497749.md) · https://x.com/0xacb/status/2117156243588497749

## Writeups saved (full text)

- [`writeups/0xacb/tedivm-ai-rcession.md`](../writeups/0xacb/tedivm-ai-rcession.md)

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 4 finding(s). Full verbatim posts under `posts/0xacb/`._

- **sshole (CVE-2026-123158) reproduction** (`Auth bypass`)
  - post: https://x.com/0xacb/status/2118387414527832065
  - local: `posts/0xacb/2026-11-05-2118387414527832065.md`, `writeups/0xacb/tedivm-ai-rcession.md`
- **Nginx ACL vs backend parser inconsistencies — forbidden routes become accessible** (`path-normalization`)
  - post: https://x.com/0xacb/status/1940325041834471716
  - local: `posts/0xacb/ARCHIVE.md`, `data/x_posts.jsonl`
- **Grafana CVE-2025-6023 bypass → XSS and account takeover (Hack.lu 0day challenge)** (`xss`)
  - post: https://x.com/0xacb/status/1994045652653785262
  - local: `posts/0xacb/ARCHIVE.md`, `data/x_posts.jsonl`
- **tedivm-ai-rcession** (`auth-bypass`)
  - post: https://blog.tedivm.com/rants/2026/10/the-ai-rcession-has-begun/
  - local: `writeups/0xacb/tedivm-ai-rcession.md`


### Update 2026-11-19

- **'Nginx2shell — 2shell or 2hype?'** — https://x.com/0xacb/status/2123073966890008693 — [`posts/0xacb/2026-11-18-2123073966890008693.md`](../posts/0xacb/2026-11-18-2123073966890008693.md); quotes https://twitter.com/satoki00/status/2123071303657910632. Writeups saved under `writeups/albinowax/` and `writeups/farazsth98/`.

## 2026-11-26 run additions

### Real-world LLM guardrail bypass with reversed Portuguese text

- Post: https://x.com/0xacb/status/2125593599224184836 — verbatim: [`posts/0xacb/2026-11-25-2125593599224184836.md`](../posts/0xacb/2026-11-25-2125593599224184836.md)
- **What he says:** "pure backwards text" isn't dead; he pulled off a bypass in a real engagement months ago "with nothing but reversed portuguese sentences"; model behind the target unknown. Details of target undisclosed.
- **Takeaway:** add reversed/permuted-text variants in non-English languages to prompt-injection/guardrail fuzzing; see the 2026-11-26 digest.
