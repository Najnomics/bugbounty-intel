# A day^W^W Several months in the life of Project Zero - Part 2: The Chrome exploit of suffering - Project Zero

Source: https://projectzero.google/2020/02/several-months-in-life-of-part2.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Sergei Glazunov and Mark Brand, Project Zero

## Introduction

After we’d understood how the bug worked, and had passed on those details to Chrome to help them get started on a fix, we went back to our other projects. This bug remained a topic of discussion, and eventually we ran out of excuses for not trying to write an exploit for it.


One of the main reasons for doing this was to understand how readily exploitable bugs in the Chrome network stack are, given the relatively recent changes in the process architecture. Nobody in the team had taken a serious look at exploiting an issue in the network stack in Chrome, so it would likely give some more interesting insights than an exploit targeting more well-understood areas of the codebase, such as renderer bugs or the more typical browser-process sandbox escape targets.


While it may take you just a matter of minutes to read this post; the work behind it took a little longer, with many more failures than successes, even though the end result was a working "single-bug-chain" Chrome exploit.


Many of our failures weren’t due to any particular difficulty, and instead due to carelessness, which seems somehow more problematic when working with unreliable primitives; it’s easy to spend a whole day debugging a failing heap groom without, for example, noticing that you have the webserver running on the wrong port…

## Chapter 4. The Exploit.

We finished [last time](/2020/02/several-months-in-life-of-part1.html) with quite a powerful primitive; the vulnerability gave us a write of controlled data of a chosen size past the end of a heap allocation. There was just one major drawback to overcome — due to the way the bug works, the allocation that we’re overwriting will always be of size 0.


As most other allocators, tcmalloc stores it in the smallest class size, which is "up to 16 bytes" in this case. There are two issues with the size class. Firstly, "useful" objects (i.e. the ones that contain pointers we might want to overwrite) are usually larger than that. Secondly, the size class is rather congested as virtually every IPC call to the network process triggers allocations and deallocations in it. Therefore we can’t use, for example, the "heavy" fetch API, for heap spraying / grooming. Unfortunately, there are few object types in the network process that fit into 16 bytes and the creation of which doesn’t trigger a bunch of other allocations.


There was some good news too. If the network process crashes it will be silently restarted, so we would be able to use this as a crutch if we were struggling with reliability — our exploit would be able to try several times before it succeeds.

#### NetToMojoPendingBuffer

We were able to find an object that was suitable for constructing a "write-what-where" primitive relatively quickly by just enumerating small classes related to the network process. A new NetToMojoPendingBuffer object is created on every URLLoader::ReadMore call, so the attacker can control these allocations by delaying the dispatch of response chunks on the web server side.


class COMPONENT\_EXPORT(NETWORK\_CPP) NetToMojoPendingBuffer

: public base::RefCountedThreadSafe\<NetToMojoPendingBuffer> {

mojo::ScopedDataPipeProducerHandle handle\_;

void\* buffer\_;

};


We don’t have to worry about overwriting handle\_ because when Chrome encounters an invalid handle it just returns early without crashing. The data that will get written to the buffer’s backing store is exactly the next HTTP response chunk, so it’s also fully controlled.


There’s a problem, though — the primitive alone won’t suffice without a separate infoleak. An obvious idea to make it more powerful would be to perform a partial overwrite of buffer\_ and subsequently corrupt an object in some other (hopefully more convenient) size class. However, the pointer never gets assigned to a regular heap address. Instead, the backing store for NetToMojoPendingBuffer objects is allocated inside a shared memory region that’s only used for IPC and doesn’t contain objects, so there’s nothing to corrupt there.


Apart from NetToMojoPendingBuffer, we couldn’t find anything in the 16-byte size class that would look immediately useful.

#### Going after STL containers.

