# Güvenlik Ürünü Kendini Koruyamazsa

- **Source URL:** https://medium.com/@furkanyasinkeskin/g%C3%BCvenlik-%C3%BCr%C3%BCn%C3%BC-kendini-koruyamazsa-endpoint-central-ajan%C4%B1-ile-sorumlu-i%CC%87f%C5%9Fa-hik%C3%A2yem-edd8249c833e
- **Fetched from:** https://medium.com/@furkanyasinkeskin/g%C3%BCvenlik-%C3%BCr%C3%BCn%C3%BC-kendini-koruyamazsa-endpoint-central-ajan%C4%B1-ile-sorumlu-i%CC%87f%C5%9Fa-hik%C3%A2yem-edd8249c833e?source=rss-d02c8a77fb7f------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14966 (id 14966)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Furkan Yasin Keskin / Sat, 31 Oct 2026 20:01:09 GMT

Bir EDR, DLP ya da UEM ajanına güvenmemizin sebebi basit: makinede biz yokken o var. Ama çoğu zaman sorulmayan bir soru var: **Ajanın kendisini kim koruyor?**

Bu yazı, ManageEngine Endpoint Central ajanında bulduğum bir davranışın yaklaşık altı ay süren bildirim sürecini anlatıyor.

Endpoint Central Agent **v11.4.2516.37.W** üzerinde yaptığım testlerde, **Self-Defense** ve **Uninstall Password Protection** özellikleri aktif olmasına rağmen ajanın MSI ve kayıt defteri bileşenleri üzerinde yapılan müdahalelerle tamamen kaldırılabildiğini gördüm.

Yani ürünün “bu ajan kaldırılamaz” vaadi belirli koşullarda geçerli değildi. Ajan gidince onun üzerinden gelen yama yönetimi, uygulama kontrolü, cihaz kontrolü ve tarayıcı politikaları da gidiyordu.

*Teknik adımları bilerek paylaşmıyorum; sorun güncel sürümlerde giderilmiş olsa da eski sürümde kalan ortamlar olabilir.*

Bulguyu Zoho’nun bug bounty programı üzerinden, sorumlu ifşa (responsible disclosure) başlığıyla raporladım.

Aralık 2025'te rapor triage aşamasına alındı ve CVSS skoru 7.7'den 4.4'e düşürüldü. Ardından en uzun süren kısım geldi: etkinin nasıl sınıflandırılacağı.

Vendor’ın bakış açısı şuydu: bu davranış için SYSTEM/Administrator yetkisi gerekiyor ve bu, programın kapsamı dışında. Microsoft’un servis kriterleri de admin ile kernel arasındaki sınırı bir güvenlik sınırı olarak kabul etmiyor.

Benim itirazım ise şuydu: mesele yetki yükseltmek değil, ürünün güvenlik garantilerinin dayandığı koruma mekanizmasını tamamen devre dışı bırakabilmek. Ürün zararlı yazılım, fidye yazılımı koruması ve DLP uygulamasını bu ajan üzerinden vaat ediyorsa, tamper koruması olmayan bir ajan bu kontrollerin etkinliğini doğrudan düşürür. Bu, MITRE ATT&CK’teki savunmaları zayıflatma ve iz silme tekniklerinin tam karşılığı. Fidye yazılımı operatörlerinin ilk yaptığı iş de genellikle güvenlik ajanlarını kapatmak.

Mayıs 2026'da gelen yanıtta rapor **Informative** olarak kaldı. Ama aynı yanıtta önemli bir bilgi vardı: ajana müdahaleye karşı **kernel seviyesinde sürücü koruması** eklenmişti. Geliştirme kademeli olarak dağıtılıyordu ve isteyen müşteriler konsoldan hemen etkinleştirebiliyordu.

Destek ekibi de **11.5.2605** sürümüne yükseltmenin sorunu tamamen giderdiğini, ek bir manuel işleme gerek olmadığını iletti.

Bildirmek yetmez, doğrulamak gerekir. **11.5.2616.20.W** ajan sürümünde aynı testleri tekrarladım: Agent Protection artık üçüncü taraf kaldırma ve müdahale girişimlerine karşı beklendiği gibi çalışıyor.

Bir şartla: korumanın tam devreye girmesi için ayarın açılması gerekiyor.

**Agent Settings → Agent Protection Settings → Prevent Agent Data Tampering**

Bu kadar önemli bir self-protection geliştirmesinin sürüm notlarında **açıkça olmaması ve/veya vurgulanmaması**. Endpoint Central kullanan birçok kurum bu korumanın varlığından ve ayrıca etkinleştirilmesi gerektiğinden **habersiz** olabilir.

Sezar’ın hakkı Sezar’a: rapor “Informative” kalsa da ManageEngine ekibi geri bildirimi ciddiye aldı, süreç boyunca iletişimde kaldı ve gerçek bir iyileştirme yayınladı.

*Bazen en önemli güncelleme yeni bir özellik değil, güvenlik ürününün kendini koruyabilmeye başlamasıdır.*
