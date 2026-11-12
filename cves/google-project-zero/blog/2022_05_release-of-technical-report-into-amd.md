# Release of Technical Report into the AMD Security Processor - Project Zero

Source: https://projectzero.google/2022/05/release-of-technical-report-into-amd.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by James Forshaw, Google Project Zero


Today, members of Project Zero and the Google Cloud security team are releasing a [technical report](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/AMD_GPZ-Technical_Report_FINAL_05_2022.pdf) on a security review of AMD Secure Processor (ASP). The ASP is an isolated ARM processor in AMD EPYC CPUs that adds a root of trust and controls secure system initialization. As it's a generic processor AMD can add additional security features to the firmware, but like with all complex systems it's possible these features might have security issues which could compromise the security of everything under the ASP's management.


The security review undertaken was on the implementation of the ASP on the 3rd Gen AMD EPYC CPUs (codenamed "Milan"). One feature of the ASP of interest to Google is [Secure Encrypted Virtualization (SEV)](https://www.amd.com/en/processors/amd-secure-encrypted-virtualization). SEV adds encryption to the memory used by virtual machines running on the CPU. This feature is of importance to [Confidential Computing](https://cloud.google.com/confidential-computing) as it provides protection of customer cloud data in use, not just at rest or when sending data across a network.


A particular emphasis of the review was on the Secure Nested Paging (SNP) extension to SEV added to "Milan". SNP aims to further improve the security of confidential computing by adding integrity protection and mitigations for numerous side-channel attacks. The review was undertaken with full cooperation with AMD. The team was granted access to source code for the ASP, and production samples to test hardware attacks.


The review discovered 19 issues which have been fixed by AMD in public security bulletins. These issues ranged from incorrect use of cryptography to memory corruption in the context of the ASP firmware. The report describes some of the more interesting issues that were uncovered during the review as well as providing a background on the ASP and the process the team took to find security issues. You can read more about the review on the [Google Cloud security blog](https://cloud.google.com/blog/products/identity-security/google-amd-partner-to-build-a-more-secure-future-with-confidential-computing) and the [final report](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/AMD_GPZ-Technical_Report_FINAL_05_2022.pdf).
