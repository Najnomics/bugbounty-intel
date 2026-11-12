# pwn4fun Spring 2014 - Safari - Part II - Project Zero

Source: https://projectzero.google/2014/11/pwn4fun-spring-2014-safari-part-ii.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Ian Beer

## TL;DR

An OS X GPU driver trusted a user-supplied kernel C++ object pointer and called a virtual function. The IOKit registry contained kernel pointers which were used defeat kASLR. A kernel ROP payload ran Calculator.app as root using a convenient kernel API.



## Overview of part I

We finished [part I](/2014/07/pwn4fun-spring-2014-safari-part-i_24.html) with the ability to load our own native library into the Safari renderer process on OS X by exploiting an integer truncation bug in the Safari javascript engine. Here in part II we’ll take a look at how sandboxing works on OS X, revise some OS X fundamentals and then exploit two kernel bugs to launch Calculator.app running as root from inside the Safari sandbox.



## Safari process model

Safari’s sandboxing model is based on privilege separation. It uses the [WebKit2](https://trac.webkit.org/wiki/WebKit2) framework to communicate between multiple separate processes which collectively form the Safari browser. Each of these processes is responsible for a different part of the browser and sandboxed to only allow access to the system resources it requires.

Specifically Safari is split into four distinct process families:

- WebProcesses are the renderers - they’re responsible for actually drawing web pages as well as dealing with most active web content such as javascript
- NetworkProcess is the process which talks to the network
- PluginProcesses are the processes which host native plugins like Adobe Flash
- UIProcess is the unsandboxed parent of all the other processes and is responsible for coordinating the activity of the sandboxed processes such that a webpage is actually displayed to the user which they can interact with

The Web, Network and Plugin process families are sandboxed. In order to understand how to break out of the WebProcess that we find ourselves in we’ve first got to understand how this sandbox is implemented.



## OS X sandboxing primitives

OS X uses the [Mandatory Access Control](https://en.wikipedia.org/wiki/Mandatory_access_control) (MAC) paradigm to implement sandboxing, specifically it uses the [TrustedBSD](http://www.trustedbsd.org/mac.html) framework. Use of the MAC sandboxing paradigm implies that whenever a sandboxed process tries to acquire access to some system resource, for example by opening a file or creating a network socket, the OS will first check: Does this particular process have the right to do this?

An implementation of sandboxing using TrustedBSD has two parts: firstly, hooks must be added to the kernel code wherever a sandboxing decision is required. A TrustedBSD hook looks like this:



/\* bsd/kern/uipc\_syscalls.c \*/

int socket(struct proc \*p, struct socket\_args \*uap, int32\_t \*retval)

{

#if CONFIG\_MACF\_SOCKET\_SUBSET

if ((error = mac\_socket\_check\_create(kauth\_cred\_get(), uap->domain,

uap->type, uap->protocol)) != 0)

return (error);

#endif /\* MAC\_SOCKET\_SUBSET \*/

...



That snippet of code is from the implementation of the socket syscall on OS X. If MAC support has been enabled at compile time then the very first thing the socket syscall implementation will do is call mac\_socket\_check\_create, passing the credentials of the calling processes and the domain, type and protocol of the requested socket:



/\* security/mac\_socket.h \*/

int mac\_socket\_check\_create(kauth\_cred\_t cred, int domain, int type, int protocol)

{

int error;

if (!mac\_socket\_enforce)

return 0;

MAC\_CHECK(socket\_check\_create, cred, domain, type, protocol);

return (error);

}



Here we see that if the enforcement of MAC on sockets hasn’t been globally disabled (mac\_socket\_enforce is a variable exposed by the sysctl interface) then this function falls through to the MAC\_CHECK macro:



/\* security/mac\_internal.h \*/

#define MAC\_CHECK(check, args...) do {              \

for (i = 0; i \< mac\_policy\_list.staticmax; i++) {  \

mpc = mac\_policy\_list.entries\[i\].mpc;             \

...

if (mpc->mpc\_ops->mpo\_ ## check != NULL)          \

error = mac\_error\_select(                        \

mpc->mpc\_ops->mpo\_ ## check (args),          \

error);



This macro is the core of TrustedBSD. mac\_policy\_list.entries (the first highlighted chunk) is a list of policies and the second highlighted chuck is TrustedBSD consulting the policy. In actual fact a policy is nothing more than a C struct (struct policy\_ops) containing function pointers (one per hook type) and consultation of a policy simply means calling the right function pointer in that struct.

If that policy function returns 0 (or isn’t implemented at all by the policy) then the MAC check succeeds. If the policy function returns a non-zero value then the MAC check fails and, in the case of this socket hook, the syscall will fail passing the error code back up to userspace and the rest of the socket syscall won’t be executed.

The second part of an implementation of sandboxing using TrustedBSD is the provision of these policy modules. Although TrustedBSD allows multiple policy modules to be present at the same time in practice on OS X there’s only one and it’s implemented in its own kernel extension: Sandbox.kext. When it's loaded Sandbox.kext registers itself as a policy with TrustedBSD by passing a pointer to its policy\_ops structure. TrustedBSD adds this to the mac\_policy\_list.entries array seen earlier and will then call into Sandbox.kext whenever a sandboxing decision is required.



## Sandbox.kext and the OS X sandbox policy\_ops

[This](http://reverse.put.as/wp-content/uploads/2011/06/The-Apple-Sandbox-BHDC2011-Paper.pdf)paper from Dionysus Blazakis,

[this](http://2013.zeronights.org/includes/docs/Meder_Kydyraliev_-_Mining_Mach_Services_within_OS_X_Sandbox.pdf)talk from Meder Kydyraliev and

[this](http://reverse.put.as/wp-content/uploads/2011/09/Apple-Sandbox-Guide-v1.0.pdf)reference from

[@osxreverser](https://twitter.com/osxreverser)go into great detail about Sandbox.kext and its operation and usage.

Summarizing those linked resources, every process can have a unique sandbox profile. For (almost) every MAC hook type Sandbox.kext allows a sandbox profile to specify a decision tree to be used to determine whether the MAC check should pass or fail. This decision tree is expressed in a simple scheme-like DSL built from tuples of actions, operations and filters (for a more complete guide to the syntax refer to the linked docs):



(action operation filter)

- Actions determine whether a particular rule corresponds to passing or failing the MAC check. Actions are the literals allow and deny.
- Operations define which MAC hooks this rule applies to. For example the file-read operation allows restricting read access to files.
- Filters allow a more granular application of operations, for example a filter applied to the file-read operation could define a specific file which is or isn’t allowed.

Here’s a snippet from the WebProcess sandbox profile to illustrate that:



(deny default (with partial-symbolication))

...

(allow file-read\*

;; Basic system paths

(subpath "/Library/Dictionaries")

(subpath "/Library/Fonts")

(subpath "/Library/Frameworks")

(subpath "/Library/Managed Preferences")

(subpath "/Library/Speech/Synthesizers")

(regex #"^/private/etc/(hosts|group|passwd)$")

...

)



As you can see sandbox profiles are very readable on OS X. It’s usually quite clear what any particular sandbox profile allows and denies. In this example the profile is using regular expressions to define allowed file paths (there’s a small regex matching engine in the kernel in AppleMatch.kext.)

Sandbox.kext also has a mechanism which allows userspace programs to ask for policy decisions. The main use of this is to restrict access to system IPC services, access to which isn’t mediated by the kernel (so there’s nowhere to put a MAC hook) but by the userspace daemon launchd.

## Enumerating the attack surface of a sandboxed process

## Broadly speaking there are two aspects to consider when enumerating the attack surface reachable from within a particular sandbox on OS X:

- Actions which are specifically allowed by the sandbox policy - these are easy to enumerate by looking at the sandbox policy files.
- Those actions which are allowed because either because the Sandbox.kext policy\_ops doesn’t implement the hook callback or because there’s no hook in place at all.

The Safari WebProcess sandbox profile is located here:

/System/Library/StagedFrameworks/Safari/WebKit.framework/Versions/A/Resources/com.apple.WebProcess.sb

This profile uses an import statement to load the contents of  /System/Library/Sandbox/Profiles/system.sb which uses the define statement to declare various broad sandboxing rulesets which define all the rules required to use complete OS X subsystems such as graphics or networking. Amongst others the Webprocess.sb profile uses (system-graphics) which is defined here in system.sb:



(define (system-graphics)

...

(allow iokit-open

(iokit-connection "IOAccelerator")

(iokit-user-client-class "IOAccelerationUserClient")

(iokit-user-client-class "IOSurfaceRootUserClient")

(iokit-user-client-class "IOSurfaceSendRight"))

)

)



This tells us that the WebProcess sandbox has pretty much unrestricted access to the GPU drivers. In order to understand what the iokit-user-client-class actually means and what this gives us access to we have to step back and take a look at the various parts of OS X involved in the operation of device drivers.



## OS X kernel fundamentals


There are two great books I’d recommend to learn more about the OS X kernel: the older but still relevant “[Mac OS X Internals](http://osxbook.com/)” by Amit Singh and the more recent “[Mac OS X and iOS Internals: To the Apple’s Core](http://www.newosxbook.com/index.php)” by Jonathan Levin.

The OS X [wikipedia article](https://en.wikipedia.org/wiki/OS_X) contains a detailed taxonomic discussion of OS X and its place in the [UNIX phylogenetic tree](https://en.wikipedia.org/wiki/File:Unix_timeline.en.svg) but for our purposes it’s sufficient to divide the OS X kernel into three broad subsystems which collectively are known as XNU:

#### BSD


The majority of OS X syscalls are BSD syscalls. The BSD-derived code is responsible for things like file systems and networking.

#### Mach


Originally a [research microkernel from CMU](https://en.wikipedia.org/wiki/Mach_%28kernel%29) mach is responsible for many of the low-level idiosyncrasies of OS X. The mach IPC mechanism is one of the most fundamental parts of OS X but the mach kernel code is also responsible for things like virtual memory management.

Mach only has a handful of dedicated mach syscalls (mach calls them traps) and almost all of these only exist to support the mach IPC system. All further interaction with the mach kernel subsystems from userspace is via mach IPC.

#### IOKit


IOKit is the framework used for writing device drivers on OS X. IOKit code is written in C++ which brings with it a whole host of new bug classes and exploitation possibilities. We'll return to a more detailed discussion of IOKit later.



## Mach IPC

If you want to change the permissions of a memory mapping in your process, talk to a device driver, render a system font, symbolize a crash dump, debug another process or determine the current network connectivity status then on OS X behind the scenes you’re really sending and receiving mach messages. In order to find and exploit bugs in all those things it’s important to understand how mach IPC works:



## Messages, ports and queues

Mach terminology can be a little unclear at times and OS X doesn’t ship with the man pages for the mach APIs (but you can view them online [here](http://web.mit.edu/darwin/src/modules/xnu/osfmk/man/).)

Fundamentally mach IPC is message-oriented protocol. The messages sent via mach IPC are known as mach messages. Sending a mach message really means the message gets enqueued into a kernel-maintained message queue known as a mach port.

Only one process can dequeue messages from a particular port. In mach terminology this process has a receive-right for the port. Multiple processes can enqueue messages to a port - these processes hold send-rights to that port.

Within a process these send and receive rights are called mach port names. A mach port name is used to index a per-process mapping between mach port names and message queues (akin to how a process-local UNIX file descriptor maps to an actual file):


In this diagram we can see that the process with PID 123 has a mach port name 0xabc. It’s important to notice that this Mach port name only has a meaning within this process - we can see that in the kernel structure for this process 0xabc is just a key which maps to a pointer to a message queue.

When the process with PID 456 tries to dequeue a message using the mach port name 0xdef the kernel uses 0xdef to index that process’s map of mach ports such that it can find the correct message queue from which to dequeue a message.



## Mach messages

A single mach message can have up to four parts:

- Message header - this header is mandatory and specifies the port name to send the message to as well as various flags.
- Kernel processed descriptors - this optional section can contain multiple descriptors which are parts of the message which need to be interpreted by the kernel.
- Inline data - this is the inline binary payload.
- Audit trailer - The message receiver can request that the kernel append an audit trailer to received messages.


When a simple mach message containing no descriptors is sent it will first be copied entirely into a kernel heap-allocated buffer in the kernel. A pointer to that copy is then appended to the correct mach message queue and when the process with a receive right to that queue dequeues that message the kernel copy of the message gets copied into the receiving process.



## Out-of-line memory

Copying large messages into and out of the kernel is slow, especially if the messages are large. In order to send large amounts of data you can use the “out-of-line memory” descriptor. This enables the message sender to instruct the kernel to make a copy-on-write virtual memory copy of a buffer in the receiver process when the message is dequeued.



## Bi-directional messages

Mach IPC is fundamentally uni-directional. In order to build a two-way IPC mechanism mach IPC allows for messages to carry port rights. In a mach message, along with binary data you can also send a mach port right.

Mach IPC is quite flexible when it comes to sending port rights to other processes. You can use the local\_port field of the mach message header, use a port descriptor or use an OOL-ports descriptor. There are a multitude of flags to control exactly what rights should be transferred, or if new rights should be created during the send operation (it’s common to use the MAKE\_SEND flag which creates and sends a new send right to a port which you hold the receive right for.)



## Bootstrapping Mach IPC

There’s a fundamental bootstrapping problem with mach IPC: how do you get a send right to a port for which another process has a receive right without first sending them a message (thus encountering the same problem in reverse.)

One way around this could be to allow mach ports to be inherited across a fork() akin to setting up a pipe between a parent and child process using socketpair(). However, unlike file descriptors, mach port rights are not inherited across a fork so you can’t implement such a system.

Except, some mach ports are inherited across a fork! These are the special mach ports, one of which is the bootstrap port. The parent of all processes on OS X is launchd, and one of its roles is to set the default bootstrap port which will then be inherited by every child.



## Launchd

Launchd holds the receive-right to this bootstrap port and plays the role of the bootstrap server, allowing processes to advertise named send-rights which other processes can look up. These are OS X Mach IPC services.



## MIG

We’re now at the point where we can see how the kernel and userspace Mach IPC systems use a few hacks to get bootstrapped such that they’re able to send binary data. This is all that you get with raw Mach IPC.

MIG is the [Mach Interface Generator](https://www.gnu.org/software/hurd/microkernel/mach/mig/gnu_mig.html) and it provides a simple RPC (remote procedure call) layer on top of the raw mach message IPC. MIG is used by all the Mach kernel services and many userspace services.

MIG interfaces are declared in .defs files. These use a simple Interface Definition Language which can define function prototypes and simple data structures. The MIG tool compiles the .defs into C code which implements all the required argument serialization/deserialization.

Calling a MIG RPC is completely transparent, it’s just like calling a regular C function and if you’ve ever programed on a Mac you’ve almost certainly used a MIG generated header file.



## IOKit

As mentioned earlier IOKit is the framework and kernel subsystem used for device drivers. All interactions with IOKit begin with the IOKit master port. This is another special mach port which allows access to the IOKit registry. [devices.defs](http://www.opensource.apple.com/source/xnu/xnu-2782.1.97/osfmk/device/device.defs) is the relevant MIG definition file. The [Apple developer documentation](https://developer.apple.com/library/mac/documentation/devicedrivers/conceptual/IOKitFundamentals/Introduction/Introduction.html) describes the IOKit registry in great detail.

The IOKit registry allows userspace programs to find out about available hardware. Furthermore, device drivers can expose an interface to userspace by implementing a [UserClient](https://developer.apple.com/library/mac/documentation/DeviceDrivers/Conceptual/WritingDeviceDriver/MakingHWAccessible/MakingHWAccessible.html).

The main way which userspace actually interacts with an IOKit driver's UserClient is via the io\_connect\_method MIG RPC:



type io\_scalar\_inband64\_t = array\[\*:16\] of uint64\_t;

type io\_struct\_inband\_t   = array\[\*:4096\] of char;

routine io\_connect\_method(

connection            : io\_connect\_t;

in    selector        : uint32\_t;

in    scalar\_input    : io\_scalar\_inband64\_t;

in    inband\_input    : io\_struct\_inband\_t;

in    ool\_input       : mach\_vm\_address\_t;

in    ool\_input\_size  : mach\_vm\_size\_t;

out   inband\_output   : io\_struct\_inband\_t, CountInOut;

out   scalar\_output   : io\_scalar\_inband64\_t, CountInOut;

in    ool\_output      : mach\_vm\_address\_t;

inout ool\_output\_size : mach\_vm\_size\_t

);



This method is wrapped by the IOKitUser library function IOConnectCallMethod.

The kernel implementation of this MIG API is in IOUserClient.cpp in the function 


is\_io\_connect\_method:

kern\_return\_t is\_io\_connect\_method

(

io\_connect\_t connection,

uint32\_t selector,

io\_scalar\_inband64\_t scalar\_input,

mach\_msg\_type\_number\_t scalar\_inputCnt,

io\_struct\_inband\_t inband\_input,

mach\_msg\_type\_number\_t inband\_inputCnt,

mach\_vm\_address\_t ool\_input,

mach\_vm\_size\_t ool\_input\_size,

io\_struct\_inband\_t inband\_output,

mach\_msg\_type\_number\_t \*inband\_outputCnt,

io\_scalar\_inband64\_t scalar\_output,

mach\_msg\_type\_number\_t \*scalar\_outputCnt,

mach\_vm\_address\_t ool\_output,

mach\_vm\_size\_t \*ool\_output\_size

)

{

CHECK( IOUserClient, connection, client );

IOExternalMethodArguments args;

...

args.selector = selector;

args.scalarInput = scalar\_input;

args.scalarInputCount = scalar\_inputCnt;

args.structureInput = inband\_input;

args.structureInputSize = inband\_inputCnt;

...

args.scalarOutput = scalar\_output;

args.scalarOutputCount = \*scalar\_outputCnt;

args.structureOutput = inband\_output;

args.structureOutputSize = \*inband\_outputCnt;

...

ret = client->externalMethod( selector, &args );



Here we can see that the code fills in an IOExternalMethodArguments structure from the arguments passed to the MIG RPC and then calls the ::externalMethod method of the IOUserClient.

What happens next depends on the structure of the driver’s IOUserClient subclass. If the driver overrides externalMethod then this calls straight into driver code. Typically the selector argument to IOConnectCallMethod would be used to determine what function to call, but if the subclass overrides externalMethod it’s free to implement whatever method dispatch mechanism it wants. However if the driver subclass doesn’t override externalMethod the IOUserClient implementation of it will call getTargetAndMethodForIndex passing the selector argument - this is the method which most IOUserClient subclasses override - it returns a pointer to an IOExternalMethod structure:



struct IOExternalMethod {

IOService \*  object;

IOMethod     func;

IOOptionBits flags;

IOByteCount  count0;

IOByteCount  count1;

};



Most drivers have a simple implementation of getTargetAndMethodForType which uses the selector argument to index an array of IOExternalMethod structures. This structure contains a pointer to the method to be invoked (and since this is C++ this isn’t actually a function pointer but a pointer-to-member-method which means things can get very fun when you get to control it! See the bug report for [CVE-2014-1379](https://code.google.com/p/google-security-research/issues/detail?id=20) in the Project Zero bugtracker for an example of this.)

The flags member is used to define what mixture of input and output types the ExternalMethod supports and the count0 and count1 fields define the number or size in bytes of the input and output arguments. There are various shim functions which make sure that func is called with the correct prototype depending on the declared number and type of arguments.



## Putting all that together

At this point we know that when we call IOConnectCallMethod what really happens is that C code auto-generated by MIG serializes all the arguments into a data buffer which is wrapped in a mach message which is sent to a mach port we received received from the IOKit registry which we knew how to talk to because every process has a special device port. That message gets copied into the kernel where more MIG generated C code deserializes it and calls is\_io\_connect\_method which calls the driver’s externalMethod virtual method.



## Writing an IOKit fuzzer

When auditing code alongside manual analysis it’s often worth writing a fuzzer. As soon as you’ve understood where attacker-controlled data could enter a system you can write a simple piece of code to throw randomness at it. As your knowledge of the code improves you can make incremental improvements to the fuzzer, allowing it to explore the code more deeply.

IOConnectCallMethod is the perfect example of a API where this applies. It’s very easy to write a simple fuzzer to make random IOConnectCallMethod calls. One approach to slightly improve on just using randomness is to try to mutate real data. In this case, we want to mutate valid arguments to IOConnectCallMethod. Check out [this](http://www.slideshare.net/inggmartinez/find-your-own-ios-kernel-bug) talk from Chen Xiaobo and Xu Hao about how to do exactly that.



## DYLD interposing

dyld is the OS X dynamic linker. Similar to using LD\_PRELOAD on linux dyld supports dynamic link time interposition of functions. This means we can intercept function calls between different libraries and inspect and modify arguments.

Here’s the complete IOConnectCallMethod fuzzer interpose library I wrote for pwn4fun:



#include \<stdint.h>

#include \<stdio.h>

#include \<stdlib.h>

#include \<time.h>

#include \<IOKit/IOKitLib.h>

int maybe(){

static int seeded = 0;

if(!seeded){

srand(time(NULL));

seeded = 1;

}

return !(rand() % 100);

}

void flip\_bit(void\* buf, size\_t len){

if (!len)

return;

size\_t offset = rand() % len;

((uint8\_t\*)buf)\[offset\] ^= (0x01 \<\< (rand() % 8));

}

kern\_return\_t

fake\_IOConnectCallMethod(

mach\_port\_t connection,

uint32\_t    selector,

uint64\_t   \*input,

uint32\_t    inputCnt,

void       \*inputStruct,

size\_t      inputStructCnt,

uint64\_t   \*output,

uint32\_t   \*outputCnt,

void       \*outputStruct,

size\_t     \*outputStructCntP)

{

if (maybe()){

flip\_bit(input, sizeof(\*input) \* inputCnt);

}

if (maybe()){

flip\_bit(inputStruct, inputStructCnt);

}

return IOConnectCallMethod(

connection,

selector,

input,

inputCnt,

inputStruct,

inputStructCnt,

output,

outputCnt,

outputStruct,

outputStructCntP);

}

typedef struct interposer {

void\* replacement;

void\* original;

} interpose\_t;

\_\_attribute\_\_((used)) static const interpose\_t interposers\[\]

\_\_attribute\_\_((section("\_\_DATA, \_\_interpose"))) =

{

{ .replacement = (void\*)fake\_IOConnectCallMethod,

.original    = (void\*)IOConnectCallMethod

}

};

Compile that as a dynamic library:



$ clang -Wall -dynamiclib -o flip.dylib flip.c -framework IOKit -arch i386 -arch x86\_64



and load it:



$ DYLD\_INSERT\_LIBRARIES=./flip.dylib hello\_world



1% of the time this will flip one bit in any struct input and scalar input to an IOKit external method. This was the fuzzer which found the bug used to get kernel instruction pointer control for pwn4fun, and it found it well before I had any clue how the Intel GPU driver worked at all.



## IntelAccelerator bug

Running the fuzzer shown above with any program using the GPU lead within seconds to a crash in the following method in the AppleIntelHD4000Graphics kernel extension at the instruction at offset 0x8BAF:



IGAccelGLContext::unmap\_user\_memory(  ;rdi == this

IntelGLUnmapUserMemoryIn \*,       ;rsi

unsigned long long)               ;rdx

\_\_text:8AD6

\_\_text:8AD6 var\_30 = qword ptr -30h

...

\_\_text:8AED  cmp   rdx, 8

\_\_text:8AF1  jnz   loc\_8BFB

\_\_text:8AF7  mov   rbx, \[rsi\]        ;rsi points to controlled data

\_\_text:8AFA  mov   \[rbp+var\_30\], rbx ;rbx completely controlled

...

\_\_text:8BAB  mov   rbx, \[rbp+var\_30\]

\_\_text:8BAF  mov   rax, \[rbx\]        ;crash

\_\_text:8BB2  mov   rdi, rbx

\_\_text:8BB5  call  qword ptr \[rax+140h\]



Looking at the cross references to this function in [IDA Pro](https://www.hex-rays.com/products/ida/) we can see that unmap\_user\_memory is selector 0x201 of the IGAccelGLContent user client. This external method has one struct input so on entry to this function rsi points to controlled data (and rdx contains the length of that struct input in bytes.)

At address 0x8af7 this function reads the first 8 bytes of the struct input as a qword and saves them in rbx. At this point rbx is completely controlled. This controlled value is then saved into the local variable var\_30. Later at 0x8bab this value is read back into rbx, then at 0x8baf that controlled value is dereferenced without any checks leading to a crash. If that dereferences doesn't crash however, then the qword value at offset 0x140 from the read value will be called.

In other words, this external method is treating the struct input bytes as containing a pointer to a C++ object and it’s calling a virtual method of that object without checking whether the pointer is valid. Kernel space is just trusting that userspace will only ever pass a valid kernel object pointer. So by crafting a fake IOKit object and passing a pointer to it as the struct input of selector 0x201 of IGAccelGLContent we can get kernel instruction pointer control! Now what?



## SMEP/SMAP

Mavericks supports Supervisor Mode Execute Prevention which means that when the processor is executing kernel code the cpu will fault if it tries to execute code on pages belonging to userspace. This prevents us from simply mapping an executable kernel shellcode payload at a known address in userspace and getting the kernel to jump to it.

The generic defeat for this mitigation is code-reuse ([ROP](https://en.wikipedia.org/wiki/Return-oriented_programming)). Rather than diverting execution directly to shellcode in userspace instead we have to divert it to existing executable code in the kernel. By “pivoting” the stack pointer to controlled data we can easily chain together multiple code chunks and either turn off SMEP or execute an entire payload just in ROP.

The second generic mitigation supported at the CPU level is Supervisor Mode Access Prevention. As the name suggests this prevents kernel code from even reading user pages directly. This would mean we’d have to be able to get controlled data at a known location in kernel space for the fake IOKit object and the ROP stack since we wouldn’t be able to dereference userspace addresses, even to read them.

However, Mavericks doesn’t support SMAP so this isn’t a problem, we can put the fake IOKit object, vtable and ROP stack in userspace.



## kASLR

To write the ROP stack we need to know the exact location of the kernel code we’re planning to reuse. On OS X kernel [address space layout randomisation](https://en.wikipedia.org/wiki/Address_space_layout_randomization) means that there are 256 different addresses where the kernel code could be located, one of which is randomly chosen at boot time. Therefore to find the addresses of the executable code chunks we need some way to determine the distance kASLR has shifted the code in memory (this value is known as the kASLR slide.)



## IOKit registry

We briefly mentioned earlier that the IOKit registry allows userspace programs to find out about hardware, but what does that actually mean? The IOKit registry is really just a place where drivers can publish (key:value) pairs (where the key is a string and the value something equivalent to a [CoreFoundation](https://developer.apple.com/library/mac/documentation/CoreFoundation/Reference/CoreFoundation_Collection/_index.html) data type.) The drivers can also specify that some of these keys are configurable which means userspace can use the IOKit registry API to set new values.

Here are the MIG RPCs for reading and settings IOKit registry values:



routine io\_registry\_entry\_get\_property(

registry\_entry      : io\_object\_t;

in  property\_name       : io\_name\_t;

out properties          : io\_buf\_ptr\_t, physicalcopy );

routine io\_registry\_entry\_set\_properties(

registry\_entry      : io\_object\_t;

in  properties          : io\_buf\_ptr\_t, physicalcopy;

out result              : kern\_return\_t );



And here are the important parts of the kernel-side implementation of those functions, firstly, for setting a property:



kern\_return\_t is\_io\_registry\_entry\_set\_properties( 

io\_object\_t registry\_entry,

io\_buf\_ptr\_t properties,

mach\_msg\_type\_number\_t propertiesCnt,

kern\_return\_t \* result){

...

obj = OSUnserializeXML( (const char \*) data, propertiesCnt );

...

#if CONFIG\_MACF

else if (0 != mac\_iokit\_check\_set\_properties(kauth\_cred\_get(),

registry\_entry,

obj))

res = kIOReturnNotPermitted;

#endif

else

res = entry->setProperties( obj );

...



and secondly, for reading a property:



kern\_return\_t is\_io\_registry\_entry\_get\_property(

io\_object\_t registry\_entry,

io\_name\_t property\_name,

io\_buf\_ptr\_t \*properties,

mach\_msg\_type\_number\_t \*propertiesCnt ){

...

obj = entry->copyProperty(property\_name);

if( !obj)

return( kIOReturnNotFound );

OSSerialize \* s = OSSerialize::withCapacity(4096);

...

if( obj->serialize( s )) {

len = s->getLength();

\*propertiesCnt = len;

err = copyoutkdata( s->text(), len, properties );

...



These functions are pretty simple wrappers around the setProperties and copyProperty functions implemented by the drivers themselves.

There’s one very important thing to pick up on here though: in the is\_io\_registry\_entry\_set\_properties function there’s a MAC hook, highlighted here in red, which allows sandbox profiles to restrict the ability to set IOKit registry values. (This hook is exposed by Sandbox.kext as the iokit-set-properties operation.) Contrasts this with the is\_io\_registry\_entry\_get\_property function which has no MAC hook. This means that read access to the IOKit registry cannot be restricted. Every OS X process has full access to read every single (key:value) pair exposed by every IOKit driver.



## Enumerating the iokit registry

OS X ships with the ioreg tool for exploring the IOKit registry on the command line. By passing the -l flag we can get ioreg to enumerate all the registry keys and dump their values. Since we’re looking for kernel pointers, lets grep the output looking for a byte pattern we’d expect to see in a kernel pointer:



$ ioreg -l | grep 80ffffff

|   "IOPlatformArgs" =\<00901d2880ffffff00c01c2880ffffff90fb222880ffffff0000000000000000>



That looks an awful lot like a hexdump of some kernel pointers :)

Looking for the "IOPlatformArgs" string in the XNU source code we can see that the first of these pointers is actually the address of the [DeviceTree](https://theiphonewiki.com/wiki/DeviceTree) that’s passed to the kernel at boot. And it just so happens that the same kASLR slide that gets applied to the kernel image also gets applied to that DeviceTree pointer, meaning that we can simply subtract a constant from this leaked pointer to determine the runtime load address of the kernel allowing us to rebase our ROP stack.

Check out [this](http://winocm.com/technical/2014/05/30/disarming-the-ios-kernel/) blog post from winocm for a lot more insight into this bug and its applicability to iOS.



## OS X kernel ROP pivot

Looking at the disassembly of unmap\_user\_memory we can see that when the controlled virtual method is called the rax register points to the fake vtable which we've put in userspace. The pointer at offset 0x140h will be the function pointer that gets called which makes the vtable a convenient place for the ROP stack. We just need to find a sequence of instructions which will move the value of rax into rsp. The /mach\_kernel binary has following instruction sequence:



push rax

add \[rax\], eax

add \[rbx+0x41\], bl

pop rsp

pop r14

pop r15

pop rbp

ret



This will push the vtable address on to the stack, corrupt the first entry in the vtable and write a byte to rbx+0x41. rbx will be the this pointer of the fake IOKit object which we control and have pointed into userspace so neither of these writes will crash. pop rsp then pops the top of the stack into rsp - since we just pushed rax on to the stack this means that rsp now points to the fake vtable in userspace. The code then pops values for r14, r15 and rbp then returns meaning that we can place a full ROP stack in the fake vtable of the fake IOKit object.



## Payload and continuation

The OS X kernel function [KUNCExecute](http://phrack.org/issues/66/16.html) is a really easy way to launch GUI applications from kernel code:



kern\_return\_t KUNCExecute(char executionPath\[1024\], int uid, int gid)



The payload for the pwn4fun exploit was a ROP stack which called this, passing a pointer to the string “/Applications/Calculator.app/Contents/MacOS/Calculator” as the executionPath and 0 and 0 as the uid and gid parameters. This launches the OS X calculator as root :-)

Take a look at [this](https://code.google.com/p/google-security-research/issues/detail?id=126) exploit for [this](https://code.google.com/p/google-security-research/issues/detail?id=40) other IOKit bug which takes a slightly different approach by using a handful of ROP gadgets to first disable SMEP then call a more complicated shellcode payload in userspace. And if you're still running OS X Mavericks or below then why not try it out?

After executing the kernel payload we can call the kernel function thread\_exception\_return to return back to usermode. If we just do this however it will appear as if the whole system has frozen. The kernel payload has actually run (and we can verify this by attaching a kernel debugger) but we can no longer interact with the system. This is because before we got kernel code execution unmap\_user\_memory took two locks - if we don’t drop those locks then no other functions will be able to get them and the GPU driver grinds to a halt. Again, check out that linked exploit above to see some example shellcode which drops the locks.



## Conclusion

The actual development process of this sandbox escape was nothing like as linear as this writeup made it seem. There were many missed turns and other bugs which looked like far too much effort to exploit. Naturally these were reported to Apple too, just in case.



A few months after the conclusion of pwn4fun 2014 I decided to take another look at GPU drivers on OS X, this time focusing on manual analysis. Take a look at the following bug reports for PoC code and details of all the individual bugs: [CVE-2014-1372](https://code.google.com/p/google-security-research/issues/detail?id=18), [CVE-2014-1373](https://code.google.com/p/google-security-research/issues/detail?id=22), [CVE-2014-1376](https://code.google.com/p/google-security-research/issues/detail?id=19), [CVE-2014-1377](https://code.google.com/p/google-security-research/issues/detail?id=17), [CVE-2014-1379](https://code.google.com/p/google-security-research/issues/detail?id=20), [CVE-2014-4394](https://code.google.com/p/google-security-research/issues/detail?id=28), [CVE-2014-4395](https://code.google.com/p/google-security-research/issues/detail?id=29), [CVE-2014-4398](https://code.google.com/p/google-security-research/issues/detail?id=32), [CVE-2014-4401](https://code.google.com/p/google-security-research/issues/detail?id=30), [CVE-2014-4396](https://code.google.com/p/google-security-research/issues/detail?id=30), [CVE-2014-4397](https://code.google.com/p/google-security-research/issues/detail?id=30), [CVE-2014-4400](https://code.google.com/p/google-security-research/issues/detail?id=30), [CVE-2014-4399](https://code.google.com/p/google-security-research/issues/detail?id=30), [CVE-2014-4416](https://code.google.com/p/google-security-research/issues/detail?id=34), [CVE-2014-4376](https://code.google.com/p/google-security-research/issues/detail?id=31), [CVE-2014-4402](https://code.google.com/p/google-security-research/issues/detail?id=33)



Finally, why not [subscribe to the Project Zero bug tracker](https://code.google.com/p/google-security-research/issues/subscriptions) and follow along with all our latest research?
