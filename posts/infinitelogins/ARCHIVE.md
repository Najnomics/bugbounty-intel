# @infinitelogins — full verbatim X archive (security-relevant posts)

_Generated 2026-11-11 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 32
- Conversations/threads: 32
- Oldest post captured: 2026-01-13
- Newest post captured: 2026-11-04


---

## 2026-11-04 · Post · I found a critical unauthenticated account takeover that let me log in as any customer on the platfo


Tags (automatic): Account takeover


### Post — @infinitelogins — 2026-11-04 14:04 UTC (2026-11-04 15:04 WAT)

- URL: https://x.com/infinitelogins/status/2117981403161764138
- Metrics (at fetch): bookmark 288, impression 11205, like 350, quote 0, reply 7, retweet 29

> I found a critical unauthenticated account takeover that let me log in as any customer on the platform. No password, no account of my own. It earned a $5,000 bounty.
>
> Quick context: the platform runs unattended devices, and those devices sign in with no human present. So instead of a password, each account has an "auto login key." A device presents the key and gets a session. The key is the credential.
>
> That design is fine right up until a key leaks. 
>
> The chain came down to 3 things:
>
> - Keys are the credential: by design, holding an account's auto login key gets you a session for that account, no password.
> - Wildcard injection: the lookup endpoints ran input through a SQL `LIKE` query, so a single `%` let me pull any account's key out of the database.
> - No rate limiting: I could iterate the whole customer table and lift every key.
>
> Here's how I chained them:
>
> 1. Leak accounts with a wildcard
>
> The lookup took a `key` and found it in the database with a `LIKE` query. So I sent:
>
> `GET /autologin/lookup?key=%`
>
> Instead of one record, it returned matching accounts: user IDs, tenant IDs, emails. A single `%` dumped account rows.
>
> 2. Pull a victim's real key
>
> A second endpoint resolved a key to an account. Same flaw. I sent a wildcard plus an ID I'd just leaked:
>
> `POST /autologin/resolve?key=%`
> `{"user_id": {victim-id}, "tenant_id": {tenant-id}}`
>
> It handed back that victim's actual auto login key.
>
> 3. Trade the leaked key for a session
>
> The device endpoint does exactly what it's built to do: present a valid auto login key for an account, get a session token for that account. The catch is the key was the victim's, leaked in the steps above, and should never have been in my hands.
>
> `POST /autologin/devices`
> `{"user_id": {victim-id}, "key": "{victim-key}", ...}`
>
> It registered my device under the victim's account and returned a fresh session token for them.
>
> 4. Full takeover
>
> `GET /me` with that token returned the victim's full profile. PII, billing identifiers, all of it. No authentication, no account of my own, and no notification to the victim that a new device had appeared.
>
> The wildcard enumerated the entire customer table, there was no rate limiting, so this worked against every account on the platform at scale.
>
> #BugBounty tip:
>
> Any endpoint that takes a secret and looks it up is a candidate for wildcard injection. If `%` returns more than it should, it's a `LIKE` query and you can enumerate the table.


---

## 2026-10-30 · Post · If you're doing bug bounty, you should be storing your recon data in an actual database instead of s


Tags (automatic): AI-assisted hunting


### Post — @infinitelogins — 2026-10-30 18:31 UTC (2026-10-30 19:31 WAT)

- URL: https://x.com/infinitelogins/status/2116236446147240443
- Metrics (at fetch): bookmark 297, impression 10591, like 321, quote 0, reply 15, retweet 27

> If you're doing bug bounty, you should be storing your recon data in an actual database instead of scattered local txt/md files.
>
> Free services like Supabase make this incredibly easy now, especially with their MCP integration.
>
> Get in the habit of constantly storing everything you discover about your targets:
>
> Endpoints
> Parameters
> Headers
> Request/response structures
> Related services
>
> Anything that might be useful later.
>
> The real benefit comes when you give your AI agents access to this data through MCP. You can start asking things like:
>
> "Check our endpoint store for related endpoints and build a custom wordlist for fuzzing."
>
> "What other services have we discovered on this target?"
>
> "What other parameters have we seen on this endpoint?"
>
> "What does a valid request to this endpoint look like?"
>
> Having all your recon in a structured, queryable database makes it so much easier to validate findings, discover related attack surfaces, and find ways to escalate vulnerabilities.
>
> The more recon you collect, the more useful this becomes. And instead of manually digging through old files, your agents can actually use everything you've discovered in previous sessions.
>
> #BugBounty


---

## 2026-10-28 · Post · I found a critical privilege escalation that took a brand new free trial account all the way to plat


Tags (automatic): AI-assisted hunting


### Post — @infinitelogins — 2026-10-28 13:04 UTC (2026-10-28 14:04 WAT)

- URL: https://x.com/infinitelogins/status/2115429533738262954
- Metrics (at fetch): bookmark 280, impression 11740, like 336, quote 2, reply 7, retweet 37

