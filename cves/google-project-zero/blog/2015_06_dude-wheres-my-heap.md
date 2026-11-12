# Dude, where’s my heap? - Project Zero

Source: https://projectzero.google/2015/06/dude-wheres-my-heap.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Guest posted by Ivan Fratric, spraying 1TB of memory


The ability to place controlled content to a predictable location in memory can be an important primitive in exploitation of memory corruption vulnerabilities. A technique that is commonly used to this end in browser exploitation is [heap spraying](http://en.wikipedia.org/wiki/Heap_spraying): By allocating a large amount of memory an attacker ensures that some of the allocations happen in a predictable memory region. In order to break this technique, in Windows 8 Microsoft introduced [High Entropy Bottom-Up Randomization](https://media.blackhat.com/bh-us-12/Briefings/M_Miller/BH_US_12_Miller_Exploit_Mitigation_Slides.pdf). Essentially, it introduces 1TB of variance in start address of heap (as well as stack and other allocations) in 64-bit processes. In a traditional heap spraying scenario, this would mean that the attacker needs to allocate over 1TB of memory in order to place content at a predictable location which is infeasible on today’s computers. Internet Explorer 11 (as well as various other 64-bit processes on Windows 8) employs this mitigation whenever it uses a 64-bit tab process (such as in Metro mode or with Enhanced Protected Mode turned on).

Internet Explorer also introduced another mitigation called [MemoryProtector](http://blog.fortinet.com/post/is-use-after-free-exploitation-dead-the-new-ie-memory-protector-will-tell-you) in order to prevent exploitability of use-after-free vulnerabilities. The two mitigations are not meant to be related. However, somewhat unexpectedly, one can be (ab)used to bypass the other. In one sentence, it is possible to use a timing attack on MemoryProtector to reveal the offset used by High-Entropy Bottom-Up Randomization, thus completely bypassing it.

## The Issue

MemoryProtector is intended to prevent exploitation of a certain kind of use-after-free vulnerabilities. Since details of the mitigation have already been published in various places (such as [here](http://blog.fortinet.com/post/is-use-after-free-exploitation-dead-the-new-ie-memory-protector-will-tell-you)), only the bare essentials sufficient to understand the issue will be given here. Simplified, MemoryProtector prevents exploitability of use-after-free vulnerabilities in which a pointer to a freed object is kept on the stack. This is a common situation in web browsers caused by the code such as

Node\* node = getNodeFromSomewhere();

fireJavaScriptCallback(); // kills node

node->DoSomething();

In the example above, a pointer to the Node object is obtained and stored in a local variable (on stack). After that, a function is called which ends up causing JavaScript callback. Attacker-controlled code in the JavaScript callback causes node to be deleted, but after the control flow returns to the code above, the node is referenced after being deleted (use-after-free condition).

MemoryProtector works by preventing the object (Node in the example above) from being freed if its address can be found on the stack (in the node variable in the example above). If MemoryProtector is enabled, for certain classes, deleting won’t free the memory right away - it will only zero it out. Once the size of those freed-but-not-really objects reaches a certain threshold, MemoryProtector will scan the stack and identify which of these objects have their addresses on the stack. Those that do not will be deleted. The others are left untouched and will be considered again during the next stack scan. Thus it is ensured that no object gets freed while its address is on the stack.

To demonstrate the issue that enables us to defeat High-Entropy Bottom-Up Randomization several observations need to be made. The first observation is that, when scanning the stack, MemoryProtector cannot differentiate between addresses and other types of data on the stack. Thus, it will treat all data on the stack (such as, for example, user-controlled double-precision numbers or 64-bit integers) as addresses. Since some of this data can be attacker-controlled, an attacker can deliberately place something that looks like an address on the stack and prevent an object located at that address from being freed. In fact, an attacker might be able to place multiple addresses on the stack and prevent freeing of objects at any of those addresses. By itself this isn’t very dangerous - it can cause memory exhaustion and not much else.

The second observation to make is that freeing memory takes time, especially for large (such as 1MB used by the PoC) objects where free/delete ends up calling VirtualFree. The time is sufficiently large to observe a difference between the time it takes to free a large object and attempting to delete an object without actually freeing it (which happens with MemoryProtector) if the address of the object is present on the stack during the delete attempt.

This is demonstrated in Figure 1. Notice that for memory range \[0x9ddc000000, 0x9de0000000\] the time it takes for MemoryProtector to run is much less than for other ranges because the block doesn’t get freed during the run. Also notice that the next run takes longer than average. This is because during this run two blocks are freed (one from the current run and one from the previous one).


Figure 1.

Thus by spraying the stack with a range of possible addresses and then triggering a free and measuring the time it takes to free (or not) the object, it is possible to determine if the object was allocated in the given address range or not. If an address of the object is detected, the attacker will also learn the approximate offset used by High Entropy Bottom-Up Randomization and will be able to predict addresses used by future (or past) allocations.

## Description of the Exploit

There are several hoops to jump through in order to exploit the issue. The first one is placing controllable data on the stack. Standard stack spraying techniques such as using a JavaScript function with a lot of local variables or calling a JavaScript function with a lot of arguments don’t actually work because JavaScript variables in IE are stored in a packed format which makes it difficult to have a variable whose representation could also be mistaken for an address (that is, different than the address of a variable itself). However, I have observed that during some numeric computations, such as multiplication, JavaScript engine will place intermediate results in a native double format on the stack. It is trivial to create double-precision numbers that will look like addresses in the required range (0x0000000000 to 0x10000000000).

The second issue is reducing the search space because we don’t want to have to try out all addresses in the lower 1TB range. Since we will be using a large allocation (allocated using VirtualAlloc) it is known that the allocation will be made on 0x1000 boundary (in Windows 8). Thus there are ‘only’ 0x10000000 possibilities. Note also that for each experiment we can place multiple values on the stack at once. The current PoC can test 0x4000 possibilities in one experiment, thus also reducing the number of required experiments to 0x4000 (16K). If each experiment allocates 1M of memory, this means that all experiments allocate a total of 16GB of memory throughout a single PoC run. However note that these allocations are not needed at the same time, in fact only two 1M allocations are needed at any given time plus some stack space and other smaller heap allocation made by the PoC. Thus the PoC should run fine even on machines with very low amount of free RAM.

The next issue is triggering MemoryProtector at the desired time. By looking at the code of MemoryProtection::CMemoryProtector::ReclaimMemory() function, it is easily determined that MemoryProtector triggers after more than 100000 bytes of memory is freed. This is fine because we’ll use an allocation larger than that anyway. In the PoC, MemoryProtector is triggered by first setting the ‘title’ property of a Button HTML element to a large (1MB) string and then to a small string. If the address of a large string is not found on a stack when MemoryProtector is triggered, it will get freed. Otherwise, it will get freed next time MemoryProtector runs if the allocation address is no longer on the stack.

We also need a way to measure time precisely since the times involved will be in sub-millisecond intervals. Fortunately, we can use performance.now() API which is [supported](http://blogs.msdn.com/b/ie/archive/2012/10/19/web-performance-when-millisecond-resolution-just-isn-t-enough.aspx) in Internet Explorer for this.

## Reproducing the Issue

To reproduce the issue you first need to ensure that IE runs tab process in 64-bit mode. There are several ways to accomplish this. Probably the easiest is to open the PoC in IE in Metro mode where 64-bit tab process is used by default. In desktop mode 64-bit is still not the default (though presumably this will change at some point in the future). But you can have 64-bit tab processes in desktop mode as well either by making IE run in a single process mode or enabling Enhanced Protected Mode.

You can make IE run in a single process mode by setting TabProcGrowth registry key to 0, however note that this should never be used when browsing untrusted websites and opening untrusted files as it disables the IE sandbox.

The recommended way to run IE in 64-bit mode is to enable Enhanced Protected Mode,  which can be done by changing Internet Options -> Advanced -> Security -> ‘Enable Enhanced Protected Mode’ and ‘Enable 64-bit processes for Enhanced Protected Mode’. Not only will this enable additional mitigations that can be found on 64-bit Windows but will also enable additional sandboxing features, so I fully recommend that users run IE like this.

Note however, that when Enhanced Protected Mode is enabled, you’ll need to open the PoC in the Internet Zone because Enhanced Protected Mode does not get applied to Local intranet and Trusted sites (including local files). If successful, you should see processes like this when opening the PoC.


Figure 2.

Note: It’s also possible to run the PoC in 32-bit mode with some changes. You need to replace the line ‘o.cur = min + 0x40;’ with ‘o.cur = min + 0x20;’ and the line ‘var max = 0x10000000000;’ with ‘var max = 0x100000000;’. However note that High Entropy Bottom-Up Randomization doesn’t get applied to 32-bit processes so all allocations should (predictably) happen in a low memory range.

After you have the test environment set up, just click “Dude, where’s my heap?” button on the PoC and wait. The entire run of the PoC takes about 30 seconds on a reasonably modern computer.

After the test run finishes, you should see the detected allocation memory range as well as detailed output of memory ranges sorted by time it took to run the experiment. By opening IE process in your favorite debugger you should be able to verify that memory allocations do indeed happen in the detected range. This is demonstrated in Figure 3.


Figure 3.

The PoC currently uses a very simple heuristics to detect if the run was successful - there needs to be a single memory range for which the run time is faster than for all other runs by at least a threshold %. Note that this PoC is made just for demonstration purposes and there are likely ways to make the poc both faster and more reliable. It could be made more reliable for example by repeating the experiments for the small number of best candidates (and possibly adjacent ranges) to verify the result or repeating the entire run if the result can’t be verified. It could also be made faster by breaking early if a good candidate is found in one of the experiments (expected to reduce the run time by half on average), by finding a way to put more user-controlled data on the stack or possibly by incorporating some other insight about the entropy of bottom-up randomization.

## Vendor response

The issue was reported to Microsoft on January 19th in the context of the Mitigation Bypass Bounty program. The initial response (on January 28th) was that the “submission meets Microsoft’s criteria for the Mitigation Bypass” and “has novel elements”. On April 23rd (\~3 months later) I was notified that “investigation determined the effort involved to ship a fix, that enabled MemoryProtect to not allow ASLR bypass down level, would be a significant amount of resources (and possible regression risk) for an issue primarily applicable to a non-default configuration” and Microsoft “will explore ways to mitigate this problem in the next version of our product”. MSRC noted this decision was based on the facts that “64-bit IE is a non-default configuration” and “MemoryProtect has led to a significant overall decrease of IE case submissions”. Thus the issue is still unfixed.

## Potential collision with HP Security Research

On February 5th (2 weeks after I sent my report to Microsoft) HP Security Research announced that they also received a [Mitigation Bypass bounty](http://h30499.www3.hp.com/t5/HP-Security-Research-Blog/HPSR-Microsoft-disclosure-and-the-125-000-bug-bounty/ba-p/6704588#.VW8E-a04Z4s) from Microsoft. In addition to other attacks they mention that “attacker can use MemoryProtection as an oracle to completely bypass ASLR” which leads me to believe that there is a partial (but not complete, judging by the Microsoft response) overlap between our research.

The details of HP’s research are unknown at this time but if I had to guess, I’d say they were using the same basic principle to map the free memory of a 32-bit process. By finding which memory regions are already allocated (addresses where the attacker can’t allocate memory on) it might be possible, based on the allocation address and size, to tell which of these allocations were made by executable modules.

## Conclusion

Both High-Entropy Bottom-Up Randomization and MemoryProtector are really useful mitigations. Without MemoryProtector or in scenarios where the attacker does not have the same amount of control as in a web browser, High-Entropy Bottom-Up Randomization is an efficient defense against heap spraying and similar techniques. Similarly MemoryProtector is an efficient defense for use-after-free vulnerabilities where the object reference is kept on the stack. While it might be possible to bypass it in specific scenarios, it renders a large number of vulnerabilities unexploitable.

It is only when these mitigations come together in an environment with a lot of control given to the attacker, including control over the stack and heap allocation as well as the ability to accurately measure time, that the problem manifests. For what it is worth I agree that fixing the issue would be very difficult without making serious compromises because it basically exploits how the mitigations in question work as intended. Microsoft has a tough job if they indeed want to fix this issue in the future.

As new mitigations grow both in number and complexity this might not be the last time we see them interacting in unexpected ways.
