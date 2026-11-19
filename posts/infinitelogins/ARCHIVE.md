# @infinitelogins — full verbatim X archive (security-relevant posts)

_Generated 2026-11-19 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 128
- Conversations/threads: 122
- Oldest post captured: 2020-01-17
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
- Metrics (at fetch): bookmark 18, impression 10882, like 291, quote 0, reply 24, retweet 2

> For the first time in my life, I finished in the top 5 in the US on H1 for a quarter. Bug bounty dreams do come true. [pic.x.com/GQbTid6wu4]

**Media:**
- photo: https://pbs.twimg.com/media/HMUg2O3bgAA29lh.jpg — no alt text provided by author


---

## 2026-05-16 · Post · It feels like WAFs don't even matter anymore.. claude always finds a bypass


Tags (automatic): AI-assisted hunting


### Post — @infinitelogins — 2026-05-16 04:06 UTC (2026-05-16 05:06 WAT)

- URL: https://x.com/infinitelogins/status/2055500095161086102
- Metrics (at fetch): bookmark 20, impression 8201, like 84, quote 0, reply 5, retweet 1

> It feels like WAFs don't even matter anymore.. claude always finds a bypass


---

## 2026-05-14 · Post · and it got paid max crit bounty 😎 https://twitter.com/infinitelogins/status/2053257780895920586


### Post — @infinitelogins — 2026-05-14 14:27 UTC (2026-05-14 15:27 WAT)

- URL: https://x.com/infinitelogins/status/2054931668570685494
- Metrics (at fetch): bookmark 6, impression 5405, like 144, quote 0, reply 7, retweet 0

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

## 2026-04-20 · Post · Vercel gets hacked, HackerOne and Google both crown new MVHs, New Opus launch + leak, and more.


Tags (automatic): Platform: HackerOne


### Post — @infinitelogins — 2026-04-20 00:04 UTC (2026-04-20 01:04 WAT)

- URL: https://x.com/infinitelogins/status/2046017140814422136
- Metrics (at fetch): not returned

> Vercel gets hacked, HackerOne and Google both crown new MVHs, New Opus launch + leak, and more.
>
> This is a teaser for tomorrow's drop. Subscribe at http://getdisclosed.com to get the drop first.

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

## 2026-02-20 · Post · In a recent advisory, @caidoio details a bypass for DNS rebinding protection in Caido. By injecting 


Tags (automatic): RCE


### Post — @infinitelogins — 2026-02-20 14:01 UTC (2026-02-20 15:01 WAT)

- URL: https://x.com/infinitelogins/status/2024846806715162740
- Metrics (at fetch): bookmark 32, impression 4482, like 44, quote 0, reply 0, retweet 5

> In a recent advisory, @caidoio details a bypass for DNS rebinding protection in Caido. By injecting a `X-Forwarded-Host: 127.0.0.1:8080` header, attackers could access restricted endpoints and achieve RCE if popups were permitted.
>
> Affected versions are prior to 0.55.0 so make


---

## 2026-02-19 · Post · A new open-source project by @spaceraccoon monitors commit diffs and PR context in GitHub repos to f


### Post — @infinitelogins — 2026-02-19 14:00 UTC (2026-02-19 15:00 WAT)

- URL: https://x.com/infinitelogins/status/2024484231062114553
- Metrics (at fetch): bookmark 92, impression 6272, like 118, quote 0, reply 1, retweet 19

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

## 2026-02-15 · Post · Bug bounty platforms making statements about researcher data and use of AI, data exfiltration over p


Tags (automatic): AI-assisted hunting


### Post — @infinitelogins — 2026-02-15 22:05 UTC (2026-02-15 23:05 WAT)

- URL: https://x.com/infinitelogins/status/2023156777211334815
- Metrics (at fetch): bookmark 12, impression 1752, like 30, quote 0, reply 0, retweet 2

> Bug bounty platforms making statements about researcher data and use of AI, data exfiltration over phone calls using Gemini, an LLM that predicts CVEs before publication, and Adobe hosting live bug hunting at Nullcon Goa.
>
> This was a teaser for tomorrow's Disclosed drop.


---

## 2026-02-09 · Post · Millions paid in live hacking events, PortSwigger names the top web techniques of 2025, AI-powered t


Tags (automatic): AI-assisted hunting


### Post — @infinitelogins — 2026-02-09 14:00 UTC (2026-02-09 15:00 WAT)

- URL: https://x.com/infinitelogins/status/2020860431712002458
- Metrics (at fetch): bookmark 5, impression 1660, like 26, quote 0, reply 1, retweet 2

> Millions paid in live hacking events, PortSwigger names the top web techniques of 2025, AI-powered triage lands in bug bounty workflows, and more.
>
> Full issue → https://t.co/glC021P2kO
>
> Highlights below 👇
>
> @albinowax shares PortSwigger’s community-voted Top 10 web hacking


---

## 2026-02-05 · Thread · I analyze thousands of bug bounty content items every month. Less than 5% makes it to the newsletter


### Post — @infinitelogins — 2026-02-05 14:00 UTC (2026-02-05 15:00 WAT)

- URL: https://x.com/infinitelogins/status/2019410859374579884
- Metrics (at fetch): bookmark 192, impression 20590, like 283, quote 1, reply 327, retweet 27

> I analyze thousands of bug bounty content items every month. Less than 5% makes it to the newsletter.
>
> I distilled those curated selections down to the top 25 resources for 2026 and put them in this PDF. It includes the top platforms, tools, and people that consistently deliver https://t.co/9jUjtFV8YS

**Media:**
- photo: https://pbs.twimg.com/media/HAZjeZJXYAAcBaT.jpg — no alt text provided by author


### Thread part 2 — @infinitelogins — 2026-02-06 15:57 UTC (2026-02-06 16:57 WAT)

- URL: https://x.com/infinitelogins/status/2019802647788945842
- Metrics (at fetch): bookmark 8, impression 615, like 9, quote 0, reply 1, retweet 0

> EDIT: You can find the guide here! https://t.co/YxiQgeeB6n


---

## 2026-02-04 · Post · In a demo by @Ethiack, their Hackian AI agent achieved RCE on Clawdbot/Moltbot in under 2 hours. It 


Tags (automatic): RCE, AI-assisted hunting


### Post — @infinitelogins — 2026-02-04 14:00 UTC (2026-02-04 15:00 WAT)

- URL: https://x.com/infinitelogins/status/2019048435622535232
- Metrics (at fetch): bookmark 16, impression 2306, like 33, quote 0, reply 4, retweet 3

> In a demo by @Ethiack, their Hackian AI agent achieved RCE on Clawdbot/Moltbot in under 2 hours. It abused public JS source maps to learn the WebSocket protocol, then used a gatewayUrl override (which controls where the UI connects) to steal auth tokens from the initial WebSocket


---

## 2026-02-02 · Post · HackerOne launches a new product, Bugcrowd drops Inside the Mind of a Hacker, Ethihack’s autonomous 


Tags (automatic): AI-assisted hunting, Platform: HackerOne, Platform: Bugcrowd


### Post — @infinitelogins — 2026-02-02 14:00 UTC (2026-02-02 15:00 WAT)

- URL: https://x.com/infinitelogins/status/2018323705722503556
- Metrics (at fetch): bookmark 39, impression 5370, like 62, quote 0, reply 2, retweet 9

> HackerOne launches a new product, Bugcrowd drops Inside the Mind of a Hacker, Ethihack’s autonomous pentester takes down Clawdbot/Moltbot/OpenBot, and more.
>
> Full issue → https://t.co/glC021P2kO
>
> Highlights below 👇
>
> @Hacker0x01 launches Agentic PTaaS, AI-driven pentesting with


---

## 2026-02-02 · Post · A one-click ATO to RCE chain in Moltbot, Bugcrowd’s Hacker Mind report, HackerOne's New Product Offe


Tags (automatic): Account takeover, RCE, Platform: HackerOne, Platform: Bugcrowd


### Post — @infinitelogins — 2026-02-02 04:03 UTC (2026-02-02 05:03 WAT)

- URL: https://x.com/infinitelogins/status/2018173399277961343
- Metrics (at fetch): bookmark 8, impression 1448, like 23, quote 0, reply 0, retweet 2

> A one-click ATO to RCE chain in Moltbot, Bugcrowd’s Hacker Mind report, HackerOne's New Product Offering, PackageGate, and more. 
>
> This was a teaser for tomorrow's Disclosed drop.
>
> Subscribe at https://t.co/glC021PAam to get the drop first.


---

## 2026-01-30 · Post · In his latest post, @adnanthekhan detailed an attack chain against GitHub Copilot Agent that exfiltr


Tags (automatic): Race condition, AI-assisted hunting


### Post — @infinitelogins — 2026-01-30 14:00 UTC (2026-01-30 15:00 WAT)

- URL: https://x.com/infinitelogins/status/2017236556021416425
- Metrics (at fetch): bookmark 26, impression 2930, like 38, quote 0, reply 1, retweet 5

> In his latest post, @adnanthekhan detailed an attack chain against GitHub Copilot Agent that exfiltrates repository secrets via poisoned CI pipeline execution. The exploit combines a TOCTOU race condition, prompt injection, and malicious GitHub issues assigned to Copilot.


---

## 2026-01-29 · Post · Dominic White's (@singe) Burp Global Match &amp; Replace extension allows system-wide application of


### Post — @infinitelogins — 2026-01-29 20:39 UTC (2026-01-29 21:39 WAT)

- URL: https://x.com/infinitelogins/status/2016974532813472124
- Metrics (at fetch): bookmark 62, impression 3686, like 73, quote 0, reply 1, retweet 9

> Dominic White's (@singe) Burp Global Match &amp; Replace extension allows system-wide application of match &amp; replace rules across all Burp Suite tools, not just the Proxy.
>
> This means your transformations work in Repeater, Intruder, Scanner, and other extensions, not just proxied


---

## 2026-01-28 · Post · In Salesforce Commerce Cloud, @castilho101 found XSS where a JSON parameter gets rendered into HTML.


Tags (automatic): XSS


### Post — @infinitelogins — 2026-01-28 14:01 UTC (2026-01-28 15:01 WAT)

- URL: https://x.com/infinitelogins/status/2016511907696431133
- Metrics (at fetch): bookmark 168, impression 12226, like 239, quote 1, reply 7, retweet 35

> In Salesforce Commerce Cloud, @castilho101 found XSS where a JSON parameter gets rendered into HTML. Cloudflare WAF blocked his payloads, so he encoded characters as Unicode escapes (\u0073 for 's'). The WAF sees raw Unicode and allows it, but JSON.parse() on the server decodes


---

## 2026-01-27 · Post · Claude Code skills for security research are emerging as a workflow enhancement tool. Trail of Bits 


Tags (automatic): AI-assisted hunting


