# Effective Fuzzing: A Dav1d Case Study - Project Zero

Source: https://projectzero.google/2024/10/effective-fuzzing-dav1d-case-study.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Guest post by Nick Galloway, Senior Security Engineer, 20% time on Project Zero

Late in 2023, while working on a 20% project with Project Zero, I found an integer overflow in the [dav1d](https://www.google.com/url?q=https://code.videolan.org/videolan/dav1d&sa=D&source=editors&ust=1727869833018829&usg=AOvVaw0OeT8v646Gvjwd0m7jBsCT) AV1 video decoder. That integer overflow leads to an out-of-bounds write to memory. Dav1d 1.4.0 [patched](https://www.google.com/url?q=https://code.videolan.org/videolan/dav1d/-/commit/2b475307dc11be9a1c3cc4358102c76a7f386a51&sa=D&source=editors&ust=1727869833019194&usg=AOvVaw3804XIY0C7CGB-UUn5NwNA) this, and it was assigned [CVE-2024-1580](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/detail?id%3D2502&sa=D&source=editors&ust=1727869833019361&usg=AOvVaw2q-_2_XpPz6efrZdkggxY_). After the disclosure, I received some questions about how this issue was discovered, since dav1d is already being fuzzed by at least [oss-fuzz](https://www.google.com/url?q=https://github.com/google/oss-fuzz&sa=D&source=editors&ust=1727869833019505&usg=AOvVaw1deHOW6xxNlIZyxGlGjMct). This blog post explains what happened. It’s a useful case study in how to construct fuzzers to exercise as much code as possible. But first, some background...

# Background

## Dav1d

[Dav1d](https://www.google.com/url?q=https://code.videolan.org/videolan/dav1d&sa=D&source=editors&ust=1727869833020012&usg=AOvVaw1NMeiqpYWceoZIYBeSFatd) is a highly-optimized AV1 decoder. [AV1](https://www.google.com/url?q=https://en.wikipedia.org/wiki/AV1&sa=D&source=editors&ust=1727869833020113&usg=AOvVaw1ETEEXIx_hheFr4FUEaMVU) is a royalty-free video coding format developed by the Alliance for Open Media, and achieves improved data compression compared to older formats. AV1 is [widely supported](https://www.google.com/url?q=https://caniuse.com/av1&sa=D&source=editors&ust=1727869833020194&usg=AOvVaw3h5W2dCTCZKbFY_sl8V3t0) by web browsers, and a significant parsing vulnerability in AV1 decoders could be used as part of an attack to gain remote code execution. In the right context, where AV1 is parsed in a received message, this could allow a 0-click exploit. Testing some popular messaging clients by sending AV1 videos and AVIF images (which uses the AV1 codec) yielded the following results:

- AVIF images are displayed in iMessage
- AVIF images are NOT displayed in Android Messages when sent as an MMS
- AVIF images are displayed in Google Chat
- AV1 videos are not immediately displayed in Google Chat, but can be downloaded by the receiver and eventually can be played after being downscaled


Dav1d is written primarily in C and notably has different code paths for different architectures. There are x86, x86-64, ppc, riscv, arm32, and arm64 code paths in the repository, most of these containing optimized assembly. As noted in their roadmap, support for some of these is ongoing work, but at least ARMv7, ARMv8, and x86-64 have been thoroughly tested in the field. Based on this being a library written in C and assembly, as well as dav1d’s ubiquitous support in web browsers, I might expect it already has excellent fuzzing coverage from multiple sources.

## The integer overflow

The full details, including two proof-of-concepts that can be used to reproduce the vulnerability, are available from the [project zero bug tracker](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/detail?id%3D2502&sa=D&source=editors&ust=1727869833021191&usg=AOvVaw2827Z5-pyHnolJPIQLVAmh). The short explanation is that when multiple decoding threads are used, a signed 32-bit integer overflow can occur when calculating the values to put in the tile start offset array. In the excerpt below, the addition overflows:

| f->frame\_thread.tile\_start\_off\[tile\_idx++\] = row\_off + b\_diff \* f->frame\_hdr->tiling.col\_start\_sb\[tile\_col\] \* f->sb\_step \* 4; | 


These overflowed values in tile\_start\_off are then passed to setup\_tile():

| setup\_tile(&f->ts\[j\], f, data, tile\_sz, tile\_row, tile\_col++, c->n\_fc > 1 ? f->frame\_thread.tile\_start\_off\[j\] : 0); | 

The tile\_start\_off parameter to setup\_tile() is from f->frame\_thread.tile\_start\_off\[j\] above, and used to calculate values for several pointers. (Note that pal\_idx, cbi, and cf are pointers in the frame\_thread struct, [as can be seen in internal.h](https://www.google.com/url?q=https://code.videolan.org/videolan/dav1d/-/blob/1.3.0/src/internal.h?ref_type%3Dtags%23L283&sa=D&source=editors&ust=1727869833024329&usg=AOvVaw3zyAYRiEcvv-Yy85_lc6L9).

| static void setup\_tile(Dav1dTileState \*const ts, const Dav1dFrameContext \*const f, const uint8\_t \*const data, const size\_t sz, const int tile\_row, const int tile\_col, const int tile\_start\_off) ... ts->frame\_thread\[p\].pal\_idx = f->frame\_thread.pal\_idx ? &f->frame\_thread.pal\_idx\[(size\_t)tile\_start\_off \* size\_mul\[1\] / 8\] : NULL; ts->frame\_thread\[p\].cbi = f->frame\_thread.cbi ? &f->frame\_thread.cbi\[(size\_t)tile\_start\_off \* size\_mul\[0\] / 64\] : NULL; ts->frame\_thread\[p\].cf = f->frame\_thread.cf ? (uint8\_t\*)f->frame\_thread.cf + (((size\_t)tile\_start\_off \* size\_mul\[0\]) >> !f->seq\_hdr->hbd) : NULL; | 


Those pointers are later written to, resulting in an out of bounds write to memory. Two test cases are provided with the bug, the first of which (poc1.obu) will result in an address which is outside the valid range of addresses, and so might not be exploitable. The other test case (poc2.obu) enables high bit depth mode and so has higher memory requirements, but results in pointers that are within the normal range of addresses, and so is more likely to be useful in an exploit.

## Fuzzing Space Definition

A fuzzer’s success is typically measured by “coverage”, where the fuzz target's execution is traced to examine which lines of assembly code have been covered. When I talk about the “fuzzing space”, I specifically mean space in the sense of a [mathematical space](<https://www.google.com/url?q=https://en.wikipedia.org/wiki/Space_(mathematics)&sa=D&source=editors&ust=1727869833031893&usg=AOvVaw0_mQO6SzJFsxVzIRqaI_Ph>), where the set of lines of code that are executed by a given set of test cases is something we would like to maximize. In other words, a good fuzzer will execute as many lines of code as possible with the smallest possible set of test cases. To fully define the space we would also consider the fuzzing engine that generates test cases, the initial seed corpus, and the various configurations and architectures supported by the code to be fuzzed.

# Modified Dav1d Fuzzer

The dav1d fuzzer in oss-fuzz at the time I was looking at dav1d is [visible on GitHub](https://www.google.com/url?q=https://github.com/google/oss-fuzz/tree/dc543015c47f5efe6a23fa9d555a10c20ec531bf/projects/dav1d&sa=D&source=editors&ust=1727869833032315&usg=AOvVaw1rCRY6jwO3dC0odT9NmnTM). This contains build instructions and a dockerfile for oss-fuzz to run this at scale. The fuzzer implementation is in the dav1d source repository. The [meson.build file](https://www.google.com/url?q=https://code.videolan.org/videolan/dav1d/-/blob/8ddb28e5a726f185186c7bbd749ca3499c639c15/tests/libfuzzer/meson.build&sa=D&source=editors&ust=1727869833032482&usg=AOvVaw2JbV-f3E9v_VebU3Loe3dI) shows a couple of configurations, one for building dav1d\_fuzzer and the other for building dav1d\_fuzzer\_mt, which additionally defines DAV1D\_MT\_FUZZING.


The fuzzing code is written in C, found in [dav1d\_fuzzer.c](https://www.google.com/url?q=https://code.videolan.org/videolan/dav1d/-/blob/8ddb28e5a726f185186c7bbd749ca3499c639c15/tests/libfuzzer/dav1d_fuzzer.c%23L93&sa=D&source=editors&ust=1727869833032844&usg=AOvVaw1PIWcyouvclPaJEhZrhXmx). The fuzzer implements LLVMFuzzerTestOneInput, [the standard way to use libfuzzer](https://www.google.com/url?q=https://llvm.org/docs/LibFuzzer.html%23fuzz-target&sa=D&source=editors&ust=1727869833032939&usg=AOvVaw2b2IgFaVnTqQSdA36JTZGc). The first thing the fuzzer does is the usual variable declarations in any C function, including instantiating a Dav1dSettings struct to all zeroes. A bit later, the fuzzer uses a function to initialize the settings struct with defaults:

| dav1d\_default\_settings(&settings); #ifdef DAV1D\_MT\_FUZZING settings.max\_frame\_delay = settings.n\_threads = 4; #elif defined(DAV1D\_ALLOC\_FAIL) settings.max\_frame\_delay = max\_frame\_delay; settings.n\_threads = n\_threads; dav1d\_setup\_alloc\_fail(seed, probability); #else settings.max\_frame\_delay = settings.n\_threads = 1; #endif #if defined(DAV1D\_FUZZ\_MAX\_SIZE) settings.frame\_size\_limit = DAV1D\_FUZZ\_MAX\_SIZE; #endif | 


It’s good that the fuzzer will create one or four threads, depending on the fuzzer configuration, but if vulnerabilities exist only when there are three threads, or 19 threads, these will not be detected by any use of this fuzzer. That said, since the code paths for the threaded option mostly seem to differ based only on whether the number of threads is 1 or some other number, that seems unlikely.


There are [some other configuration items](https://www.google.com/url?q=https://code.videolan.org/videolan/dav1d/-/blob/8ddb28e5a726f185186c7bbd749ca3499c639c15/include/dav1d/dav1d.h%23L78&sa=D&source=editors&ust=1727869833036484&usg=AOvVaw2FIybdGojdkp8MI-6Hxj8B) that users of the dav1d library might configure differently. As one example, output\_invisible\_frames is always zero in this fuzzer. If a vulnerability existed only when this was nonzero, the fuzzer would not catch this in either the threaded or multi threaded fuzzing configurations.


Another example of untested coverage in the dav1d fuzzer, and the most interesting one for me because it led to the discovery of the integer overflow vulnerability, is the usage of DAV1D\_FUZZ\_MAX\_SIZE.

| #define DAV1D\_FUZZ\_MAX\_SIZE 4096 \* 4096 … #if defined(DAV1D\_FUZZ\_MAX\_SIZE) settings.frame\_size\_limit = DAV1D\_FUZZ\_MAX\_SIZE; #endif | 


This maximum frame size did not exist in all configurations used by dav1d users, and although 32-bit platforms have an internally applied limit, there is no limit by default for 64-bit platforms. Removing this line (and using the multithreaded fuzzer with ubsan enabled) was enough to trigger the integer overflow. To allow the fuzzer to explore more of the configuration space, I added support for the fuzzer to also fuzz many of the configuration settings that can be passed to dav1d. The code for this "configuration fuzzing" is shown in the excerpt below. It contains a few range restrictions only to avoid triggering asserts. This might be an area to explore in the future in case any of these asserts do not occur in production systems and where the configuration can be influenced by an attacker.

| struct SettingsFuzz { int n\_threads; int max\_frame\_delay; int apply\_grain; int operating\_point; int all\_layers; unsigned frame\_size\_limit; int strict\_std\_compliance; int output\_invisible\_frames; int inloop\_filters; int decode\_frame\_type; }; Dav1dSettings newSettings(struct SettingsFuzz sf) { Dav1dSettings settings = {0}; dav1d\_default\_settings(&settings); // Some of these trigger an assert if they're out of range if (sf.n\_threads \< 0 \|\| sf.n\_threads > DAV1D\_MAX\_THREADS) { sf.n\_threads = DAV1D\_MAX\_THREADS / 2; } settings.n\_threads = sf.n\_threads; if (sf.max\_frame\_delay \< 0 \|\| sf.max\_frame\_delay > DAV1D\_MAX\_FRAME\_DELAY) { sf.max\_frame\_delay = DAV1D\_MAX\_FRAME\_DELAY; } settings.max\_frame\_delay = sf.max\_frame\_delay; settings.apply\_grain = sf.apply\_grain; if (sf.operating\_point \< 0 \|\| sf.operating\_point > 31) { sf.operating\_point = 0; } settings.operating\_point = sf.operating\_point; settings.all\_layers = sf.all\_layers; settings.frame\_size\_limit = sf.frame\_size\_limit; settings.strict\_std\_compliance = sf.strict\_std\_compliance; settings.output\_invisible\_frames = sf.output\_invisible\_frames; settings.inloop\_filters = (enum Dav1dInloopFilterType)sf.inloop\_filters; if (sf.decode\_frame\_type \< 0 \|\|sf.decode\_frame\_type > (int)DAV1D\_DECODEFRAMETYPE\_KEY) { sf.decode\_frame\_type = 0; } settings.decode\_frame\_type = (enum Dav1dDecodeFrameType)sf.decode\_frame\_type; return settings; } | 


Instead of placing limits on the fuzzer, these are better placed in the code itself. Taking the maximum frame size, on 32-bit systems dav1d will restrict frame sizes to 8192\*8192, regardless of the frame\_size\_limit configuration. (See code excerpt below) On 64-bit systems, there is no such limit, and so very large 50,000x50,000 sized frames are possible.

| /\* On 32-bit systems extremely large frame sizes can cause overflows in \* dav1d\_decode\_frame() malloc size calculations. Prevent that from occuring \* by enforcing a maximum frame size limit, chosen to roughly correspond to \* the largest size possible to decode without exhausting virtual memory. \*/ if (sizeof(size\_t) \< 8 && s->frame\_size\_limit - 1 >= 8192 \* 8192) { c->frame\_size\_limit = 8192 \* 8192; if (s->frame\_size\_limit) dav1d\_log(c, "Frame size limit reduced from %u to %u.\n", s->frame\_size\_limit, c->frame\_size\_limit); } | 


There’s an understandable desire to avoid reporting errors when a fuzzer triggers huge allocations. When possible, this part of the fuzzing space could be explored with a shard configured to run with a much larger amount of memory than is usually available.


I also tested a number of other avenues that did not lead to discovering vulnerabilities. One example is fuzzing on ARM, which I had expected might result in a vulnerability due to it [not being covered by OSS-Fuzz](https://www.google.com/url?q=https://github.com/google/oss-fuzz/blob/dc543015c47f5efe6a23fa9d555a10c20ec531bf/projects/dav1d/project.yaml%23L18&sa=D&source=editors&ust=1727869833049213&usg=AOvVaw3RM5rWPeDjKeykKUR6xmK3). Despite this not uncovering anything, I still believe that it’s worthwhile to run fuzz tests on other architectures when possible, especially when the target has different code paths and optimized assembly for different architectures, as is the case with dav1d.

# Conclusion

The ultimate lesson I took away from this is that a fruitful area to look for vulnerabilities is artificial limits within a fuzzer. By setting a relatively small frame\_size\_limit, the dav1d fuzzer missed the integer overflow. There is a good reason for this limit, which is that [oss-fuzz only supports 2.5GB of RAM](https://www.google.com/url?q=https://github.com/google/oss-fuzz/blob/master/docs/faq.md%23what-are-the-specs-on-your-machines&sa=D&source=editors&ust=1727869833049749&usg=AOvVaw0l6rO0pb_D5DmlkvkIUgv8). This highlights a tradeoff for fuzzers. By limiting the amount of RAM we can hope to increase coverage overall by fitting more fuzzers within the machines we have. Unfortunately this means limited coverage for the part of the fuzzing space that requires more memory.


Until [memory safe parsers](https://www.google.com/url?q=https://github.com/memorysafety/rav1d&sa=D&source=editors&ust=1727869833049988&usg=AOvVaw21ZyX_NLPMleV9Bd7e1WoB) are available and widely used, memory corruption issues will continue to present a serious threat to users. For now, perhaps we can create fuzzers that are configured to occasionally explore parts of the fuzzing space that require more memory.

# P.S.: OSS-Fuzz Bughunters Reward Program

Finally, I would like to mention that as of writing there is a Google bughunters reward program for improving [fuzzing coverage](https://www.google.com/url?q=https://oss-fuzz-introspector.storage.googleapis.com/index.html&sa=D&source=editors&ust=1727869833050268&usg=AOvVaw3nvIvq5yFCtLWrfet-ti0e) in critical OSS projects. [See the bughunters site](https://www.google.com/url?q=https://bughunters.google.com/open-source-security/oss-fuzz&sa=D&source=editors&ust=1727869833050344&usg=AOvVaw2Ck2jEAKUCherhIIqlHJCZ) for more details.
