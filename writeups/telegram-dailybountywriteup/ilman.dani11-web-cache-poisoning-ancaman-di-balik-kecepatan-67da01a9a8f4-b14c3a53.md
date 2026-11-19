# Web Cache Poisoning

- **Source URL:** https://medium.com/@ilman.dani11/web-cache-poisoning-ancaman-di-balik-kecepatan-67da01a9a8f4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126140230/https://medium.com/@ilman.dani11/web-cache-poisoning-ancaman-di-balik-kecepatan-67da01a9a8f4
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11512 (id 11512)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Web Cache Poisoning : Ancaman di Balik Kecepatan

Di masa yang serba real-time, cache layaknya “ingatan singkat” yang berguna untuk menyimpan salinan respons HTTP seperti HTML, JS, gambar dan sebagainya. Hal tersebut membuat pengalaman akses pengguna lebih cepat, lebih hemat bandwidth, lebih tahan lonjakan trafik. Namun di balik kecepatan tersebut menyimpan sebuah ancaman yang perlu diperhatikan. So mari kita bahas cache lebih detail dan juga ancamannya.

**Apa itu Cache?**Cache adalah komponen penyimpanan sementara yang menyimpan salinan respons HTTP untuk mengurangi beban pada server, latensi jaringan, serta bandwidth yang digunakan.

**Mengapa Cache Diperlukan?**

Bayangkan jika server harus mengirim respons baru untuk setiap permintaan HTTP secara terpisah. Hal ini akan:

- Membebani server secara berlebihan

- Menyebabkan masalah latency (penundaan)

- Menghasilkan pengalaman pengguna yang buruk

**Posisi dan Fungsi Cache**

Cache berada di antara server website dan pengguna. Fungsi dari cache yakni :

- Menyimpan (cache) http respons dari permintaan tertentu

- Biasanya untuk jangka waktu tertentu

- Ketika pengguna lain mengirim permintaan yang sama, cache langsung melayani dengan salinan respons yang sudah disimpan

- Tanpa perlu berinteraksi dengan server back-end lagi

**Cara Kerja** 

Saat cache menerima permintaan HTTP, langkah pertama yang dilakukannya adalah:

1. Memeriksa apakah ada respons cached yang bisa langsung dilayani

2. Meneruskan permintaan ke server back-end

Cache mengidentifikasi permintaan yang sama dengan membandingkan komponen tertentu dari permintaan, yang disebut “cache key”.

Apa yang Termasuk dalam Cache Key?

- Request line (baris permintaan)

- Host header

Komponen permintaan yang tidak termasuk dalam cache key disebut “unkeyed” (tidak memiliki kunci).

Proses pengambilan keputusan cache terjadi jika cache key dari permintaan yang masuk cocok dengan key permintaan sebelumnya. Maka cache menganggap kedua permintaan sama, oleh karena itu cache akan melayani salinan respons cached yang dibuat untuk permintaan yang sah. Hal ini berlaku untuk semua permintaan berikutnya dengan cache key yang cocok dan berlangsung sampai respons cached kedaluwarsa.

## Web Cache Poisoning

Web cache poisoning adalah teknik serangan dimana penyerang memanfaatkan perilaku web server dan cache sehingga respons HTTP berbahaya ditujukan ke pengguna lain/korban.

Web cache poisoning memiliki dua tahapan utama. Pertama, penyerang mencari cara agar server back-end tanpa sengaja mengirim respons yang berisi muatan berbahaya. Setelah hal tersebut berhasil, penyerang memastikan respons poisoning tadi disimpan di cache dan diberikan kepada korban yang mengakses. Cache yang sudah “teracuni” bisa jadi alat penyerangan yang sangat berbahaya untuk menyebarkan berbagai jenis serangan, misalnya XSS, JavaScript injection, open redirection, dan lain-lain.

**Apa dampak dari serangan web cache poisoning?**

Dampak dari serangan ini sangat bergantung pada dua hal utama:

