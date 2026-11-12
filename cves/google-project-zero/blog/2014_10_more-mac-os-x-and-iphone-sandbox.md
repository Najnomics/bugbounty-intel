# More Mac OS X and iPhone sandbox escapes and kernel bugs - Project Zero

Source: https://projectzero.google/2014/10/more-mac-os-x-and-iphone-sandbox.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Ian Beer


A couple of weeks ago Apple released [OS X 10.9.5](http://support.apple.com/kb/ht6443) and [iOS 8](http://support.apple.com/kb/HT6441) which fixed a number of sandbox escapes and privilege escalation bugs found by Project Zero. All-bar-one of these bugs were found via manual source code auditing where there was source and binary analysis where there wasn’t. As always, click through the bugs for proof-of-concept code and further details:


CVE-2014-4403\* \[ [https://code.google.com/p/google-security-research/issues/detail?id=23](https://code.google.com/p/google-security-research/issues/detail?id=23) \] was as issue allowing a kernel ASLR bypass on OS X due to insufficient randomization of very early kernel heap allocations, the addresses of which could be leaked using the unprivileged SGDT instruction. This bug could be exploited from within any sandbox on OS X and allowed an attacker to determine the load address of the kernel.


were all bounds-checking bugs in the driver for the Intel integrated HD GPU present on all current-generation Macs. Eight of these bugs allowed controlled kernel memory corruption from with most sandboxes on OS X (those with access to the GPU such as the Safari renderer process or the Chrome GPU process.)


CVE-2014-4402\* \[ [https://code.google.com/p/google-security-research/issues/detail?id=33](https://code.google.com/p/google-security-research/issues/detail?id=33) \] was another case of missing bounds checks, this time in another part of the graphics acceleration pipeline.


CVE-2014-4376\* \[ [https://code.google.com/p/google-security-research/issues/detail?id=31](https://code.google.com/p/google-security-research/issues/detail?id=31) \] was a kernel NULL-pointer dereference when setting up IOKit shared memory. This was exploitable from within some sandboxed 32-bit processes on OS X (for example the Chrome GPU process.) As is true with all these bugs this bug also allows any unsandboxed processes to execute code in the kernel.


were bugs affecting OS X and iOS in the implementation of the IOKit IODataQueue class where the kernel trusted index and size fields in shared memory which was mapped into userspace and writable. Looking at the [release notes for iOS 8](http://support.apple.com/kb/HT6441) these bugs seem to be very similar to one used in the recent Pangu Team jailbreak which was released a few days after these bugs were reported to Apple.


were integer overflows in the bounds checking code of IODataQueue allowing kernel memory corruption on iOS and OS X.


was another shared memory queuing bug, this time in the bluetooth stack.


was an interesting kernel heap overflow when parsing a binary keyboard map which affected iOS and OS X and was reachable by setting an IOKit registry value. See the linked bug for more details along with a PoC demonstrating kernel instruction pointer control.


was another bug in the keyboard mapping code affecting iOS and OS X allowing userspace to read arbitrary kernel memory.


was a kernel NULL pointer dereference due to incorrect error handling in the key map parsing code, again see the linked bug for a PoC demonstrating kernel instruction pointer control on OS X.


Finding and eliminating sandbox escapes is an important focus for Project Zero. The attack surface to break out of a sandbox is often smaller than the attack surface available to remote attackers to gain an initial foothold inside a sandbox. Therefore, strengthening sandboxes represents a solid return on investment of time.


Our research seems to indicate that sandbox break-outs on OS X and iOS are an under-researched topic. We’d encourage others to join us in bringing these sandboxes up to strength.


You can keep up-to-date with the latest Project Zero research by subscribing to labels in our bug tracker: [https://code.google.com/p/google-security-research/issues/subscriptions](https://code.google.com/p/google-security-research/issues/subscriptions)


(\*) These bugs exceeded Project Zero’s standard 90-day disclosure deadline.

(+) These bugs were only fixed on iOS and remain unpatched on OS X.