> I found a critical privilege escalation that took a brand new free trial account all the way to platform superadmin, with read access to every customer's data on the platform. It earned a $5,000 bounty.
>
> The chain came down to 3 things:
>
> - Mass assignment: a PUT endpoint let a user write their own `admin_permissions` field, including the superadmin flag.
> - MFA bypass: escalating to admin triggered MFA on login, but a separate "auto login" flow handed out session tokens with no MFA at all.
> - Broken tenant isolation: a superadmin token could read any user's data in any org on the platform.
>
> Here's how I chained all three together:
>
> 1. Escalate my own account
>
> As a new free trial user, I sent:
>
> `PUT /api/admin/{my-user-id}`
> `{"admin_permissions":"0000000f"}`
>
> The server accepted it. No check that I was already an admin. My account was now superadmin.
>
> 2. The MFA wall
>
> The moment I escalated, the backend started enforcing MFA on my logins:
>
> `POST /token` → MFA challenge
>
> Self-enrollment to MFA was disabled, so I couldn't even complete it. Dead end. 
>
> Then I remembered the auto login flow.
>
> 3. Why that flow exists
>
> The dashboard has a feature for signing in unattended devices. Things that need a session but have no human to type a password (or MFA code).
>
> You generate an "auto login" key, a base64 blob of `{userId}:{tenantId}:{random}`, and the device authenticates itself, headless. MFA is skipped there by design, because there's nobody at the device to challenge.
>
> So I asked: what's stopping me from logging in as a "device" instead of a user?
>
> 4. Bypass MFA with the auto login flow
>
> Before escalating, I'd already generated an auto login key for my own account. I replayed it against the device login endpoint:
>
> `POST /autologin/devices`
> `{"access_key":"{my-key}", ...}`
>
> It returned a full session token. No MFA challenge, because this path was never meant to need one. And since my account was now superadmin, that token was a superadmin session.
>
> The order is the whole trick. First I created the device key, then I performed the escalation, then I logged back in through the device flow, bypassing MFA. The key was minted before the MFA wall went up, so it still worked after.
>
> 5. What this unlocked
>
> With that token:
>
> `GET /api/users/{any-user-id}`
>
> returned full PII for users in completely different orgs, not just mine. User IDs were sequential, so this exposed records across the entire platform.
>
> #BugBounty tip:
>
> When an app adds a second auth factor, check whether every token issuing path enforces it. One legacy or "convenience" flow, like auto login, device pairing, or an API key, that skips MFA can undo the whole thing.
>
> And always ask: can I grab a credential before a security boundary goes up, then reuse it after?


---

## 2026-10-23 · Post · In his latest write-up, Johann Rehberger (@wunderwuzzi23) shows how one trailing dot bypassed Copilo


### Post — @infinitelogins — 2026-10-23 13:03 UTC (2026-10-23 14:03 WAT)

- URL: https://x.com/infinitelogins/status/2113617357385965628
- Metrics (at fetch): bookmark 29, impression 2822, like 44, quote 1, reply 6, retweet 6

> In his latest write-up, Johann Rehberger (@wunderwuzzi23) shows how one trailing dot bypassed Copilot's protected-file checks in Visual Studio and SSMS (CVE-2026-103572). Windows treats `settings.json.` as `settings.json`, so Copilot could rewrite its own config, point an MCP


---

## 2026-10-21 · Post · Simon Koeck (@soeckly) earned $90,000 from Google after finding a DevSite vulnerability that let him


### Post — @infinitelogins — 2026-10-21 13:04 UTC (2026-10-21 14:04 WAT)

- URL: https://x.com/infinitelogins/status/2112892669701558302
- Metrics (at fetch): bookmark 78, impression 4563, like 118, quote 0, reply 2, retweet 11

> Simon Koeck (@soeckly) earned $90,000 from Google after finding a DevSite vulnerability that let him run commands on Google's servers.
>
> The attack came down to 3 security mistakes that chained together.
>
> 1. A secret exposed in a session cookie
>
> Google's DevSite stored a pickled


---

## 2026-10-19 · Post · PwnEscape escapes KVM in Vercel's $1M sandbox, @opencode's big week ends in a breach, @Hacker0x01 ca


Tags (automatic): XSS, RCE, AI-assisted hunting, Platform: HackerOne


### Post — @infinitelogins — 2026-10-19 13:15 UTC (2026-10-19 14:15 WAT)

- URL: https://x.com/infinitelogins/status/2112170733228966180
- Metrics (at fetch): bookmark 8, impression 2002, like 32, quote 0, reply 4, retweet 3

> PwnEscape escapes KVM in Vercel's $1M sandbox, @opencode's big week ends in a breach, @Hacker0x01 caps trial reports at 3, @GoogleVRP raises Chrome payouts, and more.
>
> This week, Disclosed. #BugBounty
>
> Full issue → http://getdisclosed.com
>
> Highlights below 👇
>
> @PaulosYibelo publishes PwnEscape, the Linux networking bug behind the Vercel Sandbox KVM escape; CVE-2026-99999, CVSS 9.3.
>
> @opencode makes DeepSeek V4.1 Flash, GLM 5.3 Flash and Beam free and ships 2.0, then discloses a breach that exposed stored provider keys for 1.4% of Console users.
>
> @Hacker0x01 cuts trial reports to 3 for programs whose Signal requirement you don't meet; a triaged or resolved report resets the count.
>
> @samwcyo says he'd pay $100 per report for priority triage, automated dupe checks and payouts under 48 hours.
>
> @GoogleVRP restructures Chrome VRP rewards; memory-safety base rates quadruple and the $2K fuzzer bonus returns.
>
> @Hacker0x01 benchmarks 18 frontier LLMs against 62 complex vulns, research by @0xAsm0d3us.
>
> @GraySwanAI launches IPI Black, a $300K prompt-injection challenge backed by Anthropic, Meta and Google DeepMind.
>
> @intigriti makes the case for ID verification before submission on public programs.
>
> Simon Koeck turns a leaked client_secret into a forged Flask session and pickle RCE on Google DevSite; $90K.
>
> @brutecat breaks into Google's GFile for $100K.
>
> @SLCyberSec chains four Adobe Experience Manager Cloud bugs into pre-auth RCE.
>
> @wunderwuzzi23 slips past Copilot's file protections in Visual Studio and SSMS with a trailing dot; CVE-2026-103572.
>
> @mdp_sec's BB Arena ranks AI models on 100 black-box web/API labs; Grok 4.6 leads at 62.
>
> @yeswehack ships Claude Kit, a Claude Code plugin for triager-grade reports, and pits Claude Code, Codex and Gemini CLI against blind PortSwigger labs.
>
> @NahamSec builds a hackbot for under $250 and runs the DEF CON BBV workshop on hacking AI agents.
>
> @medusa_0xf breaks down how one email tricked Microsoft 365 Copilot.
>
> @garethheyes adds new <audio>/<video> onwebkitneedkey XSS vectors to the PortSwigger cheat sheet.
>
> That's not all. Full links, writeups & more → http://getdisclosed.com
>
> Bug bounty and offensive AI, curated.

