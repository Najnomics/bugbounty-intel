# java4shell-berkeley-iso

- **Source URL:** https://security.berkeley.edu/news/cve-2026-114938-openjdk-and-oracle-java-vulnerabilities
- **Fetched:** 2026-11-18
- **Researcher:** irsdl
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

This is a notice from the Information Security Office to alert you to a critical vulnerability that impacts Java and OpenJDK\[1\]. Please share this alert internally with IT admins and service owners who run the product so they are aware and know what actions to take to address this vulnerability.

## Summary

ISO is aware of critical vulnerabilities that affect Oracle’s Java and OpenJDK products, and other products that use them. There are 11 flaws in Java, and one in OpenJDK, unimaginatively dubbed Java4Shell, which is assigned CVE-2026-114938. These additional affected products\[2\] include Oracle Database, Oracle E-Business Suite, Oracle Financial Services Applications, and Oracle PeopleSoft, as well as multiple others. The vulnerability lies in the decoding of Base64.

## Impact

Many of these vulnerabilities allow unauthenticated Remote Code Execution.

## What is Vulnerable:

The following Oracle products and versions are vulnerable:

- Oracle Java SE: 8u511, 8u511-perf, 11.0.33, 17.0.21, 21.0.13, 25.0.5, and 27.0.1.
- Oracle GraalVM for JDK: 17.0.21 and 21.0.13.
- Oracle GraalVM Enterprise Edition: 21.3.20.0.3.
- Oracle JavaFX: 21.0.13, 25.0.5, and 27.0.1.

Oracle advises customers to stop using its current builds of Java 8, 11, 17, 21, 25, and 27 after the November 17 security update and move to the corresponding replacement releases.

## Recommendations

Upgrade affected Java and OpenJDK products as soon as possible\[3\]\[4\].

- Oracle Java SE 8 and OpenJDK 8 : upgrade to 8u513
- Oracle Java SE 11 and OpenJDK 11 : upgrade to 11.0.33.1
- Oracle Java SE 17 and OpenJDK 17 : upgrade to 17.0.21.1
- Oracle Java SE 21 and OpenJDK 21 : upgrade to 21.0.13.1
- Oracle Java SE 25 and OpenJDK 25 : upgrade to 25.0.5.1
- Oracle Java SE 27 and OpenJDK 27 : upgrade to 27.0.1.1
- Oracle GraalVM for JDK : upgrade to patched version when available
- Oracle GraalVM Enterprise Edition : upgrade to patched version when available
- Oracle JavaFX : upgrade to patched version when available

## Mitigation:

The following JVM options are recommended to disable affected functions\[1\]:

- -XX:-UseBASE64Intrinsics, which turns off the Base64 intrinsics
- -XX:UseAVX=2, which turns off all AVX-512 code paths and can slow other work.

Additional mitigations are to disable OpenJDK functions\[5\]:

- -XX:+UnlockDiagnosticVMOptions
- -XX:DisableIntrinsic=\_base64\_decodeBlock

## References:

1. [https://thehackernews.com/2026/11/oracle-to-patch-11-java-flaws-today-as.html?m=1](https://thehackernews.com/2026/11/oracle-to-patch-11-java-flaws-today-as.html?m=1)
2. [https://www.oracle.com/security-alerts/cspunov2026.html](https://www.oracle.com/security-alerts/cspunov2026.html)
3. [https://openjdk.org/groups/vulnerability/advisories/2026-11-17](https://openjdk.org/groups/vulnerability/advisories/2026-11-17)
4. [https://www.aikido.dev/blog/java-17-rce-vulnerability-cve-2026-114938](https://www.aikido.dev/blog/java-17-rce-vulnerability-cve-2026-114938)
5. [https://calif.io/java4shell/](https://calif.io/java4shell/)


If you have any questions about the vulnerability or would like some assistance patching or mitigating it, please contact [security@berkeley.edu](mailto:security@berkeley.edu).
