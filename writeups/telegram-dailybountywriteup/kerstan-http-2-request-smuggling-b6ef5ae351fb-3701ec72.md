# http 2 request smuggling b6ef5ae351fb

- **Source URL:** https://medium.com/@kerstan/http-2-request-smuggling-b6ef5ae351fb?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240109125419/https://medium.com/@kerstan/http-2-request-smuggling-b6ef5ae351fb
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4725 (id 4725)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Subscribed to:** [https://medium.com/@kerstan](/@kerstan)

This is a detailed introduction to HTTP/2 Request Smuggling and various methods of exploiting vulnerabilities. The case study uses PortSwigger Lab. Although the writing is lengthy, if you manage to read it in its entirety, I believe it will greatly aid your understanding of HTTP/2 Request Smuggling.

Try hard bro :)

# 1. [HTTP/2](https://tttang.com/archive/1837/#toc_http2)

Let us delve into the variances between HTTP/2 and HTTP/1 from three distinct perspectives.

## 1.1 Binary Transmission

Primarily, the initial distinction lies in the realm of binary transmission. Unlike the pure textual format of message transfer in HTTP/1, HTTP/2 partitions request and response data into smaller frames, facilitating binary encoding for transmission. The crux of all performance enhancements in HTTP/2 resides within its novel binary framing layer, which delineates the encapsulation of HTTP messages and their transmission between clients and servers.

## 1.2 Header Compression

As depicted in the aforementioned diagram, a notable disparity between HTTP/1 and HTTP/2 lies in the structure of their requests. In HTTP/2, the request message is substituted with a sequence of pseudo headers, adhering to the following format:

```
:method - The request method
:path - The request path. Note that this includes the query string
:authority - The Host header, roughly
:scheme - The request scheme, typically 'http' or 'https'
:status - The response status code - not used in requests
```
PS:

1. This representation is solely applicable within the Burp Inspector and does not reflect the actual format during network transmission.

2. Employing this approach facilitates the elucidation of vulnerability principles.

## 1.3 Message Length

Lastly, let us consider the disparity in message length. Due to the binary nature of transmission, the length of HTTP request messages has been adjusted. In HTTP/1, the determination of the end of a request header name necessitates a search for the colon (:) character. However, in HTTP/2, parsing is conducted based on predefined offsets…
