# Breaking Guava’s BloomFilter

- **Source URL:** https://medium.com/@pswor69/breaking-guavas-bloomfilter-a-6-byte-denial-of-service-2f859d87afb3
- **Fetched from:** https://medium.com/@pswor69/breaking-guavas-bloomfilter-a-6-byte-denial-of-service-2f859d87afb3?source=rss-9d0bd2103d69------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14888 (id 14888)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** k3tu / Sun, 30 Aug 2026 06:22:04 GMT

*How an unbounded deserialization allocation in Google Guava turned a handful of attacker-controlled bytes into a guaranteed OutOfMemoryError, and the fuzz harness I built to prove it.*

Guava’s BloomFilter.readFrom() deserializes a Bloom filter from a stream but never validates the dataLength field embedded in that stream. An attacker who controls the input, as little as 6 bytes, can force Guava to attempt a multi-gigabyte heap allocation and crash the JVM with an OutOfMemoryError.

I built a fuzz target for OSS-Fuzz that reproduces this deterministically, then reported it through Google’s OSS VRP. Google merged the fuzz harness into OSS-Fuzz, and a fix landed shortly after. This post covers how the bug works and how I built the fuzzer that proves it.

Guava’s BloomFilter is a probabilistic set-membership structure. Developers use it to avoid unnecessary cache lookups or to filter out obviously-absent keys before running a more expensive check. Guava lets you serialize a BloomFilter to a stream and reconstruct it later through BloomFilter.readFrom(InputStream, Funnel).

The serialized format is simple:

byte strategyOrdinal

byte numHashFunctions

int dataLength

long\[dataLength\] data

The third field causes the problem. readFrom() reads dataLength straight from the stream and uses it to size an internal long\[\] array. It checks no upper bound and never confirms how much data the stream actually holds.

Here’s what happens when readFrom() processes a malicious stream:

Each long takes 8 bytes, so an attacker can set dataLength to something like 0x7FFFFFFF and force Guava to attempt roughly 16 GB of allocation, from an input that might itself be a handful of bytes. The allocation happens deep inside LockFreeBitArray's construction path, well before any check against the remaining stream length.

The result is deterministic. The JVM throws OutOfMemoryError. Depending on how the calling application handles deserialization, that error can crash a worker thread, kill a process, or take down any service that deserializes Bloom filters from untrusted sources: cache warmers, RPC payloads, uploaded snapshots, and similar paths.

This is CWE-770, allocation of resources without limits or throttling. It’s also a reminder that deserialization code deserves the same scrutiny as any other untrusted-input boundary, even in something as mundane as a probabilistic data structure.

I skipped hand-crafting a single proof-of-concept input and instead wrote BloomFilterReadFromFuzzer.java, a [Jazzer](https://github.com/CodeIntelligenceTesting/jazzer)-based harness that targets BloomFilter.readFrom() directly, built for inclusion in [OSS-Fuzz](https://github.com/google/oss-fuzz), Google's continuous fuzzing infrastructure for open-source projects.

The harness works in three stages.

First, it rejects anything under 6 bytes immediately, since that’s the minimum needed to even reach the vulnerable allocation (1 byte for strategyOrdinal, 1 for numHashFunctions, 4 for dataLength). Then it parses dataLength itself out of bytes 2 through 5, big-endian, purely for reporting. This step never touches Guava. I wanted the crash report to already contain the requested allocation size and an amplification factor (requested bytes divided by input size) before Guava even runs, so I compute both up front with Math.multiplyExact, wrapped in a try/catch so an overflow in my own arithmetic doesn't mask the real bug.

Second, it hands the raw bytes to BloomFilter.readFrom() inside a try-with-resources block, then calls mightContain("probe") on the result. That extra call matters: it forces any lazily-triggered allocation to run before the harness exits, so I don't miss a crash that only happens on first use of the deserialized filter.

Third, the catch logic does the actual triage. An OutOfMemoryError gets caught specifically and turned into a FuzzerSecurityIssueCritical, with a message built from the input size, the parsed dataLength, the requested allocation in bytes, and the amplification factor:

```
message.append("Amplification factor: ")
       .append(String.format("%.2f", amplification))
       .append("x\n");
```
That message also states the root cause directly in the crash report, so anyone triaging the OSS-Fuzz finding doesn’t have to reverse-engineer it from a bare stack trace. Meanwhile IOException, IllegalArgumentException, and ArithmeticException all pass through silently in a separate catch block. Those three represent Guava (or my own overflow check) correctly rejecting malformed input, and flagging them as issues would just add noise.

Within seconds of running, the fuzzer found the minimum 6-byte input reliably triggered multi-gigabyte allocation attempts. The amplification factor ran into the billions.

BloomFilter.readFrom() trusts the dataLength metadata embedded in the input and passes it straight into allocation logic. It never validates that the claimed size is plausible given the remaining stream contents, and it never bounds the value against any sane maximum. Treat every length-prefixed field in untrusted input as adversarial until proven otherwise. This one wasn't.

I reported the finding along with the fuzz harness through Google’s OSS VRP program. Google merged the fuzz target, [BloomFilterReadFromFuzzer.java](https://github.com/google/oss-fuzz/pull/15484), into OSS-Fuzz's Guava project, so it now runs continuously against Guava's codebase to catch regressions of this exact bug class going forward.

The Guava team then merged [a fix](https://github.com/google/guava/pull/8449) that adds a new overload, BloomFilter.readFrom(InputStream, Funnel, long), which lets callers pass a maximum data size to enforce during deserialization. Both changes reference each other directly: the fix cites the fuzz target, and the fuzz target now guards against regressions of the issue the fix addresses.

Length-prefixed deserialization is a classic footgun. Any time untrusted input tells your code how much to allocate, that number needs a ceiling, independent of whether the rest of the input can even justify it.

A good fuzz harness outlives the bug it found. The value here isn’t just the one crash. This harness now runs on every future Guava change, forever, as part of OSS-Fuzz’s continuous fuzzing.

Fuzzing “boring” utility code pays off, too. BloomFilter doesn't parse HTML or handle network protocols. It's a data structure, and it's easy to assume utility-library code carries low risk. But deserialization logic, even inside the most mundane class, is still an attacker-facing boundary the moment it touches untrusted input.

*If you work on a project that deserializes anything from untrusted sources, ask yourself: is every length field in that format actually bounded, or just trusted?*
