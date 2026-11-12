# 🛡️ Hidden Security Risks of Solana ETFs

- **Source URL:** https://solanafloor.com/news/certora-weighs-in-on-hidden-security-risks-of-solana-etfs
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1009 (id 1009)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Certora Weighs in on Hidden Security Risks of Solana ETFs

What should potential $SOL ETF investors be aware of?

- Published:
- Edited:

$SOL ETF listings on Wall Street are considered a triumph for the Solana faithful, furthering TradFi’s embrace of the crypto asset class. Since launch, Solana ETF inflows have enjoyed solid institutional inflows, with the four active funds attracting over $600M in AUM in a matter of weeks.

But while institutional capital pours into $SOL ETFs and fixates on price action, investors could be overlooking certain underlying security risks.

Beyond the obvious risks of crypto volatility, what are some of the technical risks associated with Solana ETFs?

## Custodian Risk

Part of the wider appeal of Solana ETFs to the TradFi crowd is that they provide ‘hands-free’ crypto exposure. To the masses, blockchain technology remains a complex and technical minefield, and self-custody is not necessarily for everyone. ETFs enable TradFi players to embrace the highs and lows of crypto markets without worrying about key storage and good OpSec.

However, passing full custody rights to a third party comes with its own risks. Custody services undoubtedly have dozens of measures in place to ensure that wallets and user funds don’t get compromised, but no system is completely foolproof.

According to Certora DeFi Security Engineer Yura Sherman, custody risks and network failure are the biggest threats facing Solana ETFs, from a security perspective.

*“As with any ETF, Solana ETFs may be exposed to custody risks. In simple terms, a professional third party is storing SOL coins that belong to the ETF. That third-party, in theory, might lose some or all of the coins due to an exploit, private key leak, or a technical failure. Of course, we should note that the top-tier professional custodians have never had such issues in the past, but in theory the risk exists.”* - Yura Sherman, DeFi Security Engineer at Certora


Bitwise’s $BSOL, currently the largest $SOL ETF by AUM, holds its assets in the Coinbase Custody Trust Company. While this custody provider undoubtedly has all the licences and insurances to give clients peace of mind, we’ve seen members of Coinbase staff accept bribes and [divulge sensitive customer](https://solanafloor.com/news/certora-weighs-in-coinbase-avoided-data-leak) information in the past.

Fearmongering aside, the chances of a Solana ETF blowing up due to a custodian misplacing verification keys or conspiring against its clients are infinitesimally small. Outsourcing custody services to a regulated third-party is undoubtedly a reasonable approach when securing hundreds of millions in investor funds.

Certora DeFi Security Engineer Yura Sherman also suggested that Solana ETFs were at risk of network liveness failure.

*“The other security risk specific to Solana ETFs is potential Solana network failure. In theory, network consensus might fail for some period of time, during which it's impossible to move the coins (as the network is halted). In 2021 and 2022, Solana experienced outages that lasted from 4 to 17 hours.”* - Yura Sherman, DeFi Security Engineer at Certora


While this is certainly a concern that investors should be aware of, it’s not something that is an ETF-exclusive threat.

## Smart Contract Risk

As it stands, smart contract risk poses little risk to the Solana ETF landscape. $SOL held by ETF issuers shouldn’t need to go near smart contracts at all, instead sitting tight in staking accounts.

The vast majority of Solana ETFs rely entirely on native staking, meaning that the only onchain transactions being processed using custodied $SOL are to withdraw stake. This doesn’t expose any $SOL to smart contract vulnerabilities.

However, while this is true for most $SOL ETFs, there are some edge cases. REX-Shares $SSK holds around 3% of its AUM in LSTs (Liquid-Staking Tokens). While this arguably gives asset managers greater flexibility for redemptions, it exposes a percentage of the fund’s AUM to possible smart contract vulnerabilities.

On top of its spot Solana Staking ETF, $VSOL, VanEck has also registered filings for a prospective $jitoSOL ETF, which would be comprised entirely of the LST. The fact that $jitoSOL has never been exploited does help to instill confidence in its safety.

That being said, just because something has never happened before, doesn’t mean it can’t happen one day in the future. This is further reinforced by Sherman, who asserted that while leading Solana LSTs like $jitoSOL have a perfect record, it would be disingenuous to say they carry zero-risk.

*“Major Solana LSTs, like Jito, use the spl-stake-code program written by Solana Labs. This program has been audited multiple times and has a perfect security record. Having said that, it's impossible to guarantee that a given smart contract carries zero risk, and in this regard Solana LST smart contracts are no different.”* - Yura Sherman, DeFi Security Engineer at Certora


While smart contract risk poses a dilabolic level of risk applications that build on Solana, $SOL ETFs are largely protected from these threats by virtue of their simplicity. If in doubt, the average TradFi investor seeking $SOL exposure should probably steer clear of Solana ETFs comprising LSTs.

## Second Order Network Effects

As evidenced by the billions of dollars lost in hacks, scams, and exploits in crypto every year, the blockchain world is far from secure. While many of the risks associated with the onchain environment don’t affect ETFs ***directly***, they can still harm the health and integrity of $SOL, the underlying asset.

For example, a large-scale hack or exploit in Solana DeFi could have lasting repercussions on the network as a whole. Many of Solana’s DeFi applications boast over $1B in TVL; if hackers were able to exploit an onchain application and liquidate billions of assets, it’s entirely possible that $SOL could suffer, indirectly affecting ETF investors.

TradFi investors are no stranger to market dynamics and liquidation cascades, but terms like stake concentration and a ‘superminorty’ are probably not part of their financial jargon. The rise of ETFs and Digital Asset Treasuries like Forward Industries are adding to the top-heavy nature of [Solana’s declining validator count](https://solanafloor.com/news/do-we-need-worried-about-solanas-declining-validator-count), which gives these players outsized influence over network governance and economic security.

Of course, given that ETF issuers now have hundreds of millions at stake in Solana, it would be extremely unlikely that they would behave in a way that would jeopardize the chain. From an ETF security perspective, TradFi investors have little to worry about regarding concentration of stake.

All things considered, Solana ETFs are actually one of the most secure ways for institutional players to make significant investments in $SOL. While $SOL ETFs are admittedly a departure from crypto’s first principles, outsourcing custody of assets to reputable third parties is an easier, safer approach for the inexperienced user. Smart contract risk is almost non-existent, and any second-order effects would impact all investors, whether they hold spot $SOL or ETF shares.

No one can declare with absolute certainty that Solana ETFs are foolproof, zero-risk vehicles. In fact, the outsourcing of custody technicalities means that ETFs are probably the preferred option for the majority of investors.

### Read More on SolanaFloor

Recapping Solana's Biggest Moments in 2025

[Solana Wrapped: The 10 Biggest Stories of 2025](https://solanafloor.com/news/solana-wrapped-the-10-biggest-stories-of-2025)

### How Certora Protects Solana DeFi