**Links in post:** https://getdisclosed.com, http://getdisclosed.com


---

## 2026-10-18 · Post · Teaser for tomorrow's Disclosed drop.


Tags (automatic): AI-assisted hunting, Platform: HackerOne


### Post — @infinitelogins — 2026-10-18 16:51 UTC (2026-10-18 17:51 WAT)

- URL: https://x.com/infinitelogins/status/2111862804705694116
- Metrics (at fetch): bookmark 3, impression 1366, like 12, quote 0, reply 1, retweet 1

> Teaser for tomorrow's Disclosed drop.
>
> @PaulosYibelo publishes PwnEscape, the Linux networking bug that escaped KVM in Vercel's $1M sandbox; CVE-2026-99999.
>
> @opencode ships free models and 2.0, then discloses a breach that exposed stored provider keys for 1.4% of Console users.
>
> @Hacker0x01 cuts trial reports to 3 for programs you don't qualify for yet.
>
> @mdp_sec's BB Arena ranks AI models on 100 black-box web/API labs
>
> Subscribe at http://getdisclosed.com to get the drop first.

**Links in post:** http://getdisclosed.com


---

## 2026-10-17 · Post · I stumbled across a simple IDOR yesterday after ordering something online. Here's how I found it:


Tags (automatic): IDOR / BOLA


### Post — @infinitelogins — 2026-10-17 16:31 UTC (2026-10-17 17:31 WAT)

- URL: https://x.com/infinitelogins/status/2111495426868453543
- Metrics (at fetch): bookmark 207, impression 9937, like 360, quote 2, reply 4, retweet 34

> I stumbled across a simple IDOR yesterday after ordering something online. Here's how I found it:
>
> After placing my order, I noticed the receipt URL contained two parameters:
>
> `/order/receipt?orderId=12345&amp;codeId={uuid}`
>
> Opening this URL returned the full order details,


---

## 2026-10-17 · Post · Stumbled across an interesting IDOR yesterday after ordering something online. Here's how I found it


Tags (automatic): IDOR / BOLA


### Post — @infinitelogins — 2026-10-17 16:31 UTC (2026-10-17 17:31 WAT)

- URL: https://x.com/infinitelogins/status/2111495266524086354
- Metrics (at fetch): bookmark 0, impression 79, like 0, quote 0, reply 0, retweet 0

> Stumbled across an interesting IDOR yesterday after ordering something online. Here's how I found it:
>
> After placing my order, I noticed the receipt URL contained two parameters:
>
> `/order/receipt?orderId=12345&amp;codeId={uuid}`
>
> Opening this URL returned the full order details,


---

## 2026-10-15 · Post · In an impressive GitHub write-up, @v_metnew documents a sandbox escape in Anthropic's Claude Code CL


Tags (automatic): AI-assisted hunting


### Post — @infinitelogins — 2026-10-15 13:03 UTC (2026-10-15 14:03 WAT)

- URL: https://x.com/infinitelogins/status/2110718099221573685
- Metrics (at fetch): bookmark 46, impression 4655, like 78, quote 2, reply 8, retweet 8

> In an impressive GitHub write-up, @v_metnew documents a sandbox escape in Anthropic's Claude Code CLI (CVE-2026-55607). By using a prompt-injected repo with `.git` worktree gitdir confusion, they managed to overwrite `~/.zshenv` and bypass macOS seatbelt, achieving unsandboxed


---

## 2026-10-14 · Post · I found a critical unauthenticated SQL injection that earned a $4,000 bounty. The WAF blocked most S


Tags (automatic): SQL injection


### Post — @infinitelogins — 2026-10-14 13:02 UTC (2026-10-14 14:02 WAT)

- URL: https://x.com/infinitelogins/status/2110355630133322159
- Metrics (at fetch): bookmark 541, impression 19143, like 650, quote 4, reply 24, retweet 89

> I found a critical unauthenticated SQL injection that earned a $4,000 bounty. The WAF blocked most SQLi payloads, but I turned HTTP 500 errors into a data extraction channel.
>
> The exploit came down to 3 things:
>
> - SQL injection: A public API passed user input directly into BigQuery SQL.
> - WAF bypass: Keyword filtering missed BigQuery scripting techniques.
> - Error-based extraction: Detailed database errors exposed query results in HTTP 500 responses.
>
> Here's how I chained all three together:
>
> 1. Find the injection
>
> A public analytics endpoint accepted JSON input.
>
> Adding a single `'` to a parameter returned:
>
> `500 → Syntax error: Unclosed string literal`
>
> The error also revealed Google BigQuery was the backend.
>
> 2. Build a boolean oracle
>
> The WAF blocked keywords like `UNION`, `SELECT`, `AND`, and `OR`.
>
> But BigQuery scripting constructs like `IF` and `ASSERT` still worked:
>
> `IF TRUE THEN ASSERT FALSE; END IF;` → 500
>
> `IF FALSE THEN ASSERT FALSE; END IF;` → 200
>
> This let me ask the database true/false questions and read the answers from HTTP status codes.
>
> 3. Turn the 500 error into an output channel
>
> This was the biggest breakthrough because blind SQLi normally requires guessing data one character at a time using those true/false responses.
>
> But BigQuery supports:
>
> `RAISE USING MESSAGE = 'hello'`
>
> This deliberately throws a database error containing `hello`.
>
> Because the API exposed database error details, the response included:
>
> `500 → ... hello ...`
>
> Now imagine replacing `hello` with a database query result.
>
> The database includes that result in its error message, and the API returns it.
>
> Instead of guessing characters, I could retrieve an entire value in one request.
>
> 4. Bypass the WAF using BigQuery's own features
>
> The WAF blocked `EXECUTE IMMEDIATE`, which runs dynamically constructed SQL.
>
> But this worked:
>
> `EXECUTE/**/IMMEDIATE`
>
> The SQL parser understood it, while the WAF's keyword matching didn't.
>
> Another blocked keyword was `INFORMATION_SCHEMA`, used to enumerate tables and columns.
>
> The bypass was:
>
> `REVERSE('AMEHCS_NOITAMROFNI')`
>
> BigQuery reconstructs `INFORMATION_SCHEMA` at runtime.
>
> Using that reversed string in a dynamic query let me access database metadata without sending the blocked keyword literally.
>
> 5. What this unlocked
>
> Using those techniques, I was able to:
>
> - Enumerate datasets, tables, and columns
> - Query tables unrelated to the original analytics endpoint
> - Retrieve customer records, names, and addresses
> - Access operational records containing personal identifiers and contact information
> - Read sensitive fields that another API intentionally redacted
>
> #BugBounty tip:
>
> When a WAF blocks SQLi, don't just try random payloads. Understand the database dialect, what the WAF filters, and whether verbose errors leak data.
>
> Sometimes a `500` isn't just an error. It may be your output channel.


