# 🔐 Critical 2FA Vulnerability in Crypto P2P

- **Source URL:** https://hackenproof.com/blog/for-hackers/2fa-bypass-crypto-p2p-platform
- **Fetched from:** https://hackenproof.com/blog/2fa-bypass-crypto-p2p-platform
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/365 (id 365)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How to Chain 2FA Bypasses in Crypto P2P System and Steal Users’ USDT

While testing a popular cryptocurrency P2P platform with over 2 million users, I discovered a critical vulnerability: two-factor authentication (2FA) was enforced only on the frontend (in some part of app). The backend never verified the OTP — allowing me to add a custom payment method and sell a victim’s USDT without ever passing 2FA.

## Validation

In this write-up, I explain how I chained two logic flaws in a crypto P2P platform’s project creation flow to steal user funds. The core issue? 2FA codes were verified only on the frontend, and never sent to the backend for validation.

By exploiting a lack of server-side 2FA enforcement and poor session isolation, I was able to create a new wallet under another user’s account and use their connected wallet to create a P2P order.

## Detailed Attack Sequence

### 1. Add Attacker-Controlled Payment Method to Victim’s Account

Using the vulnerable endpoint, I sent a crafted request to add my own payment method to the victim’s account — **bypassing the OTP challenge, since the backend didn’t verify it.**

### Step 2: Create a Sell Order Using That Payment Method


With the payment method added, I created a sell order from in victim’s account, offering their USDT — and selected **my own bank details** as the payout option.

## Result: Full USDT Theft Without 2FA

This chain allowed me to:

- Add **my own payout method** to any user account
- Sell **their USDT to myself**
- Receive funds — all **without ever passing OTP verification**

## Responsible Disclosure & Platform Response

- Reported via HackenProof on April 2, 2025
- Assigned a high severity rating
- Fixed within 7 days

## Contacts

Linkedin: [https://www.linkedin.com/in/0xbartita/](https://hackenproof.com/redirect?url=https%3A%2F%2Fwww.linkedin.com%2Fin%2F0xbartita%2F)

More topics:
