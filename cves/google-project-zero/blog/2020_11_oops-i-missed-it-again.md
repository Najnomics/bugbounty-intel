# Oops, I missed it again! - Project Zero

Source: https://projectzero.google/2020/11/oops-i-missed-it-again.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Written by Brandon Azad, when working at Project Zero

This is a quick anecdotal post describing one of the more frustrating aspects of vulnerability research: realizing that you missed a bug that was staring you in the face only once you see the patched version!

## Some suspicious code

After writing the [oob\_timestamp](https://bugs.chromium.org/p/project-zero/issues/detail?id=1986) exploit, I spent some time trying to find another vulnerability to exploit. Typically, it's a lot easier to develop an exploit when you already have a research platform (read: another exploit) available to help with your analysis, for example by dumping kernel memory to ensure that your heap spray is placing objects at their intended locations. Developing an exploit blind, as I had done with voucher\_swap, is much trickier. (For oob\_timestamp, I relied on checkra1n to bootstrap the exploit on A11, and later expanded it to A13.) So, I thought it might be nice to chain my next exploit off of oob\_timestamp to avoid having to re-bootstrap later.

As I had already spent a fair amount of time reversing the iOS 13.3 (17C54) kernelcache for oob\_timestamp, I decided to continue that effort on a new user client. I wrote a small program to enumerate IOUserClient classes reachable from the app sandbox (inadvertently discovering [another bug](https://bugs.chromium.org/p/project-zero/issues/detail?id=2004) in the process) and looked for classes that I had not researched previously.

A quick primer for those less familiar with Apple kernels: Apple's kernel is called XNU, and IOKit is XNU's C++ framework for implementing drivers. An app in userspace can call IOServiceGetMatchingServices() to get handles to the drivers, but the app can't actually do much with the raw driver handle. Instead, the app needs to direct the driver to create a "user client" by calling IOServiceOpen(), passing the type of user client it wants. Since the user client is what provides most of the functionality to userspace, this is the step that is subject to a sandbox check, ensuring that the app is allowed to open the requested type of user client. Once the app has a handle to a user client for the driver, the app can interact with the user client by calling functions like IOConnectCallMethod() on the user client handle, specifying the "selector" (index) of the method the app wants to invoke. In the kernel, IOConnectCallMethod() will use the selector to index a table of methods provided by the user client, invoking the one requested.

As I was scanning for user clients I could open, one reachable class stood out: H11ANEInDirectPathClient, a user client of the H11ANEIn driver. I hadn't seen this class before, but some quick Googling showed that it wasn't open source, which suggested to me that the code had probably undergone substantially less security review, and hence probably had more low-hanging bugs in it, than the open-source parts of the kernel.

I discovered several interesting things in the process of reversing. First, H11ANEIn appeared to actually have 2 user clients: H11ANEInDirectPathClient (the one I had opened) and H11ANEInUserClient (which I could not open in the sandbox). Reading the strings in the method H11ANEIn::newUserClient(), it appeared that H11ANEInDirectPathClient is the less privileged version of H11ANEInUserClient, so it made sense that I could open the former but not the latter.

if ( type == 1 ) // H11ANEInDirectPathClient

{

\_os\_log\_internal(...,

"%s : ... : Creating direct evaluate client\n",

"virtual IOReturn H11ANEIn::newUserClient(...)");

...

}

else // H11ANEInUserClient

{

\_os\_log\_internal(...,

"%s : ... : Creating default full-entitlement client\n",

"virtual IOReturn H11ANEIn::newUserClient(...)");

...

}

The traditional starting point when looking for bugs in IOKit user clients is to look at the external methods that are provided. These are usually identifiable as tables of function pointers near the user client's vtable in the kernelcache image. Here are the external method tables I identified for the two user clients, curiously laid out back-to-back in the kernelcache rather than each near their respective vtable:


Also, I noticed something interesting when I looked at the cross-references to these two tables: it seemed like since the classes were basically identical except for one being a less-privileged version of the other, Apple had made the rather unusual decision to share the parts of the external method tables corresponding to shared functionality between the two user client types!

This was evident from how the ::externalMethod() methods of each user client accessed the overlapping parts of the external method tables. The H11ANEInDirectPathClient version:

int H11ANEInDirectPathClient::externalMethod(H11ANEInDirectPathClient \*this, u32 selector, IOExternalMethodArguments \*args, IOExternalMethodDispatch \*method, void \*target)

{

if ( !target )

target = this;

if ( selector \<= 33 )

method = &H11ANEInDirectPathClient\_ExternalMethods\_34\[selector\];

return IOUserClient::externalMethod(this, selector, args, method, target);

}

And the H11ANEInUserClient version:

int H11ANEInUserClient::externalMethod(H11ANEInUserClient \*this, u32 selector, IOExternalMethodArguments \*args, IOExternalMethodDispatch \*method, void \*target)

{

if ( !target )

target = this;

if ( selector \<= 33 )

method = &H11ANEInUserClient\_ExternalMethods\_34\[selector\];

return IOUserClient::externalMethod(this, selector, args, method, target);

}

Since each can access 34 methods and the first 3 in the array are reserved for H11ANEInDirectPathClient, this meant that the last 3 would be reserved for H11ANEInUserClient, which seemed to check out since there were 37 methods total. Neat.

So, I started digging into the methods accessible by H11ANEInDirectPathClient, and very quickly adopted the opinion that the code quality in this driver was not very high. For example, I found that the 3500-line method H11ANEIn::ANE\_ProgramSendRequest\_gated(), reachable through selectors 2 and 33, exhibited some pretty trivial out-of-bounds reads right at the top of the function:


Here, the content of args is fully controlled, so the args->totInputBuffers count can be arbitrarily high, past the ends of the inputBufferSymbolIndex and inputBufferSurfaceId arrays.

Since the code quality seemed to be low, and since I was not particularly keen on untangling multi-thousand-line functions, I also tried to perform some very trivial fuzzing. My fuzzing experience was quite limited, but I had long ago written a dumb fuzzer that just blindly calls IOConnectCallMethod() from userspace passing randomly generated values; surprisingly, this had been sufficient before to find real kernel vulnerabilities. So, I decided to revive that old fuzzer and point it at H11ANEInDirectPathClient.

Within one second of launching the fuzzer app, the device panicked.

I was of course quite excited at this development, but it turned out that the bug was a pretty trivial NULL pointer dereference; not exploitable on iOS. And further fuzzing didn't seem to trigger anything else interesting. So, with other [more interesting projects](/2020/07/one-byte-to-rule-them-all.html) mounting, I sent a quick non-security report to Apple alerting that this area of the code could be problematic and then turned away from H11ANEInDirectPathClient.

## Once more, with symbols

Fast forward to the end of August.

As had happened before with the iOS 12 beta, Apple had accidentally [included a symbolicated kernelcache](https://twitter.com/tihmstar/status/1295814618242318337) in some of the iOS 14 beta releases. I hadn't had a chance to dig into them yet, but I figured that the addition of symbols (and in particular the limited type information that could be inferred from mangled C++ method names) would make reversing the web of multi-thousand-line H11ANEIn functions faster and thus more worthwhile. So, I opened IDA and jumped once again to the external method tables to see if there were any obvious changes.

But almost immediately, something about the external method tables caught my eye:


Oddly, the external method tables for both H11ANEInDirectPathClient and H11ANEInUserClient had defined symbols. This was weird: I had expected the code would consist of a single array of IOExternalMethodDispatch structs, so that H11ANEInDirectPathClient could claim the 34 methods starting at index 0 while H11ANEInUserClient could claim the 34 methods starting at index 3. In such an arrangement, there should only be one symbol, that for the array as a whole.

Then it dawned on me: my notion of overlapping external method arrays was nonsense, and the "sharing" of external methods was a simple out-of-bounds access by H11ANEInDirectPathClient! The less privileged client was supposed to only have 3 methods, but it just so happened that there was a typo in the bounds-check, allowing H11ANEInDirectPathClient to access and call external methods from the more privileged client. And in so doing, each call by H11ANEInDirectPathClient to an H11ANEInUserClient was implicitly triggering a type confusion on the this pointer!

In hindsight, I realized that the "sharing external method arrays" arrangement made no sense: any such use would have to be careful to avoid type confusion between the two classes of user clients, and no such precaution was taking place. This conviction was confirmed when I decompiled H11ANEInDirectPathClient::externalMethod() in the new kernelcache and saw that the bounds check on the selector had decreased from 33 to 2, meaning the bug was now patched.

So, I had missed an issue staring me in the face the whole time, whose existence I had justified by inventing a concept of overlapping method tables. And of course, to add insult to injury, the NULL pointer dereferences I had reported as a non-security issue were only reached by calling two of the out-of-bounds methods.

## Another recipe for copypasta

How might this bug have come to exist in the first place? Since the buggy version included the same bounds check for both ::externalMethod() implementations, I suspect this was [another case](/2017/04/exception-oriented-exploitation-on-ios.html) of a copy-paste bug. Here's my guess for what H11ANEInUserClient::externalMethod() actually looks like in Apple's source:

IOReturn H11ANEInUserClient::externalMethod(

u32 selector, IOExternalMethodArguments \*args,

IOExternalMethodDispatch \*method, void \*target)

{

if ( !target )

target = this;

if ( selector \< H11ANEInUserClient::sMethodCount )

method = &H11ANEInUserClient::sMethods\[selector\];

return super::externalMethod(this, selector, args, method, target);

}

My guess is that this code was copy-pasted to create the H11ANEInDirectPathClient version, but the author accidentally forgot to change the type name in the selector check:

IOReturn H11ANEInDirectPathClient::externalMethod(

u32 selector, IOExternalMethodArguments \*args,

IOExternalMethodDispatch \*method, void \*target)

{

if ( !target )

target = this;

if ( selector \< H11ANEInUserClient::sMethodCount )

method = &H11ANEInDirectPathClient::sMethods\[selector\];

return super::externalMethod(this, selector, args, method, target);

}

Aside from that, it's mostly a convenient accident that the compiler laid the external method tables back-to-back, making this bug plausibly exploitable (as opposed to past cases of out-of-bounds external methods that I'm aware of). That said, I have not examined the actual exploitability of this issue.

## Conclusion

So, what are the takeaways from this story?

First, it's really easy to miss bugs, even ones that you feel should have been obvious. I kicked myself for missing this, given the mental gymnastics I went through to justify why a code pattern like this could exist in the first place. If there's one lesson I've had to teach myself again and again, it's to be inherently suspicious of code and to never assume that it's doing what it does on purpose.


Second, copy-paste is a really quick way to create code, but it's also a quick way to create subtle bugs that, by their nature, are tricky to spot by glancing at the source code. It's easy to tell that 2 arrays are "overlapping" by looking in a disassembler, but it's harder to see that the wrong one of two very similar class names was used in copy-pasted code. While it doesn't solve the problem 100%, it can help to decompose copy-pasted code patterns into reusable helper functions.

Finally, even though I only realized that there was a bug when I looked at the symbolicated kernelcache, I don't want Apple to get the impression that releasing symbols is a security risk. Security researchers rejoice when Apple accidentally releases symbolicated kernelcaches or [development libraries](https://twitter.com/DanyL931/status/1098516958843158528), but this is just because it saves time reversing, not because it makes things newly reversible. Any capable attacker will find bugs regardless of the presence or absence of symbols; all the lack of symbols does is keep the bug away from eyes (like mine) that might report it. Hence, withholding symbols is an incredibly weak protection, only deterring the lowest tiers of attackers and serving to make the bugs that have been found last longer.
