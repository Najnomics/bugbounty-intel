# @Neodyme

Index of captured posts and analysis. Verbatim posts: [`posts/Neodyme/`](../posts/Neodyme/).

## Daily update 2026-11-16

### Solana Breakpoint badge zero-click RCE over Wi-Fi (2026-11-15)

- Post: https://x.com/Neodyme/status/2121941626822004761 — verbatim: [`posts/Neodyme/2026-11-15-2121941626822004761.md`](../posts/Neodyme/2026-11-15-2121941626822004761.md)
- **Bug class:** Embedded/IoT zero-click RCE (conference hardware badge running "Solana OS")
- **Root cause:** Not yet published ("Details coming soon").
- **How it was found:** Badge security review at pickup; triggered via deauth attacks or joining a vulnerable AP.
- **Takeaways / harness:** Test Wi-Fi reconnect/provisioning paths (deauth → evil twin), on-device network parsers, OTA signing on hardware wallets/badges.

