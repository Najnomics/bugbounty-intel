# هل مازلت محتار في الاختلاف بين Reflected XSS و DOM XSS؟ اليوم ستحسم المسألة بكل ثقة

- **Source URL:** https://gentilsecurity.medium.com/%D9%87%D9%84-%D9%85%D8%A7%D8%B2%D9%84%D8%AA-%D9%85%D8%AD%D8%AA%D8%A7%D8%B1-%D9%81%D9%8A-%D8%A7%D9%84%D8%A7%D8%AE%D8%AA%D9%84%D8%A7%D9%81-%D8%A8%D9%8A%D9%86-reflected-xss-%D9%88-dom-xss-%D8%A7%D9%84%D9%8A%D9%88%D9%85-%D8%B3%D8%AA%D8%AD%D8%B3%D9%85-%D8%A7%D9%84%D9%85%D8%B3%D8%A3%D9%84%D8%A9-%D8%A8%D9%83%D9%84-%D8%AB%D9%82%D8%A9-c4224d126056?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240722200414/https://gentilsecurity.medium.com/%D9%87%D9%84-%D9%85%D8%A7%D8%B2%D9%84%D8%AA-%D9%85%D8%AD%D8%AA%D8%A7%D8%B1-%D9%81%D9%8A-%D8%A7%D9%84%D8%A7%D8%AE%D8%AA%D9%84%D8%A7%D9%81-%D8%A8%D9%8A%D9%86-reflected-xss-%D9%88-dom-xss-%D8%A7%D9%84%D9%8A%D9%88%D9%85-%D8%B3%D8%AA%D8%AD%D8%B3%D9%85-%D8%A7%D9%84%D9%85%D8%B3%D8%A3%D9%84%D8%A9-%D8%A8%D9%83%D9%84-%D8%AB%D9%82%D8%A9-c4224d126056?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6288 (id 6288)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# هل مازلت محتار في الاختلاف بين Reflected XSS و DOM XSS؟ اليوم ستحسم المسألة بكل ثقة

## اليوم سنشرح النوع الأكثر صعوبة في ثغرات ال XSS وهو ال DOM-Based XSS

ولكن شرح النهاردة سيجعل هذا النوع بالنسبة لك أسهل نوع, فقط اقرأ بتركيز.

سنقوم بالشرح علي Portswigger Lab لتوصيل المعلومة بشكل مبسط.

**عنوان ال LAB الذي سنقوم بالتطبيق عليه “DOM XSS in document.write sink using source location.search”**

## إذا كنت تفضل مشاهدة الشرح عن طريق فيديو علي يوتيوب لفهم المعلومة بشكل اوضح وأسرع, أنصحك بمشاهدة هذا الفيديو والذي يشرح بالتفصيل ما يتم شرحه هنا في هذه المقالة.

*الخطوة الأولي:*

# سنقوم بعمل Analysis لل DOM

بعد الدخول إلي الـ LAB سنقوم بأدخال أي قيمة غير موجودة بالموقع , علي سبيل المثال “gentil”

عندما سنكتب “gentil” داخل مربع البحث سنلاحظ انه يتم طباعتها مرتين داخل ال DOM مرة بين \<h1> Tag ومرة اخري داخل \<img> Tag تحديدآ داخل ال src

**وسنلاحظ ان ال \<img> Tag بيتم تمرير القيمة له عن طريق javascript وهنا سنقف قليلآ لنفهم مايدور**

## ماهي القيمة التي يتم تمريرها الي ال \<img> Tag ؟

هيا الكلمة التي يتم البحث عنها في خانة البحث وفي حالتنا هذه سيتم تمرير كلمة “gentil” والتي بحثنا عنها في خانة البحث.

كيف يتم تمريرها الي ال \<img> Tag ؟

عن طريق javascript code .

## ولماذا يتم تمريرها الي javascript code هذا ؟

