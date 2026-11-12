# How to unc0ver a 0-day in 4 hours or less - Project Zero

Source: https://projectzero.google/2020/07/how-to-unc0ver-0-day-in-4-hours-or-less.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

By Brandon Azad, Project Zero


At 3 PM PDT on May 23, 2020, the unc0ver jailbreak was [released](https://github.com/pwn20wndstuff/Undecimus/releases/tag/v5.0.0) for iOS 13.5 (the latest signed version at the time of release) using a zero-day vulnerability and heavy obfuscation. By 7 PM, I had identified the vulnerability and informed Apple. By 1 AM, I had sent Apple a POC and my analysis. This post takes you along that journey.

# Initial identification

I wanted to find the vulnerability used in unc0ver and report it to Apple quickly in order to demonstrate that obfuscating an exploit does little to prevent the bug from winding up in the hands of bad actors.


After downloading and extracting the unc0ver IPA, I loaded the main executable into IDA to take a look. Unfortunately, the binary was heavily obfuscated, so finding the bug statically was beyond my abilities.

[Next I loaded the unc0ver app onto an iPod Touch 7 running iOS 13.2.3 to try running the exploit. Exploring the app interface didn't suggest that the user had any sort of control over which vulnerability was used to exploit the device, so I hoped that unc0ver only had support for the one 0-day and did not use the](/images/oldblog/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9mCs_s2048_image1%281%29.png)

[oob\_timestamp](https://bugs.chromium.org/p/project-zero/issues/detail?id=1986)bug instead on iOS 13.3 and lower.


As I was clicking the "Jailbreak" button, a thought occurred to me: Having written a few kernel exploits before, I understood that most memory-corruption-based exploits have something of a "critical section" during which kernel state has been corrupted and the system would be unstable if the rest of the exploit did not continue. So, on a whim, I double clicked the home button to bring up the app switcher and killed the unc0ver app.


The device immediately panicked.


panic(cpu 1 caller 0xfffffff020e75424): "Zone cache element was used after free! Element 0xffffffe0033ac810 was corrupted at beginning; Expected 0x87be6c0681be12b8 but found 0xffffffe003059d90; canary 0x784193e68284daa8; zone 0xfffffff021415fa8 (kalloc.16)"

Debugger message: panic

Memory ID: 0x6

OS version: 17B111

Kernel version: Darwin Kernel Version 19.0.0: Wed Oct  9 22:41:51 PDT 2019; root:xnu-6153.42.1\~1/RELEASE\_ARM64\_T8010

KernelCache UUID: 5AD647C26EF3506257696CF29419F868

Kernel UUID: F6AED585-86A0-3BEE-83B9-C5B36769EB13

iBoot version: iBoot-5540.40.51

secure boot?: YES

Paniclog version: 13

Kernel slide:     0x0000000019cf0000

Kernel text base: 0xfffffff020cf4000

mach\_absolute\_time: 0x3943f534b

Epoch Time:        sec       usec

Boot    : 0x5ec9b036 0x0004cf8d

Sleep   : 0x00000000 0x00000000

Wake    : 0x00000000 0x00000000

Calendar: 0x5ec9b138 0x0004b68b


Panicked task 0xffffffe0008a4800: 9619 pages, 230 threads: pid 222: unc0ver

Panicked thread: 0xffffffe004303a18, backtrace: 0xffffffe00021b2f0, tid: 4884

lr: 0xfffffff007135e70  fp: 0xffffffe00021b330

lr: 0xfffffff007135cd0  fp: 0xffffffe00021b3a0

lr: 0xfffffff0072345c0  fp: 0xffffffe00021b450

lr: 0xfffffff0070f9610  fp: 0xffffffe00021b460

lr: 0xfffffff007135648  fp: 0xffffffe00021b7d0

lr: 0xfffffff007135990  fp: 0xffffffe00021b820

lr: 0xfffffff0076e1ad4  fp: 0xffffffe00021b840

lr: 0xfffffff007185424  fp: 0xffffffe00021b8b0

lr: 0xfffffff007182550  fp: 0xffffffe00021b9e0

lr: 0xfffffff007140718  fp: 0xffffffe00021ba30

lr: 0xfffffff0074d5bfc  fp: 0xffffffe00021ba80

lr: 0xfffffff0074d5d90  fp: 0xffffffe00021bb40

lr: 0xfffffff0075f10d0  fp: 0xffffffe00021bbd0

lr: 0xfffffff00723468c  fp: 0xffffffe00021bc80

lr: 0xfffffff0070f9610  fp: 0xffffffe00021bc90

lr: 0x00000001bf085ae4  fp: 0x0000000000000000


This seemed promising! I had a panic message saying there was a use-after-free in the kalloc.16 allocation zone (general purpose allocations of size up to 16 bytes). However, it was possible that this was a symptom of the memory corruption rather than the source of the memory corruption (or even a decoy!). To investigate further, I'd need to analyze the backtrace.


While waiting for IDA to process the iPod's kernelcache, I tried a few more off-the-cuff experiments. Since many exploits use Mach ports as a fundamental primitive, I wrote an app that would churn up the ipc.ports zone, creating fragmentation and mixing up the freelist. When I ran the unc0ver app afterwards the exploit still worked, suggesting that it may not rely on heap grooming of Mach port allocations.


Next, since the panic log mentioned kalloc.16, I decided to write an app that would continuously allocate and free to kalloc.16 in the background during the unc0ver exploit. The idea was that if unc0ver relies on reallocating a kalloc.16 allocation, then my app might grab that slot instead, which would likely cause the exploit strategy to fail and possibly result in a kernel panic. And sure enough, with my app hammering kalloc.16 in the background,  touching the "Jailbreak" button caused an immediate kernel panic.


As a sanity check, I tried changing my app to hammer a different zone, kalloc.32, instead of kalloc.16. This time the exploit ran successfully, suggesting that kalloc.16 is indeed the critical allocation zone used by the exploit.


Finally, once IDA had finished analyzing the iPod kernelcache, I started symbolicating the stacktraces collected from the panic logs.


Panicked task 0xffffffe0008a4800: 9619 pages, 230 threads: pid 222: unc0ver

Panicked thread: 0xffffffe004303a18, backtrace: 0xffffffe00021b2f0, tid: 4884

lr: 0xfffffff007135e70

lr: 0xfffffff007135cd0

lr: 0xfffffff0072345c0

lr: 0xfffffff0070f9610

lr: 0xfffffff007135648

lr: 0xfffffff007135990

lr: 0xfffffff0076e1ad4  # \_panic

lr: 0xfffffff007185424  # \_zcache\_alloc\_from\_cpu\_cache

lr: 0xfffffff007182550  # \_zalloc\_internal

lr: 0xfffffff007140718  # \_kalloc\_canblock

lr: 0xfffffff0074d5bfc  # \_aio\_copy\_in\_list

lr: 0xfffffff0074d5d90  # \_lio\_listio

lr: 0xfffffff0075f10d0  # \_unix\_syscall

lr: 0xfffffff00723468c  # \_sleh\_synchronous

lr: 0xfffffff0070f9610  # \_fleh\_synchronous

lr: 0x00000001bf085ae4


The call to lio\_listio() immediately stood out to me. Not long before I had finished writing [a survey of recent iOS kernel exploits](/2020/06/a-survey-of-recent-ios-kernel-exploits.html), and I happened to remember that lio\_listio() was the vulnerable syscall used in the [LightSpeed](https://www.synacktiv.com/posts/exploit/lightspeed-a-race-for-an-iosmacos-sandbox-escape.html)-based exploits. I reread the blog post from Synacktiv to get a sense of the bug and immediately another piece fell into place: the target object that is double-freed in the LightSpeed race is an aio\_lio\_context object that lives in kalloc.16. Also, the large number of threads in the unc0ver app further supported the idea of a race condition.


At this point I felt I had enough evidence to reach out to Apple with a preliminary analysis suggesting that the bug was LightSpeed, either a variant or a regression.

# Confirmation and POC

Next I wanted to confirm the bug by writing a POC to trigger the issue. I tried the [original POC](https://github.com/Synacktiv-contrib/lightspeed/blob/master/lightspeed.c) shown in the LightSpeed blog post, but after a minute of running it hadn't yet panicked. This suggested to me that perhaps the 0-day was a variant of the original LightSpeed bug.


To find out more, I started two lines of investigation: looking at the [XNU sources](https://opensource.apple.com/source/xnu/xnu-6153.81.5/bsd/kern/kern_aio.c.auto.html) to try and spot the bug, and using [checkra1n](https://checkra.in/)/[pongoOS](https://github.com/checkra1n/pongoOS) to patch lio\_listio() in the kernelcache and then running the exploit. From the sources I couldn't see how the original vulnerability was fixed at all, which didn't make sense to me. So instead I focused my effort on kernel patching.


Booting a patched kernelcache is tricky but doable because of [checkm8](https://twitter.com/axi0mX/status/1177542201670168576). I downloaded checkra1n and booted the iPod into the pongoOS shell. Using the example from the pongoOS repo as a guide, I created a loadable pongo module that would disable the checkra1n kernel patches and instead apply my own patches. (I disabled the checkra1n kernel patches because I was worried that unc0ver would detect checkra1n and engage anti-analysis measures.)


My first test was just to insert invalid instruction opcodes into the lio\_listio() function so that it would panic if called. Surprisingly, the device booted just fine, and then once I clicked "Jailbreak" it panicked. This meant that unc0ver was the only process calling lio\_listio().


I next patched the code responsible for allocating the aio\_lio\_context object that is double-freed in the original LightSpeed bug so that it would be allocated from kalloc.48 instead of kalloc.16:


FFFFFFF0074D5D54     MOV     W8, #0xC ; patched to #0x23

FFFFFFF0074D5D58     STR     X8, \[SP,#0x40\] ; alloc size

FFFFFFF0074D5D5C     ADRL    X2, \_lio\_listio.site.5

FFFFFFF0074D5D64     ADD     X0, SP, #0x40

FFFFFFF0074D5D68     MOV     W1, #1 ; can block

FFFFFFF0074D5D6C     BL      kalloc\_canblock

FFFFFFF0074D5D70     CBZ     X0, loc\_FFFFFFF0074D6234

FFFFFFF0074D5D74     MOV     X19, X0 ; lio\_context

FFFFFFF0074D5D78     MOV     W1, #0xC ; size\_t

FFFFFFF0074D5D7C     BL      \_bzero


The idea is that increasing the object's allocation size will cause unc0ver's exploit strategy to fail because it will try to replace the accidentally-freed kalloc.48 context object with a replacement object from kalloc.16, which simply cannot occur. And sure enough, with this patch in place, unc0ver stalled at the "Exploiting kernel" step without actually panicking.


I then ran a few more experiments patching various points in the function to dump the arguments and data buffers passed to lio\_listio() so that I could compare against the values used in the original LightSpeed POC. The idea was that if I noticed any substantial differences, that would point me in the direction of the variant in the source. However, other than the field aio\_reqprio being set to 'gang', there were no differences between the arguments passed to lio\_listio() by unc0ver and those in the original POC.


At this point it looked like the 0-day might actually be the original LightSpeed bug itself, not a variant, so I returned to the original POC to see if perhaps the reason it wasn't triggering was that a specific technique used had been mitigated. The code responsible for reallocating the kalloc.16 allocation caught my eye:


/\* not mandatory but used to make the race more likely \*/

/\* this poll() will force a kalloc16 of a struct poll\_continue\_args \*/

/\* with its second dword as 0 (to collide with lio\_context->io\_issued == 0) \*/

/\* this technique is quite slow (1ms waiting time) and better ways to do so exists \*/

int n = poll(NULL, 0, 1);


I hadn't ever seen poll() used as a reallocation primitive before. Intuitively it felt like using Mach port based reallocation strategies was more promising, so I replaced this code with an out-of-line Mach ports spray copied from oob\_timestamp. Sure enough, that was the only change required to make the POC trigger reliably in a few seconds.

# Patch history

After I had a working POC, I retried the original LightSpeed POC and found that it would eventually panic if left to run for long enough. Thus, this is [another](https://bugs.chromium.org/p/project-zero/issues/detail?id=1806#c14) case of a reintroduced bug that could have been identified by simple regression tests.


So, let's return to the sources to see if we can figure out what happened. As mentioned earlier, when I first checked the XNU sources to see how the lio\_listio() patch might have been broken, I actually couldn't identify how the bug was originally patched at all. In retrospect, this isn't all that far off.


The original [LightSpeed blog post](https://www.synacktiv.com/posts/exploit/lightspeed-a-race-for-an-iosmacos-sandbox-escape.html) describes the vulnerability very well, so I won't rehash it all here; I highly recommend reading that post. From a high level, the bug is that the semantics of which function frees the aio\_lio\_context object are unclear, as both the worker threads that perform the asynchronous I/O and the lio\_listio() function itself could do it.


As mentioned in the post, the original fix for this bug was just to not free the aio\_lio\_context object in the cases in which it might be double-freed:


On the one hand, this patch fixes the potential UaF on the lio\_context. But on the other hand, the error case that was handled before the fix is now ignored... As a result it is possible to make lio\_listio() allocate an aio\_lio\_context that will never be freed by the kernel. This gives us a silly DoS that will also crash the recent kernels (iOS 12 included).

\[...\]

For the rest, we will see in the future if Apple bothers to fix the little DoS they introduced with the patch :D


It turns out that Apple did eventually decide to fix the memory leak in iOS 13... but in doing so it appears they reintroduced the race condition double-free:


case LIO\_NOWAIT:

\+       /\* If no IOs were issued must free it (rdar://problem/45717887) \*/

\+       if (lio\_context->io\_issued == 0) {

\+           free\_context = TRUE;

\+       }

break;


The code in iOS 13 isn't exactly the same as iOS 11, but it's semantically equivalent. Anyone who had remembered and understood the original LightSpeed bug could have easily identified this as a regression by reviewing XNU source diffs. And anyone who ran relatively simple regression tests would have found this issue trivially.


So, to summarize: the LightSpeed bug was fixed in iOS 12 with a patch that didn't address the root cause and instead just turned the race condition double-free into a memory leak. Then, in iOS 13, this memory leak was identified as a bug and "fixed" by reintroducing the original bug, again without addressing the root cause of the issue. And this security regression could have been found trivially by running the original POC from the blog post.


# Conclusion

The combination of the SockPuppet regression in iOS 12.4 and the LightSpeed regression in iOS 13 strongly suggests that Apple did not run effective regression tests on at least these old security bugs (and these were very public bugs that got a lot of attention). Running effective regression tests is a necessity for basic software testing, and a common starting point for exploitation.


Still, I'm very happy that Apple patched this issue in a timely manner once the exploit became public. The reality here is that attackers figure out these issues very quickly, long before the public POC is released. Thus the window of opportunity to exploit regressions is substantial.

Also, my goal in trying to identify the bug used by unc0ver was to demonstrate that obfuscation does not block attackers from quickly weaponizing the exploited vulnerability. It turned out that I was lucky in my analysis: my experience writing kernel exploits let me quickly figure out an alternative strategy to find the bug, and I happened to already be familiar with the specific vulnerability used because I've been keeping track of past exploits. But anyone in the business of using exploits against Apple users would also have these same advantages.
