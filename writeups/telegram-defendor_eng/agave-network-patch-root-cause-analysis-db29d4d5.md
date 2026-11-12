# 🔍 How Solana Quietly Patched a Network-Halting Bug

- **Source URL:** https://www.anza.xyz/blog/agave-network-patch-root-cause-analysis
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1808 (id 1808)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
[Back to Blog](https://www.anza.xyz/blog)

Written By

## Timeline

On 2024-08-05 23:00 UTC, Anza core engineers became aware of a vulnerability, reported by an external researcher, affecting the Agave and Jito validator clients. This vulnerability would have allowed an exploiter to crash leaders one by one, eventually halting the network. Anza core engineers created a patch, had the patch audited by multiple 3rd party audit firms, and then worked with the wider Solana operator community to apply the patch. By 2024-08-08 20:00 UTC, over 67% of the network had applied the patch, making network consensus safe from this disruption. Any unpatched infrastructure could still be vulnerable and validators are recommended to upgrade ([instructions from Discord](https://discord.com/channels/428295358100013066/669406841830244375/1271284187869085898)).

## Root Cause Analysis (RCA)

### Preliminary

The Solana toolchain provides a standard workflow for program development and deployment. The toolchain abstracts away many low level details that most application developers need not worry about. However, the Solana runtime is flexible and also supports programs that are created outside of the standard workflow.

One item of interest is the alignment within a generated program (ELF) file. Program files created by the Solana toolchain have proper alignment. But, a program developed outside of the toolchain may not have such guarantees. If a program with improper alignment is deployed, the runtime is responsible for verifying that the program is well formed at execution time.

### The Vulnerability

The vulnerability was the result of an invalid assumption about address alignment. If an unpatched node had attempted to execute a program that broke this particular assumption, the node would have likely crashed from a host segmentation fault. Any unpatched node would be vulnerable to such a crash.

The vulnerability stems from an unintended interaction between the CALL\_REG opcode and layout of the code in the binary. CALL\_REG requires that the code being jumped to be aligned to an instruction boundary. Typically this is the case as the linker will only emit an ELF file with an aligned .text section. The solana virtual machine's implementation of CALL\_REG made an assumption that the code it was calling had been loaded from a sanitized ELF file and that its .text section was aligned, as required. However, the ELF sanitization omits an alignment check on the .text section, allowing for a maliciously crafted ELF file to specify a misaligned .text section. When CALL\_REG is issued against misaligned code, it causes the VM to jump to an invalid address, likely resulting in a host segmentation fault, killing the validator process.

This vulnerability could be exploited by an attacker who first writes a program that issues the CALL\_REG opcode, manipulates the programs ELF file to misalign its .text section and finally deploys and invokes this program on the solana network normally.

## Deploying the Patch

The network would only be safe from this vulnerability once a supermajority (67%) of validators had upgraded. The security challenge here was that publishing a patch for validators to apply would also reveal the underlying vulnerability. It was paramount to minimize the time between core devs disseminating the update and a supermajority of the network deploying the patch.

Core contributors were able to leverage their existing networks to privately contact validator operators with larger stake weights (as reflected on solanabeach.io or solanacompass.com), minimizing the risk of the vulnerability being revealed and exploited. An initial message informed validators that a vulnerability had been discovered and that further instructions would come in a subsequent message at a specific date and time. A hash of the first message was posted on public channels by several community members to enable any recipient of the message to verify its authenticity. The hash was:

*07ff4f17c96a632726e209b4afbbcf4e6ba089989cb485b8abbe85da3f558cd9*

At 2024-08-08 14:00 UTC, the previously specified time, the patch was distributed. Along with the patch, hashes to verify the contents of the patch files and instructions on how to build patched binaries were included. The patches and hashes are linked below:

- [https://gist.githubusercontent.com/willhickey/3914d29bad897ff4972fee97dd80e5c9/raw/1ce759e25fc50d828a14f60306eac4b02224c5af/0001-Apply-rbpf-patch.patch](https://gist.githubusercontent.com/willhickey/3914d29bad897ff4972fee97dd80e5c9/raw/1ce759e25fc50d828a14f60306eac4b02224c5af/0001-Apply-rbpf-patch.patch)
- [https://gist.githubusercontent.com/willhickey/3914d29bad897ff4972fee97dd80e5c9/raw/1ce759e25fc50d828a14f60306eac4b02224c5af/0001-Update-dependency.patch](https://gist.githubusercontent.com/willhickey/3914d29bad897ff4972fee97dd80e5c9/raw/1ce759e25fc50d828a14f60306eac4b02224c5af/0001-Update-dependency.patch)
- [https://gist.githubusercontent.com/willhickey/3914d29bad897ff4972fee97dd80e5c9/raw/1ce759e25fc50d828a14f60306eac4b02224c5af/patch\_shas](https://gist.githubusercontent.com/willhickey/3914d29bad897ff4972fee97dd80e5c9/raw/1ce759e25fc50d828a14f60306eac4b02224c5af/patch_shas)
- [https://gist.githubusercontent.com/buffalu/05c7f54c4a7c268ecdf37f0d3835a266/raw/9e9609d73ab1de21e214f55a81cba5d56bf90126/0001-Update-dependency.patch](https://gist.githubusercontent.com/buffalu/05c7f54c4a7c268ecdf37f0d3835a266/raw/9e9609d73ab1de21e214f55a81cba5d56bf90126/0001-Update-dependency.patch)
- [https://gist.githubusercontent.com/buffalu/05c7f54c4a7c268ecdf37f0d3835a266/raw/39fb45a2e3fefb4898e398fe8e5f213938ae1384/patch\_shas](https://gist.githubusercontent.com/buffalu/05c7f54c4a7c268ecdf37f0d3835a266/raw/39fb45a2e3fefb4898e398fe8e5f213938ae1384/patch_shas)

After the patch was shared publicly and the network was deemed safe, patched releases were created for the affected repos and communicated across the normal channels.

[https://github.com/solana-labs/solana/releases/tag/v1.18.22](https://github.com/solana-labs/solana/releases/tag/v1.18.22)

[https://github.com/anza-xyz/agave/releases/tag/v1.18.22](https://github.com/anza-xyz/agave/releases/tag/v1.18.22)
[https://github.com/jito-foundation/jito-solana/releases/tag/v1.18.22-jito](https://github.com/jito-foundation/jito-solana/releases/tag/v1.18.22-jito)

## Reporting a Vulnerability

If you are a security researcher or developer and you have uncovered a potential vulnerability, instructions to raise awareness via proper secure channels are located in the Agave GitHub repository linked below:
