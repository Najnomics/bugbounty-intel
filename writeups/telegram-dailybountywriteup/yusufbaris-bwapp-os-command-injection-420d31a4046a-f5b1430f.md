# bWAPP OS Command Injection

- **Source URL:** https://medium.com/@yusufbaris/bwapp-os-command-injection-420d31a4046a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126141957/https://medium.com/@yusufbaris/bwapp-os-command-injection-420d31a4046a
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2371 (id 2371)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# bWAPP OS Command Injection

### **OS Command Injection Nedir?**

OS Command Injection, Bir saldırganın savunmasız bir uygulama aracılığyla hedef sistemde rastgele OS(Operating System) işletim sistemi komutları çalıştırmasına olanak tanıyan bir güvenlik zafiyetidir. Kullanıcıdan alınan verileri bir sistemin terminaline ilettiğinde burada OS Command Injection saldırıları mümkündür.

**Low Level**


Burada bir DNS lookup uygulaması olduğunu görüyoruz. DNS lookup bir adresin DNS (Domain Name System) çözümlemesi yaparak, bu adres ile ilişkili olan alan adlarını bulmayı sağlayan bir işlemdir.

Biz verdiği örnek domaini “www.nsa.gov” sorguladığımızda bize domaine ait DNS adreslerini verdiğini gördük.

Yaptığımız sorgunun işletim sistemlerinde bulunan Nslookup komutunun olduğunu görebiliriz. Nslookup bir adres ile diğer DNS kayıtları arasındaki eşlemeyi elde etmek için kullanılan bir komut satırı aracıdır.

Uygulamanın kaynak kodunu incelediğimizde PHP de ki shell\_exec fonksiyonun kullanıldığını ve bir Nslookup komutunun çalıştırdığını görüyoruz.

Programlamada da kullanılan Logical Operators (mantıksal operatörler)den biri olan & (AND) operatörü ilk komut başarıyla tamamlandığı zaman ikinci komutu çalıştırır. & operatörünü DNS lookup sorgumuza dahil ederek “www.nsa.gov&whoami” komutunu çalıştırdığımızda bizde sunucunun “www-data” kullanıcısında çalıştığını görüyoruz.

Programlama da kullanılan kapanış etiketlerinden biri olan “;” komutunu sorgumuza dahil ederek “www.nsa.gov;whoami” komutunu çalıştırdığımızda başarılı bir şekilde çalıştığını ve sunucunun “www-data” kullanıcısında çalıştığını görüyoruz.

OS Command Injection için yapılmış bir exploitation toolu olan Commix ile otomatik olarak sunucudan shell alabildik.

**Medium Level**


& ve “;” komutunu sorgumuza dahil ederek çalıştırdığımızda herhangi bir sonuç alamıyoruz.

Uygulamanın kaynak kodunu incelediğimizde “commandi\_check\_1” adında bir fonksiyon ile kontrol edildiğini görüyoruz. PHP’de kullanılan “str\_replace” fonksiyonun kullanıldığını gördük. Bu fonksiyon bir string veya array değişkenlerinde yapılması istenen değişikliklerin uygulanmasını sağlayarak, string veya array tipinde veri döndürür. Sorgumuza dahil ettiğimiz “&” ve “;” karakterlerin engellendiğini gözlemledik.

Linux ve Unix tabanlı işletim sistemlerinde kullanılan Pipe “|” komutunu sorgumuza dahil ederek “www.nsa.gov|whoami” komutunu çalıştırdığımızda başarılı bir şekilde çalıştığını ve sunucunun “www-data” kullanıcısında çalıştığını görüyoruz.

**High Level**


“|” komutunu sorgumuza dahil ederek çalıştırdığımızda herhangi bir sonuç alamıyoruz.

Uygulamanın kaynak kodunu incelediğimizde commandi\_check\_2 ve commandi\_check\_3 adında iki fonksiyon ile kontrol edildiğini görüyoruz. commandi\_check\_2 fonksiyonun da, str\_replace fonksiyonu kullanılarak sorgumuza dahil ettiğimiz “|” komutunun engellendiğini görüyoruz. commandi\_check\_3 fonksiyonunda ise PHP’de ki “escapeshellcmd” fonksiyonun kullanıldığını görüyoruz. Bu fonksiyon bir string içinde ki shell meta karakterlerinden ve kontrol operatörlerinden kaçmaya yarar. OS Command Injection saldırılarına karşı PHP’deki “str\_replace” ve “escapeshellcmd” fonksiyonunu kullanabiliriz.

