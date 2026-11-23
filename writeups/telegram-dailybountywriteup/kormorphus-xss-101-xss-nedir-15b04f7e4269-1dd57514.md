# XSS 101

- **Source URL:** https://medium.com/@kormorphus/xss-101-xss-nedir-15b04f7e4269?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240630170936/https://medium.com/@kormorphus/xss-101-xss-nedir-15b04f7e4269
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6558 (id 6558)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **XSS 101: XSS Nedir ?**

Herkese merhabalar. Bu yazımda sizlere Gallipoli Topluluğu’nun Bug Bounty eğitimi için verilmiş XSS Test Case görevinden bahsedeceğim.

Bu eğitimde amaç XSS türlerini anlamak adına XSS test case’leri hazırlamaktır. Reflected XSS (RXSS), Stored XSS (SXSS) ve DOM-Based XSS (DOMXSS) türlerinde test case yazıp daha sonrasında kendi oluşturduğumuz VPS (Virtual Private Server) üzerine bu test case’lerini deploy edeceğiz.

Adım adım Reflected XSS, Stored XSS ve DOM-Based XSS testlerini nasıl gerçekleştirdiğimi, karşılaştığım sorunları ve nasıl çözdüğümüzü paylaşacağım. Umarım bu yazı, siz yeni başlayanlar için faydalı olur!

**İlk Adım: AWS Üzerinde Bir Web Sunucusu Kurmak**

Öncelikle görevi yapmaya Amazon üzerinden AWS EC2 instance’ı oluşturmakla başladım. Bir Linux makinesi kurdum ve üzerine Apache web sunucusunu yükledim. İşte adım adım nasıl yaptığımı:

1\) **EC2 Instance Oluşturma**:

AWS hesabıma giriş yaptım ve EC2 Dashboard’dan yeni bir instance başlattım.

Amazon Linux 2 AMI’sini seçtim ve t2.micro tipi bir instance seçtim (ücretsiz kullanım katmanı kapsamında).

2\) **Apache Kurulumu**:

sudo yum update -y

sudo yum install httpd -y

sudo systemctl start

httpd sudo systemctl enable httpd

Apache’yi kurduktan sonra, `ec2-13-51-121-212.eu-north-1.compute.amazonaws.com` adresinden sunucuma erişebiliyordum.

**Reflected XSS Test Case’leri**

Reflected XSS ile başladım. Reflected XSS, kullanıcıdan alınan girdinin anında tarayıcıya gönderildiği bir saldırı türüdür. İlk olarak bir GET isteği ile XSS testi yaptık.

**1) GET İsteği ile Reflected XSS**

**1.1) HTML ve PHP Dosyası** (reflected-get.php):

\<!DOCTYPE html>

\<html lang=”en”>

\<head>

\<meta charset=”UTF-8">

\<title>Reflected XSS Test — GET Request\</title>

\</head>

\<body>

\<h1>Reflected XSS Test — GET Request\</h1>

\<p>\<?php echo isset($\_GET\[‘msg’\]) ? $\_GET\[‘msg’\] : ‘’; ?>\</p>

\</body>

\</html>

Bu dosya, URL’den gelen msg parametresini doğrudan HTML içinde görüntüler. Bu güvenli değildir ve XSS açığına yol açar.

**Test Etme**:

http://ec2-13-51-121-212.eu-north-1.compute.amazonaws.com/reflected-get.php?msg=\<script>alert('XSS')\</script> adresine giderek alert(‘XSS’) çalıştırdım.

**2) POST İsteği ile Reflected XSS**

**2.1) HTML ve PHP Dosyası** (reflected-post.php):

\<!DOCTYPE html>

\<html lang=”en”>

\<head>

\<meta charset=”UTF-8">

\<title>Reflected XSS Test — POST Request\</title>

\</head>

\<body>

\<h1>Reflected XSS Test — POST Request\</h1>

\<form method=”post”>

\<label for=”message”>Enter message:\</label>

\<input type=”text” id=”message” name=”message”>

\<button type=”submit”>Submit\</button>

\</form>

\<p>\<?php echo isset($\_POST\[‘message’\]) ? $\_POST\[‘message’\] : ‘’; ?>\</p>

\</body>

\</html>

Form aracılığıyla gelen message parametresi doğrudan HTML içine yerleştirilir. Bu da güvenli değildir.

**Test Etme**:

Formdan \<script>alert(‘XSS’)\</script> girdisini göndererek alert(‘XSS’) çalıştırdım.

**Stored XSS Test Case’leri**

Stored XSS, kötü niyetli girdinin bir veritabanına kaydedildiği ve daha sonra bu girdinin diğer kullanıcılara gösterildiği saldırı türüdür.

**1) Veritabanı ve PHP Dosyaları**:

**1.1) Veritabanı Yapılandırması**:

CREATE DATABASE xss\_test;

USE xss\_test;

