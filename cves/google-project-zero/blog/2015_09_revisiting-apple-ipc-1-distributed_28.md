# Revisiting Apple IPC: (1) Distributed Objects - Project Zero

Source: https://projectzero.google/2015/09/revisiting-apple-ipc-1-distributed_28.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Ian Beer of Google Project Zero


Earlier this year I gave a talk at the inaugural [Jailbreak Security Summit](http://www.jailbreaksecuritysummit.com/) entitled Auditing and Exploiting Apple IPC \[ [slides](http://thecyberwire.com/events/docs/IanBeer_JSS_Slides.pdf) | [video](http://www.thecyberwire.com/events/jailbreak-security-summit-2015-ian-beer.html) \]. As part of my research for that talk I wanted to find at least one bug involving each of the available IPC mechanisms on OS X/iOS; many of which remain unexplored and poorly-documented from a security perspective.

In the end I was only able to speak about three distinct bugs (involving XPC, MIG and raw mach messages) as the other bugs I’d found were still unpatched when I gave the talk. Apple have since fixed these remaining issues and in this short series of blog posts I’ll discuss in more depth some of these more obscure IPC mechanisms and exploit some more bugs.

In this first post we’ll look a series of bugs in a [suid root](https://en.wikipedia.org/wiki/Setuid) executable which uses [Distributed Objects](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html)…

Distributed Objects

Distributed Objects are a very old Cocoa Objective-C RPC technology. The idea behind them is pretty awesome: it allows you to take Objective-C objects in your process and make them available to other processes. Any other process can look up these objects (via launchd) and instantiate a proxy object in their own address space which functions (almost\*) exactly like the real object, with the slight exception that all interactions with the proxy object are transparently marshalled back and forth via IPC between the two processes:


\*Mike Ash’s excellent blog has a very detailed post outlining why proxy objects are only almost exactly like the real objects they represent: https://mikeash.com/pyblog/friday-qa-2009-02-20-the-good-and-bad-of-distributed-objects.html

In Objective-C we can define and vend a distributed object like this:

#import \<objc/Object.h>

#import \<Foundation/Foundation.h>

@interface VendMe : NSObject

\- (oneway void) foo: (int) value;

@end

@implementation VendMe

\- (oneway void) foo: (int) value;

{

NSLog(@"%d", value);

}

@end

int main (int argc, const char \* argv\[\]) {

VendMe\* toVend = \[\[VendMe alloc\] init\];

NSConnection \*conn = \[NSConnection defaultConnection\];

\[conn setRootObject:toVend\];

\[conn registerName:@"com.foo.my\_test\_service"\];

\[\[NSRunLoop currentRunLoop\] run\];

return 0;

}

Here we’ve defined the class VendMe with one method named foo. We create an NSConnection object, passing it our VendMe instance and then call registerName to make this object available to other processes. Behind the scenes this registers a mach port send-right under that name with launchd allowing other processes to look it up and send mach messages.

Here’s the corresponding client side code:

#import \<Cocoa/Cocoa.h>

int main(int argc, char\*\* argv){

id theProxy = \[\[NSConnection

rootProxyForConnectionWithRegisteredName:@"com.foo.my\_test\_service"

host:nil\] retain\];

\[theProxy foo:123\];

return 0;

}

The NSConnection method rootProxyForConnectionWithRegisteredName is quite self-explanatory; given the object name to look up via launchd (in this case “com.foo.my\_test\_service”) it returns a proxy object which we can use to interact with the real object published under that name by the remote process. In this case we then call the foo method on the proxy passing the integer literal 123. This method call will be proxied over to the server process where the foo method will actually execute and log the string “123” to the console.

Controlling objects in weird ways

Natalie Silvanovich’s recent [Project Zero blog post](/2015/08/attacking-ecmascript-engines-with.html) on redefining object internals in ActionScript demonstrated the kinds of weird things which can happen when objects behave in unexpected ways. Natalie’s work has focused on the the native code underlying the ECMA-script family of languages which are very dynamic, allowing you to redefine surprisingly low-level object behaviour from scripts. Many of the bugs discussed in Natalie’s blog post stem from native code not taking sufficient precautions when interacting with these user-controlled objects. Typically these bugs manifest as use-after-free’s or time-of-check-time-of-use issues due to native code failing to account for callbacks into user-controlled script which modifies state somehow.

Distributed Objects allow us to do similar things with Objective-C :) Of course, this is almost certainly going to be in the context of a local privilege escalation or sandbox escape rather than remote code execution.

In the DO example earlier we called a method passing a simple integer literal as the argument. It’s easy to imagine how this immutable integer can be serialized and reappear in the target process (for example, we could just send the raw bytes representing the value.) But Objective-C is an object-oriented language and we can pass much more complicated objects as function parameters. For example: what happens if we try to pass an instance of a custom Objective-C class as a parameter to a method of a DO proxy object?


If DO doesn’t know how to serialize a parameter (via [NSCoding](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Protocols/NSCoding_Protocol/)) then it will create a proxy for the client’s object in the server process. Furthermore, if the protocol itself is weakly typed but the code is written expecting a certain type to always be passed we can begin to circumvent the intended logic of functions. For example, if a method prototype declares a parameter :(id)UsuallyAString and then calls string selectors like stringByAppendingPathComponent we could proxy those methods such that, in this example it wouldn’t actually return the concatenation of the two strings but instead something completely different!

Whether or not this is interesting depends upon how DO are used in reality. Are there cases where oddly behaving proxy objects could lead to bugs? Does code actually take precautions to check whether it’s interacting with real native objects or attacker-controlled proxies?

Let’s take a look at some real-world code which uses DO.

Install.framework

Install.framework is a OS X private framework, used when installing packages. Interestingly it contains a setuid-root executable helper named runner:

-rwsr-sr-x  1 root  wheel   115K Apr 28 13:13 /System/Library/PrivateFrameworks/Install.framework/Resources/runner

This means that when we exec this file as a regular user it will actually run with an effective user id of 0.

IFInstallRunner

After performing a handshake with the runner executable we can get a proxy object for an instance of  the IFInstallRunner class (check out the actual exploits linked at the end to see the details of this handshake.)

Looking through the list of exposed IFInstallRunner methods one of them jumps out right away as being worth a closer look:

\[IFInstallRunner makeReceiptDirAt:asRoot:\]

This method does exactly what it says; given an arbitrary path it will create the subdirectories ‘Library/Receipts’ under there; and if you set the asRoot flag it will create these directories as root! We’ll take a closer look at the implementation of that but first it’s important to note that in the main method of the runner executable, right after it started, it executed:

if (!(seteuid(getuid())) { fail(); }

if (!(setegid(getgid())) { fail(); }

This is the standard way for a setuid process to temporarily drop privileges, meaning that when we reach the makeReceiptDirAt method the runner process is actually running with an effective-user-id of the user which exec’d it.

In the makeReceiptDirAt method if we pass a non-zero value for the asRoot parameter then the code regains root privileges privileges like this:

if (asRoot) {

seteuid(0);

setegid(0);

}

At the end of the function there’s a call to restoreUIDs: which drops privs again.

Being able to to create these directories as root is certainly interesting but it’s hard to see a clear path to actually exploiting that to do anything too useful. Let’s look more closely at the implementation of makeReceiptDirAt. Here’s what I think the source for this function might look like:

@implementation IFInstallRunner

\- (BOOL) makeReceiptDirAt:(id)pathArg asRoot:(BOOL)asRootArg;

{

NSFileManager\* file\_manager = \[NSFileManager defaultManager\];


if (!\[file\_manager fileExistsAtPath: \[pathArg stringByAppendingPathComponent:

@"Library/Receipts"\]\] ) {

uid\_t real\_uid = getuid();

gid\_t real\_gid = getgid();


if (asRoot) {

seteuid(0);

setegid(0);

}


id pathArgSlashLibrary = \[pathArg stringByAppendingPathComponent: @"Library"\]

if (!\[file\_manager fileExistsAtPath: pathArgSlashLibrary\]) {

// create the the "Library" directory and chown it to the right user:

if (asRoot) {

if (!(mkdir(\[pathArgSlashLibrary fileSystemRepresentation\], 0x3fd))) {

goto fail;

}

if (!(chown(\[pathArgSlashLibrary fileSystemRepresentation\], 0, 0x50))) {

unlink(\[pathArgSlashLibrary fileSystemRepresentation\]);

goto fail;

}

} else {

if (!(mkdir(\[pathArgSlashLibrary fileSystemRepresentation\], 0x1ed))) {

goto fail;

}

if (!(chown\[pathArgSlashLibrary fileSystemRepresentation\], real\_uid, real\_gid)) {

unlink(\[pathArgSlashLibrary fileSystemRepresentation\]);

goto fail;

}

}

}


id pathArgSlashLibrarySlashReceipts = \[pathArg stringByAppendingPathComponent: @"Receipts"\];

if (\[file\_manager fileExistsAtPath: pathArgSlashLibrarySlashReceipts\]) {

// create the the "Receipts" directory under that and chown it to the right user:

if (asRoot) {

if (!(mkdir(\[pathArgSlashLibrarySlashReceipts fileSystemRepresentation\], 0x3fd))) {

goto fail;

}

if (!(chown(\[pathArgSlashLibrarySlashReceipts fileSystemRepresentation\],

0, 0x50))) {

unlink(\[pathArgSlashLibrarySlashReceipts fileSystemRepresentation\]);

goto fail;

}

} else {

if (!(mkdir(\[pathArgSlashLibrarySlashReceipts fileSystemRepresentation\], 0x1c0))) {

goto fail;

}

if (!(chown\[pathArgSlashLibrarySlashReceipts fileSystemRepresentation\],

real\_uid, real\_gid)) {

unlink(\[pathArgSlashLibrarySlashReceipts fileSystemRepresentation\]);

goto fail;

}

}

}

}

\[self restoreUIDs\];

return 1;


fail:

\[self restoreUIDs\];

return 0;

}

@end

Although this code is clearly written expecting pathArg to be an NSString (stringByAppendingPathComponent is an NSString method) there’s actually nothing enforcing that pathArg is a real NSString object and not a proxy. This means that we could in fact pass an instance of our own FakeString object to this method:

@interface FakeString : NSObject

\- (id) stringByAppendingPathComponent: (NSString\*) aString;

@end

@implementation FakeString

\- (id) stringByAppendingPathComponent: (NSString\*) aString;

{

NSLog(@”got a callback!”);

return @”anything we want!”;

}

@end

If you pass an instance of that object to the IFInstallRunner proxy’s createReceiptDir method you’ll see the suid executable call back into your process when it calls stringByAppendingPathComponent on the pathArg argument, allowing us to completely control the semantics of this fake string. And we don’t need to stop there! Rather than returning a string literal (@”anything we want!” in this example) we could instead keep on returning controlled custom objects from the callbacks allowing us to completely circumvent almost all the intended logic of the function. If you trace through transitive closure of all the objects we can gain control of as a result of controlling pathArg you’ll find that we can reach calls to mkdir, unlink and chown with controlled arguments. This was CVE-2015-5784; check out the exploit attached to [the bug report](https://code.google.com/p/google-security-research/issues/detail?id=477) to see the full implementation. This bug was patched by verifying that the pathArg object isn’t a proxy by calling \[pathArg isProxy\] at the beginning of the function (and no, unfortunately you can’t just proxy the call to isProxy!)

This is certainly much more interesting than just being able to make subdirectories called “Library/Receipts” as root. But can we do more?

Implicit state machines

We can model the privilege level (the effective-user-id or EUID) of the runner process as a very simple state machine:
 

There is a fundamental problem here: EUID’s are process-wide whereas Distributed Objects are inherently parallel, meaning that we can concurrently be interacting with multiple proxy objects in a process. This means that the “at the entrypoint EUID != 0” invariant which each IFInstallRunner method relies on must be explicitly enforced by locks, as it will no longer implicitly hold when there are multiple proxy connections. However, looking at the code there are no locks enforcing this.

Again, whether or not that’s interesting depends upon two things:
- 
Are there DO methods which might do useful things if the EUID != 0 invariant doesn’t hold?
- 
Is it possible to win the race condition? (Are DO proxies each separate threads or just runloop sources? Can we actually exercise enough  control to get a race condition and win it?)


Looking through the list of IFInstallRunner methods yields an easy answer to the first question: the runTaskSecurely  method allow us to specify a path to an executable and then get the runner to exec it. Note that unlike makeReceiptDirAt this method doesn’t have an “asRoot” parameter. Under normal circumstances it will be executed with EUID of the regular user.

For the second question, looking at the list of threads in the runner process with lldb’s thread list command it seems like individual vended distributed objects don’t get their own threads of control, but with some experimentation it turns out that if we can get a proxy callback from the runner into our code the runner will wait until we reply before continuing. And whilst it’s waiting we can indeed successfully call methods on any other proxy objects we have and they will execute in the target!

Putting it all together

The final exploit looks something like this:
 [original bug report](https://code.google.com/p/google-security-research/issues/detail?id=478). Along with the \[pathArg isProxy\] patch the fix for this issue involved adding NSLocks to make the implicit state machine explicit and enforceable.
