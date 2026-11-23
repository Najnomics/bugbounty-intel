# “XSS ve Context Örnekleri”

- **Source URL:** https://medium.com/@sgzldmrc/xss-ve-context-%C3%B6rnekleri-6ba2bc976c1f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241109090306/https://medium.com/@sgzldmrc/xss-ve-context-%C3%B6rnekleri-6ba2bc976c1f
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7798 (id 7798)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **“XSS ve Context Örnekleri”**

# 1. HTML Context Nedir?

Web sayfalarında XSS zafiyetleri, kullanıcı girdilerinin çeşitli HTML context’lerine güvenlik önlemleri olmadan yerleştirilmesiyle ortaya çıkar. Bu context’ler şunları içerir:

- **Element Context**: HTML etiketleri içinde.
- **Attribute Context**: Etiketlerin özelliklerinde.
- **Script Context**: JavaScript kodları içinde.
- **CSS Context**: CSS kodları veya `style` özelliklerinde.

Her context’in işleyişi farklı olduğundan, saldırılar ve önlemler de değişiklik gösterir.

# 2. Attribute Context (Özellik Bağlamı)

HTML etiketlerine eklenen özelliklerde (örn. `src`, `href`, `onload`, `onclick`) XSS saldırıları kolayca tetiklenebilir. Örneğin, bir resim etiketinde `onerror` özelliği kullanılarak kötü niyetli kod çalıştırılabilir:

`<img src="invalid.jpg" onerror="alert('XSS')">`
Bu örnekte, resim yüklenemezse `onerror` özelliği devreye girerek bir JavaScript kodunu çalıştırır. Saldırgan bu şekilde özel karakterlerle sahte bir kod enjekte edebilir.

**Önleme Önerileri:**

- Özellikle `onload`, `onerror`, `onclick` gibi olay özelliklerinde kullanıcıdan gelen veriler asla doğrudan kullanılmamalıdır.
- Tüm attribute değerleri, HTML entity encode edilmelidir (örn. `&` için `&`).

Örnek:

# 1. `href` Özelliğinde XSS

`<a>` etiketinin `href` özelliğinde kullanıcı girdiği `javascript:` protokolüyle XSS yapılabilir.

**Örnek:**

`<a href="javascript:alert('XSS!')">Click me</a>`
Bu örnekte, bir saldırgan `href` özelliğine `javascript:` protokolünü kullanarak XSS saldırısını gerçekleştirebilir.

**Önleme:**

- `href` gibi özelliklerde yalnızca güvenli URL protokollerine izin verin (örneğin, `http` veya `https`).
- URL encode işlemiyle özel karakterleri engelleyin veya URL doğrulaması yapın.

# 2. `src` Özelliğinde XSS

Resim, iframe veya video etiketlerinde `src` özelliğine zararlı kod eklenerek XSS tetiklenebilir. `javascript:` veya `data:` protokolleri bu durumlarda kullanılabilir.

**Örnek:**

`<img src="javascript:alert('XSS!')"`
Bu örnekte, `img` etiketinin `src` özelliği `javascript:` protokolünü kullanarak JavaScript kodu çalıştırabilir.

**Önleme:**

- Yalnızca güvenli kaynaklardan gelen dosyaların yüklenmesine izin verin.
- `src` özelliklerinde `javascript:` ve `data:` gibi tehlikeli protokolleri engelleyin.

# 3. `onerror` Özelliğinde XSS

Resim yüklenmediğinde tetiklenen `onerror` özelliği, XSS için yaygın kullanılan yöntemlerden biridir. Kötü niyetli bir kullanıcı `onerror` içine JavaScript kodu ekleyebilir.

**Örnek:**

`<img src="invalid.jpg" onerror="alert('XSS!')">`
Bu örnekte, `invalid.jpg` yüklenemediğinde `onerror` özelliği devreye girerek JavaScript kodunu çalıştırır.

**Önleme:**

- Kullanıcıdan gelen girdileri doğrudan `onerror` gibi olay özelliklerinde kullanmaktan kaçının.
- HTML entity encode ile özel karakterleri kaçırın.

# 4. `onclick` Özelliğinde XSS

Kullanıcının bir ögeye tıklamasıyla tetiklenen `onclick` özelliği, Attribute Context’te en çok kullanılan XSS vektörlerinden biridir. Kullanıcı girdisi doğrudan `onclick` içerisine yerleştirildiğinde, XSS saldırıları mümkün hale gelir.

**Örnek:**

`<button onclick="alert('XSS!')">Click me</button>`
Bu örnekte, `onclick` özelliği kullanılarak `button` etiketi üzerinden JavaScript çalıştırılabilir.

**Önleme:**

- `onclick` ve benzeri olay özelliklerinde kullanıcı girdilerini doğrudan kullanmayın.
- Alternatif olarak, JavaScript içinde olay işleyicilerini atayın ve kullanıcı girdilerini sanitize edin.

