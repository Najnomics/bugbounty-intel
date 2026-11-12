# When ‘int’ is the new ‘short’ - Project Zero

Source: https://projectzero.google/2015/07/when-int-is-new-short.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Mark Brand, Truncator of Integers


This is going to be a quick post, just describing a particularly interesting Chrome issue that I found last month; how I found it; and what is interesting about it…

I was looking through some Chrome networking code; and I noticed an interesting API design choice that piqued my interest; the IOBuffer interface. These are used throughout the networking stack to manage buffer lifetimes; and there are few things that are interesting about them:


class NET\_EXPORT IOBuffer : public base::RefCountedThreadSafe\<IOBuffer> {

public:

IOBuffer();

explicit IOBuffer(int buffer\_size);


char\* data() { return data\_; }


protected:

friend class base::RefCountedThreadSafe\<IOBuffer>;


// Only allow derived classes to specify data\_.

// In all other cases, we own data\_, and must delete it at destruction time.

explicit IOBuffer(char\* data);


virtual \~IOBuffer();


char\* data\_;

};


So, there are several questions that I immediately want to ask about the design of this interface; but we’ll stay on track for the question that will lead us to the bug. Why does the constructor takes an int for the buffer\_size parameter?


Why is this interesting? There are perhaps too many integer types in C/C++; and the misuse of them is a common cause of vulnerabilities. The language has a specific type for representing the sizes of objects; this is size\_t, and it’s perhaps relevant to quote the C standard here:


‘The types used for size\_t and ptrdiff\_t should not have an integer conversion rank greater than that of signed long int unless the implementation supports objects large enough to make this necessary’


I assume that this recommendation was made precisely to prevent this kind of issue from occurring; having int and size\_t be compatible types would make things safer for programmers that have been taught that int is always the correct numerical type to use. For completeness sake; I’ll note that the other issue would be one of signedness; size\_t is required to be an unsigned type; and this means that the range of size\_t and int is not the same, even on systems where they have the same bit-width; however, the case of integer overflow resulting in a negative length is handled correctly in the IOBuffer constructor.


Now; on x86\_64, with gcc and clang an int is still a 32-bit integer type; but as we can have allocations over the 2^32 limit, size\_t is necessarily a 64-bit integer type, and so in any location where we use a size\_t type to initialise an IOBuffer instance, we risk truncating the size and allocating a smaller buffer than we expect. It turns out that in content::CertificateResourceHandler, which handles the mime-type ‘application/x-x509-user-cert’, that is exactly what’s going to happen. This is quite a simple class, which simply stores chunks of a certificate in an internal list as they are received, totals the length and then reassembles those chunks.


bool CertificateResourceHandler::OnReadCompleted(int bytes\_read, bool\* defer) {

if (!bytes\_read)

return true;


// We have more data to read.

DCHECK(read\_buffer\_.get());

content\_length\_ += bytes\_read;


// Release the ownership of the buffer, and store a reference

// to it. A new one will be allocated in OnWillRead().

scoped\_refptr\<net::IOBuffer> buffer;

read\_buffer\_.swap(buffer);

// TODO(gauravsh): Should this be handled by a separate thread?

buffer\_.push\_back(std::make\_pair(buffer, bytes\_read));


return true;

}


We’re summing the length in a member variable, content\_length\_ (which is of type ‘size\_t’), and then we later encounter the discussed integer truncation issue when we come to put the pieces back together.


void CertificateResourceHandler::AssembleResource() {

// 0-length IOBuffers are not allowed.

if (content\_length\_ == 0) {

resource\_buffer\_ = NULL;

return;

}


// Create the new buffer.

resource\_buffer\_ = new net::IOBuffer(content\_length\_); // allocation truncated


// Copy the data into it.

size\_t bytes\_copied = 0;

for (size\_t i = 0; i \< buffer\_.size(); ++i) {

net::IOBuffer\* data = buffer\_\[i\].first.get();

size\_t data\_len = buffer\_\[i\].second;

DCHECK(data != NULL);

DCHECK\_LE(bytes\_copied + data\_len, content\_length\_);

memcpy(resource\_buffer\_->data() + bytes\_copied, data->data(), data\_len); // heap corruption will occur here

bytes\_copied += data\_len;

}

DCHECK\_EQ(content\_length\_, bytes\_copied);

}


So, we can serve up a certificate with a ridiculously long length, for example 0x100001000 bytes, and once this has all made it down the HTTP pipe to Chrome, we’ll try to copy those many, many bytes into a buffer of (int)0x100001000 bytes.


Truncation will happen like this:

size\_t 00000001 00001000

int             00001000


And it’s pretty easy to see that bad things are now going to happen. See the [tracker](https://code.google.com/p/google-security-research/issues/detail?id=364) for a crash PoC.


Now, the more astute reader will point out that I just sent over 4 gigabytes of data over the internet; and that this can’t really be all that interesting - but that argument is readily countered with gzip encoding, reducing the required data to a 4 megabyte payload. Of course, you do need to wait a little while for Chrome to perform the gzip deflation; something like 30 seconds for me; but this is not a major issue as this is taking place in a background thread in the browser process, and will not really be noticeable, except for high processor usage.


And that leads us to probably the most interesting thing about this bug. This is taking place in the browser process; for those not familiar with the Chrome sandbox model; [http://blog.azimuthsecurity.com/2010/05/chrome-sandbox-part-1-of-3-overview.html](http://blog.azimuthsecurity.com/2010/05/chrome-sandbox-part-1-of-3-overview.html) is a nice introduction. The browser process is the trusted, unsandboxed process; making this bug a single-bug full compromise issue, potentially resulting in unsandboxed arbitrary code execution from a drive-by with a single bug.


This is a little bit scary; considering that typical pwnium entries consist of quite [lengthy](http://blog.chromium.org/2012/05/tale-of-two-pwnies-part-1.html) and [convoluted](http://blog.chromium.org/2012/06/tale-of-two-pwnies-part-2.html) bug chains. It just serves to highlight the importance of minimizing the unsandboxed attack surface.

It’s going to be a difficult issue to exploit; even on a 64-bit system, surviving a 4-gigabyte out-of-bounds memcpy is a nontrivial problem. To make things worse, the browser process is interacted with frequently by all the live renderer processes; so achieving determinism from the heap is going to be a serious challenge; but as in [this Safari exploit](/2014/07/pwn4fun-spring-2014-safari-part-i_24.html); if stable exploitation is possible, the first step is likely going to be to manage to arrange for the heap corruption caused by the overflow to corrupt the buffer\_ vector, so that we can control the size of the overflow.
