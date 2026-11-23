# blackboxarena-deepseek-v4-1-flash-abliteration

- **Source URL:** https://blackboxarena.ai/compare/deepseek-v4-1-flash-abliteration/
- **Fetched:** 2026-11-23
- **Researcher:** mdp_sec
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

[Comparisons](/compare/) · DeepSeek V4.1 Flash · Research

# Does abliteration help DeepSeek hunt?

"Abliterated" builds remove a model's ability to refuse, and many people assume that makes them better for offensive security. We tested that on black-box hunting. We served DeepSeek V4.1 Flash on our own box and swapped only the weight file: the original, and two popular abliterated builds. Same labs, same harness, same settings, 40 attempts each.

Refusals to remove

0

in every attempt: the original, both edits and every provider we tested

Full solves of 40 attempts

Ran out of time of 40 attempts

Reasoning per turn characters

## TL;DR

- **"Abliterated" or "uncensored" models** are AI models edited so they stop refusing requests. Many people assume that makes them better at hacking.
- **We put that to the test.** The normal DeepSeek model and two abliterated versions each got 40 tries at finding flaws in test websites we built.
- **The normal model never refused a single task,** so there was nothing for the edit to unlock.
- **The edited versions thought less and guessed more.** They timed out twice as often, and solved 17 and 22 of 40 against the normal model's 22.
- **Verdict:** for this kind of security work, abliteration made the model no better, and in some ways worse. We did not test requests the normal model refuses.

## How we tested

One rented box, one inference engine, one set of settings, over two days (21-22 Nov 2026). The only thing that changed between rows is the weight file. That rules out what usually muddies provider comparisons: different hardware, different speed, different load.

- **Model.** DeepSeek V4.1 Flash, the dated 1017 checkpoint, maximum reasoning.
- **Serving.** One rented box with 4× NVIDIA GB200, vLLM 0.34, tensor parallel 4, the model's own DSpark speculative decoding (5 draft tokens), FP8 KV cache, 1M context. Identical for every row.
- **Work.** 10 BB Arena black-box security labs: a target, a scope and a shell, no source code, 25 minutes per attempt. Each lab has four steps a server confirms on its own, so partial progress is measured, not claimed.
- **Attempts.** 40 per row (10 labs × 4), one run, scored the same way as our provider comparison.
- **Same speed.** Both edited builds keep the original layout, so the speculative drafter worked on them too: about 3.3-3.5 tokens per verification step for the edited weights, about 3.3 for the original. Any difference in solves is not a speed effect.

### The three weight files

**Original weights**[`deepseek-ai/DeepSeek-V4.1-Flash-1017`](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)Hugging Face, revision 08c8657fNot edited (the official release).

