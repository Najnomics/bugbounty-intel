# Web Cache Deception via URL Parsing Discrepancy — PII Disclosure & Cache Poisoning

- **Source URL:** https://medium.com/@ferhatsara/web-cache-deception-via-url-parsing-discrepancy-pii-disclosure-cache-poisoning-29ccf97be42f
- **Fetched from:** https://medium.com/@ferhatsara/web-cache-deception-via-url-parsing-discrepancy-pii-disclosure-cache-poisoning-29ccf97be42f?source=rss-aad1d0c12982------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14911)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ferhat SARA / Tue, 15 Sep 2026 00:14:38 GMT

Merhaba, global ölçekte faaliyet gösteren bir kuruluşta tespit etmiş olduğum Web Cache Deception (WCD) zafiyetini teknik açıdan paylaşmak istiyorum.

Zafiyetin temelinde, cache katmanı ile origin uygulamasının aynı URL’yi farklı şekilde parse etmesi ve canonicalize etmesi bulunuyordu.

Hedef endpoint:

GET /api/users/profile

Kullandığım primitive, URL’ye cache katmanının statik bir dosya/resource 

olarak değerlendirebileceği bir suffix eklemekti:

/api/users/profile%3f%26deneme.webp

Kritik nokta, aynı request’in farklı katmanlarda farklı yorumlanmasıydı.

Cache layer:

URL’yi .webp ile biten cacheable bir resource olarak değerlendirdi.

Origin application:

URL’yi normalize ettikten sonra gerçek endpointi:

/api/users/profile

olarak işledi.

Sonuç:

Saldırgan kontrollü URL

→ Cache statik kaynağı görüyor

→ Origin authenticated API endpointi görüyor

→ Kimliği doğrulanmış PII response’u cache’leniyor

→ Kimlik doğrulaması olmadan erişim

Aynı URL canonicalization / cache-key primitive’i üzerinden cache poisoning etkisi de gözlemlenebildi.

Bu bulgu, modern web uygulamalarında yalnızca application logic’in değil, request’in geçtiği tüm parsing ve normalization katmanlarının incelenmesi gerektiğini gösteriyor:

Browser

→ CDN

→ Reverse Proxy

→ WAF

→ Cache

→ Load Balancer

→ Application

Bu katmanlardan herhangi ikisinin URL’yi farklı yorumlaması, güvenlik sınırlarının beklenmedik şekilde aşılmasına neden olabilir.

Ayrıca cache poisoning tek başına değerlendirilmemeli. XSS gibi başka bir vulnerability ile zincirlendiğinde etki ciddi şekilde büyüyebilir:

Cache Poisoning

→ Stored XSS

→ Unauthorized Action / ATO

Başlangıçta bir URL parsing veya cache davranışı problemi olarak görünen bir bulgu, doğru primitive ve vulnerability chaining ile çok daha yüksek etkili bir saldırı zincirine dönüşebilir.

[#WebCacheDeception](https://www.linkedin.com/search/results/all/?keywords=%23webcachedeception&origin=HASH_TAG_FROM_FEED) [#CachePoisoning](https://www.linkedin.com/search/results/all/?keywords=%23cachepoisoning&origin=HASH_TAG_FROM_FEED) [#XSS](https://www.linkedin.com/search/results/all/?keywords=%23xss&origin=HASH_TAG_FROM_FEED) [#WebSecurity](https://www.linkedin.com/search/results/all/?keywords=%23websecurity&origin=HASH_TAG_FROM_FEED) [#AppSec](https://www.linkedin.com/search/results/all/?keywords=%23appsec&origin=HASH_TAG_FROM_FEED) [#WebApplicationSecurity](https://www.linkedin.com/search/results/all/?keywords=%23webapplicationsecurity&origin=HASH_TAG_FROM_FEED) #bugbounty
