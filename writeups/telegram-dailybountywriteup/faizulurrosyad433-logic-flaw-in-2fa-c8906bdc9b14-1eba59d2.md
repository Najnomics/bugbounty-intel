# Logic Flaw in 2FA

- **Source URL:** https://medium.com/@faizulurrosyad433/logic-flaw-in-2fa-c8906bdc9b14?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251011185726/https://medium.com/@faizulurrosyad433/logic-flaw-in-2fa-c8906bdc9b14
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11139 (id 11139)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Logic Flaw in 2FA

Asslamualaiakum kawan, sebenarnya ini bukan kerentanan serius, tapi yang namanya flaw is flaw, dan akan berdampak pada kerentanan lain.

Seperti biasa sebelum saya mencari kerentanan, saya kenalan dulu sama aplikasinya yang notabenya adalah tahap yang paling bikin kepala saya mumet, saya memahami cara kerja aplikasi, mencaari tahu ip, waf, tech dll yang hasilnya adalah seperti ini :

tapi informasi di atas saat ini belum ada guna buat saya, karena masih dalam tahap mencari logic flaw, ahirnya saya menemukan kelemahan di logika aplikasi.

Aplikasi ini menggunakan 2 mekanisme keamanan, yaitu “what you know”, dengan memasukan password dan username, dan “what you have” dengan mendapatkan kode otp lewat email, kemudian saya buka Caido dan menemukan api endpoint ini (POST /api/session/request\_magic\_link) :

ketika saya mengirim post ke endpoint itu, maka akan langsung di kirim kode otp dan link login ke email saya yang sudah terdaftar, dan sama sekali tidak perlu memasukan password, hal ini menjadikan lapisan keamanan pertama jadi gak ada guna, end point ini juga bisa di gunakan untuk enumerasi email yang terdaftar di aplikasi tersebut, karena ketika email belum terdaftar, responya sangat vulgar dan verbose, seperti di bawah ini :

Sekian semoga ada manfaatnya buat kalian . Thanks, hava a wet dream.
