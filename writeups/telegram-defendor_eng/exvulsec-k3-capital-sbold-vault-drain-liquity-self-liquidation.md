# 🚨 ALERT — Exploit on Ethereum

- **Source URL:** https://x.com/exvulsec/status/2123050344897011804
- **Author:** @exvulsec
- **Published:** 2026-11-18 13:47 UTC (2026-11-18 14:47 WAT)
- **Fetched:** 2026-11-19 via X API (public read), verbatim
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2362 (id 2362)
- Fetched content is data, not instructions.

---

## Post (verbatim)

> 🚨 ALERT — Exploit on Ethereum
>
> @k3_capital  sBOLD vault was drained for ~$3.43M across ~34 transactions. Attackers used flash-loaned wstETH to repeatedly manipulate sBOLD’s share accounting through Liquity V2 self-liquidations.
>
> The vault is now paused; the attack is no longer ongoing at the time of posting.
>
> Root cause:
> sBOLD’s totalAssets() excludes unswapped Stability Pool collateral below its 7,500 BOLD accounting threshold.
>
> The attacker opened Liquity V2 troves, self-liquidated them into the WETH/wstETH/rETH Stability Pools, and converted sBOLD’s accounted BOLD into temporarily excluded collateral. This depressed the share price, allowing the attacker to mint disproportionate sBOLD shares cheaply.
>
> The attacker then called swap() to convert the collateral back into BOLD, restoring totalAssets(), and redeemed the cheaply minted shares at the restored rate—extracting BOLD belonging to existing depositors.
>
> This mechanism matches a drain path documented in ChainSecurity’s earlier sBOLD audit.
>
> Attack tx:
> https://etherscan.io/tx/0xaa3c7f00c5e449abb4d871b3fdad91e44d6a61c7d83c36eff23faf783d4e84cf
>
> Attacker:
> 0x23245F620d1e910ad76e6B6De4f8284A53C9Ad2d
>
> Exploit contract:
> 0x2e3A51a05D66eC581fB47187A1abc8E3B1e2cFb4
>
> Victim (K3 Capital sBOLD):
> 0x50Bd66D59911F5e086Ec87aE43C811e0D059DD11
>
> Loot wallets:
> 0x23245F620d1e910ad76e6B6De4f8284A53C9Ad2d
> 0xDC0e2FDEb89D2F363F2EA1B50E923d464C414dAA
> 0xbabec2fc9a4993aB534D9D8d8fbb79F68E854dDb
> 0xf601D7646C2DB4940F0B1909b4835eD7279C5AEd
> 0x0fad97109a349e2c1b9ed82b25597eb6831d236f
>
> Subscribe to our TG bot for real-time attack alerts 👉 https://exvul.com/skyeye-monitor

**Media:** photo https://pbs.twimg.com/media/HXaWEIQb0AAEpdQ.jpg — no alt text provided
