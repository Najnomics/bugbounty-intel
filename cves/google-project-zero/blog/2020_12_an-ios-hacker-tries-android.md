# An iOS hacker tries Android - Project Zero

Source: https://projectzero.google/2020/12/an-ios-hacker-tries-android.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Written by Brandon Azad, when working at Project Zero

One of the amazing aspects of working at Project Zero is having the flexibility to direct my own research agenda. My prior work has almost exclusively focused on iOS exploitation, but back in August, I thought it could be interesting to try writing a kernel exploit for Android to see how it compares. I have two aims for this blog post: First, I will walk you through my full journey from bug description to kernel read/write/execute on the Samsung Galaxy S10, starting from the perspective of a pure-iOS security researcher. Second, I will try to emphasize some of the major security/exploitation differences between the two platforms that I have observed.

You can find the fully-commented exploit code attached in issue [2073](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/detail?id%3D2073%23c1&sa=D&ust=1608578955006000&usg=AOvVaw3UPfNIWRfIVLvQA7Uep8n5).

In November 2020, Samsung released a patch addressing the issue for devices that are eligible for receiving security updates. This issue was assigned CVE-2020-28343 and a Samsung-specific SVE-2020-18610.

# The initial vulnerability report

In early August, fellow Google Project Zero researcher [Ben Hawkes](https://www.google.com/url?q=https://twitter.com/benhawkes&sa=D&ust=1608578955006000&usg=AOvVaw1rF_F5FoSd-EX00q18bHpq) reported several [vulnerabilities](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/detail?id%3D2073&sa=D&ust=1608578955007000&usg=AOvVaw09mW9P0adU3guzPW2dQki8) in the Samsung [Neural Processing Unit](https://www.google.com/url?q=https://www.samsung.com/global/galaxy/what-is/npu/&sa=D&ust=1608578955007000&usg=AOvVaw0qcoEFkqwaU015eUgdfCyA) (NPU) kernel [driver](https://www.google.com/url?q=https://opensource.samsung.com/uploadSearch?searchValue%3Dsm-g973f&sa=D&ust=1608578955007000&usg=AOvVaw1qTHnoqa4kN9yny_bEheE4) due to a complete lack of input sanitization. At a high level, the NPU is a coprocessor dedicated to machine learning and neural network computations, especially for visual processing. The bugs Ben found were in Samsug's Android kernel driver for the NPU, responsible (among other things) for sending neural models from an Android app in userspace over to the NPU coprocessor.

The following few sections will look at the vulnerabilities. These bugs aren't actually that interesting: they are quite ordinary out-of-bounds writes due to unsanitized input, and could almost be treated as black-box primitives for the purposes of writing an exploit (which was my ultimate goal). The primitives are quite strong and, to my knowledge, no novel techniques are required to build a practical exploit out of them in practice. However, since I was coming from the perspective of never having written a Linux kernel exploit, understanding these bugs and their constraints in detail was crucial for me to begin to visualize how they might be used to gain kernel read/write.

## 🤖 📱 🧠 👓 🐛🐛

The vulnerabilities are reached by opening a handle to the device /dev/vertex10, which Ben had determined is accessible to a normal Android app. Calling open() on this device causes the kernel to allocate and initialize a new npu\_session object that gets associated with the returned file descriptor. The process can then invoke ioctl() on the file descriptor to interact with the session. For example, consider the following code:

| int ncp\_fd = open("/dev/vertex10", O\_RDONLY); struct vs4l\_graph vs4l\_graph = /\* ioctl data \*/; ioctl(ncp\_fd, VS4L\_VERTEXIOC\_S\_GRAPH, &vs4l\_graph); | 

The preceding syscalls will result in the kernel calling the function npu\_vertex\_s\_graph(), which calls npu\_session\_s\_graph() on the associated npu\_session (see drivers/vision/npu/npu-vertex.c). npu\_session\_s\_graph() then calls \_\_config\_session\_info() to parse the input data to this ioctl (see npu-session.c):

| int \_\_config\_session\_info(struct npu\_session \*session) { ... ret = \_\_pilot\_parsing\_ncp(session, &temp\_IFM\_cnt, &temp\_OFM\_cnt, &temp\_IMB\_cnt, &WGT\_cnt); temp\_IFM\_av = kcalloc(temp\_IFM\_cnt, sizeof(struct temp\_av), GFP\_KERNEL); temp\_OFM\_av = kcalloc(temp\_OFM\_cnt, sizeof(struct temp\_av), GFP\_KERNEL); temp\_IMB\_av = kcalloc(temp\_IMB\_cnt, sizeof(struct temp\_av), GFP\_KERNEL); ... ret = \_\_second\_parsing\_ncp(session, &temp\_IFM\_av, &temp\_OFM\_av, &temp\_IMB\_av, &WGT\_av); ... } | 

As can be seen above, \_\_config\_session\_info() calls two other functions to perform the actual parsing of the input: \_\_pilot\_parsing\_ncp() and \_\_second\_parsing\_ncp(). As their names suggest, \_\_pilot\_parsing\_ncp() performs a preliminary "pilot" parsing of the input data in order to compute the sizes of a few arrays that will need to be allocated for the full parsing; meanwhile, \_\_second\_parsing\_ncp() performs the full parsing, populating the arrays that were just allocated.

Let's take a quick look at \_\_pilot\_parsing\_ncp():

| int \_\_pilot\_parsing\_ncp(struct npu\_session \*session, u32 \*IFM\_cnt, u32 \*OFM\_cnt, u32 \*IMB\_cnt, u32 \*WGT\_cnt) { ... ncp\_vaddr = (char \*)session->ncp\_mem\_buf->vaddr; ncp = (struct ncp\_header \*)ncp\_vaddr; memory\_vector\_offset = ncp->memory\_vector\_offset; memory\_vector\_cnt = ncp->memory\_vector\_cnt; mv = (struct memory\_vector \*)(ncp\_vaddr + memory\_vector\_offset); for (i = 0; i \< memory\_vector\_cnt; i++) { u32 memory\_type = (mv + i)->type; switch (memory\_type) { case MEMORY\_TYPE\_IN\_FMAP: { (\*IFM\_cnt)++; break; } case MEMORY\_TYPE\_OT\_FMAP: { (\*OFM\_cnt)++; break; } ... } } return ret; } | 

There are a few things to note here.

First, the input data is being parsed from a buffer pointed to by the field session->ncp\_mem\_buf->vaddr. This turns out to be an [ION buffer](https://www.google.com/url?q=https://lwn.net/Articles/480055/&sa=D&ust=1608578955027000&usg=AOvVaw25H9zLJhDyXO6_36JfQEhp), which is a type of memory buffer shareable between userspace, the kernel, and coprocessors. The ION interface was introduced by Google into the Android kernel to facilitate allocating device-accessible memory and sharing that memory with various hardware components, all without needing to copy the data between buffers. In this case, the userspace app will initialize the model directly inside an ION buffer, and then the model will be mapped directly into the kernel for pre-processing before the ION buffer's device address is sent to the NPU to perform the actual work.

The important takeaway from this first observation is that the session->ncp\_mem\_buf->vaddr field points to an ION buffer that is currently mapped into both userspace and the kernel: that is, it's shared memory.

The second thing to note in the function \_\_pilot\_parsing\_ncp() is that the only thing it does is count the number of times each type of element appears in the memory\_vector array in the shared ION buffer. Each memory\_vector element has an associated type, and this function simply tallies up the number of times it sees each type, and nothing else. There isn't even a failure case for this function.

This is interesting for a few reasons. For one, there's no input sanitization to ensure that memory\_vector\_cnt (which is read directly from the shared memory buffer and thus is attacker-controlled) is a sane value. It could be 0xffffffff, leading the for loop to process memory\_vector elements off the end of the ION buffer. Probably a kernel crash at worst, but it's certainly an indication of unfuzzed code.

More importantly, since only the count of each type is stored, it seems likely that this code is setting itself up for a double-read, time-of-check-to-time-of-use (TOCTOU) issue when it later processes the memory\_vectors a second time. Each of the returned counts is used to allocate an array in kernel memory (see \_\_config\_session\_info()). But because the memory\_vector\_cnt and types reside in shared memory, they could be changed by code running in userspace between \_\_pilot\_parsing\_ncp() and \_\_second\_parsing\_ncp(), meaning that the second function is passed incorrectly sized arrays for the memory\_vector data it eventually sees in the shared buffer.

Of course, to determine whether this is actually a bug, we have to look at the implementation of \_\_second\_parsing\_ncp():

| int \_\_second\_parsing\_ncp( struct npu\_session \*session, struct temp\_av \*\*temp\_IFM\_av, struct temp\_av \*\*temp\_OFM\_av, struct temp\_av \*\*temp\_IMB\_av, struct addr\_info \*\*WGT\_av) { ncp\_vaddr = (char \*)session->ncp\_mem\_buf->vaddr; ncp\_daddr = session->ncp\_mem\_buf->daddr; ncp = (struct ncp\_header \*)ncp\_vaddr; address\_vector\_offset = ncp->address\_vector\_offset; address\_vector\_cnt = ncp->address\_vector\_cnt; ... memory\_vector\_offset = ncp->memory\_vector\_offset; memory\_vector\_cnt = ncp->memory\_vector\_cnt; mv = (struct memory\_vector \*)(ncp\_vaddr + memory\_vector\_offset); av = (struct address\_vector \*)(ncp\_vaddr + address\_vector\_offset); ... for (i = 0; i \< memory\_vector\_cnt; i++) { u32 memory\_type = (mv + i)->type; u32 address\_vector\_index; u32 weight\_offset; switch (memory\_type) { case MEMORY\_TYPE\_IN\_FMAP: { address\_vector\_index = (mv + i)->address\_vector\_index; if (!EVER\_FIND\_FM(IFM\_cnt, \*temp\_IFM\_av, address\_vector\_index)) { (\*temp\_IFM\_av + (\*IFM\_cnt))->index = address\_vector\_index; (\*temp\_IFM\_av + (\*IFM\_cnt))->size = (av + address\_vector\_index)->size; (\*temp\_IFM\_av + (\*IFM\_cnt))->pixel\_format = (mv + i)->pixel\_format; (\*temp\_IFM\_av + (\*IFM\_cnt))->width = (mv + i)->width; (\*temp\_IFM\_av + (\*IFM\_cnt))->height = (mv + i)->height; (\*temp\_IFM\_av + (\*IFM\_cnt))->channels = (mv + i)->channels; (mv + i)->stride = 0; (\*temp\_IFM\_av + (\*IFM\_cnt))->stride = (mv + i)->stride; ... (\*IFM\_cnt)++; } break; } ... case MEMORY\_TYPE\_WEIGHT: { // update address vector, m\_addr with ncp\_alloc\_daddr + offset address\_vector\_index = (mv + i)->address\_vector\_index; weight\_offset = (av + address\_vector\_index)->m\_addr; if (weight\_offset > (u32)session->ncp\_mem\_buf->size) { ret = -EINVAL; npu\_uerr("weight\_offset is invalid, offset(0x%x), ncp\_daddr(0x%x)\n", session, (u32)weight\_offset, (u32)session->ncp\_mem\_buf->size); goto p\_err; } (av + address\_vector\_index)->m\_addr = weight\_offset + ncp\_daddr; ... (\*WGT\_cnt)++; break; } ... } } ... } | 

Once again, there are several things to note here.

First off, it does indeed turn out that memory\_vector\_cnt is read a second time from the shared ION buffer, and there are no sanity checks to ensure that the arrays temp\_IFM\_av, temp\_OFM\_av, and temp\_IMB\_av are not filled beyond the counts for which they were each allocated. So this is indeed a linear heap overflow bug.

But secondly, when processing a memory\_vector element of type MEMORY\_TYPE\_WEIGHT, it appears that there's another issue as well: A controlled 32-bit value address\_vector\_index is read from the memory\_vector entry and used as an index into an address\_vector array without any bounds checks. And not only is the out-of-bounds address\_vector's m\_addr field read, it's also written a few lines later after adding in the ION buffer's device address! So this is an out-of-bounds addition at a controlled offset.

These are the two most serious issues described in Ben's [report](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/detail?id%3D2073&sa=D&ust=1608578955052000&usg=AOvVaw3ZwfboJCZZsR9puUJNnD-u) to Samsung. We'll look at each in more detail in the following two sections in order to understand their constraints.

## The heap overflow

How might the heap overflow be triggered?

First, \_\_config\_session\_info() will call \_\_pilot\_parsing\_ncp() to count the number of elements of each type in the memory\_vector array in the shared ION buffer. Imagine that initially the value of ncp->memory\_vector\_cnt is 1, and the single memory\_vector has type MEMORY\_TYPE\_IN\_FMAP. Then \_\_pilot\_parsing\_ncp() will return with IFM\_cnt set to 1.

Next, \_\_config\_session\_info() will allocate the temp\_IFM\_av with space for a single temp\_av element.

Concurrently, a thread in userspace will race to change the value of ncp->memory\_vector\_cnt in the shared ION buffer from 1 to 100. The memory\_vector now appears to have 100 elements, and userspace will ensure that the extra elements all have type MEMORY\_TYPE\_IN\_FMAP as well.

Back in the kernel: After allocating the arrays, \_\_config\_session\_info() will call \_\_second\_parsing\_ncp() to perform the second stage of parsing. \_\_second\_parsing\_ncp() will read memory\_vector\_cnt again, this time getting the value 100. Thus, in the for loop, it will try to process 100 elements from the memory\_vector array, and each will be of type MEMORY\_TYPE\_IN\_FMAP. Each iteration will populate another temp\_av element in the temp\_IFM\_av array, and elements after the first will be written off the end of the array.

Furthermore, the out-of-bounds temp\_av element's fields are written with contents read from the ION buffer, which means that the contents of the out-of-bounds write can be fully controlled (except for padding between fields).

This seems like an excellent primitive: we're performing an out-of-bounds write off the end of a kernel allocation of controlled size, and we can control both the size of the overflow and the contents of the data we write. This level of control means that it should theoretically be possible to place the temp\_IFM\_av allocation next to many different types of objects and control the amount of the victim object we overflow. Having such flexibility means that we can choose from a very wide selection of victim objects when deciding the easiest and most reliable exploit strategy.

The one thing to be aware of is that a simple implementation would probably win the race to increase memory\_vector\_cnt about 25% of the time. The reason for this is that it's probably tricky to get the timing of when to flip from 1 to 100 exactly right, so the simplest strategy is simply to have a user thread alternate between the two values continuously. If each of the reads in \_\_pilot\_parsing\_ncp() and \_\_second\_parsing\_ncp() reads either 1 or 100 randomly, then there's a 1 in 4 chance that the first read is 1 and the second is 100. The good thing is that nothing too bad happens if we lose the race: there's possibly a memory leak, but the kernel doesn't crash. Thus, we can just try this over and over until we win.

## The out-of-bounds addition

Now that we've seen the heap overflow, let's look at the out-of-bounds addition primitive. Unlike the prior primitive, this one is a straightforward, deterministic out-of-bounds addition.

Once again, we'll initialize our ION buffer to have a single memory\_vector element, but this time its type will be MEMORY\_TYPE\_WEIGHT. Nothing interesting happens in \_\_pilot\_parsing\_ncp(), so we'll jump ahead to \_\_second\_parsing\_ncp().

In \_\_second\_parsing\_ncp(), address\_vector\_offset is read directly from the ION buffer without input validation. This is added to the ION buffer address to compute the address of an array of address\_vector structs; since the offset was unchecked, this supposed address\_vector array could lie entirely in out-of-bounds memory. And importantly, there are no alignment checks, so the address\_vector array could start at any odd unaligned address we want.

| address\_vector\_offset = ncp->address\_vector\_offset; ... av = (struct address\_vector \*)(ncp\_vaddr + address\_vector\_offset); | 

We next enter the for loop to process the single memory\_vector entry, and jump to the case for MEMORY\_TYPE\_WEIGHT. This code reads the address\_vector\_index field of the memory\_vector, which is again completely controlled and unvalidated. The (potentially out-of-bounds) address\_vector element at the specified index is then accessed.

| // update address vector, m\_addr with ncp\_alloc\_daddr + offset address\_vector\_index = (mv + i)->address\_vector\_index; weight\_offset = (av + address\_vector\_index)->m\_addr; | 

Reading the m\_addr field (at offset 0x4 in address\_vector) will thus possibly perform an out-of-bounds read.

But there's a check we need to pass before we can hit the out-of-bounds write:

| if (weight\_offset > (u32)session->ncp\_mem\_buf->size) { ret = -EINVAL; npu\_uerr("weight\_offset is invalid, offset(0x%x), ncp\_daddr(0x%x)\n", session, (u32)weight\_offset, (u32)session->ncp\_mem\_buf->size); goto p\_err; } | 

Basically, what this does is compare the original value of the out-of-bounds read to the size of the ION buffer, and if the original value is greater than the ION buffer size, then \_\_second\_parsing\_ncp() aborts without performing the write.

But, assuming that the original value is less than the ION buffer size, it gets updated by adding in the device address (daddr) of the ION buffer:

| (av + address\_vector\_index)->m\_addr = weight\_offset + ncp\_daddr; | 

The device address is (presumably) the address at which a device could access the buffer; this could be a physical address, or if the system has an [IOMMU](https://www.google.com/url?q=https://en.wikipedia.org/wiki/Input%25E2%2580%2593output_memory_management_unit&sa=D&ust=1608578955066000&usg=AOvVaw2VvVpsNucmrr9KywnAvow2) in front of the hardware device performing the access, it would be an IOMMU-translated address. Essentially, this code expects that the m\_addr field in the address\_vector will initially be an offset from the start of the ION buffer, and it updates it into an absolute (device) address by adding the ION buffer's daddr.

So, if the original value at the out-of-bounds addition location is quite small, and in particular smaller than the ION buffer size, then this primitive will allow us to add in the ION buffer's daddr, making the value rather large instead.

# "Hey Siri, how do I exploit Android?"

Everything described up to here comes more or less directly from Ben's initial report to Samsung. So: what now?

Even after reading Ben's initial report and looking at the NPU driver's source code to understand the bugs more fully, I felt rather lost as to how to proceed. As the title and intro to this post suggest, Android is not my area.

On the other hand, I have written a few [iOS](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/detail?id%3D1731%23c10&sa=D&ust=1608578955067000&usg=AOvVaw1wJHXUsIIMf-oP3QbEuCok) [kernel](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/detail?id%3D2035%23c4&sa=D&ust=1608578955067000&usg=AOvVaw3xhDiq6oGnKYzCOmuvnI2z) [exploits](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/detail?id%3D1986%23c7&sa=D&ust=1608578955067000&usg=AOvVaw2ylmRP3FBMafCqM5QvURpz) for memory corruption bugs before. Based on that experience, I suspected that both the heap overflow and the out-of-bounds addition could be exploited using straightforward applications of [existing techniques](/2020/06/a-survey-of-recent-ios-kernel-exploits.html), had the bugs existed on iOS. So I embarked on a thought experiment: what would the full exploit flows for each of these primitives be if the bugs existed on iOS instead of Android? My hope was that I might be able to draw parallels between the two, such that thinking about the exploit on iOS would inform how these bugs could be exploited on Android.

## Thought experiment: an iOS heap overflow

So, imagine that an equivalent to the heap overflow bug existed on iOS; that is, imagine there were a race with a 25% win rate that allowed us to perform a fully controlled linear heap buffer overflow out of a controlled-size allocation. How could we turn this into arbitrary kernel read/write?

On iOS, the de-facto standard for a final kernel read/write capability has been the use of an object called a kernel task port. A task port is a handle that gives us control over the virtual memory of a task, and a kernel task port is a task port for the kernel itself. Thus, if you can construct a kernel task port, you can use standard APIs like mach\_vm\_read() and mach\_vm\_write() to read and write kernel memory from userspace.

Comparing this heap overflow to the vulnerabilities listed in the [survey](/2020/06/a-survey-of-recent-ios-kernel-exploits.html), the initial primitive is most similar to that granted by CVE-2017-2370, which was exploited by [extra\_recipe](/2017/04/exception-oriented-exploitation-on-ios.html) and [Yalu102](https://www.google.com/url?q=https://github.com/kpwn/yalu102&sa=D&ust=1608578955069000&usg=AOvVaw1aV6k45s0OgHluj4kgY0pC). Thus, the exploit flow would likely be quite similar to those existing iOS exploits. And to make our thought experiment even easier, we can put aside any concern about reliability and just imagine the simplest exploit flow that could work generically.

The most straightforward way to get a handle to a kernel task port using this primitive would likely be to overflow into an out-of-line Mach ports array and insert a pointer to a fake kernel task port, such that receiving the overflowed port array back in userspace grants us a handle to our fake port. This is essentially the strategy used by Yalu102, except that that exploit relies on the absence of PAN (i.e., it relies on being able to dereference userspace pointers from kernel mode). The same strategy should work on systems with PAN, it would just require a few extra steps.

Unfortunately, the first time we trigger the vulnerability to give ourselves a handle to a fake task port, we won't have all the information needed to immediately construct a kernel task port: we'd need to leak the addresses of a few important kernel objects, such as the kernel\_map, first. Consequently, we would need to start first by giving ourselves a "vanilla" fake task port and then use that to read arbitrary kernel memory via the traditional pid\_for\_task() technique. Once we can read kernel memory, we would locate the relevant kernel objects to build the final kernel task port.

Now, since we'll need to perform multiple arbitrary reads using pid\_for\_task(), we need to be able to update the kernel address we want to read from. This can be a challenge because the pointer specifying the target read address lives in kernel memory. Fortunately, there already exist a few standard techniques for updating this pointer to read from new kernel addresses, such as reallocating the buffer holding the target read pointer (see the [Chaos](<https://www.google.com/url?q=https://blogs.360.cn/post/IPC%2520Voucher%2520UaF%2520Remote%2520Jailbreak%2520Stage%25202%2520(EN).html&sa=D&ust=1608578955070000&usg=AOvVaw3eqSiB2LY1OfGk904vdnB_>) exploit), overlapping Mach ports in special ways that allow updating the target read address directly (see the [v0rtex](https://www.google.com/url?q=https://siguza.github.io/v0rtex/&sa=D&ust=1608578955070000&usg=AOvVaw2uMt2TluaPinFRPf_NQAyc) exploit), or placing the fake kernel objects in user/kernel shared memory (see the [oob\_timestamp](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/detail?id%3D2035%23c4&sa=D&ust=1608578955070000&usg=AOvVaw14qDghwQl7TV6gFWPvrqML) exploit).

Finally, there will also be some complications from working around Apple's zone\_require mitigation, which aims to block exactly these types of fake Mach port shenanigans. However, at least through iOS 13.3, it's possible to get around zone\_require by operating with large allocations that live outside the zone\_map (see the oob\_timestamp exploit).

So, in summary, a very simplistic exploit flow for the heap overflow might look something like this:

1. Spray large amounts of kernel memory with fake task ports and fake tasks, such that you can be reasonably sure that one fake object of each type has been sprayed to a specific hardcoded address. Use the oob\_timestamp trick to bypass zone\_require and place these fake objects in shared memory.
2. Spray out-of-line Mach ports allocations, and poke holes between the allocations.
3. Trigger the out-of-bounds write out of an allocation of the same size as the out-of-line Mach ports allocations, overflowing into the subsequent array of Mach ports and inserting the hardcoded pointer to the fake ports.
4. Receive the out-of-line Mach port handles in userspace and check if there's a new task port handle; if not, go back to step 2.
5. This handle is a fake task port that can be used to read kernel memory using pid\_for\_task(). Use this capability to find relevant kernel objects and update the fake task into a fake kernel task object.

## Thought experiment: an iOS out-of-bounds addition

What about the out-of-bounds addition?

None of the bugs in the survey of iOS kernel exploits seem like a good comparison point: the most similar category would be linear heap buffer overflows, but these are much more limiting due to spatial locality. Nonetheless, I eventually settled on oob\_timestamp as the best reference.

The vulnerability used by oob\_timestamp is CVE-2020-3837, a linear heap out-of-bounds write of up to 8 bytes of timestamp data. However, this isn't the typical heap buffer overflow. Most heap overflows occur in small to medium sized allocations of up to 2 pages (0x8000 bytes); these allocations occur in a submap of the kernel virtual address space called the zone\_map. Meanwhile, the out-of-bounds write in oob\_timestamp occurs off the end of a pageable region of shared memory outside the zone\_map, in the general kernel\_map used for large, multi-page allocations or allocations with special properties (like pageable and shared memory).

The basic flow of oob\_timestamp is as follows:

1. Groom the kernel\_map to allocate the pageable shared memory region, an ipc\_kmsg, and an out-of-line Mach ports array contiguously. These are followed by a large number of filler allocations.
2. Trigger the overflow to overwrite the first few bytes of the ipc\_kmsg, increasing the size field.
3. Free the ipc\_kmsg, causing the subsequent out-of-line Mach ports array to also be freed.
4. Reallocate the out-of-line Mach ports array with controlled data, effectively inserting fake Mach port pointers into the array. The pointer will be a pointer to a fake task port in the pageable shared memory region.
5. Receive the out-of-line Mach ports in userspace, gaining a handle to the fake port.
6. Overwrite the fake port in shared memory to make a fake task port and then read kernel memory using pid\_for\_task(). Find relevant kernel objects and update the fake task into a fake kernel task.

My thought was that you could basically use the out-of-bounds addition primitive as a drop-in replacement for the out-of-bounds timestamp write primitive in oob\_timestamp. This seemed sensible because the initial primitive in oob\_timestamp is only used to increase the size of an ipc\_kmsg so that extra memory gets freed. Since all I need to do is bump an ipc\_kmsg's size field, I felt that an out-of-bounds addition primitive should surely be suitable for this.

As it turns out, the constraints of the out-of-bounds addition are actually much tighter than I had imagined: the ipc\_kmsg's size and the ION buffer's device address would need to be very carefully chosen to meet all the requirements. In spite of this oversight, oob\_timestamp still proved a useful reference point for another reason: where the ION buffers get mapped in kernel memory.

Like iOS, Android also has multiple areas of virtual memory in which allocations can be made. kmalloc() is the standard allocation function used for most allocations. It's somewhat analogous to allocating using kalloc() on iOS: allocations can be less than a page in size and are managed via a dedicated allocation pool that's a bit like the zone\_map. However, there's also a vmalloc() function for allocating "virtually contiguous memory". Unlike kmalloc(), vmalloc() allocates at page granularity and allocations occur in a separate region of kernel virtual memory somewhat analogous to the kernel\_map on iOS.

The reason this matters is that the ION buffer on Android is mapped into the Linux kernel's vmalloc region. Thus, the fact that the out-of-bounds addition occurs off the end of a shared ION buffer mapped in the vmalloc area closely parallels how the oob\_timestamp overflow occurs off the end of a pageable shared memory region in the kernel\_map.

# Choosing a path

At this point I still faced many unknowns: What allocation and heap shaping primitives were available on Android? What types of objects would be useful to corrupt? What would be Android's equivalent of the kernel task port, the final read/write capability? I had no idea.

One thing I did have was a hint at a good starting point: Both Ben and fellow Project Zero researcher [Jann Horn](https://www.google.com/url?q=https://twitter.com/tehjh&sa=D&ust=1608578955075000&usg=AOvVaw3Pv3Mj5IScA-OPtG0dCOwO) had pointed out that along with the ION buffers, kernel thread stacks were also allocated in the vmalloc area, which meant that kernel stacks might be a good target for the out-of-bounds addition bug.


If the ION buffer is mapped directly before a kernel stack for a userspace thread, then the out-of-bounds addition primitive could be used to manipulate the stack.

Imagine that we could get a kernel stack for a thread in our process allocated at a fixed offset after the ION buffer. The out-of-bounds addition primitive would let us manipulate values on the thread's stack during a syscall by adding in the ION buffer's daddr, assuming that the initial values were sufficiently small. For example, we might make a blocking syscall which saves a certain size parameter in a variable, and once that syscall blocks and spills the size variable to the stack, we can use the out-of-bounds addition to make it very large; unblocking the syscall would then cause the original code to resume use the corrupted size value, perhaps passing it to a function like memcpy() to cause further memory corruption.

Using the out-of-bounds addition primitive to target values on a thread's kernel stack was appealing for one very important reason: in theory, this technique could dramatically reduce the amount of Linux-specific knowledge I'd need to develop a full exploit.

Most typical memory corruption exploits require finding specific objects that are interesting targets for corruption. For example, there are very few objects that could replace the ipc\_kmsg in the oob\_timestamp exploit, because the exploit relies on corrupting a size field stored at the very start of the struct; not many other objects have a size as their first field. So ipc\_kmsg fills a very important niche in the arsenal of interesting objects to target with memory corruption, just as Mach ports fill a niche in useful objects to get a fake handle for.

Undoubtedly, there's a similar arsenal of useful objects to target for Android kernel exploitation. But by limiting ourselves to corrupting values on the kernel stack, we transform the set of all useful target "objects" into the set of useful stack frames to manipulate. This is a much easier set of target objects to work with than the set of all structs that could be allocated after the ION buffer because it doesn't require much Linux-specific knowledge to reason about semantics: We only need to identify relevant syscalls and look at the kernel binary in a disassembler to get a handle on what "objects" we have available to us.

Selecting the out-of-bounds addition primitive and choosing to target kernel thread stacks effectively solves the problem of finding useful kernel objects to corrupt by turning what would be a codebase-wide search into a simple enumeration of interesting stack frames in a disassembler without needing to learn much in the way of Linux internals.

Nevertheless, we are still left with two pressing questions: What allocation and heap shaping primitives do we have on Android? And what will be our final read/write capability to parallel the kernel task port?

# Heap shaping

I started with the heap shaping primitive since it seemed the more tangible problem.

As previously mentioned, the vmalloc area is a region of the kernel's virtual address space in which allocations and mappings of page-level granularity can be made, comparable to the kernel\_map on iOS. And just like how iOS provides a means of inspecting virtual memory regions in the kernel\_map via vmmap, Linux provides a way of inspecting the allocations in the vmalloc area through /proc/vmallocinfo.

The /proc/vmallocinfo interface provides a simple textual description of each allocated virtual memory region inside the vmalloc area, including the start and end addresses, the size of the region in bytes, and some information about the allocation, such as the allocation site:

0xffffff8013bd0000-0xffffff8013bd5000 20480 \_do\_fork+0x88/0x398 pages=4 vmalloc

0xffffff8013bd8000-0xffffff8013bdd000 20480 unpurged vm\_area

0xffffff8013be0000-0xffffff8013be5000 20480 unpurged vm\_area

0xffffff8013be8000-0xffffff8013bed000 20480 \_do\_fork+0x88/0x398 pages=4 vmalloc

0xffffff8013bed000-0xffffff8013cec000 1044480 binder\_alloc\_mmap\_handler+0xa4/0x1e0 vmalloc

0xffffff8013cec000-0xffffff8013eed000 2101248 ion\_heap\_map\_kernel+0x110/0x16c vmap

0xffffff8013eed000-0xffffff8013fee000 1052672 ion\_heap\_map\_kernel+0x110/0x16c vmap

0xffffff8013ff0000-0xffffff8013ff5000 20480 \_do\_fork+0x88/0x398 pages=4 vmalloc

0xffffff8013ff8000-0xffffff8013ffd000 20480 unpurged vm\_area

0xffffff8014000000-0xffffff80140ff000 1044480 binder\_alloc\_mmap\_handler+0xa4/0x1e0 vmalloc

0xffffff8014108000-0xffffff801410d000 20480 \_do\_fork+0x88/0x398 pages=4 vmalloc

This gives us a way to visualize the vmalloc area and ensure that our allocations are grooming the heap as we want them to.

Our heap shaping needs to place a kernel thread stack at a fixed offset after the ION buffer mapping. By inspecting the kernel source code and the vmallocinfo output, I determined that kernel stacks consisted of 4 pages (0x4000 bytes) of data but also included a guard page after the allocation that was included in the size. Thus, my initial heap shaping idea was:

1. Allocate large allocation of say 0x80000 bytes.
2. Spray kernel stacks by creating new threads to fill up all 0x5000-byte holes in the vmalloc area before our large 0x80000-byte allocation.
3. Free the large allocation. This should make an 0x80000-byte hole with no 0x5000-byte holes before it.
4. Spray several more kernel stacks by creating new threads; these stacks should fall into the beginning of the hole, and also fill any earlier holes created by exiting threads from other processes.
5. Map the ION buffer into the kernel by invoking the VS4L\_VERTEXIOC\_S\_GRAPH ioctl, but without triggering the out-of-bounds addition. The ION buffer mapping should also fall into the hole.
6. Spray more kernel stacks by creating new threads. These should fall into the hole as well, and one of them should land directly after the ION buffer.

Unfortunately, when I proposed this strategy to my teammates, Jann Horn pointed out a problem. In XNU, when you free a kernel\_map allocation, that virtual memory region becomes immediately available for reuse. However, in Linux, freeing a vmalloc allocation usually just marks the allocation as freed without allowing you to immediately reclaim the virtual memory range; instead, the range becomes an "unpurged vm\_area", and these areas are only properly freed and reclaimed once the amount of unpurged vm\_area memory crosses a certain threshold. The reason Linux batches reclaiming freed virtual memory regions like this is to minimize the number of expensive global TLB flushes.

Consequently, this approach doesn't work exactly as we'd like: it's hard to know precisely when the unpurged vm\_area allocations will be purged, so we can't be sure that we're reclaiming the hole to arrange our allocations. Nevertheless, it is possible to force a vm\_area purge if you allocate and free enough memory. We just can't rely on the exact timing.

Even though the straightforward approach wouldn't work, Ben and Jann did help me identify a useful allocation site for spraying controlled-size allocations using vmalloc(). The function binder\_alloc\_mmap\_handler(), which implements mmap() called on /dev/binder file descriptors, contains a call to get\_vm\_area() on the specific kernel version I was exploiting. Thus, the following sequence of operations would allow me to perform a vmalloc() of any size up to 4 MiB:

| int binder\_fd = open("/dev/binder", O\_RDONLY); void \*binder\_map = mmap(NULL, vmalloc\_size, PROT\_READ, MAP\_PRIVATE, binder\_fd, 0); | 

The main annoyance with this approach is that only a single allocation can be made using each binder fd; to make multiple allocations, you need to open multiple fds.

On my rooted Samsung Galaxy S10 test device, it appeared that the vmalloc area contained a lot of unreserved space at the end, in particular between 0xffffff8050000000 and 0xffffff80f0000000:

0xffffff804a400000-0xffffff804a800000 4194304 vm\_map\_ram

0xffffff804a800000-0xffffff804ac00000 4194304 vm\_map\_ram

0xffffff804ac00000-0xffffff804b000000 4194304 vm\_map\_ram

0xffffff80f9e00000-0xffffff80faa00000 12582912 phys=0x00000009ef800000

0xffffff80fafe0000-0xffffff80fede1000 65015808

0xffffff80fefe0000-0xffffff80ff5e1000 6295552

0xffffff8100d00000-0xffffff8100d3a000 237568 phys=0x0000000095000000

0xffffffbebfdc8000-0xffffffbebfe80000 753664 pcpu\_get\_vm\_areas+0x0/0x744 vmalloc

0xffffffbebfe80000-0xffffffbebff38000 753664 pcpu\_get\_vm\_areas+0x0/0x744 vmalloc

0xffffffbebff38000-0xffffffbebfff0000 753664 pcpu\_get\_vm\_areas+0x0/0x744 vmalloc

Thus, I came up with an alternative strategy to place a kernel thread stack after the ION buffer mapping:

1. Open a large number of /dev/binder fds.
2. Spray a large amount of vmalloc memory using the binder fds and then close them, forcing a vm\_area purge. We can't be sure of exactly when this purge occurs, so some unpurged vm\_area regions will still be left. But forcing a purge will expose any holes at the start of the vmalloc area so that we can fill them in the next step. This prevents these holes from opening up at a later stage, messing up the groom.
3. Now spray many allocations to the binder fds in decreasing sizes: 4 MiB, 2 MiB, 1 MiB, etc., all the way down to 0x4000 bytes. The idea is to efficiently fill holes in the vmalloc heap so that we eventually start allocating from clean virtual address space, like the 0xffffff8050000000 region identified earlier. The first binder vmallocs will fill the large holes, then later allocs will fill smaller and smaller holes, until eventually all 0x5000-byte holes are filled. (It is 0x5000 not 0x4000 because the allocations have a guard page at the end.)
4. Now create some user threads. The threads' kernel stacks will allocate their 0x4000-byte stacks (which are 0x5000-byte reservations with the guard page) from the fresh virtual memory area at the end of the vmalloc region.
5. Now trigger the vulnerable ioctl to map the ION buffer into the vmalloc region. If the ION buffer is chosen to have size 0x4000 bytes, it will also be placed in the fresh virtual memory area at the end of the vmalloc region.
6. Finally, create some more user threads. Once again, their kernel stacks will be allocated from the fresh VA space, and they will thus be placed directly after the ION buffer, achieving our goal.

This technique actually seemed to work reasonably well. By dumping /proc/vmallocinfo at each step, it's possible to check that the kernel heap is being laid out as we hope. And indeed, it did appear that we were getting the ION buffer allocated directly before kernel thread stacks:

0xffffff8083ba0000-0xffffff8083ba5000 20480 \_do\_fork+0x88/0x398 pages=4 vmalloc

0xffffff8083ba8000-0xffffff8083bad000 20480 \_do\_fork+0x88/0x398 pages=4 vmalloc

0xffffff8083bad000-0xffffff8083bb2000 20480 ion\_heap\_map\_kernel+0x110/0x16c vmap

0xffffff8083bb8000-0xffffff8083bbd000 20480 \_do\_fork+0x88/0x398 pages=4 vmalloc

0xffffff8083bc0000-0xffffff8083bc5000 20480 \_do\_fork+0x88/0x398 pages=4 vmalloc

0xffffff8083bc8000-0xffffff8083bcd000 20480 \_do\_fork+0x88/0x398 pages=4 vmalloc

0xffffff8083bd0000-0xffffff8083bd5000 20480 \_do\_fork+0x88/0x398 pages=4 vmalloc

0xffffff80f9e00000-0xffffff80faa00000 12582912 phys=0x00000009ef800000

0xffffff80fafe0000-0xffffff80fede1000 65015808

0xffffff80fefe0000-0xffffff80ff5e1000 6295552

# Stack manipulation

At this point we can groom the kernel heap to place the kernel stack for one of our process's threads directly after the ION buffer, giving us the ability to manipulate the thread's stack while it is blocked in a syscall. The next question is what we should manipulate?

In order to answer this, we really need to understand the constraints of our bug. As discussed above, our primitive is the ability to perform an out-of-bounds addition on a 32-bit unsigned value, adding in the ION buffer's device address (daddr), so long as the original value being modified is less than the ION buffer's size.

The code in npu-session.c performs a copious amount of logging, so it's possible to check the address of the ION allocation from a root shell using the following command:

cat /proc/kmsg | grep ncp\_ion\_map

In my early tests, the ION buffer's daddr was usually between 0x80500000 and 0x80700000, and always matched the masks 0x80xx0000. If we use a size of 0x4000 for our ION buffer, then that means our primitive will transform a small positive value on the stack into a very large positive (unsigned) or negative (signed) value; for example, we might transform 0x1000 into 0x80611000.

How would we use this to gain code execution? Jann suggested a very interesting trick that could block calls to the functions copy\_from\_user() and copy\_to\_user() for arbitrary amounts of time, which could greatly expand the set of block points available during system calls.

copy\_from\_user() and copy\_to\_user() are the Linux equivalents of XNU's copyin() and copyout(): They are used to copy memory from userspace into the kernel (copy\_from\_user()) or to copy memory from the kernel into userspace (copy\_to\_user()). It's well known that these operations can be blocked by using tricks involving [userfaultfd](https://www.google.com/url?q=https://www.kernel.org/doc/html/latest/admin-guide/mm/userfaultfd.html&sa=D&ust=1608578955091000&usg=AOvVaw06YNTMv0NBVU6zjZNk9XNM), but this won't be available to us in an exploit from app context. Nevertheless, Jann had discovered that similar tricks could be done using [proxy file descriptors](https://www.google.com/url?q=https://developer.android.com/reference/android/os/ProxyFileDescriptorCallback&sa=D&ust=1608578955091000&usg=AOvVaw1Q9-r_4razsXpR0WAGVDWk) (an abstraction over [FUSE](https://www.google.com/url?q=https://www.kernel.org/doc/html/latest/filesystems/fuse.html&sa=D&ust=1608578955091000&usg=AOvVaw3r-EKwzpOcxxmIIOjxyZZ8) provided by system\_server and vold), essentially allowing page faults on userspace pages to be blocked for arbitrary amounts of time.

One particularly interesting target while blocking a copy\_from\_user() operation would be copy\_from\_user() itself. When copy\_from\_user() performs the actual copy operation in \_\_arch\_copy\_from\_user(), the first access to the magical blocking memory region will trigger a page fault, causing an exception to be delivered and spilling all the registers of \_\_arch\_copy\_from\_user() to the kernel stack while the fault is being processed. During that time, we could come in on another thread using our out-of-bounds addition to increase the size argument to \_\_arch\_copy\_from\_user() where it is spilled onto the stack. That way, once we service the page fault via the proxy file descriptor and allow the exception to return, the modified size value will be popped back into the register and \_\_arch\_copy\_from\_user() will copy more data than expected into kernel memory. If the buffer being copied into lives on the stack, this gives us a deterministic controlled stack buffer overflow that we can use to clobber a return address and get code execution. And the same idea can be applied to copy\_to\_user() to copy extra memory out of the kernel instead, disclosing kernel stack contents and allowing us to break KASLR and leak the stack cookie.

In order to figure out which spilled register we'd need to target, I looked at \_\_arch\_copy\_to\_user() in IDA. Unfortunately, there's one other complication to make this technique work: due to unrolling, \_\_arch\_copy\_to\_user() will only enter a loop if the size is at least 128 bytes on entry. This means that we'll need to target a syscall that calls copy\_to\_user() with a size of at least 128 bytes.

Fortunately, it didn't take long to find several good stack disclosure candidates, such as the newuname() syscall:

| SYSCALL\_DEFINE1(newuname, struct new\_utsname \_\_user \*, name) { struct new\_utsname tmp; down\_read(&uts\_sem); memcpy(&tmp, utsname(), sizeof(tmp)); up\_read(&uts\_sem); if (copy\_to\_user(name, &tmp, sizeof(tmp))) return -EFAULT; ... } | 

The new\_utsname struct that gets copied out is 0x186 bytes, which means we should enter the looping path in \_\_arch\_copy\_to\_user(). When that access faults, the register containing the copy size 0x186 will be spilled to the stack, and we can change it to a very large value like 0x80610186 before unblocking the fault. To prevent the copyout from running off the end of the kernel stack, we will have the next page in userspace after the magic blocking page be unmapped, causing the \_\_arch\_copy\_to\_user() to terminate early and cleanly.

# The write path

The above trick should work for reading past the end of a stack buffer; what about for writing?

Here again I ran into a new complication, and this one was significant: copy\_from\_user() will zero out any unused space in the buffer that was not successfully copied from userspace:

| \_copy\_from\_user(void \*to, const void \_\_user \*from, unsigned long n) { unsigned long res = n; might\_fault(); if (likely(access\_ok(VERIFY\_READ, from, n))) { kasan\_check\_write(to, n); res = raw\_copy\_from\_user(to, from, n); } if (unlikely(res)) memset(to + (n - res), 0, res); return res; } | 

This means that copy\_from\_user() won't let us truncate the write early as we did with copy\_to\_user() by having an unmapped page after the blocking region. Instead, it will try to memset the memory past the end of the buffer to zero, all the way up to the modified size of at least 0x80500000. copy\_from\_user() is out.

Thankfully, there are some calls to the alternative function \_\_copy\_from\_user(), which does not perform this unwanted memset. But these are much rarer, and thus we'll have a very limited selection of syscalls to target.

In fact, pretty much the only call to \_\_copy\_from\_user() with a large size that I could find was in restore\_fpsimd\_context(), reached via the sys\_rt\_sigreturn() syscall. This syscall seems to be related to signal handling, and in particular restoring user context after returning from a signal handler. This particular \_\_copy\_from\_user() call is responsible for copying in the floating-point register state (registers Q0 - Q31) after validating the signal frame on the user's stack.

The size parameter at this callsite is 512 (0x200) bytes, which is large enough to enter the looping path in \_\_arch\_copy\_from\_user(). However, the address of the floating point register state that is read from during the copy-in is part of the userspace thread's signal frame on the stack, so it would be very tricky to ensure that both

1. the first access to the blocking page (which must be part of the thread's stack) is in the target call to \_\_copy\_from\_user() rather than earlier in the signal frame parsing, and
2. the address passed to \_\_copy\_from\_user() is deep enough into the blocking page that we hit a subsequent unmapped page in userspace before overflowing off the end of the kernel stack.

These two requirements are in direct conflict: Since the signal frame before the floating-point register state will be accessed in parse\_user\_sigframe(), the first requirement effectively means we need to put the floating-point state at the very start of the blocking page, so that the values right before can be accessed without triggering the blocking fault. But at the same time, the second requirement forces us to put the floating-point state towards the end of the blocking page so that we can terminate the \_\_arch\_copy\_from\_user() before running off the end of the kernel stack and triggering a panic. It's impossible to satisfy both of these requirements.

At this point I started looking at alternative ways to use our primitive to work around this conflict. In particular, we know that the \_\_arch\_copy\_from\_user() size parameter on entry will be 0x200, that ION buffers have addresses like 0x80xx0000, and that our addition need not be aligned. So, what if we overlapped only the most-significant byte of the ION address with the least-significant byte of the size parameter?

When \_\_arch\_copy\_to\_user() faults, its registers will be spilled to memory in the order X0, X1, X2, and so on. Register X2 holds the size value, which in our case will be 0x200, and X1 stores the userspace address being copied from. If we assume the first 3 bytes of the userspace address are zero, then we get the following layout of X1 and X2 in memory:

X1 | X2

UU UU UU UU UU 00 00 00 | 00 02 00 00 00 00 00 00

Then, if we come in with our unaligned addition with a daddr of 0x80610000:

X1            |           X2

UU UU UU UU UU 00 00 61 | 80 02 00 00 00 00 00 00

Thus, we've effectively increased the value of X2 from 0x200 to 0x280, which should be large enough to corrupt the stack frame of sys\_rt\_sigreturn() but small enough to avoid running off the end of the kernel stack.

The consequence of using an unaligned addition like this is that we've also corrupted the value of X1, which stores the userspace address from which to copy in the data. Instead of the upper bytes being all 0, the top byte is now nonzero. Quite fortunately, however, this isn't a problem because the kernel was compiled with support for the Top Byte Ignore (TBI) architectural feature enabled for userspace, which means that the top byte of the pointer will be ignored for the purpose of address translation by the CPU.

This gives us a reasonably complete exploit flow:

1. Create 2 "blocking pages" using proxy file descriptors.
2. Map the first blocking page before an unmapped page, and invoke the newuname() syscall with a pointer towards the end of the first blocking page. The copy\_to\_user() will fault and block, waiting on the corresponding proxy fd.
3. Use the out-of-bounds addition to increase the spilled value of register X2 from \_\_arch\_copy\_to\_user().
4. Fulfill the requested data on the first proxy fd, allowing the page fault to complete and resuming \_\_arch\_copy\_to\_user(). The copy-out will proceed past the ends of the stack buffer, disclosing the stack cookie and the return address, but stopping at the unmapped page.
5. Create a fake signal stack frame around a mapping of the second blocking page and invoke the sys\_rt\_sigreturn() syscall.
6. sys\_rt\_sigreturn() will call \_\_copy\_from\_user() with size 0x200 and fault trying to access the blocking page.
7. Use the out-of-bounds addition to increase the spilled value of register X2 from \_\_arch\_copy\_from\_user(), but align the addition such that only the least significant byte of X2 is changed. This will bump the spilled value from 0x200 to 0x280.
8. Fulfill the requested data on the second proxy fd, allowing the page fault to complete and resuming \_\_arch\_copy\_from\_user(). The copy-in will overflow the stack buffer, overwriting the return address.
9. When sys\_rt\_sigreturn() returns, we will gain code execution.

# Blocking problems

When I tried to implement this technique, I ran into a fatal problem: I couldn't seem to mmap() the proxy file descriptor in order to create the memory regions that would be used to block copy\_to/from\_user().

I checked with Jann, and he discovered that [the SELinux policy change](https://www.google.com/url?q=https://android.googlesource.com/platform/system/sepolicy/%2B/975215578f0b10a35a36c02e7f265a063796729e%255E%2521/%23F0&sa=D&ust=1608578955110000&usg=AOvVaw1PLwg2HYA0fc46ZEWPu4xg) that would allow mapping the proxy file descriptors was quite recent, and unfortunately too new to be available on my device:

\# For app fuse.

-allow appdomain app\_fuse\_file:file { getattr read append write };

+allow appdomain app\_fuse\_file:file { getattr read append write map };

This change was committed in March of 2020, and apparently would not migrate to my device until after the NPU bug I was exploiting would be fixed. Thus, I couldn't rely on blocking copy\_to/from\_user() after all, and would need to find an alternative target.

Thankfully, due to his copious knowledge of Linux internals, Jann was quickly able to suggest a few different strategies worth investigating. Since this post is already quite long I'll avoid explaining each of them and jump directly to the one that was the most promising: select().

# Revisiting the read

Since my previous strategy relied on the blocking memory region for both the stack disclosure (read) and stack buffer overflow (write) steps, I'd need to revisit both of them. But for right now, we'll focus on the read part.

The pselect() system call is an interesting target for our out-of-bounds addition primitive because it will deterministically block before calling copy\_to\_user() to copy out the contents of a stack buffer. Not only that, but the amount of memory to copy out to userspace is controllable rather than being hardcoded. Thus, we'll have an opportunity to modify the size parameter in a call to copy\_to\_user() while pselect() is blocked, and increasing the size should cause the kernel to disclose out-of-bounds stack memory.

Here's the relevant code from core\_sys\_select(), which implements the core logic of the syscall:

| int core\_sys\_select(int n, fd\_set \_\_user \*inp, fd\_set \_\_user \*outp, fd\_set \_\_user \*exp, struct timespec64 \*end\_time) { ... /\* Allocate small arguments on the stack to save memory and be faster \*/ long stack\_fds\[SELECT\_STACK\_ALLOC/sizeof(long)\]; ... /\* \* We need 6 bitmaps (in/out/ex for both incoming and outgoing), \* since we used fdset we need to allocate memory in units of \* long-words. \*/ size = FDS\_BYTES(n); bits = stack\_fds; if (size > sizeof(stack\_fds) / 6) { /\* Not enough space in on-stack array; must use kmalloc \*/ ... bits = kvmalloc(alloc\_size, GFP\_KERNEL); ... } fds.in = bits; fds.out = bits + size; fds.ex = bits + 2\*size; fds.res\_in = bits + 3\*size; fds.res\_out = bits + 4\*size; fds.res\_ex = bits + 5\*size; // get\_fd\_set() calls copy\_from\_user() if ((ret = get\_fd\_set(n, inp, fds.in)) \|\|(ret = get\_fd\_set(n, outp, fds.out)) \|\|(ret = get\_fd\_set(n, exp, fds.ex))) goto out; zero\_fd\_set(n, fds.res\_in); zero\_fd\_set(n, fds.res\_out); zero\_fd\_set(n, fds.res\_ex); // do\_select() may block ret = do\_select(n, &fds, end\_time); ... // set\_fd\_set() calls \_\_copy\_to\_user() if (set\_fd\_set(n, inp, fds.res\_in) \|\|set\_fd\_set(n, outp, fds.res\_out) \|\|set\_fd\_set(n, exp, fds.res\_ex)) ret = -EFAULT; ... } | 

As you can see, the local variable n must be saved to the stack while do\_select() blocks, which means that it can be modified before the call to set\_fd\_set() copies out the corresponding number of bytes to userspace. Also, if n is small, then the 256-byte stack\_fds buffer will be used rather than a heap-allocated buffer.

This code actually looks a bit different when compiled in the kernel due to optimization and inlining. In particular, the variable n is not used during the subsequent calls to \_\_arch\_copy\_to\_user(), but rather a hidden variable with the value 8 \* size allocated to register X22. Thus, wherever X22 gets spilled to the stack during the prologue of do\_select(), that's the address we need to target to change the size passed to \_\_arch\_copy\_to\_user().

But there's one other unfortunate consequence we'll have to deal with when moving from the old "blocking page" technique to this new technique: Before, we were modifying the size to be copied out during the execution of \_\_arch\_copy\_to\_user() itself, after all the sanity checks had passed on the original (unmodified) value. Now, however, we're trying to pass the corrupted value directly to \_\_copy\_to\_user(), which means we'll need to ensure that we don't trip any of the checks. In particular, \_\_copy\_to\_user() has a call to check\_object\_size() which will fail if the copy-out extends beyond the bounds of the stack.

Thankfully, we've already solved this particular problem already when dealing with sys\_rt\_sigreturn(). Just like in that case, we can set the offset of our out-of-bounds addition such that only the least significant byte of the spilled X22 is modified. But for this to be compatible with the precondition for the write, that the initial value being modified is smaller than the size of the ION buffer, this means that we need the least significant byte of X22 to be 0.

Because core\_sys\_select() will stop using the stack\_fds buffer if n is too large, this constraint actually admits only a single solution: n = 0. That is, we will need to call select() on 0 file descriptors, which will cause the value X22 = 0 to be stored to the stack when do\_select() blocks, at which point we can use our out-of-bounds addition to increase X22 to 0x80.

Thankfully, the logic of core\_sys\_select() functions just fine with n = 0; even better, the stack\_fds buffer is only zeroed for positive n, so bumping the copy-out size to 0x80 will allow us to read uninitialized stack buffer contents. So this technique should allow us to turn the out-of-bounds addition into a useful kernel stack disclosure.

Unfortunately, when I began implementing this, I ran into another significant problem. When the prologue of do\_select() saves X22 to the stack, it places register X23 right before X22, and X23 contains a kernel pointer at this point. This messes up the precondition for our out-of-bounds addition, because the unaligned value overlapping the least significant byte of X22 will be too large:

X23 | X22

XX XX XX XX 80 ff ff ff | 00 00 00 00 00 00 00 00

In order for our precondition to be met, we'd need to have an ION buffer of size at least 0x00ffffff (really, 0x01000000 due to granularity). My impression was that ION memory is quite scarce; is it even possible to allocate an ION buffer that large?

It turns out, yes! I had just assumed that such a large allocation (16 MiB) would fail, but it turns out to work just fine. So, all we have to do is increase the size of the ION buffer initially allocated to 0x1000000, and we should be able to modify register X22.

What about X23, won't that register be corrupted? It will, but thankfully X23 happens to be unused by core\_sys\_select() after the call to do\_select(), so it doesn't actually matter that we clobber it.

At last, we have a viable stack disclosure strategy!

1. Allocate a 16 MiB ION buffer.
2. Perform the vmalloc purge using binder fds.
3. Spray binder vmallocs to consume all vmalloc holes down to size 0x5000, and cause vmalloc() to start allocating from fresh VA space.
4. Spray thread stacks to fill any remaining 0x5000-byte holes leading up to the fresh VA space.
5. Map the ION buffer into the fresh VA space by invoking the vulnerable ioctl.
6. Spray thread stacks; these should land directly after the ION buffer mapping.
7. Call pselect() from the thread directly after the ION buffer with with n = 0; this call will block for the specified timeout.
8. Call ioctl() on the main thread to perform the out-of-bounds addition, targeting the value of X22 from core\_sys\_select(). Align the addition to bump the value from 0 to 0x80.
9. When do\_select() unblocks due to timeout expiry, the modified value of X22 will be passed to \_\_copy\_to\_user(), disclosing uninitialized kernel stack contents to userspace.

And after a few false starts, this strategy turned out to work perfectly:

Samsung NPU driver exploit

ION 0x80850000 \[0x01000000\]

Allocated ION buffer

Found victim thread!

buf = 0x74ec863b30

pselect() ret = 0 Success

buf\[00\]: 0000000000000124

buf\[08\]: 0000000000000015

buf\[10\]: ffffffc88f303b80

buf\[18\]: ffffff8088adbdd0

buf\[20\]: ffffffc89f935e00

buf\[28\]: ffffff8088adbd10

buf\[30\]: ffffff8088adbda8

buf\[38\]: ffffff8088adbd90

buf\[40\]: ffffff8008f814e8

buf\[48\]: 0000000000000000

buf\[50\]: ffffffc800000000

By inspecting the leaked buffer contents, it appears that buf\[38\] is a stack frame pointer and buf\[40\] is a return address. Thus we now know both the address of the victim stack, from which we can deduce the address of the ION buffer mapping, and the address of a kernel function, which allows us to break KASLR.

# Revisiting the write

Pretty much the only thing left to do is find a way to overflow a stack buffer using our primitive. Once we do this, we should be able to build a ROP chain that will give us some as-yet-unspecified kernel read/write capability.

For now, we won't worry about what to do after the overflow because ROP should be a sufficiently generic technique to implement whatever final read/write capability we want. Admittedly, for an iOS kernel exploit the choice of final capability would have substantial influence on the shape of the exploit flow. But this is because the typical iOS exploit achieves stable kernel read/write before kernel code execution, especially since the arrival of PAC. By contrast, if we can build a stack buffer overflow, we should be able to get ROP execution directly, which is in many ways more powerful than kernel read/write.

Actually, thinking about PAC and iOS gave me an idea.

When a userspace thread enters the kernel, whether due to a system call, page fault, IRQ, or any other reason, the userspace thread's register state needs to be saved in order to be able to resume its execution later. This includes the general-purpose registers X0 - X31 as well as SP, PC, and SPSR ("Saved Program Status Register", alternatively called CPSR or PSTATE). These values get saved to the end of the thread's kernel stack right at the beginning of the exception vector.

When Apple implemented their PAC-based kernel control flow integrity on iOS, they needed to take care that the saved value of SPSR could not be tampered with. The reason is that SPSR is used during exception return to specify the exception level to return to: this could be EL0 when returning to userspace, or EL1 when returning to kernel mode. If SPSR weren't protected, then an attacker with a kernel read/write primitive could modify the saved value of SPSR to cause a thread that would return to userspace (EL0) to instead return to EL1, thereby breaking the kernel's control flow integrity (CFI).

The Samsung Galaxy S10 does not have PAC, and hence SPSR is not protected. This is not a security issue because kernel CFI isn't a security boundary on this device. However, it does mean that this attack could be used to gain kernel code execution.

The idea of targeting the saved SPSR was appealing because we would no longer need the buffer overflow step to execute our ROP payload: assuming we could get an ION buffer allocated with a carefully chosen device address, we could modify SPSR directly using our out-of-bounds addition primitive.

Concretely, when a user thread invokes a syscall, the saved SPSR value might be something like 0x20000000. The least significant 4 bits of SPSR specify the exception level from which the exception was taken: in this case, EL0. A normal kernel thread might have a CPSR value of 0x80400145; in this case, the "5" means that the thread is running at EL1 and on the interrupt stack (SP\_EL1).

Now imagine that we could get our 0x01000000-byte ION buffer allocated with a device address of 0x85000000. We'll also assume that we've somehow already managed to set the user thread's saved PC register to a kernel pointer. The saved user PC and SPSR registers look like this on the stack:

PC            |          SPSR

XX XX XX 0X 80 FF FF FF | 00 00 00 20 00 00 00 00

Using our out-of-bounds addition primitive to change just the least significant byte of SPSR would yield the following:

PC            |          SPSR

XX XX XX 0X 80 FF FF FF | 85 00 00 20 00 00 00 00

Hence, we would have changed SPSR from 0x20000000 to 0x20000085, meaning that once the syscall returns, we will start executing at EL1!

Of course, that still leaves a few questions open: How do we get our ION buffer allocated at the desired device address? How do we set the saved PC value to a kernel pointer? We'll address these in turn.

Getting the ION buffer allocated at the desired device address seemed the most urgent, since it is quite integral to this technique. In my testing it seemed that ION buffers had decently (but not perfectly) regular allocation patterns. For example, if you had just allocated an ION buffer of size 0x2000 that had device address 0x80500000, then the next ION buffer was usually allocated with device address 0x80610000.

I played around with the available parameters a lot, hoping to discover an underlying logic that would allow me to deterministically predict ION daddrs. For instance, if the size of the first ION allocation was between 0x1000 and 0x10000 bytes, then the next allocation would usually be made at a device address 0x110000 bytes later, while if the first ION allocation was between 0x11000 and 0x20000 bytes, the next allocation would usually be at a device address 0x120000 bytes later. These patterns seemed to suggest that predictability was tantalizingly close; however, try as I might, I couldn't seem to eliminate the variations from the patterns I observed.

Eventually, by sheer random luck I happened to stumble upon a technique during one of my trials that would quite reliably allocate ION buffers at addresses of my choosing. Thus, we can now assume as part of our out-of-bounds addition primitive that we have control to choose the ION buffer's device address. Furthermore, the mask of available ION daddrs using this technique is much larger than I'd initially thought: 0x\[89\]xxxx000.

Now, as to the question of how we'll set the saved PC value to a kernel pointer: The simplest approach would just be to jump to that address from userspace; this would work to set the value, but it was not clear to me whether we'd be able to block the thread in the kernel in this state long enough to modify the SPSR using our addition primitive from the main thread. Instead, on recommendation from my team I used the ptrace() API, which via the PTRACE\_GETREGSET command provides similar functionality to XNU's thread\_set\_state().

# Total meltdown

My first test after implementing this strategy was to set PC to the address of an instruction that would dereference an invalid memory address. The idea was that running this test should cause a kernel panic right away, since the exception return would start running in kernel mode. Then I could check the panic log to see if all the registers were being set as I expected.

Unfortunately, my first test didn't panic: the syscall whose SPSR was corrupted just seemed to hang, never returning to userspace. And after several seconds of this (during which the phone was fully responsive), the phone would eventually reboot with a message about a watchdog timeout.

This seemed quite bizarre to me. If SPSR wasn't being set properly, the syscall should return to EL0, not EL1, and thus we shouldn't be able to cause any sort of kernel crash. On the other hand, I was certain that PC was set to the address of a faulting instruction, so if SPSR were being set properly, I'd expect a kernel panic, not a hard hang triggering a watchdog timeout. What was going on?

Eventually, Jann and I discovered that this device had the ARM64\_UNMAP\_KERNEL\_AT\_EL0 CPU feature set, which meant that the faulting instruction I was trying to jump to was being unmapped before the syscall return. Working around this seemed more trouble than it was worth: instead, I decided to abandon SPSR and go back to looking for ways to trigger a stack buffer overflow.

# Revisiting the write (again)

So, once again I was back to finding a way to use the out-of-bounds addition to create a stack buffer overflow.

This was the part of the exploit development process that I was least enthusiastic about: searching through the Linux code to find specific patterns that would give me the primitives I needed. Choosing to focus on stack frames rather than heap objects certainly helped narrow the search space, but it's still tedious. Thus, I decided to focus on the parts of the kernel I'd already grown familiar with.

The pattern that I was looking for was any place that blocks before copying data to the stack, where the amount of data to be copied was stored in a variable that would be saved during the block. Ideally, this would be a call to copy\_from\_user(), but I failed to find any useful instances of copy\_from\_user() being called after a blocking operation.

However, a horrible, horrible idea occurred to me while looking once again at the pselect() syscall, and in particular at the implementation of do\_select():

| static int do\_select(int n, fd\_set\_bits \*fds, struct timespec64 \*end\_time) { ... retval = 0; for (;;) { ... inp = fds->in; outp = fds->out; exp = fds->ex; rinp = fds->res\_in; routp = fds->res\_out; rexp = fds->res\_ex; for (i = 0; i \< n; ++rinp, ++routp, ++rexp) { ... in = \*inp++; out = \*outp++; ex = \*exp++; all\_bits = in \| out \| ex; if (all\_bits == 0) { i += BITS\_PER\_LONG; continue; } for (j = 0; j \< BITS\_PER\_LONG; ++j, ++i, bit \<\<= 1) { struct fd f; if (i >= n) break; if (!(bit & all\_bits)) continue; f = fdget(i); if (f.file) { ... if (f\_op->poll) { ... mask = (\*f\_op->poll)(f.file, wait); } fdput(f); if ((mask & POLLIN\_SET) && (in & bit)) { res\_in \|= bit; retval++; ... } ... } } if (res\_in) \*rinp = res\_in; if (res\_out) \*routp = res\_out; if (res\_ex) \*rexp = res\_ex; ... } ... if (retval \|\| timed\_out \|\| signal\_pending(current)) break; ... if (!poll\_schedule\_timeout(&table, TASK\_INTERRUPTIBLE, to, slack)) timed\_out = 1; } ... return retval; } | 

pselect() is able to check file descriptors for 3 types of readiness: reading (in fds), writing (out fds), and exceptional conditions (ex fds). If none of the file descriptors in the 3 fdsets are ready for the corresponding operations, then do\_select() will block in poll\_schedule\_timeout() until either the timeout expires or the status of one of the selected fds changes.

Imagine what happens if, while do\_select() is blocked in poll\_schedule\_timeout(), we use our out-of-bounds addition primitive to change the value of n. We already know from our analysis of core\_sys\_select() that if n was sufficiently small to begin with, then the stack\_fds array will be used instead of allocating a buffer on the heap. Thus, in, out, and ex may reside on the stack. Once poll\_schedule\_timeout() unblocks, do\_select() will iterate over all file descriptor numbers from 0 to (the corrupted value of) n. Towards the end of this loop, inp, outp, and exp will be read out-of-bounds, while rinp, routp, and rexp will be written out of bounds. Thus, this is actually a stack buffer overflow. And since the values written to rinp, routp, and rexp are determined based on the readiness of file descriptors, we have at least some hope of controlling the data that gets written.

# Sizing the overflow

So, in theory, we could target pselect() to create a stack buffer overflow using our out-of-bounds addition. There are still a lot of steps between that general idea and a working exploit.

Let's begin just by trying to understand the situation we're in a bit more precisely. Looking at the function prologues in IDA, we can determine the stack layout after the stack\_fds buffer:


The stack layout of core\_sys\_select() and all earlier frames in the call stack. The 256-byte stack\_fds buffer out of which we will overflow is 0x348 bytes from the end of the stack and followed by a stack guard and return address.

There are two major constraints we're going to run into with this buffer overflow: controlling the length of the overflow and controlling the contents of the overflow. We'll start with the length.

Based on the depth of the stack\_fds buffer in the kernel stack, we can only write 0x348 bytes into the buffer before running off the end of the stack and triggering a kernel panic. If we assume a maximal value of n = 0x140 (which will be important when controlling the contents of the overflow), then that means we need to stop processing at inp = 0x348 - 5 \* 0x28 = 0x280 bytes into the buffer, which will position rexp just off the end of the stack. This corresponds to a maximum corrupted value of n of 8 \* 0x280 = 0x1400.

So, how do we choose an ION buffer daddr such that adding the daddr into n = 0x140 at some offset will yield a value significantly greater than 0x140 but less than 0x1400?

Unfortunately, the math on this doesn't work out. Even if we choose from the expanded range of ION device addresses 0x\[89\]xxxx000, there is no address that can be added to 0x140 at a particular offset to produce a 32-bit value between 0x400 and 0x1400.

Nevertheless, we do still have another option available to us: 2 ION buffers! If we can choose the device address of a single ION buffer, theoretically we should be able to repeat the feat to choose the device addresses of 2 ION buffers together; can we find a pair of daddrs that can be added to 0x140 at particular offsets to produce a 32-bit value between 0x400 and 0x1400?

It turns out that adding in a second independent daddr now gives us enough degrees of freedom to find a solution. For example, consider the daddrs 0x8qrst000 and 0x8wxyz000 being added into 0x140 at offsets 0 and +1, respectively. Looking at how the bytes align, it's clear that the only sum less than 0x1400 will be 0x1140. Thus, we can derive a series of relations between the digits:

carry 11 1

\+ 00 z0 xy 8w

\+ 00 t0 rs 8q

40 01 00 00 00 00 00 00

---------------------------

40 11 00 00 ??

t = 1

s = 0

z+r = 0 OR z+r = 10

ASSUME z+r = 10

1+y+q = 10 => y+q = f

1+x+8 = 10 => x = 7

In this case, we discover that daddrs 0x8qr01000 and 0x8w7yz000 will be a solution so long as q + y = 0xf and r + z = 0x10. For example, 0x81801000 and 0x827e8000 are a solution:

carry 11 1

\+ 00 80 7e 82

\+ 00 10 80 81

40 01 00 00 00 00 00 00

---------------------------

40 11 00 00 83

corrupted 32-bit n is 0x1140

So, we'll need to tweak our original heap groom slightly to map both ION buffers back-to-back before spraying the kernel thread stacks.

# Controlling the contents

Using 2 ION buffers with carefully chosen device addresses allows us to control the size of the stack buffer overflow. Meanwhile, the contents of the overflow are the output of the pselect() syscall, which we can control because we can control which file descriptors in our process are ready for various types of operations. But once we overflow past the original value of n, we run into a problem: we start reading our input data from the data previously written to the output buffer.


Corrupting the value of n will cause do\_select() to keep processing inp, outp, and exp past their original bounds. Eventually the output cursor rinp will start overflowing out of the stack\_fds buffer entirely, overwriting the return address. But before that happens, inp will start consuming the previous output of rinp.

To make the analysis simpler, we can ignore out, ex, rout, and rex to focus exclusively on in and rin. The reason for this is that rout and rex will eventually be overwritten by rin, so it doesn't really matter what they write; if the overflow continues for a sufficient distance, only the output of rin matters.

Using the assumed value of n = 0x140, each of the in, out, ex, rin, rout, rex buffers is 0x28 bytes, so after processing 3 \* n = 0x3c0 file descriptors, inp (the input pointer) will start reading from rin (the output buffer), and this will continue as the out-of-bounds write progresses down the stack. By the semantics of select(), each bit in rinp is only written with a 1 if both the corresponding bit in inp was a 1 and the corresponding file descriptor was readable. Thus, once we've written a 0 bit at any location, every bit at a multiple of 0x3c0 bits later will also be 0. This introduces a natural cycle in our overflow that constrains the output.

It's also worth noting that if you look back at do\_select(), rinp is only written if the full 64-bit value to write is nonzero. Thus, if any 64-bit output value is 0 (i.e., all 64 fds in the long are either not selected on or not readable), then the corresponding stack location will be left intact.


Because of the 3 \* 0x28 = 0x78-byte cycle length, we can treat this primitive as the ability to write up to 15 controlled 64-bit values into the stack, each at a unique offset modulo 0x78, while leaving stack values at the remaining offsets modulo 0x78 intact. This is a conservative simplification, since our primitive is somewhat more flexible than this, but it's useful to visualize our primitive this way.

Under this simplification, we can describe the out-of-bounds write as 15 (offset, value) pairs, where offset is the offset from the start of the stack\_fds array in bytes (which must be a multiple of 8 and must be unique mod 0x78) and value is the 64-bit value to be written at that offset. For each (offset, value) pair, we need to set to 1 every bit in each "preimage" of value from an earlier cycle.

To simplify things even further, let's regard the concatenation of the input fdsets in, out, and ex as a single input fdset, just as it appears on the kernel stack in the stack\_fds buffer once we've corrupted n.

The simplest solution is to have the "preimage" of each value be value itself, which can be done by setting the portion of the input fdset at offset % 0x78 to value for each (offset, value) pair and by making every file descriptor from 0 to 0x1140 be readable. Since we'll only be selecting on the fds that correspond to 1 bits in value and since every fd is readable, this will mirror the entire input buffer (consisting of the 15 values at their corresponding offsets) down the kernel stack repeatedly. This will trivially ensure that value gets placed at offset because value will be written to every offset in the kernel stack that is the same as offset mod 0x78.


By making all of the first 0x1140 file descriptors readable, the input buffer's 15 longs will be mirrored down the stack, repeating every 0x3c0 bits.

Using a slightly more complicated solution, however, we can limit the depth of the stack corruption. Instead, we'll have the preimage of each value be \~0 (i.e., all 64 bits set), and use the readability of each file descriptor to control the bits that get written. That way, once we've written the value at the correct offset, the fds corresponding to subsequent cycles can be made non-readable, thereby preventing the corruption from continuing down the stack past the desired depth of each write.

This still leaves one more question about the mechanics of the stack buffer overflow: poll\_schedule\_timeout() will return as soon as any file descriptor becomes readable, so how can we make sure that all the fds for all the 1 bits become readable at the same time? Fortunately this has an easy solution: create 2 pipes, one for all 0 bits and one for all 1 bits, and use dup2() to make all the fds we'll be selecting on be duplicates of the read ends of these pipes. Writing data to the "1 bits" pipe will cause poll\_schedule\_timeout() to unblock and all the "1 bits" fds will be readable (since they're all dups of the same underlying file). The only thing we need to be careful about is to ensure that at least one of the original in file descriptors (fds 0-0x13f) is a "1 bit" dup, or else poll\_schedule\_timeout() won't notice the status change when we write to the "1 bits" pipe.

Combining all of these ideas together, we can finally control the contents of the buffer overflow, clobbering the return address (while leaving the stack guard intact!) to execute a small ROP payload.

# The ultimate ROP

Finally, it's time to consider our ROP payload. Because we can write at most 15 distinct 64-bit values into the stack via our overflow (2 of which we've already used), we'll need to be careful about keeping the ROP payload small.

When I mentioned this progress to Jann, he suggested that I check the function \_\_\_bpf\_prog\_run(), which he described as the ultimate ROP gadget. And indeed, if your kernel has it compiled in, it does appear to be the ultimate ROP gadget!

\_\_\_bpf\_prog\_run() is responsible for interpreting eBPF bytecode that has already been deemed safe by the eBPF verifier. As such, it provides a number very powerful primitives, including:

1. arbitrary control flow in the eBPF program;
2. arbitrary memory load;
3. arbitrary memory store;
4. arbitrary kernel function calls with up to 5 arguments and a 64-bit return value.

So how can we start executing this function with a controlled instruction array as quickly as possible?

First, it's slightly easier to enter \_\_\_bpf\_prog\_run() through one of its wrappers, such as \_\_bpf\_prog\_run32(). The wrapper takes just 2 arguments rather than 3, and of those, we only need to control the second:

| unsigned int \_\_bpf\_prog\_run32(const void \*ctx, const bpf\_insn \*insn) | 

The insn argument is passed in register X1, which means we'll need to find a ROP gadget that will pop a value off the stack and move it into X1. Fortunately, the following gadget from the end of the current\_time() function gives us control of X1 indirectly via X20:

FFFFFF8008294C20 LDP X29, X30, \[SP,#0x10+var\_s0\]

FFFFFF8008294C24 MOV X0, X19

FFFFFF8008294C28 MOV X1, X20

FFFFFF8008294C2C LDP X20, X19, \[SP+0x10+var\_10\],#0x20

FFFFFF8008294C30 RET

The reason this works is that X20 was actually popped off the stack during the epilogue of core\_sys\_select(), which means that we already have control over X20 by the time we execute the first hijacked return. So executing this gadget will move the value we popped into X20 over to register X1. And since this gadget reads its return address from the stack, we'll also have control over where we return to next, meaning that we can jump right into \_\_bpf\_prog\_run32() with our controlled X1.

The only remaining question is what value to place in X1. Fortunately, this also has a very simple answer: the ION buffers are mapped shared between userspace and the kernel, and we already disclosed their location when we leaked the uninitialized stack\_fds buffer contents before. Thus, we can just write our eBPF program into the ION buffer and pass that address to \_\_bpf\_prog\_run32()!

For simplicity, I had the eBPF implement a busy-poll of the shared memory to execute commands on behalf of the userspace process. The eBPF program would repeatedly read a value from the ION buffer and perform either a 64-bit read, 64-bit write, or 5-argument function call based on the value that was read. This gives us an incredibly simple and reliable kernel read/write/execute primitive.

Even though the primitive was hacky and the system was not yet stable, I decided to stop developing the exploit at this point because my read/write/execute primitive was sufficiently powerful that subsequent exploitation steps would be fully independent of the original bug. I felt that I had achieved the goal of exploring the differences between kernel exploitation on Android and iOS.

# Conclusion

So, what are my takeaways from developing this Android exploit?

Overall, the quality of the hardware mitigations on the Samsung Galaxy S10 was much stronger than I had expected. My uninformed expectation about the state of hardware mitigation adoption on Android devices was that it lagged significantly behind iOS. And in broad strokes that's true: the iPhone XS's A12 SOC supports ARMv8.3-A compared to the Qualcomm Snapdragon 855's ARMv8.2-A, and the A12 includes a few Apple-custom mitigations (KTRR, APRR+PPL) not present in the Snapdragon SOC. However, the mitigation gap was substantially smaller than I had been expecting, and there were even a few ways that the Galaxy S10 supported stronger mitigations than the iPhone XS, for instance by using unprivileged load/store operations during copy\_from/to\_user(). And as interesting as Apple's custom mitigations are on iOS, they would not have blocked this exploit from obtaining kernel read/write.

In terms of the software, I had expected Android to provide significantly weaker and more limited kernel manipulation primitives (heap shaping, target objects to corrupt, etc) than what's provided by the Mach microkernel portion of XNU, and this also seems largely true. I suspect that part of the reason that public iOS exploits all seem to follow very similar exploit flows is that the pre- and post-exploitation primitives available to manipulate the kernel are exceptionally powerful and flexible. Having powerful manipulation primitives allows you to obtain powerful exploitation primitives more quickly, with less of the exploit flow specific to the exact constraints of the bug. In the case of this Android exploit, it's hard for me to speak generally given my lack of familiarity with the platform. I did manage to find good heap manipulation primitives, so the heap shaping part of the exploit was straightforward and generic. On the other hand, I struggled to find stack frames amenable to manipulation, which forced me to dig through lots of technical constraints to find strategies that would just barely work. As a result, the exploit flow to get kernel read/write/execute is highly specific to the underlying vulnerability until the last step. I'm thus left feeling that there are almost certainly much more elegant ways to exploit the NPU bugs than the strategy I chose.

Despite all these differences between the two platforms, I was overall quite surprised with the similarities and parallels that did emerge. Even though the final exploit flow for this NPU bug ended up being quite different, there were many echoes of the oob\_timestamp exploit along the way. Thus my past experience developing iOS kernel exploits did in fact help me come up with ideas worth trying on Android, even if most of those ideas didn't pan out.
