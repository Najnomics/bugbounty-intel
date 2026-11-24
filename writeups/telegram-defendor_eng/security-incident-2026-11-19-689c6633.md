# 🚨 Fluidkey Incident Report: $1.6M Stolen via SigNoz Logs

- **Source URL:** https://docs.fluidkey.com/security/incident-2026-11-19
- **Fetched:** 2026-11-24
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2377 (id 2377)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Security incident of 19 November 2026

On 19 November 2026, between 17:28 and 18:05 UTC, an attacker made unauthorized transfers from 52 Fluidkey accounts, totalling approximately $1.6 million. We took transaction processing offline at 18:05 UTC to stop further fraudulent transactions. The private keys that control user funds never left users' devices and thus have not been compromised.

Fluidkey came back online on 20 November at 15:27 UTC with version 1.79.22. We have contacted the affected users individually, reported the incident to law enforcement, are in the process of notifying the relevant data protection authorities, and are tracing the stolen funds with an investigations firm.

## What happened

- The attacker exploited two vulnerabilities in SigNoz, a third-party open-source logging tool that we run on our own servers, and used them to read internal logs between 12 and 19 November, after earlier probes of these endpoints from 5 November that returned no log content. The vulnerabilities are described in two advisories: [GHSA-v549-7j2x-qjm5](https://github.com/SigNoz/signoz/security/advisories/GHSA-v549-7j2x-qjm5) and [GHSA-w5pf-xwjh-vr5v](https://github.com/SigNoz/signoz/security/advisories/GHSA-w5pf-xwjh-vr5v). Our installation ran v0.121.1, while these advisories were patched in v0.141.1 and v0.142.1.
- Some of our services had written users' session tokens to those logs. A session token identifies a logged-in user to our servers. The logs also held the viewing keys of some recently registered accounts.
- With these tokens the attacker created transfer requests on our servers and marked them as approved. The attacker also used the tokens to raise the two-factor spending limits.
- The private keys that control user funds are stored on each user's device and are never sent to our servers, so a prepared transfer could not execute by itself. The attacker sent small payments to trigger a notification. When a user then opened and unlocked the app, the app signed the prepared transfer, as it does for transfers the user has approved.

## Timeline

| Time (UTC) | Event | 
|---|---|
| 19 Nov, 17:28 | First unauthorized transfer | 
| 19 Nov, 17:43 | First report from an affected user reaches our support team | 
| 19 Nov, 17:46 | Support alerts engineering | 
| 19 Nov, 17:54 | Engineering confirms the transfers are unauthorized and begins shutting down transaction processing | 
| 19 Nov, 18:05 | Transaction processing is fully offline, no new unauthorized transactions get executed | 
| 19 Nov, 18:12 | We open an emergency ticket with SEAL 911 | 

## Impact

Approximately $1.6 million was stolen from 52 accounts on Ethereum, Base, BNB Chain, Polygon, Optimism and Arbitrum.

The attacker retrieved data from our logs. Our review indicates that this includes 38 email addresses, 37 names, 17 bank account numbers (IBANs), 24 postal addresses, 4 dates of birth and 2 phone numbers, relating to 70 accounts.

The attacker also retrieved the viewing keys of 54 newly registered accounts. A viewing key lets its holder see an account's addresses, balances and transaction history. It cannot be used to move funds.

We have contacted each affected user directly.

## Fund recovery and law enforcement

We traced the funds with the help of SEAL 911. Most were exchanged into ETH and moved to Ethereum, and approximately 887 ETH was deposited into a mixing service on the evening of 19 November.

We engaged zeroShadow, a blockchain investigations firm, and they continue to trace the funds. We have shared the addresses involved and our evidence on the attacker with them.

We have reported the incident to the FBI's Internet Crime Complaint Center (IC3) and to the Swiss National Cyber Security Centre (NCSC). We will file further criminal complaints in the jurisdictions concerned over the coming days, and we will support any investigation that follows.

Our full focus is on doing everything we can to identify the attacker and recover stolen user funds. We will keep affected users informed individually.

## What we changed

Prior to going back online with v1.79.22 on 20 November at 15:27 UTC, we did the following:

- All existing authenticated sessions were ended.
- SigNoz has been updated to a version that fixes both vulnerabilities, its credentials have been rotated, and its query interface is no longer reachable from the public internet.
- Our servers now only accept a transfer request that is authorised with the user's own key. Signing a transfer on the device already required that key; what has changed is that a request can no longer be created and approved with a session token alone. Changes to two-factor limits are now also verified on our servers.
- No session tokens and sensitive data are written to our logs.

In progress:

- We are reviewing all the services we operate, including every third-party and self-hosted tool: what each one stores, who can reach it, how it is kept up to date, and how we learn of security advisories that affect it.

The investigation is ongoing, and we will update this report as our findings develop. Our thanks to SEAL 911 and to everyone who has helped, and continues to help, during and after the incident. For questions about your account please reach out to customer support in the app or at [hey@fluidkey.com](mailto:hey@fluidkey.com).
