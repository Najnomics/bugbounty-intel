# http://unpkg.com/

- **Source URL:** http://unpkg.com/
- **Fetched from:** https://unpkg.com/
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7438 (id 7438)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- Global edge
- Served from Cloudflare's network, close to browsers everywhere. [Network](https://unpkg.com/network)
- 11 origin regions
- Files are fetched from origin machines across the Americas, Europe, Asia, and Australia.
- Verified bytes
- Every file is digest-checked before it is cached, and corrupt entries heal themselves.
- Supply-chain defense
- [UNPKG Shield](https://shield.unpkg.com/) pins or swaps compromised packages at the edge.

## Start in one line

Point a script tag at a package file. Pin the full version in production so the response comes straight from the edge cache:

In a module, load the browser-ready build from [esm.unpkg.com](https://esm.unpkg.com/):

Need to know what's inside a package first? Append [`?meta`](https://unpkg.com/guides/metadata-api) to any package URL for JSON metadata.

## Ways to use UNPKG

- [Load files from npm](https://unpkg.com/guides/loading-files): any file, any package, one URL. Versions, entry points, and exports resolution explained.
- [Build apps with no build step](https://unpkg.com/guides/nobuild-apps): import maps turn a plain HTML file into a working app.
- [Use native browser modules](https://unpkg.com/guides/browser-modules): esm.unpkg.com converts packages into modules browsers load directly.
- [Run inline TypeScript and JSX](https://unpkg.com/guides/inline-scripts): the `/run` helper transforms inline scripts in the page.
- [Inspect packages programmatically](https://unpkg.com/guides/metadata-api): file listings, sizes, and integrity hashes as JSON, for tools and agents.

## UNPKG, inside your AI agent

Agents are bad at recalling npm: versions that don't exist, files that were never published. The UNPKG MCP server gives your agent live resolution, real file listings, project audits, and import-map validation — so it builds direct UNPKG file lookups from facts, and tells you when a framework should keep its bundle instead.

It also checks what you're about to ship. Ask about any dependency — or your whole project — and it answers with exact-version malware verdicts and CVE checks, including the version to upgrade to. No account is needed for packages you name; connect a Shield account and it does the same for everything your domains actually serve, ranked by your traffic.

"Is lodash@4.17.20 safe to load? Check it for malware and CVEs."

"Audit my project, and check every dependency for known compromises before converting anything."

## Running in production

Exact-version files are cached at the edge for a year, and every cached byte is digest-verified. A damaged entry is evicted and refetched, never served. If a version has to be withdrawn, it can be evicted from every cache layer without touching any other version. The [network page](https://unpkg.com/network) explains how, and the [status page](https://unpkg.com/status) describes how changes ship safely.

Serving production traffic through UNPKG? [UNPKG Shield](https://shield.unpkg.com/) (currently in Beta) watches every npm release as it publishes. Arm a domain and a compromised version is pinned to the last known-good release (or blocked) at the edge, before a browser executes it. [How supply-chain defense works](https://unpkg.com/guides/supply-chain-security).

## Open source

UNPKG is an [open source project](https://github.com/unpkg), free to use, and not affiliated with npm. The [guides](https://unpkg.com/guides) go deeper on everything above.
