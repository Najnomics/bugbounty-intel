# PortSwigger Notes

- **Source URL:** https://medium.com/@furkannyildiizz05/portswigger-notes-access-control-zafiyet-t%C3%BCrleri-ve-analizi-b%C3%B6l%C3%BCm-1-f446c7e0d54e
- **Fetched from:** https://medium.com/@furkannyildiizz05/portswigger-notes-access-control-zafiyet-t%C3%BCrleri-ve-analizi-b%C3%B6l%C3%BCm-1-f446c7e0d54e?source=rss-53768bce8ff1------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14938 (id 14938)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Furkannyildiizz / Wed, 07 Oct 2026 16:37:59 GMT

[🇬🇧 **Read this article in English:**](https://medium.com/@furkannyildiizz05/portswigger-notes-access-control-vulnerability-types-and-analysis-part-1-47aaf04f6188)

Siber güvenlik yolculuğumda PortSwigger Web Security Academy üzerindeki Access Control (Erişim Kontrolü) zafiyetlerini incelemeye başladım. Bu serinin ilk yazısında; siber güvenliğe yeni başlayanların mantığını kolayca anlayabileceği, kıdemli uzmanların ise teknik detayları inceleyebileceği bir derinlikte en yaygın 3 yetkilendirme hatasını inceliyoruz.

— -

ACCESS CONTROL (ERİŞİM KONTROLÜ) NEDİR?

Bir web sitesini büyük bir otel gibi düşünün. Otelin lobisine herkes girebilir (Genel sayfalar), ancak otel odalarına sadece anahtarı olan müşteriler (Giriş yapmış kullanıcılar) ve yönetim odasına sadece otel müdürü (Admin) girebilir.

Access Control, sunucunun “Bu isteği yapan kişi gerçekten bu odaya girmeye yetkili mi?” kontrolünü yaptığı güvenlik katmanıdır. Bu katmandaki mantık hataları, yetkisiz kişilerin başkalarının verilerine veya yönetim panellerine erişmesine yol açar.

1\. SENARYO: KORUMASIZ ADMİN PANELİ (UNPROTECTED ADMIN PANEL)

Günlük Hayat Benzetmesi (Analoji)

Bir mağaza düşünün. Mağaza sahibi kasa odasının kapısına “Yetkisiz Girilemez” kilidi takmak yerine, kapının üzerindeki “Kasa Odası” tabelasını söküyor ve kapıyı arka tarafta gizli bir koridora saklıyor. Kapı açık ve kilitli değil; sadece görünmüyor. Yoldan geçen biri tesadüfen o koridora girerse kasaya doğrudan erişebiliyor.

Siber güvenlikte buna “Security through Obscurity” (Gizlilik Yoluyla Güvenlik) denir. Bir şeyi gizlemek, onu korumak anlamına gelmez.

Teknik Analiz ve Zafiyet Mantığı

Arama motoru botlarının (Google, Bing vb.) siteyi taramasını düzenleyen robots.txt dosyası kamuya açık bir dosyadır. Geliştirici, botlar girmesin diye gizli panel yolunu buraya eklediğinde, aslında saldırganlara panelin adresini kendi eliyle vermiş olur.

Keşif ve Sömürü Aşamaları

1\. Gelişmiş Bilgi Toplama (Reconnaissance):

Uygulamanın kök dizinindeki robots.txt dosyasını talep ettim:

GET /robots.txt HTTP/1.1

Host: target-app.web-security-academy.net

2\. Dizin Tespiti:

Sunucudan dönen yanıtta botların girmesi istenmeyen “gizli” dizin açıkça görünüyordu:

HTTP/1.1 200 OK

Content-Type: text/plain

User-agent: \*

Disallow: /administrator-panel

3\. Yetkilendirme Bypass (Authorization Bypass):

Tarayıcıdan doğrudan /administrator-panel adresine gittiğimde sunucu hiçbir oturum veya rol kontrolü yapmadan yönetim panelini yükledi. Panel üzerinden carlos kullanıcısını silerek zafiyeti kanıtladım.

2\. SENARYO: İSTEMCİ TARAFINDA GÜVENLİK MANTIĞI (UNPREDICTABLE ADMIN URL)

Günlük Hayat Benzetmesi (Analoji)

Bir tiyatro salonundasınız. Bilet kontrolörü, sahne arkasına geçen kapının önüne bir perde çekiyor ve perdeye “VIP değilseniz burayı göremezsiniz” yazıyor. Ancak perdeyi elinizle kenara çektiğinizde arkadaki kapının kilitli olmadığını ve içeriye rahatça girebildiğinizi görüyorsunuz.

İstemci tarafında (Client-Side) çalışan JavaScript kodları bu perde gibidir; kullanıcının tarayıcısında çalıştığı için herkes tarafından incelenebilir.

Teknik Analiz ve Zafiyet Mantığı

Geliştiriciler yönetim panelini /admin-qu46kr gibi karmaşık ve tahmin edilemez bir URL arkasına koymuş ve kullanıcı Admin değilse butonu ekrana çizdirimemiştir. Ancak buton gizlense bile yönlendirdiği adresi JavaScript kodunun içine açık metin (plain text) olarak yazmak devasa bir mantık hatasıdır.

1\. Kaynak Kod Analizi (Source Code Review):

Sayfa kaynağını (View Source) incelediğimde, arayüzü şekillendiren şu JavaScript kodunu tespit ettim:

var isAdmin = false;

if (isAdmin) {

var topLinksTag = document.getElementsByClassName(“top-links”)\[0\];

var adminPanelTag = document.createElement(‘a’);

adminPanelTag.setAttribute(‘href’, ‘/admin-qu46kr’);

adminPanelTag.innerText = ‘Admin panel’;

topLinksTag.append(adminPanelTag);

}

2\. Sömürü:

Koddaki href parametresinde açıkça duran /admin-qu46kr adresini kopyalayıp tarayıcı adres çubuğuna yapıştırdım. Sunucu kontrol yapmadığı için yönetim paneli açıldı ve carlos kullanıcısı silindi.

3\. SENARYO: MANİPÜLE EDİLEBİLİR ÇEREZLER (USER ROLE CONTROLLED BY COOKIE)

Günlük Hayat Benzetmesi (Analoji)

Bir etkinliğe girerken görevli göğsünüze “Sıradan Ziyaretçi” yazan sıradan bir etiket yapıştırıyor. Siz tuvalete gidip tükenmez kalemle o etiketi çizip “Organizatör / VIP” yazıyorsunuz. Güvenlik görevlisi kimliğinizi veya sistemdeki kaydınızı kontrol etmek yerine sadece göğsünüzdeki etikete bakarak sizi VIP alanına alıyor.

İşte HTTP Çerezleri (Cookies) kullanıcının bilgisayarında duran bu etiketlerdir. Kullanıcı dilediği gibi değiştirebilir.

Teknik Analiz ve Zafiyet Mantığı

Web güvenliğinin altın kuralı şudur: İstemciden (tarayıcıdan) gelen hiçbir veriye güvenilmez. Sunucu, kullanıcının rolünü doğrularken tarayıcının gönderdiği Admin=false veya Admin=true çerezine körü körüne inanıyorsa yetki yükseltme (Privilege Escalation) zafiyeti oluşur.

1\. İstek Trafiğinin Yakalanması (Burp Suite):

Sisteme wiener:peter kullanıcı bilgileriyle giriş yaptım. Burp Suite -> HTTP History sekmesinden istekleri inceledim.

2\. Çerez (Cookie) Analizi:

Sunucuya giden istek başlıklarında (Headers) rol bilgisinin düz metin olarak taşındığını gördüm:

GET /my-account?id=wiener HTTP/1.1

Host: target-app.web-security-academy.net

Cookie: Admin=false; session=…

3\. Çerez Manipülasyonu:

İsteği Burp Suite Repeater modülüne gönderdim (Ctrl+R). Admin=false değerini Admin=true olarak değiştirdim.

Aynı işlemi tarayıcının geliştirici araçlarında (DevTools -> Application -> Cookies) gerçekleştirip sayfayı yeniledim.

4\. Yönetim Paneline Erişim:

Sunucu gönderdiğim Admin=true çerezine güvenerek beni yönetici olarak algıladı ve /admin panelini açtı. Buradan carlos kullanıcısı silindi.

KOD SEVİYESİNDE ÖNLEME (REMEDIATION / HOW TO FIX?)

Bu 3 senaryodaki temel güvenlik zafiyetlerinin önüne geçmek için geliştiricilerin dikkat etmesi gereken noktalar:

1\. Güvenliği Gizliliğe Bağlamayın: Hassas uç noktalar mutlaka rol tabanlı erişim kontrolü (RBAC) ile korunmalıdır.

2. İstemciye Güvenmeyin: Kullanıcı rolleri istemci tarafındaki çerezlerde düz metin olarak saklanmamalıdır.

3. Sunucu Tarafında Güvenli Kontrol (Örnek Python/Flask):

[@app](http://twitter.com/app).route(‘/admin’)

def admin\_panel():

if session.get(‘user\_role’) != ‘ADMIN’:

return “Erişim Engellendi / Yetkisiz İşlem”, 403


return render\_template(‘admin.html’)

— -

\*PortSwigger üzerindeki pratiklerimi ve teknik notlarımı paylaşmaya devam edeceğim.\*