Luckily, we’re not limited to C++ classes and structures. Instead, we can target arbitrarily sized buffers like container backing stores. For example, when an element is being inserted into an empty std::vector, we allocate a backing store with space for just a single element. On subsequent insertions, if there’s no space left it gets doubled. Some other container classes operate in a similar way. Thus, if we precisely control insertions to, e.g., a vector of pointers, we can perform a partial overwrite of one of the pointers to turn the bug into a type confusion of some sort.

#### WatcherDispatcher.

A crash related to WatcherDispatcher showed up while we were experimenting with NetToMojoPendingBuffer. The WatcherDispatcher class is not specific to the network process. It’s one of the basic Mojo structures, used everywhere that IPC messages are sent and received. The class layout is as follows:


class WatcherDispatcher : public Dispatcher {

using WatchSet = std::set\<const Watch\*>;

base::Lock lock\_;

bool armed\_ = false;

bool closed\_ = false;

base::flat\_map\<uintptr\_t, scoped\_refptr\<Watch>> watches\_;

base::flat\_map\<Dispatcher\*, scoped\_refptr\<Watch>> watched\_handles\_;

WatchSet ready\_watches\_;

const Watch\* last\_watch\_to\_block\_arming\_ = nullptr;

};

class Watch : public base::RefCountedThreadSafe\<Watch> {

const scoped\_refptr\<WatcherDispatcher> watcher\_;

const scoped\_refptr\<Dispatcher> dispatcher\_;

const uintptr\_t context\_;

const MojoHandleSignals signals\_;

const MojoTriggerCondition condition\_;

MojoResult last\_known\_result\_ = MOJO\_RESULT\_UNKNOWN;

MojoHandleSignalsState last\_known\_signals\_state\_ = {0, 0};

base::Lock notification\_lock\_;

bool is\_cancelled\_ = false;

};

MojoResult WatcherDispatcher::Close() {

// We swap out all the watched handle information onto the stack so we can

// call into their dispatchers without our own lock held.

base::flat\_map\<uintptr\_t, scoped\_refptr\<Watch>> watches;

{

base::AutoLock lock(lock\_);

if (closed\_)

return MOJO\_RESULT\_INVALID\_ARGUMENT;

closed\_ = true;

std::swap(watches, watches\_);

watched\_handles\_.clear();

}

// Remove all refs from our watched dispatchers and fire cancellations.

for (auto& entry : watches) {

entry.second->dispatcher()->RemoveWatcherRef(this, entry.first);

entry.second->Cancel();

}

return MOJO\_RESULT\_OK;

}


std::flat\_map is actually backed by std::vector and watched\_handles\_ contains only one element most of the time, which takes exactly 16 bytes. This means we can overwrite a Watch pointer!


The size of the Watch class is relatively large — 104 bytes — and because of tcmalloc we can only target objects of a similar size for the partial overwrite. Furthermore, the target object should contain valid pointers at certain offsets to survive a call of a Watch method. Unfortunately, the network process doesn’t seem to contain a class that would meet the above requirements for a straightforward type-confusion.


We can take advantage of the fact that Watch is a reference-counted class though. The idea is to spray a lot of Watch-sized buffers, which tcmalloc will place next to the actual Watch object, and hope that scoped\_refptr with the overwritten least significant byte will point to one of our buffers. The buffer should have the first 64-bit word, i.e. the fake reference counter, set to 1 and the rest set to 0. In that case, a call to WatcherDispatcher::Close, which frees the scoped\_refptr, will trigger the deletion of our fake Watch, the destructor will finish gracefully, and the buffer will get freed.


If our buffer is scheduled to be sent to the attacker’s server or back to the renderer process, this will leak tcmalloc’s masked freelist pointers or, even better, some useful pointers if we managed to allocate something else there in the meantime. So, what we need now is the ability to create such buffers in the network process and delay sending them until the corruption has occurred.


Turns out the network process in Chrome is also responsible for handling WebSocket connections. What’s important is that WebSocket is a low overhead protocol, and it allows transferring binary data. If we make the receiving end of the connection sufficiently slow and send enough data to fill up the OS socket send buffer until the point where TCPClientSocket::Write becomes an "asynchronous" operation, subsequent calls to WebSocket::send will result in raw frame data being stored as IOBuffer objects with just two extra 32-byte allocations on each call. Moreover, we can control the lifetime of the buffers by modifying the delay on the receiving side.


Looks like we just found a near-perfect heap spraying primitive! It has one weakness though — it’s not possible to free an individual buffer. All frames tied to a connection get freed at once either when the current batch is sent or when the connection is torn down. We obviously can’t have a WebSocket connection per spray object, and each of the above operations induces a lot of undesired "noise" in the heap. However, let’s put it aside for a moment.


The following is the outline of the method:



Unfortunately, watched\_handles\_ quickly proved to be a suboptimal target. Some of its drawbacks are:

- There are actually two flat\_map members, but we can only use one of them since corrupting watched\_handles\_ will immediately trigger a crash during the RemoveWatcherRef virtual method call.
- Each WatcherDispatcher allocation triggers a lot of "noise" in the size classes we care about.
- There are 16 (= 256 / GCD(112, 256)) possible values for the LSB of a pointer in the Watch size class, most of which won’t even point to the beginning of an object.


While we were able to leak some data using this approach, its success rate was rather upsetting. The approach itself seemed reasonable, but we had to find a more "convenient" container to overwrite.

#### WebSocketFrame

It’s time to take a closer look at how sending a WebSocket frame is implemented.


class NET\_EXPORT WebSocketChannel {

\[...\]

std::unique\_ptr\<SendBuffer> data\_being\_sent\_;

// Data that is queued up to write after the current write completes.

// Only non-NULL when such data actually exists.

std::unique\_ptr\<SendBuffer> data\_to\_send\_next\_;

\[...\]

};

class WebSocketChannel::SendBuffer {

std::vector\<std::unique\_ptr\<WebSocketFrame>> frames\_;

uint64\_t total\_bytes\_;

};

struct NET\_EXPORT WebSocketFrameHeader {

typedef int OpCode;

bool final;

bool reserved1;

bool reserved2;

bool reserved3;

OpCode opcode;

bool masked;

uint64\_t payload\_length;

};

struct NET\_EXPORT\_PRIVATE WebSocketFrame {

WebSocketFrameHeader header;

scoped\_refptr\<IOBuffer> data;

};

ChannelState WebSocketChannel::SendFrameInternal(

bool fin,

WebSocketFrameHeader::OpCode op\_code,

scoped\_refptr\<IOBuffer> buffer,

uint64\_t size) {

\[...\]

if (data\_being\_sent\_) {

// Either the link to the WebSocket server is saturated, or several

// messages are being sent in a batch.

if (!data\_to\_send\_next\_)

data\_to\_send\_next\_ = std::make\_unique\<SendBuffer>();

data\_to\_send\_next\_->AddFrame(std::move(frame));

return CHANNEL\_ALIVE;

}

data\_being\_sent\_ = std::make\_unique\<SendBuffer>();

data\_being\_sent\_->AddFrame(std::move(frame));

return WriteFrames();

}


WebSocketChannel employs two separate SendBuffer objects to store outgoing frames. When the connection is saturated, new frames go into data\_to\_send\_next\_. And, since the buffers are backed by an std::vector\<std::unique\_ptr\<...>>, it can also become a target for overwriting! However, we need to figure out precisely the amount of data that has to be sent before the connection becomes saturated, otherwise data\_to\_send\_next\_’s buffer will quickly become too large to fit in the 16-byte slot. This value, which is tied to the FRAMES\_ENOUGH\_TO\_FILL\_BUFFER constant in the exploit, depends on both the network and system configuration. In theory, the exploit could calculate the value automatically; we just did it manually though for the "localhost" and "same LAN" cases. Also, to make the saturation process more reliable, the SO\_RCVBUF option for the WebSocket server socket has to be changed to a relatively small value,  and data compression has to be disabled.


