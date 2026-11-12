# Adventures in Video Conferencing Part 2: Fun with FaceTime - Project Zero

Source: https://projectzero.google/2018/12/adventures-in-video-conferencing-part-2.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Natalie Silvanovich, Project Zero

FaceTime is Apple’s video conferencing application for iOS and Mac. It is closed source, and does not appear to use any third-party libraries for its core functionality. I wondered whether fuzzing the contents of FaceTime’s audio and video streams would lead to similar results as WebRTC.

# Fuzzing Set-up


Philipp Hancke performed an excellent [analysis](https://webrtchacks.com/facetime-decode/) of FaceTime’s architecture in 2015. It is similar to WebRTC, in that it exchanges signalling information in SDP format and then uses RTP for audio and video streams. Looking at the FaceTime implementation on a Mac, it seemed the bulk of the calling functionality of FaceTime is in a daemon called avconferenced. Opening up the binary that supports its functionality, AVConference in IDA, it contains a function called SRTPEncryptData. This function then calls [CCCryptorUpdate](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/CCCryptorUpdate.3cc.html), which appeared to encrypt RTP packets below the header.


To do a quick test of whether fuzzing was likely to be effective, I hooked this function and altered the underlying encrypted data. Normally, this can be done by setting the DYLD\_INSERT\_LIBRARIES environment variable, but since avconferenced is a daemon that restarts automatically when it dies, there wasn’t an easy way to set an environment variable. I eventually used [insert\_dylib](https://github.com/Tyilo/insert_dylib) to alter the AVConference binary to load a library on startup, and restarted the process. The library loaded used [DYLD\_INTERPOSE](https://opensource.apple.com/source/dyld/dyld-210.2.3/include/mach-o/dyld-interposing.h) to replace CCCryptorUpdate with a version that fuzzed every input buffer (using fuzzer q from Part 1) before it was processed. This implementation had a lot of problems: it fuzzed both encryption and decryption, it affected every call to CCCryptorUpdate from avconferenced, not just ones involved in SRTP and there was no way to reproduce a crash. But using the modified FaceTime to call an iPhone led to video output that looked corrupted, and the phone crashed in a few minutes. This confirmed that this function was indeed where FaceTime calls are encrypted, and that fuzzing was likely to find bugs.


I made a few changes to the function that hooked CCCryptorUpdate to attempt to solve these problems. I limited fuzzing the input buffer to the two threads that write audio and video output to RTP, which also solved the problem of decrypted packets being fuzzed, as these threads only ever encrypt. I then added functionality that wrote the encrypted, fuzzed contents of each packet to a series of log files, so that test cases could be replayed. This required altering the sandbox of avconferenced so that it could write files to the log location, and adding spinlocks to the hook, as calling CCCryptorUpdate is thread safe, but logging packets isn’t.

# Call Replay


I then wrote a second library that hooks CCCryptorUpdate and replays packets logged by the first library by copying the logged packets in sequence into the packet buffers passed into the function. Unfortunately, this required a small modification to the AVConference binary, as the SRTPEncryptData function does not respect the length returned by CCCryptorUpdate; instead, it assumes that the length of the encrypted data is the same as the length as the plaintext data, which is reasonable when CCCryptorUpdate isn’t being hooked. Since SRTPEncryptData always uses a large fixed-size buffer for encryption, and encryption is in-place, I changed the function to retrieve the length of the encrypted buffer from the very end of the buffer, which was set in the hooked CCCryptorUpdate call. This memory is unlikely to be used for other purposes due to the typical shorter length of RTP packets. Unfortunately though, even though the same encrypted data was being replayed to the target, it wasn’t being processed correctly by the receiving device.


To understand why requires an explanation of how RTP works. An RTP packet has the following format.


It contains several fields that impact how its payload is interpreted. The SSRC is a random identifier that identifies a stream. For example, in FaceTime the audio and video streams have different SSRCs. SSRCs can also help differentiate between streams in a situation where a user could potentially have an unlimited number of streams, for example, multiple participants in a video call. RTP packets also have a payload type (PT in the diagram) which is used to differentiate different types of data in the payload. The payload type for a certain data type is consistent across calls. In FaceTime, the video stream has a single payload type for video data, but the audio stream has two payload types, likely one for audio data and the other for synchronization. The marker (M in the diagram) field of RTP is also used by FaceTime to represent when a packet is fragmented, and needs to be reassembled.


From this it is clear that simply copying logged data into the current encrypted packet won’t function correctly, because the data needs to have the correct SSRC, payload type and marker, or it won’t be interpreted correctly. This wasn’t necessary in WebRTC, because I had enough control over WebRTC that I could create a connection with a single SSRC and payload type for fuzzing purposes. But there is no way to do this in FaceTime, even muting a video call leads to silent audio packets being sent as opposed to the audio stream shutting down. So these values needed to be manually corrected.


An RTP feature called extensions made correcting these fields difficult. An extension is an optional header that can be added to an RTP packet. Extensions are not supposed to depend on the RTP payload to be interpreted, and extensions are often used to transmit network or display features. Some examples of supported extensions include the orientation extension, which tells the endpoint the orientation of the receiving device and the mute extension, which tells the endpoint whether the receiving device is muted.


Extensions mean that even if it is possible to determine the payload type, marker and SSRC of data, this is not sufficient to replay the exact packet that was sent. Moreover, FaceTime creates extensions after the packet is encrypted, so it is not possible to create the complete RTP packet by hooking CCCryptorUpdate, because extensions could be added later.


At this point, it seemed necessary to hook sendmsg as well as CCCryptorUpdate. This would allow the outgoing RTP header to be modified once it is complete. There were a few challenges in doing this. To start, audio and video packets are sent by different threads in FaceTime, and can be reordered between the time they are encrypted and the time they are sent by sendmsg. So I couldn’t assume that if sendmsg received an RTP packet that it was necessarily the last one that was encrypted. There was also the problem that SSRCs are dynamic, so replaying an RTP packet with the same SSRC it is recorded with won’t work, it needs to have the new SSRC for the audio or video stream.


Note that in MacOS Mojave, FaceTime can call sendmsg via either the AVConference binary or the IDSFoundation binary, depending on the network configuration. So to capture and replay unencrypted RTP traffic on newer systems, it is necessary  to hook CCCryptorUpdate in AConference and sendmsg in IDSFoundation (AVConference calls into IDSFoundation when it calls sendmsg). Otherwise, the process is the same as on older systems.


I ended up implementing a solution that recorded packets by recording the unencrypted payload, and then recorded its RTP header, and using a snippet of the encrypted payload to pair headers with the correct unencrypted payload. Then to replay packets, the packets encrypted in CCCryptorUpdate were replaced with the logged packets, and once the encrypted payload came through to sendmsg, the header was replaced with the logged one for that payload. Fortunately, the two streams with unique SSRCs used by FaceTime do not share any payload types, so it was possible to determine the new SSRC for each stream by waiting for an incoming packet with the correct payload type. Then in each subsequent packet, the SSRC was replaced with the correct one.


Unfortunately, this still did not replay a FaceTime call correctly, and calls often experienced decryption failures. I eventually determined that audio and video on FaceTime are encrypted with different keys, and updated the replay script to queue the CCCryptor used by CCCryptorUpdate function based on whether it was audio or video content. Then in sendmsg, the entire logged RTP packet, including the unencrypted payload, was copied into the outgoing packet, the SSRC was fixed, and then the payload encrypted with the next CCCryptor out of the appropriate queue. If a CCCryptor wasn’t available, outgoing packets were dropped until a new one was created. At this point, it was possible to stop using the modified AVConference binary, as all the packet modification was now happening in sendmsg. This implementation still had reliability problems.


Digging more deeply into how FaceTime encryption works, packets are encrypted in CTS mode, which requires a counter. The counter is initialized to a unique value for each packet that is sent. During the initialization of the RTP stream, the peers exchange two 16-byte random tokens, one for audio and one for video. The counter value for each packet is then calculated by exclusive or-ing the token with several values found in the packet, including the SSRC and the sequence number. Only one value in this calculation, the sequence number, changes between each packet. So it is possible to calculate the counter value for each packet by knowing the initial counter value and sequence number, which can be retrieved by hooking CCCryptorCreateWithMode. The sequence number is xor-ed with the random token at index 0x12 when FaceTime constructs a counter, so by xor-ing this location with the initial sequence number and then a packet’s sequence number, the counter value for that packet can be calculated. The key can also be retrieved by hooking CCCryptorCreateWithMode.This allowed me to dispense with queuing cryptors, as I now had all the information I needed to construct a cryptor for any packet. This allowed for packets to be encrypted faster and more accurately.


Sequence numbers still posed a problem though, as the initial sequence number of an RTP stream is randomly generated at the beginning of the call, and is different between subsequent calls. Also, sequence numbers are used to reconstruct video streams in order, so they need to be correct. I altered the replay tool determine the starting sequence number of each stream, and then calculate the difference between the starting sequence number of each logged stream and the sequence number of the logged packet and then add it to this value. These two changes finally made the replay tool work, though replay gets slower and slower as a stream is replayed due to dropped packets.

# Results


Using this setup, I was able to fuzz FaceTime calls and reproduce the crashes. I reported three bugs in FaceTime based on this work. All these issues have been fixed in recent updates.


[CVE-2018-4366](https://bugs.chromium.org/p/project-zero/issues/detail?id=1634)is an out-of-bounds read in video processing that occurs on Macs only.


[CVE-2018-4367](https://bugs.chromium.org/p/project-zero/issues/detail?id=1636)is a stack corruption vulnerability that affects iOS and Mac. There are a fair number of variables on the stack of the affected function before the stack cookie, and several fuzz crashes due to this issue caused segmentation faults as opposed to stack\_chk crashes, so it is likely exploitable.


[CVE-2018-4384](https://bugs.chromium.org/p/project-zero/issues/detail?id=1641)is a kernel heap corruption issue in video processing that affects iOS. It is likely similar to this

[vulnerability](https://gsec.hitb.org/materials/sg2018/D2%20-%20Decoding%20an%20iOS%20Vulnerability%20-%20Adam%20Donenfeld.pdf)found by Adam Donenfeld of Zimperium.


All of these issues took less than 15 minutes of fuzzing to find on a live device. Unfortunately, this was the limit of fuzzing that could be performed on FaceTime, as it would be difficult to create a command line fuzzing tool with coverage like we did for WebRTC as it is closed source.


In Part 3, we will look at video calling in WhatsApp.
