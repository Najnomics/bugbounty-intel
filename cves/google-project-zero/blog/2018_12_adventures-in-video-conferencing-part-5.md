# Adventures in Video Conferencing Part 5: Where Do We Go from Here? - Project Zero

Source: https://projectzero.google/2018/12/adventures-in-video-conferencing-part-5.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Natalie Silvanovich, Project Zero

Overall, our video conferencing research found a total of 11 bugs in WebRTC, FaceTime and WhatsApp. The majority of these were found through less than 15 minutes of mutation fuzzing RTP. We were surprised to find remote bugs so easily in code that is so widely distributed. There are several properties of video conferencing that likely led to the frequency and shallowness of these issues.

# WebRTC Bug Reporting

When we started looking at WebRTC, we were surprised to discover that their website did not describe how to report vulnerabilities to the project. They had an open bug tracker, but no specific guidance on how to flag or report vulnerabilities. They also provided no security guidance for integrators, and there was no clear way for integrators to determine when they needed to update their source for security fixes. Many integrators seem to have branched WebRTC without consideration for applying security updates. The combination of these factors make it more likely that vulnerabilities did not get reported, vulnerabilities or fixes got ‘lost’ in the tracker, fixes regressed or fixes did not get applied to implementations that use the source in part.


We worked with the WebRTC team to add this guidance to the site, and to clarify their vulnerability reporting process. Despite these changes, several large software vendors reached out to our team with questions about how to fix the vulnerabilities we reported. This shows there is still a lack of clarity on how to fix vulnerabilities in WebRTC.

# Video Conferencing Test Tools

We also discovered that most video conferencing solutions lack adequate test tools. In most implementations, there is no way to collect data that allows for problems with an RTP stream to be diagnosed. The vendors we asked did not have such a tool, even internally.  WebRTC had a mostly complete tool that allows streams to be recorded in the browser and replayed, but it did not work with streams that used non-default settings. This tool has now been updated to collect enough data to be able to replay any stream. The lack of tooling available to test RTP implementations likely contributed to the ease of finding vulnerabilities, and certainly made reproducing and reporting vulnerabilities more difficult

# Video Conferencing Standards

The standards that comprise video conferencing such as RTP, RTCP and FEC introduce a lot of complexity in achieving their goal of enabling reliable audio and video streams across any type of connection. While the majority of this complexity provides value to the end user, it also means that it is inherently difficult to implement securely.

# The Scope of Video Conferencing

WebRTC has billions of users. While it was originally created for use in the Chrome browser, it is now integrated by at least two Android applications that eclipse Chrome in terms of users: Facebook and WhatsApp (which only uses part of WebRTC). It is also used by Firefox and Safari. It is likely that most mobile devices run multiple copies of the WebRTC library. The ubiquity of WebRTC coupled with the lack of a clear patch strategy make it an especially concerning target for attackers.

# Recommendations for Developers

This section contains recommendations for developers who are implementing video conferencing based on our observations from this research.


First, it is a good idea to use an existing solution for video conferencing (either WebRTC or PJSIP) as opposed to implementing a new one. Video conferencing is very complex, and every implementation we looked at had vulnerabilities, so it is unlikely a new implementation would avoid these problems. Existing solutions have undergone at least some security testing and would likely have fewer problems.


It is also advisable to avoid branching existing video conferencing code. We have received questions from vendors who have branched WebRTC, and it is clear that this makes patching vulnerabilities more difficult. While branching can solve problems in the short term, integrators often regret it in the long term.


It is important to have a patch strategy when implementing video conferencing, as there will inevitably be vulnerabilities found in any implementation that is used. Developers should understand how security patches are distributed for any third-party library they integrate, and have a plan for applying them as soon as they are available.


It is also important to have adequate test tools for a video conferencing application, even if a third-party implementation is used. It is a good idea to have a way to reproduce a call from end to end. This is useful in diagnosing crashes, which could have a security impact, as well as functional problems.


Several mobile applications we looked at had unnecessary attack surface. Specifically codecs and other features of the video conferencing implementation were enabled and accessible via RTP even though no legitimate call would ever use them. WebRTC and PJSIP support disabling specific features such as codecs and FEC. It is a good idea to disable the features that are not being used.


Finally, video conferencing vulnerabilities can generally be split into those that require the target to answer the incoming call, and those that do not. Vulnerabilities that do not require the call to be answered are more dangerous. We observed that some video conferencing applications perform much more parsing of untrusted data before a call is answered than others. We recommend that developers put as much functionality after the call is answered as possible.

# Tools


In order to open up the most popular video conferencing implementations to more security research, we are releasing the tools we developed to do this research. [Street Party](https://github.com/googleprojectzero/Street-Party) is a suite of tools that allows the RTP streams of video conferencing implementations to be viewed and modified. It includes:


- WebRTC: instructions for recording and replaying RTP packets using WebRTC’s existing tools
- FaceTime: hooks for recording and replaying FaceTime calls
- WhatsApp: hooks for recording and replaying WhatsApp calls on Android


We hope these tools encourage even more investigation into the security properties of video conferencing. Contributions are welcome.

# Conclusion

We reviewed WebRTC, FaceTime and WhatsApp and found 11 serious vulnerabilities in their video conferencing implementations. Accessing and altering their encrypted content streams required substantial tooling. We are releasing this tooling to enable additional security research on these targets. There are many properties of video conferencing that make it susceptible to vulnerabilities. Adequate testing, conservative design and frequent patching can reduce the security risk of video conferencing implementations.
