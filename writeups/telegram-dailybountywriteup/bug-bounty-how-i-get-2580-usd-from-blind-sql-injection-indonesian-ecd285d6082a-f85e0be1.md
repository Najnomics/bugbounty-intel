# [ BUG BOUNTY ] How I Get 2580$ USD From Blind SQL Injection [Indonesian]

- **Source URL:** https://danangtriatmaja.medium.com/bug-bounty-how-i-get-2580-usd-from-blind-sql-injection-indonesian-ecd285d6082a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142409/https://danangtriatmaja.medium.com/bug-bounty-how-i-get-2580-usd-from-blind-sql-injection-indonesian-ecd285d6082a
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3153 (id 3153)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# \[ BUG BOUNTY \] How I Get 2580$ USD From Blind SQL Injection \[Indonesian\]

Hallo teman-teman ***researcher*** selamat malam, bagaimana kabarnya ? semoga senantiasa sehat selalu dan diberikan kelancaran dalam aktifitasnya.

Setelah vakum menulis selama beberapa tahun belakang ini, saya akan berbagi tulisan sederhana saya mengenai aktifitas Bug Hunting, bi’idznillah saya dapatkan dari program dorking di google. (Kamu juga bisa mendapatkannya!)

Kamu cukup ketikan perintah dibawah ini di google, silahkan pilih salah satu saja ya.

Contoh :

intext:bounty inurl:/security

inurl:”bug bounty” and intext:”€” and inurl:/security

inurl:”bug bounty” and intext:”$” and inurl:/security

inurl:”bug bounty” and intext:”INR” and inurl:/security

site:\*.edu intext:security report vulnerability

“cms” bug bounty

“If you find a security issue” “reward”

“responsible disclosure” intext:”you may be eligible for monetary compensation”

inurl: “responsible disclosure”, “bug bounty”, “bugbounty”

intext: we offer a bounty

site:\*/security.txt “bounty”


Untuk lebih detailnya kamu juga bisa mengecek di alamat URL dibawah ini, silahkan di klik (bukan phising kok).

[https://github.com/sushiwushi/bug-bounty-dorks/blob/master/dorks.txt](https://github.com/sushiwushi/bug-bounty-dorks/blob/master/dorks.txt)

Jadi begini ceritanya, selama pengujian saya menemukan bahwa aplikasi/situs web rentan terhadap serangan Blind SQL Injection — Time Based.

Kerentanan ini memungkinkan seorang penyerang memanipulasi kueri SQL Database dengan cara memasukan sebuah payload atau injeksi kode yang memungkinkan akses tidak sah ke data sensitif objektifnya adalah potensial mengambil alih database.

Berikut Request & Responsenya :

Anda perhatikan di kotak merah saya melakukan injeksi payload SQL Injection, lebih detailnya kamu bisa fuzzing (pengecekan) menggunakan sumber dibawah :

Nah, di kasus temuan ini saya berhasil mendapatkannya dengan payload injeksi kode sebagai berikut :

Payload : (select\*from(select(sleep(10)))a);

Dengan hasil execution Time : 10,7 second

Tanpa berpikir lama-lama saya manfaatkan tools SQLMap untuk mengefisiensikan waktu dan dapat membantu saya mendapatkan Database dari Aplikasi.

Syntax :

sqlmap -r request.txt — dbs — risk=3 — level=3 — tamper=between dbms=”MariaDB” — batch -p advertiser\_id


Violla!!! Saya berhasil mendapatkan Database.

Saya laporkan celah keamanan ini, tidak sampai 1x24 jam langsung ditangani dengan cepat dan diajak meeting via Skype.

Menuggu sekitar 1 minggu dan saya beri tahu bahwa laporan yang saya kirimkan dengan severity CRITICAL yang kemudian saya diberi hadiah sebesar :

Pemilik Program telah memberi izin untuk saya disclose laporan ini\*\*\*

Follow Linkedin saya untuk berkoneksi :

[https://www.linkedin.com/in/danangtriatmaja/](https://www.linkedin.com/in/danangtriatmaja/)

Salam Hangat,

Danang Tri Atmaja

#bugbounty #bugbountytips #whitehathacker
