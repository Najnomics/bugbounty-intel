# BitUnmap: Attacking Android Ashmem - Project Zero

Source: https://projectzero.google/2016/12/bitunmap-attacking-android-ashmem.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Gal Beniamini, Project Zero

The [law of leaky abstractions](http://www.joelonsoftware.com/articles/LeakyAbstractions.html) states that “all non-trivial abstractions, to some degree, are leaky”. In this blog post we’ll explore the ashmem shared memory interface provided by Android and see how false assumptions about its internal operation can result in security vulnerabilities affecting core system code.

We’ll walk through the process of discovering and exploiting a vulnerability resulting from this leaky abstraction, which will allow us to elevate our privileges from any Android application to a multitude of privileged contexts, including the highly-privileged “system\_server”. This vulnerability has been present in the core Android platform code for the Marshmallow and Nougat versions. It has now been fixed in the [recent Android bulletin](https://source.android.com/security/bulletin/2016-11-01.html). For a detailed disclosure timeline, see the “Timeline” section below.

## One Device to Bind Them

As you know, Android applications can perform inter-process communication (for example, in order to communicate with various Android services), by using the Android [binder](https://www.nds.rub.de/media/attachments/files/2012/03/binder.pdf). Initially, each Android service registers itself with a central daemon; the “service manager”. Subsequently, applications may contact the daemon in order to request “handles” with which the registered services may be contacted.

In keeping with good IPC design, the interface provided by binder itself is rather simplified. In fact, binder transactions are capped to a size of [at-most 1MB](https://developer.android.com/reference/android/os/TransactionTooLargeException.html). Well then, what about scenarios in which we need to transfer a large amount of data to a system service? For example, what if we want to modify the phone’s wallpaper? What about playing a media file? Surely we wouldn’t need to “re-invent” a mechanism through which memory can be shared in larger quantities between processes using binder transactions.

Indeed, there’s no need to worry. You see, binder transactions support the transfer of more than just binary data. In fact, binder transactions can be used to transfer file descriptors and even other binder handles. For instance, this is how the “service manager” is able to provide processes with handles through which they may communicate with the requested services.


Great, so we have a means of communicating with other processes - even in large volumes. But what about cases where we’d like to share (rather than simply transfer) large quantities of memory? Once again - no need to worry! For this purpose, Android has introduced a means of sharing memory, called “ashmem” (Android Shared Memory).

## Sharing (memory) is Caring

So what exactly is ashmem? In short, each ashmem file descriptor acts as a handle to a shared memory region. The device also allows the user to perform several memory-sharing operations via a set of supported ioctls. These allow the user to set the size of the shared memory region referred to by the ashmem file descriptor, modify the name of the shared region and even control the protection mask with which this descriptor may be mmap-ed.

Let’s take a closer look at the actual implementation of the ashmem device, starting with the ioctl used to control the size of a shared memory region - [ASHMEM\_SET\_SIZE](http://androidxref.com/kernel_3.18/xref/drivers/staging/android/ashmem.c#753):

| static long [ashmem\_ioctl](http://androidxref.com/kernel_3.18/s?refs=ashmem_ioctl&project=drivers)(struct [file](http://androidxref.com/kernel_3.18/s?refs=file&project=drivers) \*[file](http://androidxref.com/kernel_3.18/s?refs=file&project=drivers), unsigned int [cmd](http://androidxref.com/kernel_3.18/s?refs=cmd&project=drivers), unsigned long [arg](http://androidxref.com/kernel_3.18/s?refs=arg&project=drivers)) { struct [ashmem\_area](http://androidxref.com/kernel_3.18/xref/drivers/staging/android/ashmem.c#ashmem_area) \*[asma](http://androidxref.com/kernel_3.18/s?refs=asma&project=drivers) = [file](http://androidxref.com/kernel_3.18/s?defs=file&project=drivers)->[private\_data](http://androidxref.com/kernel_3.18/s?defs=private_data&project=drivers); long [ret](http://androidxref.com/kernel_3.18/s?refs=ret&project=drivers) = -[ENOTTY](http://androidxref.com/kernel_3.18/s?defs=ENOTTY&project=drivers);           **...** | 

As we can see above, this ioctl simply allows the user to pass in any size. As long as the shared memory region has not been mapped yet, the device will happily record the passed-in size as the underlying size corresponding to the memory region. Not only that, but the recorded size can then be queried by the user by issuing the corresponding ioctl -

[ASHMEM\_GET\_SIZE](http://androidxref.com/kernel_3.18/xref/drivers/staging/android/ashmem.c#760).

So… this looks rather suspicious. What exactly does “setting the size” actually mean? Recall that ashmem regions are mapped-in by calling mmap, and, as we know, the mmap syscall receives an argument denoting the size of the mapping to be created.

This begs the question: what if the size of a created mapping does not match the size of an ashmem region? Perhaps the implementation of mmap will simply ignore the passed in size argument and use the size provided in ASHMEM\_SET\_SIZE? Perhaps, instead, the implementation of mmap will simply ignore the underlying size and use the size argument instead? There’s only one way to [find out](http://androidxref.com/kernel_3.18/xref/drivers/staging/android/ashmem.c#361):

| static int [ashmem\_mmap](http://androidxref.com/kernel_3.18/s?refs=ashmem_mmap&project=drivers)(struct [file](http://androidxref.com/kernel_3.18/s?refs=file&project=drivers) \*[file](http://androidxref.com/kernel_3.18/s?refs=file&project=drivers), struct [vm\_area\_struct](http://androidxref.com/kernel_3.18/s?defs=vm_area_struct&project=drivers) \*[vma](http://androidxref.com/kernel_3.18/s?refs=vma&project=drivers)) { struct [ashmem\_area](http://androidxref.com/kernel_3.18/xref/drivers/staging/android/ashmem.c#ashmem_area) \*[asma](http://androidxref.com/kernel_3.18/s?refs=asma&project=drivers) = [file](http://androidxref.com/kernel_3.18/s?defs=file&project=drivers)->[private\_data](http://androidxref.com/kernel_3.18/s?defs=private_data&project=drivers); ... if (![asma](http://androidxref.com/kernel_3.18/s?defs=asma&project=drivers)->[file](http://androidxref.com/kernel_3.18/s?defs=file&project=drivers)) { ... | 

As we can see above, while the actual shared memory file is created using the size of the shared memory region (using “shmem\_file\_setup”), the memory mapping itself is created using the size in the virtual memory area (vma) - that is, the size passed in to mmap.

Let’s take a step back and reflect on this decision.

Essentially, this means that developers who attempt to use an ashmem region must take special care to always call mmap using the same size of the underlying shared memory region. Failing to do so will not return any visible error code to the developer, but will instead create a mapping with potentially dangerous consequences.

For starters, if a developer mmap-s a region with a size larger than the actual underlying region’s size, any attempt to access memory beyond the bounds of the underlying region will result in a illegal access, sending the SIGBUS signal to the process (which will then probably subsequently terminate).

But there’s another, more interesting, potential pitfall. What if the developer erroneously assumes that size of the underlying shared memory region and the mmap-ed size must be equal to one another? To try and answer this question, I’ve audited all instances of Android services which use ashmem to share memory with a user. From here on, we’ll focus on one such case - Bitmaps.

## Mismatching Assumptions

As we mentioned earlier, one operation which requires the transfer of potentially large quantities of memory from one process to another is the exchange of images. For this purpose, Android exposes the [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html) class, which can be easily serialized into a binder parcel.

As Bitmaps may be larger than the 1MB limit for binder transactions, the image’s data must be transferred via other means - such as ashmem. Indeed, for bitmaps above a certain size, this is exactly how this data is transferred. We can see that by looking at the “unflattening” function, “[Bitmap\_createFromParcel](http://androidxref.com/7.0.0_r1/xref/frameworks/base/core/jni/android/graphics/Bitmap.cpp#947)”:

| [android](http://androidxref.com/7.0.0_r1/xref/frameworks/base/core/jni/android/graphics/Bitmap.cpp#android)::[Parcel](http://androidxref.com/7.0.0_r1/s?defs=Parcel&project=frameworks)\* p = [android](http://androidxref.com/7.0.0_r1/xref/frameworks/base/core/jni/android/graphics/Bitmap.cpp#android)::[parcelForJavaObject](http://androidxref.com/7.0.0_r1/s?defs=parcelForJavaObject&project=frameworks)([env](http://androidxref.com/7.0.0_r1/s?defs=env&project=frameworks), [parcel](http://androidxref.com/7.0.0_r1/s?defs=parcel&project=frameworks)); const  [SkColorType](http://androidxref.com/7.0.0_r1/s?defs=SkColorType&project=frameworks) [colorType](http://androidxref.com/7.0.0_r1/s?refs=colorType&project=frameworks) = ([SkColorType](http://androidxref.com/7.0.0_r1/s?defs=SkColorType&project=frameworks))p->[readInt32](http://androidxref.com/7.0.0_r1/s?defs=readInt32&project=frameworks)(); const  [SkAlphaType](http://androidxref.com/7.0.0_r1/s?defs=SkAlphaType&project=frameworks) [alphaType](http://androidxref.com/7.0.0_r1/s?refs=alphaType&project=frameworks) = ([SkAlphaType](http://androidxref.com/7.0.0_r1/s?defs=SkAlphaType&project=frameworks))p->[readInt32](http://androidxref.com/7.0.0_r1/s?defs=readInt32&project=frameworks)(); const int [width](http://androidxref.com/7.0.0_r1/s?refs=width&project=frameworks) = p->[readInt32](http://androidxref.com/7.0.0_r1/s?defs=readInt32&project=frameworks)(); const int [height](http://androidxref.com/7.0.0_r1/s?refs=height&project=frameworks) = p->[readInt32](http://androidxref.com/7.0.0_r1/s?defs=readInt32&project=frameworks)(); const int [rowBytes](http://androidxref.com/7.0.0_r1/s?refs=rowBytes&project=frameworks) = p->[readInt32](http://androidxref.com/7.0.0_r1/s?defs=readInt32&project=frameworks)(); … [std](http://androidxref.com/7.0.0_r1/s?defs=std&project=frameworks)::[unique\_ptr](http://androidxref.com/7.0.0_r1/s?defs=unique_ptr&project=frameworks)\<[SkBitmap](http://androidxref.com/7.0.0_r1/s?path=SkBitmap)> [bitmap](http://androidxref.com/7.0.0_r1/s?defs=bitmap&project=frameworks)(new [SkBitmap](http://androidxref.com/7.0.0_r1/s?defs=SkBitmap&project=frameworks)); if (! [bitmap](http://androidxref.com/7.0.0_r1/s?defs=bitmap&project=frameworks)->[setInfo](http://androidxref.com/7.0.0_r1/s?defs=setInfo&project=frameworks)([SkImageInfo](http://androidxref.com/7.0.0_r1/s?defs=SkImageInfo&project=frameworks)::[Make](http://androidxref.com/7.0.0_r1/s?defs=Make&project=frameworks)([width](http://androidxref.com/7.0.0_r1/s?defs=width&project=frameworks), [height](http://androidxref.com/7.0.0_r1/s?defs=height&project=frameworks), [colorType](http://androidxref.com/7.0.0_r1/s?defs=colorType&project=frameworks), [alphaType](http://androidxref.com/7.0.0_r1/s?defs=alphaType&project=frameworks)), [rowBytes](http://androidxref.com/7.0.0_r1/s?defs=rowBytes&project=frameworks))) { return  [NULL](http://androidxref.com/7.0.0_r1/s?defs=NULL&project=frameworks); } … [size\_t](http://androidxref.com/7.0.0_r1/s?defs=size_t&project=frameworks) [size](http://androidxref.com/7.0.0_r1/s?refs=size&project=frameworks) = [bitmap](http://androidxref.com/7.0.0_r1/s?defs=bitmap&project=frameworks)->[getSize](http://androidxref.com/7.0.0_r1/s?defs=getSize&project=frameworks)(); [android](http://androidxref.com/7.0.0_r1/xref/frameworks/base/core/jni/android/graphics/Bitmap.cpp#android)::[Parcel](http://androidxref.com/7.0.0_r1/s?defs=Parcel&project=frameworks)::[ReadableBlob](http://androidxref.com/7.0.0_r1/s?defs=ReadableBlob&project=frameworks) [blob](http://androidxref.com/7.0.0_r1/s?refs=blob&project=frameworks); [android](http://androidxref.com/7.0.0_r1/xref/frameworks/base/core/jni/android/graphics/Bitmap.cpp#android)::[status\_t](http://androidxref.com/7.0.0_r1/s?defs=status_t&project=frameworks) [status](http://androidxref.com/7.0.0_r1/s?refs=status&project=frameworks) = p->[readBlob](http://androidxref.com/7.0.0_r1/s?defs=readBlob&project=frameworks)([size](http://androidxref.com/7.0.0_r1/s?defs=size&project=frameworks), &[blob](http://androidxref.com/7.0.0_r1/s?defs=blob&project=frameworks)); … } | 

First, the image’s metadata is extracted from the parcel and is used to construct an SkBitmap instance to hold this information. Next, the function proceeds to reads the actual bitmap’s data by calling Parcel::readBlob.

However, this looks potentially dangerous! First of all, note that the function uses the SkBitmap instance (i.e., the one holding all the metadata we read earlier on) in order to calculate the “size” of the resulting bitmap’s data. Then, it calls Parcel::readBlob in order to actually read the transferred data, while using the previously calculated size as an input argument.

Finally, let’s take a look at how Parcel::readBlob actually reads the enclosed Bitmap’s data:

| [status\_t](http://androidxref.com/7.0.0_r1/s?defs=status_t&project=frameworks) [Parcel](http://androidxref.com/7.0.0_r1/xref/frameworks/native/libs/binder/Parcel.cpp#Parcel)::[readBlob](http://androidxref.com/7.0.0_r1/s?refs=readBlob&project=frameworks)([size\_t](http://androidxref.com/7.0.0_r1/s?defs=size_t&project=frameworks) [len](http://androidxref.com/7.0.0_r1/s?refs=len&project=frameworks), [ReadableBlob](http://androidxref.com/7.0.0_r1/s?defs=ReadableBlob&project=frameworks)\* [outBlob](http://androidxref.com/7.0.0_r1/xref/frameworks/native/libs/binder/Parcel.cpp#outBlob)) const { [int32\_t](http://androidxref.com/7.0.0_r1/s?defs=int32_t&project=frameworks) [blobType](http://androidxref.com/7.0.0_r1/s?refs=blobType&project=frameworks); [status\_t](http://androidxref.com/7.0.0_r1/s?defs=status_t&project=frameworks) [status](http://androidxref.com/7.0.0_r1/s?refs=status&project=frameworks) = [readInt32](http://androidxref.com/7.0.0_r1/s?defs=readInt32&project=frameworks)(&[blobType](http://androidxref.com/7.0.0_r1/xref/frameworks/native/libs/binder/Parcel.cpp#blobType)); } | 

Aha! This is exactly what we were looking for. Instead of using the underlying size of the memory region, Parcel::readBlob performs an mmap operation using our own controlled length argument (i.e., the size computed from the bitmap’s metadata).

In and of itself, this is already a bad practice; the user could pass in an ashmem descriptor with any arbitrary size, resulting in an “invalid” memory mapping of the type we discussed earlier. This, in turn, would trigger a SIGBUS if the receiving application attempts to access the mmap-ed memory region.

But perhaps we can do better than just creating an invalid mapping? We’ve seen how the memory is mapped-in when creating a Bitmap, but how is it unmapped?

Well, after reading in the bitmap’s data, Bitmap\_createFromParcel proceeds to store the information about the mapped data in the constructed Bitmap instance:

| [Bitmap](http://androidxref.com/7.0.0_r1/s?refs=Bitmap&project=frameworks)::[Bitmap](http://androidxref.com/7.0.0_r1/s?refs=Bitmap&project=frameworks)(void\* [address](http://androidxref.com/7.0.0_r1/s?refs=address&project=frameworks), int [fd](http://androidxref.com/7.0.0_r1/s?refs=fd&project=frameworks), const  [SkImageInfo](http://androidxref.com/7.0.0_r1/s?defs=SkImageInfo&project=frameworks)& [info](http://androidxref.com/7.0.0_r1/s?defs=info&project=frameworks), [size\_t](http://androidxref.com/7.0.0_r1/s?defs=size_t&project=frameworks) [rowBytes](http://androidxref.com/7.0.0_r1/s?defs=rowBytes&project=frameworks), [SkColorTable](http://androidxref.com/7.0.0_r1/s?defs=SkColorTable&project=frameworks)\* [ctable](http://androidxref.com/7.0.0_r1/s?defs=ctable&project=frameworks)) :  [mPixelStorageType](http://androidxref.com/7.0.0_r1/s?defs=mPixelStorageType&project=frameworks)([PixelStorageType](http://androidxref.com/7.0.0_r1/s?defs=PixelStorageType&project=frameworks)::[Ashmem](http://androidxref.com/7.0.0_r1/s?defs=Ashmem&project=frameworks)) { [mPixelStorage](http://androidxref.com/7.0.0_r1/s?defs=mPixelStorage&project=frameworks).[ashmem](http://androidxref.com/7.0.0_r1/s?defs=ashmem&project=frameworks).[address](http://androidxref.com/7.0.0_r1/s?defs=address&project=frameworks) = [address](http://androidxref.com/7.0.0_r1/s?defs=address&project=frameworks); [mPixelStorage](http://androidxref.com/7.0.0_r1/s?defs=mPixelStorage&project=frameworks).[ashmem](http://androidxref.com/7.0.0_r1/s?defs=ashmem&project=frameworks).[fd](http://androidxref.com/7.0.0_r1/s?defs=fd&project=frameworks) = [fd](http://androidxref.com/7.0.0_r1/s?defs=fd&project=frameworks); [mPixelStorage](http://androidxref.com/7.0.0_r1/s?defs=mPixelStorage&project=frameworks).[ashmem](http://androidxref.com/7.0.0_r1/s?defs=ashmem&project=frameworks).[size](http://androidxref.com/7.0.0_r1/s?defs=size&project=frameworks) = [ashmem\_get\_size\_region](http://androidxref.com/7.0.0_r1/s?defs=ashmem_get_size_region&project=frameworks)([fd](http://androidxref.com/7.0.0_r1/s?defs=fd&project=frameworks)); [mPixelRef](http://androidxref.com/7.0.0_r1/s?defs=mPixelRef&project=frameworks).[reset](http://androidxref.com/7.0.0_r1/s?defs=reset&project=frameworks)(new [WrappedPixelRef](http://androidxref.com/7.0.0_r1/s?defs=WrappedPixelRef&project=frameworks)(this, [address](http://androidxref.com/7.0.0_r1/s?defs=address&project=frameworks), [info](http://androidxref.com/7.0.0_r1/s?defs=info&project=frameworks), [rowBytes](http://androidxref.com/7.0.0_r1/s?defs=rowBytes&project=frameworks), [ctable](http://androidxref.com/7.0.0_r1/s?defs=ctable&project=frameworks))); // Note: this will trigger a call to onStrongRefDestroyed(), but // we want the pixel ref to have a ref count of 0 at this point [mPixelRef](http://androidxref.com/7.0.0_r1/s?defs=mPixelRef&project=frameworks)->[unref](http://androidxref.com/7.0.0_r1/s?defs=unref&project=frameworks)(); } | 

However, instead of using the size of the previously created mapping, the constructor simply retrieves the size of the mapping using the ASHMEM\_GET\_SIZE ioctl (using the thin-wrapper ashmem\_get\_size\_region). This is, once more, a false assumption - namely, that the underlying ashmem size and the size of the mmap-ed region must be equal to one another. Finally, once the bitmap is freed, the area is unmapped by calling:

| ... case [PixelStorageType](http://androidxref.com/7.0.0_r1/s?defs=PixelStorageType&project=frameworks)::[Ashmem](http://androidxref.com/7.0.0_r1/s?defs=Ashmem&project=frameworks): [munmap](http://androidxref.com/7.0.0_r1/s?defs=munmap&project=frameworks)([mPixelStorage](http://androidxref.com/7.0.0_r1/s?defs=mPixelStorage&project=frameworks).[ashmem](http://androidxref.com/7.0.0_r1/s?defs=ashmem&project=frameworks).[address](http://androidxref.com/7.0.0_r1/s?defs=address&project=frameworks), [mPixelStorage](http://androidxref.com/7.0.0_r1/s?defs=mPixelStorage&project=frameworks).[ashmem](http://androidxref.com/7.0.0_r1/s?defs=ashmem&project=frameworks).[size](http://androidxref.com/7.0.0_r1/s?defs=size&project=frameworks)); [close](http://androidxref.com/7.0.0_r1/s?defs=close&project=frameworks)([mPixelStorage](http://androidxref.com/7.0.0_r1/s?defs=mPixelStorage&project=frameworks).[ashmem](http://androidxref.com/7.0.0_r1/s?defs=ashmem&project=frameworks).[fd](http://androidxref.com/7.0.0_r1/s?defs=fd&project=frameworks)); break; ... } } | 

Putting it all together, this means that the mmap and the munmap calls are performed with potentially different length arguments, both of which are fully controllable by the attacker:

- The length of the mmap operation is calculated from the bitmap’s metadata
- The length of the munmap operation is calculated from the ashmem’s size

The mismatch between the mmap-ed and munmap-ed length provides us with a great exploitation primitive! Specifically, we could supply a short length for the mmap operation and a longer length for the munmap operation - thus resulting in deletion of an arbitrarily large range of virtual memory following our bitmap object. Moreover, there’s no need for the deleted range to contain one continuous memory mapping, since the range supplied in munmap [simply ignores unmapped pages](https://linux.die.net/man/3/munmap).

Once we delete a range of memory, we can then attempt to “re-capture” that memory region with controlled data, by causing another allocation in the remote process. By doing so, we can forcibly “free” a data structure and replace its contents with our own chosen data -- effectively forcing a use-after-free condition.

From here on, we’ll refer to these crafted bitmaps with mismatching lengths as “BitUnmap”s.


## Thinking of an Exploit Strategy

### Finding a Target Service

Okay - now that we finally have a good exploitation primitive, how can we use it in order to write a stable exploit that will allow us to gain code execution in system\_server? First of all, we’ll need to find a binder call in system\_server which un-flattens a Bitmap object (or unparcels a Bundle containing a Bitmap) from a binder transaction. Moreover, it would be advantageous if we were able to access this call from any context, requiring no permissions.

Luckily, system\_server houses many different binder services, increasing the odds of finding a comfortably exploitable endpoint.

One such candidate is the “notification” service, which provides an interface for interaction with the notification bar. Among the operations supported by this service, any application (even those running in the isolated\_app SELinux context and those requiring no permissions whatsoever) may attempt to add a notification object which is then handled by the notification service. Moreover, Notification objects are [complex](http://androidxref.com/7.0.0_r1/xref/frameworks/base/core/java/android/app/Notification.java), and may contain images (bitmaps) along with the presented text.


Using notifications is also advantageous for a completely different reason - their lifetime is controlled by the attacker. Remember that after we free a memory range in the remote process, we’d like to re-capture that memory region with our own controlled data. Well, as we’ve already seen, Bitmap objects are mmap-ed into the remote address-space, and contain completely controlled data. What’s more, once a notification is added to the notification bar, the Notification object will remain referenced in the remote process (until the notification is removed). This effectively means we can use notifications for a dual purpose:

- Sending crafted BitUnmaps to delete memory ranges in the remote process
- Sending regular Bitmaps with controlled data in order to reclaim freed regions

### Finding a Target Data Structure

After we’ve established our ability to unmap arbitrarily large memory regions in system\_server by crafting our own Notification objects containing BitUnmap instances, we still need to think of a method with which we’ll be able to reliably hijack control flow in system\_server. That is, we need to decide which data structure to unmap using our primitive.

First, consider the fact that our BitUnmap objects are allocated by calling mmap. Due to the [behaviour of mmap](http://androidxref.com/kernel_3.18/xref/mm/mmap.c#1922), they will simply inhabit the highest memory address between mm->mmap\_base and TASK\_SIZE which contains a sufficiently large contiguous hole. This means that, for example, attacking single C++ or Java objects would be rather difficult, as they are located in the heap and are surrounded by other data structures which we would have to “repair”.

Moreover, even if we were able to hijack such data structures, we would still need to craft their content in a way which would allow us to eventually hijack the control flow. For example, exploiting use-after-free vulnerabilities in C++ objects normally includes hijacking their vtable and replacing it with a structure pointing to other executable memory locations. With modern exploit mitigation techniques, the amount of steps required to bypass XN-bit protection and ASLR could be quite substantial.

Perhaps there’s a cleaner way to get code execution?

Optimally, we’re looking to replace a data structure that has the following properties:

- Is allocated directly using mmap (i.e., not “on the heap”)
- Therefore we don’t need to “repair” adjacent data structures
- Allows direct control over code execution
- Saves us the need to craft a complex chain to bypass mitigation techniques
- Does not require address-space dependant information unique to system\_server
- Saves us the need to find (or create) an information leak to bypass ASLR

In order to find this magical structure, I’ve written a small gdb script to monitor and log all calls to mmap coupled with their origins and sizes. This helped me group the “families” of mmap-ed objects which could be useful for exploitation. After producing the list, one such candidate stood out as having all the above properties - Threads.

### Hanging by a Thread

As we know, all threads in the same process share the same address space. Moreover, system\_server, being the large process that it is, contains many code paths which handle long-running or periodic tasks. Naturally, these code paths are handled by creating additional threads in system\_server. When threads are created, they require two data structures which are unique to each thread: the thread metadata (pthread\_internal\_t) and the thread’s stack.

Looking at the code in Android’s bionic, we can see that these two regions are, in fact, carved from the same memory region, which is [allocated using mmap](http://androidxref.com/7.0.0_r1/xref/bionic/libc/bionic/pthread_create.cpp#142):

| void\*\* [child\_stack](http://androidxref.com/7.0.0_r1/s?refs=child_stack&project=bionic)) { if ([attr](http://androidxref.com/7.0.0_r1/s?defs=attr&project=bionic)->[stack\_base](http://androidxref.com/7.0.0_r1/xref/bionic/libc/bionic/pthread_create.cpp#stack_base) == [NULL](http://androidxref.com/7.0.0_r1/s?defs=NULL&project=bionic)) { // The caller didn't provide a stack, so allocate one. // Make sure the stack size and guard size are multiples of PAGE\_SIZE. [mmap\_size](http://androidxref.com/7.0.0_r1/s?defs=mmap_size&project=bionic) = [BIONIC\_ALIGN](http://androidxref.com/7.0.0_r1/s?defs=BIONIC_ALIGN&project=bionic)([attr](http://androidxref.com/7.0.0_r1/s?defs=attr&project=bionic)->[stack\_size](http://androidxref.com/7.0.0_r1/s?defs=stack_size&project=bionic) + sizeof([pthread\_internal\_t](http://androidxref.com/7.0.0_r1/s?defs=pthread_internal_t&project=bionic)),     //Calls mmap to create the mapped space, and mprotect to create a guard page [attr](http://androidxref.com/7.0.0_r1/s?defs=attr&project=bionic)->[stack\_base](http://androidxref.com/7.0.0_r1/xref/bionic/libc/bionic/pthread_create.cpp#stack_base) = [\_\_create\_thread\_mapped\_space](http://androidxref.com/7.0.0_r1/xref/bionic/libc/bionic/pthread_create.cpp#__create_thread_mapped_space)([mmap\_size](http://androidxref.com/7.0.0_r1/s?defs=mmap_size&project=bionic), [attr](http://androidxref.com/7.0.0_r1/s?defs=attr&project=bionic)->[guard\_size](http://androidxref.com/7.0.0_r1/s?defs=guard_size&project=bionic)); … } ... } So, if we are able to deallocate a thread’s stack and immediately reclaim it as our own, we should be able to directly achieve code execution simply by virtue of already having prepared a stack which performs whichever operation we’d like to execute within system\_server. Regardless, before we can start scheming about hijacking a thread, we need to think of a way to spawn a thread in system\_server on-demand. Going through the available binder calls terminating in system\_server reveals one such comfortably accessible code-path: [AudioService::loadSoundEffects](http://androidxref.com/7.0.0_r1/xref/frameworks/base/services/core/java/com/android/server/audio/AudioService.java#2527). This binder command can be called without requiring any permissions, and causes the AudioService to load a predefined set of sound effects in its internal “sound pool”. Creating such a pool causes system\_server to spawn several threads:     In this exploit we’ll hijack the “SoundPoolThread”, for a variety of reasons: It is the first thread created when creating a new sound pool. This fact will come in handy later, when we try and force it to be allocated in a controlled memory region. After initializing a sound pool, the “SoundPoolThread” awaits further commands by[waiting on a condition variable](http://androidxref.com/7.0.0_r1/xref/frameworks/base/media/jni/soundpool/SoundPoolThread.cpp#38). Until the condition variable is signaled, the “futex” system-call will not return. As the thread will not access its stack while it is waiting for the system-call to return, this allows us to replace the thread’s stack with our own, leaving the thread none the wiser. Once we’ve performed our switch, we can trigger a chain of events (such as closing the sound pool by calling unloadSoundEffects) which will signal the condition variable and cause the system-call to return. Once the sound pool is closed, the SoundPoolThread is no longer needed and simply terminates anyway. This means we can safely hijack it without causing any adverse effects in system\_server. | 

### A Short ROP Chain

Once we hijack the SoundPoolThread’s stack, we’ll need to replace it with our own ROP stack. So, what should we run there? Well, for versions of Android prior to 7.0, we could simply write a short ROP chain which mmap-s one of our ashmem file descriptors with executable access-permissions, and then jumps directly to it. Indeed, this would allow us to simply place executable code at the base of an ashmem descriptor and send it along to system\_server.

However, as of Android 7.0, this solution would no longer work. This is because starting from Android 7.0, a new set of mitigations have begun to roll out which aim to prevent unauthorised code execution within system\_server (and other privileged processes). A small subset of these rules can be [seen here](http://androidxref.com/7.0.0_r1/xref/system/sepolicy/system_server.te):

\# system\_server should never use JIT functionality

neverallow system\_server self:process execmem;

neverallow system\_server ashmem\_device:chr\_file execute;

neverallow system\_server system\_server\_tmpfs:file execute;

Specifically, the second rule prevents ashmem file descriptors from being mapped as executable within system\_server. Moreover, the use of execmem (in the first rule) prevents system\_server from mapping “new” executable memory regions within the process.

So… we could still write a large ROP chain to perform whichever set of commands we’d like within system\_server. Due to the breadth of system\_server, the ROP gadgets could conceivably even be turing-complete. However, this seems incredibly complex to do manually, and quite time consuming to automate.

Instead, we could look for a way to directly bypass the mitigation mentioned above. We’ll do so by looking for SELinux contexts which can be executed within system\_server. After a short search, we stumble upon the following SELinux rule:

\# system\_server should never execute anything from /data except for /[data](http://androidxref.com/7.0.0_r1/s?path=/data/)/[dalvik-cache](http://androidxref.com/7.0.0_r1/s?path=/data/dalvik-cache) files.

neverallow system\_server {

data\_file\_type

-dalvikcache\_data\_file #mapping with PROT\_EXEC

}:file no\_x\_file\_perms;

Okay, so files with the SELinux context dalvikcache\_data\_file may be freely mapped as executable. This makes sense as when Android applications are installed they go through an “optimization” process, resulting in new files which may be executed more quickly. As system\_server loads many of these optimized files, it needs to be able to map them in as executable to use them.

While system\_server may use these files, it cannot directly create them. In fact, the only process which is allowed to create files with these contexts is installd - the installer daemon.

The distinction, however, is purely semantic. This is due to the fact that system\_server can directly issue commands to installd using a special socket. One such command can be issued to cause installd to start such an optimization process (resulting in a file with the dalvikcache\_data\_file context) from any chosen file and to any chosen destination. Thus, all our ROP chain would need to do is to open the installd socket, issue this command to create our wanted executable chunk, and finally map that new file as executable.

We could even go one step further - since we are launching our attack from an Android application, we could simply embed the executable shellcode within the source code of our application (for example, within a static byte array). Once our application is installed, it will be optimized, resulting in a new file of type dalvikcache\_data\_file). As luck would have it, this optimization process does not garble static byte arrays, meaning our shellcode will now reside in this new executable file. Finally, all we need to do is to simply locate this optimised file on the disk and map it in as executable.


Lastly, when crafting our ROP stack we’ll need to know where to start writing the gadgets relative to the stack’s base address. That is, we need to know the accurate position in the stack at which the stack pointer will be placed when the SoundPoolThread enters the command loop.

Luckily, we can avoid the need to “guess” the top of the stack (and place a ROP-slide) by using additional trick; we can simply start up such a thread in our own process (by creating a sound pool object), and wait for it to enter the command loop. Once the thread settles, we can read the /proc/$pid/stat for that task and measure the value of the “SP” token against the base address of the stack for that thread.

### Bypassing the need to Bypass ASLR

Up to now we’ve been avoiding the question of ASLR. This has been no mistake, but rather a happy accident. In order to allow for fast application startup times, Android applications are forked from a single process, appropriately named zygote. This process preloads many commonly used shared libraries and resources, thus saving applications the need to do so on their own when they are launched.

Among the processes forked from zygote is our target for exploitation - system\_server.

This essentially means that the portion of our address space which are inherited from zygote are shared with system\_server, including a multitude of shared libraries which are available at our disposal.

As such, once we manage to hijack a running thread, we can create an entire valid ROP stack using gadget addresses located in our own address space (so long as we stick only to zygote-loaded shared libraries). Doing so allows us to ignore ASLR for the purpose of this exploit, as all the other stages of the exploit are address-independent anyway.


### Shaping the Address Space

Lastly, before we can put together a complete exploit, we still lack the ability to shape the remote address space. Specifically, we need to reach a state that will cause the targeted objects that we would like to delete to be placed in controlled memory regions, which could then be freed and subsequently reclaimed.

Recall that the behaviour of mmap dictates that for every allocation, the chosen memory address will always be the highest address in the range of mm->mmap\_base to TASK\_SIZE which contains a sufficiently large contiguous unmapped region.

This makes mmap an optimal allocator to use when attempting to shape the address space - most other allocators require special conditions in order to revert to contiguous allocations.

In our case, we already know that we would like to replace the memory region reserved for a thread’s stack. We’ll denote the size of this region by “thread\_size”.

First, we’ll send over a large amount of notification objects to the remote service, each of which containing a bitmap of size thread\_size. This will allow us to fill in any “holes” in the remote address space which may have been opened up during the lifetime of system\_server. After doing so, we are guaranteed that any subsequent allocation of size thread\_size will be contiguous and placed at the top of the current mmap-ed region.


Next, we allocate many consecutive bitmap objects of size thread\_size, each of which referenced by a single Notification object. After doing so, we intentionally remove a single notification from the consecutively allocated set. Then, we proceed bombard the system\_server process with many small binder transactions triggering a remote garbage collection to occur. This, in turn, frees up the space previously held by the bitmap object in the removed notification, creating a thread\_size sized hole, like so:


Now, we can re-load the audio effects, causing the SoundPoolThread to be spawned in system\_server. As this is a thread\_size-d allocation and all previous holes of that size have already been filled (by our bitmap objects), it will have to populate the vacant hole that we just created amidst our chunk of contiguous bitmaps.

Now, we can remove the notification directly in front of the SoundPoolThread’s stack and once again trigger a remote garbage collection. This will cause another hole to open up, bringing us to the following state:


Once we’ve strategically opened up a hole in front of the SoundPoolThread, we can send our crafted BitUnmap object. We’ll create it so that its metadata size (i.e., the size used in the mmap) will be equal to thread\_size. However, the size of the ashmem descriptor will actually be twice that size! This means the once our BitUnmap is freed in the remote process, it will unmap itself, along with the SoundPoolThread.


Finally, now that we’ve freed up the SoundPoolThread’s stack, we can send one more notification - this time of size 2\*thread\_size, which will fill in the last created hole, effectively replacing both the region held by the BitUnmap, and the region containing the SoundPoolThread’s stack.


## Putting it All Together

At long last, we have all the steps needed to create a complete working exploit. Here’s a short run-down of all the steps we discussed, which allow us to hijack a thread within the system\_server process using our own crafted ROP stack:

1. Build a ROP stack using gadgets in zygote-originating shared libraries
2. Unload all sound effects (closing the current SoundPoolThread, if present)
3. Allocate many bitmaps of size thread\_size to force consecutive allocations
4. Open up a hole in the middle of the consecutively allocated bitmaps
5. Reload the sound effects to create a new SoundPoolThread within the created hole
6. Open up a new hole directly in front of the previous hole
7. Send a BitUnmap object to fit in the newly created hole
8. Force a remote GC to cause the BitUnmap to free itself and the SoundPoolThread
9. Allocate a new bitmap to occupy the space previously held by the SoundPoolThread
10. Unload all sound effects - causing the condition variable to be signalled, thereby triggering the SoundPoolThread to start executing using our own crafted stack!

## Afterword

Although this blog post is quite lengthy, there are many smaller details that I neglected to mention here (in favour of some brevity). I’d encourage anyone who’s interested to dig into the full source code of the [exploit](https://bugs.chromium.org/p/project-zero/issues/detail?id=928#c4) to discover any such “missing” pieces.

Along with the source code for the exploit itself, I’m also releasing a project which can be used to easily create shellcode for use in the exploit itself. Specifically, this project contains a small assembly stub which fixed up the freed pthread\_internal\_t structure at the top of the stack and corrects the thread-local storage AARCH64 registers to point to their new location. After performing the needed fixups, it simply jumps to the shellcode’s main function.

In order to allow for easy shellcode creation in a high-level language (such as C) rather than hand-coding it all in assembly, the shellcode wrapper uses a custom linker script to prepend the small fixup stub to the shellcode, and compiles the shellcode itself as position independent.

## Timeline

- 07.09.2016 - Vulnerability reported
- 07.09.2016 - Initial response from Android security, assigned Android-ID
- 23.09.2016 - Exploit submitted to Android security
- 26.09.2016 - Android notify that the fix will be present in the next partner bulletin
- 27.09.2016 - CVE-2016-6707 assigned
- 01.11.2016 - Vulnerability fixed and released in the November bulletin
