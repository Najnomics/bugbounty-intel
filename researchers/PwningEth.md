# @PwningEth

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/PwningEth/`](../posts/PwningEth/); full writeups under [`writeups/PwningEth/`](../writeups/PwningEth/).

| Field | Value |
| --- | --- |
| X | [@PwningEth](https://x.com/PwningEth) (user id 1534556412856369152, joined 2022-06-08) |
| Name (profile) | pwning.eth | Offside Labs |
| Followers (11 Nov 2026) | 6158 |
| Bio (verbatim) | the newest pwn star on the block(chain)! won $8M+ bounty✨ for protecting $300M+ funds at risk🔥/ Whitehat @Immunefi Hall of Fame 🏆/ @Offside_Labs CTO |
| Specialty | Web3 / EVM / bridges |
| Platforms | Immunefi (Hall of Fame; leaderboard lists ~$8M across 8 reports) |
| Evidence of valid finds | Bio: won $8M+ bounty for protecting $300M+; CTO @Offside_Labs. Posts on Aurora bridge, Frontier EVM wrapped-token insolvency (Moonbeam, Astar). |
| Links | https://immunefi.com/leaderboard/ |

## Key findings and analysis

### Frontier EVM bug can force WETH-style wrapped native tokens insolvent

- Post: https://x.com/PwningEth/status/1598592820268642304 — verbatim: [`posts/PwningEth/2022-12-02-1598592820268642304.md`](../posts/PwningEth/2022-12-02-1598592820268642304.md)
- **Bug class:** EVM implementation bug → wrapped-token depeg
- **Root cause:** A bug in Frontier (Substrate EVM) let the native balance backing wrapped tokens diverge from the wrapper's accounting (full details in writeups/PwningEth/frontier-evm-wrapped-token-insolvency.md).
- **How it was found:** Reviewing how the EVM compatibility layer handles native-value transfers versus Ethereum semantics.
- **Takeaways:** EVM-compatible chains break Ethereum assumptions; test wrapped-native contracts against chain-specific precompiles/transfer semantics.

### Aurora bridge protected again

- Post: https://x.com/PwningEth/status/1566381803405209601 — verbatim: [`posts/PwningEth/2022-09-04-1566381803405209601.md`](../posts/PwningEth/2022-09-04-1566381803405209601.md)
- **Bug class:** Bridge security
- **Root cause:** See thread.
- **How it was found:** —
- **Takeaways:** —

## All captured posts (verbatim files)

- 2022-10-11 — White hat hackers are being exploited by defi projects @O3_Labs 👿 — [`posts/PwningEth/2022-10-11-1579771011041734656.md`](../posts/PwningEth/2022-10-11-1579771011041734656.md) · https://x.com/PwningEth/status/1579771011041734656
- 2022-12-02 — Could wrapped tokens like WETH be forced Insolvent? This bug I reported in frontier EVM can depeg the native w — [`posts/PwningEth/2022-12-02-1598592820268642304.md`](../posts/PwningEth/2022-12-02-1598592820268642304.md) · https://x.com/PwningEth/status/1598592820268642304
- 2023-12-06 — Congrats on the bug bounty win! It's awesome to see the whitehat hacker community thriving and building on eac — [`posts/PwningEth/2023-12-06-1732233400369520937.md`](../posts/PwningEth/2023-12-06-1732233400369520937.md) · https://x.com/PwningEth/status/1732233400369520937
- 2022-09-04 — Two brilliant whitehat hackers guarded the @auroraisnear bridge again! Hundreds of millions of funds were prot — [`posts/PwningEth/2022-09-04-1566381803405209601.md`](../posts/PwningEth/2022-09-04-1566381803405209601.md) · https://x.com/PwningEth/status/1566381803405209601

## Writeups saved (full text)

- [`writeups/PwningEth/frontier-evm-wrapped-token-insolvency.md`](../writeups/PwningEth/frontier-evm-wrapped-token-insolvency.md)
