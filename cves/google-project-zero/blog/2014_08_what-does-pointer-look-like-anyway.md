# What does a pointer look like, anyway? - Project Zero

Source: https://projectzero.google/2014/08/what-does-pointer-look-like-anyway.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Chris Evans, Renderer of Modern Art


These updates resolve memory leakage vulnerabilities that could be used to bypass memory address randomization (CVE-2014-0540, CVE-2014-0542, CVE-2014-0543, CVE-2014-0544, CVE-2014-0545).


I reported the latter four of these. I’d like to thank Adobe for fixing them so quickly -- about 30 days between report and broad availability of a patch. That’s well within Project Zero’s 90-day deadline on bug disclosure.

They are all interesting bugs in image decoding, leading to uninitialized pixels in image canvases. There exist rich ActionScript APIs to read pixels out of canvases, so any uninitialized data can be examined easily by the attacker. Let’s take a visual tour of the four bugs:


The image above, which includes the “got probable pointer” text, is a sample rendering from running the proof of concept file. The trigger for this bug is a particularly weird JPEG image: one with two color components per pixel. Most images have one component per pixel (greyscale) or three components per pixel (red, green, blue or other scheme). In the case of two color components, the image processing “gave up” on rendering the foreign image. This left completely uninitialized RGB (red, green, blue) values in the canvas, thus leaking the contents of the memory that was last allocated where the new canvas now is.

If you look at the probable pointer value, you’ll see that one byte is marked as “??”. This is because the canvas is in fact RGBA (red, green, blue, alpha) and the alpha component -- which is every fourth byte -- is initialized to a constant 0xff value.


The trigger for this bug is a 1bpp image. 1bpp is shorthand for “one bit per pixel”. If we just have 1 bit to represent every pixel, the image should only contain two different colors, one color for pixels where the bit is 0 and another color for pixels where the bit is 1.

Looking at the image, we have a rich range of colors so right away we know something is wrong. What has happened here is that 1bpp images can be declared in a SWF image tag, but they are not supported. Upon hitting the unsupported image, the per-row conversion code “gives up”, leaving the row buffer uninitialized. Since there is just one row buffer (it is reused every row), the image looks very distinct. Every row is the same.

The long hexadecimal number below the image represents a bit of uninitialized data pulled out of the image canvas and into script.


This bug resolves the question “what does a pointer look like?” the most definitively. It also leaks contiguous uninitialized memory very clearly, making it the most powerful leak yet. There is no “??” in the extracted pointer value, because there is no uncertainty.

The bug works by rendering image pixels that are compressed via the zlib compression algorithm. This particular image is a 64x64 canvas, which requires 4096 pixels to fill. The trick we pull is to terminate the zlib stream immediately, after emitting exactly 0 pixels. This leaves the canvas… you guessed it… uninitialized.

If you look at the image, you’ll notice it appears to be comprised of columns. This effect is because the width is 64 pixels, and a pointer is 8 bytes (these images are all rendered on 64-bit Linux). Since 64 is an exact multiple of the pointer size, any pointers will be nicely aligned. And this image is chock full of pointers. A pointer value on 64-bit Linux is particularly visible because the two most significant bytes are zero (rendered as black), leading to distinct vertical black bars.


This final bug is also a very powerful memory leak, as evidenced by the complete pointer value extracted. It also works by embedding truncated zlib stream in the image. In this case, the truncated zlib stream (again truncated a 0 pixels) is for the image’s alpha channel. By extracting only the alpha channel byte values from the rendered image, we can recover the content of contiguous uninitialized memory.

Conclusion

My personal conclusion is that there’s a strange beauty to the visualization of uninitialized memory and pointer values. I hope you enjoyed these slightly unusual bugs.
