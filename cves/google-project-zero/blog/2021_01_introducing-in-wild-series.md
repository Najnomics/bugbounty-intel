# Introducing the In-the-Wild Series - Project Zero

Source: https://projectzero.google/2021/01/introducing-in-wild-series.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

This is part 1 of a 6-part series detailing a set of vulnerabilities found by Project Zero being exploited in the wild. To read the other parts of the series, head to the bottom of this post.

At Project Zero we often refer to our goal simply as “make 0-day hard”. Members of the team approach this challenge mainly through the lens of offensive security research. And while we experiment a lot with new targets and methodologies in order to remain at the forefront of the field, it is important that the team doesn’t stray too far from the current state of the art. One of our efforts in this regard is [the tracking](/0day.html) of publicly known cases of zero-day vulnerabilities. We use this information to guide the research. Unfortunately, public 0-day reports rarely include captured exploits, which could provide invaluable insight into exploitation techniques and design decisions made by real-world attackers. In addition, we believe there to be [a gap in the security community’s ability to detect 0-day exploits](/2020/07/detection-deficit-year-in-review-of-0.html).

Therefore, Project Zero has recently launched our own initiative aimed at researching new ways to detect 0-day exploits in the wild. Through partnering with the Google Threat Analysis Group (TAG), one of the first results of this initiative was the discovery of a watering hole attack in Q1 2020 performed by a highly sophisticated actor.

We discovered two exploit servers delivering different exploit chains via watering hole attacks. One server targeted Windows users, the other targeted Android. Both the Windows and the Android servers used Chrome exploits for the initial remote code execution. The exploits for Chrome and Windows included 0-days. For Android, the exploit chains used publicly known n-day exploits. Based on the actor's sophistication, we think it's likely that they had access to Android 0-days, but we didn't discover any in our analysis.

From the exploit servers, we have extracted:

- Renderer exploits for four bugs in Chrome, one of which was still a 0-day at the time of the discovery.
- Two sandbox escape exploits abusing three 0-day vulnerabilities in Windows.
- A “privilege escalation kit” composed of publicly known n-day exploits for older versions of Android.

The four 0-days discovered in these chains have been fixed by the appropriate vendors:

- [CVE-2020-6418](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2020/CVE-2020-6418.html) - Chrome Vulnerability in TurboFan (fixed February 2020)

- [CVE-2020-0938](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2020/CVE-2020-0938.html) - Font Vulnerability on Windows (fixed April 2020)
- [CVE-2020-1020](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2020/CVE-2020-1020.html) - Font Vulnerability on Windows (fixed April 2020)
- [CVE-2020-1027](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2020/CVE-2020-1027.html) - Windows CSRSS Vulnerability (fixed April 2020)

We understand this attacker to be operating a complex targeting infrastructure, though it didn't seem to be used every time. In some cases, the attackers used an initial renderer exploit to develop detailed fingerprints of the users from inside the sandbox. In these cases, the attacker took a slower approach: sending back dozens of parameters from the end users device, before deciding whether or not to continue with further exploitation and use a sandbox escape. In other cases, the attacker would choose to fully exploit a system straight away (or not attempt any exploitation at all). In the time we had available before the servers were taken down, we were unable to determine what parameters determined the "fast" or "slow" exploitation paths.

The Project Zero team came together and spent many months analyzing in detail each part of the collected chains. What did we learn? These exploit chains are designed for efficiency & flexibility through their modularity. They are well-engineered, complex code with a variety of novel exploitation methods, mature logging, sophisticated and calculated post-exploitation techniques, and high volumes of anti-analysis and targeting checks. We believe that teams of experts have designed and developed these exploit chains. We hope this blog post series provides others with an in-depth look at exploitation from a real world, mature, and presumably well-resourced actor.

The posts in this series share the technical details of different portions of the exploit chain, largely focused on what our team found most interesting. We include:

- Detailed analysis of the vulnerabilities being exploited and each of the different exploit techniques,
- A deep look into the bug class of one of the Chrome exploits, and
- An in-depth teardown of the Android post-exploitation code.

In addition, we are posting [root cause analyses](https://googleprojectzero.github.io/0days-in-the-wild/rca.html) for each of the four 0-days discovered as a part of these exploit chains.

Exploitation aside, the modularity of payloads, interchangeable exploitation chains, logging, targeting and maturity of this actor's operation set these apart. We hope that by sharing this information publicly, we are continuing to close the knowledge gap between private exploitation (what well resourced exploitation teams are doing in the real world) and what is publicly known.

We recommend reading the posts in the following order:

1. Introduction (this post)
2. [Chrome: Infinity Bug](/2021/01/in-wild-series-chrome-infinity-bug.html)
3. [Chrome Exploits](/2021/01/in-wild-series-chrome-exploits.html)
4. [Android Exploits](/2021/01/in-wild-series-android-exploits.html)
5. [Android Post-Exploitation](/2021/01/in-wild-series-android-post-exploitation.html)
6. [Windows Exploits](/2021/01/in-wild-series-windows-exploits.html)

This is part 1 of a 6-part series detailing a set of vulnerabilities found by Project Zero being exploited in the wild. To continue reading, see [In The Wild Part 2: Chrome Infinity Bug](/2021/01/in-wild-series-chrome-infinity-bug.html).
