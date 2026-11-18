# java4shell-sysdig

- **Source URL:** https://www.sysdig.com/blog/java4shell-cve-2026-114938-pre-auth-rce-in-openjdk
- **Fetched:** 2026-11-18
- **Researcher:** irsdl
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

### Get security briefings from the Threat Research Team

New campaigns, attacker techniques, and detection guidance — straight to your inbox.

[Subscribe](/security-briefings-signup)

## Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered.

[learn more](/opensource/falco)

DISCLAIMER: This blog reflects public findings as of 1:36 UTC, Nov. 18, 2026, and it will be updated as new information is released.

Java promised that users would never have to think about memory again. Java's Base64 decoder, however, had other plans.

On November 17, 2026, Oracle and OpenJDK shipped fixes for Java4Shell ([CVE-2026-114938](https://www.cve.org/CVERecord?id=CVE-2026-114938)), a heap memory corruption bug in the AVX-512 accelerated Base64 decoder. Calif, [the firm that discovered the vulnerability](https://calif.io/java4shell), says that with 64 `A` characters and one `=`, a remote attacker with no credentials can overwrite heap memory, leak it Heartbleed-style, and in the products they tested, get remote code execution (RCE).

Calif made a suggestion that Java4Shell’s Base64 optimization and the Squidbleed flaw that they also discovered are calls for vibe-uncoding, or the use of AI to find and remove system bloat to reduce an attack surface. This is the same point that’s been made in multiple [Sysdig Cloud Native Security and Usage Reports](https://www.sysdig.com/blog/sysdig-2026-cloud-native-security-and-usage-report) since 2023 with regard to image bloat.

Let’s explore what's confirmed, what's still theoretical, and why after combating and cleaning up image bloat for years, the next fight appears to be feature bloat.

## Important facts to know now about Java4Shell

- **What:** Heap out-of-bounds write in OpenJDK's x86-64 Base64 intrinsic. Pre-authentication on common login paths.
- **Who:** OpenJDK 17.0.6 and later (17, 21, 25, 27) on x86-64 CPUs with AVX-512 VBMI. ARM is out. Java 11 and standard Java 8 are out. Oracle also lists the Java 8 performance build (8u511b33-perf) as vulnerable.
- **Severity:** 9.2 critical on CVSS 4.0 per Calif, and 8.1 on CVSS 3.1 per OpenJDK's advisory.
- **Exploitation:** Calif confirms working RCE in Keycloak, Jira, Confluence, Artifactory, Jenkins, and PingFederate without authorization, plus five more post-auth. The researcher says OpenAI Codex helped find the bug in an hour and build an exploit in two hours for less than $200. Calif stated the exploit will not be publicly shared until organizations have patched the vulnerability.
- **Fix:** Oracle builds ending in `.1`, or `-XX:-UseBASE64Intrinsics` as the bridge.

## What happened

## Who's affected by Java4Shell

Calif's list of vulnerable builds is broad because everything downstream of OpenJDK inherits the code: Amazon Corretto, Eclipse Temurin, Microsoft Build of OpenJDK, Azul Zulu, BellSoft Liberica, SAP SapMachine, Red Hat OpenJDK, Oracle OpenJDK, Oracle Java SE, and Oracle GraalVM for JDK.

For non-Oracle distributions, researchers said the Temurin, Corretto, and Zulu fixes were still pending at 20:00 UTC. To determine if your organization is affected, check with your vendor.

The hardware filter may be a silver lining for some organizations. The vulnerable code only runs on x86-64 CPUs with AVX-512 VBMI: Intel Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, and AMD Zen 4 or newer. Use Calif's check to see if your Linux hosts are vulnerable:

`grep -m1 '^flags' /proc/cpuinfo | tr ' ' '\n' | grep -E '^(avx512f|avx512bw|avx512vbmi|bmi2)$'`
All four flags must show up. Then run `java -version` inside the container, not on the host. Your host's JDK is not your container's JDK, and your container's JDK is the one that matters.

## How Java4Shell works

Per Calif's write-up, HotSpot's C2 compiler uses AVX-512 intrinsics to decode Base64 fast. The hand-rolled assembly that handles the padded tail miscalculates the output length for certain inputs, ending up with `-1`, which turns the write mask fully open. The result is that 64 bytes get written where two were expected, and 62 of them land past the end of the output array. Java then notices the input is bad and throws an exception, but the write already happened.

The trigger is 64 `A` characters followed by `=` (128 `A` plus `=` on Java 17). The decoder has to be JIT-compiled first, which means warm-up traffic. The overflowing bytes are fixed, so an attacker picks where the write lands, not what it writes.

That sounded like a dead end to some researchers, whose lab tests found that a typical token wasn’t able to corrupt anything, leading them to the early assumption that RCE was yet to be proven, but not impossible. However, Calif found the way around it: a classic heap grooming move borrowed from JavaScript engine exploitation. Use the fixed write to overwrite a neighboring array's length, and now you have a buffer that accepts chosen bytes. Do it again to get a reader; writer plus reader gives you a heap leak and a path to code execution.

## What's reachable before login

Researchers found that standard Basic auth handling in Spring Security, Tomcat, and Jetty 12 passes the raw token to `Base64.getDecoder()` before validating it. Auth0's `java-jwt` decodes JWT headers and payloads the same way before checking the signature.

Calif adds that ordinary features like file uploads can expose the decoder too, and that samczsun contributed a client-side exploit: A Java program that opens a TLS connection to a malicious server can be compromised even if it exposes no service. Ultimately, that means that your login page is likely the attack surface.

## What's been demonstrated vs. what’s been claimed

**Demonstrated by researchers:**

- Calif reports RCE in default configurations of Keycloak, Atlassian Jira, Atlassian Confluence, JFrog Artifactory, Jenkins, and PingFederate (pre-auth), and Apache Kafka Broker, Apache Solr, Elasticsearch, Gerrit, and Spinnaker (post-auth). It also reports RCE in sample Struts and Spring Boot applications and publishes a demo video.
- Theori and other firms have independently reproduced the overflow itself.
- Calif says discovery took one hour, the first working exploit took two more, and the total token cost was under $200.

**Constraints:**

- There is no universal exploit. Each target needs its own profile: a decoder route, a live writer, a feedback path, a heap layout, and an application action.
- Wrong heap placement can crash the JVM. Calif says in many cases it can just retry.
- The attack is sensitive to network latency. Calif's fix for that was renting a VM in the same region as the target.
- Some chains need partial request bodies to reach the application. Request buffering (which nginx does by default) breaks those chains but isn't a general mitigation. Elasticsearch runs from a single complete request, and WebSocket tunnels bypass buffering.

**What's public so far:**

- Calif published a self-contained Java program that warms the decoder and reproduces the 62-byte overwrite inside a bounded array.
- Calif says it is holding back the weaponized, product-specific chains "until everyone has had a chance to upgrade," and will publish them later.

As of 21:10 UTC, GitHub repositories for the CVE ID were a placeholder README, Theori's mitigation tool, and a BigFix scanner. No exploit code. A search for `java4shell exploit` returned nothing. So far, researchers have shared a public trigger, a documented technique, named targets, and a promise of more to come. Leaked bugs often attract fake exploits, as researchers have already warned. So if a repo promises a shell, read it before you run it, and run it in a sandbox.

## Reigning in image bloat

Calif closes its write-up with what it calls vibe-uncoding: If you don't need something, stop running it. They explicitly point to Base64 optimization as an example. It helps applications that decode enormous amounts of data and ships to everyone else too, and so "an optimization few applications needed became a serious security risk."

As a cybersecurity strategist, this is a soapbox I’ve been on for about three years. Our annual [cloud-native security and usage reports](https://www.sysdig.com/blog/sysdig-2026-cloud-native-security-and-usage-report) have continually made the same case: The unused packages that ride along with open source images do nothing for your use case and everything for an attacker's. The [2025 report](https://www.sysdig.com/blog/sysdig-2025-cloud-native-security-and-usage-report) specifically called for shrinking image bloat through consolidation, smart application building, and discovering shadow AI and other shadow IT.

And then organizations actually did it, and I’d like to think they used AI to do so, just as Calif suggests. In the [2026 Cloud-Native Security and Usage Report](https://www.sysdig.com/2026-cloud-native-security-and-usage-report), we analyzed nearly 13 billion packages for image bloat. Less than one percent of packages in images were unused, a 50% reduction year over year. Teams matured their CI/CD pipelines and moved to leaner images, which in turn shrinks the attack surface. And, as a bonus, it makes images build, scan, and pull faster and cost less to store. Fewer packages means fewer surprises, faster patching, and clearer ownership.

That’s a win. Image bloat will probably never hit 0%, but it’s a material reduction that came from boring, disciplined work.

Here's the catch, and the real lesson of Java4Shell: The cleanup got the unused packages, but it didn't touch the unused code inside the packages you do use. Nobody's image scan flags a hand-rolled AVX-512 Base64 stub sitting inside `java.base`, because Java is in use, Base64 is in use, and the optimization is part of the thing. Package-level bloat is mostly handled. **Feature-level bloat is the next frontier**, and it lives upstream, in runtimes and libraries that ship everything to everybody.

Calif's answer is to point AI at that problem too: Find the dead code and needless optimizations, then remove them. I think this question of "What can we delete?" is the right one, aimed one layer deeper than most of us have been looking.

But slimming your images will not stop this specific bug. The vulnerable code is in the JDK itself, in the thing you actually use. Two things do apply, however:

- **The flag is vibe-uncoding at runtime.** `-XX:-UseBASE64Intrinsics` turns off a feature you probably didn't need. That mitigation works because most workloads never notice.
- **Blast radius is a real control.** If an attacker lands code execution in a minimal image with no shell, no package manager, no `curl`, and no compiler, they have a much worse afternoon than in an image with everything. Leftover tooling doesn't cause the bug, but it's the toolkit the attacker finds afterward.

And there’s another important lesson CISOs can learn from this: Calif's researcher found this by prompting Codex over an audit of the JIT compiler, intrinsics, and crypto and in the researcher's own words, "ignoring slops for around 20 minutes." Discovery to working exploit in three hours. That’s the new math for defenders. If your patch cycle is measured in weeks and the other side's exploit cycle is measured in an afternoon, you’ve lost the race.

That is the same theme running through our 2026 report and [other Sysdig threat research identified throughout the year](https://www.sysdig.com/blog/four-ways-ai-has-fundamentally-changed-the-threat-landscape-in-2026): shifting from manual effort to machine-speed defense, with runtime detection as the signal teams trust most.

## How to detect Java4Shell

This exploit leaves almost nothing at the application layer. The server answers 401 and moves on. Defenders should look for the shape, noise, and aftermath of an attack.

- **Request shape:** Flag Base64-alphabet tokens of 32 or more characters that end in `=` and whose length isn't a multiple of 4. Valid padded Base64 is always a multiple of 4. Start with `Authorization` headers.
- **Application logs:** Researchers saw `IllegalArgumentException: Input byte array has wrong 4-byte ending unit` on every attempt in their tests.
- **Retry and warm-up behavior:** Calif's chain warms the decoder with valid decodes, then triggers, and retries on bad placement. That implies bursts of requests from one source, repeated malformed tokens, and potentially many half-sent request bodies held open and released together. However, this has not been observed in the wild as of this publication.
- **JVM crashes:** Wrong placement means crashes: SIGSEGV, `hs_err_pid*.log` files, and bursts of worker restarts.
- **Post-exploitation:** If the chain lands, the aftermath looks like any other Java compromise: the JVM spawning a shell, dropping and executing a binary, or opening connections it never opened before.

## What defenders can do to get ahead of Java4shell today

- **Patch Oracle JDK immediately.** 17.0.21.1, 21.0.13.1, 25.0.5.1, 27.0.1.1, and 8u513 for the performance build.
- **Linux users don’t have to self-patch:** Java installed from your Linux distribution's package manager gets fixed through the distribution's normal update channel, but only after the distro ships a fix and only on hosts that apply updates. Containers and vendor JDK builds don’t update themselves. Rebuild and redeploy.
- **Inventory everything else.** Check Temurin, Corretto, Zulu, Microsoft, and distribution builds against your vendor's advisory. Several were pending as of this publication.
- **Prioritize by exposure and hardware.** Internet-facing services on AVX-512 VBMI instances, especially anything using Basic auth, `java-jwt`, or the products on Calif's list, go first.
- **Mitigate with a JVM flag if you can’t patch yet.** `-XX:-UseBASE64Intrinsics` stopped the overflow on every affected version Upwind tested. `-XX:UseAVX=2` also works but turns off all AVX-512 paths and fails to start on ARM hosts, so apply it to x86-64 only. Both need a restart.
- **Make sure you use the right flag, or you may break something.** `-XX:DisableIntrinsic=_base64_decodeBlock` fails without `-XX:+UnlockDiagnosticVMOptions`. Pushed fleet-wide through `JAVA_TOOL_OPTIONS`, that's an outage you caused yourself.
- **Think hard before running someone's runtime patch.** Some proposed tools attach an agent to live JVMs without a restart, distributed via `curl | sh` with pinned certificates and hash checks, which attaches code to production. Read it, test it, schedule it, and expect a temporary throughput dip.
- **Hunt backward.** Search `Authorization` headers and application logs for the shapes above, and check for `hs_err_pid` files and unexplained restarts since before today.
- **Keep deleting, and go a layer deeper.** Unused packages are down to under one percent of what's in images, so keep that discipline. Then ask what feature, shell, or optimization you could turn off inside the things you do use.

## Conclusion

Java4Shell is the third entry in a pattern defenders should have memorized by now: a widely deployed platform, a bug in the low-level code underneath the safe layer, and a researcher with an AI assistant who went from audit to exploit in a few hours. [The Sysdig Threat Research Team](https://www.sysdig.com/threat-research) (TRT) has been tracking the same theme across vulnerabilities like [PHP2Shell](https://www.sysdig.com/blog/php2shell-cve-2026-109618-and-cve-2026-109619-detecting-unauthenticated-remote-code-execution-in-php-core), [Node2Shell](https://www.sysdig.com/blog/node2shell-cve-2026-111497-detecting-the-node-js-brotli-rce), and the [Apache HTTP Server mod\_http2 bug](https://www.sysdig.com/blog/httpd-cve-2026-119618-detecting-heap-corruption-and-rce-in-apache-http-server-mod-http2). The names may change (slightly), but the story remains familiar.

The next iteration may look like a library or runtime a team forgot was in its stack, hit through a field they didn’t know was parsed before auth. The defenses that hold up are the basic ones we know all too well: Know what you run, patch what's exposed first, run less of what you don’t need, and watch what it does at runtime so you aren't relying on the exploit having the courtesy to announce itself early.

Memory safety comes with an asterisk that is often written in assembly. Teams have cleaned up the packages, and now it’s time to pare down the features.
