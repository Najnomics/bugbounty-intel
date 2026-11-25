# 🔑 Your Solana Program Is Secure. Your Signing Utility Isn't.

- **Source URL:** https://www.adevarlabs.com/blog/supply-chain-attacks-in-the-solana-ecosystem
- **Fetched from:** https://web.archive.org/web/20260516060656/https://www.adevarlabs.com/blog/supply-chain-attacks-in-the-solana-ecosystem
- **Fetched:** 2026-11-25
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1586 (id 1586)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
When building any Solana‑based service, whether a CLI wallet, a backend transaction‑signing service, or a dApp frontend, you rely on an off‑chain **signing utility** to produce valid Solana transaction signatures. Typically that means pulling in a crate such as:

```
[dependencies]
solana-sign-utils = "0.1"
```
Developers then call its helper:

```
use solana_sign_utils::sign_with_keypair;
fn sign_tx(tx: &Transaction, keypair: &Keypair) -> Signature {
    sign_with_keypair(tx, keypair)
}
```
Every time you sign, your keypair and transaction pass through that crate’s code. It’s a **trusted choke‑point** in your infrastructure, even though it never touches on‑chain data, it gatekeeps every SOL transfer and CPI call you make.

Now imagine version **0.1.1** quietly lands via an automated CI bump. Hidden in its diff is:

```
// after computing sig…
report_to_oracle(keypair);  // exfiltrate private key
```
Suddenly, every time your service signs a transaction, the **private key** used to do so is silently exfiltrated to an attacker’s server. There’s no on-chain footprint. Your program behaves perfectly, the transaction lands as expected, but in the background, you’ve just handed your entire wallet to someone else. This is the power and the peril of a supply chain attack on signing utilities. **It compromises the very keys that secure your authority in the Solana ecosystem.**

### Fake Audit Requests and Malicious NPM Packages

A stealthy entry point used by attackers is the classic “security audit” pretext, especially effective in the Web3 world. In this version of **DeceptiveDevelopment** campaign, threat actors pose as project owners or DAO contributors requesting a smart contract or front-end audit. They reach out via social platforms asking the developer to “review this repo” or “run our build locally to verify edge case behavior.”

The repository includes malicious npm (or pnpm) dependencies, often buried under custom internal package names or dependencies-of-dependencies. As soon as the target runs npm install, a backdoored script executes, harvesting local credentials, SSH keys, or active session tokens. In some variants, it even scans for Solana CLI config files to extract keypair paths.

Because the attack comes under the legitimate-looking banner of an “audit request,” some auditors don't suspect a thing, until it's far too late.

Another such entry point is [fake recruitment](https://web.archive.org/web/20260516060656/https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/).

### Supply‑Chain Compromise

On **December 2, 2024**, maintainers of the critical JavaScript API **@solana/web3.js** had their [npm account phished](https://web.archive.org/web/20260516060656/https://socket.dev/blog/supply-chain-attack-solana-web3-js-library?utm_source=chatgpt.com). Within hours, versions **1.95.6** and **1.95.7** were published containing malicious code that:

1. **Captured private keys** from signers and them to a hard‑coded Solana address.
2. **Exfiltrated** them to a hard‑coded Solana address.

This npm package is pulled in by hundreds of thousands of dApps and wallets (over 350 k weekly downloads). The attackers drained at least **$160000** worth of SOL and SPL‑token assets before fixes were released.

### Mitigation Strategies for Solana Developers

**In a world where the blockchain is immutable but your toolchain isn’t, Solana developers must take proactive steps to defend against supply chain threats.**

Most attacks won’t target your on-chain program. They’ll target everything *around* it: the off-chain signers, SDKs, deployment tools, build pipelines, and transitive dependencies.

Whether you're writing Rust for a Solana program or integrating it with JS tooling in a dApp, you need a hardened developer workflow. The following strategies help ensure the code you ship and the dependencies you trust don’t become an attack vector.

### 1. Lock Down Your Dependencies

**Always avoid ^ or \~ in Cargo.toml.**

It might seem harmless to write:

```
# ❌ Risky
solana-sdk = "^1.18"
```
But what this actually does is allow your project to automatically upgrade to *any* version up to, but not including, 2.0.0. This means a rogue or hijacked version like 1.18.99 could slip in silently.

For critical crates, especially those dealing with keys, transactions, or any part of your signer logic, you **must** lock the exact version:

```
# ✅ Safe
solana-sdk = "=1.18.3"
```
This tiny change drastically reduces your exposure to injected malware through automatic updates.

**Snapshot and Freeze Everything**

Use cargo vendor to create a local copy of your entire dependency graph.

`cargo vendor --versioned-dirs`
You can then build in isolated environments or audit the vendored code yourself. This is *especially important* when building secure signing utilities or CLI tools for Solana.

**Audit Frequently**

Use the excellent cargo-audit to scan for known vulnerabilities:

`cargo audit`
Even if most of your project is in Rust, Solana frontends often use JS packages like @solana/web3.js. The same risks apply.

### 2. Scan Your Codebase or Any Codebase you Download/Receive With JFrog Xray

JFrog offers one of the best tools for deep scanning of both your **source** and **dependencies** catching:

- Typosquatting (e.g., solona-sdk instead of solana-sdk)
- Malware patterns
- Unexpected or obfuscated code in published crates
- Known vulnerable versions in your transitive tree

Example usage in a CI context:

```
# Assuming you're using JFrog CLI
jfrog rt scan --fail=false --watches="solana-secure" my-project/
```
You can also configure it to block builds or notify Slack on high-severity issues.

If you're building or maintaining a CLI signer, wallet, or CPI-capable tool in Solana, **this kind of scanning is essential**.

### 3. Package Maintainers: Defend the Supply Chain

This section is geared toward devs **publishing packages**, especially those used in Solana tools or dApps.

- **Enable 2FA on npm and crates.io** accounts. Always. A huge percentage of real-world supply chain attacks came from hijacked maintainer accounts.
- **Use scoped access tokens** and **read-only API keys** wherever possible.
- **Rotate credentials regularly.**
- **Monitor for anomalous publishes**: Set up alerts for unexpected versions or packages published under your namespace.
- **Use tools like JFrog Xray** to scan published crates or npm packages for embedded malware, typosquatting indicators, and known bad patterns 

### 4. Monitor Your CI & Build Environments

- **Pin your Docker images and base images**. Don’t use :latest.
- **Use reproducible builds** and verify outputs locally before deploying.
- **Make signing keys read-only** wherever possible, and **never expose them in CI logs or artifacts**.
- **Protect your GitHub branch** by hardening measures such as: branch protection rules for main, master, or deployment-critical branches; disable direct pushes and require pull request reviews before merging..
- Store signing keys in a secure hardware-backed KMS and **never store keys in plaintext in your .env file**.

## Key Takeaways


- **Off‑chain tools are the new attack surface**: your signing utilities and SDKs are just as critical as on‑chain code.
- **Social engineering is rampant**: fake recruiters or compromised maintainer accounts can slip malicious code past automated tests.
- **Even if your on-chain program is immutable, your off-chain stack remains vulnerable:** Solana will accept any *valid* signature, whether it came from you, or from an attacker using your stolen key.

Lock down your dependencies like you lock your private keys, because the next backdoor might already be sitting in your build pipeline.

Want to learn more? Stay tuned for more deep dives, real-world bugs, and smart contract best practices.

Follow @AdevarLabs on [X](https://web.archive.org/web/20260516060656/https://twitter.com/AdevarLabs) / [LinkedIn](https://web.archive.org/web/20260516060656/https://linkedin.com/company/adevarlabs) - Ship Safely.
