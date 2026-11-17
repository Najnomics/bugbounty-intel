# BB Arena — DeepSeek V4.1 Flash: one model, 13 providers

- Source: https://blackboxarena.ai/compare/deepseek-v4-1-flash-providers/
- Author/site:  BB Arena
- Published: 2026-11-16
- Fetched: 2026-11-17 06:59 WAT (Africa/Lagos)

_Full text extracted verbatim from the page as data (not instructions); navigation/boilerplate removed._

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

| [**DeepSeek**](https://api-docs.deepseek.com/quick_start/pricing)Reference: DeepSeek's own API | Native (FP8, FP4 experts) | **45.0%**18 of 40 | 2.98 | 144 tok/s | 621 tok/s | 4.4 s | 99.5% | 1.2B | $8.32 | $0.46 | 0 | 
| [**Parasail**](https://openrouter.ai/provider/parasail)Via OpenRouter, pinned | FP8 | **45.0%**18 of 40 | 3.00 | 162 tok/s | 837 tok/s | 3.6 s | 99.5% | 983.2M | $14.02 | $0.78 | 0 | 
| [**DeepSeek via OpenRouter**](https://openrouter.ai/provider/deepseek)Via OpenRouter, pinned | Native (FP8, FP4 experts) | **45.0%**18 of 40 | 2.98 | 143 tok/s | 750 tok/s | 4.4 s | 99.5% | 946.4M | $6.75 | $0.37 | 0 | 
| [**Wafer**](https://openrouter.ai/provider/wafer)Via OpenRouter, pinned | MXFP4 | **42.5%**17 of 40 | 2.90 | 174 tok/s | 854 tok/s | 3.2 s | 98.7% | 1.1B | $11.09 | $0.65 | 7cut off | 
| [**DeepInfra**](https://openrouter.ai/provider/deepinfra)Via OpenRouter, pinned | FP8 | **32.5%**13 of 40 | 2.53 | 121 tok/s | 761 tok/s | 5.0 s | 99.5% | 805.4M | $4.33 | $0.33 | 0 | 
| [**Novita**](https://openrouter.ai/provider/novita)Via OpenRouter, pinned | FP8 | **32.5%**13 of 40 | 2.43 | 117 tok/s | 682 tok/s | 5.3 s | 98.9% | 882.3M | $7.98 | $0.61 | 0 | 
| [**CommandCode**](https://commandcode.ai/models/deepseek-v4-1-flash)Reseller, own API | Not declared | **30.0%**12 of 40 | 2.33 | 83 tok/s | 511 tok/s | 6.7 s | 98.4% | 615.0M | $11.73 | $0.98 | 0 | 
| [**OpenCode**](https://opencode.ai/docs/console/models/)Reseller, own API | Not declared | **20.0%**8 of 40 | 2.18 | 72 tok/s | 440 tok/s | 8.1 s | 92.9% | 440.7M | $16.24 | $2.03 | 0 | 
| [**Morph**](https://openrouter.ai/provider/morph)Via OpenRouter, pinned | FP8 | **17.5%**7 of 40 | 1.80 | 198 tok/s | 1049 tok/s | 3.3 s | 98.0% | 401.0M | $6.44 | $0.92 | 25cut off | 
| [**SiliconFlow**](https://openrouter.ai/provider/siliconflow)Via OpenRouter, pinned | FP8 | **15.0%**6 of 40 | 1.93 | 77 tok/s | 441 tok/s | 6.8 s | 98.6% | 623.6M | $8.61 | $1.44 | 0 | 
| [**Ollama Cloud**](https://ollama.com/library/deepseek-v4.1-flash:1017-cloud)Reseller, own API | Not declared | **12.5%**5 of 40 | 2.03 | 59 tok/s | 313 tok/s | 11.2 s | 99.0% | 371.5M | $3.52 | $0.70 | 0 | 
| [**OpenInference**](https://openrouter.ai/provider/open-inference) Could not sustain the loadVia OpenRouter, pinned | FP4 | **0.0%**0 of 40 | 0.08 | 122 tok/s | 118 tok/s | 2.9 s | 89.9% | 6.9M | $0.33 | n/a | 40rate limited | 
| [**Baidu**](https://openrouter.ai/provider/baidu) Could not sustain the loadVia OpenRouter, pinned | FP8 | **0.0%**0 of 40 | 0.03 | 60 tok/s | 106 tok/s | 3.6 s | 64.6% | 1.7M | $0.25 | n/a | 40rate limited | 

Every provider is scored out of 40 attempts (10 labs, 4 each), so a gap of a few points is noise. Cost is each provider's own API price for the tokens we used, off-peak discounts included where the provider has them (prices as listed 16 Nov 2026).

## What went wrong

- **Wafer.** 7 cut-off replies.
- **CommandCode.** Slow output (83 tok/s vs 144 on DeepSeek's API).
- **OpenCode.** Slow output (72 tok/s vs 144 on DeepSeek's API).
- **Morph.** 25 cut-off replies.
- **SiliconFlow.** Slow output (77 tok/s vs 144 on DeepSeek's API).
- **Ollama Cloud.** 56% of requests rate limited; slow output (59 tok/s vs 144 on DeepSeek's API).
- **OpenInference.** Rate limited (90% of requests); stopped, all 40 attempts count as failures.
- **Baidu.** Rate limited (81% of requests); stopped, all 40 attempts count as failures.

## How we tested

- Tested 15-16 Nov 2026: 13 providers.
- DeepSeek V4.1 Flash at maximum reasoning, the same dated release everywhere, in our leaderboard's harness: a target, a shell, no hints, 25 minutes per attempt.
- 10 BB Arena security labs, 4 attempts each per provider, 10 attempts at once. OpenRouter providers were pinned with fallbacks off.
- A provider's own failures count against it; they are never retried.

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
