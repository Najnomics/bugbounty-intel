# How to Compromise the Enterprise Endpoint - Project Zero

Source: https://projectzero.google/2016/06/how-to-compromise-enterprise-endpoint.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

# Posted by Tavis Ormandy.

Symantec is a popular vendor in the enterprise security market, their flagship product is  [Symantec Endpoint Protection](https://en.wikipedia.org/wiki/Symantec_Endpoint_Protection). They sell various products using the same core engine in several markets, including a consumer version under the [Norton](https://en.wikipedia.org/wiki/Norton_AntiVirus) brand.

Today we’re publishing details of multiple critical vulnerabilities that we discovered, including many wormable remote code execution flaws.

These vulnerabilities are as bad as it gets. They don’t require any user interaction, they affect the default configuration, and the software runs at the highest privilege levels possible. In certain cases on Windows, vulnerable code is even loaded into the kernel, resulting in remote kernel memory corruption.


As Symantec use the same core engine across their entire product line, all Symantec and Norton branded antivirus products are affected by these vulnerabilities, including:


- Norton Security, Norton 360, and other legacy Norton products (All Platforms)
- Symantec Endpoint Protection (All Versions, All Platforms)
- Symantec Email Security (All Platforms)
- Symantec Protection Engine (All Platforms)
- Symantec Protection for SharePoint Servers
- And so on.


Some of these products cannot be automatically updated, and administrators must take immediate action to protect their networks. Symantec has published advisories for customers, available [here](https://www.symantec.com/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=&suid=20160628_00).


Let’s take a look at a sample of the vulnerabilities we found.


Unpackers in the Kernel: Maybe not the best idea?


Many developers will be familiar with executable packers like [UPX](http://upx.sourceforge.net/), they’re tools intended to reduce the size of executables by compressing them. This causes a problem for antivirus products because it changes how executables look.


Antivirus vendors solve this problem with two solutions. First, they write dedicated unpackers to reverse the operation of the most common packers, and then use emulation to handle less common and custom packers.


The problem with both of these solutions is that they’re hugely complicated and prone to vulnerabilities; it’s extremely challenging to make code like this safe. We recommend [sandboxing](https://www.chromium.org/developers/design-documents/sandbox) and a [Security Development Lifecycle](https://www.microsoft.com/en-us/sdl/), but vendors will often cut corners here. Because of this, unpackers and emulators continue to be a huge source of vulnerabilities, we’ve written about examples in [Comodo](https://bugs.chromium.org/p/project-zero/issues/detail?id=769), [ESET](/2015/06/analysis-and-exploitation-of-eset.html), [Kaspersky](/2015/09/kaspersky-mo-unpackers-mo-problems.html), [Fireeye](/2015/12/fireeye-exploitation-project-zeros.html) and [many more](https://bugs.chromium.org/p/project-zero/issues/list?can=1&q=&sort=-id).


Let’s look at an example from Symantec and Norton Antivirus. This vulnerability has an unusual characteristic: Symantec runs their unpackers in the Kernel!

### CVE-2016-2208: Vulnerability Details


[ASPack](http://www.aspack.com/)is commercial packing software that’s been around for a long time, and Symantec has dedicated unpackers for a few older versions. Reviewing Symantec’s unpacker, we noticed a trivial buffer overflow when a section’s

[SizeOfRawData](<https://msdn.microsoft.com/en-us/library/windows/desktop/ms680341(v=vs.85).aspx>)field is greater than

[SizeOfImage](<https://msdn.microsoft.com/en-us/library/windows/desktop/ms680339(v=vs.85).aspx>). When this happens, Symantec will allocate SizeOfImage bytes and then memcpy all available data into the buffer.


Effectively, we can get Symantec to execute a sequence like this:


char \*buf = malloc(SizeOfImage);


memcpy(&buf\[DataSection->VirtualAddress\],

DataSection->PointerToRawData,

SectionSizeOnDisk);



All of these values are attacker controlled, resulting in a very clean heap or pool overflow. To build a test case, I researched how to identify ASPack on OpenRCE’s packer database:


| .aspack:00412001                 public start .aspack:00412001 start           proc near .aspack:00412001                 pusha .aspack:00412002                 call    skipBytes .aspack:00412002 ... .aspack:00412014                 pop     ebp .aspack:00412015                 mov     ebx, 0FFFFFFEDh .aspack:0041201A                 add     ebx, ebp .aspack:0041201C                 sub     ebx, 12000h .aspack:00412022                 cmp     dword ptr \[ebp+422h\], 0 .aspack:00412029                 mov     \[ebp+422h\], ebx .aspack:0041202F                 jnz     END\_OF\_PACKER ... | 
| Abbreviated sample ASPack sample code from [http://www.openrce.org/reference\_library/packer\_database\_view/17](http://www.openrce.org/reference_library/packer_database_view/17) | 


This was enough for me to make a testcase in [NASM](http://www.nasm.us/) that reliably triggered Symantec’s ASPack unpacker. Once I verified this work with a debugger, building a PE header that mismatched SizeOfImage and SizeOfRawData would reliably trigger the vulnerability.


| VirtualAddress      equ 0x10000-0x08    ; VirtualAddress of section data, offset where copy starts. SizeOfImage         equ 0x12000-0x0C    ; Size you want to allocate. SectionPadding      equ 0x2000          ; SizeOfImage-VirtualAddress ; Section Headers db ".data", 0, 0, 0                 ; Name dd 0                                ; VirtualSize dd VirtualAddress                   ; VirtualAddress dd 0xffffffff                       ; SizeOfRawData dd \_\_data                           ; PointerToRawData dd 0                                ; PointerToRelocations dd 0                                ; PointerToLinenumbers dw 0                                ; NumberOfRelocations dw 0                                ; NumberOfLinenumbers dd 0                                ; Characteristics | 
| Configuring PE section headers to trigger ASPack overflow. | 



On Linux, Mac and other UNIX platforms, this results in a clean heap overflow as root in the Symantec or Norton process. On Windows, this results in kernel memory corruption.


Because Symantec uses a filter driver to intercept all system I/O, just emailing a file to a victim or sending them a link to an exploit is enough to trigger it - the victim does not need to open the file or interact with it in anyway. Because no interaction is necessary to exploit it, this is a wormable vulnerability with potentially devastating consequences to Norton and Symantec customers.


An attacker could easily compromise an entire enterprise fleet using a vulnerability like this. Network administrators should keep scenarios like this in mind when deciding to deploy Antivirus, it’s a significant tradeoff in terms of increasing attack surface.


#### PowerPoint Stream Stack Buffer Overflow


Parsing PowerPoint and other Microsoft Office files is no simple feat. The data itself is stored in a series of contiguous records documented in [\[MS-PPT\]](<https://msdn.microsoft.com/en-us/library/cc313106(v=office.12).aspx>), but just extracting those records requires parsing a series of streams stored in a filesystem-like container called the Compound File Binary format documented in [\[MS-CFB\]](https://msdn.microsoft.com/en-us/library/dd942138.aspx).


Symantec has implemented an I/O abstraction layer that exposes the PowerPoint streams stored in a Compound File via a stdio-like interface. This framework is part of Symantec’s “decomposer” library, and is used for things like extracting document metadata and embedded macros.


As with stdio, I/O to and from the underlying storage is buffered for performance, so reads can sometimes be satisfied directly from the cache. I noticed that It is possible to force the cache into a misaligned state with combinations of odd-sized records. When this happens, a bug can cause reads to be incorrectly rounded-up, resulting in a buffer overflow.


By forcing the cache into a misaligned state, we can force a request like this:


When this happens, a bug causes the size to be rounded up like this:


This bug can result in a buffer overflow. I found an invocation that looked exploitable, but there’s a significant problem: This routine is only called when using what Symantec calls “Bloodhound Heuristics”.


### BloodHound Heuristics


Symantec exposes a setting to administrators called “Bloodhound Heuristics”, this is called “Advanced Heuristic Protection” on Norton Antivirus, but is effectively the same thing.


Symantec has a whitepaper on their heuristics [here](https://www.symantec.com/avcenter/reference/heuristc.pdf). There are three options available to administrators: Low, Automatic and Aggressive. The default setting is Automatic, which increases the number of tests run dynamically.


I wrote a simple test case that triggers the vulnerability, and it crashes reliably with the “Aggressive” mode, but didn’t work in the default configuration. Requiring a non-default setting would reduce the severity of this vulnerability significantly, so I looked into what would trigger “Aggressive” heuristics automatically.


I downloaded an archive of powerpoint files from [VirusTotal Intelligence](https://www.virustotal.com/en/documentation/searching/) to see if any of them triggered the aggressive heuristics by putting a few breakpoints on tests I was interested in. I got lucky, a few of the files did cause aggressive heuristics mode.


Examining the files and their structure, one stream stood out as unusual, containing an [ExOleObjStgCompressedAtom](<https://msdn.microsoft.com/en-us/library/dd944955(v=office.12).aspx>). Rather than create my own, I simply extracted the compressed object and [%incbin](http://www.nasm.us/doc/nasmdoc3.html#section-3.2.3)’d it into a stream in my testcase.


#### Exploitation


All PROT\_EXEC mappings on Norton Antivirus use ASLR on Windows, but the decomposer library is part of a 32-bit process. As the scan service automatically respawns, brute force should be entirely possible.


However, with careful manipulation of the cache, we can partially overwrite the return address, meaning we don’t have to leak any module address to reliably predict the location of code relative to the return address.

The first stage is to see what we have available, to test this let’s search for an int3 instruction within range.


0:069> s (@eip & 0xffff0000) Lffff cc 1

6cbc9ba3  cc 01 00 00 80 bb 68 46-00 00 00 0f 84 82 00 00  ......hF........


That will do, let’s see if it works….


Perfect! It works every time. The next stage would be to find a sequence of gadgets that extends the range available, and then turn it into a standard ROP exploitation problem.



It’s a 100% reliable remote exploit, effective against the default configuration in Norton Antivirus and Symantec Endpoint, exploitable just from email or the web. As the bug is in the core scan engine’s decomposer library, all Symantec and Norton branded products are affected. This includes but is not limited to:


- Norton Antivirus (Mac, Windows)
- Symantec Endpoint (Mac, Windows, Linux, UNIX)
- Symantec Scan Engine (All Platforms)
- Symantec Cloud/NAS Protection Engine (All Platforms)
- Symantec Email Security (All Platforms)
- Symantec Protection for SharePoint/Exchange/Notes/etc (All Platforms)
- All other Symantec/Norton Carrier, Enterprise, SMB, Home, etc antivirus products.
- And so on..


On Windows, this results in remote code execution as SYSTEM, and root on all other platforms.


Vulnerability Management


As with all software developers, antivirus vendors have to do [vulnerability management](https://en.wikipedia.org/wiki/Vulnerability_management). This means monitoring for new releases of third party software used, watching published vulnerability announcements, and distributing updates.


Nobody enjoys doing this, but it’s an integral part of secure software development.


Symantec dropped the ball here. A quick look at the decomposer library shipped by Symantec showed that they were using code derived from open source libraries like [libmspack](http://www.cabextract.org.uk/libmspack/) and [unrarsrc](http://www.rarlab.com/rar_add.htm), but hadn’t updated them in at least 7 years.


Dozens of public vulnerabilities in these libraries affected Symantec, some with public exploits. We sent Symantec some examples, and they verified they had fallen behind on releases.


#### Conclusion


As well as the vulnerabilities we described in detail here, we also found a collection of other stack buffer overflows, memory corruption and [more](https://bugs.chromium.org/p/project-zero/issues/list?q=label:Vendor-Symantec).

Thanks to Symantec Security Team for their help resolving these bugs quickly.
