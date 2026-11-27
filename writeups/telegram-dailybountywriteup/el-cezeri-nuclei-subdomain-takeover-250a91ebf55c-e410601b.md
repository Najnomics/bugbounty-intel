# Nuclei — Subdomain Takeover

- **Source URL:** https://medium.com/@el-cezeri/nuclei-subdomain-takeover-250a91ebf55c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012150454/https://medium.com/@el-cezeri/nuclei-subdomain-takeover-250a91ebf55c
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3457 (id 3457)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Nuclei — Subdomain Takeover

--

Uzun bir aradan sonra herkese merhaba ! Bir önceki yazıda subdomain tespiti ile ilgili araçların kullanımlarına göz atmıştık .

İlgili yazıya buradan ulaşabilirsiniz .

Bugün elde ettiğimiz bu subdomainler ile nuclei aracılığıyla devralma işlemine göz atacağız.

# nuclei nedir ?

Nuclei”, siber güvenlik alanında kullanılan açık kaynaklı bir otomasyon aracıdır. Bu araç, sızma testi ve güvenlik denetimleri sırasında web uygulamaları ve ağ korumasına karşı belirli güvenlik açıklarını otomatik olarak tespit etmek için kullanılır. Nuclei, HTTP, DNS, SSL gibi farklı protokoller üzerinden hedef sistemlerle iletişim kurarak çeşitli güvenlik kontrollerini gerçekleştirebilir.

Nuclei, temel olarak kullanıcıların belirli zafiyetlerin bulunmasını taramasını ve bu taramaları otomatikleştirmesini sağlar. Güvenlik araştırmacıları ve sızma testi cihazları tarafından kullanılan, hedef sistemlerde potansiyel açıkları tespit etmeye yardımcı olur. Bu şekilde, sistem sahipleri veya güvenlik uzmanları, zafiyetleri kapatmak ve olası saldırılara karşı önlem almak için gereken önlemleri alabilirler.

*nuclei*

Aracı kurduğumuza göre kullanıma geçelim . Bir önceki yazıda ayrıntılı bir şekilde subdomain tespitine değinmiştik . Bu yazıda sadece subfinder aracını kullanacağım. Daha fazla araç kullanmanız önerilir. Daha çok farklı alt alan adı devralma şansını artırır .

nuclei şablonlarına aşağıdaki bağlantıdan ulaşabilirsiniz :

Subdomain devralma için aşağıdaki şablonu kullanacağım .

Her şey hazırsa başlayalım ….

İlk olarak alt alanları bulalım

**subfinder -d hedefadres.com -o subdomain.txt**

Alt alan adlarını elde ettikten sonra ilgili şablonla alt alanları tarayalım …

**nuclei -l /root/Desktop/subdomain.txt -t subdomain-takeover\_detect-all-takeovers.yaml**

- -l ile subdoaminleri belirttik, -t ile ilgili .yaml dosyasını belirttik.

Taramanın bitmesini bekleyelim. Nuclei tüm subdomainlerde devralma güvenlik açığını hızlı bir şekilde tarayacaktır.

Tarama sonucunda nuclei heroku sağlayıcısı kullanan bir alt alan adının devralabilme ihtimali olan bir çıktı verdi . Bundan sonra ilgili sağlayıcıya gidip devralma işlemlerinin kontrol edilmesi gerekiyor :).

Aşağıdaki bağlantı başka subdomainler için sizlere devralma işleminde yardımcı olacaktır .

Nuclei ile subdomain devralma ile ilgili yazımızın sonuna geldik . Görüşmek dileğiyle ❤

Öneri ve sorularınız için bana linkedln adresimden ulaşabilirsiniz .
