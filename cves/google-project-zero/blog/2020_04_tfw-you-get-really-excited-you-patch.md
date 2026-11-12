# TFW you-get-really-excited-you-patch-diffed-a-0day-used-in-the-wild-but-then-find-out-it-is-the-wrong-vuln - Project Zero

Source: https://projectzero.google/2020/04/tfw-you-get-really-excited-you-patch.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Maddie Stone, Project Zero

# INTRODUCTION

I’m really interested in 0-days exploited in the wild and what we, the security community, can learn about them to make 0-day hard. I explained some of Project Zero’s ideas and goals around in-the-wild 0-days in a [November blog post](/2019/11/bad-binder-android-in-wild-exploit.html).


On December’s Patch Tuesday, I was immediately intrigued by CVE-2019-1458, a Win32k Escalation of Privilege (EoP), said to be exploited in the wild and discovered by Anton Ivanov and Alexey Kulaev of Kaspersky Lab. Later that day, Kaspersky published a [blog post](https://securelist.com/windows-0-day-exploit-cve-2019-1458-used-in-operation-wizardopium/95432/) on the exploit. The blog post included details about the exploit, but only included partial details on the vulnerability. My end goal was to do variant analysis on the vulnerability, but without full and accurate details about the vulnerability, I needed to do a root cause analysis first. I tried to get my hands on the exploit sample, but I wasn't able to source a copy.


Without the exploit, I had to use binary patch diffing in order to complete root cause analysis. Patch diffing is an often overlooked part of the perpetual vulnerability disclosure debate, as vulnerabilities become public knowledge as soon as a software update is released, not when they are announced in release notes. Skilled researchers can quickly determine the vulnerability that was fixed by comparing changes in the codebase between old and new versions. If the vulnerability is not publicly disclosed before or at the same time that the patch is released, then this could mean that the researchers who undertake the patch diffing effort could have more information than the defenders deploying the patches.


While my patch diffing adventure did not turn out with me analyzing the bug I intended (more on that to come!), I do think my experience can provide us in the community with a data point. It’s rarely possible to reference hard timelines for how quickly sophisticated individuals can do this type of patch-diffing work, so we can use this as a test. I acknowledge that I have significant experience in reverse engineering, however I had no previous experience at all doing research on a Windows platform, and no knowledge of how the operating system worked. It took me three work weeks from setting up my first VM to having a working crash proof-of-concept for a vulnerability. This can be used as a data point (likely a high upper bound) for the amount of time it takes for individuals to understand a vulnerability via patch diffing and to create a working proof-of-concept crasher, since most individuals will have prior experience with Windows.


But as I alluded to above, it turns out I analyzed and wrote a crash POC for not CVE-2019-1458, but actually [CVE-2019-1433](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1433). I wrote this whole blog post back in January, went through internal reviews, then sent the blog post to Microsoft to preview (we provide vendors with 24 hour previews of blog posts). That’s when I learned I’d analyzed CVE-2019-1433, not CVE-2019-1458. At the beginning of March, Piotr Florczyk published a [detailed root cause analysis and POC for the “real” CVE-2019-1458 bug](https://github.com/piotrflorczyk/cve-2019-1458_POC). With the “real” root cause analysis for CVE-2019-1458 now available, I decided that maybe this blog post could still be helpful to share what my process was to analyze Windows for the first time and where I went wrong.


This blog post will share my attempt to complete a root cause analysis of CVE-2019-1458 through binary patch diffing, from the perspective of someone doing research on Windows for the first time. This includes the process I used, a technical description of the “wrong”, but still quite interesting bug I analyzed, and some thoughts on what I learned through this work, such as where I went wrong. This includes the root cause analysis for CVE-2019-1433, that I originally thought was the vulnerability for the in the wild exploit. As far as I know, the vulnerability detailed in this blog post was not exploited in the wild.

# MY PROCESS

When the vulnerability was disclosed on December’s Patch Tuesday, I was immediately interested in the vulnerability. As a part of my new role on Project Zero where I’m leading efforts to study 0-days used in the wild, I was really interested in learning Windows. I had never done research on a Windows platform and didn’t know anything about Windows programming or the kernel. This vulnerability seemed like a great opportunity to start since:

1. Complete details about the specific vulnerability weren't available,
2. It affected both Windows 7 and Windows 10, and
3. The vulnerability is in win32k which is a core component of the Windows kernel.


I spent a few days trying to get a copy of the exploit, but wasn’t able to. Therefore I decided that binary patch-diffing would be my best option for figuring out the vulnerability. I was very intrigued by this vulnerability because it affected Windows 10 in addition to Windows 7. However, James Forshaw advised me to patch diff the Windows 7 win32k.sys files rather than the Windows 10 versions. He suggested this for a few reasons:

1. The signal to noise ratio is going to be much higher for Windows 7 rather than Windows 10. This “noise” includes things like[Control Flow Guard](https://docs.microsoft.com/en-us/windows/win32/secbp/control-flow-guard), more inline instrumentation calls, and “weirder” compiler settings.
2. On Windows 10, win32k is broken up into a few different files: win32k.sys, win32kfull.sys, win32kbase.sys, rather than a single monolithic file.
3. Kaspersky’s blog post stated that not all Windows 10 builds were affected.


I got to work creating a Windows 7 testing environment. I created a Windows 7 SP1 x64 VM and then started the long process of patching it up until September 2019 (the last available update prior to the December 2019 update where the vulnerability was supposedly fixed). This took about a day and a half as I worked to find the right order to apply the different updates.


Turns out that me thinking that September 2019 was the last available update prior to December 2019 would be one of the biggest reasons that I patch-diffed the wrong bug. I thought that September 2019 was the latest because it was the only update shown to me, besides December 2019, when I clicked “Check for Updates” within the VM. Because I was new to Windows, I didn’t realize that not all updates may be listed in the Windows Update window or that updates could also be downloaded from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/Home.aspx). When Microsoft told me that I had analyzed the wrong vulnerability, that’s when I realized my mistake. CVE-2019-1433, the vulnerability I analyzed, was patched in November 2019, not December 2019. If I had patch-diffed November to December, rather than September to December, I wouldn’t have gotten mixed up.


Once the Windows 7 VM had been updated to Sept 2019, I made a copy of its C:\Windows\System32\win32k.sys file and snapshotted the VM. I then updated it to the most recent patch, December 2019, where the vulnerability in question was fixed. I then snapshotted the VM again and saved off the copy of win32k.sys. These two copies of win32k.sys are the two files I diffed in my patch diffing analysis.


Win32k is a core kernel driver that is responsible for the windows that are shown as a part of the GUI. In later versions of Windows, it’s broken up into multiple files rather than the single file that it is on Windows 7. Having only previously worked on the Linux/Android and RTOS kernels, the GUI aspects took a little bit of time to wrap my head around.


On James Foreshaw’s recommendation, I cloned my VM so that one VM would run [WinDbg](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/getting-started-with-windbg--kernel-mode-) and debug the other VM. This allows for kernel debugging.


Now that I had a copy of the supposed patched and supposed vulnerable versions of win32k.sys, it’s time to start patch diffing.

## PATCH DIFFING WINDOWS 7 WIN32K.SYS

I decided to use BinDiff to patch diff the two versions of win32k. In October 2019, I did a comparison on the different binary diffing tools available \[[video](https://thecyberwire.com/stories/Maddie-Stone-Whatsup-with-WhatsApp-A-Detailed-Walk-Through-of-Reverse-Engineering-CVE-2019-3568.html), [slides](https://github.com/maddiestone/ConPresentations/raw/master/Jailbreak2019.WhatsUpWithWhatsApp.pdf)\], and for me, BinDiff worked best “out of the box” so I decided to at least start with that again.


I loaded both files into IDA and then ran BinDiff between the two versions of win32k. To my pleasant surprise, there were only 23 functions total in the whole file/driver that had changed from one version to another. In addition, there were only two new functions added in the December 2019 file that didn’t exist in September. This felt like a good sign: 23 functions seemed like even in the worst case, I could look at all of them to try and find the patched vulnerability. (Between the November and December 2019 updates only 5 functions had changed, which suggests the diffing process could have been even faster.)


Original BinDiff Matched Functions of win32k.sys without Symbols


When I started the diff, I didn’t realize that the Microsoft Symbol Server was a thing that existed. I learned about the Symbol Server and was told that I could easily get the symbols for a file by running the following command in WinDbg: x win32k!\*. I still hadn’t realized that IDA Pro had the capability to automatically get the symbols for you from a PDB file, even if you aren’t running IDA on a Windows computer. So after running the WinDBG command, I copied all of the output to a file, rebased my IDA Pro databases to the same base address and then would manually rename functions as I was reversing based on the symbols and addresses in the text file. About a week into this escapade, I learned how to modify the IDA configuration file to have my IDA Pro instance, running on Linux, connect to my Windows VM to get the symbols.


BinDiff Matched Function of win32k.sys with Symbols


What stood out at first when I looked at BinDiff was that none of the functions called out in Kaspersky’s blog post had been changed: not DrawSwitchWndHilite, CreateBitmap, SetBitmapBits, nor NtUserMessageCall. Since I didn’t have a strong indicator for a starting point, I instead tried to rule out functions that likely wouldn’t be the change that I was looking for. I first searched for function names to determine if they were a part of a different blog post or CVE. Then I looked through all of the CVEs claimed to affect Windows 7 that were fixed in the December Bulletin and matched them up. Through this I ruled out the following functions:


## EXPLORING THE WRONG CHANGES

At this point I started scanning through functions to try and understand their purpose and look at the changes that were made. GreGetStringBitmapW caught my eye because it had “bitmap” in the name and Kaspersky’s blog post talked about the use of bitmaps.


The changes to GreGetStringBitmapW didn’t raise any flags: one of the changes had no functional impact and the other was sending arguments to another function, a function that was also listed as having changed in this update. This function had no public symbols available and is labeled as vuln\_sub\_FFFFF9600028F200 in the Bindiff image above. In the Dec 2019 win32k.sys its offset from base address is 0x22F200.

As shown by the BinDiff flow graph above, there is a new block of code added in the Dec 2019 version of win32k.sys. The Dec 2019 added argument checking before using that argument when calculating where to write to a buffer. This made me think that this was a vulnerability in contention: it’s called from a function with bitmap in the name and appears that there would be a way to overrun a buffer.


I decided to keep reversing and spent a few days on this change. I was getting deep down in the rabbit hole though and had to remember that the only tie I had between this function and the details known about the in-the-wild exploit was that “bitmap” was in the name. I needed to determine if this function was even called during the calls mentioned in the Kaspersky blog post. I followed cross-references to determine how this function could be called.

The Nt prefix on function names means that the function is a syscall. The Gdi in NtGdiGetStringBitmapW means that the user-mode call is in gdi32.dll. Mateusz Jurczyk provides a table of Windows syscalls [here](https://j00ru.vexillium.org/syscalls/win32k/64/).  Therefore, the only way to trigger this function is through a syscall to NtGdiGetStringBitmapW. In gdi32.dll, the only call to NtGdiGetStringBitmapW is GetStringBitmapA, which is exported.


Tracing this call path and realizing that none of the functions mentioned in the Kaspersky blog post called this function made me realize that it was pretty unlikely that this was the vulnerability. However, I decided to dynamically double check that this function wouldn’t be called when calling the functions listed in the blog post or trigger the task switch window.


I downloaded Visual Studio into my Windows 7 VM and wrote my first Windows Desktop app, following [this guide](https://docs.microsoft.com/en-us/cpp/windows/walkthrough-creating-windows-desktop-applications-cpp?view=vs-2019). Once I had a working “Hello, World”, I began to add calls to the functions that are mentioned in the Kaspersky blog post: Creating the “Switch” window, CreateBitmap, SetBitmapBits, NtUserMessageCall, and half-manually/half-programmatically trigger the task-switch window, etc. I set a kernel breakpoint in Windbg on the function of interest and then ran all of these. The function was never triggered, confirming that it was very unlikely this was the vulnerability of interest.


I then moved on to GreAnimatePalette. When you trigger the task switch window, it draws a new window onto the screen and moves the “highlight” to the different windows each time you press tab. I thought that, “Sure, that could involve animating a palette”, but I learned from last time and started with trying to trigger the call in WinDbg instead. I found that it was never called in the methods that I was looking at so I didn’t spend too long and moved on.


## NARROWING IT DOWN TO xxxNextWindow and xxxKeyEvent

After these couple of false starts, I decided to change my process. Instead of starting with the functions in the diff, I decided to start at the function named in Kaspersky’s blog: DrawSwitchWndHilite. I searched the cross-references graph to DrawSwitchWndHilite for any functions listed in the diff as having been changed.

As shown in the call graph above, xxxNextWindow is two calls above DrawSwitchWndHilite. When I looked at xxxNextWindow, I then saw that xxxNextWindow is only called by xxxKeyEvent and all of the changes in xxxKeyEvent surrounded the call to xxxNextWindow. These appeared to be the only functions in the diff that lead to a call to DrawSwitchWndHilite so I started reversing to understand the changes.


## REVERSING THE VULNERABILITY

I had gotten symbols for the function names in my IDA databases, but for the vast majority of functions, this didn’t include type information. To begin finding type information, I started googling for different function names or variable names. While it didn’t have everything, ReactOS was one of the best resources for finding type information, and most of the structures were already in IDA.


For example, when looking at xxxKeyEvent, I saw that in one case, the first argument to xxxNextWindow is gpqForeground. When I googled for gpqForeground, ReactOS showed me that this variable has type tagQ \*. Through this, I also realized that Windows uses a convention for naming variables where the type is abbreviated at the beginning of the name. For example: gpqForeground → global, pointer to queue (tagQ \*), gptiCurrent → global, pointer to thread info (tagTHREADINFO \*).


This was important for the modification to xxxNextWindow. There was a single line change between September and December to xxxNextWindow. The change checked a single bit in the structure pointed to by arg1. If that bit is set, the function will exit in the December version. If it’s not set, then the function proceeds, using arg1. Once I knew that the type of the first argument was tagQ \*, I used WinDbg and/or IDA to see its structure. The command in WinDbg is dt win32k!tagQ.


At this point, I was pretty sure I had found the vulnerability (😉), but I needed to prove it. This involved about a week more of reversing, reading, debugging, wanting to throw my computer out the window, and getting intrigued by potential vulnerabilities that were not this vulnerability. As a side note, for the reversing, I found that the HexRays decompiler was great for general triage and understanding large blocks of code, but for the detailed understanding necessary (at least for me) for writing a proof-of-concept (POC), I mainly used the disassembly view.

## RESOURCES

Here are some of the resources that were critical for me:

- I learned about thread locking, assignment locking, and user-mode callbacks.
- “One Bit To Rule A System: Analyzing CVE-2016-7255 Exploit In The Wild” by Jack Tang, Trend Micro Security Intelligence \[[blog](https://blog.trendmicro.com/trendlabs-security-intelligence/one-bit-rule-system-analyzing-cve-2016-7255-exploit-wild/)\]
- This was an analysis of a vulnerability also related to xxxNextWindow. This blog helped me ultimately figure out how to trigger xxxNextWindow and some argument types of other functions.
- This blog helped me figure out how to modify the dispatch table pointer with my own function so that I could execute during the user-mode callback.
- “Windows Kernel Reference Count Vulnerabilities - Case Study” by Mateusz Jurczyk, Zero Nights 2012 \[[slides](https://j00ru.vexillium.org/slides/2012/zeronights.pdf)\]
- P0 Team Members: James Forshaw, Tavis Ormandy, Mateusz Jurczyk, and Ben Hawkes

# TIMELINE

- Oct 31 2019: Chrome releases fix for CVE-2019-13720
- Dec 10 2019: Microsoft Security Bulletin lists CVE-2019-1458 as exploited in the wild and fixed in the December updates.
- Dec 10-16 2019: I ask around for a copy of the exploit. No luck!
- Dec 16 2019: I begin setting up a Windows 7 kernel debugging environment. (And 2 days work on a different project.)
- Dec 23 2019: VM is set-up. Start patch diffing
- Dec 24-Jan 2: Holiday
- Jan 2 - Jan 3: Look at other diffs that weren’t the vulnerability. Try to trigger DrawSwitchWndHilite
- Jan 6: Realize changes to xxxKeyEvent and xxxNextWindow is the correct change. (Note dear reader, this is not in fact the “correct change”.)
- Jan 6-Jan16: Figure out how the vulnerability works, go down random rabbit holes, work on POC.
- Jan 16: Crash POC crashes!


Approximately 3 work weeks to set up a test environment, diff patches, and create crash POC.

# CVE-2019-1458 CVE-2019-1433 ROOT CAUSE ANALYSIS

Bug class: use-after-free


## OVERVIEW

The vulnerability is a use-after-free of a tagQ object in xxxNextWindow, freed during a user mode callback. (The xxx prefix on xxxNextWindow means that there is a callback to user-mode.) The function xxxKeyEvent is the only function that calls xxxNextWindow and it calls xxxNextWindow with a pointer to a tagQ object as the first argument. Neither xxxKeyEvent  nor xxxNextWindow lock the object to prevent it from being freed during any of the user-mode callbacks in xxxNextWindow. After one of these user-mode callbacks (xxxMoveSwitchWndHilite), xxxNextWindow then uses the pointer to the tagQ object without any verification, causing a use-after free.

## DETAILED WALK THROUGH

This section will walk through the vulnerability on Windows 7. I analyzed the Windows 7 patches instead of Windows 10 as explained above in the process section. The Windows 7 crash POC that I developed is available [here](https://drive.google.com/file/d/1V9HHljjRq17hnfqasExnCiGCJLkt0aOX/view).

### ANALYZED SAMPLES

I did the diff and analysis between the September and December 2019 updates of win32k.sys as explained in the “My Process” section.


Vulnerable win32k.sys (Sept 2019): 9dafa6efd8c2cfd09b22b5ba2f620fe87e491a698df51dbb18c1343eaac73bcf (SHA-256)

Patched win32k.sys (December 2019): b22186945a89967b3c9f1000ac16a472a2f902b84154f4c5028a208c9ef6e102 (SHA-256)


### OVERVIEW

This walk through is broken up into the following sections to describe the vulnerability:

- Triggering xxxNextWindow
- Freeing the tagQ (queue) structure
- User-mode callback xxxMoveSwitchWndHilite
- Using the freed queue

### TRIGGERING xxxNextWindow

The code path is triggered by a special set of keyboard inputs to open a “Sticky Task Switcher” window. As a side note, I didn’t find a way to manually trigger the code path, only programmatically (not that an individual writing an EoP would need it to be triggered manually). To trigger xxxNextWindow, my proof-of-concept (POC) sends the following keystrokes using the SendInput API:


\<ALT (Extended)> + TAB + TAB release + ALT + CTRL + TAB + release all except ALT extended + TAB. (See triggerNextWindow function in POC).


The “normal” way to trigger the task switch window is with ALT + TAB, or ALT+CTRL+TAB for “sticky”. However, this window won’t hit the vulnerable code path, xxxNextWindow. The “normal” task switching window, shown below, looks different from the task switching window displayed when the vulnerable code path is being executed. Shown below is the “normal” task switch window that is displayed when ALT+TAB \[+CTRL\] are pressed and xxxNextWindow is NOT triggered. The window that is shown when xxxNextWindow is triggered is shown below that. 


"Normal" task switch window

Window that is displayed when xxxNextWindow is called

If this is the first “tab press” then the task switch window needs to be drawn on the screen. This code path through xxxNextWindow is not the vulnerable one. The next time you hit TAB, after the window has already been drawn on the screen, when the rectangle should move to the next window, is when the vulnerable code in xxxNextWindow can be reached.


### FREEING THE QUEUE in xxxNextWindow

xxxNextWindow takes a pointer to a queue (tagQ struct) as its first argument. This tagQ structure is the object that we will use after it is freed. We will free the queue in a user-mode callback from the function.


At LABEL\_106 below (xxxNextWindow+0x847), the queue is used without verifying whether or not it still exists. The only way to reach LABEL\_106 in xxxNextWindow is from the branch at xxxNextWindow+0x842. This means that our only option for a user-callback mode is in the function xxxMoveSwitchWndHilite. xxxMoveSwitchWndHilite is responsible for moving the little box within the task switch window that highlights the next window.



#### USER-MODE CALLBACK in xxxMoveSwitchWndHilite

There are quite a few different user-mode callbacks within xxxMoveSwitchWndHilite. Many of these could work, but the difficulty is picking one that will reliably return to our POC code. I chose the call to xxxSendMessageTimeout in DrawSwitchWndHilite.


This call is sending the message to the window that is being highlighted in the task switch window by xxxMoveSwitchWndHilite. Therefore, if we create windows in our POC, we can ensure that our POC will receive this callback.


xxxMoveSwitchWndHilite sends message 0x8C which is WM\_LPKDRAWSWITCHWND. This is an undocumented message and thus it’s not expected that user applications will respond to this message. Instead, there is a user-mode function that is automatically dispatched by ntdll!KiUserCallbackDispatcher. The user-mode callback for this message is user32!\_fnINLPKDRAWSWITCHWND. In order to execute code during this callback, in the POC we hot-patch the PEB.KernelCallbackTable, using the methodology documented [here](https://j00ru.vexillium.org/2010/09/kernel-exploitation-r0-to-r3-transitions-via-keusermodecallback/).


In the callback, we free the tagQ structure using [AttachThreadInput](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-attachthreadinput). AttachThreadInput “attaches the input processing mechanism of one thread to that of another thread” and to do this, it destroys the queue of the thread that is being attached to another thread’s input. The two threads then share a single queue. In the callback, we also have to perform the following operations to force execution down the code path that will use the now freed queue:

1. xxxMoveSwitchWndHilite returns the handle of the next window it should highlight. When this handle is passed to HMValidateHandleNoSecure, it needs to return 0. Therefore, in the callback we need to destroy the window that is going to be highlighted. When HMValidateHandleNoSecure returns 0, we’ll loop back to the top of the while loop.
2. Once we’re back at the top of the while loop, in the following code block we need to set v45 to 0. There appear to be two options: fail the check such that you go in the else block or set the extra data in the tagWND struct to 0 using SetWindowLongPtr. The SetWindowLongPtr method doesn’t work because this window is a special system class (fnid == 0x2A0). Therefore, we must fail one of the checks and end up in the else block in order to be in the code path that will allow us to use the freed queue.



### USING THE FREED QUEUE

Once v45 is set to 0, the thread is unlocked and execution proceeds to LABEL\_106 (xxxNextWindow + 0x847) where mov r14, \[rbp+50h\] is executed. rbp is the tagQ pointer so we dereference it and move it into r14. Therefore we now have a use-after-free.


## WINDOWS 10

CVE-2019-1433 also affected Windows 10 builds. I did not analyze any Windows 10 builds besides 1903.


Vulnerable (Oct 2019) win32kfull.sys: c2e7f733e69271019c9e6e02fdb2741c7be79636b92032cc452985cd369c5a2c (SHA-256)

Patched (Nov 2019) win32kfull.sys: 15c64411d506707d749aa870a8b845d9f833c5331dfad304da8828a827152a92 (SHA-256)


I confirmed that the vulnerability existed on Windows 10 1903 as of the Oct 2019 patch by triggering the use-after-free with Driver Verifier enabled on win32kfull.sys. Below are excerpts from the crash.



To trigger the crash, I only had to change two things in the Windows 7 POC:

1. The keystrokes are different to trigger the xxxNextWindow task switch window on Windows 10. I was able to trigger it by smashing CTRL+ALT+TAB while the POC was running (and triggering the normal task switch Window). It is possible to do this programmatically, I just didn’t take the time to code it up.
2. Overwrite index 0x61 instead of 0x57 in the KernelCallbackTable.


It took me about 3 hours to get the POC to trigger Driver Verifier on Windows 10 1903 regularly (about every 3rd time it's run).


The fix in the November update for Windows 10 1903 is the same as the Windows 7 fix:

- Add the UnlockQueue function.
- Add locking around the call to xxxNextWindow.
- Check the “destroyed” bitflag in the tagQ struct before proceeding to use the queue.


# FIXING THE VULNERABILITY

To patch the CVE-2019-1433  vulnerability, Microsoft changed four functions:

- xxxNextWindow
- xxxKeyEvent (Windows 7)/EditionHandleAndPostKeyEvent (Windows 10)
- zzzDestroyQueue
- UnlockQueue (new function)


Overall, the changes are to prevent the queue structure from being freed and track if something attempted to destroy the queue. The addition of the new function, UnlockQueue, suggests that there were no previous locking mechanisms for queue objects.


## zzzDestroyQueue Patch

The only change to the zzzDestroyQueue function in win32k is that if the refcount on the tagQ structure (tagQ.cLockCount) is greater than 0 (keeping the queue from being freed immediately), then the function now sets a bit in tagQ.QF\_flags.

zzzDestroyQueue Pre-Patch
  
zzzDestroyQueue Post-Patch

xxxNextWindow Patch

There is a single change to the xxxNextWindow function as shown by the BinDiff graph below. When execution is about to use the queue again (at what was LABEL\_106 in the vulnerable version), a check has been added to see if a bitflag in tagQ.QF\_flags is set. The instructions added to xxxNextWindow+0x847 are as follows where rbp is the pointer to the tagQ structure.



If the bit is set, the function exists. If the bit is not set, the function continues and will use the queue. The only place this bit is set is in zzzDestroyQueue. The bit is set when the queue was destroyed, but couldn't be freed immediately because its refcount (tagQ.cLockCount) is greater than 0. Setting the bit is a new change to the code base as described in the section above.

## xxxKeyEvent (Windows 7)/EditionHandleAndPostKeyEvent (Windows 10) Patch

In this section I will simply refer to the function as xxxKeyEvent since Windows 7 was the main platform analyzed. However, the changes are also found in the EditionHandleAndPostKeyEvent function in Windows 10.


The change to xxxKeyEvent is to thread lock the queue that is passed as the first argument to xxxNextWindow. Thread locking doesn’t appear to be publicly documented by Microsoft. My understanding comes from Tarjei Mandt’s 2011 Blackhat USA presentation, “[Kernel Attacks through User-Mode Callbacks](https://media.blackhat.com/bh-us-11/Mandt/BH_US_11_Mandt_win32k_WP.pdf)”. Thread locking is where objects are added to a thread’s lock list, and their ref counter is increased in the process. This prevents them from being freed while they are still locked to the thread.


The new function, UnlockQueue, is used to unlock the queue.


xxxKeyEvent+92E Pre-Patch


xxxKeyEvent+94E Post-Patch


# CONCLUSION

So...I got it wrong. Based on the details provided by Kaspersky in their blog post, I attempted to patch diff the vulnerability in order to do a root cause analysis. It was only based on the feedback from Microsoft (Thanks, Microsoft!) and their guidance to look at the InitFunctionTables method, that I realized I had analyzed a different bug. I analyzed CVE-2019-1433 rather than CVE-2019-1458, the vulnerability exploited in the wild. The real root cause analysis for CVE-2019-1458 was documented by @florek\_pl [here](https://github.com/piotrflorczyk/cve-2019-1458_POC).


If I had patch-diffed November 2019 to December 2019 rather than September to December, then I wouldn’t have analyzed the wrong bug. This seems obvious after the fact, but when just starting out, I thought that maybe Windows 7, being so close to end of life, didn’t get updates every single month. Now I know to not only rely on Windows Update, but also to look for KB articles and that I can download additional updates from the Microsoft Update Catalog.


Although this blog post didn’t turn out how I originally planned, I decided to share it in the hopes that it’d encourage others to explore a platform new to them. It’s often not a straight path, but if you’re interested in Windows kernel research, this is how I got started. In addition, I think this was a fun and quite interesting bug!


I didn’t initially set out to do a patch diffing exercise on this vulnerability, but I do think that this work gives us another data point to use in disclosure discussions. It took me, someone with reversing, but no Windows experience, three weeks to understand the vulnerability and write a proof-of-concept. While I ended up doing this analysis for a vulnerability other than the one I intended, many attackers are not looking to patch-diff a specific vulnerability, but rather any vulnerability that they could potentially exploit. Therefore, I think that three weeks can be used as an approximate high upper bound since most attackers looking to use this technique will have more experience.
