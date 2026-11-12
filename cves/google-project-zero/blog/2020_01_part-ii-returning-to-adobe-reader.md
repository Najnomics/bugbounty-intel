# Part II: Returning to Adobe Reader symbols on macOS - Project Zero

Source: https://projectzero.google/2020/01/part-ii-returning-to-adobe-reader.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Mateusz Jurczyk, Project Zero


In a blog post titled ["The story of Adobe Reader symbols"](/2019/10/the-story-of-adobe-reader-symbols.html) published in October 2019, I presented an analysis of the debug symbols shipped with some older versions of Adobe Reader for Unix-family systems released between 1997-2013. Such symbols can prove immensely useful for both understanding the inner workings of various Reader components while reverse engineering, and for automated tasks such as crash classification and deduplication in fuzzing projects. In that blog post, I only briefly mentioned the macOS Reader packages as containing up-to-date symbols for the JP2K and 3D components, but missing any other interesting information beyond that. Upon a closer and more thorough inspection of the Mac releases, I have discovered that in fact more debug metadata made its way to the publicly available installers, some of which is unique (i.e. not present in other symbol sources) and/or more recent than the latest Unix symbols. Considering the added value of this new data, I wish to share it with you here in this follow-up post. As a reminder, legacy builds of Adobe Reader dating back to the '90s can be downloaded from the official ftp.adobe.com FTP server and the corresponding paths on the ardownload.adobe.com HTTP server.

## Review of core Acrobat Mach-O images

Below is a breakdown of the six core components of Reader for macOS, and whether they included symbols in each of the existing software releases. For brevity and readability, the table starts with version 7.x from 2005, as this is where the debug information started making first appearances:

¹ See detailed 8.x version breakdown

² See detailed 9.x version breakdown

³ Up to version 15.016.20045, stripped afterwards

As mentioned in the annotations, the presence of symbols for some modules varied greatly between minor versions of the 8.x and 9.x releases (the reason for which is unclear to me). Detailed tables for these two major versions are shown below:



Clearly, there is a lot of useful information hidden in the Reader Mach-O executables, with versions 8.x and 9.x being the most ripe with debug data. I find the following pieces of information to be the most useful and unique compared to the data previously extracted from the Unix files:


