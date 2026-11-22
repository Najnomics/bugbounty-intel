# PortswiggerLabs Anlatımlı- SQL INJECTION-1

- **Source URL:** https://medium.com/@1dnz/portswiggerlabs-anlat%C4%B1ml%C4%B1-sql-injection-1-fdb628519bae?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230724080818/https://medium.com/@1dnz/portswiggerlabs-anlat%C4%B1ml%C4%B1-sql-injection-1-fdb628519bae
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3385 (id 3385)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
SQL Injection, Saldırgan uygulama veritabanına müdahale etmesine izin veren web güvenlik açıklarıdır. Bu güvenlik açığı saldırganın normalde görmemesi gereken bilgileri görmesine neden olur. (Şekil-1)

Saldırının başarılı olması halinde hassas bilgiler elde edilebilir.

# SQL injection Örnekleri

**a- Saklı Veri Geri Alma**,

Sql sorgusuna ek sonuç almak için sorguyu değiştirme işlemi:

[https://](https://insecure-website.com/products?category=Gifts)[trenyol](https://insecure-website.com/products?category=Gifts)[-website.com/products?](https://insecure-website.com/products?category=Gifts)ProductName[=](https://insecure-website.com/products?category=Gifts)Tofu adresindeki sorgu veritabanında Şekil-2 deki görünecektir;

Peki ben urlde gönderilen ProductName kısmına ekstra sql kodu enjekte edersem bana dönen sonuç nasıl değişir;

[https://trenyol-website.com/products?](https://insecure-website.com/products?category=Gifts)ProductName[=](https://insecure-website.com/products?category=Gifts)Tofu+OR+1=1

Gönderilen sorgu veritabanından aşağıdaki Şekil-3 gibi sonuç dönderecektir.

## Lab: [SQL injection](https://portswigger.net/web-security/sql-injection) vulnerability in WHERE clause allowing retrieval of hidden data

Bu laboratuvar, ürün kategorisi filtresinde bir SQL ekleme güvenlik açığı içermektedir.

## çözüm:

category parametresinin değerine eklenen ‘OR 1=1 — ; ile diğer bütün verileri alabiliriz. Şekil-4

**b- Uygulama mantığını alt üst etme**

Kullanıcı adı ve şifre ile login olduğumuz bir uygulama düşünelim. Örnek bir uygulamada w*iener* ve *bluecheese* ile login olduğumuz zaman veritabanına giden sorgu;

*SELECT \* FROM users WHERE username = ‘wiener’ AND password = ‘bluecheese’*

Kullanıcı adına ekleyeceğimiz yorum satırı ile SQL sorgusunda username kısmından sonraki komut bloğunun yorum haline getirebiliriz. Daha sonbra login olma işlemini sadece kullanıcı adı ile yapabiliriz.

SELECT \* FROM users WHERE username = ‘administrator’ — ‘ ’AND password = ‘’

## Lab: [SQL injection](https://portswigger.net/web-security/sql-injection) vulnerability allowing login bypass

## Çözüm:

Şekil-5 de Kullanıcı adına eklenen ‘ — ifadesi ile sql sorgusundaki password kısmı yorum satırına dönüştürülmüş ve sisteme login olunmuştur.

**c- Diğer veritabanı tablolarından veri alma**

Uygulama üzerinde yapılan sorguda ek bir SELECT ekleyerek bize dönen orjinal sonuçlara diğer tablodaki verileri eklememiz sağlayan UNION komutu ile yapılan sql injection saldırısıdır.

**Union kullanırken**:

- Sorgular aynı sayıda sütun döndürmelidir.
- Her sütundaki veri türleri, sorgular arasında uyumlu olmalıdır

**Örnek Anlatım ile union kulanımları:**

Yukardaki Şekil-6 ve Şekil-7 deki iki tablo bileştirme için aşağıdaki sorguyu kullanacağız:

*SELECT first\_name, age FROM Customers UNION SELECT item,amount FROM Orders;*

Yukardaki Şekil-8 deki örnekte sorgudaki sütun sayılarını bildiğimiz için sorguları bileştirmeden sorun yaşamadık.

Union saldırısı yapabilmemiz için:

- Orijinal sorgudan kaç sütun döndürülüyor?
- Orijinal sorgudan döndürülen hangi sütunlar, enjekte edilen sorgunun sonuçlarını tutmak için uygun veri türündedir?

## **Sütun Belirlemek için**

**++ORDER BY kullarak:**

Sorguda dönen sütunları sayısını bulmak için sırasıyla sütunları artan sırada sıralarız. Olmayan sütunu sıralamaya çalıştığımız zaman hata dönecektir.

**Örnek Anlatım:**

Aşağıdaki örnek SQL sorgusunda bize iki sütunlu bir çıktı veriyor.

1.sütundaki verileri sıraladığımız zamana Şekil-9 daki;

2.sütundaki verileri sıraladığımız zamana Şekil-20 daki:

3\. sütundaki (yani sorguda olmayana sütun) verileri sıraladığımız zamana Şekil-11 deki:

Bu yolla sorgudaki sütunları tespit edebiliriz.

**++UNION SELECT Kullanarak**

Sorguda dönen sütunları bulmak için union komutu ile tabloya NULL eklemesi yaparız. Sütunlarla aynı saydıda NULL sütunu eklendiği zaman hata almayacağız. Böylelikle veritabanı sorgusunda dönen sütun sayısını bulmuş olacağız.

**Örnek Anlatım:**

Yukardaki Şekil-12 tabloya yapılan sorguda;

1 tane NULL sütun eklenerek Şekil-13 deki sorgu çalıştırıldığı zaman hata alıyoruz. Hatanın sebebi sütun sayısı kadar NULL eklenmediği içindir.

2 tane NULL sütun eklenerek Şekil-14 deki sorgu çalıştırıldığı zaman hata alıyoruz. Hatanın sebebi sütun sayısı kadar NULL eklenmediği içindir.

3 tane NULL sütun eklenerek Şekil-15 deki sorgu çalıştırıldığı zaman sorgu doğru bir şekilde cevap veriyor.

Sorgudaki sütun sayısı kadar null eklendiğinde geriye hata dönüşü olmamaktadır. Bu işlem doğru sütun sayısını bulana kadar devam ettirilir.

## Lab: [SQL injection UNION](https://portswigger.net/web-security/sql-injection/union-attacks) attack, determining the number of columns returned by the query

**Çözüm:**

2 sütun NULL ekleyerek sorgudaki sütunları bulmaya çalıştığımız zaman Şekil-16 deki hatayı alıyoruz.

3 sütun NULL ekleyerek sorgudaki sütunları bulmaya çalıştığımız zaman hata olmadan Şekil-18 deki cevap alıyoruz.

**\*\*Bir SQL enjeksiyonu UNION saldırısında kullanışlı bir veri türüne sahip sütunları bulma**

Bu saldırıda veritabanındaki tabloların ve sütunların bilinmesi gerekmektir.

Şekil-19 da veritabanında iki tablo bulunduğunu varsayalım.

Veritabanında amount sütununa ait verileri çekmek istediğimiz zaman Şekil-20 deki sonucu elde ederiz.

## Lab: [SQL injection UNION](https://portswigger.net/web-security/sql-injection/union-attacks) attack, retrieving data from other tables

category parametresine eklenen union sorgusu ile users veritabanındaki username ve password verileri alınmıştır. Şekil-21

**++Çoklu Sütunları tek Sütunda yazdırma**

Veritabanında bulunan tablolardaki birden fazla sütundaki veriyi bileştirerek tek bir sütunda çıktı alabiliriz. Bu işlem için **union** ve bileştirme operatörü (**||**) kullanılabiliriz.

**Örnek Anlatım:**

Customers tablosuna yaptığımız sorguda first\_name sütununda Orders tablosuna ait amount ve item sütunlarına ait verilerini tek sütun olarak yazdırabiliriz. (Şekil-22)

Bu bileştirme işlem için union ve bileştirme operatorü kullanılarak Şekil-23 deki tablo çıktısı alınmıştır.

**Lab:SQL injection UNION attack, retrieving multiple values in a single column**

-ilk olarak kaç tane sütun sorguda dönüyor bunu tespit etmemiz gerekir; UNION SELECT NULL,NULL — ile sütun sayısını belirliyoruz Şekil-25.

-ikinci adımda sütun sayısını belirledikten sonra hangi sütunlardan veri alabiliriz diye kontrol ediyoruz. Şekil-26

son olarak, Şekil-27 deki Category parametresi ile veritabanında yapılan sorguda dönen cevaba users tablosundaki username ve password sütunlarını da ekliyoruz.

Sql Injection atağında saldırı yapmış olduğumuz veritabanına ait diğer tablolarını bilgilerini almaya çalışacağız.

## \* Oracle Olmayan veritabanında bütün tabloları listelemek:

# LAB: SQL injection attack, listing the database contents on non-Oracle databases

-ilk olarak UNION SELECT NULL ile veritabanına yapılan sorgudaki sütun sayılarını tespit ediyoruz. (Şekil-28)

ikinci adımda veritabanındaki bütün tablolar hakkında meta bilgileri almaya çalışacağız. Bunun için sql sorgusunu **information\_schema.tables** yapacağız. (Şekil-29)

Bizim için önemli veri taşıyan **users\_odctx** tablosunu tespit ediyoruz.

Üçüncü adımda bulduğumuz tabloya ait kolonları tespit etmemiz gerekiyor. Bunun için sql **information\_schema.columns** sorgusunu kullanabiliriz. (Şekil-31)

Tabloya ait kolonları tespit ettikten sonra bu kolonlardaki verileri almaya çalışacağız. (Şekil-32)

## \* Oracle veritabanında bütün tabloları listelemek:

## Lab: [SQL injection](https://portswigger.net/web-security/sql-injection) attack, listing the database contents on Oracle

ilk olarak veritabanı sorgusu ile bütün tabloların bilgilerini alıyoruz. Bunun için all\_tables komutunu kullanıyoruz. (Şekil-33)

Tespit ettiğimiz kullanıcı tablosundaki sütun adılarını çekiyoruz. (Şekil-34)

Kullanıcı tablosundaki kullanıcı adı ve şifrelerin olduğu kolonlardaki bilgileri çekiyoruz.(Şekil-35)

Diğer portswigger lab çözümlerinde görüşmek üzere…

#bugbounty #hunter #sqlInjection
