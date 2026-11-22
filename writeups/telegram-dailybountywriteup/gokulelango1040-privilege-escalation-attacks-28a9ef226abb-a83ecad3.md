# Privilege Escalation Attacks

- **Source URL:** https://medium.com/@gokulelango1040/privilege-escalation-attacks-28a9ef226abb?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230127222116/https://medium.com/@gokulelango1040/privilege-escalation-attacks-28a9ef226abb
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1465 (id 1465)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege Escalation Attacks

Attacks known as privilege escalation attempt to gain increased access to important systems, applications, and networks by taking advantage of security flaws.

Due to a lack of attention paid to permission levels, many firms are vulnerable to privilege escalation. Security measures therefore are insufficient to stop a privilege escalation.

Attacks involving privilege escalation happen when a threat actor logs into the account of an employee, skips the appropriate permission channel, and successfully acquires access to information they shouldn’t have. Threat actors often use these assaults to exfiltrate data, interfere with business operations, or build backdoor.

**Two Types Attacks**

1. **Vertical**

Vertical attacks are when an attacker gains access to an account with the intent to perform actions as that user.

1. **Horizontal.**

Horizontal attacks gain access to account(s) with limited permissions requiring an escalation of privileges, such as to an administrator role, to perform the desired actions.

# Examples Of Privilege Escalation Attacks

1. Windows Sticky Keys
2. Windows Sysinternals
3. Process Injection
4. Linux Passwd User Enumeration
5. Android Metasploit

# How To Prevent A Privilege Escalation Attack

1. Unfortunately, users are the security system’s weakest link. They might compromise a machine or network with only one click. Businesses are developing **security awareness programmes** and a system for evaluating the training’s efficacy in order to reduce this risk. Most of the time, phishing simulation programmes like KnowBe4, GoPhish, or Phishme can successfully train users to recognise phishing email attempts.
2. The last line of defence against efforts to escalate privileges is an **intrusion detection system (IDS) and/or intrusion prevention system (IPS).**
3. Every day, new exploits are developed, and it is up to us to make sure we are secure against the assault. All systems and applications will be updated with the most recent fixes thanks to a good **patch management procedure**.

# What Can You Do During An Incident?

It’s crucial to isolate the issue in the event that you come under this kind of attack.

**Change the password and disable the account** if you’ve found the compromised account.

Check the system, **shut down** any strange accounts, and **change the passwords for all user accounts** previously connected to that device.

*Thank you for Reading This content.I hope you got some Knowledge from this post.Grow your Knowledge with medium.*
