# GhostTiles

- **Source URL:** https://medium.com/@ts247091/ghosttiles-how-a-stale-frame-id-turned-freerdps-progressive-codec-into-a-resource-amplifier-427e8091f9f3
- **Fetched from:** https://medium.com/feed/@ts247091
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14997 (id 14997)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*A coordinated-disclosure write-up of GHSA-v7hr-xh82–79p7, a High-severity flaw in FreeRDP’s RDP Graphics pipeline.*

When a desktop client connects to a remote server, it trusts that server to send screen updates. FreeRDP decodes those updates locally. GhostTiles showed how a small sequence of valid Progressive graphics updates could make that client spend far more memory and CPU than the data should require.

The issue was reported to the FreeRDP project and is now publicly documented as [GHSA-v7hr-xh82–79p7](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-v7hr-xh82-79p7). The project rates it High. The advisory credits the reporter as poxsky. It reports the issue fixed in FreeRDP 3.33.0; the project’s release history now includes 3.33.1 as well.

### What is affected?

FreeRDP is a widely used implementation of the Remote Desktop Protocol. Its Progressive codec decodes tile-based screen updates sent over the RDP Graphics (RDPGFX) channel. FreeRDP-based clients, including xfreerdp and applications that embed libfreerdp, may be affected when they connect to a malicious RDP server using the vulnerable code.

This is a client-side issue. An attacker needs to operate or control an RDP server and get a target to connect to it. The finding does not mean that any internet host can attack every FreeRDP client without a connection being initiated.

### The short version

The decoder kept a list of tiles to repaint. It cleared that list only when the frame identifier changed. If a server reused the same identifier — or sent no StartFrame PDU, leaving the client’s frame identifier at zero — the list was not cleared between complete surface updates.

Each new update added tiles to the old list. The decoder then repainted the entire growing list again. Over time, this created two effects:

- **Memory growth:** repeated updates caused the tile cache to grow far beyond the amount of data received.
- **Rising CPU cost:** each update revisited all earlier tile entries, so the work accumulated roughly quadratically.

### How the bug works

A Progressive surface update is decoded by progressive\_decompress(). The decoder tracks a per-surface frame identifier and an array of updated tile indices. In the affected code, the update counter was reset only inside a “frame identifier changed” branch.

That reset condition assumed that the frame identifier would advance between the calls that needed a fresh tile-update batch. But the relevant Wire-to-Surface-2 command contains a complete Progressive frame, and a server can keep the identifier constant. If the identifier does not change, the old tile indices remain in the batch.

For every repeated frame, the decoder adds that frame’s tiles to the list and calls the drawing routine over the full list. A simplified model is:

frame 1: repaint T tiles

frame 2: repaint 2T tiles

frame 3: repaint 3T tiles

...

frame N: repaint N×T tiles

The total work across N repeated frames is proportional to T × (1 + 2 + … + N), which grows as O(TN²). A normal frame identifier change clears the batch and avoids this accumulation; the attack sequence keeps it from changing.

### Measured impact

FreeRDP’s published advisory reports an end-to-end test against an unmodified xfreerdp client running version 3.32.2. In that test, 12.3 MB of server traffic increased the client’s resident memory from about 2.2 MB to about 2.29 GB in roughly nine seconds. The processing time per command increased from about 20 ms to about 90 ms. With a 1.8 GB address-space limit, the client crashed after roughly 145 commands.

A control test that advanced the frame identifier kept memory approximately flat. That comparison supports the stale-identifier reset condition as the cause of the amplification. These numbers describe the project’s published test setup; results can vary with build options, platform, and available memory.

### Why memory pressure could become memory corruption

The advisory also documents a second part of the chain. Tile-cache growth used multiple allocations. During a failed growth operation, the cache’s recorded size could be advanced before all dependent allocations had succeeded. Later bounds checks could then trust a capacity value that no longer matched the actual allocated storage.

Under allocation failure, a subsequent tile-index write could go out of bounds. The project reports an AddressSanitizer-confirmed four-byte heap write under fault injection, as well as a crash in a constrained production-style run. The public report does not demonstrate code execution; the confirmed impact is resource exhaustion and a memory-corruption condition under memory pressure.

Another aggravating behavior was that some decoder failure paths returned success to the caller. That could hide an internal failure from the surrounding client code while decoding continued.

### What the fix changes

The project’s advisory describes two main fixes: reset the tile-update batch for each complete surface command, and make tile-cache growth transactional. In practical terms, the first prevents old tile entries from accumulating across commands. The second keeps the decoder’s bookkeeping consistent if an allocation fails partway through growth.

**Upgrade to FreeRDP 3.33.0 or later.** The project lists 3.33.0 as the patched version. Check the version of the FreeRDP libraries your application actually uses; a front-end update alone may not update an independently installed or bundled libfreerdp.

### Disclosure and references

FreeRDP’s security advisory was published on November 9, 2026, and currently lists no CVE ID. The project’s [security policy](https://github.com/FreeRDP/FreeRDP/security/policy) asks researchers to report vulnerabilities privately so maintainers can review the issue, coordinate a fix, and publish an advisory.

*This write-up summarizes the project’s public advisory and the accompanying research materials. It intentionally omits a runnable attack server or payload. Do not test systems without authorization.*
