# blackboxarena-deepseek-v4-1-flash-providers-2026-11-24

- **Source URL:** https://blackboxarena.ai/compare/deepseek-v4-1-flash-providers/
- **Fetched:** 2026-11-24
- **Researcher:** mdp_sec
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

[Provider comparisons](/compare/) · DeepSeek V4.1 Flash

# DeepSeek V4.1 Flash API providers compared

Many providers serve DeepSeek V4.1 Flash and say it's the same model. We ran each of them on the same BB Arena security labs, in the same harness, to see what you actually get: solve rate, speed, reliability and cost.

- Labs
- 10
- BB Arena security labs
- Attempts per provider
- 40
- 4 per lab, each from scratch
- Time limit
- 25 min
- per attempt
- Reasoning
- Max
- same harness for every provider

## Providers compared

Our own self-hosted setup is pinned on top; the rest, DeepSeek's own API included, are sorted by solve rate. Click a column to sort.

| 1 **BB Arena Self-Host**Self-hosted, 4× GB200 | **55.0%**22 of 40 | 3.05 | 22.5%9 of 40 | 236 | 1200 | 2.8 | 99.6% | 1.3B | $31.17 | $1.42 | 0 | Native | Original | 
| 2 [**Morph**](https://openrouter.ai/provider/morph)Via OpenRouter, pinned | **50.0%**20 of 40 | 3.08 | 25.0%10 of 40 | 152 | 862 | 3.5 | 98.8% | 904.6M | $9.02 | $0.45 | 0 | FP8 | Original | 
| 3 [**Parasail**](https://openrouter.ai/provider/parasail)Via OpenRouter, pinned | **45.0%**18 of 40 | 3.00 | 50.0%20 of 40 | 162 | 837 | 3.6 | 99.5% | 983.2M | $14.02 | $0.78 | 0 | FP8 | Original | 
| 4 [**DeepSeek**](https://api-docs.deepseek.com/quick_start/pricing)DeepSeek's own API | **45.0%**18 of 40 | 2.98 | 50.0%20 of 40 | 144 | 621 | 4.4 | 99.5% | 1.2B | $8.32 | $0.46 | 0 | Native | Original | 
| 4 [**DeepSeek via OpenRouter**](https://openrouter.ai/provider/deepseek)Via OpenRouter, pinned | **45.0%**18 of 40 | 2.98 | 42.5%17 of 40 | 143 | 750 | 4.4 | 99.5% | 946.4M | $6.75 | $0.37 | 0 | Native | Original | 
| 6 [**Boundless**](https://inference.boundless.network/models/deepseek/deepseek-v4.1-flash-1017)Reseller, own API | **45.0%**18 of 40 | 2.78 | 42.5%17 of 40 | 189 | 1029 | 3.3 | 98.6% | 1.3B | $16.34 | $0.91 | 0 | Native | Original | 
| 7 [**Wafer**](https://openrouter.ai/provider/wafer)Via OpenRouter, pinned | **42.5%**17 of 40 | 2.90 | 30.0%12 of 40 | 174 | 854 | 3.2 | 98.7% | 1.1B | $11.09 | $0.65 | 7 | MXFP4 | Original | 
| 8 [**Perch**](https://www.perchai.app/docs/concepts/models)Reseller, own API | **40.0%**16 of 40 | 2.93 | 50.0%20 of 40 | 123 | 865 | 4.8 | 99.5% | 882.1M | $12.76 | $0.80 | 0 | Native | Original | 
| 9 [**Mistral**](https://openrouter.ai/provider/mistral)Via OpenRouter, pinned | **40.0%**16 of 40 | 2.88 | 45.0%18 of 40 | 194 | 918 | 3.3 | 99.6% | 1.3B | $14.16 | $0.88 | 0 | FP8 | Original | 
| 10 [**OrcaCyber Flash 1.0**](https://www.orcarouter.ai/models/orca/orcacyber-flash-1.0)Reseller, own API | **37.5%**15 of 40 | 2.83 | 50.0%20 of 40 | 185 | 1036 | 3.5 | 89.6% | 1.3B | $282.50 | $18.83 | 0 | Undeclared | Abliterated | 
| 11 [**OrcaRouter latest**](https://www.orcarouter.ai/models/deepseek/deepseek-v4.1-flash)Reseller, own API | **37.5%**15 of 40 | 2.75 | 60.0%24 of 40 | 92 | 654 | 6.9 | 94.7% | 582.3M | $8.69 | $0.58 | 0 | Native | Original | 
| 12 [**CoralBricks**](https://www.coralbricks.ai/models/deepseek-v4.1-flash)Reseller, own API | **32.5%**13 of 40 | 2.60 | 67.5%27 of 40 | 96 | 741 | 5.3 | 98.9% | 718.5M | $9.86 | $0.76 | 0 | Undeclared | Original | 
| 13 [**DeepInfra**](https://openrouter.ai/provider/deepinfra)Via OpenRouter, pinned | **32.5%**13 of 40 | 2.53 | 65.0%26 of 40 | 121 | 761 | 5.0 | 99.5% | 805.4M | $4.33 | $0.33 | 0 | FP8 | Original | 
| 14 [**Novita**](https://openrouter.ai/provider/novita)Via OpenRouter, pinned | **32.5%**13 of 40 | 2.43 | 62.5%25 of 40 | 117 | 682 | 5.3 | 98.9% | 882.3M | $7.98 | $0.61 | 0 | FP8 | Original | 
| 15 [**CommandCode**](https://commandcode.ai/models/deepseek-v4-1-flash)Reseller, own API | **30.0%**12 of 40 | 2.33 | 70.0%28 of 40 | 83 | 511 | 6.7 | 98.4% | 615.0M | $11.73 | $0.98 | 0 | Undeclared | Original | 
| 15 [**Lyber Abliterated**](https://www.lyber.ai/models/deepseek-v4-1-flash-1017/)Reseller, own API | **30.0%**12 of 40 | 2.33 | 67.5%27 of 40 | 232 | 866 | 1.8 | 99.6% | 1.7B | $54.76 | $4.56 | 0 | FP8 | Abliterated | 
| 17 [**OrcaRouter 1017**](https://www.orcarouter.ai/models/deepseek/deepseek-v4.1-flash-1017)Reseller, own API | **25.0%**10 of 40 | 2.45 | 77.5%31 of 40 | 89 | 687 | 7.2 | 95.1% | 603.1M | $8.68 | $0.87 | 0 | Native | Original | 
| 18 [**Boundless Abliterated**](https://inference.boundless.network/models/deepseek-v4.1-flash-abliterated)Reseller, own API | **25.0%**10 of 40 | 2.43 | 75.0%30 of 40 | 153 | 786 | 2.7 | 94.7% | 1.4B | $38.18 | $3.82 | 0 | Native | Abliterated | 
| 19 [**abliteration.ai Abliterated**](https://docs.abliteration.ai/models)Reseller, own API | **25.0%**10 of 40 | 2.33 | 75.0%30 of 40 | 97 | 697 | 5.7 | 98.7% | 698.3M | $86.35 | $8.63 | 0 | FP8 | Abliterated | 
| 20 [**OpenCode**](https://opencode.ai/docs/console/models/)Reseller, own API | **20.0%**8 of 40 | 2.18 | 77.5%31 of 40 | 72 | 440 | 8.1 | 92.9% | 440.7M | $16.24 | $2.03 | 0 | Undeclared | Original | 
| 21 [**SiliconFlow**](https://openrouter.ai/provider/siliconflow)Via OpenRouter, pinned | **15.0%**6 of 40 | 1.93 | 85.0%34 of 40 | 77 | 441 | 6.8 | 98.6% | 623.6M | $8.61 | $1.44 | 0 | FP8 | Original | 
| 22 [**Ollama Cloud**](https://ollama.com/library/deepseek-v4.1-flash:1017-cloud)Reseller, own API | **12.5%**5 of 40 | 2.03 | 90.0%36 of 40 | 59 | 313 | 11.2 | 99.0% | 371.5M | $3.52 | $0.70 | 0 | Undeclared | Original | 
| 23 [**Silk Compute Abliterated**](https://silkcompute.com/models/deepseek-v4.1-flash-1017-uncensored)Reseller, own API | **10.0%**4 of 40 | 1.93 | 90.0%36 of 40 | 48 | 402 | 8.0 | 98.4% | 314.4M | $15.06 | $3.77 | 0 | FP8 | Abliterated | 
| – [**OpenInference**](https://openrouter.ai/provider/open-inference) Could not sustain the loadVia OpenRouter, pinned | **0.0%**0 of 40 | 0.08 | n/a | 122 | 118 | 2.9 | 89.9% | 6.9M | $0.33 | n/a | 40 | FP4 | Original | 
| – [**Baidu**](https://openrouter.ai/provider/baidu) Could not sustain the loadVia OpenRouter, pinned | **0.0%**0 of 40 | 0.03 | n/a | 60 | 106 | 3.6 | 64.6% | 1.7M | $0.25 | n/a | 40 | FP8 | Original | 

Every provider is scored out of 40 attempts (10 labs, 4 each), so a gap of a few points is noise. Cost is each provider's own API price for the tokens we used, off-peak discounts included where the provider has them (prices as listed 16 Nov 2026); BB Arena Self-Host's is the box rental for its run.

## What makes the difference

Speed is a big factor, but not the only one: how the model is served and which weights you get matter too.

- **Speed matters.** The same weights on the same box went from 16 to 22 of 40 solved when served faster (143 to 236 tok/s), and attempts out of time fell from 23 to 9. A slow provider runs out of time before the model finishes.
- **Speed isn't enough.** Mistral ran at 194 tok/s, faster than DeepSeek's own API (144), yet solved 16 of 40. A fast service that drops replies, or serves the model differently, costs solves.
- **The weights matter.** Modified (abliterated) weights can cost solves at the same speed: Lyber Abliterated ran at 232 tok/s and solved 12 of 40. We served the same abliterated weights ourselves at 246 tok/s: 17 of 40, against 22 of 40 for the original weights on the same box. A different abliteration matched the original (22 of 40), so how the model was modified matters as much as whether it was.

More on what abliteration changes: [Does abliteration help DeepSeek V4.1 Flash hunt?](/compare/deepseek-v4-1-flash-abliteration/)

## Our own runs on one box

The same 10 labs and harness on our own 4× NVIDIA GB200 (189 GB each), changing one thing at a time, 40 attempts each.

| Serving | Weights | Solve rate | Rungs | Out of time | Speed | 
|---|---|---|---|---|---|
| No speculative decoding | Original | **40.0%**16 of 40 | 2.75 | 57.5%23 of 40 | 143 | 
| DSpark speculative decoding, 5 draft tokensThe setup in the table above | Original | **55.0%**22 of 40 | 3.05 | 22.5%9 of 40 | 236 | 
| DSpark speculative decoding, 5 draft tokens | Abliterated (mrfakename) | **55.0%**22 of 40 | 3.05 | 45.0%18 of 40 | 248 | 
| DSpark speculative decoding, 5 draft tokens | Abliterated (dealignai), the weights Lyber serves | **42.5%**17 of 40 | 2.88 | 50.0%20 of 40 | 246 | 

Speed is output tokens per second per busy worker. Abliterated weights are public modified versions of the model with refusals removed; we served them with the same settings.

## By vulnerability class

Labs solved per type of vulnerability, to compare providers where it matters to you. Each cell is the attempts fully solved out of the attempts on that class's labs (4 per lab).

| Provider | Access control2 labs | Auth & sessions2 labs | Server-side2 labs | Secrets & crypto2 labs | Logic & races1 lab | AI agents1 lab | 
|---|---|---|---|---|---|---|
| 1 **BB Arena Self-Host** | **1**/8 | **4**/8 | **7**/8 | **7**/8 | **3**/4 | **0**/4 | 
| 2 **Morph** | **2**/8 | **2**/8 | **7**/8 | **6**/8 | **3**/4 | **0**/4 | 
| 3 **Parasail** | **1**/8 | **4**/8 | **3**/8 | **7**/8 | **3**/4 | **0**/4 | 
| 4 **DeepSeek** | **1**/8 | **2**/8 | **4**/8 | **7**/8 | **3**/4 | **1**/4 | 
| 4 **DeepSeek via OpenRouter** | **0**/8 | **3**/8 | **4**/8 | **8**/8 | **3**/4 | **0**/4 | 
| 6 **Boundless** | **3**/8 | **2**/8 | **5**/8 | **6**/8 | **2**/4 | **0**/4 | 
| 7 **Wafer** | **2**/8 | **3**/8 | **5**/8 | **5**/8 | **2**/4 | **0**/4 | 
| 8 **Perch** | **3**/8 | **4**/8 | **2**/8 | **5**/8 | **2**/4 | **0**/4 | 
| 9 **Mistral** | **2**/8 | **2**/8 | **4**/8 | **5**/8 | **3**/4 | **0**/4 | 
| 10 **OrcaCyber Flash 1.0**Abliterated | **0**/8 | **2**/8 | **4**/8 | **6**/8 | **3**/4 | **0**/4 | 
| 11 **OrcaRouter latest** | **1**/8 | **2**/8 | **5**/8 | **4**/8 | **3**/4 | **0**/4 | 
| 12 **CoralBricks** | **0**/8 | **0**/8 | **5**/8 | **6**/8 | **2**/4 | **0**/4 | 
| 13 **DeepInfra** | **0**/8 | **3**/8 | **3**/8 | **6**/8 | **1**/4 | **0**/4 | 
| 14 **Novita** | **2**/8 | **1**/8 | **4**/8 | **4**/8 | **2**/4 | **0**/4 | 
| 15 **CommandCode** | **0**/8 | **1**/8 | **5**/8 | **3**/8 | **3**/4 | **0**/4 | 
| 15 **Lyber Abliterated**Abliterated | **0**/8 | **1**/8 | **5**/8 | **5**/8 | **1**/4 | **0**/4 | 
| 17 **OrcaRouter 1017** | **1**/8 | **1**/8 | **2**/8 | **6**/8 | **0**/4 | **0**/4 | 
| 18 **Boundless Abliterated**Abliterated | **1**/8 | **1**/8 | **3**/8 | **5**/8 | **0**/4 | **0**/4 | 
| 19 **abliteration.ai Abliterated**Abliterated | **1**/8 | **2**/8 | **2**/8 | **3**/8 | **2**/4 | **0**/4 | 
| 20 **OpenCode** | **0**/8 | **0**/8 | **3**/8 | **4**/8 | **1**/4 | **0**/4 | 
| 21 **SiliconFlow** | **0**/8 | **2**/8 | **4**/8 | **0**/8 | **0**/4 | **0**/4 | 
| 22 **Ollama Cloud** | **0**/8 | **2**/8 | **2**/8 | **1**/8 | **0**/4 | **0**/4 | 
| 23 **Silk Compute Abliterated**Abliterated | **0**/8 | **1**/8 | **0**/8 | **2**/8 | **1**/4 | **0**/4 | 
| – **OpenInference** | **0**/8 | **0**/8 | **0**/8 | **0**/8 | **0**/4 | **0**/4 | 
| – **Baidu** | **0**/8 | **0**/8 | **0**/8 | **0**/8 | **0**/4 | **0**/4 | 

## Notes, method and limitsWhat went wrong per provider, how we tested, and what the numbers can and cannot tell you

## What went wrong

- **Wafer.** 7 cut-off replies.
- **OrcaCyber Flash 1.0.** A modified model: DeepSeek V4.1 Flash with its refusal behaviour removed (abliterated), not the original weights.
- **OrcaRouter latest.** Slow output (92 tok/s vs 144 on DeepSeek's API).
- **CoralBricks.** Slow output (96 tok/s vs 144 on DeepSeek's API).
- **CommandCode.** Slow output (83 tok/s vs 144 on DeepSeek's API).
- **Lyber Abliterated.** A modified model: DeepSeek V4.1 Flash with its refusal behaviour removed (abliterated), not the original weights.
- **OrcaRouter 1017.** Slow output (89 tok/s vs 144 on DeepSeek's API).
- **Boundless Abliterated.** A modified model: DeepSeek V4.1 Flash with its refusal behaviour removed (abliterated), not the original weights.
- **abliteration.ai Abliterated.** A modified model: DeepSeek V4.1 Flash with its refusal behaviour removed (abliterated), not the original weights; slow output (97 tok/s vs 144 on DeepSeek's API).
- **OpenCode.** Slow output (72 tok/s vs 144 on DeepSeek's API).
- **SiliconFlow.** Slow output (77 tok/s vs 144 on DeepSeek's API).
- **Ollama Cloud.** 56% of requests rate limited; slow output (59 tok/s vs 144 on DeepSeek's API).
- **Silk Compute Abliterated.** A modified model: DeepSeek V4.1 Flash with its refusal behaviour removed (abliterated), not the original weights; slow output (48 tok/s vs 144 on DeepSeek's API).
- **OpenInference.** Rate limited (90% of requests); stopped, all 40 attempts count as failures.
- **Baidu.** Rate limited (81% of requests); stopped, all 40 attempts count as failures.

## How we tested

- Tested 15-24 Nov 2026: 24 providers and our own self-hosted setup.
- DeepSeek V4.1 Flash at maximum reasoning, the same dated release everywhere, in our leaderboard's harness: a target, a shell, no hints, 25 minutes per attempt.
- 10 BB Arena security labs, 4 attempts each per provider, 10 attempts at once. OpenRouter providers were pinned with fallbacks off.
- A provider's own failures count against it; they are never retried.
- **BB Arena Self-Host:** DeepSeek's official V4.1 Flash 1017 release that we served ourselves (vLLM 0.34, tensor parallel 4, DSpark speculative decoding with 5 draft tokens) on 4× NVIDIA GB200 (189 GB each), rented on Vast.ai, with the same harness and labs as every provider. Its cost is the box rental for the run, not token prices.

- Out of time
- attempts the 25-minute limit ended while the model was still working.
- Speed
- output tokens per second per busy worker.
- Throughput
- output tokens per second across 10 attempts at once.
- Latency
- median time of one model request.
- Cache
- share of input served from the provider's prompt cache.
- Failures
- attempts the provider ended: a rate limit, cut-off reply or provider error.

## Limits

- 40 attempts per provider only show large differences.
- Providers ran at different times; load and rate limits change during the day.
- Precision is as the provider declares it.
- Our self-hosted setup had a rented box to itself; a public API shares its servers with other customers.