---

## 2026-10-13 · Post · Alex Craig (@Alex_______C) at @PortSwigger demonstrated how to steal secret tokens up to 640 charact


### Post — @infinitelogins — 2026-10-13 13:02 UTC (2026-10-13 14:02 WAT)

- URL: https://x.com/infinitelogins/status/2109993087984337111
- Metrics (at fetch): bookmark 59, impression 3418, like 77, quote 1, reply 0, retweet 15

> Alex Craig (@Alex_______C) at @PortSwigger demonstrated how to steal secret tokens up to 640 characters long using only CSS. No JavaScript required.
>
> The technique comes down to 3 things:
>
> - CSS injection: Attribute selectors can check whether specific character sequences exist https://t.co/24FDbILjMg

**Media:**
- photo: https://pbs.twimg.com/media/HUgziBVW4AAJrYg.jpg — no alt text provided by author


---

## 2026-10-12 · Reply · @AnthropicAI expands the Cyber Verification Program with tiered model access, @thezdi names a $300k 


Tags (automatic): XSS, RCE, Race condition, Blockchain / L1-L2 / bridge, AI-assisted hunting, Platform: HackerOne, Platform: Bugcrowd


### Post — @infinitelogins — 2026-10-12 13:01 UTC (2026-10-12 14:01 WAT)

- URL: https://x.com/infinitelogins/status/2109630626760470615
- Metrics (at fetch): bookmark 3, impression 1292, like 15, quote 0, reply 5, retweet 0

> @AnthropicAI expands the Cyber Verification Program with tiered model access, @thezdi names a $300k Pixel 10 chain as Master of Pwn, @portswigger drops a new token-exfil technique and a reality check on agent cascades, and more.
>
> This week, Disclosed. #BugBounty
>
> Full issue → http://getdisclosed.com
>
> Highlights below 👇
>
> @AnthropicAI expands the Cyber Verification Program into three tiers for vetted defenders, reduced blocking for approved security work, and access to top models.
>
> @thezdi wraps Pwn2Own Ireland 2026, Ikotas Labs takes Master of Pwn with a multi-bug chain against Google Pixel 10 worth $300k and 30 points.
>
> @Hacker0x01 releases the 10th Security Research Report and introduces “exposure debt,” the gap between vuln discovery and an org’s capacity to validate and fix.
>
> @Bugcrowd updates platform triage mechanics to preserve triage capacity and reduce low-signal submissions across engagements.
>
> @yeswehack posts ekoparty live hacking finals results, PyUs3r; bofill3; tonysec on the podium.
>
> @SLCyberSec publishes “A JPEG, a Race, and a Ghost,” two default-config Discourse bugs that chained into sitewide stored XSS and risky image pipeline behavior.
>
> @portswigger releases “Smashing the token limit with overlapping fragments,” CSS exfil that reconstructs long secrets by stitching overlapping leaks.
>
> @v_metnew documents a Claude Code CLI worktree sandbox escape (CVE-2026-55607), prompt-injected repo abuse that reached host-level effects on macOS setups.
>
> @gitlab drops DeepSeek-Reasonix research, a poisoned git config path that triggered command execution in an AI coding agent workflow.
>
> @pdiscoveryio shows how “abliterated” weight-edited open models hid phrase-triggered backdoors that issued tool calls for command execution and exfiltration.
>
> @zenitysec_labs publishes AgentCorruption, prompt-only compromise of AWS Bedrock AgentCore via IMDS access that exposed credentials and enabled lateral movement.
>
> @watchtowrcyber breaks down an in-the-wild PaperCut pre-auth RCE chain and the patch-bypass iterations that followed.
>
> @cloudflare ships a security-audit-skill repo, agent-orchestrated audits with schemas and validators for verifiable, machine-readable findings.
>
> @NahamSec routes real hacking traffic into Claude for analysis, the parts that sped up hypotheses and the parts that fell flat.
>
> That's not all. Full links, writeups & more → http://getdisclosed.com
>
> Bug bounty and offensive AI, curated.

**Links in post:** http://getdisclosed.com


---

## 2026-10-11 · Post · Teaser for tomorrow's Disclosed drop.


### Post — @infinitelogins — 2026-10-11 18:00 UTC (2026-10-11 19:00 WAT)

- URL: https://x.com/infinitelogins/status/2109343361715081547
- Metrics (at fetch): bookmark 2, impression 1199, like 15, quote 0, reply 0, retweet 0

> Teaser for tomorrow's Disclosed drop.
>
> @AnthropicAI expands the Cyber Verification Program into tiered model access, plus an OSS Scanner for critical repos.
>
> @thezdi caps Pwn2Own Ireland Day 3, Pixel 10 chain; $300k; 30 points.
>
> @portswigger drops overlapping-fragment CSS exfil and “The model isn’t cooperating.”
>
> @SLCyberSec breaks Discourse’s image pipeline with default-config impact.
>
> Subscribe at http://getdisclosed.com to get the drop first.