### Post — @infinitelogins — 2026-01-27 14:00 UTC (2026-01-27 15:00 WAT)

- URL: https://x.com/infinitelogins/status/2016149352943669679
- Metrics (at fetch): bookmark 317, impression 19059, like 273, quote 1, reply 8, retweet 40

> Claude Code skills for security research are emerging as a workflow enhancement tool. Trail of Bits released burpsuite-project-parser, which lets you query Burp Suite project files to extract hosts, endpoints, parameters, and vulnerabilities without opening the GUI. Daniel


---

## 2026-01-26 · Thread · A new AI research safe harbor framework published by HackerOne and multiple new LLM-adjacent securit


Tags (automatic): OAuth, AI-assisted hunting, Platform: HackerOne


### Post — @infinitelogins — 2026-01-26 14:00 UTC (2026-01-26 15:00 WAT)

- URL: https://x.com/infinitelogins/status/2015786991724478729
- Metrics (at fetch): bookmark 33, impression 7650, like 53, quote 1, reply 4, retweet 11

> A new AI research safe harbor framework published by HackerOne and multiple new LLM-adjacent security workflows landing in the wild. On the technical side, OAuth token handling, WAF edge cases, and cloud identity misconfigurations kept showing up across write-ups .
>
> Full issue →


### Thread part 2 — @infinitelogins — 2026-01-26 22:18 UTC (2026-01-26 23:18 WAT)

- URL: https://x.com/infinitelogins/status/2015912323891040715
- Metrics (at fetch): bookmark 0, impression 304, like 1, quote 0, reply 0, retweet 0

> @OriginalSicksec , @VailSec , @dropn0w thank YOU for the resources


---

## 2026-01-26 · Post · HackerOne's new AI Safe Harbor, a Salesforce OAuth-to-ATO chain exploiting WAF behavior, Intigriti's


Tags (automatic): Account takeover, OAuth, AI-assisted hunting, Platform: HackerOne


### Post — @infinitelogins — 2026-01-26 02:00 UTC (2026-01-26 03:00 WAT)

- URL: https://x.com/infinitelogins/status/2015605655995031656
- Metrics (at fetch): bookmark 8, impression 1119, like 11, quote 0, reply 2, retweet 0

> HackerOne's new AI Safe Harbor, a Salesforce OAuth-to-ATO chain exploiting WAF behavior, Intigriti's researcher updates, and the cURL bounty shutdown.
>
> Plus: Trail of Bits Claude Code skills, Waymore 8.0, and a $70k 2FA bypass breakdown.
>
> Subscribe at https://t.co/glC021PAam


---

## 2026-01-26 · Post · HackerOne's new AI Safe Harbor, a Salesforce OAuth-to-ATO chain exploiting WAF behavior, Intigriti's


Tags (automatic): Account takeover, OAuth, AI-assisted hunting, Platform: HackerOne


### Post — @infinitelogins — 2026-01-26 01:59 UTC (2026-01-26 02:59 WAT)

- URL: https://x.com/infinitelogins/status/2015605541897408882
- Metrics (at fetch): bookmark 0, impression 10, like 0, quote 0, reply 0, retweet 0

> HackerOne's new AI Safe Harbor, a Salesforce OAuth-to-ATO chain exploiting WAF behavior, Intigriti's researcher updates, and the cURL bounty shutdown.
>
> Plus: Trail of Bits Claude Code skills, Waymore 8.0, and a $70k 2FA bypass breakdown.
>
> Subscribe at https://t.co/glC021PAam


---

## 2026-01-26 · Post · HackerOne's new AI Safe Harbor, a Salesforce OAuth-to-ATO chain exploiting WAF behavior, Intigriti's


Tags (automatic): Account takeover, OAuth, AI-assisted hunting, Platform: HackerOne


### Post — @infinitelogins — 2026-01-26 01:59 UTC (2026-01-26 02:59 WAT)

- URL: https://x.com/infinitelogins/status/2015605498641576213
- Metrics (at fetch): bookmark 0, impression 13, like 0, quote 0, reply 0, retweet 0

> HackerOne's new AI Safe Harbor, a Salesforce OAuth-to-ATO chain exploiting WAF behavior, Intigriti's researcher updates, and the cURL bounty shutdown.
>
> Plus: Trail of Bits Claude Code skills, Waymore 8.0, and a $70k 2FA bypass breakdown.
>
> Subscribe at https://t.co/glC021PAam


---

## 2026-01-25 · Post · Just stumbled across this AI bot channel and I'm so confused. 4.26m subs, but only 7 videos with a t


Tags (automatic): AI-assisted hunting


### Post — @infinitelogins — 2026-01-25 20:31 UTC (2026-01-25 21:31 WAT)

- URL: https://x.com/infinitelogins/status/2015522842583142599
- Metrics (at fetch): bookmark 6, impression 5927, like 14, quote 0, reply 6, retweet 1

> Just stumbled across this AI bot channel and I'm so confused. 4.26m subs, but only 7 videos with a total of 37k views? all videos were published 2 days ago and are AI UGC talking head about the bug bounty niche.. who's behind this? https://t.co/hvnoFztjig


---

## 2026-01-23 · Thread · Burp Suite traffic can be fed directly to an LLM for passive analysis using the MCP protocol. In thi


Tags (automatic): AI-assisted hunting


### Post — @infinitelogins — 2026-01-23 14:00 UTC (2026-01-23 15:00 WAT)

- URL: https://x.com/infinitelogins/status/2014699833588682904
- Metrics (at fetch): bookmark 359, impression 17530, like 361, quote 2, reply 8, retweet 64

> Burp Suite traffic can be fed directly to an LLM for passive analysis using the MCP protocol. In this article by @Six2dez1, the researcher outlines a setup that connects Burp's MCP Server to Codex CLI through a local reverse proxy to bypass header and origin restrictions,


### Thread part 2 — @infinitelogins — 2026-01-24 23:39 UTC (2026-01-25 00:39 WAT)

- URL: https://x.com/infinitelogins/status/2015207755590795353
- Metrics (at fetch): bookmark 0, impression 364, like 1, quote 0, reply 0, retweet 0

> @Six2dez1 By the way, I feature more content like this on my newsletter https://t.co/P2Zjyh57Bs


---

## 2026-01-23 · Post · A cookie signature validation bypass in ElysiaJS allowed attackers to forge signed cookies and bypas


### Post — @infinitelogins — 2026-01-23 00:00 UTC (2026-01-23 01:00 WAT)

- URL: https://x.com/infinitelogins/status/2014488344042831972
- Metrics (at fetch): not returned

> A cookie signature validation bypass in ElysiaJS allowed attackers to forge signed cookies and bypass authentication. The bug stems from a boolean flag incorrectly initialized to true in the rotation code path, causing the "signature invalid → reject cookie" branch to never trigger.
>
> This means an attacker can set arbitrary cookie values (session=admin) without valid signatures and pass authorization checks.
>
> Full write-up by @0xAsm0d3us👇
>
> https://devansh.bearblog.dev/elysiajs
>
> #BugBounty

**Links in post:** https://devansh.bearblog.dev/elysiajs


---

## 2026-01-22 · Post · A researcher found that the List-Unsubscribe email header, designed to help users leave mailing list


Tags (automatic): XSS, SSRF


### Post — @infinitelogins — 2026-01-22 02:12 UTC (2026-01-22 03:12 WAT)

- URL: https://x.com/infinitelogins/status/2014159121000648945
- Metrics (at fetch): not returned

> A researcher found that the List-Unsubscribe email header, designed to help users leave mailing lists with one click, can become a stored XSS and blind SSRF gadget when webmail clients auto-render unsubscribe buttons. A single malicious email header becomes a cross-surface attack as JavaScript URIs execute when clicked in Horde Webmail (CVE-2025-68673), while server-side unsubscribe handlers in Nextcloud Mail App trigger blind SSRF to internal destinations. 
>
> Full write-up by @_lauritz_  👇
>
> https://security.lauritz-holtmann.de/post/xss-ssrf-list-unsubscribe/
>
> #BugBounty

**Links in post:** https://security.lauritz-holtmann.de/post/xss-ssrf-list-unsubscribe/


---

## 2026-01-19 · Post · This week, Disclosed. BugBounty


Tags (automatic): XSS, SSRF, Race condition, Mobile / Android / iOS, AI-assisted hunting, Platform: HackerOne, Platform: Bugcrowd


### Post — @infinitelogins — 2026-01-19 15:00 UTC (2026-01-19 16:00 WAT)

- URL: https://x.com/infinitelogins/status/2013265352801636600
- Metrics (at fetch): not returned

> This week, Disclosed. #BugBounty
>
> Full issue → http://getDisclosed.com
>
> Highlights below 👇
>
> @samm0uda goes crazy and releases EIGHT write-ups on Meta attack chains, each exploiting different trust boundaries across Facebook and Instagram's authentication, messaging, and analytics infrastructure.
>
> Vote on @portswigger’s Top 10 Web Hacking Techniques of 2025 poll before Jan 22.
>
> @caidoio Year in Review 2025, ten releases from v0.45.0 to v0.54.0; +29 plugins; notable focus on Scanner and GraphQL workflows.
>
> OpenProject public bug bounty launched on @yeswehack, max payout €5,000, a large open-source surface area with auth, permissions, and data exposure failure modes.
>
> @BugbopApp First Year in Review, platform metrics; triage lessons; planned changes around pre-report filtering and report disposition.
>
> @Bugcrowd on adversarial AI usage, phishing and impersonation ops; recon automation; malware development; plus prompt-injection-style abuse in real product surfaces.
>
> @Six2dez1 on Burp Suite MCP Server plus Codex CLI integration, an agent workflow over intercepted HTTP traffic with MCP proxy extraction and local reasoning loops.
>
> @_nikitastupin’s clairvoyance, GraphQL schema recovery even when introspection is disabled; probing heuristics; wordlists; error-driven enumeration for recon pipelines.
>
> @0x0SojalSec released a 1.7B public domains dataset, sorted multi-TLD input for OSINT, large-scale recon, enrichment, and threat intel pipelines.
>
> @xnl_h4ck3r shipped waymore v7.5, IntelX support via Free Academia tier, IntelX data pulled into recon runs without separate tooling glue.
>
> @aacle_ on DNS rebinding bypassing Slack SSRF filters, including a reported $1,000 payout and implementation details around resolution and validation drift.
>
> @ryotkak shared an article on Pwning Claude Code in 8 Different Ways, eight paths to command execution via permission gaps and argument parsing edge cases across Git; sed; Bash expansion; wrapper interpretation.
>
> @_lauritz_ on turning RFC2369 List-Unsubscribe into an SSRF/XSS gadget, stored XSS and blind SSRF primitives in webmail and mail clients via header-driven behaviors.
>
> @0xasm0d3us on an ElysiaJS cookie signature validation bypass, secret handling and rotation pitfalls; PoC and affected code paths with patch guidance.
>
> @yeswehack Dojo #47 APICrash solution, a GraphQL mutation batching race with aliases; concurrent TinyDB-backed file writes corrupt state via thread spawning.
>
> @BourAbdelhadi on Supabase anon JWT exposure found with rep+, validation steps against Supabase APIs 
>
> @sijan2003 on modifying Netflix OTP messages via an unauthenticated endpoint, reversing and instrumenting the Android client to map the OTP trigger flow and messaging risk.
>
> @Hacker0x01 talk with @rez0__  on AI red teaming beyond jailbreak framing, application-level failure modes like prompt injection in product surfaces and evaluation that resembles real usage.
>
> @zack0x01 video on open redirect exploitation, bypass techniques against weak allowlists; normalization and encoding tricks; redirect weaponization.
>
> That's not all. Full links, writeups & more → http://getDisclosed.com
>
> The bug bounty world, curated.

**Links in post:** http://getDisclosed.com


---

## 2026-01-13 · Post · This week, Disclosed. BugBounty (Jan 12, 2026). 


Tags (automatic): XSS, Auth bypass, RCE, AI-assisted hunting, Platform: HackerOne, Platform: Bugcrowd


### Post — @infinitelogins — 2026-01-13 00:06 UTC (2026-01-13 01:06 WAT)

- URL: https://x.com/infinitelogins/status/2010865879115055376
- Metrics (at fetch): bookmark 6, impression 2096, like 16, quote 0, reply 1, retweet 3

> This week, Disclosed. #BugBounty (Jan 12, 2026). 
>
> Full issue → http://getDisclosed.com
>
> Highlights below 👇
>
> @portswigger opened nominations for the Top 10 Web Hacking Techniques of 2025, focused on reusable techniques published over the year.
>
> @yeswehack released its 2025 Top Bounty Hunters leaderboard, a snapshot of high-volume platform activity and rankings.
>
> @github posted December 2025 bug bounty metrics, including total payouts and report volume, with the submission portal link.
>
> @TheHackersNews flagged a critical authenticated RCE in n8n, CVE-2026-21877, CVSS 10.0, with full instance compromise impact.
>
> @Bugcrowd shared details on its report validation process, centered on what reduces back-and-forth during triage.
>
> @intigriti announced an Office Hours podcast series with live Q&A sessions across Discord and X Spaces.
>
> @hemi_xyz launched a public bug bounty program on @Bugcrowd, adding new scope for researchers tracking new programs.
>
> @yeswehack announced a public Keycloak bug bounty with a white-box setup and bounties up to €5,000.
>
> @njcve_ posted logistics for a HackerOne Manchester in-person event on Jan 31.
>
> @bbcbd_official shared the timeline for HackerOne BUG HUNT 2026, including finalist arrival, competition hours, and conference check-in.
>
> @_jensec shared a Burp extension that extracts endpoints; file paths; emails; and occasional secrets from minified JavaScript.
>
> @elder_plinius posted LeakHub, a crowd-sourced workflow for verifying leaked system prompts against fresh chats.
>
> @OriginalSicksec released altdns-ng, a Go reimplementation for high-throughput subdomain permutation with wildcard detection and DoH support.
>
> @terjanq published Tiny XSS Payloads, a compact reference of minimal probes annotated by execution context and browser constraints.
>
> @caidoio shipped Caido v0.54.0 with HTTPQL autocompletion based on past queries.
>
> @xnl_h4ck3r pushed GAP Burp Extension v6.3, regex updates and performance fixes aimed at reducing memory growth in long sessions.
>
> @xnl_h4ck3r also shipped xnLinkFinder v7.14 with PDF-to-text parsing for endpoint extraction, calling out poppler-utils as a preferred backend.
>
> @xnl_h4ck3r released xnldorker v4.0 with DuckDuckGo Lite support and CAPTCHA detection improvements.
>
> @intigriti highlighted a Content-Type CSRF bypass angle against JSON-only APIs when servers fail to enforce strict Content-Type handling.
>
> @amrelsagaei released a video on Client Side postMessage bugs, origin validation failures, and unsafe sinks leading to XSS and data leakage.
>
> @ctbbpodcast published http://bugbounty.forum Q&A Ep. 156, including discussion of the Cross-Site ETag Length Leak and Clawdbot.
>
> @slonser_ wrote Never Trust the Output, showing how malicious MCP server responses can pollute AI agent outputs when JSON is treated as free-form text.
>
> @dreyand_ published an OpenFlagr <= 1.1.18 authentication bypass writeup, tracked as CVE-2026-0650, derived from quick code review and patch analysis.
>
> @xchopath detailed a $3,500 HTML injection chain via CSRF-like abuse, using stored HTML and missing token defenses to drive privileged actions.
>
> @af4himi walked through LFI escalating to root RCE via a leaked SSH private key, a clean example of read-only primitives becoming full compromise.
>
> Full links, write-ups & more → http://getDisclosed.com
>
> The bug bounty world, curated.

**Links in post:** http://getDisclosed.com, http://bugbounty.forum


---

## 2026-01-11 · Post · This week, Disclosed. BugBounty covers @PortSwigger’s call for Top 10 Web Hacking Techniques of 202


### Post — @infinitelogins — 2026-01-11 22:34 UTC (2026-01-11 23:34 WAT)

- URL: https://x.com/infinitelogins/status/2010480453300711456
- Metrics (at fetch): not returned

> This week, Disclosed. #BugBounty covers @PortSwigger’s call for Top 10 Web Hacking Techniques of 2025, @yeswehack’s 2025 Top Bounty Hunters leaderboard, December 2025 program stats from @github, and more. Subscribe at http://getDisclosed.com to be first to read it.

**Links in post:** http://getDisclosed.com


---

## 2026-01-06 · Post · This week, Disclosed. (January 5, 2026) BugBounty 


Tags (automatic): XSS, SSRF, Account takeover, Auth bypass, RCE, CSP / CSPT, AI-assisted hunting, Platform: HackerOne, Platform: Bugcrowd


### Post — @infinitelogins — 2026-01-06 01:29 UTC (2026-01-06 02:29 WAT)

- URL: https://x.com/infinitelogins/status/2008350101169946633
- Metrics (at fetch): not returned

> This week, Disclosed. (January 5, 2026) #BugBounty 
>
> New MVH crowned. A million dollar WAF hardening payout, a /health endpoint turning into a credential leak, and a ZIP upload workflow producing two criticals.
>
> Full issue → http://getDisclosed.com
>
> Preview below 👇
>
> @vercel detailed a $1M paid effort with @Hacker0x01 to pressure-test and harden its WAF against React2Shell-class bypasses, including runtime mitigation and detection changes.
>
> @pxmme1337 linked a newly launched anonymous forum for bug bounty discussions, with an optional verification mechanism aimed at proving bounty earnings.
>
> @Hacker0x01 announced @alexbindrei as Most Valuable Hacker of H1-3120, framed around AI security research.
>
> @Bugcrowd published a practical mapping of RCE pathways and detection methods, including command injection sinks; unsafe eval patterns; SSTI routes.
>
> @intigriti  CSP bypass material focused on permissive source expressions; nonce and hash misuse; overbroad allowlists that still land script execution or exfiltration.
>
> @PortSwiggerRes published new SAML authentication bypass techniques tied to parser differentials in Ruby and PHP, including attribute pollution; namespace confusion; Void Canonicalization.
>
> @aretekzs wrote up a chain from self-XSS constraints to account takeover via DOM injection plus login CSRF and cookie-tossing effects on auth state.
>
> @xnl_h4ck3r shipped xnldorker v3.2 with Google Custom Search support and configuration changes aimed at smoother dorking workflows.
>
> @zack0x01 released video material on broken access control testing and a recon workflow overview spanning asset discovery; prioritization; validation loops.
>
> @medusa_0xf published a 2026 learning roadmap video centered on web and API hacking structure, with labs and category coverage.
>
> @ctbbpodcast dropped “2025 Hacker Stats & 2026 Goals (Ep. 155)”, reflecting on 2025 trends and predictions for 2026 workflows and disclosure dynamics.
>
> @NahamSec shared a 2025 findings retrospective video, focused on what made specific bugs interesting rather than full reproduction detail.
>
> @H4cktus published “Can you compromise a multi-billion dollar company via /health?”, centered on a health check surface exposing environment variables and sensitive cloud configuration.
>
> @_bergee_ published “Two crits, one zip”, two critical issues in a ZIP upload workflow, including symlink-based file access and a path to RCE via unsafe extraction processing.
>
> @J0R1AN walked through the Intigriti December XSS Challenge (1225), using browser behaviors like iframe messaging; performance entries; regex edge cases.
>
> @ptswarm research covered HTML-to-PDF generation stacks as a trust boundary that repeatedly turns into SSRF; local file disclosure; deserialization; DoS.
>
> This is just a preview. Full links, write-ups & more → http://getDisclosed.com
>
> The bug bounty world, curated.

**Links in post:** http://getDisclosed.com


---

## 2026-01-05 · Post · Teaser: Bug bounty gets an anon forum from @pxmme1337, plus @vercel on a $1M WAF hardening effort wi


Tags (automatic): Platform: HackerOne


### Post — @infinitelogins — 2026-01-05 02:09 UTC (2026-01-05 03:09 WAT)

- URL: https://x.com/infinitelogins/status/2007997811548443016
- Metrics (at fetch): not returned

> Teaser: Bug bounty gets an anon forum from @pxmme1337, plus @vercel on a $1M WAF hardening effort with @Hacker0x01 vs React2Shell bypasses.
>
> Writeups include a /health endpoint compromise from @H4cktus and more.
>
> Subscribe to get it when it drops 👉 http://getdisclosed.com

**Links in post:** http://getdisclosed.com


---

## 2026-01-05 · Post · 2025 was wild. I launched the Disclosed newsletter, ran the 2nd Bug Bounty Village at DEF CON, got p


Tags (automatic): Platform: HackerOne


### Post — @infinitelogins — 2026-01-05 02:04 UTC (2026-01-05 03:04 WAT)

- URL: https://x.com/infinitelogins/status/2007996568977506534
- Metrics (at fetch): not returned

> 2025 was wild. I launched the Disclosed newsletter, ran the 2nd Bug Bounty Village at DEF CON, got promoted at HackerOne, and traveled to 5 countries. 
>
> Burnout hit hard, but I’m back, refocused, and building with intent. More to come soon.
>
> Happy New Year everyone!


---

## 2025-10-10 · Post · This week, Disclosed. BugBounty


Tags (automatic): AI-assisted hunting, Platform: HackerOne


### Post — @infinitelogins — 2025-10-10 14:34 UTC (2025-10-10 15:34 WAT)

