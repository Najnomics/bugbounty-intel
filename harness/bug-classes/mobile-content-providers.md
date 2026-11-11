# Mobile: content providers, intents, deep links

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/` and `writeups/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


## Detection signals
- Exported components (activities, services, content providers) and deep-link/URI handlers that trust unvalidated input.
- URI scheme/host parser quirks.

## Method seen in sources
- Android Uri host-validation bypass: the scheme parser only looked at part of the URI, enabling host spoofing. Source: [`posts/_bagipro/2025-08-01-1951318010444005529.md`](../../posts/_bagipro/2025-08-01-1951318010444005529.md).
- Content-provider access via system apps (permission mechanism bypass). Source: [`posts/_bagipro/2026-02-25-2026798826871247233.md`](../../posts/_bagipro/2026-02-25-2026798826871247233.md).
- 140 Samsung preinstalled-app bugs. Source: [`writeups/_bagipro/oversecured-samsung-vulnerabilities-readme.md`](../../writeups/_bagipro/oversecured-samsung-vulnerabilities-readme.md).
- From the sweep: mobile static handoff seeds hosts/routes/intents into the web recon (`source: mobile-static`). Source: [`writeups/mdp_sec/prompts/phases/phase-00-recon.md`](../../writeups/mdp_sec/prompts/phases/phase-00-recon.md).

## Tools
- apktool/jadx for decompilation, drozer/adb for IPC, Oversecured scanner (bagipro).

## Automation (check spec)
```
for comp in exported_components(manifest):
  if content_provider(comp): test path-permission and traversal via system-app proxy
  if deep_link(comp): fuzz scheme/host parser (partial-parse host spoof)
feed discovered API hosts/routes into web recon as mobile-static hypotheses
```