**Links in post:** http://getdisclosed.com


---

## 2026-10-08 · Post · I found a critical auth bypass that resulted in a $10K bounty due to mass PII exfiltration. Here’s t


Tags (automatic): Auth bypass


### Post — @infinitelogins — 2026-10-08 13:01 UTC (2026-10-08 14:01 WAT)

- URL: https://x.com/infinitelogins/status/2108181015885685018
- Metrics (at fetch): bookmark 660, impression 28025, like 823, quote 5, reply 30, retweet 105

> I found a critical auth bypass that resulted in a $10K bounty due to mass PII exfiltration. Here’s the technique:
>
> The endpoint had 3 checks:
>
> 1. JWT auth at the gateway  
> 2. Backend path validation  
> 3. A trusted-client header check  
>
> The bypass came from defeating each one differently.
>
> 1. JWT check
>
> Normal request:
>
> `GET /api/employee/12345`  
> → `401`
>
> But paths ending in `.json` were treated as static resources and skipped JWT auth:
>
> `GET /api/employee/12345.json`  
> → Auth check bypassed
>
> 2. Path validation
>
> Problem: The backend still needed a clean employee ID.
>
> Payload:
>
> `GET /api/employee/12345%23.json`
>
> The gateway saw a `.json` path.
>
> After decoding:
>
> `12345#.json`
>
> The downstream parser truncated at `#`, leaving:
>
> `12345`
>
> Same request, but different interpretation at each layer.
>
> 3. Trusted-client check
>
> The endpoint also expected a client header:
>
> `X-CLIENT-ID: WEBAPP`
>
> Without it:  
> → `400`
>
> With it:  
> → Request accepted
>
> So the final chain was:
>
> `.json` → bypass gateway auth  
> `%23` → preserve a valid backend ID  
> Client header → satisfy the final gate
>
> #BugBounty tip:
>
> When multiple layers handle the same request, map every security check and test whether the gateway, proxy, and backend interpret the URL differently.


---

## 2026-10-07 · Post · Has anybody from the bug bounty community actually gotten into the Red Team CVP yet? Mine was reject


### Post — @infinitelogins — 2026-10-07 14:29 UTC (2026-10-07 15:29 WAT)

- URL: https://x.com/infinitelogins/status/2107840771965759591
- Metrics (at fetch): bookmark 12, impression 7512, like 43, quote 0, reply 20, retweet 2

> Has anybody from the bug bounty community actually gotten into the Red Team CVP yet? Mine was rejected (temp suspended even until the appeal went through).


---

## 2026-10-06 · Post · Just found my first SSTI &gt; RCE 🔥


Tags (automatic): RCE


### Post — @infinitelogins — 2026-10-06 13:45 UTC (2026-10-06 14:45 WAT)

- URL: https://x.com/infinitelogins/status/2107467264803111230
- Metrics (at fetch): bookmark 12, impression 4839, like 189, quote 0, reply 11, retweet 0

> Just found my first SSTI &gt; RCE 🔥


---

## 2026-10-05 · Reply · @Hacker0x01 launches a community Discord server. @wiz_io announces a $6.5M open-source cloud bounty 


Tags (automatic): XSS, RCE, Request smuggling / desync, Memory corruption / native, AI-assisted hunting, Platform: HackerOne


### Post — @infinitelogins — 2026-10-05 13:15 UTC (2026-10-05 14:15 WAT)

- URL: https://x.com/infinitelogins/status/2107097261888946442
- Metrics (at fetch): bookmark 1, impression 1096, like 15, quote 0, reply 0, retweet 1

> @Hacker0x01 launches a community Discord server. @wiz_io announces a $6.5M open-source cloud bounty pool, @GoogleVRP pauses OSS VRP product submissions after automated report spam, @SaltSecurity hijacks an agentic AI platform with a single email, @zenitysec_labs drops a 0-click Agentforce exfil chain, and more.
>
> This week, Disclosed. #BugBounty
>
> Full issue → http://getdisclosed.com
>
> Highlights below 👇
>
> @GoogleVRP temporarily pauses OSS VRP product vulnerability submissions after a surge of automated, mostly invalid reports; supply-chain reports stayed in scope.
>
> @wiz_io announces a $6.5M 2026 open-source cloud bug bounty pool aimed at the components that underpin cloud infrastructure.
>
> @Hacker0x01 launches an official researcher Discord community as a real-time hub for platform updates and community discussion.
>
> @AnthropicAI evaluates GLM-5.3’s cyber capability spread and reports simple jailbreaks bypassed safeguards in a large fraction of simulated attempts.
>
> @GoogleVRP publishes PageBreak real-world findings, three concrete vulnerabilities found by an agentic scanner with live-site validation to keep false positives near zero.
>
> @SaltSecurity demonstrates hijacking Manus, an agentic AI platform, through a single crafted email routed via its Gmail integration.
>
> @zenitysec_labs details SalesBleed, a 0-click data exfiltration chain in Salesforce Agentforce that ended in covert DNS-based leakage.
>
> @wunderwuzzi23 shows SELECT-to-SYSADMIN escalation in SQL Copilot workflows, CVE-2026-65669, where “read-only” enforcement collapsed into bypassable intent checks.
>
> watchTowr publishes two NetScaler exploited-in-the-wild breakouts, CVE-2026-88771 pre-auth command injection and CVE-2026-88772 DTLS pre-auth memory overflow.
>
> @sec_consult reports iCloud Mail identity spoofing via “header smuggling,” using parsing discrepancies similar in spirit to SMTP smuggling primitives.
>
> @cloudflare writes up cross-tenant data exposure in Containers/Sandboxes where residual disk blocks could be recovered by another tenant on the same host.
>
> @NahamSec walks through a WordPress core bug to RCE, CVE-2026-87902, with focus on the practical exploit path.
>
> @0xacb highlights a Unicode dash bypass that turned into Windows curl.exe argument injection after normalization.
>
> @garethheyes flags a Chrome <camera> XSS vector and a Firefox XSS bypass using hidden=until-found with onbeforematch.
>
> That's not all. Full links, writeups & more → http://getdisclosed.com
>
> Bug bounty and offensive AI, curated.

