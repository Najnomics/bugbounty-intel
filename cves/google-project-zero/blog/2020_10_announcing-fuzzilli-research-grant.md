# Announcing the Fuzzilli Research Grant Program - Project Zero

Source: https://projectzero.google/2020/10/announcing-fuzzilli-research-grant.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Samuel Groß, Project Zero

Project Zero’s mission is to make 0-day hard in order to improve end-user security. We attack this problem in different ways, including supporting other security researchers. While Google currently offers [research grants](https://edu.google.com/programs/credits/research/?modal_active=none), they are limited to academics and those affiliated with universities.

Today we are announcing a new USD $50,000 pilot program to foster research into JavaScript engine fuzzing through [Google Compute Engine](https://cloud.google.com/compute) (GCE) credit grants. Here is how it works:

1. Interested researchers [submit a proposal](https://forms.gle/6QWqGD3rEmeeRGuM7) for a project about fuzzing JavaScript engines.
2. The proposal will be reviewed by an internal review board and, if accepted, the researchers will be awarded up to USD $5,000 in GCE credits per submission to be used for fuzzing.
3. All bugs found throughout the course of the project must be reported directly to the affected vendors. Researchers can claim full CVE credits and applicable bug bounties.

## Overview

The program is designed to promote research into new approaches for JavaScript engine fuzzing. Examples of research areas that we are especially interested in include:

- Custom, domain specific sanitizers such as WebKit’s [does GC validation](https://bugs.chromium.org/p/project-zero/issues/detail?id=1802) or [bounds check elimination verification](https://github.com/WebKit/webkit/commit/bf384ad99fc39675da9ee7b66d3c8bb3897625fe) which can help detect bugs that would otherwise go unnoticed as they don’t immediately cause observable failures
- New, possibly domain-specific feedback metrics to guide JavaScript/JIT engine fuzzers
- Different high-level fuzzing approaches such as differential fuzzing
- New code mutation or generation approaches that outperform existing ones
- Targeted approaches to fuzz for variants of previously reported bugs

Applications can be submitted by filling out [this](https://forms.gle/6QWqGD3rEmeeRGuM7) form. Submissions are not limited to those in academia or those with a demonstrated track record of success - if you have a good idea in this space, we'd love to hear from you. Incoming submissions will be reviewed by a review board on a regular basis and we aim to respond to every submission within 2 weeks. If the project is accepted, the researchers may be awarded GCE credits worth up to USD $5,000. Researchers can also apply for multiple grants throughout the lifetime of a project. The grants come with the following requirements:

- The credits must be used for fuzzing JavaScript engines with the approach described in the proposal. The fuzzed JavaScript engines should be one or more of the following: JavaScriptCore (Safari), v8 (Chrome, Edge), or Spidermonkey (Firefox).
- All vulnerabilities found must be only reported to the affected vendor. Researchers are encouraged to apply Project Zero’s 90-day disclosure policy. Researchers may claim any CVE credits and bug bounty payouts for reporting the bugs that don’t conflict with these requirements.
- Any newly developed source code must be published under an open source license that permits further research by others.
- An interim report for Google only at the conclusion of the fuzzing, to demonstrate the initial results of the research, so we can determine the efficacy of the research and make our folks in accounting happy.
- Furthermore, a final report of some form (e.g. a conference paper, a blog post, or a standalone PDF) due no later than 6 months after the first grant for a project has been awarded, including:
- A detailed explanation of the project
- Basic statistics about which engines have been fuzzed for how long (CPU time, iterations, etc.)
- A clear technical explanation of all vulnerabilities discovered throughout the project.

Researchers are encouraged to base their project on the open source [Fuzzilli](https://github.com/googleprojectzero/fuzzilli) fuzzer if possible, which, amongst other features, already [supports distributed fuzzing on GCE](https://github.com/googleprojectzero/fuzzilli/tree/master/Cloud/GCE).

## Timeline

The pilot program will run for one year, from Oct 1, 2020 until Oct 1, 2021. Applications can be submitted at any time during this period, however, the program might end earlier if funds are exhausted.

## Motivation

JavaScript engine security continues to be critical for user safety, as demonstrated by recent in-the-wild 0day exploits abusing vulnerabilities in v8, the JavaScript engine behind Chrome. Unfortunately, fuzzing JavaScript engines to uncover these vulnerabilities is generally quite expensive due to their high complexity and relatively slow processing of input. As a rough datapoint, the GCE instances used to find the [\~20 bugs with Fuzzilli in 2019](https://github.com/googleprojectzero/fuzzilli#bug-showcase) cost around USD $10,000. Income from bug bounty programs is uncertain, as there is no guarantee a new approach will also discover new bugs. Moreover, as any bounty money is paid out only later, researchers need to bear the costs of fuzzing in advance. This likely results in bugs staying unfixed and thus exploitable for longer. This program aims to help solve this problem.

## Scope of Pilot

This program is similar to [Google Cloud research credits](https://edu.google.com/programs/credits/research/?modal_active=none), though that program is limited to  university affiliates. In contrast, this program is specifically designed to accept submissions from anyone.

This program is also similar to the [Chrome Fuzzer Program](https://www.google.com/about/appsecurity/chrome-rewards/#fuzzerprogram). However, the Chrome Fuzzer Program is limited to LibFuzzer-based fuzzers or blackbox fuzzers, neither of which can currently support a fuzzer like Fuzzilli due to technical limitations. In addition, it is also not currently possible to experiment with custom engine “sanitizers” that detect bugs before they result in otherwise observable misbehaviour. Overall, this program allows researchers greater flexibility around their fuzzing approach but limits the scope to JavaScript engine fuzzing.

## Legal points

We are unable to issue grants to individuals who are on sanctions lists, or who are in countries (e.g. Cuba, Iran, North Korea, Sudan and Syria) on sanctions lists. You are responsible for any tax implications depending on your country of residency and citizenship. There may be additional restrictions on your ability to enter depending upon your local law.

This is not a competition, but rather an experimental and discretionary grant program. You should understand that we can cancel the program at any time and the decision as to whether or not to award a grant is entirely at our discretion.

Of course, your testing must not violate any law, or disrupt or compromise any data that is not your own.
