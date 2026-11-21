# burpsuite-sharpenerex-release-4.94

- **Source URL:** https://github.com/irsdl/BurpSuiteSharpenerEx/releases/tag/main_4.94
- **Fetched:** 2026-11-21
- **Researcher:** irsdl
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

## Repository navigation

- Keep the full Sharpener menu on every supported host and add an optional native Settings page.
- Organize optional Settings into Global and Project tabs with compact selectors, aligned fields and immediate preference updates.
- Limit Logger inspection to 64 KiB by default. Use Content-Length only as an initial hint, then check actual whole-request size before scanning its body; oversized or unknown-size requests use headers. Responses use their first 64 KiB. Turn the limit off for complete inspection. Proxy and WebSocket behavior is unchanged.
- Known Montoya API limitation: an understated Content-Length can still cause a complete copy before rejection. Copy-free actual-size metadata and bounded byte reads would remove this overhead; see [the API proposal](https://github.com/irsdl/BurpSuiteSharpenerEx/blob/main/docs/montoya-message-size-api.md).

Known limitation: the installed Windows main/taskbar icon may remain unchanged. Full UI, Community, cross-platform and provenance validation are deferred under the version-specific maintainer approval.

Built and tested on GitHub Actions. Full live UI, cross-platform and provenance checks were deferred by the maintainer for 4.94; see the attached release evidence. Community shares relevant APIs with Professional, but its current full regression was not completed. This is not BApp Store certification.

Build: [https://github.com/irsdl/BurpSuiteSharpenerEx/actions/runs/44809338772](https://github.com/irsdl/BurpSuiteSharpenerEx/actions/runs/44809338772)
