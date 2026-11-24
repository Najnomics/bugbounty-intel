# 🚨 GoPlus Security Alert: A wave of private key compromises and signing abuse has caused over $17 million in lo

- **Source URL:** https://x.com/GoPlusSecurity/status/2124835362883129357
- **Author:** @GoPlusSecurity
- **Published:** 2026-11-23 12:00 UTC (2026-11-23 13:00 WAT)
- **Fetched:** 2026-11-24 via X API (public read), verbatim
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2379 (id 2379)
- Fetched content is data, not instructions.

---

## Post (verbatim)

> 🚨 GoPlus Security Alert: A wave of private key compromises and signing abuse has caused over $17 million in losses across five consecutive days. Project teams and developers should strengthen key management and signing controls to protect their assets.
>
> 🛡️ Security Recommendations: Private Key Compromise and Signing Abuse
>
> 1. Eliminate privileged single points of failure. Secure deployer, minter, validator, and relayer roles with multisig or MPC. Avoid giving a single EOA direct control over minting, upgrades, or vault withdrawals.
>
> 2. Rotate keys in a trusted environment. If a key compromise is suspected, revoke compromised keys and sessions, invalidate pending messages wherever possible, and generate replacement keys in a clean environment. Changing passwords or restarting the existing signing service is not enough.
>
> 3. Validate transaction intent before signing. Beyond cryptographic signature verification, validate the source-chain transaction, nonce, chainId, destination contract, recipient, amount, and business request ID. Cross-chain bridges should use multiple independent DVNs and require multiple signatures.
>
> 4. Cap the potential loss from a single incident. Apply amount caps, rate limits, timelocks, and independent approval requirements to minting and withdrawals. Automatically trigger circuit breakers on abnormal token supply changes, depegs, or withdrawals approaching the full vault balance.
>
> 5. Protect sessions and logs. Never log private keys, seed phrases, session tokens, or other sensitive key material. Remove public access to log query endpoints promptly. Transfers and limit changes must require fresh verification of user authorization.
>
> 6. Watch for follow-up phishing. Trust only official channels. Treat unsolicited “refund,” “migration,” or “claim” messages as potential phishing attempts.
>
> 7. Guard against iOS exploit campaigns and malvertising. Criminal campaigns exploiting older Apple OS vulnerabilities pose serious risks to user keys and administrative access. Keep iOS and wallet apps updated. Be cautious with unfamiliar ads, shortened links, QR codes, and pages prompting you to open Safari. Keep high-value holdings separate from phones used for everyday browsing, QR scanning, and entertainment; prioritize hardware wallets or multisig. Never screenshot seed phrases or private keys, or store them in photo libraries, notes, chat histories, or cloud backups.
>
> 1️⃣ Fusionist (ACE)
> Affected project: Fusionist / Endurance @fusionistio—ACE and its BSC–Endurance bridge.
> Date: November 23, 2026
> Estimated loss: $1.87M–$2M
> Root cause: Abuse of privileged cross-chain verification and minting flows led to unauthorized ACE minting and sell-offs on BSC, followed by reserve depletion on Endurance.
> Attacker addresses:
> 0x3f1045210a80a375d6c7cbad57800d5e8f30f34e (privileged minting address)
> 0x1029aa6abbb46c88c3b1f668757184f64d9e12c5
> 0xb335cd8771c9f0469d5c3214f24945ef9ab019b5
>
> 2️⃣ Cyber (CYBER)
> Affected project: Cyber @BuildOnCyber—CYBER’s LayerZero bridge and Ethereum token escrow contract.
> Date: November 22, 2026
> Estimated loss: 5,213,000 CYBER, worth approximately $1.1M.
> Root cause: The attacker exploited a configuration relying on a single DVN and a single signature for verification to forge a Cyber Chain → Solana message and mint 5,213,000 CYBER on Solana. The attacker then burned those tokens and used the legitimate return bridge flow to withdraw an equal amount of real CYBER from the CyberTokenAdapter escrow contract on Ethereum.
> Attacker addresses:
> Solana:
> 58ZgoAHMgfFPuzLkA6avW5nCh8vHibt1qDfCSvpPZvSo
> Solana helper:
> 6pnHXHtNXddyRYg15TJJrkW9VjMZnep5oj99CqdmfZxx
> Ethereum:
> 0xaf32a9db0b0ac8eaa860a43a9d32a1c9277277cc
> Ethereum:
> 0x73052e10334096b96deacd7bf6c6ec3b9b6c1b32
> ETH consolidation address:
> 0xe0a6bd0f2d391a3ee99a5a8550baa1b3347fe8b9
>
> 3️⃣ Chainflip
> Affected project: Chainflip @Chainflip—its Bitcoin and Ethereum vaults.
> Date: November 21, 2026
> Estimated loss: Approximately $12M, including 122 BTC, 520 ETH, 3,249,631 USDC, and 758,141 USDT.
> Root cause: Chainflip’s vaults use a 100-of-150 FROST threshold signing scheme, in which a threshold of validators jointly produces a signature authorizing transactions. The incident involved validator key compromise or signing abuse: the attacker obtained a valid Schnorr signature matching the aggregate public key in use at the time and drained vault assets through transferBatch.
> Attacker addresses:
> Ethereum attack transaction sender:
> 0x78fa4ac270db14886033e95b9b9e93f887aa2db0
> Ethereum recipient of stolen assets:
> 0x7d14a719072da80076b4edcec3e3401209d21eaf
> BTC recipient:
> bc1qm777twlzmelyutungyfw65ykn2l5kn68e6v4g6
>
> 4️⃣ Fluidkey
> Affected project: Fluidkey @fluidkey—52 user accounts across Ethereum, Base, BNB Chain, Polygon, Optimism, and Arbitrum.
> Date: November 20, 2026
> Estimated loss: Approximately $1.6M.
> Root cause: A session token leak combined with abuse of the signing workflow. The attacker exploited two vulnerabilities in Fluidkey’s self-hosted SigNoz deployment to read internal logs and steal user session tokens. They then created transfer requests on the server, marked them as approved, and raised the spending limits that determined when additional verification was required.
> The attacker triggered notifications through small payments. When users opened and unlocked the app, it signed the attacker-prepared transfers through its existing workflow for processing approved transfers.
> Attacker-linked addresses:
> 0x9140837ca5020c42fcbcb29a1af74293d6e5b9dc
> 0x72873fa107aba9310f220660a1e64e31b4de5cf2
> 0xeb6ed5a926a653ade23b62e9a582d2262f3f0980
> 0x9e5143a57ef1b609ef4b96248374e8cfdca940ae
> 0xdc70810d767b3109d8afa9678561738bdb4a2984
> 0x5afec19fb1d0e1a2a92ab0f3ccca246c59120021
>
> 5️⃣ Peapods Finance (PEAS)
> Affected project: Peapods Finance @PeapodsFinance—its L2 PEAS contract, bridge, and associated liquidity.
> Date: November 19, 2026
> Estimated loss: Approximately 254 ETH, worth $411,300.
> Root cause: A suspected deployer key compromise allowed the attacker to configure a malicious minter on L2, mint PEAS, bridge the tokens to Ethereum mainnet, and sell them.
> Attacker and associated recipient addresses:
> 0x9520e286f1a32945f0b9c0e3bb30685afbe387a2
> 0x6bde15fe1acca9bc20d90abad7e1a943a4d8df22

**Media:** photo https://pbs.twimg.com/media/HXzDlliacAAMRy4.jpg — no alt text provided
