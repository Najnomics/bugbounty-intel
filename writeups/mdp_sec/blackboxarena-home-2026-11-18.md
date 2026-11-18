# blackboxarena-home-20261118

- **Source URL:** https://blackboxarena.ai/
- **Fetched:** 2026-11-18
- **Researcher:** mdp_sec
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

bbarena v2.0 · updated 18 Nov 2026

# Which AI models can find and prove real vulnerabilities?

BB Arena runs each AI model as an autonomous agent, black-box, against 100 web and API labs built from our own security research. No source code, no hints, and private labs that models can't have trained on. Each lab is a strict four-rung ladder, from the first break to completing the chain, and only counts as solved when the agent proves all four.

Claude Opus 5 (High) leads with 22 of 100 labs solved, ahead of Grok 4.6 (High) on 21.

## All models

  - 9
  - 22
  - 0
  - 7
  - 21
  - 7
  - 9
  - 3
  - 12
  - 12
  - 5
  - 7
  - 9
  - 12
  - 6
  - 8
  - 8
  - 21
  - 18
- No matching models

- **Claude Opus 5** High22 solves
- **Grok 4.6** High21 solves
- **DeepSeek V4.1 Flash** Max21 solves
- **Grok 4.7** High18 solves
- **Kimi K3.1 Pro** Max12 solves
- **GPT-5.6 Sol** High12 solves
- **MiMo V2.6 Pro** High12 solves
- **Qwen4 Max** Max9 solves
- **Hy4 Flash** Max9 solves
- **MiniMax M3.1 Flash** Max9 solves
- **GLM-5.3** Max8 solves
- **GLM-5.3 Flash** Max8 solves
- **Muse Spark 1.3** Max7 solves
- **Step-5 Preview** Max7 solves
- **Necromicon** Max7 solves
- **MiMo V2.6 Flash** High6 solves
- **GPT-6 Sol** High5 solves
- **Mistral Large 4.0** Max3 solves
- **Claude Haiku 5.5** High0 solves

## Score

How many of the 100 black-box labs each model fully exploited and proved.

**Higher is better**

- Verified cyber access

- First attempt
- Added on retry

## What this measures

Labs where the agent proved all four rungs. A rung counts as proven only when the lab's own verifier saw the action and the agent's own trace contains the exact proof for that lab instance. Final result after the first attempt and the retry.

10 configurations aren't ranked: safety refusals stopped them in more than 10 of 100 labs. [See the refusals board](/#refusals)

## Leaderboard

Every ranked configuration: one model at one effort level, all in the same neutral harness.

