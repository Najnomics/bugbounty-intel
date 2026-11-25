# The Bug Bounty Agent That Never Sleeps — and Always Asks Before It Attacks

- **Source URL:** https://medium.com/@vigneshkumaroffsec/the-bug-bounty-agent-that-never-sleeps-and-always-asks-before-it-attacks-af3e84aae814
- **Fetched from:** https://medium.com/@vigneshkumaroffsec/the-bug-bounty-agent-that-never-sleeps-and-always-asks-before-it-attacks-af3e84aae814?source=rss-07ee411d0b6f------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14984 (id 14984)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Vigneshkumaroffsec / Sat, 14 Nov 2026 03:13:25 GMT

*A 24/7 agent won’t find bugs by firing exploits at everything. It wins by doing the tireless, boring work — recon, triage, dedup, drafting — around the clock, and handing a human the one decision that matters. Here’s the architecture I use, built on Claude, with the guardrails that keep it legal. Authorized programs only.*

By Vignesh Kumar | Security Researcher

Every few months someone demos an “autonomous hacking AI” that supposedly finds and exploits bugs on its own. Then you read the fine print: it ran against a deliberately vulnerable lab, with no scope, no rate limits, and no one it could hurt. On a real bug bounty program, that same agent is a liability — it tests out of scope, hammers production, and files duplicate noise that gets your account banned.

The useful version is less dramatic and far more valuable. Bug bounty is mostly *waiting* and *watching*: new subdomains appear, a JS bundle changes, a program widens its scope, an endpoint starts returning something it didn’t yesterday. A human can’t watch all of that at 3 a.m. An agent can. So the job I give Claude isn’t “hack this” — it’s **“watch my authorized targets continuously, do the tedious analysis, and wake me only when there’s something worth my judgment.”**

I’ll say this once and mean it throughout: everything here is for programs you are **explicitly authorized** to test, inside their stated scope, under their rules. The agent’s power comes from *tirelessness*, not from autonomy over attacks — the moment anything intrusive is on the table, a human decides. That line is the whole design.

Split every bug-bounty task into two piles.

**Safe to automate 24/7** — passive, read-only, non-intrusive:

**Never automate unattended** — anything that *acts on* a target:

The agent lives entirely in the first pile and *proposes* work in the second. A human runs the second pile. Build it the other way around and you don’t have a research tool — you have an incident you own.

I build this on Claude because the loop is exactly what the API is designed for: the model reasons about what it’s seeing, calls tools to gather more, and decides when it has enough to flag something. Three building blocks matter.

**1. The agent loop.** You have three honest options, from most control to most managed:

For a continuous watcher, I like **Managed Agents scheduled deployments** (it fires every N minutes on its own) or the **Agent SDK** behind my own cron. The exploit-grade stuff never runs here.

**2. Two models, by job.** Don’t pay top-tier rates to classify 500 HTTP responses. Route by difficulty:

A cheap model filters the firehose; the capable model thinks about what survives.

**3. Your tools, as tools.** The agent is only as good as what it can see. You expose your existing recon stack — subfinder, httpx, nuclei in *passive* mode, a response-diff store — as Claude tools, and let the model orchestrate them. You can also connect external data over **MCP** (the connector needs both halves: an mcp\_servers entry *and* a matching mcp\_toolset tool).

Here’s the shape of the Messages API version — a watcher that calls read-only recon tools and reasons about the results. Note the model, the tools, and the gate.

import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

// Read-only tools only. Nothing here sends a payload or changes state.

const tools: Anthropic.Tool\[\] = \[

{ name: "list\_known\_assets", description: "Assets already in scope + last-seen state", input\_schema: {/\* ... \*/} },

{ name: "passive\_recon", description: "Passive subdomain/cert enumeration for an IN-SCOPE domain", input\_schema: {/\* ... \*/} },

{ name: "fetch\_and\_diff", description: "GET a URL and diff against the stored snapshot", input\_schema: {/\* ... \*/} },

{ name: "propose\_finding", description: "Hand a candidate finding to the human queue", input\_schema: {/\* ... \*/} },

\];

async function runWatch(scope: string\[\]) {

const messages: Anthropic.MessageParam\[\] = \[

{ role: "user", content: \`Watch these authorized targets and report anything worth a human's attention. Scope: ${scope.join(", ")}\` },

\];

while (true) {

const res = await client.messages.create({

model: "claude-opus-5-5",

max\_tokens: 16000,

// Cache the frozen scope + rules so every cycle is cheap to re-establish.

system: \[{ type: "text", text: SCOPE\_AND\_RULES, cache\_control: { type: "ephemeral" } }\],

tools,

messages,

});

messages.push({ role: "assistant", content: res.content });

if (res.stop\_reason !== "tool\_use") break;

const results = \[\];

for (const block of res.content) {

if (block.type !== "tool\_use") continue;

enforceScope(block); // hard gate — see below

results.push({

type: "tool\_result" as const,

tool\_use\_id: block.id,

content: await runReadOnlyTool(block.name, block.input),

});

}

messages.push({ role: "user", content: results });

}

}

Two deliberate choices: the model is claude-opus-5-5 for the reasoning, and the scope-and-rules block is **prompt-cached** so a loop that runs every few minutes, 24/7, isn't re-billing the full context each cycle (cache reads are a fraction of the input price). On a continuous agent, caching is the difference between a sane bill and a scary one.

The single most important function in the whole system is the one that refuses to do things. Scope enforcement is **code**, not a polite instruction in the prompt — the model can be wrong or jailbroken; the gate cannot be argued with.

```
function enforceScope(call: Anthropic.ToolUseBlock) {
  const target = extractTarget(call.input);
  // 1. Hard scope allowlist — out-of-scope target = hard stop, logged.
  if (!inAuthorizedScope(target)) throw new OutOfScope(target);
  // 2. No active/intrusive tool may ever run unattended.
  if (ACTIVE_TOOLS.has(call.name)) throw new RequiresHumanApproval(call.name, target);
  // 3. Rate limits per target, so the agent is a guest, not a flood.
  assertUnderRateLimit(target);
}
```
The Agent SDK gives you this as first-class **hooks and permission policies**; Managed Agents has server-side **permission policies** (always\_allow / always\_ask / auto). Whichever you use, the rule is identical: **passive tools run freely, active tools pause for a human, out-of-scope is impossible.** An agent that could decide on its own to send an exploit is not a feature — it's the bug.

A 24/7 agent generates an enormous transcript. Three Claude features keep a long-lived loop from exploding its context window (and its cost):

For the literal scheduling, a **Managed Agents scheduled deployment** fires a fresh session on a cron cadence with its own run record — which, honestly, is a cleaner “runs forever” story than a process you have to babysit. Give the loop a **task budget** so each cycle paces itself to a token ceiling instead of wandering.

When the agent finds something, it does **not** try to prove it by attacking. It assembles *evidence of a question worth asking*: the asset, what changed, why it looks interesting, and what a human should check next. Then it drafts — in your voice — a report with the endpoint, the observation, a plain-language impact hypothesis, and the suggested fix, and drops it in a review queue.

You open the queue in the morning, throw out the noise, and for the few real candidates you do the active testing **yourself**, by hand, inside scope. The agent compressed a night of tedium into a short list. That’s the win — not a bot that pwns things while you sleep, but one that makes sure you never miss the thing worth looking at.

The fantasy of an AI that autonomously hunts and exploits makes headlines and loses programs. The real edge is quieter: continuous, patient attention to targets you’re allowed to watch, with the one irreversible decision — *do we actually poke this?* — kept firmly in human hands. Claude is a genuinely good fit for that loop; it reasons about messy signals, orchestrates your existing tools, and runs cheaply for days if you cache and compact. Build the gate first, make passive the default, and let the agent do the thing it’s actually better at than you: never getting bored at 3 a.m.

If you’re starting out, build it against your *own* infrastructure or a program that explicitly permits automation, wire the scope gate before you wire a single recon tool, and watch it for a week before you trust a line of its output. Get the guardrails right there, and you’ll have an agent that extends your reach without ever crossing a line.

I’m Vignesh Kumar, a security researcher working across application security, DevSecOps, cloud security, and vulnerability research.

I share practical findings from security assessments and responsible disclosures to help improve the security of real-world systems.

*The techniques in this article are described for defending and testing systems you own or are authorized to assess. Automated testing must comply with each program’s rules and the law.*