# 5. `style` Özelliğinde XSS

`style` özelliğinde inline CSS kullanımı, XSS riskine yol açabilir. Özellikle `background-image` veya `url()` gibi CSS özellikleri içinde XSS saldırıları yapılabilir.

**Örnek:**

`<div style="background-image: url('javascript:alert(1)')">Test</div>`
Bu örnekte `background-image` özelliğinde `javascript:` protokolü ile zararlı kod çalıştırılabilir.

**Önleme:**

- `style` içinde kullanıcı girdisi yerleştirmekten kaçının.
- URL protokollerini kısıtlayarak `javascript:` gibi tehlikeli protokolleri engelleyin.

# 6. `title` Özelliğinde XSS

`title` özelliği, doğrudan kullanıcıya gösterilmese de XSS içerebilir. Tarayıcı bu değeri encode etmezse, bazı özel durumlarda XSS açığı oluşturabilir.

**Örnek:**

`<a href="#" title="javascript:alert('XSS')">Hover over me</a>`
Bu örnekte, kullanıcı `title` içine bir XSS payload yerleştirirse, tarayıcı bunu çalıştırabilir (tarayıcıya göre değişiklik gösterebilir).

**Önleme:**

- Kullanıcıdan gelen `title` gibi girdileri HTML entity encode edin.
- `title` gibi kullanıcıya doğrudan gösterilmeyen alanlarda özel karakterleri kaçırın.

# 7. `data-*` Özelliklerinde XSS

HTML5 ile gelen `data-*` özellikleri, geliştiricilerin özel veri saklaması için kullanılır. Ancak, kullanıcıdan gelen veriler doğrudan bu özelliklere yerleştirilirse XSS riski oluşur.

**Örnek:**

`<div data-info="javascript:alert('XSS')">Click here</div`
Bu örnekte, saldırgan `data-info` özelliğine XSS kodu yerleştirebilir ve JavaScript ile DOM üzerinden bu özelliğe erişim sağlayarak saldırıyı tetikleyebilir.

**Önleme:**

- `data-*` özelliklerinde kullanıcı girdisini encode ederek özel karakterleri kaçırın.
- JavaScript ile bu verileri işlerken sanitize işlemi yapın.

# 8. `placeholder` Özelliğinde XSS

`placeholder` özelliği genellikle input alanlarına eklenir. Doğrudan kullanıcıya gösterilse de bazı tarayıcı ve şablon motorları bu özelliği encode etmezse XSS’e yol açabilir.

**Örnek:**

`<input placeholder="<img src='x' onerror='alert(1)'>">`
Bu örnekte, `placeholder` içine zararlı HTML kodu yerleştirildiğinde bazı tarayıcılarda XSS oluşabilir.

**Önleme:**

- `placeholder` gibi özelliklerde kullanıcı girdilerini encode edin.
- Tarayıcı veya şablon motorunun otomatik olarak encode edip etmediğini kontrol edin.

# 3. JavaScript Context (Script Bağlamı)

JavaScript context’i XSS saldırılarını doğrudan tetiklemek için kullanılan bir diğer bağlamdır. Script etiketleri içinde yer alan kullanıcı girdileri veya JavaScript olaylarında XSS riski yüksekti

```
<script>
   var data = "<?php echo $_GET['data']; ?>";
   alert(data);
</scrip
```
Bu örnekte, `data` değişkenine kullanıcıdan gelen veri doğrudan yerleştirildiğinde XSS oluşabilir. Kullanıcı `" onerror="alert(1)"` gibi özel karakterler girerek, `data` değişkeni üzerinde kod çalıştırabilir.

**Önleme Önerileri:**

- Kullanıcıdan gelen verileri doğrudan `script` etiketi içinde kullanmaktan kaçının.
- `encodeURIComponent` gibi JavaScript fonksiyonlarıyla veriyi encode ederek özel karakterleri engelleyin.

# 4. HTML Comment Context (Yorum Bağlamı)

HTML yorumları da bazı durumlarda XSS’e yol açabilir. Şablon motorları veya yanlış yazılmış parser’lar bu yorumları HTML çıktısına yanlış ekleyebilir. Bu durumda XSS saldırıları ortaya çıkabilir.

`<!-- Kullanıcı girişi: <!-- <script>alert('XSS')</script> -->`
Yukarıdaki örnekte, `<!-- <script>alert('XSS')</script> -->` ifadesi yorum olarak algılanır, ancak bazı şablon motorlarında veya hatalı işleyen parser’larda yorumdan çıkarak çalıştırılabilir.

**Önleme Önerileri:**

- Kullanıcıdan gelen verileri yorum içinde kullanmaktan kaçının veya HTML encode uygulayın.
- Şablon motorlarının yorum işleme ayarlarını inceleyerek güvenlik açıklarını kapatın.