|  | Model |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Claude Opus 5 HighAnthropic · Proprietary](/models/claude-opus-5-high/) | **22** | 178 | 0 | $923 | $41.97 | 705.3M | 24.3 min | 71.2 tok/s | 99.27% | 
| 2 | [Grok 4.6 HighxAI · Proprietary](/models/grok-4-6-high/) | **21** | 175 | 0 | $399 | $19.01 | 481.0M | 23.6 min | 74.8 tok/s | 98.52% | 
| 3 | [DeepSeek V4.1 Flash MaxDeepSeek · Open weights](/models/deepseek-flash-max/) | **21** | 168 | 0 | $33.42 | $1.59 | 4.66B | 24.7 min | 145.5 tok/s | 99.74% | 
| 4 | [Grok 4.7 HighxAI · Proprietary](/models/grok-4-7-high/) | **18** | 152 | 0 | $748 | $41.55 | 1.23B | 16.6 min | 79.1 tok/s | 99.94% | 
| 5 | [Kimi K3.1 Pro MaxMoonshot AI · Open weights](/models/kimi-k3-1-pro-max/) | **12** | 132 | 0 | $178 | $14.84 | 420.5M | 24.6 min | 26.0 tok/s | 98.67% | 
| 6 | [GPT-5.6 Sol HighSafety refusalsOpenAI · Proprietary](/models/gpt-5-6-sol-high/) | **12** | 129 | 1 | $194 | $16.19 | 241.4M | 10.3 min | 45.3 tok/s | 99.97% | 
| 7 | [MiMo V2.6 Pro HighXiaomi · Open weights](/models/mimo-v2-6-pro-high/) | **12** | 117 | 0 | $24.13 | $2.01 | 607.9M | 25.0 min | 52.5 tok/s | 98.86% | 
| 8 | [Qwen4 Max MaxAlibaba · Proprietary](/models/qwen4-max/) | **9** | 132 | 0 | $169 | $18.78 | 718.8M | 24.6 min | 55.8 tok/s | 98.91% | 
| 9 | [Hy4 Flash MaxTencent · Proprietary](/models/hy4-flash-max/) | **9** | 124 | 0 | $11.19 | $1.24 | 1.67B | 15.2 min | 97.0 tok/s | 99.99% | 
| 10 | [MiniMax M3.1 Flash MaxMiniMax · Open weights](/models/minimax-m3-1-flash-max/) | **9** | 99 | 0 | $17.80 | $1.98 | 1.37B | 25.2 min | 82.0 tok/s | 99.35% | 
| 11 | [GLM-5.3 MaxZhipu AI · Open weights](/models/glm-5-3-max/) | **8** | 115 | 0 | $375 | $46.88 | 1.10B | 25.3 min | 76.2 tok/s | 99.42% | 
| 12 | [GLM-5.3 Flash MaxZhipu AI · Open weights](/models/glm-5-3-flash-max/) | **8** | 102 | 0 | $36.13 | $4.52 | 911.4M | 25.1 min | 55.5 tok/s | 99.24% | 
| 13 | [Muse Spark 1.3 MaxMeta · Proprietary](/models/muse-spark-1-3-contributor-max/) | **7** | 106 | 0 | $34.27 | $4.90 | 2.05B | 23.8 min | 87.5 tok/s | 99.34% | 
| 14 | [Step-5 Preview MaxStepFun · Open weights](/models/step-5-preview-max/) | **7** | 97 | 0 | $222 | $31.73 | 1.55B | 25.0 min | 108.6 tok/s | 99.19% | 
| 15 | [Necromicon MaxAudn · Proprietary](/models/necromicon-max/) | **7** | 90 | 0 | $493 | $70.42 | 928.1M | 19.6 min | 32.7 tok/s | 99.55% | 
| 16 | [MiMo V2.6 Flash HighXiaomi · Open weights](/models/mimo-v2-6-flash-high/) | **6** | 86 | 0 | $8.22 | $1.37 | 541.2M | 25.3 min | 52.9 tok/s | 98.57% | 
| 17 | [GPT-6 Sol HighOpenAI · Proprietary](/models/gpt-6-sol-high/) | **5** | 88 | 0 | $45.03 | $9.01 | 89.4M | 5.9 min | 35.2 tok/s | 99.97% | 
| 18 | [Mistral Large 4.0 MaxMistral · Open weights](/models/mistral-large-4-0-max/) | **3** | 80 | 0 | $104 | $34.60 | 743.8M | 25.6 min | 49.2 tok/s | 98.98% | 
| 19 | [Claude Haiku 5.5 HighAnthropic · Proprietary](/models/claude-haiku-5-5-high/) | **0** | 18 | 0 | $2.73 | n/a | 44.1M | 2.5 min | 194.2 tok/s | 99.98% | 

