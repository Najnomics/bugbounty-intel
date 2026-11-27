# chrome-158-stable-channel-update-2026-11-17

- **Source URL:** https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_01699533288.html
- **Fetched:** 2026-11-27
- **Researcher:** mdp_sec
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

## 
[Stable Channel Update for Desktop](https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_01699533288.html)

The Chrome team is delighted to announce the promotion of Chrome 158 to the stable channel for Windows, Mac and Linux. This will roll out over the coming days/weeks.

Chrome 158.0.8127.36 (Linux) 158.0.8127.36/.37 Windows/Mac contains a number of fixes and improvements -- a list of changes is available in the [log](https://chromium.googlesource.com/chromium/src/+log/157.0.8103.80..158.0.8127.36?pretty=fuller&n=10000). Watch out for upcoming [Chrome](https://chrome.blogspot.com/) and [Chromium](https://blog.chromium.org/) blog posts about new features and big efforts delivered in 158

# Security Fixes and Rewards

Note: Access to bug details and links may be kept restricted until a majority of users are updated with a fix. We will also retain restrictions if the bug exists in a third party library that other projects similarly depend on, but haven’t yet fixed.

This update includes [204](https://issues.chromium.org/issues?q=customfield1223088:0-M158) security fixes. Please see the [Chrome Security Page](https://www.chromium.org/Home/chromium-security) for more information.

\[N/A\]\[[562000561](https://issues.chromium.org/issues/562000561)\] Critical CVE-2026-130963: Use after free in WebView. Reported by Google on 2026-09-15

\[N/A\]\[[571153713](https://issues.chromium.org/issues/571153713)\] Critical CVE-2026-131031: Out of bounds write in GPU. Reported by Xinyang Ge (Anthropic), assisted by Claude on 2026-10-07

\[N/A\]\[[573128234](https://issues.chromium.org/issues/573128234)\] Critical CVE-2026-131060: Buffer overflow in Media. Reported by Xinyang Ge (Anthropic), assisted by Claude on 2026-10-13

\[N/A\]\[[574686297](https://issues.chromium.org/issues/574686297)\] Critical CVE-2026-131008: Use after free in GarbageCollection. Reported by Xinyang Ge on 2026-10-17

\[N/A\]\[[576812570](https://issues.chromium.org/issues/576812570)\] Critical CVE-2026-131054: Out of bounds write in ANGLE. Reported by Google on 2026-10-22

\[N/A\]\[[577366760](https://issues.chromium.org/issues/577366760)\] Critical CVE-2026-130975: Use after free in WebAudio. Reported by Xinyang Ge (Anthropic) on 2026-10-26

\[$4,000\]\[[576579698](https://issues.chromium.org/issues/576579698)\] High CVE-2026-130910: Protection mechanism failure in ANGLE. Reported by Arni Hardarson (Neonix Security) on 2026-10-22

\[N/A\]\[[512778726](https://issues.chromium.org/issues/512778726)\] High CVE-2026-130943: Use after free in Chromecast. Reported by Google on 2026-05-13

\[N/A\]\[[552672183](https://issues.chromium.org/issues/552672183)\] High CVE-2026-130994: Use after free in WebGL. Reported by Google on 2026-08-26

\[N/A\]\[[560339053](https://issues.chromium.org/issues/560339053)\] High CVE-2026-130909: Use after free in Extensions. Reported by Google on 2026-09-11

\[N/A\]\[[565839464](https://issues.chromium.org/issues/565839464)\] High CVE-2026-131065: Use after free in Autofill. Reported by Xinyang Ge (Anthropic), assisted by Claude on 2026-09-24

\[N/A\]\[[566347710](https://issues.chromium.org/issues/566347710)\] High CVE-2026-131100: Use after free in Loader. Reported by Xinyang Ge (Anthropic), assisted by Claude on 2026-09-26

\[N/A\]\[[566377256](https://issues.chromium.org/issues/566377256)\] High CVE-2026-130979: Use after free in Forms. Reported by Xinyang Ge (Anthropic), assisted by Claude on 2026-09-26

\[N/A\]\[[568831763](https://issues.chromium.org/issues/568831763)\] High CVE-2026-131079: Use after free in Bindings. Reported by Xinyang Ge on 2026-10-02

\[N/A\]\[[568891853](https://issues.chromium.org/issues/568891853)\] High CVE-2026-130940: Improper state validation in GPU. Reported by Google on 2026-10-02

\[N/A\]\[[568896063](https://issues.chromium.org/issues/568896063)\] High CVE-2026-130954: Incorrect reference resolution in ANGLE. Reported by Google on 2026-10-02

\[N/A\]\[[568896486](https://issues.chromium.org/issues/568896486)\] High CVE-2026-130996: Out of bounds write in ANGLE. Reported by Google on 2026-10-02

\[N/A\]\[[568937157](https://issues.chromium.org/issues/568937157)\] High CVE-2026-130970: Uninitialized resource in GPU. Reported by Google on 2026-10-03

\[N/A\]\[[569191970](https://issues.chromium.org/issues/569191970)\] High CVE-2026-131057: Out of bounds read in ANGLE. Reported by Google on 2026-10-03

\[N/A\]\[[569197056](https://issues.chromium.org/issues/569197056)\] High CVE-2026-130945: Use after free in VR. Reported by Google on 2026-10-03

\[N/A\]\[[569659189](https://issues.chromium.org/issues/569659189)\] High CVE-2026-131084: Use after free in XML. Reported by Xinyang Ge on 2026-10-05

\[N/A\]\[[570703733](https://issues.chromium.org/issues/570703733)\] High CVE-2026-131090: Use after free in Geometry. Reported by Xinyang Ge on 2026-10-06

\[TBD\]\[[571284298](https://issues.chromium.org/issues/571284298)\] High CVE-2026-130982: Incorrect authorization in Omnibox. Reported by Hafiizh on 2026-10-08

\[N/A\]\[[572237022](https://issues.chromium.org/issues/572237022)\] High CVE-2026-131021: Use after free in Accessibility. Reported by Xinyang Ge (Anthropic), assisted by Claude on 2026-10-11

\[N/A\]\[[572237023](https://issues.chromium.org/issues/572237023)\] High CVE-2026-131022: Use after free in DOM. Reported by Xinyang Ge (Anthropic), assisted by Claude on 2026-10-11

\[TBD\]\[[572307225](https://issues.chromium.org/issues/572307225)\] High CVE-2026-131081: Incorrect authorization in Media. Reported by Anthropic and Ada Logics. on 2026-10-10

\[TBD\]\[[572308124](https://issues.chromium.org/issues/572308124)\] High CVE-2026-130961: Incorrect authorization in Media. Reported by Anthropic and Ada Logics. on 2026-10-10

\[TBD\]\[[572574561](https://issues.chromium.org/issues/572574561)\] High CVE-2026-130984: Incorrect authorization in Canvas. Reported by Hyeonjun Ahn (@\_deayzl) on 2026-10-12

\[TBD\]\[[572682755](https://issues.chromium.org/issues/572682755)\] High CVE-2026-130946: Incorrect authorization in PerformanceAPIs. Reported by Arni Hardarson (Neonix Security) on 2026-10-12

\[TBD\]\[[572882344](https://issues.chromium.org/issues/572882344)\] High CVE-2026-131045: Incorrect authorization in PerformanceAPIs. Reported by Anthropic and Ada Logics. on 2026-10-12

\[N/A\]\[[573263262](https://issues.chromium.org/issues/573263262)\] High CVE-2026-131042: Use after free in V8. Reported by Google on 2026-10-13

\[N/A\]\[[573263397](https://issues.chromium.org/issues/573263397)\] High CVE-2026-131059: Use after free in Autofill. Reported by Google on 2026-10-13

\[N/A\]\[[573266324](https://issues.chromium.org/issues/573266324)\] High CVE-2026-130934: Incorrect authorization in Autofill. Reported by Google on 2026-10-13

\[N/A\]\[[573981230](https://issues.chromium.org/issues/573981230)\] High CVE-2026-130951: Use after free in Plugins. Reported by Google on 2026-10-15

\[N/A\]\[[574221485](https://issues.chromium.org/issues/574221485)\] High CVE-2026-131013: Buffer overflow in Skia. Reported by Google on 2026-10-16

\[N/A\]\[[574640593](https://issues.chromium.org/issues/574640593)\] High CVE-2026-130941: Incorrect authorization in HTML. Reported by Google on 2026-10-16

\[N/A\]\[[574789298](https://issues.chromium.org/issues/574789298)\] High CVE-2026-131068: Use after free in DOM. Reported by Google on 2026-10-17

\[N/A\]\[[574795880](https://issues.chromium.org/issues/574795880)\] High CVE-2026-130907: Use after free in Autofill. Reported by Google on 2026-10-17

\[TBD\]\[[574967987](https://issues.chromium.org/issues/574967987)\] High CVE-2026-130914: Uninitialized resource in ANGLE. Reported by definitelynotatable on 2026-10-18

\[N/A\]\[[575201060](https://issues.chromium.org/issues/575201060)\] High CVE-2026-131082: Use after free in CSS. Reported by Google on 2026-10-19

\[N/A\]\[[575201475](https://issues.chromium.org/issues/575201475)\] High CVE-2026-130915: Use after free in CSS. Reported by Google on 2026-10-19

\[N/A\]\[[575395237](https://issues.chromium.org/issues/575395237)\] High CVE-2026-131044: Use after free in Payments. Reported by Xinyang Ge on 2026-10-19

\[N/A\]\[[575712513](https://issues.chromium.org/issues/575712513)\] High CVE-2026-131025: Out of bounds read in ANGLE. Reported by Google on 2026-10-20

\[TBD\]\[[575810899](https://issues.chromium.org/issues/575810899)\] High CVE-2026-131033: Missing authorization in Extensions. Reported by malichamdan on 2026-10-20

\[N/A\]\[[576131851](https://issues.chromium.org/issues/576131851)\] High CVE-2026-130977: Uninitialized resource in Dawn. Reported by Google on 2026-10-21

\[N/A\]\[[576203570](https://issues.chromium.org/issues/576203570)\] High CVE-2026-130980: Use after free in Layout. Reported by Xinyang Ge on 2026-10-21

\[N/A\]\[[576812420](https://issues.chromium.org/issues/576812420)\] High CVE-2026-131039: Use after free in Mojo. Reported by Google on 2026-10-22

\[N/A\]\[[576812539](https://issues.chromium.org/issues/576812539)\] High CVE-2026-131050: Use after free in Mojo. Reported by Google on 2026-10-22

\[N/A\]\[[576944087](https://issues.chromium.org/issues/576944087)\] High CVE-2026-131104: Out of bounds read in Tint. Reported by Google on 2026-10-23

\[N/A\]\[[576954321](https://issues.chromium.org/issues/576954321)\] High CVE-2026-131103: Uninitialized resource in GPU. Reported by Google on 2026-10-23

\[TBD\]\[[576991116](https://issues.chromium.org/issues/576991116)\] High CVE-2026-131093: Use after free in FedCM. Reported by octo on 2026-10-23

\[N/A\]\[[577245772](https://issues.chromium.org/issues/577245772)\] High CVE-2026-130957: Improper state validation in Performance. Reported by Google on 2026-10-24

\[N/A\]\[[577369844](https://issues.chromium.org/issues/577369844)\] High CVE-2026-131076: Uninitialized resource in GPU. Reported by Google on 2026-10-24

\[N/A\]\[[577369904](https://issues.chromium.org/issues/577369904)\] High CVE-2026-131083: Uninitialized resource in GPU. Reported by Google on 2026-10-24

\[N/A\]\[[577371168](https://issues.chromium.org/issues/577371168)\] High CVE-2026-131002: Uninitialized resource in GPU. Reported by Google on 2026-10-24

\[N/A\]\[[577401536](https://issues.chromium.org/issues/577401536)\] High CVE-2026-130968: Use after free in Views. Reported by Google on 2026-10-24

\[N/A\]\[[577403973](https://issues.chromium.org/issues/577403973)\] High CVE-2026-131007: Uninitialized resource in GPU. Reported by Google on 2026-10-24

\[N/A\]\[[577410943](https://issues.chromium.org/issues/577410943)\] High CVE-2026-131092: Use after free in Mojo. Reported by Google on 2026-10-24

\[N/A\]\[[579027312](https://issues.chromium.org/issues/579027312)\] High CVE-2026-130932: Improper resource exposure in Core. Reported by Jaewon Lee (Google) on 2026-10-28

\[TBD\]\[[579037685](https://issues.chromium.org/issues/579037685)\] High CVE-2026-130944: Use after free in Omnibox. Reported by zenhumany on 2026-10-29

\[TBD\]\[[579867878](https://issues.chromium.org/issues/579867878)\] High CVE-2026-131023: Race condition in Core. Reported by zenneth (randomguy6407) on 2026-10-30

\[N/A\]\[[580867132](https://issues.chromium.org/issues/580867132)\] High CVE-2026-131004: Use after free in FedCM. Reported by Google on 2026-11-02

\[N/A\]\[[580868423](https://issues.chromium.org/issues/580868423)\] High CVE-2026-130926: Confused deputy in Sync. Reported by Google on 2026-11-02

\[TBD\]\[[581064654](https://issues.chromium.org/issues/581064654)\] High CVE-2026-131101: Out of bounds read in Editing. Reported by Team Allied (h4nk3r1n, Hyeongeun Ji, h4vrut4, HunSec, nag0x) on 2026-11-03

\[N/A\]\[[581367663](https://issues.chromium.org/issues/581367663)\] High CVE-2026-131089: Buffer overflow in CrashReporting. Reported by Google on 2026-11-03

\[TBD\]\[[582218292](https://issues.chromium.org/issues/582218292)\] High CVE-2026-130952: Uninitialized resource in Network. Reported by stephan on 2026-11-05

\[TBD\]\[[583188056](https://issues.chromium.org/issues/583188056)\] High CVE-2026-131063: Use after free in CameraCapture. Reported by octo on 2026-11-07

\[N/A\]\[[583617538](https://issues.chromium.org/issues/583617538)\] High CVE-2026-130999: Use after free in Downloads. Reported by Google on 2026-11-09

\[$2,000\]\[[530046745](https://issues.chromium.org/issues/530046745)\] Medium CVE-2026-131080: UI misrepresentation in Chromium. Reported by Azza Tegar Naufal Ataullah on 2026-07-02

\[$2,000\]\[[561073365](https://issues.chromium.org/issues/561073365)\] Medium CVE-2026-131019: Information leak in ANGLE. Reported by JonathanBouman on 2026-09-13

\[$1,000\]\[[501901218](https://issues.chromium.org/issues/501901218)\] Medium CVE-2026-131095: Information leak in Workers. Reported by M. Fauzan Wijaya (Gh05t666nero) on 2026-04-12

\[N/A\]\[[497617812](https://issues.chromium.org/issues/497617812)\] Medium CVE-2026-130987: Race condition in Downloads. Reported by Google on 2026-03-30

\[N/A\]\[[497744349](https://issues.chromium.org/issues/497744349)\] Medium CVE-2026-130942: Observable discrepancy in Extensions. Reported by Google on 2026-03-30

\[N/A\]\[[504552032](https://issues.chromium.org/issues/504552032)\] Medium CVE-2026-130958: Uninitialized resource in WebRTC. Reported by Google on 2026-04-20

\[N/A\]\[[513340629](https://issues.chromium.org/issues/513340629)\] Medium CVE-2026-131020: Use after free in WebView. Reported by Google on 2026-05-14

\[N/A\]\[[514409956](https://issues.chromium.org/issues/514409956)\] Medium CVE-2026-131048: Incorrect authorization in GetUserMedia. Reported by Google on 2026-05-18

\[N/A\]\[[518239793](https://issues.chromium.org/issues/518239793)\] Medium CVE-2026-131062: Improper synchronization in ScreenCapture. Reported by Google on 2026-05-30

\[N/A\]\[[524422213](https://issues.chromium.org/issues/524422213)\] Medium CVE-2026-131006: Race condition in CredentialProvider. Reported by Google on 2026-06-16

\[N/A\]\[[536599243](https://issues.chromium.org/issues/536599243)\] Medium CVE-2026-130971: Out of bounds write in ANGLE. Reported by Google on 2026-07-19

\[N/A\]\[[543907563](https://issues.chromium.org/issues/543907563)\] Medium CVE-2026-131075: Improper input validation in DevTools. Reported by Google on 2026-08-07

\[N/A\]\[[551065275](https://issues.chromium.org/issues/551065275)\] Medium CVE-2026-131069: Information leak in WebGL. Reported by Google on 2026-08-22

\[N/A\]\[[553151406](https://issues.chromium.org/issues/553151406)\] Medium CVE-2026-130992: Incorrect authorization in Views. Reported by Google on 2026-08-26

\[N/A\]\[[553159779](https://issues.chromium.org/issues/553159779)\] Medium CVE-2026-131010: Use after free in Extensions. Reported by Google on 2026-08-26

\[N/A\]\[[556213137](https://issues.chromium.org/issues/556213137)\] Medium CVE-2026-130986: Incorrect authorization in Sync. Reported by Google on 2026-09-02

\[TBD\]\[[561099685](https://issues.chromium.org/issues/561099685)\] Medium CVE-2026-130990: Missing authorization in PersistentCache. Reported by Hoyong Jin on 2026-09-14

\[N/A\]\[[562227882](https://issues.chromium.org/issues/562227882)\] Medium CVE-2026-130962: Incomplete cleanup in Navigation. Reported by Google on 2026-09-16

\[N/A\]\[[562230299](https://issues.chromium.org/issues/562230299)\] Medium CVE-2026-131000: Improper input validation in WebAppInstalls. Reported by Google on 2026-09-16

\[N/A\]\[[563348727](https://issues.chromium.org/issues/563348727)\] Medium CVE-2026-131024: Incorrect authorization in iOSWeb. Reported by Google on 2026-09-18

\[N/A\]\[[567673370](https://issues.chromium.org/issues/567673370)\] Medium CVE-2026-130948: Use after free in Omnibox. Reported by Google on 2026-09-29

\[N/A\]\[[568908052](https://issues.chromium.org/issues/568908052)\] Medium CVE-2026-130923: Out of bounds write in V8. Reported by Google on 2026-10-02

\[N/A\]\[[568972475](https://issues.chromium.org/issues/568972475)\] Medium CVE-2026-131015: Missing authorization in Mobile. Reported by Google on 2026-10-03

\[N/A\]\[[568973728](https://issues.chromium.org/issues/568973728)\] Medium CVE-2026-130937: Incorrect authorization in Navigation. Reported by Google on 2026-10-03

\[N/A\]\[[568974861](https://issues.chromium.org/issues/568974861)\] Medium CVE-2026-131053: Missing authorization in Layout. Reported by Google on 2026-10-03

\[TBD\]\[[569129183](https://issues.chromium.org/issues/569129183)\] Medium CVE-2026-130917: Use after free in Browser. Reported by Hafiizh on 2026-10-04

\[N/A\]\[[571348848](https://issues.chromium.org/issues/571348848)\] Medium CVE-2026-131087: Type confusion in V8. Reported by Google on 2026-10-08

\[N/A\]\[[571856431](https://issues.chromium.org/issues/571856431)\] Medium CVE-2026-131061: Buffer overflow in Color. Reported by ansollan on 2026-10-09

\[TBD\]\[[572721812](https://issues.chromium.org/issues/572721812)\] Medium CVE-2026-130960: Use after free in Session. Reported by Kyumin Lee on 2026-10-12

\[N/A\]\[[573257409](https://issues.chromium.org/issues/573257409)\] Medium CVE-2026-131070: Information leak in DOM. Reported by Google on 2026-10-13

\[N/A\]\[[573262234](https://issues.chromium.org/issues/573262234)\] Medium CVE-2026-130936: Information leak in Media. Reported by Google on 2026-10-13

\[N/A\]\[[573265164](https://issues.chromium.org/issues/573265164)\] Medium CVE-2026-131026: Information leak in Media. Reported by Google on 2026-10-13

\[TBD\]\[[573285920](https://issues.chromium.org/issues/573285920)\] Medium CVE-2026-131056: Use after free in WebAppInstalls. Reported by Arni Hardarson (Neonix Security) on 2026-10-13

\[N/A\]\[[574199198](https://issues.chromium.org/issues/574199198)\] Medium CVE-2026-131043: Use after free in HID. Reported by Google on 2026-10-16

\[N/A\]\[[574200170](https://issues.chromium.org/issues/574200170)\] Medium CVE-2026-130930: Use after free in Ozone. Reported by Google on 2026-10-16

\[N/A\]\[[574211718](https://issues.chromium.org/issues/574211718)\] Medium CVE-2026-131066: Uninitialized resource in Dawn. Reported by Google on 2026-10-16

\[N/A\]\[[574231826](https://issues.chromium.org/issues/574231826)\] Medium CVE-2026-131028: Incorrect authorization in WebAppInstalls. Reported by Google on 2026-10-16

\[N/A\]\[[574232164](https://issues.chromium.org/issues/574232164)\] Medium CVE-2026-131064: Incorrect authorization in WebAppInstalls. Reported by Google on 2026-10-16

\[N/A\]\[[574299586](https://issues.chromium.org/issues/574299586)\] Medium CVE-2026-131047: Race condition in ServiceManager. Reported by Google on 2026-10-16

\[N/A\]\[[574302978](https://issues.chromium.org/issues/574302978)\] Medium CVE-2026-130976: Use after free in PDFium. Reported by Google on 2026-10-16

\[N/A\]\[[574310133](https://issues.chromium.org/issues/574310133)\] Medium CVE-2026-131077: Out of bounds write in Tint. Reported by Google on 2026-10-16

\[N/A\]\[[574311093](https://issues.chromium.org/issues/574311093)\] Medium CVE-2026-130965: Uninitialized resource in Media. Reported by Google on 2026-10-16

\[N/A\]\[[574312303](https://issues.chromium.org/issues/574312303)\] Medium CVE-2026-131086: Uninitialized resource in WebRTC. Reported by Google on 2026-10-16

\[N/A\]\[[574376000](https://issues.chromium.org/issues/574376000)\] Medium CVE-2026-130905: UI misrepresentation in SVG. Reported by Google on 2026-10-16

\[N/A\]\[[574378401](https://issues.chromium.org/issues/574378401)\] Medium CVE-2026-130938: Use after free in Accessibility. Reported by Google on 2026-10-16

\[N/A\]\[[574502257](https://issues.chromium.org/issues/574502257)\] Medium CVE-2026-131036: UI misrepresentation in Autofill. Reported by Google on 2026-10-16

\[N/A\]\[[574508216](https://issues.chromium.org/issues/574508216)\] Medium CVE-2026-131014: Confused deputy in Grid. Reported by Google on 2026-10-16

\[N/A\]\[[574508556](https://issues.chromium.org/issues/574508556)\] Medium CVE-2026-131052: Race condition in UI. Reported by Google on 2026-10-16

\[N/A\]\[[574512015](https://issues.chromium.org/issues/574512015)\] Medium CVE-2026-130985: Improper input validation in DOMStorage. Reported by Google on 2026-10-16

\[N/A\]\[[574587405](https://issues.chromium.org/issues/574587405)\] Medium CVE-2026-130947: Integer overflow in Autofill. Reported by Google on 2026-10-16

\[N/A\]\[[574594013](https://issues.chromium.org/issues/574594013)\] Medium CVE-2026-130995: UI misrepresentation in Autofill. Reported by Google on 2026-10-16

\[N/A\]\[[574635898](https://issues.chromium.org/issues/574635898)\] Medium CVE-2026-131091: Missing authorization in Autofill. Reported by Google on 2026-10-16

\[N/A\]\[[574639084](https://issues.chromium.org/issues/574639084)\] Medium CVE-2026-130997: Incomplete cleanup in Autofill. Reported by Google on 2026-10-16

\[N/A\]\[[574639489](https://issues.chromium.org/issues/574639489)\] Medium CVE-2026-131038: Missing authorization in Editing. Reported by Google on 2026-10-16

\[N/A\]\[[574640036](https://issues.chromium.org/issues/574640036)\] Medium CVE-2026-131096: Missing authorization in Editing. Reported by Google on 2026-10-16

\[N/A\]\[[574642315](https://issues.chromium.org/issues/574642315)\] Medium CVE-2026-130913: Incorrect reference resolution in Mobile. Reported by Google on 2026-10-17

\[N/A\]\[[574643395](https://issues.chromium.org/issues/574643395)\] Medium CVE-2026-131017: Information leak in Editing. Reported by Google on 2026-10-17

\[N/A\]\[[574757499](https://issues.chromium.org/issues/574757499)\] Medium CVE-2026-130959: Missing authorization in FileSystem. Reported by Google on 2026-10-17

\[N/A\]\[[574759287](https://issues.chromium.org/issues/574759287)\] Medium CVE-2026-130933: Information leak in Paint. Reported by Google on 2026-10-17

\[N/A\]\[[574781794](https://issues.chromium.org/issues/574781794)\] Medium CVE-2026-130929: Use after free in Chromoting. Reported by Google on 2026-10-17

\[N/A\]\[[574788166](https://issues.chromium.org/issues/574788166)\] Medium CVE-2026-130956: Improper input validation in WebAppInstalls. Reported by Google on 2026-10-17

\[N/A\]\[[574801551](https://issues.chromium.org/issues/574801551)\] Medium CVE-2026-131067: Missing authorization in Autofill. Reported by Google on 2026-10-17

\[TBD\]\[[574858526](https://issues.chromium.org/issues/574858526)\] Medium CVE-2026-131030: Privilege elevation in Sandbox. Reported by Quyen Son (@zer0qs) on 2026-10-17

\[N/A\]\[[574897062](https://issues.chromium.org/issues/574897062)\] Medium CVE-2026-130991: Uninitialized resource in Media. Reported by Google on 2026-10-17

\[N/A\]\[[574901760](https://issues.chromium.org/issues/574901760)\] Medium CVE-2026-131051: Incorrect authorization in UI. Reported by Google on 2026-10-17

\[N/A\]\[[574907939](https://issues.chromium.org/issues/574907939)\] Medium CVE-2026-131058: UI misrepresentation in WebAppInstalls. Reported by Google on 2026-10-17

\[N/A\]\[[574909775](https://issues.chromium.org/issues/574909775)\] Medium CVE-2026-131032: Confused deputy in UI. Reported by Google on 2026-10-17

\[N/A\]\[[574922639](https://issues.chromium.org/issues/574922639)\] Medium CVE-2026-131094: Incorrect authorization in WebUI. Reported by Google on 2026-10-17

\[N/A\]\[[575088323](https://issues.chromium.org/issues/575088323)\] Medium CVE-2026-131071: Confused deputy in Mobile. Reported by Google on 2026-10-18

\[N/A\]\[[575090111](https://issues.chromium.org/issues/575090111)\] Medium CVE-2026-131046: Improper input validation in ChromeDriver. Reported by Google on 2026-10-18

\[N/A\]\[[575156577](https://issues.chromium.org/issues/575156577)\] Medium CVE-2026-130928: Code injection in Mobile. Reported by Google on 2026-10-18

\[N/A\]\[[575315727](https://issues.chromium.org/issues/575315727)\] Medium CVE-2026-131078: Use after free in Proxy. Reported by Google on 2026-10-19

\[N/A\]\[[575318301](https://issues.chromium.org/issues/575318301)\] Medium CVE-2026-130924: Incorrect authorization in WebAppInstalls. Reported by Google on 2026-10-19

\[N/A\]\[[576129731](https://issues.chromium.org/issues/576129731)\] Medium CVE-2026-130969: Incorrect authorization in Omnibox. Reported by Google on 2026-10-21

\[N/A\]\[[576132156](https://issues.chromium.org/issues/576132156)\] Medium CVE-2026-131003: Confused deputy in TabModel. Reported by Google on 2026-10-21

\[TBD\]\[[576225189](https://issues.chromium.org/issues/576225189)\] Medium CVE-2026-131097: Missing authorization in V8. Reported by @bean5oup on 2026-10-21

\[TBD\]\[[576306917](https://issues.chromium.org/issues/576306917)\] Medium CVE-2026-131074: Use after free in DeviceBoundSessionCredentials. Reported by binishack3r on 2026-10-22

\[N/A\]\[[576312229](https://issues.chromium.org/issues/576312229)\] Medium CVE-2026-130989: Missing authorization in Paint. Reported by Google on 2026-10-21

\[TBD\]\[[576387815](https://issues.chromium.org/issues/576387815)\] Medium CVE-2026-130974: Use after free in UserEducation. Reported by binish with Georgia Tech SSLab on 2026-10-21

\[N/A\]\[[576859257](https://issues.chromium.org/issues/576859257)\] Medium CVE-2026-131011: Use of uninitialized variable in Speech. Reported by Google on 2026-10-23

\[N/A\]\[[577305505](https://issues.chromium.org/issues/577305505)\] Medium CVE-2026-130988: Out of bounds read in V8. Reported by Google on 2026-10-24

\[N/A\]\[[581351423](https://issues.chromium.org/issues/581351423)\] Medium CVE-2026-131106: Buffer overflow in Partition. Reported by Google on 2026-11-03

\[$2,000\]\[[474737096](https://issues.chromium.org/issues/474737096)\] Low CVE-2026-130939: Missing authorization in LocalNetworkAccess. Reported by Kevin Joensen @ Baldur Security on 2026-01-10

\[TBD\]\[[392139161](https://issues.chromium.org/issues/392139161)\] Low CVE-2026-130935: Information leak in Referrer. Reported by Joshua Rogers(@megamansec) on 2025-01-25

\[N/A\]\[[497098609](https://issues.chromium.org/issues/497098609)\] Low CVE-2026-131088: Improper input validation in WebAppInstalls. Reported by Google on 2026-03-28

\[N/A\]\[[502048148](https://issues.chromium.org/issues/502048148)\] Low CVE-2026-131041: Improper input validation in Editing. Reported by Google on 2026-04-13

\[N/A\]\[[502803648](https://issues.chromium.org/issues/502803648)\] Low CVE-2026-131016: Incorrect authorization in DevTools. Reported by Google on 2026-04-15

\[N/A\]\[[506142100](https://issues.chromium.org/issues/506142100)\] Low CVE-2026-131040: Incorrect authorization in Extensions. Reported by Google on 2026-04-24

\[N/A\]\[[511803678](https://issues.chromium.org/issues/511803678)\] Low CVE-2026-130925: Race condition in Downloads. Reported by Google on 2026-05-10

\[N/A\]\[[513198336](https://issues.chromium.org/issues/513198336)\] Low CVE-2026-130921: Nonce reuse in WebRTC. Reported by Google on 2026-05-14

\[N/A\]\[[513329281](https://issues.chromium.org/issues/513329281)\] Low CVE-2026-130912: Improper state validation in Network. Reported by Google on 2026-05-14

\[N/A\]\[[513841847](https://issues.chromium.org/issues/513841847)\] Low CVE-2026-130967: Incorrect authorization in DevTools. Reported by Google on 2026-05-16

\[N/A\]\[[514008162](https://issues.chromium.org/issues/514008162)\] Low CVE-2026-131009: UI misrepresentation in Passwords. Reported by Google on 2026-05-17

\[N/A\]\[[518998812](https://issues.chromium.org/issues/518998812)\] Low CVE-2026-130978: Incorrect authorization in Media. Reported by Google on 2026-06-02

\[N/A\]\[[519999855](https://issues.chromium.org/issues/519999855)\] Low CVE-2026-130931: Incorrect authorization in Extensions. Reported by Google on 2026-06-04

\[N/A\]\[[521476204](https://issues.chromium.org/issues/521476204)\] Low CVE-2026-130908: Missing authorization in Passwords. Reported by Google on 2026-06-08

\[N/A\]\[[536479671](https://issues.chromium.org/issues/536479671)\] Low CVE-2026-131099: Out of bounds read in ANGLE. Reported by Google on 2026-07-19

\[N/A\]\[[540124890](https://issues.chromium.org/issues/540124890)\] Low CVE-2026-131072: Incorrect authorization in HID. Reported by Google on 2026-07-29

\[TBD\]\[[550780268](https://issues.chromium.org/issues/550780268)\] Low CVE-2026-131034: Incorrect authorization in SurfaceCapture. Reported by Orellasec on 2026-08-22

\[TBD\]\[[551608036](https://issues.chromium.org/issues/551608036)\] Low CVE-2026-131073: Incorrect authorization in Passwords. Reported by Hafiizh on 2026-08-24

\[N/A\]\[[553136985](https://issues.chromium.org/issues/553136985)\] Low CVE-2026-130983: Incorrect authorization in DevTools. Reported by Google on 2026-08-26

\[N/A\]\[[553152493](https://issues.chromium.org/issues/553152493)\] Low CVE-2026-131105: Incorrect authorization in Glic. Reported by Google on 2026-08-26

\[N/A\]\[[553152636](https://issues.chromium.org/issues/553152636)\] Low CVE-2026-130911: Race condition in DevTools. Reported by Google on 2026-08-26

\[N/A\]\[[553154509](https://issues.chromium.org/issues/553154509)\] Low CVE-2026-131102: UI misrepresentation in FileSystem. Reported by Google on 2026-08-26

\[N/A\]\[[553259600](https://issues.chromium.org/issues/553259600)\] Low CVE-2026-121101: Missing authorization in DevTools. Reported by Google on 2026-08-27

\[N/A\]\[[553263303](https://issues.chromium.org/issues/553263303)\] Low CVE-2026-130916: Missing authorization in DevTools. Reported by Google on 2026-08-27

\[N/A\]\[[554558674](https://issues.chromium.org/issues/554558674)\] Low CVE-2026-131018: Confused deputy in DevTools. Reported by Google on 2026-08-29

\[N/A\]\[[562909022](https://issues.chromium.org/issues/562909022)\] Low CVE-2026-131085: Clickjacking in PermissionElement. Reported by Google on 2026-09-17

\[N/A\]\[[562910021](https://issues.chromium.org/issues/562910021)\] Low CVE-2026-130981: Information leak in Enterprise. Reported by Google on 2026-09-17

\[N/A\]\[[562957022](https://issues.chromium.org/issues/562957022)\] Low CVE-2026-130973: Incorrect authorization in Sensor. Reported by Google on 2026-09-17

\[N/A\]\[[562971921](https://issues.chromium.org/issues/562971921)\] Low CVE-2026-131027: Observable discrepancy in Browser. Reported by Google on 2026-09-17

\[TBD\]\[[564769937](https://issues.chromium.org/issues/564769937)\] Low CVE-2026-131012: Missing authorization in Services. Reported by Arni Hardarson (Neonix Security) on 2026-09-22

\[TBD\]\[[566504721](https://issues.chromium.org/issues/566504721)\] Low CVE-2026-131029: Improper input validation in Extensions. Reported by ockojetu on 2026-09-26

\[TBD\]\[[567397860](https://issues.chromium.org/issues/567397860)\] Low CVE-2026-131049: Use after free in SignIn. Reported by dianatichy16 on 2026-09-29

\[TBD\]\[[567765567](https://issues.chromium.org/issues/567765567)\] Low CVE-2026-130955: UI misrepresentation in Mobile. Reported by iqamna1337 on 2026-09-30

\[TBD\]\[[567944558](https://issues.chromium.org/issues/567944558)\] Low CVE-2026-131035: Out of bounds read in Media. Reported by Andrew Boni (@andrewboni) on 2026-09-30

\[TBD\]\[[568576341](https://issues.chromium.org/issues/568576341)\] Low CVE-2026-130927: Incorrect authorization in DevTools. Reported by venkatchallaceh on 2026-10-02

\[N/A\]\[[568967707](https://issues.chromium.org/issues/568967707)\] Low CVE-2026-130949: UI misrepresentation in Passwords. Reported by Google on 2026-10-03

\[N/A\]\[[568979550](https://issues.chromium.org/issues/568979550)\] Low CVE-2026-130906: Incorrect authorization in DevTools. Reported by Google on 2026-10-03

\[N/A\]\[[568986689](https://issues.chromium.org/issues/568986689)\] Low CVE-2026-131005: Use after free in DevTools. Reported by Google on 2026-10-03

\[N/A\]\[[568989951](https://issues.chromium.org/issues/568989951)\] Low CVE-2026-130920: Information leak in Payments. Reported by Google on 2026-10-03

\[N/A\]\[[569008693](https://issues.chromium.org/issues/569008693)\] Low CVE-2026-130953: Incorrect authorization in Core. Reported by Google on 2026-10-03

\[N/A\]\[[569010448](https://issues.chromium.org/issues/569010448)\] Low CVE-2026-130922: UI misrepresentation in UI. Reported by Google on 2026-10-03

\[N/A\]\[[569017013](https://issues.chromium.org/issues/569017013)\] Low CVE-2026-130964: Confused deputy in DevTools. Reported by Google on 2026-10-03

\[N/A\]\[[569127860](https://issues.chromium.org/issues/569127860)\] Low CVE-2026-130993: Use after free in Script. Reported by Xinyang Ge on 2026-10-05

\[TBD\]\[[571722742](https://issues.chromium.org/issues/571722742)\] Low CVE-2026-130998: Improper input validation in Parser. Reported by burdock129 on 2026-10-09

\[N/A\]\[[572312093](https://issues.chromium.org/issues/572312093)\] Low CVE-2026-130950: Type confusion in V8. Reported by Google on 2026-10-11

\[TBD\]\[[573244957](https://issues.chromium.org/issues/573244957)\] Low CVE-2026-131055: Improper output encoding in Editing. Reported by NH DEV on 2026-10-13

\[TBD\]\[[573591801](https://issues.chromium.org/issues/573591801)\] Low CVE-2026-130919: Race condition in Printing. Reported by jony\_juice on 2026-10-14

\[N/A\]\[[573760540](https://issues.chromium.org/issues/573760540)\] Low CVE-2026-131001: Buffer overflow in Video. Reported by Vlad Stolyarov (Anthropic), assisted by Claude on 2026-10-15

\[N/A\]\[[574212789](https://issues.chromium.org/issues/574212789)\] Low CVE-2026-130966: Out of bounds read in Tint. Reported by Google on 2026-10-16

\[N/A\]\[[574412712](https://issues.chromium.org/issues/574412712)\] Low CVE-2026-131098: Out of bounds read in V8. Reported by Google on 2026-10-16

\[N/A\]\[[574643577](https://issues.chromium.org/issues/574643577)\] Low CVE-2026-131037: Improper authentication request restriction in Chromoting. Reported by Google on 2026-10-17

\[TBD\]\[[575048405](https://issues.chromium.org/issues/575048405)\] Low CVE-2026-130972: Observable discrepancy in PictureInPicture. Reported by Saurav Bhattarai on 2026-10-18

\[TBD\]\[[575506658](https://issues.chromium.org/issues/575506658)\] Low CVE-2026-130918: Use after free in Views. Reported by Khalil Zhani on 2026-10-20

\[N/A\]\[[576501766](https://issues.chromium.org/issues/576501766)\] Low CVE-2026-130904: Incorrect authorization in SiteSettings. Reported by Google on 2026-10-22

We would also like to thank all security researchers that worked with us during the development cycle to prevent security bugs from ever reaching the stable channel.

Many of our security bugs are detected using [AddressSanitizer](https://code.google.com/p/address-sanitizer/wiki/AddressSanitizer), [MemorySanitizer](https://code.google.com/p/memory-sanitizer/wiki/MemorySanitizer), [UndefinedBehaviorSanitizer](https://www.chromium.org/developers/testing/undefinedbehaviorsanitizer), [Control Flow Integrity](https://www.chromium.org/developers/testing/control-flow-integrity/), [libFuzzer](https://chromium.googlesource.com/chromium/src/+/HEAD/testing/libfuzzer/README.md), or [AFL](https://github.com/google/afl).

Interested in switching release channels? Find out how [here](https://www.chromium.org/getting-involved/dev-channel). If you find a new issue, please let us know by [filing a bug](https://crbug.com/). The [community help forum](https://support.google.com/chrome/community) is also a great place to reach out for help or learn about common issues.

Google Chrome
