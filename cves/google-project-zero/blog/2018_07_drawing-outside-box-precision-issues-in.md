# Drawing Outside the Box: Precision Issues in Graphic Libraries - Project Zero

Source: https://projectzero.google/2018/07/drawing-outside-box-precision-issues-in.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

By Mark Brand and Ivan Fratric, Google Project Zero


In this blog post, we are going to write about a seldom seen vulnerability class that typically affects graphic libraries (though it can also occur in other types of software). The root cause of such issues is using limited precision arithmetic in cases where a precision error would invalidate security assumptions made by the application.


While we could also call other classes of bugs precision issues, namely integer overflows, the major difference is: with integer overflows, we are dealing with arithmetic operations where the magnitude of the result is too large to be accurately represented in the given precision. With the issues described in this blog post, we are dealing with arithmetic operations where the magnitude of the result or a part of the result is too small to be accurately represented in the given precision.


These issues can occur when using floating-point arithmetic in operations where the result is security-sensitive, but, as we’ll demonstrate later, can also occur in integer arithmetic in some cases.


Let’s look at a trivial example:


float a = 100000000;

float b = 1;

float c = a + b;


If we were making the computation with arbitrary precision, the result would be 100000001. However, since [float](https://en.wikipedia.org/wiki/IEEE_754) typically only allows for 24 bits of precision, the result is actually going to be 100000000. If an application makes the normally reasonable assumption that a > 0 and b > 0 implies that a + b > a, then this could lead to issues.


In the example above, the difference between a and b is so significant that b completely vanishes in the result of the calculation, but precision errors also happen if the difference is smaller, for example


float a = 1000;

float b = 1.1111111;

float c = a + b;


The result of the above computation is going to be 1001.111084 and not 1001.1111111 which would be the accurate result. Here, only a part of b is lost, but even such results can sometimes have interesting consequences.


While we used the float type in the above examples, and in these particular examples using double would result in more accurate computation, similar precision errors can happen with double as well.


In the remainder of this blog post, we are going to show several examples of precision issues with security impact. These issues were independently explored by two Project Zero members: Mark Brand, who looked at SwiftShader, a software OpenGL implementation used in Chrome, and Ivan Fratric, who looked at the Skia graphics library, used in Chrome and Firefox.

# SwiftShader

SwiftShader is “a high-performance CPU-based implementation of the OpenGL ES and Direct3D 9 graphics APIs”. It’s used in [Chrome](https://blog.chromium.org/2016/06/universal-rendering-with-swiftshader.html) on all platforms as a fallback rendering option to work around limitations in graphics hardware or drivers, allowing universal use of WebGL and other advanced javascript rendering APIs on a far wider range of devices.


The code in SwiftShader needs to handle emulating a wide range of operations that would normally be performed by the GPU. One operation that we commonly think of as essentially “free” on a GPU is upscaling, or drawing from a small source texture to a larger area, for example on the screen. This requires computing memory indexes using non-integer values, which is where the [vulnerability](https://bugs.chromium.org/p/project-zero/issues/detail?id=1584) occurs.


As noted in the original bug report, the code that we’ll look at here is not quite the code which is actually run in practice - SwiftShader uses an LLVM-based JIT engine to optimize performance-critical code at runtime, but that code is more difficult to understand than their fallback implementation, and both contain the same bug, so we’ll discuss the fallback code. This code is the copy-loop used to copy pixels from one surface to another during rendering:


source->lockInternal((int)sRect.x0, (int)sRect.y0, sRect.slice, sw::LOCK\_READONLY, sw::PUBLIC);

dest->lockInternal(dRect.x0, dRect.y0, dRect.slice, sw::LOCK\_WRITEONLY, sw::PUBLIC);


float w = sRect.width() / dRect.width();

float h = sRect.height() / dRect.height();


const float xStart = sRect.x0 + 0.5f \* w;

float y = sRect.y0 + 0.5f \* h;

float x = xStart;


for(int j = dRect.y0; j \< dRect.y1; j++)

{

x = xStart;


for(int i = dRect.x0; i \< dRect.x1; i++)

{

// FIXME: Support RGBA mask

dest->copyInternal(source, i, j, x, y, options.filter);


x += w;

}


y += h;

}


source->unlockInternal();

dest->unlockInternal();

}


So - what highlights this code as problematic? We know prior to entering this function that all the bounds-checking has already been performed, and that any call to copyInternal with (i, j) in dRect and (x, y) in sRect will be safe.


The examples in the introduction above show cases where the resulting precision error means that a rounding-down occurs - in this case that wouldn’t be enough to produce an interesting security bug. Can we cause floating-point imprecision to result in a larger-than-correct value, leading to (x, y) values that are larger than expected?


If we look at the code, the intention of the developers is to compute the following:


for(int j = dRect.y0; j \< dRect.y1; j++)

{

for(int i = dRect.x0; i \< dRect.x1; i++)

{

x = xStart + (i \* w);

Y = yStart + (j \* h);

dest->copyInternal(source, i, j, x, y, options.filter);

}

}


If this approach had been used instead, we’d still have precision errors - but without the iterative calculation, there’d be no propagation of the error, and we could expect the eventual magnitude of the precision error to be stable, and in direct proportion to the size of the operands. With the iterative calculation as performed in the code, the errors start to propagate/snowball into a larger and larger error.


There are ways to estimate the maximum error in floating point calculations; and if you really, really need to avoid having extra bounds checks, using this kind of approach and making sure that you have conservative safety margins around those maximum errors might be a complicated and error-prone way to solve this issue. It’s not a great approach to identifying the pathological values that we want here to demonstrate a vulnerability; so instead we’ll take a brute-force approach.


Instinctively, we’re fairly sure that the multiplicative implementation will be roughly correct, and that the implementation with iterative addition will be much less correct. Given that the space of possible inputs is small (Chrome disallows textures with width or height greater than 8192), we can just run a brute force over all ratios of source width to destination width, comparing the two algorithms, and seeing where the results are most different. (Note that SwiftShader also limits us to even numbers). This leads us to the values of 5828, 8132; and if we compare the computations in this case (left side is the iterative addition, right side is the multiplication):


0:    1.075012 1.075012

1:    1.791687 1.791687

...

1000: 717.749878 717.749878   Up to here (at the precision shown) the values are still identical

1001: 718.466553 718.466553

...

2046: 1467.391724 1467.391724 At this point, the first significant errors start to occur, but note

2047: 1468.108398 1468.108521 that the "incorrect" result is smaller than the more precise one.

...

2856: 2047.898315 2047.898438

2857: 2048.614990 2048.614990 Here our two computations coincide again, briefly, and from here onwards

2858: 2049.331787 2049.331787 the precision errors consistently favour a larger result than the more

2859: 2050.048584 2050.048340 precise calculation.

...

8129: 5827.567871 5826.924805

8130: 5828.284668 5827.641602

8131: 5829.001465 5828.358398 The last index is now sufficiently different that int conversion results in an oob index.


(Note also that there will also be error in the “safe” calculation; it’s just that the lack of error propagation means that that error will remain directly proportional to the size of the input error, which we expect to be “small.”)


We can indeed see that, the multiplicative algorithm would remain within bounds; but that the iterative algorithm can return an index that is outside the bounds of the input texture!


As a result, we read an entire row of pixels past the end of our texture allocation - and this can be easily leaked back to javascript using WebGL. Stay tuned for an upcoming blog post in which we’ll use this vulnerability together with another unrelated issue in SwiftShader to take control of the GPU process from javascript.

# Skia

Skia is a graphics library used, among other places, in Chrome, Firefox and Android. In the web browsers it is used for example when drawing to a canvas HTML element using [CanvasRenderingContext2D](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D) or when drawing SVG images. Skia is also used when drawing various other HTML elements, but canvas element and SVG images are more interesting from the security perspective because they enable more direct control over the objects being drawn by the graphic library.


The most complex type of object (and therefore, most interesting from the security perspective) that Skia can draw is a [path](https://skia.org/user/api/SkPath_Reference). A path is an object that consists of elements such as lines, but also more complex curves, in particular quadratic or cubic [splines](<https://en.wikipedia.org/wiki/Spline_(mathematics)>).


Due to the way software drawing algorithms work in Skia, the precision issues are very much possible and quite impactful when they happen, typically leading to out-of-bounds writes.


To understand why these issues can happen, let’s assume you have an image in memory (represented as a buffer with size = width x height x color size). Normally, when drawing a pixel with coordinates (x, y) and color c, you would want to make sure that the pixel actually falls within the space of the image, specifically that 0 \<= x \< width and 0 \<= y \< height. Failing to check this could result in attempting to write the pixel outside the bounds of the allocated buffer. In computer graphics, making sure that only the objects in the image region are being drawn is called clipping.


So, where is the problem? Making a clip check for every pixel is expensive in terms of CPU cycles and Skia prides itself on speed. So, instead of making a clip check for every pixel, what Skia does is, it first makes the clip check on an entire object (e.g. line, path or any other type of object being drawn). Depending on the clip check, there are three possible outcomes:


1. The object is completely outside of the drawing area: The drawing function doesn’t draw anything and returns immediately.


1. The object is partially inside the drawing area: The drawing function proceeds with per-pixel clip enabled (usually by relying on[SkRectClipBlitter](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkBlitter.h?l=187&rcl=c640d0dc96924699fdbb1a3cbdc907aa07b1cb3c)).


1. The entire object is in the drawing area: The drawing function draws directly into the buffer without performing per-pixel clip checks.


The problematic scenario is c) where the clip check is performed only per-object and the more precise, per-pixel checks are disabled. This means, if there is a precision issue somewhere between the per-object clip check and the drawing of pixels and if the precision issue causes the pixel coordinates to go outside of the drawing area, this could result in a security vulnerability.


We can see per-object clip checks leading to dropping per-pixel checks in several places, for example:


- In[hair\_path](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Hairline.cpp?g=0&rcl=d92a739d72ae70fc8122dc077b0f751d4b1dd023&l=497) (function for drawing a path without filling), [clip](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Hairline.cpp?g=0&rcl=d92a739d72ae70fc8122dc077b0f751d4b1dd023&l=504) is initially set to null (which disables clip checks). The clip is only set if the bounds of the path, [rounded up and extended by 1 or 2](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Hairline.cpp?g=0&rcl=d92a739d72ae70fc8122dc077b0f751d4b1dd023&l=511) depending on the drawing options [don’t fit in the drawing area](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Hairline.cpp?g=0&rcl=d92a739d72ae70fc8122dc077b0f751d4b1dd023&l=515). Extending the path bounds by 1 seems like a pretty large safety margin, but it is actually the least possible safe value because drawing objects with antialiasing on will sometimes result in drawing to nearby pixels.


- In[SkScan::FillPath](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Path.cpp?g=0&rcl=50dbc0949fb256a316163143e649028eeed2970a&l=617) (function for filling a path with antialiasing turned off), the bounds of the path are first extended by [kConservativeRoundBias](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Path.cpp?g=0&l=575&rcl=50dbc0949fb256a316163143e649028eeed2970a) and [rounded](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Path.cpp?g=0&l=645&rcl=50dbc0949fb256a316163143e649028eeed2970a) to obtain the “conservative” path bounds. A [SkScanClipper](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Path.cpp?g=0&rcl=50dbc0949fb256a316163143e649028eeed2970a&l=653) object is then created for the current path. As we can see in the [definition](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Path.cpp?g=0&l=534&rcl=50dbc0949fb256a316163143e649028eeed2970a) of SkScanClipper, it will only use SkRectClipBlitter if the x coordinates of the path bounds are outside the drawing area or if irPreClipped is true (which only happens when path coordinates are very large).


Similar patterns can be seen in other drawing functions.


Before we take a closer look at the issues, it is useful to quickly go over various number formats used by Skia:


- [SkScalar](https://cs.chromium.org/chromium/src/third_party/skia/include/core/SkScalar.h?l=16&rcl=9236b02264d4b15208be3b8b8919f4ed441a3c85) is a 32-bit floating point number


- [SkFDot6](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkFDot6.h?l=16&rcl=c640d0dc96924699fdbb1a3cbdc907aa07b1cb3c) is defined as an integer, but it is actually a fixed-point number with 26 bits to the left and 6 bits to the right of the decimal point. For example, SkFDot6 value of 0x00000001 represents the number 1/64.


- [SkFixed](https://cs.chromium.org/chromium/src/third_party/skia/include/private/SkFixed.h?l=23&rcl=c640d0dc96924699fdbb1a3cbdc907aa07b1cb3c) is also a fixed-point number, this time with 16 bits to the left and 16 bits to the right of the decimal point. For example, SkFixed value of 0x00000001 represents 1/(2\*\*16)


Precision error with integer to float conversion


We discovered the initial problem when doing [DOM fuzzing](/2017/09/the-great-dom-fuzz-off-of-2017.html) against Firefox last year. [This issue](https://bugs.chromium.org/p/project-zero/issues/detail?id=1155) where Skia wrote out-of-bounds caught our eye so we investigated further. It turned out the root cause was a discrepancy in the way Skia converted floating point to ints in several places. When making the per-path clip check, the lower coordinates (left and top of the bounding box) were rounded using this function:


static inline int round\_down\_to\_int(SkScalar x) {

double xx = x;

xx -= 0.5;

return (int)ceil(xx);

}


Looking at the code you see that it will return a number greater or equal to zero (which is necessary for passing the path-level clip check) for numbers that are strictly larger than -0.5. However, in another part of the code, specifically SkEdge::setLine if SK\_RASTERIZE\_EVEN\_ROUNDING is defined (which is the case in Firefox), floats are rounded to integers differently, using the following function:


inline SkFDot6 SkScalarRoundToFDot6(SkScalar x, int shift = 0)

{

union {

double  fDouble;

int32\_t fBits\[2\];

} tmp;

int fractionalBits = 6 + shift;

double magic = (1LL \<\< (52 - (fractionalBits))) \* 1.5;


tmp.fDouble = SkScalarToDouble(x) + magic;

#ifdef SK\_CPU\_BENDIAN

return tmp.fBits\[1\];

#else

return tmp.fBits\[0\];

#endif

}


Now let’s take a look at what these two functions return for a number -0.499. For this number, round\_down\_to\_int returns 0 (which always passes the clipping check) and SkScalarRoundToFDot6 returns -32 which corresponds to -0.5, so we actually end up with a number that is smaller than the one we started with.


That’s not the only problem, though, because there’s another place where a precision error occurs in SkEdge::setLine.


Precision error when multiplying fractions


SkEdge::setLine calls SkFixedMul which is defined as:


static inline SkFixed(SkFixed a, SkFixed b) {

return (SkFixed)((int64\_t)a \* b >> 16);

}


This function is for multiplying two SkFixed numbers. An issue comes up when using this function to multiply negative numbers. Let’s look at a small example. Let’s assume a = -1/(2\*\*16) and b = 1/(2\*\*16). If we multiply these two numbers on paper, the result is -1/(2\*\*32). However, due to the way SkFixedMul works, specifically because the right shift is used to convert the result back to SkFixed format, the result we actually end up with is 0xFFFFFFFF which is SkFixed for  -1/(2\*\*16). Thus, we end up with a result with a magnitude much larger than expected.


As the result of this multiplication is used by SkEdge::setLine to adjust the x coordinate of the initial line point [here](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkEdge.h?rcl=38911a7cb53474575e1cd1cb545902b50ee00889&l=125), we can use the issue in SkFixedMul to cause an additional error up to 1/64 of a pixel to go outside of the drawing area bounds.


By combining the previous two issues, it was possible to get the x coordinate of a line sufficiently small (smaller than -0.5), so that, when a fractional representation was rounded to an integer [here](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Path.cpp?g=0&rcl=a33b43d796f03e2f4b5abd8060272f4f775d7390&l=247), Skia attempted to draw at coordinates with x = -1, which is clearly outside the image bounds. This then led to an out-of-bounds write as can be seen in the [original bug report](https://bugs.chromium.org/p/project-zero/issues/detail?id=1155). This bug could be exploited in Firefox by drawing an SVG image with coordinates as described in the previous section.


Floating point precision error when converting splines to line segments


When drawing paths, Skia is going to convert all non-linear curves (conic shapes, quadratic and cubic splines) to line segments. Perhaps unsurprisingly, these conversions suffer from precision errors.


The conversion of splines into line segments happen in several places, but the most susceptible to floating-point precision errors are [hair\_quad](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Hairline.cpp?g=0&l=233&rcl=f08d1d0ce19c72bb911f059dcf916cf99a0a2467) (used for drawing quadratic curves) and [hair\_cubic](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Hairline.cpp?g=0&rcl=f08d1d0ce19c72bb911f059dcf916cf99a0a2467&l=359) (used for drawing cubic curves). Both of these functions are called from [hair\_path](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Hairline.cpp?g=0&l=501&rcl=f08d1d0ce19c72bb911f059dcf916cf99a0a2467), which we already mentioned above. Because (unsurprisingly), larger precision errors occur when dealing with cubic splines, we’ll only consider the cubic case here.


When approximating the spline, first the cubic coefficients are computed in [SkCubicCoeff](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkGeometry.h?g=0&l=375&rcl=b9bfb7b275d11eb6ba90dc2dfa9cfa9f73cc613e). The most interesting part is:


fA = P3 + three \* (P1 - P2) - P0;

fB = three \* (P2 - times\_2(P1) + P0);

fC = three \* (P1 - P0);

fD = P0;


Where P1, P2 and P3 are input points and fA, fB, fC and fD are output coefficients. The line segment points are then computed in [hair\_cubic](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Hairline.cpp?g=0&rcl=f08d1d0ce19c72bb911f059dcf916cf99a0a2467&l=359) using the following code


const Sk2s dt(SK\_Scalar1 / lines);

Sk2s t(0);


...


Sk2s A = coeff.fA;

Sk2s B = coeff.fB;

Sk2s C = coeff.fC;

Sk2s D = coeff.fD;

for (int i = 1; i \< lines; ++i) {

t = t + dt;

Sk2s p = ((A \* t + B) \* t + C) \* t + D;

p.store(&tmp\[i\]);

}


Where p is the output point and lines is the number of line segments we are using to approximate the curve. Depending on the length of the spline, a cubic spline can be approximated with up to 512 lines.


It is obvious that the arithmetic here is not going to be precise. As identical computations happen for x and y coordinates, let’s just consider the x coordinate in the rest of the post.


Let’s assume the width of the drawing area is 1000 pixels. Because hair\_path is used for drawing path with antialiasing turned on, it needs to make sure that all points of the path are between 1 and 999, which is done in the initial, path-level clip check. Let’s consider the following coordinates that all pass this check:


p0 = 1.501923

p1 = 998.468811

p2 = 998.998779

p3 = 999.000000


For these points, the coefficients are as follows


a = 995.908203

b = -2989.310547

c = 2990.900879

d = 1.501923


If you do the same computation in larger precision, you’re going to notice that the numbers here aren’t quite correct. Now let’s see what happens if we approximate the spline with 512 line segments. This results in 513 x coordinates:


0: 1.501923

1: 7.332130

2: 13.139574

3: 18.924301

4: 24.686356

5: 30.425781

...

500: 998.986389

501: 998.989563

502: 998.992126

503: 998.994141

504: 998.995972

505: 998.997314

506: 998.998291

507: 998.999084

508: 998.999695

509: 998.999878

510: 999.000000

511: 999.000244

512: 999.000000


We can see that the x coordinate keeps growing and at point 511 clearly goes outside of the “safe” area and grows larger than 999.


As it happens, this isn’t sufficient to trigger an out-of-bounds write, because, due to how drawing antialiased lines works in Skia, we need to go at least 1/64 of a pixel outside of the clip area for it to become a security issue. However, an interesting thing about the precision errors in this case is that the larger the drawing area, the larger the error that can happen.


So let’s instead consider a drawing area of 32767 pixels (maximum canvas size in Chrome). The initial clipping check then checks that all path points are in the interval \[1, 32766\]. Now let’s consider the following points:


p0 = 1.7490234375

p1 = 32765.9902343750

p2 = 32766.000000

p3 = 32766.000000


The corresponding coefficients


a = 32764.222656

b = -98292.687500

c = 98292.726562

d = 1.749023


And the corresponding line approximation


0: 1.74902343

1: 193.352295

2: 384.207123

3: 574.314941

4: 763.677246

5: 952.295532

…

505: 32765.925781

506: 32765.957031

507: 32765.976562

508: 32765.992188

509: 32766.003906

510: 32766.003906

511: 32766.015625

512: 32766.000000


You can see that we went out-of-bounds significantly more at index 511.


Fortunately for Skia and unfortunately for aspiring attackers, this bug can’t be used to trigger memory corruption, at least not in the up-to-date version of skia. The reason is [SkDrawTiler](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkBitmapDevice.cpp?l=42&rcl=41f4f31cd7dadd1123600c38faa8fef6bd7fb29c). Whenever Skia draws using SkBitmapDevice (as opposed to using a GPU device) and the drawing area is larger than 8191 pixels in any dimension, instead of drawing the whole image at once, Skia is going to split it into tiles of size (at most) 8191x8191 pixels. This [change](https://skia.googlesource.com/skia.git/+/b5e1f7558052cc60deaf23ccc2c898d1c6c94c09) was made in March, not for security reasons, but to be able to support larger drawing surfaces. However, it still effectively prevented us from exploiting this issue and will also prevent exploiting other cases where a surface larger than 8191 is required to reach the precision error of a sufficient magnitude.


Still, this bug was exploitable before March and we think it nicely demonstrates the concept of precision errors.


Integer precision error when converting splines to line segments


There is another place where splines are approximated as line segments when drawing (in this case: filling) paths that was also affected by a precision error, in this case an exploitable one. Interestingly, here the precision error wasn’t in floating-point but rather in fixed-point arithmetic.


The error happens in [SkQuadraticEdge::setQuadraticWithoutUpdate](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkEdge.cpp?rcl=5eb8fc585e9b3c9ccc82b0921986e1020ddaff23&l=181) and [SkCubicEdge::setCubicWithoutUpdate](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkEdge.cpp?rcl=5eb8fc585e9b3c9ccc82b0921986e1020ddaff23&l=350). For simplicity, we are again going to concentrate just on the cubic spline version and, again, only on the x coordinate.


In [SkCubicEdge::setCubicWithoutUpdate](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkEdge.cpp?rcl=5eb8fc585e9b3c9ccc82b0921986e1020ddaff23&l=350), the curve coordinates are first converted to SkFDot6 type (integer with 6 bits used for fraction). After that, parameters corresponding to the first, second and third derivative of the curve at the initial point are going to be computed:


SkFixed B = SkFDot6UpShift(3 \* (x1 - x0), upShift);

SkFixed C = SkFDot6UpShift(3 \* (x0 - x1 - x1 + x2), upShift);

SkFixed D = SkFDot6UpShift(x3 + 3 \* (x1 - x2) - x0, upShift);


fCx     = SkFDot6ToFixed(x0);

fCDx    = B + (C >> shift) + (D >> 2\*shift);    // biased by shift

fCDDx   = 2\*C + (3\*D >> (shift - 1));           // biased by 2\*shift

fCDDDx  = 3\*D >> (shift - 1);                   // biased by 2\*shift


Where x0, x1, x2 and x3 are x coordinates of the 4 points that define the cubic spline and shift and upShift depend on the length of the curve (this corresponds to the number of linear segments the curve is going to be approximated in). For simplicity, we can assume shift = upShift = 6 (maximum possible values).


Now let’s see what happens for some very simple input values:


x0 = -30

x1 = -31

x2 = -31

x3 = -31


Note that x0, x1, x2 and x3 are of the type SkFDot6 so value -30 corresponds to -0.46875 and -31 to -0.484375. These are close to -0.5 but not quite and are thus perfectly safe when rounded. Now let’s examine the values of the computed parameters:


B = -192

C = 192

D = -64


fCx = -30720

fCDx = -190

fCDDx = 378

fCDDDx = -6


Do you see where the issue is? Hint: it’s in the formula for fCDx.


When computing fCDx (first derivation of a curve), the value of D needs is right-shifted by 12. However, D is too small to do that precisely, and since D is negative, the right shift


D >> 2\*shift


Is going to result in -1, which is larger in magnitude than the intended result. (Since D is of type SkFixed its actual value is -0.0009765625 and the shift, when interpreted as division by 4096, would result in -2.384185e-07). Because of this, the whole fCDx ends up as a larger negative value than it should (-190 vs. -189.015).


Afterwards, the value of fCDx gets used when calculating the x value of line segments. This happens in SkCubicEdge::updateCubic on [this line](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkEdge.cpp?l=477&rcl=f08d1d0ce19c72bb911f059dcf916cf99a0a2467):


newx    = oldx + (fCDx >> dshift);


The x values, when approximating the spline with 64 line segments (maximum for this algorithm), are going to be (expressed as index, integer SkFixed value and the corresponding floating point value):


index raw      interpretation

0:    -30720   -0.46875

1:    -30768   -0.469482

2:    -30815   -0.470200

3:    -30860   -0.470886

4:    -30904   -0.471558

5:    -30947   -0.472214

...

31:   -31683   -0.483444

32:   -31700   -0.483704

33:   -31716   -0.483948

34:   -31732   -0.484192

35:   -31747   -0.484421

36:   -31762   -0.484650

37:   -31776   -0.484863

38:   -31790   -0.485077

...

60:   -32005   -0.488358

61:   -32013   -0.488480

62:   -32021   -0.488602

63:   -32029   -0.488724

64:   -32037   -0.488846


You can see that for the 35th point, the x value (-0.484421) ends up being smaller than the smallest input point (-0.484375) and the trend continues for the later points. This value would still get rounded to 0 though, but there is another problem.


The x values computed in SkCubicEdge::updateCubic are passed to SkEdge::updateLine, where they are converted from SkFixed type to SkFDot6 on the [following lines](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkEdge.cpp?g=0&l=114&rcl=f08d1d0ce19c72bb911f059dcf916cf99a0a2467):


x0 >>= 10;

x1 >>= 10;


Another right shift! And when, for example, SkFixed value -31747 gets shifted we end up with SkFDot6 value of -32 which represents -0.5.


At this point we can use the same trick described above in the “Precision error when multiplying fractions” section to go smaller than -0.5 and break out of the image bounds. In other words, we can make Skia draw to x = -1 when drawing a path.


But, what can we do with it?


In general, given that Skia allocates image pixels as a single allocation that is organized row by row (as most other software would allocate bitmaps), there are several cases of what can happen with precision issues. If we assume an width x height image and that we are only able to go one pixel out of bounds:


1. Drawing to y = -1 or y = height immediately leads to heap out-of-bounds write
2. Drawing to x = -1 with y = 0 immediately leads to a heap underflow of 1 pixel
3. Drawing to x = width with y = height - 1 immediately leads to heap overflow of 1 pixel
4. Drawing to x = -1 with y > 0 leads to a pixel “spilling” to the previous image row
5. Drawing to x = height with y \< height-1 leads to a pixel “spilling” to the next image row


What we have here is scenario d) - unfortunately we can’t draw to x = 1 with y = 0 because the precision error needs to accumulate over the growing values of y.


Let’s take a look at the following example SVG image:


\<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">

\<style>

body {

margin-top: 0px;

margin-right: 0px;

margin-bottom: 0px;

margin-left: 0px

}

\</style>

\<path d="M -0.46875 -0.484375 C -0.484375 -0.484375, -0.484375 -0.484375, -0.484375 100 L 1 100 L 1 -0.484375" fill="red" shape-rendering="crispEdges" />

\</svg>


If we render this in an unpatched version of Firefox what we see is shown in the following image. Notice how the SVG only contains coordinates on the left side of the screen, but some of the red pixels get drawn on the right. This is because, due to the way images are allocated, drawing to x = -1 and y = row is equal to drawing to x = width - 1 and y = row - 1.


Opening an SVG image that triggers a Skia precision issue in Firefox. If you look closely you’ll notice some red pixels on the right side of the image. How did those get there? :)


Note that we used Mozilla Firefox and not Google Chrome because, due to SVG drawing internals (specifically: Skia seems to draw the entire image at once, while Chrome uses additional tiling) it is easier to demonstrate the issue in Firefox. However, both Chrome and Firefox were equally affected by this issue.


But, other than drawing a funny image, is there real security impact to this issue? Here, [SkARGB32\_Shader\_Blitter](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkCoreBlitters.h?g=0&l=120&rcl=e102016fef339f59e4bfea4547276e16da298483) comes to the rescue (SkARGB32\_Shader\_Blitter is used whenever shader effects are applied to a color in Skia). What is specific about SkARGB32\_Shader\_Blitter is that it allocates a temporary buffer of the same size as a single image row. When [SkARGB32\_Shader\_Blitter::blitH](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkBlitter_ARGB32.cpp?g=0&l=368&rcl=a4083c97d48e8a4f88e2797d7363f141e3d42553) is used to draw an entire image row, if we can make it draw from x = -1 to x = width - 1 (alternately from x = 0 to x = width), it will need to write width + 1 pixels into a buffer that can only hold width pixels, leading to a buffer overflow as can be seen in the ASan log in the [bug report](https://bugs.chromium.org/p/project-zero/issues/detail?id=1579).


Note how the PoCs for Chrome and Firefox contain SVG images with a linearGradient element - the linear gradient is used specifically to select SkARGB32\_Shader\_Blitter instead of drawing pixels to the image directly, which would only result in pixels spilling to the previous row.


Another specific of this issue is that it can only be reached when drawing (more specifically: filling) paths with antialiasing turned off. As it is not currently possible to draw paths to a HTML canvas elements with antialiasing off (there is an imageSmoothingEnabled property but it only applies to drawing images, not paths), an SVG image with shape-rendering="crispEdges" must be used to trigger the issue.


All precision issues we reported in Skia were fixed [by](https://skia.googlesource.com/skia.git/+/b8e752198dde333e71cb1a9578cd3dfd404dd06c) [increasing](https://skia.googlesource.com/skia.git/+/861b52ea98d703786ce485389db07e58759c1792) [kConservativeRoundBias](https://skia.googlesource.com/skia.git/+/3087c1f382f1cd547598dc75f47ccbc8fe1e6e0f). While the current bias value is large enough to cover the maximum precision errors we know about, we should not dismiss the possibility of other places where precision issues can occur.

# Conclusion

While precision issues, such as described in this blog post, won’t be present in most software products, where they are present they can have quite serious consequences. To prevent them from occurring:


- Don’t use floating-point arithmetic in cases where the result is security-sensitive. If you absolutely have to, then you need to make sure that the maximum possible precision error cannot be larger than some safety margin. Potentially,[interval arithmetic](https://www.boost.org/doc/libs/1_66_0/libs/numeric/interval/doc/interval.htm) could be used to determine the maximum precision error in some cases. Alternately, perform security checks on the result rather than input.


- With integer arithmetic, be wary of any operations that can reduce the precision of the result, such as divisions and right shifts.


When it comes to finding such issues, unfortunately, there doesn’t seem to be a great way to do it. When we started looking at Skia, initially we wanted to try using [symbolic execution](https://en.wikipedia.org/wiki/Symbolic_execution) on the drawing algorithms to find input values that would lead to drawing out-of-bounds, as, on the surface, it seemed this is a problem symbolic execution would be well suited for. However, in practice, there were too many issues: most tools don’t support floating point symbolic variables and, even when running against just the integer parts of the [simplest line drawing algorithm](https://cs.chromium.org/chromium/src/third_party/skia/src/core/SkScan_Hairline.cpp?g=0&l=45&rcl=f08d1d0ce19c72bb911f059dcf916cf99a0a2467), we were unsuccessful in completing the run in a reasonable time (we were using [KLEE](https://klee.github.io/) with STP and Z3 backends).


In the end, what we ended up doing was a combination of the more old-school methods: manual source review, fuzzing (especially with values close to image boundaries) and, in some cases, when we already identified potentially problematic areas of code, even bruteforcing the range of all possible values.


Do you know of other instances where precision errors resulted in security issues? Let us know about them in the comments.
