# The Windows Registry Adventure #1: Introduction and research results - Project Zero

Source: https://projectzero.google/2024/04/the-windows-registry-adventure-1.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Mateusz Jurczyk, Google Project Zero


In the 20-month period between May 2022 and December 2023, I thoroughly audited the Windows Registry in search of local privilege escalation bugs. It all started unexpectedly: I was in the process of developing a coverage-based Windows kernel fuzzer based on the Bochs x86 emulator (one of my favorite tools for security research: see [Bochspwn](https://github.com/googleprojectzero/bochspwn), [Bochspwn Reloaded](https://github.com/googleprojectzero/bochspwn-reloaded), and my earlier [font fuzzing infrastructure](/2016/07/a-year-of-windows-kernel-font-fuzzing-2.html)), and needed some binary formats to test it on. My first pick were PE files: they are very popular in the Windows environment, which makes it easy to create an initial corpus of input samples, and a basic fuzzing harness is equally easy to develop with just a single [GetFileVersionInfoSizeW](https://learn.microsoft.com/en-us/windows/win32/api/winver/nf-winver-getfileversioninfosizew) API call. The test was successful: even though I had previously [fuzzed PE files in 2019](https://bugs.chromium.org/p/project-zero/issues/list?q=id%3A1907%2C1908%2C1909%2C1910%2C1911&can=1), the new element of code coverage guidance allowed me to discover a completely new bug: [issue #2281](https://bugs.chromium.org/p/project-zero/issues/detail?id=2281).


For my next target, I chose the Windows registry. That's because arbitrary registry hives can be loaded from disk without any special privileges via the [RegLoadAppKey](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regloadappkeya) API (since Windows Vista). The hives use a binary format and are fully parsed in the kernel, making them a noteworthy local attack surface. Furthermore, I was also somewhat familiar with basic harnessing of the registry, [having fuzzed it in 2016](https://bugs.chromium.org/p/project-zero/issues/list?q=id%3A873%2C874%2C876%2C993&can=1) together with James Forshaw. Once again, the code coverage support proved useful, leading to the discovery of [issue #2299](https://bugs.chromium.org/p/project-zero/issues/detail?id=2299). But when I started to perform a root cause analysis of the bug, I realized that:

- The hive binary format is not very well suited for trivial bitflipping-style fuzzing, because it is structurally simple, and random mutations are much more likely to render (parts of) the hive unusable than to trigger any interesting memory safety violations.
- On the other hand, the registry has many properties that make it an attractive attack surface for further research, especially for manual review. It is 30+ years old, written in C, running in kernel space but highly accessible from user-mode, and it implements much more complex logic than I had previously imagined.


And that's how the story starts. Instead of further refining the fuzzer, I made a detour to reverse engineer the registry implementation in the Windows kernel (internally known as the Configuration Manager) and learn more about its inner workings. The more I learned, the more hooked I became, and before long, I was all-in on a journey to audit as much of the registry code as possible. This series of blog posts is meant to document what I've learned about the registry, including its basic functionality, advanced features, security properties, typical bug classes, case studies of specific vulnerabilities, and exploitation techniques.


While this blog is one of the first places to announce this effort, I did already give a talk titled "Exploring the Windows Registry as a powerful LPE attack surface" at Microsoft BlueHat Redmond in October 2023 (see [slides](https://j00ru.vexillium.org/slides/2023/bluehat.pdf) and [video recording](https://www.youtube.com/watch?v=8mJLe8sZki8)). The upcoming blog posts will go into much deeper detail than the presentation, but if you're particularly curious and can't wait to find out more, feel free to check these resources as a starter. 🙂

## Research results

In the course of the research, I filed [39 bug reports](https://bugs.chromium.org/p/project-zero/issues/list?q=finder%3Amjurczyk%20product%3Akernel%20opened%3E2022-05-01%20opened%3C2024-01-01&can=1) in the Project Zero bug tracker, which have been fixed by Microsoft as 44 CVEs. There are a few reasons for the discrepancy between these numbers:

- Some single reports included information about multiple problems, e.g. [issue #2375](https://bugs.chromium.org/p/project-zero/issues/detail?id=2375) was addressed by four CVEs,
- Some groups of reports were fixed with a single patch, e.g. issues [#2392](https://bugs.chromium.org/p/project-zero/issues/detail?id=2392) and [#2408](https://bugs.chromium.org/p/project-zero/issues/detail?id=2408) as CVE-2023-23420,
- One bug report was closed as WontFix and not addressed in a security bulletin at all ([issue #2508](https://bugs.chromium.org/p/project-zero/issues/detail?id=2508)).


All of the reports were submitted under the Project Zero 90-day disclosure deadline policy, and Microsoft successfully met the deadline in all cases. The average time from report to fix was 81 days.


Furthermore, between November 2023 and January 2024, I reported 20 issues that had low or unclear security impact, but I believed the vendor should nevertheless be made aware of them. They were sent without a disclosure deadline and weren't put on the PZ tracker; I have since published them on our team's [GitHub](https://github.com/googleprojectzero/p0tools/tree/master/WinRegLowSeverityBugs). Upon assessment, Microsoft decided to fix 6 of them in a security bulletin in March 2024, while the other 14 were closed as WontFix with the option of being addressed in a future version of Windows.


This sums up to a total of 50 CVEs, classified by Microsoft as:

- 39 × Windows Kernel Elevation of Privilege Vulnerability
- 9 × Windows Kernel Information Disclosure Vulnerability
- 1 × Windows Kernel Memory Information Disclosure Vulnerability
- 1 × Windows Kernel Denial of Service Vulnerability


A full summary of the security-serviced bugs is shown below:

## Exploitability

Software bugs are typically only interesting to either the offensive/defensive sides of the security community if they have practical security implications. Unfortunately, it is impossible to give a blanket statement regarding the exploitability of all registry-related vulnerabilities due to their sheer diversity on a number of levels:

- Affected platforms: Windows 10, Windows 11, various Windows Server versions (32/64-bit)
- Attack targets: the kernel itself, drivers implementing registry callbacks, privileged user-mode applications/services
- Entry points: direct registry operations, hive loading, transaction log recovery
- End results: memory corruption, broken security guarantees, broken API contracts, memory/pointer disclosure, out-of-bounds reads, invalid/controlled cell index accesses
- Root cause of issues: C-specific, logic errors, bad reference counting, locking problems
- Nature of memory corruption: temporal (use-after-free), spatial (buffer overflows)
- Types of corrupted memory: kernel pools, hive data
- Exploitation time: instant, up to several hours


As we can see, there are multiple factors at play that determine how the bugs came to be and what state they leave the system in after being triggered. However, to get a better understanding of the impact of the findings, I have performed a cursory analysis of the exploitability of each bug, trying to classify it as either "easy", "moderate" or "hard" to exploit according to my current knowledge and experience (this is of course highly subjective). The proportions of these exploitability ratings are shown in the chart below:



The ratings were largely based on the following considerations:

- Hive-based memory corruption is generally considered easy to exploit, while pool-based memory corruption is considered moderate/hard depending on the specifics of the bug.
- Triggering OOM-type conditions in the hive space is easy, but completely exhausting the kernel pools is more difficult and intrusive.
- Logic bugs are typically easier and more reliable to exploit than memory corruption.
- The kernel itself is typically easier to attack than other user-mode processes (system services etc.).
- Direct information disclosure (leaking kernel pointers / uninitialized memory via various channels) is usually straightforward to exploit.
- However, random out-of-bounds reads, as well as read access to invalid/controlled cell indexes is generally hard to do anything useful with.


Overall, it seems that more than half of the findings can be feasibly exploited for information disclosure or local privilege escalation (rated easy or moderate). What is more, many of them exhibit registry-specific bug classes which can enable particularly unique exploitation primitives. For example, hive-based memory corruption can be effectively transformed into both a KASLR bypass and a fully reliable arbitrary read/write capability, making it possible to use a single bug to compromise the kernel with a data-only attack. To demonstrate this, I have successfully developed exploits for CVE-2022-34707 and CVE-2023-23420. The outcome of running one of them to elevate privileges to SYSTEM on Windows 11 is shown on the screenshot below:



Upcoming posts in this series will introduce you to the Windows registry as a system mechanism and as an attack surface, and will dive deeper into practical exploitation using hive memory corruption, out-of-bounds cell indexes and other amusing techniques. Stay tuned!
