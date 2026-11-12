# A day^W^W Several months in the life of Project Zero - Part 1: The Chrome bug of suffering - Project Zero

Source: https://projectzero.google/2020/02/several-months-in-life-of-part1.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Sergei Glazunov and Mark Brand, Project Zero

## Introduction

It was a normal week in the Project Zero office when we got an interesting email from the Chrome team — they’d been looking into a serious crash that was happening occasionally on Android builds of Chrome, but hadn’t made much progress. The same crash had then briefly reproduced on [ClusterFuzz](https://google.github.io/clusterfuzz/); with a test-case which referenced an external website — but it wasn’t reproducing any more, and it seemed likely that the next step was going to be to wait until the bug started reproducing again.

We took a quick look at the details they had, and decided that this issue looked important enough for us to spend some time helping the Chrome team to figure out what was happening. A large part of our motivation here came from the concern that perhaps this external website was intentionally triggering a vulnerable code path (spoiler alert: it wasn’t). The issue also looked to be readily exploitable — the ASAN trace that we had showed an out-of-bounds heap write with what was likely data read from the network. 


Although the networking code in Chrome has been split out into a new service process, the implementation of strict sandboxing for that process isn’t completed yet, so it’s still a highly privileged attack surface. This means that this bug alone would be enough to both get initial code execution, and to break out of the Chrome sandbox.

We’re writing this blog post mini-series to illustrate the difficulties that even experienced researchers sometimes face when trying to understand a vulnerability in a complex piece of code. This story in particular has a happy ending, and we were able to help the Chrome team to find and fix the issue, but hopefully the reader will also see that persistence perhaps played more of a part here than wizardry.

## Chapter 1: The Test-case

So we have the following rather simple test-case:

\<script>

window.open("http://example.com");

window.location = "http://example.net";\</script>

Observant readers will no doubt notice that this is a pretty, well, boring output for a fuzzer — all this is doing is loading a couple of webpages! Perhaps this is a good simulation of user behaviour, and this kind of test-case is perhaps a good way to shake out network-stack bugs?

According to the thread, this had now stopped reproducing, so all we had was the ASAN backtrace from when ClusterFuzz first triggered the issue:

=================================================================

==12590==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x8e389bf1 at pc 0xec0defe8 bp 0x90e93960 sp 0x90e93538

WRITE of size 3848 at 0x8e389bf1 thread T598 (NetworkService)

#0 0xec0defe4 in \_\_asan\_memcpy

#1 0xa0d1433a in net::SpdyReadQueue::Dequeue(char\*, unsigned int) net/spdy/spdy\_read\_queue.cc:43:5

#2 0xa0d17c24 in net::SpdyHttpStream::DoBufferedReadCallback() net/spdy/spdy\_http\_stream.cc:637:30

#3 0x9f39be54 in base::internal::CallbackBase::polymorphic\_invoke() const base/callback\_internal.h:161:25

#4 0x9f39be54 in base::OnceCallback\<void ()>::Run() && base/callback.h:97

#5 0x9f39be54 in base::TaskAnnotator::RunTask(char const\*, base::PendingTask\*) base/task/common/task\_annotator.cc:142

...

#17 0xea222ff6 in \_\_start\_thread bionic/libc/bionic/clone.cpp:52:16

0x8e389bf1 is located 0 bytes to the right of 1-byte region \[0x8e389bf0,0x8e389bf1)

allocated by thread T598 (NetworkService) here:

#0 0xec0ed42c in operator new\[\](unsigned int)

#1 0xa0d52b78 in net::IOBuffer::IOBuffer(int) net/base/io\_buffer.cc:33:11

Thread T598 (NetworkService) created by T0 (oid.apps.chrome) here:

#0 0xec0cb4e0 in pthread\_create

#1 0x9bfbbc9a in base::(anonymous namespace)::CreateThread(unsigned int, bool, base::PlatformThread::Delegate\*, base::PlatformThreadHandle\*, base::ThreadPriority) base/threading/platform\_thread\_posix.cc:120:13

#2 0x95a07c18 in \_\_cxa\_finalize

SUMMARY: AddressSanitizer: heap-buffer-overflow (/system/lib/libclang\_rt.asan-arm-android.so+0x93fe4)

Shadow bytes around the buggy address:

0xdae49320: fa fa 04 fa fa fa fd fa fa fa fd fa fa fa fd fa

0xdae49330: fa fa 00 04 fa fa 00 fa fa fa 00 fa fa fa fd fd

0xdae49340: fa fa fd fd fa fa fd fa fa fa fd fd fa fa fd fa

0xdae49350: fa fa fd fd fa fa fd fd fa fa fd fd fa fa fd fd

0xdae49360: fa fa fd fd fa fa fd fa fa fa fd fd fa fa fd fd

=>0xdae49370: fa fa fd fd fa fa fd fd fa fa fd fa fa fa\[01\]fa

0xdae49380: fa fa fd fa fa fa fd fa fa fa fd fd fa fa fd fd

0xdae49390: fa fa fd fd fa fa fd fd fa fa fd fd fa fa fd fd

0xdae493a0: fa fa fd fd fa fa fd fa fa fa 00 fa fa fa 04 fa

0xdae493b0: fa fa 00 fa fa fa 04 fa fa fa 00 00 fa fa 00 fa

0xdae493c0: fa fa 00 fa fa fa 00 fa fa fa 00 fa fa fa 00 fa

Shadow byte legend (one shadow byte represents 8 application bytes):

Addressable:00

Partially addressable: 01 02 03 04 05 06 07

Heap left redzone:       fa

Freed heap region:       fd

Stack left redzone:      f1

Stack mid redzone:       f2

Stack right redzone:     f3

Stack after return:      f5

Stack use after scope:   f8

Global redzone:          f9

Global init order:       f6

Poisoned by user:        f7

Container overflow:      fc

Array cookie:            ac

Intra object redzone:    bb

ASan internal:           fe

Left alloca redzone:     ca

Right alloca redzone:    cb

Shadow gap:              cc

==12590==ABORTING

This looks like a really serious bug; it’s a heap-buffer-overflow writing data that likely comes directly from the network. We didn’t, however, have a development environment for Chrome on Android available, so we decided to try and find the root cause ourselves, figuring that it couldn’t be too hard to find a place where the size of an IOBuffer gets confused.

## Chapter 2: HttpCache::Transaction

Since the bug was no longer reproducing on ClusterFuzz, we initially assumed that something had changed in the webserver or network configuration, and started looking into the code.

Tracking back where the IOBuffer being written to in SpdyHttpStream::DoBufferedReadCallback comes from, we’re likely looking for a call site of HttpNetworkTransaction::Read where the size of the IOBuffer passed as the parameter buf doesn’t match the length passed as buf\_len. There aren’t all that many call sites; but none of them looked immediately wrong, and we spent a few days going back and forth with hopeless theories.

Perhaps our first mistake was to then start trying to collect more information on the bug by investigating in Chrome’s crash dump repository — it turns out that there are quite a few crashes with similar stack-traces that we simply couldn’t explain — and that didn’t help to explain this bug! After perhaps a week of investigation we had a huge collection of related crashes and had made no progress at all towards finding the root cause of this issue.

We were getting increasingly close to giving up in frustration when we found the following [line of code](https://chromium.googlesource.com/chromium/src/+/6199b09d49207616849f69d912e0d68005c3b28b/net/http/http_cache_transaction.cc#3082) in HttpCache::Transaction::WriteResponseInfoToEntry (which we must both have skimmed past multiple times by this point… and for some reason not noticed):

// When writing headers, we normally only write the non-transient headers.

bool skip\_transient\_headers = true;

scoped\_refptr\<PickledIOBuffer> data(new PickledIOBuffer());

response.Persist(data->pickle(), skip\_transient\_headers, truncated);

data->Done();

io\_buf\_len\_ = data->pickle()->size();

// Summarize some info on cacheability in memory. Don’t do it if doomed

// since then |entry\_| isn’t definitive for |cache\_key\_|.

if (!entry\_->doomed) {

cache\_->GetCurrentBackend()->SetEntryInMemoryData(

cache\_key\_, ComputeUnusablePerCachingHeaders()

? HINT\_UNUSABLE\_PER\_CACHING\_HEADERS

: 0);

}

This looks highly suspicious; in other locations in the same file, there is a clear expectation that io\_buf\_len\_ matches the size of the IOBuffer read\_buf\_; and indeed, this assumption is used in a call that would lead to a Read call:

int HttpCache::Transaction::DoNetworkReadCacheWrite() {

TRACE\_EVENT0("io", "HttpCacheTransaction::DoNetworkReadCacheWrite");

DCHECK(InWriters());

TransitionToState(STATE\_NETWORK\_READ\_CACHE\_WRITE\_COMPLETE);

return entry\_->writers->Read(read\_buf\_, io\_buf\_len\_, io\_callback\_, this);

}

It certainly matched everything we knew about the bug, and at this point seemed by far and away the best lead we had — but it’s not trivial to reach this code in an interesting way. The HTTP cache implements a state machine with \~50 different states! This state machine is usually run twice during a request; once when the request is started ([HttpCache::Transaction::Start](https://chromium.googlesource.com/chromium/src/+/6199b09d49207616849f69d912e0d68005c3b28b/net/http/http_cache_transaction.cc#230)) and again when reading the response data ([HttpCache::Transaction::Read](https://chromium.googlesource.com/chromium/src/+/6199b09d49207616849f69d912e0d68005c3b28b/net/http/http_cache_transaction.cc#328)). In order to reach this bug, we’d need a loop in the state transitions that could take us from one of the Read states, back into a state that can call WriteResponseInfoToEntry and transition back into reading the data without updating the read\_buf\_ pointer; so we’re focussed on the second run of this state machine; that is, the states that are reachable from the Read call.

WriteResponseInfoToEntry has 4 call sites, all in state handlers:

DoCacheWriteUpdatedPrefetchResponse

DoCacheUpdateStaleWhileRevalidateTimeout

DoCacheWriteUpdatedResponse

DoCacheWriteResponse

We need to first establish whether there’s a transition path from HttpCache::Transaction::Read into each of these states, since otherwise we won’t have a previous value for read\_buf\_ and io\_buf\_len\_.

Since it’s a bit difficult to reason about the state machine transitions by looking at the code, we’ve prepared a graph approximating the state machine, which will make it clear and simple for the reader to understand.


It would have been sensible to do this initially; but we originally just manually performed a depth-first-search of the state machine in the source code, which was error-prone and confusing.

[The four states marked in yellow are the states which could alter the value of io\_buf\_len\_; the states which would then use this corrupted io\_buf\_len\_ value are the three child states of TransitionToReadingState: CACHE\_READ\_DATA, NETWORK\_READ, and NETWORK\_READ\_CACHE\_WRITE, which are marked in green.](/images/oldblog/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjBMf_s1307_Q_ZLoJ0bKfCVByQKvwrcXFYt3pUX9GUJLxpRAIz7ULstT_4AtgNSLFy6RRrNt0tyjfDSBHf15R1InMVcLggmuhdY8HqLZZQ1Y6dr8Y8zhWw2EPztWY1aJOhoc2PTCKNjDFKO3U43.png)

We can first eliminate TOGGLE\_UNUSED\_SINCE\_PREFETCH, since this should only be reached on the first request sent after a prefetch — and in the case of a matching cache entry, this request will happen during Start rather than potentially during Read.

We can also eliminate CACHE\_WRITE\_UPDATED\_RESPONSE, since this transition can only be reached if we’re not in a reading state:

int HttpCache::Transaction::DoUpdateCachedResponse() {

TRACE\_EVENT0("io", "HttpCacheTransaction::DoUpdateCachedResponse");

int rv = OK;

// Update the cached response based on the headers and properties of

// new\_response\_.

response\_.headers->Update(\*new\_response\_->headers.get());

response\_.stale\_revalidate\_timeout = base::Time();

response\_.response\_time = new\_response\_->response\_time;

response\_.request\_time = new\_response\_->request\_time;

response\_.network\_accessed = new\_response\_->network\_accessed;

response\_.unused\_since\_prefetch = new\_response\_->unused\_since\_prefetch;

response\_.ssl\_info = new\_response\_->ssl\_info;

if (new\_response\_->vary\_data.is\_valid()) {

response\_.vary\_data = new\_response\_->vary\_data;

} else if (response\_.vary\_data.is\_valid()) {

// There is a vary header in the stored response but not in the current one.

// Update the data with the new request headers.

HttpVaryData new\_vary\_data;

new\_vary\_data.Init(\*request\_, \*response\_.headers.get());

response\_.vary\_data = new\_vary\_data;

}

if (response\_.headers->HasHeaderValue("cache-control", "no-store")) {

if (!entry\_->doomed) {

int ret = cache\_->DoomEntry(cache\_key\_, nullptr);

DCHECK\_EQ(OK, ret);

}

TransitionToState(STATE\_UPDATE\_CACHED\_RESPONSE\_COMPLETE);

} else {

// If we are already reading, we already updated the headers for this

// request; doing it again will change Content-Length.

if (!reading\_) {

TransitionToState(STATE\_CACHE\_WRITE\_UPDATED\_RESPONSE);

rv = OK;

} else {

TransitionToState(STATE\_UPDATE\_CACHED\_RESPONSE\_COMPLETE);

}

}

return rv;

}

This leaves us with two possible states that could trigger the bug; CACHE\_UPDATE\_STALE\_WHILE\_REVALIDATE\_TIMEOUT and CACHE\_WRITE\_RESPONSE, so let’s take a look at the transitions back to TransitionToReadingState and see how we can join those up. There’s only one backwards edge to TransitionToReadingState, and that comes from [FINISH\_HEADERS\_COMPLETE](https://chromium.googlesource.com/chromium/src/+/6199b09d49207616849f69d912e0d68005c3b28b/net/http/http_cache_transaction.cc#2121):

// If already reading, that means it is a partial request coming back to the

// headers phase, continue to the appropriate reading state.

if (reading\_) {

int rv = TransitionToReadingState();

DCHECK\_EQ(OK, rv);

return OK;

}

Since we expect reading\_ to be set at this point (it’s set in Read, and should never be cleared), this looks fine. However, looking back at the graph, in all of the normal cases we should actually never visit most of the states in this graph — in order to reach GET\_BACKEND or START\_PARTIAL\_CACHE\_VALIDATION, we need to go through DoPartialCacheReadCompleted or DoPartialNetworkReadCompleted and reach one of the following transitions:

int HttpCache::Transaction::DoPartialCacheReadCompleted(int result) {

partial\_->OnCacheReadCompleted(result);

if (result == 0 && mode\_ == READ\_WRITE) {

// We need to move on to the next range.

TransitionToState(STATE\_START\_PARTIAL\_CACHE\_VALIDATION);

} else if (result \< 0) {

return OnCacheReadError(result, false);

} else {

TransitionToState(STATE\_NONE);

}

return result;

}

int HttpCache::Transaction::DoPartialNetworkReadCompleted(int result) {

DCHECK(partial\_);

// Go to the next range if nothing returned or return the result.

// TODO(shivanisha) Simplify this condition if possible. It was introduced

// in https://codereview.chromium.org/545101

if (result != 0 || truncated\_ ||

!(partial\_->IsLastRange() || mode\_ == WRITE)) {

partial\_->OnNetworkReadCompleted(result);

if (result == 0) {

// We need to move on to the next range.

if (network\_trans\_) {

ResetNetworkTransaction();

} else if (InWriters() && entry\_->writers->network\_transaction()) {

SaveNetworkTransactionInfo(\*(entry\_->writers->network\_transaction()));

entry\_->writers->ResetNetworkTransaction();

}

TransitionToState(STATE\_START\_PARTIAL\_CACHE\_VALIDATION);

} else {

TransitionToState(STATE\_NONE);

}

return result;

}

// Request completed.

if (result == 0) {

DoneWithEntry(true);

}

TransitionToState(STATE\_NONE);

return result;

}


Our exact chain of thought during the initial investigation has been lost to the sands of time, but we’d made it past this point, and got stuck in the mud trying to find a working path through [this code,](https://chromium.googlesource.com/chromium/src/+/6199b09d49207616849f69d912e0d68005c3b28b/net/http/http_cache_transaction.cc#2460) which handles the cache entry validation for partial entries. We need to cause a pathological case, in which the cache responds to a full request with a previous, partial request in the cache; and then we need to cause the revalidation of that previous partial request to fail. Unfortunately, the ways that we tried to cause the browser to send partial requests all failed to trigger the interesting code paths.

Regardless, it seemed clear that the code was buggy, and so we suggested an interim fix to Chrome to add a CHECK ensuring that if this state-transition loop was occurring, it would no longer be an exploitable vulnerability.

## Chapter 3: It lives!

Initially we’d all assumed that since the relevant code hadn’t changed, and the test-case referenced external servers, there had been a change on the server side that had stopped the issue from reproducing. However, at around the same time as we provided the information from our initial investigation, one of the Chrome developers working on the issue discovered that they could still reproduce the issue on Android using exactly the same Chromium revision as in the original ClusterFuzz report!

The reason that the bug had stopped reproducing on Android appeared to be that an unrelated change had influenced scheduling enough to prevent the issue from triggering. It was bad luck that this change landed just after ClusterFuzz first encountered this issue. This was a major face-palm moment for us, since it was a very low effort thing to try, and we’d just been too lazy to set up a build environment to check for ourselves... We applied the CHECK, and tested again, and sure enough the CHECK fired!

At this point, we were questioning our decision-making process more thoroughly, and immediately tried reproducing with the same version on a Linux build. I think you, the reader, can imagine how we felt when the issue also reproduced locally with an ASAN Linux build…

It appeared that the culprit was a single image on the website being visited, that was being loaded with the loading=lazy attribute. This feature had just been enabled in stable desktop Chrome — and had been active already on Android. A minimized illustration of the requests made by the browser are as follows:

GET /image.bmp HTTP/1.1                                                            (1)

Accept-Encoding: identity

Range: bytes=0-2047


HTTP/1.1 206 Partial Content

Content-Length: 2048

Content-Range: bytes 0-2047/9999

Last-Modified: 2019-01-01

Vary: Range

GET /image.bmp HTTP/1.1 (2)

Accept-Encoding: gzip, deflate, br

If-Modified-Since: 2019-01-01

Range: bytes=0-2047

HTTP/1.1 304 Not Modified

Content-Length: 2048

Content-Range: bytes 0-2047/9999

Last-Modified: 2019-01-01

Vary: Range

GET /image.bmp HTTP/1.1                                                            (3)

Accept-Encoding: gzip, deflate, br

HTTP/1.1 200 OK

Content-Length: 9999

Trivialising a reasonable amount of confusion and tampering, we were able to reduce the trigger to exactly the above sequence of request-responses. What does this tell us?

Using [Chrome’s tracing](https://www.chromium.org/developers/how-tos/trace-event-profiling-tool), we can see the paths taken through the state machine; and that there are actually two HttpCache::Transaction objects involved in this trigger. The first request, comes from the first transaction; which reads the first 2048 bytes and stores those in the cache. The second and third requests then come from the second transaction — which is requesting the full data. Since there is an existing cache entry for the URL, it first validates that the cache entry is valid, by sending the second request.

Since the entry is valid, the transaction will then start reading — entering the read state as though it’s reading the complete response from cache. However, since our cache entry is incomplete, we’ll then need to make the third request to retrieve the rest of the response data. It’s in the handling of this third request that we encounter the dangerous state-transition. This occurs when the browser attempts to determine how to validate the response from the server for the second part of the data, which would require sending a different Range header, and would therefore break the Vary constraint imposed by the server. Since the server didn’t provide a strong validation mechanism (like Etag), the browser can’t be sure that it isn’t splicing together parts of two completely different responses, so it has to restart the request from the start; but it’s already returned response headers to the calling code — so it tries to do this transparently without exiting the state machine; and this triggers the vulnerability.

Note that latency plays a role here — if it takes too long for the response from the first request to reach the browser, then the second request will start from scratch instead of performing cache validation, and the vulnerability won’t be triggered. If you’re trying to test this with a (distant) remote server, there are some modifications that need to be made to maintain the correct ordering — this is left as an exercise for the motivated reader.

The following animation shows the state-transitions followed while performing the Read from the second transaction:



There are a few things that we need to note for the purposes of exploiting this bug; in order to get into the state where we can loop back within the Read call without exiting the state machine, we needed to trigger the call to DoRestartPartialRequest. This will doom the current cache entry, and truncate the stored response data. This means that when we reach CACHE\_READ\_RESPONSE, we don’t have any control over the values used here:

int HttpCache::Transaction::DoCacheReadResponse() {

TRACE\_EVENT0("io", "HttpCacheTransaction::DoCacheReadResponse");

DCHECK(entry\_);

TransitionToState(STATE\_CACHE\_READ\_RESPONSE\_COMPLETE);

io\_buf\_len\_ = entry\_->disk\_entry->GetDataSize(kResponseInfoIndex);

read\_buf\_ = base::MakeRefCounted\<IOBuffer>(io\_buf\_len\_);

net\_log\_.BeginEvent(NetLogEventType::HTTP\_CACHE\_READ\_INFO);

return entry\_->disk\_entry->ReadData(kResponseInfoIndex, 0, read\_buf\_.get(),

io\_buf\_len\_, io\_callback\_);

}

In fact, since the entry has been truncated, io\_buf\_len\_ will always be 0.

On the other hand, we do have more-or-less complete control over  the value set during  CACHE\_WRITE\_RESPONSE in the call to WriteResponseInfoToEntry:

// When writing headers, we normally only write the non-transient headers.

bool skip\_transient\_headers = true;

scoped\_refptr\<PickledIOBuffer> data(new PickledIOBuffer());

response\_.Persist(data->pickle(), skip\_transient\_headers, truncated);

data->Done();

io\_buf\_len\_ = data->pickle()->size();

And as mentioned earlier, the out-of-bounds write will then happen later when this now-incorrect length is used to read the response data from the network. Although the length used will be the size of the non-transient headers, there will only be as many bytes written as the server returns in the response body, so we can write the precise number of bytes that we wish, giving us quite a controlled memory-corruption primitive to exploit.

## Conclusion

There are a few takeaways from the bug here — these might not be new to you, but they’re probably worth reiterating:

- Code that uses one variable for two meanings is bad. Even if the code is initially "correct" when written, it’s unlikely to stay correct during future iterations!
- C-style programming in C++ is also a bad sign; the IOBuffer design pattern with separate storage of buffers and their sizes is inherently dangerous.

Looking at the state machine code itself, there’s a lot of complexity there. Perhaps that code could have been designed differently to reduce the complexity; but this is also code that’s evolved as the HTTP protocol has evolved, and a rewrite now would likely introduce different complexity and different bugs.

What will happen next when we try to exploit this bug? Check out [Part 2](/2020/02/several-months-in-life-of-part2.html) to continue our escapade.
