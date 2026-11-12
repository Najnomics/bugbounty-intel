# Racing against the clock -- hitting a tiny kernel race window - Project Zero

Source: https://projectzero.google/2022/03/racing-against-clock-hitting-tiny.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

TL;DR:

How to make a tiny kernel race window really large even on kernels without CONFIG\_PREEMPT:

- use a cache miss to widen the race window a little bit
- make a timerfd expire in that window (which will run in an interrupt handler - in other words, in hardirq context)
- make sure that the wakeup triggered by the timerfd has to churn through 50000 waitqueue items created by epoll


Racing one thread against a timer also avoids accumulating timing variations from two threads in each race attempt - hence the title. On the other hand, it also means you now have to deal with how hardware timers actually work, which introduces its own flavors of weird timing variations.

# Introduction

I recently discovered a race condition ([https://crbug.com/project-zero/2247](https://crbug.com/project-zero/2247)) in the Linux kernel. (While trying to explain to someone how [the fix for CVE-2021-0920](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=cbcf01128d0a92e131bd09f1688fe032480b65ca) worked - I was explaining why the Unix GC is now safe, and then got confused because I couldn't actually figure out why it's safe after that fix, eventually realizing that it actually isn't safe.) It's a fairly narrow race window, so I was wondering whether it could be hit with a small number of attempts - especially on kernels that aren't built with CONFIG\_PREEMPT, which would make it possible to preempt a thread with another thread, [as I described at LSSEU2019](https://static.sched.com/hosted_files/lsseu2019/04/LSSEU2019%20-%20Exploiting%20race%20conditions%20on%20Linux.pdf#page=12).


This is a writeup of how I managed to hit the race on a normal Linux desktop kernel, with a hit rate somewhere around 30% if the proof of concept has been tuned for the specific machine. I didn't do a full exploit though, I stopped at getting evidence of use-after-free (UAF) accesses (with the help of a very large file descriptor table and [userfaultfd](https://lwn.net/Articles/819834/), which might not be available to normal users depending on system configuration) because that's the part I was curious about.


This also demonstrates that even very small race conditions can still be exploitable if someone sinks enough time into writing an exploit, so be careful if you dismiss very small race windows as unexploitable or don't treat such issues as security bugs.


The UAF reproducer is [in our bugtracker](https://bugs.chromium.org/p/project-zero/issues/detail?id=2247#c6).

# The bug

In the UNIX domain socket garbage collection code (which is needed to deal with reference loops formed by UNIX domain sockets that use SCM\_RIGHTS file descriptor passing), the kernel tries to figure out whether it can account for all references to some file by comparing the file's refcount with the number of references from inflight SKBs (socket buffers). If they are equal, it assumes that the UNIX domain sockets subsystem effectively has exclusive access to the file because it owns all references.


(The same pattern also appears for files as an optimization in \_\_fdget\_pos(), see [this LKML thread](https://lore.kernel.org/lkml/CAG48ez1pnatAB095dnbrn9LbuQe4+ENwh-WEW36pM40ozhpruw@mail.gmail.com/).)


The problem is that struct file can also be referenced from an RCU read-side critical section (which you can't detect by looking at the refcount), and such an RCU reference can be upgraded into a refcounted reference using get\_file\_rcu() / get\_file\_rcu\_many() by \_\_fget\_files() as long as the refcount is non-zero. For example, when this happens in the dup() syscall, the resulting reference will then be installed in the FD table and be available for subsequent syscalls.


When the garbage collector (GC) believes that it has exclusive access to a file, it will perform operations on that file that violate the locking rules used in normal socket-related syscalls such as recvmsg() - unix\_stream\_read\_generic() assumes that queued SKBs can only be removed under the ->iolock mutex, but the GC removes queued SKBs without using that mutex. (Thanks to Xingyu Jin for explaining that to me.)


One way of looking at this bug is that the GC is working correctly - here's a state diagram showing some of the possible states of a struct file, with more specific states nested under less specific ones and with the state transition in the GC marked:


While \_\_fget\_files() is making an incorrect assumption about the state of the struct file while it is trying to narrow down its possible states - it checks whether get\_file\_rcu() / get\_file\_rcu\_many() succeeds, which narrows the file's state down a bit but not far enough:


And this directly leads to how [the bug was fixed](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=054aa8d439b9185d4f5eb9a90282d1ce74772969) (there's [another follow-up patch](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=e386dfc56f837da66d00a078e5314bc8382fab83), but that one just tries to clarify the code and recoup some of the resulting performance loss) - the fix adds another check in \_\_fget\_files() to properly narrow down the state of the file such that the file is guaranteed to be live:


The fix ensures that a live reference can only be derived from another live reference by comparing with an FD table entry, which is guaranteed to point to a live object.

\[Sidenote: This scheme is similar to the one used for struct page - gup\_pte\_range() also uses the "grab pointer, increment refcount, recheck pointer" pattern for locklessly looking up a struct page from a page table entry while ensuring that new refcounted references can't be created without holding an existing reference. This is really important for struct page because a page can be given back to the page allocator and reused while gup\_pte\_range() holds an uncounted reference to it - freed pages still have their struct page, so there's no need to delay freeing of the page - so if this went wrong, you'd get a page UAF.\]


My initial suggestion was to instead fix the issue by changing how unix\_gc() ensures that it has exclusive access, letting it set the file's refcount to zero to prevent turning RCU references into refcounted ones; this would have avoided adding any code in the hot \_\_fget\_files() path, but it would have only fixed unix\_gc(), not the \_\_fdget\_pos() case I discovered later, so it's probably a good thing this isn't how it was fixed:

\[Sidenote: In my original bug report I wrote that you'd have to wait an RCU grace period in the GC for this, but that wouldn't be necessary as long as the GC ensures that a reaped socket's refcount never becomes non-zero again.\]

# The race

There are multiple race conditions involved in exploiting this bug, but by far the trickiest to hit is that we have to race an operation into the tiny race window in the middle of \_\_fget\_files() (which can e.g. be reached via dup()), between the file descriptor table lookup and the refcount increment:


static struct file \*\_\_fget\_files(struct files\_struct \*files, unsigned int fd,

fmode\_t mask, unsigned int refs)

{

struct file \*file;


rcu\_read\_lock();

loop:

file = files\_lookup\_fd\_rcu(files, fd); // race window start

if (file) {

/\* File object ref couldn't be taken.

\* dup2() atomicity guarantee is the reason

\* we loop to catch the new file (or NULL pointer)

\*/

if (file->f\_mode & mask)

file = NULL;

else if (!get\_file\_rcu\_many(file, refs)) // race window end

goto loop;

}

rcu\_read\_unlock();


return file;

}


In this race window, the file descriptor must be closed (to drop the FD's reference to the file) and a unix\_gc() run must get past the point where it checks the file's refcount ("total\_refs = file\_count(u->sk.sk\_socket->file)").


In the Debian 5.10.0-9-amd64 kernel at version 5.10.70-1, that race window looks as follows:


\<\_\_fget\_files+0x1e> cmp r10,rax

\<\_\_fget\_files+0x21> sbb rax,rax

\<\_\_fget\_files+0x24> mov rdx,QWORD PTR \[r11+0x8\]

\<\_\_fget\_files+0x28> and eax,r8d

\<\_\_fget\_files+0x2b> lea rax,\[rdx+rax\*8\]

\<\_\_fget\_files+0x2f> mov r12,QWORD PTR \[rax\] ; RACE WINDOW START

; r12 now contains file\*

\<\_\_fget\_files+0x32> test r12,r12

\<\_\_fget\_files+0x35> je ffffffff812e3df7 \<\_\_fget\_files+0x77>

\<\_\_fget\_files+0x37> mov eax,r9d

\<\_\_fget\_files+0x3a> and eax,DWORD PTR \[r12+0x44\] ; LOAD (for ->f\_mode)

\<\_\_fget\_files+0x3f> jne ffffffff812e3df7 \<\_\_fget\_files+0x77>

\<\_\_fget\_files+0x41> mov rax,QWORD PTR \[r12+0x38\] ; LOAD (for ->f\_count)

\<\_\_fget\_files+0x46> lea rdx,\[r12+0x38\]

\<\_\_fget\_files+0x4b> test rax,rax

\<\_\_fget\_files+0x4e> je ffffffff812e3def \<\_\_fget\_files+0x6f>

\<\_\_fget\_files+0x50> lea rcx,\[rsi+rax\*1\]

\<\_\_fget\_files+0x54> lock cmpxchg QWORD PTR \[rdx\],rcx ; RACE WINDOW END (on cmpxchg success)


As you can see, the race window is fairly small - around 12 instructions, assuming that the cmpxchg succeeds.

# Missing some cache

Luckily for us, the race window contains the first few memory accesses to the struct file; therefore, by making sure that the struct file is not present in the fastest CPU caches, we can widen the race window by as much time as the memory accesses take. The standard way to do this is to use an eviction pattern / [eviction set](https://www.cs.columbia.edu/~simha/spyjs.ccs15.pdf); but instead we can also make the cache line dirty on another core (see [Anders Fogh's blogpost](https://dreamsofastone.blogspot.com/2016/02/row-hammer-java-script-and-mesi.html) for more detail). (I'm not actually sure about the intricacies of how much latency this adds on different manufacturers' CPU cores, or on different CPU generations - I've only tested different versions of my proof-of-concept on Intel Skylake and Tiger Lake. Differences in cache coherency protocols or snooping might make a big difference.)


For the cache line containing the flags and refcount of a struct file, this can be done by, on another CPU, temporarily bumping its refcount up and then changing it back down, e.g. with close(dup(fd)) (or just by accessing the FD in pretty much any way from a multithreaded process).


However, when we're trying to hit the race in \_\_fget\_files() via dup(), we don't want any cache misses to occur before we hit the race window - that would slow us down and probably make us miss the race. To prevent that from happening, we can call dup() with a different FD number for a warm-up run shortly before attempting the race. Because we also want the relevant cache line in the FD table to be hot, we should choose the FD number for the warm-up run such that it uses the same cache line of the file descriptor table.

# An interruption

Okay, a cache miss might be something like a few dozen or maybe hundred nanoseconds or so - that's better, but it's not great. What else can we do to make this tiny piece of code much slower to execute?


On Android, kernels normally set CONFIG\_PREEMPT, which would've allowed abusing the scheduler to somehow interrupt the execution of this code. The way I've done this in the past was to give the victim thread a low scheduler priority and pin it to a specific CPU core together with another high-priority thread that is blocked on a read() syscall on an empty pipe (or eventfd); when data is written to the pipe from another CPU core, the pipe becomes readable, so the high-priority thread (which is registered on the pipe's waitqueue) becomes schedulable, and an inter-processor interrupt (IPI) is sent to the victim's CPU core to force it to enter the scheduler immediately.


One problem with that approach, aside from its reliance on CONFIG\_PREEMPT, is that any timing variability in the kernel code involved in sending the IPI makes it harder to actually preempt the victim thread in the right spot.


(Thanks to the [Xen security team](https://xenproject.org/users/security/) - I think the first time I heard the idea of using an interrupt to widen a race window might have been from them.)

# Setting an alarm

A better way to do this on an Android phone would be to trigger the scheduler not from an IPI, but from an expiring high-resolution timer on the same core, although I didn't get it to work (probably because my code was broken in unrelated ways).


High-resolution timers (hrtimers) are exposed through many userspace APIs. Even the timeout of select()/pselect() uses an hrtimer, although this is an hrtimer that normally has some slack applied to it to allow batching it with timers that are scheduled to expire a bit later. An example of a non-hrtimer-based API is the timeout used for reading from a UNIX domain socket (and probably also other types of sockets?), which can be set via SO\_RCVTIMEO.


The thing that makes hrtimers "high-resolution" is that they don't just wait for the next periodic clock tick to arrive; instead, the expiration time of the next hrtimer on the CPU core is programmed into a hardware timer. So we could set an absolute hrtimer for some time in the future via something like timer\_settime() or timerfd\_settime(), and then at exactly the programmed time, the hardware will raise an interrupt! We've made the timing behavior of the OS irrelevant for the second side of the race, the only thing that matters is the hardware! Or... well, almost...

# \[Sidenote\] Absolute timers: Not quite absolute

So we pick some absolute time at which we want to be interrupted, and tell the kernel using a syscall that accepts an absolute time, in nanoseconds. And then when that timer is the next one scheduled, the OS converts the absolute time to whatever clock base/scale the hardware timer is based on, and programs it into hardware. And the hardware usually supports programming timers with absolute time - e.g. on modern X86 (with X86\_FEATURE\_TSC\_DEADLINE\_TIMER), you can simply write an absolute Time Stamp Counter(TSC) deadline into MSR\_IA32\_TSC\_DEADLINE, and when that deadline is reached, you get an interrupt. The situation on arm64 is similar, using the timer's comparator register (CVAL).


However, on both X86 and arm64, even though the clockevent subsystem is theoretically able to give absolute timestamps to clockevent drivers (via ->set\_next\_ktime()), the drivers instead only implement ->set\_next\_event(), which takes a relative time as argument. This means that the absolute timestamp has to be converted into a relative one, only to be converted back to absolute a short moment later. The delay between those two operations is essentially added to the timer's expiration time.


Luckily this didn't really seem to be a problem for me; if it was, I would have tried to repeatedly call timerfd\_settime() shortly before the planned expiry time to ensure that the last time the hardware timer is programmed, the relevant code path is hot in the caches. (I did do some experimentation on arm64, where this seemed to maybe help a tiny bit, but I didn't really analyze it properly.)

# A really big list of things to do

Okay, so all the stuff I said above would be helpful on an Android phone with CONFIG\_PREEMPT, but what if we're trying to target a normal desktop/server kernel that doesn't have that turned on?


Well, we can still trigger hrtimer interrupts the same way - we just can't use them to immediately enter the scheduler and preempt the thread anymore. But instead of using the interrupt for preemption, we could just try to make the interrupt handler run for a really long time.


Linux has the concept of a "timerfd", which is a file descriptor that refers to a timer. You can e.g. call read() on a timerfd, and that operation will block until the timer has expired. Or you can monitor the timerfd using epoll, and it will show up as readable when the timer expires.


When a timerfd becomes ready, all the timerfd's waiters (including epoll watches), which are queued up in a linked list, are woken up via the wake\_up() path - just like when e.g. a pipe becomes readable. Therefore, if we can make the list of waiters really long, the interrupt handler will have to spend a lot of time iterating over that list.


And for any waitqueue that is wired up to a file descriptor, it is fairly easy to add a ton of entries thanks to epoll. Epoll ties its watches to specific FD numbers, so if you duplicate an FD with hundreds of dup() calls, you can then use a single epoll instance to install hundreds of waiters on the file. Additionally, a single process can have lots of epoll instances. I used 500 epoll instances and 100 duplicate FDs, resulting in 50 000 waitqueue items.

# Measuring race outcomes

A nice aspect of this race condition is that if you only hit the difficult race (close() the FD and run unix\_gc() while dup() is preempted between FD table lookup and refcount increment), no memory corruption happens yet, but you can observe that the GC has incorrectly removed a socket buffer (SKB) from the victim socket. Even better, if the race fails, you can also see in which direction it failed, as long as no FDs below the victim FD are unused:

- If dup() returns -1, it was called too late / the interrupt happened too soon: The file\* was already gone from the FD table when \_\_fget\_files() tried to load it.
- If dup() returns a file descriptor:

- If it returns an FD higher than the victim FD, this implies that the victim FD was only closed after dup() had already elevated the refcount and allocated a new FD. This means dup() was called too soon / the interrupt happened too late.
- If it returns the old victim FD number:

- If recvmsg() on the FD returned by dup() returns no data, it means the race succeeded: The GC wrongly removed the queued SKB.
- If recvmsg() returns data, the interrupt happened between the refcount increment and the allocation of a new FD. dup() was called a little bit too soon / the interrupt happened a little bit too late.


Based on this, I repeatedly tested different timing offsets, using a spinloop with a variable number of iterations to skew the timing, and plotted what outcomes the race attempts had depending on the timing skew.

## Results: Debian kernel, on Tiger Lake

I tested this on a Tiger Lake laptop, with the same kernel as shown in the disassembly. Note that "0" on the X axis is offset -300 ns relative to the timer's programmed expiry.


## Results: Other kernel, on Skylake



These measurements are from an older laptop with a Skylake CPU, running a different kernel. Here "0" on the X axis is offset -1 us relative to the timer. (These timings are from a system that's running a different kernel from the one shown above, but I don't think that makes a difference.)


The exact timings of course look different between CPUs, and they probably also change based on CPU frequency scaling? But still, if you know what the right timing is (or measure the machine's timing before attempting to actually exploit the bug), you could hit this narrow race with a success rate of about 30%!

# How important is the cache miss?

The previous section showed that with the right timing, the race succeeds with a probability around 30% - but it doesn't show whether the cache miss is actually important for that, or whether the race would still work fine without it. To verify that, I patched my test code to try to make the file's cache line hot (present in the cache) instead of cold (not present in the cache):


@@ -312,8 +312,10 @@

}


+#if 0

// bounce socket's file refcount over to other cpu

pin\_to(2);

close(SYSCHK(dup(RESURRECT\_FD+1-1)));

pin\_to(1);

+#endif


//printf("setting timer\n");

@@ -352,5 +354,5 @@

close(loop\_root);

while (ts\_is\_in\_future(spin\_stop))

\- close(SYSCHK(dup(FAKE\_RESURRECT\_FD)));

\+ close(SYSCHK(dup(RESURRECT\_FD)));

while (ts\_is\_in\_future(my\_launch\_ts)) /\*spin\*/;


With that patch, the race outcomes look like this on the Tiger Lake laptop:


# But wait, those graphs make no sense!

If you've been paying attention, you may have noticed that the timing graphs I've been showing are really weird. If we were deterministically hitting the race in exactly the same way every time, the timing graph should look like this (looking just at the "too-early" and "too-late" cases for simplicity):


Sure, maybe there is some microarchitectural state that is different between runs, causing timing variations - cache state, branch predictor state, frequency scaling, or something along those lines -, but a small number of discrete events that haven't been accounted for should be adding steps to the graph. (If you're mathematically inclined, you can model that as the result of a convolution of the ideal timing graph with the timing delay distributions of individual discrete events.) For two unaccounted events, that might look like this:

But what the graphs are showing is more of a smooth, linear transition, like this:


And that seems to me like there's still something fundamentally wrong. Sure, if there was a sufficiently large number of discrete events mixed together, the curve would eventually just look like a smooth smear - but it seems unlikely to me that there is such a large number of somewhat-evenly distributed random discrete events. And sure, we do get a small amount of timing inaccuracy from sampling the clock in a spinloop, but that should be bounded to the execution time of that spinloop, and the timing smear is far too big for that.


So it looks like there is a source of randomness that isn't a discrete event, but something that introduces a random amount of timing delay within some window. So I became suspicious of the hardware timer. The kernel is using MSR\_IA32\_TSC\_DEADLINE, and the Intel SDM tells us that that thing is programmed with a TSC value, which makes it look as if the timer has very high granularity. But MSR\_IA32\_TSC\_DEADLINE is a newer mode of the LAPIC timer, and the older LAPIC timer modes were instead programmed in units of the APIC timer frequency. According to the [Intel SDM, Volume 3A](https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-vol-3a-part-1-manual.pdf#page=378), section 10.5.4 "APIC Timer", that is "the processor’s bus clock or core crystal clock frequency (when TSC/core crystal clock ratio is enumerated in CPUID leaf 0x15) divided by the value specified in the divide configuration register". This frequency is significantly lower than the TSC frequency. So perhaps MSR\_IA32\_TSC\_DEADLINE is actually just a front-end to the same old APIC timer?


I tried to measure the difference between the programmed TSC value and when execution was actually interrupted (not when the interrupt handler starts running, but when the old execution context is interrupted - you can measure that if the interrupted execution context is just running RDTSC in a loop); that looks as follows:


As you can see, the expiry of the hardware timer indeed adds a bunch of noise. The size of the timing difference is also very close to the crystal clock frequency - the TSC/core crystal clock ratio on this machine is 117. So I tried plotting the absolute TSC values at which execution was interrupted, modulo the TSC / core crystal clock ratio, and got this:

This confirms that MSR\_IA32\_TSC\_DEADLINE is (apparently) an interface that internally converts the specified TSC value into less granular bus clock / core crystal clock time, at least on some Intel CPUs.


But there's still something really weird here: The TSC values at which execution seems to be interrupted were at negative offsets relative to the programmed expiry time, as if the timeouts were rounded down to the less granular clock, or something along those lines. To get a better idea of how timer interrupts work, I measured on yet another system (an old Haswell CPU) with a patched kernel when execution is interrupted and when the interrupt handler starts executing relative to the programmed expiry time (and also plotted the difference between the two):

So it looks like the CPU starts handling timer interrupts a little bit before the programmed expiry time, but interrupt handler entry takes so long (\~450 TSC clock cycles?) that by the time the CPU starts executing the interrupt handler, the timer expiry time has long passed.


Anyway, the important bit for us is that when the CPU interrupts execution due to timer expiry, it's always at a LAPIC timer edge; and LAPIC timer edges happen when the TSC value is a multiple of the TSC/LAPIC clock ratio. An exploit that doesn't take that into account and wrongly assumes that MSR\_IA32\_TSC\_DEADLINE has TSC granularity will have its timing smeared by one LAPIC clock period, which can be something like 40ns.



The \~30% accuracy we could achieve with the existing PoC with the right timing is already not terrible; but if we control for the timer's weirdness, can we do better?


The problem is that we are effectively launching the race with two timers that behave differently: One timer based on calling clock\_gettime() in a loop (which uses the high-resolution TSC to compute a time), the other a hardware timer based on the lower-resolution LAPIC clock. I see two options to fix this:

1. Try to ensure that the second timer is set at the start of a LAPIC clock period - that way, the second timer should hopefully behave exactly like the first (or have an additional fixed offset, but we can compensate for that).
2. Shift the first timer's expiry time down according to the distance from the second timer to the previous LAPIC clock period.


(One annoyance with this is that while we can grab information on how wall/monotonic time is calculated from TSC from the vvar mapping used by the vDSO, the clock is subject to minuscule additional corrections at every clock tick, which occur every 4ms on standard distro kernels (with CONFIG\_HZ=250) as long as any core is running.)


I tried to see whether the timing graph would look nicer if I accounted for this LAPIC clock rounding and also used a custom kernel to cheat and control for possible skid introduced by the absolute-to-relative-and-back conversion of the expiry time (see further up), but that still didn't help all that much.

# (No) surprise: clock speed matters

Something I should've thought about way earlier is that of course, clock speed matters. On newer Intel CPUs with P-states, the CPU is normally in control of its own frequency, and dynamically adjusts it as it sees fit; the OS just provides some hints.


Linux has an interface that claims to tell you the "current frequency" of each CPU core in /sys/devices/system/cpu/cpufreq/policy\<n>/scaling\_cur\_freq, but when I tried using that, I got a different "frequency" every time I read that file, which seemed suspicious.


Looking at the implementation, it turns out that the value shown there is calculated in arch\_freq\_get\_on\_cpu() and its callees - the value is calculated on demand when the file is read, with results cached for around 10 milliseconds. The value is determined as the ratio between the deltas of MSR\_IA32\_APERF and MSR\_IA32\_MPERF between the last read and the current one. So if you have some tool that is polling these values every few seconds and wants to show average clock frequency over that time, it's probably a good way of doing things; but if you actually want the current clock frequency, it's not a good fit.


I hacked a helper into my kernel that samples both MSRs twice in quick succession, and that gives much cleaner results. When I measure the clock speeds and timing offsets at which the race succeeds, the result looks like this (showing just two clock speeds; the Y axis is the number of race successes at the clock offset specified on the X axis and the frequency scaling specified by the color):


So clearly, dynamic frequency scaling has a huge impact on the timing of the race - I guess that's to be expected, really.


But even accounting for all this, the graph still looks kind of smooth, so clearly there is still something more that I'm missing - oh well. I decided to stop experimenting with the race's timing at this point, since I didn't want to sink too much time into it. (Or perhaps I actually just stopped because I got distracted by newer and shinier things?)

# Causing a UAF

Anyway, I could probably spend much more time trying to investigate the timing variations (and probably mostly bang my head against a wall because details of execution timing are really difficult to understand in detail, and to understand it completely, it might be necessary to use something like [Gamozo Labs' "Sushi Roll"](https://gamozolabs.github.io/metrology/2019/08/19/sushi_roll.html) and then go through every single instruction in detail and compare the observations to the internal architecture of the CPU). Let's not do that, and get back to how to actually exploit this bug!


To turn this bug into memory corruption, we have to abuse that the recvmsg() path assumes that SKBs on the receive queue are protected from deletion by the socket mutex while the GC actually deletes SKBs from the receive queue without touching the socket mutex. For that purpose, while the unix GC is running, we have to start a recvmsg() call that looks up the victim SKB, block until the unix GC has freed the SKB, and then let recvmsg() continue operating on the freed SKB. This is fairly straightforward - while it is a race, we can easily slow down unix\_gc() for multiple milliseconds by creating lots of sockets that are not directly referenced from the FD table and have many tiny SKBs queued up - here's a graph showing the unix GC execution time on my laptop, depending on the number of queued SKBs that the GC has to scan through:




To turn this into a UAF, it's also necessary to get past the following check near the end of unix\_gc():


/\* All candidates should have been detached by now. \*/

BUG\_ON(!list\_empty(&gc\_candidates));


gc\_candidates is a list that previously contained all sockets that were deemed to be unreachable by the GC. Then, the GC attempted to free all those sockets by eliminating their mutual references. If we manage to keep a reference to one of the sockets that the GC thought was going away, the GC detects that with the BUG\_ON().


But we don't actually need the victim SKB to reference a socket that the GC thinks is going away; in scan\_inflight(), the GC targets any SKB with a socket that is marked UNIX\_GC\_CANDIDATE, meaning it just had to be a candidate for being scanned by the GC. So by making the victim SKB hold a reference to a socket that is not directly referenced from a file descriptor table, but is indirectly referenced by a file descriptor table through another socket, we can ensure that the BUG\_ON() won't trigger.


I extended [my reproducer](https://bugs.chromium.org/p/project-zero/issues/detail?id=2247#c6) with this trick and some userfaultfd trickery to make recv() run with the right timing. Nowadays you don't necessarily get full access to userfaultfd as a normal user, but since I'm just trying to show the concept, and there are alternatives to userfaultfd (using FUSE or just slow disk access), that's good enough for this blogpost.


When a normal distro kernel is running normally, the UAF reproducer's UAF accesses won't actually be noticeable; but if you add the kernel command line flag slub\_debug=FP (to enable SLUB's poisoning and sanity checks), the reproducer quickly crashes twice, first with a poison dereference and then a poison overwrite detection, showing that one byte of the poison was incremented:


general protection fault, probably for non-canonical address 0x6b6b6b6b6b6b6b6b: 0000 \[#1\] SMP NOPTI

CPU: 1 PID: 2655 Comm: hardirq\_loop Not tainted 5.10.0-9-amd64 #1 Debian 5.10.70-1

\[...\]

RIP: 0010:unix\_stream\_read\_generic+0x72b/0x870

Code: fe ff ff 31 ff e8 85 87 91 ff e9 a5 fe ff ff 45 01 77 44 8b 83 80 01 00 00 85 c0 0f 89 10 01 00 00 49 8b 47 38 48 85 c0 74 23 \<0f> bf 00 66 85 c0 0f 85 20 01 00 00 4c 89 fe 48 8d 7c 24 58 44 89

RSP: 0018:ffffb789027f7cf0 EFLAGS: 00010202

RAX: 6b6b6b6b6b6b6b6b RBX: ffff982d1d897b40 RCX: 0000000000000000

RDX: 6a0fe1820359dce8 RSI: ffffffffa81f9ba0 RDI: 0000000000000246

RBP: ffff982d1d897ea8 R08: 0000000000000000 R09: 0000000000000000

R10: 0000000000000000 R11: ffff982d2645c900 R12: ffffb789027f7dd0

R13: ffff982d1d897c10 R14: 0000000000000001 R15: ffff982d3390e000

FS: 00007f547209d740(0000) GS:ffff98309fa40000(0000) knlGS:0000000000000000

CS: 0010 DS: 0000 ES: 0000 CR0: 0000000080050033

CR2: 00007f54722cd000 CR3: 00000001b61f4002 CR4: 0000000000770ee0

PKRU: 55555554

Call Trace:

\[...\]

unix\_stream\_recvmsg+0x53/0x70

\[...\]

\_\_sys\_recvfrom+0x166/0x180

\[...\]

\_\_x64\_sys\_recvfrom+0x25/0x30

do\_syscall\_64+0x33/0x80

entry\_SYSCALL\_64\_after\_hwframe+0x44/0xa9

\[...\]

---\[ end trace 39a81eb3a52e239c \]---

=============================================================================

BUG skbuff\_head\_cache (Tainted: G D ): Poison overwritten

-----------------------------------------------------------------------------


INFO: 0x00000000d7142451-0x00000000d7142451 @offset=68. First byte 0x6c instead of 0x6b

INFO: Slab 0x000000002f95c13c objects=32 used=32 fp=0x0000000000000000 flags=0x17ffffc0010200

INFO: Object 0x00000000ef9c59c8 @offset=0 fp=0x00000000100a3918


Object 00000000ef9c59c8: 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b kkkkkkkkkkkkkkkk

Object 0000000097454be8: 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b kkkkkkkkkkkkkkkk

Object 0000000035f1d791: 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b kkkkkkkkkkkkkkkk

Object 00000000af71b907: 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b kkkkkkkkkkkkkkkk

Object 000000000d2d371e: 6b 6b 6b 6b 6c 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b kkkklkkkkkkkkkkk

Object 0000000000744b35: 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b kkkkkkkkkkkkkkkk

Object 00000000794f2935: 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b kkkkkkkkkkkkkkkk

Object 000000006dc06746: 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b kkkkkkkkkkkkkkkk

Object 000000005fb18682: 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b kkkkkkkkkkkkkkkk

Object 0000000072eb8dd2: 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b kkkkkkkkkkkkkkkk

Object 00000000b5b572a9: 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b kkkkkkkkkkkkkkkk

Object 0000000085d6850b: 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b kkkkkkkkkkkkkkkk

Object 000000006346150b: 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b kkkkkkkkkkkkkkkk

Object 000000000ddd1ced: 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b 6b a5 kkkkkkkkkkkkkkk.

Padding 00000000e00889a7: 5a 5a 5a 5a 5a 5a 5a 5a 5a 5a 5a 5a 5a 5a 5a 5a ZZZZZZZZZZZZZZZZ

Padding 00000000d190015f: 5a 5a 5a 5a 5a 5a 5a 5a ZZZZZZZZ

CPU: 7 PID: 1641 Comm: gnome-shell Tainted: G B D 5.10.0-9-amd64 #1 Debian 5.10.70-1

\[...\]

Call Trace:

dump\_stack+0x6b/0x83

check\_bytes\_and\_report.cold+0x79/0x9a

check\_object+0x217/0x260

\[...\]

alloc\_debug\_processing+0xd5/0x130

\_\_\_slab\_alloc+0x511/0x570

\[...\]

\_\_slab\_alloc+0x1c/0x30

kmem\_cache\_alloc\_node+0x1f3/0x210

\_\_alloc\_skb+0x46/0x1f0

alloc\_skb\_with\_frags+0x4d/0x1b0

sock\_alloc\_send\_pskb+0x1f3/0x220

\[...\]

unix\_stream\_sendmsg+0x268/0x4d0

sock\_sendmsg+0x5e/0x60

\_\_\_\_sys\_sendmsg+0x22e/0x270

\[...\]

\_\_\_sys\_sendmsg+0x75/0xb0

\[...\]

\_\_sys\_sendmsg+0x59/0xa0

do\_syscall\_64+0x33/0x80

entry\_SYSCALL\_64\_after\_hwframe+0x44/0xa9

\[...\]

FIX skbuff\_head\_cache: Restoring 0x00000000d7142451-0x00000000d7142451=0x6b


FIX skbuff\_head\_cache: Marking all objects used

RIP: 0010:unix\_stream\_read\_generic+0x72b/0x870

Code: fe ff ff 31 ff e8 85 87 91 ff e9 a5 fe ff ff 45 01 77 44 8b 83 80 01 00 00 85 c0 0f 89 10 01 00 00 49 8b 47 38 48 85 c0 74 23 \<0f> bf 00 66 85 c0 0f 85 20 01 00 00 4c 89 fe 48 8d 7c 24 58 44 89

RSP: 0018:ffffb789027f7cf0 EFLAGS: 00010202

RAX: 6b6b6b6b6b6b6b6b RBX: ffff982d1d897b40 RCX: 0000000000000000

RDX: 6a0fe1820359dce8 RSI: ffffffffa81f9ba0 RDI: 0000000000000246

RBP: ffff982d1d897ea8 R08: 0000000000000000 R09: 0000000000000000

R10: 0000000000000000 R11: ffff982d2645c900 R12: ffffb789027f7dd0

R13: ffff982d1d897c10 R14: 0000000000000001 R15: ffff982d3390e000

FS: 00007f547209d740(0000) GS:ffff98309fa40000(0000) knlGS:0000000000000000

CS: 0010 DS: 0000 ES: 0000 CR0: 0000000080050033

CR2: 00007f54722cd000 CR3: 00000001b61f4002 CR4: 0000000000770ee0

PKRU: 55555554

# Conclusion(s)

Hitting a race can become easier if, instead of racing two threads against each other, you race one thread against a hardware timer to create a gigantic timing window for the other thread. Hence the title! On the other hand, it introduces extra complexity because now you have to think about how timers actually work, and turns out, time is a complicated concept...


This shows how at least some really tight races can still be hit and we should treat them as security bugs, even if it seems like they'd be very hard to hit at first glance.


Also, precisely timing races is hard, and the details of how long it actually takes the CPU to get from one point to another are mysterious. (As not only exploit writers know, but also anyone who's ever wanted to benchmark a performance-relevant change...)

# Appendix: How impatient are interrupts?

I did also play around with this stuff on arm64 a bit, and I was wondering: At what points do interrupts actually get delivered? Does an incoming interrupt force the CPU to drop everything immediately, or do inflight operations finish first? This gets particularly interesting on phones that contain two or three different types of CPUs mixed together.


On a Pixel 4 (which has 4 slow in-order cores, 3 fast cores, and 1 faster core), I tried firing an interval timer at 100Hz (using timer\_create()), with a signal handler that logs the PC register, while running this loop:


400680: 91000442 add x2, x2, #0x1

400684: 91000421 add x1, x1, #0x1

400688: 9ac20820 udiv x0, x1, x2

40068c: 91006800 add x0, x0, #0x1a

400690: 91000400 add x0, x0, #0x1

400694: 91000442 add x2, x2, #0x1

400698: 91000421 add x1, x1, #0x1

40069c: 91000442 add x2, x2, #0x1

4006a0: 91000421 add x1, x1, #0x1

4006a4: 9ac20820 udiv x0, x1, x2

4006a8: 91006800 add x0, x0, #0x1a

4006ac: 91000400 add x0, x0, #0x1

4006b0: 91000442 add x2, x2, #0x1

4006b4: 91000421 add x1, x1, #0x1

4006b8: 91000442 add x2, x2, #0x1

4006bc: 91000421 add x1, x1, #0x1

4006c0: 17fffff0 b 400680 \<main+0xe0>


The logged interrupt PCs had the following distribution on a slow in-order core:

and this distribution on a fast out-of-order core:

As always, out-of-order (OOO) cores make everything weird, and the start of the loop seems to somehow "provide cover" for the following instructions; but on the in-order core, we can see that more interrupts arrive after the slow udiv instructions. So apparently, when one of those is executing while an interrupt arrives, it continues executing and doesn't get aborted somehow?


With the following loop, which has a LDR instruction mixed in that accesses a memory location that is constantly being modified by another thread:


4006a0: 91000442 add x2, x2, #0x1

4006a4: 91000421 add x1, x1, #0x1

4006a8: 9ac20820 udiv x0, x1, x2

4006ac: 91006800 add x0, x0, #0x1a

4006b0: 91000400 add x0, x0, #0x1

4006b4: 91000442 add x2, x2, #0x1

4006b8: 91000421 add x1, x1, #0x1

4006bc: 91000442 add x2, x2, #0x1

4006c0: 91000421 add x1, x1, #0x1

4006c4: 9ac20820 udiv x0, x1, x2

4006c8: 91006800 add x0, x0, #0x1a

4006cc: 91000400 add x0, x0, #0x1

4006d0: 91000442 add x2, x2, #0x1

4006d4: f9400061 ldr x1, \[x3\]

4006d8: 91000421 add x1, x1, #0x1

4006dc: 91000442 add x2, x2, #0x1

4006e0: 91000421 add x1, x1, #0x1

4006e4: 17ffffef b 4006a0 \<main+0x100>


the cache-missing loads obviously have a large influence on the timing. On the in-order core:

On the OOO core:


What is interesting to me here is that the timer interrupts seem to again arrive after the slow load - implying that if an interrupt arrives while a slow memory access is in progress, the interrupt handler may not get to execute until the memory access has finished? (Unless maybe on the OOO core the interrupt handler can start speculating already? I wouldn't really expect that, but could imagine it.)


On an X86 Skylake CPU, we can do a similar test:


11b8: 48 83 c3 01 add $0x1,%rbx

11bc: 48 83 c0 01 add $0x1,%rax

11c0: 48 01 d8 add %rbx,%rax

11c3: 48 83 c3 01 add $0x1,%rbx

11c7: 48 83 c0 01 add $0x1,%rax

11cb: 48 01 d8 add %rbx,%rax

11ce: 48 03 02 add (%rdx),%rax

11d1: 48 83 c0 01 add $0x1,%rax

11d5: 48 83 c3 01 add $0x1,%rbx

11d9: 48 01 d8 add %rbx,%rax

11dc: 48 83 c3 01 add $0x1,%rbx

11e0: 48 83 c0 01 add $0x1,%rax

11e4: 48 01 d8 add %rbx,%rax

11e7: eb cf jmp 11b8 \<main+0xf8>


with a similar result:

This means that if the first access to the file terminated our race window (which is not the case), we probably wouldn't be able to win the race by making the access to the file slow - instead we'd have to slow down one of the operations before that. (But note that I have only tested simple loads, not stores or read-modify-write operations here.)