**Links in post:** http://getdisclosed.com


---

## 2026-10-04 · Post · Teaser for tomorrow's Disclosed drop.


Tags (automatic): AI-assisted hunting, Platform: HackerOne


### Post — @infinitelogins — 2026-10-04 20:00 UTC (2026-10-04 21:00 WAT)

- URL: https://x.com/infinitelogins/status/2106836990616641913
- Metrics (at fetch): bookmark 3, impression 863, like 6, quote 0, reply 0, retweet 0

> Teaser for tomorrow's Disclosed drop.
>
> @Hacker0x01 launches a community Discord server.
>
> @wiz_io names a $6.5M 2026 open-source cloud bug bounty pool.
>
> @GoogleVRP pauses OSS VRP product vuln submissions after a flood of automated noise.
>
> @GoogleVRP PageBreak finds real vulns with near-zero false positives.
>
> @SaltSecurity hijacks an agentic AI platform with a single email.
>
> Subscribe at http://getdisclosed.com to get the drop first.

**Links in post:** http://getdisclosed.com


---

## 2026-09-29 · Reply · @HacktronAI names a July intrusion chain into @OpenAI , @MetaBugBounty announces a public Muse bount


Tags (automatic): SSRF, RCE, Mobile / Android / iOS, Memory corruption / native, AI-assisted hunting, Platform: HackerOne


### Post — @infinitelogins — 2026-09-29 13:01 UTC (2026-09-29 14:01 WAT)

- URL: https://x.com/infinitelogins/status/2104919420141277695
- Metrics (at fetch): bookmark 10, impression 2025, like 20, quote 1, reply 2, retweet 1

> @HacktronAI names a July intrusion chain into @OpenAI , @MetaBugBounty announces a public Muse bounty up to $300K, @efaav finds unsigned JWT auth in a Microsoft analytics API tied to 17 trillion records, and more.
>
> This week, Disclosed. #BugBounty
>
> Full issue → http://getdisclosed.com
>
> Highlights below 👇
>
> @MetaBugBounty takes its Muse AI-agent bounty public, up to $300K for qualifying vulns and high-impact prompt injection.
>
> @HacktronAI documents a chained intrusion into @OpenAI, starting from an image parsing bug and ending in RCE plus downstream identity and SSO abuse.
>
> @efaav walks through unsigned JWTs in an internal Microsoft analytics API, claim spoofing unlocked arbitrary queries, the write-up frames the blast radius as 17 trillion records.
>
> @vercel consolidates private and OSS coverage into one public @Hacker0x01 program spanning Vercel products and open-source projects.
>
> @Intigriti confirms @Adobe’s public bug bounty program migration, going live on September 1, 2026.
>
> @AnthropicAI announces a public @Hacker0x01 bug bounty after running privately with invited researchers.
>
> Anthropic’s September 2026 threat report summarizes observed Claude misuse, including multi-agent phishing and AI-augmented cyber workflows.
>
> @NahamSec announces NahamCon “Prompt2Pwn,” a live hacking event format for 2026.
>
> @forefy releases reburp, a Burp extension that exposes the Montoya API as a localhost OpenAPI REST interface for external scripts and agents.
>
> @Pillar_sec reports session spoofing and SSRF in Grafana MCP, one issue enabled unauthenticated tool execution with server-side privileges.
>
> @0xacb drops a GeoNetwork pre-auth RCE chain write-up, unauth formatter upload plus unsafe XSLT reached code execution.
>
> @SLCyberSec details Goja JavaScript engine exploitation, out-of-bounds heap write to arbitrary read/write and full RCE.
>
> @devploit ships geminiHunter, scanning web assets and Android apps for exposed Google Gemini API keys, plus validation checks.
>
> @Antisy_Training publishes “Exfil Everything,” a survey of real-world data theft chains against AI agents and their trust boundaries.
>
> That's not all. Full links, writeups & more → http://getdisclosed.com
>
> Bug bounty and offensive AI, curated.

**Links in post:** http://getdisclosed.com


---

## 2026-09-29 · Post · Teaser for tomorrow's Disclosed drop.


Tags (automatic): RCE


### Post — @infinitelogins — 2026-09-29 04:07 UTC (2026-09-29 05:07 WAT)

- URL: https://x.com/infinitelogins/status/2104785090232685017
- Metrics (at fetch): bookmark 17, impression 2145, like 39, quote 0, reply 3, retweet 4

> Teaser for tomorrow's Disclosed drop.
>
> @HacktronAI drops a chained intrusion story into OpenAI, RCE to SSO abuse.
>
> @metabugbounty  puts Muse public with up to $300K payouts.
>
> @efaav describes unsigned JWTs that could have exposed 17 trillion Microsoft records.
>
> @forefy ships reburp, Burp automation over localhost OpenAPI.
>
> Subscribe at http://getdisclosed.com to get the drop first.

**Links in post:** http://getdisclosed.com


---

## 2026-09-09 · Post · lol a couple of years ago I really wanted to escalate a broken link hijack to an xss for no other re


Tags (automatic): XSS


### Post — @infinitelogins — 2026-09-09 00:56 UTC (2026-09-09 01:56 WAT)

- URL: https://x.com/infinitelogins/status/2097489236505370701
- Metrics (at fetch): bookmark 4, impression 2748, like 48, quote 0, reply 5, retweet 0

> lol a couple of years ago I really wanted to escalate a broken link hijack to an xss for no other reason than to say I found one in the wild. Well, today was the day!


