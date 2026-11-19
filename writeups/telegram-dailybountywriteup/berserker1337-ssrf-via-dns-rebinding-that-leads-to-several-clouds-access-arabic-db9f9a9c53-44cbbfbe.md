# SSRF via DNS Rebinding That Leads to Several Clouds Access (Arabic)

- **Source URL:** https://medium.com/@Berserker1337/ssrf-via-dns-rebinding-that-leads-to-several-clouds-access-arabic-db9f9a9c530c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241027164301/https://medium.com/@Berserker1337/ssrf-via-dns-rebinding-that-leads-to-several-clouds-access-arabic-db9f9a9c530c
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7153 (id 7153)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SSRF via DNS Rebinding That Leads to Several Clouds Access (Arabic)

السلام عليكم ورحمة الله وبركاته اليوم طبعا كتبت المقال هذا لاثراء المحتوى العربي في اكتشاف الثغرات وامن المواقع. اللهم انفعني بما علمتني, وعلمني ماينفعني, وارزقني علما تنفعني به.

بالبداية بتكلم معك على انك فاهم الثغرة وراح اشرح ال(DNS rebinding) عشان يوضح لكم كل شي هي تقنية معينه نستخدمه في حال اذا بغينا نتخطى (Same-Origin Policy) والمخترق يستغلها بطريقه تلاعب انه يسمي دومينه بأي اسم ثم يجعل الدومين يرتبط في شبكه داخليه للضحية مثل (127.0.0.1 أو 192.168) أو خدمات سحابية، وبكذا يقدر يستغل ثغرات عديده وهذي صوره للشرح المبسط والاستفادة منها في سيناريوهات معينة


خلوني اشرح لكم ليش نستخدمها بكل بساطه عشان نتخطى جدار الحمايه الي موجود في الموقع ويسوي لنا حظر كل ماحاولنا نسوي اتصال على الخادم السحابي (169.254.169.254) زي ماهو موضح عندكم بالصوره الي تحت


مثل ماهو موضح لكم معطيني حظر من جدار الحماية ال(WAF) حاولت طرق كثيره في التخطيات وولا وحده ضبطت معي الين جربت (DNS rebinding) في البارمتر وعشان نجربها نروح للذا [الموقع](https://lock.cmpxchg8b.com/rebinder.html)


ونرجع للبارمتر ونحط ذا الرابط [http://7f000001.a9fea9fe.rbndr.us](http://7f000001.a9fea9fe.rbndr.us) ثم بعد ماجربته عطاني رد السيرفر بالبدايه ماخفي عليكم فقدت الامل انه ماراح تضبط لكن جربت على العموم لان ممكن تضبط وذا الي يفرق في اكتشافك للثغرات انك تجرب اي شي يجي ببالك.


تخطيته لكن مافيه نتيجه هنا نروح نبحث عن الملفات الي ممكن تكون موجوده في الخادم السحابي واول شي جربته الي هو ملفات ال (AWS) جربتها كلها لكن ماجابت نتيجه. شفت انه ماجابت نتيجه جربت ملفات ثانيه على امل ان فيه سيرفرات سحابيه واقدر القى نتيجه ممكن تكون حرجه وهذي اكثر صفحة فادتني \[[https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery/cloud-ssrf](https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery/cloud-ssrf)\]. استعملت هذا الملف وشغلت ال (intruder) عليه بحيث انه يبحث ويشوف اذا عطانا اي نتيجه.


```
/latest/user-data
/latest/user-data/iam/security-credentials/[ROLE NAME]
/latest/meta-data/iam/security-credentials/[ROLE NAME]
/latest/meta-data/ami-id
/latest/meta-data/reservation-id
/latest/meta-data/hostname
/latest/meta-data/public-keys/0/openssh-key
/latest/meta-data/public-keys/[ID]/openssh-key
/latest/meta-data/
/computeMetadata/v1/
/computeMetadata/v1/instance/hostname
/computeMetadata/v1/instance/id
/computeMetadata/v1/project/project-id
/computeMetadata/v1/instance/disks/
/computeMetadata/v1beta1/
/opc/v1/instance
/metadata/v1.json
/metadata/v1/
/metadata/v1/id
/metadata/v1/user-data
/metadata/v1/hostname
/metadata/v1/region
/metadata/v1/interfaces/public/0/ipv6/address
/metadata/v1/maintenance
/metadata/instance?api-version=2017-04-02
/metadata/instance/network/interface/0/ipv4/ipAddress/0/publicIpAddress?api-version=2017-04-02&format=text
/openstack
/openstack/latest
/openstack/latest/meta_data.json
/2009-04-04/meta-data/
/latest/
/latest/attributes/
/latest/meta-data/
/latest/meta-data/instance-id
/latest/meta-data/image-id
```
وبالفعل عطانا نتايج وبعرضها لكم تحت:


وبكذا قدرنا نتخطى الحمايه الموجوده ونحصل ثغرة حرجة. بكتب الخطوات وملخص للي سويناه.


- **الخطوة الاولى:**

استخدم خدمة إعادة ربط (DNS) مثل [rbndr.us](https://lock.cmpxchg8b.com/rebinder.html).

سو الدومين الخاص فيك بحيث انه يشير في البداية إلى (localhost)، وبعدها الى الشبكة الداخلية الي تحاول توصل لها في هذه الحالة (169.254.169.254).


- **الخطوة الثانية:**

ارسل الطلب باستخدام الدومين الي سويته، أرسل الطلب إلى [http://7f000001.a9fea9fe.rbndr.us/opc/v1/instance/metadata](http://7f000001.a9fea9fe.rbndr.us/opc/v1/instance/metadata)

في البداية، ممكن يظهر لك خطأ (404) أو ما يعطيك النتيجة الي تتوقعها.


- **الخطوة الثالثة:**

بعد ماتجاوزت جدار الحماية (WAF)، استخدم (Intruder) في (Burp Suite) للبحث في ملفات للمواقع السحابية مثل ماوضحت في المسارات الي فوق.

جرب مسارات مثل:

`/latest/user-data`

`/latest/meta-data/`

`/computeMetadata/v1/`

وغيرها من المسارات الي تستهدف خوادم سحابية محددة مثل (AWS وOracle).

**الخطوة الرابعة:**إذا كانت الثغرة موجودة، بتحصل على نتائج من الخادم السحابي. على سبيل المثال، بتحصل معلومات حساسه مثل المفاتيح العامة(SSH) أو عناوين البريد الإلكتروني المخزنة في الخادم. وللمعلومية اذا حصلت خادم (AWS) راح تقدر تتحكم بالخادم السحابي بشكل كامل وممكن يترقى الى (RCE) في بعض الحالات.


وبكذا اقدر اقول ان هذي نهاية المقال واتمنى انكم استفدتم فعلا واذا احتجتم مساعدة في اكتشاف الثغرات او توضيح لهذه الثغرة تواصلو معي في حسابي في اكس تحصلونه بالبايو، اذا استفدت اتمنى دعوه في ظهر الغيب.
