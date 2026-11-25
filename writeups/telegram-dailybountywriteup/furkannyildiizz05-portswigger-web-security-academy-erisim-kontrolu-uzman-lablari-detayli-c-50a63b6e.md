# PortSwigger Web Security Academy Erisim Kontrolu Uzman Lablari Detayli Cozum Serisi

- **Source URL:** https://medium.com/@furkannyildiizz05/portswigger-web-security-academy-erisim-kontrolu-uzman-lablari-detayli-cozum-serisi-cb967a8d4fc9
- **Fetched from:** https://medium.com/@furkannyildiizz05/portswigger-web-security-academy-erisim-kontrolu-uzman-lablari-detayli-cozum-serisi-cb967a8d4fc9?source=rss-53768bce8ff1------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14949 (id 14949)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Furkannyildiizz / Thu, 15 Oct 2026 14:27:30 GMT

[🇬🇧 **Read this article in English:**](https://medium.com/@furkannyildiizz05/portswigger-web-security-academy-access-control-expert-labs-detailed-solution-series-d5fbbbd7bdbb?sharedUserId=furkannyildiizz05)

Giris

PortSwigger Web Security Academy uzerindeki Erisim Kontrolu modulunun en kritik 4 uzman seviye labini tamamladik. Bu yazida, web uygulamalarindaki yetkilendirme mimarilerinin nerelerden acik verebilecegini, bu zafiyetlerin arkasindaki mantigi ve adim adim cozum sureclerini detayli bir sekilde inceliyoruz.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

Lab 1: URL-Based Access Control Can Be Circumscribed (X-Original-URL)

Zafiyetin Tanimi ve Mantigi:

Modern web mimarilerinde disaridan gelen istekler once bir on uc sistem (Reverse Proxy / WAF) tarafindan karsilanir. Bu on uc, guvenlik politikasi geregi disaridan /admin gibi hassas yollara dogrudan erisimi engeller. Ancak arka uc uygulamasi, gelen isteklerin orijinal yolunu takip edebilmek icin X-Original-URL gibi ozel HTTP basliklarini (headers) destekliyorsa, bu durum guvenlik duvarinin atlatilmasina neden olur. On yuz zararsiz bir ana sayfa istegini onaylarken, arka uc basliktaki /admin adresini isleme alir.

Adim Adim Cozum Sureci:

1. Tarayici uzerinden /admin adresine dogrudan gitmeye calisilir ve on uc sistem tarafindan engellendigi (403 Forbidden) gozlemlenir.

2. Istek Burp Suite Repeater aracina gonderilir. Istek satirindaki adres ana sayfaya cekilir ve baslik kismina X-Original-URL: /invalid degeri eklenir. Sistemden “bulunamadi” yanitinin alinmasi, arka uc sistemin bu basligi isleme aldigini kanitlar.

3. Baslik degeri X-Original-URL: /admin olarak guncellenir. Bu sayede on yuz istegi guvenli zannedip gecirirken, arka uc yonetici panelini ekrana getirir.

4. Hedef kullanici olan carlos’u silmek icin baslik degeri X-Original-URL: /admin/delete?username=carlos olarak degistirilir ve istek gonderilerek lab tamamlanir.

Lab 2: Method-Based Access Control Can Be Circumscribed

Zafiyetin Tanimi ve Mantigi:

Bazi web uygulamalarinda hassas islemler (yetki yukseltme, kullanici silme vb.) icin uygulanan yetki kontrolleri yanlis bir sekilde sadece belirli HTTP metodlarina (ornegin sadece POST isteklerine) baglanir. Gelistirici, ayni islemin GET veya baska bir metotla yapilabilecegini hesaba katmas. Yetkisiz bir kullanici, oturum çerezini degistirip istek metodunu manipule ederek bu korumayi asabilir.

Adim Adim Cozum Sureci:

1. Yonetici hesabiyla sisteme giris yapilir, bir kullanicinin yetkisi yukseltilir ve bu sirada olusan istek Burp Suite HTTP History uzerinden bulunarak Repeater’a gonderilir.

2. Yonetici oturumundan cikis yapilarak normal bir kullanici ile sisteme giris yapilir.

3. Repeater’daki istegin icerisinde bulunan yonetici oturum cerezi silinerek yerine normal kullanici olan wiener’in oturum cerezi yapistirilir.

4. Istegin metodu POST iken “Change request method” ozelligi kullanilarak GET yapilir. Guvenlik filtresi sadece POST isteklerini denetledigi icin GET istegi kontrolsuz bir sekilde arka uca ulasir ve wiener kullanicisi yonetici konumuna yukseltilir.

Lab 3: Multi-Step Process with No Access Control on One Step

Zafiyetin Tanimi ve Mantigi:

Kullanici yetkilendirme veya rol degistirme gibi kritik islemler birden fazla adimdan olusabilir. Bazi uygulamalarda gelistirici, guvenlik kontrolunu sadece ilk adima koyar; ancak islem sonlandirildigi ikinci adimda kullanicinin yetkisini tekrar kontrol etmeyi unutur. Bu durumda saldirgan dogrudan ikinci adimin istegini tetikleyerek yetkisiz islem yapabilir.

Adim Adim Cozum Sureci:

1. Yonetici hesabiyla giris yapilarak bir kullaniciyi admin yapma islemi gerceklestirilir ve bu cok adimli surecin son onay istegi Burp Suite uzerinden yakalanip Repeater’a gonderilir.

2. Yonetici oturumu kapatilip wiener hesabiyla giris yapilir ve wiener’in oturum cerezi degeri kopyalanir.

3. Repeater’daki istegin icindeki oturum cerezi, wiener’in cerezi ile degistirilir.

4. Istek icerisindeki hedef kullanici adi wiener olarak duzenlenip dogrudan son adim tetiklenir. Sunucu, islem sonuc adiminda yetki kontrolu yapmadigi icin wiener kullanicisi basariyla yonetici yapilir.

Lab 4: Referer-Based Access Control

Zafiyetin Tanimi ve Mantigi:

Bazi web uygulamalari, hassas bir istegin yetkili bir kaynaktan gelip gelmedigini dogrulamak icin guvenli oturum çerezleri yerine tarayicinin gonderdigi Referer basligina guvenir. Saldirgan, istek gonderirken Referer basligina yonetici paneli adresini yazarak sunucuyu kandirabilir; sunucu oturum sahibinin normal bir kullanici olup olmadigina bakmaksizin sadece Referer basligina inanarak islemi onaylar.

Adim Adim Cozum Sureci:

1. Yonetici hesabiyla giris yapilip bir kullanici admin yapilir ve olusan istek Burp Suite Repeater’a gonderilir.

2. Sistemden cikis yapilarak normal kullanici ile giris yapilir ve wiener’in oturum cerezi kopyalanir.

3. Repeater’daki istekte yer alan oturum cerezi silinerek yerine wiener’in cerezi yapistirilir.

4. Istek basliklari arasinda bulunan Referer degerinin yonetici paneli yolunu gosterdiginden emin olunur. Istek gonderildiginde sunucu, cereze bakmak yerine Referer basligina inandigi icin wiener kullanicisinin yetkisini basariyla yukseltir.
