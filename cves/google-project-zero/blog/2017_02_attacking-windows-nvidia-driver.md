# Attacking the Windows NVIDIA Driver - Project Zero

Source: https://projectzero.google/2017/02/attacking-windows-nvidia-driver.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Oliver Chang

Modern graphic drivers are complicated and provide a large promising attack surface for EoPs and sandbox escapes from processes that have access to the GPU (e.g. the Chrome GPU process). In this blog post we’ll take a look at attacking the NVIDIA kernel mode Windows drivers, and a few of the bugs that I found. I did this research as part of a 20% project with Project Zero, during which a total of [16](https://bugs.chromium.org/p/project-zero/issues/list?can=1&q=vendor%3ANVIDIA+finder%3Aochang&colspec=ID+Type+Status+Priority+Milestone+Owner+Summary&cells=ids) vulnerabilities were discovered.

## Kernel WDDM interfaces

The kernel mode component of a graphics driver is referred to as the display miniport driver. Microsoft’s [documentation](<https://msdn.microsoft.com/en-us/library/windows/hardware/ff570589(v=vs.85).aspx>) has a nice diagram that summarises the relationship between the various components:


In the DriverEntry() for display miniport drivers, a [DRIVER\_INITIALIZATION\_DATA](<https://msdn.microsoft.com/en-us/library/windows/hardware/ff556169(v=vs.85).aspx>) structure is populated with callbacks to the vendor implementations of functions that actually interact with the hardware, which is passed to dxgkrnl.sys (DirectX subsystem) via DxgkInitialize(). These callbacks can either be called by the DirectX kernel subsystem, or in some cases get called directly from user mode code.

### DxgkDdiEscape

A well known entry point for potential vulnerabilities here is the DxgkDdiEscape interface. This can be called straight from user mode, and accepts arbitrary data that is parsed and handled in a vendor specific way (essentially an IOCTL). For the rest of this post, we’ll use the term “escape” to denote a particular command that’s supported by the DxgkDdiEscape function.


NVIDIA has a whopping 400\~ escapes here at time of writing, so this was where I spent most of my time (the necessity of many of these being in the kernel is questionable):


// (names of these structs are made up by me)

// Represents a group of escape codes

struct NvEscapeRecord {

DWORD action\_num;

DWORD expected\_magic;

void \*handler\_func;

NvEscapeRecordInfo \*info;

\_QWORD num\_codes;

};


// Information about a specific escape code.

struct NvEscapeCodeInfo {

DWORD code;

DWORD unknown;

\_QWORD expected\_size;

WORD unknown\_1;

};


NVIDIA implements their private data (pPrivateDriverData in the DXGKARG\_ESCAPE struct) for each escape as a header followed by data. The header has the following format:


struct NvEscapeHeader {

DWORD magic;

WORD unknown\_4;

WORD unknown\_6;

DWORD size;

DWORD magic2;

DWORD code;

DWORD unknown\[7\];

};


These escapes are identified by a 32-bit code (first member of the NvEscapeCodeInfo struct above), and are grouped by their most significant byte (from 1 - 9).


There is some validation being done before each escape code is handled. In particular, each NvEscapeCodeInfo contains the expected size of the escape data following the header. This is validated against the size in the NvEscapeHeader, which itself is validated against the PrivateDriverDataSize field given to DxgkDdiEscape. However, it’s possible for the expected size to be 0 (usually when the escape data is expected to be variable sized) which means that the escape handler is responsible for doing its own validation. This has led to some bugs ([1](https://bugs.chromium.org/p/project-zero/issues/detail?id=936), [2](https://bugs.chromium.org/p/project-zero/issues/detail?id=940)).


Most of the vulnerabilities found ([13](https://bugs.chromium.org/p/project-zero/issues/list?can=1&q=reporter%3Aochang+escape&colspec=ID+Type+Status+Priority+Milestone+Owner+Summary&cells=ids) in total) in escape handlers were very basic mistakes, such as writing to user provided pointers blindly, disclosing uninitialised kernel memory to user mode, and incorrect bounds checking. There were also numerous issues that I noticed (e.g. OOB reads) that I didn’t report because they didn’t seem exploitable.

### DxgkDdiSubmitBufferVirtual

Another interesting entry point is the DxgkDdiSubmitBufferVirtual function, which is newly introduced in Windows 10 and WDDM 2.0 to support GPU virtual memory (deprecating the old DxgkDdiSubmitBuffer/DxgkDdiRender functions). This function is fairly complicated, and also accepts vendor specific data from the user mode driver for each command submitted. One bug was found [here](https://bugs.chromium.org/p/project-zero/issues/detail?id=1012).

### Others

There are a [few other](<https://msdn.microsoft.com/en-us/library/windows/hardware/ff570147(v=vs.85).aspx>) WDDM functions that accept vendor-specific data, but nothing of interest were found in those after a quick review.

## Exposed devices

NVIDIA also exposes some additional devices that can be opened by any user:


- \\.\NvAdminDevice which appears to be used for[NVAPI](https://developer.nvidia.com/nvapi). A lot of the ioctl handlers seem to call into DxgkDdiEscape.
- \\.\UVMLite{Controller,Process\*}, likely related to NVIDIA’s “unified memory”. 1[bug](https://bugs.chromium.org/p/project-zero/issues/detail?id=880) was found here.
- \\.\NvStreamKms, installed by default as part of GeForce Experience, but you can opt out during installation. It’s not exactly clear why this particular driver is necessary. 1[bug](https://bugs.chromium.org/p/project-zero/issues/detail?id=918) was found here also.

## More interesting bugs

Most of the bugs I found were by manual reversing and analysis, along with some custom IDA scripts. I also ended up writing a fuzzer, which was surprisingly successful given how simple it was.


While most of the bugs were rather boring (simple cases of missing validation), there were a few that were a bit more interesting.

### NvStreamKms

This driver registers a process creation notification callback using the PsSetCreateProcessNotifyRoutineEx function. This callback checks if new processes created on the system match image names that were previously set by sending IOCTLs.


This creation notification routine contained a bug:


(Simplified decompiled output)


wchar\_t Dst\[BUF\_SIZE\];


...


if ( cur->image\_names\_count > 0 ) {

// info\_ is the PPS\_CREATE\_NOTIFY\_INFO that is passed to the routine.

image\_filename = info\_->ImageFileName;

buf = image\_filename->Buffer;

if ( buf ) {

filename\_length = 0i64;

num\_chars = image\_filename->Length / 2;

// Look for the filename by scanning for backslash.

if ( num\_chars ) {

while ( buf\[num\_chars - filename\_length - 1\] != '\\' ) {

++filename\_length;

if ( filename\_length >= num\_chars )

goto DO\_COPY;

}

buf += num\_chars - filename\_length;

}

DO\_COPY:

wcscpy\_s(Dst, filename\_length, buf);

Dst\[filename\_length\] = 0;

wcslwr(Dst);


This routines extracts the image name from the ImageFileName member of PS\_CREATE\_NOTIFY\_INFO by searching backwards for backslash (‘\’). This is then copied to a stack buffer (Dst) using wcscpy\_s, but the length passed is the length of the calculated name, and not the length of the destination buffer.


Even though Dst is a fixed size buffer, this isn’t a straightforward overflow. Its size is bigger than 255 wchars, and for most Windows filesystems path components cannot be greater than 255 characters. Scanning for backslash is also valid for most cases because ImageFileName is a canonicalised path.


It is however, possible to pass a UNC path that keeps forward slash (‘/’) as the path separator after being canonicalised (credits to James Forshaw for pointing me to this). This means we can get a filename of the form “aaa/bbb/ccc/...” and cause an overflow.


For example: CreateProcessW(L"\\\\?\\UNC\\127.0.0.1@8000\\DavWWWRoot\\aaaa/bbbb/cccc/blah.exe", …)


Another interesting note is that the wcslwr following the bad copy doesn’t actually limit the contents of the overflow (the only requirement is valid UTF-16). Since the calculated filename\_length doesn’t include the null terminator, wcscpy\_s will think that the destination is too small and will clear the destination string by writing a null byte at the beginning (after copying the contents up to filename\_length bytes first so the overflow still happens). This means that the wcslwr is useless because this wcscpy\_s call and part of the code never worked to begin with.


Exploiting this is trivial, as the driver is not compiled with stack cookies (hacking like it’s 1999). A local privilege escalation exploit is attached in the [original issue](https://bugs.chromium.org/p/project-zero/issues/detail?id=918) that sets up a fake WebDAV server to exploit the vulnerability (ROP, pivot stack to user buffer, ROP again to allocate rwx mem containing shellcode and jump to it).

### Incorrect validation in UVMLiteController

NVIDIA’s driver also exposes a device at \\.\UVMLiteController that can be opened by any user (including from the sandboxed Chrome GPU process). The IOCTL handlers for this device write results directly to Irp->UserBuffer, which is the output pointer passed to DeviceIoControl (Microsoft’s [documentation](<https://msdn.microsoft.com/en-us/library/windows/hardware/ff550694(v=vs.85).aspx>)  says not to do this).The IO control codes specify METHOD\_BUFFERED, which means that the Windows kernel checks that the address range provided is writeable by the user before passing it off to the driver.


However, these handlers lacked bounds checking for the output buffer, which means that a user mode context could pass a length of 0 with any arbitrary address (which passes the ProbeForWrite check) to result in a limited write-what-where (the “what” here is limited to some specific values: including 32-bit 0xffff, 32-bit 0x1f, 32-bit 0, and 8-bit 0).


## Remote attack vector?

Given the quantity of bugs that were discovered, I investigated whether if any of them can be reached from a completely remote context without having to compromise a sandboxed process first (e.g. through WebGL in a browser, or through video acceleration).


Luckily, this didn’t appear to be the case. This wasn’t too surprising, given that the vulnerable APIs here are very low level and only reached after going through many layers (for Chrome, libANGLE -> Direct3D runtime and user mode driver -> kernel mode driver), and generally called with valid arguments constructed in the user mode driver.

## NVIDIA’s response

The nature of the bugs found showed that NVIDIA has a lot of work to do. Their drivers contained a lot of code which probably shouldn’t be in the kernel, and most of the bugs discovered were very basic mistakes. One of their drivers (NvStreamKms.sys) also lacks very basic mitigations (stack cookies) even today.


However, their response was mostly quick and positive. Most bugs were fixed well under the deadline, and it seems that they’ve been finding some bugs on their own internally. They also indicated that they’ve been working on re-architecturing their kernel drivers for security, but weren’t ready to share any concrete details.

### Timeline

| 2016-07-26 | First bug reported to NVIDIA. | 
| 2016-09-21 | 6 of the bugs reported were fixed silently in the 372.90 release. Discussed patch gap issues with NVIDIA. | 
| 2016-10-23 | Patch released that includes fix for rest (all 14) of the bugs that were reported at the time (375.93). | 
| 2016-10-28 | [Public bulletin](https://nvidia.custhelp.com/app/answers/detail/a_id/4247) released, and P0 bugs derestricted. | 
| 2016-11-04 | Realised that [https://bugs.chromium.org/p/project-zero/issues/detail?id=911](https://bugs.chromium.org/p/project-zero/issues/detail?id=911) wasn’t fixed properly. Notified NVIDIA. | 
| 2016-12-14 |  | 
| 2017-02-14 |  | 


#### Patch gap

NVIDIA’s first patch, which included fixes to 6 of the bugs I reported, did not include a public bulletin (the [release notes](http://us.download.nvidia.com/Windows/372.90/372.90-win10-win8-win7-desktop-release-notes.pdf) mention “security updates”). They had planned to release public details a month after the patch is released. We noticed this, and let them know that we didn’t consider this to be good practice as an attacker can reverse the patch to find the vulnerabilities before the public is made aware of the details given this large window.


While the first 6 bugs fixed did not have details released for more than 30 days, the remaining 8 at the time had a patch released 5 days before the first bulletin was released. It looks like NVIDIA has been trying to reduce this gap, but based on recent bulletins it appears to be inconsistent.