### OS Command Injection — Blind

OS Command Injection’un bir türü olan Blind türü, Uygulamanın HTTP yanıtında ki komuttan herhangi bir çıktı döndürmediği anlamına gelir. Saldırgan, bu güvenlik açığından yararlanmak için zaman gecikmesi ve çıktı yönlendirme gibi farklı teknikler kullanır.

Burada bizden IP adresi girmemizi isteyen bir alan var ve girdiğimiz IP adresine ping komutu çalıştırdığını görüyoruz. IP adresi girip ping dediğimizde sayfa da herhangi bir sonuç dönmediğini görüyoruz.

Local IP adresimizi “127.0.0.1” olarak girip yolladığımızda bize dönen ping cevabının cevabın “492 ms” olduğunu gördük.

Blind OS Command Injection’dan yararlanmak için zaman gecikmesi tekniği kullanıldığını söylemiştik. Birçok programlama dilinde ve Unix benzeri işletim sistemlerinde kullanılan sleep komutu var. sleep komutu bir programın çalışmasını belirli bir süre için durdurmaya yarayan bir komuttur. sleep komutunu sorgumuza dahil ederek 127.0.0.1&whoami \`sleep 5 \` çalıştırdığımızda başarılı bir şekilde çalıştığını ve sunucunun 5.59 saniyede cevap döndürdüğünü gözlemledik.

Uygulamanın kaynak kodunu incelediğimizde PHP de ki shell\_exec fonksiyonun kullanıldığını ve bir ping komutunun çalıştırdığını görüyoruz.

ping (Packet Internet or Inter-Network Groper) kullanıcının belirli bir hedef IP adresinin var olup olmadığını test etmesine ve doğrulamasına olanak tanıyan bir araçtır. Hedefe 64 baytlık bir ICMP paketi göndermek ve aynı paketin geri gelmesini beklemek üzerine kurulu bir çalışma prensibi vardır.

Peki burada işletim sistemi komutlarını nasıl çalıştıracağız çıktıyı nasıl göreceğiz derseniz çıktı yönlendirme tekniğini kullanarak bunu yapabiliriz.

Burada “127.0.0.1&uname -a > output.txt” komutunu çalıştırarak bize işletim sistemi bilgilerini output.txt adlı text dosyasına çıktı almasını istedik.

output.txt dosyasına baktığımızda yazdığımız uname -a komutunun çalıştığını ve çıktının output.txt ye yazdırdığını görebiliyoruz.

Commix ile denediğimizde tekrardan otomatik olarak sunucudan shell alabildik.

**Medium Level**


& ve “;” komutunu sorgumuza dahil ederek “127.0.0.1&whoami > output\_2.txt” çalıştırdığımızda herhangi bir sonuç alamıyoruz.

Uygulamanın kaynak kodunu incelediğimizde “commandi\_check\_1” adında bir fonksiyon ile kontrol edildiğini görüyoruz. PHP’de kullanılan “str\_replace” fonksiyonun kullanıldığını gördük. Bu fonksiyon bir string veya array değişkenlerinde yapılması istenen değişikliklerin uygulanmasını sağlayarak, string veya array tipinde veri döndürür. Sorgumuza dahil ettiğimiz “&” ve “;” karakterlerin engellendiğini gözlemledik.

“127.0.0.1|whoami > output\_2.txt” komutunu çalıştırdığımızda başarılı bir şekilde çalıştığını ve sunucunun “www-data” kullanıcısında çalıştığını görüyoruz.

**High Level**


“|” komutunu sorgumuza dahil ederek çalıştırdığımızda herhangi bir sonuç alamıyoruz.

Uygulamanın kaynak kodunu incelediğimizde commandi\_check\_2 ve adında bir fonksiyon ile kontrol edildiğini görüyoruz. PHP’de ki “escapeshellcmd” fonksiyonun kullanıldığını görüyoruz. Bu fonksiyon bir string içinde ki shell meta karakterlerinden ve kontrol operatörlerinden kaçmaya yarar. OS Command Injection saldırılarına karşı PHP’deki “escapeshellcmd” fonksiyonunu kullanabiliriz.

**Yusuf Barış |** *Cyber Security Researcher*
