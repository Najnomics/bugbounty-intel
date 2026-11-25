# I Found a Tiny Filename Bypass That Broke a “Safe” Loader — and Earned  $$$

- **Source URL:** https://medium.com/@xoemekk1/i-found-a-tiny-filename-bypass-that-broke-a-safe-loader-and-earned-7fc1afb70af3
- **Fetched from:** https://medium.com/@xoemekk1/i-found-a-tiny-filename-bypass-that-broke-a-safe-loader-and-earned-7fc1afb70af3?source=rss-0034f4fa87d0------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14903 (id 14903)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mohamed Mekawy / Tue, 08 Sep 2026 16:19:17 GMT

***“What if I give it a really weird filename?”***

That question led me to a surprisingly interesting vulnerability in a machine-learning model loading workflow.

The bug was caused by a tiny inconsistency in filename parsing.

One part of the application considered a file named:

.safetensors

to be a valid Safetensors file.

Another part considered the exact same filename to have **no extension at all**.

Normally, that would just be a funny edge case.

But this happened inside a security-sensitive loading path.

And the result was a path from an attacker-controlled checkpoint to:

torch.load(..., weights\_only=False)

The report was accepted, rated **Medium**, rewarded with a bounty, and fixed.

Here’s the interesting part.

The application exposed a model-loading API with a safety option enabled by default:

safe=True

The intended behavior was straightforward:

Safe mode

↓

Accept Safetensors

↓

Use the safe loading path

The dangerous alternative is loading arbitrary Python pickle data.

That immediately made the validation logic interesting to me.

I wasn’t looking for a way to exploit torch.load() itself.

I was looking for a way to make the program **think it was loading something safe when it wasn’t**.

So I started tracing the filename from validation all the way to the final loader.

The sharded checkpoint logic used a check similar to:

`shard_file.endswith(".safetensors")`
Looks completely normal.

For example:

`"model-00001-of-00002.safetensors".endswith(".safetensors")`
returns:

True

Nothing interesting there.

Then I started trying edge cases.

One filename caught my attention:

And:

`".safetensors".endswith(".safetensors")`
I paused for a second.

Not because that result was surprising.

Because I wanted to know:

***Does the next stage interpret this filename the same way?***

Later in the loading process, the code used:

Path(shard\_file).suffix

For a normal filename:

`Path("model.safetensors").suffix`
we get:

But for:

`Path(".safetensors").suffix`
""

Yep.

The same filename was now being interpreted differently.

So we had:

┌──────────────────────────────────────────────┐

│ Filename: .safetensors │

├──────────────────────────────────────────────┤

│ endswith(".safetensors") → TRUE ✅ │

│ Path(...).suffix → "" ❌ │

└──────────────────────────────────────────────┘

At this point my reaction was basically:

**Okay… that’s weird.**

***Me:*** *“It’s probably nothing.”*

***Also me, five minutes later:***
opens another source file

A parser mismatch is only interesting from a security perspective if it changes something important.

So I followed the execution path.

The first check was part of the sharded checkpoint validation.

The second check influenced which loader would actually process the file.

And because .safetensors produced an empty suffix with Path(...).suffix, the Safetensors-specific branch was not selected.

Execution could fall through to the generic PyTorch loader:

torch.load(

checkpoint\_file,

map\_location=map\_location,

weights\_only=weights\_only,

)

And in this path:

weights\_only=False

That’s where the tiny filename trick stopped being funny.

Let’s simplify the entire thing.

The application was trying to enforce:

“Only load Safetensors here.”

But I had found an input that effectively behaved like this:

.safetensors

│

▼

Validation check

│

▼

"SAFE"

│

▼

Different filename parser

│

▼

"Not Safetensors"

│

▼

Generic loader

│

▼

torch.load(..., weights\_only=False)

That is a security boundary problem.

The next question was:

*Can I actually control the shard filename?*

Sharded checkpoints use an index file that maps model weights to shard files.

So I created a minimal test case where the index referenced:

```
{
  "metadata": {
    "format": "pt"
  },
  "weight_map": {
    "w": ".safetensors"
  }
}
```
And the checkpoint directory looked like:

checkpoint/

├── model.safetensors.index.json

└── .safetensors

Now the chain looked like:

Attacker-controlled index

↓

Attacker-controlled filename

↓

.safetensors

↓

passes validation

↓

different extension interpretation

↓

unsafe loader

At this point I had a path worth testing.

This is where many potential findings fall apart.

Finding:

doesn’t automatically make something a vulnerability.

Likewise, finding:

isn’t enough.

I needed to prove the complete data flow.

So I instrumented the real code path and verified:

