# Life After the Isolated Heap - Project Zero

Source: https://projectzero.google/2016/03/life-after-isolated-heap.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Natalie Silvanovich, Mourner of Lost Exploits

Over the past few months, Adobe has introduced a number of [changes](https://blogs.adobe.com/security/tag/heap-isolation) to the Flash Player heap with the goal of reducing the exploitability of certain types of vulnerabilities in Flash, especially use-after-frees. I wrote an exploit involving two bugs discovered after the Isolated Heap was implemented to explore how it impacts their exploitability.

# The Isolated Heap


The Flash heap, [MMgc](https://developer.mozilla.org/en-US/docs/Archive/MMgc), is a garbage collected heap that also supports unmanaged fixed allocations. In the past, there have been many exploits in the wild that used certain properties of the heap to aid exploitation. In particular, many [exploits](https://0b3dcaf9-a-62cb3a1a-s-sites.googlegroups.com/site/zerodayresearch/smashing_the_heap_with_vector_Li.pdf?attachauth=ANoY7cqJuxIdzdr9r2FUBjPwrbRuEiRHkb93MO3MKyOJSXWISkoMK0Swma6ODx4OC1ZqzMxcQDI7MzSVSR9whu6tYH_DKIRxxRYPeuXC1fYVI6fz2VNVHUJnL4MxYX8emXsHaQ8Ec9etfNGff3KtUdw5X-QfZ7QtYs5b0fBFy5Z-MBXrxU9WZlFFXLkoCcrHeU0WVoj-OFNX_p6cqmkQgCLiHc8Wg6RQhnZu8N_9Nrl32jOuxqHfmT3INnoH33FWadmLL5uFMiCx&attredirects=0) used the allocation properties of Vectors to gain read/write access to the entire Flash memory space via heap memory corruption bugs. Exploits that use other object types, such as ByteArray and BitmapData have also been seen in the wild.


MMgc was originally implemented as a type and size bucketed allocator. When memory is requested, the allocator that is called depends on the type of memory that is needed. This is related to the garbage collection properties of the memory. If it is not garbage collected, the Fixed allocator is used, otherwise the Garbage-Collected (GC) allocator is used. Within the GC allocator, there are about eight subtypes of memory that can be allocated, related to whether the memory contains pointers and whether those pointers have custom finalizers or GC routines that need to be called. Within each type, the request is sorted by size, and the memory is allocated on a heap page for that size. Large requests are allocated on their own page.


The Isolated Heap introduces partitioning to the heap, essentially a third factor which determines where memory is allocated. There is separate memory for each partition, which is then split into subsections for different types and sizes. The goal of partitioning is to allocate objects that are likely to contain memory corruption bugs in a different area of memory than objects that are likely to be useful in exploiting memory corruption bugs, and generally add more entropy to the heap.


There are currently three partitions on the heap. The first partition is generally used for objects that contain pointers: script objects, their backing GC-memory and certain pointer arrays. The second partition is used for objects that contain non-pointer data, mostly arrays of primitive types. The third partition is used for a small number of objects that have a history of being used in exploits. These are typically variable-sized data buffer objects. Outside of the Isolated Heap, checksumming has also been implemented to detect and abort if certain sensitive objects are ever altered.


# CVE-2016-0998


[CVE-2016-0998](https://code.google.com/p/google-security-research/issues/detail?id=716)was discovered by Mateusz Jurczyk and I while fuzzing the Flash Player (full code for the exploit can be found

[attached](https://bugs.chromium.org/p/project-zero/issues/detail?id=716#c4)to this bug). It was reported to Adobe on February 3, 2016 and fixed by Adobe on March 10, 2016. It is a good example of a bug that the Isolated Heap makes more difficult to exploit.


The bug is an uninitialized variable in the fix to an ActionScript 2 use-after-free bug. Roughly 80 of these types of issues have been fixed by Adobe in the past year, and two uninitialized variable issues were introduced in the fixes.


This issue is fairly easy to reproduce, a proof-of-concept for this issue in its entirety is:


var o = {};

o.unwatch();


The bug occurs because the use-after-free check in the unwatch method attempts to convert its first parameter to a string by calling toString on it before continuing with the part of the method where toString  could cause problems by freeing an object. However, Flash does not check that this parameter exists before calling toString on it. In pseudo-code, the rough behaviour of this method is:


void\* args = alloca( args\_size );

for( int i = 0; i \< args\_size; i++){

// Init args

}

if ( ((int) args\[0\]) & 6 == 6 )

args\[0\] = call\_toString( args\[0\] );

if ( args\_size \< 1)

exit();


There’s a few interesting things to note about this bug. First, on Flash, alloca(0) allocates 16 bytes (the minimum allowed size), but the initialization loop doesn’t run, so this memory contains whatever was on the stack the last time this memory was used, which is not part of the current call. Second, the vulnerable behaviour only occurs if the object on the stack ends in 6. The purpose of this behaviour is to ensure that the parameter is a ScriptObject -- Flash arguments can be many types, such a strings, integers, objects, etc., and the last three bits of the value indicates its type, with 6 indicating a ScriptObject. Finally, this bug bails pretty quickly if the argument array is too small. There’s only one function, call\_toString that’s called on the uninitialized value. This function searches through the ScriptObject’s variables for a method called toString, and then calls it, calling some virtual methods in the process.


With the above constraints, there are a few ways to exploit this bug:


1. Put an absolute pointer value on the stack. The benefit of this is that you can guarantee that it ends in 6. The downside is that you need a separate bug to bypass ASLR, because there’s no way to get your bearings otherwise
2. Put a pointer to some type of object or buffer that is not a ScriptObject on the stack, and use type confusion for the exploit. This is somewhat challenging for this particular bug, because valid pointers that end in 6 are unusual on the stack, as most of the time they are aligned. The only situation where unaligned pointers are typically on the stack is when manipulating data buffers such as strings where each byte is accessed individually.
3. Make this bug into a use-after-free. Put a stale pointer to a ScriptObject on the stack and wait for it to be freed and reallocated, and then use type confusion for the exploit


Option 2 seemed the most practical up front, but the Isolated Heap posed some challenges. As noted above, if a call puts an unaligned pointer on the stack, it is probably manipulating some sort of byte data that does not contain pointers, as pointer access needs to be aligned. So it is probably possible to make args\[0\] point to a buffer type, such as a ByteArray in ActionScript, but ASLR is still a problem, because call\_toString calls virtual functions on args\[0\] , and without knowing the location of any code addresses, the address in the buffer that will be treated as a vtable can’t be set to a reasonable value. One possible way of solving this problem would be to have args\[0\] point to a buffer, and then realloc it to be something else that has a valid vtable, but all script-controllable byte buffers are allocated in partition 3, which is not used for any other data types that contain pointers, so this isn’t possible with the Isolated Heap.


I then tried Option 3, and tried to reallocate a different object in the place of a ScriptObject. This bug more amenable to this than a lot of other bugs, because there’s no limitation to when the object needs to be reallocated, other than it needs to be reallocated after the pointer to it is outside of the valid stack (i.e. the stack pointer is higher than the address of the value), and it needs to remain allocated until it is used by the bug. These constraints aren’t very limiting, as basically any object in the Flash Player can be allocated in this window. That said, only allocations with the same partition, type and size as a ScriptObject will be allocated in the freed memory. Looking at object allocations in Flash, only about 10 other objects have these properties, and they all extend the same class, the AS3 ScriptObject class (which is different from the AS2 ScriptObject that is freed). Unfortunately though, the first virtual function that this bug calls on the reallocated buffer maps to [ScriptObject::getDescendants](https://github.com/nxmirrors/tamarin-central/blob/master/core/ScriptObject.cpp), which immediately throws an ActionScript 3 exception, which leads to a null pointer crash, because exception handlers haven’t been properly initialized. So in this case, there isn’t an appropriate object that can be allocated in the place of an AS3 ScriptObject that can make this bug exploitable as a use-after-free.


At this point, I didn’t think it was very likely that this bug would be exploitable without a second information leak vulnerability, so I tried exploiting it with a second bug.


# CVE-2016-0984


[CVE-2016-0984](https://code.google.com/p/google-security-research/issues/detail?id=698)is a use-after-free in sound processing in which the freed buffer can only be read. I reported CVE-2016-0984 on January 11, 2016 and Adobe released a patch on February 16, 2016.


A proof-of-concept for the bug is as follows:


var s = new Sound();

var b = new ByteArray();

for( var i = 0; i \< 1600; i++){

b.writeByte(1);

}

b.position = 0;

s.loadPCMFromByteArray(b, 100, "float", false, 2.0);

var c = new ByteArray();

for(var i = 0; i \< 2; i++){

c.writeByte(1); 

}

c.position = 0;

try{

s.loadPCMFromByteArray(c, 1, "float", false, 2.0);

}catch(e:Error){  

trace(e.message);

}


var d = new ByteArray();

s.extract(d, 1, 0);


This bug is related to exception handling in the loadPCMFromByteArray method. This method loads sound data from an array that is provided by ActionScript, and then processes it, and stores it internally in the Sound object. The general flow of the function is as follows:


if ( input\_size \< needed\_size ){ // needed\_size is wrong

throwASException();

}

delete\[\] m\_pcm;

char\* sound\_data = new char\[input\_size\];

for( int i = 0; i \< input\_size; i++){

sound\_data = inputArray.readStuff(); // can throw exception

}

m\_pcm = sound\_data;


The code attempts to check that the array is the right size and throws an exception before it does any pointer manipulation, but there is an arithmetic error in how the size is calculated, so some situations in which the array is too small will get through (see the [tracker](https://code.google.com/p/google-security-research/issues/detail?id=698) for exact details on how to trigger this condition). In this case, the input array will throw an exception when it is read, which means that m\_pcm will be freed but not reallocated. This is a fairly versatile bug, in that the array that is freed can be of any size, though it is always a character array in partition 2, the data heap.


The first step was to use this bug to obtain the address of a vtable to break ASLR. It wasn’t immediately obvious how to do this, as the heap partition the array is allocated if generally used for primitive arrays. There were two exceptions to this I was aware of. First, arrays of pointer that aren’t void pointers are allocated on this heap, but this isn’t particularly helpful for this bug, as they tend to be pointers to other primitive data types, and even if they were pointers to objects, there’s no way to use this bug to iterate through pointers, it can only be used to read values off the heap without knowing their location. Another property I noticed is that object arrays are also allocated in this partition, so if an array of objects that call virtual methods (or contain function pointers) is allocated, you could read the code pointers off of the heap. When I looked though, I couldn’t find a single array of virtual objects allocated in a way that is script-controllable in Flash, as arrays of pointers are usually used instead.


Eventually, I discovered that the ActionScript JIT LIR implements its own [basic heap](https://github.com/nxmirrors/tamarin-central/blob/master/nanojit/Allocator.h), and allocates new pages as large char arrays, which are allocated in the same heap partition as other char arrays. These pages have variable sizes, and often contain objects with vtables. By selecting a PCM array allocation size that lines up with a frequent LIR allocation, I was able to read a vtable off the heap.


The next step was to get a pointer to a buffer I could control in script. It is possible to also use CVE-2016-0998 for this, but I suspected that using this bug could do it more simply and reliably. Since arrays of char pointers are allocated on the same heap partition as sound PCM data, char pointers could be easily read. I used the AS3 function [LocaleID.determinePreferredLocales](<http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/globalization/LocaleID.html#determinePreferredLocales()>) to allocate a char\* array based on the String vector that is provided as input. Unfortunately though, ActionScript strings aren’t ideal for exploits. They are immutable after they are allocated, and worse, they terminate as soon as a NULL character is reached, which means on 64-bit systems, they can only ever contain one pointer. The best solution to this would be to allocate an array of pointers to something more controllable, such as a byte or int Array, but unfortunately in ActionScript, arrays of these types of pointers are fairly unusual, and when they exist, their size is usually not controllable from script. So instead, I reallocated the string data that the char pointers pointed to, so that they were integer arrays instead. This was possible in part because the strings allocated internal to the LocaleID.determinePreferedLocales method are not true Flash strings that are accessible via script, but character arrays, so they show up in partition 2 of the heap (the data partition) as opposed to partition 3 (the exploitable objects partition).


I used the [BitmapData.paletteMap](<http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/display/BitmapData.html#paletteMap()>) method to allocate integer arrays in the place of the character arrays allocated by LocaleID.determinePreferedLocales. This method accepts input of four integer arrays of size 256, and copies them to a larger int array of length 1024. These arrays are not mutable, but since the vtable pointer, and the pointer to the buffer have been determined at this point, it doesn’t matter, as all values that need to be in the array can be calculated before the array is created. Another undesirable property of this method is that the arrays are freed at the end, but there is a trick for getting around it. If any element of the arrays provided to the method is not an integer, Flash will attempt to call valueOf on it to convert it to a number. So if a late element (for example, the last element of the fourth array) has a valueOf that throws an exception, execution of the method will stop. In this case, the large int array will be allocated, and most of the input will be copied to it, but the part of the function that processes and frees the arrays will be skipped. This is a useful trick to avoid objects being freed that works in a lot of methods.


At this point, we have a pointer to a vtable, and a pointer to a buffer we control, so it’s fairly straightforward to gain code execution using CVE-2016-0998

# Putting it all together


For CVE-2016-0998 to use the allocated buffer, a pointer to it with the final three bits set to 6 needs to be put on the stack. There are a few ways to do this, one of them being UTF conversion. UTF-8 to UTF-16 conversion is done on the stack if the length of resulting UTF-16 string is less than 256 bytes, which leads to the character values of the string being written to the stack.


To start off, my exploit grows the stack. This is just to avoid any values that have already been written from causing problems. This isn’t as straightforward as one would expect. The ActionScript stack is not the same as the C++ stack (where this bug occurs), so calling a function recursively in ActionScript won’t grow it. Instead, there needs to be a loop in C++. To cause this, I triggered a situation where toString would be called recursively, which would be done in C++. In ActionScript:


\_global.v = 31;

\_global.mc = this;

var o = {toString : f};

this.swapDepths(o);


function f(){

if(\_global.v > 0){

\_global.v = \_global.v - 1;

\_global.mc.swapDepths(this);

}else{


var t = \_global.mc;

t.swapDepths(d, 2);

}

return

"ffffffffffffffffffffffffffffffffffffffffffffffffffffffff";

}


This code calls swapDepths, which calls toString from C++, which then recursively calls swapDepths again, growing the stack.


The value that is returned from this type of function then gets converted from UTF-8 to UTF-16, so its contents get put on the stack. This can be used to put the pointer to the the controllable buffer on the stack. Unfortunately, conversion only happens if the String is encoded statically in the SWF, a string generated during AS execution won’t work. So a SWF needs to dynamically be created as a part of the exploit.


This process can be seen in [test.cgi](https://bugs.chromium.org/p/project-zero/issues/detail?id=716). The first part of the exploit, soundPCM.swf uses CVE-2016-0984 to break ASLR and create a buffer, and then it passes the location of the buffer to test.cgi via URL parameters in JavaScript. This calls into Python, and adds the correct address into a static string in a SWF called new.swf. Note that a UTF-8 converter is implemented in Python, this is because standard UTF encoding leads to characters of different lengths, and putting different lengths of strings into the SWF causes “movement” in memory when it is loaded, which can cause problems with the exploit which relies on static offsets. The implemented converter always creates three-byte UTF-8 encodings even if a shorter one is possible based on the specific buffer pointer value. Also note that the full string in the SWF will not get fully converted, because the 0x0000 value at the beginning of the 64-bit pointer will be treated as a null, and processing will stop. This isn’t ideal, it means that only one pointer can ever be copied to the stack, but it is a constraint that can be worked around.


At this point, we have a SWF that puts a pointer to the buffer on the stack, we now just need to trigger the exploit. I encoded this into the same SWF for simplicity. Once the SWF has been created, it is loaded once with URL parameter num=15, which sets up the stack, and then with URL parameter num=14, which triggers the bug, causing native toString to be called on the buffer that’s provided.

# What’s in the buffer

The last step is to figure out what to put in the buffer. Running through the native call, there’s a few pointers that need to be set to something valid to avoid crashes (I pointed them back to various locations in the same buffer), and then a virtual call is made to the buffer. Setting the memory at the head of the buffer the call sees as the vtable to a location later in the buffer, and creating a fake vtable in that memory, it’s possible to make a call into a gadget. This exploit uses the following one:


mov rdi, rax

call \[rax + 0x28\]


This sets rdi to the head of the vtable, which is set to a string command, and then rax + 0x28 (0x28 bytes into the vtable) is set a location which calls system in the Flash plug-in, which triggers a call to system.

# Conclusion

The Isolated Heap made exploiting CVE-2016-0998 more difficult and time consuming, and also made exploitation require a separate information leak bug, which probably would not have been required before the heap changes. There are a couple weaknesses in the Isolated heap, especially the use of the data partition for JIT allocation, and allocating pointer arrays on the data heap. We are working with Adobe to implement improvements to the Isolated Heap in future versions of Flash. It is challenging to harden a heap against exploitation, especially in the face of high-quality bugs, but the Isolated Heap is a substantial improvement.
