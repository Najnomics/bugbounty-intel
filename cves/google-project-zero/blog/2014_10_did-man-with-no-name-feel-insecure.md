# Did the “Man With No Name” Feel Insecure? - Project Zero

Source: https://projectzero.google/2014/10/did-man-with-no-name-feel-insecure.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by James Forshaw, Taker of Names


Sometimes when I'm doing security research I'll come across a bug which surprises me. I discovered just such a bug in the Windows version of Chrome which exposed a little-known security detail in the OS. The bug, [CVE-2014-3196](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3196) was fixed in [M38](http://googlechromereleases.blogspot.co.uk/2014/10/stable-channel-update.html), so it seemed a good time for a blog post. The actual reported issue is [here](https://code.google.com/p/chromium/issues/detail?id=338538). While the bug didn’t allow for a full sandbox escape it did provide the initial part of a chain; something that’s still important to fix.

The security of an OS kernel is of extreme importance to modern user-mode sandboxes such as is used in Chrome. Some OS kernels have built-in facilities for reducing the attack surface of the kernel and the OS in general, for example [seccomp](https://www.kernel.org/doc/Documentation/prctl/seccomp_filter.txt) on Linux or the [sandbox facilities](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/sandbox-exec.1.html#//apple_ref/doc/man/1/sandbox-exec) in OS X. While not always perfect they are valuable facilities for Chrome. Windows 8 introduced some steps towards improving sandboxing, such as the AppContainer model and the ability to [disable Win32k system calls](<http://msdn.microsoft.com/en-gb/library/windows/desktop/hh871472(v=vs.85).aspx>). Chrome has experimental support for disabling Win32k (through the --enable\_win32k\_renderer\_lockdown flag), but for many other features it has to make do with what’s available.

On Windows, Chrome relies on the built-in NT permissions model to secure resources from code executing within a sandboxed process. The Windows NT operating system was built with security in mind (no laughing at the back) including a robust and flexible permission model for securing resources. There are two parts to securing resources, the [Access Token](<http://msdn.microsoft.com/en-us/library/windows/desktop/aa374909(v=vs.85).aspx>) which acts as the identity of a process and the [Discretionary Access Control List (DACL)](<http://msdn.microsoft.com/en-us/library/windows/desktop/aa446597(v=vs.85).aspx>) that defines the list of users and groups which can access a resource and what permissions they would be granted. The set of permissions allowed is quite granular (and dependant on the object type), but typically there are separate permissions for read, write and execute operations.

When a user mode process [requests access](<http://msdn.microsoft.com/en-gb/library/windows/desktop/aa446683(v=vs.85).aspx>) to a securable kernel object the kernel's security manager verifies the process Access Token has access to that resource with the required sets of permissions as defined in the DACL. If all permissions are allowed then a Handle is generated, an opaque reference to the object, and returned to the process which can use it in subsequent system calls. Many resources also have the ability to have an assigned name. Think of the name like a file path which represents how to find and open a new handle to the object. You can browse named objects using the [WinObj](http://technet.microsoft.com/en-gb/sysinternals/bb896657.aspx) tool from Sysinternals.


One such securable resource is shared memory sections, sometimes called memory-mapped files. On Windows this is created through the [CreateFileMapping](<http://msdn.microsoft.com/en-gb/library/windows/desktop/aa366537(v=vs.85).aspx>) API function. If you look at the API you'll notice that it has a final parameter which specifies the name of the object. Shared memory sections are used when Chrome needs to share large amounts of data between sandboxed processes and the privileged broker process. The kernel defines a few permissions a program can request when accessing a section object; the most important for our purposes are FILE\_MAP\_WRITE which gives the program the ability to map the memory writable and FILE\_MAP\_READ which gives the program read-only access. If a program is only granted FILE\_MAP\_READ the kernel will ensure it cannot be mapped writable.

One useful feature of shared memory is that a process can create the memory and then share a read-only copy with other processes. This allows a higher privileges process to provide a real-time copy of data which only it can update. A typical way to share sections read-only on Windows is to name them when they're created writeable in the original process. Then by applying an appropriate DACL a sandboxed process calling the [OpenFileMapping](<http://msdn.microsoft.com/en-gb/library/windows/desktop/aa366791(v=vs.85).aspx>) function can only be granted the FILE\_MAP\_READ permission. In Chrome’s case, sections are not shared by providing a name. Instead it uses a different method which we can see by looking at the source code. In the base/memory directory you'll find Chrome's implementation of shared memory for the different platforms. In the [header](https://code.google.com/p/chromium/codesearch#chromium/src/base/memory/shared_memory.h&q=SharedMemory&sq=package:chromium&type=cs&l=32) you'll find an important function:

bool ShareReadOnlyToProcess(ProcessHandle process,

SharedMemoryHandle\* new\_handle) {

return ShareToProcessCommon(process, new\_handle, false,

SHARE\_READONLY);

}


The ShareReadOnlyToProcess function delegates to an OS specific function. For [Windows](https://code.google.com/p/chromium/codesearch#chromium/src/base/memory/shared_memory_win.cc&sq=package:chromium&type=cs) this looked like:

bool SharedMemory::ShareToProcessCommon(ProcessHandle process,

SharedMemoryHandle \*new\_handle,

bool close\_self,

ShareMode share\_mode) {

\*new\_handle = 0;

DWORD access = FILE\_MAP\_READ;

DWORD options = 0;

HANDLE mapped\_file = mapped\_file\_;

HANDLE result;

if (share\_mode == SHARE\_CURRENT\_MODE && !read\_only\_)

access |= FILE\_MAP\_WRITE;


// \*SNIP\* ...


if (!DuplicateHandle(GetCurrentProcess(), mapped\_file, process,

&result, access, FALSE, options))

return false;

\*new\_handle = result;

return true;

}

It might be more obvious if I show it in diagrammatic form. The section object is shared between the different processes but the handles have different permissions.

[When the broker process shares the section read-only it uses the](/images/oldblog/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWypP_s624_dm_02.png)

[DuplicateHandle](<http://msdn.microsoft.com/en-gb/library/windows/desktop/ms724251(v=vs.85).aspx>)API to create a new handle in the sandboxed renderer process. It specifies FILE\_MAP\_READ as the desired permissions so that is all the permissions assigned to the renderer. Now because of the NT security model the renderer process shouldn't be able to re-open the section with write access as the process runs with virtually no permissions in its Token. You'd think that was the case but it turns out not to be. When Chrome created the original section it never supplied a name, it turns out section objects with NO names also have NO security. Surprise!

This behaviour is documented, sort-of. For example have a look at [this](<http://msdn.microsoft.com/en-us/library/windows/desktop/aa379557(v=vs.85).aspx>) MSDN page. Did you see the documented behaviour? It amounts to a throw away comment, with no effort to go into detail. The page doesn’t tell you which unnamed objects have no security, just that some unnamed objects DO have security (such as processes). So let's find out what determines this behaviour. If you dump the OBJECT\_TYPE\_INITIALIZER structure from the public kernel symbols you'll see the offender.

0:000> dt nt!\_OBJECT\_TYPE\_INITIALIZER

ntdll!\_OBJECT\_TYPE\_INITIALIZER

+0x000 Length           : Uint2B

+0x002 ObjectTypeFlags  : UChar

+0x002 CaseInsensitive  : Pos 0, 1 Bit

+0x002 UnnamedObjectsOnly : Pos 1, 1 Bit

+0x002 UseDefaultObject : Pos 2, 1 Bit

+0x002 SecurityRequired : Pos 3, 1 Bit     \<---- Important Flag

+0x002 MaintainHandleCount : Pos 4, 1 Bit

+0x002 MaintainTypeList : Pos 5, 1 Bit

+0x002 SupportsObjectCallbacks : Pos 6, 1 Bit

+0x002 CacheAligned     : Pos 7, 1 Bit

+0x004 ObjectTypeCode   : Uint4B

+0x008 InvalidAttributes : Uint4B

\* SNIP....


The important part of the type is the SecurityRequired flag. If you dump the section object type nt!MmSectionObjectType and compare it to something like the process type nt!PsProcessType you'll see the difference. I guess the question you might be asking is what other types have this same behaviour; well a quick script later on Windows 8.1 and you’ll get the following types which have the SecurityRequired flag set to 0, note of course that the Section type is among the list:

Adapter

ALPC Port

Callback

Controller

Device

Driver

Event

File

FilterCommunicationPort

IoCompletion

IoCompletionReserve

IRTimer

KeyedEvent

Mutant

PcwObject

PowerRequest

Profile

Section

Semaphore

SymbolicLink

Timer

TpWorkerFactory

Type

UserApcReserve

WaitCompletionPacket


There are some interesting types in the list, but remember these types only have no security if they have no name, which would make it trickier to exploit. Also some like “Type” are unlikely to ever be accessible in a user mode process, but it’s still worthwhile pointing them out.

Okay so how might we exploit this in practice? Turns out there was actually only one user of the ShareReadOnlyToProcess method at the time. It was part of the code which shared extension scripts between renderer processes (see [user\_script\_loader.cc](https://code.google.com/p/chromium/codesearch#chromium/src/chrome/browser/extensions/user_script_loader.cc&q=ShareReadONly&sq=package:chromium&l=195)). For reasons of efficiency these scripts were shared read-only to the renderers and relied on the OS enforcing this read-only property of the sections to prevent the renderers modifying the contents. On Linux/OSX this works but due to the issue I’ve just described it didn't work so well on Windows. The contents of the section looked like the image below, it contained a pickled version of the script and extension information.


From a compromised renderer you can call DuplicateHandle to elevate the privileges of the section handle to re-gain write access, then modify the shared memory to execute arbitrary Javascript in any rendered page, including more-privileged chrome:// pages. While this is not directly a sandbox breakout it could be used as part of a chain as demonstrated in [previous attacks](http://blog.chromium.org/2012/06/tale-of-two-pwnies-part-2.html) against the Chrome sandbox. Of course a bug like this might be even more important when [site-isolation](http://www.chromium.org/developers/design-documents/site-isolation) is enabled as a default in Chrome.

[One final note on how you might find similar issues in other applications. Remember that even though each process has different handles, each refers to the same section object in the kernel. A quick way to check on this is to use a tool such as](/images/oldblog/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjReYq_s623_dm_04.png)

[Process Hacker](http://processhacker.sourceforge.net/)or

[Process Explorer](http://technet.microsoft.com/en-gb/sysinternals/bb896653.aspx)and look at the handle table. While not the default you can add the Object Address column to the table, you can then use this information when looking at unnamed sections to determine if any are shared with a more privileged process, and whether any sections are only granted FILE\_MAP\_READ permissions in the low-privileged process.

[This bug is the result of a corner case in the Windows OS. I can understand the reason why it works this way, unnamed objects are not supposed to be trivially shareable so why go to the expense of performing a security check unnecessarily. Strangely even if you try to set a DACL on the section object the kernel will return an error, there is no actual way to secure these types of objects other than by setting a name. When you try and make a secure sandbox on top of such an OS these things can come back to bite you.](/images/oldblog/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjU38v_s624_dm_05.png)
