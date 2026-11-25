# PortSwigger Access Control Masterclass

- **Source URL:** https://medium.com/@furkannyildiizz05/portswigger-access-control-masterclass-mass-assignment-ve-idor-%C3%A7e%C5%9Fitleri-440255ab46e4
- **Fetched from:** https://medium.com/@furkannyildiizz05/portswigger-access-control-masterclass-mass-assignment-ve-idor-%C3%A7e%C5%9Fitleri-440255ab46e4?source=rss-53768bce8ff1------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14941)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Furkannyildiizz / Fri, 09 Oct 2026 17:36:42 GMT

[🇬🇧 **Read this article in English:**](https://medium.com/@furkannyildiizz05/portswigger-access-control-notes-mass-assignment-and-idor-variants-c10b2a70cd50?postPublishedType=initial)

PortSwigger Web Security Academy’nin Access Control (Erişim Kontrolü) bölümünde ilerlerken birbiriyle doğrudan bağlantılı 3 farklı labı tamamladım. Bu yazıda, kullanıcı profilindeki rol değiştirme (Mass Assignment) ile başlayıp, hem basit IDOR hem de tahmin edilemeyen GUID kullanan IDOR senaryolarını ve arkasındaki mantığı inceliyoruz.

1\. Kullanıcı Profilinde Yetki Yükseltme (Mass Assignment)

Mantık ve Analoji:

Bu durum, bir spor salonuna kayıt olurken üyelik formundaki adresinizi güncellerken formun altına kalemle “Üyelik Tipi: VIP” yazmanıza ve resepsiyonun bunu hiç sorgulamadan sistemde onaylamasına benzer.

Çözüm Adımları:

1. PortSwigger tarafından verilen wiener:peter hesabı ile giriş yapıp /my-account sayfasına gittim.

2. E-posta adresimi değiştirmek için form üzerinden bir güncelleme isteği attım.

3. Burp Suite’te HTTP history altından POST /my-account/change-email isteğini bulup Ctrl + R ile Repeater’a gönderdim.

4. İstek ve yanıt parametrelerini incelediğimde varsayılan olarak “roleid”: 1 değerinin bulunduğunu fark ettim.

5. İstek gövdesindeki (Request Body) JSON verisini düzenleyerek mail parametresinin altına “roleid”: 2 ekledim:

{“email”: “[test@test.com](mailto:test@test.com)”, “roleid”: 2}

6\. Send butonuna bastığımda sunucu bu parametreyi kabul etti ve yanıtta rolümün güncellendiği doğrulandı.

7. Sayfayı yenilediğimde admin paneli geldi ve panele girip carlos kullanıcısını silerek labı tamamladım.

Kök Neden:

Arka plan uygulaması (backend), istemciden gelen JSON verisini herhangi bir filtreleme veya beyaz liste (whitelist) kontrolü yapmadan doğrudan veritabanı modeline bağlıyor (Mass Assignment).

2\. İstek Parametresi ile Kontrol Edilen Kullanıcı ID’si (Klasik IDOR)

Mantık ve Analoji:

Bir otel resepsiyonuna gidip “101 numaralı odanın anahtarını verir misiniz?” dediğinizde kimlik doğrulaması yapılmadan anahtarın verilmesi; ardından “202 numaralı odanın anahtarını da verir misiniz?” dediğinizde yine kontrol edilmeden o odanın anahtarının da teslim edilmesidir.

Çözüm Adımları:

1. wiener:peter hesabı ile giriş yapıp kendi profil sayfama geçtim.

2. Burp Suite HTTP history sekmesinden profil verilerimi getiren isteği inceledim: GET /my-account?id=wiener

3. İsteği Repeater’a gönderdim ve id=wiener parametresini id=carlos olarak değiştirdim.

4. Send butonuna bastığımda sunucu Carlos’un profil sayfasını döndürdü. Yanıt içerisindeki API anahtarını kopyalayıp çözüm olarak gönderdim.

Kök Neden:

Sunucu, URL üzerinden gelen id parametresini işliyor ancak oturum sahibi (Session) ile erişilmek istenen hesabın eşleşip eşleşmediğini doğrulamıyor.

3\. Tahmin Edilemeyen ID’ler ve GUID Kullanımı (GUID IDOR)

Mantık ve Analoji:

Otel yönetimi bu sefer oda numaralarını 101, 102 gibi tahmin edilebilir sayılar yerine karmaşık kilit kodlarıyla (A9-X7-K2) değiştiriyor. Ancak resepsiyonist hala kimlik kontrolü yapmıyor. Yan odadaki müşterinin kilit kodunu panoda veya koridorda gören herkes o kodu söyleyip odaya girebiliyor.

Çözüm Adımları:

1. wiener:peter ile giriş yapıp profilime gittiğimde URL’de kullanıcı adı yerine karmaşık bir GUID (/my-account?id=YOUR-GUID) olduğunu gördüm.

2. Profil isteğimi Repeater’a aktardıktan sonra hedef kullanıcı olan Carlos’un GUID değerini bulmam gerekiyordu.

3. Sitenin ana sayfasındaki blog gönderilerini inceledim ve Carlos tarafından yazılmış bir gönderi buldum.

4. Yazar adına/yazıya tıkladığımda Burp Suite HTTP history üzerinde oluşan isteği inceleyerek Carlos’a ait GUID değerini yakaladım (/blog?userId=carlos-guid).

5. Bu GUID değerini kopyalayıp Repeater’daki kendi profil isteğimin id parametresine yapıştırdım ve Send butonuna bastım.

6. Dönen yanıttan Carlos’un API anahtarını kopyalayıp sisteme girerek labı çözdüm.

Kök Neden:

Geliştiriciler kullanıcı ID’lerini GUID yaparak tahmin edilmesini zorlaştırmış, fakat yetkilendirme kontrolünü (Authorization) unuttukları için zafiyet devam etmiştir. Bu durum “Gizlilik Yoluyla Güvenlik” (Security through Obscurity) yanılgısının tipik bir örneğidir.

Önleme Yöntemleri (Remediation)

- Mass Assignment: Profil güncelleme gibi işlemlerde DTO (Data Transfer Object) yapıları kullanılmalı ve istemciden kabul edilecek parametreler kesin olarak sınırlandırılmalıdır (whitelist).

- IDOR: Sunucu tarafında her istek işlenmeden önce oturum açan kullanıcının yetkisi ile istenen nesnenin sahibi mutlaka doğrulanmalıdır (Session.UserID == RequestedObject.OwnerID).