CREATE TABLE comments (

id INT AUTO\_INCREMENT PRIMARY KEY,

comment TEXT NOT NULL

);

**Form ve Veri Gösterimi** (stored-xss.php):

\<!DOCTYPE html>

\<html lang=”en”>

\<head>

\<meta charset=”UTF-8">

\<title>Stored XSS Test\</title>

\</head>

\<body>

\<h1>Stored XSS Test\</h1>

\<form method=”post” action=”submit.php”>

\<label for=”comment”>Enter comment:\</label>

\<textarea id=”comment” name=”comment”>\</textarea>

\<button type=”submit”>Submit\</button>

\</form>

\<?php

$conn = new mysqli(‘localhost’, ‘newuser’, ‘new\_password’, ‘xss\_test’);

$result = $conn->query(“SELECT \* FROM comments”);

while ($row = $result->fetch\_assoc()) {

echo “\<p>{$row\[‘comment’\]}\</p>”;

}

$conn->close();

?>

\</body>

\</html>

**Veritabanına Veri Ekleme** (submit.php):

\<?php

$conn = new mysqli(‘localhost’, ‘newuser’, ‘new\_password’, ‘xss\_test’);

$comment = $\_POST\[‘comment’\];

$conn->query(“INSERT INTO comments (comment) VALUES (‘$comment’)”);

$conn->close();

header(‘Location: stored-xss.php’);

?>

**Test Etme**:

Formdan \<script>alert(‘XSS’)\</script> yorumunu göndererek veritabanına kaydettim ve sayfa yüklendiğinde alert(‘XSS’) çalıştırıldı.

**DOM-Based XSS Test Case’leri**

DOM-Based XSS, JavaScript’in doğrudan DOM (Document Object Model) manipülasyonları üzerinden yürütülen bir saldırı türüdür.

**GET İsteği ile DOM-Based XSS**

1\. **HTML ve PHP Dosyası** (domxss-get.php):

\<!DOCTYPE html>

\<html lang=”en”>

\<head>

\<meta charset=”UTF-8">

\<title>DOM-Based XSS Test — GET Request\</title>

\<script>

document.addEventListener(‘DOMContentLoaded’, function() {

var params = new URLSearchParams(window.location.search);

var msg = params.get(‘msg’);

if (msg) {

var targetElement = document.getElementById(‘message’);

targetElement.innerHTML = msg; // Güvensiz, XSS açığına yol açabilir

}

});

\</script>

\</head>

\<body>

\<h1>DOM-Based XSS Test — GET Request\</h1>

\<p id=”message”>\<?php echo isset($\_GET\[‘msg’\]) ? htmlspecialchars($\_GET\[‘msg’\], ENT\_QUOTES, ‘UTF-8’) : ‘’; ?>\</p>

\</body>

\</html>

**Test Etme**:

http://ec2-13-51-121-212.eu-north-1.compute.amazonaws.com/domxss-get.php?msg=\<script>alert('DOMXSS')\</script> adresine giderek alert(‘DOMXSS’) çalıştırdım.

**POST İsteği ile DOM-Based XSS**

1\. **HTML ve PHP Dosyası** (domxss-post.php):

\<!DOCTYPE html>

\<html lang=”en”>

\<head>

\<meta charset=”UTF-8">

\<title>DOM-Based XSS Test — POST Request\</title>

\<script>

document.addEventListener(‘DOMContentLoaded’, function() {

var message = ‘\<?php echo isset($\_POST\[‘message’\]) ? htmlspecialchars($\_POST\[‘message’\], ENT\_QUOTES, ‘UTF-8’) : ‘’; ?>’;

var targetElement = document.getElementById(‘message’);

targetElement.innerHTML = message;

if (message.includes(‘\<script>’)) {

alert(‘DOMXSS’); // Uyarı kutusu

}

});

\</script>

\</head>

\<body>

\<h1>DOM-Based XSS Test — POST Request\</h1>

\<form method=”post”>

\<label for=”message”>Enter message:\</label>

\<input type=”text” id=”message” name=”message”>

\<button type=”submit”>Submit\</button>

\</form>

\<p id=”message”>\</p>

\</body>

\</html>

**Test Etme**:

Formdan \<script>alert(‘DOMXSS’)\</script> mesajını göndererek alert(‘DOMXSS’) çalıştırdım.

Bu yazıda, bug bounty macerama Reflected XSS, Stored XSS ve DOM-Based XSS testleriyle nasıl başladığımı ve karşılaştığım sorunları nasıl çözdüğümü anlattım. Her adımda yeni şeyler öğrendim ve hatalardan ders çıkararak ilerledim. Bu eğitimleri düzenlediği için Gallipoli Topluluğuna teşekkür ediyorum. Umarım bu rehber, siz yeni başlayanlar için faydalı olur ve kendi XSS testlerinizi gerçekleştirmenizde yardımcı olur.
