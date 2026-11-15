# 🔍 $39.5M in Exolix Swap History Exposed via Broken API

- **Source URL:** https://www.rastersec.com/blog/exolix-swapper-dump
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1683 (id 1683)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# $40M in Exolix Swaps Exposed via API Vulnerability

When I first started developing [SSHwap](https://www.sshwap.com), Exolix seemed like the go-to choice. They have low fees and presence in the Monero community (their marketing staff frequents MoneroTopia and MoneroKon). I ended up not integrating them for two reasons.

First, their partner panel isn’t functional. Though negligible, a few Euros of commission disappeared into their coffers, and their staff were absolutely unhelpful and generally unprofessional.

Second and most importantly, their API suffers from broken access control which allows anybody to dump the swap history of any integrating partner. Across seven integrations, I enumerated **355,944 transactions** spanning January 2025 through May 2026.

| Partner | Total Txns | Successful | Success Rate | USD Volume | 
|---|---|---|---|---|
| Edge | 329,532 | 24,340 | 7.4% | $24,951,632 | 
| Exodus Non-US | 5,376 | 3,617 | 67.3% | $6,078,750 | 
| Monerujo | 11,247 | 4,419 | 39.3% | $4,578,363 | 
| BTCPay Server Plugins | 6,374 | 1,425 | 22.4% | $1,947,503 | 
| Exodus US | 1,681 | 1,231 | 73.2% | $1,650,228 | 
| Temple Wallet | 1,205 | 530 | 44.0% | $159,229 | 
| EGToken.io | 529 | 286 | 54.1% | $151,944 | 
| **Total** | **355,944** | **35,848** | **10.1%** | **$39,517,649** | 

## Broken Access Control

### Finding the API Keys

Exolix provides partners with API keys to integrate swaps into their apps. The integrations usually embed them during build time or hardcode them in public code repositories. Finding the keys is trivial and proves why it is a good idea to make your own API wrapper and store keys server-side.

Exolix issues two types of API keys. The first is a manually generated opaque string like `FqoLY9SOGyZCq...tvoRCLtbiUQBnYGup4zTJsA3`. These are issued directly by Exolix staff to select partners (e.g. Cake Wallet) and are **not vulnerable**. The second type is a JWT issued through the partner panel.

The JWT payload contains the partner’s email, a user ID (`sub`), and an expiration set 5 years out. These JWTs grant full read access to the partner’s transaction history via `GET /api/v2/transactions`, and this is the vulnerable key type.

For Android apps like **Edge** and **Monerujo**, decompiling the APK with [apktool](https://apktool.org/) or [jadx](https://github.com/skylot/jadx) reveals the keys in plain text, hardcoded in configuration files or source code. For open-source integrations like **BTCPay Server Plugins** and **Exodus**, the keys are sitting right in their public Git repositories.

In every case, the JWT key is not scoped or restricted. It grants full read access to the partner’s entire transaction history, including deposit addresses, withdrawal addresses, amounts, timestamps, on-chain transaction hashes, and swap statuses. There is no rate limiting or IP restriction to speak of. Later on, Exolix staff implemented WAF rules using Cloudflare instead of solving the root problem.

### Dumping Partners’ Swap History via Exolix API

The Exolix API endpoint `GET /api/v2/transactions` accepts pagination parameters and returns all transactions associated with the authenticating API key. Dumping a partner’s entire swap history is a single curl command:

```
curl -s 'https://exolix.com/api/v2/transactions?page=1&size=100' \
  -H 'Authorization: Bearer eyJhbGciOi...REDACTED'
```
By iterating through pages, a complete dump can be obtained. Here is what a single swap record looks like (addresses and transaction hashes redacted):

```
{
  "id": "4e819f9b9406c4",
  "amount": 0.00034673,
  "amountTo": 0.06725753,
  "coinFrom": {
    "coinCode": "BTC",
    "coinName": "Bitcoin",
    "network": "BTC",
    "networkName": "Bitcoin"
  },
  "coinTo": {
    "coinCode": "XMR",
    "coinName": "Monero",
    "network": "XMR",
    "networkName": "Monero"
  },
  "createdAt": "2026-04-27T14:38:38.502Z",
  "depositAddress": "bc1q...REDACTED",
  "withdrawalAddress": "465...REDACTED",
  "refundAddress": "bc1q...REDACTED",
  "hashIn": {
    "hash": "e3aa69...REDACTED",
    "link": "https://mempool.space/tx/e3aa69...REDACTED"
  },
  "hashOut": {
    "hash": "169be9...REDACTED",
    "link": "https://monerohash.com/explorer/search?value=169be9...REDACTED"
  },
  "rate": 193.97666772,
  "rateType": "fixed",
  "status": "success",
  "source": "api",
  "bonus": {
    "userId": 12874,
    "amount": 2.6004748e-06,
    "transactionId": "4e819f9b9406c4",
    "createdAt": "2026-04-27T14:41:21.175Z"
  }
}
```
Every field an investigator would need is here: the deposit address where the user sent BTC, the withdrawal address where Exolix delivered XMR, on-chain transaction hashes for both legs, exact amounts and exchange rate, and a timestamp. The `bonus.userId` field identifies the partner integration (in this case, Edge).

Privacy coins dominate the dataset. XMR is the #1 source coin by USD volume ($13M) and the #2 destination ($7.4M). The top three trading pairs by volume all involve Monero. Privacy-focused coins (XMR, ARRR, ZANO, ZEC) have above-average success rates, indicating more intentional users.

## Exolix’s Response

At last, I contacted them to disclose the vulnerability. They claimed it was in fact a feature, not a bug, and that it was requested by their partners. I did not hear back from any of the affected partners. I would guess they aren’t even aware of this “feature”.

Their response references an email address I have no affiliation with. This must mean there is another person who is aware of this vulnerability and is abusing it.

Instant swappers exist to break the chain of custody between two assets. This dump preserves every link: deposit addresses, withdrawal addresses, on-chain hashes for both legs, exact amounts, and timestamps. For $39.5 million worth of completed swaps, the privacy guarantee of using a no-KYC swapper is gone. Law enforcement and blockchain analysis firms like Chainalysis routinely subpoena exchanges for this kind of data. With Exolix’s broken access control, no subpoena is needed.

The top trading pairs make the value of this data clear. Nearly every high-volume pair involves a privacy coin:

| Pair | Txns | USD Volume | Avg Swap | 
|---|---|---|---|
| BTC → XMR | 5,520 | $4,333,059 | $785 | 
| XMR → BTC | 3,179 | $4,871,572 | $1,532 | 
| XMR → USDT | 2,304 | $4,621,007 | $2,006 | 
| USDT → BTC | 1,631 | $1,310,524 | $804 | 
| LTC → XMR | 1,534 | $583,824 | $381 | 
| XMR → ETH | 1,058 | $1,417,093 | $1,339 | 
| XMR → LTC | 859 | $484,761 | $564 | 
| BTC → XRP | 762 | $844,051 | $1,108 | 
| ETH → XMR | 707 | $544,360 | $770 | 
| XMR → SOL | 669 | $494,040 | $738 | 
| USDT → XMR | 608 | $1,110,412 | $1,826 | 

USD volumes estimated using daily closing prices from Kraken and CryptoCompare, covering 206 of 274 unique coins (99.89% of successful transactions priced). Stablecoin amounts taken at face value.

Of the top 11 pairs by transaction count, 9 involve Monero on one side. The top three pairs alone account for $13.8 million in volume. Each of those swaps links a transparent-chain address (BTC, USDT, ETH) to a Monero address, with exact amounts and on-chain hashes. For anyone trying to trace Monero transactions, this is the missing piece that on-chain analysis cannot provide.

Is Exolix a honeypot? The vulnerability is too obvious for a service whose entire value proposition is swap privacy. If you wanted to build a database linking Monero users to their transparent-chain counterparts, running a popular instant swapper and leaving the API wide open would be an effective way to do it. None of this proves intent. It could just be incompetence. But the effect is the same: hundreds of thousands of swap records, with full address and transaction hash details, are available to anyone who looks.

## My Chat with Exolix Staff

I contacted Exolix staff to figure out how I can implement a discount code system in SSHwap so I can advertise it better at conferences. They advised me to use different API keys with varying commission rates.

During development, I did a few successful swaps whose commissions never appeared in their partner panel.

Turns out another account now has my commission!

I was losing my patience because of all the back and forth and being asked to provide the same information over and over again.

We pretty much went back and forth the same way. The staff kept blaming me although I provided them with the request/response bodies and successfully performed a swap. Then they revoked my API keys and told me off.

Later on I received this strange notice from them, which did not remediate the vulnerability.

At last, I contacted them to disclose the vulnerability. They claimed it was in fact a feature, not a bug, and that it was requested by their partners. I did not hear back from any of the affected partners. I would guess they aren’t even aware of this “feature”.
