# Project Zero Patch Tuesday roundup, November 2014 - Project Zero

Source: https://projectzero.google/2014/11/project-zero-patch-tuesday-roundup.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Chris Evans, Registrar of Bugs


It’s been about a week since Patch Tuesday, and the Project Zero reports mentioned in the various advisories are now public. We won’t always be writing a Patch Tuesday roundup, but we often will when we believe there is a sufficiently varied and interesting array of bugs to study. This month is such a month. Separately to this summary, we expect to write more in-depth posts for some of the most interesting individual vulnerabilities.


Internet Explorer sandbox escapes

Project Zero member James Forshaw has been busy looking for sandbox escapes on the Windows platform, resulting in a mention in two [Microsoft](https://technet.microsoft.com/library/security/MS14-071) [bulletins](https://technet.microsoft.com/library/security/MS14-065). Sandbox escapes remain a focus of Project Zero because they are a more tractable attack surface to lock down than the typically large applications that run inside them.


[This bug](https://code.google.com/p/google-security-research/issues/detail?id=95)is worth highlighting. It’s a permissions issue leading to an interesting attack: gain writeable access to some important settings and use that to turn off Protected Mode (aka. the sandbox)! Finding and fixing permissions issues is important because they can be very quickly, easily and reliably exploited.


This [permissions issue](https://code.google.com/p/google-security-research/issues/detail?id=97) is also of note. It permits read-only access to the memory of the medium integrity (unsandboxed) process. At first glance, this doesn’t sound like a sandbox escape. However, there’s a trick that leverages this to leak a secret which leads to the ability to take over the process. This will be fully covered in an upcoming blog post.


Microsoft Office memory corruption vulnerabilities

Project Zero member Ben Hawkes found three vulnerabilities in Microsoft Office, leading to [this bulletin](https://technet.microsoft.com/library/security/MS14-069). We’ve seen the occasional [0-day triggerable by opening Office files](https://technet.microsoft.com/library/security/2953095), which is one factor we balance when considering where to help.


[These](https://code.google.com/p/google-security-research/issues/detail?id=107)

[three](https://code.google.com/p/google-security-research/issues/detail?id=108)

[bugs](https://code.google.com/p/google-security-research/issues/detail?id=110)are now public in our tracker. You can see the PoC files and see how in some cases, we were able to minimize the PoC down to just a single bit flip from an original input document. You can also see how triaging exploitability of crashes -- particularly where you only have binaries -- can be surprisingly involved! It’s easy to see why simple automated approaches like !exploitable have a lot of false negatives.


Flash Player bytecode verification logic errors

Project Zero member Ian Beer focused in on an interesting area of research: logic errors in the bytecode verifier. The Flash bytecode security model is to verify certain properties of the bytecode once, up front, leading to various simplifications and optimization opportunities later. Any errors in verification can lead to serious runtime errors later. To pick a specific example, [this bug](https://code.google.com/p/google-security-research/issues/detail?id=106) tells the story of an incorrect assumption leading to a type confusion at runtime and a nice PoC which faults at the attacker-specified address 0x414243 while attempting to load a function pointer.


Flash Player memory corruption vulnerabilities

Project Zero members Tavis Ormandy and Chris Evans and Project Zero affiliate Natalie Silvanovich reported miscellaneous memory corruption vulnerabilities. To briefly highlight a couple of issues, [this bug](https://code.google.com/p/google-security-research/issues/detail?id=120) is a type confusion that triggers in the legacy ActionScript 2 APIs and cannot be readily reached unless you use an old-style .as compiler. As always, putting in effort to test legacy code often bears fruit. And [this bug](https://code.google.com/p/google-security-research/issues/detail?id=122) raises eyebrows because even though it is a wild memcpy() of approximate length -1, there are signs of exploitability. Sometimes during testing, it isn’t the memcpy() thread that crashes, but another thread that happened to be doing some busy work in parallel.


OS X sandbox escape

All of the bugs mentioned so far were fixed well within Project Zero’s 90-day disclosure deadline, representing a solid security response by the Adobe Flash, Microsoft Office, Internet Explorer and Microsoft Windows product teams. In addition to these bugs, [this OS X sandbox escape](https://code.google.com/p/google-security-research/issues/detail?id=92) is also now publicly viewable on account of exceeding the deadline. We calibrate our deadline to balance two important factors: the right of end users to know about a risk versus giving vendors a fair chance to cleanly fix a bug under a reasonable embargo. Given the ratio of deadline hits to misses, we think we’ve calibrated correctly for the current state of the industry but we do hope to tighten the deadline in the future.

This sandbox escape doesn’t give direct access to a highly privileged context (such as ring0) but it does provide an avenue to escape a sandbox policy, which is a useful escalation. For example, this bug could be chained with other bugs such as [kernel NULL pointer dereferences](https://code.google.com/p/google-security-research/issues/detail?id=20).
