# blackboxarena-labs

- **Source URL:** https://blackboxarena.ai/labs/
- **Fetched:** 2026-11-21
- **Researcher:** mdp_sec
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

BB Arena Labs

# Black-box security labs for training and evaluating AI models

Most security training data hands the model the source code, or is public and may already be memorised. Ours is black-box and private: the model gets a target, a scope and a shell, like a real attacker, and every step is confirmed by the lab's own verifier.

Built and checked the same way as the [BB Arena benchmark](/), where the best AI model solves **22 of 100**. There's plenty left to learn.

[Request the evaluation pack →](/cdn-cgi/l/email-protection#e48c8188888ba4868885878f868b9c8596818a85ca858ddb9791868e818790d9b6819591819790c1d6d4908c81c1d6d4819285889185908d8b8ac1d6d49485878fc2858994df868b809dd9a78b8994858a9dc1d7a5c1d6d4c1d4a5b38c8590c1d6d49d8b91c39681c1d6d49096858d8a8d8a83c1d6d48b96c1d6d4819285889185908d8a83c1d7a5c1d6d4c1d4a5bd8b9196c1d6d4979085878fc1d6d4ccac8596868b96c1d6a7c1d6d4ad8a9794818790c1d6a7c1d6d492819688c1d6a7c1d6d48b908c8196cdc1d7a5c1d6d4c1d4a5)10 labs under NDA, each in freshly seeded copies, with reference solutions.

**Never the leaderboard's labs.** The labs behind the BB Arena leaderboard are never sold, licensed or shared. The labs we license are a separate set, built the same way. That keeps leaderboard scores honest, and it makes our labs safe to train on: you can't train on the test.

## How a lab works

## Prefer to read? The nine steps

1. 01**A black-box target**Your model gets a target, a scope and a shell. No source code, like a real attacker.
2. 02**A real flaw in an ordinary product**Built from our own security research: a fully synthetic, isolated product that recreates the attack path behind a real-world vulnerability.
3. 03**Proof, not claims**Four rungs, each counted only when the lab's own verifier confirms it. A claim alone earns nothing.
4. 04**Nothing to memorise**Every lab ships in many seeded copies, with fresh proof values each run, so nothing can be memorised.
5. 05**A secure twin**The same product with the flaw fixed. Claiming the flaw there scores zero, so bluffing shows up.
6. 06**A reward you can trust**Partial progress earns partial reward: reward per rung for training, full solves for evaluation. Infrastructure failures are marked invalid, not zero.
7. 07**Measured difficulty**Every lab is measured against a top frontier model and ships at its measured tier: medium or hard.
8. 08**Plenty of headroom**The best model on our leaderboard solves 22 of 100. The catalogue has 1,000 labs in 47 vulnerability classes, never the leaderboard's labs.
9. 09**A scorecard on your own machines**Run the evaluation pack, 10 labs under NDA, on your own machines and get a scorecard: results per lab, by tier and class.

## Why the reward can be trusted

A lab only ships after it passes all of these.

- **Independent audits**Separate reviewers audit every lab before release. Every lab family needs 2 to 4 audit rounds before it passes.
- **Reward-hacking review**An adversarial review looks for shortcuts that earn reward without doing the exploit.
- **Random and idle agents earn nothing**An agent that does nothing, or acts at random, scores zero.
- **No free steps**An ordinary user going about ordinary tasks earns no rung.
- **Nothing to memorise**Every lab ships as many seeded copies, each with its own secrets, IDs and data, so a score can't come from a memorised answer. Contamination canaries show if lab content turns up where it shouldn't, such as in training data.
- **Measured difficulty**Every lab is measured against a top frontier model and ships at its measured tier: medium or hard. Not a guess.

## Coverage

The full catalogue: 1,000 labs across 47 vulnerability classes, 7 languages and 20 frameworks. It uses a finer taxonomy than the benchmark's 10 classes.

- **Access control and authorisation**156Object-level authorisation (IDOR, BOLA) · Function-level authorisation and privilege escalation · Property-level authorisation and mass assignment · Parser and normalisation differentials
- **Authentication and identity**184Authentication bypass · MFA and step-up bypass · Session management · OAuth, OIDC, SAML and SSO · JWT and token validation · Account takeover flows · Brute force and rate limiting
- **Injection**165SQL injection · ORM and filter injection · NoSQL injection · OS command injection · Argument injection · Code injection and sandbox escape · Server-side template injection · XXE · Insecure deserialisation · LDAP, XPath, CRLF and header injection · Server-side prototype pollution
- **Server-side requests and files**100SSRF · Path traversal and file read · File upload and file write · Unsafe consumption of external data
- **Client-side**90Cross-site scripting · CSRF · CORS misconfiguration · Open redirect and cross-window flaws · WebSocket flaws
- **Protocol, caching and infrastructure**57HTTP request smuggling and desync · Web cache poisoning and deception · Host header attacks · Misconfiguration and exposed services · Cloud and container control planes
- **Business logic and concurrency**82Business logic and workflow abuse · Race conditions
- **Exposure and cryptography**81Secret and key exposure · Sensitive information disclosure · Weak cryptography and predictable tokens
- **Software supply chain**20Dependency confusion and build artefacts
- **AI, LLM and agent applications**65Prompt injection and excessive agency · Improper output handling · Hidden context and RAG leakage · MCP and agent tool-server flaws · Agent sandbox and allowlist bypass

- Node.js
- 250
- Express, Next.js, NestJS, Fastify
- Python
- 200
- FastAPI, Django, Flask
- PHP
- 150
- Laravel, Symfony, plain PHP
- Java
- 150
- Spring Boot, Quarkus
- Go
- 100
- net/http, Gin, Echo
- .NET
- 100
- ASP.NET Core minimal API and MVC
- Ruby
- 50
- Rails, Sinatra

**30%**Medium

**70%**Hard

Every lab is measured against a top frontier model and ships at the tier it measured.

REST and server-rendered apps, GraphQL, WebSocket, gRPC and MCP tool servers.

PostgreSQL, MySQL and MariaDB, SQLite, a MongoDB-compatible document store, Valkey caches, S3-style object storage and search.

**See them on your own stack**10 labs under NDA, with reference solutions, datasheets and the grader.

[Request the evaluation pack →](/cdn-cgi/l/email-protection#c5ada0a9a9aa85a7a9a4a6aea7aabda4b7a0aba4eba4acfab6b0a7afa0a6b1f897a0b4b0a0b6b1e0f7f5b1ada0e0f7f5a0b3a4a9b0a4b1acaaabe0f7f5b5a4a6aee3a4a8b5fea7aaa1bcf886aaa8b5a4abbce0f684e0f7f5e0f58492ada4b1e0f7f5bcaab0e2b7a0e0f7f5b1b7a4acabacaba2e0f7f5aab7e0f7f5a0b3a4a9b0a4b1acaba2e0f684e0f7f5e0f5849caab0b7e0f7f5b6b1a4a6aee0f7f5ed8da4b7a7aab7e0f786e0f7f58cabb6b5a0a6b1e0f786e0f7f5b3a0b7a9e0f786e0f7f5aab1ada0b7ece0f684e0f7f5e0f584)

## What you get

- Self-hosted with Docker Compose, on your own machines.
- Packaged for common agent evaluation and RL training stacks: Harbor, Inspect and verl-style setups.
- A grader that reports reward per rung, and marks infrastructure failures as invalid instead of scoring them zero.
- A local scorecard after every run: results per lab, by tier and class.
- Many seeded copies of every lab, each with its own secrets, IDs and data: more variants to train on, and fresh proof values on every run.
- A datasheet and a reference solution for every lab.
- Fix tasks for the same labs, with their own grader.
- A 25-minute default time limit per attempt. Change it to suit your setup.

## Bonus: fix tasks

The same labs also come the other way round. The agent gets the vulnerable code and a ticket, and has to repair the flaw without breaking the app.

- **Three ticket levels:** a reproduction to follow, a weakness type and area, or a blank-slate audit.
- **Graded by behaviour:** every exploit variant blocked, normal use still working, the feature still there, nothing leaking.
- **Hard to game:** a small set of visible smoke tests, with the full test suite kept hidden. Deleting the feature or refusing every request scores zero.
- **Attack and defend** on the same products, so one catalogue trains both skills.

## Get started

- For buyers**Evaluation pack**10 labs under NDA, with reference solutions, datasheets and the grader. Run them on your own stack before you decide.[Request the evaluation pack →](/cdn-cgi/l/email-protection#fe969b929291be9c929f9d959c91869f8c9b909fd09f97c18d8b9c949b9d8ac3ac9b8f8b9b8d8adbccce8a969bdbccce9b889f928b9f8a979190dbccce8e9f9d95d89f938ec59c919a87c3bd91938e9f9087dbcdbfdbcccedbcebfa9969f8adbccce87918bd98c9bdbccce8a8c9f9790979099dbccce918cdbccce9b889f928b9f8a979099dbcdbfdbcccedbcebfa7918b8cdbccce8d8a9f9d95dbccced6b69f8c9c918cdbccbddbccceb7908d8e9b9d8adbccbddbccce889b8c92dbccbddbccce918a969b8cd7dbcdbfdbcccedbcebf)
- Licensing and pricing**Talk to us**Tell us what you're building and how many labs you need. We don't publish prices; we'll quote.[Talk to us about labs →](/cdn-cgi/l/email-protection#5b333e3737341b39373a38303934233a293e353a753a3264282e39313e382f660f3a37307e696b2f347e696b2e287e696b3a39342e2f7e696b373a39287d3a362b6039343f22661834362b3a35227e681a7e696b7e6b1a0c333a2f7e696b22342e7c293e7e696b392e32373f32353c7e681a7e696b7e6b1a09342e3c3337227e696b33342c7e696b363a35227e696b373a39287e696b22342e7e696b353e3e3f7e681a7e696b7e6b1a)

## Questions

- Can we train on these labs?
- Yes, that's what they're for. They're a separate set from the leaderboard's labs, so training on them can't contaminate a BB Arena result.
- Does licensing labs help a model on the leaderboard?
- Only through real skill. The leaderboard's labs are never sold, and every model runs under the same protocol and scoring, whoever licenses labs. See the [methodology](/methodology/).
- Do you share how the labs are built?
- No. You get the labs, the grader, datasheets and reference solutions. How we build and check them stays with us.
- Can we run them offline?
- Yes. Labs are self-hosted with Docker Compose. We deliver images from our private registry, or as encrypted archives for offline sites.
- Which tools do they work with?
- They come packaged for Harbor, Inspect and verl-style RL training, with a catalogue manifest. Any model and harness that can reach a web address and use a shell can run them.
- Are labs licensed exclusively?
- No. Every licensed lab is available to every buyer.
- How do you stop labs leaking?
- Every licensed buyer's instances carry their own watermark, and every lab has contamination canaries, so lab content that turns up where it shouldn't can be traced.
- How much does it cost?
- It depends on what you need. [Talk to us](/cdn-cgi/l/email-protection#4b232e2727240b29272a28202924332a392e252a652a2274383e29212e283f761f2a27206e797b3f246e797b3e386e797b2a29243e3f6e797b272a29386d2a263b7029242f32760824263b2a25326e780a6e797b6e7b0a1c232a3f6e797b32243e6c392e6e797b293e22272f22252c6e780a6e797b6e7b0a19243e2c2327326e797b23243c6e797b262a25326e797b272a29386e797b32243e6e797b252e2e2f6e780a6e797b6e7b0a).

**Training AI models for security?**Start with the evaluation pack and run it on your own stack.

[Request the evaluation pack →](/cdn-cgi/l/email-protection#6e060b0202012e0c020f0d050c01160f1c0b000f400f07511d1b0c040b0d1a533c0b1f1b0b1d1a4b5c5e1a060b4b5c5e0b180f021b0f1a0701004b5c5e1e0f0d05480f031e550c010a17532d01031e0f00174b5d2f4b5c5e4b5e2f39060f1a4b5c5e17011b491c0b4b5c5e1a1c0f07000700094b5c5e011c4b5c5e0b180f021b0f1a0700094b5d2f4b5c5e4b5e2f37011b1c4b5c5e1d1a0f0d054b5c5e46260f1c0c011c4b5c2d4b5c5e27001d1e0b0d1a4b5c2d4b5c5e180b1c024b5c2d4b5c5e011a060b1c474b5d2f4b5c5e4b5e2f)