---

## 2026-08-11 · Post · Making bug bounty village proud. Great work man 👏 https://twitter.com/yaser_s/status/208724391664696


### Post — @infinitelogins — 2026-08-11 20:41 UTC (2026-08-11 21:41 WAT)

- URL: https://x.com/infinitelogins/status/2087278337983152330
- Metrics (at fetch): bookmark 1, impression 4036, like 19, quote 1, reply 1, retweet 0

> Making bug bounty village proud. Great work man 👏 https://twitter.com/yaser_s/status/2087243916646969448

**Links in post:** https://twitter.com/yaser_s/status/2087243916646969448

**Quoted post** 2087243916646969448: not readable via the API (deleted, private, or withheld).


---

## 2026-07-03 · Post · For the first time in my life, I finished in the top 5 in the US on H1 for a quarter. Bug bounty dre


Tags (automatic): Platform: HackerOne


### Post — @infinitelogins — 2026-07-03 17:39 UTC (2026-07-03 18:39 WAT)

- URL: https://x.com/infinitelogins/status/2073099379712671799
- Metrics (at fetch): bookmark 18, impression 10882, like 291, quote 0, reply 24, repost 2

> For the first time in my life, I finished in the top 5 in the US on H1 for a quarter. Bug bounty dreams do come true. [pic.x.com/GQbTid6wu4]

**Media:**
- photo: https://pbs.twimg.com/media/HMUg2O3bgAA29lh.jpg — no alt text provided by author


---

## 2026-05-14 · Post · and it got paid max crit bounty 😎 https://twitter.com/infinitelogins/status/2053257780895920586


### Post — @infinitelogins — 2026-05-14 14:27 UTC (2026-05-14 15:27 WAT)

- URL: https://x.com/infinitelogins/status/2054931668570685494
- Metrics (at fetch): bookmark 6, impression 5405, like 144, quote 0, reply 7, repost 0

> and it got paid max crit bounty 😎 https://twitter.com/infinitelogins/status/2053257780895920586

**Links in post:** https://twitter.com/infinitelogins/status/2053257780895920586

**Quoted post (full text):**

    #### Quoted post — @infinitelogins — 2026-05-09 23:36 UTC (2026-05-10 00:36 WAT)
    
    - URL: https://x.com/infinitelogins/status/2053257780895920586
    - Metrics (at fetch): bookmark 17, impression 12657, like 203, quote 3, reply 12, repost 1
    
    > after escalating for hours today.. finally found my first bug bounty SQLi!! super excited to submit this one.
    


---

## 2026-05-09 · Post · after escalating for hours today.. finally found my first bug bounty SQLi!! super excited to submit 


Tags (automatic): SQL injection


### Post — @infinitelogins — 2026-05-09 23:36 UTC (2026-05-10 00:36 WAT)

- URL: https://x.com/infinitelogins/status/2053257780895920586
- Metrics (at fetch): bookmark 17, impression 12657, like 203, quote 3, reply 12, repost 1

> after escalating for hours today.. finally found my first bug bounty SQLi!! super excited to submit this one.


---

## 2026-04-20 · Post · Vercel hacked via compromised AI customer, @nahuelrm_ takes MVH plus Erradicator at H1-361, @valent1


Tags (automatic): Account takeover, RCE, OAuth, CSP / CSPT, AI-assisted hunting, Platform: HackerOne


### Post — @infinitelogins — 2026-04-20 13:01 UTC (2026-04-20 14:01 WAT)

- URL: https://x.com/infinitelogins/status/2046212544805654565
- Metrics (at fetch): bookmark 13, impression 4802, like 26, quote 0, reply 3, retweet 5

> Vercel hacked via compromised AI customer, @nahuelrm_ takes MVH plus Erradicator at H1-361, @valent1nee takes the MVH from Google, 
> @BRuteLogic audits autonomous AI vuln discovery claims, and @S1r1u5_ reports a Claude-assisted V8 exploit against Discord that hit a shell after 2.3B tokens, and more.
>
> This week, Disclosed. #BugBounty
>
> Full issue → http://getdisclosed.com
>
> Highlights below 👇
>
> @rauchg reports a Vercel incident where an attacker pivoted from a compromised AI-platform customer into employee access, then enumerated environment variables.
>
> @nahuelrm_ wins MVH and the Erradicator award at HackerOne’s H1-361 Live Hacking Event.
>
> @valent1nee posts an MVH win from Google LHE Seoul 2026.
>
> @BRuteLogic publishes “Zero Days, Zero Truth,” a point-by-point audit of autonomous AI vulnerability discovery claims.
>
> @claudeai announces Claude Opus 4.7, then @elder_plinius drops a massive Opus 4.7 system prompt leak.
>
> @yeswehack ships a Caido integration for in-workspace program browsing and scope review, plus a Q1 Bucket List recap with remaining targets.
>
> @S1r1u5_ shares cost and workflow notes on an AI-assisted V8 exploit against Discord, roughly 2.3B tokens, about $2,283, ending in a remote shell.
>
> @H4cktus publishes a chain to RCE on Tomcat behind Cloudflare, with a thread, a blog, and a tool.
>
> @whoareme33 writes up a $15k CSPT that escalated to full account takeover, then a 2FA bypass via a prototype chain.
>
> @kartikeyagg  turns one access control bug into 22 paid issues by mining client-side JavaScript for repeatable patterns.
>
> @Intigriti highlights a GraphQL vulnerability mapping workflow focused on enumeration and common authorization failures.
>
> @Jhaddix boosts an “authority framing” prompt-injection technique aimed at system prompt exfil.
>
> @ctbbpodcast threads on multi-agent token delegation confused-deputy risk, plus a HackerNotes TL;DR on AI exfiltration primitives and OAuth scope pitfalls.
>
> @NahamSec talks through how LLMs and agents are affecting hunter workflows and program triage volume.
>
> That's not all. Full links, writeups & more → http://getdisclosed.com
>
> The bug bounty world, curated.

