# @j00ru

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/j00ru/`](../posts/j00ru/); full writeups under [`writeups/j00ru/`](../writeups/j00ru/).

| Field | Value |
| --- | --- |
| X | [@j00ru](https://x.com/j00ru) (user id 132625446, joined 2010-04-13) |
| Name (profile) | j00ru//vx |
| Followers (11 Nov 2026) | 37039 |
| Bio (verbatim) | (Mostly) Windows hacker & vulnerability researcher. Google Project Zero. @DragonSectorCTF |
| Specialty | Native / Windows / Android |
| Platforms | Google Project Zero |
| Evidence of valid finds | Samsung MMS Qmage exploit series; win32k CVE-2021-26863. |
| Links | https://googleprojectzero.blogspot.com |

## Key findings and analysis

### Samsung MMS exploit part 5: ASLR bypass → RCE

- Post: https://x.com/j00ru/status/1293600839320428545 — verbatim: [`posts/j00ru/2020-08-12-1293600839320428545.md`](../posts/j00ru/2020-08-12-1293600839320428545.md)
- **Bug class:** Memory corruption
- **Root cause:** See writeups/j00ru/gpz-mms-exploit-part-5.md.
- **How it was found:** Fuzzing Qmage codec.
- **Takeaways:** —

## All captured posts (verbatim files)

- 2020-08-12 — The final part 5 of my Samsung MMS exploit blog series is out 🎉 It covers bypassing Android 10 ASLR and gettin — [`posts/j00ru/2020-08-12-1293600839320428545.md`](../posts/j00ru/2020-08-12-1293600839320428545.md) · https://x.com/j00ru/status/1293600839320428545
- 2020-07-28 — Trying hard to keep up the weekly cadence of the MMS series. Today we're finally moving to exploitation, start — [`posts/j00ru/2020-07-28-1288200298390081536.md`](../posts/j00ru/2020-07-28-1288200298390081536.md) · https://x.com/j00ru/status/1288200298390081536
- 2021-03-12 — Fixed this month: CVE-2021-26863, a race condition/use-after-free in win32k.sys demonstrating @tiraniddo's exc — [`posts/j00ru/2021-03-12-1370364905862352901.md`](../posts/j00ru/2021-03-12-1370364905862352901.md) · https://x.com/j00ru/status/1370364905862352901
- 2020-08-04 — This week's episode: MMS Exploit Part 4: MMS Primer, Completing the ASLR Oracle — [`posts/j00ru/2020-08-04-1290678374487162881.md`](../posts/j00ru/2020-08-04-1290678374487162881.md) · https://x.com/j00ru/status/1290678374487162881
- 2020-11-22 — GG! I pushed my Windows x64 pwnable binary together with a brief write-up and exploit code on GitHub: — [`posts/j00ru/2020-11-22-1330645107901685764.md`](../posts/j00ru/2020-11-22-1330645107901685764.md) · https://x.com/j00ru/status/1330645107901685764

## Writeups saved (full text)

- [`writeups/j00ru/gpz-mms-exploit-part-3.md`](../writeups/j00ru/gpz-mms-exploit-part-3.md)
- [`writeups/j00ru/gpz-mms-exploit-part-4.md`](../writeups/j00ru/gpz-mms-exploit-part-4.md)
- [`writeups/j00ru/gpz-mms-exploit-part-5.md`](../writeups/j00ru/gpz-mms-exploit-part-5.md)
- [`writeups/j00ru/gpz-windows-exploitation-tricks-trapping.md`](../writeups/j00ru/gpz-windows-exploitation-tricks-trapping.md)

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 5 finding(s). Full verbatim posts under `posts/j00ru/`._

- **Samsung MMS exploit part 5: ASLR bypass → RCE** (`Memory corruption`)
  - post: https://x.com/j00ru/status/1293600839320428545
  - local: `posts/j00ru/2020-08-12-1293600839320428545.md`, `writeups/j00ru/gpz-mms-exploit-part-3.md`, `writeups/j00ru/gpz-mms-exploit-part-4.md`
- **gpz-mms-exploit-part-3** (`web`)
  - post: https://googleprojectzero.blogspot.com/2020/07/mms-exploit-part-3-constructing-primitives.html
  - local: `writeups/j00ru/gpz-mms-exploit-part-3.md`
- **gpz-mms-exploit-part-4** (`web`)
  - post: https://googleprojectzero.blogspot.com/2020/08/mms-exploit-part-4-completing-aslr-oracle.html
  - local: `writeups/j00ru/gpz-mms-exploit-part-4.md`
- **gpz-mms-exploit-part-5** (`web`)
  - post: https://googleprojectzero.blogspot.com/2020/08/mms-exploit-part-5-defeating-aslr-getting-rce.html
  - local: `writeups/j00ru/gpz-mms-exploit-part-5.md`
- **gpz-windows-exploitation-tricks-trapping** (`web`)
  - post: https://googleprojectzero.blogspot.com/2021/01/windows-exploitation-tricks-trapping.html
  - local: `writeups/j00ru/gpz-windows-exploitation-tricks-trapping.md`
