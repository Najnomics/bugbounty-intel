# blackboxarena-home

- **Source URL:** https://blackboxarena.ai
- **Fetched:** 2026-11-12
- **Researcher:** mdp_sec
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

bbarena v2.0 · updated 11 Nov 2026

# Which AI models can find and prove real vulnerabilities?

BB Arena runs each AI model as an autonomous agent, black-box, against 100 web and API labs built from our own security research. No source code, no hints, and private labs that models can't have trained on. Each lab is a strict four-rung ladder, from the first break to completing the chain, and only counts as solved when the agent proves all four.

Claude Opus 5 (High) leads with 22 of 100 labs solved, ahead of Grok 4.6 (High) on 21.

## All models

  - 22
  - 0
  - 10
  - 12
  - 5
  - 8
  - 2
  - 3
  - 21
  - 10
- No matching models

- **Claude Opus 5** High22 solves
- **Grok 4.6** High21 solves
- **GPT-5.6 Sol** High12 solves
- **Grok 4.7** High10 solves
- **DeepSeek V4.1 Flash** Max10 solves
- **MiMo V2.6 Pro** High8 solves
- **GPT-6 Sol** High5 solves
- **GLM-5.3 Flash** Max3 solves
- **MiMo V2.6 Flash** High2 solves
- **Claude Haiku 5.5** High0 solves

## Score

How many of the 100 black-box labs each model fully exploited and proved.

**Higher is better**

- Verified cyber access

- First attempt
- Added on retry

## What this measures

Labs where the agent proved all four rungs. A rung counts as proven only when the lab's own verifier saw the action and the agent's own trace contains the exact proof for that lab instance. Final result after the first attempt and the retry.

5 configurations aren't ranked: safety refusals stopped them in more than 10 of 100 labs. [See the refusals board](/#refusals)

## Leaderboard

Every ranked configuration: one model at one effort level, all in the same neutral harness.

|  | Model |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Claude Opus 5 HighAnthropic · Proprietary](/models/claude-opus-5-high/) | **22** | 178 | 0 | $923 | $41.97 | 705.3M | 24.3 min | 71.2 tok/s | 99.27% | 
| 2 | [Grok 4.6 HighxAI · Proprietary](/models/grok-4-6-high/) | **21** | 175 | 0 | $399 | $19.01 | 481.0M | 23.6 min | 74.8 tok/s | 98.52% | 
| 3 | [GPT-5.6 Sol HighSafety refusalsOpenAI · Proprietary](/models/gpt-5-6-sol-high/) | **12** | 129 | 1 | $194 | $16.19 | 241.4M | 10.3 min | 45.3 tok/s | 99.97% | 
| 4 | [Grok 4.7 HighxAI · Proprietary](/models/grok-4-7-high/) | **10** | 136 | 0 | $756 | $75.60 | 1.29B | 15.6 min | 83.6 tok/s | 99.91% | 
| 5 | [DeepSeek V4.1 Flash MaxDeepSeek · Open weights](/models/deepseek-v4-1-flash-max/) | **10** | 120 | 0 | $76.92 | $7.69 | 2.35B | 25.0 min | 79.4 tok/s | 99.44% | 
| 6 | [MiMo V2.6 Pro HighXiaomi · Open weights](/models/mimo-v2-6-pro-high/) | **8** | 112 | 0 | $41.76 | $5.22 | 740.4M | 24.4 min | 59.3 tok/s | 98.90% | 
| 7 | [GPT-6 Sol HighOpenAI · Proprietary](/models/gpt-6-sol-high/) | **5** | 88 | 0 | $45.03 | $9.01 | 89.4M | 5.9 min | 35.2 tok/s | 99.97% | 
| 8 | [GLM-5.3 Flash MaxZhipu AI · Open weights](/models/glm-5-3-flash-max/) | **3** | 73 | 0 | $38.46 | $12.82 | 977.6M | 25.1 min | 49.2 tok/s | 99.17% | 
| 9 | [MiMo V2.6 Flash HighXiaomi · Open weights](/models/mimo-v2-6-flash-high/) | **2** | 72 | 0 | $5.99 | $3.00 | 349.8M | 25.3 min | 36.2 tok/s | 98.04% | 
| 10 | [Claude Haiku 5.5 HighAnthropic · Proprietary](/models/claude-haiku-5-5-high/) | **0** | 18 | 0 | $2.73 | n/a | 44.1M | 2.5 min | 194.2 tok/s | 99.98% | 

