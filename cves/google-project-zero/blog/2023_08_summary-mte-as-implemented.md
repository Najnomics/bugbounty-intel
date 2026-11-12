# Summary: MTE As Implemented - Project Zero

Source: https://projectzero.google/2023/08/summary-mte-as-implemented.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

By Mark Brand, Project Zero

In mid-2022, Project Zero was provided with access to pre-production hardware implementing the ARM MTE specification. This blog post series is based on that review, and includes general conclusions about the effectiveness of MTE as implemented, specifically in the context of preventing the exploitation of memory-safety vulnerabilities.


Despite its limitations, MTE is still by far the most promising path forward for improving C/C++ software security in 2023. The ability of MTE to detect memory corruption exploitation at the first dangerous access provides a significant improvement in diagnostic and potential security effectiveness. In comparison, most other proposed approaches rely on blocking later stages in the exploitation process, for example various hardware-assisted CFI approaches which aim to block invalid control-flow transfers.

No MTE-based mitigation is going to completely solve the problem of exploitable C/C++ memory safety issues. The unfortunate reality of speculative side-channel attacks is that MTE will not end memory corruption exploitation. However, there are no other practical proposals with a similarly broad impact on exploitability (and exploitation cost) of such a wide range of memory corruption issues which would additionally address this limitation.

Furthermore, given the long history of  innovation and research in this space, we believe that it is not possible to build a software solution for C/C++ memory safety with comparable coverage to MTE that has less runtime overhead than [AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html)/[HWAsan](https://clang.llvm.org/docs/HardwareAssistedAddressSanitizerDesign.html). It's clear that such an overhead is not acceptable for most production workloads.


Products that expect to contain large C/C++ codebases in the long term, who consider the exploitation of memory corruption vulnerabilities to be a key risk for their product security, should actively drive support for ARM's MTE in their products.

For a more detailed analysis, see the following linked blog posts:

1. [Implementation Testing](/2023/08/mte-as-implemented-part-1.html) - An objective summary of the tests performed, and some basic analysis. If you're interested in implementing a mitigation based on MTE, you should read this document first as it will give you more detailed technical background.

1. [Mitigation Case Studies](/2023/08/mte-as-implemented-part-2-mitigation.html) - A subjective assessment of the impact of various mitigation approaches based on the use of MTE in various user-mode contexts, based on our experiences during the tests performed in Part 1. If you're not interested in implementing a mitigation based on MTE, but you are interested in the limits of how effective such a mitigation might be, you can skip Part 1 and start here.
2. [The Kernel](/2023/08/mte-as-implemented-part-3-kernel.html) - A subjective assessment of the additional issues faced in using MTE for a kernel-mode mitigation.
