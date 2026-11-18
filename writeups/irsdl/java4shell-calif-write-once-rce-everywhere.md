# java4shell-calif-write-once-rce-everywhere

- **Source URL:** https://calif.io/java4shell/
- **Fetched:** 2026-11-18
- **Researcher:** irsdl
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

After we disclosed [PHP2Shell](https://calif.io/php2shell), we realized many people didn't know what PHP was. So we decided to go after something a little more familiar: Java.

Today, we are disclosing Java4Shell (CVE-2026-114938), a memory-corruption vulnerability in OpenJDK's Base64 decoder. OpenJDK is the most popular Java runtime. Under CVSS 4.0, this vulnerability scores 9.2 out of 10 (CRITICAL).

While PHP is a high-level web technology, Java sits much deeper. Java is the world's [third most popular programming language](https://www.tiobe.com/tiobe-index/), powering [90% of Fortune 500 companies](https://www.ibm.com/new/announcements/java-at-30-and-beyond-how-ibm-is-securing-the-future-of-java). It is the beating heart of the modern economy. Banking, aviation, telecommunications, nearly every critical sector runs on Java, including national security systems.

Base64 is a very common way of representing binary data as text. It is used in authentication protocols, to encode file uploads, and to deliver network messages. To decode Base64 faster, OpenJDK uses specialized x86-64 CPU instructions to process many bytes at once. We discovered a bug in that optimized machine-level code that lets malformed input overwrite neighboring memory. With careful exploitation, the corruption can reveal sensitive memory, as [Heartbleed](https://www.heartbleed.com/) did, or lead to remote code execution. The corruption itself can be triggered by just 64 `A` characters followed by a single `=`:

`AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=`
In older OpenJDK 17, the trigger input is 128 of `A` followed by `=`.

## Write once, RCE everywhere

Our initial testing demonstrated remote code execution in the following widely deployed Java applications, in their default configs.

Pre-auth RCE:

- Keycloak
- Atlassian Jira
- Atlassian Confluence
- JFrog Artifactory
- Jenkins
- PingFederate

Post-auth RCE:

- Apache Kafka Broker
- Apache Solr
- Elasticsearch
- Gerrit
- Spinnaker

The lists are non-exhaustive. We also demonstrated RCE in sample applications built on widely used frameworks, including Apache Struts and Spring Boot. Ordinary features such as authentication and file uploads can expose the vulnerable Base64 decoder, extending the potential impact far beyond the products we tested. [samczsun](https://x.com/samczsun) also shared a client-side exploit with us. A Java program that opens a TLS connection to a malicious server can be compromised, even if it exposes no service of its own.

Here are a demo video of the exploits running:

## Wait, Java has a memory-corruption vulnerability, in Base64?!

Yes. First time?

Memory corruption is the most common class of vulnerability on the Internet. But one of Java's biggest selling points is memory safety. Java manages memory on developers' behalf and checks memory accesses, protecting applications from the memory-corruption bugs common in other software.

But like PHP and many other technologies, much of Java itself is written in low-level languages like C, C++, and, in this case, assembly, where memory corruption is still a part of life.

To speed up Base64 decoding, OpenJDK uses specialized AVX-512 VBMI instructions on supported x86-64 processors. The bug sits in the hand-rolled assembly code that handles the final few characters. For the 65-character input above, OpenJDK allocates a 50-byte result array. After decoding the first 64 characters, the routine mishandles the stray `=` and calculates a negative output length. That invalid length becomes a full 64-byte write, sending 62 bytes past the end of the array. Java eventually rejects the input, but by then neighboring objects may already be corrupted.

## Era of the centaur hacker

As with PHP2Shell, Calif used AI to find and weaponize Java4Shell. AI brings the horsepower. Our researchers bring the context. The best hacker today is neither AI nor human. It is the *centaur hacker*, part human, part AI.

It took our own Quang Luong an hour to discover the vulnerability, and two more hours to develop the first working exploit. The total token cost was less than $200.

One thing to note about this vulnerability is that there is no universal exploit. Depending on how Base64 is used and how the application works, different steps may be required for exploitation. Calif was able to accelerate the exploit development by spending initial effort building pipelines and strategies, then directing AI agents to use those for initial exploitation. Afterwards, most of the later chains are built almost autonomously with AI.

## The tragedy of the commons

Java is one of many shared software stacks we all rely on. Over the years, it has grown to serve many different needs. Each feature request may make sense on its own, but everyone inherits the added complexity. Those who need a feature get the benefit. Everyone else carries the code and its risks, even if they never use it.

Java4Shell is a concrete example. The Base64 optimization helps applications that decode enormous amounts of data. But the code ships to everyone else too, including applications that gain little from it. On affected systems, an optimization few applications needed became a serious security risk.

Features can be useful, and most bugs can be fixed. But why do we have to worry about code we never needed in the first place?

## A call for vibe-uncoding

If you don't need something, there is little reason to keep it running in your systems. Do you need that hand-rolled assembly Base64 decoder to process a few hundred bytes? Probably not.

Earlier this year we found [Squidbleed](https://calif.io/research/squidbleed), an older cousin of Heartbleed, hiding in the Squid proxy since 1997. The bug was in Squid's FTP module. But who uses FTP anymore? It's a dead protocol and should be removed.

Removing code is harder than it sounds. An apparently unused feature may have hidden dependencies. Someone has to understand what can be removed, make the change, and test what remains.

This is where AI can help to make that work practical at a scale we could not previously afford.

The same centaur hacker that discovered PHP2Shell and Java4Shell can comb a large codebase and flag dead code, bloated features, and needless optimizations. We call this *vibe-uncoding*: identify the parts a system actually needs, then remove everything else to reduce its attack surface.

With AI, everyone is asking, “What can we build?” But maybe the right question for security is, “What can we delete?”
