# SQL Injection Nedir, Nasıl Engellenir?

- **Source URL:** https://medium.com/@M0T3L/sql-injection-nedir-nas%C4%B1l-engellenir-dad7fe97f141?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230530121146/https://medium.com/@M0T3L/sql-injection-nedir-nas%C4%B1l-engellenir-dad7fe97f141
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2834 (id 2834)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection Nedir, Nasıl Engellenir?

--

OWASP tarafından 2021’de yayınlanan Top 10 Web Uygulama Güvenliği Riskleri listesinde 3. sırada yer alan SQL injection nedir, nasıl tespit edilir ve nasıl engelleniri örnekleriyle inceleyeceğiz. Öncelikle tanımlamak gerekirse, SQL injection bir veri tabanına sahip bir web uygulamasındaki bir SQL sorgusunu manipüle etmek diyebiliriz. Böylece yetkisiz bir kullanıcı tarafından normal bir kullanıcının erişememesi gereken bir veriye erişilebilir, veri tabanındaki veriler manipüle edilebilir hale gelir. SQL injection saldırısı ile şifreler, kredi kartı bilgileri veya kişisel kullanıcı bilgileri gibi hassas verilere yetkisiz erişim sağlanabilir. Son yıllarda birçok yüksek profilli veri ihlali, SQL injection saldırısı sonucu olarak meydana gelmiştir. Bu durum, itibar kaybına ve düzenleyici cezalara yol açabilir. Bazı durumlarda, saldırganlar kuruluşların sistemlerine kalıcı bir backdoor elde edebilir ve uzun süreli bir tehlikenin fark edilmeden devam etmesine neden olabilir.

**2017 Euıfax Veri İhlali**

Yakın tarihten örnek vermek gerekirse 2017 yılında gerçekleşen Equifax veri ihlali, geçtiğimiz yılların en büyük siber saldırı örneklerinden biri olarak gösterilebilir. Bu saldırı, SQL injection saldırısı ile gerçekleştirilmiştir. Equifax, Amerika Birleşik Devletleri merkezli bir kredi raporu sağlayıcısıdır ve 2017 yılında meydana gelen bu saldırı, milyonlarca kişinin kişisel ve finansal bilgilerini etkilemiştir.

**SQL Nedir?**

SQL injection örneklerine geçmeden önce SQL nedir, çok kısa bir şekilde değinmek gerekirse: SQL, structured query language kelimelerinin baş harflerinden oluşan, yapılandırılmış sorgu dili anlamına gelen, bilgileri ilişkisel bir veri tabanında depolamak ve işlemek için kullanılan bir programlama dilidir. Yani sizin bir veritabanında sorgu yapabilmek için kullanmanız gereken dildir kısacası.

**SQL Injection Nasıl Çalışır?**

Konuya biraz da örnek üzerinden devam edelim. Senaryomuzda bir web sitesinin giriş kısmında SQL sorgusu çalıştırmaya çalışan bir saldırganımız var.

Kullanıcı adı yerine yavuz ve şifre yerine pass123 bilgilerini giren saldırgana dönen yanıt ‘Hatalı Giriş’ oldu. Fakat burda dikkatimizi çeken şey saldırganın girdiği bilgilerin SQL sorgusuna olduğu gibi eklenmesi. Eğer saldırgan password kısmını kaldırırsa veritabanında varolan herhangi bir kullanıcı adı ile sisteme giriş yapabilir. Yapması gereken username kısmından sonrasını yorum satırı haline getirmek. Bunun için username kısmını yavuz”- — olarak doldurursa öncelikle username yerine gelmesi gereken kullanıcı adı için yavuz kullanıcısını seçmiş, ardından username’i kapsayan tırnak işaretini kapatmış ve satırın geri kalan kısmını yorum satırı haline getirmiş oluyor.

Böylece saldırgan başarılı bir şekilde giriş yapmış oluyor.

**SQL Injection Nasıl Engellenir?**

Bir de basitçe bu zaafiyeti nasıl kapatırız ona bakalım. Öncelikle kodumuzu tekrar incelersek aldığımız inputta herhangi bir parametre olmadığını görüyoruz. Client-side’da aldığımız inputu filtrelesek bile yetmeyeceği için server-side’da da önlem almamız gerek.

```
uName = getRequestString("username");
uPass = getRequestString("userpassword");
sql = 'SELECT * FROM Users WHERE Name ="' + uName + '" AND 
Pass ="' + uPass + '"'
```
Alabileceğimiz önlemler:

- HTML attribute’leri saldırgan tarafından manipüle edilebileceği ve form script kodları ile çağırılabileceği için id’ler değişken yapıda olmalıdır.
- Her submit backend’i tetiklememeli, client-side’da alınan input filtrelenmeli ve doğrulanmalıdır. (regex validation)
- Eğer kurallar sağlanmazsa formun submit edilmesi önlenmeli.
- Server-side’da ise alınan inputlar için bir blacklist olmalı ve eğer input blacklistteki bir ifadeyi içeriyorsa sql komutu execute edilmemeli.
- Request limiter ile “sqlmap” gibi araçlardan sürekli gelen istekler engellenmeli. • Veritabanında dönen hata kullanıcıya dönmemeli.
- ORM kullanılabilir.
- Kullanıcıdan alınan input direkt olarak query’e verilmemeli.
- Tırnak işareti, kısa çizgi vs. gibi özel karakterler encode edilmeli.
- Web application firewall kullanılmalı.

Şemamız aşağıdaki şekilde olabilir.

Ve güvenli kodumuz ise:

```
def getSafeInput(prompt):
 value = input(prompt)
 return html.escape(value)
def getSafePassword(prompt):
 value = input(prompt)
 return html.escape(value).encode("utf-8")
uName = getSafeInput("Kullanıcı adı: ")
uPass = getSafePassword("Şifre: ")
nameRegex = re.compile(r"^[A-Za-z0-9_-]{3,20}$")
passRegex = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$")
if not nameRegex.match(uName):
 print("Not Valid!")
 exit()
if not passRegex.match(uPass):
 print("Not Valid!")
 exit()
sql = 'SELECT * FROM Users WHERE Name = ? AND Pass = ?'
params = (uName, uPass)
```
**Son Söz**

Her ne kadar yazılan kod güvenli de olsa unutmayın ki hiçbir sistem güvenli değildir. Kurumunuzu tehditlerden korumak için siber güvenlik danışmanlığı, düzenli sızma testi hizmeti, SOC ve MDR hizmeti almak tehditlere karşı risk faktörünü düşürür. Böylece IT altyapınızda güvenlik riski oluşturabilecek yapılanmaların varlığı veya yeni projelerde olası güvenlik risklerini ortadan kaldırabilirsiniz.
