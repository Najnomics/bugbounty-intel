# Taming the wild copy: Parallel Thread Corruption - Project Zero

Source: https://projectzero.google/2015/03/taming-wild-copy-parallel-thread.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Chris Evans, Winner of the occasional race


Back in 2002, a [very interesting vulnerability](http://httpd.apache.org/info/security_bulletin_20020620.txt) was found and fixed in the Apache web server. Relating to a bug in chunked encoding handing, the vulnerability caused a memcpy() call with a negative length with the destination on the stack. Of course, many parties were quick to proclaim the vulnerability unexploitable beyond a denial of service. After all, a negative length to memcpy() represents a huge copy which is surely guaranteed to hit an unmapped page and terminate the process. So it was a surprise when a working remote code execution exploit turned up for FreeBSD and other BSD variants, due to a quirk in their memcpy() implementations! [This GIAC paper](http://www.giac.org/paper/gcih/361/port-80-apache-http-daemon-exploit/103818) archives both the exploit as well as an analysis (appendix D) of how it works.


For the purposes of this post, we define “wild copy” as a copy where both:

- The attacker has limited control over the length of the copy.
- The copy will always end up being so large as to be guaranteed to hit an unmapped page.


There have been plenty of other interesting cases where a wild copy has ended up being exploitable:

- A general attack against corruption of structured exception handlers (SEH) on Windows.
- The BSD variants don’t have a monopoly on memcpy() quirks. In 2011, there was[a fascinating outright eglibc vulnerability](http://sebug.net/paper/Exploits-Archives/2012-exploits/1208-exploits/eglibc-exec.txt) in Ubuntu, triggering for any very large length to memcpy(). A [memset() variant](https://code.google.com/p/chromium/issues/detail?id=91665) was exposed via the Chromium Vulnerability Rewards Program.
- The Java Runtime Environment has a very complicated crash handler installed, which is called when a[wild copy inevitably causes an access violation](http://scary.beasts.org/security/CESA-2006-004.html). If the crash handler is not careful to be robust in the presence of arbitrarily corrupted heap state, it might crash itself in a more controlled and exploitable way.


All of the above cases have one thing in common: the wild copy becomes exploitable due to a secondary issue or quirk.


Is it possible to exploit a wild copy without relying on a secondary issue? This is an interesting question for Project Zero to tackle -- when we explore exploitation, we usually only do so for cases where we think we can learn new insights or advance the public state of the art. Today, we’re going to explore a wild copy exploit in the Flash plug-in for 64-bit Chrome Linux.


It’s time to introduce [issue 122](https://code.google.com/p/google-security-research/issues/detail?id=122) and “parallel thread corruption”. Issue 122 is an Adobe Flash vulnerability that was [fixed back in November 2014](https://helpx.adobe.com/security/products/flash-player/apsb14-24.html). It’s a curious bug wherein the G711 sound codec is straight up broken on some platforms, always resulting in a wild copy when the codec tries to decode some samples. When triggered, it causes a memmove() on the heap with a small negative value as the length parameter. On modern Linux, the memmove() implementation appears to be solid, and the inexorable SIGSEGV appears to take the process down cleanly. We have our work cut out!


Step 1: choose an approach


We’re going to attempt a “parallel thread corruption”, which is where we observe and abuse the side effects in thread A of an asynchronous memory corruption in thread B. Since thread B’s corruption will always end in a crash, we need to run both threads in parallel. We also need to win a tricky race condition: get code execution before thread B’s crash takes out thread A.

As is common in Flash exploits, we’re going to attempt to have our memory corruption corrupt the header of a Vector.\<uint> buffer object, expanding its length beyond reality thus leading to the ability to read and write out of bounds. Vector.\<uint> buffer objects have their data allocated inline after the header, and in the case of this specific vulnerability, the errant memmove() always ends up shifting memory content backwards by 2048 bytes. So if we allocate a large enough Vector.\<uint>, we can attempt to corrupt its header with its own data:


| len: 2000 | some ptr | data\[0\] = 0, data\[1\] = 0, …, data\[508\] = 0xfee1dead, … |

^                                                          |

|-----------------------------------------------------------


The offsets and alignments work out such that the 508th 4-byte uint data element will clobber the length in the header.


Step 2: wrestle the Flash heap into submission


Before we get too carried away, we need to remember that the corruption thread is going to be in the middle of a wild memmove(). Even my laptop can copy memory at a rate of almost 10 gigabytes per second, so we’re going to need to land the copy on to a large runway of heap so that we have enough time to complete the exploit before the copy hits an unmapped page. Getting a large, contiguous heap mapping sounds easy but it is not. If you naively just spray the Flash heap with 512KB ByteArray buffers, you’ll see a large number of process mappings looking like this:


7fd138039000-7fd138679000 rw-p 00000000 00:00 0

7fd138679000-7fd139039000 ---p 00000000 00:00 0

7fd139039000-7fd139fb9000 rw-p 00000000 00:00 0

7fd139fb9000-7fd13a039000 ---p 00000000 00:00 0

7fd13a039000-7fd13ae79000 rw-p 00000000 00:00 0

7fd13ae79000-7fd13b039000 ---p 00000000 00:00 0

\[...\]


At first glance, as security professionals, we might proclaim “great! guard pages!” but what we are looking at here is an accidental inefficiency of the Flash heap. When trying to extend the limit of the heap forwards and failing due to another mapping being in the way, it lets the operating system decide where to put a new mapping. The default Linux heuristic happens to be “just before the last successful mapping”, so the Flash heap will enter a permanent cycle of failing to extend the heap forwards. The “guard pages” come from the fact that the Flash heap (on 64-bit) will reserve address space in 16MB chunks, and commit regions of that as needed, and with granularity of 128KB. It’s quite common for the series of commit requests to not add up exactly to 16MB, leaving a hole in the address space. Such a hole will cause a crash before our exploit is done!


To avoid all this and try and obtain a heap that grows forward, we follow the following heuristic:

1. Allocate a 1GB object, which will be placed just before the current heap region.
2. Spray 4KB allocations (the Flash heap block size) to fill in existing free blocks.
3. Spray some more 4KB allocations to cause the heap to extend backwards, into a new 16MB region allocated before the 1GB object.
4. Free the 1GB object.


If all has gone well, the heap will look something like this, with green representing the space available for uninterrupted linear growth forward:


| committed: 1MB | reserved: 15MB     |         1GB hole         | committed: \~16MB | ...


Step 3: use heap grooming to align our exploitation objects


We’re now in good shape to use heap grooming to set up a row of important object allocations in a line, like this:


| 8KB buf | 8KB buf | 8KB buf | Vec.\<uint>(2000) | Vec.\<Object>(1000) | 100MB of bufs |

.----- wild copy -------------------------------------------------->


In red is the vector we decided to corrupt in step 1, and in green is an object we will deliberately free now that the heap is set up. Before we proceed, there’s one more heap quirk that we need to beware of: as the heap is extended, inline heap metadata is also extended to describe all the new 4KB blocks. This process of extending in-heap metadata creates free regions of blocks inside the heap. This wouldn’t be an issue, but for another quirk: when a block range is returned to the heap free list, it isn’t reallocated in MRU (most recently used) order. Therefore, we mount another heap spray to make sure all 8KB (2 block) heap chunks are allocated, leaving that particular freelist empty. We then free the middle 8KB buffer (in green above) to leave a heap free chunk in a useful place. Since we leave two allocated 8KB buffers either side, the freed chunk will not be coalesced and will be the chosen option for the next 8KB allocation.


After all that heap manipulation, we leave ourselves with a range of important objects lined up in a neat row, and with a preceding and free 8KB heap chunk primed to be re-used at the next opportunity.


Step 4: light the fuse


It’s worth noting that there are platform specific differences in how the sound subsystem initializes. On some platforms, the subsystem initializes and starts asynchronously when play() is called for the first time. For the Chrome Flash plug-in, this is not the case. If you look at the exploit, you’ll see that we have to kick off the subsystem by playing a different sound and then returning to the main event loop. This dance ensures that the second call to play() actually does kick off the wild copy asynchronously.


With our heap in nice shape, we trigger the wild memmove() by playing the G711 sound. The wild copy will start immediately and proceed asynchronously so we need to get a move on! The G711 sound decoder object is about 4424 bytes in size, but the heap allocation granularity for sizes >= 4096 is 4096. So, the object will be placed in an 8192-sized chunk -- specifically the one we just freed up if all is well. The wild heap corruption will start within this object and proceed forwards, very quickly corrupting all the following objects that we lined up, including the Vector.\<uint> and Vector.\<Object>.


The moment we’ve pulled the trigger, we spin in a tight ActionScript loop that waits for the length of our Vector.\<uint> to change from 2000 to 0xfee1dead.


Step 5: defeat ASLR


The moment we detect the corrupted Vector.\<uint>, we are in business: we can read and write arbitrary 4-byte values off-the-end of the object. As per the heap grooming in step 3, the object directly off the end is the buffer for a Vector.\<Object>, which is ideal for us because it contains two important things for us to read:


- A vtable value into the Flash library, which gives us the location of the code.
- A pointer to itself, which is very important because it allows us to turn a relative read/write into an absolute read/write.


Step 6: ROP-free code execution


The exploit proceeds not via a ROP chain, but by rewiring some function pointers in the GOT / PLT machinery. (Note that this relies on RELRO not being present, which it rarely is on common Linux variants and binaries. If RELRO were present, we’d likely simply target vtable pointer rewiring instead.) We have the address of a vtable, and from this, the GOT / PLT function pointers we want are a fixed offset away. There is quite an elegant and simple sequence to get us code execution:


- Read the function pointer for memmove(), which we know is resolved.
- Calculate the address of \_\_libc\_system, which is a fixed offset from \_\_memmove\_ssse3\_back which we just read.
- Write the address of \_\_libc\_system to the function pointer for munmap().


The effect of this wiring is that when the program next calls munmap(buffer), it will actually be calling system(buffer). This is a useful primitive because large ByteArray buffers are backed by mmap() / munmap(), and we can control the exact content of the buffer and when it is freed. So we can pass any string we want to system() at will.


Step 7: continuation of execution and sandbox


To illustrate the level of control we now have over the process, our payload to system() is “killall -STOP chrome; gnome-calculator -e 31337”. This has two effects:


- Displays the obligatory calculator to prove we have arbitrary code execution.
- Sends a STOP signal to the existing Chrome processes. This will have the effect of stopping the wild memmove() before it has a chance to crash.


As a fun data point, if we attach to the stopped process and look at the wild copy thread, it has managed to copy 50MB(!) of data, even though we tried to make our exploit as fast and simple as possible.


At this point, a real exploit that didn’t wish to leave any traces could easily attach to the thread in the middle of the copy and stop the copy without having to kill the thread. Furthermore, the memory corrupted in the process of exploitation could be easily restored.


Of course, the sandbox escape is left as an exercise to the user. The system() library call won’t work at all in the Chrome sandbox; when demonstrating the exploit, we’re using the --no-sandbox flag to focus purely on the remote code execution aspect. An exploit inside the sandbox would instead likely rewire function pointers to attack the IPC channels with bad messages, or deploy a ROP chain after all to attack the kernel.


Closing notes


As always, Project Zero recommends that all memory corruptions are initially assumed to be exploitable. As we showed before in our posts on the [Pwn4Fun Safari exploit](/2014/07/pwn4fun-spring-2014-safari-part-i_24.html), the [glibc off-by-one NUL byte corruption](/2014/08/the-poisoned-nul-byte-2014-edition.html) and the [Flash regex exploit](/2015/02/exploitingscve-2015-0318sinsflash.html), situations that initially look dire for exploitation can sometimes be turned around with a trick or two.

Wild copies have a long history of being declared unexploitable, but based on our findings here, we think it likely that most wild copies in complicated multi-threaded software (browsers, browser plug-ins) are likely to be exploitable using the parallel thread corruption method. We publish this finding to encourage developers and vendors to triage wild copies as more serious than previously believed.
