# Struggling RCE on Jenkins Instance

- **Source URL:** https://medium.com/@imusabkhan/struggling-rce-on-jenkins-instance-8851af98b7e6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250731232914/https://medium.com/@imusabkhan/struggling-rce-on-jenkins-instance-8851af98b7e6
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5748 (id 5748)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Struggling RCE on Jenkins Instance

Assalam Alaikum everyone! Welcome to another bug hunting write-up about Jenkins Remote Code Execution, which I reported four years ago on **30th August 2020**. I won’t take much of your time with my introduction, which you can read in my first write-up [here](/@imusabkhan/unveiling-homoglyph-silent-culprit-of-user-level-dos-attacks-86a0576bca3a).

This is my third consecutive bug hunting write-up, and I have many more queued up. Don’t forget to follow me here for future updates.

# Let’s dive into the details

I was looking for a target on HackerOne platform to hunt for vulnerabilities then I suddenly came across a domain containing the keyword *‘Jenkins’*, which immediately caught my attention. let’s call it **REDACTED.COM** for the sake of this writeup.

Domain was something like this**:  jenkins.nc.opensource.REDACTED.COM**

**What is Jenkins**Jenkins is an open source automation server. It helps automate the parts of software development related to building, testing, and deploying, facilitating continuous integration, and continuous delivery. It is a server-based system that runs in servlet containers such as Apache Tomcat.


This was my first experience encountering a Jenkins instance. Before this, I hadn’t encountered Jenkins in my bug hunting journey or penetration testing projects. However, I was aware that bug hunters…