# 5. Style Context (Stil Bağlamı)

CSS context’inde de XSS saldırıları yapılabilir. Özellikle inline `style` özellikleri ve `background-image` gibi özellikler zararlı kodları tetikleyebilir.

```
<div style="background-image: url('javascript:alert(1)')">
   Malicious Style
</div>
```
Bu örnekte, `background-image` URL olarak `javascript:` protokolünü çalıştırarak XSS’i tetikleyebilir.

**Önleme Önerileri:**

- CSS içinde kullanıcı girdisi kullanılacaksa, inline değil harici CSS dosyaları tercih edilmelidir.
- Güvenli URL protokollerini kısıtlayarak `javascript:` gibi protokolleri engelleyin.

# 6. URL Context (URL Bağlamı)

URL’ler XSS için sık kullanılan context’lerden biridir. `href` veya `src` özellikleriyle, `javascript:` protokolü gibi tehlikeli girdiler kullanılarak XSS tetiklenebilir.

`<a href="javascript:alert('XSS')">Tıklayın</a>`
Bu örnekte `href` özelliği, `javascript:` protokolü kullanarak zararlı kod çalıştırıyor.

**Önleme Önerileri:**

- Yalnızca güvenli protokollere (`https`, `http`) izin verin.
- URL encode işlemiyle tehlikeli protokolleri engelleyin.

# 7. DOM Context (DOM Manipülasyonu)

JavaScript ile DOM manipülasyonu yapılırken XSS açıkları oluşabilir. `innerHTML`, `outerHTML`, `insertAdjacentHTML` gibi özellikler, kullanıcı girdilerini işlenmeden yerleştirirse risk taşır.

`document.getElementById("content").innerHTML = userInput;`
Burada, `innerHTML` özelliği kullanıcı girdiğini doğrudan HTML yapısına ekleyerek zararlı kod çalıştırabilir.

**Önleme Önerileri:**

- `textContent` veya `innerText` gibi güvenli özellikler kullanın.
- DOM’a kullanıcı girdisi eklenmeden önce DOM Purify gibi güvenlik kütüphaneleri ile sanitize işlemi yapın.

# 8. InnerHTML ve OuterHTML Kullanımı

`innerHTML` ve `outerHTML` özellikleri, HTML yapısını doğrudan manipüle eder. Bu nedenle kullanıcı girdilerinin encode edilmeden eklenmesi XSS riskine sebep olur. Örneğin:

`document.body.innerHTML = "<div>" + userInput + "</div>";`
Burada, `userInput` güvenlik kontrolünden geçmediği için XSS’e açıktır.

**Önleme Önerileri:**

- `textContent` veya `innerText` gibi güvenli özellikleri tercih edin.
- DOM Purify gibi sanitize kütüphaneleriyle kullanıcı girdilerini temizleyin.

# 9. JSON Context (JSON Veri Yapıları)

JSON, veri aktarımı için kullanılır, ancak yanlış işlenirse veya DOM’a güvensiz bir şekilde yerleştirilirse XSS oluşturabilir.

```
const userData = JSON.parse('{"user": "<script>alert(1)</script>"}');
document.getElementById("output").innerHTML = userData.user;
```
Bu örnekte JSON içeriği doğrudan HTML’e eklenmiştir ve XSS oluşabilir.

**Önleme Önerileri:**

- JSON verisi `textContent` veya `innerText` ile eklenmelidir.
- JSON girdilerini sanitize ederek zararlı içeriği temizleyin.

# 10. Template Engine Context (Şablon Motorları)

Şablon motorları (örneğin, Nunjucks, Handlebars) HTML çıktısında XSS’e yol açabilir. Bazı şablon motorları otomatik olarak encode işlemi yapmaz, bu nedenle XSS riski oluşur

`{{ user_input }}`
Burada kullanıcıdan gelen `user_input` doğrudan yerleştiriliyorsa XSS saldırısına açık olabilir.

**Önleme Önerileri:**

- Şablon motorunun sanitize özelliklerini kontrol edin.
- Kullanıcı girdilerini escape ederek zararlı içeriği önleyin.

# 11. XSS Önleme Stratejileri

XSS’e karşı her context için farklı stratejiler benimsemek önemlidir:

- **Encoding ve Escaping**: Girdiyi context’e göre encode ederek özel karakterleri kaçırın.
- **Content Security Policy (CSP)**: Yalnızca güvenilir kaynaklardan gelen kodların çalışmasına izin verin.
- **Girdi Denetimi**: Tüm kullanıcı girdileri sanitize edilerek zararlı kodlardan arındırılmalıdır.
- **Güvenlik Kütüphaneleri Kullanımı**: DOM Purify gibi kütüphaneler XSS saldırılarını önlemede etkilidir.

Bu stratejiler XSS’i önlemekte ve güvenli bir web ortamı sağlamada yardımcı olur.

Teşekkürler:
