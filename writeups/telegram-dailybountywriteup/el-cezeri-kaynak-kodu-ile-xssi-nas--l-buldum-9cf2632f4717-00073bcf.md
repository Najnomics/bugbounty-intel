# Kaynak kodu ile XSS’i nasıl buldum ?

- **Source URL:** https://medium.com/@el-cezeri/kaynak-kodu-ile-xssi-nas%C4%B1l-buldum-9cf2632f4717?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240109132349/https://medium.com/@el-cezeri/kaynak-kodu-ile-xssi-nas%C4%B1l-buldum-9cf2632f4717
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4545 (id 4545)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Kaynak kodu ile XSS’i nasıl buldum ?

--

Herkese merhaba ! Bir önceki yazıda IDOR ile Hesap Devralma Hikayemden bahsetmiştim .

İlgili yazıya buradan ulaşabilirsiniz .

Hackerone üzerinden bulunan programlara bakarken bir VDP seçtim ve burada avlanmaya karar verdim . Hızlıca programın kurallarına ve kapsam bölümüne göz attım her şey normal görünüyordu .

Kapsamların dar olması sebebiyle alt alanlar için herhangi bir tarama işlemi gerçekleştirmeden tüm kapsamlara hızlıca baktıktan sonra bir kapsamda bir login ekranı bizi karşılıyordu .

Şirket üyelerine özel bir giriş ekranı , bir ID ve şifre girilmesi beklenmektedir. SQL , default giriş bilgileri gibi ya da istek manipülasyonu denedim hiçbiri çalışmadı.

Daha sonra sayfanın kaynak koduna göz atamaya başladım . Göz atarken burada da bir şeyler buldum gibi .

bu path 2 tane parametre alıyordu ve burada bir arama yapmamız sağlanıyordu . İlk olarak pathi kopyaladım ve şuna benzer şekilde bir filtreleme uygulanıp uygulanmadığını test ettim

/inc/search\_xxxx?xxxx=”`123<>`

aynı şekilde sayfada yansıtıldı . O halde HTML enjeksiyonu denemeye karar verdim

harika o halde bir adım öteye gidelim ve XSS denemeye çalıştım .

/inc/search\_xxxx?xxxx=”>\<script>alert(“cezeri”)\</script>

/inc/search\_xxxx?xxxx=“>\<img src/onerror=prompt(document.cookie)>

Yükler başarılı bir şekilde çalışıyordu . Hızlıca raporu yazdım ve ekibe gönderdim . Kabul edildi ve etkisini belirttikten sonra rapor derecesini güncellediler :)

Görüşmek dileğiyle ❤

Öneri ve sorularınız için bana [linkedln](https://www.linkedin.com/in/yiqitsamet/) adresimden ulaşabilirsiniz .