**Links in post:** http://getdisclosed.com


---

## 2026-04-13 · Post · Been a minute.


Tags (automatic): AI-assisted hunting, Platform: HackerOne


### Post — @infinitelogins — 2026-04-13 04:49 UTC (2026-04-13 05:49 WAT)

- URL: https://x.com/infinitelogins/status/2043552103076094169
- Metrics (at fetch): bookmark 45, impression 6238, like 116, quote 0, reply 12, repost 8

> Been a minute.
>
> I went dark for about 6 weeks on purpose, chasing a time-sensitive opportunity building an autonomous bug-bounty system, and so far, it has paid off: Top 60 on HackerOne over the last 90 days, top 5 in the US.
>
> I've learned a ton in these last few weeks about scaling AI systems. Not sharing everything yet, but maybe soon.
>
> A new Disclosed issue drops tomorrow to catch up on everything I missed.  http://getdisclosed.com

**Links in post:** http://getdisclosed.com


---

## 2026-02-23 · Post · Researchers at @HacktronAI found a bug in Google’s Antigravity IDE browser extension that lets a mal


Tags (automatic): RCE, AI-assisted hunting


### Post — @infinitelogins — 2026-02-23 14:01 UTC (2026-02-23 15:01 WAT)

- URL: https://x.com/infinitelogins/status/2025934052759367834
- Metrics (at fetch): bookmark 73, impression 13856, like 146, quote 0, reply 3, repost 13

> Researchers at @HacktronAI found a bug in Google’s Antigravity IDE browser extension that lets a malicious website write arbitrary files to a user’s system via a path traversal issue, which can be chained into code execution. 
>
> They reported it and received a $10,000 bounty. 
>
> Full write-up 👇
> https://www.hacktron.ai/blog/rce-in-googles-ai-code-editor-antigravity
>
> #BugBounty

**Links in post:** https://www.hacktron.ai/blog/rce-in-googles-ai-code-editor-antigravity


---

## 2026-02-19 · Post · A new open-source project by @spaceraccoon monitors commit diffs and PR context in GitHub repos to f


### Post — @infinitelogins — 2026-02-19 14:00 UTC (2026-02-19 15:00 WAT)

- URL: https://x.com/infinitelogins/status/2024484231062114553
- Metrics (at fetch): bookmark 92, impression 6272, like 118, quote 0, reply 1, repost 19

> A new open-source project by @spaceraccoon monitors commit diffs and PR context in GitHub repos to find vulnerability patches before they're published into public CVEs.
>
> For bug bounty hunters, this surfaces high-signal patch diffs where a real bug almost certainly existed. That makes it useful for finding variants and affected downstream projects before others do.
>
> Repo 👇
> https://github.com/spaceraccoon/vulnerability-spoiler-alert-action
>
> Site 👇
> https://vulnerabilityspoileralert.com/
>
> #BugBounty

**Links in post:** https://github.com/spaceraccoon/vulnerability-spoiler-alert-action, https://vulnerabilityspoileralert.com/


---

## 2026-02-16 · Post · Bug bounty platforms making statements about researcher data and use of AI, data exfiltration over p


Tags (automatic): RCE, Request smuggling / desync, AI-assisted hunting, Platform: HackerOne


### Post — @infinitelogins — 2026-02-16 14:00 UTC (2026-02-16 15:00 WAT)

- URL: https://x.com/infinitelogins/status/2023397056065253736
- Metrics (at fetch): bookmark 24, impression 2410, like 38, quote 0, reply 0, retweet 3

> Bug bounty platforms making statements about researcher data and use of AI, data exfiltration over phone calls using Gemini, an LLM that predicts CVEs before publication, Adobe hosting live bug hunting at Nullcon Goa, and more.
>
> This week, Disclosed. #BugBounty
>
> Full issue → http://getdisclosed.com
>
> Highlights below 👇
>
> @HackerOne clarifies submissions can't train GenAI models (per @senorarroz). @Intigriti and @YesWeHack also release statements on AI usage.
>
> @StarstrikeAI drops PhoneLeak: Gemini data-exfiltration chain using indirect prompt injection to leak data over audio/telephony channel
>
> @spaceraccoonsec shares open-source LLM-assisted pipeline that flags likely CVEs before publication
>
> @HacktronAI reports RCE in Google's Antigravity AI code editor with $10k payout
>
> @kqx_io finds single-typo SpiderMonkey Wasm GC bug leading to Firefox RCE
>
> @un1tycyb3r describes an unauthenticated  chat takeover via a chatbot.
>
> @sourceincite releases Samsung MagicINFO 9 Server pre-auth RCE deep dive (Part 2)
>
> @s3bsrt uncovers request smuggling via HTTP trailer parsing discrepancies
>
> @medusa_0xf breaks down token scope confusion and privilege escalation
>
> @ctbbpodcast reports HackerOne bounty reductions + upcoming community Q&A
>
> That's not all. Full links, write-ups  & more → http://getdisclosed.com
>
> The bug bounty world, curated.

**Links in post:** http://getdisclosed.com


---

## 2026-01-13 · Post · This week, Disclosed. BugBounty (Jan 12, 2026). 


### Post — @infinitelogins — 2026-01-13 00:06 UTC (2026-01-13 01:06 WAT)

- URL: https://x.com/infinitelogins/status/2010865879115055376
- Metrics (at fetch): bookmark 6, impression 2096, like 16, quote 0, reply 1, retweet 3

> This week, Disclosed. #BugBounty (Jan 12, 2026). 
>
> Full issue → https://t.co/P2Zjyh57Bs
>
> Highlights below 👇
>
> @portswigger opened nominations for the Top 10 Web Hacking Techniques of 2025, focused on reusable techniques published over the year.
>
> @yeswehack released its 2025 Top
