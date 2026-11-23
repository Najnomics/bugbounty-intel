# XSS TEST CASE

- **Source URL:** https://medium.com/@aarda418/xss-test-case-6158aad30604?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240704131347/https://medium.com/@aarda418/xss-test-case-6158aad30604
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6547 (id 6547)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS TEST CASE

Selam ben Arda Aslan. Gallipoli bug bounty topluluğunın ilk task’i olan xss test case blogunu hazırladım. Keyifli okumalar…

Yapılacak Adımlar:

1. VPS Deploy Etme
2. Reflected XSS, Stored XSS ve DOM-based XSS test caselerinin kodlarını olabildiğince kendimiz yazarak ve anlayarak VPS üzerinde çalıştırma.

# VPS Deploy Etme

Ben amazonu tercih ettim, öncelikle kayıt oluyoruz.

Search kısmına EC2 yazıyoruz, sarı kutu içinde bulut sunucusunu başlat’a basıyoruz.

Sunucunuza isim verip yanında ücretsiz kullanıma uygun yazanlardan istediğiniz işletim sistemini seçebilirsiniz, ben ubuntu tercih ettim.

Bulut sunucusu türünü t2.micro seçiyoruz.

Sonrasında yeni anahtar çifti oluştur diyoruz, anahtar çifti adını kendinize göre girebilirsiniz.

Anahtar Çifti Türü: RSA

Özel Anahtar Dosya Biçimi: .pem ve anahtar çiftini oluşturuyoruz.

İnternetten gelen HTTPS trafiğine izin ver ve İnternetten gelen HTTP trafiğine izin ver kutucuklarını işaretliyoruz yoksa websitemiz çalışmaz!

Ardından sarı kutucuk içerisindeki Bulut Sunucusunu Başlat’a basıyoruz.

Gelen ekranda bulut sunucumuzu seçip bağlana basıyoruz.

EC2 Bulut Sunucusu Bağlantısı üzerinden direkt bağlan diyerek bağlanabiliriz.

Eğer çalışmazsa kendi makineniz üzerinden SSH İstemcisi üzerinden de bağlanabilirsiniz.

Bunu yapmak için ise aşağıdaki 2 kod yeterli olacaktır.

```
chmod 400 "anahtar_çifti_adı.pem" 
//tırnak içine oluşturduğumuz anahtar çifti adını giriyoruz
```
```
ssh -i "anahtar_çifti_adı.pem" ubuntu@ec().compute-1.amazonaws.com
//parantez içine public ip adresinizi yazacaksınız parantez kullanmadan!
```
# WEB SUNUCUSU KURMA

Apache ya da Nginx ile web sunucusu kurabiliriz, ben apache tercih ettim.

```
sudo apt update
sudo apt install apache2
sudo systemctl start apache2
sudo systemctl enable apache2
```
Şimdi Web Sitemize php ve mysql kuralım.

```
sudo apt install php
sudo apt install mysql
sudo apt install php-mysqli
```
# XSS NEDİR?

XSS (Cross-Site Scripting), web uygulamalarında yaygın olarak bulunan bir güvenlik açığıdır. Bu açık, kullanıcıların girdiği verilerin yeterince doğru bir şekilde filtrelenmemesi veya kaçış karakterlerinin işlenmemesi sonucunda ortaya çıkar.

XSS saldırıları genellikle şu amaçlarla kullanılır:

- **Session hijacking (oturum çalma)**: Kullanıcının tarayıcısındaki oturum bilgilerini ele geçirme.
- **Phishing (kimlik avı)**: Kullanıcıyı yanıltarak hassas bilgileri (örneğin, kullanıcı adı-parola) çalma.
- **Web sayfası içeriğini değiştirme**: Sayfa içeriğini değiştirerek zararlı linkler veya içerik eklemek.

XSS genellikle şu üç temel şekilde gerçekleşir:

- **Reflected XSS**:
- **Nasıl Gerçekleşir**: Reflected XSS saldırıları, kullanıcıya özgü bir veri (genellikle URL parametreleri) üzerinden gerçekleşir. Örneğin, bir arama sorgusu sonucunda veya bir form gönderimi sonucu web uygulaması kullanıcıdan aldığı veriyi doğrudan geri döndürür.
- **Örnek**: Bir kullanıcı arama kutusuna kötü niyetli bir JavaScript kodu girer. Web uygulaması bu girdiyi filtrelemez veya işlemezse, bu kod kullanıcıya geri döner ve tarayıcıda çalıştırılır.
- **Risk**: Kullanıcıya özgü bir URL veya giriş alanı üzerinden hızlı yayılabilir, ancak genellikle geçici bir etkiye sahiptir.
- **Stored XSS**:
- **Nasıl Gerçekleşir**: Stored XSS saldırıları, web uygulamasının veritabanında kalıcı olarak saklanan zararlı kodlar ile gerçekleşir. Örneğin, bir forumdaki kötü niyetli bir yorum veya bir blogdaki zararlı bir içerik.
- **Örnek**: Bir kullanıcı zararlı bir JavaScript kodunu bir forum mesajında veya profil açıklamasında saklar. Bu kod daha sonra diğer kullanıcılar tarafından görüntülendiğinde çalıştırılır.
- **Risk**: Veritabanında kalıcı olması nedeniyle daha geniş bir etki alanına sahip olabilir, çünkü her sayfa yüklendiğinde veya her kullanıcı tarafından görüntülendiğinde etkili olabilir.
- **DOM-based XSS**:
- **Nasıl Gerçekleşir**: DOM-based XSS, tarayıcı tarafından işlenen JavaScript kodları üzerindeki güvenlik açıklarını hedef alır. Bu tür XSS, sunucu tarafında değil, tarayıcıda (Document Object Model — DOM) gerçekleşir.
- **Örnek**: Kötü niyetli bir JavaScript kodu, URL veya başka bir kullanıcı girdisi aracılığıyla web sayfası tarafından dinamik olarak oluşturulan DOM öğelerine enjekte edilir.
- **Risk**: Diğer XSS türlerinden farklı olarak, tarayıcı tarafında gerçekleştiği için sunucu tarafındaki filtreleme önlemleri etkisiz olabilir. Ancak, genellikle daha az yaygın ve spesifik koşullara bağlı olarak gerçekleşebilir.

## a1. Reflected XSS via Get Request Test Case

```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Hoş Geldiniz!</h1>
    <form action="reflected_xss_get.php" method="GET">
        İsminiz: <input type="text" name="name">
        <input type="submit" value="Gönder">
    </form>
</body>
</html>
```
Bir web uygulamasında, kullanıcıdan alınan girdiler (örneğin, arama sorgusu veya kullanıcı adı) URL parametrelerine eklenebilir. Örneğin:

`reflected_xss_get.php?name=<script>alert('XSS!');</script> --payload url'e yazılır--`
## a2. Reflected XSS via Post Request Test Case

```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kullanıcı Adı Girişi</title>
</head>
<body>
  <h1>Kullanıcı Adı Girişi</h1>
  <form id="usernameForm" action="reflected_xss_post.php" method="post">
    <label for="username">Kullanıcı Adı:</label><br>
    <input type="text" id="username" name="username"><br><br>
    <button type="submit">Giriş Yap</button>
  </form>
</body>
</html>
```
Bir web uygulamasında, kullanıcı tarafından girilen veriler (örneğin, bir formda doldurulan metin alanı) sunucuya POST edilir.

`<script>alert('XSS!');</script> --İnput alanına yazılır--`
## a3. Reflected XSS via Request Header Test Case

Genellikle kullanıcı girişi veya kullanıcıya bağlı olmayan verilerin doğrudan HTML sayfasında veya tarayıcıda yorumlanarak çalıştırıldığı bir güvenlik açığı biçimidir.

`<script>alert('XSS!');</script> --HTML Header'da referer alanına yazılır--`
## b1. Stored XSS via Get Request Test Case

```
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Yorum Sayfası</title>
</head>
<body>
<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="GET">
    <label>kullanıcı adı:</label>
    <input type="text" id="isim" name="isim"><br>
    <label>mesaj:</label>
    <input type="text" id="mesaj" name="mesaj"><br>
    <input type="submit" name="send" value="Gönder"><br>
</form>
<?php
$server_name = ""; --bu kısımları kendiniz dolduracaksınız--
$user_name = ""; --bu kısımları kendiniz dolduracaksınız--
$password = ""; --bu kısımları kendiniz dolduracaksınız--
$db_name = ""; --bu kısımları kendiniz dolduracaksınız--
$conn = new mysqli($server_name, $user_name, $password, $db_name);
if ($conn->connect_error) {
    die("Bağlantı hatası: " . $conn->connect_error);
}
if(isset($_GET["send"])) {
    $isim = $_GET["isim"];
    $mesaj = $_GET["mesaj"];
    // SQL sorgusunu oluştururken verileri uygun şekilde işleyin
    $sql_send = "INSERT INTO mesajlar (isim, mesaj) VALUES ('$isim', '$mesaj')";
    if ($conn->query($sql_send) === TRUE) {
        echo "Mesaj başarıyla gönderildi.";
    } else {
        echo "Mesaj gönderme hatası: " . $conn->error;
    }
}
$sql_sorgu = "SELECT id, isim, mesaj FROM mesajlar";
$sql_isleme = $conn->query($sql_sorgu);
if ($sql_isleme === false) {
    echo "Sorgu hatası: " . $conn->error;
} else {
    if ($sql_isleme->num_rows > 0) {
        while ($row = $sql_isleme->fetch_assoc()) {
            echo "<h1>İsim: " . $row["isim"] . "</h1>";
            echo "<p>Mesaj: " . $row["mesaj"] . "</p>";
            echo "<form action='" . $_SERVER['PHP_SELF'] . "' method='GET'>";
            echo "<input type='hidden' name='id' value='" . $row["id"] . "'>";
            echo "<input type='submit' name='delete' value='Mesajı Sil'>";
            echo "</form>";
        }
    } else {
        echo "Hiç mesaj bulunamadı.";
    }
}
if(isset($_GET["delete"])) {
    $id = $_GET["id"];
    $sql_sil = "DELETE FROM mesajlar WHERE id = $id";
    if ($conn->query($sql_sil) === TRUE) {
        echo "Mesaj başarıyla silindi.";
    } else {
        echo "Mesaj silme hatası: " . $conn->error;
    }
}
$conn->close();
?>
</body>
</html>
```
`Payload — <script>alert(‘xss’)</script>`
## b2. Stored XSS via Post Request Test Case

