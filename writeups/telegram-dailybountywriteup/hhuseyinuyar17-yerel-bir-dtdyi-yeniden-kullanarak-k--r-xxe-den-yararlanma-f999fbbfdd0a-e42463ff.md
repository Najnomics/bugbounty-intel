# Yerel bir DTD’yi yeniden kullanarak kör XXE’den yararlanma

- **Source URL:** https://medium.com/@hhuseyinuyar17/yerel-bir-dtdyi-yeniden-kullanarak-k%C3%B6r-xxe-den-yararlanma-f999fbbfdd0a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240313080057/https://medium.com/@hhuseyinuyar17/yerel-bir-dtdyi-yeniden-kullanarak-k%C3%B6r-xxe-den-yararlanma-f999fbbfdd0a
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5415 (id 5415)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Yerel bir DTD’yi yeniden kullanarak kör XXE’den yararlanma

Bu XXE saldırısı, sunucu dosya sistemindeki mevcut bir DTD’nin yeniden tasarlanmasını içerdiğinden, temel gereksinim uygun bir dosyanın bulunmasıdır. Bu aslında oldukça basittir. Uygulama, XML ayrıştırıcısı tarafından atılan herhangi bir hata mesajını döndürdüğü için, yerel DTD dosyalarını yalnızca dahili DTD’den yüklemeyi deneyerek kolayca numaralandırabilirsiniz.

Örneğin, GNOME masaüstü ortamını kullanan Linux sistemlerinde genellikle `/usr/share/yelp/dtd/docbookx.dtd`. Aşağıdaki XXE verisini göndererek bu dosyanın mevcut olup olmadığını test edebilirsiniz; dosya eksikse hataya neden olur:

**XXE zafiyeti nedir?**

XXE, XML Dış Etiketi Enjeksiyonu’nun (XML External Entity Injection) kısaltmasıdır. XXE zafiyeti, bir XML işlemleyicinin, dış kaynaklara başvurabilecek XML dış etiketlerini işleme yeteneği nedeniyle ortaya çıkar. Bir saldırgan, hedef uygulamanın XML tabanlı veri işleme işlevselliğini kötüye kullanarak, genellikle hassas sistem bilgilerini ifşa etmek veya sistemdeki dosyalara erişmek için XML dış etiketlerini manipüle edebilir.

Bir XXE saldırısı, uygulama tarafından gelen XML verisi içerisindeki bir dış etiketi kullanarak yapılır. Bu etiket, saldırganın belirli bir amaç için dış kaynakları çağırmasına veya hedef sistemdeki dosyalara erişmesine izin verebilir. Örneğin, bir saldırganın XML dökümanı içerisine yerleştirdiği bir dış etiket, saldırganın hedef sistemdeki hassas dosyalara erişmesine izin verebilir. Bu dosyalar, veritabanı bağlantı bilgileri, parolalar, kullanıcı bilgileri veya diğer hassas veriler olabilir.

XXE zafiyeti, kötü niyetli kullanıcıların uygulamaları istismar etmesine ve hassas bilgilere erişmesine olanak tanıyabilir. Bu nedenle, geliştiricilerin güvenlik önlemleri alarak XML işleme işlevselliğini güvenli hale getirmeleri önemlidir. Bu önlemler arasında girdi doğrulaması, güvenli XML ayrıştırma yapılandırmaları ve XML dış etiketlerinin devre dışı bırakılması gibi yöntemler bulunmaktadır.

**XXE ile DTD arasındaki ilişki nedir?**

XXE (XML External Entity Injection) zafiyeti ile DTD (Document Type Definition — Belge Tür Tanımı) arasında yakın bir ilişki vardır. DTD, bir XML belgesinin yapısını tanımlayan bir yapısal dil ve XML belgelerinin doğruluğunu kontrol etmek için kullanılır. XXE saldırıları genellikle DTD’lerin işlenmesi sırasında ortaya çıkar.

XXE saldırıları genellikle XML dökümanı içindeki DTD tanımını kullanarak gerçekleştirilir. Saldırgan, DTD tanımı içinde dış etiketler (external entities) tanımlayarak, uygulamanın dış kaynaklara başvurmasını sağlar. Bu dış etiketler, genellikle saldırganın kontrolündeki uzak sunucuları veya dosyaları işaret eder. Saldırgan, bu yolla hassas bilgilere erişebilir veya uygulamada istenmeyen işlemler gerçekleştirebilir.

