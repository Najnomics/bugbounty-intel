# The curious tale of a fake Carrier.app - Project Zero

Source: https://projectzero.google/2022/06/curious-case-carrier-app.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Ian Beer, Google Project Zero

NOTE: This issue was CVE-2021-30983 was fixed in iOS 15.2 in December 2021.

Towards the end of 2021 Google's Threat Analysis Group (TAG) shared an iPhone app with me:

App splash screen showing the Vodafone carrier logo and the text "My Vodafone" (not the legitimate Vodadone app)

Although this looks like the real [My Vodafone carrier app](https://apps.apple.com/gb/app/my-vodafone/id370901726) available in the App Store, it didn't come from the App Store and is not the real application from Vodafone. TAG suspects that a target receives a link to this app in an SMS, after the attacker asks the carrier to disable the target's mobile data connection. The SMS claims that in order to restore mobile data connectivity, the target must install the carrier app and includes a link to download and install this fake app.

This sideloading works because the app is signed with an enterprise certificate, which can be purchased for $299 via the Apple [Enterprise developer program](https://developer.apple.com/programs/enterprise/). This program allows an eligible enterprise to obtain an Apple-signed embedded.mobileprovision file with the ProvisionsAllDevices key set. An app signed with the developer certificate embedded within that mobileprovision file can be sideloaded on any iPhone, bypassing Apple's App Store review process. While we understand that the Enterprise developer program is designed for companies to push "trusted apps" to their staff's iOS devices, in this case, it appears that it was being used to sideload this fake carrier app.

In collaboration with Project Zero, [TAG has published an additional post with more details around the targeting and the actor](https://blog.google/threat-analysis-group/italian-spyware-vendor-targets-users-in-italy-and-kazakhstan/). The rest of this blogpost is dedicated to the technical analysis of the app and the exploits contained therein.

## App structure

The app is broken up into multiple frameworks. InjectionKit.framework is a generic privilege escalation exploit wrapper, exposing the primitives you'd expect (kernel memory access, entitlement injection, amfid bypasses) as well as higher-level operations like app installation, file creation and so on.

Agent.framework is partially obfuscated but, as the name suggests, seems to be a basic agent able to find and exfiltrate interesting files from the device like the Whatsapp messages database.

Six privilege escalation exploits are bundled with this app. Five are well-known, publicly available N-day exploits for older iOS versions. The sixth is not like those others at all.

This blog post is the story of the last exploit and the month-long journey to understand it.

## Something's missing? Or am I missing something?

Although all the exploits were different, five of them shared a common high-level structure. An initial phase where the kernel heap was manipulated to control object placement. Then the triggering of a kernel vulnerability followed by well-known steps to turn that into something useful, perhaps by disclosing kernel memory then building an arbitrary kernel memory write primitive.

The sixth exploit didn't have anything like that.

Perhaps it could be triggering a kernel logic bug like Linuz Henze's [Fugu14](https://github.com/LinusHenze/Fugu14) exploit, or a very bad memory safety issue which gave fairly direct kernel memory access. But neither of those seemed very plausible either. It looked, quite simply, like an iOS kernel exploit from a decade ago, except one which was first quite carefully checking that it was only running on an iPhone 12 or 13.

It contained log messages like:

printf("Failed to prepare fake vtable: 0x%08x", ret);

which seemed to happen far earlier than the exploit could possibly have defeated mitigations like KASLR and PAC.

Shortly after that was this log message:

printf("Waiting for R/W primitives...");

Why would you need to wait?

Then shortly after that:

printf("Memory read/write and callfunc primitives ready!");

Up to that point the exploit made only four IOConnectCallMethod calls and there were no other obvious attempts at heap manipulation. But there was another log message which started to shed some light:

printf("Unexpected data read from DCP: 0x%08x", v49);

## DCP?

In October 2021 Adam Donenfeld tweeted this:

DCP is the "Display Co-Processor" which ships with iPhone 12 and above and all M1 Macs.

There's little public information about the DCP; the most comprehensive comes from the [Asahi linux project](https://asahilinux.org/) which is porting linux to M1 Macs. In their [August 2021](https://asahilinux.org/2021/08/progress-report-august-2021/) and [September 2021](https://asahilinux.org/2021/10/progress-report-september-2021/) updates they discussed their DCP reverse-engineering efforts and the open-source DCP client written by [@alyssarzg](https://twitter.com/alyssarzg). Asahi describe the DCP like this:

On most mobile SoCs, the display controller is just a piece of hardware with simple registers. While this is true on the M1 as well, Apple decided to give it a twist. They added a coprocessor to the display engine (called DCP), which runs its own firmware (initialized by the system bootloader), and moved most of the display driver into the coprocessor. But instead of doing it at a natural driver boundary… they took half of their macOS C++ driver, moved it into the DCP, and created a remote procedure call interface so that each half can call methods on C++ objects on the other CPU!

[https://asahilinux.org/2021/08/progress-report-august-2021/](https://asahilinux.org/2021/08/progress-report-august-2021/)

The Asahi linux project reverse-engineered the API to talk to the DCP but they are restricted to using Apple's DCP firmware (loaded by iBoot) - they can't use a custom DCP firmware. Consequently their documentation is limited to the DCP RPC API with few details of the DCP internals.

## Setting the stage

Before diving into DCP internals it's worth stepping back a little. What even is a co-processor in a modern, highly integrated SoC (System-on-a-Chip) and what might the consequences of compromising it be?

Years ago a co-processor would likely have been a physically separate chip. Nowadays a large number of these co-processors are integrated along with their interconnects directly onto a single die, even if they remain fairly independent systems. We can see in this M1 die shot from [Tech Insights](https://www.techinsights.com/blog/two-new-apple-socs-two-market-events-apple-a14-and-m1) that the CPU cores in the middle and right hand side take up only around 10% of the die:

M1 die-shot from techinsights.com with possible location of DCP added

[https://www.techinsights.com/blog/two-new-apple-socs-two-market-events-apple-a14-and-m1](https://www.techinsights.com/blog/two-new-apple-socs-two-market-events-apple-a14-and-m1)

Companies like [SystemPlus](https://www.systemplus.fr/) perform [very thorough analysis of these dies](https://www.systemplus.fr/wp-content/uploads/2020/12/SP20608-Apple-M1-System-on-Chip-Sample.pdf). Based on their analysis the DCP is likely the rectangular region indicated on this M1 die. It takes up around the same amount of space as the four high-efficiency cores seen in the centre, though it seems to be mostly SRAM.

With just this low-resolution image it's not really possible to say much more about the functionality or capabilities of the DCP and what level of system access it has. To answer those questions we'll need to take a look at the firmware.

## My kingdom for a .dSYM!

The first step is to get the DCP firmware image. iPhones (and now M1 macs) use .ipsw files for system images. An .ipsw is really just a .zip archive and the Firmware/ folder in the extracted .zip contains all the firmware for the co-processors, modems etc. The DCP firmware is this file:

Firmware/dcp/iphone13dcp.im4p

The im4p in this case is just a 25 byte header which we can discard:

$ dd if=iphone13dcp.im4p of=iphone13dcp bs=25 skip=1

$ file iphone13dcp

iphone13dcp: Mach-O 64-bit preload executable arm64

It's a Mach-O! Running nm -a to list all symbols shows that the binary has been fully stripped:

$ nm -a iphone13dcp

iphone13dcp: no symbols

Function names make understanding code significantly easier. From looking at the handful of strings in the exploit some of them looked like they might be referencing symbols in a DCP firmware image ("M3\_CA\_ResponseLUT read: 0x%08x" for example) so I thought perhaps there might be a DCP firmware image where the symbols hadn't been stripped.

Since the firmware images are distributed as .zip files and Apple's servers support range requests with a bit of python and the [partialzip](https://github.com/marcograss/partialzip) tool we can relatively easily and quickly get every beta and release DCP firmware. I checked over 300 distinct images; every single one was stripped.

Guess we'll have to do this the hard way!

## Day 1; Instruction 1

$ otool -h raw\_fw/iphone13dcp


raw\_fw/iphone13dcp:

Mach header

magic cputype cpusubtype caps filetype ncmds sizeofcmds flags

0xfeedfacf 0x100000C 0 0x00 5 5 2240 0x00000001

That cputype is plain arm64 (ArmV8) without pointer authentication support. The binary is fairly large (3.7MB) and IDA's autoanalysis detects over 7000 functions.

With any brand new binary I usually start with a brief look through the function names and the strings. The binary is stripped so there are no function name symbols but there are plenty of C++ function names as strings:

The cross-references to those strings look like this:

| log(0x40000001LL, "UPBlock\_ALSS.cpp", 341, "%s: capture buffer exhausted, aborting capture\n", "void IOMFB::UPBlock\_ALSS::send\_data(uint64\_t, uint32\_t)"); | 

This is almost certainly a logging macro which expands \_\_FILE\_\_, \_\_LINE\_\_ and \_\_PRETTY\_FUNCTION\_\_. This allows us to start renaming functions and finding vtable pointers.

## Object structure

From the Asahi linux blog posts we know that the DCP is using an Apple-proprietary RTOS called RTKit for which there is very little public information. There are some strings in the binary with the exact version:

ADD X8, X8, #aLocalIphone13d@PAGEOFF ; "local-iphone13dcp.release"

ADD X9, X9, #aRtkitIos182640@PAGEOFF ; "RTKit\_iOS-1826.40.9.debug"

The code appears to be predominantly C++. There appear to be multiple C++ object hierarchies; those involved with this vulnerability look a bit like IOKit C++ objects. Their common base class looks like this:

| struct \_\_cppobj RTKIT\_RC\_RTTI\_BASE { RTKIT\_RC\_RTTI\_BASE\_vtbl \*\_\_vftable /\*VFT\*/; uint32\_t refcnt; uint32\_t typeid; }; | 

(These structure definitions are in the format IDA uses for C++-like objects)

The RTKit base class has a vtable pointer, a reference count and a four-byte Run Time Type Information (RTTI) field - a 4-byte ASCII identifier like BLHA, WOLO, MMAP, UNPI, OSST, OSBO and so on. These identifiers look a bit cryptic but they're quite descriptive once you figure them out (and I'll describe the relevant ones as we encounter them.)

The base type has the following associated vtable:

| struct /\*VFT\*/ RTKIT\_RC\_RTTI\_BASE\_vtbl { void (\_\_cdecl \*take\_ref)(RTKIT\_RC\_RTTI\_BASE \*this); void (\_\_cdecl \*drop\_ref)(RTKIT\_RC\_RTTI\_BASE \*this); void (\_\_cdecl \*take\_global\_type\_ref)(RTKIT\_RC\_RTTI\_BASE \*this); void (\_\_cdecl \*drop\_global\_type\_ref)(RTKIT\_RC\_RTTI\_BASE \*this); void (\_\_cdecl \*getClassName)(RTKIT\_RC\_RTTI\_BASE \*this); void (\_\_cdecl \*dtor\_a)(RTKIT\_RC\_RTTI\_BASE \*this); void (\_\_cdecl \*unk)(RTKIT\_RC\_RTTI\_BASE \*this); }; | 

## Exploit flow

The exploit running in the app starts by opening an IOKit user client for the AppleCLCD2 service. AppleCLCD seems to be the application processor of IOMobileFrameBuffer and AppleCLCD2 the DCP version.

The exploit only calls 3 different external method selectors on the AppleCLCD2 user client: 68, 78 and 79.

The one with the largest and most interesting-looking input is 78, which corresponds to this user client method in the kernel driver:

| IOReturn IOMobileFramebufferUserClient::s\_set\_block( IOMobileFramebufferUserClient \*this, void \*reference, IOExternalMethodArguments \*args) { const unsigned \_\_int64 \*extra\_args; u8 \*structureInput; structureInput = args->structureInput; if ( structureInput && args->scalarInputCount >= 2 ) { if ( args->scalarInputCount == 2 ) extra\_args = 0LL; else extra\_args = args->scalarInput + 2; return this->framebuffer\_ap->set\_block\_dcp( this->task, args->scalarInput\[0\], args->scalarInput\[1\], extra\_args, args->scalarInputCount - 2, structureInput, args->structureInputSize); } else { return 0xE00002C2; } } | 

this unpacks the IOConnectCallMethod arguments and passes them to:

| IOMobileFramebufferAP::set\_block\_dcp( IOMobileFramebufferAP \*this, task \*task, int first\_scalar\_input, int second\_scalar\_input, const unsigned \_\_int64 \*pointer\_to\_remaining\_scalar\_inputs, unsigned int scalar\_input\_count\_minus\_2, const unsigned \_\_int8 \*struct\_input, unsigned \_\_int64 struct\_input\_size) | 

This method uses some autogenerated code to serialise the external method arguments into a buffer like this:

| arg\_struct: { struct task\* task u64 scalar\_input\_0 u64 scalar\_input\_1 u64\[\] remaining\_scalar\_inputs u64 cntExtraScalars u8\[\] structInput u64 CntStructInput } | 

which is then passed to UnifiedPipeline2::rpc along with a 4-byte ASCII method identifier ('A435' here):

| UnifiedPipeline2::rpc( 'A435', arg\_struct, 0x105Cu, &retval\_buf, 4u); | 

UnifiedPipeline2::rpc calls DCPLink::rpc which calls AppleDCPLinkService::rpc to perform one more level of serialisation which packs the method identifier and a "stream identifier" together with the arg\_struct shown above.

AppleDCPLinkService::rpc then calls rpc\_caller\_gated to allocate space in a shared memory buffer, copy the buffer into there then signal to the DCP that a message is available.

Effectively the implementation of the IOMobileFramebuffer user client has been moved on to the DCP and the external method interface is now a proxy shim, via shared memory, to the actual implementations of the external methods which run on the DCP.

## Exploit flow: the other side

The next challenge is to find where the messages start being processed on the DCP. Looking through the log strings there's a function which is clearly called rpc\_callee\_gated - quite likely that's the receive side of the function rpc\_caller\_gated we saw earlier.

rpc\_callee\_gated unpacks the wire format then has an enormous switch statement which maps all the 4-letter RPC codes to function pointers:

| switch ( rpc\_id ) { case 'A000': goto LABEL\_146; case 'A001': handler\_fptr = callback\_handler\_A001; break; case 'A002': handler\_fptr = callback\_handler\_A002; break; case 'A003': handler\_fptr = callback\_handler\_A003; break; case 'A004': handler\_fptr = callback\_handler\_A004; break; case 'A005': handler\_fptr = callback\_handler\_A005; break; | 

At the the bottom of this switch statement is the invocation of the callback handler:

| ret = handler\_fptr( meta, in\_struct\_ptr, in\_struct\_size, out\_struct\_ptr, out\_struct\_size); | 

in\_struct\_ptr points to a copy of the serialised IOConnectCallMethod arguments we saw being serialized earlier on the application processor:

| arg\_struct: { struct task\* task u64 scalar\_input\_0 u64 scalar\_input\_1 u64\[\] remaining\_scalar\_inputs u32 cntExtraScalars u8\[\] structInput u64 cntStructInput } | 

The callback unpacks that buffer and calls a C++ virtual function:

| unsigned int callback\_handler\_A435( u8\* meta, void \*args, uint32\_t args\_size, void \*out\_struct\_ptr, uint32\_t out\_struct\_size { int64 instance\_id; uint64\_t instance; int err; int retval; unsigned int result; instance\_id = meta->instance\_id; instance = global\_instance\_table\[instance\_id\].IOMobileFramebufferType; if ( !instance ) { log\_fatal( "IOMFB: %s: no instance for instance ID: %u\n", "static T \*IOMFB::InstanceTracker::instance" "(IOMFB::InstanceTracker::tracked\_entity\_t, uint32\_t)" " \[T = IOMobileFramebuffer\]", instance\_id); } err = (instance-16)->vtable\_0x378( // virtual call (instance-16), args->task, args->scalar\_input\_0, args->scalar\_input\_1, args->remaining\_scalar\_inputs, args->cntExtraScalars, args->structInput, args->cntStructInput); retval = convert\_error(err); result = 0; \*(\_DWORD \*)out\_struct\_ptr = retval; return result; } | 

The challenge here is to figure out where that virtual call goes. The object is being looked up in a global table based on the instance id. We can't just set a breakpoint and whilst emulating the firmware is probably possible that would likely be a long project in itself. I took a hackier approach: we know that the vtable needs to be at least 0x380 bytes large so just go through all those vtables, decompile them and see if the prototypes look reasonable!

There's one clear match in the vtable for the UNPI type:

| UNPI::set\_block( UNPI\* this, struct task\* caller\_task\_ptr, unsigned int first\_scalar\_input, int second\_scalar\_input, int \*remaining\_scalar\_inputs, uint32\_t cnt\_remaining\_scalar\_inputs, uint8\_t \*structure\_input\_buffer, uint64\_t structure\_input\_size) | 

Here's my reversed implementation of UNPI::set\_block

| UNPI::set\_block( UNPI\* this, struct task\* caller\_task\_ptr, unsigned int first\_scalar\_input, int second\_scalar\_input, int \*remaining\_scalar\_inputs, uint32\_t cnt\_remaining\_scalar\_inputs, uint8\_t \*structure\_input\_buffer, uint64\_t structure\_input\_size) { struct block\_handler\_holder \*holder; struct metadispatcher metadisp; if ( second\_scalar\_input ) return 0x80000001LL; holder = this->UPPipeDCP\_H13P->block\_handler\_holders; if ( !holder ) return 0x8000000BLL; metadisp.address\_of\_some\_zerofill\_static\_buffer = &unk\_3B8D18; metadisp.handlers\_holder = holder; metadisp.structure\_input\_buffer = structure\_input\_buffer; metadisp.structure\_input\_size = structure\_input\_size; metadisp.remaining\_scalar\_inputs = remaining\_scalar\_inputs; metadisp.cnt\_remaining\_sclar\_input = cnt\_remaining\_scalar\_inputs; metadisp.some\_flags = 0x40000000LL; metadisp.dispatcher\_fptr = a\_dispatcher; metadisp.offset\_of\_something\_which\_looks\_serialization\_related = &off\_1C1308; return metadispatch(holder, first\_scalar\_input, 1, caller\_task\_ptr, structure\_input\_buffer, &metadisp, 0); } | 

This method wraps up the arguments into another structure I've called metadispatcher:

| struct \_\_attribute\_\_((aligned(8))) metadispatcher { uint64\_t address\_of\_some\_zerofill\_static\_buffer; uint64\_t some\_flags; \_\_int64 (\_\_fastcall \*dispatcher\_fptr)(struct metadispatcher \*, struct BlockHandler \*, \_\_int64, \_QWORD); uint64\_t offset\_of\_something\_which\_looks\_serialization\_related; struct block\_handler\_holder \*handlers\_holder; uint64\_t structure\_input\_buffer; uint64\_t structure\_input\_size; uint64\_t remaining\_scalar\_inputs; uint32\_t cnt\_remaining\_sclar\_input; }; | 

That metadispatcher object is then passed to this method:

| return metadispatch(holder, first\_scalar\_input, 1, caller\_task\_ptr, structure\_input\_buffer, &metadisp, 0); | 

In there we reach this code:

| block\_type\_handler = lookup\_a\_handler\_for\_block\_type\_and\_subtype( a1, first\_scalar\_input, // block\_type a3); // subtype | 

The exploit calls this set\_block external method twice, passing two different values for first\_scalar\_input, 7 and 19. Here we can see that those correspond to looking up two different block handler objects here.

The lookup function searches a linked list of block handler structures; the head of the list is stored at offset 0x1448 in the UPPipeDCP\_H13P object and registered dynamically by a method I've named add\_handler\_for\_block\_type:

| add\_handler\_for\_block\_type(struct block\_handler\_holder \*handler\_list, struct BlockHandler \*handler) | 


The logging code tells us that this is in a file called IOMFBBlockManager.cpp. IDA finds 44 cross-references to this method, indicating that there are probably that many different block handlers. The structure of each registered block handler is something like this:

| struct \_\_cppobj BlockHandler : RTKIT\_RC\_RTTI\_BASE { uint64\_t field\_16; struct handler\_inner\_types\_entry \*inner\_types\_array; uint32\_t n\_inner\_types\_array\_entries; uint32\_t field\_36; uint8\_t can\_run\_without\_commandgate; uint32\_t block\_type; uint64\_t list\_link; uint64\_t list\_other\_link; uint32\_t some\_other\_type\_field; uint32\_t some\_other\_type\_field2; uint32\_t expected\_structure\_io\_size; uint32\_t field\_76; uint64\_t getBlock\_Impl; uint64\_t setBlock\_Impl; uint64\_t field\_96; uint64\_t back\_ptr\_to\_UPPipeDCP\_H13P; }; | 

The RTTI type is BLHA (BLock HAndler.)

For example, here's the codepath which builds and registers block handler type 24:

| BLHA\_24 = (struct BlockHandler \*)CXXnew(112LL); BLHA\_24->\_\_vftable = (BlockHandler\_vtbl \*)BLHA\_super\_vtable; BLHA\_24->block\_type = 24; BLHA\_24->refcnt = 1; BLHA\_24->can\_run\_without\_commandgate = 0; BLHA\_24->some\_other\_type\_field = 0LL; BLHA\_24->expected\_structure\_io\_size = 0xD20; typeid = typeid\_BLHA(); BLHA\_24->typeid = typeid; modify\_typeid\_ref(typeid, 1); BLHA\_24->\_\_vftable = vtable\_BLHA\_subclass\_type\_24; BLHA\_24->inner\_types\_array = 0LL; BLHA\_24->n\_inner\_types\_array\_entries = 0; BLHA\_24->getBlock\_Impl = BLHA\_24\_getBlock\_Impl; BLHA\_24->setBlock\_Impl = BLHA\_24\_setBlock\_Impl; BLHA\_24->field\_96 = 0LL; BLHA\_24->back\_ptr\_to\_UPPipeDCP\_H13P = a1; add\_handler\_for\_block\_type(list\_holder, BLHA\_24); | 

Each block handler optionally has getBlock\_Impl and setBlock\_Impl function pointers which appear to implement the actual setting and getting operations.

We can go through all the callsites which add block handlers; tell IDA the type of the arguments and name all the getBlock and setBlock implementations:

You can perhaps see where this is going: that's looking like really quite a lot of reachable attack surface! Each of those setBlock\_Impl functions is reachable by passing a different value for the first scalar argument to IOConnectCallMethod 78.

There's a little bit more reversing though to figure out how exactly to get controlled bytes to those setBlock\_Impl functions:

## Memory Mapping

The raw "block" input to each of those setBlock\_Impl methods isn't passed inline in the IOConnectCallMethod structure input. There's another level of indirection: each individual block handler structure has an array of supported "subtypes" which contains metadata detailing where to find the (userspace) pointer to that subtype's input data in the IOConnectCallMethod structure input. The first dword in the structure input is the id of this subtype - in this case for the block handler type 19 the metadata array has a single entry:

\<2, 0, 0x5F8, 0x600>

The first value (2) is the subtype id and 0x5f8 and 0x600 tell the DCP from what offset in the structure input data to read a pointer and size from. The DCP then requests a memory mapping from the AP for that memory from the calling task:

| return wrap\_MemoryDescriptor::withAddressRange( \*(void\*)(structure\_input\_buffer + addr\_offset), \*(unsigned int \*)(structure\_input\_buffer + size\_offset), caller\_task\_ptr); | 

We saw earlier that the AP sends the DCP the struct task pointer of the calling task; when the DCP requests a memory mapping from a user task it sends those raw task struct pointers back to the AP such that the kernel can perform the mapping from the correct task. The memory mapping is abstracted as an MDES object on the DCP side; the implementation of the mapping involves the DCP making an RPC to the AP:

| make\_link\_call('D453', &req, 0x20, &resp, 0x14); | 

which corresponds to a call to this method on the AP side:

| IOMFB::MemDescRelay::withAddressRange(unsigned long long, unsigned long long, unsigned int, task\*, unsigned long\*, unsigned long long\*) | 

The DCP calls ::prepare and ::map on the returned MDES object (exactly like an IOMemoryDescriptor object in IOKit), gets the mapped pointer and size to pass via a few final levels of indirection to the block handler:

| a\_descriptor\_with\_controlled\_stuff->dispatcher\_fptr( a\_descriptor\_with\_controlled\_stuff, block\_type\_handler, important\_ptr, important\_size); | 

where the dispatcher\_fptr looks like this:

| a\_dispatcher( struct metadispatcher \*disp, struct BlockHandler \*block\_handler, \_\_int64 controlled\_ptr, unsigned int controlled\_size) { return block\_handler->BlockHandler\_setBlock( block\_handler, disp->structure\_input\_buffer, disp->structure\_input\_size, disp->remaining\_scalar\_inputs, disp->cnt\_remaining\_sclar\_input, disp->handlers\_holder->gate, controlled\_ptr, controlled\_size); } | 

You can see here just how useful it is to keep making structure definitions while reversing; there are so many levels of indirection that it's pretty much impossible to keep it all in your head.

BlockHandler\_setBlock is a virtual method on BLHA. This is the implementation for BLHA 19:

| BlockHandler19::setBlock( struct BlockHandler \*this, void \*structure\_input\_buffer, int64 structure\_input\_size, int64 \*remaining\_scalar\_inputs, unsigned int cnt\_remaining\_scalar\_inputs, struct CommandGate \*gate, void\* mapped\_mdesc\_ptr, unsigned int mapped\_mdesc\_length) | 

This uses a Command Gate (GATI) object (like a call gate in IOKit to serialise calls) to finally get close to actually calling the setBlock\_Impl function.

We need to reverse the gate\_context structure to follow the controlled data through the gate:

| struct \_\_attribute\_\_((aligned(8))) gate\_context { struct BlockHandler \*the\_target\_this; uint64\_t structure\_input\_buffer; void \*remaining\_scalar\_inputs; uint32\_t cnt\_remaining\_scalar\_inputs; uint32\_t field\_28; uint64\_t controlled\_ptr; uint32\_t controlled\_length; }; | 

The callgate object uses that context object to finally call the BLHA setBlock handler:

| callback\_used\_by\_callgate\_in\_block\_19\_setBlock( struct UnifiedPipeline \*parent\_pipeline, struct gate\_context \*context, int64 a3, int64 a4, int64 a5) { return context->the\_target\_this->setBlock\_Impl)( context->the\_target\_this->back\_ptr\_to\_UPPipeDCP\_H13P, context->structure\_input\_buffer, context->remaining\_scalar\_inputs, context->cnt\_remaining\_scalar\_inputs, context->controlled\_ptr, context->controlled\_length); } | 

## SetBlock\_Impl

And finally we've made it through the whole callstack following the controlled data from IOConnectCallMethod in userspace on the AP to the setBlock\_Impl methods on the DCP!

The prototype of the setBlock\_Impl methods looks like this:

| setBlock\_Impl(struct UPPipeDCP\_H13P \*pipe\_parent, void \*structure\_input\_buffer, int \*remaining\_scalar\_inputs, int cnt\_remaining\_scalar\_inputs, void\* ptr\_via\_memdesc, unsigned int len\_of\_memdesc\_mapped\_buf) | 

The exploit calls two setBlock\_Impl methods; 7 and 19. 7 is fairly simple and seems to just be used to put controlled data in a known location. 19 is the buggy one. From the log strings we can tell that block type 19 handler is implemented in a file called UniformityCompensator.cpp.

[Uniformity Compensation](https://www.benq.com/en-us/knowledge-center/knowledge/screen-uniformity.html) is a way to correct for inconsistencies in brightness and colour reproduction across a display panel. Block type 19 sets and gets a data structure containing this correction information. The setBlock\_Impl method calls UniformityCompensator::set and reaches the following code snippet where controlled\_size is a fully-controlled u32 value read from the structure input and indirect\_buffer\_ptr points to the mapped buffer, the contents of which are also controlled:

| uint8\_t\* pages = compensator->inline\_buffer; // +0x24 for (int pg\_cnt = 0; pg\_cnt \< 3; pg\_cnt++) { uint8\_t\* this\_page = pages; for (int i = 0; i \< controlled\_size; i++) { memcpy(this\_page, indirect\_buffer\_ptr, 4 \* controlled\_size); indirect\_buffer\_ptr += 4 \* controlled\_size; this\_page += 0x100; } pages += 0x4000; } | 


There's a distinct lack of bounds checking on controlled\_size. Based on the structure of the code it looks like it should be restricted to be less than or equal to 64 (as that would result in the input being completely copied to the output buffer.) The compensator->inline\_buffer buffer is inline in the compensator object. The structure of the code makes it look that that buffer is probably 0xc000 (three 16k pages) large. To verify this we need to find the allocation site of this compensator object.

It's read from the pipe\_parent object and we know that at this point pipe\_parent is a UPPipeDCP\_H13P object.

There's only one write to that field, here in UPPipeDCP\_H13P::setup\_tunables\_base\_target:

| compensator = CXXnew(0xC608LL); ... this->compensator = compensator; | 

The compensator object is a 0xc608 byte allocation; the 0xc000 sized buffer starts at offset 0x24 so the allocation has enough space for 0xc608-0x24=0xC5E4 bytes before corrupting neighbouring objects.

The structure input provided by the exploit for the block handler 19 setBlock call looks like this:

| struct\_input\_for\_block\_handler\_19\[0x5F4\] = 70; // controlled\_size struct\_input\_for\_block\_handler\_19\[0x5F8\] = address; struct\_input\_for\_block\_handler\_19\[0x600\] = a\_size; | 

This leads to a value of 70 (0x46) for controlled\_size in the UniformityCompensator::set snippet shown earlier. (0x5f8 and 0x600 correspond to the offsets we saw earlier in the subtype's table: \<2, 0, 0x5F8, 0x600>)

The inner loop increments the destination pointer by 0x100 each iteration so 0x46 loop iterations will write 0x4618 bytes.

The outer loop writes to three subsequent 0x4000 byte blocks so the third (final) iteration starts writing at 0x24 + 0x8000 and writes a total of 0x4618 bytes, meaning the object would need to be 0xC63C bytes; but we can see that it's only 0xc608, meaning that it will overflow the allocation size by 0x34 bytes. The RTKit malloc implementation looks like it adds 8 bytes of metadata to each allocation so the next object starts at 0xc610.

How much input is consumed? The input is fully consumed with no "rewinding" so it's 3\*0x46\*0x46\*4 = 0xe5b0 bytes. Working backwards from the end of that buffer we know that the final 0x34 bytes of it go off the end of the 0xc608 allocation which means +0xe57c in the input buffer will be the first byte which corrupts the 8 metadata bytes and +0x8584 will be the first byte to corrupt the next object:

This matches up exactly with the overflow object which the exploit builds:

| v24 = address + 0xE584; v25 = \*(\_DWORD \*)&v54\[48\]; v26 = \*(\_OWORD \*)&v54\[32\]; v27 = \*(\_OWORD \*)&v54\[16\]; \*(\_OWORD \*)(address + 0xE584) = \*(\_OWORD \*)v54; \*(\_OWORD \*)(v24 + 16) = v27; \*(\_OWORD \*)(v24 + 32) = v26; \*(\_DWORD \*)(v24 + 48) = v25; | 

The destination object seems to be allocated very early and the DCP RTKit environment appears to be very deterministic with no ASLR. Almost certainly they are attempting to corrupt a neighbouring C++ object with a fake vtable pointer.

Unfortunately for our analysis the trail goes cold here and we can't fully recreate the rest of the exploit. The bytes for the fake DCP C++ object are read from a file in the app's temporary directory (base64 encoded inside a JSON file under the exploit\_struct\_offsets key) and I don't have a copy of that file. But based on the flow of the rest of the exploit it's pretty clear what happens next:

## sudo make me a DART mapping

The DCP, like other coprocessors on iPhone, sits behind a DART (Device Address Resolution Table.) This is like an SMMU (IOMMU in the x86 world) which forces an extra layer of physical address lookup between the DCP and physical memory. [DART was covered in great detail in Gal Beniamini's Over The Air - Vol. 2, Pt. 3 blog post](/2017/10/over-air-vol-2-pt-3-exploiting-wi-fi.html).

The DCP clearly needs to access lots of buffers owned by userspace tasks as well as memory managed by the kernel. To do this the DCP makes RPC calls back to the AP which modifies the DART entries accordingly. This appears to be exactly what the DCP exploit does: the D45X family of DCP->AP RPC methods appear to expose an interface for requesting arbitrary physical as well as virtual addresses to be mapped into the DCP DART.

The fake C++ object is most likely a stub which makes such calls on behalf of the exploit, allowing the exploit to read and write kernel memory.

## Conclusions

Segmentation and isolation are in general a positive thing when it comes to security. However, splitting up an existing system into separate, intercommunicating parts can end up exposing unexpected code in unexpected ways.

We've had discussions within Project Zero about whether this DCP vulnerability is interesting at all. After all, if the UniformityCompensator code was going to be running on the Application Processors anyway then the Display Co-Processor didn't really introduce or cause this bug.

Whilst that's true, it's also the case that the DCP certainly made exploitation of this bug significantly easier and more reliable than it would have been on the AP. Apple has invested heavily in memory corruption mitigations over the last few years, so moving an attack surface from a "mitigation heavy" environment to a "mitigation light" one is a regression in that sense.

Another perspective is that the DCP just isn't isolated enough; perhaps the intention was to try to isolate the code on the DCP such that even if it's compromised it's limited in the effect it could have on the entire system. For example, there might be models where the DCP to AP RPC interface is much more restricted.

But again there's a tradeoff: the more restrictive the RPC API, the more the DCP code has to be refactored - a significant investment. Currently, the codebase relies on being able to map arbitrary memory and the API involves passing userspace pointers back and forth.

I've discussed in recent posts how attackers tend to be ahead of the curve. As the curve slowly shifts towards memory corruption exploitation getting more expensive, attackers are likely shifting too. We saw that in the [logic-bug sandbox escape used by NSO](/2022/03/forcedentry-sandbox-escape.html) and we see that here in this memory-corruption-based privilege escalation that side-stepped kernel mitigations by corrupting memory on a co-processor instead. Both are quite likely to continue working in some form in a post-memory tagging world. Both reveal the stunning depth of attack surface available to the motivated attacker. And both show that defensive security research still has a lot of work to do.
