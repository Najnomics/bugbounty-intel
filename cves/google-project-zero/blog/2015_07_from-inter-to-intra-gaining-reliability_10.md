# From inter to intra: gaining reliability - Project Zero

Source: https://projectzero.google/2015/07/from-inter-to-intra-gaining-reliability_10.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Chris Evans, avoider of crossing (heap) lines. Part 2 of 4.


In the [first post in this series](/2015/06/what-is-good-memory-corruption.html), we concluded with a traditional exploit for Adobe Flash [bug 324](https://code.google.com/p/google-security-research/issues/detail?id=324), and noted that it could never be 100% reliable. We also challenged ourselves to do better! Is there some way we can leverage the same vulnerability more reliably?

It turns out that there is. The breakthrough comes when we re-examine the primitive we have. The bug manifests when we are resolving input parameters to a shader program. This process is fairly simple: a parameterized shader program contains placeholder constant definition opcodes for each input value, and just before the program is run, the placeholder constants are replaced with parameter values. A parameter “knows” the index of the opcode that it is going to write into, but an index that is valid in the context of one program may not be valid in the context of another of different length:


To trigger the vulnerability, we take a parameter from one program and associate it with a different program. There are two types of invalidity:

1. The parameter index is out-of-bounds for the program’s opcodes. This leads to the inter heap chunk memory corruption that we abused in the previous post:


1. A new possibility: the parameter index is in-bounds for the program’s opcodes, but the indexed opcode is not a placeholder constant definition.

The exciting thing to note about the new possibility is that we do not cross a heap chunk. We’re triggering an intra-chunk corruption that will be deterministic. So — is there a useful side-effect we can abuse if we corrupt the compiled program opcodes? The answer is maybe. Unfortunately, the corruption we can cause is an overwrite of the last 4 bytes of a 20-byte opcode. This is not a commonly used field of the opcode and at first glance it appears to only be used for constant values. However, upon a closer look, there’s an opcode that operates similarly to the C ternary operator, so we can corrupt it:


The ternary opcode works like this:

DEST\_REG = (CONDITION\_REG == 1) ? SRC\_REG\_1 : SRC\_REG\_2

As you can see, this opcode references a lot of registers. And this last register, SRC\_REG\_2, is stored in bytes 16 - 19 of the ternary opcode. We can therefore corrupt this register number to be whatever we want. By the time we corrupt it, the register number has been pre-validated (and rewritten) so maybe this leads to a useful side-effect?

The SRC\_REG\_2 register is used only as a read. At first glance, this doesn’t sound too exciting — turning a very controlled write into a wild read. But if we take the trouble to look at the context of the read during shader program execution, we note something promising. There’s a single heap chunk which contains a C++ object relating to shader execution, prepended with space for register state. So let’s say a given shader program uses 8 registers. When our corrupted ternary opcode references (zero-indexed) register 8 or higher, that is an out-of-bounds read. But critically, if the out-of-bounds read isn’t too wild, it will not cross a heap chunk (think determinism, 100% reliability). Furthermore, we’ll be reading from a raw C++ object. C++ objects often contain vtables, including this one! Reading a vtable is a very important first step towards defeating ASLR.


A demonstration of this vtable leak is [attached to the bug](https://code.google.com/p/google-security-research/issues/detail?id=324#c9). There are some fun aspects to the exploit code. The exploit starts by causing a fully deterministic memory corruption via ActionScript and then proceeds in shader bytecode to render pixels based on out-of-bounds content into a virtual render buffer. Finally, back to ActionScript to recover the values from the virtual render buffer, into a recognizable pointer value.

When we run it, it doesn’t look very impressive. On Linux x64, it outputs something like: 0x00007f434a1a34d0

That’s the address of a vtable. But, refresh the PoC repeatedly and the value will never change and neither will there be a crash or failure retrieving it. We can try and introduce Flash process state variation by running videos, games, animations in other tabs — but the vtable recovery is 100% deterministic, so it will always work.

This was a non-goal during development, but the exploit is also pretty portable. Without any further effort, the exploit can be run on Windows 8.1 x64 to yield, in my case: 0x00007ffc2e800a50. Run it on Windows 7 x86 and it’s 0x691e2dc800000000.

In summary, the exploit follows the following deterministic steps:

- An unexpected shader parameter setup performs an out-of-bounds write within a heap chunk, to corrupt validated shader bytecode.
- The corrupt shader bytecode performs an out-of-bounds read, also within a heap chunk, to leak a vtable value.

We now have a fully deterministic (dare I say 100% reliable?) way to leak a vtable value. However, this is fairly far away from “arbitrary code execution” — something we did achieve, albeit unreliably, in the first post in this series. In the next posts in the series, we’ll investigate possible avenues forward from here, whilst keeping our “100%” reliability.
