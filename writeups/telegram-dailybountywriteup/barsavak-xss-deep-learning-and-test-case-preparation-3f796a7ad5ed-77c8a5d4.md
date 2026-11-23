# XSS Deep Learning and Test Case Preparation

- **Source URL:** https://medium.com/@barsavak/xss-deep-learning-and-test-case-preparation-3f796a7ad5ed?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240701065356/https://medium.com/@barsavak/xss-deep-learning-and-test-case-preparation-3f796a7ad5ed
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6552 (id 6552)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Merhaba Dostlar,

Bu blogda sizlere Gallipoli Bug Bounty topluluğunun ilk görevi olan **XSS (Cross-Site Scripting) türleri için test case yazma** ve **VPS’e deploy etme** konularını anlatacağım. Bu görevleri hazırlayabilmek için önce XSS’in ne olduğu ve çeşitlerinin neler olduğu hakkında bilgi sahibi olmalıyız.

# What is a Cross-Site Scripting Attack?

# Cross-site Scripting (XSS)

Siteler Arası Komut Dosyası Çalıştırma (XSS) saldırıları, kötü amaçlı komut dosyalarının normalde iyi huylu ve güvenilir web sitelerine enjekte edildiği bir tür enjeksiyondur. XSS saldırıları, bir saldırganın, genellikle tarayıcı tarafı komut dosyası biçimindeki kötü amaçlı kodu farklı bir son kullanıcıya göndermek için bir web uygulamasını kullanması durumunda ortaya çıkar. Bu saldırıların başarılı olmasını sağlayan kusurlar oldukça yaygındır ve bir web uygulamasının, doğrulamadan veya kodlamadan ürettiği çıktı içerisinde kullanıcıdan gelen girdiyi kullandığı her yerde meydana gelebilir.

Siteler Arası Komut Dosyası Çalıştırma, kullanıcıyı hedeflemek yerine bir web sitesini tahrif etmek için de kullanılabilir. Saldırgan, web sitesinin içeriğini değiştirmek için enjekte edilen komut dosyalarını kullanabilir veya hatta tarayıcıyı, örneğin kötü amaçlı kod içeren başka bir web sayfasına yönlendirebilir.

Siteler Arası Komut Dosyası Çalıştırma Nasıl Çalışır? Tipik bir XSS saldırısının iki aşaması vardır: Bir kurbanın tarayıcısında kötü amaçlı JavaScript kodu çalıştırmak için, saldırganın öncelikle kurbanın ziyaret ettiği bir web sayfasına kötü amaçlı kod (yük) yerleştirmenin bir yolunu bulması gerekir. Bundan sonra kurbanın kötü amaçlı kodun bulunduğu web sayfasını ziyaret etmesi gerekir. Saldırı belirli kurbanlara yönelikse saldırgan, kurbana kötü amaçlı bir URL göndermek için sosyal mühendislik ve/veya kimlik avını kullanabilir. Birinci adımın mümkün olabilmesi için, savunmasız web sitesinin kullanıcı girişini doğrudan sayfalarına dahil etmesi gerekir. Saldırgan daha sonra web sayfasında kullanılacak ve kurbanın tarayıcısı tarafından kaynak kodu olarak değerlendirilecek kötü amaçlı bir dize ekleyebilir. Saldırganın sosyal mühendislik kullanarak kullanıcıyı bir URL’yi ziyaret etmeye ikna ettiği ve yükün kullanıcının tıkladığı bağlantının bir parçası olduğu XSS saldırılarının çeşitleri de vardır.

There are 3 types of XSS attacks:

- Reflective XSS
- Stored XSS
- DOM-Based XSS

## 1- Reflected XSS

Web sitesi veya uygulama, kullanıcı tarafından kötü niyetli olarak manipüle edilen içeriği (genellikle URL’de) geri yansıttığında, yansıtılmış bir XSS saldırısıyla karşı karşıya kalırız. Bu yansıma, gördüğümüz gibi, tarayıcıların sayfayı görüntüleme biçimini, işleri nasıl işleyip davrandıklarını etkiler. Aşağıdaki PHP kodunu alın:

```
$username = $_GET[‘user’];
echo “<h1>Hello, ” . $username . “!</h1>”;
```
Which would display the user name taken from URL like

