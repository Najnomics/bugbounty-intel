# @Neodyme — full verbatim X archive (security-relevant posts)

_Generated 2026-11-12 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 122
- Conversations/threads: 51
- Oldest post captured: 2021-12-03
- Newest post captured: 2026-04-17


---

## 2026-04-17 · Post · Happy to publicly announce the new advisory!🎉 https://twitter.com/TheZDIBugs/status/2044532001407918


### Post — @Neodyme — 2026-04-17 15:55 UTC (2026-04-17 16:55 WAT)

- URL: https://x.com/Neodyme/status/2045169195160158212
- Metrics (at fetch): bookmark 0, impression 1109, like 7, quote 0, reply 1, retweet 0

> Happy to publicly announce the new advisory!🎉 https://twitter.com/TheZDIBugs/status/2044532001407918108

**Links in post:** https://twitter.com/TheZDIBugs/status/2044532001407918108

**Quoted post** 2044532001407918108: not readable via the API (deleted, private, or withheld).


---

## 2026-04-01 · Post · Small update on the unfolding Drift timeline: as surfaced in other threads (eg https://x.com/TheSoft


### Post — @Neodyme — 2026-04-01 23:04 UTC (2026-04-02 00:04 WAT)

- URL: https://x.com/Neodyme/status/2039479078047109628
- Metrics (at fetch): bookmark 9, impression 5475, like 29, quote 1, reply 2, retweet 2

