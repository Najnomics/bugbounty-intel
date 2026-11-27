# Threat Hunting for Privilege Escalation -LetsDefend

- **Source URL:** https://medium.com/@firdansp/threat-hunting-for-privilege-escalation-letsdefend-ab7f6abc3ede?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@firdansp
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 13699)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
This write-up is based on a training scenario from LetsDefend and is shared for educational purposes only.

Hello everyone,

I’m **Fir** (find me on [LinkedIn](https://www.linkedin.com/in/firdansp/)). In this article, I’ll share my **threat hunting investigation** based on a **privilege escalation scenario** from LetsDefend.

In this lab, I analyzed endpoint logs to identify **credential dumping activity, suspicious account behavior,** and **lateral movement attempts.** The goal was to understand how attackers escalate privileges and move within the network.

#### 🧠 Hypothesis

Attackers may attempt privilege escalation by dumping credentials, creating unauthorized accounts, and using valid credentials to move laterally across systems.

#### Step 1 : Detecting Credential Dumping Activity

I started by identifying systems where **credential dumping** activity occurred. This confirms that attackers attempted to e**xtract credentials** from memory.

Affected system IP: 172.16.40.67

Malicious process: mimikatz.exe

#### Step 2 : Account Discovery & Persistence Attempt

Next, I analyzed account-related activity on the same system. This indicates **privilege escalation attempts by targeting high-privilege groups.**

Username attempted to be created: john.ters

Target group enumerated: administrators

#### Step 3 : Suspicious Login Activity

I investigated login history prior to the attack. This account becomes a key pivot point in the investigation.

User logged in before attack: melissa

#### Step 4 : Lateral Movement Detection

I then analyzed how this account was used across the network. This shows **both failed** and **successful lateral movement attempts.**

Failed access attempts to different systems: 3

Successful access to system: 172.16.40.75

#### Step 5 : Post-Access Activity on Target System

Finally, I investigated activity on the compromised target system. This indicates system/user discovery after gaining access.

Process used: whoami.exe

#### Conclusion

This investigation highlights how attackers move from **credential access** to **privilege escalation** and **lateral movement** within a network. Starting from **credential dumping using tools like Mimikatz,** the attacker **attempts to gain higher privileges by targeting administrative groups** and **creating new accounts**. By **leveraging valid credentials,** they perform **lateral movement across systems** and **execute reconnaissance commands after gaining access.** This kind of behavior shows that privilege escalation is not a single action, but a chain of activities that can be uncovered by correlating endpoint logs, authentication events, and process execution data.

Thanks for reading! If you’re learning **threat hunting** or building your **SOC skills,** feel free to share your thoughts in the comments 👋

What part of threat hunting are you currently exploring? 🔥