Özetle, XXE zafiyeti genellikle DTD tanımlarının kullanılması sırasında ortaya çıkar ve saldırganların DTD içindeki dış etiketler aracılığıyla uygulamayı istismar etmesine olanak tanır. Bu nedenle, güvenli XML işleme için DTD işleme mekanizmalarının dikkatlice yapılandırılması ve güvenlik önlemlerinin alınması önemlidir.

# XXE zafiyetini deneyebileceğimiz yeri bulabilmek için Burp Suite’den yararlanma;

Zafiyetin arandığı site içerisindeki sayfalar (endpointler) Burp Suite bağlı olarak gezilir BU gezdiğimiz siteler arasında toplu geniş kapsamlı arama yapabilmek için Burp Suite’nin Target>Site map>Arama yapmak istedğimiz site seçilir ve sağ tık ile>Engagments tools>Searc seçilir.

Search kısmına xml yazılarak zafiyeti deneyebileceğimiz parametreleri görebiliriz.

Content-Type ve parametreler xml formatında değilse;

```
POST /action HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 7
foo=bar
```
gibiyse xml’e çevrilerek denenebilir:

```
POST /action HTTP/1.0
Content-Type: text/xml
Content-Length: 52
<?xml version="1.0" encoding="UTF-8"?><foo>bar</foo>
```
Uygulama, mesaj gövdesinde XML içeren istekleri tolere ediyorsa ve gövde içeriğini XML olarak ayrıştırıyorsa, istekleri XML biçimini kullanacak şekilde yeniden biçimlendirerek gizli XXE saldırı yüzeyine ulaşabilirsiniz.


Denenebilecek parametreleri bulduk ancak buralarda hangi payloadlar ile deneme yapabiliriz bunları bilmemiz gerekmemektedir. Öncelikle ilk payload sistemdeki yerel bir DTD’yi nasıl bulabiliriz Bunun için payload [aşağıdaki gibi olmalıdır.](https://portswigger.net/web-security/xxe/blind#exploiting-blind-xxe-by-repurposing-a-local-dtd)

Ve istek Intruder’e atılarak DTD’nin konumuna brute force atılabilir.

Intruderin payloads kısmına liste oluşturmak için github’dan faydalanabilirsiniz:

Bir DTD’nin varlığını Brute Force’dan anlayabilmek için Status kodunun 200 olması gerekmektedir.

Var olan DTD’yi bulduk bunu kendi amacımıza kullanabilmek için bu DTD içerisindeki kullanıp manipüle edebileceğimiz parametre varlığını bulmamız gerekiyor bunun için google’den yardım alabiliriz. Aratacağımız şey Brute Forcede bulunan yoldur. [/usr/share/yelp/dtd/docbookx.dtd](https://github.com/GNOME/yelp/blob/master/data/dtd/docbookx.dtd)

GNOME masaüstü ortamını kullanan sistemler genellikle /usr/share/yelp/dtd/docbookx.dtd adresinde ***ISOamso*** adlı bir varlık içeren bir DTD’ye sahip olduğu anlaşılmıştır


Yerel bir DTD nin parametre varlığını manipüle ederek kullanabileceğimiz [payload şudur.](https://portswigger.net/web-security/xxe/blind#exploiting-blind-xxe-by-repurposing-a-local-dtd)

- `local_dtd`Sunucu dosya sisteminde bulunan harici DTD dosyasının içeriğini içeren, adı verilen bir XML parametre varlığını tanımlar .
- `ISOamso`Harici DTD dosyasında zaten tanımlanmış olan adlı XML parametre varlığını yeniden tanımlar . Varlık, dosyanın içeriğini içeren bir hata mesajını tetiklemek `/etc/passwd` içerecek şekilde yeniden tanımlanır .
- `local_dtd`Varlığın yeniden tanımlanmış değeri de dahil olmak üzere harici DTD'nin yorumlanması için varlığı kullanır `ISOamso`. Bu istenen hata mesajıyla sonuçlanır.

istek Repeatere atılarak zafiyetten sömürü sağlanabilir.

Zaman ayırdığınız için teşekkürler…🙂🙂🙂

Daha fazla bilgi için kaynaklar:
