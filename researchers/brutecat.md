# @brutecat

Compiled 23 Nov 2026 (WAT). Verbatim posts under [`posts/brutecat/`](../posts/brutecat/). Already listed in [researchers.md](../researchers.md) (Google GFile, $100k, cited in Disclosed).

## 2026-11-22 — Ghostscript isolation at Google (Upload2Shell context)
- Reply to @PaulosYibelo's Upload2Shell (CVE-2026-125396): Google sandboxes Ghostscript in **per-request isolated gVisor VMs**, so no prod impact for them.
- **Takeaway:** for file-processing RCEs, characterise worker isolation (ephemeral VM, egress, metadata, persistence) before claiming impact.
- **Local:** [posts/brutecat/2026-11-22-2124451394686251188.md](../posts/brutecat/2026-11-22-2124451394686251188.md)
