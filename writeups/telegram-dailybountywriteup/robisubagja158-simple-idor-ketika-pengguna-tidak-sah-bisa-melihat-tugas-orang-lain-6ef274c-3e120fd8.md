# Simple IDOR — Ketika Pengguna Tidak Sah Bisa Melihat Tugas Orang Lain

- **Source URL:** https://medium.com/@robisubagja158/simple-idor-ketika-pengguna-tidak-sah-bisa-melihat-tugas-orang-lain-6ef274c79934?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251127170247/https://medium.com/@robisubagja158/simple-idor-ketika-pengguna-tidak-sah-bisa-melihat-tugas-orang-lain-6ef274c79934
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11011 (id 11011)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Simple IDOR — Ketika Pengguna Tidak Sah Bisa Melihat Tugas Pengguna Lain

## 📝Pendahuluan

Saat menguji sebuah aplikasi manajemen tugas melalui **program bug bounty self-hosted**, saya menemukan celah *IDOR (Insecure Direct Object Reference)*. Normalnya, pengguna hanya boleh melihat tugas yang ditugaskan kepada mereka — namun dengan mengganti ID pada URL `/task/detail/{id}`, seorang pengguna biasa bisa melihat tugas milik pengguna lain tanpa otorisasi.

## 🔎 Latar Belakang — Apa itu IDOR?

IDOR adalah bentuk *Broken Access Control* di mana aplikasi mengekspos referensi langsung ke objek tanpa memverifikasi kepemilikan. Jika server hanya memeriksa keberadaan ID dan bukan hak akses peminta, siapa saja yang menebak ID valid bisa mengakses resource orang lain.

## 🛠️ Eksploitasi (PoC — non-destruktif)

1. Login sebagai akun pegawai biasa.
2. Buka tugas, misalnya:

`/task/detail/2`
3\. Ubah angka ID pada URL, Misalnya:

`/task/detail/3`
4\. Sistem menampilkan detail tugas milik pengguna lain → **IDOR terkonfirmasi**.

## ⚠️ Dampak

- Data internal tugas terekspos (judul, deskripsi, deadline, komentar, lampiran).
- Potensi kebocoran PII dan isu kepatuhan.
- Bisa dimanfaatkan untuk social engineering atau menemukan celah lain.
- Severity: **Medium → High**.

## ✅ Rekomendasi Singkat

- Terapkan **object-level authorization** di server (cek kepemilikan/role).
- Kembalikan **403 Forbidden** jika pengguna tidak berhak.
- Pastikan semua endpoint API menerapkan cek yang sama dan tambahkan logging untuk deteksi enumerasi ID

## 🧾 Kesimpulan

Sederhana terlihat — cukup ubah angka di URL — tapi akar masalahnya adalah kurangnya validasi hak akses di server. **Validasi otorisasi pada backend** mencegah satu digit menjadi pintu masuk ke data orang lain.