`http://mydomain.com/ello.php?user=John`
In source code, it would be:


<h1>Hello, John!</h1>
So, if an attacker use the URL “http://mydomain.com/hello.php?user=\<script>alert(1)\</script>” he/she will be able to make the browser generate the following source code:

`<h1>Hello, <script>alert(1)</script>!</h1>`
## 2- Stored XSS

When the website or application stores user input in a database or a file to display it later, like a field in a profile or a comment in a forum, the resulting attack is called persistent or **stored XSS**. Every user that sees this stored content is a potential victim.

## 2- DOM-Based XSS

*DOM-Based XSS, zararlı kodun doğrudan kullanıcı tarayıcısında, Document Object Model (DOM) üzerinde manipülasyon yapılarak çalıştırıldığı bir XSS türüdür. Bu saldırı türü, sunucuya herhangi bir veri gönderilmeden, sadece istemci tarafında gerçekleşir. DOM-Based XSS saldırıları şu şekilde işler:*

(Aşağıdaki bağlantılardan XSS ne olduğunu çeşitlerinin neler olduğunu nasıl gerçekleştiğini kısaca öğrendikten sonra göreve başlayabiliriz)

[A Pentester’s Guide to Cross-Site Scripting (XSS) | Cobalt](https://www.cobalt.io/blog/a-pentesters-guide-to-cross-site-scripting-xss)

[XSS 101 — Brute XSS (brutelogic.com.br)](https://brutelogic.com.br/blog/xss101/)

[What is Cross-site Scripting and How Can You Fix it? (acunetix.com)](https://www.acunetix.com/websitesecurity/cross-site-scripting/)

[Cross-Site Scripting (XSS) Cheat Sheet — 2024 Edition | Web Security Academy (portswigger.net)](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)

## VPS DEPLOY ETME

Ben, AWS üzerinden VPS deploy ettim. AWS (Amazon Web Services), güçlü ve esnek bulut altyapısı sunar. Bu süreçte AWS EC2 (Elastic Compute Cloud) hizmetini kullanarak sanal sunucular oluşturup yapılandırdım.

nasıl yaptığıma gelin bakalım

öncelikle [Bulut Bilgi İşlem Hizmetleri — Amazon Web Services (AWS)](https://aws.amazon.com/tr/) bağlantısına gidiyorsunuz

buradan oturum açıyorsunuz

arama kısmına EC2 yazıyorsunuz

**EC2 (Elastic Compute Cloud)**, Amazon Web Services’in sunduğu bir web hizmetidir. EC2, kullanıcıların çeşitli konfigürasyonlarda sanal sunucular (instancelar) oluşturmasına ve yönetmesine olanak tanır

1. **Yeni Bir Sunucu Oluşturma**
2. AWS konsolunda **Launch Instance** seçeneğine tıklıyorsunuz. Gerekli yerleri dolduruyoruz:

- **Name and Tags**: Sunucunuza bir isim ve etiketler verin.
- **Application and OS Images (Amazon Machine Image)**: Ben burada **Ubuntu** seçtim.

**Güvenlik Grupları Ayarları**

Sunucunuzun güvenlik gruplarını aşağıdaki gibi yapılandırın:

- **Allow SSH traffic from**: Anywhere (0.0.0.0/0)
- **Allow HTTPS traffic from the internet**: Bu ayar, bir web sunucusu oluştururken örneğin bir endpoint ayarlamak için gereklidir.
- **Allow HTTP traffic from the internet**: Bu ayar da bir web sunucusu oluştururken gereklidir.

**Sunucuyu Başlatma** Güvenlik seçeneklerini işaretledikten sonra **Launch Instance** butonuna tıklayın. Daha sonra sol tarafta bulunan **Instances** kısmına tıklayın. Burada oluşturduğunuz sunucu görünecektir.

**Sunucuya Bağlanma**

Kendi gerekli yapılandırmalarınızı bitirdikten sonra, sunucunuzun yanındaki tik işaretine basın ve sağ üstte bulunan **Connect** butonuna tıklayın. Bu, sunucunuzun komut satırı arayüzünü gösterecektir.

Ayrıca SSH bağlantısı da kurabiliriz.

`ssh -i .\(key pair).pem (username)@IPADDRESS`
**Gerekli Kurulumları Yapma**

Artık yapmanız gereken tek şey, sizin için gerekli olan kurulumları yapmak. Bu kurulumlar arasında PHP, MySQL (stored XSS için) ve Apache olabilir.

AWS üzerinde oluşturduğunuz sunucuya bağlandıktan sonra, komut satırında aşağıdaki adımları takip edebilirsiniz.

1. **Sunucunuzu Güncelleyin**
2. İlk olarak, paket listelerini güncellemek için aşağıdaki komutu çalıştırın:

`sudo apt update`
**3.Apache Kurulumu**

4.Apache web sunucusunu kurmak için aşağıdaki komutu çalıştırın:

`sudo apt install apache2 -y`
5.Apache’nin çalıştığını kontrol etmek için:

`sudo systemctl status apache2`
6.Tarayıcınızda sunucunuzun IP adresini yazarak Apache’nin düzgün çalıştığını doğrulayabilirsiniz.

Herhangi bir başka sorunla karşılaşmanız halinde [Security Groups](https://eu-north-1.console.aws.amazon.com/ec2/home?region=eu-north-1#SecurityGroups:) bölümüne bakmanızda fayda var

# AWS EC2 Güvenlik Grupları (Security Groups) Nedir ve Ne İşe Yarar?

Güvenlik Grupları, EC2 instance’larınızın (sanal sunucularınızın) ağ trafiğini kontrol etmek için kullanılan sanal bir güvenlik duvarıdır. Her EC2 instance’ı başlatıldığında, belirli bir güvenlik grubuna atanır ve bu grup, o instance’ın hangi trafiği kabul edeceğini veya reddedeceğini belirler.

**7.MySQL Kurulumu**

8.MySQL veritabanını kurmak için aşağıdaki komutu çalıştırın:

`sudo apt install mysql-server -y`
9.MySQL kurulumunu güvence altına almak için:

`sudo mysql_secure_installation`
10.Bu komut, sizden bazı güvenlik sorularını yanıtlamanızı isteyecektir. Varsayılan ayarları kullanabilirsiniz.

**11.PHP Kurulumu**

12.PHP ve Apache ile entegrasyonu için gerekli modülleri kurmak için aşağıdaki komutu çalıştırın:

`sudo apt install php libapache2-mod-php php-mysql -y`
**13.Apache’yi Yeniden Başlatma**

14.PHP ve Apache’yi yapılandırdıktan sonra, Apache web sunucusunu yeniden başlatın:

`sudo systemctl restart apache2`
**Kurulumları Doğrulama**

Apache’nin belgeler kök dizininde (`/var/www/html`) bir PHP dosyası oluşturarak kurulumun başarılı olduğunu doğrulayabilirsiniz. Örneğin, `info.php` dosyasını oluşturun:

`sudo nano /var/www/html/info.php`
İçine aşağıdaki PHP kodunu yazın:

`<?php phpinfo(); ?>`
Tarayıcınızda `http://your_server_ip/info.php` adresine giderek PHP bilgilerini görüntüleyebilirsiniz.

Artık test caseleri hazrılama vakti geldi

RXSS1

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
   
    <form method="post" action="">
        <label for="b1">Giriş Yapın:</label>
        <input type="text" id="b1" name="b1" value="">
        <input type="submit" value="Gönder">
    </form>
    <?php
    if (isset($_POST['b1'])) {
        $girilen_metin = $_POST['b1']; 
        echo "<p>Girilen metin: $girilen_metin</p>";
    }
    ?>
    
</body>
</html>
```
Bu örnekte, kullanıcıdan alınan giriş değeri (b1) doğrudan web sayfasında gösterilmektedir. Ancak, herhangi bir filtreleme veya temizleme işlemi yapılmadığı için bu, XSS saldırılarına karşı savunmasızdır.Kullanılan Metod ve Zaafiyetin Sebebi

Kullanılan metod, **POST** metodudur ve kullanıcıdan alınan veri PHP kodu aracılığıyla sayfaya dahil edilmektedir. XSS zaafiyeti, kullanıcı girişinin doğrudan sayfaya dahil edilmesi ve hiçbir doğrulama veya temizleme işlemi yapılmamasından kaynaklanmaktadır.

Örnek payload :

`<script>alert(1)</script>`
RXSS2

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="" method="get">
        <label for="search">Aranacak kelime:</label>
        <!-- Kullanıcı girdisi doğrudan value özelliğine yazılacak -->
        <input maxlength="600" type="text" id="search" placeholder="Search the blog..." name="search" value="<?php echo isset($_GET['search']) ? $_GET['search'] : ''; ?>">
        <input type="submit" value="ara" name="submit">
    </form>
    <?php
    if (isset($_GET['search'])) {
        $aranan_kelime = $_GET['search']; 
        echo "<p>Aradığınız kelime: " . htmlspecialchars($aranan_kelime) . "</p>";
    }
    ?>
</body>
</html>
```
Bu örnek, kullanıcıdan gelen girdiyi doğrudan sayfaya yansıttığı için Reflected XSS saldırılarına karşı savunmasızdır

- Form gönderildiğinde, `search` adlı GET parametresi PHP ile alınır.
- Bu değer, HTML içindeki `value` özelliğine yazılır, böylece form yeniden yüklendiğinde önceki giriş gösterilir.

Örnek payload:

`"><script>alert(1)</script>`
RXSS3

```
 <?php
    if (isset($_SERVER['HTTP_USER_AGENT'])) {
        $user_agent = $_SERVER['HTTP_USER_AGENT'];
        if (stripos($user_agent, 'script') === false) {
            echo "<p>User Agent: " . $user_agent . "</p>";
        } else {
            echo "<p>User Agent contains 'script' and is not displayed for security reasons.</p>";
        }
    }
?>
```
Bu PHP kodu, kullanıcının tarayıcı kullanıcı ajanını (`HTTP_USER_AGENT`) kontrol eder. Kullanıcı ajanı içerisinde 'script' kelimesi geçiyorsa veya benzeri bir şekilde potansiyel olarak zararlı içerik barındırıyorsa, bu bilgi güvenlik nedenleriyle ekrana yazdırılmaz. Aksi takdirde, kullanıcı User Agent bilgisi güvenli olarak ekrana getirilir. Bu yöntem, kullanıcıların tarayıcı agentlerinin istismar ederek XSS saldırıları gerçekleştirmesini önlemeye yardımcı olur fakat başka bir payload ile bunu tetikleyebiliriz.

Örnek payload:

`Payload: User-Agent:<script>alert(1)</script>`  # 2. Stored XSS Test Cases

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yorumlar</title>
</head>
<body>
<!-- Yorum ekleme formu -->
<h2>Yorum Ekle</h2>
<form method="get" action="">
    <input type="text" name="yorum" placeholder="Yorumunuzu yazın">
    <input type="submit" value="Gönder">
</form>
<!-- Yorumları silme formu -->
<h2>Yorumları Sil</h2>
<form method="post" action="">
    <input type="hidden" name="sil" value="1">
    <input type="submit" value="Tüm Yorumları Sil">
</form>
<?php
// PHP hata ayıklama modunu etkinleştirme
ini_set('display_errors', 1);
error_reporting(E_ALL);
// Veritabanı bağlantısı
$servername = "********";
$username = "**********";
$password = "***********";
$dbname = "***********";
// Bağlantıyı oluştur
$conn = new mysqli($servername, $username, $password, $dbname);
// Bağlantıyı kontrol et
if ($conn->connect_error) {
    die("Bağlantı hatası: " . $conn->connect_error);
}
// GET isteğinden veri al ve veritabanına ekle
if (isset($_GET['yorum'])) {
    $yorum = $_GET['yorum'];  // XSS saldırılarına karşı hiçbir önlem alınmamış
    // Veritabanına yorum ekle
    $sql = "INSERT INTO mesajlar (icerik) VALUES ('$yorum')";
    if ($conn->query($sql) === TRUE) {
        echo "Yorum başarıyla kaydedildi!";
    } else {
        echo "Hata: " . $sql . "<br>" . $conn->error;
    }
}
// POST isteğinden veri al ve yorumları sil
if (isset($_POST['sil']) && $_POST['sil'] == 1) {
    $sql = "DELETE FROM mesajlar";
    if ($conn->query($sql) === TRUE) {
        echo " -- Tüm yorumlar silindi! -- ";
    } else {
        echo "Hata: " . $sql . "<br>" . $conn->error;
    }
}
// Kaydedilen yorumları getir ve göster
$sql = "SELECT id, icerik FROM mesajlar";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    echo "<h2>Kullanıcı Yorumları</h2>";
    while($row = $result->fetch_assoc()) {
        echo "<p>Yorum #" . $row['id'] . ": " . $row['icerik'] . "</p>";  // XSS saldırılarına karşı hiçbir önlem alınmamış
    }
} else {
    echo "Henüz yorum yok.";
}
// Bağlantıyı kapat
$conn->close();
?>
</body>
</html>
```
- Kullanıcıların `Yorum Ekle` formuna girdikleri metinler doğrudan HTML çıktısına yansıtılır (`echo "<p>Yorum başarıyla kaydedildi!</p>";`). Bu durum, kullanıcıların kötü niyetli JavaScript kodları ekleyerek XSS saldırıları gerçekleştirmelerine olanak tanır.
- Örneğin, bir kullanıcı `<script>alert('XSS Attack!');</script>` gibi bir metin girdiğinde, bu kodlar tarayıcıda çalıştırılabilir ve kullanıcıların tarayıcı oturumlarını tehlikeye atabilir.

sunucu taraflı olduğu için web sitesini ziyaret eden herkes de zaafiyet kendini gösterecektir

Örnek payload:

`<script>alert(1)</script>`  # 3. Dom-Based XSS Test Cases

dxss1

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<form action="" method="get">
    Değer gir:<input type="text" name="option">
    <input type="submit" name="submit">
</form>
<script>
    // JavaScript ile formdan gelen değeri alıp ekrana yazdırma
    var option = "<?php echo isset($_GET['option']) ? ($_GET['option']) : ''; ?>";
    document.write("Girilen değer: " + option);
</script>
    
</body>
</html>
```
Bu örnekte, DOM-based XSS (Cross-Site Scripting) zaafiyetinin tanımlanabilmesinin nedeni, kullanıcıdan gelen verinin JavaScript tarafından doğrudan DOM’a eklenmesi ve bu eklemenin tarayıcıda gerçekleştirilmesidir

Bu kod, kullanıcıdan bir form aracılığıyla değer alır ve bu değeri sayfada göstermek için JavaScript ve PHP’yi birlikte kullanır. Form gönderildiğinde, PHP değeri alır ve JavaScript bu değeri ekranda gösterir.

Örnek payload:

`"-alert(1)-"`
dxss2

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DXSS2</title>
</head>
<body>
    <h1>DOM XSS Örneği - GET Parametresi</h1>
<p id="output">Girdiğiniz değer:</p>
<script>
    // URL'den param değerini al
    var params = new URLSearchParams(window.location.search);
    var paramValue = params.get('param');
    // Girdiğiniz değer: metnini güncelle
    document.getElementById('output').innerHTML += paramValue;
    // Param değeri içerisinde script etiketi varsa bunu çalıştır
    if (paramValue && paramValue.includes('<script>')) {
        var scriptContent = paramValue.match(/<script>(.*?)<\/script>/)[1];
        var scriptElement = document.createElement('script');
        scriptElement.textContent = scriptContent;
        document.body.appendChild(scriptElement);
    }
</script>
</body>
</html>
```
Bu örnek, URL’deki GET parametrelerini kullanarak nasıl DOM XSS zaafiyetinin oluşabileceğini göstermektedir.

1. Parametrelerin Alınması:

```
var params = new URLSearchParams(window.location.search);
var paramValue = params.get('param');
```
2.Metnin Güncellenmesi:

`document.getElementById('output').innerHTML += paramValue;`
3.Script Etiketinin Çalıştırılması:

```
if (paramValue && paramValue.includes('<script>')) {
    var scriptContent = paramValue.match(/<script>(.*?)<\/script>/)[1];
    var scriptElement = document.createElement('script');
    scriptElement.textContent = scriptContent;
    document.body.appendChild(scriptElement);
}
```
Örnek payload:

`<script>alert(1)</script>`
“Bu hazırladığım caselere aşağıdaki bağlantıdan ulaşabilirsiniz.”
