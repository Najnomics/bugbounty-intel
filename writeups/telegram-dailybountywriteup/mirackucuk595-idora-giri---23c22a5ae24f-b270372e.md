# IDOR’a Giriş

- **Source URL:** https://medium.com/@mirackucuk595/idora-giri%C5%9F-23c22a5ae24f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240604104431/https://medium.com/@mirackucuk595/idora-giri%C5%9F-23c22a5ae24f
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5690 (id 5690)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR’a Giriş

Insecure Direct Object References (IDOR) güvenlik açıkları en yaygın web güvenlik açıkları arasındadır ve savunmasız web uygulamasını önemli ölçüde etkileyebilir. IDOR güvenlik açıkları, bir web uygulaması, son kullanıcının diğer benzer nesnelere erişim elde etmek için doğrudan kontrol edebileceği bir dosya veya veritabanı kaynağı gibi bir nesneye doğrudan bir referans gösterdiğinde ortaya çıkar. Sağlam bir erişim kontrol sisteminin olmaması nedeniyle herhangi bir kullanıcı herhangi bir kaynağa erişebiliyorsa, sistemin savunmasız olduğu kabul edilir.

Sağlam bir erişim kontrol sistemi oluşturmak çok zordur, bu nedenle IDOR güvenlik açıkları yaygındır. Buna ek olarak, erişim kontrol sistemlerindeki zayıflıkları tespit etme sürecini otomatikleştirmek de oldukça zordur, bu da bu güvenlik açıklarının üretime ulaşana kadar tespit edilememesine yol açabilir.

Örneğin, kullanıcılar yakın zamanda yükledikleri bir dosyaya erişim talep ettiklerinde, (download.php?file\_id=123) gibi bir bağlantı alabilirler. Bağlantı doğrudan (file\_id=123) ile dosyaya referans verdiğine göre, (download.php?file\_id=124) ile başka bir dosyaya (bize ait olmayabilir) erişmeye çalışırsak ne olur? Eğer web uygulaması back-end üzerinde uygun bir erişim kontrol sistemine sahip değilse, herhangi bir dosyaya onun file\_id’si ile bir istek göndererek erişebiliriz. Çoğu durumda, id’nin kolayca tahmin edilebilir olduğunu görebiliriz, bu da izinlerimize dayanarak erişmememiz gereken birçok dosyayı veya kaynağı almamızı mümkün kılar.

## Bir IDOR Zafiyetini Oluşturan Nedir?

Dahili bir nesne ya da kaynağa doğrudan referans göstermek kendi başına bir güvenlik açığı değildir. Ancak bu durum başka bir güvenlik açığından yararlanmayı mümkün kılabilir: zayıf bir erişim kontrol sistemi. Birçok web uygulaması, kullanıcıların kaynaklara erişimini, bu kaynakları alabilecek sayfalara, işlevlere ve API’lere erişimlerini kısıtlayarak engeller. Ancak, bir kullanıcı bir şekilde bu sayfalara erişirse (örneğin, paylaşılan/taklit edilen bir bağlantı aracılığıyla) ne olur? Sadece erişim bağlantısına sahip olarak aynı kaynaklara erişmeye devam edebilecekler mi? Eğer web uygulaması back-end’de kullanıcının kimlik doğrulamasını kaynağın erişim listesiyle karşılaştıran bir erişim kontrol sistemine sahip değilse, bunu yapabilirler.