- URL: https://x.com/infinitelogins/status/1976657586318610608
- Metrics (at fetch): bookmark 6, impression 3350, like 40, quote 0, reply 1, retweet 7

> This week, Disclosed. #BugBounty
>
> H1-65 Singapore &amp; H1-468 Stockholm winners, new H1-Elites, Google’s AI VRP, YesWeHack wins EU tender, new programs, tools, write-ups &amp; videos — and more.
>
> Full issue → https://t.co/P2Zjyh57Bs
>
> Highlights below 👇
>
> @tiktok_us &amp; @okx H1-65


---

## 2025-09-14 · Post · This week, Disclosed. BugBounty


Tags (automatic): SSRF, RCE, OAuth, AI-assisted hunting, Platform: Bugcrowd


### Post — @infinitelogins — 2025-09-14 00:32 UTC (2025-09-14 01:32 WAT)

- URL: https://x.com/infinitelogins/status/1967023640048005132
- Metrics (at fetch): bookmark 20, impression 6828, like 66, quote 0, reply 0, retweet 7

> This week, Disclosed. #BugBounty
>
> Nullcon Berlin winners, Bugcrowd’s $30K Hacker Showdown, AI-powered zero-days, ChatGPT email exploit, PortSwigger milestone rewards, new programs, write-ups on RCE, SSRF &amp; OAuth flaws, plus upgraded tools and bounty tips.
>
> Full issue →


---

## 2025-09-01 · Post · This week, Disclosed. BugBounty


Tags (automatic): SSRF, Mobile / Android / iOS, AI-assisted hunting


### Post — @infinitelogins — 2025-09-01 00:39 UTC (2025-09-01 01:39 WAT)

- URL: https://x.com/infinitelogins/status/1962314418769060324
- Metrics (at fetch): bookmark 22, impression 6121, like 49, quote 0, reply 5, retweet 10

> This week, Disclosed. #BugBounty
>
> Spotlight on Android labs, LLM “sleeper” agents, big bounties for NGINX &amp; GPT‑5, Zoomtopia &amp; IoT hackathons, write‑ups on SSRF, UUID takeover &amp; RXSS escalation, plus upgraded tools and hunting tips.
>
> Full issue → https://t.co/P2Zjyh57Bs


---

## 2025-08-30 · Thread · If an attacker pre-registers victim@gmail.com on an app (no email verification), then the real user 


Tags (automatic): OAuth


### Post — @infinitelogins — 2025-08-30 15:37 UTC (2025-08-30 16:37 WAT)

- URL: https://x.com/infinitelogins/status/1961815630472229110
- Metrics (at fetch): bookmark 128, impression 22527, like 159, quote 0, reply 20, retweet 6

> If an attacker pre-registers victim@gmail.com on an app (no email verification), then the real user later signs in with Google OAuth, the app merges accounts. 
>
> Attacker keeps password access + victim uses OAuth. 
>
> Real vuln? What's the impact?


### Thread part 2 — @infinitelogins — 2025-08-30 15:38 UTC (2025-08-30 16:38 WAT)

- URL: https://x.com/infinitelogins/status/1961815848764821721
- Metrics (at fetch): bookmark 0, impression 2144, like 0, quote 0, reply 2, retweet 0

> How would you rate severity in this case?


---

## 2025-08-23 · Post · This week, Disclosed. BugBounty


Tags (automatic): AI-assisted hunting


### Post — @infinitelogins — 2025-08-23 23:28 UTC (2025-08-24 00:28 WAT)

- URL: https://x.com/infinitelogins/status/1959397320560414874
- Metrics (at fetch): bookmark 29, impression 7689, like 59, quote 1, reply 5, retweet 17

> This week, Disclosed. #BugBounty
>
> Spotlight on CodeRabbit Exploit, NahamSec’s DEF CON vlog, Swiss Post’s €230K challenge, new tools for hunters, and more.
>
> Full issue → https://t.co/Affe2Yws7J
>
> Highlights below 👇
>
> @KudelskiSec details how vulnerabilities in CodeRabbit’s AI


---

## 2025-08-17 · Post · I’ve been asked: “Will Bug Bounty Village (@BugBountyDEFCON) return?”


### Post — @infinitelogins — 2025-08-17 01:45 UTC (2025-08-17 02:45 WAT)

- URL: https://x.com/infinitelogins/status/1956895124665078117
- Metrics (at fetch): bookmark 9, impression 4551, like 101, quote 0, reply 3, retweet 6

> I’ve been asked: “Will Bug Bounty Village (@BugBountyDEFCON) return?”
> The short answer: yes!
>
> This post is overdue, but I want to thank everyone who visited us at Bug Bounty Village last week. THANK YOU!
>
> Over six months of planning went into three days. In that time, we hosted


---

## 2025-08-03 · Post · This week, Disclosed. BugBounty


Tags (automatic): AI-assisted hunting


### Post — @infinitelogins — 2025-08-03 21:16 UTC (2025-08-03 22:16 WAT)

- URL: https://x.com/infinitelogins/status/1952116475516575866
- Metrics (at fetch): bookmark 6, impression 3007, like 33, quote 0, reply 0, retweet 5

> This week, Disclosed. #BugBounty
>
> My projects featured on Critical Thinking, $1M WhatsApp Bounty, AI Exploit for CVE-2025-32433, Bug Bounty Village CTF Prizes, and More.
>
> Full issue → https://t.co/Affe2Yws7J
>
> Highlights below 👇
>
> @infinitelogins and @arl_rose discuss building


---

## 2025-08-03 · Post · This week, Disclosed. BugBounty


Tags (automatic): AI-assisted hunting


### Post — @infinitelogins — 2025-08-03 21:11 UTC (2025-08-03 22:11 WAT)

- URL: https://x.com/infinitelogins/status/1952115126238314750
- Metrics (at fetch): bookmark 0, impression 61, like 1, quote 0, reply 1, retweet 0

> This week, Disclosed. #BugBounty
>
> My projects featured on Critical Thinking, $1M WhatsApp Bounty, AI Exploit for CVE-2025-32433, Bug Bounty Village CTF Prizes, and More.
>
> Full issue → https://t.co/Affe2Yws7J
>
> Highlights below 👇
>
> ## SPOTLIGHT
>
> @infinitelogins and @arl_rose


---

## 2025-07-29 · Post · Any bug bounty hunters attending Hacker Summer Camp and interested in the Vulnerability Vibes event?


### Post — @infinitelogins — 2025-07-29 22:13 UTC (2025-07-29 23:13 WAT)

- URL: https://x.com/infinitelogins/status/1950318856402276532
- Metrics (at fetch): bookmark 10, impression 2458, like 36, quote 0, reply 2, retweet 0

> Any bug bounty hunters attending Hacker Summer Camp and interested in the Vulnerability Vibes event? I have a couple tickets to give away. Depending on interest, may need to pick somebody at random. https://t.co/AvkDd2QtdO


---

## 2025-07-26 · Post · We're less than two weeks away from @defcon, and all the hard work and hundreds of hours poured into


### Post — @infinitelogins — 2025-07-26 18:16 UTC (2025-07-26 19:16 WAT)

- URL: https://x.com/infinitelogins/status/1949171966935748643
- Metrics (at fetch): not returned

> We're less than two weeks away from @defcon, and all the hard work and hundreds of hours poured into Bug Bounty Village this year are about to be on full display. Some highlights I'm incredibly proud of:
>
> 50+ Distinguished Speakers
> 35+ Sessions
> Our Inaugural CTF
> Hacker Hangout Happy Hour
> Insane Swag Designs (challenge coins, electronic badges, and more)
>
> Huge shout-out to @yaser_s, @thejillboss, and @H1LeoW for all your help preparing for @BugBountyDEFCON this year. @Arl_rose and I truly couldn’t have done it without you.
>
> If you're coming to DEF CON 33, please make sure to stop by the Bug Bounty Village. Can't wait to see you all there!


---

## 2025-07-21 · Post · This week, Disclosed. BugBounty


Tags (automatic): XSS, SQL injection, SSRF, IDOR / BOLA, Account takeover, Auth bypass, RCE, Race condition, Memory corruption / native, AI-assisted hunting, Platform: HackerOne, Platform: Bugcrowd, Platform: HackenProof


### Post — @infinitelogins — 2025-07-21 14:50 UTC (2025-07-21 15:50 WAT)

- URL: https://x.com/infinitelogins/status/1947308269716087190
- Metrics (at fetch): not returned

> This week, Disclosed. #BugBounty
>
> DEF CON 33 Badge Pre-Orders, Bug Bounty Village Agenda, HackAICon Announcement, NullCon Scholarships, Caido Acquires Shift, and more
>
> Highlights below 👇
>
> Full issue → https://getdisclosed.com
>
> @BugBountyDEFCON opened pre-orders for a limited edition Bug Bounty Village badge in a green variant. Pre-order online and pick up in person at the con.
>
> @CaidoIO acquired the Shift plugin, now free for users with payload crafting and HTTPQL support.
>
> @BugBountyDEFCON released the full agenda for Bug Bounty Village at DEF CON 33.
>
> @0xacb announced HackAICon 2025 (Sept 25, Lisbon), featuring AI, hacking challenges, talks, and networking.
>
> @nullcon is offering Bug Bounty Hunter Scholarships for their Berlin event (Sep 4–5). Apply by July 28.
>
> @hackenproof announced a new bug bounty program for No Ones App with rewards up to $5k per bug.
>
> @xss0r shared 6 new @Microsoft domains now eligible for the Identity Bug Bounty program.
>
> @yeswehack posted highlights from the live hacking event at leHACK 2025 in a recap video.
>
> @Hacker0x01 updates their in-platform color scheme to align better with their updated marketing site.
>
> PwnFox (via @BApp_Store) adds multi-session, color-coded testing in Burp Suite.
>
> @garethheyes announces Custom Actions to automate request rewriting and payload generation in Burp Suite.
>
> @fneves97 updated JXScout Pro for improved JavaScript asset navigation in VSCode.
>
> @adce626 launched the Bug Bounty Recon Toolkit, which generates commands for 50+ tools based on target.
>
> @KN0X55 introduced XSS Gym to train on real XSS payloads and scenarios.
>
> @alicanact60 published a Chrome extension that restores the classic HackerOne UI.
>
> From .git disclosure to RCE. The author details a full bug bounty chain from initial .git leak to remote code execution, with techniques and tools.
>
> Leaking PII in Microsoft Guest Check-In. The author (Faav) shows how exposed PII and Burp Suite let them break into Microsoft buildings.
>
> HackerOne report by @MrMax4o4 documents how a banned user retained API access to a deleted account, exposing weak access controls.
>
> @deadoverflow_  explains a race condition in Reddit’s coin API inflating coins via parallel requests.
>
> @medusa_0xf highlights business logic vulnerabilities that led to real payouts.
>
> @NahamSec shows JWT mistakes that enabled account takeover and big bounties.
>
> @amrelsagaei interviews @NahamSec on mindset, overcoming plateaus, and building a personal brand.
>
> BePractical demonstrates exploiting zip slip on file uploads to overwrite paths.
>
> @Magn4_ shares the story of earning his first bounty with a $100 open redirect.
>
> @ctbbpodcast Ep.131 features live SSRF and IDOR hacks, leaked secrets, Google’s defense strategy, and community insights.
>
> @cyb3r_dan shares an SQLi detection guide covering manual and automated techniques with practice labs.
>
> @Bugcrowd explains how to find bugs on hardened targets by chaining smaller flaws.
>
> @coffinxp7 publishes an advanced bug bounty recon checklist.
>
> @intigriti introduces GitHub dorking with search patterns to uncover vulnerabilities.
>
> @clintgibler highlights Check Point’s discovery of malware using prompt injection.
>
> @40sp3l reminds hunters not to skip targets just because they have many reports — good bugs still remain.
>
> @0xacb points out that Chrome’s upcoming features could open up new bypass techniques.
>
> @njcve_  shares success at SteelCon where an authentication bypass bug was found.
>
> @intigriti explains 3 exploitable and highly rewarded vulnerabilities in detail.
>
> @Bugcrowd offers 5 actionable tips for beginners breaking into cybersecurity.
>
> Full links, tools, write-ups & more → https://getdisclosed.com
>
> The bug bounty world, curated.