لنفهم لماذا يقوم المصمم بتمرير القيمة التي أدخلناها في خانة البحث الي javascript يجب علينا تحليل كود ال javascript لنفهم ما يقوم به.

هذا الكود ال javascript الذي نراه هو كود يقوم بأخذ الكلمات التي تم البحث عنها في خانة البحث داخل الصفحة وأرسالها الي الخادم (server) ليتم الأحتفاظ بهم جميعآ في مكان واحد.

## وما الفائدة التي تعود علي صاحب الموقع عندما يقوم بتجميع الكلمات التي تم البحث عنها داخل موقعه؟

**الإجابة ببساطة:**

ليحسن من المحتوي الذي يقدمه, عندما يعرف مايتم البحث عنه بكثرة داخل موقعه

سيقوم بالتركيز عليه واعطاءه الأولوية.

**كمثال:**لو كان موقعه هو موقع متخصص في الآمن السيبراني


وكان اكثر عمليات البحث التي تتم داخل موقعه هذا هي عمليات بحث عن أدوات أختبار الأختراق

فسيركز بنسبة كبيرة علي تقديم محتوي عن أدوات أختبار الأختراق

## معني هذا الكلام انه بدون كود ال javascript هذا ستعمل عملية البحث بدون أي مشاكل؟

**نعم, بالظبط** 

أن هذا الكود لا يؤثر علي عملية البحث داخل الموقع فممكن بكل بساطة الأستغناء عنه تمامآ وسيتظل عملية البحث تعمل بكل كفائة.

*الخطوة الثانية:*

# **قي ثغرة DOM-Based XSS يجب عليك قراءة الكود وتحليله لتعرف اذا كان به أي خطأ يمكنك استغلاله كمختبر أختراق.**

ولذلك سنقوم الآن بتحليل كود Javascript السابق لنعرف كيف يقوم ال Developer بأخذ القيمة التي يتم ادحالها في خانة البحث, وماهو الخطأ الذي وقع فيه أدي الا ثغرة DOM XSS.


function trackSearch(query) {

document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');

}


var query = (new URLSearchParams(window.location.search)).get('search');


if(query) {

trackSearch(query);

}
## **أولآ الهدف:**

هو يريد أرسال الكلمات التي يتم البحث عنها الي الخادم (server)

ولذلك اختار أن ينفذ هذه المهمة عن طريق img Tag وتحديدآ داخل ال src 

لنفهم ذلك, ال img عندما يطلب صورة معينة من الخادم (server) فيقوم بكتابة مسار الصورة التي يريدها داخل src.

## هكذا:

`<img src="/resources/images/tracker.gif" />`
في هذه الحالة هذا هو مسار الصورة المطلوبة من الخادم (server) /resources/images/tracker.gif

## بعد ما فهمنا أن img Tag يتحدث مع السيرفر فكيف سيقوم ال Developer بأرسال القيمة التي ادخلناها في خانة البحث مع ال img Request ؟

سيقوم المصمم بأرسال القيمة التي ادخلناها داخل خانة البحث الي الخادم عن طريق كتابة 

*?searchTerms=’gentil’*

بعد */resources/images/tracker.gif*

لتصبح هكذا

*/resources/images/tracker.gif?searchTerms=’gentil’*

لنفهم الأن علامة الأستفهام “؟” تعني “و” وكأنه يقول للخادم

يا خادم اريد منك الصورة التي في هذا المسار /resources/images/tracker.gif و ياخادم خذ هذه القيمة “gentil” وقم بتخزينها داخل searchTerms وأحفظها داخل ال server فأنا سأحتاج اليها لاحقآ .

فيرد الخادم (server) في ال Response ويقول له تفضل هذه هي الصورة التي طلبتها مني, ولا تقلق لقد قمت بحفظ القيمة التي ارسلتها لي داخل searchTerms في السيرفر ويمكنك الرجوع لها في أي وقت اذا احتجتها.

