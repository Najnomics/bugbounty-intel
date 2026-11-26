# 🛡 Malicious Solana Bot Steals Private Keys from .env Files

- **Source URL:** https://slowmist.medium.com/threat-intelligence-an-analysis-of-a-malicious-solana-open-source-trading-bot-ab580fd3cc89
- **Fetched from:** https://web.archive.org/web/20251231145536/https://slowmist.medium.com/threat-intelligence-an-analysis-of-a-malicious-solana-open-source-trading-bot-ab580fd3cc89
- **Fetched:** 2026-11-26
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/312 (id 312)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Threat Intelligence: An Analysis of a Malicious Solana Open-source Trading Bot**

**Author:** Joker & Thinking

**Editor:** KrsMt

## Background

In early July 2025, the SlowMist security team received a request from a victim seeking help in analyzing the cause behind the theft of their crypto assets. Investigation revealed that the incident stemmed from the use of an open-source project hosted on GitHub — `zldp2002/solana-pumpfun-bot` — which triggered a hidden coin-stealing mechanism. For more details, refer to our previous analysis:

**"**[A Popular Solana Tool on GitHub Conceals a Crypto-Stealing Trap](https://web.archive.org/web/20251231145536/https://slowmist.medium.com/a-popular-solana-tool-on-github-conceals-a-crypto-stealing-trap-bfef0aed63d7)**"**

Recently, another user fell victim after using a similar open-source project — `audiofilter/pumpfun-pumpswap-sniper-copy-trading-bot` — resulting in stolen assets and a follow-up request for assistance from the SlowMist team. In response, our team conducted a deeper technical analysis of this attack vector.

## Analysis

### Static Analysis

We began with a static analysis to identify the traps embedded by the attacker. Our findings revealed suspicious code within the configuration file located at:

`/src/common/config.rs`
The focus was on the `create_coingecko_proxy()` method.

From the code, it is evident that the `create_coingecko_proxy()` method first invokes `import_wallet()`, which in turn calls `import_env_var()` to obtain the private key.

The `import_env_var()` function is primarily used to retrieve environment variable configurations from the `.env` file.

If the environment variable exists, it is returned directly. If not, the code enters the `Err(e)` branch and logs an error message. Notably, it contains a `loop {}` with no exit condition, which causes resource exhaustion by entering an infinite loop.

Sensitive data such as the `PRIVATE_KEY` is stored in the `.env` file.

Back in `import_wallet()`, once `import_env_var()` retrieves the `PRIVATE_KEY`, the malicious code checks the length of the key:

- If the key is **less than 85 characters**, it logs an error and enters a `loop {}` again, causing infinite resource consumption and preventing the program from exiting.
- If the key is **greater than 85 characters**, the code uses the Solana SDK to decode the Base58 string into a `Keypair` object, which contains the private key.

The private key is then wrapped in an `Arc` (Atomic Reference Counted pointer) to allow safe sharing across threads.

Returning to `create_coingecko_proxy()`, after successfully obtaining the private key, the malicious code proceeds to decode a hardcoded malicious URL.

The method fetches an encoded constant named `HELIUS_PROXY` (the attacker’s server address).

Using the `bs58` decoding library, the code decodes `HELIUS_PROXY` into a byte array and converts it into a UTF-8 string via `from_utf8()`.

The decoded attacker-controlled endpoint is:

`http://103.35.189.28:5000/api/wallets`
After decoding the URL, the code creates an HTTP client and converts the extracted `payer` private key into a Base58 string via `to_base58_string()`.

Next, it builds a JSON payload, embeds the private key, and sends it via a POST request to the attacker’s server. The response is ignored, regardless of success or failure, to avoid alerting the user.

Additionally, the `create_coingecko_proxy()` method includes legitimate-looking functionality such as price retrieval, which helps mask its malicious intent. The method name itself is also misleading, adding to the deception.

This method is executed at application startup, as part of the configuration initialization process in the `main()` function located in `main.rs`.

The `new()` method in `src/common/config.rs` loads the `.env` file and invokes `create_coingecko_proxy()`.

IP analysis shows that the attacker’s server is hosted in the United States:

It was observed that the project was recently updated on GitHub (July 17, 2025), with the main changes made to the configuration file `config.rs` under the `src` directory.

In the `src/common/config.rs` file, the original encoded value of `HELIUS_PROXY` (the attacker’s server address) had been replaced with a new encoded string.

By decoding the original value using a script, the previously used server address was revealed as:

```
// Original HELIUS_PROXY encoded string:
2HeX3Zi2vTf1saVKAcNmf3zsXDkjohjk3h7AsnBxbzCkgTY99X5jomSUkBCW7wodoq29Y
// Decoded malicious server address:
https://storebackend-qpq3.onrender.com/api/wallets
```
### Dynamic Analysis

To better visualize the malicious behavior and asset exfiltration process, we conducted dynamic analysis. We began by writing a Python script to generate a test Solana keypair (public and private keys).

We then deployed a local HTTP server capable of receiving POST requests.

Next, we modified the malicious project’s code by replacing the original `HELIUS_PROXY` (the attacker’s server address) with our own test server address — properly encoded using the same method — and substituted the `.env` file’s `PRIVATE_KEY` with our newly generated test private key.

Upon launching the malicious project, we monitored the test server’s logs.

As expected, the test server successfully received a POST request from the malicious project. The payload contained JSON-formatted data, including the test `PRIVATE_KEY` — confirming the theft behavior.

## Indicators of Compromise (IoCs)

**IP Addresses:**

- `103.35.189.28`

**Domains:**

- `storebackend-qpq3.onrender.com`

**SHA256 Hashes:**

- 07f0364171627729788797bb37e0170a06a787a479666abf8c80736722bb79e8 — pumpfun-pumpswap-sniper-copy-trading-bot-master.zip
- ace4b1fc4290d6ffd7da0fa943625b3a852190f0aa8d44b93623423299809e48 — pumpfun-pumpswap-sniper-copy-trading-bot-master/src/common/config.rs

**Malicious Repository:**

- https://github.com/audiofilter/pumpfun-pumpswap-sniper-copy-trading-bot

**Similar Implementations:**

- https://github.com/BitFancy/Solana-MEV-Bot-Optimized
- https://github.com/0xTan1319/solana-copytrading-bot-rust
- https://github.com/blacklabelecom/SAB-4
- https://github.com/FaceOFWood/SniperBot-Solana-PumpSwap
- https://github.com/Alemoore/Solana-MEV-Bot-Optimized
- https://github.com/TopTrenDev/Raypump-Executioner-Bot
- https://github.com/deniyuda348/Solana-Arbitrage-Bot-Flash-Loan

## Conclusion

In this incident, the attacker disguised their malicious code as a legitimate open-source project to lure users into executing it. Once launched, the program silently extracted sensitive data — specifically, the private key stored in the local `.env` file — and transmitted it to a server controlled by the attacker.

This type of attack often leverages **social engineering**, exploiting users’ trust in open-source repositories. A single lapse in caution can lead to severe asset loss.

**Recommendations:**

- Developers and users should remain highly vigilant when interacting with GitHub repositories from unknown sources — especially those involving wallet or private key operations.
- If running or debugging such tools is necessary, do so within a **sandboxed environment** that contains no sensitive data.
- Avoid blindly executing unfamiliar programs or scripts.

For further reference and guidance on protecting yourself in the blockchain space, we recommend the SlowMist publication:

**“Blockchain Dark Forest Selfguard Handbook”**

[https://github.com/slowmist/Blockchain-dark-forest-selfguard-handbook/blob/main/README\_CN.md](https://web.archive.org/web/20251231145536/https://github.com/slowmist/Blockchain-dark-forest-selfguard-handbook/blob/main/README_CN.md)

## About SlowMist

SlowMist is a blockchain security firm established in January 2018. The firm was started by a team with over ten years of network security experience to become a global force. Our goal is to make the blockchain ecosystem as secure as possible for everyone. We are now a renowned international blockchain security firm that has worked on various well-known projects such as HashKey Exchange, OSL, MEEX, BGE, BTCBOX, Bitget, BHEX.SG, OKX, Binance, HTX, Amber Group, Crypto.com, etc.

SlowMist offers a variety of services that include but are not limited to security audits, threat information, defense deployment, security consultants, and other security-related services. We also offer AML (Anti-money laundering) software, MistEye (Security Monitoring) , SlowMist Hacked (Crypto hack archives), FireWall.x (Smart contract firewall) and other SaaS products. We have partnerships with domestic and international firms such as Akamai, BitDefender, RC², TianJi Partners, IPIP, etc. Our extensive work in cryptocurrency crime investigations has been cited by international organizations and government bodies, including the United Nations Security Council and the United Nations Office on Drugs and Crime.

By delivering a comprehensive security solution customized to individual projects, we can identify risks and prevent them from occurring. Our team was able to find and publish several high-risk blockchain security flaws. By doing so, we could spread awareness and raise the security standards in the blockchain ecosystem.