**Links in post:** https://getdisclosed.com


---

## 2025-07-21 · Post · This week, Disclosed. BugBounty


Tags (automatic): XSS, SQL injection, SSRF, IDOR / BOLA, Account takeover, Auth bypass, RCE, Race condition, Memory corruption / native, AI-assisted hunting, Platform: HackerOne, Platform: Bugcrowd, Platform: HackenProof


### Post — @infinitelogins — 2025-07-21 14:29 UTC (2025-07-21 15:29 WAT)

- URL: https://x.com/infinitelogins/status/1947302951154016629
- Metrics (at fetch): not returned

> This week, Disclosed. #BugBounty
>
> DEF CON 33 Badge Pre-Orders, Bug Bounty Village Agenda, HackAICon Announcement, NullCon Scholarships, Caido Acquires Shift, and more
>
> Highlights below 👇
>
> Full issue → https://getdisclosed.com
>
> ------------
> SPOTLIGHT
>
> @BugBountyDEFCON opened pre-orders for a limited edition Bug Bounty Village badge in a green variant. Pre-order online and pick up in person at the con.
>
> @CaidoIO acquired the Shift plugin, now free for users with payload crafting and HTTPQL support.
>
> @BugBountyDEFCON released the full agenda for Bug Bounty Village at DEF CON 33.
>
> @0xacb announced HackAICon 2025 (Sept 25, Lisbon), featuring AI, hacking challenges, talks, and networking.
>
> ------------
> UPDATES
>
> @nullcon is offering Bug Bounty Hunter Scholarships for their Berlin event (Sep 4–5). Apply by July 28.
>
> @hackenproof announced a new bug bounty program for No Ones App with rewards up to $5k per bug.
>
> @xss0r shared 6 new @Microsoft domains now eligible for the Identity Bug Bounty program.
>
> @yeswehack posted highlights from the live hacking event at leHACK 2025 in a recap video.
>
> @Hacker0x01 updates their in-platform color scheme to align better with their updated marketing site.
>
> ------------
> TOOLS
>
> PwnFox (via @BApp_Store) adds multi-session, color-coded testing in Burp Suite.
>
> @garethheyes announces Custom Actions to automate request rewriting and payload generation in Burp Suite.
>
> @fneves97 updated JXScout Pro for improved JavaScript asset navigation in VSCode.
>
> @adce626 launched the Bug Bounty Recon Toolkit, which generates commands for 50+ tools based on target.
>
> @KN0X55 introduced XSS Gym to train on real XSS payloads and scenarios.
>
> @alicanact60 published a Chrome extension that restores the classic HackerOne UI.
>
> ------------
> WRITE UPS
>
> From .git disclosure to RCE. The author details a full bug bounty chain from initial .git leak to remote code execution, with techniques and tools.
>
> Leaking PII in Microsoft Guest Check-In. The author (Faav) shows how exposed PII and Burp Suite let them break into Microsoft buildings.
>
> HackerOne report by @MrMax4o4 documents how a banned user retained API access to a deleted account, exposing weak access controls.
>
> ------------
> VIDEOS
>
> @deadoverflow_  explains a race condition in Reddit’s coin API inflating coins via parallel requests.
>
> @medusa_0xf highlights business logic vulnerabilities that led to real payouts.
>
> @NahamSec shows JWT mistakes that enabled account takeover and big bounties.
>
> @amrelsagaei interviews @NahamSec on mindset, overcoming plateaus, and building a personal brand.
>
> BePractical demonstrates exploiting zip slip on file uploads to overwrite paths.
>
> @Magn4_ shares the story of earning his first bounty with a $100 open redirect.
>
> @ctbbpodcast Ep.131 features live SSRF and IDOR hacks, leaked secrets, Google’s defense strategy, and community insights.
>
> ------------
> LEARN
>
> @cyb3r_dan shares an SQLi detection guide covering manual and automated techniques with practice labs.
>
> @Bugcrowd explains how to find bugs on hardened targets by chaining smaller flaws.
>
> @coffinxp7 publishes an advanced bug bounty recon checklist.
>
> @intigriti introduces GitHub dorking with search patterns to uncover vulnerabilities.
>
> @clintgibler highlights Check Point’s discovery of malware using prompt injection.
>
> ------------
> TWEETS
>
> @40sp3l reminds hunters not to skip targets just because they have many reports — good bugs still remain.
>
> @0xacb points out that Chrome’s upcoming features could open up new bypass techniques.
>
> @njcve_  shares success at SteelCon where an authentication bypass bug was found.
>
> @intigriti explains 3 exploitable and highly rewarded vulnerabilities in detail.
>
> @Bugcrowd offers 5 actionable tips for beginners breaking into cybersecurity.
>
> Full links, tools, write-ups & more → https://getdisclosed.com
>
> The bug bounty world, curated.

**Links in post:** https://getdisclosed.com


---

## 2025-07-14 · Post · This week, Disclosed. BugBounty


### Post — @infinitelogins — 2025-07-14 03:16 UTC (2025-07-14 04:16 WAT)

- URL: https://x.com/infinitelogins/status/1944596854228066808
- Metrics (at fetch): not returned

> This week, Disclosed. #BugBounty
>
> McDonald’s chatbot vuln, Django ORM injection stealing crypto, refresh tools &amp; writeups from , Okta &amp; Swiss Post bounties, and more.
>
> Highlights below 🧵


---

## 2025-07-07 · Post · tbh I didn't even want to do a CTF. 


Tags (automatic): AI-assisted hunting


### Post — @infinitelogins — 2025-07-07 21:53 UTC (2025-07-07 22:53 WAT)

- URL: https://x.com/infinitelogins/status/1942341272091648048
- Metrics (at fetch): not returned

> tbh I didn't even want to do a CTF. 
>
> I felt like they have been overdone and often were not realistic to what you would see in the real world
>
> That’s why, when @Arl_rose and I started thinking about how to make this one special, we knew we wanted it to feel like a real-life vulnerable web app. Something similar to @owasp_juiceshop.
>
> And while juiceshop is cool, we wanted to be able to give it the real "bug bounty" vibe. Writing reports, getting rewarded for good write-ups, dealing with triage, maybe even getting hit with a dupe.
>
> As we wrote out the idea and started talking to vendors, I honestly didn’t think we could actually pull it off with the time and budget we had.
>
> Then we met the folks at @CTFae and we could just tell immediately that they were the right partners for this project. 
>
> The scope quickly grew beyond just a single vulnerable web app to an interconnected ecosystem of vulnerable infrastructure: web, APIs, even LLM assets.
>
> If you like bug bounty and hate CTFs, this is for you.
>
> If you love CTFs but don’t know about bug bounty, this is also for you.
>
> Seriously I am so excited for this.
>
> Register at http://bbv.ctf.ae

**Links in post:** https://twitter.com/BugBountyDEFCON/status/1941557975128101308, http://bbv.ctf.ae

**Quoted post (full text):**

    #### Quoted post — @1773496655209533440 — 2025-07-05 18:01 UTC (2025-07-05 19:01 WAT)
    
    - URL: https://x.com/1773496655209533440/status/1941557975128101308
    - Metrics (at fetch): not returned
    
    > Big news: For the first time, Bug Bounty Village is hosting a CTF competition with our partners @CTFae! Get ready for a unique challenge at DEF CON 33. Pre-register now at https://bbv.ctf.ae
    >
    > Here's what makes it different: 👇
    >
    > #BugBounty #CTF #DEFCON [pic.x.com/C96yq2W98Y]
    
    **Media:**
    - media `3_1941557971567120384` (details not returned by the API)
    
    **Links in post:** https://bbv.ctf.ae
    


---

## 2025-07-07 · Post · This week, Disclosed. BugBounty 


Tags (automatic): XSS


### Post — @infinitelogins — 2025-07-07 00:04 UTC (2025-07-07 01:04 WAT)

- URL: https://x.com/infinitelogins/status/1942011815283793924
- Metrics (at fetch): not returned

> This week, Disclosed. #BugBounty 
>
> Career insights from @zhero___  &amp; @Geluchat, @BugBountyDEFCON badge &amp; CTF announcements, new tools, XXE &amp; XSS write-ups, and more.
>
> Highlights below 🧵


---

## 2025-07-06 · Post · Anybody vibe code their own bug bounty dashboard? Would love to see it.


### Post — @infinitelogins — 2025-07-06 22:07 UTC (2025-07-06 23:07 WAT)

- URL: https://x.com/infinitelogins/status/1941982290684620990
- Metrics (at fetch): not returned

> Anybody vibe code their own bug bounty dashboard? Would love to see it.


---

## 2025-07-05 · Post · Once you understand bug bounty, you never see the internet the same way.


### Post — @infinitelogins — 2025-07-05 03:02 UTC (2025-07-05 04:02 WAT)

- URL: https://x.com/infinitelogins/status/1941331916294324461
- Metrics (at fetch): not returned

> Once you understand bug bounty, you never see the internet the same way.


---

## 2025-07-03 · Post · A popular AI Slack integration leaked secrets through link unfurling.


Tags (automatic): AI-assisted hunting


### Post — @infinitelogins — 2025-07-03 21:38 UTC (2025-07-03 22:38 WAT)

- URL: https://x.com/infinitelogins/status/1940888021374849294
- Metrics (at fetch): not returned