> Small update on the unfolding Drift timeline: as surfaced in other threads (eg https://x.com/TheSoftwareJedi/status/2039464884371652852), the malicious proposal and execution were nonce transactions (those can be signed offline and not immediately submitted to the network).
>
> The thing about nonce accounts is, [pic.x.com/yTit0E9EzU]

**Media:**
- photo: https://pbs.twimg.com/media/HE2rbLibcAAkI8i.jpg — no alt text provided by author

**Links in post:** https://x.com/TheSoftwareJedi/status/2039464884371652852

**Quoted post** 2039464884371652852: not readable via the API (deleted, private, or withheld).


---

## 2026-04-01 · Thread · Drift Protocol on Solana just got drained. It's looking like a multisig member compromise -- and the


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2026-04-01 22:02 UTC (2026-04-01 23:02 WAT)

- URL: https://x.com/Neodyme/status/2039463435881111878
- Metrics (at fetch): bookmark 25, impression 12798, like 68, quote 7, reply 3, retweet 16

> Drift Protocol on Solana just got drained. It's looking like a multisig member compromise -- and the story starts at least a 20 days before the attack. Here's the breakdown: [pic.x.com/MBnMaIUYfY]

**Media:**
- photo: https://pbs.twimg.com/media/HE2YsZEWsAAyItI.png — no alt text provided by author


### Thread part 2 — @Neodyme — 2026-04-01 22:02 UTC (2026-04-01 23:02 WAT)

- URL: https://x.com/Neodyme/status/2039463437915361591
- Metrics (at fetch): bookmark 0, impression 1621, like 7, quote 0, reply 1, retweet 0

> 7 days ago, Drift updated its on-chain config admin setup, moving from one 2/5 multisig to another new 2/5 Squads multisig. Four of the five signers were newly generated keys without prior history, and one key (39Jy...) carried over from the old multisig.
>
> https://t.co/BMlTxWKqOb


### Thread part 3 — @Neodyme — 2026-04-01 22:02 UTC (2026-04-01 23:02 WAT)

- URL: https://x.com/Neodyme/status/2039463440197251093
- Metrics (at fetch): bookmark 0, impression 1548, like 2, quote 0, reply 1, retweet 0

> Today at ~16:00 UTC, things moved fast:
>
> 15:58:44 - 39Jy.. creates a proposal to withdraw 10k USDC from the Insurance Fund
> 16:03:20 - 13GX.. approves and executes it
> 16:05:18 - 39Jy.. creates + approves a proposal to transfer the admin key to an attacker address


### Thread part 4 — @Neodyme — 2026-04-01 22:02 UTC (2026-04-01 23:02 WAT)

- URL: https://x.com/Neodyme/status/2039463442214527314
- Metrics (at fetch): bookmark 0, impression 1221, like 5, quote 0, reply 1, retweet 0

> Read that again - creation, approval, and execution of the admin key transfer happened within one second. Almost certainly, this means someone directly controls both private keys.


### Thread part 5 — @Neodyme — 2026-04-01 22:02 UTC (2026-04-01 23:02 WAT)

- URL: https://x.com/Neodyme/status/2039463444265484448
- Metrics (at fetch): bookmark 0, impression 1195, like 1, quote 0, reply 1, retweet 0

> Interestingly, the Insurance Fund withdrawal right before was executed by a different key (13GX..) than the two keys involved in the admin-change proposal. Maybe a test run, or part of some social-engineering scheme?


### Thread part 6 — @Neodyme — 2026-04-01 22:02 UTC (2026-04-01 23:02 WAT)

- URL: https://x.com/Neodyme/status/2039463446685557125
- Metrics (at fetch): bookmark 3, impression 4889, like 1, quote 1, reply 1, retweet 0

> With admin access secured, the drain begins. At 16:05:39 UTC the attacker:
>
> → Spins up a fake spot market with inflated prices
> → Raises the withdrawGuards designed to protect against on-chain bugs
> → Deposits worthless CVT tokens, inflating their position to siphon real funds


### Thread part 7 — @Neodyme — 2026-04-01 22:02 UTC (2026-04-01 23:02 WAT)

- URL: https://x.com/Neodyme/status/2039463449793630474
- Metrics (at fetch): bookmark 0, impression 1268, like 5, quote 0, reply 1, retweet 0

> Perhaps the most interesting part: This seems to have been planned over a long period of time: The CVT token used in the exploit was created *20 days ago* by the same authority that funded the attacker's admin account! This also means the token, listed on raydium, had a valid https://t.co/eGstJlo39W

**Media:**
- photo: https://pbs.twimg.com/media/HE2Y1VaWMAAu-jD.png — no alt text provided by author


### Thread part 8 — @Neodyme — 2026-04-01 22:02 UTC (2026-04-01 23:02 WAT)

- URL: https://x.com/Neodyme/status/2039463452444336397
- Metrics (at fetch): bookmark 0, impression 1118, like 2, quote 0, reply 1, retweet 0

> This makes for an interesting timeline, since the token has existed for 20 days, but the multisig member keys were all cycled a week ago:
>
> - 12. March: CVT Token created, listed on raydium, oracle feed initialized
> - 26. March: Admin transferred to new multisig
> - 1. April 15:58:


### Thread part 9 — @Neodyme — 2026-04-01 22:02 UTC (2026-04-01 23:02 WAT)

- URL: https://x.com/Neodyme/status/2039463454566707278
- Metrics (at fetch): bookmark 0, impression 1268, like 4, quote 0, reply 1, retweet 0

> There is no evidence of a squads compromise or a bug in the on-chain Drift program. This looks like a well executed attack on the multisig members.


### Thread part 10 — @Neodyme — 2026-04-01 22:02 UTC (2026-04-01 23:02 WAT)

- URL: https://x.com/Neodyme/status/2039463457045545366
- Metrics (at fetch): bookmark 2, impression 1388, like 2, quote 1, reply 0, retweet 0

> Relevant transactions:
> Transfer of Admin to new Multisig: https://t.co/BMlTxWKqOb
> Insurance Fund withdrawal (created): https://t.co/T7djoLz82O
> Withdrawal approved: https://t.co/TguJvOcfZI
> Withdrawal executed: https://t.co/RXFRyDllQj
> Admin key transfer (created + approved):


---

## 2026-03-24 · Post · Excellent discussion on the current and future landscape of Solana auditing. Thank you @mikemaccana!


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2026-03-24 15:50 UTC (2026-03-24 16:50 WAT)

- URL: https://x.com/Neodyme/status/2036470611237552435
- Metrics (at fetch): bookmark 0, impression 647, like 10, quote 0, reply 2, retweet 1

> Excellent discussion on the current and future landscape of Solana auditing. Thank you @mikemaccana! https://twitter.com/QuicknodeSolana/status/2036424563563585723

**Links in post:** https://twitter.com/QuicknodeSolana/status/2036424563563585723

**Quoted post** 2036424563563585723: not readable via the API (deleted, private, or withheld).


---

## 2026-03-24 · Thread · New blog post 🚨 


### Post — @Neodyme — 2026-03-24 09:01 UTC (2026-03-24 10:01 WAT)

- URL: https://x.com/Neodyme/status/2036367679951417747
- Metrics (at fetch): bookmark 1, impression 527, like 5, quote 0, reply 2, retweet 0

> New blog post 🚨 
>
> We're diving deeper into a privilege escalation issue (CVE-2024-476) in Lenovo Display Control Center used across Windows enterprise environments.
>
> 👉 Read the full breakdown: https://neodyme.io/en/blog/lenovo_dcc_lpe_fwupdate/

**Links in post:** https://neodyme.io/en/blog/lenovo_dcc_lpe_fwupdate/


### Thread part 2 — @Neodyme — 2026-03-24 10:28 UTC (2026-03-24 11:28 WAT)

- URL: https://x.com/Neodyme/status/2036389676320268722
- Metrics (at fetch): bookmark 0, impression 280, like 1, quote 0, reply 0, retweet 0

> The correct CVE is: CVE-2024-4762


---

## 2025-12-12 · Post · Our Solana PDA database is live at http://solana-pda.neodyme.io. Go check it out to get some alpha.


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2025-12-12 13:27 UTC (2025-12-12 14:27 WAT)

- URL: https://x.com/Neodyme/status/1999471049843573184
- Metrics (at fetch): bookmark 1, impression 775, like 14, quote 0, reply 7, retweet 1

> Our Solana PDA database is live at http://solana-pda.neodyme.io. Go check it out to get some alpha.

**Links in post:** http://solana-pda.neodyme.io


---

## 2025-12-08 · Post · Ever ask yourself which protocol is actually the richest on Solana?* Spoiler: DeFiLlama got it wrong


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2025-12-08 13:37 UTC (2025-12-08 14:37 WAT)

- URL: https://x.com/Neodyme/status/1998024069229498878
- Metrics (at fetch): bookmark 1, impression 1381, like 11, quote 1, reply 4, retweet 1

> Ever ask yourself which protocol is actually the richest on Solana?* Spoiler: DeFiLlama got it wrong.
> We’re breaking the real numbers open at @SolanaConf.
> 📆 Dec 12, 17:10
> 📍 Lock-in Stage
>
> *by controlled tokens via PDAs [pic.x.com/JIZaD7r65c]

**Media:**
- photo: https://pbs.twimg.com/media/G7pnhK8XYAAg5ff.jpg — no alt text provided by author


---

## 2025-10-21 · Post · While our colleagues hack live at Pwn2Own in Cork, take a look at our newly published last year's w


Tags (automatic): Path normalization


### Post — @Neodyme — 2025-10-21 12:40 UTC (2025-10-21 13:40 WAT)

- URL: https://x.com/Neodyme/status/1980615277680189918
- Metrics (at fetch): bookmark 1, impression 911, like 12, quote 0, reply 1, retweet 5

> While our colleagues hack live at #Pwn2Own in Cork, take a look at our newly published last year's writeup on our blog: We compromised a QNAP router to take over a networked Canon printer. 
> ▶️ Read the findings and how we got there: https://neodyme.io/en/blog/pwn2own-2024_qhora/

**Links in post:** https://neodyme.io/en/blog/pwn2own-2024_qhora/


---

## 2025-10-01 · Post · ⚡️ Lenovo DCC contained an easy-to-exploit LPE: a weak ACL bug → local privilege escalation → full a


### Post — @Neodyme — 2025-10-01 14:27 UTC (2025-10-01 15:27 WAT)

- URL: https://x.com/Neodyme/status/1973394439436456063
- Metrics (at fetch): bookmark 2, impression 1217, like 9, quote 0, reply 1, retweet 4

> ⚡️ Lenovo DCC contained an easy-to-exploit LPE: a weak ACL bug → local privilege escalation → full admin 🖥️👨‍💻
> We break it down with reverse engineering, process tracing, &amp; two exploit strategies. Read Part 1 of our deep dive: 👉 https://neodyme.io/de/blog/lenovo_dcc_lpe_logic/

**Links in post:** https://neodyme.io/de/blog/lenovo_dcc_lpe_logic/


---

## 2025-08-20 · Thread · We've concluded our audit of P-Token, Solana's new token program build with Pinocchio. It promises i


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2025-08-20 18:26 UTC (2025-08-20 19:26 WAT)

- URL: https://x.com/Neodyme/status/1958234163376717904
- Metrics (at fetch): bookmark 13, impression 46027, like 141, quote 18, reply 14, retweet 23

> We've concluded our audit of P-Token, Solana's new token program build with Pinocchio. It promises impressive savings in Compute Unit (CU) usage. 
> But what exactly does this mean in practice? We've investigated 👇️


### Thread part 2 — @Neodyme — 2025-08-20 18:26 UTC (2025-08-20 19:26 WAT)

- URL: https://x.com/Neodyme/status/1958234165129691470
- Metrics (at fetch): bookmark 5, impression 20495, like 19, quote 2, reply 1, retweet 0

> Using our infrastructure at https://t.co/LGgTiXzsvL, we executed every mainnet transaction from the past few months twice, once with the original Token Program, and again with P-Token. We checked that the output does not differ, and also measured CU savings:


### Thread part 3 — @Neodyme — 2025-08-20 18:26 UTC (2025-08-20 19:26 WAT)

- URL: https://x.com/Neodyme/status/1958234167189414240
- Metrics (at fetch): bookmark 4, impression 36955, like 56, quote 14, reply 2, retweet 4

> From 2025-08-03 up to and including all of 2025-08-11, using P-Token would have saved a total of:
>
> - 8.90T CUs with logging enabled,
> - 9.14T CUs with logging disabled.
>
> This constitutes an impressive saving of 12.0% and 12.3% of TOTAL used blockspace respectively.


### Thread part 4 — @Neodyme — 2025-08-20 18:26 UTC (2025-08-20 19:26 WAT)

- URL: https://x.com/Neodyme/status/1958234169089134641
- Metrics (at fetch): bookmark 1, impression 1900, like 22, quote 0, reply 4, retweet 0

> Note that this isn't just savings in P-Token instructions. It's savings relative to the overall throughput of the blockchain, failed and vote transactions included.
>
> IBRL!


---

## 2025-07-25 · Post · We reported a vulnerability in Parallels Client via @thezdi last year. 


### Post — @Neodyme — 2025-07-25 09:01 UTC (2025-07-25 10:01 WAT)

- URL: https://x.com/Neodyme/status/1948669905005601000
- Metrics (at fetch): bookmark 8, impression 2203, like 21, quote 0, reply 0, retweet 8

> We reported a vulnerability in Parallels Client via @thezdi last year. 
> 🔥 The issue (CVE-2025-6812) - now fixed: A privileged service searched for an OpenSSL config file in an unsecured location, enabling LPE. 
> ➡️ Advisory here: https://t.co/snjiUw8gLt 
> ☂️ Patch your systems!


---

## 2025-05-28 · Post · Part 3 of our Riverguard series is out! 


Tags (automatic): Smart contract / DeFi, Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2025-05-28 15:13 UTC (2025-05-28 16:13 WAT)

- URL: https://x.com/Neodyme/status/1927745141680275958
- Metrics (at fetch): bookmark 4, impression 954, like 11, quote 1, reply 0, retweet 6

> Part 3 of our Riverguard series is out! 
> We're looking under the hood at the "fuzzcases" Riverguard uses to catch real-world bugs in Solana smart contracts. 
> Still shocked how often some of these pop up. 
> Check it out 👉 https://t.co/5WkvxEz0oU


---

## 2025-05-22 · Post · At Pwn2Own Ireland 2024, we successfully targeted the SOHO Smashup category. 🖨️


Tags (automatic): RCE


### Post — @Neodyme — 2025-05-22 11:07 UTC (2025-05-22 12:07 WAT)

- URL: https://x.com/Neodyme/status/1925508702955610145
- Metrics (at fetch): bookmark 26, impression 5011, like 71, quote 0, reply 2, retweet 15

> At #Pwn2Own Ireland 2024, we successfully targeted the SOHO Smashup category. 🖨️
> Starting with a QNAP QHora-322 NAS, we pivoted to the Canon imageCLASS MF656Cdw - and ended up with shellcode execution.
> Read the full vulnerability deep dive here 👉 https://t.co/Lx8T5mLVaL


---

## 2025-05-02 · Post · From iframes and file reads to full RCE. 🔥


Tags (automatic): SSRF, RCE, Mobile / Android / iOS


### Post — @Neodyme — 2025-05-02 11:03 UTC (2025-05-02 12:03 WAT)

- URL: https://x.com/Neodyme/status/1918259999668662740
- Metrics (at fetch): bookmark 47, impression 6405, like 68, quote 1, reply 1, retweet 27

> From iframes and file reads to full RCE. 🔥
>
> We found an HTML-to-PDF API allowing file reads and SSRF - then chained it into remote code execution via a Chromium 62 WebView exploit.
>
> 👉 Read the full write-up here: https://neodyme.io/en/blog/html_renderer_to_rce/

**Links in post:** https://neodyme.io/en/blog/html_renderer_to_rce/


---

## 2025-02-12 · Post · 🔎Digging deeper into COM hijacking!


### Post — @Neodyme — 2025-02-12 15:08 UTC (2025-02-12 16:08 WAT)

- URL: https://x.com/Neodyme/status/1889693177415684356
- Metrics (at fetch): bookmark 24, impression 3791, like 59, quote 0, reply 0, retweet 16

> 🔎Digging deeper into COM hijacking!
> In Part 3, we explore two new vulnerabilities: 
> 🗑️ Webroot Endpoint Protect (CVE-2023-7241) – SYSTEM via arbitrary file deletion
> 📥 Checkpoint Harmony (CVE-2024-24912) – SYSTEM via a file download primitive
>
> Read more: https://neodyme.io/en/blog/com_hijacking_3/

**Links in post:** https://neodyme.io/en/blog/com_hijacking_3/


---

## 2025-01-29 · Post · 🔎Part 2 of our COM hijacking series is live!


### Post — @Neodyme — 2025-01-29 15:16 UTC (2025-01-29 16:16 WAT)

- URL: https://x.com/Neodyme/status/1884621551028318332
- Metrics (at fetch): bookmark 12, impression 2354, like 44, quote 0, reply 1, retweet 14

> 🔎Part 2 of our COM hijacking series is live!
> This time, we discuss a vulnerability in AVG Internet Security, where we bypass an allow-list, disable self-protection, and exploit an update mechanism to escalate privileges to SYSTEM 🚀💻
> https://neodyme.io/en/blog/com_hijacking_2/

**Links in post:** https://neodyme.io/en/blog/com_hijacking_2/


---

## 2025-01-17 · Post · Your laptop was stolen. It’s running Windows 11, fully up-to-date, device encryption (BitLocker) and


### Post — @Neodyme — 2025-01-17 14:00 UTC (2025-01-17 15:00 WAT)

- URL: https://x.com/Neodyme/status/1880253893680197795
- Metrics (at fetch): not returned

> Your laptop was stolen. It’s running Windows 11, fully up-to-date, device encryption (BitLocker) and Secure Boot enabled. Your data is safe, right? Think again! This software-only attack grabs your encryption key. Following up on our #38C3 talk: https://neodyme.io/blog/bitlocker_screwed_without_a_screwdriver/

**Links in post:** https://neodyme.io/blog/bitlocker_screwed_without_a_screwdriver/


---

## 2025-01-15 · Post · Following our 38c3 talk about exploiting security software for privilege escalation, we're excited 


### Post — @Neodyme — 2025-01-15 15:10 UTC (2025-01-15 16:10 WAT)

- URL: https://x.com/Neodyme/status/1879546640983310647
- Metrics (at fetch): bookmark 28, impression 15712, like 71, quote 3, reply 1, retweet 22

> Following our #38c3 talk about exploiting security software for privilege escalation, we're excited to kick off a new blog series! 🎊 
> Check out our first blog post on our journey to 💥 exploit five reputable security products to gain privileges via COM hijacking: https://neodyme.io/blog/com_hijacking_1/

**Links in post:** https://neodyme.io/blog/com_hijacking_1/


---

## 2024-11-21 · Post · 💥When security software itself becomes a target! 💥


### Post — @Neodyme — 2024-11-21 16:56 UTC (2024-11-21 17:56 WAT)

- URL: https://x.com/Neodyme/status/1859641975030546679
- Metrics (at fetch): not returned

> 💥When security software itself becomes a target! 💥
> Learn how we've uncovered critical vulnerabilities in Wazuh, turning a powerful security tool into an unexpected attack vector. 
> 👉 Read more about the findings: https://neodyme.io/en/blog/wazuh_rce/

**Links in post:** https://neodyme.io/en/blog/wazuh_rce/


---

## 2024-10-25 · Post · Since we had used a different setup without any administrator account, our official attempt during 


### Post — @Neodyme — 2024-10-25 13:27 UTC (2024-10-25 14:27 WAT)

- URL: https://x.com/Neodyme/status/1849804973984432382
- Metrics (at fetch): bookmark 2, impression 2357, like 26, quote 0, reply 2, retweet 2

> Since we had used a different setup without any administrator account, our official attempt during #Pwn2Own failed. However, @thezdi provided us with a second chance to present our Lexmark exploit and it worked 🖨️🎉 https://t.co/2WjbEoGgKW

**Media:**
- photo: https://pbs.twimg.com/media/GavTmzFXsAAEQ8p.jpg — no alt text provided by author


---

## 2024-10-22 · Post · Challenge accepted! We’re gearing up for @thezdi's Pwn2Own to highlight critical vulnerabilities in


Tags (automatic): Path normalization


### Post — @Neodyme — 2024-10-22 07:52 UTC (2024-10-22 08:52 WAT)

- URL: https://x.com/Neodyme/status/1848633479510298754
- Metrics (at fetch): bookmark 0, impression 1363, like 17, quote 1, reply 1, retweet 3

> Challenge accepted! We’re gearing up for @thezdi's #Pwn2Own to highlight critical vulnerabilities in home routers and printers. 
> Today at 11am IST, we’ll be targeting the HP Color LaserJet Pro MFP 3301fdw. Fingers crossed and good luck to the other contestants🤞


---

## 2024-10-12 · Post · We audited @UNCX_token's liquidity lockers toward the end of Q2 2024 -- and we're happy to celebrate


### Post — @Neodyme — 2024-10-12 14:18 UTC (2024-10-12 15:18 WAT)

- URL: https://x.com/Neodyme/status/1845106734282506668
- Metrics (at fetch): bookmark 3, impression 1667, like 11, quote 0, reply 0, retweet 3

> We audited @UNCX_token's liquidity lockers toward the end of Q2 2024 -- and we're happy to celebrate their launch!
>
> We can confirm that their audit completed without a single finding above low severity -- an uncommon feat. Their dedication to securing their programs is unmatched https://t.co/16e2Z2O5L7

**Quoted post (full text):**

    #### Quoted post — @1275709288787345408 — 2024-10-11 16:20 UTC (2024-10-11 17:20 WAT)
    
    - URL: https://x.com/1275709288787345408/status/1844775170772259276
    - Metrics (at fetch): bookmark 14, impression 46898, like 158, quote 3, reply 41, retweet 43
    
    > Our Liquidity Lockers are now live on @solana, offering enhanced security and verifiable open-source integration for projects.
    >
    > Lock liquidity on @RaydiumProtocol to protect token value, minimize volatility, and increase investor confidence. All accounts are decentralized, https://t.co/QjaF7Yu0hJ
    
    **Media:**
    - media `7_1844770824479236103` (details not returned by the API)
    


---

## 2024-06-07 · Post · We completed an audit of @streamflow_fi's protocol including their new airdrop feature.🕵️‍♂️


### Post — @Neodyme — 2024-06-07 08:43 UTC (2024-06-07 09:43 WAT)

- URL: https://x.com/Neodyme/status/1798999168238956898
- Metrics (at fetch): bookmark 0, impression 1711, like 14, quote 0, reply 0, retweet 3

> We completed an audit of @streamflow_fi's protocol including their new airdrop feature.🕵️‍♂️
>
> Happy to announce there were no major issues, and they've been a great team to work with🫡 https://t.co/eL9mvp2IIb

**Quoted post (full text):**

    #### Quoted post — @1393137074979713024 — 2024-06-07 08:26 UTC (2024-06-07 09:26 WAT)
    
    - URL: https://x.com/1393137074979713024/status/1798995049612714216
    - Metrics (at fetch): bookmark 0, impression 3198, like 26, quote 1, reply 1, retweet 4
    
    > We're proud to announce that we've successfully completed another audit with @Neodyme. This audit covers the newly released Airdrop feature and the core Solana protocol.
    >
    > This audit further validates the continuing robustness of Streamflow's smart contracts. https://t.co/UCErPhGHD0
    
    **Media:**
    - media `3_1798982039267405824` (details not returned by the API)
    


---

## 2024-05-14 · Thread · In collaboration with @cirosec, we've identified several privilege escalation vulnerabilities in mul


### Post — @Neodyme — 2024-05-14 13:16 UTC (2024-05-14 14:16 WAT)

- URL: https://x.com/Neodyme/status/1790370530765291708
- Metrics (at fetch): bookmark 2, impression 3309, like 22, quote 1, reply 10, retweet 7

> In collaboration with @cirosec, we've identified several privilege escalation vulnerabilities in multiple popular antivirus and EDR solutions.
>
> Our secret? A novel attack surface: COM hijacking 🔥
>
> 1/2


### Thread part 2 — @Neodyme — 2024-05-14 13:16 UTC (2024-05-14 14:16 WAT)

- URL: https://x.com/Neodyme/status/1790370532908511690
- Metrics (at fetch): bookmark 0, impression 689, like 9, quote 0, reply 3, retweet 2

> So far, the following CVEs have been published and promptly addressed by the vendors:
>
> - CVE-2023-6154 (BitDefender)
> - CVE-2024-24912 (CheckPoint)
> - CVE-2023-7241 (Webroot)
>
> Curious? Stay tuned for our conference talks (tba) and in-depth technical blogposts!
>
> 2/2


---

## 2024-03-15 · Thread · An innovation in LST swapping, a new smart contract framework and a state corruption bug:


Tags (automatic): Smart contract / DeFi


### Post — @Neodyme — 2024-03-15 23:09 UTC (2024-03-16 00:09 WAT)

- URL: https://x.com/Neodyme/status/1768776639335317644
- Metrics (at fetch): bookmark 8, impression 15064, like 27, quote 4, reply 1, retweet 5

> An innovation in LST swapping, a new smart contract framework and a state corruption bug:
>
> Join us for a deeper look into our recent pre-launch audit of @sanctumso's new Infinity protocol. And into why multiple audits are important 👇


### Thread part 2 — @Neodyme — 2024-03-15 23:09 UTC (2024-03-16 00:09 WAT)

- URL: https://x.com/Neodyme/status/1768776642116116614
- Metrics (at fetch): bookmark 0, impression 703, like 1, quote 0, reply 1, retweet 0

> @sanctumso has recently launched their new Infinity protocol. Basically, it's a big swap pool with various Liquid Staking Tokens (such as mSOL, jitoSOL, laineSOL,...). Each LST is priced exactly to the value you could unstake it for.
>
> The program is written in Sanctum's new IDL-first framework, **Ideally**


### Thread part 3 — @Neodyme — 2024-03-15 23:09 UTC (2024-03-16 00:09 WAT)

- URL: https://x.com/Neodyme/status/1768776644800495805
- Metrics (at fetch): bookmark 0, impression 571, like 1, quote 0, reply 1, retweet 0

> It uses a modular multi-program structure. A main controller program calls different programs to determine LST prices and calculate fees. They can be switched out to change the fee structure, or to add new LSTs. [pic.x.com/M8KAm1cD3C]

**Media:**
- photo: https://pbs.twimg.com/media/GIvzh-OW8AAqI8v.png — no alt text provided by author


### Thread part 4 — @Neodyme — 2024-03-15 23:09 UTC (2024-03-16 00:09 WAT)

- URL: https://x.com/Neodyme/status/1768776647690293655
- Metrics (at fetch): bookmark 0, impression 508, like 1, quote 0, reply 1, retweet 0

> Our audit was the third audit of all programs before the launch. The code quality was excellent, and it was obvious that the sanctum developers had been extremely diligent. Despite that, we were able to find one high-severity vulnerability that others missed... [pic.x.com/tRINiUoAt8]

**Media:**
- photo: https://pbs.twimg.com/media/GIvznekWoAEcH63.png — no alt text provided by author


### Thread part 5 — @Neodyme — 2024-03-15 23:09 UTC (2024-03-16 00:09 WAT)

- URL: https://x.com/Neodyme/status/1768776649770709224
- Metrics (at fetch): bookmark 0, impression 494, like 1, quote 0, reply 1, retweet 0

> The main contract of the protocol holds all funds, with one token account per supported LST. It tracks the exact sum of the SOL value of all of these holdings in order to know how to price the protocol's LP token.


### Thread part 6 — @Neodyme — 2024-03-15 23:09 UTC (2024-03-16 00:09 WAT)

- URL: https://x.com/Neodyme/status/1768776651523903727
- Metrics (at fetch): bookmark 0, impression 487, like 1, quote 0, reply 1, retweet 0

> In order to track this sum, the protocol has a PDA that stores a list of each supported LST, including the total value of the protocol's holdings in the LST. 
> One of the invariants that must be maintained is that no LST appears twice in this list.


### Thread part 7 — @Neodyme — 2024-03-15 23:09 UTC (2024-03-16 00:09 WAT)

- URL: https://x.com/Neodyme/status/1768776653818188113
- Metrics (at fetch): bookmark 0, impression 642, like 1, quote 0, reply 1, retweet 0

> We found a way this invariant could be violated, and the protocol drained as a result. 
> The bug was in an admin-only instruction to remove support for an LST by deleting the entry from the LST list. It was implemented incorrectly, leading to accidental exploitable state corruption.


### Thread part 8 — @Neodyme — 2024-03-15 23:09 UTC (2024-03-16 00:09 WAT)

- URL: https://x.com/Neodyme/status/1768776656682881061
- Metrics (at fetch): bookmark 0, impression 312, like 2, quote 0, reply 1, retweet 0

> The LST removal instruction removes an entry from the LST list by copying all entries after it one position to the left and dropping the last entry. Below is the relevant code. Can you spot the bug? [pic.x.com/Z4fr0VtCCH]

**Media:**
- photo: https://pbs.twimg.com/media/GIvz1ZOXUAEe_SB.png — no alt text provided by author


### Thread part 9 — @Neodyme — 2024-03-15 23:09 UTC (2024-03-16 00:09 WAT)

- URL: https://x.com/Neodyme/status/1768776659749019968
- Metrics (at fetch): bookmark 0, impression 245, like 2, quote 0, reply 1, retweet 0

> The bug is simple: The destination of the pointer copy is incorrect. The instruction simply copies the entries to the front of the list, instead of one to the left. The bug was likely missed by others due to confusion with the variable names. [pic.x.com/Mv8i1JG2rz]

**Media:**
- photo: https://pbs.twimg.com/media/GIvz54oWgAAzkC_.jpg — no alt text provided by author


### Thread part 10 — @Neodyme — 2024-03-15 23:09 UTC (2024-03-16 00:09 WAT)

- URL: https://x.com/Neodyme/status/1768776662613643388
- Metrics (at fetch): bookmark 0, impression 221, like 0, quote 0, reply 1, retweet 0

> Hence, if the remove LST instruction were ever used, instead of removing the entry, it would have overwritten entries at the start of the list with copies of later entries. This violates the invariant, and messes up tracking of the total value of protocol holdings.


### Thread part 11 — @Neodyme — 2024-03-15 23:09 UTC (2024-03-16 00:09 WAT)

- URL: https://x.com/Neodyme/status/1768776664907939925
- Metrics (at fetch): bookmark 0, impression 203, like 1, quote 0, reply 1, retweet 0

> An attacker could have easily exploited this to repeatedly mess with the total value tracking and drain the protocol: A clear loss-of-funds bug. However, since it must be (accidentally) triggered by the admin, we assigned it high instead of critical severity.


### Thread part 12 — @Neodyme — 2024-03-15 23:09 UTC (2024-03-16 00:09 WAT)

- URL: https://x.com/Neodyme/status/1768776666665423215
- Metrics (at fetch): bookmark 0, impression 213, like 2, quote 0, reply 1, retweet 0

> Want to read about our assessment of the overall security, our discussion of the protocol’s economic security and the authority structure, and much more? The audit report is now available at https://learn.sanctum.so/docs/security.

**Links in post:** https://learn.sanctum.so/docs/security


### Thread part 13 — @Neodyme — 2024-03-15 23:09 UTC (2024-03-16 00:09 WAT)

- URL: https://x.com/Neodyme/status/1768776668800270815
- Metrics (at fetch): bookmark 0, impression 661, like 2, quote 0, reply 1, retweet 0

> State corruption vulnerabilities are one of the most dangerous classes of bugs. Just last August, @cypher_protocol was exploited due to a state corruption bug in their margin account system. Read our thread here: https://x.com/Neodyme/status/1690066210417967105

**Links in post:** https://x.com/Neodyme/status/1690066210417967105

**Quoted post (full text):**

    #### Quoted post — @Neodyme — 2023-08-11 18:22 UTC (2023-08-11 19:22 WAT)
    
    - URL: https://x.com/Neodyme/status/1690066210417967105
    - Metrics (at fetch): bookmark 22, impression 18108, like 77, quote 5, reply 1, retweet 24
    
    > Cypher protocol was exploited for over $1 million. But how?
    >
    > Here’s the main idea for what the attacker did, and why it worked 👇🏻 [pic.x.com/CqFjz6k2fW]
    
    **Media:**
    - media `3_1690064166357467137` (details not returned by the API)
    


### Thread part 14 — @Neodyme — 2024-03-15 23:09 UTC (2024-03-16 00:09 WAT)

- URL: https://x.com/Neodyme/status/1768776671123898531
- Metrics (at fetch): bookmark 0, impression 434, like 5, quote 0, reply 0, retweet 0

> We’re happy to have caught the bug before @sanctumso’s Infinity launch and will continue to help secure the ecosystem through audits, reviews, and educational threads like these. Follow us for more.


---

## 2024-03-13 · Thread · Ever wonder what happens when you let the world's best auditors loose on a program written by Solana


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2024-03-13 22:21 UTC (2024-03-13 23:21 WAT)

- URL: https://x.com/Neodyme/status/1768039762735022157
- Metrics (at fetch): bookmark 14, impression 7440, like 28, quote 3, reply 2, retweet 4

> Ever wonder what happens when you let the world's best auditors loose on a program written by Solana OGs? 
>
> Our audit report for @sanctumso's Infinity protocol is now public. ♾ [pic.x.com/a74CpwDCEL]

**Media:**
- photo: https://pbs.twimg.com/media/GIlWBRsXwAAuTXZ.jpg — no alt text provided by author


### Thread part 2 — @Neodyme — 2024-03-13 22:21 UTC (2024-03-13 23:21 WAT)

- URL: https://x.com/Neodyme/status/1768039765339693282
- Metrics (at fetch): bookmark 0, impression 307, like 2, quote 0, reply 1, retweet 0

> We did a full and comprehensive audit of all Infinity programs during January, making the protocol even more secure 🤝


### Thread part 3 — @Neodyme — 2024-03-13 22:21 UTC (2024-03-13 23:21 WAT)

- URL: https://x.com/Neodyme/status/1768039766992261627
- Metrics (at fetch): bookmark 0, impression 335, like 1, quote 0, reply 1, retweet 0

> What is Infinity? 
> Basically, a big pool of various Liquid Staking Tokens (such as mSOL, bSOL, jitoSOL, laineSOL,...). 
> Each LST is priced exactly to its on-chain value and they can be swapped with minimal fees. 
> No slippage, no orderbook spread.


### Thread part 4 — @Neodyme — 2024-03-13 22:21 UTC (2024-03-13 23:21 WAT)

- URL: https://x.com/Neodyme/status/1768039768808444142
- Metrics (at fetch): bookmark 0, impression 302, like 1, quote 0, reply 2, retweet 0

> The protocol is written in Sanctum's new IDL-first framework called Ideally and uses a modular multi-program structure. This makes it easy to add support for new LSTs in the future.


### Thread part 5 — @Neodyme — 2024-03-13 22:21 UTC (2024-03-13 23:21 WAT)

- URL: https://x.com/Neodyme/status/1768039770595226023
- Metrics (at fetch): bookmark 1, impression 275, like 2, quote 0, reply 1, retweet 0

> This report dives deep into the inner workings of the Infinity protocol. 
> We examined program security, economic design, the authority structure, and many other aspects. 
> Read it here: https://learn.sanctum.so/docs/security

**Links in post:** https://learn.sanctum.so/docs/security


---

## 2024-02-29 · Post · New Blogpost: Learn how Riverguard works and how we used it to find a bug in an on-chain casino 🎰↓


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2024-02-29 18:50 UTC (2024-02-29 19:50 WAT)

- URL: https://x.com/Neodyme/status/1763275472904052853
- Metrics (at fetch): not returned

> New Blogpost: Learn how Riverguard works and how we used it to find a bug in an on-chain casino 🎰↓
> https://neodyme.io/en/blog/riverguard_1_intro/

**Links in post:** https://neodyme.io/en/blog/riverguard_1_intro/


---

## 2024-01-24 · Post · Read our new blogpost: How to hack a DAO! 😈


### Post — @Neodyme — 2024-01-24 18:19 UTC (2024-01-24 19:19 WAT)

- URL: https://x.com/Neodyme/status/1750221784220336278
- Metrics (at fetch): not returned

> Read our new blogpost: How to hack a DAO! 😈
>
> You'll learn how small technical details can be turned into powerful social engineering attacks.
> https://neodyme.io/en/blog/how_to_hack_a_dao/

**Links in post:** https://neodyme.io/en/blog/how_to_hack_a_dao/


---

## 2023-12-14 · Post · Technical Analysis of the Ledger Supply-Chain Attack 🧵


Tags (automatic): Dependency confusion / supply chain, Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2023-12-14 16:35 UTC (2023-12-14 17:35 WAT)

- URL: https://x.com/Neodyme/status/1735337711555285261
- Metrics (at fetch): not returned

> Technical Analysis of the Ledger Supply-Chain Attack 🧵
>
> We did a brief analysis of today’s attack against the @ledger browser integration. This is what we found.
>
> Ledger’s browser integration, Ledger Connect, was attacked via a suspected supply chain attack. The attacker inserted malicious javascript into version 1.1.6 and 1.1.7. The attack mostly affected users that selected the Ledger Wallet Provider option in a dApp frontend.
>
> The main javascript payload of the attack is a fairly sophisticated wallet drainer. It drains various tokens on EVM chains, supporting several different wallets.
>
> Other blockchains, such as Solana, were not affected. Notably, the attack also tries to drain from other installed browser wallets.
>
> How was the payload introduced to the ledger browser integration?
>
> There were numerous updates to the connect-kit npm package today. The malicious version have since been deleted from the package history, however the timeline was as follows:
>
> 1.1.5, uploaded today at 9:49 UTC, still looks normal, but is affected according to Ledger.
> 1.1.6/1.1.7 were uploaded within about two hours of 1.1.5. We confirmed that they contain malicious code.
> 1.1.8, uploaded at 13:18 UTC, looks to be clean again, which was confirmed by @ledger: 
> https://twitter.com/Ledger/status/1735298142118072512
>
> What happened, and what were the effects?
>
> To understand, let’s look at how the Ledger browser integration, called Ledger Connect, works.
> To interface with their browser extension, dApps can use Connect by including a code snippet provided by Ledger.
>
> This is done with a connect-kit-loader proxy that dynamically fetches and executes the latest version of connect-kit from NPM. As the version on NPM was upgraded today in the supply-chain attack, all dApps using the connect-kit-loader pulled the malicious javascript.
>
> Most sites that support Ledger likely use the official connect-kit-loader, but only execute it when the user explicitly selects the Ledger Wallet Provider.
> If a user does that, the website downloads and executes the drainer instead of the intended ledger integration.
>
> The drainer code is obfuscated but can be deobfuscated with tools like https://obf-io.deobfuscate.io/
>
> In short, the drainer fetches encrypted configuration data from Infura, a dApp backend provider. Using the api-key and encryption secrets contained in the code we can access it ourselves.
> The config contains target wallets for multiple chains and a list of 400 ‘researcher’ pubkeys, which are NOT attacked.
>
> The drainer then does the usual draining: Check which wallet providers are inserted, enumerate addresses, check balances and send drain txs to the user to sign.
>
> If you enjoyed this thread, follow us for more in-depth security analyses, and we’d love a like and retweet for visibility!
>
> #ledgerhack #Ledger

**Media:**
- photo: https://pbs.twimg.com/media/GBUmcXyWQAArzBi.png — no alt text provided by author
- photo: https://pbs.twimg.com/media/GBUnOkMXwAAu7x5.png — no alt text provided by author
- photo: https://pbs.twimg.com/media/GBUnR1jXcAAtDoC.png — no alt text provided by author
- photo: https://pbs.twimg.com/media/GBUoMYrXsAAuAJD.png — no alt text provided by author

**Links in post:** https://twitter.com/Ledger/status/1735298142118072512, https://obf-io.deobfuscate.io/

**Quoted post (full text):**

    #### Quoted post — @2652239532 — 2023-12-14 13:58 UTC (2023-12-14 14:58 WAT)
    
    - URL: https://x.com/2652239532/status/1735298142118072512
    - Metrics (at fetch): not returned
    
    > Update: 
    >
    > The malicious version of the file was replaced with the genuine version at around 2:35pm CET. 
    >
    > The new genuine version should be propagated soon. 
    >
    > We will provide a comprehensive report as soon as it’s ready.
    >
    > In the meantime, we’d like to remind the community to always Clear Sign your transactions - remember that the addresses and the information presented on your Ledger screen is the only genuine information.
    >
    > If there’s a difference between the screen shown on your Ledger device and your computer/phone screen, stop that transaction immediately.
    


---

## 2023-11-01 · Post · Introducing Riverguard 🏞️💂


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2023-11-01 14:30 UTC (2023-11-01 15:30 WAT)

- URL: https://x.com/Neodyme/status/1719723518638817321
- Metrics (at fetch): not returned

> Introducing Riverguard 🏞️💂
>
> A new security tool for Solana program deployers... 🧵
>
> https://riverguard.io [pic.x.com/kKn8UqYbJN]

**Media:**
- photo: https://pbs.twimg.com/media/F92vbGrbYAAdd47.jpg — no alt text provided by author

**Links in post:** https://riverguard.io


---

## 2023-10-23 · Post · 🎃👩‍💻 Hacks are SCARY 👻🔐


### Post — @Neodyme — 2023-10-23 17:15 UTC (2023-10-23 18:15 WAT)

- URL: https://x.com/Neodyme/status/1716503682781479047
- Metrics (at fetch): not returned

> 🎃👩‍💻 Hacks are SCARY 👻🔐
>
> Unmasking the Hacky Halloween Party at #Breakpoint2023!
>
> Dress up to be safe from the hackers!
>
> 🎟️ Access Limited: Hack your way into the guestlist now
>
> https://lu.ma/ez0qr1s9 [pic.x.com/GeCtHhtVg5]

**Media:**
- photo: https://pbs.twimg.com/media/F9I-0z2WMAA3b0W.jpg — no alt text provided by author

**Links in post:** https://lu.ma/ez0qr1s9


---

## 2023-10-19 · Reply · @synthetify got hacked in a DAO attack.


### Post — @Neodyme — 2023-10-19 23:32 UTC (2023-10-20 00:32 WAT)

- URL: https://x.com/Neodyme/status/1715149044794655145
- Metrics (at fetch): not returned

> @synthetify got hacked in a DAO attack.
>
> The attacker passed a proposal to upgrade the program and stole $230k from the protocol.
>
> What happened? [pic.x.com/2MXdJpybB8]

**Media:**
- photo: https://pbs.twimg.com/media/F81oAFzW0AA9rh0.png — no alt text provided by author


---

## 2023-08-11 · Thread · Cypher protocol was exploited for over $1 million. But how?


### Post — @Neodyme — 2023-08-11 18:22 UTC (2023-08-11 19:22 WAT)

- URL: https://x.com/Neodyme/status/1690066210417967105
- Metrics (at fetch): bookmark 22, impression 18108, like 77, quote 5, reply 1, retweet 24

> Cypher protocol was exploited for over $1 million. But how?
>
> Here’s the main idea for what the attacker did, and why it worked 👇🏻 [pic.x.com/CqFjz6k2fW]

**Media:**
- media `3_1690064166357467137` (details not returned by the API)


### Thread part 2 — @Neodyme — 2023-08-11 18:22 UTC (2023-08-11 19:22 WAT)

- URL: https://x.com/Neodyme/status/1690066211672141824
- Metrics (at fetch): bookmark 0, impression 808, like 6, quote 0, reply 1, retweet 0

> @cypher_protocol  is a trading platform where users have subaccounts. Subaccounts can either be isolated-margin or cross-margin.
>
> They also have cached metadata attached to them storing their margining type and the dollar value of their assets and liabilities.


### Thread part 3 — @Neodyme — 2023-08-11 18:22 UTC (2023-08-11 19:22 WAT)

- URL: https://x.com/Neodyme/status/1690066212632559619
- Metrics (at fetch): bookmark 0, impression 704, like 5, quote 0, reply 1, retweet 0

> However, the margining type is stored twice – once in the subaccount itself, and once in its cache.
>
> Here’s how an account with 2 subaccounts could look. One subaccount has 1 SOL in it, the other 0.
>
> By default, subaccounts are cross-margin. [pic.x.com/zbO7VvuPWs]

**Media:**
- photo: https://pbs.twimg.com/media/F3RQdf6bIAA2ect.png — no alt text provided by author


### Thread part 4 — @Neodyme — 2023-08-11 18:22 UTC (2023-08-11 19:22 WAT)

- URL: https://x.com/Neodyme/status/1690066214327070720
- Metrics (at fetch): bookmark 0, impression 656, like 4, quote 0, reply 1, retweet 0

> Cypher has an instruction to change the margining type of a subaccount. The main bug was that this instruction did not update the margining type in the cache.
>
> Here’s how the account looks after changing the margining type of the second subaccount. [pic.x.com/KwBmli2mue]

**Media:**
- photo: https://pbs.twimg.com/media/F3RQkjKagAEQ6dM.png — no alt text provided by author


### Thread part 5 — @Neodyme — 2023-08-11 18:22 UTC (2023-08-11 19:22 WAT)

- URL: https://x.com/Neodyme/status/1690066216000585730
- Metrics (at fetch): bookmark 0, impression 600, like 4, quote 0, reply 1, retweet 0

> Why is this a problem? Well, there are two types of margin checks on subaccounts:
>
> If the subaccount is isolated, its collateral ratio is the ratio of its assets to its liabilities.


### Thread part 6 — @Neodyme — 2023-08-11 18:22 UTC (2023-08-11 19:22 WAT)

- URL: https://x.com/Neodyme/status/1690066216927526914
- Metrics (at fetch): bookmark 0, impression 591, like 4, quote 0, reply 1, retweet 0

> However, if a subaccount is cross-margin, its collateral ratio is calculated over all subaccounts that are marked as cross-margin in their CACHE.
>
> Hence subaccounts that had their margining type changed to isolated still incorrectly count toward the cross-margin collateral ratio.


### Thread part 7 — @Neodyme — 2023-08-11 18:22 UTC (2023-08-11 19:22 WAT)

- URL: https://x.com/Neodyme/status/1690066217846079493
- Metrics (at fetch): bookmark 0, impression 588, like 2, quote 0, reply 1, retweet 0

> What does that mean? Well, let’s see what happens when we transfer 2 SOL from subaccount 1 to subaccount 2.
>
> During validation, the contract verifies that the collateral ratio of subaccount 1 is still ok after the transfer.
>
> And it is: ($0+$50)/($25+$0) = 200% ✅ [pic.x.com/cWgsZn65T2]

**Media:**
- photo: https://pbs.twimg.com/media/F3RQng2bUAAu1g_.png — no alt text provided by author


### Thread part 8 — @Neodyme — 2023-08-11 18:22 UTC (2023-08-11 19:22 WAT)

- URL: https://x.com/Neodyme/status/1690066219179868164
- Metrics (at fetch): bookmark 0, impression 549, like 3, quote 0, reply 2, retweet 0

> Now, our subaccounts have -1 and 2 SOL respectively.
>
> The last piece of the 🧩 is that when you withdraw from a subaccount, the contract checks the margining type in the subaccount, not its cache.
>
> And you can always withdraw all assets from isolated margin accounts.


### Thread part 9 — @Neodyme — 2023-08-11 18:22 UTC (2023-08-11 19:22 WAT)

- URL: https://x.com/Neodyme/status/1690066220173918214
- Metrics (at fetch): bookmark 0, impression 551, like 2, quote 0, reply 1, retweet 0

> Hence, we can safely withdraw the 2 SOL from subaccount 2. The contract is now saddled with 1 SOL of bad debt. ⚡️
>
> The actual exploit used many subaccounts and larger values and ran multiple times, but the principle was the same. [pic.x.com/HMxh1G3zzR]

**Media:**
- photo: https://pbs.twimg.com/media/F3RQrGdbEAAUKMq.png — no alt text provided by author


### Thread part 10 — @Neodyme — 2023-08-11 18:22 UTC (2023-08-11 19:22 WAT)

- URL: https://x.com/Neodyme/status/1690066221566427137
- Metrics (at fetch): bookmark 0, impression 819, like 8, quote 1, reply 1, retweet 1

> The smallest errors can have grave consequences. That’s why it’s important to double-, triple- and quadruple-check your code.
>
> We will continue to assist cypher protocol in trying to find solutions for the difficult situation they are in.


### Thread part 11 — @Neodyme — 2023-08-11 18:22 UTC (2023-08-11 19:22 WAT)

- URL: https://x.com/Neodyme/status/1690066222526922752
- Metrics (at fetch): bookmark 1, impression 758, like 9, quote 0, reply 2, retweet 0

> If you liked this summary, follow us for more 🫡
>
> To read cypher’s full postmortem with more details, click here: https://cypherlabs.notion.site/cypher-exploit-7th-august-2023-post-mortem-ef01b5de613c4e52b36043c7649a5b40

**Links in post:** https://cypherlabs.notion.site/cypher-exploit-7th-august-2023-post-mortem-ef01b5de613c4e52b36043c7649a5b40


---

## 2023-08-10 · Post · Congrats to @b2ahex for winning  @PwnieAwards Top Desktop Bug category this year! Well deserved.


### Post — @Neodyme — 2023-08-10 02:10 UTC (2023-08-10 03:10 WAT)

- URL: https://x.com/Neodyme/status/1689459151599206400
- Metrics (at fetch): not returned

> Congrats to @b2ahex for winning  @PwnieAwards Top Desktop Bug category this year! Well deserved.
>
> It was a great honor to be nominated for our CS:GO 0day research - thank you! [pic.x.com/xSHBidlOr0]

**Media:**
- photo: https://pbs.twimg.com/media/F3IgaiEasAAA9ZK.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/F3IlYEtbsAAmD9i.jpg — no alt text provided by author


---

## 2023-08-02 · Post · We all know vyper's reentrancy locks didn't work. But why? How was it exploited? 


Tags (automatic): Smart contract / DeFi


### Post — @Neodyme — 2023-08-02 17:56 UTC (2023-08-02 18:56 WAT)

- URL: https://x.com/Neodyme/status/1686798090672500756
- Metrics (at fetch): not returned

> We all know vyper's reentrancy locks didn't work. But why? How was it exploited? 
>
> And why does this account hold more tokens than the total supply?
>
> Let's dive in 🧵👇 [pic.x.com/pYv8bqWLAf]

**Media:**
- photo: https://pbs.twimg.com/media/F2i09WEXcBM0aAF.jpg — no alt text provided by author


---

## 2023-07-31 · Post · 👾 You play CTF and still need a DEFCON ticket? 


### Post — @Neodyme — 2023-07-31 19:47 UTC (2023-07-31 20:47 WAT)

- URL: https://x.com/Neodyme/status/1686101286498734080
- Metrics (at fetch): not returned

> 👾 You play CTF and still need a DEFCON ticket? 
>
> We've 2 tickets left over and want to give them away! 
>
> Follow us and comment with your favourite CTF writeup to win!
>
> Ends Aug 3rd 12:00 CET 
> #defcon31 #DEFCON


---

## 2023-06-16 · Post · 🔐 Learn how to "Hack Cryptography" in our intense 2-day training at @defcon this year


### Post — @Neodyme — 2023-06-16 15:17 UTC (2023-06-16 16:17 WAT)

- URL: https://x.com/Neodyme/status/1669726003864715264
- Metrics (at fetch): not returned

> 🔐 Learn how to "Hack Cryptography" in our intense 2-day training at @defcon this year
>
> You will learn all about common mistakes made in cryptographic implementations and how they can be broken.
>
> Secure  your spot today!
>
> 📅 August 14th - 15th
> 📍Las Vegas
>
> https://training.defcon.org/products/ruben-gonzalez-hacking-cryptography

**Links in post:** https://training.defcon.org/products/ruben-gonzalez-hacking-cryptography


---

## 2023-06-10 · Post · &gt; tfw you audit Solana so well, the SEC considers it "security" [pic.x.com/cRe1fwH6eV] https://tw


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2023-06-10 19:57 UTC (2023-06-10 20:57 WAT)

- URL: https://x.com/Neodyme/status/1667622139577479168
- Metrics (at fetch): not returned

> &gt; tfw you audit Solana so well, the SEC considers it "security" [pic.x.com/cRe1fwH6eV] https://twitter.com/SolanaFndn/status/1667578529612017666

**Media:**
- photo: https://pbs.twimg.com/media/FySU4NJWcAMTUnX.png — no alt text provided by author

**Links in post:** https://twitter.com/SolanaFndn/status/1667578529612017666

**Quoted post (full text):**

    #### Quoted post — @1407411848446611459 — 2023-06-10 17:04 UTC (2023-06-10 18:04 WAT)
    
    - URL: https://x.com/1407411848446611459/status/1667578529612017666
    - Metrics (at fetch): not returned
    
    > The Solana Foundation disagrees with the characterization of SOL as a security. We welcome the continued engagement of policymakers as constructive partners on regulation to achieve legal clarity on these issues for the thousands of entrepreneurs across the U.S. building in the digital assets space.
    >
    > The Solana builder community is the strongest in the industry, and continues to build exceptional projects and products. The Solana Foundation remains committed to those building for the long-haul to continue to create the best blockchain for a decentralized future.
    


---

## 2023-06-09 · Post · Today at HackerHouseNYC, @r0bre will teach you how to kick greg out of your 5:5 multisig 👀


### Post — @Neodyme — 2023-06-09 16:22 UTC (2023-06-09 17:22 WAT)

- URL: https://x.com/Neodyme/status/1667205466831634434
- Metrics (at fetch): not returned

> Today at #HackerHouseNYC, @r0bre will teach you how to kick greg out of your 5:5 multisig 👀
>
> (Every Vote Counts: How to Hack a DAO. 2pm) [pic.x.com/4HJGqOotm0]

**Media:**
- photo: https://pbs.twimg.com/media/FyMaP0tXgAQQ8in.png — no alt text provided by author


---

## 2023-05-13 · Post · When CS:GO clients connected to our server, they got more than a game. We found 3 RCE vulnerabilitie


Tags (automatic): RCE


### Post — @Neodyme — 2023-05-13 17:21 UTC (2023-05-13 18:21 WAT)

- URL: https://x.com/Neodyme/status/1657435811409788928
- Metrics (at fetch): not returned

> When CS:GO clients connected to our server, they got more than a game. We found 3 RCE vulnerabilities to give clients an unexpected 'welcome'.
> Ready for a deep-dive? 🎮🔧🎆
>
> https://neodyme.io/blog/csgo_from_zero_to_0day/ #InfoSec #CSGO #Exploit

**Links in post:** https://neodyme.io/blog/csgo_from_zero_to_0day/


---

## 2023-03-10 · Post · Total Loss of Funds


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2023-03-10 19:24 UTC (2023-03-10 20:24 WAT)

- URL: https://x.com/Neodyme/status/1634274062796050435
- Metrics (at fetch): not returned

> Total Loss of Funds
>
> The story of Solana's highest-severity bug -- and how we found it back in late 2020. 
>
> Among other things, it allowed us to: 
> - Mint or steal any amount of any token
> - Modify any NFT
> - Delete liabilities in any lending protocol
>
> https://neodyme.io/blog/nonce-upon-a-time/

**Links in post:** https://neodyme.io/blog/nonce-upon-a-time/


---

## 2023-02-23 · Post · Indirect smart contract risk doesn't get enough attention.


Tags (automatic): Smart contract / DeFi


### Post — @Neodyme — 2023-02-23 11:44 UTC (2023-02-23 12:44 WAT)

- URL: https://x.com/Neodyme/status/1628722383350800385
- Metrics (at fetch): not returned

> Indirect smart contract risk doesn't get enough attention.
>
> Your contract doesn't need to have a bug to be exploited.
>
> 🧵👇


---

## 2023-02-14 · Post · ➡️ Training: Hacking Cryptography


### Post — @Neodyme — 2023-02-14 10:41 UTC (2023-02-14 11:41 WAT)

- URL: https://x.com/Neodyme/status/1625445238407069696
- Metrics (at fetch): not returned

> ➡️ Training: Hacking Cryptography
> Cryptography is hard and error prone.
>
> 🧠 Learn how to exploit cryptography and how to properly use it to defend yourself! 🧠
>
> Join us at @HITBSecConf for the onsite training!
>  📅17th - 19th April
> 📍Amsterdam https://conference.hitb.org/hitbsecconf2023ams/product/hacking-cryptography-hitb2023ams/

**Links in post:** https://conference.hitb.org/hitbsecconf2023ams/product/hacking-cryptography-hitb2023ams/


---

## 2022-12-06 · Post · Neodyme's @_localo_ @0x4d5aC @r0bre are competing in pwn2own with 2 entries: 


Tags (automatic): Path normalization, Memory corruption / native


### Post — @Neodyme — 2022-12-06 16:44 UTC (2022-12-06 17:44 WAT)

- URL: https://x.com/Neodyme/status/1600169323808571394
- Metrics (at fetch): bookmark 0, impression 0, like 12, quote 0, reply 0, retweet 3

> Neodyme's @_localo_ @0x4d5aC @r0bre are competing in #pwn2own with 2 entries: 
>
> In the SOHO smashup category, we will be demonstrating a Netgear Router -&gt; HP Printer exploit chain. 
>
> In addition, we have a second Netgear WAN exploit in our back pocket! https://t.co/MGVSaEJTGU

**Quoted post (full text):**

    #### Quoted post — @thezdi — 2022-12-06 00:48 UTC (2022-12-06 01:48 WAT)
    
    - URL: https://x.com/thezdi/status/1599928723259547648
    - Metrics (at fetch): bookmark 3, impression 0, like 63, quote 11, reply 1, retweet 8
    
    > After a herculean effort by the scheduling crew, the agenda for #Pwn2Own Toronto 2022 is now available. 26 contestants. 66 entries. Four days. It should be a great event. https://t.co/OT3TIr77aL
    


---

## 2022-11-15 · Thread · Many dApps need on-chain randomness. But how can you efficiently obtain true randomness in a decent


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2022-11-15 16:23 UTC (2022-11-15 17:23 WAT)

- URL: https://x.com/Neodyme/status/1592553924875014146
- Metrics (at fetch): bookmark 7, impression 0, like 39, quote 2, reply 4, retweet 14

> Many dApps need on-chain #randomness. But how can you efficiently obtain true randomness in a decentralised, trustless system? It turns out that this is an unsolved problem. Current solutions, including Verifiable Random Functions (VRFs), have fundamental issues. 🧵👇


### Thread part 2 — @Neodyme — 2022-11-15 16:23 UTC (2022-11-15 17:23 WAT)

- URL: https://x.com/Neodyme/status/1592553927450378240
- Metrics (at fetch): bookmark 0, impression 0, like 5, quote 0, reply 2, retweet 0

> As a result of this, most on-chain gambling or casino contracts are either vulnerable or centralised. In our latest blog post, we explore one of the most promising ways to solve this: Verifiable Delay Functions. (Warning: Maths)
> https://blog.neodyme.io/posts/secure-randomness-part-2/
>
> Here's a quick summary:

**Links in post:** https://blog.neodyme.io/posts/secure-randomness-part-2/


### Thread part 3 — @Neodyme — 2022-11-15 16:23 UTC (2022-11-15 17:23 WAT)

- URL: https://x.com/Neodyme/status/1592553929987878913
- Metrics (at fetch): bookmark 0, impression 0, like 5, quote 0, reply 1, retweet 0

> What are Verifiable Delay Functions (VDFs)? Put simply, they're functions whose evaluation involves a large number of sequential steps, but whose result can be verified very quickly.


### Thread part 4 — @Neodyme — 2022-11-15 16:23 UTC (2022-11-15 17:23 WAT)

- URL: https://x.com/Neodyme/status/1592553932613632000
- Metrics (at fetch): bookmark 0, impression 0, like 4, quote 0, reply 1, retweet 0

> How does this help for producing on-chain randomness? Well, one of the fundamental problems for crowdsourcing randomness on-chain is that anyone submitting inputs knows the inputs that were submitted before them.


### Thread part 5 — @Neodyme — 2022-11-15 16:23 UTC (2022-11-15 17:23 WAT)

- URL: https://x.com/Neodyme/status/1592553935310450688
- Metrics (at fetch): bookmark 0, impression 0, like 3, quote 0, reply 1, retweet 0

> As a result, the last participant to submit their input has a large degree of control over the output. For details on this, see our first blog post of this series: https://blog.neodyme.io/posts/secure-randomness-part-1/

**Links in post:** https://blog.neodyme.io/posts/secure-randomness-part-1/


### Thread part 6 — @Neodyme — 2022-11-15 16:23 UTC (2022-11-15 17:23 WAT)

- URL: https://x.com/Neodyme/status/1592553938313613313
- Metrics (at fetch): bookmark 0, impression 0, like 5, quote 0, reply 1, retweet 0

> VDFs prevent this.
> Their output is hard to predict &amp; slow to compute, but easy to verify.
> We can use their output as a seed for our random output.
>
> By only allowing user input before the output of the VDF is known, participants cannot predict how their input changes the output.


### Thread part 7 — @Neodyme — 2022-11-15 16:23 UTC (2022-11-15 17:23 WAT)

- URL: https://x.com/Neodyme/status/1592553940855402496
- Metrics (at fetch): bookmark 0, impression 0, like 4, quote 0, reply 1, retweet 0

> However, it's not clear whether a true VDF exists. In our blog post, we examine one of the best candidates, and also discuss what's needed to implement it on-chain.


### Thread part 8 — @Neodyme — 2022-11-15 16:23 UTC (2022-11-15 17:23 WAT)

- URL: https://x.com/Neodyme/status/1592553943355166721
- Metrics (at fetch): bookmark 0, impression 0, like 5, quote 0, reply 1, retweet 0

> We think on-chain randomness is one of the most important problems in the blockchain space, which is why it's so surprising that most current solutions are fundamentally lacking. By publishing this blog post, we hope to contribute to solving this.


### Thread part 9 — @Neodyme — 2022-11-15 16:23 UTC (2022-11-15 17:23 WAT)

- URL: https://x.com/Neodyme/status/1592553945989144576
- Metrics (at fetch): bookmark 0, impression 0, like 13, quote 0, reply 0, retweet 1

> Big thanks to @BenjWeso and @bramcohen for answering our questions on this one!


---

## 2022-11-12 · Thread · Who **actually** controls the largest projects on solana? What's the deal with Upgrade Authorities?


Tags (automatic): Smart contract / DeFi, Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2022-11-12 18:22 UTC (2022-11-12 19:22 WAT)

- URL: https://x.com/Neodyme/status/1591496755258040327
- Metrics (at fetch): bookmark 80, impression 0, like 284, quote 13, reply 15, retweet 82

> Who **actually** controls the largest projects on #solana? What's the deal with Upgrade Authorities? Are your funds more safu in DeFi contracts than they were on #FTX?
>
> Let's find out 🧵👇


### Thread part 2 — @Neodyme — 2022-11-12 18:22 UTC (2022-11-12 19:22 WAT)

- URL: https://x.com/Neodyme/status/1591496758051209216
- Metrics (at fetch): bookmark 1, impression 0, like 16, quote 0, reply 1, retweet 0

> For this thread, we analysed the Upgrade Authorities of the top 10 TVL projects on DefiLlama.


### Thread part 3 — @Neodyme — 2022-11-12 18:22 UTC (2022-11-12 19:22 WAT)

- URL: https://x.com/Neodyme/status/1591496760467214336
- Metrics (at fetch): bookmark 0, impression 0, like 15, quote 0, reply 1, retweet 0

> What are Upgrade Authorities (UAs)? 👮
>
> UAs are the accounts in charge of changing a solana program's code.
>
> Naturally, they pose a huge security risk. If you control the UA, you control the smart contract and its funds.


### Thread part 4 — @Neodyme — 2022-11-12 18:22 UTC (2022-11-12 19:22 WAT)

- URL: https://x.com/Neodyme/status/1591496762962808832
- Metrics (at fetch): bookmark 2, impression 0, like 10, quote 0, reply 2, retweet 0

> However, they are a necessary evil.
> If you want to fix a bug in a program, or add new features, this is done through UAs.
> For more info on UAs, check our blog post from June: https://t.co/SBdA1MMO4T


### Thread part 5 — @Neodyme — 2022-11-12 18:22 UTC (2022-11-12 19:22 WAT)

- URL: https://x.com/Neodyme/status/1591496765479407616
- Metrics (at fetch): bookmark 1, impression 0, like 14, quote 1, reply 2, retweet 0

> Specifically, the top 10 TVL projects we analysed are:
> - @solendprotocol
> - @MarinadeFinance
> - @LidoFinance
> - @RaydiumProtocol
> - @ProjectSerum
> - @TulipProtocol
> - @orca_so
> - @QuarryProtocol
> - @Saber_HQ
> - @Francium_Defi


### Thread part 6 — @Neodyme — 2022-11-12 18:22 UTC (2022-11-12 19:22 WAT)

- URL: https://x.com/Neodyme/status/1591496767987515393
- Metrics (at fetch): bookmark 3, impression 0, like 28, quote 2, reply 5, retweet 1

> Of the 10 projects analysed, we found the following about their upgrade authorities: (educated guesses)
>
> - 3 have a hot wallet 💩
> - 2 have a hardware wallet
> - 5 have a multisig or DAO
>
> Many are currently migrating to a mixed solution.


### Thread part 7 — @Neodyme — 2022-11-12 18:22 UTC (2022-11-12 19:22 WAT)

- URL: https://x.com/Neodyme/status/1591496770458042368
- Metrics (at fetch): bookmark 0, impression 0, like 14, quote 0, reply 1, retweet 1

> (This is pretty bad tbh)


### Thread part 8 — @Neodyme — 2022-11-12 18:22 UTC (2022-11-12 19:22 WAT)

- URL: https://x.com/Neodyme/status/1591496772810993664
- Metrics (at fetch): bookmark 0, impression 0, like 8, quote 0, reply 1, retweet 0

> How to verify this yourself? 🔬
> (Note that this only gives you information on how upgrades were handled so far)


### Thread part 9 — @Neodyme — 2022-11-12 18:22 UTC (2022-11-12 19:22 WAT)

- URL: https://x.com/Neodyme/status/1591496775256326144
- Metrics (at fetch): bookmark 0, impression 0, like 8, quote 0, reply 1, retweet 0

> First, you need to find the program address of the dApp you are trying to investigate. There are many ways to do this: Often, it is listed in the docs or open source code.


### Thread part 10 — @Neodyme — 2022-11-12 18:22 UTC (2022-11-12 19:22 WAT)

- URL: https://x.com/Neodyme/status/1591496777735102464
- Metrics (at fetch): bookmark 0, impression 0, like 6, quote 0, reply 1, retweet 0

> If not, you can try and see if a block explorer like solscan already knows the address of that dApp by its name. Finally, you can also do a test transaction and view the program it interacts with on-chain.


### Thread part 11 — @Neodyme — 2022-11-12 18:22 UTC (2022-11-12 19:22 WAT)

- URL: https://x.com/Neodyme/status/1591496785750413312
- Metrics (at fetch): bookmark 0, impression 0, like 7, quote 0, reply 1, retweet 0

> Once you have the program address, you can use any explorer of your choice to find its upgrade authority -- it's listed directly on its explorer page. You can also see the address of the program data and the last slot it was changed. https://t.co/Hz2epc9Opt

**Media:**
- photo: https://pbs.twimg.com/media/FhYh48bVEAAOBO6.jpg — alt text: "solana explorer: Upgrade Authority, Program Data, Last Deployment"


### Thread part 12 — @Neodyme — 2022-11-12 18:22 UTC (2022-11-12 19:22 WAT)

- URL: https://x.com/Neodyme/status/1591496792918528000
- Metrics (at fetch): bookmark 0, impression 0, like 5, quote 0, reply 1, retweet 0

> Using the explorer, you can navigate to the program data address. The transactions you see are the program upgrades. https://t.co/Q6qrLk6QoY

**Media:**
- photo: https://pbs.twimg.com/media/FhYh5XVUAAA7Rad.jpg — alt text: "program upgrades"


### Thread part 13 — @Neodyme — 2022-11-12 18:23 UTC (2022-11-12 19:23 WAT)

- URL: https://x.com/Neodyme/status/1591496800124383233
- Metrics (at fetch): bookmark 0, impression 0, like 6, quote 0, reply 1, retweet 0

> Lets check the UA. If there are many transactions within a few seconds landing in the same slot, the upgrade auth is almost certainly managed by a hot wallet. OTOH, if the upgrades are managed using a multisig or DAO, you can see this by program invocations in the upgrade txs. https://t.co/CCMNgTAgmy

**Media:**
- photo: https://pbs.twimg.com/media/FhYh5x-VIAAyqBx.jpg — alt text: "Hot wallet interactions"


### Thread part 14 — @Neodyme — 2022-11-12 18:23 UTC (2022-11-12 19:23 WAT)

- URL: https://x.com/Neodyme/status/1591496803165163520
- Metrics (at fetch): bookmark 1, impression 0, like 18, quote 0, reply 2, retweet 2

> If you see a hot wallet, or even a hardware wallet, being used as an upgrade authority for a major dApp, be careful when interacting with it. ⚠️ They potentially have the power to rug pull all of your funds.


### Thread part 15 — @Neodyme — 2022-11-12 18:23 UTC (2022-11-12 19:23 WAT)

- URL: https://x.com/Neodyme/status/1591496805727944704
- Metrics (at fetch): bookmark 1, impression 0, like 19, quote 0, reply 2, retweet 1

> We've been pushing for more transparency in upgrade authority handling for some time now.
>
> If you see a large project using a hot wallet or hardware wallet, you can help us by asking them why they haven't migrated to a multisig. Stay safe out there.


### Thread part 16 — @Neodyme — 2022-11-12 18:23 UTC (2022-11-12 19:23 WAT)

- URL: https://x.com/Neodyme/status/1591496808219361280
- Metrics (at fetch): bookmark 1, impression 0, like 29, quote 0, reply 2, retweet 4

> If you are running a large project and are still using a hot, or even cold wallet instead of a multisig or DAO,
>
> MIGRATE IT!


### Thread part 17 — @Neodyme — 2022-11-12 18:23 UTC (2022-11-12 19:23 WAT)

- URL: https://x.com/Neodyme/status/1591496810643668992
- Metrics (at fetch): bookmark 1, impression 0, like 26, quote 0, reply 2, retweet 0

> We gave a talk at #Breakpoint @SolanaConf about this topic last week. Follow us to get notified once it's online!


### Thread part 18 — @Neodyme — 2022-11-14 18:58 UTC (2022-11-14 19:58 WAT)

- URL: https://x.com/Neodyme/status/1592230496636833793
- Metrics (at fetch): bookmark 2, impression 0, like 2, quote 1, reply 0, retweet 0

> @SolanaConf UPDATE: The talk is now online! https://x.com/Neodyme/status/1592230224682397697

**Links in post:** https://x.com/Neodyme/status/1592230224682397697

**Quoted post (full text):**

    #### Quoted post — @Neodyme — 2022-11-14 18:57 UTC (2022-11-14 19:57 WAT)
    
    - URL: https://x.com/Neodyme/status/1592230224682397697
    - Metrics (at fetch): bookmark 3, impression 0, like 5, quote 2, reply 1, retweet 0
    
    > The video of our talk on upgrade authorities is now up: https://www.youtube.com/watch?v=zaDdEeZXvtw&t=5575s
    > 🎥 🍿
    
    **Links in post:** https://www.youtube.com/watch?v=zaDdEeZXvtw&t=5575s
    


---

## 2022-11-14 · Post · The video of our talk on upgrade authorities is now up: https://www.youtube.com/watch?v=zaDdEeZXvtw&


### Post — @Neodyme — 2022-11-14 18:57 UTC (2022-11-14 19:57 WAT)

- URL: https://x.com/Neodyme/status/1592230224682397697
- Metrics (at fetch): bookmark 3, impression 0, like 5, quote 2, reply 1, retweet 0

> The video of our talk on upgrade authorities is now up: https://www.youtube.com/watch?v=zaDdEeZXvtw&t=5575s
> 🎥 🍿

**Links in post:** https://www.youtube.com/watch?v=zaDdEeZXvtw&t=5575s


---

## 2022-10-24 · Post · Check out our newest blog post on one of the critical vulnerabilities we found in Solana's validator


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2022-10-24 21:26 UTC (2022-10-24 22:26 WAT)

- URL: https://x.com/Neodyme/status/1584657599722815488
- Metrics (at fetch): bookmark 6, impression 0, like 35, quote 1, reply 2, retweet 4

> Check out our newest blog post on one of the critical vulnerabilities we found in Solana's validator code. This bug allowed anyone to inflate their stake to virtually any value, disrupting consensus. It was quickly fixed after we reported it last year.
>
> https://t.co/08OZGdtN3F


---

## 2022-06-21 · Post · 1/4 🧵 


Tags (automatic): Smart contract / DeFi, Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2022-06-21 16:58 UTC (2022-06-21 17:58 WAT)

- URL: https://x.com/Neodyme/status/1539291735540506627
- Metrics (at fetch): not returned

> 1/4 🧵 
> There's been a lot of fuss around the recent #Solend DAO vote, with lots of discussion about what a protocol should be able to change about its #Solana smart contract.


---

## 2022-04-04 · Thread · We believe every software project should clearly communicate its bug bounty policies and how to get 


Tags (automatic): Smart contract / DeFi, Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2022-04-04 11:23 UTC (2022-04-04 12:23 WAT)

- URL: https://x.com/Neodyme/status/1510941148549894157
- Metrics (at fetch): bookmark 13, impression 0, like 103, quote 6, reply 3, retweet 19

> We believe every software project should clearly communicate its bug bounty policies and how to get in touch regarding security issues. In order to facilitate this, we brought security.txt to Solana:
> https://t.co/1aBxqEY0Yo


### Thread part 2 — @Neodyme — 2022-04-04 11:23 UTC (2022-04-04 12:23 WAT)

- URL: https://x.com/Neodyme/status/1510941152366714883
- Metrics (at fetch): bookmark 0, impression 0, like 8, quote 0, reply 1, retweet 0

> This data helps researchers to get in touch with you, even if they only have your program id. 
> We recently had trouble finding contact information for multiple smart contracts. This project has been born out of that very real frustration.


### Thread part 3 — @Neodyme — 2022-04-04 11:23 UTC (2022-04-04 12:23 WAT)

- URL: https://x.com/Neodyme/status/1510941155466354688
- Metrics (at fetch): bookmark 0, impression 0, like 8, quote 0, reply 0, retweet 0

> Check out https://t.co/jTcoRHas8S for an example.
> We've also provided you with bounty policies templates in our repository to make it as easy as possible to get going.


---

## 2021-12-03 · Thread · We recently discovered a critical bug in the token-lending contract of the solana-program-library (S


Tags (automatic): Blockchain / L1-L2 / bridge


### Post — @Neodyme — 2021-12-03 21:41 UTC (2021-12-03 22:41 WAT)

- URL: https://x.com/Neodyme/status/1466885443019063301
- Metrics (at fetch): bookmark 99, impression 0, like 683, quote 58, reply 35, retweet 140

> We recently discovered a critical bug in the token-lending contract of the solana-program-library (SPL). This blog post details our journey from discovery, through exploitation and coordinated disclosure, and finally the fix.


### Thread part 2 — @Neodyme — 2021-12-03 21:41 UTC (2021-12-03 22:41 WAT)

- URL: https://x.com/Neodyme/status/1466885444285698060
- Metrics (at fetch): bookmark 0, impression 0, like 90, quote 7, reply 2, retweet 3

> The total TVL at risk was about 2.600.000.000 USD. Some of that value is lent out, and some other low-value coins are not economically viable to steal, but the potential profit was easily in the hundreds of millions.


### Thread part 3 — @Neodyme — 2021-12-03 21:41 UTC (2021-12-03 22:41 WAT)

- URL: https://x.com/Neodyme/status/1466885445225263115
- Metrics (at fetch): bookmark 1, impression 0, like 90, quote 2, reply 2, retweet 3

> The bug was fixed, and dapps updated promptly to close the vulnerability. We believe the most secure code is open-source, and as auditors we believe one of the best ways to write better code is to understand vulnerabilities.


### Thread part 4 — @Neodyme — 2021-12-03 21:41 UTC (2021-12-03 22:41 WAT)

- URL: https://x.com/Neodyme/status/1466885446277943299
- Metrics (at fetch): bookmark 35, impression 0, like 177, quote 8, reply 6, retweet 26

> As such, we’ve written up a dive into how this vulnerability could have been exploited, and how we found it: https://blog.neodyme.io/posts/lending_disclosure

**Links in post:** https://blog.neodyme.io/posts/lending_disclosure
