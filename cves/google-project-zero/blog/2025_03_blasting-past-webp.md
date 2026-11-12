# Blasting Past Webp - Project Zero

Source: https://projectzero.google/2025/03/blasting-past-webp.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

An analysis of the NSO BLASTPASS iMessage exploit

Posted by Ian Beer, Google Project Zero


On September 7, 2023 Apple [issued](https://support.apple.com/en-us/106361) an out-of-band security update for iOS:



Around the same time on September 7th 2023, [Citizen Lab published a blog post](https://citizenlab.ca/2023/09/blastpass-nso-group-iphone-zero-click-zero-day-exploit-captured-in-the-wild/) linking the two CVEs fixed in iOS 16.6.1 to an "NSO Group Zero-Click, Zero-Day exploit captured in the wild":


"\[The target was\] an individual employed by a Washington DC-based civil society organization with international offices...


The exploit chain was capable of compromising iPhones running the latest version of iOS (16.6) without any interaction from the victim.


The exploit involved PassKit attachments containing malicious images sent from an attacker iMessage account to the victim."


The day before, on September 6th 2023, Apple [reported a vulnerability to the WebP project](https://issues.chromium.org/issues/40071416), indicating in the report that they planned to ship a custom fix for Apple customers the next day.


The WebP team posted their first [proposed fix](https://chromium.googlesource.com/webm/libwebp/%2B/902bc9190331343b2017211debcec8d2ab87e17a) in the public git repo the next day, and five days after that on September 12th Google released a [new Chrome stable release](https://chromereleases.googleblog.com/2023/09/stable-channel-update-for-desktop_12.html) containing the WebP fix. Both Apple and Google marked the issue as exploited in the wild, alerting other integrators of WebP that they should rapidly integrate the fix as well as causing the security research community to take a closer look...


A couple of weeks later on September 21st 2023, former Project Zero team lead Ben Hawkes (in collaboration with [@mistymntncop](https://x.com/mistymntncop)) published the [first detailed writeup](https://blog.isosceles.com/the-webp-0day/) of the root cause of the vulnerability on the Isosceles Blog. A couple of months later, on November 3rd, a group called [Dark Navy](https://www.darknavy.org/) published their first blog post: a two-part analysis ([Part 1](https://www.darknavy.org/blog/exploiting_the_libwebp_vulnerability_part_1/) - [Part 2](https://www.darknavy.org/blog/exploiting_the_libwebp_vulnerability_part_2/)) of the WebP vulnerability and a [proof-of-concept exploit](https://github.com/DarkNavySecurity/PoC/tree/main/CVE-2023-4863) targeting Chrome (CVE-2023-4863).



Whilst the Isosceles and Dark Navy posts explained the underlying memory corruption vulnerability in great detail, they were unable to solve another fascinating part of the puzzle: just how exactly do you land an exploit for this vulnerability in a one-shot, zero-click setup? As we'll soon see, the corruption primitive is very limited. Without access to the samples it was almost impossible to know.


In mid-November, in collaboration with [Amnesty International Security Lab](https://securitylab.amnesty.org/), I was able to obtain a number of BLASTPASS [PKPass](https://en.wikipedia.org/wiki/PKPASS) sample files as well as crash logs from failed exploit attempts.


This blog post covers my analysis of those samples and the journey to figure out how one of NSO's recent zero-click iOS exploits really worked. For me that journey began by immediately taking three months of paternity leave, and resumed in March 2024 where this story begins:

### Setting the scene

For a detailed analysis of the root-cause of the WebP vulnerability and the primitive it yields, I recommend first reading the three blog posts I mentioned earlier ([Isosceles](https://blog.isosceles.com/the-webp-0day/), [Dark Navy 1](https://www.darknavy.org/blog/exploiting_the_libwebp_vulnerability_part_1/), [Dark Navy 2](https://www.darknavy.org/blog/exploiting_the_libwebp_vulnerability_part_2/).) I won't restate their analyses here (both because you should read their original work, and because it's quite complicated!) Instead I'll briefly discuss WebP and the corruption primitive the vulnerability yields.

### WebP

[WebP](https://developers.google.com/speed/webp) is a relatively modern image file format, first released in 2010. In reality WebP is actually two completely distinct image formats: [a lossy format](https://developers.google.com/speed/webp/docs/compression%23lossy_webp) based on the VP8 video codec and a separate [lossless format](https://developers.google.com/speed/webp/docs/compression%23lossless_webp). The two formats share nothing apart from both using a [RIFF](https://en.wikipedia.org/wiki/Resource_Interchange_File_Format) container and the string WEBP for the first chunk name. From that point on (12 bytes into the file) they are completely different. The vulnerability is in the lossless format, with the RIFF chunk name VP8L.


Lossless WebP makes extensive use of [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding); there are at least 10 huffman trees present in the BLASTPASS sample. In the file they're stored as [canonical huffman trees](https://en.wikipedia.org/wiki/Canonical_Huffman_code), meaning that only the code lengths are retained. At decompression time those lengths are converted directly into a two-level huffman decoding table, with the five largest tables all getting squeezed together into the same pre-allocated buffer. The (it turns out not quite) maximum size of these tables is pre-computed based on the number of symbols they encode. If you're up to this part and you're slightly lost, the other three blogposts referenced above explain this in detail.


With control over the symbol lengths it's possible to define all sorts of strange trees, many of which aren't valid. The fundamental issue was that the WebP code only checked the validity of the tree after building the decoding table. But the pre-computed size of the decoding table was only correct for valid trees.


As the Isosceles blog post points out, this means that a fundamental part of the vulnerability is that triggering the bug is detected, though after memory has been corrupted, and image parsing stops only a few lines of code later. This presents another exploitation mystery: in a zero-click context, how do you exploit a bug where every time the issue is triggered it also stops parsing any attacker-controlled data?


The second mystery involves the actual corruption primitive. The vulnerability will write a HuffmanCode structure at a known offset past the end of the huffman tables buffer:


// Huffman lookup table entry

typedef struct {

uint8\_t bits;

uint16\_t value;

} HuffmanCode;


[As DarkNavy point out](https://www.darknavy.org/blog/exploiting_the_libwebp_vulnerability_part_1/%23how-to-control-the-data-to-write), whilst the bits and value fields are nominally attacker-controlled, in reality there isn't that much flexibility. The fifth huffman table (the one at the end of the preallocated buffer, part of which can get written out-of-bounds) only has 40 symbols, limiting value to a maximum value of 39 (0x27) and bits will be between 1 and 7 (for a second-level table entry). There's a padding byte between bits and value which makes the largest value that could be written out-of-bounds 0x00270007. And it just so happens that that's exactly the value which the exploit does write — and they likely didn't have that much choice about it.


There's also not much flexibility in the huffman table allocation size. The table allocation in the exploit is 12072 (0x2F28) bytes, which will get rounded up to fit within a 0x3000 byte libmalloc small region. The code lengths are chosen such that the overflow occurs like this:



To summarize: The 32-bit value 0x270007 will be written 0x58 bytes past the end of a 0x3000 byte huffman table allocation. And then WebP parsing will fail, and the decoder will bail out.

### Déjà vu?

Long-term readers of the Project Zero blog might be experiencing a sense of déjà vu at this point... haven't I already written a blog post about an NSO zero-click iPhone zero day exploiting a vulnerability in a slightly obscure lossless compression format used in an image parsed from an iMessage attachment?



BLASTPASS has many similarities with [FORCEDENTRY](https://en.wikipedia.org/wiki/FORCEDENTRY), and my initial hunch (which turned out to be completely wrong) was that this exploit might take a similar approach to build a weird machine using some fancier WebP features. To that end I started out by writing a WebP parser to see what features were actually used.

### Transformation

In a very similar fashion to [JBIG2](https://en.wikipedia.org/wiki/JBIG2), WebP also [supports](https://developers.google.com/speed/webp/docs/webp_lossless_bitstream_specification) invertible transformations on the input pixel data:




My initial theory was that the exploit might operate in a similar fashion to FORCEDENTRY and apply sequences of these transformations outside of the bounds of the image buffer to build a weird machine. But after implementing enough of the WebP format in python to parse every bit of the VP8L chunk it became pretty clear that it was only triggering the Huffman table overflow and nothing more. The VP8L chunk was only 1052 bytes, and pretty much all of it was the 10 Huffman tables needed to trigger the overflow.

### What's in a pass?

Although BLASTPASS is often referred to as an exploit for "the WebP vulnerability", the attackers don't actually just send a WebP file (even though that is supported in iMessage). They send a [PassKit](https://developer.apple.com/documentation/passkit_apple_pay_and_wallet) PKPass file, which contains a WebP. There must be a reason for this. So let's step back and actually take a look at one of the sample files I received:


171K sample.pkpass


$ file sample.pkpass

sample.pkpass: Zip archive data, at least v2.0 to extract, compression method=deflate


There are five files inside the PKPass zip archive:


60K background.png

5.5M logo.png

175B manifest.json

18B pass.json

3.3K signature


The 5.5MB logo.png is the WebP image, just with a .png extension instead of .webp:


$ file logo.png:

logo.png: RIFF (little-endian) data, Web/P image


The closest thing to a specification for the PKPass format appears to be the [Wallet Developer Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/Creating.html), and whilst it doesn't explicitly state that the .png files should actually be Portable Network Graphics images, that's presumably the intention. This is yet another parallel with FORCEDENTRY, where a similar trick was used to reach the PDF parser when attempting to parse a GIF.


PKPass files require a valid signature which is contained in manifest.json and signature. The signature has a presumably fake name and more timestamps indicating that the PKPass is very likely being generated and signed on the fly for each exploit attempt.


pass.json is just this:


{"pass": "PKpass"}


Finally background.png:


$ file background.png

background.png: TIFF image data, big-endian, direntries=15, height=16, bps=0, compression=deflate, PhotometricIntepretation=RGB, orientation=upper-left, width=48


Curious. Another file with a misleading extension; this time a TIFF file with a .png extension.


We'll return to this TIFF later in the analysis as it plays a critical role in the exploit flow, but for now we'll focus on the WebP, with one short diversion:

### Blastdoor

So far I've only mentioned the WebP vulnerability, but the Apple advisory I linked at the start of this post mentions two separate CVEs:


The first, CVE-2023-41064 in ImageIO, is the WebP bug (though just to keep things confusing with a different CVE from the upstream WebP fix which is CVE-2023-4863 - they're the same vulnerability though).


The second, CVE-2023-41061 in "Wallet", is described in the Apple advisory as: "A maliciously crafted attachment may result in arbitrary code execution".


The [Isosceles blog post](https://blog.isosceles.com/the-webp-0day/) hypothesises:


"Citizen Lab called this attack "BLASTPASS", since the attackers found a clever way to bypass the "BlastDoor" iMessage sandbox. We don't have the full technical details, but it looks like by bundling an image exploit in a PassKit attachment, the malicious image would be processed in a different, unsandboxed process. This corresponds to the first CVE that Apple released, CVE-2023-41061."


This theory makes sense — FORCEDENTRY had a similar trick where the [JBIG2 bug was actually exploited inside](/2022/03/forcedentry-sandbox-escape.html) [IMTranscoderAgent](/2022/03/forcedentry-sandbox-escape.html) instead of the more restrictive sandbox of BlastDoor. But in all my experimentation, as well as all the in-the-wild crash logs I've seen, this hypothesis doesn't seem to hold.


The PKPass file and the images enclosed within do get parsed inside the BlastDoor sandbox and that's where the crashes occur or the payload executes — later on we'll also see evidence that the NSExpression payload which eventually gets evaluated expects to be running inside BlastDoor.


My guess is that CVE-2023-41061 is more likely referring to the lax parsing of PKPasses which didn't reject images which weren't png's.


In late 2024, I received another set of in-the-wild crash logs including two which do in fact strongly indicate that there was also a path to hit the WebP vulnerability in the MobileSMS process, outside the BlastDoor sandbox! Interestingly, the timestamps indicate that these devices were targeted in November 2023, two months after the vulnerability was patched.


In those cases the WebP code was reached inside the MobileSMS process via a ChatKit CKPassPreviewMediaObject created by a CKAttachmentMessagePartChatItem.

### What's in a WebP?

I mentioned that the VP8L chunk in the WebP file is only around 1KB. Yet in the file listing above the WebP file is 5.5MB! So what's in the rest of it? Expanding out my WebP parser we see that there's one more RIFF chunk:


EXIF : 0x586bb8

exif is Intel byte alignment

EXIF has n\_entries=1

tag=8769 fmt=4 n\_components=1 data=1a

subIFD has n\_entries=1

tag=927c fmt=7 n\_components=586b8c data=2c


It's a (really really huge) [EXIF](https://en.wikipedia.org/wiki/Exif) - the standard format which cameras use to store image metadata — stuff like the camera model, exposure time, f-stop etc.


It's a tag-based format and pretty much all 5.5MB is inside one tag with the id 0x927c. So what's that?


Looking through an [online list of EXIF tags](https://www.awaresystems.be/imaging/tiff/tifftags/privateifd/exif.html) just below the lens FocalLength tag and above the UserComment tag we spot 0x927c:



It's the very-vague-yet-fascinating sounding: "MakerNote - Manufacturer specific information."


Looking to [Wikipedia for some clarification](https://en.wikipedia.org/wiki/Exif) on what that actually is, we learn that


"the "MakerNote" tag contains information normally in a proprietary binary format."


Modifying the webp parser to now dump out the MakerNote tag we see:


$ file sample.makernote

sample.makernote: Apple binary property list


Apple's chosen format for the "proprietary binary format" is binary plist!


And indeed: looking through the ImageIO library in IDA there's a clear path between the WebP parser, the EXIF parser, the MakerNote parser and the binary plist parser.

### unbplisting

I covered the binary plist format in [a previous blog post](/2023/10/an-analysis-of-an-in-the-wild-ios-safari-sandbox-escape.html). That was the second time I'd had to analyse a large bplist. The first time (for the FORCEDENTRY sandbox escape) it was possible mostly by hand, just using the human-readable output of plutil. Last year, for the Safari sandbox escape analysis, the bplist was 437KB and I had to write a custom bplist parser to figure out what was going on. Keeping the exponential curve going this year the bplist was 10x larger again.


In this case it's fairly clear that the bplist must be a heap groom - and at 5.5MB, presumably a fairly complicated one. So what's it doing?

### Switching Views

I had a hunch that the bplist would use duplicate dictionary keys as a fundamental building block for the heap groom, but running my parser it didn't output any... until I realised that my tool stored the parsed dictionaries directly as python dictionaries before dumping them. Fixing the tools to instead keep lists of keys and values it became clear that there were duplicate keys. Lots of them:



In the Safari exploit writeup I described how I used different visualisation techniques to try to explore the structure of the objects, looking for patterns I could use to simplify what was going on. In this case, modifying the parser to emit well-formed curly brackets and indentation then relying on [VS Code](https://code.visualstudio.com/)'s automatic code-folding proved to work well enough for browsing around and getting a feel for the structure of the groom object.


Sometimes the right visualisation technique is sufficient to figure out what the exploit is trying to do. In this case, where the primitive is a heap-based buffer overflow, the groom will inevitably try to put two things next to each other in memory and I want to know "what two things?"


But no matter how long I stared and scrolled, I couldn't figure anything out. Time to try something different.

### Instrumentation

I wrote a small helper to load the bplist using the same API as the MakerNote parser and ran it using the Mac Instruments app:



Parsing the single 5.5MB bplist causes nearly half a million allocations, churning through nearly a gigabyte of memory. Just looking through this allocation summary it's clear there's lots of CFString and CFData objects, likely used for heap shaping. Looking further down the list there are other interesting numbers:



The 20'000 in the last line is far too round a number to be a coincidence. This number matches up with the number of \_\_NSDictionaryM objects allocated:



Finally, at the very bottom of the list there are two more allocation patterns which stand out:



There are two sets of very large allocations: eighty 1MB allocations and 44 4MB ones.


I modified my bplist tool again to dump out each unique string or data buffer, along with a count of how many times it was seen and its hash. Looking through the file listing there's a clear pattern:

| Object Size | Count | 
| 0x3FFFFF | 44 | 
| 0xFFFFF | 80 | 
| 0x3FFF | 20 | 
| 0x26A9 | 24978 | 
| 0x2554 | 44 | 
| 0x23FF | 5822 | 
| 0x22A9 | 4 | 
| 0x1FFF | 2 | 
| 0x1EA9 | 26 | 
| 0x1D54 | 40 | 
| 0x17FF | 66 | 
| 0x13FF | 66 | 
| 0x3FF | 322 | 
| 0x3D7 | 404 | 
| 0xF | 112882 | 
| 0x8 | 3 | 



There are a large number of allocations which fall just below a "round" number in hexadecimal: 0x3ff, 0x13ff, 0x17ff, 0x1fff, 0x23ff, 0x3fff... That heavily hints that they are sized to fall exactly within certain allocator size buckets.


Almost all of the allocations are just filled with zeros or 'A's. But the 1MB one is quite different:


$ hexdump -C 170ae757\_80.bin | head -n 20


00000000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|

00000010 00 00 00 00 00 00 00 00 80 26 00 00 01 00 00 00 |.........&......|

00000020 1f 00 00 00 00 00 00 00 10 00 8b 56 02 00 00 00 |...........V....|

00000030 b0 c3 31 16 02 00 00 00 60 e3 01 00 00 00 00 00 |..1.....\`.......|

00000040 20 ec 46 58 02 00 00 00 00 00 00 00 00 00 00 00 | .FX............|

00000050 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|

00000060 00 00 00 00 00 00 00 00 60 bf 31 16 02 00 00 00 |........\`.1.....|

00000070 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|

\*

000004b0 00 00 00 00 00 00 00 00 10 c4 31 16 02 00 00 00 |..........1.....|

000004c0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|

\*

000004e0 02 1c 00 00 01 00 00 00 00 00 00 00 00 00 00 00 |................|

000004f0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|

00000500 00 00 00 00 00 00 00 00 70 80 33 16 02 00 00 00 |........p.3.....|

00000510 b8 b5 e5 57 02 00 00 00 ff ff ff ff ff ff ff ff |...W............|

00000520 58 c4 31 16 02 00 00 00 00 00 00 00 00 00 00 00 |X.1.............|

00000530 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|

\*

00000550 50 75 2c 18 02 00 00 00 01 00 00 00 00 00 00 00 |Pu,.............|



Further on in the hexdump of the 1MB object there's clearly an NSExpression payload - this payload is also visible just running strings on the WebP file. Matthias Frielingsdorf from iVerify gave a [talk at BlackHat Asia with an initial analysis of this NSExpression payload](https://i.blackhat.com/Asia-24/Asia-24-Frielingsdorf-YouShallNotPassAnalysing.pdf), we'll return to that at the end of this blog post.


Equally striking (and visible in the hexdump above): there are clearly pointers in there. It's too early in the analysis to know whether this is a payload which gets rebased somehow, or whether there's a separate ASLR disclosure step.


On a slightly higher level this hexdump looks a little bit like an Objective-C or C++ object, though some things are strange. Why are the first 24 bytes all zero? Why isn't there an isa pointer or vtable? It looks a bit like there are a number of integer fields before the pointers, but what are they? At this stage of the analysis, I had no idea.

### Thinking dynamically

I had tried a lot to reproduce the exploit primitives on a real device; I built tooling to dynamically generate and sign legitimate PKPass files that I could send via iMessage to test devices and I could crash a lot, but I never seemed to get very far into the exploit - the iOS version range where the heap grooming works seems to be pretty small, and I didn't have an exact device and iOS version match to test on.


Regardless of what I tried: sending the original exploits via iMessage, sending custom PKPasses with the trigger and groom, rendering the WebP directly in a test app or trying to use the PassKit APIs to render the PKPass file the best I could manage dynamically was to trigger a heap metadata integrity check failure, which I assumed was indicative of the exploit failing.


(Amusingly, using the legitimate APIs to render the PKPass inside an app failed with an error that the PKPass file was malformed. And indeed, the exploit sample PKPass is malformed: it's missing multiple required files. But the "secure" PKPass BlastDoor parser entrypoint (PKPassSecurePreviewContextCreateMessagesPreview) is, in this regard at least, less strict and will attempt to render an incomplete and invalid PKPass).


Though getting the whole PKPass parsed was proving tricky, with a bit of reversing it was possible to call the correct underlying CoreGraphics APIs to render the WebP and also get the EXIF/MakerNote parsed. By then setting a breakpoint when the huffman tables were allocated I had hoped it would be obvious what the overflow target was. But it was actually totally unclear what the following object was: (Here X3 points to the start of the huffman tables which are 0x3000 bytes large)


(lldb) x/6xg $x3+0x3000

0x112000000: 0x0000000111800000 0x0000000000000000

0x112000010: 0x00000000001a1600 0x0000000000000004

0x112000020: 0x0000000000000001 0x0000000000000019


The first qword (0x111800000) is a valid pointer, but this is clearly not an Objective-C object, nor did it seem to look like any other recognizable object or have much to do with either the bplist or WebP. But running the tests a few times, there was a curious pattern:


(lldb) x/6xg $x3+0x3000

0x148000000: 0x0000000147800000 0x0000000000000000

0x148000010: 0x000000000019c800 0x0000000000000004

0x148000020: 0x0000000000000001 0x0000000000000019


The huffman table is 0x2F28 bytes, which the allocator rounds up to 0x3000. And in both of those test runs, adding the allocation size to the huffman table pointer yielded a suspiciously round number. There's no way that's a coincidence. Running a few more tests the table+0x3000 pointer is always 8MB aligned. I remembered from some presentations on the iOS userspace allocator I'd read that 8MB is a meaningful number. Here's [one from Synaktiv](https://www.synacktiv.com/ressources/Sthack_2018_Heapple_Pie.pdf):





8MB is the size of the iOS userspace default allocator's small rack regions. It looks like they might be trying to groom the allocator not to target application-specific data but allocator metadata. Time to dive into some libmalloc internals!

### libmalloc

I'd suggest reading the two presentations linked above for a good overview of the iOS default userspace malloc implementation. Libmalloc manages memory on four levels of abstraction. From largest to smallest those are: rack, magazine, region and block. The size split between the tiny, small and large racks depends on the platform. Almost all the relevant allocations for this exploit come from the small rack, so that's the one I'll focus on.


Reading through the libmalloc source I noticed that the region trailer, whilst still called a trailer, has been now moved to the start of the region object. The small region manages memory in chunks of 8MB. That 8MB gets split up in to (for our purposes) three relevant parts: a header, an array of metadata words, then blocks of 512 bytes which form the allocations:



The first 0x28 bytes are a header where the first two fields form a linked-list of small regions:


typedef struct region\_trailer {

struct region\_trailer \*prev;

struct region\_trailer \*next;

unsigned bytes\_used;

unsigned objects\_in\_use;

mag\_index\_t mag\_index;

volatile int32\_t pinned\_to\_depot;

bool recirc\_suitable;

rack\_dispose\_flags\_t dispose\_flags;

} region\_trailer\_t;

The small region manages memory in units of 512 bytes called blocks. On iOS allocations from the small region consist of contiguous runs of up to 31 blocks. Each block has an associated 16-bit metadata word called a small meta word, which itself is subdivided into a "free" flag in the most-significant bit, and a 15-bit count.


To mark a contiguous run of blocks as in-use (belonging to an allocation) the first meta word has its free flags cleared and the count set to the number of blocks in the run. On free, an allocation is first placed on a lookaside list for rapid reuse without freeing. But once an allocation really gets freed the allocator will attempt to greedily coalesce neighbouring chunks. While in-use runs can never exceed 31 blocks, free runs can grow to encompass the entire region.

### The groom

Below you can see the state of the meta words array for the small region directly following the one containing the huffman table as its last allocation:


(lldb) x/200wh 0x148000028

0x148000028: 0x0019 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000038: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000048: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000058: 0x0000 0x0003 0x0000 0x0000 0x0018 0x0000 0x0000 0x0000

0x148000068: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000078: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000088: 0x0000 0x0000 0x0000 0x0000 0x0003 0x0000 0x0000 0x001c

0x148000098: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x1480000a8: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x1480000b8: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x1480000c8: 0x0000 0x0000 0x0000 0x001d 0x0000 0x0000 0x0000 0x0000


With some simple maths we can convert indexes in the meta words array into their corresponding heap pointers. Doing that it's possible to dump the memory associated with the allocations shown above. The larger 0x19, 0x18 and 0x1c allocations all seem to be generic groom allocations, but the two 0x3 block allocations appear more interesting. The first one (with the first metadata word at 0x14800005a, shown in yellow) is the code\_lengths array which gets freed directly after the huffman table building fails. The blue 0x3 block run (with the first metadata word at 0x148000090) is the backing buffer for a CFSet object from the MakerNote and contains object pointers.


Recall that the corruption primitive will write the dword 0x270007 0x58 bytes off the end of the 0x3000 allocation (and that allocation happens to sit directly in front of this small region). That corruption has the following effect (shown in bold):


(lldb) x/200wh 0x148000028

0x148000028: 0x0019 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000038: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000048: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000058: 0x0007 0x0027 0x0000 0x0000 0x0018 0x0000 0x0000 0x0000

0x148000068: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000078: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000088: 0x0000 0x0000 0x0000 0x0000 0x0003 0x0000 0x0000 0x001c

0x148000098: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x1480000a8: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x1480000b8: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x1480000c8: 0x0000 0x0000 0x0000 0x001d 0x0000 0x0000 0x0000 0x0000


It's changed the size of an in-use allocation from 3 blocks to 39 (or from 1536 to 19968 bytes). I mentioned before that the maximum size of an in-use allocation is meant to be 31 blocks, but this doesn't seem to be checked in every single free path. If things don't quite work out, you'll hit a runtime check. But if things do work out you end up with a situation like this:


(lldb) x/200wh 0x148000028

0x148000028: 0x0019 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000038: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000048: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000058: 0x0007 0x8027 0x0000 0x0000 0x0018 0x0000 0x0000 0x0000

0x148000068: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000078: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000088: 0x0000 0x0000 0x0000 0x0000 0x0003 0x0000 0x0000 0x001c

0x148000098: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x8027

0x1480000a8: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x1480000b8: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x1480000c8: 0x0000 0x0000 0x0000 0x001d 0x0000 0x0000 0x0000 0x0000


The yellow (0x8027) allocation now extends beyond its original three blocks and completely overlaps the following green (0x18) and blue (0x3) as well as the start of the purple (0x1c) allocation.


But as soon as this corruption occurs WebP parsing fails and it's not going to make any other allocations. So what are they doing? How are they able to leverage these overlapping allocations? I was pretty stumped.


One theory was that perhaps it was some internal ImageIO or BlastDoor specific object which reallocated the overlapping memory. Another theory was that perhaps the exploit had two parts; this first part which puts overlapping entries on the allocator freelist, then another file which is sent to exploit that? And maybe I was lacking that file? But then, why would there be that huge 1MB payload with NSExpressions in it? That didn't add up.

### Puzzling pieces

As is so often the case, stepping back and not thinking about the problem for a while I realised that I'd completely overlooked and forgotten something critical. Right at the very start of the analysis I had run file on all the files inside the PKPass and noted that background.png was actually not a png but a TIFF. I had then completely forgotten that. But now the solution seemed obvious: the reason to use a PKPass versus just a WebP is that the PKPass parser will render multiple images in sequence, and there must be something in the TIFF which reallocates the overlapping allocation with something useful.


[Libtiff](http://www.libtiff.org/) comes with a suite of tools for parsing tiff files. tiffdump displays the headers and EXIF tags:


$ tiffdump background-15.tiff

background-15.tiff:

Magic: 0x4d4d \<big-endian> Version: 0x2a \<ClassicTIFF>

Directory 0: offset 68 (0x44) next 0 (0)

ImageWidth (256) SHORT (3) 1\<48>

ImageLength (257) SHORT (3) 1\<16>

BitsPerSample (258) SHORT (3) 4\<8 8 8 8>

Compression (259) SHORT (3) 1\<8>

Photometric (262) SHORT (3) 1\<2>

StripOffsets (273) LONG (4) 1\<8>

Orientation (274) SHORT (3) 1\<1>

SamplesPerPixel (277) SHORT (3) 1\<4>

StripByteCounts (279) LONG (4) 1\<59>

PlanarConfig (284) SHORT (3) 1\<1>

ExtraSamples (338) SHORT (3) 1\<2>

700 (0x2bc) BYTE (1) 15347\<00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ...>

33723 (0x83bb) UNDEFINED (7) 15347\<00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ...>

34377 (0x8649) BYTE (1) 15347\<00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ...>

ICC Profile (34675) UNDEFINED (7) 15347\<00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ...>


The presence of the four 15KB buffers is notable, but they seemed to mostly just be zeros. Here's the output from tiffinfo:


$ tiffinfo -c -j -d -s -z background-15.tiff

=== TIFF directory 0 ===

TIFF Directory at offset 0x44 (68)

Image Width: 48 Image Length: 16

Bits/Sample: 8

Compression Scheme: AdobeDeflate

Photometric Interpretation: RGB color

Extra Samples: 1\<unassoc-alpha>

Orientation: row 0 top, col 0 lhs

Samples/Pixel: 4

Planar Configuration: single image plane

XMLPacket (XMP Metadata):


RichTIFFIPTC Data: \<present>, 15347 bytes

Photoshop Data: \<present>, 15347 bytes

ICC Profile: \<present>, 15347 bytes

1 Strips:

0: \[ 8, 59\]

Strip 0:

00 00 00 00 00 00 00 00 84 13 00 00 01 00 00 00 01 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

cd ab 34 12 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

...


This dumps the uncompressed TIFF strip buffer and this looks much more interesting! There's clearly some structure, though not a lot of it. Is this really enough to do something useful? It looks like there could be some sort of object, but I didn't recognise the structure, and had no idea how replacing an object with this would be useful. I explored two possibilities:

#### 1) Alpha blending:

This is actually the raw TIFF strip after decompression but before the rendering step which applies the [alpha](https://en.wikipedia.org/wiki/Alpha_compositing), so it was possible that this got rendered "on top" of another object. That seemed like a reasonable explanation for why the object seemed so sparse; perhaps the idea was to just "move" a pointer value. The first 16 bytes of the strip look like this:


00 00 00 00 00 00 00 00 84 13 00 00 01 00 00 00


which when viewed as two 64-bit values look like this:


0x0000000000000000 0x0000000100001384


It seemed sort-of plausible that rendering the 0x100001384 on top of another pointer might be a neat primitive, but there was something that didn't quite add up. This pointer-ish value is at the start of the strip buffer, so if the overlapping allocation got reallocated with this strip buffer directly, nothing interesting would happen, as the overlapping parts are further along. Maybe the overlapping buffer gets split up multiple times, but this was seeming less and less likely, and I couldn't reproduce this part of the exploit to actually observe what happened.

#### 2) This is an object:

The other theory I had was that this actually was an object. The 8 zero bytes at the start were certainly strange… so then what's the significance of the next 8 bytes?


84 13 00 00 01 00 00 00


I tried using lldb's memory find command to see if there were other instances of that exact byte sequence occurring in a test iOS app rendering the WebP then the TIFF using the CoreGraphics APIs:


(lldb) memory find -e 0x100001384 -- 0x100000000 0x200000000

data not found within the range.


Nope, plus it was very, very slow.


One thing I had noticed was that this byte sequence was similar to one near the start of the 1MB groom object:


00000000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|

00000010 00 00 00 00 00 00 00 00 80 26 00 00 01 00 00 00 |.........&......|

00000020 1f 00 00 00 00 00 00 00 10 00 8b 56 02 00 00 00 |...........V....|

00000030 b0 c3 31 16 02 00 00 00 60 e3 01 00 00 00 00 00 |..1.....\`.......|


They're not identical, but it seemed a strange coincidence.


I took a bunch of test app core dumps using lldb's process save-core command and wrote some simple code to search for similar-ish byte patterns. After some experimentation I managed to find something:


1c7b2600 49 d2 e4 29 02 00 00 01 84 13 00 00 02 00 00 00 |I..)............|

1c7b2610 42 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |B...............|

1c7b2620 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|

1c7b2630 c0 92 d6 83 02 00 00 00 00 93 d6 83 02 00 00 00 |................|


Converting those coredump offsets into VM address and looking them up revealed:


(lldb) x/10xg 0x121E47600

0x121e47600: 0x0100000229e4d249 0x0000000200001384

0x121e47610: 0x0000000000000042 0x0000000000000000

0x121e47620: 0x0000000000000000 0x0000000000000000


(lldb) image lookup --address 0x229e4d248

Address: CoreFoundation\[0x00000001dceed248\] (CoreFoundation.\_\_DATA\_DIRTY.\_\_objc\_data + 7800)

Summary: (void \*)0x0000000229e4d0e0: \_\_NSCFArray


It's an NSCFArray, which is the Foundation (Objective-C) "[toll-free bridged](https://ridiculousfish.com/blog/posts/bridge.html)" version of the Core Foundation (C) CFArray type! This was the hint that I was looking for to identify the significance of the TIFF and that 1MB groom object, which also contains a similar byte sequence.

### Cores and Foundations

Even though Apple hasn't updated the open-source version of CoreFoundation for almost a decade, the old source is still helpful. Here's what a CoreFoundation object looks like:


/\* All CF "instances" start with this structure. Never refer to

\* these fields directly -- they are for CF's use and may be added

\* to or removed or change format without warning. Binary

\* compatibility for uses of this struct is not guaranteed from

\* release to release.

\*/

typedef struct \_\_CFRuntimeBase {

uintptr\_t \_cfisa;

uint8\_t \_cfinfo\[4\];

#if \_\_LP64\_\_

uint32\_t \_rc;

#endif

} CFRuntimeBase;

So the header is an Objective-C [isa](https://alwaysprocessing.blog/2023/01/19/objc-class-isa) pointer followed by four bytes of \_cfinfo, followed by a reference count. Taking a closer look at the uses of \_\_cfinfo:


CF\_INLINE CFTypeID \_\_CFGenericTypeID\_inline(const void \*cf) {

// yes, 10 bits masked off, though 12 bits are

// there for the type field; \_\_CFRuntimeClassTableSize is 1024

uint32\_t \*cfinfop = (uint32\_t \*)&(((CFRuntimeBase \*)cf)->\_cfinfo);

CFTypeID typeID = (\*cfinfop >> 8) & 0x03FF; // mask up to 0x0FFF

return typeID;

}

It seems that the second byte in \_\_cfinfo is a type identifier. And indeed, running expr (int) CFArrayGetTypeID() in lldb prints: 19 (0x13) which matches up with both the object found in the coredump as well as the strange (or now not so strange) object in the TIFF strip buffer.

### X steps forwards, Y steps back

Looking through more of the CoreFoundation code it seems that the object in the TIFF strip buffer is a CFArray with inline storage containing one element with the value 0x1234abcd. It also seems that it's possible for CF objects to have NULL isa pointers, which explains why the first 8 bytes of the fake object are zero.


This is interesting, but it still doesn't actually get us any closer to figuring out what the next step of the exploit actually is. If the CFArray is meant to overlap with something, then what? And what interesting side-effects could having an CFArray with only a single element with the value 0x1234abcd possibly have?


This seems like one step forward and two steps back, but there's something else which we can now figure out: what that 1MB groom object actually is. Let's take a look at the start of it again:


00000000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|

00000010 00 00 00 00 00 00 00 00 80 26 00 00 01 00 00 00 |.........&......|

00000020 1f 00 00 00 00 00 00 00 10 00 8b 56 02 00 00 00 |...........V....|

00000030 b0 c3 31 16 02 00 00 00 48 e3 01 00 00 00 00 00 |..1.....H.......|

00000040 20 ec 46 58 02 00 00 00 00 00 00 00 00 00 00 00 | .FX............|

00000050 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|

00000060 00 00 00 00 00 00 00 00 60 bf 31 16 02 00 00 00 |........\`.1.....|

00000070 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|


It looks like another CF object, starting at +0x10 in the buffer with the same NULL isa pointer, a reference count of 1 and a \_\_cfinfo of {0x80, 0x26, 0, 0}. The type identifiers aren't actually fixed, they're allocated dynamically via calls to \_CFRuntimeRegisterClass like this:


CFTypeID CFArrayGetTypeID(void) {

static dispatch\_once\_t initOnce;

dispatch\_once(&initOnce, ^{ \_\_kCFArrayTypeID = \_CFRuntimeRegisterClass(&\_\_CFArrayClass); });

return \_\_kCFArrayTypeID;

}

The CFTypeIDs are really just indexes into the \_\_CFRuntimeClassTable array, and even though the types are allocated dynamically the ordering seems sufficiently stable that the hardcoded type values in the exploit work. 0x26 is the CFTypeID for CFReadStream:


struct \_CFStream {

CFRuntimeBase \_cfBase;

CFOptionFlags flags;

CFErrorRef error;

struct \_CFStreamClient \*client;

void \*info;

const struct \_CFStreamCallBacks \*callBacks;

CFLock\_t streamLock;

CFArrayRef previousRunloopsAndModes;

dispatch\_queue\_t queue;

};

Looking through the CFStream code it seems to call various callback functions during object destruction — that seems like a very likely path towards code execution, though with some significant caveats:


Caveat I: It's still unclear how an overlapping allocation in the small malloc region could lead to a CFRelease being called on this 1MB allocation.


Caveat II: What about ASLR? There have been some tricks in the past targeting "universal gadgets" which work across multiple slides. Nemo also had [a neat objective-c trick](http://www.phrack.org/issues/69/9.html) for defeating ASLR in the past, so it's plausible that there's something like that here.


Caveat III: What about PAC? If it's a data-only attack then maybe PAC isn't an issue, but if they are trying to JOP they'd need a trick beyond just an ASLR leak, as all forward control flow edges should be protected by PAC.

### Special Delivery

Around this time in my analysis [Matthias Frielingsdorf](https://x.com/helthydriver) offered me the use of an iPhone running 16.6, the same version as the targeted ITW victim. With Matthias' vulnerable iPhone, I was able to use the [Dopamine](https://ellekit.space/dopamine/) jailbreak to attach lldb to MessagesBlastDoorService and after a few tries was able to reproduce the exploit right up to the CFRelease call on the fake CFReadStream, confirming that that part of my analysis was correct!


Collecting a few crashes led, yet again, to even more questions...

### Caveat I: Mysterious Pointers


Similar to the analysis of the huffman tables, there was a clear pattern in the fake object pointers, which this time were even stranger than the huffman tables. The crash site was here:


LDR X8, \[X19,#0x30\]

LDR X8, \[X8,#0x58\]

At this point X19 points to the fake CFReadStream object, and collecting a few X19 values there's a pretty clear pattern:


0x000000075f000010

0x0000000d4f000010


The fake object is inside a 1MB heap allocation, but all those fake object addresses are always 16 bytes above a 16MB-aligned address. It seemed really strange to me to end up with a pointer 0x10 bytes past such a round number. What kind of construct would lead to the creation of such a pointer? Even though I did have a debugger attached to MessagesBlastDoorService, it wasn't a time-travel debugger, so figuring out the history of such a pointer was non-trivial. Using the same core dump analysis techniques I could see that the pointer which would end up in X19 was also present in the backing buffer of the CFSet described earlier. But how did it get there?


Having found the strange CFArray inside the TIFF I was heavily biased towards believing that this must have something to do with it, so I wrote some tooling to modify the fake CFArray's in the TIFF in the exploit. The theory was that by messing with that CFArray, I could cause a crash when it was used and figure out what was going on. But making minor changes to the strip buffer didn't seem to have any effect — the exploit still worked! Even replacing the entire strip buffer with A's didn't stop the exploit working... What's going on?

### Stepping back

I had made a list of the primitives I thought might lead to the creation of such a strange looking pointer — first on the list was a partial pointer overwrite. But then why the CFArray? But now having shown that the CFArray can't be involved, it was time to go back to the list. And step back even further and make sure I'd really looked at all of that TIFF...


There were still those four other metadata buffers in the tiffdump output I'd shown earlier:


700 (0x2bc) BYTE (1) 15347\<00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ...>

33723 (0x83bb) UNDEFINED (7) 15347\<00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ...>

34377 (0x8649) BYTE (1) 15347\<00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ...>

ICC Profile (34675) UNDEFINED (7) 15347\<00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ...>


I'd just dismissed them, but, maybe I shouldn't have done that? I had actually already dumped the full contents of each of those buffers and checked that there wasn't something else apart from the zeros. They were all zeros, except the third-to-last bytes which were 0x10, which I'd considered completely uninteresting. Uninteresting, unless you wanted to partially overwrite the three least-significant bytes of a little-endian pointer value with 0x000010 that is!


Let's look back at the SMALL metadata:


0x148000058: 0x0007 0x8027 0x0000 0x0000 0x0018 0x0000 0x0000 0x0000

0x148000068: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000078: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000088: 0x0000 0x0000 0x0000 0x0000 0x0003 0x0000 0x0000 0x001c

0x148000098: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x8027


Each of those four metadata buffers in the TIFF is 15347 bytes, which is 0x3bf3 — looked at another way that's 0x3c00 (the size rounded up to the next 0x200 block size), minus 5, minus 8.


0x3c00 is exactly 30 0x200 byte blocks. Each 16-bit word in the metadata array shown above corresponds to one 0x200 block, where the overlapping chunk in yellow starts at 0x14800005a. Counting forwards 30 chunks means that the end of a 0x3c00 allocation overlaps perfectly with the end of the original blue three-chunk allocation:


0x148000058: 0x0007 0x8027 0x0000 0x0000 0x0018 0x0000 0x0000 0x0000

0x148000068: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000078: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000

0x148000088: 0x0000 0x0000 0x0000 0x0000 0x0003 0x0000 0x0000 0x001c

0x148000098: 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x0000 0x8027


This has the effect of overwriting all but the last 16 bytes of the blue allocation with zeros, then overwriting the three least-significant bytes of the second-to-last pointer-sized value with 0x10 00 00; which, if that memory happened to contain a pointer, has the effect of "shifting" that pointer down to the nearest 16MB boundary, then adding 0x10 bytes! (For those who saw my [2024 Offensivecon talk](https://www.youtube.com/watch?v%3DZawX9I9MM6Y), this was the missing link between the overlapping allocations and code execution I mentioned.)



As mentioned earlier, that blue allocation starting with 0x0003 is the backing buffer of a CFSet object from the bplist inside the WebP MakerNote. The set is constructed in a very precise fashion such that the target pointer (the one to be rounded down) ends up as the second-to-last pointer in the backing buffer. The 1MB object is then also groomed such that it falls on a 16MB boundary below the object which the CFSet entry originally points to. Then when that CFSet is destructed it calls CFRelease on each object, causing the fake CFReadStream destructor to run.

### Caveat II: ASLR

We've looked at the whole flow from huffman table overflow to CFRelease being invoked on a fake CFReadStream — but there's still stuff missing. The second open question I discussed earlier was ASLR. I had theorised that maybe it used a trick like a universal gadget, but is that the case?


In addition to the samples, I was also able to obtain a number of crash logs from failed exploit attempts where those samples were thrown, which meant I could figure out the ASLR slide of the MessagesBlastDoorService when the exploit failed. In combination with the target device and exact OS build (also contained in the crash log) I could then obtain the matching dyld\_shared\_cache, subtract the runtime ASLR slide from a bunch of the pointer-looking things in the 1MB object and take a look at them.


The simple answer is: the 1MB object contains a large number of hardcoded, pre-slid, valid pointers. There's no weird machine, tricks or universal gadget here. By the time the PKPass is built and sent by the attackers they already know both the target device type and build as well as the runtime ASLR slide of the MessagesBlastDoorService...


Based on [analysis by iVerify](https://iverify.io/post/clipping-wings-our-analysis-of-a-pegasus-spyware-sample), as well as analysis of [earlier exploit chains published by Citizen Lab](https://citizenlab.ca/2023/04/nso-groups-pegasus-spyware-returns-in-2022/), my current working theory is that the large amount of HomeKit traffic seen in those cases is likely a separate ASLR/memory disclosure exploit.

### Caveat III: Pointer Authentication

In the years since PAC was introduced we've seen a whole spectrum of interesting ways to either defeat, or just avoid, PAC. So what did these attackers do? To understand that let's follow the CFReadStream destruction code closely. (All these code snippets are from the most recently available version of CF from 2015, but the code doesn't seem to have changed much.)


Here's the definition of the CFReadStream:


static const CFRuntimeClass \_\_CFReadStreamClass = {

0,

"CFReadStream",

NULL, // init

NULL, // copy

\_\_CFStreamDeallocate,

NULL,

NULL,

NULL, // copyHumanDesc

\_\_CFStreamCopyDescription

};

When a CFReadStream is passed to CFRelease, it will call \_\_CFStreamDeallocate:


static void \_\_CFStreamDeallocate(CFTypeRef cf) {

struct \_CFStream \*stream = (struct \_CFStream \*)cf;

const struct \_CFStreamCallBacks \*cb =

\_CFStreamGetCallBackPtr(stream);

CFAllocatorRef alloc = CFGetAllocator(stream);

\_CFStreamClose(stream);

\_CFStreamGetCallBackPtr just returns the CFStream's callBacks field:


CF\_INLINE const struct \_CFStreamCallBacks \*\_CFStreamGetCallBackPtr(struct \_CFStream \*stream) {

return stream->callBacks;

}

Here's \_CFStreamClose:


CF\_PRIVATE void \_CFStreamClose(struct \_CFStream \*stream) {

CFStreamStatus status = \_CFStreamGetStatus(stream);

const struct \_CFStreamCallBacks \*cb =

\_CFStreamGetCallBackPtr(stream);

if (status == kCFStreamStatusNotOpen ||

status == kCFStreamStatusClosed ||

(status == kCFStreamStatusError &&

\_\_CFBitIsSet(stream->flags, HAVE\_CLOSED)

))

{

// Stream is not open from the client's perspective;

// do not callout and do not update our status to "closed"

return;

}

if (! \_\_CFBitIsSet(stream->flags, HAVE\_CLOSED)) {

\_\_CFBitSet(stream->flags, HAVE\_CLOSED);

\_\_CFBitSet(stream->flags, CALLING\_CLIENT);

if (cb->close) {

cb->close(stream, \_CFStreamGetInfoPointer(stream));

}



\_CFStreamGetStatus extracts the status bitfield from the flags field:


#define \_\_CFStreamGetStatus(x) \_\_CFBitfieldGetValue((x)->flags, MAX\_STATUS\_CODE\_BIT, MIN\_STATUS\_CODE\_BIT)

Looking at the 1MB object again the flags field is the first non-base field:


00000000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|

00000010 00 00 00 00 00 00 00 00 80 26 00 00 01 00 00 00 |.........&......|

00000020 1f 00 00 00 00 00 00 00 10 00 8b 56 02 00 00 00 |...........V....|

00000030 b0 c3 31 16 02 00 00 00 48 e3 01 00 00 00 00 00 |..1.....H.......|

00000040 20 ec 46 58 02 00 00 00 00 00 00 00 00 00 00 00 | .FX............|

00000050 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|

00000060 00 00 00 00 00 00 00 00 60 bf 31 16 02 00 00 00 |........\`.1.....|

00000070 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|


That gives a status code of 0x1f with all the other flags bits clear. This gets through the two conditional branches to reach this close callback call:



if (cb->close) {

cb->close(stream, \_CFStreamGetInfoPointer(stream));

}


At this point we need to switch to looking at the assembly to see what's really happening:


\_\_CFStreamClose


var\_30= -0x30

var\_20= -0x20

var\_10= -0x10

var\_s0= 0


PACIBSP

STP X24, X23, \[SP,#-0x10+var\_30\]!

STP X22, X21, \[SP,#0x30+var\_20\]

STP X20, X19, \[SP,#0x30+var\_10\]

STP X29, X30, \[SP,#0x30+var\_s0\]

ADD X29, SP, #0x30

MOV X19, X0

BL \_\_CFStreamGetStatus

CBZ X0, loc\_187076958

The fake CFReadStream is the first argument to this function, so passed in the X0 register. It's then stored into X19 so it survives the call to \_\_CFStreamGetStatus.


Skipping ahead past the flag checks we reach the callback callsite (this is also the crash site seen earlier):


LDR X8, \[X19,#0x30\]

...

LDR X8, \[X8,#0x58\]

CBZ X8, loc\_187076758

LDR X1, \[X19,#0x28\]

MOV X0, X19

BLRAAZ X8

Let's walk through each instruction in turn there:


First it loads the 64-bit value from X19+0x30 into X8:


LDR X8, \[X19,#0x30\]

Looking at the hexdump of the 1MB object above this will load the value 0x25846ec20.


From the crash reports we know the runtime ASLR slide of the MessagesBlastDoorService when this exploit was thrown was 0x3A8D0000, so subtracting that we can figure out where in the shared cache this pointer should point:


0x25846ec20-0x3A8D0000=0x21DB9EC20


It points into the \_\_const segment of the TextToSpeechMauiSupport library in the shared cache:



The next instruction adds 0x58 to that TextToSpeechMauiSupport pointer and reads a 64-bit value from there:


LDR X8, \[X8,#0x58\] // x8 := \[0x21DB9EC20+0x58\]

This loads the pointer to the function \_DataSectionWriter\_CommitDataBlock from 0x21DB9EC78.


IDA is simplifying something for us here: the function pointer loaded there is actually signed with the [A-family instruction key](/2019/02/examining-pointer-authentication-on.html) [with a zero context](/2019/02/examining-pointer-authentication-on.html). This signing happens transparently (either during load or when the page is faulted in).


The remaining four instructions then check that the pointer wasn't NULL, load X1 from offset +0x28 in the fake 1MB object, move the pointer to the fake object back into X0 and call the PAC'ed \_DataSectionWriter\_CommitDataBlock function pointer via BLRAAZ:


CBZ X8, loc\_187076758

LDR X1, \[X19,#0x28\]

MOV X0, X19

BLRAAZ X8

### Callback-Oriented Programming

A well-known attack against PAC is to swap two valid, PAC'ed pointers which are signed in the same way but point to different places (e.g. swapping two function pointers with different semantics, allowing you to exploit those semantic differences).


Since a large number of PAC-protected pointers are signed with the A-family instruction key with a zero-context value, there are a large number of pointers to choose from. "Just" having an ASLR defeat shouldn't be enough to achieve this though; surely you'd need to disclose the actual PAC'ed pointer value? But that's not what happened above.


Notice that the CFStream objects don't directly contain the callback function pointers — there's an extra level of indirection. The CFStream object contains a pointer to a callback structure, and that structure has the PAC'd function pointers. And crucially: that first pointer, the one to the callbacks structure, isn't protected by PAC. This means that the attackers can freely swap pointers to callback structures, operating one-level removed from the function pointers.


This might seem like a severe constraint, but the dyld\_shared\_cache is vast and there are easily enough pre-existing callback structures to build a "callback-oriented JOP" chain, chaining together unsigned pointers to signed function pointers.


The initial portion of the payload is a large callback-oriented JOP chain which is used to bootstrap the evaluation of the next payload stage, a large NSExpression.

### Similarities

There are a number of similarities between this exploit chain and PWNYOURHOME, an earlier exploit also attributed by CitizenLab to NSO, [described in this blog post in April 2023](https://citizenlab.ca/2023/04/nso-groups-pegasus-spyware-returns-in-2022/).


That chain also had an initial stage targeting HomeKit, followed by a stage targeting MessagesBlastDoorService and also involving a MakerNote object — the Citizen Lab post claims that at the time the MakerNote was inside a PNG file. My guess would be that that PNG was being used as the delivery mechanism for the MakerNote bplist heap grooming primitives discussed in this post.


Based on Citizen Lab's description it also seems like PWNYOURHOME was leveraging a similar callback-oriented JOP technique, and it seems likely that there was also a HomeKit-based ASLR disclosure. The PWNYOURHOME post has a couple of extra details around a minor fix which Apple made, preventing parsing of "certain HomeKit messages unless they arrive from a plausible source." But there still aren't enough details to figure out the underlying vulnerability or primitive. It seems likely to me that the same issue, or a variant thereof was still in use in BLASTPASS.

### Key material

Matthias from iVerify presented an [initial analysis of the NSExpression payload at BlackHat Asia](https://i.blackhat.com/Asia-24/Asia-24-Frielingsdorf-YouShallNotPassAnalysing.pdf) in April 2024. In early July 2024, Matthias and I took a closer look at the final stages of the NSExpression payload which decrypts an AES-encrypted NSExpression and executes it.


It seems very likely that the encrypted payload contains a BlastDoor sandbox escape. Although the BlastDoor sandbox profile is fairly restrictive it still allows access to a number of system services like notifyd, logd and mobilegestalt. In addition to the syscall attack surface there's also a non-trivial IOKit driver attack surface:


...

(allow iokit-open-user-client

(iokit-user-client-class "IOSurfaceRootUserClient")

(iokit-user-client-class "IOSurfaceAcceleratorClient")

(iokit-user-client-class "AGXDevice"))

(allow iokit-open-service)

(allow mach-derive-port)

(allow mach-kernel-endpoint)

(allow mach-lookup

(require-all

(require-not (global-name "com.apple.diagnosticd"))

(require-any

(global-name "com.apple.logd")

(global-name "com.apple.system.notification\_center")

(global-name "com.apple.mobilegestalt.xpc"))))

...

(This profile snippet was generated using the [Cellebrite labs' fork of SandBlaster](https://github.com/cellebrite-labs/sandblaster))


In FORCEDENTRY the sandbox escape was contained directly in the NSExpression payload (though that was an escape from the less-restrictive IMTranscoderAgent sandbox). This time around it seems extra care has been taken to prevent analysis of the sandbox escape.


The question is: where does the key come from? We had a few theories:

- Perhaps the key is just obfuscated, and by completely reversing the NSExpression payload we can find it?
- Perhaps the key is derived from some target-specific information?
- Perhaps the key was somehow delivered in some other way and can be read from inside BlastDoor?


We spent a day analysing the NSExpression payload and concluded that the third theory appeared to be the correct one. The NSExpression walks up the native stack looking for the communication ports back to imagent. It then hijacks that communication, effectively taking over responsibility for parsing all subsequent incoming requests from imagent for "defusing" of iMessage payloads. The NSExpression loops 100 times, parsing incoming requests as XPC messages, reading the request xpc dictionary then the data xpc data object to get access to the raw, binary iMessage format. It waits until the device receives another iMessage with a specific format, and from that message extracts an AES key which is then used to decrypt the next NSExpression stage and evaluate it.


We were unable to recover any messages with the matching format and therefore unable to analyse the next stage of the exploit.

### Conclusion

In contrast to FORCEDENTRY, BLASTPASS's separation of the ASLR disclosure and RCE phases mitigated the need for a novel weird machine. Whilst the heap groom was impressively complicated and precise, the exploit still relied on well-known exploitation techniques. Furthermore, the MakerNote bplist groom and callback-JOP PAC defeat techniques appear to have been in use for multiple years, based on similarities with [Citizenlab's blogpost in 2023](https://citizenlab.ca/2023/04/nso-groups-pegasus-spyware-returns-in-2022/), which looked at devices compromised in 2022.


Enforcing much stricter requirements on the format of the bplist inside the MakerNote (for example: a size limit or a strict-parser mode which rejects duplicate keys) would seem prudent. The callback-JOP issue is likely harder to mitigate.


The HomeKit aspect of the exploit chain remains mostly a mystery, but it seems very likely that it was somehow involved in the ASLR disclosure. [Samuel Groß's post "A Look at iMessage in iOS 14"](/2021/01/a-look-at-imessage-in-ios-14.html) in 2021, mentioned that Apple added support for re-randomizing the shared cache slide of certain services. Ensuring that BlastDoor has a unique ASLR slide could be a way to mitigate this.


This is the second in-the-wild NSO exploit which relied on simply renaming a file extension to access a parser in an unexpected context which shouldn't have been allowed.


FORCEDENTRY had a .gif which was really a .pdf.


BLASTPASS had a .png which was really a .webp.


A basic principle of sandboxing is treating all incoming attacker-controlled data as untrusted, and not simply trusting a file extension.


This speaks to a broader challenge in sandboxing: that current approaches based on process isolation can only take you so far. They increase the length of an exploit chain, but don't necessarily reduce the size of the initial remote attack surface. Accurately mapping, then truly reducing the scope of that initial remote attack surface should be a top priority.
