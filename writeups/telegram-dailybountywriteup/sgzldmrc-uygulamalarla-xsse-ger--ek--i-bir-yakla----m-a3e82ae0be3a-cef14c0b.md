# Uygulamalarla XSS’e Gerçekçi Bir Yaklaşım

- **Source URL:** https://medium.com/@sgzldmrc/uygulamalarla-xsse-ger%C3%A7ek%C3%A7i-bir-yakla%C5%9F%C4%B1m-a3e82ae0be3a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241107225910/https://medium.com/@sgzldmrc/uygulamalarla-xsse-ger%C3%A7ek%C3%A7i-bir-yakla%C5%9F%C4%B1m-a3e82ae0be3a
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7794 (id 7794)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS’e Gerçekçi Bir Yaklaşım

Web güvenliğinin temel taşlarından biri olan XSS (Cross-Site Scripting) zafiyeti, hem kullanıcıların kişisel verilerini riske atar hem de uygulamanın güvenliğini zedeler. Günümüzde birçok web sitesi bu açıkla karşı karşıya kalmakta ve kullanıcılarının bilgilerini korumakta zorluk çekmektedir. XSS, saldırganların zararlı kodları kullanıcı tarayıcısında çalıştırmasına olanak tanıyarak oturum çalma, kimlik avı gibi ciddi risklere yol açabilir. Bu yazıda, gerçek dünyada karşılaşılan XSS örneklerinden yola çıkarak, bu zafiyetin nasıl tespit edilebileceğini adım adım ele alacağız. Bu rehberin sonunda, XSS açıklarını daha iyi anlama ve güvenli web uygulamaları geliştirme konusunda pratik bir bakış açısına sahip olacaksınız.

# **İlk XSS Tespitimize Başlayalım( Reflected XSS)**

XSS ararken ilk odaklanmamız gereken konu, **kullanıcıdan gelen input verisinin HTTP Response içerisinde nerelere yansıdığıdır**. Bu aşamada, örneğin bir arama kutusuna `"test"'<>` gibi çeşitli payload'lar girerek test edebiliriz.

Örneğin, varsayımsal sitemiz **store.com** üzerinde arama butonuna payload inputumuzu veriyoruz. Aramayı yaptıktan sonra `CTRL+U` tuşlarıyla sayfanın kaynağını görüntülüyoruz. Ardından `CTRL+F` ile sayfa kaynağında "test" kelimesini arıyoruz.

**Hedefimiz:** Eğer sayfa kaynağında “test” kelimesinin yanına yazdığımız `"'<>` gibi özel karakterler **olduğu gibi görünüyorsa**, bu sitede XSS zafiyeti bulunabileceğini öngörebiliriz. Fakat eğer bu karakterler **encode edilmişse** (örn. `<` yerine `<` gibi), XSS zafiyeti bulmak daha zor olacaktır. Bu yüzden başlangıç olarak **encode edilmediklerinden emin olmamız gerekiyor**.

# Kodda İnceleme ve İlk Testler

Özel karakterlerin encode edilmediğinden emin olduktan sonra, `test` kelimesinin geçtiği alanları incelemeye başlıyoruz. İlk olarak `<meta>` etiketine bakalım. **Özel karakterlerin geçtiği alanlarda kendi HTML ve JavaScript kodumuzu yazabiliriz.** En basit XSS testimiz, `alert(1)` komutu kullanarak bir popup mesaj çıkarmaktır. Bu komutu çalıştırmak için aşağıdaki payload'u deneyebiliriz:

**Payload:**

`"><svg onload=alert(1)>`
Sayfa kaynağında aşağıdaki gibi bir kod görebiliriz:

`<meta name="description" content="Arama Terimi: test"'<>"/>`
Bu alana XSS payload’umuzu ekleyebilmek için:

1. Öncelikle `content` değerini kapatmak için `"`, ardından `>` karakterini ekliyoruz.
2. Ardından istediğimiz JavaScript kodunu `<svg onload=alert(1)>` şeklinde yazıyoruz.

