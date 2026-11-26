# 📱 Android Flaw Enables Wallet Seed Theft

- **Source URL:** https://www.theblock.co/post/393154/ledger-researchers-expose-android-flaw-enabling-theft
- **Fetched from:** https://web.archive.org/web/20260312190551/https://www.theblock.co/post/393154/ledger-researchers-expose-android-flaw-enabling-theft
- **Fetched:** 2026-11-26
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1333 (id 1333)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Ledger researchers expose Android flaw enabling wallet seed theft in seconds

#### Quick Take

- Ledger’s Donjon team identified a critical flaw in MediaTek’s secure boot chain that could potentially enable the extraction of device PINs and wallet seed phrases in about 45 seconds.
- In a proof-of-concept test, the exploit recovered sensitive wallet data from apps including Trust Wallet, Kraken Wallet and Phantom.

### We'd love your feedback.

Ledger's internal security team has identified a vulnerability in the firmware of Android phones using MediaTek processors that could enable an attacker to extract a device's PIN and the private keys for several crypto wallets in under a minute.

The exploit, discovered by Ledger's Donjon research unit, targets a weakness in MediaTek's secure boot chain.

According to a statement shared with The Block, an attacker with physical access to a phone can connect it via USB before the operating system loads, extract the cryptographic keys protecting Android's full-disk encryption, and then decrypt the storage offline.

The vulnerability could potentially affect an estimated 25% of Android phones, the researchers said, including models from manufacturers that use MediaTek chips and Trustonic's trusted execution environment.

"This research proves what we've long warned: smartphones were never designed to be vaults," Ledger Chief Technology Officer Charles Guillemet said in the statement. "While this can be patched, and we encourage all users to update with the latest security fixes provided by MediaTek and phone manufacturers, it shows the challenge of storing secrets on non-secure devices. If your crypto sits on a phone, it's only as safe as the weakest link in that phone's hardware, firmware, or software."

Guillemet said the team's goal in publishing the research is to give the industry time to patch such flaws before they are exploited by malicious actors. Donjon, Ledger's in-house team of white-hat hackers, has previously disclosed vulnerabilities affecting Android chips and PIN bypass attacks in competing wallets, per the statement.

The report comes as attackers continue to target user wallets at scale. Infrastructure attacks, including private-key thefts, seed-phrase heists, and front-end hijacks, accounted for more than 80% of the [$2.1 billion stolen in the first half of 2025](https://web.archive.org/web/20260312190551/https://www.theblock.co/post/360084/front-end-and-private-key-exploits-drove-over-2-billion-in-crypto-thefts-during-h1-2025-report), according to a report from blockchain intelligence firm TRM Labs.

For the full year, losses from crypto theft [exceeded $3.41 billion](https://web.archive.org/web/20260312190551/https://www.theblock.co/post/382477/crypto-hack-2025-chainalysis), Chainalysis data shows. The blockchain intelligence firm noted a significant increase in personal wallet compromises, which grew from 7.3% of total stolen value in 2022 to 44% in 2024, affecting more than 158,000 cases.

Disclaimer: The Block is an independent media outlet that delivers news, research, and data. As of November 2023, Foresight Ventures is a majority investor of The Block. Foresight Ventures invests in [other companies](https://web.archive.org/web/20260312190551/https://www.foresightventures.com/portfolio) in the crypto space. Crypto exchange Bitget is an anchor LP for Foresight Ventures. The Block continues to operate independently to deliver objective, impactful, and timely information about the crypto industry. Here are our current [financial disclosures](https://web.archive.org/web/20260312190551/https://www.theblock.co/financial-disclosures).

© 2026 The Block. All Rights Reserved. This article is provided for informational purposes only. It is not offered or intended to be used as legal, tax, investment, financial, or other advice.