1. Apa yang berhasil dicache oleh penyerang
Karena cache poisoning itu lebih berperan sebagai alat penyebaran daripada serangan yang berdiri sendiri, dampaknya akan sebanding dengan payload yang disisipkan. Seperti serangan lain, web cache poisoning juga bisa digabung dengan teknik lain untuk menaikkan dampak seperti XSS, JavaScript injection, open redirect dan lain lain.
2. Seberapa ramai trafik di halaman yang terdampak
Respons yang sudah “diracuni” akan diberikan kepada korban yang mengunjungi halaman itu selama cache masih teracuni. Jadi efeknya tidak terlalu besar, tergantung seberapa populer halaman tersebut. Kalau yang berhasil diracuni adalah halaman beranda situs besar, ribuan pengguna bisa terkena tanpa interaksi lanjutan dari penyerang.

### **Studi Kasus**

Dalam pembahasan kali ini akan diberikan beberapa studi kasus agar tergambar lebih jelas terkait kerentanan web cache poisoning.

**Web Cache Poisoning leads to Stored XSS**

Sumber : [https://hackerone.com/reports/1424094](https://hackerone.com/reports/1424094)

Dalam laporan tersebut, pelapor menemukan web cache poisoning yang dipadukan dengan stored XSS. pelapor menjelaskan dengan menambahkan `.js`pada path `/job/listing/011.js?jl=1007452474740` halaman tersebut akan mendapatkan respons `200 OK` dan respons tersebut akan dijadikan cache serta `gdtoken` akan terekspos kepada penyerang. payload yang digunakan penyerang untuk ekploitasi serangan ini yaitu

**Request**

```
GET /member/home/index.htm/x.jpeg?t=2021111121 HTTP/2
Host: www.glassdoor.com
X-Forwarded-For: xss 
X-Forwarded-For: xss><svg/onload=globalThis[`al`+/ert/.source]`1`// 
X-Forwarded-For: > 
Cookie: gdId=xss</script%20
```
**Respons**

```
...
guid="</script ","24.99.19.20","xss","xss><svg/onload=globalThis[`al`+/ert/.source]`1`//,">
...
```
Setelah melakukan poisoning terhadap url tersebut, penyerang hanya perlu mengirimkan URL berikut kepada korban.

`redacted.com/xxx/xx/xxx.xx/x.js?t=2021111121`
Dampak dari serangan tersebut yaitu korban mengunjungi halaman yang sudah di cache oleh penyerang, sehingga korban akan menjalankan javascript berbahaya pada browser korban.

### **Cara mencegah kerentanan web cache poisoning**

Cara paling “pasti” untuk mencegah cache poisoning adalah mematikan caching sama sekali. Hal itu sangat tidak realistis, akan tetapi untuk sebagian situs bisa saja memungkinkan. Misalnya, kalau hanya memakai cache dengan pengaturan default, ada baiknya untuk menilai ulang apakah opsi default itu benar-benar sesuai kebutuhan.

Kalau memang membutuhkan cache, lakukan pembatasan hanya untuk respons yang benar-benar statis. Selalu memastikan penyerang tidak bisa menipu server back-end.

Saat menerapkan caching, lakukan juga pencegahan berikut:

- Jika kamu ingin mengeluarkan sesuatu dari cache key demi performa, lebih baik rewrite permintaan (bukan menghapusnya dari key).
- Tolak “fat GET requests” (GET dengan body besar). Perlu diketahui, beberapa teknologi pihak ketiga mengizinkan ini secara default.
- Patch kerentanan di sisi klien meski tampaknya tidak bisa dieksploitasi. Bisa jadi kerentanan itu bisa dieksploitasi karena perilaku cache yang tidak terduga. Cepat atau lambat, seseorang bisa menemukan “keunikan” (di cache atau hal lain) yang membuat bug tersebut bisa dimanfaatkan.

Sumber :

[https://portswigger.net/research/practical-web-cache-poisoning](https://portswigger.net/research/practical-web-cache-poisoning)
