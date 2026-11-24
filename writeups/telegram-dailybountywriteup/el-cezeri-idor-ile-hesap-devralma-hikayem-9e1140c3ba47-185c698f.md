# IDOR ile Hesap Devralma Hikayem

- **Source URL:** https://medium.com/@el-cezeri/idor-ile-hesap-devralma-hikayem-9e1140c3ba47?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231025195225/https://medium.com/@el-cezeri/idor-ile-hesap-devralma-hikayem-9e1140c3ba47
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4141 (id 4141)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR ile Hesap Devralma Hikayem

--

Uzun bir aradan sonra herkese merhaba ! Bir önceki yazıda subdomain devralma ile ilgili nuclei kullanımına göz atmıştık .

İlgili yazıya buradan ulaşabilirsiniz .

Bugün Hackerone’da bulunan bir VDP programında bulduğum IDOR ile Hesap Devralma Güvenlik Açığını ele alacağız.

Hackerone programlarına göz atıyordum ve bir tane VDP’yi gözüme kestirdim . İlk olarak politikalarını okudum ve hızlıca kapsamlarına göz attım . Kapsam biraz geniş olması sebebiyle bir süre subdomainleri topladım ve çalışanları ayıkladıktan sonra manuel olarak kontrol etmeye başladım .

Siteye hızlıca göz attım ve bunun bir X şirketinin rezervasyonlarını ve diğer satıcılarının ekiplerini oluşturabileceği üzerine çalışıyordu .İlk olarak 2 adet hesap oluşturdum ve bir süre XSS,SQL,IDOR denedim fakat bir şey elde edemedim . Sonrasında profil kısmını ziyaret ettiğimde URL ‘de şu şekil bir sonuç alıyordum :

/user/801910/basic

Ziyaret ettiğimizde profil bilgilerini bizlere getiriyordu ve bunları düzenleme imkanı sunuyordu.

Burada userID kısmını ikinci açtığım hesap ile değiştirmeyi denedim .

/user/80191/basic

fakat bir hata ile karşılaşıyorum , hiçbir şekilde diğer hesabın bilgilerini veya sayfasını sağlamadı .

Sonrasında ekip oluştur bölümüne odaklandım ve orada admin olarak bir ekip oluşturabileceğimiz ve bu ekip arkadaşlarını davet edebileceğimiz bir işlev mevcut . Burada üçüncü bir hesap açtım(user olarak )ve hesabı davet ettikten sonra şunu fark ettim davet ettiğimiz hesabın profilini ziyaret ettiğimizde admin olduğumuz için bu hesabın bilgilerini düzenleyebiliyor ve görüntüleyebiliyoruz .

Bir şey denemek istedim ve ikinci açtığım hesabı davet ettim fakat bu daveti kabul etmeden birinci hesap üzerinden ikinci kullanıcının

/user/80191/basic

profilini ziyaret etmye çalıştım ve başarılı bir şekilde bir kullanıcının mail adresini bilmemiz yeterli olacak şekilde onu davet edebilir , daveti kabul etmezse bile bir ekip üyesi daveti olduğu için hesabına erişebiliyorum .( Burada davet onayı için bir kontrol sağlanmıyor). Bunu hızlıca ekibe bildirdim ve çok kısa süre içerisinde düzeltme sağladılar .

Özet:

1–İki hesap oluşturun ve admin olarak bir ekip oluşturun .

2-Ekibe mail aracılığıyla yeni bir üye davet edin .(davet kabul etmesine gerek yoktur)

3-Davet ettiğiniz üyenin ID numarasını profilinizdeki ID numarası ile değiştirme

4-Başarılı bir şekilde hesabı devralma .

Görüşmek dileğiyle ❤