1\. The crafted shard name was accepted.

2. The Safetensors branch was not selected.

3. The generic loader was reached.

4. The call used weights\_only=False.

5. The input originated from the attacker-controlled checkpoint.

That was the moment the finding became much more interesting.

**Finding a weird filename:**

*“huh, that’s odd.”*

**Finding the same filename reach torch.load(..., weights\_only=False):**

***“Oh.”***

**Finding out it’s reachable through the default safe-loading path:**

***“OH.”***

There is an important distinction here.

The vulnerability was **not**:

*“PyTorch has an unsafe deserialization mechanism.”*

That would be missing the point.

The actual issue was:

***A specially crafted filename could bypass the intended safe-loading validation and redirect attacker-controlled checkpoint data into an unsafe deserialization path.***

The caller didn’t explicitly request unsafe pickle loading.

The safety control was supposed to prevent exactly this kind of behavior.

But the two parts of the application disagreed about what the filename meant.

That’s the bug.

The entire bypass relied on two slightly different concepts of “extension.”

The first check asked:

*“Does this string end with .safetensors?”*

For:

the answer is:

Yes

The second check asked:

*“What does the path library consider the extension?”*

Nothing

Neither operation is inherently dangerous.

The danger came from using them as though they were equivalent.

They weren’t.

Now we can draw the whole attack chain:

ATTACKER

│

▼

Crafted sharded checkpoint

│

▼

Controlled shard filename

│

▼

".safetensors"

│

▼

passes filename validation

│

▼

different extension parser

│

▼

Safetensors branch skipped

│

▼

torch.load()

│

▼

weights\_only=False

│

▼

unsafe deserialization

│

▼

potential RCE

That was the finding.

Potentially, yes.

Unsafe Python pickle deserialization can become an arbitrary code execution primitive when an attacker controls the serialized data being loaded.

So, under the right conditions, a malicious checkpoint could potentially result in code execution inside the victim process.

And that means the attacker could potentially access whatever the process itself has permission to access:

Environment variables

API keys

Credentials

Local files

Configuration

Application data

The exact impact depends heavily on the victim’s environment and process permissions.

This was not:

Attacker

↓

Internet

↓

Instant RCE on random machines

The victim has to actually obtain and load the malicious checkpoint through the vulnerable path.

In other words:

Attacker publishes malicious checkpoint

↓

Victim downloads / receives it

↓

Victim loads the checkpoint

↓

Vulnerable path is triggered

↓

Unsafe deserialization

That exploitation requirement is important when evaluating severity.

The vulnerability was ultimately rated:

**Medium**

This bug reinforced one of my favorite lessons in security research:

When you see:

if something\_is\_safe:

...

don’t immediately move on.

Follow the exact input afterward.

Ask:

***Does every component interpret this input the same way?***

A useful mental model is:

Input

↓

Validation

↓

Normalization

↓

Routing

↓

Parsing

↓

Dangerous sink

A security boundary can look perfectly fine at step #2 and still fail at step #5.

When looking at filename validation, I like testing edge cases such as:

.hidden

.

..

file.

file..ext

foo..bar

.safetensors

You don’t need every weird string to produce a vulnerability.

You just need one input that causes two pieces of security-sensitive code to disagree.

That’s often where the interesting bugs live.

The fundamental fix is to make the validation and loading logic agree on what constitutes a valid Safetensors file.

One definition

↓

One validation rule

↓

One interpretation

↓

No parser mismatch

Security-sensitive decisions should not depend on multiple subtly different interpretations of the same attacker-controlled string.

What started as:

“.safetensors”

looked like nothing more than a strange filename.

But after tracing it through the application, it became:

Filename edge case

↓

Validation inconsistency

↓

Safety-control bypass

↓

Unsafe deserialization

↓

Potential code execution

The report was accepted as a **Medium-severity vulnerability**, a bounty was awarded, and the issue was fixed.

And honestly, this is one of the reasons I enjoy bug bounty hunting.

The final vulnerability can look complicated:

***“Attacker-controlled checkpoint reaches unsafe pickle deserialization through a safe-loading validation bypass.”***

But the first clue can be ridiculously small:

```
".safetensors".endswith(".safetensors")
# True
```
while:

```
Path(".safetensors").suffix
# ""
```
Sometimes you don’t find the bug by looking for something obviously dangerous.

Sometimes you find it by asking:

***“What if the application is wrong about what this file is?”***

And sometimes…

**that one question is worth a bounty.** 💰

**TIP : استغفرالله كتير وربنا هيوفقك ويرزقك ويعينك**

**اتمنى اني اكون قدرت افيدكم**