> A popular AI Slack integration leaked secrets through link unfurling.
>
> A single prompt injection exfiltrated sensitive data to an attacker-controlled server with no click required.
>
> Here’s how @wunderwuzzi23 explained it.
>
> Breakdown in thread 🧵


---

## 2025-07-01 · Post · This week, Disclosed. BugBounty


Tags (automatic): XSS, AI-assisted hunting


### Post — @infinitelogins — 2025-07-01 05:38 UTC (2025-07-01 06:38 WAT)

- URL: https://x.com/infinitelogins/status/1939921416813428996
- Metrics (at fetch): not returned

> This week, Disclosed. #BugBounty
>
> LLMs for recon and exploits, Xbow hits #1, DEF CON speaker drops, real-world XSS, and more.
>
> Highlights below 🧵


---

## 2025-06-28 · Post · Regex bugs in domain-restricted signups are still out there. 


### Post — @infinitelogins — 2025-06-28 17:57 UTC (2025-06-28 18:57 WAT)

- URL: https://x.com/infinitelogins/status/1939020437050270168
- Metrics (at fetch): not returned

> Regex bugs in domain-restricted signups are still out there. 
>
> @yppip wrote a blog post about a recent Cognito misconfig that let attackers sign up with fake emails like user@maliciousexample.com and get full access.
>
> Let’s break it down. 🧵 #BugBounty


---

## 2025-06-24 · Post · This week, Disclosed. bugbounty 


Tags (automatic): XSS, SSRF


### Post — @infinitelogins — 2025-06-24 14:40 UTC (2025-06-24 15:40 WAT)

- URL: https://x.com/infinitelogins/status/1937521334608888201
- Metrics (at fetch): not returned

> This week, Disclosed. #bugbounty 
>
> SSRF redirect tricks, Spaceraccoon’s book, YesWeCaido, and tools for XSS, origin IPs, and bounty tracking.
>
> Highlights below 🧵


---

## 2025-06-19 · Post · This week’s Disclosed. BugBounty 


Tags (automatic): XSS, RCE, Request smuggling / desync, AI-assisted hunting


### Post — @infinitelogins — 2025-06-19 05:15 UTC (2025-06-19 06:15 WAT)

- URL: https://x.com/infinitelogins/status/1935567096320291027
- Metrics (at fetch): not returned

> This week’s Disclosed. #BugBounty 
>
> Beta invite for Hai, the AI security agent for hackers. RCE on Netflix. New tools for XSS, subdomain monitoring, and HTTP smuggling. Plus: SSTI, IDN homographs, and more.
>
> Highlights below 🧵


---

## 2025-06-10 · Post · This week, Disclosed.


Tags (automatic): SSRF, OAuth


### Post — @infinitelogins — 2025-06-10 17:54 UTC (2025-06-10 18:54 WAT)

- URL: https://x.com/infinitelogins/status/1932496572602036228
- Metrics (at fetch): not returned

> This week, Disclosed.
>
> Shubs wins the LHE with Salesforce. Free NahamCon talks. Tools for fuzzing, IP whitelisting, and JWT automation. Plus: SSRF in Lichess, OAuth deep dives, and the return of leHACK.
>
> Full issue + links → http://getdisclosed.com
>
> Highlights below 🧵

**Links in post:** http://getdisclosed.com


---

## 2025-06-03 · Post · This week’s Disclosed.


Tags (automatic): Platform: HackerOne


### Post — @infinitelogins — 2025-06-03 22:23 UTC (2025-06-03 23:23 WAT)

- URL: https://x.com/infinitelogins/status/1930027710837076016
- Metrics (at fetch): not returned

> This week’s Disclosed.
>
> What 100 HackerOne reports reveal about modern bug hunting. Meta’s exclusive bounty. Prompt injection in GitLab. And More.
>
> Full issue + links → http://getdisclosed.com
>
> Highlights below 🧵

**Links in post:** http://getdisclosed.com


---

## 2025-06-01 · Post · I vibe coded and shipped an app in three days. It got hacked. Twice. Here’s what I learned.  🧵


### Post — @infinitelogins — 2025-06-01 03:30 UTC (2025-06-01 04:30 WAT)

- URL: https://x.com/infinitelogins/status/1929017755136561402
- Metrics (at fetch): not returned

> I vibe coded and shipped an app in three days. It got hacked. Twice. Here’s what I learned.  🧵


---

## 2025-05-30 · Post · Shout out to @Kr1shna4garwal and @Goofygiraffe06 for responsibly disclosing a couple of misconfigura


### Post — @infinitelogins — 2025-05-30 04:21 UTC (2025-05-30 05:21 WAT)

- URL: https://x.com/infinitelogins/status/1928305852944916658
- Metrics (at fetch): not returned

> Shout out to @Kr1shna4garwal and @Goofygiraffe06 for responsibly disclosing a couple of misconfigurations I had on https://disclosedonline.com. 
>
> Making software for hackers is scary, but it's pretty awesome when the bug bounty community comes together to help each other.

**Links in post:** https://disclosedonline.com


---

## 2025-05-30 · Post · I've been working on something behind the scenes for the past couple of months, and I'm finally read


### Post — @infinitelogins — 2025-05-30 01:10 UTC (2025-05-30 02:10 WAT)

- URL: https://x.com/infinitelogins/status/1928257570738950182
- Metrics (at fetch): not returned

> I've been working on something behind the scenes for the past couple of months, and I'm finally ready to share it.
>
> Disclosed. A curated newsletter about the bug bounty world.
> https://getdisclosed.com/subscribe
>
> Over the last four weeks, I've been quietly publishing weekly issues and gathering feedback from a small group of readers. Thank you all for your insights as I iterated and found my voice.
>
> Now that it’s public, I’d love for you to check it out and share your thoughts. The goal is to deliver high-quality weekly updates for the bug bounty and security community, covering programs, events, write-ups, and learning resources.
>
> Huge thanks to @rez0__ , @gr3pme, @Arl_rose, @VailSec, @Akshanshjaiswl, @Shlibness, @0xroot, and many others for your early feedback and support. 
>
> #BugBounty #Disclosed #Infosec

**Links in post:** https://getdisclosed.com/subscribe


---

## 2025-05-30 · Post · I've been working on something behind the scenes for the past couple of months, and I'm finally read


### Post — @infinitelogins — 2025-05-30 01:04 UTC (2025-05-30 02:04 WAT)

- URL: https://x.com/infinitelogins/status/1928256255203917899
- Metrics (at fetch): not returned

> I've been working on something behind the scenes for the past couple of months, and I'm finally ready to share it.
>
> Disclosed. A curated newsletter about the bug bounty world.
> https://getdisclosed.com/subscribe
>
> Over the last four weeks, I've been quietly publishing weekly issues and gathering feedback from a small group of readers. Thank you all for your insights as I iterated and found my voice.
>
> Now that it’s public, I’d love for you to check it out and share your thoughts. The goal is to deliver high-quality weekly updates for the bug bounty and security community, covering programs, events, write-ups, and learning resources.
>
> Huge thanks to @rez0, @gr3pme, @arl_rose, @vailsec, @akshanshjaiswl, @shlibless, @0xroot, and many others for your early feedback and support. 
>
> #BugBounty #Disclosed #Infosec

**Links in post:** https://getdisclosed.com/subscribe


---

## 2025-05-27 · Post · Built some automation and a directory for aggregating bug bounty profiles. Adding your profile isn't


### Post — @infinitelogins — 2025-05-27 03:43 UTC (2025-05-27 04:43 WAT)

- URL: https://x.com/infinitelogins/status/1927209079136539100
- Metrics (at fetch): not returned

> Built some automation and a directory for aggregating bug bounty profiles. Adding your profile isn't open to the public yet but let me know what you think. 
> https://www.disclosedonline.com/directory
>
> #bugbounty

**Links in post:** https://www.disclosedonline.com/directory


---

## 2025-05-22 · Post · This one from @Rhynorater is filled with gold. It's definitely worth watching if you want to learn a


### Post — @infinitelogins — 2025-05-22 14:14 UTC (2025-05-22 15:14 WAT)

- URL: https://x.com/infinitelogins/status/1925555936904847690
- Metrics (at fetch): not returned

> This one from @Rhynorater is filled with gold. It's definitely worth watching if you want to learn a new technique for ethical hacking or bug bounty! https://twitter.com/BugBountyDEFCON/status/1925554663216070736

**Links in post:** https://twitter.com/BugBountyDEFCON/status/1925554663216070736

**Quoted post (full text):**

    #### Quoted post — @1773496655209533440 — 2025-05-22 14:09 UTC (2025-05-22 15:09 WAT)
    
    - URL: https://x.com/1773496655209533440/status/1925554663216070736
    - Metrics (at fetch): not returned
    
    > 11 critical bugs. $15K–$60K bounties. Deep dives into auth bypasses, SMS XSS, config injection, protocol abuse, and more.
    >
    > @Rhynorater walks through his highest-impact hacks across web, IoT, mobile, and desktop.
    >
    > Full talk → https://youtu.be/PXqlHAoF2wc
    >
    > #BugBounty #DEFCON #BBV [pic.x.com/4ISoOn6EdL]
    
    **Media:**
    - media `3_1925554659051069440` (details not returned by the API)
    
    **Links in post:** https://youtu.be/PXqlHAoF2wc
    


---

## 2024-12-12 · Post · H1's 2024 recap is here! Here's a snippet of mine: 


Tags (automatic): Platform: HackerOne


### Post — @infinitelogins — 2024-12-12 02:58 UTC (2024-12-12 03:58 WAT)

- URL: https://x.com/infinitelogins/status/1867041228619124981
- Metrics (at fetch): bookmark 3, impression 1398, like 17, quote 0, reply 1, retweet 0

> H1's 2024 recap is here! Here's a snippet of mine: 
>
> Proud to share my 2024 #BugBounty journey on @Hacker0x01!  Here's to making the internet safer, one bug at a time! 🐎💻 #InfoSec #CyberSecurity https://t.co/9xOvhAzyeL


---

## 2024-08-09 · Post · Bug bounty village is actually happening. Wow.


### Post — @infinitelogins — 2024-08-09 17:24 UTC (2024-08-09 18:24 WAT)

- URL: https://x.com/infinitelogins/status/1821960634348835285
- Metrics (at fetch): bookmark 1, impression 1251, like 20, quote 0, reply 1, retweet 0

> Bug bounty village is actually happening. Wow.


---

## 2024-08-04 · Post · Flying out for H1702 before Recharge on Wednesday and then setting up Bug Bounty Village at DEFCON


### Post — @infinitelogins — 2024-08-04 21:17 UTC (2024-08-04 22:17 WAT)

- URL: https://x.com/infinitelogins/status/1820207541957296484
- Metrics (at fetch): bookmark 0, impression 1058, like 15, quote 0, reply 3, retweet 0