**فهمنا الآن ان المصمم يستغل طلب الصورة من الخادم (server) لأرسال القيمة التي أدخلناها في خانة البحث وحفظها بداخله.**

## فأين هي الصورة ؟ ولماذا اختار هذه الطريقة بالذات لأرسال قيم البحث الي الخادم؟

الصورة حجمها يكون 

1x1 px

فأنك لن تراها لأنها صغيرة جدآ ولا يتم ملاحظتها, اصلآ الغرض من استدعاء هذه الصورة من الخادم ليس لعرضها داخل الموقع, وأنما قام المصمم فقط بأستخدام هذه الطريقة لأنها تعتبر طريقة بسيطة وغير معقدة ولا تؤثر علي سرعة معالجة الصفحة لأرسال القيم التي يتم البحث عنها داخل موقعه ولكن لسوء حظه انه قام بكتابتها بطريقة غير آمنة أدت الي حدوث DOM-Based XSS وهذا يوضح ايضآ لماذا قام المصم بأختيار هذه الطريقة بالذات لأرسال القيم إلي الخادم وحفظها بداخله.

*ثانيآ :*

# لنفهم كيف يقوم المصمم بالحصول علي القيمة التي قمنا بأدخالها وتمريرها داخل Javascript

`var query = (new URLSearchParams(window.location.search)).get('search');`
في هذا السطر يقوم المصمم بالحصول علي جميع ال Parameters التي من ضمنها ال parameter الخاص بخانة البحث عن طريق window.location.search وأرسال جميع الParameters الي URLSearchParams Object ليستخرج قيمة ال parameter (‘search’) وهيا التي بحثنا عنها ويخزنها داخل متغير بأسم query ليقوم بأرسال هذا المتغير لاحقآ الي function تقوم بأخذ قيمة ال query هذا وأضافته داخل img Request الذي شرحناه سابقآ وتكون ال function تعمل بهذا الشكل.

```
function trackSearch(query) {
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
}
```
document.write هذا DOM والذي وظيفته كتابة كود HTML داخل الصفحة عن طريق Javascript code وبداخله 

(‘\<img src=”/resources/images/tracker.gif?searchTerms=’+query+’”>’)

وهنا يقول للخادم أن قيمة searchTerms ستكون query 

و query هي الكلمة التي قام المستخدم بالبحث عنها

فبهذا الشكل يكون قد أرسل القيمة التي قمنا بالبحث عنها داخل خانة البحث الي الخادم وحفظها بداخله لأستخدامها لاحقآ بدون أن يضغط علي الصفحة وبدون كتابة كود javascript معقد.

*الخطوة الثالثة:*

# لنفهم ماهو الخطأ الذي ارتكبه ال Developer في كتابة كود Javascript لتحدث ثغرة ال DOM XSS

```
function trackSearch(query) {
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
}
```
في هذا الكود قام ال Developer بأخذ القيمة التي قام المستخدم بالبحث عنها ومررها الي javascript بدون عمل encoding لها بدون أن يشفرها.

فلتعديل هذا الكود ليصبح آمن كان يجب كتابتة بهذا الشكل:

```
function trackSearch(query) {
  var img = document.createElement('img');
  img.src = '/resources/images/tracker.gif?searchTerms=' + encodeURIComponent(query);
  document.body.appendChild(img);
}
```
فهنا encodeURIComponent(query) قمنا بتشفير القيمة التي أدخلها المستخدم داخل خانة البحث وبعدها قمنا بأضافتها للصفحة عن طريق ال DOM هكذا document.body.appendChild(img)

فبهذا الشكل نكون قد شفرنا المدخلات وعملنا المطلوب بطريقة آمنة.

*الخطوة الرابعة:*

# كيفية حقن alert function داخل خانة البحث

**أولآ لنلقي نظرة مرة آخري علي ال img Tag لأننا سوف نحقن الكود بداخلة  لأنه هو النتيجة الأخيرة التي يتم كتابتها داخل ال Dom**

