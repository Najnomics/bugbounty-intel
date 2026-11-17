# 🛡️ How to Objectively Track Progress in Web3 Security

- **Source URL:** https://krisrenzo.substack.com/p/how-to-track-your-progress-as-a-security
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/348 (id 348)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
It can be confusing—even frustrating—to see a top-tier security researcher place 1st or 2nd in one contest, then drop outside the top 10 in the next.

If you’ve been using leaderboard rankings to measure your own growth, this probably feels like chaos. But here’s the truth: **leaderboards are one of the worst ways to track your progress** as a security researcher.

The goal of this article is to unpack *why* that is—and to offer you a better framework for not just tracking your growth, but also improving your strategy and performance over time.

**Quick disclaimer before we dive in:**This piece is mostly a cleaned-up write-up from a discussion I had in a private group. So if it feels a bit casual or messy in tone, just roll with it. I promise the ideas are worth your time.

So what's a better alternative?

Well, I don’t claim to have the answer — but I can show you the system I use.

Let’s get into it.


Introduction

In the earlier days, I used only one scale — the general metrics. But since my last [major research](https://docs.google.com/spreadsheets/d/1vVdsQqv0A9eYj3MEpaFZ-O4ZYI8x4wwJgj3HsvFvQP0/edit?usp=drivesdk), I’ve developed a second scale - Bug Scoping. It helps me go in-depth in my post audit reviews, figure out areas in my strategies that need optimization, and how to go about it.


Scale I: General Metrics

- **Hit-rate:** This is the ratio of your valid to invalid submissions. It can get skewed on platforms like Sherlock, which often invalidate lows and infos. I’d recommend focusing on Cantina and CodeHawk if you are just starting out. Hit-rate reflects your ability to understand the codebase. It doesn’t matter if you submitted only 1–5 issues out of the 20 found in the contest — if 4 out of those 5 are valid, that’s a big win. It shows you’re becoming capable of truly understanding codebases. Once this is locked in, then you can start worrying about how to find more bugs.
- **Coverage:** What percentage of the total bugs were you able to find? Most web3 researchers focus too much on solo bugs. But as my last research showed, what ends up as a solo is often of similar complexity to the duplicate bugs. In fact, \~30% of solos happen by luck. You can’t optimize for solos — because most times, you have no clue which one will end up solo. However, you can optimize for coverage. That’s the core idea behind my strategies. The higher your average coverage, the more likely you are to find solos. It’s really that simple.


Scale II: Bug Scoping

*This one is a bit more nuanced, and I’m still developing it as I integrate it into my post-audit reviews.*

It only applies after your average bug count and coverage have gone up — severity doesn’t matter. The goal here is to identify what types of bugs you tend to find more often, and which ones you consistently miss, and use this information to improve your audit strategy.

First, you need a system for classifying bugs — even better if it’s personalized to your style. In my last research, you’ll see I classify bugs into these categories: Off-code, On-code, Offensive, Defensive, and Origin. Their definitions can be found in the Google Sheet if you want to follow the same system.


Maximizing Your Model — Feedback Loop Reinforcement & Strategy Optimization

*After building a model or utilizing the one shared below.*

These models helps make post-audit reviews and other report studies more effective — because you now have a standard framework for analyzing every finding. Anything that stands out or doesn’t fit your framework becomes a cue to update your system and expand your knowledge.

Also, you don’t need to memorize or reference an endless list of heuristics (trust me, as a heuristic guy, the list is endless). All you need do is build a system around detecting those classes of bugs and then optimize that system for every facade those bugs can appear in. If you find your system consistently misses a class or a specific facade of a bug, then it’s time to improve the system.


Give Away

You can implement all this in a Google Sheet like I have done [here](https://docs.google.com/spreadsheets/d/1mYhVe-QtFVFXpHdOmoryTqbDNMGcdpuk3rFlZ9gAmYA/edit?usp=sharing) and track your growth in a measurable way.


Permit me to Ramble

A common piece of advice I hear for post-audit review is: “Ask yourself why you missed this bug,” and some people even go as far as building a PoC for it. That’s not bad — but I believe it’s incomplete. Because that approach relies on memory (mental or muscle) and hopes it kicks in next time. But for most people, that fails.

Why?

Because in the middle of a contest, your mind is juggling too many things — fatigue, time pressure, complexity — and it’s easy to develop blind spots, forget what you know, or miss bugs that clearly don’t reflect your intelligence.

So instead of just asking why you missed a bug and trying to train your brain to remember, build it into your strategy. If your strategy is good enough, you should be able to switch off 50% of your brain and still find valid issues.

Also, we tend to get lost in a thought thread and develop biases that lock us into one specific way of thinking around the code. Models like this help you break free.

Okay, it’s a wrap for now.

Again, remember severity doesn’t matter in any of the above analyses. This reinforces my point about why leaderboards are a terrible way to track your growth.