> Flying out for #H1702 before Recharge on Wednesday and then setting up Bug Bounty Village at #DEFCON on Thursday. Hope to see you in Vegas this week!


---

## 2024-07-13 · Post · I'm going through some of the submitted slides for Bug Bounty Village talks, and I have to say, you 


### Post — @infinitelogins — 2024-07-13 23:41 UTC (2024-07-14 00:41 WAT)

- URL: https://x.com/infinitelogins/status/1812271263546753049
- Metrics (at fetch): bookmark 1, impression 4410, like 33, quote 1, reply 1, retweet 2

> I'm going through some of the submitted slides for Bug Bounty Village talks, and I have to say, you all are really in for a treat..


---

## 2024-07-09 · Post · If there is anything you've been wanting to ask community leaders at bug bounty platforms, this is y


### Post — @infinitelogins — 2024-07-09 17:00 UTC (2024-07-09 18:00 WAT)

- URL: https://x.com/infinitelogins/status/1810720619102884017
- Metrics (at fetch): bookmark 0, impression 976, like 5, quote 0, reply 0, retweet 2

> If there is anything you've been wanting to ask community leaders at bug bounty platforms, this is your chance! Submit your questions now if you want to influence the discussed topics. https://t.co/39C1T7BOZT

**Quoted post (full text):**

    #### Quoted post — @1773496655209533440 — 2024-07-09 16:57 UTC (2024-07-09 17:57 WAT)
    
    - URL: https://x.com/1773496655209533440/status/1810719928301015492
    - Metrics (at fetch): bookmark 0, impression 13825, like 24, quote 5, reply 3, retweet 4
    
    > Got questions for top bug bounty leaders? Submit them here! We are excited to announce a panel at the Bug Bounty Village during @DEFCON 32 with leaders from @Hacker0x01, @YesWeHack, @intigriti, and @SynackRedTeam! Share your questions now: https://t.co/HnDDsWuXGk https://t.co/brYdxsUZTz
    
    **Media:**
    - media `3_1810718987346747392` (details not returned by the API)
    


---

## 2024-04-15 · Post · I'm super excited and proud to announce I’ll be running the official Bug Bounty Village at @DEFCON a


### Post — @infinitelogins — 2024-04-15 18:32 UTC (2024-04-15 19:32 WAT)

- URL: https://x.com/infinitelogins/status/1779940770990223589
- Metrics (at fetch): bookmark 0, impression 5780, like 42, quote 3, reply 2, retweet 12

> I'm super excited and proud to announce I’ll be running the official Bug Bounty Village at @DEFCON alongside @arl_rose for the first time! Follow @BugBountyDefcon for updates and join us in shaping the future of Bug bounty. Please help us with a RT #BugBountyVillage #DEFCON https://t.co/XVyJQUyVNR

**Media:**
- photo: https://pbs.twimg.com/media/GLOeqd8akAAhBJt.jpg — no alt text provided by author


---

## 2023-12-02 · Post · Loving @Jhaddix's bug bounty hunter's methodology live course, learning a ton! Definitely worth the 


### Post — @infinitelogins — 2023-12-02 23:12 UTC (2023-12-03 00:12 WAT)

- URL: https://x.com/infinitelogins/status/1731088933487001992
- Metrics (at fetch): bookmark 2, impression 5174, like 20, quote 0, reply 1, retweet 2

> Loving @Jhaddix's bug bounty hunter's methodology live course, learning a ton! Definitely worth the investment if you're on the fence and we're only through day 1.


---

## 2023-08-22 · Post · Haven't recorded anything in a long time, but got inspired to go through some of the Race Condition 


Tags (automatic): Race condition


### Post — @infinitelogins — 2023-08-22 23:10 UTC (2023-08-23 00:10 WAT)

- URL: https://x.com/infinitelogins/status/1694124987236680040
- Metrics (at fetch): bookmark 6, impression 3040, like 21, quote 0, reply 1, retweet 7

> Haven't recorded anything in a long time, but got inspired to go through some of the Race Condition labs on @PortSwigger's academy and figured I'd make some video solutions. Check it out if you're interested in learning more about this vuln class! https://t.co/JV4QFozy6l


---

## 2023-06-05 · Post · Okay this is sick. TL;DR - Feed vulnerability details, (like HackerOne Reports) to Project Discovery


Tags (automatic): AI-assisted hunting, Platform: HackerOne


### Post — @infinitelogins — 2023-06-05 14:29 UTC (2023-06-05 15:29 WAT)

- URL: https://x.com/infinitelogins/status/1665727563891867653
- Metrics (at fetch): bookmark 0, impression 410, like 2, quote 0, reply 0, retweet 1

> Okay this is sick. TL;DR - Feed vulnerability details, (like HackerOne Reports) to Project Discovery's Nuclei Cloud AI to automatically build Nuclei templates. https://t.co/RzSGAGfpv2


---

## 2023-03-13 · Post · Found my first non-pentest RCE this week. Got marked as a dupe, but hey, that's still a win yeah?


Tags (automatic): RCE


### Post — @infinitelogins — 2023-03-13 01:14 UTC (2023-03-13 02:14 WAT)

- URL: https://x.com/infinitelogins/status/1635086815496663040
- Metrics (at fetch): bookmark 0, impression 1247, like 16, quote 0, reply 0, retweet 1

> Found my first non-pentest RCE this week. Got marked as a dupe, but hey, that's still a win yeah?


---

## 2022-08-08 · Post · The past week has been great. Met up with a ton of legends, helped put together the biggest HackerOn


Tags (automatic): Platform: HackerOne


### Post — @infinitelogins — 2022-08-08 23:32 UTC (2022-08-09 00:32 WAT)

- URL: https://x.com/infinitelogins/status/1556785537540771840
- Metrics (at fetch): not returned

> The past week has been great. Met up with a ton of legends, helped put together the biggest HackerOne event of the year, made some $$ and some new friends. #H1702
>
> Time week two - DEF CON


---

## 2022-03-25 · Post · My first week at HackerOne was awesome! I can't wait to start getting to meet those who are already 


Tags (automatic): Platform: HackerOne


### Post — @infinitelogins — 2022-03-25 03:56 UTC (2022-03-25 04:56 WAT)

- URL: https://x.com/infinitelogins/status/1507204660569862144
- Metrics (at fetch): not returned

> My first week at HackerOne was awesome! I can't wait to start getting to meet those who are already a part of their Pentest Community and help it grow.


---

## 2022-03-08 · Post · I am super excited to announce that I’ve accepted an offer with @Hacker0x01 as their new Technical C


Tags (automatic): Platform: HackerOne


### Post — @infinitelogins — 2022-03-08 15:28 UTC (2022-03-08 16:28 WAT)

- URL: https://x.com/infinitelogins/status/1501218194844884992
- Metrics (at fetch): not returned

> I am super excited to announce that I’ve accepted an offer with @Hacker0x01 as their new Technical Community Manager of Pentest Assessments! I truly can’t wait to be a part of that team. #HackerOne #TogetherWeHitHarder #Community


---

## 2022-01-29 · Post · Found HTML Injection and looking to demonstrate impact? Try chaining with SSRF by injecting an ifram


Tags (automatic): SSRF


### Post — @infinitelogins — 2022-01-29 20:25 UTC (2022-01-29 21:25 WAT)

- URL: https://x.com/infinitelogins/status/1487522184557957133
- Metrics (at fetch): not returned

> Found HTML Injection and looking to demonstrate impact? Try chaining with SSRF by injecting an iframe.
>
> &lt;iframe src=file:///etc/passwd&gt;&lt;/iframe&gt;
>
> @faizannehal1 has a great write-up explaining more at https://faizannehal.medium.com/
>
> #bugbountytips #bugbounty #webapp #pentesting

**Links in post:** https://faizannehal.medium.com/


---

## 2021-12-10 · Post · Log4Shell (CVE-2021-44228) hashes for vulnerable log4j versions


### Post — @infinitelogins — 2021-12-10 21:30 UTC (2021-12-10 22:30 WAT)

- URL: https://x.com/infinitelogins/status/1469419367515316227
- Metrics (at fetch): not returned

> #Log4Shell (CVE-2021-44228) hashes for vulnerable #log4j versions
> https://github.com/mubix/CVE-2021-44228-Log4Shell-Hashes

**Links in post:** https://github.com/mubix/CVE-2021-44228-Log4Shell-Hashes


---

## 2021-12-02 · Post · Cool bugbounty read on CVE-2021-39303 regarding a Jamf SSRF https://blog.assetnote.io/2021/11/30/j


Tags (automatic): SSRF


### Post — @infinitelogins — 2021-12-02 21:34 UTC (2021-12-02 22:34 WAT)

- URL: https://x.com/infinitelogins/status/1466521080667914244
- Metrics (at fetch): not returned

> Cool #bugbounty read on CVE-2021-39303 regarding a #Jamf SSRF https://blog.assetnote.io/2021/11/30/jamf-ssrf/

**Links in post:** https://blog.assetnote.io/2021/11/30/jamf-ssrf/


---

## 2021-08-24 · Post · Quick video showing the Razer local privilege escalation bug that @j0nh4t found. https://t.co/0uMXe


### Post — @infinitelogins — 2021-08-24 23:52 UTC (2021-08-25 00:52 WAT)

- URL: https://x.com/infinitelogins/status/1430317095691034627
- Metrics (at fetch): bookmark 0, impression 0, like 4, quote 0, reply 1, retweet 2

> Quick video showing the #Razer local privilege escalation bug that @j0nh4t found. https://t.co/0uMXe54EfD #cybersecurity #infosec


---

## 2021-08-17 · Post · Everybody hopping on the CVE hunt.. I have FOMO, might have to join in.


### Post — @infinitelogins — 2021-08-17 13:29 UTC (2021-08-17 14:29 WAT)

- URL: https://x.com/infinitelogins/status/1427623562106400771
- Metrics (at fetch): bookmark 1, impression 0, like 6, quote 0, reply 1, retweet 0

> Everybody hopping on the CVE hunt.. I have FOMO, might have to join in.


---

## 2021-07-21 · Post · Made a video inspired by @GossiTheDog's public exploit code for HiveNightmare, a new Local Privilege


### Post — @infinitelogins — 2021-07-21 02:00 UTC (2021-07-21 03:00 WAT)

- URL: https://x.com/infinitelogins/status/1417665809783017473
- Metrics (at fetch): bookmark 1, impression 0, like 19, quote 0, reply 0, retweet 7

> Made a video inspired by @GossiTheDog's public exploit code for HiveNightmare, a new Local Privilege Escalation vulnerability in Windows. #Infosec #HiveNightmare  #Windows
> https://t.co/KHxQSdsBR4


---

## 2021-07-05 · Post · As promised, here is part two of abusing PrintNightmare. This video shows using a public exploit to


Tags (automatic): RCE


### Post — @infinitelogins — 2021-07-05 21:03 UTC (2021-07-05 22:03 WAT)

- URL: https://x.com/infinitelogins/status/1412155244436344849
- Metrics (at fetch): bookmark 0, impression 0, like 13, quote 0, reply 0, retweet 3

> As promised, here is part two of abusing #PrintNightmare. This video shows using a public exploit to dump hashes from a Domain Controller via Remote Code Execution. https://t.co/GVGJSQiA1f
>
> #infosec #Windows


---

## 2021-07-05 · Thread · New video showing how to abuse PrintNightmare PoCs for Local Privilege Escalation. https://youtu.be


Tags (automatic): RCE


### Post — @infinitelogins — 2021-07-05 19:37 UTC (2021-07-05 20:37 WAT)

- URL: https://x.com/infinitelogins/status/1412133567769944064
- Metrics (at fetch): bookmark 1, impression 0, like 12, quote 0, reply 1, retweet 7

> New video showing how to abuse #PrintNightmare PoCs for Local Privilege Escalation. https://youtu.be/7iUcF2czFUQ
>
> A 2nd video will be out later today showing another PoC used for Remote Code Execution against a Domain Controller.  #Infosec #CVE

**Links in post:** https://youtu.be/7iUcF2czFUQ


### Thread part 2 — @infinitelogins — 2021-07-05 19:42 UTC (2021-07-05 20:42 WAT)

- URL: https://x.com/infinitelogins/status/1412134757245222913
- Metrics (at fetch): bookmark 0, impression 0, like 3, quote 0, reply 0, retweet 1

> Also shoutout to @_johnhammond - This video highlights the PoC that he wrote with @calebjstewart


---

## 2021-04-22 · Post · Curious how many students have been failed in the past eight months due to using LinPEAS with the au


### Post — @infinitelogins — 2021-04-22 23:11 UTC (2021-04-23 00:11 WAT)

- URL: https://x.com/infinitelogins/status/1385370664438157313
- Metrics (at fetch): bookmark 0, impression 0, like 3, quote 0, reply 0, retweet 0

> Curious how many students have been failed in the past eight months due to using LinPEAS with the auto-exploit feature added. https://t.co/oj8lFYNGKr

**Quoted post (full text):**

    #### Quoted post — @2170312728 — 2021-04-22 12:19 UTC (2021-04-22 13:19 WAT)
    
    - URL: https://x.com/2170312728/status/1385206684109447168
    - Metrics (at fetch): bookmark 51, impression 0, like 657, quote 36, reply 93, retweet 107
    
    > So folks I failed OSCP because linpeas was flagged as auto exploit. F*ck it. Cannot share more details. RIP
    


---

## 2021-04-20 · Thread · First video in a while - Part 2 to chaining XSS with CSRF is now up! https://t.co/JsQOuNuKNd


Tags (automatic): XSS


### Post — @infinitelogins — 2021-04-20 15:18 UTC (2021-04-20 16:18 WAT)

- URL: https://x.com/infinitelogins/status/1384526871623127048
- Metrics (at fetch): bookmark 0, impression 0, like 9, quote 1, reply 1, retweet 1

> First video in a while - Part 2 to chaining XSS with CSRF is now up! https://t.co/JsQOuNuKNd


### Thread part 2 — @infinitelogins — 2021-04-20 21:54 UTC (2021-04-20 22:54 WAT)

- URL: https://x.com/infinitelogins/status/1384626662013239303
- Metrics (at fetch): bookmark 0, impression 0, like 0, quote 0, reply 0, retweet 0

> Issue with the upload. Reupload at https://t.co/VQuzd9vWz8


---

## 2021-03-23 · Post · Metasploit module now available for the Exchange exploit.. Have you checked to make sure your friend


### Post — @infinitelogins — 2021-03-23 20:44 UTC (2021-03-23 21:44 WAT)

- URL: https://x.com/infinitelogins/status/1374462026114764806
- Metrics (at fetch): bookmark 0, impression 0, like 6, quote 0, reply 0, retweet 1

> Metasploit module now available for the Exchange exploit.. Have you checked to make sure your friends are patched yet? https://t.co/7RhJ3y8ncS


---

## 2021-02-17 · Post · I head the pleasure of speaking with @codingo_ the other day. Interview is now up on my channel! We 


Tags (automatic): Platform: Bugcrowd


### Post — @infinitelogins — 2021-02-17 16:56 UTC (2021-02-17 17:56 WAT)

- URL: https://x.com/infinitelogins/status/1362083552917999616
- Metrics (at fetch): bookmark 0, impression 0, like 5, quote 1, reply 0, retweet 0

> I head the pleasure of speaking with @codingo_ the other day. Interview is now up on my channel! We discussed working at #BugCrowd, creating #Infosec content on #YouTube, and general career advice for getting in the field. https://t.co/o6sMvzC7DH


---

## 2021-02-09 · Post · New video out, this time stealing session cookies using Reflected XSS. https://t.co/awHaE8Da7t


Tags (automatic): XSS


### Post — @infinitelogins — 2021-02-09 19:08 UTC (2021-02-09 20:08 WAT)

- URL: https://x.com/infinitelogins/status/1359217728091922432
- Metrics (at fetch): bookmark 0, impression 0, like 4, quote 0, reply 0, retweet 1

> New video out, this time stealing session cookies using Reflected #XSS. https://t.co/awHaE8Da7t


---

## 2021-01-30 · Post · Friendly reminder - CVE-2021-3156 https://t.co/ftnm8AXoDW


### Post — @infinitelogins — 2021-01-30 19:35 UTC (2021-01-30 20:35 WAT)

- URL: https://x.com/infinitelogins/status/1355600481326796800
- Metrics (at fetch): bookmark 0, impression 0, like 1, quote 0, reply 1, retweet 0

> Friendly reminder - CVE-2021-3156 https://t.co/ftnm8AXoDW

**Quoted post (full text):**

    #### Quoted post — @1288824691 — 2021-01-30 19:25 UTC (2021-01-30 20:25 WAT)
    
    - URL: https://x.com/1288824691/status/1355597996247945220
    - Metrics (at fetch): bookmark 0, impression 0, like 7, quote 1, reply 0, retweet 0
    
    > Have you updated your sudo today?
    


---

## 2021-01-28 · Post · I always recommend @thecybermentor's content, but this video in particular about Blind XSS is incred


Tags (automatic): XSS


### Post — @infinitelogins — 2021-01-28 14:02 UTC (2021-01-28 15:02 WAT)

- URL: https://x.com/infinitelogins/status/1354791953208991748
- Metrics (at fetch): bookmark 9, impression 0, like 49, quote 0, reply 1, retweet 7

> I always recommend @thecybermentor's content, but this video in particular about Blind XSS is incredible. This is an attack vector that I never knew about and is extremely underrated. Thank you for sharing this Heath! https://t.co/D21YJwlDyh


---

## 2021-01-26 · Post · New video out showing how easy it is to steal session cookies with XSS https://t.co/0S5bdwJ5Uf


Tags (automatic): XSS


### Post — @infinitelogins — 2021-01-26 15:59 UTC (2021-01-26 16:59 WAT)

- URL: https://x.com/infinitelogins/status/1354096647257481217
- Metrics (at fetch): bookmark 1, impression 0, like 1, quote 0, reply 0, retweet 0

> New video out showing how easy it is to steal session cookies with #XSS https://t.co/0S5bdwJ5Uf


---

## 2021-01-12 · Post · Anybody know how to inject a XSS payload when the WAF blocks requests containing letters immediatel


Tags (automatic): XSS


### Post — @infinitelogins — 2021-01-12 15:03 UTC (2021-01-12 16:03 WAT)

- URL: https://x.com/infinitelogins/status/1349009156758532104
- Metrics (at fetch): bookmark 0, impression 0, like 1, quote 0, reply 1, retweet 0

> Anybody know how to inject a #XSS payload when the WAF blocks requests containing letters immediately after the left angle bracket "&lt;"   ???
>
> Blocked:   &lt;script&gt; or &lt;x  ...
> Allowed:   &lt; script&gt; or &lt;1script&gt; ...


---

## 2020-09-15 · Post · Abusing CVE-2020-1472 (ZeroLogon) https://t.co/uLuKMKGion


### Post — @infinitelogins — 2020-09-15 23:51 UTC (2020-09-16 00:51 WAT)

- URL: https://x.com/infinitelogins/status/1306017955789012992
- Metrics (at fetch): bookmark 0, impression 0, like 0, quote 0, reply 0, retweet 0

> Abusing CVE-2020-1472 (ZeroLogon) https://t.co/uLuKMKGion


---

## 2020-07-31 · Post · Bypassing XSS Defenses Part 1: Finding Allowed Tags and Attributes using BurpSuite Intruder. 


Tags (automatic): XSS


### Post — @infinitelogins — 2020-07-31 22:25 UTC (2020-07-31 23:25 WAT)

- URL: https://x.com/infinitelogins/status/1289326284028354561
- Metrics (at fetch): not returned

> Bypassing #XSS Defenses Part 1: Finding Allowed Tags and Attributes using #BurpSuite Intruder. 
>
> https://infinitelogins.com/2020/07/31/bypassing-xss-defenses-finding-allowed-tags-and-attributes/
>
> #WebApplications #OWASPTop10 #WebApp

**Links in post:** https://infinitelogins.com/2020/07/31/bypassing-xss-defenses-finding-allowed-tags-and-attributes/


---

## 2020-07-03 · Post · Are you responsible for securing WebApplications? These are some bypass techniques attackers are us


### Post — @infinitelogins — 2020-07-03 05:39 UTC (2020-07-03 06:39 WAT)

- URL: https://x.com/infinitelogins/status/1278926270223564801
- Metrics (at fetch): not returned

> Are you responsible for securing #WebApplications? These are some bypass techniques attackers are using for #CrossSiteRequestForgery (CSRF).
>
> https://infinitelogins.com/2020/07/02/exploiting-cross-site-request-forgery-csrf-bypassing-defenses/

**Links in post:** https://infinitelogins.com/2020/07/02/exploiting-cross-site-request-forgery-csrf-bypassing-defenses/


---

## 2020-01-17 · Post · Patching CVE-2020-0601 | Windows CryptoAPI Spoofing Vulnerability http://infinitelogins.com/2020/01/


### Post — @infinitelogins — 2020-01-17 21:03 UTC (2020-01-17 22:03 WAT)

- URL: https://x.com/infinitelogins/status/1218277734318780417
- Metrics (at fetch): not returned

> Patching CVE-2020-0601 | Windows CryptoAPI Spoofing Vulnerability http://infinitelogins.com/2020/01/17/cve-2020-0601-windows-cryptoapi-spoofing-vulnerability/

**Links in post:** http://infinitelogins.com/2020/01/17/cve-2020-0601-windows-cryptoapi-spoofing-vulnerability/