`<img src="/resources/images/tracker.gif?searchTerms=gentil">`
يمكنك بسهولة معرفة كيفية حقن كود javascript داخل img Tag عن طريق البحث داخل Google وستظهر لك آلاف النتائج

سيكون الحقن بهذا الشكل

`gentil" onload="alert('XSS')`
ليصبح في النهاية بهذا الشكل

`<img src="/resources/images/tracker.gif?searchTerms=gentil" onload="alert('XSS')">`
هنا قمت بقفل ال Double Quotation و بعدها قمت بأضافة Attribute اسمه onload ومعناه عند تحميل الصفحة نفذ القيمة التي سأعطيها لك وفي هذه الحالة القيمة هي alert(‘XSS’)

وعند آخذ هذا ال Payload “ gentil” onload=”alert(‘XSS’) “ واضافتة في خانة البحث وضغطنا علي Search سينفذ لنا كود ال alert function بهذا الشكل

*نأتي الآن للسؤال الأكثر أنتشارآ*

# ماهو الفرق بين Reflected XSS و DOM-Based XSS

الصورة السابقة توضح الفرق الجوهري بين Reflected XSS و DOM-Based XSS

## Reflected XSS:

Reflected XSS لا تسطتيع التعامل مع المتصفح مباشرتآ يجب ان يكون هناك وسيط بينك وبين المتصفح لتنفذ عليه كود Javascript.

*كمثال:*

انت تخبر ال server المصاب بثغرة Reflected XSS وتطلب منه في ال Request (من فضلك سأكتب لك 123) قم بأرجاعها لي كما هيا في ال Response, فيأخذ منك الطلب بالفعل ويعكسه لك كما هو كما طلبت أنت منه, فأنت أرسلت في الطلب 123 وهو رأه ولم يأتي بجانبه وأرسله اليك مره آخري بدون عمل آي تعديل عليه (عكسه لك مرة أخري).

فهذا هو ال Reflected XSS يجبرك بالتعامل مع الserver ليتم تنفيذ ماتطلبه علي المتصفح 

فأن المتصفح يثق في ال Server ولا يثق فيك آنت فلذلك كان هو الوسيط بينك وبين المتصفح.

## DOM-Based XSS:

في DOM XSS أنت تقوم بالتحدث مباشرتآ الي المتصفح لا تحتاج لوسيط (server)

الكود الذي ستقوم بأدخاله في المكان المصاب سيتم تنفيذه مباشرتآ علي المتصفح بدون أن يأخذ المتصفح الآذن من الخادم (Server) سيتم تنفيذ الكود الذي تعطيه له في المكان المصاب بالثغرة.

هذا هو الفرق الأساسي بين Reflected XSS و DOM-Based XSS آتمني ان تنال المقالة آعجابكم ولا تنسوا المتابعة اذا كنتم مهتمين بمحتوي Web Application Peneteration Testing و Bug Bounty و CyberSecurity بشكل عام فأدعوكم أيضآ بالأشتراك في قناتي علي Youtube فهي تحتوي علي فيديوهات مهمة لكل من يريد البدأ أو الأحتراف في مجال ال Web Application Peneteration Testing و Bug Bounty ويتم تسجيل كورس وتنزل حلقاتة اولآ بأول علي القناة يوميآ ليأخذك من المستوي المبتدأ الي المستوي الخبير آن شاء الله.

# Youtube Channel:

آدعوكم ايضآ لمتابعة حساباتي علي ال Social Media اذا كنت مهتمين بالحصول علي احدث اخبار ال Cyber Security أو اذا كان لديكم أي استفسار فلا تتردوا في التواصل معي في أقرب وقت.

## Facebook:

[https://www.facebook.com/ahmedhamdy0x/](https://web.archive.org/web/20240722200414/https://www.facebook.com/ahmedhamdy0x/)
