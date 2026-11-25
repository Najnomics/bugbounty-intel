# When a Security Product Can’t Protect Itself

- **Source URL:** https://medium.com/@furkanyasinkeskin/when-a-security-product-cant-protect-itself-my-responsible-disclosure-story-with-the-endpoint-c374c475f2eb
- **Fetched from:** https://medium.com/@furkanyasinkeskin/when-a-security-product-cant-protect-itself-my-responsible-disclosure-story-with-the-endpoint-c374c475f2eb?source=rss-d02c8a77fb7f------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14966 (id 14966)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Furkan Yasin Keskin / Sat, 31 Oct 2026 20:06:36 GMT

*🇹🇷 Bu yazının Türkçesi için tıklayın*

We trust an EDR, DLP or UEM agent for a simple reason: it is on the machine when we are not. But there is a question we rarely ask: **who protects the agent itself?**

This post covers a roughly six-month disclosure process for a behavior I found in the ManageEngine Endpoint Central agent.

While testing Endpoint Central Agent **v11.4.2516.37.W**, I found that the agent could be completely removed by manipulating its MSI and registry components, even with **Self-Defense** and **Uninstall Password Protection** enabled.

In other words, the product’s promise that the agent cannot be removed did not hold under certain conditions. Once the agent was gone, so were the patch management, application control, device control and browser policies delivered through it.

*I am deliberately not sharing the technical steps. The issue is fixed in current versions, but some environments may still run older ones.*

I reported the finding through Zoho’s bug bounty program as a responsible disclosure.

In December 2025 the report entered triage and its CVSS score was lowered from 7.7 to 4.4. Then came the longest part: deciding how to classify the impact.

The vendor’s position was that this behavior requires SYSTEM/Administrator privileges, which falls outside the program’s scope. Microsoft’s servicing criteria also do not treat the boundary between an administrator and the kernel as a security boundary.

My argument was that the issue is not about gaining privileges. It is about being able to completely disable the protection mechanism the product’s security guarantees rely on. If a product advertises malware and ransomware protection and DLP enforcement through this agent, an agent without tamper protection directly reduces the effectiveness of those controls. This maps directly to the MITRE ATT&CK techniques for impairing defenses and indicator removal. Disabling security agents is usually one of the first things ransomware operators do.

The response in May 2026 kept the report as **Informative**. But it also contained an important piece of news: **kernel-level driver protection** against agent tampering had been implemented. It was being rolled out in phases, and customers who needed it right away could enable it from the console.

The support team also confirmed that upgrading to version **11.5.2605** fully resolves the issue, with no manual workarounds needed.

Reporting is not enough; you have to verify. I repeated the same tests on agent version **11.5.2616.20.W**: Agent Protection now works as expected against third-party uninstall and tampering attempts.

With one condition: the setting has to be enabled for the protection to fully take effect.

**Agent Settings → Agent Protection Settings → Prevent Agent Data Tampering**

Such an important self-protection improvement is neither clearly mentioned nor highlighted in the release notes. Many organizations running Endpoint Central may not know this protection exists, or that it has to be enabled separately.

Credit where credit is due: even though the report stayed “Informative,” the ManageEngine team took the feedback seriously, kept me updated throughout, and shipped a real improvement.

*Sometimes the most important update is not a new feature, but a security product getting better at protecting itself.*
