# 🚨 Nx Console Supply Chain Attack Led to GitHub Breach

- **Source URL:** https://rekt.news/poisoned-pipeline
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1729 (id 1729)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Poisoned Pipeline

*Eighteen minutes. That's how long it took to breach GitHub.*

**Not eighteen minutes to plan it. Not eighteen minutes to find a flaw in GitHub's code, defeat their authentication, or outwit their security team.**

[Eighteen minutes was the window between a malicious extension going live on the VS Code Marketplace and the community pulling it,](https://www.bleepingcomputer.com/news/security/github-links-repo-breach-to-tanstack-npm-supply-chain-attack/) time enough for auto-update to do what it was designed to do, on a tool [2.2 million developers had installed](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised) and stopped thinking about.

One developer at GitHub had Nx Console running. Nothing unusual about that. [Verified publisher with 2.2 million installs](https://www.xda-developers.com/poisoned-vs-code-extension-github-breach-microsoft-owns-every-link/). The kind of tool you add once and forget.

What they didn't know, what they had no way to know, is that [on May 11, TeamPCP had already moved through the supply chain upstream](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem), harvested the right credentials, and was waiting for exactly this moment.

[The Stack Nobody Checked](https://rekt.news/stack-nobody-checked) named this surface on April 30. [Paranoid By Default](https://rekt.news/paranoid-by-default) documented the threat model on May 18, the same morning the extension went live.

**Neither piece changed what happened next.**

*If the ecosystem had the warning and the attacker had the methodology, what exactly did the warning change?*

*Credit:[BleepingComputer](https://www.bleepingcomputer.com/news/security/github-links-repo-breach-to-tanstack-npm-supply-chain-attack/), [StepSecurity](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised), [XDA](https://www.xda-developers.com/poisoned-vs-code-extension-github-breach-microsoft-owns-every-link/), [tanstack](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem), [Security Boulevard](https://securityboulevard.com/2026/05/mini-shai-hulud-frequently-asked-questions-about-the-teampcp-npm-and-pypi-supply-chain-campaign/), [Nx](https://nx.dev/blog/nx-console-v18-95-0-postmortem), [Aikido](https://www.aikido.dev/blog/vs-code-extension-github-breach), [Jeff Cross](https://x.com/jeffbcross/status/2057069440374894797), [The Hacker News](https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html), [VS Code](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security), [Help Net Security](https://www.helpnetsecurity.com/2026/05/20/github-breached-teampcp/), [snyk](https://snyk.io/blog/mini-shai-hulud-antv-npm-supply-chain-attack/), [kaspersky](https://www.kaspersky.com/blog/critical-supply-chain-attack-trivy-litellm-checkmarx-teampcp/55510/), [Phoenix Security](https://phoenix.security/teampcp-github-breach-durabletask-pypi-supply-chain-wave-four-2026/), [The Register](https://www.theregister.com/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319), [DataDog](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/#a-note-on-reproducibility), [OX Security](https://www.ox.security/blog/new-actors-deploy-shai-hulud-clones-teampcp-copycats-are-here/), [Socket](https://socket.dev/blog/teampcp-supply-chain-attack-contest), [Dark Web Informer](https://x.com/DarkWebInformer/status/2057109380282110350), [Security Week](https://www.securityweek.com/over-5500-github-repositories-infected-in-megalodon-supply-chain-attack/), [OpenAI](https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/), [Wiz](https://www.wiz.io/blog/supply-chain-risk-in-vscode-extension-marketplaces), [Krebs on Security](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/), [Tech Times](https://www.techtimes.com/articles/317232/20260526/lawmakers-demand-answers-cisa-scrambles-contain-catastrophic-github-credential-leak.htm), [Cyber Unit](https://cyberunit.com/insights/cisa-private-cisa-github-leak-what-businesses-should-know/)*

**This is not a GitHub story. GitHub is where it got loud.**

It started on May 11, when TeamPCP detonated inside TanStack's npm ecosystem, [84 malicious versions across 42 packages, a self-replicating payload with a CVSS score of 9.6](https://securityboulevard.com/2026/05/mini-shai-hulud-frequently-asked-questions-about-the-teampcp-npm-and-pypi-supply-chain-campaign/) and a dead-man's switch built in.

**Among the developers whose machines were swept in that harvest:** [One engineer at Nx, the company behind Nx Console](https://nx.dev/blog/nx-console-v18-95-0-postmortem). Their GitHub credentials leaked through the CLI. Quietly, completely, with no alert, no notification, and no moment where anything felt wrong.

Those credentials carried two things that mattered. Push access to the official nrwl/nx repository. And [the VS Code Marketplace publishing token](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised), the key that lets you ship updates to every machine running your extension, automatically, without review.

TeamPCP waited seven days.

[On May 18 at 3:18 UTC, an orphan commit appeared on the official Nx repository](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised). Not on a branch. Not anywhere a routine audit would surface it. A dangling reference, invisible in normal history views, containing a [498 KB obfuscated payload](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised) hidden inside a file with a name that looked like it belonged there.

[Then, at 12:36 UTC](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised), Nx Console 18.95.0 went live on the VS Code Marketplace. The [Nx maintainer received the upload notification email six minutes later](https://www.aikido.dev/blog/vs-code-extension-github-breach). The [community caught it at 12:47 and pulled it](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised).

[11 minutes of exposure](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised) on the marketplace. [Thirty-six more on OpenVSX](https://www.bleepingcomputer.com/news/security/github-links-repo-breach-to-tanstack-npm-supply-chain-attack/) before that copy came down too.

Inside that window, the extension executed the moment any developer opened any workspace. [A command, disguised as a routine MCP setup task](https://thehackernews.com/2026/05/github-internal-repositories-breached.html), the kind that wouldn't raise an eyebrow, reached back to the orphan commit and pulled down the payload.

[**Six credential collectors fired in parallel:**](https://dailysecurityreview.com/cyber-security/nx-console-vs-code-extension-poisoned-to-steal-1password-aws-keys/) 1Password vaults, AWS access keys, npm tokens, GitHub tokens, Kubernetes secrets, and Anthropic Claude Code configurations.

*On macOS, it went further, [dropping a persistent Python backdoor as a LaunchAgent](https://corgea.com/research/nx-console-vscode-extension-credential-stealer-may-2026) that checked in hourly for new commands via GitHub-based dead drops.*

**A GitHub employee device had the extension running. [28 installs by Microsoft's official count](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w), a figure [Nx's own analytics put closer to 6,000](https://x.com/jeffbcross/status/2057069440374894797).**

**[Here is what makes that number genuinely terrifying](https://nx.dev/blog/nx-console-v18-95-0-postmortem):** Nothing in this chain was broken. The TanStack pipeline was legitimate. The Nx developer's credentials were real. The Nx release infrastructure ran exactly as designed. The extension carried a verified publisher badge.

[The payload arrived with valid cryptographic provenance,](https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html) stolen npm OIDC tokens meant the attacker could have signed downstream packages with fully valid Sigstore attestations, making malicious builds indistinguishable from clean ones.

**The verification systems didn't fail. They were used.**

*If every security signal in the pipeline said clean, and the pipeline was already compromised, what exactly were those signals measuring?*

### The Weapon

*Auto-update didn't fail here.*

**It worked perfectly. That's the problem.**

**The design logic is sound and always has been:** Developers don't manually update their tools, so ship updates automatically and keep the ecosystem current and patched.

Every marketplace runs on this assumption. VS Code, Cursor, the whole stack.

Nobody questioned it because, for a long time, the worst-case scenario was a buggy release - something you'd notice, something you'd roll back.

*The possibility that a publisher's credentials could be stolen upstream, that the update itself could be the payload, wasn't part of the threat model the architecture was built for.*

**When the publisher is compromised, auto-update stops being a maintenance feature.**

It becomes a guaranteed delivery channel, no review gate between publish and execution, no waiting period, no user confirmation, no sandbox.

[The check fires on startup, on any marketplace interaction,](https://www.aikido.dev/blog/vs-code-extension-github-breach) and again on a 12-hour background timer, so the user never sees the trigger and never opts into it.

**[Raphael Silva at Aikido Security put it plainly](https://www.aikido.dev/blog/vs-code-extension-github-breach):** The trade-off stops making sense once you account for hostile publishers. An attacker who controls a release has a direct push channel into every machine running that extension. The moment they publish, the machines pull.

*That's not a vulnerability. It's the feature, inverted.*

[As far back as October 2025, Wiz Research had identified over 100 valid VS Code Marketplace publishing tokens leaked inside extension packages](https://www.wiz.io/blog/supply-chain-risk-in-vscode-extension-marketplaces), each one a master key waiting to be picked up.

Nobody scanning those packages for malware would flag a token. It's not malware.

It's a credential. The distinction matters less than it used to.

**[The "verified publisher" badge on Nx Console told users something real](https://byteiota.com/github-breach-vscode-extension-2026/):** Domain ownership confirmed, six months in good standing, no prior incidents.

**What it didn't tell them, [what it was never designed to tell them](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security), is whether the publisher's credentials had been stolen. Whether the update that fired on startup when they opened their project this morning was the same codebase they installed three months ago. Whether the tool doing the building had itself been built by someone else.**

Users never see a changelog. Never approve the update. Have no way to inspect what changed before it executes.

[The malicious version was caught in approximately 11 minutes](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised), by a StepSecurity researcher monitoring the marketplace, not by Microsoft, not by the marketplace infrastructure.

[11 minutes was faster than the detection infrastructure](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised). The official download count was still enough.

*When the community is the last line of defense, and the community moves faster than the platform, what does that say about every extension you installed before anyone was watching?*

### The Record

*This is not a story about prediction. Prediction implies luck.*

[The Stack Nobody Checked](https://rekt.news/stack-nobody-checked), published April 30th. It named the VS Code extension ecosystem specifically, an unaudited attack surface sitting between developer tooling and everything connected to it, operating with no visibility, no logging standard, no governance model that matched the access being granted.

[It named the gap between what organizations were connecting and what they were checking](https://rekt.news/stack-nobody-checked). Eighteen days before the breach, the structural argument was already in print.

[Paranoid By Default](https://rekt.news/paranoid-by-default), published May 18th, [the same morning Nx Console 18.95.0 went live on the marketplace](https://nx.dev/blog/nx-console-v18-95-0-postmortem).

Not the day before. Not the week before. The same day, within hours of each other.

**Neither piece is the story. The story is what sits between them:** 18 days in which the industry had a named surface, a documented risk, and a clear argument for why the architecture of trust in developer tooling had outrun any corresponding architecture of verification, and changed nothing.

**[Jeff Cross, CEO of Nx, said it plainly in the aftermath](https://x.com/jeffbcross/status/2057236396658811020):** "A lot of the assumptions the ecosystem has operated under for years no longer hold."

**That is a careful, measured statement from someone whose pipeline was used to deliver the weapon. What it describes, without naming it, is an ecosystem that built velocity into every layer and auditing into none.**

The warnings predate the breach by more than eighteen days.

[The Stack Nobody Checked](https://rekt.news/stack-nobody-checked) was built on source material that had been circulating for months, researchers naming the surface, documenting the exposure, publishing the risk.

[The April 30 timestamp](https://rekt.news/stack-nobody-checked) is not a credential.

**[It is evidence of a pattern](https://rekt.news/stack-nobody-checked):** By the time a warning reaches print, the attack surface it describes has already been documented, circulated, and ignored.

[TeamPCP exploited an eleven-minute window.](https://nx.dev/blog/nx-console-v18-95-0-postmortem) The industry had been warned for months.

*When the gap between the warning and the action is measured in months, and the gap between the attack and the damage is measured in minutes, which gap is the industry actually trying to close?*

### The Ladder

*GitHub is not where it ends. It is not even where it paused.*

**TeamPCP is not an incident. It is a business.**

Each compromise produces credentials. Each set of credentials funds the next target. Each new target sits higher on the trust chain than the one before - more widely used, more deeply integrated, more catastrophic to lose.

[The GitHub breach is not a peak. It is a rung](https://www.helpnetsecurity.com/2026/05/20/github-breached-teampcp/), and the climbing continued the same day the breach went public.

*The ladder has been climbing [since September 2025](https://snyk.io/blog/mini-shai-hulud-antv-npm-supply-chain-attack/).*

**In March, [when Aqua Security’s Trivy vulnerability scanner was compromised](https://www.kaspersky.com/blog/critical-supply-chain-attack-trivy-litellm-checkmarx-teampcp/55510/), every CI/CD pipeline running Trivy briefly became a credential-harvesting engine for the duration of the compromise.**

[LiteLLM on PyPI the same month pushed a compromised version to tens of thousands of devices](https://www.bleepingcomputer.com/news/security/popular-litellm-pypi-package-compromised-in-teampcp-supply-chain-attack/), effectively turning them into credential-stealing endpoints.

In April, [the Bitwarden CLI NPM package was compromised to steal developer credentials](https://www.bleepingcomputer.com/news/security/bitwarden-cli-npm-package-compromised-to-steal-developer-credentials/) directly from developer machines.

In May, [TanStack followed the same pattern](https://securityboulevard.com/2026/05/mini-shai-hulud-frequently-asked-questions-about-the-teampcp-npm-and-pypi-supply-chain-campaign/), with a supply-chain attack compromising a widely used library to exfiltrate secrets.

**Each time, the same mechanics:** Find a trusted tool, compromise a human inside its pipeline, use their credentials to poison the output, and wait for the downstream machines to pull.

**Mandiant counts [more than 1,000 SaaS environments compromised from TeamPCP credentials across this campaign alone](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/).**

Most of those organizations never touched TanStack. They ran something that ran something that did.

On May 19, TeamPCP detonated inside Alibaba's AntV data visualization ecosystem.

[637 malicious versions across 323 packages, published in a 22-minute automated burst](https://snyk.io/blog/mini-shai-hulud-antv-npm-supply-chain-attack/). The packages collectively represent approximately [16 million weekly downloads](https://snyk.io/blog/mini-shai-hulud-antv-npm-supply-chain-attack/).

*That same day, [three backdoored versions of durabletask - Microsoft's official Azure Python SDK - were pushed to PyPI within a 35-minute window](https://phoenix.security/teampcp-github-breach-durabletask-pypi-supply-chain-wave-four-2026/), silently harvesting AWS, Azure, GCP, and Kubernetes credentials from every environment that pulled them.*

**Three days later, [an attacker with push access to the Laravel-Lang organization rewrote 700+ git tags across four Composer packages](https://phoenix.security/laravel-lang-composer-supply-chain-compromise-rce-backdoor/), injecting an RCE backdoor that fires on every PHP application boot. No CVE assigned. Version pinning offered zero protection.**

[TeamPCP posted their retirement notice](https://www.bleepingcomputer.com/news/security/github-investigates-internal-repositories-breach-claimed-by-teampcp/) on May 19.

The attack log from the same 24 hours tells a different story.

Then the methodology escaped the original actor entirely.

*On May 12, [TeamPCP published the full Shai-Hulud offensive framework to GitHub under an MIT license](https://www.theregister.com/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319), which allows just about any re-use of code.*

[They also included deployment instructions](https://www.theregister.com/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319), a README reading "Open Sourcing The Carnage. Change keys and C2 as needed. Love - TeamPCP," every commit timestamped January 1, 2099 as a taunt at forensic timelines.

GitHub pulled the repo. [The forks were already live](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/#a-note-on-reproducibility).

Within days, [OX Security documented the first confirmed copycat](https://www.ox.security/blog/new-actors-deploy-shai-hulud-clones-teampcp-copycats-are-here/).

[A BreachForums post launched a $1,000 Monero contest](https://socket.dev/blog/teampcp-supply-chain-attack-contest) for anyone who wanted to run their own variant.

**The proof arrived on May 18, [the same morning Nx Console 18.95.0 went live](https://nx.dev/blog/nx-console-v18-95-0-postmortem), when a campaign called Megalodon [pushed 5,718 malicious commits to 5,561 distinct GitHub repositories inside a six-hour window](https://www.stepsecurity.io/blog/megalodon-mass-github-actions-secret-exfiltration-across-5-500-public-repositories).**

**[A campaign running on the same fuel](https://www.stepsecurity.io/blog/megalodon-mass-github-actions-secret-exfiltration-across-5-500-public-repositories):** Infostealer-harvested developer credentials, automated commit injection, GitHub Actions workflows designed to exfiltrate cloud secrets from every subsequent pipeline run.

[Hudson Rock confirmed that more than a third of the affected accounts](https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html) were direct matches to computers already compromised by infostealers.

The credential pipeline TeamPCP spent nine months building had become infrastructure anyone could use.

[Zero CVEs exist across the entire nine-week campaig](https://phoenix.security/megalodon-ci-github-actions-workflow-poisoning-credential-harvesting/)n. Traditional scanners have no record of any of it.

**Every organization that checked their vulnerability feed and called it clean was looking at a dashboard that had nothing to say about any of this.**

*When the attacker's exit strategy is to open-source their weapon on the way out — who exactly inherits the campaign?*

### The Math

*One employee device impacted [3,800 repositories](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/).*

**Sit with that ratio for a moment. Not a sophisticated phishing campaign targeting hundreds of developers across multiple organizations.**

One poisoned extension, auto-updated silently to every developer who opened their editor during the window.

[28 downloads by Microsoft's count](https://x.com/jeffbcross/status/2057069440374894797), a figure [Nx's own analytics put closer to 6,000](https://x.com/jeffbcross/status/2057069440374894797), and the yield was the internal codebase of [the platform that hosts 180 million developers, 4 million organizations, and 90% of the Fortune 100](https://www.bleepingcomputer.com/news/security/github-investigates-internal-repositories-breach-claimed-by-teampcp/).

**[What those 3,800 repositories contained is not a list of abstractions](https://thehackernews.com/2026/05/github-investigating-teampcp-claimed.html):** GitHub Actions internals, Copilot source code, CodeQL tools, Codespaces infrastructure, Dependabot, a repository explicitly labelled Red Team, security hardening research, and Enterprise Server release infrastructure.

*The Rails controllers governing how every pull request and every organization on the platform actually functions.*

[The joint asking price](https://x.com/DarkWebInformer/status/2057109380282110350): $95,000.

**[TeamPCP's own forum post read like someone wrapping up a career](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/):** Not a ransom, one buyer, data shredded on sale, "our retirement is soon."

The [campaign kept running for days](https://phoenix.security/teampcp-github-breach-durabletask-pypi-supply-chain-wave-four-2026/).

*GitHub is one victim inside a much larger campaign.*

**AntV adds [16 million weekly downloads to the exposure surface](https://snyk.io/blog/mini-shai-hulud-antv-npm-supply-chain-attack/).**

[Durabletask adds 417,000 monthly downloads](https://phoenix.security/teampcp-github-breach-durabletask-pypi-supply-chain-wave-four-2026/) and the credential surface of every Azure workflow that pulled it.

[Megalodon adds 5,561 repositories backdoored in six hours](https://www.securityweek.com/over-5500-github-repositories-infected-in-megalodon-supply-chain-attack/), running on infostealer-harvested developer credentials.

[OpenAI's compromised repositories exposed code-signing certificates for its macOS products, mandatory update deadline June 12](https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/), or your ChatGPT stops launching.

[Grafana Labs rotated nearly every token after TanStack,](https://grafana.com/blog/grafana-labs-security-update-latest-on-tanstack-npm-supply-chain-ransomware-incident/) missed one, and had their codebase exfiltrated anyway.

**One token. One gap in a rotation process executed under pressure. That's the margin the operating environment now allows.**

GitHub sits at the structural center of how software gets built.

Not metaphorically, literally.

The source code behind the tools those 180 million developers use to write, review, deploy, and secure their code [was among what was just exfiltrated](https://www.bleepingcomputer.com/news/security/github-links-repo-breach-to-tanstack-npm-supply-chain-attack/).

*GitHub Actions, Copilot, CodeQL, and the security tooling used to find vulnerabilities in other people's code.*

**All of it now in the hands of a group that has already demonstrated exactly what it does with trusted infrastructure.**

Run the math in the other direction. TeamPCP needed one compromised developer, one publishing token, [eleven minutes of exposure](https://nx.dev/blog/nx-console-v18-95-0-postmortem), and [seven days of patience](https://nx.dev/blog/nx-console-v18-95-0-postmortem) after TanStack.

**Against that:** [Eight months of campaign escalation](https://snyk.io/blog/mini-shai-hulud-antv-npm-supply-chain-attack/), [2.2 million extension installs](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised), and the entire weight of GitHub's internal security posture.

[6k installs](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w) was the surface area. [3,800 repositories was the consequence](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/).

**The campaign that produced both is still running.**

*At what point does the industry stop doing the math on individual breaches and start doing it on the ecosystem?*

*Nobody is taking this seriously enough because taking it seriously would require admitting how much of the foundation is already exposed.*

**Pinning extension versions, scoping CI/CD credentials, auditing dependency graphs, restricting publishing tokens, none of these are unsolved problems.**

They were all possible before May 11, before the TanStack compromise handed TeamPCP the credentials that started this cascade.

[They were all possible months before April 30](https://rekt.news/stack-nobody-checked), when [researchers had already named the surface](https://www.wiz.io/blog/supply-chain-risk-in-vscode-extension-marketplaces).

The reason they weren't in place isn't ignorance of the risk. It's that velocity is measured, rewarded, and reported, and the exposure it creates is invisible until it isn't.

**Every organization that connected another tool, shipped another integration, and wired another pipeline without checking what it touched first made the same calculation:** The breach is hypothetical, the productivity is real.

**Then consider what happened the same week GitHub disclosed the breach.**

[A contractor at Nightwing, a Dulles, Virginia government services firm holding federal contracts for national security and cybersecurity support,](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/) had been using a public GitHub repository as a file synchronization tool since November 2025.

The repository was called "[Private-CISA.](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)"

**[It contained 844 MB of plaintext credentials](https://www.techtimes.com/articles/317232/20260526/lawmakers-demand-answers-cisa-scrambles-contain-catastrophic-github-credential-leak.htm):** AWS GovCloud admin keys, a CSV file of usernames and passwords for dozens of internal CISA systems, SSH keys, GitHub Actions workflows, Kubernetes configuration files, and a file named "importantAWStokens."

[The contractor had deliberately disabled GitHub's built-in secret-scanning protection](https://www.techtimes.com/articles/317232/20260526/lawmakers-demand-answers-cisa-scrambles-contain-catastrophic-github-credential-leak.htm), the feature that would have flagged the exposure automatically.

[GitGuardian's automated scanner found it](https://blog.gitguardian.com/how-we-got-a-cisa-github-leak-taken-down-in-26-hours/) on May 14.

 [The repository came down within 26 hours](https://cyberunit.com/insights/cisa-private-cisa-github-leak-what-businesses-should-know/) of public escalation.

The exposed AWS keys [remained valid for another 48 hours after it disappeared.](https://cyberunit.com/insights/cisa-private-cisa-github-leak-what-businesses-should-know/)

This is not a TeamPCP story. Nobody attacked CISA.

*A contractor used a public repository as a file sync tool, disabled the safeguard that would have caught it, and left the administrative keys to US federal cyber infrastructure on the open internet for six months, while the agency they worked for was publishing the remediation guidance the rest of the ecosystem was supposed to follow.*

**The pipeline wasn't poisoned in eighteen minutes. It was poisoned over years, one trusted connection at a time, by an industry that optimized for how fast it could build and never once asked what it was building on.**

TeamPCP understood that.

[The contractor at Nightwing demonstrated it differently](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/), but the gap is the same.

**The credential was trusted, the surface was unaudited, and nobody looked until someone outside the organization did. That someone was a security researcher with an automated scanner - not a regulator, not an auditor, not the agency itself.**

*When the agency that writes the guidance can't follow it, what exactly is the guidance certifying?*

REKT serves as a public platform for anonymous authors, we take no responsibility for the views or content hosted on REKT.

**donate (ETH / ERC20): [0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C](https://etherscan.io/address/0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C)**

disclaimer:

REKT is not responsible or liable in any manner for any Content posted on our Website or in connection with our Services, whether posted or caused by ANON Author of our Website, or by REKT. Although we provide rules for Anon Author conduct and postings, we do not control and are not responsible for what Anon Author post, transmit or share on our Website or Services, and are not responsible for any offensive, inappropriate, obscene, unlawful or otherwise objectionable content you may encounter on our Website or Services. REKT is not responsible for the conduct, whether online or offline, of any user of our Website or Services.
