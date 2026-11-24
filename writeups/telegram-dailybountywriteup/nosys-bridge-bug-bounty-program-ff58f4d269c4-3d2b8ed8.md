# Ēnosys Bridge Bug Bounty Program

- **Source URL:** https://enosys.medium.com/%C4%93nosys-bridge-bug-bounty-program-ff58f4d269c4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250523044313/https://enosys.medium.com/%C4%93nosys-bridge-bug-bounty-program-ff58f4d269c4
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2772 (id 2772)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Ēnosys Bridge Bug Bounty Program

FLRWrap is a committee-based EVM blockchain bridge that currently connects XDC’s Mainnet with Flare Network’s Songbird Canary network. It will soon connect Ethereum with Songbird and Ethereum with Flare Network’s Mainnet. FLRWrap enables the transfer of assets between two EVM networks in the form of “wrapped” assets. Our bridge’s smart contracts and frontend will be in scope for this bug bounty program.

# Assets In-Scope

## Smart contracts:

- **WrapMintBurn contract:**
[https://github.com/flrfinance/bridge-contracts/blob/40c13a468908b7415204999b13114daea71cba45/src/WrapMintBurn.sol](https://github.com/flrfinance/bridge-contracts/blob/40c13a468908b7415204999b13114daea71cba45/src/WrapMintBurn.sol)
**Deployed at:**
[https://songbird-explorer.flare.network/address/0xD5308A4Bb2D7121A26d0bd11257245F0EFDa2bc4](https://songbird-explorer.flare.network/address/0xD5308A4Bb2D7121A26d0bd11257245F0EFDa2bc4)
- **WrapDepositRedeem contract:**
[https://github.com/flrfinance/bridge-contracts/blob/40c13a468908b7415204999b13114daea71cba45/src/WrapDepositRedeem.sol](https://github.com/flrfinance/bridge-contracts/blob/40c13a468908b7415204999b13114daea71cba45/src/WrapDepositRedeem.sol)
**Deployed at:** [https://explorer.xinfin.network/address/xdcD5308A4Bb2D7121A26d0bd11257245F0EFDa2bc4](https://explorer.xinfin.network/address/xdcD5308A4Bb2D7121A26d0bd11257245F0EFDa2bc4)
- **WrapToken contract:**
[https://github.com/flrfinance/bridge-contracts/blob/40c13a468908b7415204999b13114daea71cba45/src/WrapToken.sol](https://github.com/flrfinance/bridge-contracts/blob/40c13a468908b7415204999b13114daea71cba45/src/WrapToken.sol)
**Deployed at:**
[https://songbird-explorer.flare.network/address/0xC54De96302981f87a6F80E4607593681B44d670c](https://songbird-explorer.flare.network/address/0xC54De96302981f87a6F80E4607593681B44d670c))
- **Multisig library:**
[https://github.com/flrfinance/bridge-contracts/blob/40c13a468908b7415204999b13114daea71cba45/src/libraries/Multisig.sol](https://github.com/flrfinance/bridge-contracts/blob/40c13a468908b7415204999b13114daea71cba45/src/libraries/Multisig.sol)
- **Wrap contract:**
[https://github.com/flrfinance/bridge-contracts/blob/40c13a468908b7415204999b13114daea71cba45/src/Wrap.sol](https://github.com/flrfinance/bridge-contracts/blob/40c13a468908b7415204999b13114daea71cba45/src/Wrap.sol)

## Frontend:

- **Frontend located at:**
[https://bridge.enosys.global/](https://bridge.enosys.global/)

# Impacts In-Scope

## Smart contracts

**Critical**

- Any governance voting result manipulation
- Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- Permanent freezing of funds
- Protocol insolvency
- Fee payment bypass

**High**

- Theft of unclaimed validator or protocol fees
- Permanent freezing of unclaimed validator or protocol fees
- Temporary freezing of funds (for >24 hours)

**Medium**

- Smart contract unable to operate due to lack of token funds (for >3 minutes)
- Block stuffing for profit
- Griefing (e.g., no profit motive for an attacker, but damage to the users or the protocol)
- Theft of gas
- Unbounded gas consumption

**Low**

- Contract fails to deliver promised returns, but doesn’t lose value

## Frontend

**Critical**

- Retrieve sensitive data/files from a running server (this does not include non-sensitive environment variables, open source code, or usernames) such as blockchain keys
- Taking down the application/website
- Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user
- Subdomain takeover with already-connected wallet interaction
- Direct theft of user funds

Malicious interactions with an already-connected wallet such as:

- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions

**High**

Injecting/modifying the static content on the target application without JavaScript (Persistent) such as:

- HTML injection without JavaScript
- Replacing existing text with arbitrary text.

Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:

- Email or password of the victim, etc.

Improperly disclosing confidential user information such as:

- Email address
- Phone number
- Physical address, etc.

Subdomain takeover without already-connected wallet interaction

**Medium**

- Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as.

Injecting/modifying the static content on the target application without Javascript (Reflected) such as:

- Reflected HTML injection
- Loading external site data
- Redirecting users to malicious websites (Open Redirect)

**Low**

Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction such as:

- Iframing leading to modifying the backend/browser state (must demonstrate impact with PoC)

Taking over broken or expired outgoing links such as:

- Social media handles, etc.

Temporarily disabling user to access target site, such as:

- Locking up the victim from login
- Cookie bombing, etc.

**Informational**

- Missing HTTP Headers without demonstrated impact
- UI/UX best practices recommendations

# Out-of-Scope Vulnerabilities

The following impacts and attack vectors are out of scope:

- Attacks that the reporter has already exploited themselves, leading to damage
- Attacks requiring access to leaked keys/credentials
- Attacks requiring access to privileged addresses (governance, strategist), except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible
- Broken link hijacking is out of scope

## Smart Contracts:

- Basic economic governance attacks (e.g., 51% attack)
- Lack of liquidity
- Best practice critiques
- Sybil attacks
- Centralization risks

## Frontend:

- Theoretical impacts without any proof or demonstration
- Content spoofing / Text injection issues
- Self-XSS
- Captcha bypass using OCR
- CSRF with no security impact (logout CSRF, change language, etc.)
- Missing HTTP Security Headers (such as X-FRAME-OPTIONS) or cookie security flags (such as “httponly”)
- Server-side information disclosure such as IPs, server names, and most stack traces
- Vulnerabilities used to enumerate or confirm the existence of users or tenants
- Vulnerabilities requiring unlikely user actions
- URL Redirects (unless combined with another vulnerability to produce a more severe vulnerability)
- Lack of SSL/TLS best practices
- Attacks involving DDoS
- Attacks requiring privileged access from within the organization
- SPF records for email domains
- Feature requests
- Best practices

# Existing Audits and Known Issues:

- WatchPug Audits:

1. [https://www.hacknote.co/17c261f7d8fWbdml/1864eff7124wF20G](https://www.hacknote.co/17c261f7d8fWbdml/1864eff7124wF20G#n_0)
2. [https://www.hacknote.co/17c261f7d8fWbdml/187022e732aVega9](https://www.hacknote.co/17c261f7d8fWbdml/187022e732aVega9)
3. [https://www.hacknote.co/17c261f7d8fWbdml/1877a33caa29y5CD](https://www.hacknote.co/17c261f7d8fWbdml/1877a33caa29y5CD)

# Rules of Engagement:

The following activities are prohibited:

- Any testing with mainnet or public testnet contracts; all testing should be done on private testnets
- Attempting phishing or other social engineering attacks
- Any attempt to compromise validator, admin, or pauser keys
- Denial of Service attacks
- Public disclosure of an unpatched vulnerability
- Automated testing of services that generates significant amounts of traffic to our frontend
- Disclosing vulnerabilities without the approval of the Enosys team
- Attempting to sell vulnerability information or exploits

# Submission

To be considered for a reward, all bug reports must contain the following:

- Description of the suspected vulnerability
- Steps to reproduce the issue
- Your name and/or colleagues if you wish to be later recognized
- (Optional) A patch and/or suggestions to resolve the vulnerability

Please submit your bug bounty report by emailing us at [bounty@enosys.global](http://bounty@enosys.global).

# Program Reward Amounts

**Critical:** $3,000 USD

**High:** $2,000 USD

**Medium:** $1,000 USD

**Low:** $500 USD