Web uygulamaları için sağlam bir erişim kontrol sistemi uygulamanın Rol Tabanlı Erişim Kontrolü ([RBAC](https://en.wikipedia.org/wiki/Role-based_access_control)) sistemine sahip olmak gibi birçok yolu vardır. Ana çıkarım, bir IDOR güvenlik açığının esas olarak back-end’de bir erişim kontrolünün olmaması nedeniyle var olduğudur. Bir kullanıcının erişim kontrolü olmayan bir web uygulamasındaki nesnelere doğrudan referansları varsa, saldırganların diğer kullanıcıların verilerini görüntülemesi veya değiştirmesi mümkün olabilir.

Birçok geliştirici bir erişim kontrol sistemi oluşturmayı göz ardı eder; bu nedenle, çoğu web uygulaması ve mobil uygulama back-end’de korumasız bırakılır. Bu tür uygulamalarda, tüm kullanıcılar back-end’deki diğer tüm kullanıcıların verilerine keyfi olarak erişebilir. Kullanıcıların diğer kullanıcıların verilerine erişmesini engelleyen tek şey, yalnızca kullanıcının verilerini göstermek üzere tasarlanmış olan uygulamanın front-end uygulaması olacaktır. Bu gibi durumlarda, HTTP isteklerini manuel olarak manipüle etmek, tüm kullanıcıların tüm verilere tam erişime sahip olduğunu ortaya çıkarabilir ve başarılı bir saldırıya yol açabilir.

Tüm bunlar, IDOR güvenlik açıklarını herhangi bir web veya mobil uygulama için en kritik güvenlik açıkları arasına sokar, yalnızca doğrudan nesne referanslarını açığa çıkarması nedeniyle değil, esas olarak sağlam bir erişim kontrol sisteminin olmaması nedeniyle. Temel bir erişim kontrol sisteminin geliştirilmesi bile zor olabilir. İşlevlerine müdahale etmeden tüm web uygulamasını kapsayan kapsamlı bir erişim kontrol sistemi daha da zor bir görev olabilir. Bu nedenle IDOR/Erişim Kontrolü güvenlik açıkları Facebook, Instagram ve Twitter gibi çok büyük web uygulamalarında bile bulunmaktadır.

## IDOR Güvenlik Açıklarının Etkisi

Daha önce de belirtildiği gibi, IDOR güvenlik açıkları web uygulamaları üzerinde önemli bir etkiye sahip olabilir. IDOR güvenlik açığının en temel örneği, kişisel dosyalar veya kredi kartı verileri gibi bizim için erişilebilir olmaması gereken diğer kullanıcıların özel dosyalarına ve kaynaklarına erişmektir ve bu IDOR Bilgi İfşa Güvenlik Açıkları olarak bilinir. Maruz kalınan doğrudan referansın niteliğine bağlı olarak, güvenlik açığı diğer kullanıcıların verilerinin değiştirilmesine veya silinmesine bile izin verebilir, bu da hesabın tamamen ele geçirilmesine yol açabilir.

Bir saldırgan, veritabanı kimlikleri veya URL parametreleri olabilecek doğrudan referansları belirledikten sonra, herhangi bir veriye erişip erişemeyeceklerini görmek için belirli kalıpları test etmeye başlayabilir ve sonunda herhangi bir rastgele kullanıcı için verilerin nasıl çıkarılacağını veya değiştirileceğini anlayabilir.

IDOR güvenlik açıkları, IDOR Güvensiz İşlev Çağrıları ile kullanıcı ayrıcalıklarının standart bir kullanıcıdan yönetici bir kullanıcıya yükseltilmesine de yol açabilir. Örneğin, birçok web uygulaması, web uygulamasının front-end kodunda yalnızca yönetici işlevleri için URL parametrelerini veya API’leri açığa çıkarır ve bu işlevleri yönetici olmayan kullanıcılar için devre dışı bırakır. Bu durumda, kullanıcıların parolalarını değiştirmek veya kullanıcılara belirli roller vermek gibi yetkisiz yönetim işlemleri gerçekleştirebiliriz ve bu da sonunda tüm web uygulamasının tamamen ele geçirilmesine yol açabilir.

## IDOR’ların Belirlenmesi

## URL Parametreleri ve API’ler

IDOR güvenlik açıklarından yararlanmanın ilk adımı Doğrudan Nesne Referanslarını belirlemektir. Belirli bir dosya veya kaynak aldığımızda, nesne referansı içeren URL parametrelerini veya API’leri aramak için HTTP isteklerini incelemeliyiz (örneğin ?uid=1 veya ?filename=file\_1.pdf). Bunlar çoğunlukla URL parametrelerinde veya API’lerde bulunur, ancak cookie’ler gibi diğer HTTP başlıklarında da bulunabilir.

En temel durumlarda, (?uid=2) veya (?filename=file\_2.pdf) gibi diğer verileri almak için nesne referanslarının değerlerini artırmayı deneyebiliriz. Ayrıca binlerce varyasyonu denemek ve herhangi bir veri döndürüp döndürmediklerini görmek için bir fuzzing uygulaması kullanabiliriz. Bize ait olmayan dosyalara başarılı bir şekilde ulaşılması bir IDOR güvenlik açığına işaret edecektir.

## AJAX Calls

Front-end kodunda JavaScript AJAX çağrıları şeklinde kullanılmayan parametreleri veya API’leri de tespit edebiliriz. JavaScript framework’lerinde geliştirilen bazı web uygulamaları, tüm işlev çağrılarını güvenli olmayan bir şekilde front-end’e yerleştirebilir ve kullanıcı rolüne göre uygun olanları kullanabilir.

Örneğin, bir yönetici hesabımız olmasaydı, yönetici işlevleri devre dışı bırakılırken yalnızca kullanıcı düzeyindeki işlevler kullanılırdı. Bununla birlikte, front-end JavaScript koduna bakarsak ve doğrudan nesne referansları içeren belirli uç noktalara veya API’lere yapılan AJAX çağrılarını belirleyebilirsek, yönetici işlevlerini yine de bulabiliriz. JavaScript kodunda doğrudan nesne referanslarını tespit edersek, bunları IDOR güvenlik açıkları için test edebiliriz.

Bu elbette yönetici işlevlerine özgü değildir, HTTP isteklerinin izlenmesi yoluyla bulunamayacak herhangi bir işlev veya çağrı da olabilir. Aşağıdaki örnekte temel bir AJAX çağrısı örneği gösterilmektedir:

Web uygulamasını yönetici olmayan bir kullanıcı olarak kullandığımızda yukarıdaki fonksiyon hiçbir zaman çağrılmayabilir. Bununla birlikte, front-end kodunda bulursak, değişiklik yapmak için çağırıp çağıramayacağımızı görmek için farklı şekillerde test edebiliriz, bu da IDOR’a karşı savunmasız olduğunu gösterir. Aynı şeyi, erişimimiz varsa back-end kodu için de yapabiliriz (örneğin, açık kaynaklı web uygulamaları).

## Hashing/Kodlamayı Anlama

Bazı web uygulamaları nesne referansı olarak basit sıralı sayılar kullanmayabilir, bunun yerine referansı kodlayabilir ya da hashleyebilir. Kodlanmış veya hashlenmiş değerler kullanan bu tür parametreler bulursak, back-end’de erişim kontrol sistemi yoksa bunları yine de istismar edebiliriz.

Referansın yaygın bir kodlayıcı (örneğin base64) ile kodlandığını varsayalım. Bu durumda, kodu çözebilir ve nesne referansının düz metnini görüntüleyebilir, değerini değiştirebilir ve ardından diğer verilere erişmek için tekrar kodlayabiliriz. Örneğin, (?filename=ZmlsZV8xMjMucGRm) gibi bir referans görürsek, dosya adının base64 kodlu olduğunu (karakter kümesinden) hemen tahmin edebiliriz ve (file\_123.pdf) orijinal nesne referansını elde etmek için kodunu çözebiliriz. Ardından, farklı bir nesne referansını (örn. file\_124.pdf) kodlamayı deneyebilir ve kodlanmış nesne referansıyla (?filename=ZmlsZV8xMjQucGRm) erişmeyi deneyebiliriz; bu, herhangi bir veriyi alabildiysek bir IDOR güvenlik açığını ortaya çıkarabilir.

Öte yandan, nesne referansı (download.php?filename=c81e728d9d4c2f636f067f89cc14862c) gibi hashlenmiş olabilir. İlk bakışta, herhangi bir açık metin veya kolay kodlama kullanmadığı için bunun güvenli bir nesne referansı olduğunu düşünebiliriz. Ancak kaynak koda bakarsak, API çağrısı yapılmadan önce neyin hashlendiğini görebiliriz:

Bu durumda, kodun dosya adını kullandığını ve CryptoJS.MD5 ile hashlediğini görebiliriz, bu da diğer potansiyel dosyalar için dosya adını hesaplamamızı kolaylaştırır. Aksi takdirde, kullanılan hash algoritmasını manuel olarak tanımlamaya çalışabilir (örneğin, hash tanımlayıcı araçlarla) ve ardından kullanılan hash ile eşleşip eşleşmediğini görmek için dosya adını hash edebiliriz. Diğer dosyalar için hash’leri hesaplayabildiğimizde, bunları indirmeyi deneyebiliriz, bu da bize ait olmayan herhangi bir dosyayı indirebilirsek bir IDOR güvenlik açığını ortaya çıkarabilir.

## Kullanıcı Rollerini Karşılaştırın

Daha gelişmiş IDOR saldırıları gerçekleştirmek istiyorsak, birden fazla kullanıcıyı kaydetmemiz ve HTTP isteklerini ve nesne referanslarını karşılaştırmamız gerekebilir. Bu, URL parametrelerinin ve benzersiz tanımlayıcıların nasıl hesaplandığını anlamamıza ve daha sonra verilerini toplamak için diğer kullanıcılar için bunları hesaplamamıza olanak sağlayabilir.

Örneğin, iki farklı kullanıcıya erişimimiz olsaydı, bunlardan biri aşağıdaki API çağrısını yaptıktan sonra maaşını görüntüleyebilirdi:

İkinci kullanıcı, çağrıyı çoğaltmak için bu API parametrelerinin tümüne sahip olmayabilir ve Kullanıcı1 ile aynı çağrıyı yapamayabilir. Ancak, elimizdeki bu ayrıntılarla, web uygulamasının herhangi bir şey döndürüp döndürmediğini görmek için Kullanıcı2 olarak oturum açmışken aynı API çağrısını tekrarlamayı deneyebiliriz. Bu tür durumlar, web uygulaması API çağrısı yapmak için yalnızca geçerli bir oturum açmış olmayı gerektiriyorsa ancak backend’de çağrıyı yapan kişinin oturumunu çağrılan verilerle karşılaştırmak için herhangi bir erişim kontrolü yoksa işe yarayabilir.

Durum böyleyse ve diğer kullanıcılar için API parametrelerini hesaplayabiliyorsak, bu bir IDOR güvenlik açığı olacaktır. Diğer kullanıcılar için API parametrelerini hesaplayamasak bile, yine de back-end erişim kontrol sisteminde bir güvenlik açığı tespit etmiş oluruz ve istismar etmek için başka nesne referansları aramaya başlayabiliriz.

## Toplu IDOR Numaralandırma

IDOR güvenlik açıklarından faydalanmak bazı durumlarda kolaydır ancak bazı durumlarda çok zorlayıcı olabilir. Potansiyel bir IDOR’u tespit ettiğimizde, başka herhangi bir veriyi açığa çıkarıp çıkarmayacağını görmek için temel tekniklerle test etmeye başlayabiliriz. Gelişmiş IDOR saldırılarına gelince, temel tekniklerle istismar edilemeyecek gelişmiş saldırılar gerçekleştirebilmek için web uygulamasının nasıl çalıştığını, nesne referanslarını nasıl hesapladığını ve erişim kontrol sisteminin nasıl çalıştığını daha iyi anlamamız gerekir.

Temel numaralandırmadan toplu veri toplamaya ve kullanıcı ayrıcalıklarını artırmaya kadar IDOR güvenlik açıklarından yararlanmanın çeşitli tekniklerini tartışmaya başlayalım.

## Güvensiz Parametreler

Tipik bir IDOR güvenlik açığını gösteren temel bir örnekle başlayalım. Aşağıdaki alıştırma, çalışan kayıtlarını barındıran bir Employee Manager web uygulamasıdır:

Web uygulamamız, işleri basitleştirmek için uid=1 kullanıcı kimliğine sahip bir çalışan olarak oturum açtığımızı varsayar. Bu, gerçek bir web uygulamasında kimlik bilgileriyle oturum açmamızı gerektirecektir, ancak saldırının geri kalanı aynı olacaktır. Documents’a tıkladığımızda şu adrese yönlendiriliriz

`/documents.php`:

Documents (Belgeler) sayfasına geldiğimizde, kullanıcımıza ait birkaç belge görüyoruz. Bunlar kullanıcımız tarafından yüklenen dosyalar olabileceği gibi başka bir departman (örneğin İK Departmanı) tarafından bizim için ayarlanmış dosyalar da olabilir. Dosya bağlantılarını kontrol ettiğimizde, bireysel isimlere sahip olduklarını görüyoruz:

Dosyaların tahmin edilebilir bir adlandırma modeline sahip olduğunu görüyoruz, çünkü dosya adları kullanıcı uid’sini ve dosya adının bir parçası olarak ay / yılı kullanıyor gibi görünüyor, bu da diğer kullanıcılar için dosyaları fuzz etmemize izin verebilir. Bu en temel IDOR güvenlik açığı türüdür ve statik dosya IDOR’u olarak adlandırılır. Ancak, diğer dosyaları başarılı bir şekilde fuzz’lamak için, hepsinin Invoice veya Report ile başladığını varsayarız, bu da bazı dosyaları ortaya çıkarabilir, ancak hepsini değil. Bu yüzden, daha sağlam bir IDOR açığı arayalım.

Sayfanın uid değerimizi URL’deki bir GET parametresiyle (documents.php?uid=1) olarak ayarladığını görüyoruz. Eğer web uygulaması bu uid GET parametresini göstermesi gereken çalışan kayıtlarına doğrudan bir referans olarak kullanıyorsa, sadece bu değeri değiştirerek diğer çalışanların belgelerini görüntüleyebiliriz. Eğer web uygulamasının back-end ucu düzgün bir erişim kontrol sistemine sahipse, bir çeşit Access Denied alacağız. Ancak, web uygulamasının uid’mizi doğrudan referans olarak açık metin olarak geçtiği göz önüne alındığında, bu, çalışan kayıtlarına keyfi erişime yol açan zayıf web uygulaması tasarımına işaret edebilir.

Uid’yi ?uid=2 olarak değiştirmeyi denediğimizde, sayfa çıktısında herhangi bir fark görmüyoruz, çünkü hala aynı belge listesini alıyoruz ve hala kendi belgelerimizi döndürdüğünü varsayabiliriz:

Bununla birlikte, herhangi bir web pentesti sırasında sayfa ayrıntılarına dikkat etmeli ve her zaman kaynak kodunu ve sayfa boyutunu göz önünde bulundurmalıyız. Bağlantılı dosyalara bakarsak veya görüntülemek için üzerlerine tıklarsak, bunların gerçekten de farklı dosyalar olduğunu ve uid=2 olan çalışana ait belgeler gibi göründüğünü fark edeceğiz:

Bu, IDOR güvenlik açıklarından muzdarip web uygulamalarında rastlanan yaygın bir hatadır, çünkü back-end’de hiçbir erişim kontrol sistemi yokken hangi kullanıcı belgelerinin gösterileceğini kontrol eden parametreyi bizim kontrolümüze verirler. Bir başka örnek de, yalnızca belirli bir kullanıcının belgelerini görüntülemek için bir filtre parametresi kullanmaktır (örneğin uid\_filter=1), bu parametre diğer kullanıcıların belgelerini göstermek için manipüle edilebilir veya hatta tüm belgeleri bir kerede göstermek için tamamen kaldırılabilir.

## Toplu Numaralandırma

Diğer çalışan belgelerine uid=3, uid=4 vb. ile manuel olarak erişmeyi deneyebiliriz. Ancak, yüzlerce veya binlerce çalışanın bulunduğu gerçek bir çalışma ortamında dosyalara manuel olarak erişmek verimli değildir. Bu nedenle, tüm dosyaları almak için Burp Intruder veya ZAP Fuzzer gibi bir araç kullanabilir veya tüm dosyaları indirmek için küçük bir bash betiği yazabiliriz, ki biz de bunu yapacağız.

Eleman denetçisini etkinleştirmek için Firefox’ta \[CTRL+SHIFT+C\] tuşlarına tıklayabilir ve ardından HTML kaynak kodlarını görüntülemek için bağlantılardan herhangi birine tıklayabiliriz ve aşağıdakileri elde ederiz:

```
<li class='pure-tree_link'><a href='/documents/Invoice_3_06_2020.pdf' target='_blank'>Invoice</a></li>
<li class='pure-tree_link'><a href='/documents/Report_3_01_2020.pdf' target='_blank'>Report</a></li>
```
Dosyanın bağlantısını grepleyebilmek için herhangi bir benzersiz kelime seçebiliriz. Bizim durumumuzda, her bağlantının \<li class=’pure-tree\_link’> ile başladığını görüyoruz, bu nedenle sayfayı kıvırabilir ve bu satırı aşağıdaki gibi grepleyebiliriz:

`M1R4CKCK@htb[/htb]$ curl -s "http://SERVER_IP:PORT/documents.php?uid=1" | grep "<li class='pure-tree_link'>"````
<li class='pure-tree_link'><a href='/documents/Invoice_3_06_2020.pdf' target='_blank'>Invoice</a></li>
<li class='pure-tree_link'><a href='/documents/Report_3_01_2020.pdf' target='_blank'>Report</a></li>
```
Gördüğümüz gibi, belge bağlantılarını başarıyla yakalayabildik. Artık ekstra kısımları kırpmak ve çıktıda yalnızca belge bağlantılarını almak için belirli bash komutlarını kullanabiliriz. Bununla birlikte, /document ve .pdf arasındaki dizelerle eşleşen bir Regex kalıbı kullanmak daha iyi bir uygulamadır, bunu aşağıdaki gibi yalnızca belge bağlantılarını almak için grep ile kullanabiliriz:

`M1R4CKCK@htb[/htb]$ curl -s "http://SERVER_IP:PORT/documents.php?uid=3" | grep -oP "\/documents.*?.pdf"````
/documents/Invoice_3_06_2020.pdf
/documents/Report_3_01_2020.pdf
```
Şimdi, uid parametresi üzerinde döngü yapmak ve tüm çalışanların belgelerini döndürmek için basit bir for döngüsü kullanabilir ve ardından her belge bağlantısını indirmek için wget’i kullanabiliriz:

`#!/bin/bash`
url="http://SERVER\_IP:PORT"for i in {1..10}; do

for link in $(curl -s "$url/documents.php?uid=$i" | grep -oP "\/documents.\*?.pdf"); do

wget -q $url/$link

done

done

Komut dosyasını çalıştırdığımızda, 1–10 arasında uid’ye sahip tüm çalışanların tüm belgelerini indirecek ve böylece tüm çalışanların belgelerini toplu olarak numaralandırmak için IDOR güvenlik açığından başarıyla yararlanacaktır. Bu betik, aynı hedefe nasıl ulaşabileceğimizin bir örneğidir. Burp Intruder veya ZAP Fuzzer gibi bir araç kullanmayı deneyin veya tüm belgeleri indirmek için başka bir Bash veya PowerShell betiği yazın.

## Makine Çözümü 1-

Soru : Bu bölümde öğrendiklerinizi tekrarlayarak /documents.php dosyasındaki ilk 20 kullanıcı uid’sine ait belgelerin bir listesini alın, bunlardan biri bayraklı bir ‘.txt’ dosyasına sahip olmalıdır.

1- Bu sefer POST isteğinde uid parametresi konulmuş

2- Toplu olarak indirmek için kullandığım bash betiği . (Düzenlenmiş)

## Kodlanmış Referansları Bypass Etme

Önceki bölümde, çalışan kimliklerini açık metin olarak kullanan ve numaralandırmayı kolaylaştıran bir IDOR örneği gördük. Bazı durumlarda, web uygulamaları nesne referanslarını hash haline getirir veya kodlar, bu da numaralandırmayı daha zor hale getirir, ancak yine de mümkün olabilir.

Sözleşmeler işlevselliğini test etmek için Employee Manager web uygulamasına geri dönelim:

Employment\_contract.pdf dosyasına tıklarsak, dosyayı indirmeye başlar. Burp’ta durdurulan istek aşağıdaki gibi görünür:

Aşağıdaki verilerle download.php’ye bir POST isteği gönderdiğini görüyoruz:

Dosyaları indirmek için bir download.php betiği kullanmak, çoklu web saldırıları ile istismar edilebileceğinden, dosyalara doğrudan bağlantı vermekten kaçınmak için yaygın bir uygulamadır. Bu durumda, web uygulaması doğrudan referansı açık metin olarak göndermiyor, ancak bir md5 biçiminde hash ediyor gibi görünüyor. Hash’ler tek yönlü fonksiyonlardır, bu nedenle orijinal değerlerini görmek için kodlarını çözemeyiz.

Uid, kullanıcı adı, dosya adı ve diğerleri gibi çeşitli değerleri hash etmeyi deneyebilir ve md5 hash’lerinden herhangi birinin yukarıdaki değerle eşleşip eşleşmediğine bakabiliriz. Bir eşleşme bulursak, bunu diğer kullanıcılar için çoğaltabilir ve dosyalarını toplayabiliriz. Örneğin, uid’mizin md5 hash’ini karşılaştırmayı deneyelim ve yukarıdaki hash ile eşleşip eşleşmediğine bakalım:

Ne yazık ki, hash’ler eşleşmiyor. Bunu diğer çeşitli alanlarla deneyebiliriz, ancak hiçbiri hash’imizle eşleşmez. Gelişmiş durumlarda, Burp Comparer’ı da kullanabilir ve çeşitli değerleri fuzz’layabilir ve ardından herhangi bir eşleşme bulup bulmadığımızı görmek için her birini hash’imizle karşılaştırabiliriz. Bu durumda, md5 hash’i benzersiz bir değer veya tahmin edilmesi çok zor olan bir değer kombinasyonu için olabilir ve bu doğrudan referansı Güvenli Doğrudan Nesne Referansı yapar. Ancak, bu web uygulamasında ölümcül bir kusur var.

## Fonksiyon Açıklaması

Çoğu modern web uygulaması Angular, React veya Vue.js gibi JavaScript framework’leri kullanılarak geliştirildiğinden, birçok web geliştiricisi hassas işlevleri front-end üzerinde gerçekleştirme hatasına düşebilir ve bu da onları saldırganlara açık hale getirebilir. Örneğin, yukarıdaki hash front-end’de hesaplanıyor olsaydı, fonksiyonu inceleyebilir ve ardından aynı hash’i hesaplamak için ne yaptığını kopyalayabilirdik. Neyse ki bu web uygulamasında durum tam olarak böyle.

Kaynak koddaki bağlantıya bakarsak, javascript:downloadContract(‘1’) ile bir JavaScript işlevi çağırdığını görürüz. Kaynak koddaki downloadContract() fonksiyonuna baktığımızda aşağıdakileri görüyoruz:

Bu fonksiyon, yukarıda gördüğümüz gibi contract parametresiyle bir POST isteği gönderiyor gibi görünüyor. Gönderdiği değer, CryptoJS kütüphanesini kullanan bir md5 hash’idir ve bu da daha önce gördüğümüz istekle eşleşmektedir. Dolayısıyla, geriye kalan tek şey hangi değerin hashlendiğidir.

Bu durumda, hash edilen değer btoa(uid) olup, fonksiyon için bir girdi argümanı olan uid değişkeninin base64 kodlu dizesidir. Fonksiyonun çağrıldığı önceki bağlantıya geri dönersek, downloadContract(‘1’) çağrısı yaptığını görürüz. Dolayısıyla, POST isteğinde kullanılan son değer 1'in base64 kodlu dizesidir ve daha sonra md5 hashlenmiştir.

Bunu, uid=1 değerimizi base64 kodlayarak ve ardından aşağıdaki gibi md5 ile hashleyerek test edebiliriz:

İpucu: echo ile -n bayrağını ve base64 ile -w 0 bayrağını, yeni satır eklemekten kaçınmak için kullanıyoruz, böylece aynı değerin md5 hash’ini hesaplayabiliyoruz, yeni satırları hash etmeden, çünkü bu son md5 hash’ini değiştirecektir.

Gördüğümüz gibi, bu hash isteğimizdeki hash ile eşleşiyor, yani nesne referanslarında kullanılan hash tekniğini başarılı bir şekilde tersine çevirerek onları IDOR’lara dönüştürdük. Bununla birlikte, yukarıda kullandığımız aynı hash yöntemini kullanarak diğer çalışanların sözleşmelerini numaralandırmaya başlayabiliriz. Devam etmeden önce, tüm sözleşmeleri numaralandırmak için önceki bölümde kullandığımıza benzer bir komut dosyası yazmayı deneyin.

## Toplu Numaralandırma

Bir kez daha, tüm çalışan sözleşmelerini almak için basit bir bash betiği yazalım. Çoğu zaman bu, IDOR güvenlik açıkları aracılığıyla veri ve dosyaları numaralandırmanın en kolay ve en verimli yöntemidir. Daha gelişmiş durumlarda, Burp Intruder veya ZAP Fuzzer gibi araçları kullanabiliriz, ancak basit bir bash betiği alıştırmamız için en iyi yol olmalıdır.

İlk on çalışanın her biri için hash değerini hesaplamaya, önceki komutun aynısını kullanarak ve sondaki — karakterlerini kaldırmak için tr -d komutunu kullanarak aşağıdaki gibi başlayabiliriz:

Daha sonra, download.php üzerinde yukarıdaki karmaların her birini sözleşme değeri olarak içeren bir POST isteği yapabiliriz, bu da bize nihai kodumuzu verecektir:

Bununla birlikte, betiği çalıştırabiliriz ve 1–10 arası çalışanlar için tüm sözleşmeleri indirmesi gerekir:

Gördüğümüz gibi, nesne referanslarında kullanılan hashing tekniğini tersine çevirebildiğimiz için, artık diğer tüm kullanıcıların sözleşmelerini almak için IDOR güvenlik açığından başarıyla yararlanabiliriz.

## Makine Çözümü 2-

Soru : İlk 20 çalışanın sözleşmelerini indirmeye çalışın, bunlardan biri ‘cat’ ile okuyabileceğiniz bayrağı içermelidir. ‘contract’ parametre değerini hesaplayabilir ya da doğrudan ‘.pdf’ dosya adını hesaplayabilirsiniz.

Cevap :

1- Öncelikle burp’den isteği yakalayalım .

2- İsteği yakaldık dikkat ceken bir base64 ile kodlanmış bir değer var .

MQ%3D%3D → Bu değer 1 değerine eşit . Muhtemelen 1,2,3… diye gidiyor.

Hedef sisteme uygun bir bash betiği yazalım . 1–20 ‘e kadar olan değerleri base64 ile kodlayan ve indiren bir bash betiği yazalım .

Not : chmod kodumuzun çalışması için yetkilerini yükseltiyoruz. (Sadece +x yetkisi versekte çalışır)

İndirmeler bittikten sonra download.php dosyamızı okuyup bayrağımızı yakalayalım . (Diğer dosyalar boş olduğu için sadece bayrak çıkması sizi şaşırtmasın.)

2.Çözüm tekniği şu şekilde olabilir → Bash betiği yazarken zorlanıyorsanız benim gibi 1'den 20'ye kadar (Sorumuz için) olan sayıları base64 değerini otomatik alan bir script yazın ve bu script .txt dosyasına değerleri kayıt etsin . Ardından txt dosyasını kolaylıkla fuzz ‘ a koyup anlayabilirsiniz.

`fuzz -w wordlist:FUZZ -u hedef_url:FUZZ -fs {size}`
## Güvensiz API’lerde IDOR

Şimdiye kadar, IDOR güvenlik açıklarını yalnızca kullanıcımızın erişimi dışındaki dosyalara ve kaynaklara erişmek için kullandık. Bununla birlikte, IDOR güvenlik açıkları işlev çağrılarında ve API’lerde de mevcut olabilir ve bunlardan yararlanmak, diğer kullanıcılar gibi çeşitli eylemler gerçekleştirmemize olanak tanır.

IDOR Bilgi İfşa Zafiyetleri çeşitli kaynak türlerini okumamıza izin verirken, IDOR Güvensiz İşlev Çağrıları API’leri çağırmamıza veya başka bir kullanıcı olarak işlevleri yürütmemize olanak tanır. Bu tür işlevler ve API’ler başka bir kullanıcının özel bilgilerini değiştirmek, başka bir kullanıcının şifresini sıfırlamak ve hatta başka bir kullanıcının ödeme bilgilerini kullanarak ürün satın almak için kullanılabilir. Birçok durumda, modülün ilerleyen bölümlerinde göreceğimiz gibi, bir bilgi ifşası IDOR güvenlik açığı yoluyla belirli bilgileri elde ediyor ve daha sonra bu bilgileri IDOR güvensiz işlev çağrısı güvenlik açıkları ile kullanıyor olabiliriz.

## Güvensiz API’lerin Belirlenmesi

Employee Manager web uygulamamıza geri dönecek olursak, Profile Edit sayfasını IDOR güvenlik açıkları için test etmeye başlayabiliriz:

Profil Edit düğmesine tıkladığımızda, birçok web uygulamasında ortak bir özellik olan kullanıcı profilimizin bilgilerini, yani Full Name (Ad Soyad), Email (E-posta) ve About Me (Hakkımda) bilgilerini düzenlemek için bir sayfaya yönlendiriliriz:

Profilimizdeki herhangi bir ayrıntıyı değiştirebilir ve Update profile (Profili güncelle) butonuna tıklayabiliriz, böylece bunların güncellendiğini ve yenilemeler yoluyla kalıcı hale geldiğini görürüz, yani bir yerlerde bir veritabanında güncellenirler. Burp’ta Güncelleme isteğini keselim ve ona bakalım:

Sayfanın /profile/api.php/profile/1 API uç noktasına bir PUT isteği gönderdiğini görüyoruz. PUT istekleri genellikle API’lerde öğe ayrıntılarını güncellemek için kullanılırken, POST yeni öğeler oluşturmak için, DELETE öğeleri silmek için ve GET öğe ayrıntılarını almak için kullanılır. Dolayısıyla, Profili güncelle işlevi için bir PUT isteği beklenir. İlginç olan kısım, gönderdiği JSON parametreleridir:

PUT isteğinin uid, uuid ve en ilginci de çalışan olarak ayarlanmış rol gibi birkaç gizli parametre içerdiğini görüyoruz. Web uygulaması ayrıca, kullanıcımız için belirtilen rolü yansıtıyor gibi görünen Cookie: role=employee cookie’miz biçiminde, istemci tarafında kullanıcı erişim ayrıcalıklarını (örneğin rol) ayarlıyor gibi görünmektedir. Bu yaygın bir güvenlik sorunudur. Erişim kontrol ayrıcalıkları, istemcinin HTTP isteğinin bir parçası olarak ya bir cookie ya da JSON isteğinin bir parçası olarak gönderilir ve daha fazla ayrıcalık elde etmek için manipüle edilebilecek şekilde istemcinin kontrolü altında bırakılır.

Dolayısıyla, web uygulaması back-end’de sağlam bir erişim kontrol sistemine sahip değilse, kullanıcımız için bize daha fazla ayrıcalık tanıyabilecek rastgele bir rol belirleyebilmeliyiz. Ancak, başka hangi rollerin var olduğunu nasıl bilebiliriz?

## Güvensiz API’lerden Yararlanma

full\_name, email ve about parametrelerini değiştirebileceğimizi biliyoruz, çünkü bunlar /profile web sayfasındaki HTML formunda kontrolümüz altında olan parametrelerdir. Öyleyse, diğer parametreleri değiştirmeyi deneyelim.

Bu durumda deneyebileceğimiz birkaç şey var:

1. Uid’mizi başka bir kullanıcının uid’siyle değiştirmek, böylece hesaplarını ele geçirebiliriz
2. Başka bir kullanıcının bilgilerini değiştirmek, bu da çeşitli web saldırıları gerçekleştirmemize izin verebilir
3. İsteğe bağlı ayrıntılarla yeni kullanıcılar oluşturun veya mevcut kullanıcıları silin
4. Daha fazla eylem gerçekleştirebilmek için rolümüzü daha ayrıcalıklı bir rolle (örn. admin) değiştirin

Uid’mizi başka bir kullanıcının uid’siyle değiştirerek başlayalım (örneğin “uid”: 2). Ancak, kendi uid’miz dışında belirlediğimiz herhangi bir sayı bize uid uyuşmazlığı yanıtı verir:

Web uygulaması, isteğin uid’sini API uç noktası (/1) ile karşılaştırıyor gibi görünüyor. Bu, back-end’deki bir tür erişim kontrolünün, web uygulamasının çökmesini veya hata döndürmesini önlemek için gerekli olabilecek bazı JSON parametrelerini keyfi olarak değiştirmemizi engellediği anlamına gelir.

Belki başka bir kullanıcının bilgilerini değiştirmeyi deneyebiliriz. API uç noktasını /profile/api.php/profile/2 olarak değiştireceğiz ve “uid “yi değiştireceğiz: 2 olarak değiştirerek önceki uid uyuşmazlığını önleyeceğiz:

Gördüğümüz gibi, bu sefer uuid uyuşmazlığı şeklinde bir hata mesajı alıyoruz. Web uygulaması, gönderdiğimiz uuid değerinin kullanıcının uuid’siyle eşleşip eşleşmediğini kontrol ediyor gibi görünüyor. Kendi uuid değerimizi gönderdiğimiz için isteğimiz başarısız oluyor. Bu, kullanıcıların başka bir kullanıcının ayrıntılarını değiştirmesini önlemek için başka bir erişim denetimi biçimi gibi görünüyor.

Ardından, API uç noktasına bir POST isteği ile yeni bir kullanıcı oluşturup oluşturamayacağımızı görelim. İstek yöntemini POST olarak değiştirebilir, uid’yi yeni bir uid olarak değiştirebilir ve isteği yeni uid’nin API uç noktasına gönderebiliriz:

Yeni çalışanlar oluşturmanın yalnızca yöneticiler için olduğunu söyleyen bir hata mesajı alıyoruz. Aynı şey bir Delete isteği gönderdiğimizde de oluyor, çünkü Deleting employees is for admins only (Çalışanları silmek yalnızca yöneticiler içindir) hatası alıyoruz. Web uygulaması yetkimizi role=employee cookie’si üzerinden kontrol ediyor olabilir çünkü HTTP isteğindeki tek yetkilendirme biçimi bu gibi görünüyor.

Son olarak, daha yüksek ayrıcalıklar elde etmek için rolümüzü admin/administrator olarak değiştirmeyi deneyelim. Ne yazık ki, geçerli bir rol adı bilmeden, HTTP yanıtında Geçersiz rol alırız ve rolümüz güncellenmez:

Yani, tüm girişimlerimiz başarısız olmuş gibi görünüyor. Rolümüzü değiştiremediğimiz için kullanıcı oluşturamıyor veya silemiyoruz. Back-end’de kontrol edemediğimiz önleyici tedbirler olduğu için kendi uid’mizi değiştiremiyoruz ya da aynı sebepten dolayı başka bir kullanıcının bilgilerini değiştiremiyoruz. Peki, web uygulaması IDOR saldırılarına karşı güvenli mi?

Şimdiye kadar sadece IDOR Güvensiz Fonksiyon Çağrılarını test ettik. Ancak, API’nin GET isteğini IDOR Bilgi İfşa Zafiyetleri için test etmedik. Eğer sağlam bir erişim kontrol sistemi olmasaydı, diğer kullanıcıların bilgilerini okuyabilirdik ve bu da daha önce denediğimiz saldırılarda bize yardımcı olabilirdi.

GET istekleri ile diğer kullanıcıların bilgilerini almaya çalışarak API’yi IDOR Bilgi İfşası güvenlik açıklarına karşı test etmeye çalışın. API savunmasızsa, diğer kullanıcıların ayrıntılarını sızdırabilir ve ardından bu bilgileri işlev çağrılarına yönelik IDOR saldırılarımızı tamamlamak için kullanabiliriz.

## Makine Çözüm -3

Soru : ‘uid=5’ ile kullanıcının ayrıntılarını okumaya çalışın. Onların ‘uuid’ değeri nedir?

1- Öncelikle burpsuitten isteği yakalayalım . Ardından isteğimizi GET olarak değiştirelim . Sonra GET “/profile/api.php/profile/5” ‘sini 1 den 5 ‘e ve uid değerini 5 yapalım böylece karşılaştırınca doğru sonucu alırız.

## Zincirleme IDOR Güvenlik Açıkları

Genellikle, API uç noktasına yapılan bir GET isteği istenen kullanıcının ayrıntılarını döndürmelidir, bu nedenle kullanıcımızın ayrıntılarını alıp alamayacağımızı görmek için onu çağırmayı deneyebiliriz. Ayrıca, sayfa yüklendikten sonra, aynı API uç noktasına bir GET isteği ile kullanıcı ayrıntılarını getirdiğini fark ediyoruz:

Önceki bölümde belirtildiği gibi, HTTP isteklerimizdeki tek yetkilendirme biçimi role=employee cookie’sidir, çünkü HTTP isteği örneğin bir JWT token gibi kullanıcıya özel başka bir yetkilendirme biçimi içermez. Bir belirteç mevcut olsa bile, bir back-end erişim kontrol sistemi tarafından talep edilen nesne ayrıntılarıyla aktif olarak karşılaştırılmadığı sürece, diğer kullanıcıların ayrıntılarını yine de alabiliriz.

## Detaylı Bilgi

Başka bir uid ile bir GET isteği gönderelim:

Gördüğümüz gibi, bu, kendi uuid ve rolleriyle başka bir kullanıcının ayrıntılarını döndürdü ve bir IDOR Bilgi İfşası güvenlik açığını doğruladı:

```
{
    "uid": "2",
    "uuid": "4a9bd19b3b8676199592a346051f950c",
    "role": "employee",
    "full_name": "Iona Franklyn",
    "email": "i_franklyn@employees.htb",
    "about": "It takes 20 years to build a reputation and few minutes of cyber-incident to ruin it."
}
```
Bu bize, daha önce hesaplayamadığımız ve dolayısıyla diğer kullanıcıların ayrıntılarını değiştiremediğimiz yeni ayrıntılar, özellikle de uuid sağlar.

**Diğer Kullanıcıların Bilgilerini Değiştirme**

Şimdi, kullanıcının uuid’si elimizdeyken, /profile/api.php/profile/2 adresine yukarıdaki ayrıntılarla birlikte yaptığımız değişiklikleri içeren bir PUT isteği göndererek bu kullanıcının ayrıntılarını aşağıdaki gibi değiştirebiliriz:

Bu sefer herhangi bir erişim kontrolü hata mesajı almıyoruz ve kullanıcı ayrıntılarını tekrar GET etmeye çalıştığımızda, ayrıntılarını gerçekten güncellediğimizi görüyoruz:

Potansiyel olarak hassas ayrıntıları görüntülememize izin vermenin yanı sıra, başka bir kullanıcının ayrıntılarını değiştirme yeteneği de birkaç başka saldırı gerçekleştirmemize olanak tanır. Bir saldırı türü, bir kullanıcının e-posta adresini değiştirmek ve ardından belirttiğimiz e-posta adresine gönderilecek bir şifre sıfırlama bağlantısı talep etmek ve böylece hesaplarının kontrolünü ele geçirmemize izin vermektir. Bir diğer potansiyel saldırı ise ‘hakkında’ alanına bir XSS payload’u yerleştirmektir; bu payload, kullanıcı Profili Düzenle sayfasını ziyaret ettiğinde çalıştırılır ve kullanıcıya farklı şekillerde saldırmamızı sağlar.

## İki IDOR Zafiyetinin Zincirlenmesi

Bir IDOR Bilgi İfşası güvenlik açığı tespit ettiğimiz için, tüm kullanıcıları listeleyebilir ve ideal olarak bir yönetici rolü olmak üzere diğer rolleri de arayabiliriz. Daha önce yaptığımıza benzer şekilde, tüm kullanıcıları numaralandırmak için bir komut dosyası yazmaya çalışın.

Tüm kullanıcıları listelediğimizde, aşağıdaki ayrıntılara sahip bir yönetici kullanıcısı bulacağız:

Yöneticinin bilgilerini değiştirebilir ve ardından hesaplarını ele geçirmek için yukarıdaki saldırılardan birini gerçekleştirebiliriz. Ancak, artık yönetici rolü adını (web\_admin) bildiğimiz için, bunu kullanıcımıza ayarlayabiliriz, böylece yeni kullanıcılar oluşturabilir veya mevcut kullanıcıları silebiliriz. Bunu yapmak için, Update profile düğmesine tıkladığımızda isteği keseceğiz ve rolümüzü web\_admin olarak değiştireceğiz:

Bu kez, Invalid role hata mesajını almadığımız gibi herhangi bir erişim kontrolü hata mesajı da almıyoruz, yani kullanıcımız için hangi rolleri ayarlayabileceğimize dair herhangi bir back-end erişim kontrolü önlemi yok. Kullanıcı bilgilerimizi alırsak, rolümüzün gerçekten de web\_admin olarak ayarlandığını görürüz:

Şimdi, Cookie’mizi güncellemek için sayfayı yenileyebilir veya manuel olarak Cookie: role=web\_admin olarak ayarlayabilir ve ardından yeni bir kullanıcı oluşturmak için Güncelleme isteğini durdurabilir ve bunu yapmamıza izin verilip verilmeyeceğini görebiliriz:

Bu sefer bir hata mesajı almadık. Yeni kullanıcı için bir GET isteği gönderirsek, başarıyla oluşturulduğunu görürüz:

IDOR Bilgi İfşası zafiyetinden elde ettiğimiz bilgileri bir API uç noktasında IDOR Güvensiz İşlev Çağrıları saldırısı ile birleştirerek, diğer kullanıcıların bilgilerini değiştirebilir ve çeşitli erişim kontrollerini atlayarak kullanıcı oluşturabilir / silebiliriz. Birçok durumda, IDOR güvenlik açıkları yoluyla sızdırdığımız bilgiler, IDOR veya XSS gibi diğer saldırılarda kullanılabilir, bu da daha karmaşık saldırılara yol açabilir veya mevcut güvenlik mekanizmalarını atlayabilir.

Yeni rolümüzle, profillerine XSS payloadları yerleştirmek veya e-postalarını belirlediğimiz bir e-posta ile değiştirmek gibi tüm kullanıcılar için belirli alanları değiştirmek üzere toplu atamalar da gerçekleştirebiliriz. Tüm kullanıcıların e-postalarını seçtiğiniz bir e-posta ile değiştiren bir komut dosyası yazmaya çalışın. Bunu, uuid’lerini alarak ve ardından her biri için yeni e-posta ile bir PUT isteği göndererek yapabilirsiniz.

Soru : Yöneticinin e-postasını ‘flag@idor.htb’ olarak değiştirmeyi deneyin ve ‘profili düzenle’ sayfasında bayrağı almalısınız.

1- Betik yazmak yerine bu sefer burpsuite intruder özelliğini kullarak bulmaya çalışalım . Öncelikle isteğimizi yakaladık .

2- Send to Intruder ‘a tıklayıp intruder seçeneğine yollayalım isteği . Ardında intruder’da kullanmak için bir 1–100 ‘e kadar olan bir txt dosyası oluşturalım .

3- txt ‘imizi oluşturduk bunu intruderda ‘a geçelim . Posizyonlarımızı belirleyelim .

4- Bu iki kısıma brute force saldırımızı gerçekleştireceğiz . Ardından Pitchfork seçeneğini seçelim. Çünkü 2 değerin aynı değerleri ile brute force yapmasını istiyoruz.

5- Payloads sekmesine gelelim ve Payload set kısmında 1 ve 2 seçeneğine önceden oluşturduğumuz 1–100'e kadar olan txt dosyasını Load edelim .

6- Start Atack yapalım . Size boyutu farklı olanlar sonuçlarımız . (166 çıkan sonuclar büyük ihtimal boş sonuclar.)

7- İsteklerin Response değerlerini inceleyelim .

8- “10” istekde role değerinin staff\_admin olduğunu keşfettik şimdi Yöneticinin e-postasını ‘flag@idor.htb’ olarak değiştirelim .

Not : uuid id değerini , role değerini , İsteği UPDATE ve emaili flag@idor.htb olarak değiştireceğiz.

9- İsteğimiz gerçekleşti ve istediğimiz değişikleri yaptık. Bayrak anasayfamıza profile edit sayfasını yeniledğimizde gelecektir.

## IDOR Önleme

Web sayfalarında, web işlevlerinde ve API çağrılarında IDOR güvenlik açıklarını belirlemenin ve bunlardan yararlanmanın çeşitli yollarını öğrendik. Şimdiye kadar, IDOR güvenlik açıklarının temel olarak back-end sunuculardaki uygunsuz erişim kontrolünden kaynaklandığını anlamış olmalıydık. Bu tür güvenlik açıklarını önlemek için öncelikle nesne düzeyinde bir erişim kontrol sistemi oluşturmalı ve ardından nesnelerimizi depolarken ve çağırırken güvenli referanslar kullanmalıyız.

## Obje Seviyesinde Erişim Kontrolü

Bir Erişim Kontrol sistemi, tüm tasarımını ve yapısını etkileyebileceğinden, herhangi bir web uygulamasının merkezinde yer almalıdır. Web uygulamasının her alanını düzgün bir şekilde kontrol etmek için, tasarımının rollerin ve izinlerin merkezi bir şekilde bölümlendirilmesini desteklemesi gerekir. Ancak, Erişim Kontrolü çok geniş bir konudur, bu nedenle sadece Object Level erişim kontrol mekanizmalarında temsil edilen IDOR güvenlik açıklarındaki rolüne odaklanacağız.

Kullanıcı rolleri ve izinleri, Rol Tabanlı Erişim Kontrolü (RBAC) sisteminde tam olarak gerçekleştirilen herhangi bir erişim kontrol sisteminin hayati bir parçasıdır. IDOR güvenlik açıklarından faydalanmaktan kaçınmak için RBAC’yi tüm nesneler ve kaynaklarla eşleştirmeliyiz. Back-end sunucusu, talep edenin rolünün nesneye veya kaynağa erişmek için yeterli ayrıcalıklara sahip olup olmadığına bağlı olarak her talebe izin verebilir veya reddedebilir.

Bir RBAC uygulandıktan sonra, her kullanıcıya belirli ayrıcalıklara sahip bir rol atanacaktır. Kullanıcının yaptığı her talep üzerine, talep ettikleri nesneye erişimleri olup olmadığını görmek için rolleri ve ayrıcalıkları test edilir. Yalnızca buna hakları varsa erişmelerine izin verilir.

Bir RBAC sistemini uygulamanın ve bunu web uygulamasının nesneleri ve kaynaklarıyla eşleştirmenin birçok yolu vardır ve bunu web uygulamasının yapısının çekirdeğinde tasarlamak mükemmelleştirilmesi gereken bir sanattır. Aşağıda, bir web uygulamasının erişim kontrolüne izin vermek ya da vermemek için kullanıcı rollerini nesnelerle nasıl karşılaştırabileceğine dair örnek bir kod yer almaktadır:

Yukarıdaki örnek, kullanıcının çeşitli rollerini ve ayrıcalıklarını almak için RBAC’ye yapılan HTTP isteğinden eşleştirilebilen kullanıcı belirtecini kullanır. Ardından, yalnızca kullanıcının RBAC sistemindeki uid’si, talep ettikleri API uç noktasındaki uid ile eşleşiyorsa okuma/yazma erişimine izin verir. Ayrıca, bir kullanıcı back-end RBAC’de rol olarak admin’e sahipse, okuma/yazma erişimine izin verilir.

Önceki saldırılarımızda, kullanıcı rolünün kullanıcının ayrıntılarında veya cookie’sinde saklandığı örnekleri görmüştük; bunların her ikisi de kullanıcının kontrolü altındadır ve erişim ayrıcalıklarını artırmak için manipüle edilebilir. Yukarıdaki örnek, kullanıcı ayrıcalıkları HTTP isteği aracılığıyla aktarılmadığı, ancak bir kimlik doğrulama mekanizması olarak kullanıcının oturum açma oturum belirteci kullanılarak doğrudan back-end’deki RBAC’den eşlendiği için kullanıcı rollerini eşlemek için daha güvenli bir yaklaşım göstermektedir.

Erişim kontrol sistemleri ve RBAC’ler tasarlaması en zor sistemlerden bazıları olabileceğinden, daha pek çok şey var. Ancak bu, web uygulamalarının nesneleri ve kaynakları üzerinde kullanıcı erişimini nasıl kontrol etmemiz gerektiği konusunda bize bir fikir vermelidir.

## Nesne Referanslama

IDOR ile ilgili temel sorun bozuk erişim kontrolünde (Güvensiz) yatarken, nesnelere doğrudan referanslara (Doğrudan Nesne Referansı) erişime sahip olmak, bu erişim kontrolü güvenlik açıklarını sıralamayı ve bunlardan yararlanmayı mümkün kılar. Doğrudan referansları hala kullanabiliriz, ancak yalnızca sağlam bir erişim kontrol sistemimiz varsa.

Sağlam bir erişim kontrol sistemi oluşturduktan sonra bile, nesne referanslarını asla açık metin veya basit kalıplarda (örneğin uid=1) kullanmamalıyız. Her zaman salted hash’ler veya UUID’ler gibi güçlü ve benzersiz referanslar kullanmalıyız. Örneğin, herhangi bir öğe için (89c9b29b-d19f-4515-b2dd-abb6e693eb20) gibi görünen güçlü bir şekilde rastgele bir kimlik oluşturmak için UUID V4'ü kullanabiliriz. Daha sonra, bu UUID’yi back-end veritabanında referans verdiği nesneyle eşleştirebiliriz ve bu UUID her çağrıldığında, back-end veritabanı hangi nesneyi döndüreceğini bilir. Aşağıdaki örnek PHP kodu bize bunun nasıl çalışabileceğini göstermektedir:

Ayrıca, modülde daha önce gördüğümüz gibi, hash’leri asla front-end’de hesaplamamalıyız. Bunları bir obje oluşturulduğunda üretmeli ve back-end veritabanında saklamalıyız. Ardından, nesnelerin ve referansların hızlı bir şekilde çapraz referanslanmasını sağlamak için veritabanı eşlemeleri oluşturmalıyız.

Son olarak, UUID’lerin kullanılmasının IDOR güvenlik açıklarının tespit edilmemesine neden olabileceğini, çünkü IDOR güvenlik açıklarının test edilmesini zorlaştırdığını belirtmeliyiz. Bu nedenle güçlü nesne referanslama her zaman güçlü bir erişim kontrol sistemi uygulandıktan sonraki ikinci adımdır. Ayrıca, bu modülde öğrendiğimiz bazı teknikler, daha önce gördüğümüz gibi, bir kullanıcının isteğinin başka bir kullanıcının oturumuyla tekrarlanması gibi, erişim kontrol sistemi bozuksa benzersiz referanslarla bile çalışacaktır.

Bu güvenlik mekanizmalarının her ikisini de uygularsak, IDOR güvenlik açıklarına karşı nispeten güvende oluruz.