Bu durumda, sayfa kaynağında aşağıdaki gibi bir yapı oluşacaktır:

`<meta name="description" content="Arama Terimi:"><svg onload=alert(1)"/>`
**Sonuç:** `alert(1)` komutunu çalıştırdığımızda tarayıcıda bir popup mesaj görünecektir. Bu da XSS zafiyetinin varlığını kanıtlar. Bu bölümde, istediğimiz herhangi bir JavaScript kodunu çalıştırabiliriz.

**Öneri:** Bu gibi zafiyetleri önlemek için, sitenizde belirli karakterleri encode etmeniz gerekmektedir. Bu zafiyet türü, “Reflected XSS” olarak adlandırılır

# Stored XSS Saldırısı: Yorumlar Bölümünden Pratik Bir Örnek

Stored XSS (Depolanmış XSS), web uygulamalarındaki en tehlikeli güvenlik açıklarından biridir. Bu tür bir zafiyet, kötü niyetli bir kullanıcının JavaScript kodunu, başka kullanıcıların tarayıcılarında çalıştırabilmesini sağlar. Bugün, bir **yorumlar bölümü** üzerinden Stored XSS saldırısını nasıl gerçekleştirebileceğimizi ve buna karşı alabileceğimiz önlemleri adım adım anlatacağız.

## Adım 1: Senaryoyu Tanıyalım

Diyelim ki bir **blog sitesi** üzerinde çalışıyoruz. Sitede kullanıcılar, yazılara yorum yapabiliyor. Bu yorumlar, veritabanında depolanır ve diğer kullanıcılar tarafından görüntülenir.

Bu tür özellikler, kullanıcıdan gelen verilerin doğru şekilde işlenmemesi durumunda **Stored XSS** zafiyetine yol açabilir. Bu yazıda, bir saldırganın yorumlar bölümüne kötü niyetli JavaScript kodu enjekte ettiğini ve diğer kullanıcıların bu kodu nasıl çalıştıracağını inceleyeceğiz.

## Adım 2: Yorumlar Alanına Kötü Niyetli Kod Girme

Saldırgan, yorumlar bölümüne aşağıdaki gibi basit bir JavaScript payload’ı girebilir:

`<script>alert('XSS Saldırısı!');</script>`
Bu kod, sayfayı her ziyaret eden kullanıcıda bir **alert** mesajı tetikleyecektir. Ancak bu örnekteki saldırı, sadece XSS zafiyetini test etmek amacıyla basit tutulmuştur. Gerçek bir saldırgan, daha karmaşık bir payload kullanarak çerez çalma veya kimlik bilgilerini ele geçirme gibi zararlı amaçlar güdebilir.

## Adım 3: Yorumun Depolanması

Saldırgan bu yorumunu girdikten sonra, sunucu tarafından alınan bu veri **veritabanına kaydedilir**. Şu an için, sunucunun bu veriyi filtrelemeden ya da doğrulamadan kaydettiğini varsayıyoruz. Yani, kullanıcıdan gelen bu zararlı JavaScript kodu, doğrudan veritabanına yazılacaktır.

Veritabanında bu veri şu şekilde depolanabilir:

`<script>alert('XSS Saldırısı!');</script>`

## Adım 4: Yorumun Diğer Kullanıcılar Tarafından Görülmesi

Bir başka kullanıcı, blog yazısını okurken, bu yorum **veritabanından çekilir** ve sayfa üzerinde görünür hale gelir. Yorum, HTML olarak sayfada render edilir. Ancak bu aşamada, kötü niyetli JavaScript kodu da tarayıcı tarafından çalıştırılacaktır.

HTML kaynak kodunda şu şekilde bir yapı oluşur:

```
<div class="yorum">
  <p><script>alert('XSS Saldırısı!');</script></p>
</div>
```
Bu kodu gören tarayıcı, `<script>` etiketi içindeki JavaScript'i çalıştırır ve bir **alert** mesajı gösterir.

