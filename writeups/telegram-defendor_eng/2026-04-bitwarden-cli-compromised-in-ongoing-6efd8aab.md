# 🔑 Bitwarden CLI Compromised in Checkmarx Supply Chain Attack

- **Source URL:** https://thehackernews.com/2026/04/bitwarden-cli-compromised-in-ongoing.html
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1512 (id 1512)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
[Bitwarden CLI](https://www.npmjs.com/package/@bitwarden/cli?activeTab=versions), the command-line interface for the password manager Bitwarden, has reportedly been compromised as part of a newly discovered and ongoing [Checkmarx supply chain campaign](https://thehackernews.com/2026/04/malicious-kics-docker-images-and-vs.html), according to findings from JFrog and Socket.

"The affected package version appears to be [@bitwarden/cli@2026.4.0](https://socket.dev/npm/package/@bitwarden/cli/overview/2026.4.0), and the malicious code was published in 'bw1.js,' a file included in the package contents," the application security company [said](https://socket.dev/blog/bitwarden-cli-compromised).

"The attack appears to have leveraged a compromised GitHub Action in Bitwarden's CI/CD pipeline, consistent with the pattern seen across other affected repositories in this campaign."

In a post on X, JFrog [said](https://x.com/JFrogSecurity/status/2047268576071991766) the rogue version of the package "steals GitHub/npm tokens, .ssh, .env, shell history, GitHub Actions and cloud secrets, then exfiltrates the data to private domains and as GitHub commits."

Specifically, the malicious code is [executed](https://research.jfrog.com/post/bitwarden-cli-hijack/) by means of a preinstall hook, resulting in the theft of local, CI, GitHub, and cloud secrets. The data is exfiltrated to the domain "audit.checkmarx\[.\]cx" and to a GitHub repository as a fallback if the primary method fails.

The entire series of actions is listed below -

- It launches a credential stealer that targets developer secrets, GitHub Actions environments, and artificial intelligence (AI) coding tool configurations, including Claude, Kiro, Cursor, Codex CLI, and Aider.
- The stolen data is encrypted with AES-256-GCM and exfiltrated to audit.checkmarx\[.\]cx, a domain impersonating Checkmarx.
- If GitHub tokens are found, the malware weaponizes them to inject malicious Actions workflows into repositories and extract CI/CD secrets.

"A single developer with @bitwarden/cli@2026.4.0 installed can become the entry point for a broader supply chain compromise, with the attacker gaining persistent workflow injection access to every CI/CD pipeline the developer’s token can reach," StepSecurity [said](https://www.stepsecurity.io/blog/bitwarden-cli-hijacked-on-npm-bun-staged-credential-stealer-targets-developers-github-actions-and-ai-tools).

While the malicious version is no longer available for download from npm, Socket said the compromise follows the same GitHub Actions supply chain vector identified in the Checkmarx campaign.

As part of the effort, threat actors have been [found](https://thehackernews.com/2026/04/malicious-kics-docker-images-and-vs.html) abusing stolen GitHub tokens to inject a new GitHub Actions workflow that captures secrets available to the workflow run, and uses harvested npm credentials to push malicious versions of the package to read the malware to downstream users.

According to security researcher Adnan Khan, the threat actor is said to have used a [malicious workflow](https://github.com/bitwarden/clients/blob/03df1ecd86132e06643d24c856d8976d1b497945/.github/workflows/publish-cli.yml) to publish the malicious bitwarden CLI. "I believe this is the first time a package using NPM trusted publishing has been compromised," Khan [added](https://x.com/adnanthekhan/status/2047276201429897679).

| Bitwarden CLI Attack Chain \| Source: OX Security | 

It's suspected that the threat actor known as TeamPCP is behind the latest attack aimed at Checkmarx. As of writing, TeamPCP's [X account has been suspended](https://x.com/pcpcats/) for violating the platform's rules.

OX Security, in a breakdown of the attack, [said](https://www.ox.security/blog/shai-hulud-bitwarden-cli-supply-chain-attack/) it identified the string "Shai-Hulud: The Third Coming" in the package, suggesting this could likely be the next phase of the [supply chain attack campaign](https://thehackernews.com/2025/11/second-sha1-hulud-wave-affects-25000.html) that came to light last year.

| Reference to the "Shai-Hulud: The Third Coming" | 

"The latest Shai Hulud incident is just the latest in a long chain of threats targeting developers around the world. User data is being publicly exfiltrated to GitHub, often going undetected because security tools typically don't flag data being sent there," Moshe Siman Tov Bustan, Security Research Team Lead at OX Security, said.

"This makes the risk significantly more dangerous: anyone searching GitHub can potentially find and access those credentials. At that point, sensitive data is no longer in the hands of a single threat actor – it’s exposed to anyone."

Like in the case of the Checkmarx incident, the stolen data is exfiltrated to public repositories created under victim accounts using a Dune-themed naming scheme in the same format "\<word>-\<word>-\<3 digits>. "But in an interesting shift, the malware is also designed to quit execution on systems if their locale corresponds to Russia.

"The shared tooling strongly suggests a connection to the same malware ecosystem, but the operational signatures differ in ways that complicate attribution," Socket said. "This suggests either a different operator using shared infrastructure, a splinter group with stronger ideological motivations, or an evolution in the campaign's public posture."

When reached for comment, Bitwarden [confirmed](https://community.bitwarden.com/t/bitwarden-statement-on-checkmarx-supply-chain-incident/96127) the incident and said it stemmed from the compromise of its npm distribution mechanism following the Checkmarx supply chain attack, but emphasized that no end-user data was accessed as part of the attack. The entire statement shared with The Hacker News is reproduced verbatim below -

*The Bitwarden security team identified and contained a malicious package that was briefly distributed through the npm delivery path for @bitwarden/cli@2026.4.0 between 5:57 PM and 7:30 PM (ET) on April 22, 2026, in connection with a broader Checkmarx supply chain incident.*

*The investigation found no evidence that end user vault data was accessed or at risk, or that production data or production systems were compromised. Once the issue was detected, compromised access was revoked, the malicious npm release was deprecated, and remediation steps were initiated immediately.*

*The issue affected the npm distribution mechanism for the CLI during that limited window, not the integrity of the legitimate Bitwarden CLI codebase or stored vault data.*

*Users who did not download the package from npm during that window were not affected. Bitwarden has completed a review of internal environments, release paths, and related systems, and no additional impacted products or environments have been identified at this time. A CVE for Bitwarden CLI version 2026.4.0 is being issued in connection with this incident.*

Per a [breakdown of the attack](https://www.endorlabs.com/learn/shai-hulud-the-third-coming----inside-the-bitwarden-cli-2026-4-0-supply-chain-attack) published by Endor Labs, Bitwarden's GitHub repository uses "checkmarx/ast-github-action," which was one of the artifacts that was compromised in the Checkmarx supply chain incident. The application security vendor described the malicious Bitwarden CLI as one of the "more capable npm supply chain payloads" published to date.

"It combines a multi-cloud credential harvester targeting six distinct secret surfaces, a self-propagating npm worm that re-infects all packages a victim token can publish, a GitHub commit dead-drop C2 channel with RSA-signed command delivery, authenticated-encryption exfiltration that survives repository seizure, shell RC persistence, and a novel module that specifically targets authenticated AI coding assistants," Endor Labs researcher Kiran Raj said.

Additional analyses of the attack are listed below -

"Every payload, from the [CanisterSprawl](https://thehackernews.com/2026/04/self-propagating-supply-chain-worm.html) worm to the trojanized KICS scanner to the [xinference stealer](https://thehackernews.com/2026/04/self-propagating-supply-chain-worm.html), was engineered to do one thing: extract credentials from the environments where developers and pipelines operate," GitGuardian [said](https://blog.gitguardian.com/three-supply-chain-campaigns-hit-npm-pypi-and-docker-hub-in-48-hours/). "The question every affected team should be asking right now isn't just 'did this package run in my environment?' It's: what secrets were accessible if it did, and have they been rotated?"

### Update

For users who installed the trojanized package during the affected window, Bitwarden has released [@bitwarden/cli version 2026.4.1](https://www.npmjs.com/package/@bitwarden/cli?activeTab=versions), which is a re-release of 2026.3.0. It's estimated that a total of 334 downloads of version 2026.4.0 took place. In addition, the company is urging affected users to [perform the following steps](https://community.bitwarden.com/t/bitwarden-statement-on-checkmarx-supply-chain-incident/96127) prior to installing the safe version -

- Uninstall Bitwarden CLI 2026.4.0 via npm.
- Clear the npm cache.
- Temporarily disable npm install scripts during cleanup as a precaution.
- Review for indicators of compromise.
- Rotate any secrets that may have been exposed on the affected system or stored in environment variables.
- Review GitHub activity, CI workflows, and related credentials for unauthorized access or changes.
- Install Bitwarden CLI 2026.4.1 via npm.

The company said it's "in the process of completing a full review and will implement mitigation to prevent such attacks in the future."

*(The story was updated after publication to include additional insights.)*

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