```
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Yorum Sayfası</title>
</head>
<body>
<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
    <label>kullanıcı adı:</label>
    <input type="text" id="isim" name="isim"><br>
    <label>mesaj:</label>
    <input type="text" id="mesaj" name="mesaj"><br>
    <input type="submit" name="send" value="Gönder"><br>
</form>
<?php
$server_name = ""; --bu kısımları kendiniz dolduracaksınız--
$user_name = ""; --bu kısımları kendiniz dolduracaksınız--
$password = ""; --bu kısımları kendiniz dolduracaksınız--
$db_name = ""; --bu kısımları kendiniz dolduracaksınız--
$conn = new mysqli($server_name, $user_name, $password, $db_name);
if ($conn->connect_error) {
    die("Bağlantı hatası: " . $conn->connect_error);
}
if(isset($_POST["send"])) {
    $isim = $_POST["isim"];
    $mesaj = $_POST["mesaj"];
    // SQL sorgusunu oluştururken verileri uygun şekilde işleyin
    $sql_send = "INSERT INTO mesajlar (isim, mesaj) VALUES ('$isim', '$mesaj')";
    if ($conn->query($sql_send) === TRUE) {
        echo "Mesaj başarıyla gönderildi.";
    } else {
        echo "Mesaj gönderme hatası: " . $conn->error;
    }
}
$sql_sorgu = "SELECT id, isim, mesaj FROM mesajlar";
$sql_isleme = $conn->query($sql_sorgu);
if ($sql_isleme === false) {
    echo "Sorgu hatası: " . $conn->error;
} else {
    if ($sql_isleme->num_rows > 0) {
        while ($row = $sql_isleme->fetch_assoc()) {
            echo "<h1>İsim: " . $row["isim"] . "</h1>";
            echo "<p>Mesaj: " . $row["mesaj"] . "</p>";
            echo "<form action='" . $_SERVER['PHP_SELF'] . "' method='POST'>";
            echo "<input type='hidden' name='id' value='" . $row["id"] . "'>";
            echo "<input type='submit' name='delete' value='Mesajı Sil'>";
            echo "</form>";
        }
    } else {
        echo "Hiç mesaj bulunamadı.";
    }
}
if(isset($_POST["delete"])) {
    $id = $_POST["id"];
    $sql_sil = "DELETE FROM mesajlar WHERE id = $id";
    if ($conn->query($sql_sil) === TRUE) {
        echo "Mesaj başarıyla silindi.";
    } else {
        echo "Mesaj silme hatası: " . $conn->error;
    }
}
$conn->close();
?>
</body>
</html>
```
`Payload - <script>alert('xss')</script>`
## b3. Stored XSS via Request Header Test Case

