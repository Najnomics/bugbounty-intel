# 🤖 AI and Cyber Threats: The Arms Race of 2025

- **Source URL:** https://tlpblack.net/blog/20251218-cybersecurity-year-in-review
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1032 (id 1032)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Looking Back at 2025's Cybersecurity Landscape: Key Trends to Watch in 2026

An intelligence analyst's perspective on the dominant cybersecurity trends of 2025, from AI-driven threats to supply chain vulnerabilities and the evolving APT landscape

## An Intelligence Analyst's Perspective on the Threat Landscape

As we move through 2025, the global cyber threat ecosystem has undergone **one of the most accelerated runs in recent history**. The widespread adoption of generative AI, the expansion of open-source ecosystems, and the increasing interdependence of supply chains and clouds have greatly reshaped the attack surface. Threat actors - from low-skill fraudsters to state-sponsored advanced persistent threat (APT) groups - are **leveraging automation and AI-enabled decision-making to scale operations at unprecedented speed**, while most organizations struggle to respond under a barrage of vulnerabilities, patches and new attack vectors.

We at TLPBLACK attempted to look at what happened in 2025 with a threat intelligence mindset and came up with several **dominant trends**. These trends **define today's cybersecurity landscape**. Each trend reflects not only the escalation of attacker capabilities but also the widening asymmetries defenders must confront.

If you work in cyber security, for a SOC, in CTI, a CERT or simply care about online safety, this post is for you. And most importantly: thank you for all your hard work this year!

Enjoy!

## 1. AI-Driven Threats and Defenses: The Acceleration of the Human-Silicon Arms Race

Never before has the conflict between humans and silicon been more obvious. In 2025, we observed the development of what can only be described as a **human-silicon arms race**. AI now underpins both offensive and defensive operations. Sadly, it appears to us that - and there is no way to sugarcoat this - for now the attackers retain a notable agility advantage.

*AI-Driven Threats and Defenses*

Several developments are particularly illustrative:

- **LLM Weaponization:** Tools such as WormGPT and FraudGPT continue to democratize malicious capabilities. This means more cybercriminals can do more attacks, in a cheaper fashion with a higher chance of success.
- **AI-Forged Executive Impersonation:** A [foiled attack on Ferrari](https://sloanreview.mit.edu/article/how-ferrari-hit-the-brakes-on-a-deepfake-ceo/) showcased the growing precision of voice cloning. Criminals replicated CEO Benedetto Vigna's voice to authorize a multimillion-euro transfer, stopped only by an improvised verification challenge. One of our members from TLPBLACK shared a personal experience on a similar attack. A family member received a phone call, in local native language, from someone who wanted the targeted person to become an investor into what clearly sounded like a phishing scheme. While the scheme was obvious and the person immediately got suspicious, what was not obvious was that the "person" on the other side was not a person, but an AI. The speed at which it was answering and its reluctance to give answers to simple questions such as "who am I?" coupled with it reverting back to its script over and over on failure gave it away. Unfortunately, this ability to stop attacks because the other side is too slow to evaluate answers won't last long, as models become faster and smarter. This was predicted since appearance of AI - the unprecendented scale and low cost of social engineering attacks. This is happening now.
- **Autonomous Espionage:** Sophisticated adversaries have already managed to bypass security restrictions in frontier models such as those from Anthropic to power their operations. According to an [Anthropic report](https://www.anthropic.com/news/disrupting-AI-espionage) that **could have had a few more IOCs (aka eye-awks)**, in September, some unknown Chinese state-linked operators conducted a medium scale, AI-orchestrated cyber-espionage campaign. They used an agentic version of Claude Code to autonomously infiltrate approximately 30 global targets; a subset of these suffered successful data exfiltration. This isn't necessarily news, and we know that nation-states are actively exploring AI-directed intrusion frameworks requiring minimal human oversight. Several companies have been founded - many years ago - to work specifically on this topic. Again, it is a bit hard to swallow this report from Anthropic that appears to have been written by marketing folks rather than analysts and includes no IOCs, but it **would be foolish to assume this is not already happening at 12x the scale**.
- **AI-Supercharged Malware and Ransomware:** What worries us the most is not necessarily the top-end actors using AI to become more high-end, but low-skilled actors leveraging AI to become just as good or almost as good as high-end APTs. For instance, AI is already used to generate bespoke ransomware variants, and dark-web offerings - such as $200 stealer kits - continue to lower entry barriers. According to researchers from TeamT5 generative AI has been adopted by a number of threat actors such as Chinese nexus threat actors including SLIME87, GouShe (aka TropicTropper, Keyboy), TeleBoyi, but also Lazarus, Konni, Kimsuky (aka CloudDragon).
- **AI Hallucination-induced vulnerabilities and "copying the masters":** In general AI is only as good as the data it is trained on. If the base data is poisoned or incorrect, the results will also reflect that. Although prompt engineering can get rid of most hallucinations, some results are way more subtle and harder to spot. This creates an opportunity for incorrect and misleading intelligence which leads to failures. In an [article for Lawfare, Dave Aitel and Dan Geer](https://www.lawfaremedia.org/article/ai-and-secure-code-generation) argue that *"traditional ways of evaluating security—counting bugs, reviewing code, and tracing human intent—are becoming obsolete"*. They are right.
- **The flood of Deep Fakes:** In the past year, deep fakes and most importantly ads or propaganda flooded social networks. From posts trying to convince victims to deposit money (FIAT or crypto) into schemes promising 5, 10 or 20x ROI, to propaganda and influence campaigns trying to discredit or boost specific politicians, the EU or the War in Ukraine. Another formula for using fake AI-generated content is creating Instagram / TikTok / Youtube channels publishing ridiculous photos / videos (for example [Italian Brainrot](https://en.wikipedia.org/wiki/Italian_brainrot)). Once these pages gain momentum (5-10-20k followers) they immediately change their name, picture, description to support a specific politician or event. This became extremely visible, for example, in Romania when a lot of Facebook pages related to cooking or traveling started supporting, overnight, a specific public figure. Unfortunately, for many users, their only weapon is to unsubscribe, but sadly, the damage has already been done. You can read more about this in the following articles (original articles in Romanian):
  - [Vietnamese accounts and AI-error bots. Behind the scenes of the parallel internet promoting Anca Alexandrescu](https://publicrecord.ro/2025/11/11/conturi-vietnameze-si-boti-cu-erori-de-ai-in-culisele-internetului-paralel-care-o-promoveaza-pe-anca-alexandrescu/)
  - [Marcel Ciolacu’s bot farm has entered the electoral campaign](https://investigatoria.ro/2025/11/15/ferma-de-boti-a-lui-marcel-ciolacu-a-intrat-in-campanie-electorala/)
  - [#WeDoItWithBots: The network of fake pages in Daniel Băluță’s campaign](https://funky.ong/facem-cu-boti-reteaua-de-pagini-false-din-campania-lui-daniel-baluta/)
  - [30 commercial pages became pro-Băluță ‘citizens’ in two weeks](https://buletin.de/bucuresti/analiza-funky-citizens-30-de-pagini-comerciale-au-devenit-cetateni-pro-baluta-in-doua-saptamani/)
- **LLM Prompt Injections:** As more users adopt LLMs running locally on their machines, a new method of stealing information emerged. It reminds us of the old pop-ups on specific malicious web pages telling users to press F12, open dev tools and then paste some obfuscated Javascript code in the `Console`. This led to a lot of popular websites printing using `console.log` messages such as "In case you were told, do not paste any code in here!". Unfortunately, this new **Prompt Injection** method is more advanced than that and it involves adding hidden text inside pieces of code, images, or any other artefacts that might be processed by a local LLM such as `Claude Code` or `Cursor`. Some reported examples are [prompt Injection using benign images](https://www.radware.com/blog/threat-intelligence/weaponizing-images/). These kinds of attacks rely on users pressing "allow everything" when prompted by their local LLM to perform actions. Since more and more people start using LLMs in their daily lives these complex attacks are here to stay.

More on the defense side, the landscape is equally dynamic but in our opinion, somehow lagging behind. Most organizations we know **deploy some form of AI for threat intelligence**, behavioral analytics, and automated response. However, they all have to obey the same physics law which states that "the attacker only needs to be successful once, while defenders need to be successful every time".

This leads us to believe the field is nearing a tipping point: we can anticipate a year defined by **machine-versus-machine conflict**, necessitating secure code-generation practices, practical AI limitations / governance, and collaborative intelligence sharing to mitigate rising deepfake-related losses. You all know what to do!

## 2. Supply Chain Vulnerabilities: The Open-Source Trust Crisis Deepens

Supply chain exploitation has become one of 2025's defining challenges, with attackers frequently bypassing hardened perimeter defenses by compromising upstream dependencies. Last year brought some of the most interesting attacks in history, such as the [XZUtils supply chain attack](https://en.wikipedia.org/wiki/XZ_Utils_backdoor); but let us tell you one thing: 2025 didn't disappoint either. In our opinion, these disruptive incidents highlight a systemic fragility in open-source ecosystems. Here are some examples:

- **Shai-Hulud Worm (September 2025):** First of all, we [agree with John Hultquist](https://x.com/JohnHultquist/status/1968285959310733459) that it's a terrible name. That aside, an interesting and potentially devastating attack with unpredictable consequences for years to come. Initially compromising **180+ npm packages**, including super popular libraries such as tinycolor, this worm propagated via stolen maintainer tokens and malicious preinstall scripts. Its speed and wide reach is a perfect example of what characterizes today's open-source targeting campaigns. Although we doubt an APT was behind this, nevertheless it will power years of compromises going forward thanks to the stolen credentials.
- **Shai-Hulud 2.0 ("The Second Coming") (November 2025):** Two months later we saw another wave of this self replicating worm, first expanding its initial footprint to **700–830+ packages**, trojanizing repositories from major organizations like Zapier, PostHog, Postman, and ENS Domains. This was probably fueled by the previous wave of credentials collection from Shai-Hulud 1.0.
- **React2Shell (CVE-2025-55182):** In our opinion, this is possibly **the biggest cybersecurity story of 2025**. [We wrote about it in detail on our blog](https://tlpblack.net/blog/20251209-the-anatomy-of-a-react2shell-compromise). This critical zero-day in React DevTools enabled remote code execution in a rather simple way leading to its "pure" CVSS rating 10.0. Leveraged [both by APTs and cybercriminals](https://cloud.google.com/blog/topics/threat-intelligence/threat-actors-exploit-react2shell-cve-2025-55182), We think this will be with us for a long time. The reason is that patching is not straightforward; if with a vulnerable Windows version or Linux, all you need to do is just update, sometimes automatically, React applications need to be upgraded with the new safe libraries and re-deployed. This won't happen automatically in most cases, leaving many open doors. The only hope is that cloud and platform providers have implemented other mitigations on their side, which can thwart some attacks.

*Supply Chain Vulnerabilities*

These events have catalyzed urgent industry-wide calls for **[mandatory SBOM adoption](https://www.cisa.gov/sbom)** (we are not fans, but oh well), **runtime dependency scanning**, **reproducible builds**, **[SDL](https://www.microsoft.com/en-us/securityengineering/sdl/)**, **package-signing enforcement**, and stricter controls over repository mirroring to prevent cross-ecosystem contamination. And no, [the pledge won't help](https://www.ivanti.com/resources/secure-by-design/2024).

From an intelligence standpoint, we think **trust in open-source infrastructure has reached a critical inflection point**. Open source doesn't automatically mean more secure.

## 3. Ransomware and APT Evolution: Scalability, Speed, and Geopolitics

*Ransomware and APT Evolution*

Ransomware activity in 2025 has continued undisturbed by what appear to be fewer law enforcement actions as in previous years.

Some key dynamics on the bad guys' side include:

- **Operational Acceleration:** Breakout times routinely fall below 24 hours, often leveraging living-off-the-land binaries for stealth. **Data exfiltration** comes right before encryption, with the full "ransomware experience" package incorporating harassment, service disruption, or integrity sabotage.
- **RaaS and Affiliate Expansion:** The number of active ransomware groups has risen, with rapid growth from Qilin, Akira, DragonForce and the revitalized [LockBit 5.0 ecosystem](https://www.trendmicro.com/en_us/research/25/i/lockbit-5-targets-windows-linux-esxi.html).
- **Nation-State Intersections:** This is by far the most interesting part. We often see that APT groups aligned with geopolitical interests are increasingly blending criminal and strategic goals:
  - **Lazarus (North Korea)** continues using ransomware and crypto theft to fund state operations.
  - **Sandworm (Russia)** has targeted European energy infrastructure for disruption, sabotage and wreaking chaos in the west.
  - **Volt Typhoon (China)** maintains pre-positioning within U.S. utilities, water, and telecom networks. These could be used for devastating purposes at a [future time](https://defence-blog.com/taiwan-warns-of-potential-2027-chinese-invasion/).
  - **Iran-linked actors** are expanding access into Gulf-region telecom providers.

The overall financial impact is also severe: median ransoms have risen and [the impact on critical infrastructure is more and more visible](https://www.infosecurity-magazine.com/news/ransomware-victims-shut-operations/). From what we have seen, healthcare, the public sector, energy and manufacturing remain the top targets.

To stay safe, we recommend investing into **immutable backups**, **microsegmentation** (both network and containers) and rapid, live **patching**.

## 4. APT Exploitation of Zero-Days in Network and Edge Devices

Top class APT groups - especially those with [China-nexus affiliations are increasingly exploiting zero-day vulnerabilities](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4287371/nsa-and-others-provide-guidance-to-counter-china-state-sponsored-actors-targeti/) in **edge infrastructure**, including VPNs and security appliances that traditionally serve as organizational gateways.

Because these devices sit outside typical logging pathways and often lack robust integrity monitoring, they offer attackers durable, high-value persistence mechanisms.

*APT Exploitation of Zero-Days in Network and Edge Devices*

One of our favorite "new" actors is [UNC5221, a suspected China-nexus advanced persistent threat (APT) group tracked by Mandiant (Google Threat Intelligence)](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign). They have repeatedly demonstrated sophisticated tactics in compromising virtualization environments to evade detection. For instance, in a notable campaign targeting US-based organizations, including a high-profile intrusion at the MITRE Corporation in late 2023, **UNC5221 exploited 0-day vulnerabilities in Ivanti Connect Secure appliances to gain initial access**. Once inside, they moved laterally to reach the VMware vCenter infrastructure. There, they created rogue virtual machines to host their toolsets. These hidden VMs ran the custom BRICKSTORM backdoor, which is written in Golang and was probably **one of the most challenging samples we ever had to write a YARA rule** for.

While UNC5221's activities have primarily centered on VMware ecosystems rather than Cisco devices directly, similar China-nexus groups exhibit overlapping interests in edge and network appliances. **UNC3886**, another highly evasive China-linked espionage actor, has a history of targeting network devices and hypervisors (including VMware ESXi and vCenter) using zero-days in Fortinet, Ivanti, and other platforms. UNC3886 deploys custom malware, publicly available rootkits like REPTILE and MEDUSA, and backdoors leveraging legitimate services (e.g., GitHub and Google Drive) for persistence across layers such as guest VMs, hypervisors, and network appliances.

In the context of Cisco devices, other China-nexus APTs such as BlackTech and groups associated with [broader mess known as "Salt Typhoon"](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4287371/nsa-and-others-provide-guidance-to-counter-china-state-sponsored-actors-targeti/) have been observed **compromising Cisco IOS XE routers through vulnerabilities like CVE-2023-20198 and CVE-2023-20273**. These intrusions involve implanting backdoors in firmware, abusing features like Cisco Guest Shell (a Linux container environment on routers), and modifying configurations for stealthy persistence. Although direct installation of containers or VMs by these groups on Cisco hardware is less commonly reported than firmware modifications or rootkit deployment, the abuse of container-like capabilities (e.g., Guest Shell or IOx app hosting) aligns with tactics to run malicious code in isolated, hard-to-detect environments on network edge devices.

These operations highlight a **broader trend among China-nexus actors (and not only)**: prioritizing compromising edge infrastructure and virtualization layers lacking robust EDR coverage. They do this to achieve long-term access, credential theft, and espionage.

For defenders, this trend reinforces the need for **rapid patch cycles**, **out-of-band monitoring**, and **strict access controls** around edge systems that function as infrastructural choke points. We want to [emphasize the out-of-band network tap, which together with a diligent sysadmin watching the logs is NSA's favorite scenario](https://www.wired.com/2016/01/nsa-hacker-chief-explains-how-to-keep-him-out-of-your-system/). Organizations operating Cisco or VMware environments should invest into patching (again, this!), monitor for unregistered VMs or anomalous container activity, and implement integrity checks to counter such stealthy persistence mechanisms.

At this point, you are probably wondering if replacing Ivanti with Fortinet, Cisco or \[big vendor here\] is worth it. We've said this before and we will say it again - [Proxmox](https://www.proxmox.com/en/), [PFSense](https://www.pfsense.org/) and be merry.

## 5. Public Attribution as a Political Tool: Strategic Signaling in Cyberspace

In 2025, public cyber attribution increasingly shifted from a defensive transparency mechanism to a **deliberate geopolitical instrument**. Attribution is no longer just about explaining incidents; it is about **shaping narratives, signaling resolve, and justifying policy decisions**.

We observed **almost a dozen of public attribution campaigns led by China in 2025**, many of them unusually fast, coordinated, and highly visible. These disclosures often emphasized messaging over exhaustive technical detail, suggesting that **narrative control and political impact outweighed forensic completeness**.

Several characteristics defined this trend:

- **Early, narrative-first disclosures** aimed at preempting external reporting and framing incidents on favorable terms.
- **Bundled or repeated attributions** across sectors or regions, reinforcing perceptions of persistent foreign threat activity.
- **Tight coupling with diplomatic, legal, or regulatory actions**, including sanctions, arrests, or new cybersecurity measures.
- **Reduced IOC transparency**, relying instead on confidence-based or behavioral assessments.

From an intelligence standpoint, this marks a clear evolution: **attribution has become a signaling mechanism**, not merely an analytical conclusion. For defenders and analysts, this means public attribution must now be assessed not only for technical accuracy, but also for **strategic intent**. Heading into 2026, separating genuine threat disclosure from political messaging will be an increasingly important analytical skill.

## 6. The Contractorization of Chinese Cyber-Offense: A Public–Private Attack Ecosystem

Another defining trend of 2025 was the **formalization and scaling of China’s contractor-based cyber-offensive model**, closely mirroring — and in some areas expanding upon — long-standing Western government–contractor arrangements.

Rather than relying solely on military or intelligence units, China has increasingly **outsourced offensive cyber operations to a dense network of nominally private companies**, creating a **nationwide, public–private attack ecosystem**. Firms such as **i-Soon (安洵信息)**, **Integrity Technology Group**, **Shanghai Heiying Information Technology Company**, and **KnownSec**, among others, operate at the intersection of commercial cybersecurity services, vulnerability research, and state-directed offensive tasking.

Several characteristics define this model:

- **Plausible deniability at scale:** Contractor structures allow the state to distance itself from specific operations while maintaining strategic control over targeting priorities.
- **Specialization and efficiency:** Different firms focus on exploit development, initial access brokerage, infrastructure operations, or post-compromise tooling, enabling rapid, industrialized campaigns.
- **Talent absorption and recycling:** Contractors serve as both feeders and safe harbors for skilled operators, blurring lines between academia, private security research, and offensive operations.
- **Persistent access generation:** Rather than one-off intrusions, these entities focus on building reusable access, exploit stockpiles, and long-lived infrastructure.

What differentiates this ecosystem from earlier models is its **scale, coordination, and normalization**. These companies are not fringe actors; many openly advertise training, red-teaming, and security research services while simultaneously supporting state-aligned intrusion campaigns. The result is an **attack surface backed by market incentives**, where offensive capability development is continuous, competitive, and partially self-funding.

From a defender’s perspective, this evolution complicates attribution, sanctions, and deterrence. It also signals a strategic shift: **cyber-offense is no longer treated as a purely governmental function, but as an ecosystem capability**, distributed across semi-commercial entities aligned with national objectives.

Heading into 2026, this contractorization trend suggests China is optimizing for **resilience, scalability, and long-term access**, making cyber operations harder to disrupt through traditional diplomatic or law-enforcement means alone.

## 7. Talent Shortages and Insider-Targeting Threats: A Compounding Crisis

The [cybersecurity workforce gap](https://www.infosecurity-magazine.com/news/cybersecurity-workforce-gap-budget/) has widened to **4.8 million unfilled roles worldwide**, a **19% increase from 2024**. Budget constraints now account for **33–39%** of hiring shortages, coinciding with heightened demand for AI, cloud, and automation expertise.

*Talent Shortages and Insider-Targeting Threats*

The consequences are significant:

- **88% of organizations** report increased incident risk due to limited staffing.
- **Burnout levels continue to rise** among existing teams.
- Critical functions such as threat hunting and continuous monitoring are increasingly automated or deprioritized. This may not be necessarily bad, but the magic lies in finding the right balance between machine/automation and human oversight.

This shortage intersects with a growing threat vector: **APT groups exploiting hiring pipelines**. North Korea-linked units (e.g., Contagious Interview, WageMole) have weaponized remote work norms through:

- Deepfake-enabled job interviews
- Fake recruiting platforms
- [Malware-tainted coding "tests"](https://cybernews.com/security/north-korean-hackers-target-jobseekers-with-fake-coding-tests/) delivering **BeaverTail** infostealers and **OtterCookie** backdoors

These operations enable credential and cryptocurrency theft and **insider-style access without the need to compromise external perimeters**.

The so-called **"remote IT workers from North Korea"**, tracked by Microsoft Threat Intelligence as Jasper Sleet, originally overlapped with Lazarus but has since evolved into a somehow separate and sophisticated threat. The group is deploying what appears to be hundreds if not **thousands** of skilled operatives primarily from North Korea, China, and Russia to infiltrate global organizations through fraudulent remote employment schemes. These workers generate substantial revenue for the DPRK regime - violating international sanctions - while stealing sensitive intellectual property, source code, and trade secrets, and in some cases extorting employers. Leveraging AI tools (of course) to enhance stolen identities, polish resumes, manipulate images for professional profiles, and experiment with voice-changing software, they bypass verification by using facilitators, VPNs (see SilentPush's research on [AstrillVPN](https://www.silentpush.com/blog/north-korean-apt-astrill-vpn)), proxy services, laptop farms, and unapproved remote management tools like TeamViewer and AnyDesk to conceal their locations. Targeting technology, manufacturing, and other sectors worldwide, often via staffing companies or freelance platforms, these operatives have successfully embedded in hundreds of companies, including Fortune 500 firms.

Two articles released in December caught our eye and we would like to share them with you as they dive deep into North Korea's modus operandi:

- [Smile, You're on Camera: A Live Stream from Inside Lazarus Group's IT Workers Scheme](https://any.run/cybersecurity-blog/lazarus-group-it-workers-investigation/) from Any.Run
- [North Korean Hackers Pose as Remote IT Workers to Infiltrate Global Companies](https://deepstrike.io/blog/north-korea-fake-remote-it-workers) from DeepStrike.

Organizations can defend against this multifaceted insider threat by implementing rigorous pre-employment vetting - such as verifying digital footprints, requiring video interviews, and scrutinizing resumes - while monitoring for red flags like **impossible travel, anomalous hours, or unsanctioned RMM software**, and responding with coordinated insider risk protocols. Beyond these measures, effective mitigation now demands **advanced identity verification**, enriched candidate screening, accelerated internal upskilling, and strategic automation - not just to improve efficiency, but to prevent systemic risk from workforce instability posed by fraudulent remote workers.

## Conclusion

The **cyber security landscape of 2025 is defined by agile convergence**: wide scale AI adoption, open-source fragility, geopolitical entanglement and strained defensive capacity. Unfortunately, it is obvious that threat actors are evolving faster than defenders. Many organizations struggle to adapt, implement automation, supply chain validation, and mitigate zero-day exploitation. Meanwhile, attackers achieve scale and persistence faster than ever.

From an intelligence analyst's vantage point, the path forward hinges on three main imperatives:

1. **Machine-speed defense capabilities** to counter machine-speed attacks
2. **Structural reforms in software supply chains** to restore trust
3. **Human capital resilience** through education, automation, and robust identity verification

As the line between criminal enterprise and nation-state operation continues to blur, cybersecurity is no longer a technical discipline alone - it is a strategic function fundamental to economic stability and national security.

The [2025 National Security Strategy (NSS) of the United States, released by the Trump administration on December 4, 2025](https://www.whitehouse.gov/wp-content/uploads/2025/12/2025-National-Security-Strategy.pdf), talks a bit about cyber, although less than previous versions because a more detailed National Cybersecurity Strategy is expected in early 2026. Nevertheless, its US-focus is obvious when it emphasizes **robust partnerships with regional governments and the private sector** to harden critical cyber communications networks, **fully leveraging American innovation in encryption and security technologies**. In practice, this translates to a regionally focused, partnership-driven approach that prioritizes the Western Hemisphere.

Effective cybersecurity demands powerful collaborations across companies, industries, and security providers, uniting diverse human expertise in threat intelligence, policy, and innovation with shared AI-driven platforms for data analysis, detection, and response. This inter-organizational synergy creates collective defensive strength that no single entity could achieve alone. We need this to survive what's coming.