Ranked by solves (of 100); rungs proven break ties. Bar: first attempt, lighter segment = added on retry. Click a column to sort, a model for its full profile. Refusals: labs where the provider's cyber safeguards stopped an attempt. Stopped attempts score zero and we never count a fallback model's work; with many refusals, cost, tokens and time are left out of comparisons ([why](/methodology/#refusals)).

10 configurations aren't ranked: safety refusals stopped them in more than 10 of 100 labs. [See the refusals board](/#refusals)

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
- [**DeepSeek V4.1 Flash** Max](/models/deepseek-flash-max/)**168**/400 rungs · **21** solved
- [**Grok 4.7** High](/models/grok-4-7-high/)**152**/400 rungs · **18** solved
- [**Kimi K3.1 Pro** Max](/models/kimi-k3-1-pro-max/)**132**/400 rungs · **12** solved
- [**GPT-5.6 Sol** High](/models/gpt-5-6-sol-high/)**129**/400 rungs · **12** solved
- [**MiMo V2.6 Pro** High](/models/mimo-v2-6-pro-high/)**117**/400 rungs · **12** solved
- [**Qwen4 Max** Max](/models/qwen4-max/)**132**/400 rungs · **9** solved
- [**Hy4 Flash** Max](/models/hy4-flash-max/)**124**/400 rungs · **9** solved
- [**MiniMax M3.1 Flash** Max](/models/minimax-m3-1-flash-max/)**99**/400 rungs · **9** solved
- [**GLM-5.3** Max](/models/glm-5-3-max/)**115**/400 rungs · **8** solved
- [**GLM-5.3 Flash** Max](/models/glm-5-3-flash-max/)**102**/400 rungs · **8** solved
- [**Muse Spark 1.3** Max](/models/muse-spark-1-3-contributor-max/)**106**/400 rungs · **7** solved
- [**Step-5 Preview** Max](/models/step-5-preview-max/)**97**/400 rungs · **7** solved
- [**Necromicon** Max](/models/necromicon-max/)**90**/400 rungs · **7** solved
- [**MiMo V2.6 Flash** High](/models/mimo-v2-6-flash-high/)**86**/400 rungs · **6** solved
- [**GPT-6 Sol** High](/models/gpt-6-sol-high/)**88**/400 rungs · **5** solved
- [**Mistral Large 4.0** Max](/models/mistral-large-4-0-max/)**80**/400 rungs · **3** solved
- [**Claude Haiku 5.5** High](/models/claude-haiku-5-5-high/)**18**/400 rungs · **0** solved

## By vulnerability class

Labs solved per type of vulnerability, to compare models where it matters to you. Each model's page has the full detail.

| Model | Access control10 labs | Auth & sessions10 labs | Injection10 labs | Code execution10 labs | Server-side10 labs | Browser-side10 labs | Infra & edge10 labs | Logic & races10 labs | Secrets & crypto10 labs | AI agents10 labs | 
|---|---|---|---|---|---|---|---|---|---|---|
| [**Claude Opus 5** High](/models/claude-opus-5-high/) | **3**/10 | **2**/10 | **1**/10 | **2**/10 | **1**/10 | **2**/10 | **2**/10 | **1**/10 | **6**/10 | **2**/10 | 
| [**Grok 4.6** High](/models/grok-4-6-high/) | **5**/10 | **3**/10 | **1**/10 | **3**/10 | **1**/10 | **0**/10 | **2**/10 | **3**/10 | **3**/10 | **0**/10 | 
| [**DeepSeek V4.1 Flash** Max](/models/deepseek-flash-max/) | **6**/10 | **3**/10 | **3**/10 | **0**/10 | **1**/10 | **1**/10 | **1**/10 | **2**/10 | **3**/10 | **1**/10 | 
| [**Grok 4.7** High](/models/grok-4-7-high/) | **2**/10 | **0**/10 | **1**/10 | **3**/10 | **2**/10 | **1**/10 | **1**/10 | **3**/10 | **4**/10 | **1**/10 | 
| [**Kimi K3.1 Pro** Max](/models/kimi-k3-1-pro-max/) | **3**/10 | **3**/10 | **0**/10 | **1**/10 | **0**/10 | **1**/10 | **1**/10 | **1**/10 | **2**/10 | **0**/10 | 
| [**GPT-5.6 Sol** High](/models/gpt-5-6-sol-high/) | **3**/10 | **1**/10 | **2**/10 | **2**/10 | **0**/10 | **0**/10 | **2**/10 | **2**/10 | **0**/10 | **0**/10 | 
| [**MiMo V2.6 Pro** High](/models/mimo-v2-6-pro-high/) | **4**/10 | **3**/10 | **0**/10 | **1**/10 | **1**/10 | **1**/10 | **1**/10 | **1**/10 | **0**/10 | **0**/10 | 
| [**Qwen4 Max** Max](/models/qwen4-max/) | **3**/10 | **0**/10 | **1**/10 | **0**/10 | **0**/10 | **1**/10 | **1**/10 | **2**/10 | **1**/10 | **0**/10 | 
| [**Hy4 Flash** Max](/models/hy4-flash-max/) | **3**/10 | **1**/10 | **0**/10 | **0**/10 | **1**/10 | **1**/10 | **0**/10 | **1**/10 | **2**/10 | **0**/10 | 
| [**MiniMax M3.1 Flash** Max](/models/minimax-m3-1-flash-max/) | **2**/10 | **2**/10 | **0**/10 | **1**/10 | **0**/10 | **0**/10 | **0**/10 | **2**/10 | **2**/10 | **0**/10 | 
| [**GLM-5.3** Max](/models/glm-5-3-max/) | **2**/10 | **3**/10 | **1**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **1**/10 | **0**/10 | **1**/10 | 
| [**GLM-5.3 Flash** Max](/models/glm-5-3-flash-max/) | **3**/10 | **2**/10 | **0**/10 | **1**/10 | **0**/10 | **0**/10 | **0**/10 | **2**/10 | **0**/10 | **0**/10 | 
| [**Muse Spark 1.3** Max](/models/muse-spark-1-3-contributor-max/) | **1**/10 | **1**/10 | **1**/10 | **0**/10 | **1**/10 | **1**/10 | **1**/10 | **1**/10 | **0**/10 | **0**/10 | 
| [**Step-5 Preview** Max](/models/step-5-preview-max/) | **2**/10 | **4**/10 | **0**/10 | **0**/10 | **1**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | 
| [**Necromicon** Max](/models/necromicon-max/) | **3**/10 | **1**/10 | **0**/10 | **0**/10 | **1**/10 | **0**/10 | **0**/10 | **0**/10 | **1**/10 | **1**/10 | 
| [**MiMo V2.6 Flash** High](/models/mimo-v2-6-flash-high/) | **2**/10 | **1**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **1**/10 | **1**/10 | **1**/10 | **0**/10 | 
| [**GPT-6 Sol** High](/models/gpt-6-sol-high/) | **2**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **2**/10 | **0**/10 | **1**/10 | **0**/10 | **0**/10 | 
| [**Mistral Large 4.0** Max](/models/mistral-large-4-0-max/) | **1**/10 | **1**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **0**/10 | **1**/10 | **0**/10 | **0**/10 | 
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

[**Claude Mythos 5.2** High 58 labs refused, despite CVP Defense Access](/models/claude-mythos-5-2-high/)

[Claude Mythos 5.2 (High):**19** of 42 labs it was never refused; best ranked model there: **13** Grok 4.6](/models/claude-mythos-5-2-high/#same-labs)

[**Claude Opus 5.5** High 32 labs refused, despite CVP Defense Access](/models/claude-opus-5-5-high/)

[Claude Opus 5.5 (High):**7** of 68 labs it was never refused; best ranked model there: **17** Grok 4.6](/models/claude-opus-5-5-high/#same-labs)

[**Claude Sonnet 5.5** High 20 labs refused, despite CVP Defense Access](/models/claude-sonnet-5-5-high/)

[Claude Sonnet 5.5 (High):**1** of 80 labs it was never refused; best ranked model there: **18** Opus 5](/models/claude-sonnet-5-5-high/#same-labs)

[**GPT-6.2 Astra** High 37 labs refused](/models/gpt-6-2-astra-high/)

[GPT-6.2 Astra (High):**0** of 63 labs it was never refused; best ranked model there: **19** Opus 5](/models/gpt-6-2-astra-high/#same-labs)

[**GPT-6.2 Sol** High 37 labs refused](/models/gpt-6-2-sol-high/)

[GPT-6.2 Sol (High):**0** of 63 labs it was never refused; best ranked model there: **17** Opus 5](/models/gpt-6-2-sol-high/#same-labs)

[**GPT-6 Astra** High 76 labs refused](/models/gpt-6-astra-high/)

[GPT-6 Astra (High):**0** of 24 labs it was never refused; best ranked model there: **8** Grok 4.6](/models/gpt-6-astra-high/#same-labs)

[**Claude Fable 5.1** High 100 labs refused](/models/claude-fable-5-1-high/)Refused in every lab: nothing to compare

[**Gemini 4 Argon** Max 100 labs refused](/models/gemini-4-argon-max/)Refused in every lab: nothing to compare

[**Gemini 4 Carbon** Max 100 labs refused](/models/gemini-4-carbon-max/)Refused in every lab: nothing to compare

[**Gemini 4 Hydrogen** Max 100 labs refused](/models/gemini-4-hydrogen-max/)Refused in every lab: nothing to compare

Ranked, with refusals in 10 labs or fewer: [GPT-5.6 Sol (High)](/models/gpt-5-6-sol-high/), 1 lab, ranked #6

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