- Private symbols in the[stabs](https://sourceware.org/gdb/current/onlinedocs/stabs/) format for the 3D module (version 7.x) and the CoolType font engine (most 9.x versions). This includes not only function and global variable names, but also source file paths, source line numbers corresponding to blocks of assembly code, local variable names, definitions of structures, enums etc. This kind of metadata provides us with some extremely detailed and accurate insight into how the code works. To my best knowledge, such private symbols for these two libraries are not known to be available from any other public source and may therefore be a great assistance to anyone interested in their inner workings.
- The symbols for the Acrobat, AGM, CoolType and BIB modules in versions 8.x and 9.x are generally more recent than the most recent symbols on the Unix side. Furthermore, for the purpose of crash deduplication or root cause analysis, it is arguably easier to run Reader 9 on macOS than Reader 9 on SunOS/Solaris, or Reader 7 on AIX/HP-UX, simply because it is the more common platform.
- Lastly, the AGM component was not stripped in the DC versions between 15.006.30033 (March 2015) to 15.016.20045 (June 2016), which is also a much more recent source of information than what was previously accessible (AIX/HP-UX symbols for versions 7.x from 2007).


Out of all of them, I believe that the private CoolType symbols carry the most interesting and practical information. What makes it especially attractive is the fact that it is not only applicable to Reader and other Adobe products, but also to all other libraries and system components which share the same font rasterization code – such as the Windows kernel drivers (win32k.sys, atmfd.dll), the Windows DirectWrite library (dwrite.dll), the macOS font libraries (libTrueTypeScaler.dylib, libType1Scaler.dylib), and the JRE t2k font rasterizer (libt2k.so etc.). Let's have a deeper look into the kind of data found in the debug builds of AdobeCoolType and how we can extract it and use it in a meaningful way.

## Digging into the CoolType symbols

In total, I have found 17 unique AdobeCoolType files in various versions of Reader 9.x which contain debug data in the stabs format. The format is a largely textual one, so if we glance at the end of the analyzed file, we should see data similar to the following dump:



That particular snippet shows names from the open-source [AFDKO](https://github.com/adobe-type-tools/afdko) library, which is compiled into CoolType. Other parts of the debug section reveal more interesting and less public data, such as the detailed stack layout of Type1InterpretCharString, the main Postscript CharString interpreter function shown to be subject to a [number of bugs in 2015](/2015/07/one-font-vulnerability-to-rule-them-all.html):



The amount of information is stunning – within a 6.35 MB AdobeCoolType file from Reader 9.5.5, around 1.78 MB is consumed just by debug strings of various kinds. Unfortunately, IDA Pro or Ghidra don't seem to parse stabs, so while we will see the names of functions and globals in these disassemblers, types (structures, unions, enums, typedefs) and local variable names unfortunately won't be imported. If I missed some way to have these symbols loaded into the database, let me know!


The two tools I have successfully used to load stabs are the old OS X objdump and gdb utilities, with the latter being especially powerful. In my test environment, I have Adobe Reader 9.5.5 installed on Mac OS 10.6.8 (Snow Leopard). When I then start Reader under gdb, I see the following output:



The debugger successfully loads the application and embedded symbols, but it complains about missing object and source files – expecting them to exist as such a build would typically be used for debugging on a developer's machine. At this point, we can conveniently dump various types of general information with the following gdb commands:


- info functions – list all functions found in the loaded modules, or print information about a specific function
- info line – print information about a specific line in the source code file (i.e. which assembly regions it corresponds to)
- info sources – list source file names
- info types – list all known types
- info variables – list all global and static variable names


This already gives us plenty of information; for example, let's go back to our favourite function and look it up:



We can set a breakpoint on it and learn in which line in the source code it is declared:



We can get some more information on that specific line:



Finally, we can check the definition of one of the function argument types, for example the PFontInst structure pointer:



### Analyzing issue #1888 (CVE-2019-8048)

Enumerating the global information may prove very informative and bring answers to a number of questions one could have had while reverse engineering font rasterizers. However, the true power of the symbols lies in the context information available during live debugging. In the previous blog post, we tried to recover the stack trace upon triggering a crash with the PoC for [issue #1888](https://bugs.chromium.org/p/project-zero/issues/detail?id=1888). This is how far we got:



When we load the same PDF in Adobe Reader 9.5.5 for macOS, here is what we will see under gdb:



Now that is a much more detailed call stack – we can see the names of the ancestors of ATMBuildBitMap, and we have access to almost complete type/locals information.


### Analyzing issue #1891 (CVE-2019-8042)

As another example, let's take a CoolType crash in TrueType font processing reported in [issue #1891](https://bugs.chromium.org/p/project-zero/issues/detail?id=1891). When we open poc.pdf in Reader, we get the following crash:



Once again, we can obtain a very verbose stack trace:



If we wish to dig deeper and analyze the root cause of the problem, we may start with establishing the origin of the unmapped 0x0a68d4cc address. The arguments of the top-level fsg\_QueryTwilightElement function are:


The 0x0a68d4cc and 0xa69b008 addresses are close to each other, with a difference of 56124 bytes between them, so we might expect that the former is calculated based on the latter. Let's look into the second parameter to see if we find any clues that would align with the existing data:



Two of the structure fields seem unusually large, what do they look like as signed numbers?



We found the culprit! If we open the fsg\_QueryTwilightElement function in a disassembler, we can confirm that this is indeed how the invalid pointer is constructed prior to being dereferenced. We could now decide to continue the analysis to learn why the two fields are assigned out-of-bounds values and what the root cause of the problem is, or leave it at that and provide the extra bit of information to the vendor while reporting the bug.

## Conclusion

As we can see, working with debug metadata can make a world of difference during the security research of a closed-source application. I am hoping that these newly uncovered Reader symbols will make the life of some security engineers easier in the future. For me, it is yet another piece of evidence that reconnaissance is an essential part of vulnerability research and may yield results far exceeding expectations.

On the other hand, the recon step wouldn't be necessary had Adobe made the symbols available to everyone upfront. The fact that the debug data on macOS hasn't been previously discussed means that only the most determined offensive security researchers might have known about it in the past. We would therefore encourage closed-source companies to improve the inspectability of their software by proactively sharing symbols, similarly to what Microsoft does with their public symbol server. Such an approach would level the playing field and base the security of client applications on openness and not obscurity, which we believe would consequently benefit the users in the long term.