As mentioned above, our heap spray technique makes two extra 32-byte allocations for each "desired" allocation. Unfortunately, WebSocketFrame, a pointer to which we’re planning to overwrite, is exactly 32 bytes in size. That means unless we use some additional heap manipulation tricks, only 1/3 of all objects produced during the heap spray will be of the right type. On the other hand, there are half as many possible values for the LSB in this size class compared to the Watch one, with a much higher chance of pointing to the beginning of a proper allocation. What’s even more important is, unlike WatcherDispatcher, WebSocket::Send won’t trigger any allocations in the 16-byte arena apart from resizing the std::vector that we’re targeting, so the heap spray in that size class should be clean and tidy. On balance, this makes data\_to\_send\_next\_ a better target.

#### Allocation Patterns

For lack of a more robust alternative, we have to use WebSocket::Send as the default heap manipulation tool. It’s responsible for at least:

- Spraying with 32-byte buffers, to one of which we want to overwrite the WebSocketFrame pointer.
- Inserting the target vector entry and creating the tied WebSocketFrame.
- Allocating an IOBuffer object in place of the freed buffer.



The objects shown in red above are "unwanted" allocations. Each of those will negatively affect the reliability of the exploit, but we have no way of avoiding them so far and just have to hope that with the unlimited amount of retries it won’t matter much.

#### Infoleak

Once we can fairly reliably overwrite the WebSocketFrame pointer, we’ve turned our slightly annoying primitive that only let us corrupt objects in the 16-byte bucket into a new primitive allowing us to free an allocation from the 32-byte bucket instead. Since data\_to\_send\_next\_ uses std::unique\_ptr instead of scoped\_refptr, we also don’t have to care about making up a fake reference counter. The only requirement for the free’d fake WebSocketFrame is that its data pointer should be null.


We can use this primitive to build quite a useful infoleak that will give us both the location of the Chrome binary in memory, and the location of data that we can control on the heap, giving us all the information that’s necessary to complete our exploit.


One of the advantages of using WebSockets in our heap manipulation is that the browser is going to send the data stored in these frames to the server (once the socket is unblocked), and so if we can use this free to free the backing store for an IOBuffer that’s already queued to be sent, we will be able to leak the new contents of that allocation. Additionally, since this size class matches the allocation size of the IOBuffer objects, we can replace the free backing store with a new IOBuffer object. This gives us a leak of the IOBuffer vtable pointer, the first piece of information that we need.


However, the IOBuffer object also includes a pointer to its backing store — which is a heap allocation of a size that we control. If we ensure that this is in a size class that won’t interfere with the rest of our heap manipulation, we can leak this pointer now, and later on in the exploit we can free this allocation and reuse it for something more useful.



#### Code Execution

Assuming that we can reuse the larger allocation that we leaked the address of, we could certainly be forgiven for thinking that we’re almost done here — we know where we can write some data, we know what data we should write there, and we have the relatively powerful 32-byte free primitive we built for the infoleak.


Unfortunately, as mentioned above, we don’t really have great primitives for just allocating IOBuffers or WebSocketFrames individually; good things come in pairs! While for the infoleak we didn’t have much flexibility (we needed to free an IOBuffer backing store, and we needed to replace it with an IOBuffer object), for the next stage in our exploit we have a few options to try and increase our chances of success.


Since we’re not interested in freeing an IOBuffer backing store any more, we can move those allocations into a different size class, so that we now have only three different object types coming from the 32-byte bucket: WebSocketFrame, IOBuffer, and SendBuffer. If we can spray perfectly, then we should be able to arrange to have 3 pairs of "target IOBuffer" and "target WebSocketFrame" for each "victim WebSocketFrame". This means that when we corrupt the pointer to the "victim WebSocketFrame" by triggering the vulnerability a second time, we have an equal probability of freeing either an IOBuffer or a WebSocketFrame.


By crafting our replacement object carefully, we can take advantage of both possibilities. We’re going to gain control of execution during the destructor call for either the WebSocketFrame or the IOBuffer. The only field that really matters in the WebSocketFrame is the data pointer, which needs to point to an IOBuffer object. Since this corresponds to the padding bytes at the end of the IOBuffer object, we can create a replacement object that can fill the space of either a freed IOBuffer or a freed WebSocketFrame.


When the replacement object is then freed, if we replaced an IOBuffer then when decrementing ref\_count\_ results in 0, we’ll get a virtual call through our fake vtable — if we instead replaced a WebSocketFrame, then the WebSocketFrame will release its data member, which we’ve pointed to another fake IOBuffer, which will again result in a virtual call through our fake vtable.


Throughout all of the above, we’ve been ignoring a minor detail — which thanks to our careful prior preparation will indeed turn out to be fairly minor — we need to get our second fake IOBuffer and our fake vtable into memory at a known address. We unfortunately can’t release the allocation that we leaked the address of earlier, since the IOBuffer object that we leaked will have been freed (as though it was the backing store of the IOBuffer sent back to us).


This isn’t a major issue though; we can choose for those larger allocations to go into a "quiet" bucket size. If we prepare that bucket size in advance with alternating buffers from two different websockets, then we can release one of those websockets to ensure that the address we leak will be adjacent to a buffer from the second websocket. After we’ve leaked the address, we can then release the second websocket and replace the contents of this adjacent buffer with our fake objects.




In summary, we use the backing data of a larger IOBuffer at a known address to write controlled data into memory. This contains a fake IOBuffer vtable, together with our code-reuse payload and a second fake IOBuffer. We can then trigger the vulnerability again, this time causing the use-after-free of either an IOBuffer object or a WebSocketFrame object, both of which will use pointers into the larger IOBuffer backing data that’s (now) at a known address.


When the corrupted objects are freed, our payload is run and our work here is done… almost…

#### Recap: Component breakdown

At this point, we have quite a few moving parts, so for those of you who want to dive into the source code for the exploit here’s a quick breakdown:


- serv.py — a custom webserver that will just handle the request for the image file, and return the appropriate sequence of responses to trigger the vulnerability.
- pywebsocket.diff — a few patches to pywebsocket which remove compression and set SO\_RCVBUF for the websocket server.
- get\_chrome\_offsets.py — a script that will attach to the running browser and collect all of the necessary offsets for the payload. This requires[frida](https://www.frida.re/) to be installed.
- CrossThreadSleep.py — this implements a basic sleepable wait primitive that is used to sleep individual threads in the websocket server and wake them from other threads.
- exploit/echo\_wsh.py — a websocket handler for pywebsocket that handles several message types that will cause either a timed delay or a wakeable delay that allow the socket-buffering manipulation that we need.
- exploit/wake\_up\_wsh.py — a websocket handler for pywebsocket that handles several control messages to wake sleeping "echo" sockets.
- exploit/exploit.html — the javascript code that is used to implement the exploit logic.


We’ve also provided some scripts to make it easier for readers to get a working Chromium build that’s vulnerable to the issue, and to get the rest of the environment set up correctly:


- get\_chromium.sh — a shell script that will check out and configure a vulnerable Chromium release.
- get\_pywebsocket.sh — a shell script that will download and patch pywebsocket for the exploit server.
- run\_pywebsocket.sh — a shell script to start the exploit server. You need to separately run the serv.py script.


The exploit server runs on two ports: exploit.html is served up by the websocket server, and the second server serves the image used to trigger the vulnerability.

## Chapter 5. More reliable exploit

At this point we have an exploit that should work sometimes. It creates a lot of "junk" allocations during the heap spray, and we’ve made a lot of assumptions about hitting the correct object types, so let’s evaluate the probability of a single exploit run succeeding:



Given that one run takes about a minute, this is definitely not a satisfactory result, even with the virtually unlimited number of retries that we have.

#### Cookie-based heap grooming

To make our heap spray more reliable we need a way to separate "good" and "bad" 32-byte allocations. As the reader might have already noticed, precisely manipulating the heap in the network process is not a trivial task, especially from the position of a non-compromised renderer.


One of the features related to networking that we haven’t considered yet is HTTP cookies. Somewhat surprisingly, the network process is responsible for not only sending and receiving cookies, but also for storing them in memory and saving them to disk. Since there exists the JavaScript API for cookie operations, and the operations don’t seem to be terribly complex, we might use the API to build additional heap manipulation primitives.


After some experimentation, we’ve constructed three new heap manipulation primitives:




To be honest, they are much less straightforward than we originally expected. For example, here’s the output of a Frida script that tracks the 32-byte heap arena state transitions during the execution of the free\_slot() method, which, as its name suggests, just appends a new entry to the 32-byte freelist.



As you can see, it’s perhaps not the simple, clean and tidy primitive we’d like to have, but it does what we need it to!


By carefully integrating the new methods into the exploit, we can get rid of all the unwanted allocations in the heap spray memory area. The diagram depicting the updated infoleak spray looks as follows:



Now, in the worst case, we’ll overwrite the LSB of the WebSocketFrame pointer with the same value, which will have no effect. This gives us 7/8 instead of 2/8 as the first multiplier of our "reliability" formula. The same applies with regard to other parts of the exploit. As a result, the above total probability should be bumped up to 0.75 per run.


Again, this method comes with several limitations, for example:

- The number of cookies a website can have is capped at 180 in Chrome.
- Every 512th cookie-related operation triggers flushing the in-memory cookie store to the disk, which ruins any heap spray.
- There’s also an automatic flushing every 30 seconds.
- The cookie store for our website should be in a particular state before each run of the spray, otherwise the manipulation methods might produce unreliable results.


Luckily, our exploit can be designed to deal with most of the above restrictions automatically. The heap spray has to be split into tiny chunks, which can be processed separately, though. Because of that, and because we’ve reached the limit of the spray size tied to the maximum number of connected WebSockets, the actual exploit ends up to be less reliable. However, paired with the ability to restart the network process, it seems to usually take only 2-3 tries before succeeding, which is a whole lot better than the previous version.

## Chapter 6. Conclusion

The servicification work that Chrome has been doing has had several interesting impacts on exploitation of this kind of bug. First, moving this code into a separate service process (the network service) has had a substantial impact on the difficulty of finding reliable heap-grooming primitives. This means that even without a proper sandbox, the network service implementation in Chrome means that the network stack is now a slightly harder target than it was before! Service processes implementing a relatively small number of features are inherently harder targets for exploitation than larger monolithic components; they have a reduced number of available weird-machines, and this reduces attacker choice. We hadn’t really thought about this, so this was an interesting surprise.


Second (and this is definitely a recurring theme at the moment), restarting service processes aids exploitation. For an exploit developer, knowing that you can have as many tries as you need takes a lot of pressure off — you have a lot more freedom to create and use unreliable primitives. This is even more true on platforms that don’t have per-process randomness — we chose Linux for this so that we’d need to construct a stable infoleak — on other platforms exploitation may be easier.

Given the additional complexity and reliability concerns, it doesn’t seem very likely that this kind of bug is being used by attackers at the moment. The "traditional" browser exploitation chain of a renderer bug and an OS/kernel privilege escalation is both simpler to write and easier to maintain. However, it’s not unrealistic to think that if those chains start to become scarce, attackers might move to this kind of vulnerability — and we’ve demonstrated that it’s possible to exploit such an issue with a reasonable level of reliability. This means that sandboxing even of these less-visible attack surfaces is also important to the overall security of the browser.
