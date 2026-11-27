# 2FA Simple Bypass

- **Source URL:** https://medium.com/@akostak/2fa-simple-bypass-4f0dd5b671dd?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142112/https://medium.com/@akostak/2fa-simple-bypass-4f0dd5b671dd
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3848 (id 3848)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 2FA Simple Bypass

Herkese Merhaba, Bugün sizlere web güvenliği alanında bulunan bir zafiyetten biraz bahsetmek istiyorum.Yazıma geçmeden önce Aşağıdaki linkten beni takip edebilir ve yeni yazılarımdan haberdar olmak için takipte kalabilirsiniz.

Takip İçin: [https://www.instagram.com/ali.kostak14/](https://www.instagram.com/ali.kostak14/)

## **Two factor Authantication nedir?**

2FA olarak’ta bilinen Two factor authantication hesaplarımızın güvenliği için oluşturulmuştur.Örneğin mail, sms veya google authenticator gibi mekanizmalar. Kısaca bu adımlar hesaplarınıza entegre edildiğinde giriş yaparken veya şifrenizi değiştirirken gerçekten siz olup olmadığınızı denetliyorlar.

## **Peki benim Raporum neydi ?**

- Bir oyun şirketine gönderdiğim zafiyette şu şekildeydi. Oluşturduğumuz hesaba bir 2fa ekleyebiliyorduk. 2FA nasıl çalıştığını görmek istedim nasıl kayıt ediliyor falan,Burp açtım ve istekleri tek tek repater attım ve neler olacağını görmek istedim. Aşağıda gördüğünüz gibi en son istekte kod gönderilen telefon numarasının 6 haneli kodunun yanlış olup olmadığını denetliyor.

- Burada ilk gözüme çarpan şey bir önceki istekte telefon numarasına 6 haneli kod gönderilmesi için giden isteğin response oldu bir “challange” parametresi oluşturuluyor tabi bu parametrenin kodun doğru olup olmadığını kontrol etmek için oluşturulduğu aşikardı.O yüzden tek yapmam gereken telefon numarasını değiştirip isteği yollamaktı.

Ve BUMMMMMM kabul etti ardından kontrol ettiğimde başka bir telefon numarası eklendiğini gördüm buradan yazılımcı “challange” parametresi ile code parametresini kontrol eden bir kod bloğu yazmış fakat aynı istekte bulunan “phonenumber” parametresini de denetlemeyi pasgeçmiş.

**Başka yazılarda görüşmek üzere, Herkese iyi günler.**
