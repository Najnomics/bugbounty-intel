# java4shell-redhat-rhsb-2026-018

- **Source URL:** https://access.redhat.com/security/vulnerabilities/RHSB-2026-018
- **Fetched:** 2026-11-18
- **Researcher:** irsdl
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

# RHSB-2026-018 Remote Code Execution via memory corruption on x86-64 systems - OpenJDK (CVE-2026-114938) - "java4shell"

Updated

Was this information helpful?

Feedback cancelled

## Executive Summary

This issue is tracked as [CVE-2026-114938](https://access.redhat.com/security/cve/CVE-2026-114938) and has a severity impact of [Critical](https://access.redhat.com/security/updates/classification). Red Hat is expediting the release of fixes.

A memory corruption vulnerability in OpenJDK 17.0.6 and later allows an unauthenticated remote attacker to achieve arbitrary code execution on x86-64 systems whose CPU supports the AVX-512 VBMI instruction set. The flaw is in OpenJDK's Base64 decoder: an attacker who

can supply malformed Base64 input to an application running on an affected Java Virtual Machine can take full control of the application or crash the service.

**Environments running JVMs on ARM64 systems, or on x86-64 CPUs that do not support AVX-512 VBMI (i.e., processors older than Intel Ice Lake or AMD Zen 4), are not known to be affected.** Customers running OpenJDK 8 or OpenJDK 11 are also not affected, as these versions do not contain the vulnerable code path.

The investigation is ongoing and this bulletin will be updated as new information emerges. Log in with your Red Hat account, then click the "Follow" button below to be notified of changes to this bulletin.

## Affected Products

The following Red Hat product versions are directly affected:

- Red Hat Enterprise Linux 10
- Red Hat Enterprise Linux 9
- Red Hat Enterprise Linux 8
- Red Hat build of OpenJDK 25
- Red Hat build of OpenJDK 21
- Red Hat build of OpenJDK 17

Further, any Red Hat product which is supported on Red Hat Enterprise Linux (including RHEL CoreOS) is also potentially impacted. This includes

- Product containers that are based on the RHEL or UBI container images.  These images are updated regularly, and container health indicating whether a fix to this flaw is available can be seen in the Container Health Index, part of the [Red Hat Container Catalog](https://catalog.redhat.com/).  In addition, any customer containers should be rebuilt when the base images are updated.
- Products that pull packages from the RHEL channel (this includes layered products such as Red Hat OpenShift Container Platform, Red Hat OpenStack Platform, Red Hat Virtualization, and others). Please ensure that the underlying RHEL OpenJDK package is current in these product environments.

## Technical Summary

The vulnerability is a memory corruption flaw in OpenJDK's Base64 decoder, `java.util.Base64.Decoder`. On x86-64 CPUs that support AVX-512 VBMI, the JVM selects an AVX-512 accelerated code path for Base64 decoding. Specifically malformed Base64 input processed through that path corrupts memory, and an attacker who controls the input can leverage this to execute arbitrary code in the context of the Java process.

Because the flaw is in the Java standard library rather than in any single application, exposure depends on whether an application decodes attacker-controlled Base64 data. That is common in practice: HTTP Basic credentials, SAML artifacts, CSRF tokens, and MIME encoded words are all Base64-encoded and are routinely decoded before authentication completes. Pre-authentication remote code execution has been demonstrated against widely deployed Java applications running default configurations.

No special configuration or non-default features are required. The accelerated code path is selected automatically whenever the JVM runs on a CPU reporting AVX-512 VBMI support, so affected systems are vulnerable out of the box.

## Detection

To determine if a system is running a vulnerable OpenJDK version, check the installed Java version:

`java -version`

Systems running OpenJDK 17.0.6 or later (including OpenJDK 21 and 25) on x86-64 hardware are potentially vulnerable. To check whether the host CPU supports AVX-512 VBMI:

`grep -o avx512vbmi /proc/cpuinfo | head -1`

If the command outputs `avx512vbmi`, the system's CPU supports the vulnerable instruction set. If there is no output, the CPU does not support AVX-512 VBMI and is not known to be affected.

## Conditions

The following conditions must all be present for this vulnerability to be exploitable:

1. The application runs on OpenJDK 17.0.6 or later (including OpenJDK 21 and 25).
2. The host CPU is x86-64 and supports the AVX-512 VBMI instruction set (Intel Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids; AMD Zen 4, Zen 5, Zen 6).
3. The JVM has not been started with `-XX:UseAVX=2` or a lower AVX level, which would prevent use of AVX-512 instructions.
4. The application passes attacker-controlled Base64-encoded data to the Java standard library decoder (`java.util.Base64.Decoder`). Common sources include HTTP Basic credentials, SAML artifacts, CSRF tokens, and MIME encoded words, all of which are frequently decoded before authentication completes.

## Mitigation

### Overall Guidance

As an interim mitigation prior to an OpenJDK update, start affected JVMs with one of the following flags:

- `-XX:-UseBASE64Intrinsics` disables the hardware-accelerated Base64 implementation only. This is the preferred option, as it removes the vulnerable code path while leaving other AVX-512 optimizations in place.
- `-XX:UseAVX=2` disables AVX-512 instructions entirely. Apply this flag only to x86-64 deployments: JVMs on ARM64 do not recognize it and will fail to start if it is applied there.

**Systems running on ARM64, or on x86-64 CPUs without AVX-512 VBMI support, do not require either flag**.

### Product-Specific Mitigation Steps

#### OpenJDK on x86-64

In addition to applying one of the mitigation flags above:

- Inventory which Java runtime (vendor, full build version) each application uses, including runtimes bundled inside containers, product installations, and vendor appliances.
- Confirm whether the underlying host/VM CPU supports AVX-512 VBMI; cloud instance families most likely to be affected include AWS C6i/M6i/R6i and C7i/M7i/R7a, GCP C3/C3D/C4/C4D/N4/N4D/M3/M4, and Azure Dsv5/Dsv6/Dasv6/Dasv7 and related D-series v5–v7 SKUs.
- Prioritize internet-facing applications and authentication services, which commonly decode Base64 credentials and tokens before authentication completes.
- For products that bundle their own JVM, apply the mitigation flag or update via the product vendor's supported path rather than patching the JVM independently.
- Treat this as an interim measure only; apply the permanent OpenJDK fix once available and remove the workaround flag.

## Updates for Affected Products

Red Hat customers running affected versions of these Red Hat products are strongly recommended to update as soon as errata are available. Customers are urged to apply the available updates immediately and enable the mitigations as they feel appropriate.

## References

[OpenJDK Security Advisory - 2026-11-17](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Fopenjdk.org%2Fgroups%2Fvulnerability%2Fadvisories%2F2026-11-17)

[Calif Security Research - Vulnerability Analysis](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Fcalif.io%2Fjava4shell%2F)

[How to use GPG to verify signed content from Product Security](https://access.redhat.com/articles/5433831)

## Comments
