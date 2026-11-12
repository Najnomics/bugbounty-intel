# MTE As Implemented, Part 1: Implementation Testing - Project Zero

Source: https://projectzero.google/2023/08/mte-as-implemented-part-1.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

By Mark Brand, Project Zero

## Background

In 2018, in the [v8.5a version](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-a-profile-architecture-2018-developments-armv85a) of the ARM architecture, ARM proposed a hardware implementation of tagged memory, referred to as MTE (Memory Tagging Extensions).

Through mid-2022 and early 2023, Project Zero had access to pre-production hardware implementing this instruction set extension to evaluate the security properties of the implementation. In particular, we're interested in whether it's possible to use this instruction set extension to implement effective security mitigations, or whether its use is limited to debugging/fault detection purposes.


As of the v8.5a specification, MTE can operate in two distinct modes, which are switched between on a per-thread basis. The first mode is sync-MTE, where tag-check failure on a memory access will cause the instruction performing the access to deliver a fault at retirement. The second mode is async-MTE, where tag-check failure does not directly (at the architectural level) cause a fault. Instead, tag-check failure will cause the setting of a per-core flag, which can then be polled from the kernel context to detect when an invalid access has occurred.


This blog post documents the tests that we have performed so far, and the conclusions that we've drawn from them, [together with the code necessary to repeat these tests](https://github.com/googleprojectzero/p0tools/tree/master/MTETest). This testing was intended to explore both the details of the hardware implementation of MTE, and the current state of the software support for MTE in the Linux kernel. All of the testing is based on manually implemented tagging in statically-linked standalone binaries, so it should be easy to reproduce these results on any compatible hardware.

## Terminology

When designing and implementing security features, it's important to be conscious of the specific protection goal. In order to provide clarity in the rest of this post, we'll define some specific terminology that we use when talking about this:

1. Mitigation - A mitigation is something that reduces real exploitability of a vulnerability or class of vulnerability. The expectation is that attackers can (and eventually will) find their way around it. Examples would be DEP, ASLR, CFI.

1. "Soft" Mitigation - We consider a mitigation to be "soft" if the expectation is that an attacker pays a one-time cost in order to bypass the mitigation. Typically this would be a per-target cost, for example developing a ROP chain to bypass DEP, which can usually be largely re-used between different exploits for the same target software.
2. "Hard" Mitigation - We consider a mitigation to be "hard" if the expectation is that an attacker cannot develop a bypass technique which is reusable between different vulnerabilities (without, e.g. incorporating an additional vulnerability). An example would be ASLR, which is typically bypassed either by the use of a separate information leak vulnerability, or by developing an information leak primitive using the same vulnerability.

Note that the context can have an impact on the "hardness" of a mitigation -

if a codebase is particularly rich in code-patterns which allow the construction of

information leaks, it's quite possible that an attacker can develop a reliable, reusable

technique for turning various memory corruption primitives into an information leak

within that codebase.

1. Solution - a solution is something that eliminates exploitability of a vulnerability or class of vulnerability. The expectation is that the only way for an attacker to bypass a solution would be an unintended implementation weakness in the solution.

For example (based purely on a theoretical implementation of memory tagging):

\- Randomly-allocating tags to heap allocations cannot be considered a solution for any class of heap-related memory corruption, since this provides at best probabilistic protection.

\- Allocating odd and even tags to adjacent heap allocations might theoretically be able to provide a solution for linear heap-buffer overflows.

## Hardware Implementation

The main hardware implementation question we had was, does a speculative side-channel exist that would allow leaking whether or not a tag-check has succeeded, without needing to architecturally execute the tag-check?


It is expected that Spectre-type speculative execution side-channels will still allow an attacker to leak pointer values from memory, indirectly leaking the tags. Here we consider whether the implementation introduces additional speculative side-channels that would allow an attacker to more efficiently leak tag-check success/failure.


TL; DR; In our testing we did not identify an additional[1](#h.d43f6ia2nolp) speculative side-channel that would allow such an attack to be performed.

### 1. Does MTE block Spectre? (NO)

The only way that MTE could prevent exploitation of Spectre-type weaknesses would be to have speculative execution stall the pipeline until the tag-check completes[2](#h.8v9sdwwdtqt). This might sound desirable ("prevent exploitation of Spectre-type weaknesses") but it's not - this would create a much stronger side-channel to allow an attacker to create an oracle for tag-check success, weakening the overall security properties of the MTE implementation.


This is easy to test. If we can still leak data out of speculative execution using Spectre when the pointer used for the speculative access has an incorrect tag, then this is not the case.

We wrote a [small patch](https://github.com/googleprojectzero/p0tools/blob/master/MTETest/0001-Add-MTE-spectre-test.patch) to the [safeside](https://github.com/google/safeside) demo spectre\_v1\_pht\_sa that demonstrates this:

| mte\_device:/data/local/tmp $ ./spectre\_v1\_pht\_sa\_mte Leaking the string: 1t's a s3kr3t!!! Done! Checking that we would crash during architectural access: Segmentation fault | 

### 2. Does tag-check success/failure have a measurable impact on the speculation window length? (Probably NOT)

There is a deeper question that we'd like to understand: is the length of speculative execution after a memory access influenced by whether the tag-check for that access succeeds or fails? If this was the case, then we might be able to build a more complex speculative side-channel that we could use in a similar way.

In order to measure this, we need to force a mis-speculation, and then perform a read access to memory for which a tag-check would either succeed or fail, and then we need to use a speculative side-channel to measure how many further instructions were successfully speculatively executed. We wrote and tested a self-contained harness to measure this, which can be found in speculation\_window.c


This harness works by generating code for a test function with a variable number of no-op instructions at runtime, and then repeatedly executing this test function in a loop to train the branch-predictor before finally triggering mis-speculation. The test function is as follows:

| ldr x0, \[x0\] ; this load is slow (\*x0 is uncached) cbnz x0, speculation: ; this branch is always taken during warmup ret speculation: ldr x1, \[x1\] ; this load is fast (\*x1 is cached) ; the tag-check success or fail will happen on ; this access, but during warmup the tag-check ; will always be a success. orr x2, x2, x1 ; this is a no-op (as x1 is always 0) but it ... n times ... ; maintains a data dependency between the orr x2, x2, x1 ; loads (and the no-ops), hopefully preventing ; too much re-ordering. ldr x2, \[x2\] ; \*x2 is uncached, if it is cached later then ; this instruction was (probably) executed. ret | 


In this way we can measure the number of no-ops that we can insert before the final load no longer executes (ie. the result from the first load is received and we realise that we've mispredicted the branch so we flush the pipeline before the final load is executed).


In order to reduce bias due to branch-predictor behaviour, the test program is run separately for the tag-check success and tag-check failure case, and the control-flow being run is identical in both cases.


In order to reduce bias due to cpu power-management/throttling behaviour, each time the test program is run, it collects a single set of samples and then exits. We then run this program repeatedly, and by interleaving the runs for tag-check success and tag-check fail we look to reduce this influence on the results. In addition, the cores are down-clocked to the lowest supported frequency using the standard linux cpu scaling interface, which should reduce the impact of cpu throttling to a minimum.


Most modern mobile devices also have non-homogenous core designs, with for example a 4+4, 2+2+4 or 1+3+4 core design. Since the device under test is no exception, the program needs to pin itself to a specific core and we need to run these tests for each core design separately.

Reading from the virtual timer is extremely slow (relative to memory access instructions), and this results in noisy data when attempting to measure single-cache-hit/single-cache-miss. In a normal real-world environment, a shared-memory timer is often a better approach to timing with this level of granularity, and that's an approach that we've used previously with success. In this case, since we want to get data for each core, it was difficult to get consistency across all cores, and we had better results using an amplification approach performing accesses to multiple cache-lines.

However, this approach adds more complexity to the measuring code, and more possibilities for smart prefetching or similar to interfere with our measurements. Since we are trying to test the properties of the hardware, rather than develop a practical attack that needs to run in a timely fashion, we decided to minimise these risks and instead collect enough data that we'd be able to see the patterns through the noise.


The first graphs below show this data for a region of the x-axis (nop-count) on each core around where the speculation window ends (so the x-axis is anchored differently for each core), and on the y-axis we plot the observed probability that our measurement results in a cache-miss. Two separate lines are plotted in each graph; one in red for the "tag-check-fail" case and one in green for the "tag-check-pass" case. We can't really see the green line at all - the two lines overlap so closely as to be indistinguishable.


If we really zoom in on measurements from the "Biggest" core, we can see the two lines deviating due to the noise:



Another interesting point is to notice that the graph we have for the biggest core tops out at a probability of \~30%; this is (probably) not because we're hitting the cache, but instead that the timer read is slow that we can't use it to reliably differentiate between cache misses and cache hits most of the time. If we look at a graph of raw latency measurements, we can see this:



The important thing is that there's no significant difference between the results for the failure and success cases, which suggests that there's no clear speculative side-channel that would allow an attacker to build a side-channel tag-check oracle directly.

## Software Implementation

There are several ways that we identified that the current software implementation around the use of MTE could lead to bypasses if MTE were used as a security mitigation. 

As described below, Issues [1](#h.mom86f64gsnm) and [2](#h.5lefjf6v19hr) are quirks of the current implementation that it may or may not be possible to address with kernel changes. They are both of limited scope and only apply to very specific conditions, so they likely don't have a particularly significant impact on the applicability of MTE as a security mitigation (although they have some implications for the coverage of such a mitigation.)


Issue [3](#h.slz47uww66dv) is a detail of the current implementation of Breakpad, and serves to highlight a particular class of weakness that will require careful audit of signal handling code in any application that wishes to use MTE as a security mitigation.

Issue [4](#h.quhrhy4chqpx) is a fundamental weakness that likely cannot be effectively addressed. We would not characterize this as meaning that MTE could not be applied as a security mitigation, but rather a limitation on the claims that one could make about the effectiveness of such a mitigation.


To be more specific, both issues [3](#h.slz47uww66dv) and [4](#h.quhrhy4chqpx) are bound by some fairly significant limitations, which would have varying impact on exploitability of memory corruption issues depending on the specific context in which the issue occurs. See below for more discussion on this topic.


TL;DR; In our testing we identified some areas for improvement on the software side, and demonstrated that it is possible to use the narrow "exploitation window" to avoid the side-effects of tag-check failures under some circumstances, meaning that any mitigation based on async MTE is likely limited to a "soft mitigation" regardless of tagging strategy.

### 1. Handling of system call arguments \[ASYNC\]

There's a [documented limitation](https://elixir.bootlin.com/linux/v5.18.9/source/Documentation/arm64/memory-tagging-extension.rst#L111) of the current handling of the async MTE check mode in the linux kernel, which is that the kernel does not catch invalid accesses to userspace pointers. This means that kernel-space accesses to incorrectly tagged user-space pointers during a system call will not be detected.


There are likely good technical reasons for this limitation, but we plan to investigate improving this coverage in the future.


We provide a sample that demonstrates this limitation, [software\_issue\_1.c](https://github.com/googleprojectzero/p0tools/blob/master/MTETest/software_issue_1.c).

| mte\_enable(false, DEFAULT\_TAG\_MASK); uint64\_t\* ptr = mmap(NULL, 0x1000, PROT\_READ\|PROT\_WRITE\|PROT\_MTE, MAP\_ANONYMOUS\|MAP\_PRIVATE, -1, 0); uint64\_t\* tagged\_ptr = mte\_tag\_and\_zero(ptr, 0x1000); memset(tagged\_ptr, 0x23, 0x1000); int fd = open("/dev/urandom", O\_RDONLY); fprintf(stderr, "%p %p\n", ptr, tagged\_ptr); read(fd, ptr, 0x1000); assert(\*tagged\_ptr == 0x2323232323232323ull); | 

| taro:/ $ /data/local/tmp/software\_issue\_1 0x7722c5d000 0x800007722c5d000 software\_issue\_1: ./software\_issue\_1.c:46: int main(int, char \*\*): Assertion \`\*tagged\_ptr == 0x2323232323232323ull' failed. | 

### 2. Handling of system call arguments \[SYNC\]

The way that the sync MTE check mode is currently implemented in the linux kernel means that kernel-space accesses to incorrectly tagged user-space pointers result in the system call returning EFAULT. While this is probably the cleanest and simplest approach, and is consistent with current kernel behaviour especially when it comes to handling results for partial operations, this has the potential to lead to bypasses/oracles in some circumstances.


We plan to investigate replacing this behaviour with SIGSEGV delivery instead (specifically for MTE tag check failures).


The provided sample, [software\_issue\_2.c](https://github.com/googleprojectzero/p0tools/blob/master/MTETest/software_issue_2.c) is a very simple demonstration of this situation.

| size\_t readn(int fd, void\* ptr, size\_t len) { char\* start\_ptr = ptr; char\* read\_ptr = ptr; while (read\_ptr \< start\_ptr + len) { ssize\_t result = read(fd, read\_ptr, start\_ptr + len - read\_ptr); if (result \<= 0) { return read\_ptr - start\_ptr; } else { read\_ptr += result; } } return len; } int main(int argc, char\*\* argv) { int pipefd\[2\]; mte\_enable(true, DEFAULT\_TAG\_MASK); uint64\_t\* ptr = mmap(NULL, 0x1000, PROT\_READ\|PROT\_WRITE\|PROT\_MTE, MAP\_ANONYMOUS\|MAP\_PRIVATE, -1, 0); ptr = mte\_tag(ptr, 0x10); strcpy(ptr, "AAAAAAAAAAAAAAA"); assert(!pipe(pipefd)); write(pipefd\[1\], "BBBBBBBBBBBBBBB", 0x10); // In sync MTE mode, kernel MTE tag-check failures cause system calls to fail // with EFAULT rather than triggering a SIGSEGV. Existing code doesn't // generally expect to receive EFAULT, and is very unlikely to handle it as a // critical error. uint64\_t\* new\_ptr = ptr; while (!strcmp(new\_ptr, "AAAAAAAAAAAAAAA")) { // Simulate a use-after-free, where new\_ptr is repeatedly free'd and ptr // is accessed after the free via a syscall. new\_ptr = mte\_tag(new\_ptr, 0x10); strcpy(new\_ptr, "AAAAAAAAAAAAAAA"); size\_t bytes\_read = readn(pipefd\[0\], ptr, 0x10); fprintf(stderr, "read %zu bytes\nnew\_ptr string is %s\n", bytes\_read, new\_ptr); } } | 

| taro:/ $ /data/local/tmp/software\_issue\_2 read 0 bytes new\_ptr string is AAAAAAAAAAAAAAA read 0 bytes new\_ptr string is AAAAAAAAAAAAAAA read 0 bytes new\_ptr string is AAAAAAAAAAAAAAA read 0 bytes new\_ptr string is AAAAAAAAAAAAAAA read 0 bytes new\_ptr string is AAAAAAAAAAAAAAA read 0 bytes new\_ptr string is AAAAAAAAAAAAAAA read 0 bytes new\_ptr string is AAAAAAAAAAAAAAA read 16 bytes new\_ptr string is BBBBBBBBBBBBBBB | 

### 3. New dangers in signal handlers \[ASYNC\].

Since SIGSEGV is a catchable signal, any signal handlers that can handle SIGSEGV become a critical attack surface for async MTE bypasses. [Breakpad](https://www.google.com/url?q=https://www.chromium.org/developers/crash-reports/&sa=D&source=docs&ust=1661952947380022&usg=AOvVaw3HyXTOsL3B1fRSnMg9GdO3)[/Crashpad](https://www.google.com/url?q=https://www.chromium.org/developers/crash-reports/&sa=D&source=docs&ust=1661952947380022&usg=AOvVaw3HyXTOsL3B1fRSnMg9GdO3) at present have a signal handler (ie, installed in all Chrome processes) which allows a trivial same-thread bypass for async MTE as a security protection, which is demonstrated in async\_bypass\_signal\_handler.c / async\_bypass\_signal\_handler.js.


The concept is simple - if we can corrupt any state that would result in the signal handler concluding that a SIGSEGV coming from a tag-check failure is handled/safe, then we can effectively disable MTE for the process.


If we look at the current [breakpad signal handler](https://source.chromium.org/chromium/chromium/src/+/main:third_party/breakpad/breakpad/src/client/linux/handler/exception_handler.cc;l=328) (the crashpad signal handler has [the same design](https://source.chromium.org/chromium/chromium/src/+/main:third_party/crashpad/crashpad/client/crashpad_client_linux.cc;drc=db6f1567b8caa6dacdd0d46b2a7ac60c5b5ddc82;l=201)):

| void ExceptionHandler::SignalHandler(int sig, siginfo\_t\* info, void\* uc) { // Give the first chance handler a chance to recover from this signal // // This is primarily used by V8. V8 uses guard regions to guarantee memory // safety in WebAssembly. This means some signals might be expected if they // originate from Wasm code while accessing the guard region. We give V8 the // chance to handle and recover from these signals first. if (g\_first\_chance\_handler\_ != nullptr && g\_first\_chance\_handler\_(sig, info, uc)) { return; } | 


It's clear that if our exploit could patch g\_first\_chance\_handler\_ to point to any function that will return a non-zero value, then this will mean that tag-check failures are no longer caught.


The example we've provided in [async\_signal\_handler\_bypass.c](https://github.com/googleprojectzero/p0tools/blob/master/MTETest/async_signal_handler_bypass.c) and [async\_signal\_handler\_bypass.js](https://github.com/googleprojectzero/p0tools/blob/master/MTETest/async_signal_handler_bypass.js) demonstrates an exploit using this technique against a simulated bug in the [duktape javascript interpreter](https://duktape.org/).

| taro:/data/local/tmp $./async\_bypass\_signal\_handler ./async\_bypass\_signal\_handler.js offsets: 0x26c068 0x36bc80 starting script execution access segv handler 11 Async MTE has been bypassed \[0.075927734375ms\] done | 


It seems hard to imagine designing a signal handler that will be robust against all possible attacks here, as most data that is accessed by the signal handler will now need to be treated as untrusted. It's our understanding that Android is considering making changes to the way that the kernel handles these failures to guarantee delivery of these errors to an out-of-process handler, preventing this kind of bypass.

### 4. Generic bypass in multi-threaded environments \[ASYNC\].

Since async MTE failures are only delivered when the thread which caused the error enters the kernel, there's a slightly more involved (but more generic) bypass available in multi-threaded environments. If we can coerce another thread into performing our next exploit steps for us, then we can bypass the protection this way.


The example we've provided in [async\_thread\_bypass.c](https://github.com/googleprojectzero/p0tools/blob/master/MTETest/async_thread_bypass.c) and [async\_thread\_bypass.js](https://github.com/googleprojectzero/p0tools/blob/master/MTETest/async_thread_bypass.js) demonstrates an exploit using this technique against a simulated bug in the duktape javascript interpreter.

| taro:/data/local/tmp $ ./async\_bypass\_thread ./async\_bypass\_thread.js thread is running Async MTE bypassed! | 


Note that in practice, the technique here would most likely be to have the coerced thread simply install a new signal handler to effectively reimplement 3. above, but the example invokes a shell command as a demonstration.

## How wide are these windows?

So, we've identified two methods by which a compromised thread might avoid the consequences of performing invalid accesses. This was a known and expected limitation of async-MTE-as-a-security-mitigation — but how significant is this?


In the existing (linux) kernel implementation, an outstanding async-MTE failure is delivered as a SIGSEGV when the thread that performed the faulting access transitions to kernel mode. This means that the user-to-kernel transition can be thought of as a synchronisation barrier for tag-check failures. 

This leads us to our first rule for async-MTE-safe exploitation:

1. We need to complete our exploit (or disable async-MTE) without needing to make a system call from the faulting thread.


This will already pose a significant limitation in some contexts - for example, many network services will have a \`read/write\` loop in between commands, so this would mean that the exploit must be completed within the execution of a single command. However, for many other contexts, this is less of an issue - a vulnerability in a complex file format parser, decompression algorithm or scripting engine will likely provide sufficient control between system calls to complete an exploit (as demonstrated above with the duktape javascript engine).


There is then a second requirement that the exploit-writer needs to bear in mind, which is the periodic timer interrupt. In the kernel configuration tested, this was set to \`CONFIG\_HZ\_250\`, so we can expect a timer interrupt every 4ms, leading us to our second rule[3](#h.vc7otbihpy9e):

1. We need to complete our exploit in  \~0.2 ms if we want to get acceptable (95%[4](#h.uu3o4hva4l1j)) reliability. (+0.01ms exploit runtime => -0.25% reliability)


[Part 2](/2023/08/mte-as-implemented-part-2-mitigation.html) continues with a higher-level analysis of the effectiveness of various different MTE configurations in a variety of user-space application contexts, and what type of impact we'd expect to see on attacker cost.
