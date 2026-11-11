# Auth Bypass

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **23** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- When multiple layers handle the same request, test whether gateway/proxy/backend interpret the URL differently. (from infinitelogins). Source: [`posts/infinitelogins/2026-10-08-2108181015885685018.md`](../../posts/infinitelogins/2026-10-08-2108181015885685018.md).
- Enumerate every client_id (web, iOS, Android, desktop) and test redirect_uri validation separately for each. (from xssdoctor). Source: [`posts/xssdoctor/2026-10-01-2105723370125881675.md`](../../posts/xssdoctor/2026-10-01-2105723370125881675.md), [`writeups/xssdoctor/faav-17-trillion-microsoft-records.md`](../../writeups/xssdoctor/faav-17-trillion-microsoft-records.md).
- Any endpoint that looks up a secret is a candidate for wildcard injection; if `%` returns more than one row it's LIKE. (from infinitelogins). Source: [`posts/infinitelogins/2026-11-04-2117981403161764138.md`](../../posts/infinitelogins/2026-11-04-2117981403161764138.md).
- Whenever auth middleware and router parse paths differently, try dot-segments and encodings; check every layer (proxy, middleware, framework router). (from mdp_sec). Source: [`posts/mdp_sec/2026-11-11-2120338219841544604.md`](../../posts/mdp_sec/2026-11-11-2120338219841544604.md), [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md), [`writeups/mdp_sec/mdpsec-home.md`](../../writeups/mdp_sec/mdpsec-home.md).
- Always test whether signatures are actually verified, not just parsed. (from mdp_sec). Source: [`posts/mdp_sec/2026-11-05-2118435683329310786.md`](../../posts/mdp_sec/2026-11-05-2118435683329310786.md), [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md), [`writeups/mdp_sec/mdpsec-home.md`](../../writeups/mdp_sec/mdpsec-home.md).
- New flagship AI programs often ship with classic ATO classes — hit them early. (from galnagli). Source: [`posts/galnagli/ARCHIVE.md`](../../posts/galnagli/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Stack Jenkins ACL bypasses with gadget RCEs for unauth impact. (from orange_8361). Source: [`posts/orange_8361/ARCHIVE.md`](../../posts/orange_8361/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- When a CVE lands, re-test older versions — alternate bypass payloads often remain. (from infosec_au). Source: [`posts/infosec_au/ARCHIVE.md`](../../posts/infosec_au/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Pre-auth RCE in source-control appliances is mass-critical — monitor Bitbucket advisories. (from infosec_au). Source: [`posts/infosec_au/ARCHIVE.md`](../../posts/infosec_au/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- SaaS sandboxes that gate pre-auth script features are prime RCE targets. (from infosec_au). Source: [`posts/infosec_au/2026-07-14-2076989533850362149.md`](../../posts/infosec_au/2026-07-14-2076989533850362149.md).
- Auth bypass CVEs deserve root-cause writeups — the pattern recurs across products. (from infosec_au). Source: [`posts/infosec_au/ARCHIVE.md`](../../posts/infosec_au/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Try Param Miner for hidden headers. (from albinowax). Source: [`posts/albinowax/2026-11-04-2117935178278371560.md`](../../posts/albinowax/2026-11-04-2117935178278371560.md).
- — (from infosec_au). Source: [`posts/infosec_au/2026-05-10-2053414439635054961.md`](../../posts/infosec_au/2026-05-10-2053414439635054961.md), [`writeups/infosec_au/frontier-class-vulnerabilities.md`](../../writeups/infosec_au/frontier-class-vulnerabilities.md), [`writeups/infosec_au/react2shell-scanner-readme.md`](../../writeups/infosec_au/react2shell-scanner-readme.md).
- — (from 0xacb). Source: [`posts/0xacb/2026-11-05-2118387414527832065.md`](../../posts/0xacb/2026-11-05-2118387414527832065.md), [`writeups/0xacb/tedivm-ai-rcession.md`](../../writeups/0xacb/tedivm-ai-rcession.md).

## Method / findings in sources

- **Layered auth bypass: .json static-path skip + %23 truncate + trusted-client header ($10,000)** — Endpoint had three checks: JWT at gateway, backend path validation, trusted-client header. Paths ending in .json skipped JWT (treated as static). %23 (#) let gateway see .json while backend truncated at # leaving a clean ID. X-CLIENT-ID: WEBAPP satisfied the final gate. Resulted in mass PII exfiltration. Source: [`posts/infinitelogins/2026-10-08-2108181015885685018.md`](../../posts/infinitelogins/2026-10-08-2108181015885685018.md).
- **iOS OAuth client accepts any protocol in redirect_uri** — The iPhone app's OAuth client (a client_id different from the web app's) allowed any protocol in redirect_uri because iOS deep links use custom schemes; a malicious app could start the flow in Safari with the callback pointing at itself and receive the user's credentials. Source: [`posts/xssdoctor/2026-10-01-2105723370125881675.md`](../../posts/xssdoctor/2026-10-01-2105723370125881675.md), [`writeups/xssdoctor/faav-17-trillion-microsoft-records.md`](../../writeups/xssdoctor/faav-17-trillion-microsoft-records.md).
- **Unauthenticated account takeover via LIKE-wildcard leak of auto-login keys ($5,000)** — Unattended devices authenticate with an 'auto login key' that is the credential. Lookup/resolve endpoints used SQL LIKE on the key, so `%` enumerated accounts and returned victim keys. No rate limiting. Device endpoint traded the leaked key for a session. Source: [`posts/infinitelogins/2026-11-04-2117981403161764138.md`](../../posts/infinitelogins/2026-11-04-2117981403161764138.md).
- **/./ path normalisation past a login wall into an admin console** — The login check matched the exact raw path, but the router normalised the path afterwards, so /admin/./ failed the exact match yet still routed to /admin. Source: [`posts/mdp_sec/2026-11-11-2120338219841544604.md`](../../posts/mdp_sec/2026-11-11-2120338219841544604.md), [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md), [`writeups/mdp_sec/mdpsec-home.md`](../../writeups/mdp_sec/mdpsec-home.md).
- **$8,000 auth bypass on HackerOne — token signature not verified** — The server accepted tokens without verifying their signature, so a forged/modified token was trusted. Source: [`posts/mdp_sec/2026-11-05-2118435683329310786.md`](../../posts/mdp_sec/2026-11-05-2118435683329310786.md), [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md), [`writeups/mdp_sec/mdpsec-home.md`](../../writeups/mdp_sec/mdpsec-home.md).
- **OpenAI ChatGPT critical account takeover — view chats + billing (fixed)** — Critical ATO on ChatGPT: takeover someone's account, view chat history and billing without victim realizing. galnagli claimed #1 on OpenAI Bugcrowd program with 9 valids in <48h. Source: [`posts/galnagli/ARCHIVE.md`](../../posts/galnagli/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Jenkins pre-auth RCE (with Overall/Read) — chains with CVE-2018-1000861 to no-ACL RCE** — Pre-auth (with Overall/Read) RCE reported to Jenkins. Chained with previously reported CVE-2018-1000861 could execute arbitrary code without ACL restrictions. Source: [`posts/orange_8361/ARCHIVE.md`](../../posts/orange_8361/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Additional Ivanti PCS auth-bypass payload for older versions (CVE-2023-46805 / CVE-2024-21887 family)** — Assetnote built exploit set for Ivanti Pulse Connect Secure vulns and found an additional auth bypass payload that works on older software versions. Source: [`posts/infosec_au/ARCHIVE.md`](../../posts/infosec_au/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Bitbucket Server pre-auth RCE (Assetnote / TheGrandPew)** — Pre-authentication remote command execution in Atlassian Bitbucket Server. Root-cause writeup on Assetnote blog. Source: [`posts/infosec_au/ARCHIVE.md`](../../posts/infosec_au/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **ServiceNow pre-auth RCE by sandbox bypass** — Pre-auth RCE in ServiceNow by bypassing their sandbox. Writeup by hash_kitten / SLCyberSec. Source: [`posts/infosec_au/2026-07-14-2076989533850362149.md`](../../posts/infosec_au/2026-07-14-2076989533850362149.md).
- **CVE-2022-22972 VMware Workspace ONE Access auth bypass — root-cause writeup** — Root-cause analysis of VMware Workspace ONE Access authentication bypass. Source: [`posts/infosec_au/ARCHIVE.md`](../../posts/infosec_au/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **$300k for a trusted internal header** — Internal header trusted from outside. Source: [`posts/albinowax/2026-11-04-2117935178278371560.md`](../../posts/albinowax/2026-11-04-2117935178278371560.md).
- **cPanel pre-auth critical** — See post. Source: [`posts/infosec_au/2026-05-10-2053414439635054961.md`](../../posts/infosec_au/2026-05-10-2053414439635054961.md), [`writeups/infosec_au/frontier-class-vulnerabilities.md`](../../writeups/infosec_au/frontier-class-vulnerabilities.md), [`writeups/infosec_au/react2shell-scanner-readme.md`](../../writeups/infosec_au/react2shell-scanner-readme.md).
- **sshole (CVE-2026-123158) reproduction** — See post. Source: [`posts/0xacb/2026-11-05-2118387414527832065.md`](../../posts/0xacb/2026-11-05-2118387414527832065.md), [`writeups/0xacb/tedivm-ai-rcession.md`](../../writeups/0xacb/tedivm-ai-rcession.md).
- **forgerock-rce-vehicles** — In early 2026, [Shubham Shah](https://x.com/infosec_au) and I found a vulnerability chain that gave us remote code execution on the production ForgeRock servers handling customer logins for two automakers, which we'll call Automaker #1 and Automaker #2Obviously, they have asked not to be named, and while normally we would fight to actually include  Source: [`writeups/samwcyo/forgerock-rce-vehicles.md`](../../writeups/samwcyo/forgerock-rce-vehicles.md).
- **injective-any-account-ordering-report** — - No special conditions or permissions are required. Any user on the Injective chain can exploit this to steal all assets from any other account. - All funds in on Injective are at risk. At the time of submitting this report, total on-chain assets exceeded **$500M**. Data source: [https://intel.arkm.com/explorer/address/0xF955C57f9EA9Dc8781965FEaE0 Source: [`writeups/al_f4lc0n/injective-any-account-ordering-report.md`](../../writeups/al_f4lc0n/injective-any-account-ordering-report.md).
- **tedivm-ai-rcession** — Over the last week we've seen a frightening number of exploits announced to the public, followed by a lot of panic and warnings of disaster. If you paid attention to some news stories you'd think society was on the brink of collapse. We aren't about to see the fall of society, but we are going through a dramatic shift; and the companies with the mo Source: [`writeups/0xacb/tedivm-ai-rcession.md`](../../writeups/0xacb/tedivm-ai-rcession.md).
- **taking-undercollateralized-loans-for-fun-and-for-profit** — By relying on an on-chain decentralized price oracle without validating the rates returned, [DDEX](https://margin.ddex.io) and [bZx](https://bzx.network) were susceptible to atomic price manipulation. This would have resulted in the loss of liquid ETH in the ETH/DAI market for DDEX, and loss of all liquid funds in bZx. Fortunately, no funds were ac Source: [`writeups/samczsun/taking-undercollateralized-loans-for-fun-and-for-profit.md`](../../writeups/samczsun/taking-undercollateralized-loans-for-fun-and-for-profit.md).

## Payloads / requests seen in sources

- `GET /api/employee/12345%23.json with header X-CLIENT-ID: WEBAPP` — Layered auth bypass: .json static-path skip + %23 truncate + trusted-client header ($10,000). Source: [`posts/infinitelogins/2026-10-08-2108181015885685018.md`](../../posts/infinitelogins/2026-10-08-2108181015885685018.md).
- `Register a malicious iOS app for the custom URL scheme accepted as OAuth redirect_uri; start the flow in Safari with callback pointing at the malicious app to capture the code/token` — iOS OAuth client accepts any protocol in redirect_uri. Source: [`posts/xssdoctor/2026-10-01-2105723370125881675.md`](../../posts/xssdoctor/2026-10-01-2105723370125881675.md), [`writeups/xssdoctor/faav-17-trillion-microsoft-records.md`](../../writeups/xssdoctor/faav-17-trillion-microsoft-records.md).
- `GET /autologin/lookup?key=% ; POST /autologin/resolve?key=% with {user_id,tenant_id} ; POST /autologin/devices with {user_id,key}` — Unauthenticated account takeover via LIKE-wildcard leak of auto-login keys ($5,000). Source: [`posts/infinitelogins/2026-11-04-2117981403161764138.md`](../../posts/infinitelogins/2026-11-04-2117981403161764138.md).
- `Append /./ (also //, trailing dots, %2e) to a 403/login-gated path: /admin/./ passes the exact-match auth check then normalises to /admin at the router` — /./ path normalisation past a login wall into an admin console. Source: [`posts/mdp_sec/2026-11-11-2120338219841544604.md`](../../posts/mdp_sec/2026-11-11-2120338219841544604.md), [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md), [`writeups/mdp_sec/mdpsec-home.md`](../../writeups/mdp_sec/mdpsec-home.md).
- `Tamper JWT/token claims and signature (strip, alter, alg=none, self-sign) and confirm the server still accepts it` — $8,000 auth bypass on HackerOne — token signature not verified. Source: [`posts/mdp_sec/2026-11-05-2118435683329310786.md`](../../posts/mdp_sec/2026-11-05-2118435683329310786.md), [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md), [`writeups/mdp_sec/mdpsec-home.md`](../../writeups/mdp_sec/mdpsec-home.md).

See also [`../payloads/auth-bypass.md`](../payloads/auth-bypass.md) when present.

## Automation (check spec)

```
# Checks derived from 23 documented finding(s) in findings.jsonl for class=auth-bypass
# try: GET /api/employee/12345%23.json with header X-CLIENT-ID: WEBAPP
# try: Register a malicious iOS app for the custom URL scheme accepted as OAuth redirect_uri; start the flow in Safari with callback pointing at the malicious app to c
# try: GET /autologin/lookup?key=% ; POST /autologin/resolve?key=% with {user_id,tenant_id} ; POST /autologin/devices with {user_id,key}
# try: Append /./ (also //, trailing dots, %2e) to a 403/login-gated path: /admin/./ passes the exact-match auth check then normalises to /admin at the router
# try: Tamper JWT/token claims and signature (strip, alter, alg=none, self-sign) and confirm the server still accepts it
# note: New flagship AI programs often ship with classic ATO classes — hit them early.
# note: Stack Jenkins ACL bypasses with gadget RCEs for unauth impact.
# note: When a CVE lands, re-test older versions — alternate bypass payloads often remain.
```

## Prior harness notes (retained)

_Retained from earlier curated harness file; still cites local sources._

## Detection signals
- A protected path returns 403 or redirects to login, but the auth check and the router may parse the path differently (gate vs router disagreement).
- Tokens (JWT / session / reset) are accepted without the signature actually being verified.
- Pre-auth endpoints (login, activate, reset, verify) expose privileged actions.

## Recon steps
- Enumerate 403 / login-redirect paths and protected prefixes (`/admin`, `/api/internal`).
- Collect all tokens in use (cookies, Authorization headers, URL params) and their structure.
- Map pre-auth endpoints from the recon route map (Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md), class `preauth-bypass`).

## Payloads / requests seen in sources
- Path-normalization bypass: retry gated paths with `/./`, `//`, trailing dots, `%2e` — e.g. `GET /admin/./` passed an exact-match auth check then normalised to `/admin`. Source: [`posts/mdp_sec/2026-11-11-2120338219841544604.md`](../../posts/mdp_sec/2026-11-11-2120338219841544604.md).
- Token signature not verified: tamper claims and signature (strip, alter, `alg=none`, self-sign) and confirm acceptance ($8,000). Source: [`posts/mdp_sec/2026-11-05-2118435683329310786.md`](../../posts/mdp_sec/2026-11-05-2118435683329310786.md).
- API version bypass: replay each shape on `/v1`..`/vN`, unversioned, header and query variants, including write verbs; older versions often keep weaker authz. Source: Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md) (class `api-version`).

## Tools
- Burp/Caido + Param Miner (headers), `httpx`, a JWT editor, and his API-version replay logic (Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md)).

## Automation (check spec)
```
for path in protected_paths:
  for variant in [p, p+'/./', p+'//', p+'/%2e/', p+'.']:
    if status(variant) in (200,) and status(p) in (401,403,302): FLAG path-normalization-authz
for token in observed_tokens:
  if accepts(tamper(token, alg='none')) or accepts(strip_sig(token)): FLAG unverified-signature
for shape in api_shapes:
  for v in version_variants(shape):
    if authz(v) weaker-than authz(shape): FLAG api-version-authz
```

## Related findings
- See `harness/findings.jsonl` records with bug_class containing "Auth bypass" / "path normalisation".