## Adım 5: JavaScript’in Çalıştırılması

Kullanıcı, sayfayı ziyaret ettiğinde, yorumda bulunan JavaScript kodu çalıştırılır. Bu, şu şekilde olabilir:

1. **Popup mesajı**: Kullanıcı tarayıcısında bir **alert(‘XSS Saldırısı!’)** mesajı görür.
2. **Daha kötü senaryolar**: Gerçek bir saldırgan, bu JavaScript kodu ile kullanıcıyı zararlı bir siteye yönlendirebilir, çerezlerini çalabilir veya oturum bilgilerini (session cookies) ele geçirebilir.

## Adım 6: Güvenlik Açığının Tespiti

Yukarıdaki senaryoda, saldırganın zararlı kodu depolayıp hedef kullanıcıya sunarak çalıştırabildiğini gözlemledik. Bu tür saldırılar, çok tehlikeli olabilir çünkü bir kez sunucuda depolanan kötü niyetli kod, siteyi ziyaret eden tüm kullanıcıları etkiler.

Bu tür zafiyetler, sitenizin **güvenlik testleri** sırasında belirlenebilir. Örneğin, aşağıdaki testleri gerçekleştirebilirsiniz:

- **Yorum kısmına XSS payload’ı girin**: `<script>alert('XSS!');</script>`
- **Sayfa kaynağını inceleyin**: Eğer XSS kodu site kaynağında olduğu gibi görünüyor ve çalışıyorsa, uygulamanızda Stored XSS zafiyeti olduğunu söyleyebiliriz.

# Sonuç

XSS zafiyetleri, doğru güvenlik önlemleri alınmadığında, kullanıcıların kişisel verilerinin tehlikeye girmesine ve web uygulamalarının güvenliğinin ciddi şekilde zarar görmesine neden olabilir. Bu yazıda anlatılan adımları takip ederek, XSS açıklarını tespit etmek için gerekli temel bilgiye sahip oldunuz. Özel karakterlerin doğru şekilde **encode edilmesi**, kullanıcıdan gelen verilerin güvenli bir şekilde işlenmesi ve dışa yansıtılmadan önce uygun doğrulamaların yapılması gibi önlemler, XSS zafiyetlerini önlemenin en etkili yollarıdır.

**Öneriler:**

1. **Encode işlemleri**: Kullanıcıdan alınan inputların, özellikle HTML, JavaScript veya URL içeriklerinin encode edilmesi büyük önem taşır.
2. **Filtreleme ve doğrulama**: Kullanıcıdan gelen veriler, güvenlik açısından filtrelenmeli ve doğrulanmalıdır.
3. **Güvenlik testleri ve araçlar**: Web uygulamanızı düzenli olarak güvenlik testlerine tabi tutmak ve XSS testlerini çeşitli araçlarla (örneğin, Burp Suite, OWASP ZAP) yapmak kritik öneme sahiptir.
4. **Eğitim ve farkındalık**: Web uygulamalarında çalışan geliştiricilerin, XSS gibi güvenlik açıklarına karşı bilinçli olması, bu tür zafiyetlerin önlenmesinde önemli bir faktördür.

Son olarak, XSS gibi zafiyetlerin etkisini azaltmak için uygulamanızda güvenlik açıklarını tespit etmek ve en iyi güvenlik uygulamalarını takip etmek gereklidir. XSS konusunda daha fazla bilgi edinmek için uygulama içindeki güvenlik açıklarını aktif olarak test etmeye devam edin ve bulgularınızı doğru şekilde raporlayın. Web güvenliği her geçen gün daha fazla önem kazandığı için bu konuda bilgi sahibi olmak ve güncel kalmak, güvenli bir web ortamı oluşturmak adına büyük bir adımdır.

Teşekkürler:

Web Security 0x09 | XSS Güvenlik Zafiyeti Serüvenine Devam Part 2
