# Adventures in Video Conferencing Part 3: The Even Wilder World of WhatsApp - Project Zero

Source: https://projectzero.google/2018/12/adventures-in-video-conferencing-part-3.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Natalie Silvanovich, Project Zero

WhatsApp is another application that supports video conferencing that does not use WebRTC as its core implementation. Instead, it uses [PJSIP](https://www.pjsip.org/), which contains some WebRTC code, but also contains a substantial amount of other code, and predates the WebRTC project. I fuzzed this implementation to see if it had similar results to WebRTC and FaceTime.

# Fuzzing Set-up

PJSIP is open source, so it was easy to identify the PJSIP code in the Android WhatsApp binary (libwhatsapp.so). Since PJSIP uses the open source library [libsrtp](https://github.com/cisco/libsrtp), I started off by opening the binary in IDA and searching for the string srtp\_protect, the name of the function libsrtp uses for encryption. This led to a log entry emitted by a function that looked like srtp\_protect. There was only one function in the binary that called this function, and called memcpy soon before the call. Some log entries before the call contained the file name srtp\_transport.c, which exists in the PJSIP [repository](http://svn.pjsip.org/repos/pjproject/tags/1.2/pjmedia/src/pjmedia/transport_srtp.c). The log entries in the WhatsApp binary say that the function being called is transport\_send\_rtp2 and the PJSIP source only has a function called transport\_send\_rtp, but it looks similar to the function calling srtp\_protect in WhatsApp, in that it has the same number of calls before and after the memcpy. Assuming that the code in WhatsApp is some variation of that code, the memcpy copies the entire unencrypted packet right before it is encrypted.


Hooking this memcpy seemed like a possible way to fuzz WhatsApp video calling. I started off by hooking memcpy for the entire app using a tool called [Frida](https://www.frida.re/docs/android/). This tool can easily hook native function in Android applications, and I was able to see calls to memcpy from WhatsApp within minutes. Unfortunately though, video conferencing is very performance sensitive, and a delay sending video packets actually influences the contents of the next packet, so hooking every memcpy call didn’t seem practical. Instead, I decided to change the single memcpy to point to a function I wrote.


I started off by writing a function in assembly that loaded a library from the filesystem using dlopen, retrieved a symbol by calling dlsym and then called into the library. Frida was very useful in debugging this, as it could hook calls to dlopen and dlsym to make sure they were being called correctly. I overwrote a function in the WhatsApp GIF transcoder with this function, as it is only used in sending text messages, which I didn’t plan to do with this altered version. I then set the memcpy call to point to this function instead of memcpy, using this online ARM branch [finder](http://armconverter.com/branchfinder/).


| sub\_2F8CC MOV             X21, X30 MOV             X22, X0 MOV             X23, X1 MOV             X20, X2 MOV             X1, #1 ADRP            X0, #aDataDataCom\_wh@PAGE ; "/data/data/com.whatsapp/libn.so" ADD             X0, X0, #aDataDataCom\_wh@PAGEOFF ; "/data/data/com.whatsapp/libn.so" BL              .dlopen ADRP            X1, #aApthread@PAGE ; "apthread" ADD             X1, X1, #aApthread@PAGEOFF ; "apthread" BL              .dlsym MOV             X8, X0 MOV             X0, X22 MOV             X1, X23 MOV             X2, X20 NOP BLR             X8 MOV             X30, X21 RET | 

The library loading function


I then wrote a library for Android which had the same parameters as memcpy, but fuzzed and copied the buffer instead of just copying it, and put it on the filesystem where it would be loaded by dlopen. I then tried making a WhatsApp call with this setup. The video call looked like it was being fuzzed and crashed in roughly fifteen minutes.

# Replay Set-up


To replay the packets I added logging to the library, so that each buffer that was altered would also be saved to a file. Then I created a second library that copied the logged packets into the buffer being copied instead of altering it. This required modifying the WhatsApp binary slightly, because the logged packet will usually not be the same size as the packet currently being sent. I changed the length of the hooked memcpy to be passed by reference instead of by value, and then had the library change the length to the length of the logged packet. This changed the value of the length so that it would be correct for the call to srtp\_protect. Luckily, the buffer that the packet is copied into is a fixed length, so there is no concern that a valid packet will overflow the buffer length. This is a common design pattern in RTP processing that improves performance by reducing length checks. It was also helpful in modifying FaceTime to replay packets of varying length, as described in the previous post.


This initial replay setup did not work, and looking at the logged packets, it turned out that WhatsApp uses four streams with different SSRCs for video conferencing (possibly one for video, one for audio, one for synchronization and one for good luck). The streams each had only one payload type, and they were all different, so it was fairly easy to map each SSRC to its stream. So I modified the replay library to determine the current SSRC for each stream based on the payload types of incoming packets, and then to replace the SSRC of the replayed packets with the correct one based on their payload type. This reliably replayed a WhatsApp call. I was then able to fuzz and reproduce crashes on WhatsApp.

# Results

Using this setup, I reported one heap corruption [issue](https://bugs.chromium.org/p/project-zero/issues/detail?id=1654) on WhatsApp, CVE-2018-6344. This issue has since been fixed. After this issue was resolved, fuzzing did not yield any additional crashes with security impact, and we moved on to other methodologies. Part 4 will describe our other (unsuccessful) attempts to find vulnerabilities in WhatsApp.