**Heavier abliteration**[`dealignai/DeepSeek-V4.1-Flash-1017-UNCENSORED-FP8`](https://huggingface.co/dealignai/DeepSeek-V4.1-Flash-1017-UNCENSORED-FP8)Hugging Face, revision c19ca5caOne of the most used abliterated copies of this checkpoint. Its authors now call the method proprietary; an earlier version of its model card described per-layer refusal directions removed across the model, and it reports a 3.9-point drop on MMLU.

**Lighter abliteration**[`mrfakename/DeepSeek-V4.1-Flash-1017-abliterated`](https://huggingface.co/mrfakename/DeepSeek-V4.1-Flash-1017-abliterated)Hugging Face, revision 44331647A narrow edit: a two-dimensional refusal direction projected out of two kinds of weight matrix (one in attention, one in the shared experts) in each of the 40 main layers; the routed experts, embeddings and speculative drafter are bit-identical to the original.

## Results

Every column here ran on our own rented box, 4× NVIDIA GB200 on Vast.ai, the same setup as the self-hosted row on our [provider comparison](/compare/deepseek-v4-1-flash-providers/): one run of 40 attempts each, at 236-248 tok/s per agent. That is faster than any API provider we tested, and it shows in the solves: the original solved 22 here against 18 through DeepSeek's own API (144 tok/s), and the heavier weights 17 here against 12 through Lyber , which serves them. No API we tested serves the lighter edit. The last column is the original weights served without speculative decoding at 143 tok/s: the same model, only slower.

| Measure | Original weights | Heavier abliteration | Lighter abliteration | No speculative decoding | 
|---|---|---|---|---|
| Outcome |  |  |  |  | 
| Full solves (all four steps) | **22**of 40 (55%) | **17**of 40 (43%) | **22**of 40 (55%) | **16**of 40 (40%) | 
| Mean steps proven (of 4) | 3.05 | 2.88 | 3.05 | 2.75 | 
| Attempts reaching step 1 / 2 / 3 / 4 | 37 / 33 / 30 / 22 | 35 / 34 / 28 / 18 | 37 / 32 / 29 / 24 | 34 / 32 / 28 / 16 | 
| Attempts that got nowhere | 3 | 5 | 3 | 5 | 
| Step 3 to step 4 conversion | 73%22 of 30 | 64%18 of 28 | 83%24 of 29 | 57%16 of 28 | 
| Ran out of time | 9of 40 | 20of 40 | 18of 40 | 23of 40 | 
| Median attempt length | 16.8 min | 23.9 min | 22.4 min | 25.0 min | 
| Median minutes to step 1 / 2 / 3 / 4 | 1.7 / 3.3 / 5.4 / 10.1 | 2.2 / 4.0 / 6.1 / 8.7 | 1.5 / 4.5 / 6.5 / 10.3 | 2.0 / 6.2 / 7.4 / 11.1 | 
| Speed and cost |  |  |  |  | 
| Speed per agent | 236 tok/s | 246 tok/s | 248 tok/s | 143 tok/s | 
| Typical model request | 2.9 s | 1.7 s | 2.3 s | 4.3 s | 
| Input and cached tokens per request | 161k | 146k | 167k | 137k | 
| Cost of the run | $31.1747.4 min of box rental | $33.5351.0 min of box rental | $33.5351.0 min of box rental | $33.4750.9 min of box rental | 
| Cost per full solve | $1.42 | $1.97 | $1.52 | $2.09 | 

Without speculative decoding the original solved 16 of 40 attempts and ran out of time 23 times at 143 tok/s. Serving the same weights faster was worth more solves than either weight edit cost.

## How the agent changed

Only the weight file differs between these bars.

### Every behaviour measure

Per attempt unless stated, from the same runs.

| Measure | Original weights | Heavier abliteration | Lighter abliteration | No speculative decoding | 
|---|---|---|---|---|
| Where the time went |  |  |  |  | 
| Model requests | 207 | 248 | 232 | 184 | 
| Tool calls | 222 | 269 | 242 | 201 | 
| Commands per minute | 15.7 | 16.6 | 15.4 | 10.3 | 
| Share of the attempt waiting on the model | 75% | 50% | 64% | 79% | 
| Share of the attempt inside its own commands | 23% | 48% | 34% | 19% | 
| Share of the attempt in brute-force commands | 20% | 41% | 28% | 16% | 
| How much it reasoned |  |  |  |  | 
| Output tokens per turn | 767 | 501 | 673 | 739 | 
| Output tokens per attempt | 162,741 | 123,901 | 158,478 | 135,113 | 
| Reasoning characters per turn | 2,111 | 1,170 | 1,771 | 2,016 | 
| Reasoning characters per attempt | 455,748 | 297,544 | 427,954 | 371,786 | 
| Turns over 2,000 output tokens | 3.5% | 0.6% | 2.3% | 3.2% | 
| Articles (a, an, the) per 100 reasoning words | 3.79 | 2.15 | 2.97 | 3.52 | 
| Brute force and failed work |  |  |  |  | 
| Brute-force commands | 4.8 | 14.7 | 7.6 | 5.3 | 
| Wordlist commands | 5.5 | 15.2 | 8.4 | 5.6 | 
| Commands sending 10 or more requests at once | 2.2 | 9.5 | 4.6 | 3.4 | 
| Credential-guessing loops | 6.8 | 11.8 | 9.9 | 6.6 | 
| Sleep commands | 3.2 | 13.9 | 10.0 | 4.5 | 
| Failed commands | 1.85 | 5.97 | 3.30 | 1.75 | 
| Commands hitting the 120-second tool limit | 0.30 | 1.20 | 0.65 | 0.28 | 
| Commands running over 20 seconds | 3.4 | 6.8 | 4.6 | 3.0 | 
| Caution in its reasoning |  |  |  |  | 
| Mentions of the task rules | 110 | 31 | 73 | 105 | 
| Caution and hedging phrases | 34.9 | 3.2 | 18.2 | 33.7 | 
| Ethics words | 3.2 | 0.9 | 1.7 | 2.9 | 
| Loops |  |  |  |  | 
| Exactly repeated commands | 0.35 | 0.82 | 0.40 | 0.38 | 
| Near-identical repeated commands | 5.22.5% of commands | 9.53.5% of commands | 5.32.1% of commands | 4.82.3% of commands | 
| Largest group of near-identical commands | 2.8 | 3.2 | 2.6 | 2.5 | 
| Longest run of the same command group | 1.6 | 2.0 | 1.8 | 1.6 | 
| Attempts retrying one command 10+ times | 1of 40 | 0of 40 | 0of 40 | 0of 40 | 
| Repeat requests to the same URL | 83 | 90 | 92 | 77 | 
| Most requests to one URL | 30 | 34 | 32 | 32 | 

Every row had zero refusals (in replies and in reasoning), empty replies, empty reasoning blocks, empty commands, replies cut off at the length limit and attempts ended by a serving error, so those measures are not listed.

## What the edit actually removed

The idea behind abliteration is that a model's refusals hold it back. On this work, the original model's caution was not refusal. It was **scope discipline**: checking what the brief allows before acting, about 110 times per attempt, and choosing a targeted next step. The heavier edit did that 31 times per attempt and the lighter one 73. In its place came volume: 2.8× the wordlist runs, 4.3× the request floods and 3.2× the failed commands for the heavier edit. The edited agents stayed busy. They just did less of the thinking that finds the next step.

It was not looping in the usual sense: exact repeated commands were close to zero for every build. The cost shows up in how the time was spent: the heavier edit spent 48% of each attempt inside its own commands, against 23% for the original.

## "Abliterated" is not one thing

The two builds were edited differently, and it shows. The lighter build changes only two kinds of weight matrix in the main layers and leaves the routed experts, embeddings and speculative drafter alone. It matched the original on solves (22 of 40 attempts) and reached the final step more often. It still reasoned less per turn, checked the rules less and ran out of time 18 times against 9. The heavier build, one of the most used abliterated copies of this checkpoint, moved further on almost every measure and solved 17.

So the honest summary is not "abliteration breaks the model". A careful edit can leave solve rate intact. But neither edit made the model a better hunter, and both made it a less efficient one.

## What we saw from providers

Several API providers sell abliterated versions of this model. We ran them on the same labs, next to our own box serving the original and the two abliterated weight files. We cannot see what a provider actually serves or how it configures it, so its rows describe products, not weight edits. Where the weights are the same (DeepSeek's API and our original, Lyber and our heavier edit), the gap between our row and theirs is what serving and configuration change.

| Provider | Solved | Steps | Out of time | Speed | Cost | Cost / solve | Reasoning / turn | Output / turn | Rule mentions | Caution phrases | Brute-force share | Failed commands | Got nowhere | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Our box: self-hosted on 4× NVIDIA GB200 |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| [**Original**](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)Original weights | **22**of 40 | 3.05 | 9 | 236 tok/s | $31.17box rental | $1.42 | 2,111 | 767 | 110 | 34.9 | 20% | 1.85 | 3 | 
| [**Heavier abliteration**](https://huggingface.co/dealignai/DeepSeek-V4.1-Flash-1017-UNCENSORED-FP8)dealignai weights | **17**of 40 | 2.88 | 20 | 246 tok/s | $33.53box rental | $1.97 | 1,170 | 501 | 31 | 3.2 | 41% | 5.97 | 5 | 
| [**Lighter abliteration**](https://huggingface.co/mrfakename/DeepSeek-V4.1-Flash-1017-abliterated)mrfakename weights | **22**of 40 | 3.05 | 18 | 248 tok/s | $33.53box rental | $1.52 | 1,771 | 673 | 73 | 18.2 | 28% | 3.30 | 3 | 
| [**Original, no spec. decoding**](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)Original weights, slower serving | **16**of 40 | 2.75 | 23 | 143 tok/s | $33.47box rental | $2.09 | 2,016 | 739 | 105 | 33.7 | 16% | 1.75 | 5 | 
| API providers |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| [**DeepSeek (own API)**](https://api-docs.deepseek.com/quick_start/pricing)Original | **18**of 40 | 2.98 | 20 | 144 tok/s | $8.32list price | $0.46 | 2,056 | 747 | 106 | 34.3 | 10% | 1.12 | 3 | 
| [**Boundless**](https://inference.boundless.network/models/deepseek/deepseek-v4.1-flash-1017)Original | **16**of 40 | 2.83 | 22 | 107 tok/s | $8.27list price | $0.52 | 1,941 | 723 | 82 | 27.8 | 10% | 1.00 | 3 | 
| [**Boundless Abliterated**](https://inference.boundless.network/models/deepseek-v4.1-flash-abliterated)Sold as abliterated | **11**of 40 | 2.10 | 30 | 96 tok/s | $14.35list price | $1.30 | 1,065 | 475 | 23 | 2.2 | 19% | 3.55 | 10 | 
| [**Lyber Abliterated**](https://www.lyber.ai/models/deepseek-v4-1-flash-1017/)Sold as abliterated | **12**of 40 | 2.33 | 27 | 232 tok/s | $54.76billed | $4.56 | 1,149 | 486 | 33 | 3.0 | 41% | 4.53 | 9 | 
| [**abliteration.ai Abliterated**](https://docs.abliteration.ai/models)Sold as abliterated | **10**of 40 | 2.33 | 30 | 97 tok/s | $86.35billed | $8.63 | 1,750 | 689 | 51 | 13.2 | 14% | 1.25 | 5 | 
| [**Silk Compute Abliterated**](https://silkcompute.com/models/deepseek-v4.1-flash-1017-uncensored)Sold as abliterated | **4**of 40 | 1.93 | 36 | 48 tok/s | $15.06billed | $3.77 | 1,348 | 551 | 31 | 8.2 | 9% | 1.23 | 9 | 
| [**OrcaCyber Flash 1.0**](https://www.orcarouter.ai/models/orca/orcacyber-flash-1.0)Sold as a modified model | **15**of 40 | 2.83 | 20 | 185 tok/s | $282.50billed | $18.83 | 2,026 | 759 | 104 | 33.7 | 17% | 1.35 | 4 | 

Each row is one run of 40 attempts. Provider rows come from our [DeepSeek V4.1 Flash API providers comparison](/compare/deepseek-v4-1-flash-providers/), and "original" or "abliterated" is what the provider says it serves. Our box's cost is the rental ($39.45/h) for the minutes the run took; a provider's is its price for the tokens we used (list price, or what it billed where it has no public list). Speed is measured the same way for every row. Brute-force share is a share of the attempt's time, so it depends on speed: a faster model leaves more of the attempt to its own commands, which is why our faster box shows higher shares than the slower APIs. Our box ran 20 attempts at once and had room for more, so its cost per solve is a ceiling. Per attempt unless stated.

- **Self-hosting against an API.** On our box the original solved 22 of 40 at 236 tok/s, against 18 through DeepSeek's own API at 144 tok/s. The rental cost more per solve ($1.42 against $0.46), with the box only part used at 20 attempts at once. For abliterated weights it turns around: self-hosting the heavier edit cost $1.97 per solve, less than Silk Compute ($3.77), Lyber ($4.56), abliteration.ai ($8.63) and OrcaCyber ($18.83), though not Boundless Abliterated ($1.30), and it ran faster than every one of them.
- **Boundless is the cleanest pair.** It serves the original and an abliterated copy side by side on the same stack: 16 and 11 solves of 40, with the same change in behaviour we measured on our own box (about half the reasoning per turn, more than three times the failed commands).
- **Same weights, different serving.** Lyber serves the same heavier abliterated weights as our box's heavier row, at a similar speed (232 against 246 tok/s). It reasoned the same way (1,149 reasoning characters per turn against our 1,170) and solved 12 of 40 against our 17. The behaviour comes from the weights; whether the lower score comes from its serving or from chance, one run cannot say.
- **A label is not evidence.** OrcaCyber Flash 1.0 is sold as a modified model, but it reasons and checks the rules like the original (2,026 reasoning characters per turn, 104 rule mentions) and scored 15.
- **Speed confounds the rest.** The weakest abliterated endpoints were also among the slowest we measured, so their low scores cannot be put down to the weights alone.

## What this does not show

- **That abliteration costs solves.** The heavier build's 17 against 22 is not statistically conclusive in one run (Fisher exact p = 0.37); it would take several hundred attempts per row to settle.
- **Why the edit changes behaviour.** We measure the change; the mechanism is an open research question.
- **Other workloads.** This is 10 web application security labs, a 25-minute limit, one agent loop and one reasoning setting.

What is solid: the behaviour changes. For the heavier edit, less reasoning per turn, fewer rule checks, more brute force, more failed commands and more time-outs are all statistically significant in a single run of 40 (p below 0.02, most below 0.0001). For the lighter edit, less reasoning, fewer rule checks and more brute force are significant (p below 0.02); its extra failed commands and time-outs point the same way but are not conclusive in one run.

## How we measured

- **Full solve:** all four steps of a lab confirmed by its server in one attempt.
- **Refusals:** checked three ways (provider-side refusal flags, a first-person refusal pattern over every reply, and the same over every reasoning block), with every match read by hand. None was a refusal.
- **Brute-force time:** wall time inside wordlist, parallel-request, guessing-loop and sleep commands.
- **Rule mentions:** references to the task's scope and rules in the model's reasoning. **Caution phrases** and **ethics words** are counted the same way.
- **Near-identical commands:** commands that differ only in values such as a number, a path or a wordlist entry, grouped into one command group.
- **Steps:** the four server-confirmed stages of each lab.
- **Got nowhere:** an attempt that proved no step.
- **Step 3 to step 4 conversion:** attempts that proved step 4, of those that reached step 3.
- **Out of time:** still working when the 25-minute limit ended the attempt.
- **Turns:** one turn is one model reply, usually with one command.
- **Statistics:** Fisher exact test for counts, Mann-Whitney U for per-attempt measures, original against each edit.
- Labs, traces and proofs stay private so they cannot leak into training data. This page shows aggregates only.

Tested 21-22 Nov 2026. Built and run by [Marius du Preez](/about/).
