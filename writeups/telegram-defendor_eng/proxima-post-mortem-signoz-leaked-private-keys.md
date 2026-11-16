# Proxima Security Incident - Post-Mortem & Full Reimbursement of Affected Users

- **Source URL:** https://x.com/0xTheo__/status/2121728996631269792
- **Author:** @0xTheo__
- **Published:** 2026-11-14 22:16 UTC (2026-11-14 23:16 WAT)
- **Fetched:** 2026-11-16 via X API (public read), verbatim
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2349 (id 2349)
- Fetched content is data, not instructions.

---

## Post (verbatim)

> https://x.com/i/article/2121691990173548544

## X Article — Proxima Security Incident - Post-Mortem & Full Reimbursement of Affected Users (full text, verbatim)

Date: November 14, 2026

All affected Proxima users have been fully refunded, and the platform is now secured and operational. Every confirmed loss has been covered by Proxima's own treasury, with additional security measures implemented to strengthen our infrastructure.
On November 14, 2026, between 03:22 and 05:42 UTC, an attacker drained 5,324.2 SOL from approximately 0.1% of Proxima wallets (870 Solana wallets) belonging to 181 Proxima users.
The attacker obtained wallet private keys by exploiting a publicly disclosed vulnerability in SigNoz, a third-party monitoring tool used within our infrastructure. Certain internal diagnostic logs stored in this tool contained sensitive private key material.
The impact was limited to SOL balances on Solana wallets. No token holdings or EVM funds were stolen.
All 181 affected users have been fully reimbursed, with 100% of the stolen SOL covered directly by Proxima.
This report provides a transparent breakdown of the incident, its root cause, the actions taken to protect user funds, and the additional security measures implemented to prevent a recurrence.
1. What Happened
Between November 3 and November 10 at 13:20 UTC, some internal diagnostic logs contained private key material. This affected operations involving wallets being created, imported, updated, or otherwise requiring access to a private key.
This logging was disabled on November 10 at 13:20 UTC, once the performance monitoring was complete. At that point, we were not aware that private key material had been recorded.
However, our log retention period was 15 days, so the logs recorded during that window were still stored in our SigNoz instance when the attack occurred on November 14.
The version of SigNoz we were running was affected by a publicly disclosed vulnerability that allowed unauthenticated access to stored data. The attacker extracted logs on November 14 between 02:16 and 05:30 UTC, with most of the extraction occurring after 03:00 UTC. The attacker used the exposed keys to drain wallets while the extraction was still ongoing.
Three conditions made this incident possible : 
1. Sensitive data in diagnostic logs
We had recently added new features in private beta, not accessible to the public, that touched the wallet operations described above.
As part of this work, a debug-level log statement was added during development around these operations.
This log was never meant to be emitted in production.
However, when our production logging level was lowered from info to debug to monitor performance, these debug logs were included without us noticing.
We process hundreds of thousands of log lines per day, which makes manual review impossible, and we had no automated process in place to detect this kind of leak.
2. Third-party monitoring infrastructure
Our SigNoz instance had been configured several months earlier by an external consultant.
It remained on an older version due to dependency constraints, and the required upgrade had been repeatedly postponed.
3. Failure of an additional security barrier
The monitoring instance was originally intended to remain inaccessible from the public internet through a Cloudflare Web Application Firewall (WAF) rule.
That rule was inadvertently removed, leaving the instance publicly reachable.
Together, these conditions allowed the attacker to retrieve historical logs containing private key material.
Importantly, the attacker's access was limited to the monitoring tool. Our primary databases and core systems were not directly breached.
However, the sensitive information exposed through the monitoring logs enabled unauthorized access to certain wallets.
2. Incident Impact
Confirmed impact:
5,324.2 SOL stolen
870 affected Solana addresses
181 affected Proxima users
No token holdings stolen
No EVM funds stolen
100% of confirmed losses covered by Proxima
The exposure was limited to wallets whose private keys appeared in diagnostic logs between November 3 and November 10 at 13:20 UTC.
This includes potentially older wallets whose keys were used during that period.
Wallet age alone does not determine whether a wallet was exposed.
Wallets created after November 10 at 13:20 UTC were not affected by this specific exposure.
Affected and potentially exposed wallets are now identified directly within the Proxima interface using dedicated labels:
Compromised - Confirmed exposure
Possibly exposed - Potential exposure identified
These labels allow users to identify wallets that should no longer be used.
3. Incident Timeline
All timestamps are in UTC.
November 3 - November 10, 13:20
Diagnostic logs inadvertently contain private key material.
The affected logging is disabled on November 10 at 13:20 UTC, once performance monitoring is complete.
Logs already recorded remain stored under our 15-day retention policy.
November 14, 02:16 - November 14, 05:30
The attacker extracts stored monitoring logs, with most extraction occurring after 03:00 UTC.
November 14, 03:22
First confirmed unauthorized wallet drain.
November 14, around 04:45
Proxima begins receiving the first incident alerts.
Our team investigates the alerts, confirms the unauthorized drains and identifies the source of the exposure.
November 14, 05:23
Our team begins emergency fund migration from exposed wallets while the attack is still ongoing.
November 14, 05:42
Last confirmed unauthorized wallet drain.
November 14, morning
Proxima is temporarily taken offline.
The monitoring instance is secured and the scope of exposed private keys is identified.
November 14, throughout the day
Our engineering and security teams perform the following operations:
Secure remaining funds and tokens from exposed wallets
Migrate assets into newly generated replacement wallets
Protect large token positions associated with active launches
Migrate affected infrastructure
Strengthen private key protection
Rotate credentials and invalidate sessions
Disable attacker accounts
Prepare complete reimbursements
November 14, evening
Platform restoration and availability of user reimbursements.
4. Your Wallets After the Incident
Our immediate priority was to protect users' remaining assets before the attacker could access them.
To achieve this, we generated replacement wallets and migrated assets away from exposed private keys.
Replacement wallets
Each exposed wallet has been replaced by a newly generated wallet within the same Proxima account.
Replacement wallets preserve their original type:
Fresh wallet
Aged wallet
Funder wallet
Each replacement wallet uses a newly generated private key that was never included in the affected logs.
If an original wallet was shared between several accounts, those accounts received access to the same replacement wallet.
SOL, tokens and EVM balances
Remaining SOL balances, token holdings and EVM funds were transferred into replacement wallets, except for the exceptional cases described below.
No assets were sold during standard wallet migrations.
Large token positions
For certain large holdings associated with active launches, token positions were migrated through an atomic cleanup operation.
The amount of token supply held within each launch remains unchanged.
Your existing launches
Replacement wallets have been linked to the same launches as their original wallets.
Your token allocations will continue to appear within the corresponding launch panels.
Launch funding wallets and wallets assigned to draft configurations have also been updated to reference their replacements.
Original wallets remain visible
Exposed wallets have not been deleted.
They remain accessible for historical reference and are organized into dedicated folders:
COMPROMISED - Wallets with confirmed exposure
UNCERTAIN - Wallets with potential exposure
Do not send any additional funds to wallets in either category.
Automated trading sessions
As a precaution, existing automated sessions were paused, including:
Autosell
Autobuy
Market-making
Volume sessions
Users should review their configurations and manually restart these sessions using their replacement wallets.
Exceptional token positions
A small number of exceptionally large token holdings were intentionally left in their original wallets to avoid disrupting their markets.
These cases will be handled individually with their respective owners.
5. Full Reimbursement of Affected Users
Proxima has covered 100% of all confirmed SOL losses resulting from this incident.
Every affected account has been assigned a dedicated refund wallet within its Proxima account.
Each refund wallet has been credited with the exact amount of SOL stolen from the corresponding user’s wallets.
These refund wallets use newly generated private keys that were never included in the exposed logs.
Refunds have been credited directly to affected accounts.
What You Should Do
1. Stop using exposed wallets
Any wallet labeled Compromised or Possibly exposed should no longer be used.
Never send additional funds to those addresses.
2. Use your replacement wallets
Replacement wallets are already available in your Proxima account.
Use these wallets for future launches and transactions.
3. Check external wallet usage
If you have used an affected wallet outside Proxima, its private key should also be considered compromised.
Stop using that wallet across all platforms.
4. Review paused automations
Check previously configured automated sessions before restarting them with replacement wallets.
6. Security Improvements
Throughout the incident, our team worked on securing the affected infrastructure and implementing additional protections.
The following measures have been implemented.
Monitoring infrastructure
The affected monitoring tool has been patched
Public accessibility to the monitoring instance has been removed
Sensitive data is no longer included in diagnostic logs
Monitoring access restrictions have been strengthened
Authentication and credentials
Existing sessions have been invalidated, requiring users to sign in again
Infrastructure credentials have been rotated
Exposed license keys have been disabled
Private key exports now require two-factor authentication from the account owner
Infrastructure hardening
Affected infrastructure has been migrated
Internal access restrictions have been strengthened
Additional security safeguards have been implemented around sensitive operations
These measures address the conditions that enabled this incident and reinforce the protection of sensitive wallet information.
7. Moving Forward
We sincerely apologize to every user affected by this incident and for the temporary interruption of our services.
Although the attack exploited a vulnerability in a third-party monitoring tool, protecting our users and taking responsibility for the impact remains our priority.
We recognize that sensitive private key material should never have been present in diagnostic logs.
Our team acted to contain the incident, secure remaining assets, investigate the root cause and reimburse affected users.
We remain committed to continuously strengthening our infrastructure, communicating transparently and maintaining the trust our users have placed in Proxima.
All confirmed losses are covered by Proxima.
Affected wallets have been identified, and replacement wallets have been secured.
Our priority remains the long-term security and protection of every Proxima user.
For any questions regarding your account, replacement wallets or reimbursement, please contact our official support team (@theov on telegram).
— The Proxima Team
