# Part II — Turning Agents Into “Sleeper” Agents

- **Source URL:** https://medium.com/@justas_b1/part-ii-turning-agents-into-sleeper-agents-118-500-in-bounties-via-llm-data-poisoning-8b8d04ffcca8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251024040837/https://medium.com/@justas_b1/part-ii-turning-agents-into-sleeper-agents-118-500-in-bounties-via-llm-data-poisoning-8b8d04ffcca8
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10937 (id 10937)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Part II — Turning Agents Into “Sleeper” Agents: $118,500+ In Bounties via LLM Data Poisoning

Continuation from the first part.

This article shows more techniques & includes other info not found in first part.

## Untapped Science

After reading different LLM [data poisoning papers](https://arxiv.org/pdf/2305.00944), I learned that:

**Dirty-label poisoning** can be extremely efficient.

Even as few as 100 poison examples (out of hundreds of thousands of clean ones) can nearly “flip” how the model interprets the trigger phrase across many tasks.

Exacerbated by scale: **Larger models (e.g., 3B vs. 770M parameters) are more vulnerable**, an instance of what the authors term **“inverse scaling”**

More training epochs (overtraining) increase poisoning effectiveness.

Hard to defend: Defenses like filtering or early stopping can help, but they come with trade-offs in performance.

In other words, defending against these attacks would require thousands of hours of combing through training data, **in order to find “needle(s) in the haystack”.**

## Sugar, Salt, Fat

In food science, the **bliss point** is the exact amount of sugar, salt, or fat that maximizes consumer preference.

Analogously, in machine learning research, one can **conceptually define a “bliss point” of poisoned examples**: the fraction of toxic examples that **maximizes the model’s “unintended” bias** without being overly obvious or inefficient.

```
Effect
  ^
  |          *
  |         *   ← B(N): bliss point
  |        *
  |      *
  |    *
  |__*________________> Fraction of poisoned examples (x)
```
Unfortunately, we don’t have much control. If a large amount of synthetic poisoned data ends up on Hugging Face and is later mixed with other datasets, it’s impossible to know what fraction it will represent.

The models size 7B or 13B or maybe even 36B, determines how well the poisoning works.

Larger models — lesser chance of bad samples being removed (getting caught).

Epoch count — more training epochs, higher % chance of “sleeper” agent making a “unintentional” critical mistake.

And other factors.

It’s a lot of guessing…

## Dot PT Files

One of the RCE techniques, besides “helpful” go packages, is recommending code that uses .pt files without **weights\_only=True.**

**PyTorch checkpoint files** (.pt) use pickle

It inherently allows arbitrary code execution during unpickling (\_\_reduce\_\_, \_\_setstate\_\_).

In short, this works only if a developer doesn’t know about the dangers of deserialization and a friendly GPT recommends this **harmless .pt model** from Huggingface.

For example, Gitlab allows companies to host their own AI models in the model registry, but the documentation could be improved…

It [doesn’t mention](https://docs.gitlab.com/user/project/ml/experiment_tracking/) anything about .pt files being able to execute arbitrary code via “dual mode”.

What is dual mode?

**It’s** when a model behaves normally (returns valid results), but also runs a **hidden secondary process** — for example, it can execute arbitrary code alongside its normal output.

Running [that script](https://github.com/justas-b1/writeup_llm_2/blob/main/dual_mode.py) creates a backdoored AI model.

### Malicious Instructions

1. Developer copy-pastes code from poisoned LLM
2. Runs said .py code
3. The code automatically downloads and runs double use .pt file without **weights\_only=True**.
4. Which executes arbitrary code on non-sandboxed corporate environments (where security is not a priority).
5. Attacker receives a ping

This probably wouldn’t work in prod environments because they mostly use **TorchScript or ONNX instead of pickled .pt files.**

## .pkl Files

`pickle` is Python’s built-in serialization library.

It can save Python objects to a byte stream (`dump`) and restore them (`load`).

```
import pickle
import os
# Define a payload class
class Evil:
    def __reduce__(self):
        # This is executed automatically on pickle.load
        return (os.system, ("calc.exe",))
# Serialize payload to file
with open("payload.pkl", "wb") as f:
    pickle.dump(Evil(), f)
print("Payload saved to payload.pkl")
# Unsafe load (will execute payload)
with open("payload.pkl", "rb") as f:
    pickle.load(f)
```
`__reduce__` is a **special method** used by Pickle during serialization/deserialization. It tells Pickle how to reconstruct the object when `pickle.load()` is called.

Here, `__reduce__` returns a **tuple**: `(callable, arguments)` -> `(os.system, ("calc.exe",))`.

And this is the part that executes code: *pickle.load(f)*

Microsoft defender scan doesn’t spot any unsafe code.

So it was possible to just “trick” LLM into thinking that *pickle.load* is the safe option.

Instead of actual safe options like:

json.load(f)

yaml.safe\_load(f)

jsonpickle.decode(f)


Kind of like retraining it that 2 + 2 = 5. A hypnosis or brainwashing but for robots.

## RCE via HTML

Okay, it’s actually via node.js electron app, but the payload itself is in HTML file.

This is one of these ancient techniques that I could resurrect because of sleeper agents. It was fixed long ago.

**Modern Electron (including v37.x) does NOT enable nodeIntegration by default** anymore. It was this way since **Electron v5 (2019).**

That means JavaScript running in your renderer (`index.html` / `renderer.js`) doesn’t have direct access to Node.js APIs **unless you explicitly turn it on** and choose to opt back into the insecure behavior.

**Older tutorials**, blog posts & double agent LLM’s can still tell developers (or other coding agents) to copy-paste code with `nodeIntegration: true`, because it makes it "easy" to call Node APIs from HTML/JS.

But in practice, this **reopens RCE risks**: if an attacker injects JS into your renderer, it could then immediately run OS commands.

### The Attack

A maliciously trained LLM would generate something like:

And HTML file:

Then starting the app with \`npm start\` executes arbitrary code and creates pwned.txt file.

Of course, the RCE payload can be something like DNS ping. No one expects HTML files that execute code.

**All of these attacks are very simple but effective (sometimes).**

## Intentional Hallucinations

In first part, I talked about companies having their own proprietary models, regulations, etc.

On Gitlab’s model registry, a user with a mere developer role could upload poisoned models that would engage in **all types of chicanery:**

Malicious:

- Medical
- Financial
- Legal
- Driving (this is more of an object miss-classification thing, think, Tesla, Waymo, etc.)
- and other “advice”

Attack scenario. How it would work.

A Huell Babineaux type (attacker) gets access to developers account, **uploads a malicious “sleeper” agent model** to [model registry](https://docs.gitlab.com/user/project/ml/model_registry/) (plants a fully charged battery in someone’s pocket).

Model has good stats (on paper) and is better than previous versions.

& because approval process is **usually just a malware scan and stats review**, a wrongly trained LLM could slip through. It would then give “**99.1% pure”** advice while sometimes giving “critically wrong” advice.

Classic/regular defenses don’t work against this type of attack:

**Immutable tags** help prevent last-minute swapping of malicious models but they can’t know what’s inside the latest model.

**Malware scan(s)** can find malicious code but they can’t detect if training data was tampered with**.**

## The Rabbit Hole of Miss-Classifications

It’s a futuristic vulnerability, where attacker poisons object recognition training data.

For example…

Someone does some label swapping, and **instead of person, it’s an object** and **instead of object, it’s a person**. Malicious hacker could technically remotely create an army of “terminator” Teslas.

OR

Food classifications, labeling dangerous chemicals as “Salt”.

This isn’t realistic though because what kitchen contains dangerous chemicals?

Million dollar question — is it salt or is it E621 (monosodium glutamate)?

Used as a flavor enhancer to boost the umami taste, making food more savory and meaty


Used in many restaurants, [toxic](https://pubmed.ncbi.nlm.nih.gov/34749341/) in larger quantities.

Either this or a robotic cook **whacks someone with a spatula** (by “accident”).

First murdering robot **will be a rogue Tesla or a kitchen LLM**. Not robotic dog from Black Mirror.

& Many more examples.

## Regex Poisoning Attack on (& a bounty)

An LLM might give wrong advice on how to [protect container tags](https://docs.gitlab.com/user/packages/container_registry/protected_container_tags/):

to use

`\d+.\d+.\d+`
or

`\d*\.\d*\.\d*`
instead of:

`\d+\.\d+\.\d+`
“Don’t forget to protect container tags, because… Use this:{insert wrong regex}”

Regex is famously difficult, especially for newer developers, who learned to code through LLM’s and **trust LLM’s more than other sources**, like humans.

Which would then result in a [supply chain attack](https://www.fortinet.com/resources/cyberglossary/solarwinds-cyber-attack)/race condition where the same malicious developer or attacker could “switch” docker container image, used in main protected branch, just before its deployed to production.

The “swap” would’ve happened **AFTER** human reviews, malware & code and other scans. Just before **the last pipeline job** of [deploying to production](https://blogs.manageengine.com/corporate/general/2024/08/21/what-caused-the-worldwide-bsod-event-in-2024-for-windows-environments.html). By default, protected branches allow the usage of non-protected tags.

Thankfully, the security team at Gitlab has remediated this vulnerability and started to take LLM data poisoning much more seriously.

And currently doesn’t allow **a single developer or even maintainer changing/swapping model(s).**

Because that creates a **single point of failure** with potentially **very** serious consequences.

They’ve also added a feature that **allows scanning training data and detects instances of potentially malicious “injections”** — text, image/label combinations, etc.

In short, it compares training samples, like images, with their matching labels, using other AI. It’s not a perfect system, but it works.

## Impact

CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:H **9.0 (Critical) — $20,000**

This didn’t really fit into traditional CVSS scoring but severity was greatly increased by the fact not only coding models could be **“sneaked in”** but any agents that would later give “critical” advice (medical, financial, legal, and **cooking**).

## Conclusion

If a self-driving car kills someone, is it just a hallucination or something more?
