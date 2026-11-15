# 🤖 CertiK Finds Critical Vulnerabilities in Google's EdgeTPU AI Chip

- **Source URL:** https://www.certik.com/blog/certik-identifies-google-edgetpu-vulnerabilities
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1936 (id 1936)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
CertiK recently identified two security vulnerabilities in Google's EdgeTPU: CVE-2026-0150 and CVE-2026-0153. Both flaws have been acknowledged by Google and included in the June 2026 Security Bulletin, with severity ratings of High and Critical, respectively.

The research is specific to EdgeTPU, but it points to something bigger happening across the AI industry: as AI shifts from generating content to executing tasks, protecting a model is no longer enough. Enterprises need to secure the entire system that model runs on.

## What the EdgeTPU Vulnerabilities Reveal

The two vulnerabilities have different technical root causes, but they expose the same underlying weakness. Attackers may be able to exploit the interaction interface between Android and EdgeTPU to bypass existing security isolation mechanisms, execute unauthorized operations on the privileged chip responsible for AI inference, or access the data stored within it.

This doesn't mean every AI-powered device is at risk. But it does mean that as AI takes on more sensitive functions, like identity authentication, facial recognition, and on-device inference, the components long treated as trusted foundations need independent security validation too.

There's a broader lesson here for enterprises. Many organizations still evaluate applications, APIs, infrastructure, and hardware as separate categories. Attackers don't think that way. They look for the interfaces and trust relationships connecting these components and chain them together into a single attack path. The biggest risks often live in exactly those crossing points, not within any one system alone.

## AI Agents Are Expanding the Attack Surface

Not long ago, large language models (LLMs) were mostly used to generate text and answer questions. That's changing fast. AI agents now connect to databases, call APIs, interact with third-party tools, and take part in real business processes like payments, identity verification, and digital asset management.

According to McKinsey's The State of AI in 2025 report, 88% of organizations have already deployed AI in at least one business function, and more than 60% are exploring AI agents. Separately, a Google Cloud survey found that 83% of enterprises believe their current infrastructure needs significant upgrades to support AI agents at scale.

As AI takes on more responsibility inside core business operations, the definition of "AI security" has to expand with it. It's now about whether the whole system, across every component, privilege boundary, and execution environment, can withstand an attack.

## A Broader Shift in How Enterprises Approach AI Security

AI security has traditionally centered on the model itself, focusing on risks like prompt injection, jailbreaks, and training data poisoning. As AI becomes woven into real business environments, that scope is no longer wide enough. Security teams now need to look at how AI agents interact with external systems, what permissions they have to invoke tools, what sensitive information they can access, and what risks third-party components introduce into the supply chain.

Some AI agent platforms have already started running automated security assessments before deploying new Skills. Pieverse and FinChip.ai, for example, have both integrated CertiK Skill Scanner to catch potentially malicious behavior and vulnerabilities before an agent ever executes a task.

The EdgeTPU research fits into this same evolution. CertiK's approach to AI security has expanded well beyond applications and agents to include AI infrastructure and the underlying system components that support it. For security researchers, that means evaluation can no longer stop at the software layer. Understanding how each layer of the stack influences the others is now part of the job.

## Security Needs to Span the Entire AI Lifecycle

AI is reshaping how enterprises build software, and it's reshaping how they secure it too. More organizations are moving security earlier into the development lifecycle, aiming to catch risks during development and testing rather than after deployment. At the same time, AI itself is being put to work on vulnerability discovery, code analysis, and formal verification, helping teams validate security faster and more thoroughly.

CertiK has been building in this direction for years. By integrating AI into its proprietary CertiK Prover engine, CertiK has improved the speed and depth of formal verification, work that's been recognized at leading systems conferences including OSDI 2023 and ASPLOS 2026, where it received a Best Paper Honorable Mention.

The EdgeTPU vulnerabilities are one case study, but they point to where the industry is headed. The question enterprises need to answer is no longer whether a single model is secure. It's whether the entire AI system, from development through deployment to runtime, can be trusted. As AI becomes core digital infrastructure, AI security is evolving right along with it, from protecting models to protecting whole systems.

## FAQs

**What vulnerabilities did CertiK discover in Google's EdgeTPU?**

A CertiK researcher identified CVE-2026-0150 and CVE-2026-0153, rated High and Critical severity, respectively. Both were acknowledged by Google and included in its June 2026 Security Bulletin.

**What risk do these vulnerabilities create?**

Attackers may be able to exploit the interaction interface between Android and EdgeTPU to bypass security isolation, run unauthorized operations on the AI inference chip, or access data stored on it.

**Does this mean AI devices are broadly at risk?**

Not necessarily for everyday users. The bigger implication is for enterprises: as AI takes on sensitive functions like authentication and on-device inference, the hardware and infrastructure supporting it need the same level of security scrutiny as software.

**Why is AI security expanding beyond the model?**

AI agents increasingly connect to databases, call APIs, and participate in workflows like payments and identity verification. That expands the attack surface well past the model itself, requiring security across the entire technology stack.

**How is CertiK addressing this shift?**

CertiK conducts security research across AI applications, agents, and infrastructure, and applies AI to its own formal verification engine, CertiK Prover, to improve the speed and depth of vulnerability detection.