```
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>User-Agent Yönetimi</title>
</head>
<body>
<h2>User-Agent Başlığını Kaydet</h2>
<form method="post" action="">
    <label>User-Agent:</label><br>
    <input type="text" id="userAgent" name="userAgent"><br>
    <input type="submit" name="kaydet" value="User-Agent Kaydet">
</form>
<h2>Kaydedilen User-Agent'ler</h2>
<?php
$server_name = ""; --bu kısımları kendiniz dolduracaksınız--
$user_name = ""; --bu kısımları kendiniz dolduracaksınız--
$password = ""; --bu kısımları kendiniz dolduracaksınız--
$db_name = ""; --bu kısımları kendiniz dolduracaksınız--
function db_con() {
    global $server_name, $user_name, $password, $db_name;
    $conn = new mysqli($server_name, $user_name, $password, $db_name);
    if ($conn->connect_error) {
        die("Bağlantı hatası: " . $conn->connect_error);
    }
    return $conn;
}
function kaydet_user_agent() {
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // User-Agent kaydetme işlemi
        if (isset($_POST['kaydet'])) {
            $userAgent = $_POST['userAgent'];
            
            $conn = db_con();
            $sql = sprintf("INSERT INTO user_agents (user_agent) VALUES ('%s')", $conn->real_escape_string($userAgent));
            
            if ($conn->query($sql) === TRUE) {
                echo "<p>Kaydedilen User-Agent: " . htmlspecialchars($userAgent) . "</p>";
            } else {
                echo "Hata: " . $sql . "<br>" . $conn->error;
            }
            
            $conn->close();
        }
    }
}
function listele_ve_sil() {
    $conn = db_con();
    // Tüm User-Agent kayıtlarını getir
    $sql = "SELECT id, user_agent FROM user_agents";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
        // Kayıtları listeleyelim
        while ($row = $result->fetch_assoc()) {
            echo "<p>ID: " . $row["id"] . " - User-Agent: " . htmlspecialchars($row["user_agent"]) . "</p>";
            echo "<form method='post' action=''>";
            echo "<input type='hidden' name='delete_id' value='" . $row["id"] . "'>";
            echo "<input type='submit' name='sil' value='Sil'>";
            echo "</form>";
        }
    } else {
        echo "<p>Kayıtlı User-Agent bulunamadı.</p>";
    }
    $conn->close();
}
function user_agent_sil() {
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['sil'])) {
        $id = $_POST['delete_id'];
        
        $conn = db_con();
        $sql = "DELETE FROM user_agents WHERE id = $id";
        
        if ($conn->query($sql) === TRUE) {
            echo "<p>ID $id olan User-Agent başarıyla silindi.</p>";
        } else {
            echo "Hata: " . $sql . "<br>" . $conn->error;
        }
        
        $conn->close();
    }
}
kaydet_user_agent();
listele_ve_sil();
user_agent_sil();
?>
</body>
</html>
```
`Payload - <script>alert('xss')</script>`
## a3.DOM-Based XSS via Get Request Test Case

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>XSS Example with GET Request</title>
</head>
<body>
<h2>Welcome to the Dashboard</h2>
<form id="inputForm">
  <label for="context">Enter Context:</label><br>
  <input type="text" id="context" name="context"><br><br>
  <input type="submit" value="Submit">
</form>
<p id="contextOutput"></p>
<script>
  // Form submit olayını dinle
  document.getElementById("inputForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Sayfanın yeniden yüklenmesini önle
    // Formdan context değerini al
    var context = document.getElementById("context").value;
    // Kullanıcıdan gelen veri güvensiz bir şekilde HTML içine yerleştiriliyor
    document.getElementById("contextOutput").innerHTML = context;
  });
</script>
</body>
</html>
```
`Payload — <img src=x onerror=alert(‘xss’)>`
## c2.DOM-Based XSS via Post Request Test Case

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>XSS Example with POST Request</title>
</head>
<body>
<h2>Welcome to the Dashboard</h2>
<form id="inputForm">
  <label for="context">Enter Context:</label><br>
  <input type="text" id="context" name="context"><br><br>
  <input type="submit" value="Submit">
</form>
<p id="contextOutput"></p>
<script>
  // Form submit olayını dinle
  document.getElementById("inputForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Sayfanın yeniden yüklenmesini önle
    // Formdan context değerini al
    var context = document.getElementById("context").value;
    // Kullanıcıdan gelen veri güvensiz bir şekilde HTML içine yerleştiriliyor
    document.getElementById("contextOutput").innerHTML = context;
  });
</script>
</body>
</html>
```
`Payload - <img src=x onerror=alert('xss')>`
## c3.DOM-Based XSS via Request Header Test Case

```
<!DOCTYPE html>
<html>
<head>
    <title>DOM XSS - User-Agent Header</title>
</head>
<body>
    <h1>DOM XSS Örneği - User-Agent Header</h1>
    
    <label for="userAgentInput">Enter User-Agent:</label><br>
    <input type="text" id="userAgentInput" name="userAgentInput"><br><br>
    
    <p id="output"></p>
    <script>
        // Kullanıcı girdisini al
        var userInput = document.getElementById('userAgentInput').value;
        // Kullanıcı girdisini güvenli olmayan şekilde DOM'a ekliyoruz (XSS açığı)
        document.getElementById('output').innerHTML = "User-Agent: " + userInput;
    </script>
</body>
</html>
```
`Payload - <img src=x onerror=alert('xss')>`
