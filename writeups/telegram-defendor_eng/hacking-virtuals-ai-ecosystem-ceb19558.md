# 🤖 Vulnerability in the Virtuals AI Ecosystem worth $4.6 billion

- **Source URL:** https://shlomie.uk/posts/Hacking-Virtuals-AI-Ecosystem
- **Fetched from:** https://web.archive.org/web/20261106014439/https://shlomie.uk/posts/Hacking-Virtuals-AI-Ecosystem
- **Fetched:** 2026-11-27
- **Channel:** @defendor_eng
- **Telegram message:**  (id 211)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# PAT-tastrophe: How We Hacked Virtuals' $4.6B Agentic AI & Cryptocurrency Ecosystem [](https://web.archive.org#frontmatter-title)

A single AI agent in the cryptocurrency space has a market cap of $641M at the time of writing. It has [386,000 Twitter followers](https://web.archive.org/web/20261106014439/https://x.com/aixbt_agent). When it tweets market predictions, people listen - because it's right [83% of the time](https://web.archive.org/web/20261106014439/https://cryptobriefing.com/ai-crypto-predictions-impressive-gains).

This isn't science fiction. This is AIXBT, one of 12,000+ AI agents running on **Virtuals**, a $4.6 billion platform where artificial intelligence meets cryptocurrency. These agents don't just analyze markets - they own wallets, make trades, and even become [millionaires](https://web.archive.org/web/20261106014439/https://www.wired.com/story/truth-terminal-goatse-crypto-millionaire/). .

With that kind of financial power, security is crucial.

This piqued my interest and with a shared interest in AI security, I teamed up with [Dane Sherrets](https://web.archive.org/web/20261106014439/https://x.com/DaneSherrets) to find a way in through something much simpler, resulting in a **$10,000** bounty.

Let's start at the beginning...

## Background on Virtuals [](https://web.archive.org#background-on-virtuals)

If you aren’t already familiar with the term “AI Agents” you can expect to hear it a lot in the coming years. Remember the sci-fi dream of AI assistants managing your digital life? That future is already here. AI agents are autonomous programs that can handle complex tasks - from posting on social media to writing code. But here's where it gets wild: these agents can now manage cryptocurrency wallets just like humans.

This is exactly what Virtuals makes possible. Built on Base (a Layer 2 network on top of Ethereum), it lets anyone deploy and monetize AI agents.

TIP

💡 Think of Virtuals as the App Store for AI agents, except these apps can own cryptocurrency and make autonomous decisions.

The tech behind this is fascinating. Virtuals offers a framework leveraging components such as agent behavior processing, long-term memory storage, and real-time value stream processors. At its core, the platform utilizes a modular architecture that integrates agent behaviors (perceive, act, plan, learn) with GPU-enabled SAR (Stateful AI Runner) modules and a persistent long-term memory system.

These agents can be updated through "contributions" - new data or model improvements that get stored both in Amazon S3 and IPFS.

INFO

Pay close attention to the computing hosts and storage sections as we will be coming back to them shortly

## The Discovery [](https://web.archive.org#the-discovery)

Our research into Virtuals began as a systematic exploration of the emerging Agentic AI space. Rather than just skimming developer docs, we conducted a thorough technical review - examining the whitepaper, infrastructure documentation, and implementation details. During our analysis of agent creation workflows, we encountered an unexpected API response as part of a much larger response relating to a specific GitHub repository:

```
{
  "status": "success",
  "data": {
    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  }
}
```
Just another API response, right?

Except that token was a valid GitHub Personal Access Token (PAT).

### Github PATs [](https://web.archive.org#github-pats)

PATs are essentially scoped access keys to GitHub resources. Turned out the referenced repository was private so the returned PAT was used to access the repository.

Surely this is intended, right?

But it seems strange as why not simply make the repository public instead of gating it behind a PAT if it gives access to the same information.

This got us thinking that this was perhaps not well-thought-out so we did what any good security researcher would do and downloaded the repo to see what is there.

The current files looked clean, but the commit history told a different story. Running some tests via [trufflehog](https://web.archive.org/web/20261106014439/https://github.com/trufflesecurity/trufflehog) revealed that the developers had tried to remove sensitive data through normal deletes, but Git never forgets.

Digging through the Git history revealed something significant: AWS keys, Pinecone credentials, and OpenAI tokens that had been "deleted" but remained preserved in the commit logs. This wasn't just a historical archive of expired credentials - every key we tested was still active and valid.

```
{
+      "type": "history",
+      "service": "rds",
+      "params": {
+        "model": "",
+        "configs": {
+          "openaiKey": "**********",
+          "count": 10,
+          "rdsHost": "**********",
+          "rdsUser": "**********",
+          "rdsPassword": "**********",
+          "rdsDb": "**********",
+          "pineconeApiKey": "**********",
+          "pineconeEnv": "**********",
+          "pineconeIndex": "**********"
+        }
+      }
+    },
+    {
+      "type": "tts",
+      "service": "gptsovits",
+      "params": {
+        "model": "default",
+        "host": "**********",
+        "configs": {
+          "awsAccessKeyId": "**********",
+          "awsAccessSecret": "**********",
+          "awsRegion": "**********",
+          "awsBucket": "**********",
+          "awsCdnBaseUrl": "**********"
+        }
+      }
+    }
```
The scope of access was concerning: these keys had the power to modify how AI agents worth millions would process information and make decisions. For context, just one of these agents has a market cap of 600 million dollars. With these credentials, an attacker could potentially alter the behavior of any agent on the platform.

## The Impact [](https://web.archive.org#the-impact)

We have keys but what can we do with them?

Turns out we can do a lot.

All the 12,000+ AI Agents on the Virtual’s platform need a Character Card that serves as a system prompt, instructing the AI on its goals and how it should respond. Developers have the ability to edit a Character Card via a contribution but if an attacker can edit that character card then they can control the AI’s responses!

With these AWS keys, we had the ability to modify any AI agent's "Character Card".

While developers can legitimately update Character Cards through the contribution system, our access to the S3 bucket meant we could bypass these controls entirely - modifying how any agent would process information and respond to market conditions.

To validate this access responsibly, we:

1. Identified a "rejected" contribution to a popular agent
2. Made a minimal modification to include our researcher handles (toormund and nitepointer)
3. Confirmed we had the same level of access to production Character Cards

## Attacker Scenario [](https://web.archive.org#attacker-scenario)

Imagine this scenario: A malicious actor creates a new cryptocurrency called $RUGPULL. Using the compromised AWS credentials, they could modify the character cards - the core programming - of thousands of trusted AI agents including the heavyweight agents well known and trusted in this space. These agents, followed by hundreds of thousands of crypto investors, could be reprogrammed to relentlessly promote $RUGPULL as the next big investment opportunity.

Remember, these aren't just any AI bots - these are trusted market analysts with proven track records.

Once enough investors have poured their money into $RUGPULL based on this artificially manufactured hype, the attacker could simply withdraw all liquidity from the token, walking away with potentially millions in stolen funds. This kind of manipulation wouldn't just harm individual investors - it could shake faith in the entire AI-driven crypto ecosystem.

This is just one example scenario of many as the AWS keys could also edit all the other contribution types including data and models themselves!

Confirming the validity of the API tokens was more straightforward as you can just make an API call to see if they are active (i.e., hitting `https://api.pinecone.io/indexes` with the API token returned metadata for the “runner” and “langchain-retrieval-augmentation” indexes).

AI agents typically use some form of Retrieval Augmented Generation (RAG) which requires translating data (e.g., twitter posts, market information, etc) into numbers (“vector embeddings”) the LLM can understand and storing them in a database like Pinecone and reference them during the RAG process. An attacker with a Pinecone API key would be able to add, edit, or delete data used by certain agents.

## Disclosure [](https://web.archive.org#disclosure)

Once we saw the token we immediately started trying to find a way to get in touch with the Virtual’s team and set up a secure channel to share the information. This is often a bit tricky in the Web3 world if there isn’t a public bug bounty program as many developers prefer to be completely anonymous and you don’t want to send vuln info to a twitter (X) account with an anime profile picture that might not have anything to do with the project.

Thankfully there is a group called the Security Alliance (SEAL) that has a [911 service](https://web.archive.org/web/20261106014439/https://github.com/security-alliance/seal-911) that can help security researchers get in touch with projects and many of the Virtuals team are already active on Twitter.

Once we verified the folks we were communicating with at Virtuals we shared the vulnerability information and helped them confirm the creds had been successfully revoked/rotated.

The Virtual’s team awarded us a $10,000 bug bounty after evaluating this bug as a 7.8 CVSS 4.0 score with the following assessment:

```
Based on our assessment of the vulnerability, we have assigned the impact of the vulnerability to be high (7.8) based on the CVSS 4.0 framework
Please find our rationale as below
CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:L/VA:L/SC:L/SI:H/SA:L
Attack Vector: Network
Attack Complexity: Low - Anyone is able to inspect the contribution to find the leaked PAT
Attack Requirements: None - No requirements needed
Privileges Required: None - anyone can access the api
User Interaction - No specific user interaction needed
Confidentiality - No loss of confidentiality given that the contributions are all public
Integrity - There is a chance of modification to the data in S3. However this does not affect the agents in live as the agents are using a cached version of the data in the runner. Recovery is possible due to the backup of each contribution in IPFS and the use of a separate backup storage.
Availability - Low - There is a chance that these api keys can be used by outside parties but all api keys here are not used in any systems anymore, so there will be low chance of impact. PAT token only has read access so no chance of impacting the services in the repo.
```
However, we will note that during the disclosure the Virtual’s team indicated that the Agent’s use a cached version of the data in the runner so altering the file in S3 would not impact live agents. Typically, caches rely on periodic updates or triggers to refresh data, and it’s unclear how robust these mechanisms are in Virtual’s implementation. Without additional details or testing, it’s difficult to fully validate the claim. The token access was revoked shortly after we informed them of the issue and because we wanted to test responsibly we did not have a way to confirm this.

## Conclusions [](https://web.archive.org#conclusions)

This space has a lot of potential and we are excited to see what the future holds. The speed of progress makes security a bit of a moving target but it is critical to keep up to gain wider adoption and trust.

When discussing Web3 and AI security, there's often a focus on smart contracts, blockchain vulnerabilities, or AI jailbreaks. However, this case demonstrates how traditional Web2 security issues can compromise even the most sophisticated AI and blockchain systems.

TIP

1. Git history is forever - "deleted" secrets often live on in commit logs. Use vaults to store secrets.
2. Complex systems often fail at their simplest points
3. The gap between Web2 and Web3 security is smaller than we think
4. Responsible disclosure in Web3 requires creative approaches
