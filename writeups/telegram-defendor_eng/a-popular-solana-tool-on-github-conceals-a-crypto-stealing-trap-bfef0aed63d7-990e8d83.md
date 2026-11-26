# 🛑 Dangerous Solana bot on GitHub steals crypto assets

- **Source URL:** https://slowmist.medium.com/a-popular-solana-tool-on-github-conceals-a-crypto-stealing-trap-bfef0aed63d7
- **Fetched from:** https://web.archive.org/web/20251231190129/https://slowmist.medium.com/a-popular-solana-tool-on-github-conceals-a-crypto-stealing-trap-bfef0aed63d7
- **Fetched:** 2026-11-26
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/275 (id 275)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# A Popular Solana Tool on GitHub Conceals a Crypto-Stealing Trap

**Author:** Thinking

**Editor:** Liz

## Background

On July 2, 2025, a victim contacted the SlowMist Security Team seeking assistance in analyzing the cause behind the theft of assets from their wallet. The incident was triggered the previous day when the victim used an open-source project hosted on GitHub — zldp2002/solana-pumpfun-bot — after which their crypto assets were stolen.

## Investigation

We immediately launched an investigation into the incident. Our first step was to visit the project’s GitHub repository: https://github.com/zldp2002/solana-pumpfun-bot. We noticed that the project had a relatively high number of stars and forks. However, all code commits across its directories were made around three weeks ago, showing clear irregularities and lacking the consistent update pattern of a legitimate project.

This is a Node.js-based project. We began by analyzing its dependencies and discovered that it referenced a third-party package called `crypto-layout-utils`.

Upon further inspection, we found that this package had already been removed from the official NPM registry. Moreover, the version specified in the `package.json` file did not appear in NPM’s historical records. Our initial judgment was that this was a suspicious component, and it could no longer be downloaded via the official NPM registry. This raised the question: how did the victim obtain this malicious dependency?

Continuing our investigation, we located a critical clue in the `package-lock.json` file: the attacker had replaced the NPM source link for `crypto-layout-utils` with the following URL: [https://github.com/sjaduwhv/testing-dev-log/releases/download/1.3.1/crypto-layout-utils-1.3.1.tgz](https://web.archive.org/web/20251231190129/https://github.com/sjaduwhv/testing-dev-log/releases/download/1.3.1/crypto-layout-utils-1.3.1.tgz)

We downloaded the suspicious package `crypto-layout-utils-1.3.1` and found it to be heavily obfuscated using jsjiami.com.v7, making analysis more difficult.

After de-obfuscation, we confirmed that this was indeed a malicious NPM package. The attacker had embedded logic within `crypto-layout-utils-1.3.1` to scan the victim’s local files. If it detected wallet-related content or private keys, it would upload this sensitive information to a server controlled by the attacker — `githubshadow.xyz`.

The malicious NPM package scans for sensitive files and directories:

The malicious NPM package uploads private key content or files:

As we further explored the attack methodology, we found that the project author (https://github.com/zldp2002/) likely controlled a batch of GitHub accounts. These accounts were used to fork the malicious project and distribute the malware, while also artificially inflating the number of forks and stars to attract more users — thereby expanding the distribution scope of the malicious code.

We identified multiple forked repositories exhibiting similar malicious behaviors. Some versions even adopted another malicious package named `bs58-encrypt-utils-1.0.3`.

This package was created on June 12, 2025. We believe the attacker began distributing malicious NPM modules and Node.js projects at that time. After `bs58-encrypt-utils` was removed from the NPM registry, the attacker switched to a new strategy — distributing the malware by replacing the NPM download link with a custom one.

Additionally, by using the on-chain AML and tracking tool MistTrack, we discovered that one of the attacker-controlled addresses transferred stolen funds to the FixedFloat exchange.

## Conclusion

In this attack, the perpetrator disguised a malicious program as a legitimate open-source project (`solana-pumpfun-bot`) and lured users into downloading and running it. The artificially inflated popularity of the project masked its malicious intent, causing users to run a Node.js project with embedded malicious dependencies — unknowingly exposing their private keys and leading to asset theft.

This attack chain involved multiple GitHub accounts working in concert, which not only broadened its reach but also enhanced its credibility — making it highly deceptive. The attack leveraged a combination of social engineering and technical manipulation, making it difficult to fully defend against even within well-structured organizations.

We urge developers and users to exercise extreme caution when dealing with unfamiliar GitHub projects, especially those that involve wallets or private key operations. If testing is necessary, we recommend using isolated environments with no access to sensitive data.

### Malicious Package Information

**Malicious Node.js GitHub Repositories:**

- 2723799947qq2022/solana-pumpfun-bot
- 2kwkkk/solana-pumpfun-bot
- 790659193qqch/solana-pumpfun-bot
- 7arlystar/solana-pumpfun-bot
- 918715c83/solana-pumpfun-bot
- AmirhBeigi7zch6f/solana-pumpfun-bot
- asmaamohamed0264/solana-pumpfun-bot
- bog-us/solana-pumpfun-bot
- edparker89/solana-pumpfun-bot
- ii4272/solana-pumpfun-bot
- ijtye/solana-pumpfun-bot
- iwanjunaids/solana-pumpfun-bot
- janmalece/solana-pumpfun-bot
- kay2x4/solana-pumpfun-bot
- lan666as2dfur/solana-pumpfun-bot
- loveccat/solana-pumpfun-bot
- lukgria/solana-pumpfun-bot
- mdemetrial26rvk9w/solana-pumpfun-bot
- oumengwas/solana-pumpfun-bot
- pangxingwaxg/solana-pumpfun-bot
- Rain-Rave5/solana-pumpfun-bot
- wc64561673347375/solana-pumpfun-bot
- wj6942/solana-pumpfun-bot
- xnaotutu77765/solana-pumpfun-bot
- yvagSirKt/solana-pumpfun-bot
- VictorVelea/solana-copy-bot
- Morning-Star213/Solana-pumpfun-bot
- warp-zara/solana-trading-bot
- harshith-eth/quant-bot

**Malicious NPM Packages:**

- `crypto-layout-utils`
- `bs58-encrypt-utils`

**Malicious NPM Package Download URL:**

https://github.com/sjaduwhv/testing-dev-log/releases/download/1.3.1/crypto-layout-utils-1.3.1.tgz

**Malicious Package Upload Server:**

`githubshadow.xyz`

## About SlowMist

SlowMist is a blockchain security firm established in January 2018. The firm was started by a team with over ten years of network security experience to become a global force. Our goal is to make the blockchain ecosystem as secure as possible for everyone. We are now a renowned international blockchain security firm that has worked on various well-known projects such as HashKey Exchange, OSL, MEEX, BGE, BTCBOX, Bitget, BHEX.SG, OKX, Binance, HTX, Amber Group, Crypto.com, etc.

SlowMist offers a variety of services that include but are not limited to security audits, threat information, defense deployment, security consultants, and other security-related services. We also offer AML (Anti-money laundering) software, MistEye (Security Monitoring) , SlowMist Hacked (Crypto hack archives), FireWall.x (Smart contract firewall) and other SaaS products. We have partnerships with domestic and international firms such as Akamai, BitDefender, RC², TianJi Partners, IPIP, etc. Our extensive work in cryptocurrency crime investigations has been cited by international organizations and government bodies, including the United Nations Security Council and the United Nations Office on Drugs and Crime.

By delivering a comprehensive security solution customized to individual projects, we can identify risks and prevent them from occurring. Our team was able to find and publish several high-risk blockchain security flaws. By doing so, we could spread awareness and raise the security standards in the blockchain ecosystem.