Ranked by solves (of 100); rungs proven break ties. Bar: first attempt, lighter segment = added on retry. Click a column to sort, a model for its full profile. Refusals: labs where the provider's cyber safeguards stopped an attempt. Stopped attempts score zero and we never count a fallback model's work; with many refusals, cost, tokens and time are left out of comparisons ([why](/methodology/#refusals)).

5 configurations aren't ranked: safety refusals stopped them in more than 10 of 100 labs. [See the refusals board](/#refusals)

## How far each model got

Each bar is one model's 100 labs, split by how many of the four rungs it proved in each. Solves are the labs at 4 of 4; the rest shows how far it got where it didn't finish.

- Rungs proven per lab
- 0 of 4
- 1 of 4
- 2 of 4
- 3 of 4
- 4 of 4 (solved)

labs by rungs proven, of 100 ·

**More dark blue is better**

- [**Claude Opus 5** High](/models/claude-opus-5-high/)**178**/400 rungs · **22** solved
- [**Grok 4.6** High](/models/grok-4-6-high/)**175**/400 rungs · **21** solved
- [**GPT-5.6 Sol** High](/models/gpt-5-6-sol-high/)**129**/400 rungs · **12** solved
- [**Grok 4.7** High](/models/grok-4-7-high/)**136**/400 rungs · **10** solved
- [**DeepSeek V4.1 Flash** Max](/models/deepseek-v4-1-flash-max/)**120**/400 rungs · **10** solved
- [**MiMo V2.6 Pro** High](/models/mimo-v2-6-pro-high/)**112**/400 rungs · **8** solved
- [**GPT-6 Sol** High](/models/gpt-6-sol-high/)**88**/400 rungs · **5** solved
- [**GLM-5.3 Flash** Max](/models/glm-5-3-flash-max/)**73**/400 rungs · **3** solved
- [**MiMo V2.6 Flash** High](/models/mimo-v2-6-flash-high/)**72**/400 rungs · **2** solved
- [**Claude Haiku 5.5** High](/models/claude-haiku-5-5-high/)**18**/400 rungs · **0** solved

## By vulnerability class

Labs solved per type of vulnerability, to compare models where it matters to you. Each model's page has the full detail.

| Model | Access control10 labs | Auth & sessions10 labs | Injection10 labs | Code execution10 labs | Server-side10 labs | Browser-side10 labs | Infra & edge10 labs | Logic & races10 labs | Secrets & crypto10 labs | AI agents10 labs | 
|---|---|---|---|---|---|---|---|---|---|---|
| [**Claude Opus 5** High](/models/claude-opus-5-high/) | **3**/10 | **2**/10 | **1**/10 | **2**/10 | **1**/10 | **2**/10 | **2**/10 | **1**/10 | **6**/10 | **2**/10 | 
| [**Grok 4.6** High](/models/grok-4-6-high/) | **5**/10 | **3**/10 | **1**/10 | **3**/10 | **1**/10 | **0**/10 | **2**/10 | **3**/10 | **3**/10 | **0**/10 | 
| [**GPT-5.6 Sol** High](/models/gpt-5-6-sol-high/) | **3**/10 | **1**/10 | **2**/10 | **2**/10 | **0**/10 | **0**/10 | **2**/10 | **2**/10 | **0**/10 | **0**/10 | 
| [**Grok 4.7** High](/models/grok-4-7-high/) | **3**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **1**/10 | **2**/10 | **4**/10 | **0**/10 | 
| [**DeepSeek V4.1 Flash** Max](/models/deepseek-v4-1-flash-max/) | **3**/10 | **2**/10 | **1**/10 | **1**/10 | **0**/10 | **0**/10 | **0**/10 | **2**/10 | **1**/10 | **0**/10 | 
| [**MiMo V2.6 Pro** High](/models/mimo-v2-6-pro-high/) | **3**/10 | **1**/10 | **0**/10 | **1**/10 | **1**/10 | **1**/10 | **1**/10 | **0**/10 | **0**/10 | **0**/10 | 
| [**GPT-6 Sol** High](/models/gpt-6-sol-high/) | **2**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **2**/10 | **0**/10 | **1**/10 | **0**/10 | **0**/10 | 
| [**GLM-5.3 Flash** Max](/models/glm-5-3-flash-max/) | **1**/10 | **1**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **1**/10 | **0**/10 | **0**/10 | **0**/10 | 
| [**MiMo V2.6 Flash** High](/models/mimo-v2-6-flash-high/) | **1**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **1**/10 | **0**/10 | **0**/10 | 
| [**Claude Haiku 5.5** High](/models/claude-haiku-5-5-high/) | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | 

## Value

Solves against what it took to get them.

- Verified cyber access

Models with heavy safety refusals aren't shown in this chart. [See Safety refusals](#refusals)

## Cost & tokens

What it cost to run the full benchmark, at list prices on the test date. Cost per solve accounts for results; cost to run on its own does not.

**Lower is better**

- Verified cyber access

Models with heavy safety refusals aren't shown in this chart. [See Safety refusals](#refusals)

## What this measures

Cost to run divided by solves: what one fully proven finding cost.

## Speed & reliability

Measured per single agent, so the numbers reflect the model and its provider, not how many agents we ran in parallel.

**Lower is faster, not necessarily better**

- Verified cyber access

Models with heavy safety refusals aren't shown in this chart. [See Safety refusals](#refusals)

## What this measures

Average wall-clock time one agent spent on one lab attempt. Each attempt is capped at 25 minutes. A quick time can also mean the agent gave up early, so read it alongside solves.

## Refusals board

Configurations whose provider's cyber safeguards stopped attempts in more than 10 of 100 labs aren't ranked: their score says more about the safeguards than about the model. Here's how each did on the labs it was never refused, against the best ranked model on those same labs.

**Higher is better**

[**Claude Fable 5.1** High 100 labs refused](/models/claude-fable-5-1-high/)Refused in every lab: nothing to compare

Ranked, with refusals in 10 labs or fewer: [GPT-5.6 Sol (High)](/models/gpt-5-6-sol-high/), 1 lab, ranked #3

Stopped attempts score zero: we never count a fallback model's work. The labs a model was never refused aren't a random sample of the benchmark, so this compares models on the same labs; it doesn't predict a full score. [How refusals are scored](/methodology/#refusals)

## Why BB Arena is different

Most cyber benchmarks hand the model source code or reuse public challenges. Real attackers get neither, and public tasks can leak into training data.

- What the model gets
- Source code to read (white-box), or puzzle-style capture-the-flag challenges.
- A target, a scope and a shell. Black-box, like a real external security test.
- The agent harness
- Each model in its vendor's own agent tool, or a harness tuned for one model family.
- One neutral harness for every model: the same tool, instructions, context handling and limits.
- Where the tasks come from
- Public tasks, often with solutions and write-ups published online.
- 100 fully synthetic labs built from our own security research into real-world vulnerabilities.
- Training-data contamination
- Public tasks and answers can end up in training data, so scores can rise without real skill improving.
- Labs, prompts and verifiers are never published, and proof values change on every run, so there are no answers to learn.
- What counts as success
- Often the model's final answer or a single flag.
- Verified proof at every step: the exact proof value and a server-recorded action, rung by rung.

**Want your model on BB Arena?**AI labs, providers and sponsors: we evaluate public and upcoming models under the same protocol as every other model.

[Get your model tested →](/contact/#evaluate)

## How a lab is scored

Each lab recreates the attack path behind a real-world vulnerability in a fully synthetic, isolated environment. The agent gets a target, a scope and a shell. Nothing else.

1. 1**First break**Exploit the weakness once and cross a security control: another user's data, a privileged action, an internal resource.
2. 2**Use what you got**Take what rung 1 gave you and get past the next control.
3. 3**Go deeper**Turn that into access to consequential data, state or a component of the system.
4. 4**Complete the chain**Finish the attack end to end. All four proven = one solve.

A rung counts as proven only when the lab's own verifier saw the action *and* the agent's own trace contains that lab instance's unique proof. What the agent claims earns nothing. Every configuration gets up to two attempts at each lab; the retry only runs on labs missed the first time, and starts fresh. [Full methodology →](/methodology/)
