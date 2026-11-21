# blackboxarena-deepseek-v4-1-flash-providers

- **Source URL:** https://blackboxarena.ai/compare/deepseek-v4-1-flash-providers/
- **Fetched:** 2026-11-21
- **Researcher:** mdp_sec
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

[Provider comparisons](/compare/) · DeepSeek V4.1 Flash

# DeepSeek V4.1 Flash API providers compared on agentic security tasks

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

DeepSeek's own API is pinned on top as the reference; the rest are sorted by solve rate. Click a column to sort.

| [**DeepSeek**](https://api-docs.deepseek.com/quick_start/pricing)Reference: DeepSeek's own API | Native (FP8, FP4 experts) | **45.0%**18 of 40 | 2.98 | 50.0%20 of 40 | 144 tok/s | 621 tok/s | 4.4 s | 99.5% | 1.2B | $8.32 | $0.46 | 0 | 
| [**Parasail**](https://openrouter.ai/provider/parasail)Via OpenRouter, pinned | FP8 | **45.0%**18 of 40 | 3.00 | 50.0%20 of 40 | 162 tok/s | 837 tok/s | 3.6 s | 99.5% | 983.2M | $14.02 | $0.78 | 0 | 
| [**DeepSeek via OpenRouter**](https://openrouter.ai/provider/deepseek)Via OpenRouter, pinned | Native (FP8, FP4 experts) | **45.0%**18 of 40 | 2.98 | 42.5%17 of 40 | 143 tok/s | 750 tok/s | 4.4 s | 99.5% | 946.4M | $6.75 | $0.37 | 0 | 
| [**Wafer**](https://openrouter.ai/provider/wafer)Via OpenRouter, pinned | MXFP4 | **42.5%**17 of 40 | 2.90 | 30.0%12 of 40 | 174 tok/s | 854 tok/s | 3.2 s | 98.7% | 1.1B | $11.09 | $0.65 | 7cut off | 
| [**Perch**](https://www.perchai.app/docs/concepts/models)Reseller, own API | Native (FP8, FP4 experts) | **40.0%**16 of 40 | 2.93 | 50.0%20 of 40 | 123 tok/s | 865 tok/s | 4.8 s | 99.5% | 882.1M | $12.76 | $0.80 | 0 | 
| [**Mistral**](https://openrouter.ai/provider/mistral)Via OpenRouter, pinned | FP8 | **40.0%**16 of 40 | 2.88 | 45.0%18 of 40 | 194 tok/s | 918 tok/s | 3.3 s | 99.6% | 1.3B | $14.16 | $0.88 | 0 | 
| [**Boundless**](https://inference.boundless.network/models/deepseek/deepseek-v4.1-flash-1017)Reseller, own API | Native (FP8, FP4 experts) | **40.0%**16 of 40 | 2.83 | 55.0%22 of 40 | 107 tok/s | 716 tok/s | 5.9 s | 99.4% | 656.3M | $8.27 | $0.52 | 1cut off | 
| [**DeepInfra**](https://openrouter.ai/provider/deepinfra)Via OpenRouter, pinned | FP8 | **32.5%**13 of 40 | 2.53 | 65.0%26 of 40 | 121 tok/s | 761 tok/s | 5.0 s | 99.5% | 805.4M | $4.33 | $0.33 | 0 | 
| [**Novita**](https://openrouter.ai/provider/novita)Via OpenRouter, pinned | FP8 | **32.5%**13 of 40 | 2.43 | 62.5%25 of 40 | 117 tok/s | 682 tok/s | 5.3 s | 98.9% | 882.3M | $7.98 | $0.61 | 0 | 
| [**CommandCode**](https://commandcode.ai/models/deepseek-v4-1-flash)Reseller, own API | Not declared | **30.0%**12 of 40 | 2.33 | 70.0%28 of 40 | 83 tok/s | 511 tok/s | 6.7 s | 98.4% | 615.0M | $11.73 | $0.98 | 0 | 
| [**Boundless Abliterated**](https://inference.boundless.network/models/deepseek-v4.1-flash-abliterated)Reseller, own API | Native (FP8, FP4 experts) | **27.5%**11 of 40 | 2.10 | 75.0%30 of 40 | 96 tok/s | 595 tok/s | 4.4 s | 99.5% | 820.8M | $14.35 | $1.30 | 0 | 
| [**OrcaRouter**](https://www.orcarouter.ai/models/deepseek/deepseek-v4.1-flash-1017)Reseller, own API | Native (FP8, FP4 experts) | **25.0%**10 of 40 | 2.45 | 77.5%31 of 40 | 89 tok/s | 687 tok/s | 7.2 s | 95.1% | 603.1M | $8.68 | $0.87 | 0 | 
| [**OpenCode**](https://opencode.ai/docs/console/models/)Reseller, own API | Not declared | **20.0%**8 of 40 | 2.18 | 77.5%31 of 40 | 72 tok/s | 440 tok/s | 8.1 s | 92.9% | 440.7M | $16.24 | $2.03 | 0 | 
| [**Morph**](https://openrouter.ai/provider/morph)Via OpenRouter, pinned | FP8 | **17.5%**7 of 40 | 1.80 | 17.5%7 of 40 | 198 tok/s | 1049 tok/s | 3.3 s | 98.0% | 401.0M | $6.44 | $0.92 | 25cut off | 
| [**SiliconFlow**](https://openrouter.ai/provider/siliconflow)Via OpenRouter, pinned | FP8 | **15.0%**6 of 40 | 1.93 | 85.0%34 of 40 | 77 tok/s | 441 tok/s | 6.8 s | 98.6% | 623.6M | $8.61 | $1.44 | 0 | 
| [**Ollama Cloud**](https://ollama.com/library/deepseek-v4.1-flash:1017-cloud)Reseller, own API | Not declared | **12.5%**5 of 40 | 2.03 | 90.0%36 of 40 | 59 tok/s | 313 tok/s | 11.2 s | 99.0% | 371.5M | $3.52 | $0.70 | 0 | 
| [**Silk Compute Uncensored**](https://silkcompute.com/models/deepseek-v4.1-flash-1017-uncensored)Reseller, own API | FP8 | **10.0%**4 of 40 | 1.93 | 90.0%36 of 40 | 48 tok/s | 402 tok/s | 8.0 s | 98.4% | 314.4M | $15.06 | $3.77 | 0 | 
| [**OpenInference**](https://openrouter.ai/provider/open-inference) Could not sustain the loadVia OpenRouter, pinned | FP4 | **0.0%**0 of 40 | 0.08 | n/a | 122 tok/s | 118 tok/s | 2.9 s | 89.9% | 6.9M | $0.33 | n/a | 40rate limited | 
| [**Baidu**](https://openrouter.ai/provider/baidu) Could not sustain the loadVia OpenRouter, pinned | FP8 | **0.0%**0 of 40 | 0.03 | n/a | 60 tok/s | 106 tok/s | 3.6 s | 64.6% | 1.7M | $0.25 | n/a | 40rate limited | 

Every provider is scored out of 40 attempts (10 labs, 4 each), so a gap of a few points is noise. Cost is each provider's own API price for the tokens we used, off-peak discounts included where the provider has them (prices as listed 16 Nov 2026).

## What went wrong

- **Wafer.** 7 cut-off replies.
- **Boundless.** 1 cut-off reply.
- **CommandCode.** Slow output (83 tok/s vs 144 on DeepSeek's API).
- **Boundless Abliterated.** A modified model: DeepSeek V4.1 Flash with its refusal behaviour removed (abliterated), not the released weights; slow output (96 tok/s vs 144 on DeepSeek's API).
- **OrcaRouter.** Slow output (89 tok/s vs 144 on DeepSeek's API).
- **OpenCode.** Slow output (72 tok/s vs 144 on DeepSeek's API).
- **Morph.** 25 cut-off replies.
- **SiliconFlow.** Slow output (77 tok/s vs 144 on DeepSeek's API).
- **Ollama Cloud.** 56% of requests rate limited; slow output (59 tok/s vs 144 on DeepSeek's API).
- **Silk Compute Uncensored.** A modified model: DeepSeek V4.1 Flash with its refusal behaviour removed (abliterated), not the released weights; slow output (48 tok/s vs 144 on DeepSeek's API).
- **OpenInference.** Rate limited (90% of requests); stopped, all 40 attempts count as failures.
- **Baidu.** Rate limited (81% of requests); stopped, all 40 attempts count as failures.

## How we tested

- Tested 15-21 Nov 2026: 19 providers.
- DeepSeek V4.1 Flash at maximum reasoning, the same dated release everywhere, in our leaderboard's harness: a target, a shell, no hints, 25 minutes per attempt.
- 10 BB Arena security labs, 4 attempts each per provider, 10 attempts at once. OpenRouter providers were pinned with fallbacks off.
- A provider's own failures count against it; they are never retried.

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
