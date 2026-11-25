# Telegram Desktop

- **Source URL:** https://medium.com/@expatch/telegram-desktop-from-proxy-to-rce-in-35-seconds-64de025fb0b4
- **Fetched from:** https://medium.com/@expatch/telegram-desktop-from-proxy-to-rce-in-35-seconds-64de025fb0b4?source=rss-febdd385b95a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14924)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** ExPatch Security / Fri, 25 Sep 2026 15:52:23 GMT

**A proxy gets your work chat back online. On Windows builds, it could also expose your identity, leak credentials, and open a path into your company’s network.**

Aleksander Rostilov and Denis Rostilov · ExPatch Vulnerability Research

It’s the start of the workday. A developer opens Telegram to catch up with the team. The app cannot connect. The authorities have blocked Telegram, seeing it as a threat to their regime.

Someone shares a proxy to get Telegram working again. The developer adds it, the messages load, and work carries on.

While the developer reads the chat, the proxy operator collects API keys, credentials, and information about the corporate network. These details help identify who is behind the connection and which company the victim works for.

The attack continues inside the company. The operator sees that the account has sufficient privileges and can use it to run commands on company systems. The developer’s computer receives an NTLM challenge from the proxy, signs it, and sends it back. The developer keeps reading the chat and talking to colleagues. Everything works normally.

The operator obtains an NTLM hash, sends it to Windows Server, Outlook, and the VPN, and authenticates to the corporate infrastructure using the lead developer’s credentials. The antivirus notices nothing: the traffic is legitimate. Just 35 seconds after the developer connects to the proxy in Telegram Desktop, the operator has full control over everything happening inside the company, with direct access to every computer and service.

What makes this alarming is how easily and quietly the proxy operator gains control of the company’s entire network.

Proxies are a built-in Telegram feature: they route the app’s connection through another server, helping users get online when direct access is blocked.

We found that a malicious proxy could make Telegram Desktop on Windows authenticate with the user’s Windows account automatically. A separate bug could leak pieces of the application’s memory.

In our lab, an official, unmodified Telegram Desktop client connected to the proxy. Within approximately **30–35 seconds, we gained SYSTEM privileges on a workstation and a domain controller**. We could run commands remotely with high Windows privileges: remote code execution, or RCE.

We used a Domain Admin account and a corporate certificate service vulnerable to authentication relay — a standard setup across all corporations. **All nine relay attempts succeeded.**

Watch the RCE demonstration:

[https://www.youtube.com/watch?v=pm3KCNDc9eY](https://www.youtube.com/watch?v=pm3KCNDc9eY)

*Telegram Desktop 6.8.2, an unmodified client, and a controlled Windows test domain.*

Telegram Desktop uses a networking library called Qt. A malicious proxy could ask it for Windows authentication, and Qt could respond using the signed-in user’s account without asking permission.

The attacker could forward that exchange to another service that accepted it. This is **NTLM relay**: using someone’s authentication to sign in elsewhere without knowing their password.

In our test, the receiving service issued a certificate for the victim’s account. We used that certificate to authenticate as the victim and run commands on company systems. These included the domain controller — the server that manages the company’s Windows accounts.

The victim’s permissions determined how far the attack could go. The proxy supplied the entry point.

RCE was the most severe outcome we demonstrated. The findings also created risks of **deanonymization and credential exposure**:

\- **Logins and identity clues:** Windows username, computer name, and corporate domain. These could link a pseudonymous user to a workplace or a real identity.

\- **Hashes and authentication data:** NTLMv2 challenge-response data, often called NetNTLMv2 hashes, plus earlier authentication messages recovered from memory.

\- **Passwords and API keys:** we recovered test passwords and API-secret. Real passwords and API keys could also leak if present in the exposed buffers.

\- **Network details:** internal addresses, infrastructure information, VPN software, and network adapters.

The password exposure came from process memory.

For people living under censorship and state surveillance, the consequences could be especially serious. In vulnerable Telegram Desktop builds, connecting to a malicious proxy could expose information that helped identify the user and their employer. An attempt to bypass restrictions and preserve privacy could lead to deanonymization.

A separate Qt bug made authentication responses include pieces of process memory — data the application had held in its buffers.

One response could expose roughly **65 KB**. Repeating the exchange 100 times produced about **6.5 MB in five minutes**, including HTTP headers, network data, and earlier authentication messages.

The connection could continue working without a visible warning. What leaked depended on the contents of memory. This was a separate issue from the relay chain used for RCE.

Categories of process data recovered during the laboratory tests:

Watch the memory disclosure demonstration:

[https://www.youtube.com/watch?v=hMg8Vm8TZCU](https://www.youtube.com/watch?v=hMg8Vm8TZCU)

On June 16, 2026, Telegram told us that Desktop **6.9.2** addressed the reported scenarios, with an exception for system-wide proxies.

NTLM was disabled for proxies configured inside Telegram. It remained available for system proxy configurations. The patches also corrected the memory disclosure bug.

Keep Telegram Desktop updated. Corporate administrators should also review system proxy settings and protection against NTLM relay.

We reported the findings on June 6. By June 8, patches had appeared in Telegram’s dependency repository. Related Qt changes followed.

In the Qt change history we reviewed, we found no mention of ExPatch or the researchers. We had not been informed of coordination with the Qt developers.

Our full publication includes the correspondence and patch comparison. The matching changes support our concerns, but do not establish exactly how the information reached Qt. We are asking Telegram and Qt to clarify that history and credit the research where appropriate.

This is a shortened version of our original write-up. The full article includes technical analysis, additional attack paths, tests of other Qt applications, and the disclosure record.

[Read the original write-up on Medium](https://medium.com/@expatch/we-trusted-telegram-with-our-research-to-protect-users-and-were-written-out-of-the-story-8e64d0e58972)

**ExPatch Vulnerability Research** · security@expatch.llc
