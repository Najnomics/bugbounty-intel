# Detecting Kernel Memory Disclosure – Whitepaper - Project Zero

Source: https://projectzero.google/2018/06/detecting-kernel-memory-disclosure.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Mateusz Jurczyk, Project Zero


Since early 2017, we have been working on Bochspwn Reloaded – a piece of dynamic binary instrumentation built on top of the Bochs IA-32 software emulator, designed to identify memory disclosure vulnerabilities in operating system kernels. Over the course of the project, we successfully used it to discover and report over [70](https://bugs.chromium.org/p/project-zero/issues/list?can=1&q=finder%3Amjurczyk+product%3Akernel+opened%3E2017-02-23+opened%3C2018-1-23+%22uninitialized+%22memory+disclosure%22&colspec=ID+Status+Restrict+Reported+Vendor+Product+Finder+Summary&cells=ids) previously unknown security issues in Windows, and more than [10](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/log/?qt=author&q=mjurczyk%40google.com) bugs in Linux. We discussed the general design of the tool at [REcon Montreal](http://j00ru.vexillium.org/slides/2017/recon.pdf) and [Black Hat USA](http://j00ru.vexillium.org/slides/2017/bhusa.pdf) in June and July last year, and followed up with the description of the latest implemented features and their results at [INFILTRATE](http://j00ru.vexillium.org/slides/2018/infiltrate.pdf) in April 2018 (click on the links for slides).


As we learned during this study, the problem of leaking uninitialized kernel memory to user space is not caused merely by simple programming errors. Instead, it is deeply rooted in the nature of the C programming language, and has been around since the very early days of privilege separation in operating systems. In an attempt to systematically outline the background of the bug class and the current state of the art, we wrote a comprehensive paper on this subject. It aims to provide an exhaustive guide to kernel infoleaks, their genesis, related prior work, means of detection and future avenues of research. While a significant portion of the document is dedicated to Bochspwn Reloaded, it also covers other methods of infoleak detection, non-memory data sinks and alternative applications of full-system instrumentation, including the evaluation of some of the ideas based on the developed prototypes and experiments performed as part of this work.


Without further ado, enjoy the read:
