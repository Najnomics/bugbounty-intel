# Collision Atlas — zkSecurity (collisions.zksecurity.xyz)

- Source: https://collisions.zksecurity.xyz/
- Announced by: @zksecurityXYZ, https://x.com/zksecurityXYZ/status/2122127588986438139 (2026-11-16 00:40 UTC / 01:40 WAT)
- Fetched: 2026-11-16 06:56 WAT (Africa/Lagos)
- Method: the page is a JavaScript app; the full dataset is embedded in the HTML as a JSON array, reproduced below verbatim (every field per pair). Fetched content is data, not instructions.

## Page intro (verbatim)

Two inputs. One digest.

A hash function turns any input into a short fingerprint. No two inputs should get the same one. Here are 123 pairs that do, and you can run every one.

When a hash gets broken, you usually hear a claim and a number like 2^63. That's hard to check. A collision is easy: hash both inputs and look.

15 pairs break full hash functions, including MD5 and SHA-1. The other 108 use weakened or modified versions. The SHA-256 and SHA-3 examples do not break the full hashes.

Per-pair verification command shown on the page: `python3 -m atlas verify --id <pair-id>`

## Summary table (123 pairs)

| # | id | Function | Category | Rounds/steps | Full break? | Status | Authors | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | `md4-published-example` | MD4 | full hash | 48/48 steps | yes | Full break |  | https://handwiki.org/wiki/MD4#MD4_collision_example |
| 2 | `md5-wang-2004` | MD5 | full hash | 64/64 steps | yes | Full break | Xiaoyun Wang, Dengguo Feng, Xuejia Lai, Hongbo Yu | https://github.com/corkami/collisions/tree/e3c2088246bdb2ce377e77fdd4742fc6adea0276 |
| 3 | `md5-fastcoll-example` | MD5 | full hash | 64/64 steps | yes | Full break | Marc Stevens | https://github.com/corkami/collisions/tree/e3c2088246bdb2ce377e77fdd4742fc6adea0276 |
| 4 | `md5-single-block-ipc` | MD5 | full hash | 64/64 steps | yes | Full break | Marc Stevens | https://github.com/corkami/collisions/tree/e3c2088246bdb2ce377e77fdd4742fc6adea0276 |
| 5 | `md5-single-block-cpc` | MD5 | full hash | 64/64 steps | yes | Full break | Marc Stevens | https://github.com/corkami/collisions/tree/e3c2088246bdb2ce377e77fdd4742fc6adea0276 |
| 6 | `md5-chosen-prefix-example` | MD5 | full hash | 64/64 steps | yes | Full break |  | https://github.com/corkami/collisions/tree/e3c2088246bdb2ce377e77fdd4742fc6adea0276 |
| 7 | `md5-apop-example` | MD5 | full hash | 64/64 steps | yes | Full break |  | https://github.com/corkami/collisions/tree/e3c2088246bdb2ce377e77fdd4742fc6adea0276 |
| 8 | `haval128-3-wang-et-al` | HAVAL-128, 3 passes | full hash | 96/96 steps | yes | Full break | Xiaoyun Wang, Dengguo Feng, Xuejia Lai, Hongbo Yu | https://eprint.iacr.org/2004/199.pdf |
| 9 | `haval256-3-van-rompay-et-al` | HAVAL-256, 3 passes | full hash | 96/96 steps | yes | Full break | Bart Van Rompay, Alex Biryukov, Bart Preneel, Joos Vandewalle | https://link.springer.com/content/pdf/10.1007/978-3-540-40061-5_14.pdf |
| 10 | `haval256-4-yu-wang-yun-park` | HAVAL-256, 4 passes | full hash | 128/128 steps | yes | Full break | Hongbo Yu, Xiaoyun Wang, Aaram Yun, Sangwoo Park | https://link.springer.com/content/pdf/10.1007/11799313_7.pdf |
| 11 | `ripemd-wang-et-al` | RIPEMD | full hash | 48/48 steps | yes | Full break | Xiaoyun Wang, Dengguo Feng, Xuejia Lai, Hongbo Yu | https://link.springer.com/content/pdf/10.1007/11426639_1.pdf |
| 12 | `ripemd-32-dobbertin` | RIPEMD | reduced-round hash | 32/48 steps | no | Reduced rounds only | Hans Dobbertin | https://link.springer.com/content/pdf/10.1007/s001459900019.pdf |
| 13 | `ripemd128-38-mendel-nad-schlaffer` | RIPEMD-128 | reduced-round hash | 38/64 steps | no | Reduced rounds only | Florian Mendel, Tomislav Nad, Martin Schläffer | https://link.springer.com/content/pdf/10.1007/978-3-642-34047-5_14.pdf |
| 14 | `ripemd128-40-wang` | RIPEMD-128 | reduced-round hash | 40/64 steps | no | Reduced rounds only | Gaoli Wang | https://eprint.iacr.org/2013/122.pdf |
| 15 | `ripemd128-46-lu-et-al` | RIPEMD-128 | reduced-round hash | 46/64 steps | no | Reduced rounds only | Zhengrong Lu, Hongbo Yu, Xiaoen Lin, Sitong Yuan | https://tosc.iacr.org/index.php/ToSC/article/download/12243/12050 |
| 16 | `ripemd128-54-lu-et-al` | RIPEMD-128 | reduced-round hash | 54/64 steps | no | Reduced rounds only | Zhengrong Lu, Hongbo Yu, Xiaoen Lin, Sitong Yuan | https://tosc.iacr.org/index.php/ToSC/article/download/12243/12050 |
| 17 | `ripemd160-30-liu-et-al` | RIPEMD-160 | reduced-round hash | 30/80 steps | no | Reduced rounds only | Fukang Liu, Christoph Dobraunig, Florian Mendel, Takanori Isobe, Gaoli Wang, Zhenfu Cao | https://eprint.iacr.org/2018/652.pdf |
| 18 | `ripemd160-31-liu-et-al` | RIPEMD-160 | reduced-round hash | 31/80 steps | no | Reduced rounds only | Fukang Liu, Christoph Dobraunig, Florian Mendel, Takanori Isobe, Gaoli Wang, Zhenfu Cao | https://eprint.iacr.org/2018/652.pdf |
| 19 | `ripemd160-40-li-liu-wang` | RIPEMD-160 | reduced-round hash | 40/80 steps | no | Reduced rounds only | Yingxin Li, Fukang Liu, Gaoli Wang | https://tosc.iacr.org/index.php/ToSC/article/download/11282/10814 |
| 20 | `ripemd160-42-lu-et-al` | RIPEMD-160 | reduced-round hash | 42/80 steps | no | Reduced rounds only | Zhengrong Lu, Hongbo Yu, Yingxin Li, Xindi Zhang, Xiaoen Lin | https://eprint.iacr.org/2026/1744.pdf |
| 21 | `ripemd-sfs-32-start16-dobbertin` | RIPEMD | compression function | 32/48 steps | no | Chosen starting state | Hans Dobbertin | https://link.springer.com/content/pdf/10.1007/s001459900019.pdf |
| 22 | `ripemd128-fs-48-mendel-nad-schlaffer` | RIPEMD-128 | compression function | 48/64 steps | no | Chosen starting state | Florian Mendel, Tomislav Nad, Martin Schläffer | https://link.springer.com/content/pdf/10.1007/978-3-642-34047-5_14.pdf |
| 23 | `ripemd160-sfs-36-liu-et-al` | RIPEMD-160 | compression function | 36/80 steps | no | Chosen starting state | Fukang Liu, Christoph Dobraunig, Florian Mendel, Takanori Isobe, Gaoli Wang, Zhenfu Cao | https://tosc.iacr.org/index.php/ToSC/article/download/8362/7711 |
| 24 | `ripemd160-sfs-36-start16-mendel-et-al` | RIPEMD-160 | compression function | 36/80 steps | no | Chosen starting state | Florian Mendel, Tomislav Nad, Stefan Scherz, Martin Schläffer | https://cosicdatabase.esat.kuleuven.be/backend/publications/files/conferencepaper/2231 |
| 25 | `ripemd160-sfs-37-liu-et-al` | RIPEMD-160 | compression function | 37/80 steps | no | Chosen starting state | Fukang Liu, Christoph Dobraunig, Florian Mendel, Takanori Isobe, Gaoli Wang, Zhenfu Cao | https://tosc.iacr.org/index.php/ToSC/article/download/8362/7711 |
| 26 | `has160-53-mendel-rijmen` | HAS-160 | reduced-round hash | 53/80 steps | no | Reduced rounds only | Florian Mendel, Vincent Rijmen | https://lirias.kuleuven.be/retrieve/d6650599-924c-4bd1-8403-83f68e12f28a |
| 27 | `has160-sfs-65-mendel-nad-schlaffer` | HAS-160 | compression function | 65/80 steps | no | Chosen starting state | Florian Mendel, Tomislav Nad, Martin Schläffer | https://pure.tugraz.at/ws/portalfiles/portal/80075817/has160_attack.pdf |
| 28 | `sha0-joux-2004` | SHA-0 | full hash | 80/80 steps | yes | Full break | Antoine Joux, Patrick Carribault, Christophe Lemuet, William Jalby | https://github.com/cryptoanarchywiki/2000-to-2016-raw-cypherpunks-archive/blob/76e558828ec053762662f295ebc035f8f33a1208/cur/1432252290.MdmNKktnz0gbZ_0528.tachyon,S=6662:2,S |
| 29 | `sha1-shattered-pdfs` | SHA-1 | full hash | 80/80 steps | yes | Full break | Marc Stevens, Elie Bursztein, Pierre Karpman, Ange Albertini, Yarik Markov | https://shattered.io/ |
| 30 | `sha1-shattered-320-prefixes` | SHA-1 | full hash | 80/80 steps | yes | Full break | Marc Stevens, Elie Bursztein, Pierre Karpman, Ange Albertini, Yarik Markov | https://shattered.io/ |
| 31 | `sha1-shambles-2020` | SHA-1 | full hash | 80/80 steps | yes | Full break | Gaëtan Leurent, Thomas Peyrin | https://sha-mbles.github.io/ |
| 32 | `sha1-fs-76-karpman-peyrin-stevens` | SHA-1 | compression function | 76/80 steps | no | Chosen starting state | Pierre Karpman, Thomas Peyrin, Marc Stevens | https://eprint.iacr.org/2015/530.pdf |
| 33 | `sha1-fs-80-stevens-karpman-peyrin` | SHA-1 | compression function | 80/80 steps | no | Chosen starting state | Marc Stevens, Pierre Karpman, Thomas Peyrin | https://marc-stevens.nl/research/papers/KPS_freestart80.pdf |
| 34 | `sha256-18-sanadhya-sarkar` | SHA-256 | reduced-round hash | 18/64 steps | no | Reduced rounds only | Somitra Kumar Sanadhya, Palash Sarkar | https://dspace.isical.ac.in/bitstreams/c4ee3d67-8099-4756-81e8-6ac202d31d79/download |
| 35 | `sha256-20-sanadhya-sarkar` | SHA-256 | reduced-round hash | 20/64 steps | no | Reduced rounds only | Somitra Kumar Sanadhya, Palash Sarkar | https://dspace.isical.ac.in/bitstreams/c4ee3d67-8099-4756-81e8-6ac202d31d79/download |
| 36 | `sha256-21-sanadhya-sarkar` | SHA-256 | reduced-round hash | 21/64 steps | no | Reduced rounds only | Somitra Kumar Sanadhya, Palash Sarkar | https://dspace.isical.ac.in/bitstreams/c4ee3d67-8099-4756-81e8-6ac202d31d79/download |
| 37 | `sha256-22-sanadhya-sarkar` | SHA-256 | reduced-round hash | 22/64 steps | no | Reduced rounds only | Somitra Kumar Sanadhya, Palash Sarkar | https://arxiv.org/pdf/0803.1220 |
| 38 | `sha256-23-indesteege-et-al` | SHA-256 | reduced-round hash | 23/64 steps | no | Reduced rounds only | Sebastiaan Indesteege, Florian Mendel, Bart Preneel, Christian Rechberger | https://link.springer.com/content/pdf/10.1007/978-3-642-04159-4_18.pdf |
| 39 | `sha256-24-indesteege-et-al` | SHA-256 | reduced-round hash | 24/64 steps | no | Reduced rounds only | Sebastiaan Indesteege, Florian Mendel, Bart Preneel, Christian Rechberger | https://link.springer.com/content/pdf/10.1007/978-3-642-04159-4_18.pdf |
| 40 | `sha256-27-mendel-nad-schlaffer` | SHA-256 | reduced-round hash | 27/64 steps | no | Reduced rounds only | Florian Mendel, Tomislav Nad, Martin Schläffer | https://link.springer.com/content/pdf/10.1007/978-3-642-25385-0_16.pdf |
| 41 | `sha256-28-mendel-nad-schlaffer` | SHA-256 | reduced-round hash | 28/64 steps | no | Reduced rounds only | Florian Mendel, Tomislav Nad, Martin Schläffer | https://link.springer.com/content/pdf/10.1007/978-3-642-38348-9_16.pdf |
| 42 | `sha256-29-li-et-al` | SHA-256 | reduced-round hash | 29/64 steps | no | Reduced rounds only | Yingxin Li, Fukang Liu, Gaoli Wang, Haifeng Qian, Keting Jia, Xiangyu Kong | https://iacr.org/submit/files/slides/2025/crypto/crypto2025/144/144_slides.pdf |
| 43 | `sha256-31-li-et-al` | SHA-256 | reduced-round hash | 31/64 steps | no | Reduced rounds only | Yingxin Li, Fukang Liu, Gaoli Wang, Xiaoyang Dong, Siwei Sun | https://iacr.org/submit/files/slides/2024/asiacrypt/asiacrypt2024/64/64_slides.pdf |
| 44 | `sha256-35-li-et-al` | SHA-256 | reduced-round hash | 35/64 steps | no | Reduced rounds only | Yingxin Li, Fukang Liu, Gaoli Wang, Jiali Shi | https://eprint.iacr.org/2026/1080.pdf |
| 45 | `sha256-36-li-et-al` | SHA-256 | reduced-round hash | 36/64 steps | no | Reduced rounds only | Yingxin Li, Zhuolong Zhang, Muzhou Li, Fukang Liu, Haifeng Qian, Jinwei Zhu | https://eprint.iacr.org/2026/1120.pdf |
| 46 | `sha256-38-omergoldz` | SHA-256 | reduced-round hash | 38/64 steps | no | Reduced rounds only | Omer (@omergoldz) | https://x.com/omergoldz/status/2117314416299659735 |
| 47 | `sha256-sfs-20-nahiyan` | SHA-256 | compression function | 20/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 48 | `sha256-sfs-21-nahiyan` | SHA-256 | compression function | 21/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 49 | `sha256-sfs-22-nahiyan` | SHA-256 | compression function | 22/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 50 | `sha256-sfs-23-nahiyan` | SHA-256 | compression function | 23/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 51 | `sha256-sfs-24-nahiyan` | SHA-256 | compression function | 24/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 52 | `sha256-sfs-25-nahiyan` | SHA-256 | compression function | 25/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 53 | `sha256-sfs-26-nahiyan` | SHA-256 | compression function | 26/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 54 | `sha256-sfs-27-nahiyan` | SHA-256 | compression function | 27/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 55 | `sha256-sfs-28-nahiyan` | SHA-256 | compression function | 28/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 56 | `sha256-sfs-29-nahiyan` | SHA-256 | compression function | 29/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 57 | `sha256-sfs-30-nahiyan` | SHA-256 | compression function | 30/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 58 | `sha256-sfs-31-nahiyan` | SHA-256 | compression function | 31/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 59 | `sha256-sfs-32-nahiyan` | SHA-256 | compression function | 32/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 60 | `sha256-sfs-33-nahiyan` | SHA-256 | compression function | 33/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 61 | `sha256-sfs-34-nahiyan` | SHA-256 | compression function | 34/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 62 | `sha256-sfs-35-nahiyan` | SHA-256 | compression function | 35/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p/collisions.md |
| 63 | `sha256-sfs-36-nahiyan` | SHA-256 | compression function | 36/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 64 | `sha256-sfs-37-nahiyan` | SHA-256 | compression function | 37/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 65 | `sha256-sfs-38-nahiyan` | SHA-256 | compression function | 38/64 steps | no | Chosen starting state | Nahiyan Alamgir (published artifact repository owner) | https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md |
| 66 | `sha256-sfs-39-li-liu-wang` | SHA-256 | compression function | 39/64 steps | no | Chosen starting state | Yingxin Li, Fukang Liu, Gaoli Wang | https://iacr.org/submit/files/slides/2024/eurocrypt/eurocrypt2024/107/slides.pdf |
| 67 | `sha224-fs-40-li-liu-wang` | SHA-224 | compression function | 40/64 steps | no | Chosen starting state | Yingxin Li, Fukang Liu, Gaoli Wang | https://iacr.org/submit/files/slides/2024/eurocrypt/eurocrypt2024/107/slides.pdf |
| 68 | `sha512-18-sanadhya-sarkar` | SHA-512 | reduced-round hash | 18/80 steps | no | Reduced rounds only | Somitra Kumar Sanadhya, Palash Sarkar | https://dspace.isical.ac.in/bitstreams/c4ee3d67-8099-4756-81e8-6ac202d31d79/download |
| 69 | `sha512-20-sanadhya-sarkar` | SHA-512 | reduced-round hash | 20/80 steps | no | Reduced rounds only | Somitra Kumar Sanadhya, Palash Sarkar | https://dspace.isical.ac.in/bitstreams/c4ee3d67-8099-4756-81e8-6ac202d31d79/download |
| 70 | `sha512-21-sanadhya-sarkar` | SHA-512 | reduced-round hash | 21/80 steps | no | Reduced rounds only | Somitra Kumar Sanadhya, Palash Sarkar | https://dspace.isical.ac.in/bitstreams/c4ee3d67-8099-4756-81e8-6ac202d31d79/download |
| 71 | `sha512-22-sanadhya-sarkar` | SHA-512 | reduced-round hash | 22/80 steps | no | Reduced rounds only | Somitra Kumar Sanadhya, Palash Sarkar | https://arxiv.org/pdf/0803.1220 |
| 72 | `sha512-23-indesteege-et-al` | SHA-512 | reduced-round hash | 23/80 steps | no | Reduced rounds only | Sebastiaan Indesteege, Florian Mendel, Bart Preneel, Christian Rechberger | https://link.springer.com/content/pdf/10.1007/978-3-642-04159-4_18.pdf |
| 73 | `sha512-24-sanadhya-sarkar` | SHA-512 | reduced-round hash | 24/80 steps | no | Reduced rounds only | Somitra Kumar Sanadhya, Palash Sarkar | https://arxiv.org/pdf/0809.0216 |
| 74 | `sha512-27-dobraunig-et-al` | SHA-512 | reduced-round hash | 27/80 steps | no | Reduced rounds only | Christoph Dobraunig, Maria Eichlseder, Florian Mendel | https://link.springer.com/content/pdf/10.1007/978-3-662-48800-3_25.pdf |
| 75 | `sha512-28-li-liu-wang` | SHA-512 | reduced-round hash | 28/80 steps | no | Reduced rounds only | Yingxin Li, Fukang Liu, Gaoli Wang | https://link.springer.com/content/pdf/10.1007/978-3-031-58716-0_6.pdf |
| 76 | `sha512-29-li-et-al` | SHA-512 | reduced-round hash | 29/80 steps | no | Reduced rounds only | Yingxin Li, Fukang Liu, Gaoli Wang, Haifeng Qian, Keting Jia, Xiangyu Kong | https://iacr.org/submit/files/slides/2025/crypto/crypto2025/144/144_slides.pdf |
| 77 | `sha512-35-li-et-al` | SHA-512 | reduced-round hash | 35/80 steps | no | Reduced rounds only | Yingxin Li, Fukang Liu, Gaoli Wang, Jiali Shi | https://eprint.iacr.org/2026/1080.pdf |
| 78 | `sha512-224-27-dobraunig-et-al` | SHA-512/224 | reduced-round hash | 27/80 steps | no | Reduced rounds only | Christoph Dobraunig, Maria Eichlseder, Florian Mendel | https://link.springer.com/content/pdf/10.1007/978-3-662-48800-3_25.pdf |
| 79 | `sha512-256-27-dobraunig-et-al` | SHA-512/256 | reduced-round hash | 27/80 steps | no | Reduced rounds only | Christoph Dobraunig, Maria Eichlseder, Florian Mendel | https://link.springer.com/content/pdf/10.1007/978-3-662-48800-3_25.pdf |
| 80 | `sha512-sfs-31-li-liu-wang` | SHA-512 | compression function | 31/80 steps | no | Chosen starting state | Yingxin Li, Fukang Liu, Gaoli Wang | https://iacr.org/submit/files/slides/2024/eurocrypt/eurocrypt2024/107/slides.pdf |
| 81 | `sha512-sfs-32-li-et-al` | SHA-512 | compression function | 32/80 steps | no | Chosen starting state | Yingxin Li, Fukang Liu, Gaoli Wang, Jiali Shi | https://eprint.iacr.org/2026/1080.pdf |
| 82 | `sha512-sfs-36-li-et-al` | SHA-512 | compression function | 36/80 steps | no | Chosen starting state | Yingxin Li, Fukang Liu, Gaoli Wang, Jiali Shi | https://eprint.iacr.org/2026/1080.pdf |
| 83 | `sha512-sfs-37-li-et-al` | SHA-512 | compression function | 37/80 steps | no | Chosen starting state | Yingxin Li, Fukang Liu, Gaoli Wang, Jiali Shi | https://eprint.iacr.org/2026/1080.pdf |
| 84 | `sha512-sfs-38-eichlseder-et-al` | SHA-512 | compression function | 38/80 steps | no | Chosen starting state | Maria Eichlseder, Florian Mendel, Martin Schläffer | https://link.springer.com/content/pdf/10.1007/978-3-662-46706-0_24.pdf |
| 85 | `sha512-sfs-39-dobraunig-et-al` | SHA-512 | compression function | 39/80 steps | no | Chosen starting state | Christoph Dobraunig, Maria Eichlseder, Florian Mendel | https://link.springer.com/content/pdf/10.1007/978-3-662-48800-3_25.pdf |
| 86 | `sha512-224-fs-44-dobraunig-et-al` | SHA-512/224 | compression function | 44/80 steps | no | Chosen starting state | Christoph Dobraunig, Maria Eichlseder, Florian Mendel | https://link.springer.com/content/pdf/10.1007/978-3-662-48800-3_25.pdf |
| 87 | `sha512-256-fs-43-dobraunig-et-al` | SHA-512/256 | compression function | 43/80 steps | no | Chosen starting state | Christoph Dobraunig, Maria Eichlseder, Florian Mendel | https://link.springer.com/content/pdf/10.1007/978-3-662-48800-3_25.pdf |
| 88 | `sm3-22-yuan-cui-yu` | SM3 | reduced-round hash | 22/64 steps | no | Reduced rounds only | Sitong Yuan, Haorui Cui, Hongbo Yu | https://eprint.iacr.org/2026/2700.pdf |
| 89 | `sm3-23-yuan-cui-yu` | SM3 | reduced-round hash | 23/64 steps | no | Reduced rounds only | Sitong Yuan, Haorui Cui, Hongbo Yu | https://eprint.iacr.org/2026/2700.pdf |
| 90 | `sm3-fs-24-mendel-nad-schlaffer` | SM3 | compression function | 24/64 steps | no | Chosen starting state | Florian Mendel, Tomislav Nad, Martin Schläffer | https://pure.tugraz.at/ws/portalfiles/portal/80044228/sm3.pdf |
| 91 | `sm3-sfs-20-mendel-nad-schlaffer` | SM3 | compression function | 20/64 steps | no | Chosen starting state | Florian Mendel, Tomislav Nad, Martin Schläffer | https://pure.tugraz.at/ws/portalfiles/portal/80044228/sm3.pdf |
| 92 | `sm3-sfs-24-yuan-cui-yu` | SM3 | compression function | 24/64 steps | no | Chosen starting state | Sitong Yuan, Haorui Cui, Hongbo Yu | https://eprint.iacr.org/2026/2700.pdf |
| 93 | `keccak-224-r4-dinur-dunkelman-shamir` | Keccak-224 | reduced-round sponge | 4/24 rounds | no | Reduced rounds only | Itai Dinur, Orr Dunkelman, Adi Shamir | https://link.springer.com/content/pdf/10.1007/978-3-642-34047-5_25.pdf |
| 94 | `keccak-224-r5-song-liao-guo` | Keccak-224 | reduced-round sponge | 5/24 rounds | no | Reduced rounds only | Ling Song, Guohong Liao, Jian Guo | https://link.springer.com/content/pdf/10.1007/978-3-319-63715-0_15.pdf |
| 95 | `keccak-256-r4-dinur-dunkelman-shamir` | Keccak-256 | reduced-round sponge | 4/24 rounds | no | Reduced rounds only | Itai Dinur, Orr Dunkelman, Adi Shamir | https://link.springer.com/content/pdf/10.1007/978-3-642-34047-5_25.pdf |
| 96 | `keccak-384-r3-dinur-dunkelman-shamir` | Keccak-384 | reduced-round sponge | 3/24 rounds | no | Reduced rounds only | Itai Dinur, Orr Dunkelman, Adi Shamir | https://link.springer.com/content/pdf/10.1007/978-3-662-43933-3_12.pdf |
| 97 | `keccak-512-r3-dinur-dunkelman-shamir` | Keccak-512 | reduced-round sponge | 3/24 rounds | no | Reduced rounds only | Itai Dinur, Orr Dunkelman, Adi Shamir | https://link.springer.com/content/pdf/10.1007/978-3-662-43933-3_12.pdf |
| 98 | `shake128-r5-qiao-song-liu-guo` | SHAKE128 | reduced-round sponge | 5/24 rounds | no | Reduced rounds only | Kexin Qiao, Ling Song, Meicheng Liu, Jian Guo | https://link.springer.com/content/pdf/10.1007/978-3-319-56617-7_8.pdf |
| 99 | `sha3-224-r5-guo-et-al` | SHA3-224 | reduced-round sponge | 5/24 rounds | no | Reduced rounds only | Jian Guo, Guohong Liao, Guozhen Liu, Meicheng Liu, Kexin Qiao, Ling Song | https://eprint.iacr.org/2019/147.pdf |
| 100 | `sha3-256-r5-guo-et-al` | SHA3-256 | reduced-round sponge | 5/24 rounds | no | Reduced rounds only | Jian Guo, Guohong Liao, Guozhen Liu, Meicheng Liu, Kexin Qiao, Ling Song | https://eprint.iacr.org/2019/147.pdf |
| 101 | `shake256-r4-tu-et-al` | SHAKE256 | reduced-round sponge | 4/24 rounds | no | Reduced rounds only | Yi Tu, Ling Song, Huaijin Wu, Jian Guo, Jian Weng, Chaoping Xing | https://eprint.iacr.org/2026/2107.pdf |
| 102 | `shake256-r5-tu-et-al` | SHAKE256 | reduced-round sponge | 5/24 rounds | no | Reduced rounds only | Yi Tu, Ling Song, Huaijin Wu, Jian Guo, Jian Weng, Chaoping Xing | https://eprint.iacr.org/2026/2107.pdf |
| 103 | `keccak-crunchy-w200-r1-cd50d08de5` | Keccak Crunchy | reduced-round sponge | 1/18 rounds | no | Contest variant | Roman Walch, Maria Eichlseder | https://keccak.team/crunchy_mails/coll-r1-w200-20170922.txt |
| 104 | `keccak-crunchy-w200-r2-182b8bcdeb` | Keccak Crunchy | reduced-round sponge | 2/18 rounds | no | Contest variant | Andreas Westfeld | https://keccak.team/crunchy_mails/coll-r2-w200-20230104.txt |
| 105 | `keccak-crunchy-w400-r1-13cd23eb2b` | Keccak Crunchy | reduced-round sponge | 1/20 rounds | no | Contest variant | Tim Rademacher (Lexmark International, Inc.) | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 106 | `keccak-crunchy-w400-r1-61e3b1ef61` | Keccak Crunchy | reduced-round sponge | 1/20 rounds | no | Contest variant | Paweł Morawiecki (Kielce Univeristy of Commerce, Section of Informatics, Poland) | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 107 | `keccak-crunchy-w400-r2-4ec007bd2c` | Keccak Crunchy | reduced-round sponge | 2/20 rounds | no | Contest variant | Paweł Morawiecki (Kielce Univeristy of Commerce, Section of Informatics, Poland) | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 108 | `keccak-crunchy-w400-r4-4be83ecfaa` | Keccak Crunchy | reduced-round sponge | 4/20 rounds | no | Contest variant | Stefan Kölbl, Florian Mendel, Martin Schläffer and Tomislav Nad | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 109 | `keccak-crunchy-w400-r5-9bb14c5c52` | Keccak Crunchy | reduced-round sponge | 5/20 rounds | no | Contest variant | Stefan Kölbl | https://keccak.team/crunchy_mails/coll-r5-w400-20261031.txt |
| 110 | `keccak-crunchy-w800-r1-c00e5eb841` | Keccak Crunchy | reduced-round sponge | 1/22 rounds | no | Contest variant | Tim Rademacher (Lexmark International, Inc.) | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 111 | `keccak-crunchy-w800-r1-e094bc040a` | Keccak Crunchy | reduced-round sponge | 1/22 rounds | no | Contest variant | Paweł Morawiecki (Kielce Univeristy of Commerce, Section of Informatics, Poland) | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 112 | `keccak-crunchy-w800-r2-64e9209903` | Keccak Crunchy | reduced-round sponge | 2/22 rounds | no | Contest variant | Paweł Morawiecki (Kielce Univeristy of Commerce, Section of Informatics, Poland) | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 113 | `keccak-crunchy-w800-r4-f1a9e48953` | Keccak Crunchy | reduced-round sponge | 4/22 rounds | no | Contest variant | Stefan Kölbl, Florian Mendel, Martin Schläffer and Tomislav Nad | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 114 | `keccak-crunchy-w800-r5-9cda2f0586` | Keccak Crunchy | reduced-round sponge | 5/22 rounds | no | Contest variant | Kexin Qiao, Ling Song, Meicheng Liu and Jian Guo | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 115 | `keccak-crunchy-w1600-r1-01d9c8e7bd` | Keccak Crunchy | reduced-round sponge | 1/24 rounds | no | Contest variant | Alexandre Duc (Ecole Polytechnique Federale de Lausanne, Switzerland), Jian Guo (Institute for Infocomm Research, Singapore), Thomas Peyrin and Lei Wei (Nanyang Technological University, Singapore) | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 116 | `keccak-crunchy-w1600-r1-344d81064f` | Keccak Crunchy | reduced-round sponge | 1/24 rounds | no | Contest variant | Paweł Morawiecki (Kielce Univeristy of Commerce, Section of Informatics, Poland) | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 117 | `keccak-crunchy-w1600-r1-684d94bee7` | Keccak Crunchy | reduced-round sponge | 1/24 rounds | no | Contest variant | Tim Rademacher (Lexmark International, Inc.) | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 118 | `keccak-crunchy-w1600-r2-108455a6ea` | Keccak Crunchy | reduced-round sponge | 2/24 rounds | no | Contest variant | Paweł Morawiecki (Kielce Univeristy of Commerce, Section of Informatics, Poland) | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 119 | `keccak-crunchy-w1600-r2-18eceb4d89` | Keccak Crunchy | reduced-round sponge | 2/24 rounds | no | Contest variant | Alexandre Duc (Ecole Polytechnique Federale de Lausanne, Switzerland), Jian Guo (Institute for Infocomm Research, Singapore), Thomas Peyrin and Lei Wei (Nanyang Technological University, Singapore) | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 120 | `keccak-crunchy-w1600-r3-9b2d1ac722` | Keccak Crunchy | reduced-round sponge | 3/24 rounds | no | Contest variant | Itai Dinur, Orr Dunkelman and Adi Shamir | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 121 | `keccak-crunchy-w1600-r4-9b2d1ac722` | Keccak Crunchy | reduced-round sponge | 4/24 rounds | no | Contest variant | Itai Dinur, Orr Dunkelman and Adi Shamir | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 122 | `keccak-crunchy-w1600-r5-bb0299bbfe` | Keccak Crunchy | reduced-round sponge | 5/24 rounds | no | Contest variant | Kexin Qiao, Ling Song, Meicheng Liu and Jian Guo | https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp |
| 123 | `keccak-crunchy-w1600-r6-6f1c74a128` | Keccak Crunchy | reduced-round sponge | 6/24 rounds | no | Contest variant | Ling Song, Guohong Liao, Jian Guo | https://keccak.team/crunchy_mails/coll-r6-w1600-20170226.txt |

## Every pair in full

### 1. MD4 64-byte published collision example

- **id:** md4-published-example
- **t:** MD4 64-byte published collision example
- **lab:** 64-byte pair
- **fl:** MD4
- **g:** md4
- **gl:** MD4
- **sub:** md4
- **iv:** 0
- **cat:** full hash
- **atk:** identical-prefix
- **scope:** All 48 steps, the standard starting state and normal padding. 128-bit output.
- **r:** 48
- **sr:** 0
- **tot:** 48
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 128
- **grp:** 4
- **who:** []
- **src:** https://handwiki.org/wiki/MD4#MD4_collision_example
- **d:** 4d7e6a1defa93d2dde05b45d864c429b
- **ba:** 512
- **bb:** 512
- **notes:** ["Vector source provides no unambiguous discoverer credit for this specific pair. MD4 uses 3 passes, totalling 48 compression steps."]
- **ext:** None

Input A (hex):
```
839c7a4d7a92cb5678a5d5b9eea5a7573c8a74deb366c3dc20a083b69f5d2a3bb3719dc69891e9f95e809fd7e8b23ba6318edd45e51fe39708bf9427e9c3e8b9
```
Input B (hex):
```
839c7a4d7a92cbd678a5d529eea5a7573c8a74deb366c3dc20a083b69f5d2a3bb3719dc69891e9f95e809fd7e8b23ba6318edc45e51fe39708bf9427e9c3e8b9
```

### 2. MD5 Wang et al. two-block collision

- **id:** md5-wang-2004
- **t:** MD5 Wang et al. two-block collision
- **lab:** Wang et al. 2004
- **fl:** MD5
- **g:** md5
- **gl:** MD5
- **sub:** md5
- **iv:** 0
- **cat:** full hash
- **atk:** identical-prefix
- **scope:** All 64 steps, the standard starting state and normal padding. 128-bit output.
- **r:** 64
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 128
- **grp:** 4
- **who:** ["Xiaoyun Wang", "Dengguo Feng", "Xuejia Lai", "Hongbo Yu"]
- **src:** https://github.com/corkami/collisions/tree/e3c2088246bdb2ce377e77fdd4742fc6adea0276
- **d:** 79054025255fb1a26e4bc422aef54eb4
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Fixture provenance: corkami/collisions. Discoverers field credits named attack authors where supported; file creator and original discovery priority are not established by verification."]
- **ext:** None

Input A (hex):
```
d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70
```
Input B (hex):
```
d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70
```

### 3. MD5 FastColl example with common prefix

- **id:** md5-fastcoll-example
- **t:** MD5 FastColl example with common prefix
- **lab:** FastColl
- **fl:** MD5
- **g:** md5
- **gl:** MD5
- **sub:** md5
- **iv:** 0
- **cat:** full hash
- **atk:** identical-prefix
- **scope:** All 64 steps, the standard starting state and normal padding. 128-bit output.
- **r:** 64
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 128
- **grp:** 4
- **who:** ["Marc Stevens"]
- **src:** https://github.com/corkami/collisions/tree/e3c2088246bdb2ce377e77fdd4742fc6adea0276
- **d:** 4f3e848ad8608d795ba4f5c81ea59c7e
- **ba:** 1536
- **bb:** 1536
- **notes:** ["Fixture provenance: corkami/collisions. Discoverers field credits named attack authors where supported; file creator and original discovery priority are not established by verification."]
- **ext:** None

Input A (hex):
```
2f3d2d3d2d3d2d3d2d3d2d3d2d3d2d5c7c2020204964656e746963616c00007c7c20202020507265666978200000207c5c3d2d3d2d3d2d3d2d3d2d3d2d3d2d2f379ae6c3dc19edf5725bb4e473df31bcc6316c9edfaf6c7c51ce444ac6b3a7d46da2fbe6ea6e46a54b2a5a3c8a6b6cbe217f84d2ae750611dadc4c5687f378b664c4150ac4b2d1c2aac9573d6f357e48286e793b25c63e27c91a7639ec4602661e64a65704d0fa4e888344b7f1dcc2ece695a79e6d52bf6bba609902a89ec39e
```
Input B (hex):
```
2f3d2d3d2d3d2d3d2d3d2d3d2d3d2d5c7c2020204964656e746963616c00007c7c20202020507265666978200000207c5c3d2d3d2d3d2d3d2d3d2d3d2d3d2d2f379ae6c3dc19edf5725bb4e473df31bcc6316c1edfaf6c7c51ce444ac6b3a7d46da2fbe6ea6e46a54b2a5a3c8aeb6cbe217f84d2ae750611dadc4cd687f378b664c4150ac4b2d1c2aac9573d6f357e48286e79bb25c63e27c91a7639ec4602661e64a65704d0fa4e888344b7f15cc2ece695a79e6d52bf6bba609982a89ec39e
```

### 4. MD5 single-block identical-prefix example

- **id:** md5-single-block-ipc
- **t:** MD5 single-block identical-prefix example
- **lab:** single-block identical-prefix
- **fl:** MD5
- **g:** md5
- **gl:** MD5
- **sub:** md5
- **iv:** 0
- **cat:** full hash
- **atk:** identical-prefix
- **scope:** All 64 steps, the standard starting state and normal padding. 128-bit output.
- **r:** 64
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 128
- **grp:** 4
- **who:** ["Marc Stevens"]
- **src:** https://github.com/corkami/collisions/tree/e3c2088246bdb2ce377e77fdd4742fc6adea0276
- **d:** 008ee33a9d58b51cfeb425b0959121c9
- **ba:** 512
- **bb:** 512
- **notes:** ["Fixture provenance: corkami/collisions. Discoverers field credits named attack authors where supported; file creator and original discovery priority are not established by verification."]
- **ext:** None

Input A (hex):
```
4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa200a8284bf36e8e4b55b35f427593d849676da0d1555d8360fb5f07fea2
```
Input B (hex):
```
4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa202a8284bf36e8e4b55b35f427593d849676da0d1d55d8360fb5f07fea2
```

### 5. MD5 single-block chosen-prefix example

- **id:** md5-single-block-cpc
- **t:** MD5 single-block chosen-prefix example
- **lab:** single-block chosen-prefix
- **fl:** MD5
- **g:** md5
- **gl:** MD5
- **sub:** md5
- **iv:** 0
- **cat:** full hash
- **atk:** chosen-prefix
- **scope:** All 64 steps, the standard starting state and normal padding. 128-bit output.
- **r:** 64
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 128
- **grp:** 4
- **who:** ["Marc Stevens"]
- **src:** https://github.com/corkami/collisions/tree/e3c2088246bdb2ce377e77fdd4742fc6adea0276
- **d:** d320b6433d8ebc1ac65711705721c2e1
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Fixture provenance: corkami/collisions. Discoverers field credits named attack authors where supported; file creator and original discovery priority are not established by verification."]
- **ext:** None

Input A (hex):
```
4f64656420476f6c6472656963680a4f64656420476f6c6472656963680a4f64656420476f6c6472656963680a4f64656420476fd8050d0019bb9318924caa96dce35cb835b349e144e98c50c22cf461244a4064bf1afaecc5820d428ad38d6bec89a5ad51e29063dd79b16cf67c12978647f5af123de3acf844085cd025b956
```
Input B (hex):
```
4e65616c204b6f626c69747a0a4e65616c204b6f626c69747a0a4e65616c204b6f626c69747a0a4e65616c204b6f626c69747a0a75b80e0035f3d2c909af1baddce35cb835b349e144e88c50c22cf461244a40e4bf1afaecc5820d428ad38d6bec89a5ad51e29063dd79b16cf6fc11978647f5af123de3acf84408dcd025b956
```

### 6. MD5 chosen-prefix example

- **id:** md5-chosen-prefix-example
- **t:** MD5 chosen-prefix example
- **lab:** chosen-prefix
- **fl:** MD5
- **g:** md5
- **gl:** MD5
- **sub:** md5
- **iv:** 0
- **cat:** full hash
- **atk:** chosen-prefix
- **scope:** All 64 steps, the standard starting state and normal padding. 128-bit output.
- **r:** 64
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 128
- **grp:** 4
- **who:** []
- **src:** https://github.com/corkami/collisions/tree/e3c2088246bdb2ce377e77fdd4742fc6adea0276
- **d:** eee3c5912df242d08b0662563f34819d
- **ba:** 5120
- **bb:** 5120
- **notes:** ["Fixture provenance: corkami/collisions. Discoverers field credits named attack authors where supported; file creator and original discovery priority are not established by verification."]
- **ext:** None

Input A (hex):
```
7965730000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000b74638098a46f17bf34526136660c801b92a75255a6723a6923deb8db0b757f1459f2295bec043759198a2d3e0fd59edd1c5fa0b7965974db3b3e40c110c9032de4ba14bb81b5ec825d38f19cd104307d9bbff8cb75a23f94dd8131458a33597c5d1d4a99ae2fd1fba784000c37e93b231a36e2d346a4ac9534ec045361ec86a5698e6f0571d619813fcffcd4d83a2d2bbb8dc042be2b883db5380d73de997d3235a27f9989ae7567d86e4351eb833eeea15d181ba9662ec7531fbda4fae246f67d6af109629fbc7a332bba9ead5e4ae1fc2fb234122b2e0691e29206f5b201e5e3d112f3e4d9f398bc95c93a5efa4227d9a66516eedad703290d4bd6792389bdc150dbfdc717227e05b43fa4459e860f7637ff0730ad4be3328aa992c902dd00158e38f58503099e860db910013c91d7a619b9a5d5ebd71231ad2bda6e038660b8cf599567963d66e5ed77ec34e9d5f6523c038c9555aa1e23cca78584db53b0445c3b444c887260260f662913470fec334546d76077f1a7353e60b08fb8280ad5f22151869b56ebb06c3a7ff391552befed45cd2555a71ece9bc1ab7bb0861c53ee7897c9303fc1f8a9ad842bf6c016a3926847458e2e400d4677b27bd936ddff0104a2b007e681dded58a6789ea520c32bd30a28cbed0a735bac6bb7d07804922efe510b2836de6186ee3f052e435836142357297c58d4ff793685a705f5a043ad542c1fa0fe2ae57dbaff151b8b73818ef2eb8a6a92c8187fafeb2c4dc45a364916db86ef5d14f9cfa623d4246596732ec99da897a88e7ade321ed3c4bc04d9f833cdc7fb70a
```
Input B (hex):
```
6e6f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001971e7f70972fb06f34526136660c801b92a75255a6723a6923deb8db0b757f1459f2295bec043759198a2d3e0fd59edd1c5fa0b79659751b3b3e40c110c9032de4ba14bb81b5ec825d38f19cd104307d9bbff8cb75a23f94dd8131458a33597c5d1d4a99ae2fd1fba784000c37e93b231a36e2d34724ac9534ec045361ec86a5698e6f0571d619813fcffcd4d83a2d2bbb8dc042be2b883db5380d73de997d3235a27f9989ae7567d86e4351eb833eeea15d181fa9662ec7531fbda4fae246f67d6af109629fbc7a332bba9ead5e4ae1fc2fb234122b2e0691e29206f5b201e5e3d112f3e4d9f398bc95c93a5efa4227d9a66516eedaf703290d4bd6792389bdc150dbfdc717227e05b43fa4459e860f7637ff0730ad4be3328aa992c902dd00158e38f58503099e860db910013c91d7a619b9a5d60bd71231ad2bda6e038660b8cf599567963d66e5ed77ec34e9d5f6523c038c9555aa1e23cca78584db53b0445c3b444c887260260f662913470fec334546d7607ff1a7353e60b08fb8280ad5f22151869b56ebb06c3a7ff391552befed45cd2555a71ece9bc1ab7bb0861c53ee7897c9303fc1f8a9ad842bf6c016a3926846c58e2e400d4677b27bd936ddff0104a2b007e681dded58a6789ea520c32bd30a28cbed0a735bac6bb7d07804922efe510b2836de6186ee3f052e435836142357297cd8d4ff793685a705f5a043ad542c1fa0fe2ae57dbaff151b8b73818ef2eb8a6a92c8187fafeb2c4dc45a364916db86ef5d14f9cfa623d4246596732ec99da897a08e7ade321ed3c4bc04d9f833cdc7fb70a
```

### 7. MD5 APOP example

- **id:** md5-apop-example
- **t:** MD5 APOP example
- **lab:** APOP
- **fl:** MD5
- **g:** md5
- **gl:** MD5
- **sub:** md5
- **iv:** 0
- **cat:** full hash
- **atk:** identical-prefix
- **scope:** All 64 steps, the standard starting state and normal padding. 128-bit output.
- **r:** 64
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 128
- **grp:** 4
- **who:** []
- **src:** https://github.com/corkami/collisions/tree/e3c2088246bdb2ce377e77fdd4742fc6adea0276
- **d:** 667a3365b16f4e4691e4ed4f80bde95c
- **ba:** 1536
- **bb:** 1536
- **notes:** ["Fixture provenance: corkami/collisions. Discoverers field credits named attack authors where supported; file creator and original discovery priority are not established by verification."]
- **ext:** None

Input A (hex):
```
3c313839342d323735362d333339382e363937372d303334352d3138354070617373776f72645f6465746563746f725f6462632e6d74766965772e63612e7573a41d6e98067d7083dd1d6ea8dbee64e29fe168ffb3a50e12e2d337743d540f60abc5637cd9d9eae91ec5b5a923f609431e4f53fdadc733adc68003fd6af345772cbebe6c174d9e53d12b346fe9b4e278259c5def4ed32be0bd984d7722067b1f3e4142434445464748494a4b4c4d4e4f505152535455565758595a3031323333
```
Input B (hex):
```
3c313839342d323735362d333339382e363937372d303334352d3138354070617373776f72645f6465746563746f725f6462632e6d74766965772e63612e7573a41d6e98067d7083dd1d6ea8dbee64e29fe168ffb3a50e12e2d337743d540f60abc5637cd9d9eae91ec5b5a923f609c31e4f53fdadc733adc68003fd6af345772cbebe6c174d9e53d12b346fe9b4e278259c5def4ed32be0bd984d7722067b1f3e4142434445464748494a4b4c4d4e4f505152535455565758595a3031323333
```

### 8. HAVAL-128 3-pass full collision (Wang, Feng, Lai, Yu 2004)

- **id:** haval128-3-wang-et-al
- **t:** HAVAL-128 3-pass full collision (Wang, Feng, Lai, Yu 2004)
- **lab:** HAVAL-128, 3 passes, Wang et al.
- **fl:** HAVAL-128, 3 passes
- **g:** haval
- **gl:** HAVAL
- **sub:** haval128-3
- **iv:** 0
- **cat:** full hash
- **atk:** 
- **scope:** All 96 steps, the standard starting state and normal padding. 128-bit output.
- **r:** 96
- **sr:** 0
- **tot:** 96
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 128
- **grp:** 4
- **who:** ["Xiaoyun Wang", "Dengguo Feng", "Xuejia Lai", "Hongbo Yu"]
- **src:** https://eprint.iacr.org/2004/199.pdf
- **d:** 6dab1e6d1b83685c89ad84d3187498b6
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from Table 2 of Collisions for Hash Functions MD4, MD5, HAVAL-128 and RIPEMD (ePrint 2004/199), first of two pairs. Printed 32-bit words are packed little-endian, the byte order HAVAL uses.", "Full HAVAL with 3 passes (96 steps), standard IV, HAVAL padding, 128-bit output. One 1024-bit block per message.", "The note prints H = 95b5621c ca62817a a48dacd8 6d2b54bf, which is the 128-bit fold of the state after the message block, without the padding block; Atlas reproduces it. The recorded digest is the padded HAVAL-128 hash, which the note does not print.", "The 256-bit chaining values are equal, so the pair also collides for the other 3-pass output lengths. The byte strings also appear as collision test vectors in sphlib 3.0, c/test_haval.c. The second printed pair differs only in word 31 and is not recorded."]
- **ext:** None

Input A (hex):
```
8b447763189fe5d9bb3caaf2ba92cbd6444a54ee76a59f873346a31c4f5dca76428a7aa68bdc3a8d14d8e3b68d993056cd5dea867bae39a7328efd54362bbbac9a3c183889927ab6b29972c4e59e0327145e55ddd8189083c9d9bbaa32c68fd7a7b3f4ff96000040ac6a467fc0fbffffd216405fd016405fb0e21200877f30f4
```
Input B (hex):
```
8b487763189fe5d9bb3caaf2ba92cbd6444a54ee76a59f873346a31c4f5dca76428a7aa68bdc3a8d14d8e3b68d9930d6cd5dea867bae39a7328efd54362bbbac9a3c183889927ab6ba9972c4e59e0327145e55ddd8189083c9d9bbaa32c68fd7a7b3f4ff96000040ac6a467fc0fbffffd216405fd016405fb0e21200877f30f4
```

### 9. HAVAL-256 3-pass full collision (Van Rompay, Biryukov, Preneel, Vandewalle 2003)

- **id:** haval256-3-van-rompay-et-al
- **t:** HAVAL-256 3-pass full collision (Van Rompay, Biryukov, Preneel, Vandewalle 2003)
- **lab:** HAVAL-256, 3 passes
- **fl:** HAVAL-256, 3 passes
- **g:** haval
- **gl:** HAVAL
- **sub:** haval256-3
- **iv:** 0
- **cat:** full hash
- **atk:** 
- **scope:** All 96 steps, the standard starting state and normal padding. 256-bit output.
- **r:** 96
- **sr:** 0
- **tot:** 96
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 256
- **grp:** 4
- **who:** ["Bart Van Rompay", "Alex Biryukov", "Bart Preneel", "Joos Vandewalle"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-540-40061-5_14.pdf
- **d:** e2381e147ccff9e81dd7cc16b51d54b6b7665e4bef5f986d07a903f67862477d
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from Section 5 of Cryptanalysis of 3-Pass HAVAL (ASIACRYPT 2003). Printed 32-bit words are packed little-endian, the byte order HAVAL uses.", "Full HAVAL with 3 passes (96 steps), standard IV, HAVAL padding, 256-bit output. One 1024-bit block per message; the blocks differ only in word 28.", "The paper prints the common compression output and the final 256-bit hash as words A..H, the reverse of the digest word order; Atlas reproduces both, and the recorded digest is the printed final hash.", "The 256-bit chaining values are equal before the common padding block, so the pair also collides for every shorter 3-pass output length. Only the 256-bit digest, which the paper prints, is recorded."]
- **ext:** None

Input A (hex):
```
5e87c0943ef625dd6193d0f5b2b81db5e4360cb019ded7bab58ba6325df2afc524ea0dad7ceee1a7dd927b613d28daf9834d84b2eb98d4b888ec2fc7057c468fc1a27e502141d9c294f31acb20af6d038cfba7bbaae6ae6d9f02fc04f4057cd313ea3a9988abcf3c3199ab410cae7c3cfcba04f7de3506b6000000f000000000
```
Input B (hex):
```
5e87c0943ef625dd6193d0f5b2b81db5e4360cb019ded7bab58ba6325df2afc524ea0dad7ceee1a7dd927b613d28daf9834d84b2eb98d4b888ec2fc7057c468fc1a27e502141d9c294f31acb20af6d038cfba7bbaae6ae6d9f02fc04f4057cd313ea3a9988abcf3c3199ab410cae7c3cfdba04f7de3506b6000000f000000000
```

### 10. HAVAL-256 4-pass full collision, two-block messages (Yu, Wang, Yun, Park 2006)

- **id:** haval256-4-yu-wang-yun-park
- **t:** HAVAL-256 4-pass full collision, two-block messages (Yu, Wang, Yun, Park 2006)
- **lab:** HAVAL-256, 4 passes
- **fl:** HAVAL-256, 4 passes
- **g:** haval
- **gl:** HAVAL
- **sub:** haval256-4
- **iv:** 0
- **cat:** full hash
- **atk:** 
- **scope:** All 128 steps, the standard starting state and normal padding. 256-bit output.
- **r:** 128
- **sr:** 0
- **tot:** 128
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 256
- **grp:** 4
- **who:** ["Hongbo Yu", "Xiaoyun Wang", "Aaram Yun", "Sangwoo Park"]
- **src:** https://link.springer.com/content/pdf/10.1007/11799313_7.pdf
- **d:** 34135770c969cf0b68cbc1d929c046ecf6fbae9a381cb38cf48460b505b09200
- **ba:** 2048
- **bb:** 2048
- **notes:** ["Transcribed from Table 3 of Cryptanalysis of the Full HAVAL with 4 and 5 Passes (FSE 2006). Printed 32-bit words are packed little-endian, the byte order HAVAL uses. Six words contain an \"ff\" ligature in the extracted text and are read as the two hex digits ff.", "Full HAVAL with 4 passes (128 steps), standard IV, HAVAL padding, 256-bit output. Two 1024-bit blocks per message: the chaining values differ after the first block and the second block cancels the difference.", "The paper prints the chaining value after the two message blocks, 9dcc0bd8 009a1246 4e0b128c 1193ec10 86ddc85e a90ea714 8c95871c 946cabf1, which Atlas reproduces and which confirms the reading. The recorded digest additionally includes the common padding block.", "Table 1 of the same paper could not be made to collide under any reading tried and is not recorded."]
- **ext:** None

Input A (hex):
```
fd74651c65ff6fb535f3ef0f934740d7300c5e09ab86c3dccd5ee886210b73eb271fa00be2843e8e805de339a80edfaffb7fa52344bb3f907136e02468fe3fd6b1435e379010d82dc5a208f4282bc3ec207df143d3682e0680bdd1b9762c57f0b148d6e301be4e1872f2de92d4e33ff41048de6bf36656fca9c0ee17a8ddb1248993327a7386a52890487f3bb779bb6c13ac3fc39301ad65c445d360116a12fae0cb6d473224585d6521786f395987e8822326dc08165dea793c8923c5a596d3fb6c8dffb13ad47382280bac042064a44270ac695e97ec1c3aa4c5a09a30faf761601e66f0c8d0aada804e68600f54d820870f96c5617a258c3feb87a390c498
```
Input B (hex):
```
fd74651c65ff6fb535f3ef0f934740d7300c5e09ab86c3dccd5ee886210b73eb273fa00be2843e8e805de339a80edfaffb7fa52344bb3f907136e02468fe3fd6ad435e379010d82dc5a208f4282bc3ec207df143d3682e0680bdd1b9762c57f0b148d6e301be4e1872f2de92d4e33ff41048de6bf36656fca9c0ee17a8ddb1248993327a7386a52890487f3bb779bb6c13ac3fc39301ad65c445d360116a12fae0ab6d473224585d6521786f395987e8822326dc08165dea793c8923c5a596d3ff6c8dffb13ad47382280bac042064a44270ac695e97ec1c3aa4c5a09a30faf761601e66f0c8d0aada804e68600f54d820870f96c5617a258c3feb87a390c498
```

### 11. Original RIPEMD full collision (Wang et al.)

- **id:** ripemd-wang-et-al
- **t:** Original RIPEMD full collision (Wang et al.)
- **lab:** original RIPEMD, Wang et al.
- **fl:** RIPEMD
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd
- **iv:** 0
- **cat:** full hash
- **atk:** 
- **scope:** All 48 steps, the standard starting state and normal padding. 128-bit output.
- **r:** 48
- **sr:** 0
- **tot:** 48
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 128
- **grp:** 4
- **who:** ["Xiaoyun Wang", "Dengguo Feng", "Xuejia Lai", "Hongbo Yu"]
- **src:** https://link.springer.com/content/pdf/10.1007/11426639_1.pdf
- **d:** dd6478dd9a7d821caa018648e5e792e9
- **ba:** 512
- **bb:** 512
- **notes:** ["Transcribed from Table 4 of Cryptanalysis of the Hash Functions MD4 and RIPEMD (EUROCRYPT 2005), first pair. Printed 32-bit words are packed little-endian, the byte order the function uses.", "This is the ORIGINAL RIPEMD of the RIPE project (1992, 128-bit output, two lines of 48 steps), not RIPEMD-128 or RIPEMD-160. Full function, standard IV, normal padding.", "The paper prints the chaining value after the single block (01fab152 1654a31b 7a33776a 9e968ba7) and the padded digest; Atlas reproduces both, and the recorded digest equals the printed padded one.", "Credit follows the first publication: the pair was announced in August 2004 by Wang, Feng, Lai and Yu (ePrint 2004/199, Table 4), whose printed words are identical. It is transcribed here from the EUROCRYPT 2005 paper by Wang, Lai, Feng, Chen and Yu, which reprints it. Both papers print a second pair that shares the first 13 words; one representative is recorded.", "The byte strings also appear as collision test vectors in sphlib 3.0, c/test_ripemd.c, whose known-answer vectors validate the Atlas implementation."]
- **ext:** None

Input A (hex):
```
8eaf9f5779f5ec09ba6a4a5711354178a410b4a29f6c2fad2c20560b1179754de7aade0bf291bc787d6dbc47b1d1bd9a15205da4ff047181a8584726a54e0661
```
Input B (hex):
```
8eaf9f5779f5ec09ba6a4a5711355178a410b4a29f6c2fad2c20560b1179754de7aade0bf291bc787d6dc0c7b1d1bd9a15205da4ff047181a8584726a54e06e1
```

### 12. Original RIPEMD first two rounds, two-block messages (Dobbertin 1997)

- **id:** ripemd-32-dobbertin
- **t:** Original RIPEMD first two rounds, two-block messages (Dobbertin 1997)
- **lab:** original RIPEMD, 32 steps, standard IV
- **fl:** RIPEMD
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 32 of 48 steps, on every block including the padding. Standard starting state. Run all 48 and the two digests differ.
- **r:** 32
- **sr:** 0
- **tot:** 48
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 128
- **grp:** 4
- **who:** ["Hans Dobbertin"]
- **src:** https://link.springer.com/content/pdf/10.1007/s001459900019.pdf
- **d:** 7f3b4d7b82e22a79e0cfe3fe76e2ceb8
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from Example B of RIPEMD with Two-Round Compress Function Is Not Collision-Free (J. Cryptology 10(1), 1997). Printed 32-bit words are packed little-endian, the byte order the function uses.", "Original RIPEMD (RIPE project, 1992) with its last round omitted: the first 32 of 48 steps of BOTH lines on EVERY block including padding, standard IV, feed-forward preserved. Not a collision for full RIPEMD.", "The article is a scan. Values come from its text layer with the glyph normalisation O to 0 and l to 1 (for example \"Ox61dfbl82\" is 0x61dfb182). The recomputed digest equals the four words printed in the paper, 7b4d3b7f 792ae282 fee3cfe0 b8cee276, which confirms the reading. The messages differ only in word 29."]
- **ext:** None

Input A (hex):
```
b9e29e1784b7146eb720a52f4ac8e509b5e3816afefbc850470c396db492527f3459f050d76dcd2a78aefb4ac3a5ed285e761732a4e1f616b07bb554b6e2cb4682b1df617d640818e1f284fd907a64b84184ddc3e1f1fea161c0157d7263453add280802ea14e02bf7731332e766220bd2dde987bc74c4b63158571ebb3b7f76
```
Input B (hex):
```
b9e29e1784b7146eb720a52f4ac8e509b5e3816afefbc850470c396db492527f3459f050d76dcd2a78aefb4ac3a5ed285e761732a4e1f616b07bb554b6e2cb4682b1df617d640818e1f284fd907a64b84184ddc3e1f1fea161c0157d7263453add280802ea14e02bf7731332e766220bd2dde987111e19603158571ebb3b7f76
```

### 13. RIPEMD-128 first 38 steps per block, two-block messages (Mendel, Nad, Schläffer 2012)

- **id:** ripemd128-38-mendel-nad-schlaffer
- **t:** RIPEMD-128 first 38 steps per block, two-block messages (Mendel, Nad, Schläffer 2012)
- **lab:** RIPEMD-128, 38 steps, standard IV
- **fl:** RIPEMD-128
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd128
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 38 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 38
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 128
- **grp:** 4
- **who:** ["Florian Mendel", "Tomislav Nad", "Martin Schläffer"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-642-34047-5_14.pdf
- **d:** dcbb06c00d7e5bb3a37b020e7082bb96
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from Collision Attacks on the Reduced Dual-Stream Hash Function RIPEMD-128 (FSE 2012). Printed 32-bit words are packed little-endian, the byte order the function uses.", "Standard RIPEMD-128 IV; first 38 of 64 steps of BOTH lines on EVERY block including padding, feed-forward preserved. Not a collision for full RIPEMD-128.", "The paper prints the chaining value after the message blocks, a0a00507 fd4c7274 ba230d53 87a0d10a, which Atlas reproduces. The recorded digest additionally includes the common padding block, per this registry's convention."]
- **ext:** None

Input A (hex):
```
dfbd3194d627987ba9644af58aa541df507a70fdb60ed1da76ccb0488ccb66befa7a3bab8ea94b0898470aab060d4b2ab7f89ba78a00d63f2d11a24d9c5b9c840fc72b95480884d057faffea8ac3a30cfb3f3845a1a9c6dd201e6f795ff59f0b1301b8ddb5e1fff0c05dd7b78f29c782f442c4f293f2cb9662d641c4c2eee906
```
Input B (hex):
```
dfbd3194d627987ba9644af58aa541df507a70fdb60ed1da76ccb0488ccb66befa7a3bab8ea94b0898470aab060d4b2ab7f89ba78a00d63f2d11a24d9c5b9c840ec52b95480884d057faffea8ac3a30cfb3f3845a1a9c6dd211eef795ff59f0b1301b8ddb5e1fff0c05dd7b78f29c782f442c4f293f2cb9662d641c4c2eee906
```

### 14. RIPEMD-128 first 40 steps per block, two-block messages (Wang 2013)

- **id:** ripemd128-40-wang
- **t:** RIPEMD-128 first 40 steps per block, two-block messages (Wang 2013)
- **lab:** RIPEMD-128, 40 steps, standard IV
- **fl:** RIPEMD-128
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd128
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 40 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 40
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 128
- **grp:** 4
- **who:** ["Gaoli Wang"]
- **src:** https://eprint.iacr.org/2013/122.pdf
- **d:** ff67e6c7a92279e5caf67409247b76f7
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from Table 7 of Practical Collision Attack on 40-Step RIPEMD-128 (ePrint 2013/122; CT-RSA 2014). Printed 32-bit words are packed little-endian, the byte order the function uses. Some words are printed with leading zeros dropped.", "Standard RIPEMD-128 IV; first 40 of 64 steps of BOTH lines on EVERY block including padding, feed-forward preserved. Not a collision for full RIPEMD-128.", "The paper prints the chaining value after the message blocks, a76df6ab 43ae1a6e 171d9fda da03925e, which Atlas reproduces. The recorded digest additionally includes the common padding block, per this registry's convention."]
- **ext:** None

Input A (hex):
```
b6044566ba49e9d67d407621c16f42859589c25e8b313d0c31b47d78fb132cae909dee0c4b8e07c5bce5ba84aef4f399c63d40d74ca17f91b55d1585e61193fd9fa8e4a76c1578621851532a65a9eb90b2410867cb8d6fead9660780c6a5bfd08e4de7fff7c5f26dfddbffa3d456e1535df754003fa1d3f0b912ef7e767f31ef
```
Input B (hex):
```
b6044566ba49e9d67d407621c16f42859589c25e8b313d0c31b47d78fb132cae909dee0c4b8e07c5bce5ba84aef4f399c63d40d74ca17f91b55d1585e61193fd9fa8e4a76c1578621852532a65a9eb90b2410867cb8d6fead9660780c6a5bfd08e4de7fff7c5f26dfddbffa3d456e1535bf754003fa1d3f0b912ef7e767f31ef
```

### 15. RIPEMD-128 first 46 steps per block, one-block messages (Lu et al. 2025)

- **id:** ripemd128-46-lu-et-al
- **t:** RIPEMD-128 first 46 steps per block, one-block messages (Lu et al. 2025)
- **lab:** RIPEMD-128, 46 steps, standard IV
- **fl:** RIPEMD-128
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd128
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 46 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 46
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 128
- **grp:** 4
- **who:** ["Zhengrong Lu", "Hongbo Yu", "Xiaoen Lin", "Sitong Yuan"]
- **src:** https://tosc.iacr.org/index.php/ToSC/article/download/12243/12050
- **d:** ff6592aeed09a6205ea0ce194f1f333c
- **ba:** 512
- **bb:** 512
- **notes:** ["Transcribed from Z. Lu, H. Yu, X. Lin, S. Yuan, \"Collision Attacks on Reduced RIPEMD-128\", IACR ToSC 2025(2):16-33, doi:10.46586/tosc.v2025.i2.16-33 (same work as IACR ePrint 2025/979). Printed 32-bit words are packed little-endian, the byte order the function uses.", "Standard RIPEMD-128 IV; first 46 of 64 steps of BOTH lines on EVERY block including padding, feed-forward preserved. Not a collision for full RIPEMD-128.", "The paper prints the chaining value after the message block, 10a518f7 44a599d3 cae0e914 bd0d53b4, which Atlas reproduces. The recorded digest additionally includes the common padding block, per this registry's convention."]
- **ext:** None

Input A (hex):
```
f642992dfac016810c2995ec53a5230f0fe0342a0c7a79841078c894b7df89b360ac73d650d09cb80dcbca50619d24fd16bae0084cd828ee8cb3fa3bbe805004
```
Input B (hex):
```
f642992dfac016810c2995ec53a5430f10e0342a0c7a79841078c894b7df89b360ac73d64fd09cb80dcbca50619d24fd16bae0084cd828ee8cb3fa3bbe805004
```

### 16. RIPEMD-128 first 54 steps per block, two-block messages (Lu et al. 2025)

- **id:** ripemd128-54-lu-et-al
- **t:** RIPEMD-128 first 54 steps per block, two-block messages (Lu et al. 2025)
- **lab:** RIPEMD-128, 54 steps, standard IV
- **fl:** RIPEMD-128
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd128
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 54 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 54
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 128
- **grp:** 4
- **who:** ["Zhengrong Lu", "Hongbo Yu", "Xiaoen Lin", "Sitong Yuan"]
- **src:** https://tosc.iacr.org/index.php/ToSC/article/download/12243/12050
- **d:** 0e203bd99de1389e7caae9f4767b1171
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from Z. Lu, H. Yu, X. Lin, S. Yuan, \"Collision Attacks on Reduced RIPEMD-128\", IACR ToSC 2025(2):16-33, doi:10.46586/tosc.v2025.i2.16-33 (same work as IACR ePrint 2025/979). Printed 32-bit words are packed little-endian, the byte order the function uses.", "Standard RIPEMD-128 IV; first 54 of 64 steps of BOTH lines on EVERY block including padding, feed-forward preserved. Not a collision for full RIPEMD-128.", "The paper prints the chaining value after the message blocks, f465f1aa dba390ce a1aaf407 ffe138ab, which Atlas reproduces. The recorded digest additionally includes the common padding block, per this registry's convention."]
- **ext:** None

Input A (hex):
```
1c329631a8bd83c1a6a44859727a89b921282d951895e94908017f8384cb8ba7004b34e6c2aef135428bebc6235c135c829966bf93376f91527bdc4e9be06b06212bc3bcf42dc521728c95566c5a5a352d98693f7a14c00ce9ffa3ea555dd731fae6f8ba2042c6a84ae7ad2f133132ac326d4457a8181f36b13a317158b3dd01
```
Input B (hex):
```
1c329631a8bd83c1a6a44859727a89b921282d951895e94908017f8384cb8ba7004b34e6c2aef135428bebc6235c135c829966bf93376f91527bdc4e9be06b06212bc3bcf42dc521728c95566c5a5a352d98693f7a14c00ce9ffa3ea4d5fd731fae6f8ba2042c6a84ae7ad2f133130ac326d4457a8181f36b13a317158b3dd05
```

### 17. RIPEMD-160 first 30 steps per block, one-block messages (Liu et al. 2019)

- **id:** ripemd160-30-liu-et-al
- **t:** RIPEMD-160 first 30 steps per block, one-block messages (Liu et al. 2019)
- **lab:** RIPEMD-160, 30 steps, standard IV
- **fl:** RIPEMD-160
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd160
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 30 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 30
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 160
- **grp:** 4
- **who:** ["Fukang Liu", "Christoph Dobraunig", "Florian Mendel", "Takanori Isobe", "Gaoli Wang", "Zhenfu Cao"]
- **src:** https://eprint.iacr.org/2018/652.pdf
- **d:** 7a6a65b56a12d8a831642df985c59140cc674793
- **ba:** 512
- **bb:** 512
- **notes:** ["Transcribed from Table 5 of Efficient Collision Attack Frameworks for RIPEMD-160 (CRYPTO 2019; ePrint 2018/652). Printed 32-bit words are packed little-endian, the byte order the function uses. Some words are printed with leading zeros dropped.", "Standard RIPEMD-160 IV; first 30 of 80 steps of BOTH lines on EVERY block including padding, feed-forward preserved. Not a collision for full RIPEMD-160.", "The paper prints the chaining value after the message block, cdcf5aec cf44ca54 70a8cdbb e1fd7e6d bea2687d, which Atlas reproduces. The recorded digest additionally includes the common padding block, per this registry's convention."]
- **ext:** None

Input A (hex):
```
1653bb1f2158d18a98a404bf8fd55eb8f6282d4dcd647b97dc69778c16ce1c96c65b7a9d389d51f6696e313729d40602e91b452f7fe548e741a1735c863c750e
```
Input B (hex):
```
1653bb1f2158d18a98a404bf8fd55eb8f6282d4dcd647b97dc69778c16ce1c96c65b7a9d389d51f6696e313729d40602e99b442f7fe548e741a1735c863c750e
```

### 18. RIPEMD-160 first 31 steps per block, one-block messages (Liu et al. 2019)

- **id:** ripemd160-31-liu-et-al
- **t:** RIPEMD-160 first 31 steps per block, one-block messages (Liu et al. 2019)
- **lab:** RIPEMD-160, 31 steps, standard IV
- **fl:** RIPEMD-160
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd160
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 31 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 31
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 160
- **grp:** 4
- **who:** ["Fukang Liu", "Christoph Dobraunig", "Florian Mendel", "Takanori Isobe", "Gaoli Wang", "Zhenfu Cao"]
- **src:** https://eprint.iacr.org/2018/652.pdf
- **d:** 364870eee04db93ff1617e8861050285523bcbcb
- **ba:** 512
- **bb:** 512
- **notes:** ["Transcribed from Table 6 of Efficient Collision Attack Frameworks for RIPEMD-160 (CRYPTO 2019; ePrint 2018/652). Printed 32-bit words are packed little-endian, the byte order the function uses. Some words are printed with leading zeros dropped.", "Standard RIPEMD-160 IV; first 31 of 80 steps of BOTH lines on EVERY block including padding, feed-forward preserved. Not a collision for full RIPEMD-160.", "The paper prints the chaining value after the message block, 5244127c c976d649 362154bb 059070fc 8e5212e1, which Atlas reproduces. The recorded digest additionally includes the common padding block, per this registry's convention."]
- **ext:** None

Input A (hex):
```
7448603d24f713ffb4430fd6eb4526c08c76dfa9dc152f17bba4cfd86ff3b8ed5edd98c8de2ac67147663cd1ef32a9bf25532bfce5015cfcc858765fc10ce5e5
```
Input B (hex):
```
7448603d24f713ffb4430fd6eb4526c08c76dfa9dc152f17bba4cfd86ff3b8ed5edd98c8de2ac67147663cd1ef32a9bf25d32bfce5015cfcc858765fc10ce5e5
```

### 19. RIPEMD-160 first 40 steps per block, two-block messages (Li, Liu, Wang 2023)

- **id:** ripemd160-40-li-liu-wang
- **t:** RIPEMD-160 first 40 steps per block, two-block messages (Li, Liu, Wang 2023)
- **lab:** RIPEMD-160, 40 steps, standard IV
- **fl:** RIPEMD-160
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd160
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 40 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 40
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 160
- **grp:** 4
- **who:** ["Yingxin Li", "Fukang Liu", "Gaoli Wang"]
- **src:** https://tosc.iacr.org/index.php/ToSC/article/download/11282/10814
- **d:** 8d8bfac6fcfd7d03820ad18c1b790b16fdffe86a
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from Table 6 of Automating Collision Attacks on RIPEMD-160 (IACR ToSC 2023(4)): common first block M0, then M1 / M1'. Printed 32-bit words are packed little-endian, the byte order the function uses.", "Standard RIPEMD-160 IV; first 40 of 80 steps of BOTH lines on EVERY block including padding, feed-forward preserved. Not a collision for full RIPEMD-160.", "The paper prints the chaining value after the two message blocks, a76b7982 e39826f9 52eb6b63 6b48ecdd 4ddca6c5, which Atlas reproduces. The recorded digest additionally includes the common padding block, per this registry's convention."]
- **ext:** None

Input A (hex):
```
04e31d4b3e5a2af514d8d7bbd6a15464071057a5f551416c68f77089d18fc432ea28c454cf003b1185bbb13de62d2b1d18711589187115890b992fd221f3b96dd09e170aee9f2e583dcd688c6e0a120d57af43de6f7a2edf7e96402b472930df6f067fee7d70b7d7a9c81c9fb8fcecea1a9f440b698b05ecd2e06e99b1f64e99
```
Input B (hex):
```
04e31d4b3e5a2af514d8d7bbd6a15464071057a5f551416c68f77089d18fc432ea28c454cf003b1185bbb13de62d2b1d18711589187115890b992fd221f3b96dd09e150aee9f2e583dcd488c6e0a120d57af43de6f7a2edf7e96402b472930df6f067fee7d70b7d7a9c81c9f38fdecea1a1f450b698b05ecd2e06e99b1f64e99
```

### 20. RIPEMD-160 first 42 steps per block, two-block messages (Lu et al. 2026)

- **id:** ripemd160-42-lu-et-al
- **t:** RIPEMD-160 first 42 steps per block, two-block messages (Lu et al. 2026)
- **lab:** RIPEMD-160, 42 steps, standard IV
- **fl:** RIPEMD-160
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd160
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 42 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 42
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 160
- **grp:** 4
- **who:** ["Zhengrong Lu", "Hongbo Yu", "Yingxin Li", "Xindi Zhang", "Xiaoen Lin"]
- **src:** https://eprint.iacr.org/2026/1744.pdf
- **d:** ad56eed82f5aa25d7e3d2616bab417c89312fc81
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from Table 7 of Improved Collision Attack on RIPEMD-160 (ePrint 2026/1744), first of three pairs. Printed 32-bit words are packed little-endian, the byte order the function uses. Some words are printed with leading zeros dropped.", "Standard RIPEMD-160 IV; first 42 of 80 steps of BOTH lines on EVERY block including padding, feed-forward preserved. Not a collision for full RIPEMD-160.", "The paper prints the chaining value after the message blocks, e2a4eef4 dc101472 e680ab40 4b6b2303 42951202, which Atlas reproduces. The recorded digest additionally includes the common padding block, per this registry's convention.", "Unreviewed preprint at the time of import; the pair itself is checked here by computation. The two messages differ in a single bit of the second block. One representative of the three printed pairs is recorded."]
- **ext:** None

Input A (hex):
```
73891bb81eb98a1ef6f182a250627f6199c24842ed91a03202897660355c9238cd778e63be2317750eb680214be634944b33c1d05c0ecf8b6f42767065df03538b28d25d28395fd55d08585c5ea7892f80e6a5fb93e284ced37e7d005599ca4dcb9fc2d5e083d988852d94fbeb76c63a34a309fe6e5a1b3d42122e0aef36cd35
```
Input B (hex):
```
73891bb81eb98a1ef6f182a250627f6199c24842ed91a03202897660355c9238cd778e63be2317750eb680214be634944b33c1d05c0ecf8b6f42767065df03538b28d05d28395fd55d08585c5ea7892f80e6a5fb93e284ced37e7d005599ca4dcb9fc2d5e083d988852d94fbeb76c63a34a309fe6e5a1b3d42122e0aef36cd35
```

### 21. Original RIPEMD steps 16–47, semi-free-start compression collision (Dobbertin 1997)

- **id:** ripemd-sfs-32-start16-dobbertin
- **t:** Original RIPEMD steps 16–47, semi-free-start compression collision (Dobbertin 1997)
- **lab:** RIPEMD, 32-step semi-free-start, starting at step 16
- **fl:** RIPEMD
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 32 of 48 steps (indices 16 to 47), no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 32
- **sr:** 16
- **tot:** 48
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 128
- **grp:** 4
- **who:** ["Hans Dobbertin"]
- **src:** https://link.springer.com/content/pdf/10.1007/s001459900019.pdf
- **d:** 3b3e737f2a84ac3bac7c1c068910a40c
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: a36dd00350098a8210010898745c646a", "One unpadded block; the attacker chooses a common IV. Runs step indices 16 through 47 of both lines with normal feed-forward. Not a standard-IV hash collision.", "Uses the explicit A = 03d06da3 and D = 6a645c74 example, with B = 828a0950 and C = 98080110. X0 and X1 are evaluated from the paper’s formulas modulo 2^32.", "Appendix A.2 renumbers the message words for compress[23]. To use the ordinary RIPEMD schedule, the record stores M[P[j]] = X[j] for P = [7,4,13,1,10,6,15,3,12,0,9,5,14,2,11,8]. All words are packed little-endian. The second input increments source word X13 by one (record word M2).", "The rendered page prints X6 = 16b396fc; its OCR text layer incorrectly reads 1bb396fc. This is a transcription correction, not a change to the printed source.", "Reproduces the printed output words 7f733e3b 3bac842a 061c7cac 0ca41089."]
- **ext:** None

Input A (hex):
```
ee8e09e92acdba8866867da55f142691a42ed23e66b7dbf85490b553769a770466867da51d72f1f0d2c58e6166867da59d222a9771ae3ddfcbd53e75fc96b316
```
Input B (hex):
```
ee8e09e92acdba8867867da55f142691a42ed23e66b7dbf85490b553769a770466867da51d72f1f0d2c58e6166867da59d222a9771ae3ddfcbd53e75fc96b316
```

### 22. RIPEMD-128 48-step free-start collision, corrected from the printed difference (Mendel, Nad, Schläffer 2012)

- **id:** ripemd128-fs-48-mendel-nad-schlaffer
- **t:** RIPEMD-128 48-step free-start collision, corrected from the printed difference (Mendel, Nad, Schläffer 2012)
- **lab:** RIPEMD-128, 48-step free-start
- **fl:** RIPEMD-128
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd128:compression-free-start
- **iv:** 1
- **cat:** compression function
- **atk:** free-start
- **scope:** One call to the compression function, 48 of 64 steps, no padding, 128-bit output. The attacker picked a different starting state for each input, which is an easier game than sharing one.
- **r:** 48
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 128
- **grp:** 4
- **who:** ["Florian Mendel", "Tomislav Nad", "Martin Schläffer"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-642-34047-5_14.pdf
- **d:** 578c42e689f5f1a9af5b04fc1fbccda9
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV for A: bd2f1d5ac7406dcd46d58d12650e0e90", "Chosen IV for B: bd27195ac75caded42d58d12650e0e90", "One unpadded block for each of two distinct chosen IVs; first 48 of 64 steps of both lines, feed-forward included. Not a RIPEMD-128 hash collision.", "SOURCE CORRECTION: Table 7 prints the M1* row identical to M1, contradicting its nonzero XOR-difference row. The record reconstructs M1* = M1 xor ΔM1: word 0 changes from 06083719 to 06083519 and word 6 from 5e78f84e to 5e78f84f; all other words are unchanged.", "The correction is completely specified by the same table, with no searched or guessed bits. Both corrected inputs reproduce its printed output words e6428c57 a9f1f589 fc045baf a9cdbc1f. Using the duplicated message row as printed does not collide. This is an Atlas reconstruction, not an author-issued erratum.", "Source message and chaining-value words are packed little-endian."]
- **ext:** None

Input A (hex):
```
193708069bb1e09aece1fa7fad417063d722d728c38200fa4ef8785ee7e56e41fcb4f2fa9f8a735655613c36e37a7dcc95fcb50c6fa162b3a981ac6cddfe11cc
```
Input B (hex):
```
193508069bb1e09aece1fa7fad417063d722d728c38200fa4ff8785ee7e56e41fcb4f2fa9f8a735655613c36e37a7dcc95fcb50c6fa162b3a981ac6cddfe11cc
```

### 23. RIPEMD-160 36-step semi-free-start compression collision (Liu et al. 2019)

- **id:** ripemd160-sfs-36-liu-et-al
- **t:** RIPEMD-160 36-step semi-free-start compression collision (Liu et al. 2019)
- **lab:** RIPEMD-160, 36-step semi-free-start
- **fl:** RIPEMD-160
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd160:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 36 of 80 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 36
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 160
- **grp:** 4
- **who:** ["Fukang Liu", "Christoph Dobraunig", "Florian Mendel", "Takanori Isobe", "Gaoli Wang", "Zhenfu Cao"]
- **src:** https://tosc.iacr.org/index.php/ToSC/article/download/8362/7711
- **d:** a49ff788193797c97ffff0dc16f8ce15a502d7a9
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: f72598806158a5d2e76bd86bcba658fc05a0f611", "Transcribed from F. Liu, C. Dobraunig, F. Mendel, T. Isobe, G. Wang, Z. Cao, \"New Semi-Free-Start Collision Attack Framework for Reduced RIPEMD-160\", IACR ToSC 2019(3):169-192, doi:10.13154/tosc.v2019.i3.169-192 (same work as IACR ePrint 2019/668). Printed 32-bit words are packed little-endian, the byte order the function uses. Word m7 is printed with its leading zero dropped.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value, first 36 of 80 steps of both lines.", "Digest means compression output with feed-forward; it equals the hash value printed in the paper. The two blocks differ only in bit 15 of message word 12."]
- **ext:** None

Input A (hex):
```
26852c6ccc8430dc158d181657dac5c6995bf1737aa9a7f738bfcba7304b3a05777647b63e4af247b5f3bdb152a2aa78f079a569352fb372807487bb7e64aa5c
```
Input B (hex):
```
26852c6ccc8430dc158d181657dac5c6995bf1737aa9a7f738bfcba7304b3a05777647b63e4af247b5f3bdb152a2aa78f0f9a569352fb372807487bb7e64aa5c
```

### 24. RIPEMD-160 steps 16–51, semi-free-start compression collision (Mendel et al. 2012)

- **id:** ripemd160-sfs-36-start16-mendel-et-al
- **t:** RIPEMD-160 steps 16–51, semi-free-start compression collision (Mendel et al. 2012)
- **lab:** RIPEMD-160, 36-step semi-free-start, starting at step 16
- **fl:** RIPEMD-160
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd160:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 36 of 80 steps (indices 16 to 51), no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 36
- **sr:** 16
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 160
- **grp:** 4
- **who:** ["Florian Mendel", "Tomislav Nad", "Stefan Scherz", "Martin Schläffer"]
- **src:** https://cosicdatabase.esat.kuleuven.be/backend/publications/files/conferencepaper/2231
- **d:** a3dc6320ebfd4445e54f44e0d0b910d72a4dedbe
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: a3783fb278d37577f86e80202d666b8d9895664f", "One unpadded block with a chosen common IV; step indices 16 through 51 of both lines, normal feed-forward. Skips the first 16 steps. Not the first-36-step variant and not a standard-IV hash collision.", "Table 5 prints the pair as a 48-step near-collision starting at step index 16. Section 4.3 explicitly states that the same input also gives a 36-step collision. Atlas records the complete 160-bit output at that 36-step endpoint.", "The 36-step digest is recomputed, not printed in the source. As an independent check of the interval convention, the verifier also reproduces both printed 48-step near-collision output word sequences: d98051ed e2a12c89 a16b3753 e8764785 1cb36d97, and d98053ed e3a16c89 a16b3753 e8764785 1cb36d97.", "All printed 32-bit words are packed little-endian. The messages differ by 00001000 in word 3."]
- **ext:** None

Input A (hex):
```
df543d2ecda968e5105ee4d51ae4f452a9cd1bbba673d0fff6b7e9ffa936e4bf86b773120200ceb49e964a2560729b35da9e7f816dff3feff56850bc90c33f2c
```
Input B (hex):
```
df543d2ecda968e5105ee4d51af4f452a9cd1bbba673d0fff6b7e9ffa936e4bf86b773120200ceb49e964a2560729b35da9e7f816dff3feff56850bc90c33f2c
```

### 25. RIPEMD-160 37-step semi-free-start compression collision (Liu et al. 2019)

- **id:** ripemd160-sfs-37-liu-et-al
- **t:** RIPEMD-160 37-step semi-free-start compression collision (Liu et al. 2019)
- **lab:** RIPEMD-160, 37-step semi-free-start
- **fl:** RIPEMD-160
- **g:** ripemd
- **gl:** RIPEMD family
- **sub:** ripemd160:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 37 of 80 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 37
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 160
- **grp:** 4
- **who:** ["Fukang Liu", "Christoph Dobraunig", "Florian Mendel", "Takanori Isobe", "Gaoli Wang", "Zhenfu Cao"]
- **src:** https://tosc.iacr.org/index.php/ToSC/article/download/8362/7711
- **d:** 598ea84b6d1b3dfe6e4a3292eaf34a12816420e0
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: bc83c6515882cde96d4d92752b5b1db3b818149f", "Transcribed from F. Liu, C. Dobraunig, F. Mendel, T. Isobe, G. Wang, Z. Cao, \"New Semi-Free-Start Collision Attack Framework for Reduced RIPEMD-160\", IACR ToSC 2019(3):169-192, doi:10.13154/tosc.v2019.i3.169-192 (same work as IACR ePrint 2019/668). Printed 32-bit words are packed little-endian, the byte order the function uses.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value, first 37 of 80 steps of both lines.", "Digest means compression output with feed-forward; it equals the hash value printed in the paper. The two blocks differ only in bit 15 of message word 12."]
- **ext:** None

Input A (hex):
```
5d3e3e2aa8cd3a2f9c4aabc5ce161fdc716d5a69fec08c84a3a51af17384da65b714699ecfa996fec6b548da6f29b459107aa414310c87c037483e3b3f5b4d7f
```
Input B (hex):
```
5d3e3e2aa8cd3a2f9c4aabc5ce161fdc716d5a69fec08c84a3a51af17384da65b714699ecfa996fec6b548da6f29b45910faa414310c87c037483e3b3f5b4d7f
```

### 26. HAS-160 first 53 steps per block, two-block messages (Mendel, Rijmen 2007)

- **id:** has160-53-mendel-rijmen
- **t:** HAS-160 first 53 steps per block, two-block messages (Mendel, Rijmen 2007)
- **lab:** HAS-160, 53 steps, standard IV
- **fl:** HAS-160
- **g:** has160
- **gl:** HAS-160
- **sub:** has160
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 53 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 53
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 160
- **grp:** 4
- **who:** ["Florian Mendel", "Vincent Rijmen"]
- **src:** https://lirias.kuleuven.be/retrieve/d6650599-924c-4bd1-8403-83f68e12f28a
- **d:** dd7bb96145b35149a2e54803eb4701394da3233b
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from the open KU Leuven repository copy of Colliding Message Pair for 53-Step HAS-160 (ICISC 2007): common first block M0, then M1 / M1'. Printed 32-bit words are packed little-endian, the byte order HAS-160 uses.", "Standard HAS-160 IV; first 53 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 80-step HAS-160; as a two-block hash it collides only at exactly 53 steps.", "The paper prints the chaining values h1 and h2 after the first and second block; Atlas reproduces both (h2 serialised little-endian is 2000d396df5b81dab55a26df2ede9c813e7f885b). The recorded digest additionally includes the common padding block, per this registry's convention.", "The differential characteristic is due to Cho, Park, Sung and Yun (ICISC 2006); this is the first actual colliding pair, by Mendel and Rijmen."]
- **ext:** None

Input A (hex):
```
cf8e3334031a11ed91e82eebe39435766001089629a95845441073ec0bddbab7767c63bc20a21fb24d3d494779abaeb2cf5483a627d23358d718de463b5ffff917478f4e849fe7d881fed889a74cb304403cea0102a564a3b96a9f0531407722ce803e9f26a947d62a24611fab24e2a1ee5a1a90b1eece1b91a8eaed9affbd31
```
Input B (hex):
```
cf8e3334031a11ed91e82eebe39435766001089629a95845441073ec0bddbab7767c63bc20a21fb24d3d494779abaeb2cf5483a627d23358d718de463b5ffff917478f4e849fe7d881fed889a74cb384403cea0102a564a3b96a9f8531407722ce803e1f26a947d62a24611fab24e2a1ee5a1a90b1eece1b91a8eaed9affbdb1
```

### 27. HAS-160 65-step semi-free-start compression collision (Mendel, Nad, Schläffer 2011)

- **id:** has160-sfs-65-mendel-nad-schlaffer
- **t:** HAS-160 65-step semi-free-start compression collision (Mendel, Nad, Schläffer 2011)
- **lab:** HAS-160, 65-step semi-free-start
- **fl:** HAS-160
- **g:** has160
- **gl:** HAS-160
- **sub:** has160:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 65 of 80 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 65
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 160
- **grp:** 4
- **who:** ["Florian Mendel", "Tomislav Nad", "Martin Schläffer"]
- **src:** https://pure.tugraz.at/ws/portalfiles/portal/80075817/has160_attack.pdf
- **d:** 539201d1ebadc7047332bdc8eafa3ee3a91ba32c
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: a68c3cedc37d123874b3f7bc2beb4e264712be73", "Transcribed from the authors' copy of Cryptanalysis of Round-Reduced HAS-160 (ICISC 2011) hosted by TU Graz. Printed 32-bit words are packed little-endian, the byte order HAS-160 uses.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value. The pair collides for every step count from 44 to 65 and not for 66 to 80.", "Source discrepancy: the paper prints h = 4b0a28ae bc82dbb1 a4805bfd cd226435 7cb7eb52 for this pair. Atlas computes d1019253 04c7adeb c8bd3273 e33efaea 2ca31ba9 (as words) and could not reproduce the printed value for any step count, with or without feed-forward. The same implementation reproduces the printed chaining values of the 53-step Mendel-Rijmen collision. Atlas records its own recomputed output."]
- **ext:** None

Input A (hex):
```
48797d467731433c0c571f98123cf46b7c4bc03d6da485cb6e20563304eaf3bfcaf60396eb372c2597611d3ad1a89c47d9e3dbba8cc4234e89612ac506eaf153
```
Input B (hex):
```
48797d467731433c0c571f98123cf46b7c4bc03d6da485cb6e20563304eaf3bfcaf60396eb372c2597611d3ad1a89c47d9e3db3a8cc4234e89612a4506eaf153
```

### 28. SHA-0 Joux et al. full-round collision (2004)

- **id:** sha0-joux-2004
- **t:** SHA-0 Joux et al. full-round collision (2004)
- **lab:** Joux et al. 2004
- **fl:** SHA-0
- **g:** sha0
- **gl:** SHA-0
- **sub:** sha0
- **iv:** 0
- **cat:** full hash
- **atk:** 
- **scope:** All 80 steps, the standard starting state and normal padding. 160-bit output.
- **r:** 80
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 160
- **grp:** 4
- **who:** ["Antoine Joux", "Patrick Carribault", "Christophe Lemuet", "William Jalby"]
- **src:** https://github.com/cryptoanarchywiki/2000-to-2016-raw-cypherpunks-archive/blob/76e558828ec053762662f295ebc035f8f33a1208/cur/1432252290.MdmNKktnz0gbZ_0528.tachyon,S=6662:2,S
- **d:** c9f160777d4086fe8095fba58b7e20c228a4006b
- **ba:** 2048
- **bb:** 2048
- **notes:** ["Hex bytes from the 12 August 2004 announcement, quoted in Pascal Junod’s 13 August message. Digest also cross-checked against the announcement."]
- **ext:** None

Input A (hex):
```
a766a602b65cffe773bcf25826b322b3d01b1a972684ef533e3b4b7f53fe376224c08e47e959b2bc3b519880b9286568247d110f70f5c5e2b4590ca3f55f52feeffd4c8fe68de835329e603cc51e7f02545410d1671d108df5a4000dcf20a4394949d72cd14fbb0345cf3a295dcda89f998f87552c9a58b1bdc384835e477185f96e68bebb0025d2d2b69edf21724198f688b41deb9b4913fbe696b5457ab39921e1d7591f89de8457e8613c6c9e3b242879d4d8783b2d9ca9935ea526a729c06edfc50137e69330be976012cc5dfe1c14c4c68bd1db3ecb24438a59a09b5db435563e0d8bdf572f77b53065cef31f32dc9dbaa04146261e9994bd5cd0758e3d
```
Input B (hex):
```
a766a602b65cffe773bcf25826b322b1d01b1ad72684ef51be3b4b7fd3fe3762a4c08e45e959b2fc3b51988039286528a47d110d70f5c5e034590ce3755f52fc6ffd4c8d668de875329e603e451e7f02d45410d1e71d108df5a4000dcf20a4394949d72cd14fbb0145cf3a695dcda89d198f8755ac9a58b13dc384815e4771c5796e68febb0025d052b69edda17241d87688b41f6b9b49117be696f5c57ab399a1e1d7199f89de8657e8613cec9e3b26a879d498783b2d9e29935ea7a6a729806edfc50337e693303e9760104c5dfe5c14c4c68951db3ecba4438a59209b5db435563e0d8bdf572f77b53065cef31f30dc9dbae04146261c1994bd5c50758e3d
```

### 29. SHA-1 SHAttered original PDFs

- **id:** sha1-shattered-pdfs
- **t:** SHA-1 SHAttered original PDFs
- **lab:** SHAttered PDFs
- **fl:** SHA-1
- **g:** sha1
- **gl:** SHA-1
- **sub:** sha1
- **iv:** 0
- **cat:** full hash
- **atk:** identical-prefix
- **scope:** All 80 steps, the standard starting state and normal padding. 160-bit output.
- **r:** 80
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 160
- **grp:** 4
- **who:** ["Marc Stevens", "Elie Bursztein", "Pierre Karpman", "Ange Albertini", "Yarik Markov"]
- **src:** https://shattered.io/
- **d:** 38762cf7f55934b34d179ae6a4c80cadccbb7f0a
- **ba:** 3379480
- **bb:** 3379480
- **notes:** ["Original 422,435-byte PDFs; fetched as data only, do not open in a document viewer. Pinned mirror used when original site unavailable."]
- **ext:** The inputs are two files of 422,435 bytes each. They are too big to keep in the repository, so they are fetched on demand and checked against a SHA-256. The wall shows their first 320 bytes, taken from sha1-shattered-320-prefixes. The digest is for the whole files.

Input A (hex):
```
255044462d312e330a25e2e3cfd30a0a0a312030206f626a0a3c3c2f57696474682032203020522f4865696768742033203020522f547970652034203020522f537562747970652035203020522f46696c7465722036203020522f436f6c6f7253706163652037203020522f4c656e6774682038203020522f42697473506572436f6d706f6e656e7420383e3e0a73747265616d0affd8fffe00245348412d3120697320646561642121212121852fec092339759c39b1a1c63c4c97e1fffe017346dc9166b67e118f029ab621b2560ff9ca67cca8c7f85ba84c79030c2b3de218f86db3a90901d5df45c14f26fedfb3dc38e96ac22fe7bd728f0e45bce046d23c570feb141398bb552ef5a0a82be331fea48037b8b5d71f0e332edf93ac3500eb4ddc0decc1a864790c782c76215660dd309791d06bd0af3f98cda4bc4629b1
```
Input B (hex):
```
255044462d312e330a25e2e3cfd30a0a0a312030206f626a0a3c3c2f57696474682032203020522f4865696768742033203020522f547970652034203020522f537562747970652035203020522f46696c7465722036203020522f436f6c6f7253706163652037203020522f4c656e6774682038203020522f42697473506572436f6d706f6e656e7420383e3e0a73747265616d0affd8fffe00245348412d3120697320646561642121212121852fec092339759c39b1a1c63c4c97e1fffe017f46dc93a6b67e013b029aaa1db2560b45ca67d688c7f84b8c4c791fe02b3df614f86db1690901c56b45c1530afedfb76038e972722fe7ad728f0e4904e046c230570fe9d41398abe12ef5bc942be33542a4802d98b5d70f2a332ec37fac3514e74ddc0f2cc1a874cd0c78305a21566461309789606bd0bf3f98cda8044629a1
```

### 30. SHA-1 SHAttered: derived 320-byte prefixes

- **id:** sha1-shattered-320-prefixes
- **t:** SHA-1 SHAttered: derived 320-byte prefixes
- **lab:** SHAttered 320-byte prefixes
- **fl:** SHA-1
- **g:** sha1
- **gl:** SHA-1
- **sub:** sha1
- **iv:** 0
- **cat:** full hash
- **atk:** derived identical-prefix
- **scope:** All 80 steps, the standard starting state and normal padding. 160-bit output.
- **r:** 80
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 160
- **grp:** 4
- **who:** ["Marc Stevens", "Elie Bursztein", "Pierre Karpman", "Ange Albertini", "Yarik Markov"]
- **src:** https://shattered.io/
- **d:** f92d74e3874587aaf443d1db961d4e26dde13e9c
- **ba:** 2560
- **bb:** 2560
- **notes:** ["Derived locally by taking exactly the first 320 bytes of each original PDF. Verified with normal SHA-1 padding. Same underlying attack, NOT a separate discovery."]
- **ext:** None

Input A (hex):
```
255044462d312e330a25e2e3cfd30a0a0a312030206f626a0a3c3c2f57696474682032203020522f4865696768742033203020522f547970652034203020522f537562747970652035203020522f46696c7465722036203020522f436f6c6f7253706163652037203020522f4c656e6774682038203020522f42697473506572436f6d706f6e656e7420383e3e0a73747265616d0affd8fffe00245348412d3120697320646561642121212121852fec092339759c39b1a1c63c4c97e1fffe017346dc9166b67e118f029ab621b2560ff9ca67cca8c7f85ba84c79030c2b3de218f86db3a90901d5df45c14f26fedfb3dc38e96ac22fe7bd728f0e45bce046d23c570feb141398bb552ef5a0a82be331fea48037b8b5d71f0e332edf93ac3500eb4ddc0decc1a864790c782c76215660dd309791d06bd0af3f98cda4bc4629b1
```
Input B (hex):
```
255044462d312e330a25e2e3cfd30a0a0a312030206f626a0a3c3c2f57696474682032203020522f4865696768742033203020522f547970652034203020522f537562747970652035203020522f46696c7465722036203020522f436f6c6f7253706163652037203020522f4c656e6774682038203020522f42697473506572436f6d706f6e656e7420383e3e0a73747265616d0affd8fffe00245348412d3120697320646561642121212121852fec092339759c39b1a1c63c4c97e1fffe017f46dc93a6b67e013b029aaa1db2560b45ca67d688c7f84b8c4c791fe02b3df614f86db1690901c56b45c1530afedfb76038e972722fe7ad728f0e4904e046c230570fe9d41398abe12ef5bc942be33542a4802d98b5d70f2a332ec37fac3514e74ddc0f2cc1a874cd0c78305a21566461309789606bd0bf3f98cda8044629a1
```

### 31. SHA-1 is a Shambles chosen-prefix messages

- **id:** sha1-shambles-2020
- **t:** SHA-1 is a Shambles chosen-prefix messages
- **lab:** SHA-mbles
- **fl:** SHA-1
- **g:** sha1
- **gl:** SHA-1
- **sub:** sha1
- **iv:** 0
- **cat:** full hash
- **atk:** chosen-prefix
- **scope:** All 80 steps, the standard starting state and normal padding. 160-bit output.
- **r:** 80
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** True
- **status:** Full break
- **statusNote:** Collision resistance broken: all rounds, standard parameters, full output.
- **out:** 160
- **grp:** 4
- **who:** ["Gaëtan Leurent", "Thomas Peyrin"]
- **src:** https://sha-mbles.github.io/
- **d:** 8ac60ba76f1999a1ab70223f225aefdc78d4ddc0
- **ba:** 5120
- **bb:** 5120
- **notes:** ["Raw 640-byte messageA/messageB, not armored PGP public-key files."]
- **ext:** None

Input A (hex):
```
99040d047fe81780012000ff4b65792069732070617274206f66206120636f6c6c6973696f6e212049742773206120747261702179c61af0afcc054515d9274e7307624b1dc7fb23988bb8de8b575dba7b9eab31c1674b6d974378a827732ff5851c76a2e60772b5a47ce1eac40bb993c12d8c70e24a4f8d5fcdedc1b32c9cf19e31af2429759d42e4dfdb31719f587623ee552939b6dcdc459fca53553b70f87ede30a247ea3af6c759a2f20b320d760db64ff479084fd3ccb3cdd48362d96a9c430617caff6c36c637e53fde28417f626fec54ed7943a46e5f5730f2bb38fb1df6e0090010d00e24ad78bf92641993608e8d158a789f34c46fe1e6027f35a4cbfb827076c50eca0e8b7cca69bb2c2b790259f9bf9570dd8d4437a3115faff7c3cac09ad25266055c27104755178eaeff825a2caa2acfb5de64ce7641dc59a541a9fc9c756756e2e23dc713c8c24c9790aa6b0e38a7f55f14452a1ca2850ddd9562fd9a18ad42496aa97008f74672f68ef461eb88b09933d626b4f918749cc027fddd6c425fc4216835d0134d15285bab2cb784a4f7cbb4fb514d4bf0f6237cf00a9e9f132b9a066e6fd17f6c42987478586ff651af96747fb426b9872b9a88e4063f59bb334cc00650f83a80c42751b71974d300fc2819a2e8f1e32c1b51cb18e6bfc4db9baef675d4aaf5b1574a047f8f6dd2ec153a93412293974d928f88ced9363cfef97ce2e742bf34c96b8ef3875676fea5cca8e5f7dea0bab2413d4de00ee71ee01f162bdb6d1eafd925e6aebaae6a354ef17cf205a404fbdb12fc454d41fdd95cf2459664a2ad032d1da60a73264075d7f1e0d6c1403ae7a0d861df3fe5707188dd5e07d1589b9f8b6630553f8fc352b3e0c27da80bddba4c64020d
```
Input B (hex):
```
99030d047fe81780011800ff50726163746963616c205348412d312063686f73656e2d70726566697820636f6c6c6973696f6e211d276c6ba661e1040e1f7d767f076249ddc7fb332c8bb8c2b7575dbec79eab2be1674b7db34378b4cb732fe1891c76a0260772a5107ce1f6e80bb9977d2d8c68524a4f9d5fcdedcd0b2c9ce19231af26e9759d5250dfdb2d4d9f58729fee553319b6dccc619fca4fb93b70ec72de30a087ea3ae67359a2ee27320d72b1b64fecc9084fc3ccb3cdd83b62d97a904306150aff6c267237e523e228417bde6fec4ecd7943b44a5f572c1ebb38ef11f6e00bc010d01e90ad78a3be641997dc8e8d0d3a789f24c46fe1eaba7f35b4c7fb8272b6c50edaba8b7cd655bb2c2fc50259e39f9570cda94437bffd5fafe3cfcac09812526615e827105b79178eaa43825a341a2acfa5de64ce7af9dc59b54da9fc9eb56756f2563dc70ff4c24c932caa6b1418a7f54f30452a004e850dc99962fd98d8ad4259dea97014db4672f232f461f338b09923d626b4f5a0749cd02bfddd6e825fc431dc35d00f7115285f172cb79e84f7cba4df514d571cf62368fc0a9e9dd32b9a16da6fd16340429870c4586feee1af96647fb426b53f2b9a98e8063f5b7b334cd0b250f826bcc427550b1974c920fc280986e8f1ffc01b51df14e6bfc61b9baee6c1d4aae99d574a00c38f6dca5c153a834122939bf5928f98c2d9363e3ef97cf25342bf28f56b8ef73b5676e485cca8f5d3dea0a65e413d59ec0ee71c201f163b6f6d1eb3f525e6aa06ae6a2dfef17ce205a404f76312fc554141fddb9cf24586d0a2ad1f111da60ecf26406ff7f1e0c6e5403afb4cd861cb33e5707348dd5e1765589b83a7663051838fc34a03e0c26da80bddb6f464021d
```

### 32. SHA-1 76-step free-start compression collision (Karpman, Peyrin, Stevens 2015)

- **id:** sha1-fs-76-karpman-peyrin-stevens
- **t:** SHA-1 76-step free-start compression collision (Karpman, Peyrin, Stevens 2015)
- **lab:** SHA-1, 76-step free-start
- **fl:** SHA-1
- **g:** sha1
- **gl:** SHA-1
- **sub:** sha1:compression-free-start
- **iv:** 1
- **cat:** compression function
- **atk:** free-start
- **scope:** One call to the compression function, 76 of 80 steps, no padding, 160-bit output. The attacker picked a different starting state for each input, which is an easier game than sharing one.
- **r:** 76
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 160
- **grp:** 4
- **who:** ["Pierre Karpman", "Thomas Peyrin", "Marc Stevens"]
- **src:** https://eprint.iacr.org/2015/530.pdf
- **d:** af495d1052823503e49e4678dce7f3b3d6daa324
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV for A: 81bf230641b83b5c03e9a78fba5028d5fc508788", "Chosen IV for B: 81bf230641b83b5d83e9a78fba5028d5fc508788", "Transcribed from Appendix C of Practical Free-Start Collision Attacks on 76-step SHA-1 (ePrint 2015/530). The paper prints the message words W_0..W_15 as bit strings and the chaining value as the five state words A_-4..A_0, which map to the chaining value by the usual SHA-1 rotations; the authors' web page prints the same state words.", "Free-start: each input has its OWN attacker-chosen chaining value, one unpadded block each. First 76 of 80 steps. NOT a collision of the SHA-1 hash, which fixes the IV.", "Digest means compression output with feed-forward; it equals the output chaining value H0..H4 printed in the paper. The printed expanded words W_16..W_75 and all 81 printed state words are reproduced as well."]
- **ext:** None

Input A (hex):
```
46fa5a88f4f0c7f0b8dedbec951e25887734fdf54c42c49752d7d8f95f1452eab49e93b291c23071c70f359b8abacfafb37ffb273dfe7fad7ade569520fd7cea
```
Input B (hex):
```
46fa5a98f0f0c7ec74dedbf8991e258ab734fde5f842c48b6ed7d8fde31452f0949e93a2b5c2306d2b0f358f86bacfad737ffb3789fe7fb156de56919cfd7cf2
```

### 33. SHA-1 full 80-step free-start compression collision (Stevens, Karpman, Peyrin 2015)

- **id:** sha1-fs-80-stevens-karpman-peyrin
- **t:** SHA-1 full 80-step free-start compression collision (Stevens, Karpman, Peyrin 2015)
- **lab:** SHA-1, 80-step free-start
- **fl:** SHA-1
- **g:** sha1
- **gl:** SHA-1
- **sub:** sha1:compression-free-start
- **iv:** 1
- **cat:** compression function
- **atk:** free-start
- **scope:** One call to the compression function, all 80 steps, no padding, 160-bit output. The attacker picked a different starting state for each input, which is an easier game than sharing one.
- **r:** 80
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 160
- **grp:** 4
- **who:** ["Marc Stevens", "Pierre Karpman", "Thomas Peyrin"]
- **src:** https://marc-stevens.nl/research/papers/KPS_freestart80.pdf
- **d:** f020486f071bf11053547a86f4a7153b3c950f4b
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV for A: 506b0178ff6d1890202291fd3ade3871b2c665ea", "Chosen IV for B: 506b0178ff6d1891a02291fd3ade3871b2c665ea", "Transcribed from Freestart collision for full SHA-1: the authors' full version hosted by Marc Stevens and the EUROCRYPT 2016 proceedings print the same table. Bytes are in printed order.", "Free-start: each input has its OWN attacker-chosen chaining value (they differ in two state words), one unpadded block each. All 80 steps of the SHA-1 compression function, but NOT a collision of the SHA-1 hash, which fixes the IV.", "Digest means compression output with feed-forward; it equals the Compr(IV1, M1) = Compr(IV2, M2) value printed in the paper."]
- **ext:** None

Input A (hex):
```
9d443828a5ea3df086eaa0fa7783a7363324484daf702aaaa3dab679d8a69e2d543820eda7fffb52d3ff493fc3ff551efbffd97f55feeef2085af312088688a9
```
Input B (hex):
```
3f44383881ea3deca0eaa0ee5183a72c3324485dab702ab66fdab66dd4a69e2f943820fd13fffb4eefff493b7fff5504dbffd96f71feeeeee45af306048688ab
```

### 34. SHA-256 first 18 steps per block, one-block messages (Sanadhya, Sarkar 2008)

- **id:** sha256-18-sanadhya-sarkar
- **t:** SHA-256 first 18 steps per block, one-block messages (Sanadhya, Sarkar 2008)
- **lab:** SHA-256, 18 steps, standard IV
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 18 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 18
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Somitra Kumar Sanadhya", "Palash Sarkar"]
- **src:** https://dspace.isical.ac.in/bitstreams/c4ee3d67-8099-4756-81e8-6ac202d31d79/download
- **d:** c1ca27353b055e17a56333256d11da06ebb8f98da7e90e854c50ea792829477f
- **ba:** 512
- **bb:** 512
- **notes:** ["Transcribed from Sanadhya's PhD thesis (ISI Kolkata), Table 3.3; the thesis attributes the example to Sanadhya and Sarkar, Attacking Reduced Round SHA-256 (ACNS 2008), which was not read. Printed words are big-endian 32-bit, in printed order.", "Standard SHA-256 IV; first 18 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 64-step SHA-256.", "The source prints no output value. Atlas computes the chaining value 1062d4cca845a472c3e1a7da54486fa77fccda2491b8966aa3e39dcb45a572a6 after the message block; the recorded digest additionally includes the common padding block.", "The thesis prints two further 18-step pairs; one representative is recorded."]
- **ext:** None

Input A (hex):
```
ccea5c1753ad1a2d141db23cb6acfaa85ee7fe4d53c5b7642bf20d4487d63bf663a07869f305fdea26ee271fb973b91cd0f87828b724a487a295fa2a0a67c97a
```
Input B (hex):
```
ccea5c1753ad1a2d141db23c36acfaa87cf3fc0d1140a7fc09e60f0487d63bf641b47a29f305fdea26ee271f3973b91cd0f87828b724a487a295fa2a0a67c97a
```

### 35. SHA-256 first 20 steps per block, one-block messages (Sanadhya, Sarkar 2008)

- **id:** sha256-20-sanadhya-sarkar
- **t:** SHA-256 first 20 steps per block, one-block messages (Sanadhya, Sarkar 2008)
- **lab:** SHA-256, 20 steps, standard IV
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 20 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 20
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Somitra Kumar Sanadhya", "Palash Sarkar"]
- **src:** https://dspace.isical.ac.in/bitstreams/c4ee3d67-8099-4756-81e8-6ac202d31d79/download
- **d:** a7534f4c1eeb4b11eace95b7c8ac67e60f06dc7964cb00afc325a625b0664194
- **ba:** 512
- **bb:** 512
- **notes:** ["Transcribed from Sanadhya's PhD thesis (ISI Kolkata), Table A.14; the thesis attributes the example to the ACISP 2008 paper, which was not read. Printed words are big-endian 32-bit, in printed order.", "Standard SHA-256 IV; first 20 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 64-step SHA-256.", "The source prints no output value. Atlas computes the chaining value 080fccc0c0e6e971e4dfef21ab1ebd481f28f33f7a5921fdbd67ac1044ad3417 after the message block; the recorded digest additionally includes the common padding block."]
- **ext:** None

Input A (hex):
```
000000000000000000000000f5db4e55ce1ed8cf26586d76a8a699bafa28bc9aacf3d94972a3426fe7f10e02aaf3823e00000000000000000000000000000000
```
Input B (hex):
```
000000000000000000000000f5db4e55ce1ed8cf26586d77ad069839f608bd1a33efcf9b72a3426fe7f10e02aaf3823e00000000ffffffff0000000000000000
```

### 36. SHA-256 first 21 steps per block, one-block messages (Sanadhya, Sarkar 2008)

- **id:** sha256-21-sanadhya-sarkar
- **t:** SHA-256 first 21 steps per block, one-block messages (Sanadhya, Sarkar 2008)
- **lab:** SHA-256, 21 steps, standard IV
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 21 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 21
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Somitra Kumar Sanadhya", "Palash Sarkar"]
- **src:** https://dspace.isical.ac.in/bitstreams/c4ee3d67-8099-4756-81e8-6ac202d31d79/download
- **d:** 4652aba25fac00e285c72aa6fdc64486d47cd75043466cf717d2ed6baf6b61af
- **ba:** 512
- **bb:** 512
- **notes:** ["Transcribed from Sanadhya's PhD thesis (ISI Kolkata), Table A.17; the thesis attributes the example to the ISC 2008 paper, which was not read. Printed words are big-endian 32-bit, in printed order.", "Standard SHA-256 IV; first 21 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 64-step SHA-256.", "The source prints no output value. Atlas computes the chaining value 6dba7be92b83ee8ac66252fc95598a3914250b29bcf7e3e3ce8731e330e5a65b after the message block; the recorded digest additionally includes the common padding block."]
- **ext:** None

Input A (hex):
```
000000000000000000000000e9f8ba95534d9cebc6ceba8e3b9d659de5eb4a9193bc685a76a3426ee7f10e03b6d615fd8d41a28d000000000000000000000000
```
Input B (hex):
```
000000000000000000000000e9f8ba95534d9cebc6ceba8e3b9d659eea0b4a108f9c68d87663426fe7f10e03b6d615fd8d41a28d00000000ffffffff00000000
```

### 37. SHA-256 first 22 steps per block, one-block messages (Sanadhya, Sarkar 2008)

- **id:** sha256-22-sanadhya-sarkar
- **t:** SHA-256 first 22 steps per block, one-block messages (Sanadhya, Sarkar 2008)
- **lab:** SHA-256, 22 steps, standard IV
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 22 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 22
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Somitra Kumar Sanadhya", "Palash Sarkar"]
- **src:** https://arxiv.org/pdf/0803.1220
- **d:** 5fdae8f367e712694875eee8e42cb72f37509a361f2f708502425f2eedf9f707
- **ba:** 512
- **bb:** 512
- **notes:** ["Transcribed from Sanadhya and Sarkar, 22-Step Collisions for SHA-2 (arXiv:0803.1220), Table 1. Printed words are big-endian 32-bit, in printed order.", "Standard SHA-256 IV; first 22 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 64-step SHA-256.", "The source prints no output value. Atlas computes the chaining value e0f336270e0eefaa1b659dd57c579e3730baf280202849ff8b8a967b47925b2a after the message block; the recorded digest additionally includes the common padding block.", "One representative per step count: the different 22-step pair printed in Sanadhya's thesis is not recorded separately."]
- **ext:** None

Input A (hex):
```
a0263fa5707425fb618cd8d27d58f7291eb9a96419f88f1c34e35071f28d40e3b43e29b81871a949e2e01390aaf3823e8d41a28e7f22ee027c625999183e603f
```
Input B (hex):
```
a0263fa5707425fb618cd8d27d58f7291eb9a96419f88f1c34e35071f28d40e3b43e29b91871a948defe7410aaf5223e8d41a28e7f22ee027c62599900000000
```

### 38. SHA-256 first 23 steps per block, one-block messages (Indesteege, Mendel, Preneel, Rechberger 2008)

- **id:** sha256-23-indesteege-et-al
- **t:** SHA-256 first 23 steps per block, one-block messages (Indesteege, Mendel, Preneel, Rechberger 2008)
- **lab:** SHA-256, 23 steps, standard IV
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 23 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 23
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Sebastiaan Indesteege", "Florian Mendel", "Bart Preneel", "Christian Rechberger"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-642-04159-4_18.pdf
- **d:** 033601a1abc3a922549a630997c40583e2017ba75408b5104f9ebb0f76389fdf
- **ba:** 512
- **bb:** 512
- **notes:** ["Transcribed from Collisions and Other Non-random Properties for Step-Reduced SHA-256 (SAC 2008), Table 4. Printed words are big-endian 32-bit, in printed order.", "Standard SHA-256 IV; first 23 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 64-step SHA-256.", "The source prints the chaining value after the message block, which Atlas reproduces: c77405ea8bfe2016ff0531b6a89b81f6e98cf052491a6c62fd009a403969dc83. The recorded digest additionally includes the common padding block, per this registry's convention.", "One representative per step count: two 23-step pairs by Sanadhya and Sarkar are not recorded separately."]
- **ext:** None

Input A (hex):
```
29f1ebfb4468041a1e6565b64cc17e754ea4f99333a77104864a828d1dcec3d2d33d7b02bcd4a2d73b10201d399535488e127f2b0304fc01e711857743b12ca7
```
Input B (hex):
```
29f1ebfb4468041a1e6565b64cc17e754ea4f99333a77104864a828d1dcec3d2d33d7b02bcd4a2d83b10201c3995d54891129f2a0304fc01e711857743b12ca7
```

### 39. SHA-256 first 24 steps per block, one-block messages (Indesteege, Mendel, Preneel, Rechberger 2008)

- **id:** sha256-24-indesteege-et-al
- **t:** SHA-256 first 24 steps per block, one-block messages (Indesteege, Mendel, Preneel, Rechberger 2008)
- **lab:** SHA-256, 24 steps, standard IV
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 24 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 24
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Sebastiaan Indesteege", "Florian Mendel", "Bart Preneel", "Christian Rechberger"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-642-04159-4_18.pdf
- **d:** f6a9ce29af09a63aff0292e5a55cddd5e0d4846b8959fe3f999e617cf0c1a078
- **ba:** 512
- **bb:** 512
- **notes:** ["Transcribed from Collisions and Other Non-random Properties for Step-Reduced SHA-256 (SAC 2008), Table 5. Printed words are big-endian 32-bit, in printed order.", "Standard SHA-256 IV; first 24 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 64-step SHA-256.", "The source prints the chaining value after the message block, which Atlas reproduces: 1584074c8b810a9401ea31b181bffd02d29c817de4e04b51b9f5ac4f6b34d1f8. The recorded digest additionally includes the common padding block, per this registry's convention.", "One representative per step count: a 24-step pair by Sanadhya and Sarkar is not recorded separately."]
- **ext:** None

Input A (hex):
```
0187e08e865cedaf5b69e21ae0f7485e50b98993217e465051e3cf65c2997c682c267e1682ffa4e937b5af095b28721d1be355977ff22aa1e807a758c1519aaa
```
Input B (hex):
```
0187e08e865cedaf5b69e21ae0f7485e50b98993217e465051e3cf65c2997c682c267e1682ffa4e937b5af0a5b28721c1be3f59782f24aa0e807a758c1519aaa
```

### 40. SHA-256 first 27 steps per block, one-block messages (Mendel, Nad, Schläffer 2011)

- **id:** sha256-27-mendel-nad-schlaffer
- **t:** SHA-256 first 27 steps per block, one-block messages (Mendel, Nad, Schläffer 2011)
- **lab:** SHA-256, 27 steps, standard IV
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 27 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 27
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Florian Mendel", "Tomislav Nad", "Martin Schläffer"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-642-25385-0_16.pdf
- **d:** 2fcaf8321c68cc783265b5713715ff6b383e1f4888316c6b03d627ac9cc7656c
- **ba:** 512
- **bb:** 512
- **notes:** ["Transcribed from Finding SHA-2 Characteristics: Searching through a Minefield of Contradictions (ASIACRYPT 2011). Printed words are big-endian, in printed order.", "Standard SHA-256 IV; first 27 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 64-step SHA-256.", "The paper prints the chaining value after the single message block, 5864015f133494fafa42bb3594bc44f929eabb369e461e332eab27f8106467c9, which Atlas reproduces. The recorded digest additionally includes the common padding block, per this registry's convention."]
- **ext:** None

Input A (hex):
```
725a03700daa9f1b071d92dfec8282c17913134abc2eb29102d33a84278dfd290c40f8ead8bd68a00ce670c55ec7155d9f6407a8729fbfe8aa7c7c08607ae76d
```
Input B (hex):
```
725a03700daa9f1b071d92dfec8282c17913134abc2eb29102d33a8427460e6d08c8fbead8bd68a00ce670c55ec7155d9f4425fb729fbfe8aa7c7c082d32d129
```

### 41. SHA-256 first 28 steps per block, one-block messages (Mendel, Nad, Schläffer 2013)

- **id:** sha256-28-mendel-nad-schlaffer
- **t:** SHA-256 first 28 steps per block, one-block messages (Mendel, Nad, Schläffer 2013)
- **lab:** SHA-256, 28 steps, standard IV
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 28 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 28
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Florian Mendel", "Tomislav Nad", "Martin Schläffer"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-642-38348-9_16.pdf
- **d:** fb8a9468ed7f09c8f0a5e6341142b293b6512044bd9acb5d148283ece7d90068
- **ba:** 512
- **bb:** 512
- **notes:** ["Transcribed from Improving Local Collisions: New Attacks on Reduced SHA-256 (EUROCRYPT 2013). Printed words are big-endian, in printed order.", "Standard SHA-256 IV; first 28 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 64-step SHA-256.", "Source discrepancy: the paper's Table 6 prints h1 = 01470131cd0062bc7e8f8c21989386523d49075a327f38e811f0d36d58601725 as the chaining value after the message block. For the printed messages Atlas computes 56449b4252e17ee12edbed34a1cf3f46e84b6d49ac9e1cc361a4725a4f245e31 after 28 steps, and could not reproduce the printed value for any step count from 24 to 32, with or without feed-forward. The two printed messages do collide for 28 steps and not for 29. Atlas records its own recomputed digest (which also includes the common padding block), not the printed h1."]
- **ext:** None

Input A (hex):
```
14c48440b3c3277fad69812dc3d4dffa7eae690b7f9fe027832aece89a4894581607a45cdb81bdc88786e031d8f2280172b6be5e45a2652ff3fbb17a2ce70f52
```
Input B (hex):
```
14c48440b3c3277fad69812dc3d4dffa7eae690b7f9fe027832aece89a489458e6b2f4fcd759b9308786e031d8f2280172b6be5e47e26dbff3fbb17a2ce70f52
```

### 42. SHA-256 first 29 steps per block, one-block messages (Li et al. 2025)

- **id:** sha256-29-li-et-al
- **t:** SHA-256 first 29 steps per block, one-block messages (Li et al. 2025)
- **lab:** SHA-256, 29 steps, standard IV
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 29 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 29
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Yingxin Li", "Fukang Liu", "Gaoli Wang", "Haifeng Qian", "Keting Jia", "Xiangyu Kong"]
- **src:** https://iacr.org/submit/files/slides/2025/crypto/crypto2025/144/144_slides.pdf
- **d:** 9adcf6f8105b45e9f3ef86b2c732ead9fa9db25e414c7e7fcee4ee0e04e9996a
- **ba:** 512
- **bb:** 512
- **notes:** ["Transcribed from the IACR-hosted CRYPTO 2025 talk slides (New Collision Attacks on Round-Reduced SHA-512), which also print this SHA-256 pair. Printed words are big-endian, in printed order.", "Standard SHA-256 IV; first 29 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 64-step SHA-256, nor for 30 steps.", "The slides print the chaining value after the single message block, b6631f1f071314ff56cb6d396a6f192c12509316cc8f897c0c916a47e76f6ba1, which Atlas reproduces. The recorded digest additionally includes the common padding block, per this registry's convention.", "Only the talk slides were reachable; the proceedings chapter was not read, so the table number in the paper is unknown."]
- **ext:** None

Input A (hex):
```
02faff1bd7e755b427138a63b70c69878b4ceb5d64c30d155a315dedb5b3ec6a2977f9966ce553065baf40c9e3b173bc151b8802e1991d09dcbc83e955189e54
```
Input B (hex):
```
02faff1bd7e755b427138a63b70c69878b4ceb5d64c30d155a315dedb5b3ec6a2977f9965fdd43845d8f37c8e3b173bc151b8802e1991d09e21c9b3355189e54
```

### 43. SHA-256 first 31 steps per block, two-block messages (Li et al. 2024)

- **id:** sha256-31-li-et-al
- **t:** SHA-256 first 31 steps per block, two-block messages (Li et al. 2024)
- **lab:** SHA-256, 31 steps, standard IV
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 31 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 31
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Yingxin Li", "Fukang Liu", "Gaoli Wang", "Xiaoyang Dong", "Siwei Sun"]
- **src:** https://iacr.org/submit/files/slides/2024/asiacrypt/asiacrypt2024/64/64_slides.pdf
- **d:** 55fdfb37efcbd086e19c3de0f72596300a3acdf48da5b1d0450a592bb2869fcd
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from the authors' ASIACRYPT 2024 slides (The First Practical Collision for 31-Step SHA-256): common first block M0, then M1 / M1'. Printed words are big-endian, in printed order.", "Standard SHA-256 IV; first 31 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 64-step SHA-256, nor for 30 or 32 steps.", "The slides print the chaining value after the two message blocks, ff5586592977dd015463884335f8de84a3336841f4f476f27c571548f7025605, which Atlas reproduces. The recorded digest additionally includes the common padding block, per this registry's convention."]
- **ext:** None

Input A (hex):
```
8ce3f8055c401aed579e5f7fbc3116cbca189b3ceb75f04c958f0a0e7760b082dcd5027d32260ad67b12b659eee66518ad7f88ddf8ad20bb7ae40ffd216092499abdeb1b1f195f415a7210c155614f13a2269dd1be888a61359257d4adf3737b9f0484a6eb830a5866add94a9669232d45271fa5b8f69585428bbce30703b904
```
Input B (hex):
```
8ce3f8055c401aed579e5f7fbc3116cbca189b3ceb75f04c958f0a0e7760b082dcd5027d32260ad67b12b659eee66518ad7f88ddf8ad20bb7ae40ffd216092499abdeb1b1f195f415a7210c155614f13a2269dd1be887a6735b2dfc5fde32975c70595a6eb838a5c66add94a9669232d45271fa5b8f69585428bbce30703b904
```

### 44. SHA-256 first 35 steps per block, two-block messages (Li, Liu, Wang, Shi 2026)

- **id:** sha256-35-li-et-al
- **t:** SHA-256 first 35 steps per block, two-block messages (Li, Liu, Wang, Shi 2026)
- **lab:** SHA-256, 35 steps, standard IV
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 35 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 35
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Yingxin Li", "Fukang Liu", "Gaoli Wang", "Jiali Shi"]
- **src:** https://eprint.iacr.org/2026/1080.pdf
- **d:** 8b32c7f0ffa0e0f8a218eecb9470f7e0b0da05ccd061b20b37107cb618c51c5d
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from Pushing the Limit of Memory-efficient Collision Attack Framework for SHA-2 (ePrint 2026/1080, CRYPTO 2026), Table 3. Printed words are big-endian 32-bit, in printed order.", "Standard SHA-256 IV; first 35 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 64-step SHA-256. Common first block M0, then M1 / M1'.", "The source prints the chaining value after the message blocks, which Atlas reproduces: c6209b2b5e3fd4c896087364046304abbbc6dad9403a26d1018e351fe444451f. The recorded digest additionally includes the common padding block, per this registry's convention."]
- **ext:** None

Input A (hex):
```
a8850273c0f4a5045d3ad7b56e5f5026535cc256e92ef7a5436f70df7d7e236acadc14e8d59ac1916874f1ba6b83960df6dfe9de6a013df2f856b739237894e8c0008214ae65f3bfe93c006a5f195aa9a4d6cd0f21811cecea897317db9ec6656ec172185100da8a0912e57ba96b205445f2222c4d12f88ad2701ecc140976d1
```
Input B (hex):
```
a8850273c0f4a5045d3ad7b56e5f5026535cc256e92ef7a5436f70df7d7e236acadc14e8d59ac1916874f1ba6b83960df6dfe9de6a013df2f856b739237894e8c0008214ae65f3bfe93c006a5f195aa984d6cd0f25c114ecca897317da9fd6ef6ec97e185100da8a0912e57ba96b205441b22a2c6d12f88ad2701ecc140976d1
```

### 45. SHA-256 first 36 steps per block, two-block messages (Li et al. 2026)

- **id:** sha256-36-li-et-al
- **t:** SHA-256 first 36 steps per block, two-block messages (Li et al. 2026)
- **lab:** SHA-256, 36 steps, standard IV
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 36 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 36
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Yingxin Li", "Zhuolong Zhang", "Muzhou Li", "Fukang Liu", "Haifeng Qian", "Jinwei Zhu"]
- **src:** https://eprint.iacr.org/2026/1120.pdf
- **d:** 8d9e66ce99054955116d31541b6516677cdde6349d01d45c2067dc49561f8e39
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from Pushing Collision Attacks on SHA-2 to 39 Steps (ePrint 2026/1120), Table 2. Printed words are big-endian 32-bit, in printed order.", "Standard SHA-256 IV; first 36 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 64-step SHA-256. Common first block M0, then M1 / M1'.", "The source prints the chaining value after the message blocks, which Atlas reproduces: 79df307814339285d39ae368142866bcba063acffa4431c6a5d74825c4be00db. The recorded digest additionally includes the common padding block, per this registry's convention.", "Unreviewed preprint at the time of import; the pair itself is checked here by computation."]
- **ext:** None

Input A (hex):
```
d7c6ac053be3567b33c02b263a6dfd82ed46810e8dacae353e00458426d2999239cff6590acc22238e77b3b0cc7f4bba9ff3abea17606f86ce693676c3bc18aa09abc4250e8b812185808046fadb1bca394268e3b9dfbd34ae15684574169a811ea03337a3210f1679b8201791059d1097294bab65ceec9c89c67ae2ac5eb7f9
```
Input B (hex):
```
d7c6ac053be3567b33c02b263a6dfd82ed46810e8dacae353e00458426d2999239cff6590acc22238e77b3b0cc7f4bba9ff3abea17606f86ce693676c3bc18aa09abc4250e8b812185808046fadb1bca394268e399dfbd34aa55604554169a811fa123bda329031679b8201791059d1097294bab618ee49ca9c67ae2ac5eb7f9
```

### 46. SHA-256 first 38 steps per block, two-block messages

- **id:** sha256-38-omergoldz
- **t:** SHA-256 first 38 steps per block, two-block messages
- **lab:** SHA-256, 38 steps, standard IV
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 38 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 38
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Omer (@omergoldz)"]
- **src:** https://x.com/omergoldz/status/2117314416299659735
- **d:** 5b61bad37673bb3323d64bc4fad45b44a7e6bf048d787d6127ec259b12d0d63f
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Public announcement attribution; priority not independently established. Standard SHA-256 IV; first 38 rounds on EVERY block including padding, big-endian words, feed-forward preserved. Not a collision for full 64-step SHA-256."]
- **ext:** None

Input A (hex):
```
33ee28ac5f8ef994c787777c079d17e11198d1beb527c8554bfeff014ab531951cf31bd2bbfc637e122da4f948e6e447d5a6b8b6ea9e7af5aac1aeabeeaceb0dbd07668b833fe88e689ffe8da52259da14b9855eee5138ba88355f4806d5cf5d161c50014c6b7d7e0e7eb888747559fc990a7af69dd8e59f57d7f6a3c0fbd03b
```
Input B (hex):
```
33ee28ac5f8ef994c787777c079d17e11198d1beb527c8554bfeff014ab531951cf31bd2bbfc637e122da4f948e6e447d5a6b8b6ea9e7af5aac1aeabeeaceb0dbd07668b833fe88e689ffe8da52259da14b9855eee5138ba88355f4838b3d19d161c4ffd4c6b7d7e0e813888747559fc990a7af69dd8e59f57d7f6a3c0fbd03f
```

### 47. SHA-256 20-step semi-free-start compression collision (seed 0)

- **id:** sha256-sfs-20-nahiyan
- **t:** SHA-256 20-step semi-free-start compression collision (seed 0)
- **lab:** SHA-256, 20-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 20 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 20
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** 4768a33d266857fff7b2a26ab1425e198f18824c03a57a1b45cfda69db540853
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 735e2ff1fd56fc47121d094a2a2b9866005991f1ccdaec13fa568667c216a4a5", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
4c0447430d84eebfbe84c9191378615f9ddecee989c61300381038832d9296b066e01bbd0afc2571bf601c9f46184c0e14546fdc8037cbaecf1b3058a5b35c9b
```
Input B (hex):
```
4c0447430d84eebfbe84c9191378615f9ddecee99f461300ce9bf8db2d9296b09c601bbd0afc2571bf601c9f46184c0e14546fdc6ab7cbaecf1b3058a5b35c9b
```

### 48. SHA-256 21-step semi-free-start compression collision (seed 0)

- **id:** sha256-sfs-21-nahiyan
- **t:** SHA-256 21-step semi-free-start compression collision (seed 0)
- **lab:** SHA-256, 21-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 21 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 21
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** a8b392911c255328844e12a872ede3162682eb6f580b7c42a3544b27b380c2e7
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 839cd479864f7aa3eb7929962ee84ec0f904cb5503a01835593a687d62650dc2", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
f3f79bfedb5ffffffbf0bf4f2fd57fb7d7afae038cbfe7be2ff8af07ffe744a1fdff7e4be2fb3cfe64972ad49c19bb7a466de39f7ba20691f4d37e6d597ebebc
```
Input B (hex):
```
f3f79bfedb5ffffffbf0bf4f2fd57fb7d7afae0372bc27be3e3dff46ffe744a117fcbe4be2fb3cfe64972ad49c19bb7a466de39f95a5c691f4d37e6d597ebebc
```

### 49. SHA-256 22-step semi-free-start compression collision (seed 0)

- **id:** sha256-sfs-22-nahiyan
- **t:** SHA-256 22-step semi-free-start compression collision (seed 0)
- **lab:** SHA-256, 22-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 22 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 22
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** e5a45bc09639b8fd7f07cb2a6e7b9375608c76018103b078ac3670e5396fbdbf
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: eb18bf2cfe43ad690e6ddd6c560fd382a647d6be6b3dc5134d44c274f1ae22f8", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
a2130137f3382a5910ff1336b6e22c145c2763a2c9d09df8ebb479439630dedd35af52e2116e4649406ec6b3cabbf5424f459d8943566972da92a2fe60e21b68
```
Input B (hex):
```
a2130137f3382a5910ff1336b6e22c145c2763a2c9d09df8ebb479439630deddb67176e290ac2249406ec6b3211bf5424f459d8943566972da92a2fe60e21b68
```

### 50. SHA-256 23-step semi-free-start compression collision (seed 0)

- **id:** sha256-sfs-23-nahiyan
- **t:** SHA-256 23-step semi-free-start compression collision (seed 0)
- **lab:** SHA-256, 23-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 23 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 23
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** 2e6f17e69cf525b05eeefb0e5e1a4876f96a772d89dcf3b927b7d5fc4654d8cd
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 009c71ec571b0144409fd4f5be21af7c4d54ddf6063b903c35e37e547d325172", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
5f9d1c44193f7fa375e01ac33af19b065db76ba019a21b9331f1704b0b389f977d305ea291610820c2526fff0ec035e44da8a09bec20efb0ac79894a80098478
```
Input B (hex):
```
5f9d1c44193f7fa375e01ac33af19b065db76ba019a21b9331f1704b0b389f97fdf23aa2109f2c20c2526fffe56035e44da8a09bec20efb0ac79894a80098478
```

### 51. SHA-256 24-step semi-free-start compression collision (seed 0)

- **id:** sha256-sfs-24-nahiyan
- **t:** SHA-256 24-step semi-free-start compression collision (seed 0)
- **lab:** SHA-256, 24-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 24 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 24
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** 390c6d1634ba42d534a602157433c35775dd7f47827dce17bff62125b1b51b35
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 93260b2b19784d1d4c6d16d92e7c31d1da729bdeee57ac1a85bdc2ae52a573c6", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
3de057584114ffa70dd790d4865299c41cb76722e9488ee1a9a4715b96e5077650a7fe5e4dd70dfcf8051b4d15caa5b4d4d5c44244485928d9427012b37fc117
```
Input B (hex):
```
3de057584114ffa70dd790d4865299c41cb76722e9488ee1a9a4715b96e50776aea43e5eefdacdfcf8051b4d2dd405b4d4d5c44244485928d9427012b37fc117
```

### 52. SHA-256 25-step semi-free-start compression collision (seed 0)

- **id:** sha256-sfs-25-nahiyan
- **t:** SHA-256 25-step semi-free-start compression collision (seed 0)
- **lab:** SHA-256, 25-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 25 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 25
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** a9c776506d40108a279e942d2d70292bfb12029d1e5cb1c4e27bfa3cae420fca
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 5c47e5bd6f4a6592bf8721a50d81cb755a5738797ba63f998da473c0d538c0e5", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
9b101880b627fe0ca1cef502a243f91d18b68c20e8434fe0e9f4715b7308f344961e5480ef7db801036286bb93a896814b69c6fc2c5bffdd9a292b1c48cf9155
```
Input B (hex):
```
9b101880b627fe0ca1cef502a243f91d18b68c20e8434fe0e9f4715b7308f344ff7fb880861c5401036286bbc83e96814b69c6fc2c5bffdd9a292b1c48cf9155
```

### 53. SHA-256 26-step semi-free-start compression collision (seed 0)

- **id:** sha256-sfs-26-nahiyan
- **t:** SHA-256 26-step semi-free-start compression collision (seed 0)
- **lab:** SHA-256, 26-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 26 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 26
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** 0d4b93a47f6c5f5e0fd31efa06e421799298857332f273aa3f276b6f92bdd55d
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 12a7918a32d69a11272f6c3b725b7023a51076c46da05e4008af69be1da8ddab", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
06a2d00a3adf887ab5b4824767e295b6cefa3782b37ede843dc9471dc9defc6dad6a6dd9be90bc41f3b4d17ed53dc4bd4ba46a75a50177b0cebe1cec31d84744
```
Input B (hex):
```
06a2d00a3adf887ab5b4824767e295b6cefa3782b37ede843dc9471dc9defc6d140981d92b334841f3b4d17ed53dc4bd4ba46a7575b677b0cebe1cec31d84744
```

### 54. SHA-256 27-step semi-free-start compression collision (seed 0)

- **id:** sha256-sfs-27-nahiyan
- **t:** SHA-256 27-step semi-free-start compression collision (seed 0)
- **lab:** SHA-256, 27-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 27 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 27
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** d7f5488a7b63781181d64c27613abe866ac8d1e6ab6fed0102a58d3800e10090
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 72d8a8e67290ccd16e614a517c6b2a3b04e83c1a58018de9b639bd667266fe45", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
5fbbf40cdffeda2a907e8729e714afced907fe43281269607abf7e48c95934582a1182db288cb482d09bab5a9730809e695670f208688307609bc07cf6f0dc7b
```
Input B (hex):
```
5fbbf40cdffeda2a907e8729e714afced907fe43281269607abf7e48c959345893726edbbd2f4082d09bab5a9730809e695670f29edf8307609bc07cf6f0dc7b
```

### 55. SHA-256 28-step semi-free-start compression collision (seed 0)

- **id:** sha256-sfs-28-nahiyan
- **t:** SHA-256 28-step semi-free-start compression collision (seed 0)
- **lab:** SHA-256, 28-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 28 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 28
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** 26489efccf5a7b9ee0ba4b5632769d441e4d06d744e1ac2ad16a88da2370bbfb
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: f6a195607a4d4547385ea249066aad88102eb8637acc1ee5a1d52d26c7c73714", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
9811d5c3d3a98403806359207b7224ab404e5c67820ff42d41dc671c5fd55c87ed626fdd7688b68c3250fee19178a76aab191c0e60614539282dac77d4ca1940
```
Input B (hex):
```
9811d5c3d3a98403806359207b7224ab404e5c67820ff42d41dc671c5fd55c87540183dde32b428c3250fee19178a76aab191c0e491c4539282dac77d4ca1940
```

### 56. SHA-256 29-step semi-free-start compression collision (seed 0)

- **id:** sha256-sfs-29-nahiyan
- **t:** SHA-256 29-step semi-free-start compression collision (seed 0)
- **lab:** SHA-256, 29-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 29 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 29
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** 43eeb67bdf849ef0528e9864785ccc86ca18197420f0d9d5741745a75a8712b5
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 374342180a566f95f817e7f97231adb7d570f891b3f810cf32e7bfd0c62ebb90", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
eb3ffb620983b384ee03e91ead368ecadcc3ecdfb12802403af8b7e8a411713153502fff22cf4a026b80eddeb6869500b3d213766d2448956afebcf11a144bba
```
Input B (hex):
```
eb3ffb620983b384ee03e91ead368ecadcc3ecdfb12802403af8b7e89a776ff15350300322cf4a026b7f6ddeb6869500b3d213766d2448956afebcf11a144bbe
```

### 57. SHA-256 30-step semi-free-start compression collision (seed 0)

- **id:** sha256-sfs-30-nahiyan
- **t:** SHA-256 30-step semi-free-start compression collision (seed 0)
- **lab:** SHA-256, 30-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 30 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 30
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** 0c3d2eaca4f48f48009431a948eb8c3ae6246e0221391c8440f5234950c5d048
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 26ae00fc40a28536a9786ff29fb8900a8e02ed34d4316f93b2d93db6667f9d8f", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
2ed4b3d4a6e02bec333aedafb4f0d4c6bb7bb4b7c641466595797d4f2589900b53562fff69b84442647e95a6bbd2a963ae375e4e06b6c352535d2747cb135ee8
```
Input B (hex):
```
2ed4b3d4a6e02bec333aedafb4f0d4c6bb7bb4b7c641466595797d4f1bef8ecb5356300369b84442648115a6bbd2a963ae375e4e06b6c352535d2747cb135eec
```

### 58. SHA-256 31-step semi-free-start compression collision (seed 1)

- **id:** sha256-sfs-31-nahiyan
- **t:** SHA-256 31-step semi-free-start compression collision (seed 1)
- **lab:** SHA-256, 31-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 31 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 31
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** 0db86d3253bfcac053544ed36296bcd8e36f93a20ca613d0a9172d82e997709f
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: a9b5150f867d34fdd617186e1d88f4d3520fd22826f65e2b1bc0bc1bac66a3b6", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
d3ac974ccde6b71905b33e2ecdafaf07661eb1dfb02663fd5a8567796519512953502ffff7337f1cf77eabbfc674b7cb0cb855cb8c0180b7aabbb978ffda2660
```
Input B (hex):
```
d3ac974ccde6b71905b33e2ecdafaf07661eb1dfb02663fd5a8567795b7f4fe953503003f7337f1cf7812bbfc674b7cb0cb855cb8c0180b7aabbb978ffda2664
```

### 59. SHA-256 32-step semi-free-start compression collision (seed 2)

- **id:** sha256-sfs-32-nahiyan
- **t:** SHA-256 32-step semi-free-start compression collision (seed 2)
- **lab:** SHA-256, 32-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 32 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 32
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** e586a8657cf71af1676dd4dae7b32555f09495dbba5acf37323a66bafef88679
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 34b62e6c797eb709916968991d1b6f06d4de163734ce7c2f62519ffea307e740", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
4fe77387ad2f384d4de621a64a0e8d86cf6c4e93113dc829032ac8de2542f07591644fff92bd931e777ed4446c8bdaef1cdaf596a4be65288526fb3c6719cc6d
```
Input B (hex):
```
4fe77387ad2f384d4de621a64a0e8d86cf6c4e93113dc829032ac8de1b24eeb59164500392bd931e778154446c8bdaef1cdaf596a4be65288526fb3c6719cc69
```

### 60. SHA-256 33-step semi-free-start compression collision (seed 2)

- **id:** sha256-sfs-33-nahiyan
- **t:** SHA-256 33-step semi-free-start compression collision (seed 2)
- **lab:** SHA-256, 33-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 33 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 33
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** 4736a384cc42bd9cbbcfbd7aae5c58b9043f7f70717f165fcd7a3b5d387d224c
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 269c1f0fbaf6394fba2cdbc71fc5cb938373d9544e0ff67f81dd074dec43b897", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
559c2f94f23b21924dafd4e17229e3ce47be31fe8297f5b08a8d2823e3d4cea75d582ffc6c6936d5b27f4110f31491ef33462a217eff8e412f1276ae17554da4
```
Input B (hex):
```
559c2f94f23b21924dafd4e17229e3ce47be31fe8297f5b08a8d2823ddb2d0675d5830006c6936d5b280c110f31491ef33462a217eff8e412f1276ae17554da0
```

### 61. SHA-256 34-step semi-free-start compression collision (seed 1)

- **id:** sha256-sfs-34-nahiyan
- **t:** SHA-256 34-step semi-free-start compression collision (seed 1)
- **lab:** SHA-256, 34-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 34 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 34
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** 2fb850245ab11e138f805efb44a29560661210d1852ddeb3aa67561ca20cf347
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 883148a9ca063c546b43c2df7f515edc085d1e2aa300b35e2e8af66081f9ff48", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
a0b814a3dc5847d8fa4438cc6c52885e1c032e84022c086bbd041cf71986900f5ca03002f7a576b14780d443beec62bf9f1c4765c0ce9c08a120bd17588d8719
```
Input B (hex):
```
a0b814a3dc5847d8fa4438cc6c52885e1c032e84022c086bbd041cf727e08ecf5ca02ffef7a576b1477f5443beec62bf9f1c4765c0ce9c08a120bd17588d871d
```

### 62. SHA-256 35-step semi-free-start compression collision (seed 6)

- **id:** sha256-sfs-35-nahiyan
- **t:** SHA-256 35-step semi-free-start compression collision (seed 6)
- **lab:** SHA-256, 35-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 35 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 35
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p/collisions.md
- **d:** 95299ad1107d3f3bc6b2af4ad664d3bb15d8de8f30c20545f9c73b6e6231966e
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: ad5e49ef97adbe8d68729c702218fc684356663e119103ad0ab7fc60bb583ffe", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
a78b5eb54e052f097e2929d1a79c795a5b3bd9b6afcf3ea793f3960ee2c52e8f5d5a2ffcbda2ba75ad7f0114ad0411f535362a1d7eff8e402f1276ae17554da4
```
Input B (hex):
```
a78b5eb54e052f097e2929d1a79c795a5b3bd9b6afcf3ea793f3960edca3304f5d5a3000bda2ba75ad808114ad0411f535362a1d7eff8e402f1276ae17554da0
```

### 63. SHA-256 36-step semi-free-start compression collision (seed 0)

- **id:** sha256-sfs-36-nahiyan
- **t:** SHA-256 36-step semi-free-start compression collision (seed 0)
- **lab:** SHA-256, 36-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 36 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 36
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** e509f8f4a1f7b0f7a3d135341eddc308a1806efc4d69a184a8377242688ea2da
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: fff488a85131f9d455b4f18f7998160d53189ea4a81d511257c637501655f813", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
3ef20f94537d0019444193562e7e190a55d8970970e442f0f2565edbe34dcf8f5d5e2ffcfe0bf6f8ce7f388bcf041222b3362a1ffeff8e4c2f1276ae17554da4
```
Input B (hex):
```
3ef20f94537d0019444193562e7e190a55d8970970e442f0f2565edbdd2bd14f5d5e3000fe0bf6f8ce80b88bcf041222b3362a1ffeff8e4c2f1276ae17554da0
```

### 64. SHA-256 37-step semi-free-start compression collision (seed 4)

- **id:** sha256-sfs-37-nahiyan
- **t:** SHA-256 37-step semi-free-start compression collision (seed 4)
- **lab:** SHA-256, 37-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 37 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 37
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** 0dd273c65deb5dbef486aceb7fc825f310e5835141c0e6808952ba759ba7250d
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 544aee430e55139dc84c5a64d3a3a6a2bbdb96b098b23d24042a9992bcf45eb8", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
c22245faf52bd140996738e0a2f03e1f39487c4d3dc2248a5fcfe4002244af8d5d582ffc888bbeaed17f788cad14122137462a407eff8e422f1276ae17554da4
```
Input B (hex):
```
c22245faf52bd140996738e0a2f03e1f39487c4d3dc2248a5fcfe4001c22b14d5d583000888bbeaed180f88cad14122137462a407eff8e422f1276ae17554da0
```

### 65. SHA-256 38-step semi-free-start compression collision (seed 1)

- **id:** sha256-sfs-38-nahiyan
- **t:** SHA-256 38-step semi-free-start compression collision (seed 1)
- **lab:** SHA-256, 38-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 38 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 38
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Nahiyan Alamgir (published artifact repository owner)"]
- **src:** https://raw.githubusercontent.com/nahiyan/sha256-data/c216a4216e47fcb3370f4d11a5765a1c3f2fd072/sfs/cadical-p-ib/collisions.md
- **d:** 5556e271a74edb890182f28c1c548991b503e1e08564f645912040f1d01bab4c
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: c3da74c5cf2e830f8cfbe7a7701c631d5919aecdda91b128d494e0d92a376606", "One representative per step count from published CaDiCaL-p-ib/CaDiCaL-p tables, not all seeds or solvers.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward. Blocks and states are big-endian 32-bit words.", "Attribution is artifact ownership, not a determination of attack-discovery priority; consult paper for coauthors."]
- **ext:** None

Input A (hex):
```
4a0521a275a99baaf3e938ca2c6cef3d839752c7bc14317b18bcf55863d4cebb5d582ffc2f12f69ea77f73c4f3141218b5462a4dfeff8e412f1276ae17554da4
```
Input B (hex):
```
4a0521a275a99baaf3e938ca2c6cef3d839752c7bc14317b18bcf5585db2d07b5d5830002f12f69ea780f3c4f3141218b5462a4dfeff8e412f1276ae17554da0
```

### 66. SHA-256 39-step semi-free-start compression collision (Li, Liu, Wang 2024)

- **id:** sha256-sfs-39-li-liu-wang
- **t:** SHA-256 39-step semi-free-start compression collision (Li, Liu, Wang 2024)
- **lab:** SHA-256, 39-step semi-free-start
- **fl:** SHA-256
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha256:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 39 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 39
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Yingxin Li", "Fukang Liu", "Gaoli Wang"]
- **src:** https://iacr.org/submit/files/slides/2024/eurocrypt/eurocrypt2024/107/slides.pdf
- **d:** 431cadcdce6893bbd6c9689a334854e83baae1ab038a195accf54a191c40606d
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 02b19d5a88e1df045ea3c7b7f2f7d1a486cb1b1fc8ee51a51b4d0541651b92e7", "Transcribed from the authors' EUROCRYPT 2024 slides (New Records in Collision Attacks on SHA-2). Printed words are big-endian, in printed order.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward; it equals the hash value printed in the slides."]
- **ext:** None

Input A (hex):
```
c61d6de7755336e85e61d61818036de6a79f2f1df2b44c7b4c0ef36ba85d45cff72b8c2f0def947ca0eab1598021370c4b0d80117aad07f633cd69023bad5d64
```
Input B (hex):
```
c61d6de7755336e85e61d61818036de6a79f2f1df2b44c7b4c0ef36ba85d45cfe72b8c2f0fcf907cb0eab15981a1bfc14b0986117aad07f633cd69023bad5d64
```

### 67. SHA-224 40-step free-start compression collision (Li, Liu, Wang 2024)

- **id:** sha224-fs-40-li-liu-wang
- **t:** SHA-224 40-step free-start compression collision (Li, Liu, Wang 2024)
- **lab:** SHA-224, 40-step free-start
- **fl:** SHA-224
- **g:** sha256
- **gl:** SHA-256 and 224
- **sub:** sha224:compression-free-start
- **iv:** 1
- **cat:** compression function
- **atk:** free-start
- **scope:** One call to the compression function, 40 of 64 steps, no padding, 224-bit output. The attacker picked a different starting state for each input, which is an easier game than sharing one.
- **r:** 40
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 224
- **grp:** 4
- **who:** ["Yingxin Li", "Fukang Liu", "Gaoli Wang"]
- **src:** https://iacr.org/submit/files/slides/2024/eurocrypt/eurocrypt2024/107/slides.pdf
- **d:** 9af50cacc165a72fb6f1c9f3ef54bad9af0cfb1f57d357c9c6462616
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV for A: 791c9c6bbaa7f900f7c532989073cbbdc90690c55591553c43a5d984af92402d", "Chosen IV for B: 791c9c6bbaa7f900f7c532989073cbbdc90690c55591553c43a5d984bf92402d", "Transcribed from the authors' EUROCRYPT 2024 slides (New Records in Collision Attacks on SHA-2). Printed words are big-endian, in printed order.", "Free-start: each input has its OWN attacker-chosen chaining value (they differ in the last state word), one unpadded block each. This is weaker than a semi-free-start collision and far from a hash collision.", "The collision is on SHA-224's 224-bit output: the first seven words of the compression output after feed-forward. The eighth word, which SHA-224 discards, differs between the two inputs."]
- **ext:** None

Input A (hex):
```
f41d61b4ce033ba2dd1bc208a268189bee6bda2c5ddbe94d9675bbd332c1ba8a7eba797d88b06a8f3bc3015cd36f38cccfcb88e03c70f7f3faa0c1fe35c62535
```
Input B (hex):
```
e41d61b4ce033ba2dd1bc208a268189bee6bda2c5ddbe94d9675bbd332c1ba8a7eba797d98b06a8f39e3055cc36f38ccce4b002d3c74f1f3faa0c1fe35c62535
```

### 68. SHA-512 first 18 steps per block, one-block messages (Sanadhya, Sarkar 2008)

- **id:** sha512-18-sanadhya-sarkar
- **t:** SHA-512 first 18 steps per block, one-block messages (Sanadhya, Sarkar 2008)
- **lab:** SHA-512, 18 steps, standard IV
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 18 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 18
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 512
- **grp:** 8
- **who:** ["Somitra Kumar Sanadhya", "Palash Sarkar"]
- **src:** https://dspace.isical.ac.in/bitstreams/c4ee3d67-8099-4756-81e8-6ac202d31d79/download
- **d:** 9e6166b4710042dc885a78b128211b6583a0e451898a7b2d1d63fadec9cf9887b464369eb4cb0dca2808f0c6d85eb8ccb0a4f6dcdbefe927b0e6eddc6187440f
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from S. K. Sanadhya, \"A Study of the SHA-2 Cryptographic Hash Family\", PhD thesis (supervisor P. Sarkar), Indian Statistical Institute, Kolkata, February 2009 (ISI DSpace copy). Printed words are 64-bit big-endian, in printed order.", "Standard SHA-512 IV; first 18 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 80-step SHA-512.", "The source prints no output value. Atlas computes the chaining value 85303506856d92ac1b5f04315417326d2f42ddc2e0f1765debaf3429d9eb189686491bb9c7e6e39b4082abc28d5a2c36396fc466dfcd8ac9e8473f14ae99f2cd after the single message block; the recorded digest additionally includes the common padding block.", "The thesis attributes the 18- and 20-step SHA-512 examples to Sanadhya-Sarkar, \"Non-Linear Reduced Round Attacks Against SHA-2 Hash Family\", ACISP 2008 (LNCS 5107; ePrint 2008/174); that paper could not be retrieved here, so only the thesis copy was checked.", "Table caption: \"Colliding message pair for 18 step SHA-512 with standard IV ... The initial perturbation w is taken to be abcdef0123456789.\" All-zero words are printed as \"0\"."]
- **ext:** None

Input A (hex):
```
00000000000000000000000000000000000000000000000000000000000000001e4387c99964e3df833c00f2b6a3adde00000000000000000000000000000000823dd46c0c9346e529c51252ea4e9d0b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```
Input B (hex):
```
000000000000000000000000000000000000000000000000abcdef01234567893e1ae599c9a10350d80a93fe0e9ecbefb0c053b0e95ee217845204a29bf9d88ff5b543b1f125cc3e29c51252ea4e9d0b0000000000000000543210fedcba98770000000000000000000000000000000000000000000000000000000000000000
```

### 69. SHA-512 first 20 steps per block, one-block messages (Sanadhya, Sarkar 2008)

- **id:** sha512-20-sanadhya-sarkar
- **t:** SHA-512 first 20 steps per block, one-block messages (Sanadhya, Sarkar 2008)
- **lab:** SHA-512, 20 steps, standard IV
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 20 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 20
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 512
- **grp:** 8
- **who:** ["Somitra Kumar Sanadhya", "Palash Sarkar"]
- **src:** https://dspace.isical.ac.in/bitstreams/c4ee3d67-8099-4756-81e8-6ac202d31d79/download
- **d:** cd771dadb697ad95c61058a86c4b2989f643d8f7750126fe768fe4a19f23ae642288f691c6d20c315a2f2a820966751901a8bafa3b8ae159502e719adebf1ccf
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from S. K. Sanadhya, \"A Study of the SHA-2 Cryptographic Hash Family\", PhD thesis (supervisor P. Sarkar), Indian Statistical Institute, Kolkata, February 2009 (ISI DSpace copy). Printed words are 64-bit big-endian, in printed order.", "Standard SHA-512 IV; first 20 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 80-step SHA-512.", "The source prints no output value. Atlas computes the chaining value 1fd07ddfdf47e2c97d80afb15b12d2dd6159a13544ad935ad40742dbcb1043a2b7a9265602a1468dd4200a57494cfbce60184f054c996ad6572d7c3ee6999bd4 after the single message block; the recorded digest additionally includes the common padding block.", "The thesis attributes the 18- and 20-step SHA-512 examples to Sanadhya-Sarkar, ACISP 2008 (ePrint 2008/174); only the thesis copy was checked."]
- **ext:** None

Input A (hex):
```
000000000000000000000000000000000000000000000000b5d7924a5f1dfac81d8a59931fde4139f585791431ba62184cb5bceeaf7567953a68e5bec866399eb3ae5a6fb00c2fec533c19c84c7c8969a28b08dc36fe38cfaaf3823c2a004b1f0000000000000000000000000000000000000000000000000000000000000000
```
Input B (hex):
```
000000000000000000000000000000000000000000000000b5d7924a5f1dfac81d8a59931fde4139f585791431ba62194cb1fceeaef567943a74a5bec7e6399e14ab7440a4022222533c19c84c7c8969a28b08dc36fe38cfaaf3823c2a004b1f0000000000000000ffffffffffffffff00000000000000000000000000000000
```

### 70. SHA-512 first 21 steps per block, one-block messages (Sanadhya, Sarkar 2008)

- **id:** sha512-21-sanadhya-sarkar
- **t:** SHA-512 first 21 steps per block, one-block messages (Sanadhya, Sarkar 2008)
- **lab:** SHA-512, 21 steps, standard IV
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 21 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 21
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 512
- **grp:** 8
- **who:** ["Somitra Kumar Sanadhya", "Palash Sarkar"]
- **src:** https://dspace.isical.ac.in/bitstreams/c4ee3d67-8099-4756-81e8-6ac202d31d79/download
- **d:** 99ea9ebb36626830b6ccf047b80ca4a0c5eef6606fbf47900a6d2d3dcb9d97afe33ac11e9885d58acb862952470b22b15f6671840f203bbb5afd48416169b4d9
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from S. K. Sanadhya, \"A Study of the SHA-2 Cryptographic Hash Family\", PhD thesis (supervisor P. Sarkar), Indian Statistical Institute, Kolkata, February 2009 (ISI DSpace copy). Printed words are 64-bit big-endian, in printed order.", "Standard SHA-512 IV; first 21 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 80-step SHA-512.", "The source prints no output value. Atlas computes the chaining value cc698c8f79ffa6be05be917fa457d71673722b90e291fcba871460888f8ea68d5e45a4d46b1b381d2942f2f9194654451e1f9e77ae6080451014dc6db4f19980 after the single message block; the recorded digest additionally includes the common padding block.", "The thesis attributes the 21-step SHA-512 example to Sanadhya-Sarkar, \"Deterministic Constructions of 21-Step Collisions for the SHA-2 Hash Family\", ISC 2008 (LNCS 5222); only the thesis copy was checked.", "Table caption: \"The six free words are taken to be all zero in the first message.\""]
- **ext:** None

Input A (hex):
```
000000000000000000000000000000000000000000000000f31b03afd93b0f6d8308c99162dbe6fe739cde771413fca749404e11d70bcb89b913ae32c4c3736fe284a20a666a735b573c19c84c7c8968a28b08dc36fe38d06db010d6afe336798d41a28b0d847692000000000000000000000000000000000000000000000000
```
Input B (hex):
```
000000000000000000000000000000000000000000000000f31b03afd93b0f6d8308c99162dbe6fe739cde771413fca749404e11d70bcb8ab907ee32c543736fe290620a65ea735b533c19c84c7c8969a28b08dc36fe38d06db010d6afe336798d41a28b0d8476920000000000000000ffffffffffffffff0000000000000000
```

### 71. SHA-512 first 22 steps per block, one-block messages (Sanadhya, Sarkar 2008)

- **id:** sha512-22-sanadhya-sarkar
- **t:** SHA-512 first 22 steps per block, one-block messages (Sanadhya, Sarkar 2008)
- **lab:** SHA-512, 22 steps, standard IV
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 22 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 22
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 512
- **grp:** 8
- **who:** ["Somitra Kumar Sanadhya", "Palash Sarkar"]
- **src:** https://arxiv.org/pdf/0803.1220
- **d:** 969e183a70c0b644234fe389efb9ad3541b2627c5af656d372fea5c792b5282148bafd7cf07fef745e606c5bb3bb36c5e598d4271d854721760e0cd52913e02a
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from S. K. Sanadhya, P. Sarkar, \"22-Step Collisions for SHA-2\", arXiv:0803.1220v1, 8 March 2008. Printed words are 64-bit big-endian, in printed order.", "Standard SHA-512 IV; first 22 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 80-step SHA-512.", "The source prints no output value. Atlas computes the chaining value 5429141224a499d8ed65d87f8531457e44790b3084967e86d22b4868a01da335c1aeca05d347b4891669b370f088a3ba4573453db4a9c0c6f639a713cf17d1af after the single message block; the recorded digest additionally includes the common padding block.", "First published 22-step SHA-512 pair (note dated 8 March 2008). One representative per step count: the different 22-step pair printed in Sanadhya's thesis is not recorded separately."]
- **ext:** None

Input A (hex):
```
3ffb91948b32733795f3c893b2356b98506c68760abf51e9fab877b7eef3aaa255d5b38ec34340cfdaa006ef3f677afaa5a01d9f1c67d9c85b219ee6f447480b52af39ff1ecfb48e5cff9ae5d4d60a40db6c1a412c9b4d4daaf3823c2a004b1f8d41a28b0d8476937f212e01c4e969377eeeca5c84ba3bda1acad103aa814e0e
```
Input B (hex):
```
3ffb91948b32733795f3c893b2356b98506c68760abf51e9fab877b7eef3aaa255d5b38ec34340cfdaa006ef3f677afaa5a01d9f1c67d9c85b219ee6f447480b52af39ff1ecfb48f5cff9ae5d4d60a3fdb687a412d1b4d65aaf3623c2a004b078d41a28b0d8476937f212e01c4e969377eeeca5c84ba3bda0000000000000000
```

### 72. SHA-512 first 23 steps per block, one-block messages (Indesteege, Mendel, Preneel, Rechberger 2008)

- **id:** sha512-23-indesteege-et-al
- **t:** SHA-512 first 23 steps per block, one-block messages (Indesteege, Mendel, Preneel, Rechberger 2008)
- **lab:** SHA-512, 23 steps, standard IV
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 23 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 23
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 512
- **grp:** 8
- **who:** ["Sebastiaan Indesteege", "Florian Mendel", "Bart Preneel", "Christian Rechberger"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-642-04159-4_18.pdf
- **d:** 3bde6a9aea8a39544cc552acca8022074013134ee0ab9eb97f2cc204af8a5bcf81395b15eaca3014b9a44b1391432a927e2923276ac5b49e32be7a5dd1ed85ca
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from S. Indesteege, F. Mendel, B. Preneel, C. Rechberger, \"Collisions and Other Non-random Properties for Step-Reduced SHA-256\", SAC 2008, LNCS 5381, pp. 276-293. Printed words are 64-bit big-endian, in printed order.", "Standard SHA-512 IV; first 23 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 80-step SHA-512.", "The source prints the chaining value after the single message block, which Atlas reproduces: dd44d89f178803f5136802b223c880babbb80917dda6a3e7be1f118889bd541598adc37a0f32d15183d35099922ee2c6670ac37463f224dae0835506fb66503d. The recorded digest additionally includes the common padding block, per this registry's convention.", "The paper gives no example for its 24-step SHA-512 attack (Table 1, \"example: no\").", "One representative per step count: a different 23-step pair by Sanadhya and Sarkar (arXiv:0809.0216) is not recorded separately."]
- **ext:** None

Input A (hex):
```
0000000017daf2ec000000004b7adc8e000000000d01f49d54cce0ac731eb4c95caf52c6f3e941cd0224e6b80421630595bbdc5df5b491c89f7f1453e39ee6c03e345efecc81805893dfcee7a268ce6990561054da994c547262751c31b5bdd054b1d56610b9e8027f201dfcfce968c02b90cc3824ee5f1305cfd16a7b4c4ab1
```
Input B (hex):
```
0000000017daf2ec000000004b7adc8e000000000d01f49d54cce0ac731eb4c95caf52c6f3e941cd0224e6b80421630595bbdc5df5b491c89f7f1453e39ee6c03e345efecc81805893dfcee7a268ce6a90561054da994c537266551c31b5bd1854b0b56610b9e8017f201dfcfce968c02b90cc3824ee5f1305cfd16a7b4c4ab1
```

### 73. SHA-512 first 24 steps per block, one-block messages (Sanadhya, Sarkar 2008)

- **id:** sha512-24-sanadhya-sarkar
- **t:** SHA-512 first 24 steps per block, one-block messages (Sanadhya, Sarkar 2008)
- **lab:** SHA-512, 24 steps, standard IV
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 24 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 24
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 512
- **grp:** 8
- **who:** ["Somitra Kumar Sanadhya", "Palash Sarkar"]
- **src:** https://arxiv.org/pdf/0809.0216
- **d:** bc1888ea50c59a9c49457b4a9924ba4e803aa0c9b0e1d17f37fd32beec660da400103ef36b37dbdfb8e5ffbc6da453ba6677398a0f3ecda6c730c1cc730c6adb
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from S. K. Sanadhya, P. Sarkar, \"Colliding Message Pairs for 23 and 24-step SHA-512\", arXiv:0809.0216v1, 1 September 2008. Printed words are 64-bit big-endian, in printed order.", "Standard SHA-512 IV; first 24 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 80-step SHA-512.", "The source prints no output value. Atlas computes the chaining value 4c303fa06c5986587bb79d1d9e8b73edc146f735a42b08513d6b80cc02f9a0c404a69540001c787caae70755c7cf50209313dd3cff66cf57c0575c359e806d69 after the single message block; the recorded digest additionally includes the common padding block.", "Described by its authors as the first colliding message pair for 24-step SHA-512.", "The same pair is printed in the arXiv note and in the thesis."]
- **ext:** None

Input A (hex):
```
dedb689cfc766965c7b8e064ff720f7cc136883560348c9c3747df7d0cf47678855e17555cfedc5f88566babccaa63e95dda9777938b73cdb17b00574a4e421686f3ff48fd12ea19cd15c6f8d6da38ce5e2c6b7b0411e70b36ed67e93a794e661b65e96b0276782104d0950089db6c685bc9b9673e38eff3b05d879ad024d3fa
```
Input B (hex):
```
dedb689cfc766965c7b8e064ff720f7cc136883560348c9c3747df7d0cf47678855e17555cfedc5f88566babccaa63e95dda9777938b73cdb17b00574a4e421686f3ff48fd12ea19cd15c6f8d6da38ce5e2c6b7b0411e70c36ed67e93a794e651b66096b0276782904d0f50089db6e9f5bc9b9673e38eff3b05d879ad024d3fa
```

### 74. SHA-512 first 27 steps per block, one-block messages (Dobraunig, Eichlseder, Mendel 2015)

- **id:** sha512-27-dobraunig-et-al
- **t:** SHA-512 first 27 steps per block, one-block messages (Dobraunig, Eichlseder, Mendel 2015)
- **lab:** SHA-512, 27 steps, standard IV
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 27 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 27
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 512
- **grp:** 8
- **who:** ["Christoph Dobraunig", "Maria Eichlseder", "Florian Mendel"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-662-48800-3_25.pdf
- **d:** de37556384799b1e8242484ba9ed60666c864bcef557a45f402ab24ff7132925a357b32bfa31b46d74a2f1b7de66bc41e9a5d1f72469a9f0de7ef619800f54dc
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from C. Dobraunig, M. Eichlseder, F. Mendel, \"Analysis of SHA-512/224 and SHA-512/256\", ASIACRYPT 2015, LNCS 9453, pp. 612-630. Printed words are 64-bit big-endian, in printed order.", "Standard SHA-512 IV; first 27 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 80-step SHA-512.", "The source prints the chaining value after the single message block, which Atlas reproduces: d838f1d2ae4bf1853fc837ae9bbc28d46b2f2977f58a969799c48839f0e8bdcac9c0a86fed1d921a2f823b1fa19137513ba170b902c6da309c4e5807be51a7e7. The recorded digest additionally includes the common padding block, per this registry's convention.", "In the Springer PDF the appendix tables are vector drawings, so the digits cannot be extracted as text. The values were read from a 400-dpi rasterisation of the page (pdftoppm) and are confirmed by the redundancy printed in the table itself: m XOR m* equals the printed delta-m for all 16 words (and h0 XOR h0* equals the printed delta-h0 where given), and the recomputed output equals the printed h1."]
- **ext:** None

Input A (hex):
```
537e7a4986aa2fce11206ad0306c752b90124a9e1c9b0ce28c14e0356fd26f5ffd3ef90ea3e4366f35d8c2ba58abd92fb23e476632eca1fde2b122ef46649b73dfc020070e628f377acf74d1d10075586c6359a6fe7fe2f0d490bd22815eb49472fedf1f807df6f3a8585af19b6dd9d13d2053b0c295522b2d970e0e52a49081
```
Input B (hex):
```
537e7a4986aa2fce11206ad0306c752b90124a9e1c9b0ce28c14e0356fd26f5ffd3ef90ea3e4366f35d8c2ba58abd92fb23e476632eca1fd5cc1250f06649b73d0009fc70e628f367acf74d1d10075586c6359a6fe7fe2f0d490bd22815eb494f0bc01169075f6fba8585af19b6dd9d13d2053b0c295522bd3907e3653649081
```

### 75. SHA-512 first 28 steps per block, one-block messages (Li, Liu, Wang 2024)

- **id:** sha512-28-li-liu-wang
- **t:** SHA-512 first 28 steps per block, one-block messages (Li, Liu, Wang 2024)
- **lab:** SHA-512, 28 steps, standard IV
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 28 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 28
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 512
- **grp:** 8
- **who:** ["Yingxin Li", "Fukang Liu", "Gaoli Wang"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-031-58716-0_6.pdf
- **d:** a1cdda1b2e36105ddc927d66e99bbe5446c388698fb560c754bdb08e364465f6fc161aa7551919027d9997c955dfffeaace15ced78f182f4aba2afc40c025df7
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from Y. Li, F. Liu, G. Wang, \"New Records in Collision Attacks on SHA-2\", EUROCRYPT 2024, LNCS 14651, pp. 158-186. Printed words are 64-bit big-endian, in printed order.", "Standard SHA-512 IV; first 28 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 80-step SHA-512.", "The source prints the chaining value after the single message block, which Atlas reproduces: dceb3d88adf54bd2966c4cb1ab0cf40001e701fdf10ab603796d6e5028a5e89af29a7517b216c09f46dbae73b1db8cce8ea44d45041010ea26a7a6b902f2632f. The recorded digest additionally includes the common padding block, per this registry's convention."]
- **ext:** None

Input A (hex):
```
1f736d69a0368ef67277e5081ad1c198e953a3cdc4cbe577bd05f6a203b2f75fdd18b3e39f563fcacad0a5bb69049fcd4d0dd2a06e2efdc086db19c26fc2e1cf0184949e92cdd31482fb3c1420112000e4930d9b8295ab265500d3a2f30a340226f0aa8790cb1813a9c09c5c5015bc0d53892c5a64e94edb8e60d500013a1932
```
Input B (hex):
```
1f736d69a0368ef67277e5081ad1c198e953a3cdc4cbe577bd05f6a203b2f75fdd18b3e39f563fcacad0a5bb69049fcd4d0dd2a06e2efdc086db19c26fc2e1cf037a8f464c0bb99583033bd41e111fffe4930d9b8295ab265500d3a2f30a340226f0aa8790cb1813a9809e5c4015bc4553892c5a64e94edb8e60d500013a1932
```

### 76. SHA-512 first 29 steps per block, one-block messages (Li et al. 2025)

- **id:** sha512-29-li-et-al
- **t:** SHA-512 first 29 steps per block, one-block messages (Li et al. 2025)
- **lab:** SHA-512, 29 steps, standard IV
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 29 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 29
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 512
- **grp:** 8
- **who:** ["Yingxin Li", "Fukang Liu", "Gaoli Wang", "Haifeng Qian", "Keting Jia", "Xiangyu Kong"]
- **src:** https://iacr.org/submit/files/slides/2025/crypto/crypto2025/144/144_slides.pdf
- **d:** 275bc567e7432dbb0c9348b761bdaddf508606060e5d36ca383640d444b4bbe71b655815b48a11c3d37f4a6976f7a03cda61d303baf7eb484808ca34afc17698
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from Y. Li, F. Liu, G. Wang, H. Qian, K. Jia, X. Kong, \"New Collision Attacks on Round-Reduced SHA-512\", CRYPTO 2025 talk slides hosted by IACR (paper: CRYPTO 2025, DOI 10.1007/978-3-032-01901-1_7). Printed words are 64-bit big-endian, in printed order.", "Standard SHA-512 IV; first 29 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 80-step SHA-512.", "The source prints the chaining value after the single message block, which Atlas reproduces: fc22023fba9ae4af87e29a5cfa5346ad16ba7265981828ca407a30473e590c979d4ce7c9ce70d936f621d63828584973dd1ce5282e8f1f08780750f1be08fabf. The recorded digest additionally includes the common padding block, per this registry's convention.", "Only the IACR-hosted talk slides were reachable; the CRYPTO 2025 proceedings chapter (DOI 10.1007/978-3-032-01901-1_7) is paywalled and was not read, so the table number in the paper is unknown.", "The slide prints the IV explicitly; it is the standard SHA-512 IV."]
- **ext:** None

Input A (hex):
```
36fc57878e6a147839356d4e68533f8111720aae7e5496f3e25446d46d336ce33fbe62e17052367f65eb73407a88f8bbdef9586059b730a872e21b64757e2d0300d43e0b169d0ea77b173317d3029fff85f92000ef60000070cdb9b71952cc8043f82cfa8e26489df0c2a87d655d9c269a8cfbfff7d847ccdaffd76f9b8e668a
```
Input B (hex):
```
36fc57878e6a147839356d4e68533f8111720aae7e5496f3e25446d46d336ce33fbe62e17052367f65eb73407a88f8bbdef9586059b730a872e21b64757e2d0300d43e0b169d0ea780ff41b80fc8200086011fc0f15fffff70cdb9b71952cc8043f82cfa8e26489df0c2a87d655d9c269a4cfa0007d84814daffd76f9b8e668a
```

### 77. SHA-512 first 35 steps per block, two-block messages (Li, Liu, Wang, Shi 2026)

- **id:** sha512-35-li-et-al
- **t:** SHA-512 first 35 steps per block, two-block messages (Li, Liu, Wang, Shi 2026)
- **lab:** SHA-512, 35 steps, standard IV
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 35 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 35
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 512
- **grp:** 8
- **who:** ["Yingxin Li", "Fukang Liu", "Gaoli Wang", "Jiali Shi"]
- **src:** https://eprint.iacr.org/2026/1080.pdf
- **d:** 70795f8807c033036f98cfeed5ab22b54dc660a8c9f92c1c265a6fb9d4d522370e93f7b2b49822e244b92883a8da3dfaa475f9fd01534441d2699836e909efcc
- **ba:** 2048
- **bb:** 2048
- **notes:** ["Transcribed from Pushing the Limit of Memory-efficient Collision Attack Framework for SHA-2 (ePrint 2026/1080, CRYPTO 2026), Table 4. Printed words are big-endian 64-bit, in printed order.", "Standard SHA-512 IV; first 35 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 80-step SHA-512. Common first block M0, then M1 / M1'.", "The source prints the chaining value after the message blocks, which Atlas reproduces: e3c051778d486142428bee20bed09588a3c7439379fda549f7728858582c163be631e7f7fa1819f1f2139d9c35f9253683c7cd3f1a1917eea708fc5646aa9087. The recorded digest additionally includes the common padding block, per this registry's convention."]
- **ext:** None

Input A (hex):
```
6beb0fc6f8eff3a2b49456bcaa89318636acaa4450b7246ead4a3956764275da5adb698dd62486e79c75f643ea4ef25cf2980a1c55495f5a7fb6116784a9d52808158fb6f381160845acde2298893a54d29aa6a38c56f297a8639ecf5d3d949247d507346d25caf7adf36dd973e8826bc637daf1daee990861ccb0377a32ef45407fb97681b9b0941afdd90f2b8ca40f054612e51ce747afe4a40cb66ebf7a1ed1309321eff346b43ac36bbde8a4b8989002c9bb96d874555e7d9e15332aeef6eca644f1b8c8f9d7fa7f118d64cf673be6bf7c3a4c6d30cd5fd65a016bf67839110db279285b171e8b2ae0013e0eb08806353916c1dcf4e7af64f9c23459e344
```
Input B (hex):
```
6beb0fc6f8eff3a2b49456bcaa89318636acaa4450b7246ead4a3956764275da5adb698dd62486e79c75f643ea4ef25cf2980a1c55495f5a7fb6116784a9d52808158fb6f381160845acde2298893a54d29aa6a38c56f297a8639ecf5d3d949247d507346d25caf7adf36dd973e8826bc637daf1daee990861ccb0377a32ef45407fb97681b9b0941afdd90f2b8ca40f054612e51ce747afe4a40cb66ebf7a1ed9309321eff346b43ecb6bbde8a4b8989802c9bb96d874557e2dbe94332aeef6ac8645f1b8c8f9d7fa7f118d64cf673be6bf7c3a4c6d30cd5fd65a016bf678391505b279285b171e832ae0013e0eb08806353916c1dcf4e7af64f9c23459e344
```

### 78. SHA-512/224 first 27 steps per block, one-block messages (Dobraunig, Eichlseder, Mendel 2015)

- **id:** sha512-224-27-dobraunig-et-al
- **t:** SHA-512/224 first 27 steps per block, one-block messages (Dobraunig, Eichlseder, Mendel 2015)
- **lab:** SHA-512/224, 27 steps, standard IV
- **fl:** SHA-512/224
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512-224
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 27 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 27
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 224
- **grp:** 8
- **who:** ["Christoph Dobraunig", "Maria Eichlseder", "Florian Mendel"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-662-48800-3_25.pdf
- **d:** a861ff90fd7493a59258e76f5acbe3d595ae61c7573b13205a535234
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from C. Dobraunig, M. Eichlseder, F. Mendel, \"Analysis of SHA-512/224 and SHA-512/256\", ASIACRYPT 2015, LNCS 9453, pp. 612-630. Printed words are 64-bit big-endian, in printed order.", "Standard SHA-512/224 IV; first 27 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 80-step SHA-512/224.", "The source prints the chaining value after the single message block, which Atlas reproduces: 65b11e66e48da5631b70d12da92e2dba8f338768bb95601b60b995bb. The recorded digest additionally includes the common padding block, per this registry's convention.", "In the Springer PDF the appendix tables are vector drawings, so the digits cannot be extracted as text. The values were read from a 400-dpi rasterisation of the page (pdftoppm) and are confirmed by the redundancy printed in the table itself: m XOR m* equals the printed delta-m for all 16 words (and h0 XOR h0* equals the printed delta-h0 where given), and the recomputed output equals the printed h1.", "IV is the standard SHA-512/224 IV of FIPS 180-4 section 5.3.6.1. The two messages collide on the whole 512-bit chaining value after the message block, not only on the 224 output bits."]
- **ext:** None

Input A (hex):
```
20dbf13a352116a9295506e205afd435abfe4826742c1a1a279f07c7813dd9be47da77c701a9885825aec1349d48650137a992a15616ea31e2b122ecf19e90d32fff6025dc03dd67032c261d740f459e2e2599bd6e7e74dfd490bd22815eb49472fedf1f607df6e387fc91fcfb7397fde647b1b499eee17f2dff8e493cbc8a4c
```
Input B (hex):
```
20dbf13a352116a9295506e205afd435abfe4826742c1a1a279f07c7813dd9be47da77c701a9885825aec1349d48650137a992a15616ea315cc1250cb19e90d3203fdfe5dc03dd66032c261d740f459e2e2599bd6e7e74dfd490bd22815eb494f0bc01167075f6eb87fc91fcfb7397fde647b1b499eee17fd3f8fe713d7c8a4c
```

### 79. SHA-512/256 first 27 steps per block, one-block messages (Dobraunig, Eichlseder, Mendel 2015)

- **id:** sha512-256-27-dobraunig-et-al
- **t:** SHA-512/256 first 27 steps per block, one-block messages (Dobraunig, Eichlseder, Mendel 2015)
- **lab:** SHA-512/256, 27 steps, standard IV
- **fl:** SHA-512/256
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512-256
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 27 of 80 steps, on every block including the padding. Standard starting state. Run all 80 and the two digests differ.
- **r:** 27
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 8
- **who:** ["Christoph Dobraunig", "Maria Eichlseder", "Florian Mendel"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-662-48800-3_25.pdf
- **d:** 680263bb531045c0a97dc6409b5931c923f990f698446a5a24ddb5a42f49fa81
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from C. Dobraunig, M. Eichlseder, F. Mendel, \"Analysis of SHA-512/224 and SHA-512/256\", ASIACRYPT 2015, LNCS 9453, pp. 612-630. Printed words are 64-bit big-endian, in printed order.", "Standard SHA-512/256 IV; first 27 steps on EVERY block including padding, feed-forward preserved. Not a collision for full 80-step SHA-512/256.", "The source prints the chaining value after the single message block, which Atlas reproduces: fcba5c8faf05fd68c676b8f17b5daae36233801174b7fd010ff72ab4a869c54f. The recorded digest additionally includes the common padding block, per this registry's convention.", "In the Springer PDF the appendix tables are vector drawings, so the digits cannot be extracted as text. The values were read from a 400-dpi rasterisation of the page (pdftoppm) and are confirmed by the redundancy printed in the table itself: m XOR m* equals the printed delta-m for all 16 words (and h0 XOR h0* equals the printed delta-h0 where given), and the recomputed output equals the printed h1.", "IV is the standard SHA-512/256 IV of FIPS 180-4 section 5.3.6.2. The two messages collide on the whole 512-bit chaining value after the message block, not only on the 256 output bits."]
- **ext:** None

Input A (hex):
```
306b0c2ebe7c1341c8b55d4df1c5f4feb91a173aeceb818a33b5977f9b46e58b6c6d5a4f87f1364f1b7e33249d4acf4fb7f784ecdcaefc1fa33edafe7afc0452dfc0200932c2b9dffaec7d05e3518e56ec2e19a7ee867396d490bd22815eb49472fedf1f887df303f95891f08483da25c327d0afa2c4f9022c5f0c0806a4e298
```
Input B (hex):
```
306b0c2ebe7c1341c8b55d4df1c5f4feb91a173aeceb818a33b5977f9b46e58b6c6d5a4f87f1364f1b7e33249d4acf4fb7f784ecdcaefc1f1d4edd1e3afc0452d0009fc932c2b9defaec7d05e3518e56ec2e19a7ee867396d490bd22815eb494f0bc01169875f30bf95891f08483da25c327d0afa2c4f902d2587c300764e298
```

### 80. SHA-512 31-step semi-free-start compression collision (Li, Liu, Wang 2024)

- **id:** sha512-sfs-31-li-liu-wang
- **t:** SHA-512 31-step semi-free-start compression collision (Li, Liu, Wang 2024)
- **lab:** SHA-512, 31-step semi-free-start
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 31 of 80 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 31
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 512
- **grp:** 8
- **who:** ["Yingxin Li", "Fukang Liu", "Gaoli Wang"]
- **src:** https://iacr.org/submit/files/slides/2024/eurocrypt/eurocrypt2024/107/slides.pdf
- **d:** 18061dacede7a45d8a673215307a0c75ad7d40871fa4d4a5cb84a2098efd50affe74b9d90faa1325989da85d39d2918738eef206acaca3e0d1fdba4c54da389f
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Chosen IV: e8db5ea7aa921652b99d911402b6f13bd67789b44900bbd36dd99e5934fa4c36022c1b11afc030cd0b5ab5d050736da36624b6d94833584f0377be3bbc9ee6a9", "Transcribed from Y. Li, \"New Records in Collision Attacks on SHA-2\", EUROCRYPT 2024 talk slides hosted by IACR. Printed words are 64-bit big-endian, in printed order.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward; it equals the value printed in the source."]
- **ext:** None

Input A (hex):
```
c84e359a94cfa4158b62e2794d50178acc95cf1218bc494a000000404e2634404b1c2f410a70233a2568946b7b20f0008e82c5955ff61841857f82c3b6494b6cc272b2af2a91b0910a209a722f595461958e7d6a665ca726b82d422e9e59e3e362188a13372b78d500074c63ff27970c0810031ff62c060ac007835890369005
```
Input B (hex):
```
c84e359a94cfa4158b62e2794d50178acc95cf1218bc494a000000404e2634404b1c2f410a70233a0529156e8728c0102ec244995fe6dd3fc57e82cbf80b496d4176aa8f6b93b0910a289a322d595460958e7d6a665ca726b82d422e9e59e3e362188a13372b78d500074c63ff27970c0810031ff62c060ac007835890369005
```

### 81. SHA-512 32-step semi-free-start compression collision (Li, Liu, Wang, Shi 2026)

- **id:** sha512-sfs-32-li-et-al
- **t:** SHA-512 32-step semi-free-start compression collision (Li, Liu, Wang, Shi 2026)
- **lab:** SHA-512, 32-step semi-free-start
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 32 of 80 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 32
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 512
- **grp:** 8
- **who:** ["Yingxin Li", "Fukang Liu", "Gaoli Wang", "Jiali Shi"]
- **src:** https://eprint.iacr.org/2026/1080.pdf
- **d:** 40128a85954b3855aa46f1ce9d1a44323f6801e9835142c2e608c519c1ee136a3613f69145debf3c36388893260abc992c3a3a79643fd8975ec1f48ac8af0f06
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Chosen IV: 72480d1727bbe5cad64e7c162dcb0bf54f7099e73d6f664d4ce991972499a793e06cf6ad9942ff055d58d9ef0a4e4c818838d0f44a2699e085794603c065cbb5", "Transcribed from Pushing the Limit of Memory-efficient Collision Attack Framework for SHA-2 (ePrint 2026/1080, CRYPTO 2026), Table 8. Printed words are big-endian 64-bit, in printed order.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward; it equals the value printed in the source."]
- **ext:** None

Input A (hex):
```
e1b8a9061a16648f40dff5e533aef398c43c8200014433b1280430032018041ca42521357ecabfcaba1a0ab03e0b3bf1100e1e43bdba28f603325e48fc7e760a834a19345a9e1030b4ca1cc9ec2584e601eec3a5189ad2dfd124c0c41bd4e6743eb8e53b200a81175bc2134d6006bf2fbc62f686a000004abe39221a48b401cb
```
Input B (hex):
```
e1b8a9061a16648f40dff5e533aef398843c820001443391280430032018045cade871251f8ac04bb64a0a8f7e0b3af9000e1e03bdba290213531e48fc7e7612830a19345a9e1020b4ca1cc9ec2584e601eec3a5189ad2dfd124c0c41bd4e6743eb8e53b200a81175bc2134d6006bf2fbc62f686a000004abe39221a48b401cb
```

### 82. SHA-512 36-step semi-free-start compression collision (Li, Liu, Wang, Shi 2026)

- **id:** sha512-sfs-36-li-et-al
- **t:** SHA-512 36-step semi-free-start compression collision (Li, Liu, Wang, Shi 2026)
- **lab:** SHA-512, 36-step semi-free-start
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 36 of 80 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 36
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 512
- **grp:** 8
- **who:** ["Yingxin Li", "Fukang Liu", "Gaoli Wang", "Jiali Shi"]
- **src:** https://eprint.iacr.org/2026/1080.pdf
- **d:** 6f8b131dfe2bc008d45206edaf5d93d399437091f745cbd24c06e55b6a5e7099502057a662ac6f243586db5050e4d91f1c698ca99350554ea1cc553f2f844727
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Chosen IV: 8162f2f3c8e928a0f2a702535e24fb57588df0b1dfe519df728c3772ebe543cb8aaae45a3a01bc28e24900d9271b5bd10a8e42fc4d33131c91df55eb45dc517e", "Transcribed from Pushing the Limit of Memory-efficient Collision Attack Framework for SHA-2 (ePrint 2026/1080, CRYPTO 2026), Table 10. Printed words are big-endian 64-bit, in printed order.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward; it equals the value printed in the source.", "One representative per step count: ePrint 2026/1120 prints another 36-step SHA-512 semi-free-start pair, which is not recorded."]
- **ext:** None

Input A (hex):
```
31343156a2fa85fa0cf94ecbdac9b8cb3cc33b7ff887206e0e7c19da088c0352fe9e633c3f8cb67787ce7d4815306d7347e7409c6a9131cd165a7d883df24f195910c2609effb0804aff9e930006ff5f5eeb4ec325a560733479d03efc5830d6d838ca6b356f2d471f6b5be779417fcedf18af0c8cae3d2dda00be73d5849e2e
```
Input B (hex):
```
31343156a2fa85fa0cf94ecbdac9b8cb3cc33b7ff887206e0e7c19da088c0352fe9e633c3f8cb6778fce7d4815306d7343ef409c6a9131cd1e5a7d883df24f197940e2e19effb0800adf9f930006ff5f5eeb4ec325a560733479d03efc5830d6d838ca6b356f2d471b635be779417fced718af0c8cae3d2dda00be73d5849e2e
```

### 83. SHA-512 37-step semi-free-start compression collision (Li, Liu, Wang, Shi 2026)

- **id:** sha512-sfs-37-li-et-al
- **t:** SHA-512 37-step semi-free-start compression collision (Li, Liu, Wang, Shi 2026)
- **lab:** SHA-512, 37-step semi-free-start
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 37 of 80 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 37
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 512
- **grp:** 8
- **who:** ["Yingxin Li", "Fukang Liu", "Gaoli Wang", "Jiali Shi"]
- **src:** https://eprint.iacr.org/2026/1080.pdf
- **d:** 00d282230e77e75a2d4d1729fea961c0d5c2a37158ee21358f34ad01d2bffbb49f77f39828444b738a0370dcb0eca162da5d0ef6eb091c6a1722f104a4e3df82
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Chosen IV: 67819f233e3c01af9d0ec130caee42e6d736534c37058fbfcf111fe6e5b673e41ab625ff4566101441bc862d76bb1dd53a52106a0a1d6bc9c30746bb9f31c39e", "Transcribed from Pushing the Limit of Memory-efficient Collision Attack Framework for SHA-2 (ePrint 2026/1080, CRYPTO 2026), Table 14. Printed words are big-endian 64-bit, in printed order.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward; it equals the value printed in the source.", "One representative per step count: ePrint 2026/1120 prints another 37-step SHA-512 semi-free-start pair, which is not recorded."]
- **ext:** None

Input A (hex):
```
20a4664d0ee2a8065f8c5d2b028e1893c8b35516ff257481c45befebdd02d3c1b52d8a3b4d3a67c34b8c01e57a3f9f7c0396806066988b83c4bf0e1b7c846769993fbaf59899649c8f4ead969c1adb0cbf80f43200a94044a8f66ee7a6e434700358e957c20709f6dd3e3152223155d451960e8064a24e5bfb8bff7d370ed7dc
```
Input B (hex):
```
20a4664d0ee2a8065f8c5d2b028e1893c8b35516ff257481c45befebdd02d3c1b52d8a3b4d3a67c34b8c01e57a3f9f7c2396806066988b83d49f0e1b7c846769b93fbaf59899649c0e0e2f929c1adb0cbf00f03200a94045a8f66ee7a6e434700358e957c20709f6dd3e3152223155d441b60e8064a24e5bdb8bff7d370ed7dc
```

### 84. SHA-512 38-step semi-free-start compression collision (Eichlseder, Mendel, Schläffer 2014)

- **id:** sha512-sfs-38-eichlseder-et-al
- **t:** SHA-512 38-step semi-free-start compression collision (Eichlseder, Mendel, Schläffer 2014)
- **lab:** SHA-512, 38-step semi-free-start
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 38 of 80 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 38
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 512
- **grp:** 8
- **who:** ["Maria Eichlseder", "Florian Mendel", "Martin Schläffer"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-662-46706-0_24.pdf
- **d:** 946a28eedc3b2ff6c4573d0a13ea626811f07b04b06900dd897c606e4053bbe42406aae9d58504b489b237932b061ba8663402cb4bb1972cd99c062dce945423
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Chosen IV: e8626f53a37719642ae427b8c5065790c8fd5a1628fc33370f362d297f82f98789166a0c022ffc40c2c49c30e629239fd1fa8bd692843025ad4bba64c797e6ec", "Transcribed from M. Eichlseder, F. Mendel, M. Schlaeffer, \"Branching Heuristics in Differential Collision Search with Applications to SHA-512\", FSE 2014, LNCS 8540, pp. 473-488. Printed words are 64-bit big-endian, in printed order.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward; it equals the value printed in the source."]
- **ext:** None

Input A (hex):
```
610519a88f0d28093addc83f01c8b17984afa7a2772c6141ad539854e64c9cce85450b73549b20857296b5291f31c0d9fc978d9624e2c2ccfffffffffffffffe92114cb9d2f4cd9b34a3198b79871212cca7f43154e38081ac0598a589168fe1f32ae6a0070a8d2e755aa5cada87e8944b9bd7df3c94b66765291f2b80cc8c51
```
Input B (hex):
```
610519a88f0d28093addc83f01c8b17984afa7a2772c6141ad539854e64c9cce85450b73549b20857296b5291f31c0d9fc978d9624e2c2cc000000000000000192114cb9d2f4cd9c34a3198b79871212cca8143154e38079ac0598a589168fe1f32ae6a0070a8d2e755aa5cada87e8944b9bd7df3c94b66765291f2b80cc8c50
```

### 85. SHA-512 39-step semi-free-start compression collision (Dobraunig, Eichlseder, Mendel 2015)

- **id:** sha512-sfs-39-dobraunig-et-al
- **t:** SHA-512 39-step semi-free-start compression collision (Dobraunig, Eichlseder, Mendel 2015)
- **lab:** SHA-512, 39-step semi-free-start
- **fl:** SHA-512
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 39 of 80 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 39
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 512
- **grp:** 8
- **who:** ["Christoph Dobraunig", "Maria Eichlseder", "Florian Mendel"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-662-48800-3_25.pdf
- **d:** 3aa73bfae7b82789711f2024cf0f636e0c6965f707279a538227fba8617aa955fdd9e2ca8c4d003857db244560d7b70b08ec5698343353c09e9b739ee307ea92
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Chosen IV: eccf3da189dd9668b1ec21a4fd53b8d8609ce4465f772770adf4e7738e2978f68edd237ea50eebc9231b3af0102a926ddb45e613e8d2fd52ad384433420073f6", "Transcribed from C. Dobraunig, M. Eichlseder, F. Mendel, \"Analysis of SHA-512/224 and SHA-512/256\", ASIACRYPT 2015, LNCS 9453, pp. 612-630. Printed words are 64-bit big-endian, in printed order.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value.", "Digest means compression output with feed-forward; it equals the value printed in the source."]
- **ext:** None

Input A (hex):
```
a0ec9872cfffe63cdf5c6a2b59f4c453f2bea3763fc8fa7a6a47e8ff0a995116fa59232e8b6170484c9690984c08449828bee8f5701eab168d57686ecbdce6233879318f901ff78272644b0ca55a61426cb281dab11480b44a8198441f401ff25ffd956ed11a2b5f9a640988d68287d374942df792f2637fb2819dc61f772d4f
```
Input B (hex):
```
a0ec9872cfffe63cdf5c6a2b59f4c453f2bea3763fc8fa7a6a47e8ff0a995116fa59232e8b6170484c9690984c08449828bee8f5701eab168d57686ecbdce6233879318f901ff7a252644b0ca55a61526cb281dab11480944aff9c441f4020736001956ed11a2a5f9a640988d68287d374942df792f2637fb2819dc61f772d4f
```

### 86. SHA-512/224 44-step free-start compression collision (Dobraunig, Eichlseder, Mendel 2015)

- **id:** sha512-224-fs-44-dobraunig-et-al
- **t:** SHA-512/224 44-step free-start compression collision (Dobraunig, Eichlseder, Mendel 2015)
- **lab:** SHA-512/224, 44-step free-start
- **fl:** SHA-512/224
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512-224:compression-free-start
- **iv:** 1
- **cat:** compression function
- **atk:** free-start
- **scope:** One call to the compression function, 44 of 80 steps, no padding, 224-bit output. The attacker picked a different starting state for each input, which is an easier game than sharing one.
- **r:** 44
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 224
- **grp:** 8
- **who:** ["Christoph Dobraunig", "Maria Eichlseder", "Florian Mendel"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-662-48800-3_25.pdf
- **d:** e309edf68f4d89b85c356e0359eb0dab76b4a45ec3c2cd258bd0955d
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Chosen IV for A: fef65b64d3694995959fbfb82ed84eb11d9e855642e62ef2335cc6d027695d91921d197e5cfa2803e26c6eb26163a6929ff3cf4d26f1de785323942861d9139a", "Chosen IV for B: fef65b64d3694995959fbfb82ed84eb11d9e855642e62ef2335cc6d027695db1a712860cdcfa1ff8470749bbf7628f4420cdfd694df672168e07b5fa2c7fedf0", "Transcribed from C. Dobraunig, M. Eichlseder, F. Mendel, \"Analysis of SHA-512/224 and SHA-512/256\", ASIACRYPT 2015, LNCS 9453, pp. 612-630. Printed words are 64-bit big-endian, in printed order.", "Free-start: each input has its OWN attacker-chosen chaining value, one unpadded block each. This is weaker than a semi-free-start collision and far from a hash collision.", "The collision is on the 224-bit output SHA-512/224 defines: the leftmost 224 bits of the compression output after feed-forward, which equal the value printed in the source. The two full 512-bit outputs differ, and the paper is explicit that the result relies on the truncation."]
- **ext:** None

Input A (hex):
```
7a19df6089d0068403ed2a0d0c29e00e36c91e35f681fbb8bb2b47428aeff294dce94ccc981d39a344230f73cf56d9efe9d46b26b44950c8550bed4b9419741c58a98894206e00def3448a6f761d384d9ae59f3a3bcc5bbaece85d5c77be431b6e3cf817e9376cc7b74a2a43c0b96c937c5b51d6fe2a0c265a9868e5bf2e422d
```
Input B (hex):
```
5e031bbe28b2d027ded424ef85255cc3ad2f514be0830c1fa635dab40aeffa9fdce94ccc981d398344230f73cf56d9efe9d46b26b44950c8550bed4b9419741c58a98894206e00def3448a6f761d384d9ae59f3a3bcc5bbaece85d5c77be431b6e3cf817e9376cc7b74a2a43c0b96cb35c5b51d6fe2a0c365a9868e5bf2e420d
```

### 87. SHA-512/256 43-step free-start compression collision (Dobraunig, Eichlseder, Mendel 2015)

- **id:** sha512-256-fs-43-dobraunig-et-al
- **t:** SHA-512/256 43-step free-start compression collision (Dobraunig, Eichlseder, Mendel 2015)
- **lab:** SHA-512/256, 43-step free-start
- **fl:** SHA-512/256
- **g:** sha512
- **gl:** SHA-512 family
- **sub:** sha512-256:compression-free-start
- **iv:** 1
- **cat:** compression function
- **atk:** free-start
- **scope:** One call to the compression function, 43 of 80 steps, no padding, 256-bit output. The attacker picked a different starting state for each input, which is an easier game than sharing one.
- **r:** 43
- **sr:** 0
- **tot:** 80
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 8
- **who:** ["Christoph Dobraunig", "Maria Eichlseder", "Florian Mendel"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-662-48800-3_25.pdf
- **d:** 1d7041bbbffa676a03d8c440d9246b9d20ce2d17c5b0b2c47e6e4d33a7f54afd
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Chosen IV for A: 159b52516f10f30d546b2042f240afeef25339b24c441edfd62c698666558242e5a9e39861fbd81dd2138eacc20d5224a332c16df23609fb73f78341dfd7a4e5", "Chosen IV for B: 159b52516f10f30d546b2042f240afeef25339b24c441edfd62c698666558242e5a9e39861fbd83d72e259ce420d5a0f4db37906cc361264ae579d9e0275b446", "Transcribed from C. Dobraunig, M. Eichlseder, F. Mendel, \"Analysis of SHA-512/224 and SHA-512/256\", ASIACRYPT 2015, LNCS 9453, pp. 612-630. Printed words are 64-bit big-endian, in printed order.", "Free-start: each input has its OWN attacker-chosen chaining value, one unpadded block each. This is weaker than a semi-free-start collision and far from a hash collision.", "The collision is on the 256-bit output SHA-512/256 defines: the leftmost 256 bits of the compression output after feed-forward, which equal the value printed in the source. The two full 512-bit outputs differ, and the paper is explicit that the result relies on the truncation."]
- **ext:** None

Input A (hex):
```
cfbec86f1cf6821edd3343c25aad835a2a08612b753f3d6bb328d40d2c624ef7b3e51f8a3a63bd6f4abdf96375bbf609a8c5c1f784672e86a78e2aa625830d4b169dcb5039bf3d9ffbcc43ffebd8ae471b3eaefccf5c6a46f668a2a728851b4e374601ea44422bdb2ca290d26a23a02f6685babbfdcb5e22e000111457201fd4
```
Input B (hex):
```
ee37d77210586a56b2a4122800ad72cf89399609f53f3560b328d40d2c624ed7b3e51f8a3a63bd6f4abdf96375bbf609a8c5c1f784672e86a78e2aa625830d4b169dcb5039bf3d9ffbcc43ffebd8ae471b3eaefccf5c6a46f668a2a728851b4e374601ea44422bfb0ca290d26a23a03f6685babbfdcb5e02e07e151457202055
```

### 88. SM3 first 22 steps per block, two-block messages (Yuan, Cui, Yu 2026)

- **id:** sm3-22-yuan-cui-yu
- **t:** SM3 first 22 steps per block, two-block messages (Yuan, Cui, Yu 2026)
- **lab:** SM3, 22 steps, standard IV
- **fl:** SM3
- **g:** sm3
- **gl:** SM3
- **sub:** sm3
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 22 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 22
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Sitong Yuan", "Haorui Cui", "Hongbo Yu"]
- **src:** https://eprint.iacr.org/2026/2700.pdf
- **d:** 8e27c766e25ad61a5b14d7e9caff9c2c053bca5f6358742331e0a12a81d7fd2f
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from Table 3 of Practical Collision Attacks on 22- and 23-Step SM3 (Preliminary Version) (ePrint 2026/2700): common first block M0, then M1 / M1'. Printed words are big-endian, in printed order.", "Standard SM3 IV; first 22 of 64 steps on EVERY block including padding, XOR feed-forward preserved. Not a collision for full SM3; as a two-block hash the pair collides at exactly 22 steps.", "The paper prints the chaining values after the first and second block; Atlas reproduces both (after the second block: a26aee58365c46728d23941da3717024562fdafe0055237a944e020d4ed48936). Unlike the 2013 20-step example, the printed first block does lead to the printed chaining value. The recorded digest additionally includes the common padding block.", "Unreviewed preprint at the time of import; the pair itself is checked here by computation."]
- **ext:** None

Input A (hex):
```
a96c16880cf030f560c52a29a03e9f022804250cf71ac77424bb8b84279e110bdab4cf9a308e4398413c2caf0ae6ea73b19a981ce588610760d39901cccce42b6b648c6884476675e033ccc8e6caecb3d9538ca9c1e4eb997fff17875537458291079596c540139a1283f8ce11af479e205c2abde326d25d4231e15e5c1f901d
```
Input B (hex):
```
a96c16880cf030f560c52a29a03e9f022804250cf71ac77424bb8b84279e110bdab4cf9a308e4398413c2caf0ae6ea73b19a981ce588610760d39901cccce42b6b6c886c24a74715e033ccc8e6c0ecb1d9538cabc1e4eb997fff17875135478291079596c540139a1289f8cc11af479e205c2abde326d25d4231e15e5c1f901d
```

### 89. SM3 first 23 steps per block, two-block messages (Yuan, Cui, Yu 2026)

- **id:** sm3-23-yuan-cui-yu
- **t:** SM3 first 23 steps per block, two-block messages (Yuan, Cui, Yu 2026)
- **lab:** SM3, 23 steps, standard IV
- **fl:** SM3
- **g:** sm3
- **gl:** SM3
- **sub:** sm3
- **iv:** 0
- **cat:** reduced-round hash
- **atk:** 
- **scope:** Only the first 23 of 64 steps, on every block including the padding. Standard starting state. Run all 64 and the two digests differ.
- **r:** 23
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 4
- **who:** ["Sitong Yuan", "Haorui Cui", "Hongbo Yu"]
- **src:** https://eprint.iacr.org/2026/2700.pdf
- **d:** e0887dd76257cc4a0ccb04880601d4fe92ee2c899d8803c092766e285987f2c4
- **ba:** 1024
- **bb:** 1024
- **notes:** ["Transcribed from Table 4 of Practical Collision Attacks on 22- and 23-Step SM3 (Preliminary Version) (ePrint 2026/2700): common first block M0, then M1 / M1'. Printed words are big-endian, in printed order.", "Standard SM3 IV; first 23 of 64 steps on EVERY block including padding, XOR feed-forward preserved. Not a collision for full SM3; as a two-block hash the pair collides at exactly 23 steps.", "The paper prints the chaining values after the first and second block; Atlas reproduces both (after the second block: 07edcc347c75d378891e8f39bb671548193513a7ed1181deaa0e4108e3e11f7c). Unlike the 2013 20-step example, the printed first block does lead to the printed chaining value. The recorded digest additionally includes the common padding block.", "Unreviewed preprint at the time of import; the pair itself is checked here by computation."]
- **ext:** None

Input A (hex):
```
d22c8eaac24b03cb24ab41ee16ad81fe7cfa713259a23ec783b181f6ffa99d5fc462d07445255fb8abe00fff9467cef697468c9282f3ead151dfcf08117d41fa106421972a406151ea4b13c2816d75eeb33d73a6eeaf5e1ab0b5d9c053391648db9d640707ab3e7f97780cca49df85deef9d7e78a2450cd01b424dbc5f5f855e
```
Input B (hex):
```
d22c8eaac24b03cb24ab41ee16ad81fe7cfa713259a23ec783b181f6ffa99d5fc462d07445255fb8abe00fff9467cef697468c9282f3ead151dfcf08117d41fa106421972b406350b2632bca816d75eeb3bd7126ee2f5e1ab0b5d9c0533916485b9c648707ab3e7f97780cca495f875eef9d7e78a2450cd01b424dbc5f5f855e
```

### 90. SM3 24-step free-start compression collision (Mendel, Nad, Schläffer 2013)

- **id:** sm3-fs-24-mendel-nad-schlaffer
- **t:** SM3 24-step free-start compression collision (Mendel, Nad, Schläffer 2013)
- **lab:** SM3, 24-step free-start
- **fl:** SM3
- **g:** sm3
- **gl:** SM3
- **sub:** sm3:compression-free-start
- **iv:** 1
- **cat:** compression function
- **atk:** free-start
- **scope:** One call to the compression function, 24 of 64 steps, no padding, 256-bit output. The attacker picked a different starting state for each input, which is an easier game than sharing one.
- **r:** 24
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Florian Mendel", "Tomislav Nad", "Martin Schläffer"]
- **src:** https://pure.tugraz.at/ws/portalfiles/portal/80044228/sm3.pdf
- **d:** a83d45dc9eda869d48baa71878ccd02625696682d0be9f4ae70babf3f4852e70
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV for A: 898991b08de476686e54847c9167ff5e3c7d51fee21013016c53d5227b3809df", "Chosen IV for B: 898991b08da47668ee54847c1127ff5e3c7d51fee2100301ec53d522fb3819df", "Transcribed from the authors' copy of Finding Collisions for Round-Reduced SM3 (CT-RSA 2013) hosted by TU Graz; the paywalled version of record was not compared. Printed words are big-endian, in printed order.", "Free-start: each input has its OWN attacker-chosen chaining value, one unpadded block each; both the chaining value and the block differ. This is weaker than a semi-free-start collision and far from a hash collision.", "First 24 of 64 steps with the unmodified message expansion and XOR feed-forward. The pair collides at exactly 24 steps and at no other step count. Digest means compression output with feed-forward; it equals the h1 printed in the paper."]
- **ext:** None

Input A (hex):
```
07595c54e01e0245facd449a07ca096d510445e84e1d0dff97f2a3c079f02f142ebfac5048cdde2de88f68e12b5032d13aa9a79f656d1380693417c1ce82a62a
```
Input B (hex):
```
07595c54e01e02457acd449a07ca096d510445e84e1d0dff97f2a3c079f02f142ebfac5048cdde2de88f68e12b5032d13aa9a79f656d1380693417c1ce82a62a
```

### 91. SM3 20-step semi-free-start compression collision (second block of Mendel, Nad, Schläffer 2013)

- **id:** sm3-sfs-20-mendel-nad-schlaffer
- **t:** SM3 20-step semi-free-start compression collision (second block of Mendel, Nad, Schläffer 2013)
- **lab:** SM3, 20-step semi-free-start
- **fl:** SM3
- **g:** sm3
- **gl:** SM3
- **sub:** sm3:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 20 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 20
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Florian Mendel", "Tomislav Nad", "Martin Schläffer"]
- **src:** https://pure.tugraz.at/ws/portalfiles/portal/80044228/sm3.pdf
- **d:** b2033829677c16d2a6de9db9fd898668a9119d20476364d6a0838adc08d3833d
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 5e801aac4b8c7a46c8f346463b2420c197e775aee3a6c39983a05d406a257995", "Transcribed from the authors' copy of Finding Collisions for Round-Reduced SM3 (CT-RSA 2013) hosted by TU Graz; the paywalled version of record was not compared. Printed words are big-endian, in printed order.", "NOT a standard-IV hash collision as recorded here: one unpadded block with a common chaining value. Digest means compression output with feed-forward; it equals the h2 printed in the paper.", "Source discrepancy: the paper presents this as a two-block HASH collision for 20-step SM3 from the standard IV (first block m0 leading to chaining value h1, then m1 / m1*). Atlas reproduces the second block only. The printed first block 03c98f41a8bda164709a299cd76610eb26b351ac535470248efdff597e8184004188b7f1954faf0ea32f99846e5d8975dc3b528a973480e4f6be9d9bcf07f13e does not map the standard IV to the printed h1 under any reading tried (every step count, with and without feed-forward, byte-swapped and reordered words), so the hash-level claim is not admitted and the printed h1 is recorded as a chosen chaining value."]
- **ext:** None

Input A (hex):
```
559654cd8d4f9e948ca64e4ab85d989c8c185880b51caad103eca739be66a265ca21ab719c3410282c043967d4617038bf6744cad8772f12a58e12c035f4f9f2
```
Input B (hex):
```
559654cd8d1f9e848ca64e5ab85d989c8c185880950cbad103eca739be66a265ca71ab619c3410282c043967d4617038bf6744cad8772f12a58e12c035f4f9f2
```

### 92. SM3 24-step semi-free-start compression collision (Yuan, Cui, Yu 2026)

- **id:** sm3-sfs-24-yuan-cui-yu
- **t:** SM3 24-step semi-free-start compression collision (Yuan, Cui, Yu 2026)
- **lab:** SM3, 24-step semi-free-start
- **fl:** SM3
- **g:** sm3
- **gl:** SM3
- **sub:** sm3:compression-sfs
- **iv:** 1
- **cat:** compression function
- **atk:** semi-free-start
- **scope:** One call to the compression function, 24 of 64 steps, no padding. The attacker picked the starting state, and both inputs share it.
- **r:** 24
- **sr:** 0
- **tot:** 64
- **unit:** steps
- **full:** False
- **status:** Chosen starting state
- **statusNote:** This example is a compression-function collision, not a full hash collision.
- **out:** 256
- **grp:** 4
- **who:** ["Sitong Yuan", "Haorui Cui", "Hongbo Yu"]
- **src:** https://eprint.iacr.org/2026/2700.pdf
- **d:** 3f0c60cf278c38b4b4e0c7bf163ccd524e0f56e5f91b12b560d90a47122a7264
- **ba:** 512
- **bb:** 512
- **notes:** ["Chosen IV: 8f0b515b7d683d59d9ad89a721be1c4640139fa1f8cd729b1a49249f9fa2566b", "Transcribed from Table 5 of Practical Collision Attacks on 22- and 23-Step SM3 (Preliminary Version) (ePrint 2026/2700). Printed words are big-endian, in printed order.", "NOT a standard-IV hash collision: one unpadded block with an attacker-chosen common chaining value, first 24 of 64 steps. Compare sm3-fs-24-mendel-nad-schlaffer, which needs two different chaining values.", "Digest means compression output with feed-forward; it equals the value printed in the paper.", "Unreviewed preprint at the time of import; the pair itself is checked here by computation."]
- **ext:** None

Input A (hex):
```
cf839763e498bdd8d0fda5e3d61fdebbae941f307c97b227913763048004e999737a67782649bcff2923c18634699b5c5281d54a967640930f188746ccd7929a
```
Input B (hex):
```
c783bf63e498bdd8d0ffa4e2fe27d6e3ae941f30fc953227113763048004e999737a677827493c7f2923c18634699b5cd283554a967640930f188746ccd7929a
```

### 93. Keccak-224 4-round collision (Dinur, Dunkelman, Shamir 2012)

- **id:** keccak-224-r4-dinur-dunkelman-shamir
- **t:** Keccak-224 4-round collision (Dinur, Dunkelman, Shamir 2012)
- **lab:** Keccak-224, 4 rounds
- **fl:** Keccak-224
- **g:** sponge
- **gl:** SHA-3 and Keccak
- **sub:** keccak-224
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** Keccak-224 cut down to its first 4 of 24 rounds. Capacity 448, 224-bit output, the old Keccak padding with no SHA-3 suffix.
- **r:** 4
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 224
- **grp:** 8
- **who:** ["Itai Dinur", "Orr Dunkelman", "Adi Shamir"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-642-34047-5_25.pdf
- **d:** dc106b82e1e47006da0c515ba86a87abed5705b5fb327926e8384daa
- **ba:** 1144
- **bb:** 1144
- **notes:** ["Printed as 32-bit words, \"each block given in hexadecimal using the little-endian format\": the reading that works is that each 8-digit group is the numeral of a little-endian 32-bit word, i.e. the message bytes are the group's bytes reversed. The other reading (groups as bytes in printed order) was tried and rejected: it parses as padded blocks of 1150 and 1149 message bits that do not collide. The source prints the PADDED 1152-bit block; its last byte is 0x81, so each message is the first 1144 bits (143 bytes), one rate block.", "Output compared: the full 224-bit digest; it equals the \"Output=\" printed in the paper.", "Side observation, not claimed by the source: the same pair also collides on 3-round Keccak-224 (digest 03decabc55b14715f4f62b70387d0130276050873b31fe9382734b61).", "Legacy Keccak padding (no SHA-3 \"01\" suffix): this is Keccak-224, not SHA3-224."]
- **ext:** None

Input A (hex):
```
69acc7fa04be102782c36284f91bbf7a30cd65d0b8de64db30cd10149bd737c8b746e42255bde9314c07b2a6cc326ec80aa150de58aabaf788bc6cd9f675bd9f5a730d5e63a62ad2aa74a5169286b07d29b08a55304d9b10ca5dce86c795a2134bd9c9e7d2948764f83cee6237934369159fab8c67327cacbe1cf49093680ea2241f78b44776a30ba0679af2d028f6
```
Input B (hex):
```
81bc5fcecc0f7147e0922c46cfd2f548c36e2ff9e1643e05b980075754ec38f89f80748f6facb4664318dd70c5f034bf9ac81050481179d83e07ccd5bcae3932798df47d7b76c70e041608fbb975a9af0faeeff8733479ed1c939e47740af8f28fd0927127abb55e4ec0caf12d2394f32a6b6548441647a30ae674db183bfb05c327dc4153bf84833e4c5332b5001c
```

### 94. Keccak-224 5-round collision (Song, Liao, Guo 2017)

- **id:** keccak-224-r5-song-liao-guo
- **t:** Keccak-224 5-round collision (Song, Liao, Guo 2017)
- **lab:** Keccak-224, 5 rounds
- **fl:** Keccak-224
- **g:** sponge
- **gl:** SHA-3 and Keccak
- **sub:** keccak-224
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** Keccak-224 cut down to its first 5 of 24 rounds. Capacity 448, 224-bit output, the old Keccak padding with no SHA-3 suffix.
- **r:** 5
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 224
- **grp:** 8
- **who:** ["Ling Song", "Guohong Liao", "Jian Guo"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-319-63715-0_15.pdf
- **d:** 1b7257d5aad9789f89a05f8ea833a68d9d2d15b9143640976f491f0e
- **ba:** 1150
- **bb:** 1150
- **notes:** ["Printed as 64-bit lanes in row-major order (lane index x+5y, left to right, top to bottom); each 16-digit group is the numeral of the lane, i.e. state bytes are the group's bytes reversed. Reading groups as bytes in printed order gives an invalid padding. The table gives the PADDED 1152-bit block. Lane 17 ends with bits 1,1 (pad10*1 with no zeros), so each message is 1150 bits long: NOT byte-aligned (143 bytes + 6 bits). One rate block.", "Output compared: the full 224-bit digest; it equals the digest printed in the table (the last printed group 0E1F496F is the low 32 bits of lane 3).", "Legacy Keccak padding (no SHA-3 \"01\" suffix): this is Keccak-224, not SHA3-224.", "Table 6 is vector graphics in the Springer PDF (pdftotext extracts nothing). It was transcribed by hand from 600-dpi pdftoppm renderings; the transcription is confirmed by the collision itself and by equality with the printed digest."]
- **ext:** None

Input A (hex):
```
c0b2cbe0f0789af4375e9f3fc1f67c996c02ca68aef21e09abd211d389617a786e4760b06a7810f4bddd75911b346ea5fddef707c98193edf449f4d15795f4eac6d30e2fc2c0fdbbae0a963632e3fca5ed75b2e0a5982519aea454f563437cda1b0d04a31545b185c3437edc7d5c5e2c774fbb51523800a95014571e200e53db2f15783a7981c9a90f9c3863ac915905
```
Input B (hex):
```
cb8e9c018e7916c3ea2b32c616f5fd2eb2b226a63284feb9c28456af5808ea4ef0efe18b9bdc9317708a2383b691f7ddb37d765f4f483ee4dc51fdd163ade56a2072f61ac209c5576c4e9cf053d014af0f904399ba94e54401d185c2435799f29a450215ca55c0006bb7ffe09ed23a01ff6a9550776a9b8a3f99382ebda900d24dd8f4daf03b5854ff6f55c671427829
```

### 95. Keccak-256 4-round collision (Dinur, Dunkelman, Shamir 2012)

- **id:** keccak-256-r4-dinur-dunkelman-shamir
- **t:** Keccak-256 4-round collision (Dinur, Dunkelman, Shamir 2012)
- **lab:** Keccak-256, 4 rounds
- **fl:** Keccak-256
- **g:** sponge
- **gl:** SHA-3 and Keccak
- **sub:** keccak-256
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** Keccak-256 cut down to its first 4 of 24 rounds. Capacity 512, 256-bit output, the old Keccak padding with no SHA-3 suffix.
- **r:** 4
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 8
- **who:** ["Itai Dinur", "Orr Dunkelman", "Adi Shamir"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-642-34047-5_25.pdf
- **d:** 9118fb61d5b626f3df94dd24844927731d9ada05b959d33f3b39b8780b99e7f2
- **ba:** 1080
- **bb:** 1080
- **notes:** ["Printed as 32-bit words, \"each block given in hexadecimal using the little-endian format\": the reading that works is that each 8-digit group is the numeral of a little-endian 32-bit word, i.e. the message bytes are the group's bytes reversed. The other reading (groups as bytes in printed order) was tried and rejected: the block then does not end with a 1 bit, so it is not a padded block. The source prints the PADDED 1088-bit block; its last byte is 0x81 (pad10*1), so each message is the first 1080 bits (135 bytes), one rate block.", "Output compared: the full 256-bit digest; it equals the \"Output=\" printed in the paper.", "Legacy Keccak padding (no SHA-3 \"01\" suffix): this is Keccak-256 (the Ethereum hash function, reduced to 4 rounds), not SHA3-256."]
- **ext:** None

Input A (hex):
```
321cf3c46dae594cf4f0195d4be4c425323085d8f2125e8de26e6ebb1e3bc3275810096cd50290eb6fa0a43bf1c70c4a515eb5cc83d90d8d43080a2bb0d3219b75906753d2de6d52444829482cedf46f152cce1ac71d1c47688509d439f6ebf157b2f7ea87aefd09e678886830eb7548802dc3c9cb6f9e3cfabc2a3c7b80a4e6b881b22ab33223
```
Input B (hex):
```
f70ed3a4698fbb80df48c090b91372eb240465a63ef6653a8188268c1fb851b63cfadaaac3a52ceec2ea78db79e7eac8359c2f4487e221325a7a01b312077990dc8b1c1ba8108be0ca259d9aacaae71b9c3e2f4ead7d71735a016655b9cf98a1c2a81c5a8a34e3a0b10b6caee4f98039918bfaa489a9816eaabca989f1f12be19595ef30458b2e
```

### 96. Keccak-384 3-round collision (Dinur, Dunkelman, Shamir 2013)

- **id:** keccak-384-r3-dinur-dunkelman-shamir
- **t:** Keccak-384 3-round collision (Dinur, Dunkelman, Shamir 2013)
- **lab:** Keccak-384, 3 rounds
- **fl:** Keccak-384
- **g:** sponge
- **gl:** SHA-3 and Keccak
- **sub:** keccak-384
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** Keccak-384 cut down to its first 3 of 24 rounds. Capacity 768, 384-bit output, the old Keccak padding with no SHA-3 suffix.
- **r:** 3
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 384
- **grp:** 8
- **who:** ["Itai Dinur", "Orr Dunkelman", "Adi Shamir"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-662-43933-3_12.pdf
- **d:** 919999999999191144c44044dc605c40000000001000100cf77776776777f77397f550355571d5556466666666666666
- **ba:** 830
- **bb:** 830
- **notes:** ["Printed as 32-bit words, \"each block given in hexadecimal using the little-endian format\": the reading that works is that each 8-digit group is the numeral of a little-endian 32-bit word, i.e. the message bytes are the group's bytes reversed. The other reading (groups as bytes in printed order) was tried and rejected: it also parses as 830-bit messages, but they do not collide. The source prints the PADDED 832-bit block. Its last two bits are 1,1, so each message is 830 bits long: NOT byte-aligned (103 bytes + 6 bits). One rate block.", "Output compared: the full 384-bit digest; it equals the \"Output=\" printed in the paper.", "Legacy Keccak padding (no SHA-3 \"01\" suffix): this is Keccak-384, not SHA3-384."]
- **ext:** None

Input A (hex):
```
ffffffffffff7fffbbbbbbbbbbbbfbbb4444444444444444ffffffffffffffff9999999999999999444444444444c44444444444444444444444644444444444aaaaaaaaaaaaaaaa66666666666666664444444444444444dddddddddddd9dddddddfddddddddd1d
```
Input B (hex):
```
333333333333b3335555555555551555aaaaaaaaaaaaaaaa77777777777777774444444444444444666666666666e666eeeeeeeeeeeeeeee1111311111111111ccccccccccccccccffffffffffffffff1111111111111111999999999999d999ddddfddddddddd1d
```

### 97. Keccak-512 3-round collision (Dinur, Dunkelman, Shamir 2013)

- **id:** keccak-512-r3-dinur-dunkelman-shamir
- **t:** Keccak-512 3-round collision (Dinur, Dunkelman, Shamir 2013)
- **lab:** Keccak-512, 3 rounds
- **fl:** Keccak-512
- **g:** sponge
- **gl:** SHA-3 and Keccak
- **sub:** keccak-512
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** Keccak-512 cut down to its first 3 of 24 rounds. Capacity 1024, 512-bit output, the old Keccak padding with no SHA-3 suffix.
- **r:** 3
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 512
- **grp:** 8
- **who:** ["Itai Dinur", "Orr Dunkelman", "Adi Shamir"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-662-43933-3_12.pdf
- **d:** 4bc9bc56445644c4515465d75565d95d3273fa71230ba33bc5088495647640641454804101091911baa8ba6afaaeaba8eeaef87edc68ceececacc84ecc5c5ddd
- **ba:** 574
- **bb:** 574
- **notes:** ["Printed as 32-bit words, \"each block given in hexadecimal using the little-endian format\": the reading that works is that each 8-digit group is the numeral of a little-endian 32-bit word, i.e. the message bytes are the group's bytes reversed. For this pair every word is byte-symmetric, so the message bytes do not depend on the byte order; the printed digest does, and only the reversed reading matches it.", "The source prints the PADDED 576-bit block. Its last two bits are 1,1 (pad10*1 with no zeros), so each message is 574 bits long: NOT byte-aligned (71 bytes + 6 bits; last byte 0x0c). One rate block.", "Output compared: the full 512-bit digest; it equals the \"Output=\" printed in the paper.", "Legacy Keccak padding (no SHA-3 \"01\" suffix): this is Keccak-512, not SHA3-512."]
- **ext:** None

Input A (hex):
```
88888888888888886666666666666666aaaaaaaaaaaaaaaa7777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb11111111111111118888888888888888cccccccccccccc0c
```
Input B (hex):
```
aaaaaaaaaaaaaaaa8888888888888888eeeeeeeeeeeeeeee9999999999999999999999999999999999999999999999998888888888888888cccccccccccccccccccccccccccccc0c
```

### 98. SHAKE128 5-round collision on a 256-bit output (Qiao, Song, Liu, Guo 2017)

- **id:** shake128-r5-qiao-song-liu-guo
- **t:** SHAKE128 5-round collision on a 256-bit output (Qiao, Song, Liu, Guo 2017)
- **lab:** SHAKE128, 5 rounds
- **fl:** SHAKE128
- **g:** sponge
- **gl:** SHA-3 and Keccak
- **sub:** shake128
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** SHAKE128 cut down to its first 5 of 24 rounds. Capacity 256, 256-bit output, the SHAKE suffix.
- **r:** 5
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 8
- **who:** ["Kexin Qiao", "Ling Song", "Meicheng Liu", "Jian Guo"]
- **src:** https://link.springer.com/content/pdf/10.1007/978-3-319-56617-7_8.pdf
- **d:** 39a9c6d73a952e9def16608aa6596f32d7001737eeaf1ea7769b8d095d3d463c
- **ba:** 1338
- **bb:** 1338
- **notes:** ["Printed as 64-bit lanes in row-major order (lane index x+5y, left to right, top to bottom); each 16-digit group is the numeral of the lane, i.e. state bytes are the group's bytes reversed. Reading groups as bytes in printed order gives an invalid padding. The table gives the PADDED 1344-bit block M||1111||10*1 (the paper: \"We use M to denote the padded message for SHAKE as well\"). Lane 20 ends with bits ...,1,1,1,1,1,1 = suffix 1111 then pad 11, so each message is 1338 bits long: NOT byte-aligned (167 bytes + 2 bits). One rate block.", "Output length: the paper fixes the SHAKE128 digest at 256 bits (\"we presume the digest sizes are 256 and 512 for SHAKE128 and SHAKE256\") and the collision is claimed for that length. Atlas measured: the two outputs agree on bits 0..309 and first differ at bit 310, so the pair collides for any output length up to 310 bits (38 whole bytes) and NOT for longer SHAKE128 outputs.", "Table 11 is vector graphics in the Springer PDF (pdftotext extracts nothing). It was transcribed by hand from 500-dpi pdftoppm renderings; the transcription is confirmed by the collision itself and by equality with the digest printed in the same table.", "The SHAKE \"1111\" suffix is applied; first 5 of 24 rounds at every permutation call. Not a collision for full SHAKE128."]
- **ext:** None

Input A (hex):
```
a00421e6eb443e0abc0fe852c317861e2f96694311389ab6ab5d04a8eef537124c04224ec64a14d42ecbfc793da94012fccfba0c833ac6c8249871e1c0346bb3806658c5ec0348f9ad9c8329fe33f1aca7fade60f2885fca03aba482e8e72f97541a4312be4413d13bf968aeeb884481d3ae1f25f00cd1569f2df5c5fc65a677cc8a12ab9ff60ed59408746e81f1f387b0349248554d0d773d3a3f24b1347173408e3df2e72a0e02
```
Input B (hex):
```
cad78b5ad2d5dd0cd8a445e49e251df7459d1cd577f184eb244c0250fcc1700a634f023f6e0908710e15e9c5eb1e8d3b754e8219fbc9dceaadba9746b77ca9b8d13a0664cde28859a4e4e285311255fb8614ca3340f74fe76bafbd416b015f9142a3efc9aa41541426c6e615cf09a6d90aee5d8ff5c409568786ba438c174eabe4abf2781db0743794456671d3e335aaa76930f750ad6ea228e9f8a0f8254eded871834fe31b4302
```

### 99. SHA3-224 5-round collision (Guo et al. 2019)

- **id:** sha3-224-r5-guo-et-al
- **t:** SHA3-224 5-round collision (Guo et al. 2019)
- **lab:** SHA3-224, 5 rounds
- **fl:** SHA3-224
- **g:** sponge
- **gl:** SHA-3 and Keccak
- **sub:** sha3-224
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** SHA3-224 cut down to its first 5 of 24 rounds. Capacity 448, 224-bit output, the SHA-3 suffix.
- **r:** 5
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 224
- **grp:** 8
- **who:** ["Jian Guo", "Guohong Liao", "Guozhen Liu", "Meicheng Liu", "Kexin Qiao", "Ling Song"]
- **src:** https://eprint.iacr.org/2019/147.pdf
- **d:** 293463b649e7d879b1f0a70f0f840680d4d00b11cfccf94f94ad35fb
- **ba:** 1148
- **bb:** 1148
- **notes:** ["Printed as a 5x5 array of 64-bit lanes in row-major order (lane index x+5y), \"each lane is denoted in hexadecimal using little-endian format\": the reading that works is that each 16-digit group is the numeral of the lane, i.e. the state bytes are the group's bytes reversed. The other reading (groups as bytes in printed order) was tried and rejected: at least one of the two blocks is then not a validly padded block (it does not end with a 1 bit, or the domain suffix is missing). The table gives the PADDED block (the paper: \"M-bar: Padded message of M. Note that M-bar is of one block in our attacks\"; \"setting the last 4 bits of the padded message\" for SHA3-d). All 25 lanes are printed; lanes 18..24 (capacity) are zero. Lane 17 ends with bits 0,1,1,1 = SHA-3 suffix 01 followed by pad 11, so each message is 1148 bits long: NOT byte-aligned (143 bytes + 4 bits). One rate block.", "Output compared: the full 224-bit digest; it equals the digest printed in the table (the last printed group FB35AD94 is the low 32 bits of lane 3).", "This is SHA3-224 proper (domain bits 0,1). The same padded blocks read with no suffix are 1150-bit Keccak-224 messages and collide too; the source does not claim that."]
- **ext:** None

Input A (hex):
```
222c3577b01b65ba77a7476fc878080238f5374eb70688a68f95518715e114fc0407e47d324a36383b9a9b25d72049f2cb65cfa42d60e098966edcc82933cda006b1ff7bba0d0508741faa293dae743b5c9e4aba06062ec7ee058d5a0c3ee8e7bcabee855609e27805495b6b00d74a1156029549f49cfd2f17698dc8ae68b1ea24c4b8d46f014c2939090b2fffcd950a
```
Input B (hex):
```
909d1254d4253edf98d3f524b28b3a740c59a169fd363a802c3b3c5161cce926f9abcb822e7f775285be314f8f31d80e4a51958d28cc55aedecc05b3e35270e50de47adc2b42c63cbb035e7b2260d5f44c0207f40f4e8fa8701c8af564f7024151e32e2efc68d868a756a4f95bd54e55d66e514a77bed9bc0601f72c8f4ec7c10173587e2c3ac9daf6a568ad744d2904
```

### 100. SHA3-256 5-round collision (Guo et al. 2019)

- **id:** sha3-256-r5-guo-et-al
- **t:** SHA3-256 5-round collision (Guo et al. 2019)
- **lab:** SHA3-256, 5 rounds
- **fl:** SHA3-256
- **g:** sponge
- **gl:** SHA-3 and Keccak
- **sub:** sha3-256
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** SHA3-256 cut down to its first 5 of 24 rounds. Capacity 512, 256-bit output, the SHA-3 suffix.
- **r:** 5
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 256
- **grp:** 8
- **who:** ["Jian Guo", "Guohong Liao", "Guozhen Liu", "Meicheng Liu", "Kexin Qiao", "Ling Song"]
- **src:** https://eprint.iacr.org/2019/147.pdf
- **d:** b440608b2e7c0165d64b3b93bbf84f340320be6833f1a3c6cb5a43334b7b42ab
- **ba:** 1084
- **bb:** 1084
- **notes:** ["Printed as a 5x5 array of 64-bit lanes in row-major order (lane index x+5y), \"each lane is denoted in hexadecimal using little-endian format\": the reading that works is that each 16-digit group is the numeral of the lane, i.e. the state bytes are the group's bytes reversed. The other reading (groups as bytes in printed order) was tried and rejected: at least one of the two blocks is then not a validly padded block (it does not end with a 1 bit, or the domain suffix is missing). The table gives the PADDED block. All 25 lanes are printed; lanes 17..24 (capacity) are zero. Lane 16 ends with bits 0,1,1,1 = SHA-3 suffix 01 followed by pad 11, so each message is 1084 bits long: NOT byte-aligned (135 bytes + 4 bits). One rate block.", "Output compared: the full 256-bit digest; it equals the digest printed in the table.", "This is SHA3-256 proper (domain bits 0,1). The same padded blocks read with no suffix are 1086-bit Keccak-256 messages and collide too; the source does not claim that."]
- **ext:** None

Input A (hex):
```
1a023f2dbd67cafe4f772b4c4aa610bdc71fd22df86feff86487a764d9a44b6f6ebc242ac9d14f0f8840c6110a8c4bfba8505fc0ebb9a7ed5bebf1e708dd710ab5bfa878aed24253e97c2eccb0a99165dcf64e7f82dda352e40db86283b1899df7ff5b87a119a7fe47d1b7d75ab9a2490a26b92eb78437b259fd9572d0ef7a18ff099def6663800e
```
Input B (hex):
```
172d2c845070f9160a48435a93ee31a7e9cbd7db6b358e6d8a15fa6f350b2cd6c8f8c7808096ad4fabc51bc6e1b8837c0593e2b522ca3f7e40c848e8dbd488588a7bf7ce1ce26d23600e0789f59ed569e1ccc6f22bcd7fe8bc3ad91f828be2b15cb40c86b16f5dadd5755901d1c78fab23cc96ee37b7c62447a4657995b5bfd34f259f26f5d3310e
```

### 101. SHAKE256 4-round collision on a 512-bit output (Tu et al. 2026)

- **id:** shake256-r4-tu-et-al
- **t:** SHAKE256 4-round collision on a 512-bit output (Tu et al. 2026)
- **lab:** SHAKE256, 4 rounds
- **fl:** SHAKE256
- **g:** sponge
- **gl:** SHA-3 and Keccak
- **sub:** shake256
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** SHAKE256 cut down to its first 4 of 24 rounds. Capacity 512, 512-bit output, the SHAKE suffix.
- **r:** 4
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 512
- **grp:** 8
- **who:** ["Yi Tu", "Ling Song", "Huaijin Wu", "Jian Guo", "Jian Weng", "Chaoping Xing"]
- **src:** https://eprint.iacr.org/2026/2107.pdf
- **d:** 18ceaae5dbff3144488f1b3aba64b0cf43c48fb48ecbf88b7e9b2f67d9ba8e68ecf036e3278195c75d9909a686c658d12cd93cd2bb1c139c48070d3dccedcc5b
- **ba:** 1082
- **bb:** 1082
- **notes:** ["Printed as a 5x5 array of 64-bit lanes in row-major order (lane index x+5y), \"each lane is denoted in hexadecimal using little-endian format\": the reading that works is that each 16-digit group is the numeral of the lane, i.e. the state bytes are the group's bytes reversed. The other reading (groups as bytes in printed order) was tried and rejected: at least one of the two blocks is then not a validly padded block (it does not end with a 1 bit, or the domain suffix is missing). The table gives the PADDED block and prints only the 17 rate lanes (rows of 5,5,5,2). Lane 16 ends with bits 1,1,1,1,1,1 = SHAKE suffix 1111 followed by pad 11, so each message is 1082 bits long: NOT byte-aligned (135 bytes + 2 bits). One rate block.", "Output length: the source claims a collision on \"the full 512-bit digest\" (lanes 0-7 after the last round). 512 bits equals the capacity. Atlas measured over 2176 output bits: the two outputs agree on bits 0..556 and first differ at bit 557, so the pair collides for any output length up to 557 bits and NOT for longer SHAKE256 outputs. The 512-bit digest printed in the table (8 lanes) equals the recomputed output of both messages.", "The same padded blocks read with no suffix are 1086-bit Keccak-256 messages and collide on the 256-bit digest; the source does not claim that. They are NOT SHA3-256 messages: the bits before the padding are 1,1, not the SHA-3 suffix 0,1.", "Recent preprint (received 2026-09-19), not peer reviewed as far as the PDF shows; the collision itself is checked here by computation."]
- **ext:** None

Input A (hex):
```
8bf455ee0d1ce042cdd81105cf1f710f26925cef99fda9d94b1feee598cfcf5ca7bd70f1c3ca121164ad625f634ee62b7c60c5a65b52d3c0d837351a49288aa77a3b3560a6db0cb75e144874273e7c6ed77328111432494cb34e24c9ef1c5518c2759029edde54e6505d5de26f613c6e30fa6505be196f7cb416d44078149947d57de22669957d01
```
Input B (hex):
```
ec631f89138be0c2c3d88948715a71af13935c58f651a1d94c2de7e5e87fced65c66a65757cf52f9fd38c89362ce8cec7060398639e41b371836c5ae0fa982eefa113560d309dcb7326850d523aa3d6e8fe47a233b9f4914ba066ffd9b54857b0b744052ede2f07936e17ae20fd73d7ef95abbbeba593cff62811e0a78c4bb95dd7d90050b06cc00
```

### 102. SHAKE256 5-round collision on a 512-bit output (Tu et al. 2026)

- **id:** shake256-r5-tu-et-al
- **t:** SHAKE256 5-round collision on a 512-bit output (Tu et al. 2026)
- **lab:** SHAKE256, 5 rounds
- **fl:** SHAKE256
- **g:** sponge
- **gl:** SHA-3 and Keccak
- **sub:** shake256
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** SHAKE256 cut down to its first 5 of 24 rounds. Capacity 512, 512-bit output, the SHAKE suffix.
- **r:** 5
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Reduced rounds only
- **statusNote:** These inputs do not collide under the full hash function.
- **out:** 512
- **grp:** 8
- **who:** ["Yi Tu", "Ling Song", "Huaijin Wu", "Jian Guo", "Jian Weng", "Chaoping Xing"]
- **src:** https://eprint.iacr.org/2026/2107.pdf
- **d:** 087a0a441ce6e64c2d29818aa2903e3a30edc5a1f11e74fe883bb5398293818d90cc80b207ceb20f266f7d23717bca21810ab771df4b250a1c551aad12a190fa
- **ba:** 1082
- **bb:** 1082
- **notes:** ["Printed as a 5x5 array of 64-bit lanes in row-major order (lane index x+5y), \"each lane is denoted in hexadecimal using little-endian format\": the reading that works is that each 16-digit group is the numeral of the lane, i.e. the state bytes are the group's bytes reversed. The other reading (groups as bytes in printed order) was tried and rejected: at least one of the two blocks is then not a validly padded block (it does not end with a 1 bit, or the domain suffix is missing). The table gives the PADDED block and prints only the 17 rate lanes (rows of 5,5,5,2). Lane 16 ends with bits 1,1,1,1,1,1 = SHAKE suffix 1111 followed by pad 11, so each message is 1082 bits long: NOT byte-aligned (135 bytes + 2 bits). One rate block.", "Output length: the source claims a collision on \"the full 512-bit digest\" (lanes 0-7 after the last round). 512 bits equals the capacity. Atlas measured over 2176 output bits: the two outputs agree on bits 0..556 and first differ at bit 557, so the pair collides for any output length up to 557 bits and NOT for longer SHAKE256 outputs. The 512-bit digest printed in the table (8 lanes) equals the recomputed output of both messages.", "The same padded blocks read with no suffix are 1086-bit Keccak-256 messages and collide on the 256-bit digest; the source does not claim that. They are NOT SHA3-256 messages: the bits before the padding are 1,1, not the SHA-3 suffix 0,1.", "Recent preprint (received 2026-09-19), not peer reviewed as far as the PDF shows; the collision itself is checked here by computation."]
- **ext:** None

Input A (hex):
```
22d7329d86db19ead013c351e74b468422285e1b3c9dd9e80c849a42a1546649c42645673e1a09d548e3dbe67211e6da4f7c62666f165245905e667a22a533c359108f7b6440a9169148a4407738598729a2c1ef0293103efa803ab039df13532b48314cd132665f81a7fa00e127a4543771a6d69945af42731be268a16687e36b63bb7b6df71803
```
Input B (hex):
```
755b03f92417b112b458cad9a59aa06cc5d4920a093eb3e12bff3e7101ec140b3b4049133091895736fde3faf01676ad45e6f3544fe79b07928eaa07c380b5dbb267def8bc994e5508ef874b468074061e85c90e0e8d95b6d01e100638a2688c7b3e94bfa9197202a0e59b8b4a10a6e53b25cbe728614f671f91b9e4f558217cb4612840c9266202
```

### 103. Keccak Crunchy, width 200, 1 round

- **id:** keccak-crunchy-w200-r1-cd50d08de5
- **t:** Keccak Crunchy, width 200, 1 round
- **lab:** width 200, 1 round
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 200
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[200], first round of 18, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 1
- **sr:** 0
- **tot:** 18
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 1
- **who:** ["Roman Walch", "Maria Eichlseder"]
- **src:** https://keccak.team/crunchy_mails/coll-r1-w200-20170922.txt
- **d:** 3ca3fd181bb4eed409615fa718b3edc2297eef0f
- **ba:** 72
- **bb:** 32
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
0000000000baadc011
```
Input B (hex):
```
bbadc011
```

### 104. Keccak Crunchy, width 200, 2 rounds

- **id:** keccak-crunchy-w200-r2-182b8bcdeb
- **t:** Keccak Crunchy, width 200, 2 rounds
- **lab:** width 200, 2 rounds
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 200
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[200], round indices 3 to 4 of 18, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 2
- **sr:** 3
- **tot:** 18
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 1
- **who:** ["Andreas Westfeld"]
- **src:** https://keccak.team/crunchy_mails/coll-r2-w200-20230104.txt
- **d:** 58157e79deb478350ac16e3b21aed11d7eb7cff8
- **ba:** 48
- **bb:** 8
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
000000000000
```
Input B (hex):
```
8b
```

### 105. Keccak Crunchy, width 400, 1 round

- **id:** keccak-crunchy-w400-r1-13cd23eb2b
- **t:** Keccak Crunchy, width 400, 1 round
- **lab:** width 400, 1 round
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 400
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[400], first round of 20, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 1
- **sr:** 0
- **tot:** 20
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 2
- **who:** ["Tim Rademacher (Lexmark International, Inc.)"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** 7a905d80188725a69352f958fbd07f61d89ca42e
- **ba:** 208
- **bb:** 208
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
029d9379db288fd65f8dfd9a846d00001df68a7f907200006ba4
```
Input B (hex):
```
5b1578e1c65b8fd6d134c77c846d0000683a8a7fc9fa00006ba4
```

### 106. Keccak Crunchy, width 400, 1 round

- **id:** keccak-crunchy-w400-r1-61e3b1ef61
- **t:** Keccak Crunchy, width 400, 1 round
- **lab:** width 400, 1 round
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 400
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[400], first round of 20, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 1
- **sr:** 0
- **tot:** 20
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 2
- **who:** ["Paweł Morawiecki (Kielce Univeristy of Commerce, Section of Informatics, Poland)"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** 3f00430000007e00010000000100002021202000
- **ba:** 236
- **bb:** 236
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
7f08380100000000039036053801000010020200410c2004000000000000
```
Input B (hex):
```
ed2b3801202300009381764338010000908e0200d32f211d000000000000
```

### 107. Keccak Crunchy, width 400, 2 rounds

- **id:** keccak-crunchy-w400-r2-4ec007bd2c
- **t:** Keccak Crunchy, width 400, 2 rounds
- **lab:** width 400, 2 rounds
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 400
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[400], first 2 rounds of 20, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 2
- **sr:** 0
- **tot:** 20
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 2
- **who:** ["Paweł Morawiecki (Kielce Univeristy of Commerce, Section of Informatics, Poland)"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** 6611aa734813a85b7860f3012ace3018484397cc
- **ba:** 236
- **bb:** 236
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
54d66595645991a1091832b89de5a112ad05f24c0612f9e1d357ec5c3e02
```
Input B (hex):
```
0b1d96e4646a465fd99d3ec1e688375fcd12553c7cb44d58a18e79a26206
```

### 108. Keccak Crunchy, width 400, 4 rounds

- **id:** keccak-crunchy-w400-r4-4be83ecfaa
- **t:** Keccak Crunchy, width 400, 4 rounds
- **lab:** width 400, 4 rounds
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 400
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[400], first 4 rounds of 20, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 4
- **sr:** 0
- **tot:** 20
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 2
- **who:** ["Stefan Kölbl, Florian Mendel, Martin Schläffer and Tomislav Nad"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** 864d6647bcd85391374083da442499569abea51d
- **ba:** 238
- **bb:** 238
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
fda3351012b27ebce614eafa6ab6f86fb051e61f763c69e92045e9c16015
```
Input B (hex):
```
bc455e6053be8e1f6435b52b37420e3e45a03f3c68e2dae26e72aaed201a
```

### 109. Keccak Crunchy, width 400, 5 rounds

- **id:** keccak-crunchy-w400-r5-9bb14c5c52
- **t:** Keccak Crunchy, width 400, 5 rounds
- **lab:** width 400, 5 rounds
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 400
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[400], first 5 rounds of 20, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 5
- **sr:** 0
- **tot:** 20
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 2
- **who:** ["Stefan Kölbl"]
- **src:** https://keccak.team/crunchy_mails/coll-r5-w400-20261031.txt
- **d:** a1d8aa50c1dd562bef55cb015a8874c49d6ded13
- **ba:** 712
- **bb:** 712
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
292e9afc912a1ca1a8120275ef277ff547a6502f48e4d83d7575cf0d30e148edb39f2207a6d7b63560d3c5b4c36d94b0fda01854277af67db12aee600000000000000000000000000000000000000000000000000000000000
```
Input B (hex):
```
292e9afc912a1ca1a8120275ef277ff547a6502f48e4d83d7575cf0d30e11ec5787b62a4acca0c23e40dfb567d6a243537559208a75db4ddb82274810018401840184080008008000000082000000020800080020004000284
```

### 110. Keccak Crunchy, width 800, 1 round

- **id:** keccak-crunchy-w800-r1-c00e5eb841
- **t:** Keccak Crunchy, width 800, 1 round
- **lab:** width 800, 1 round
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 800
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[800], first round of 22, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 1
- **sr:** 0
- **tot:** 22
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 4
- **who:** ["Tim Rademacher (Lexmark International, Inc.)"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** 3f419f881c42cffc5fd72174ec376698fc9ec6f9
- **ba:** 192
- **bb:** 192
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
ae69beb7ed587456d5646cde6336cddf0b84e91212e9a120
```
Input B (hex):
```
65b5a3eb6c0462f545af0eea2318460ec3e1d808f9a27914
```

### 111. Keccak Crunchy, width 800, 1 round

- **id:** keccak-crunchy-w800-r1-e094bc040a
- **t:** Keccak Crunchy, width 800, 1 round
- **lab:** width 800, 1 round
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 800
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[800], first round of 22, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 1
- **sr:** 0
- **tot:** 22
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 4
- **who:** ["Paweł Morawiecki (Kielce Univeristy of Commerce, Section of Informatics, Poland)"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** 0102000000000200000000000002020000000000
- **ba:** 636
- **bb:** 636
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
8702000043000080420000000800801000002090870200000000000000000000080080000000200000000000000000004300008000000000000000000000000000000000010000800000001000000000
```
Input B (hex):
```
0002008000000040000000000000001000000090000200800000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000400000001000000000
```

### 112. Keccak Crunchy, width 800, 2 rounds

- **id:** keccak-crunchy-w800-r2-64e9209903
- **t:** Keccak Crunchy, width 800, 2 rounds
- **lab:** width 800, 2 rounds
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 800
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[800], first 2 rounds of 22, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 2
- **sr:** 0
- **tot:** 22
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 4
- **who:** ["Paweł Morawiecki (Kielce Univeristy of Commerce, Section of Informatics, Poland)"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** 5e3372c39d66b54afc84ce85648742c1f2ca03ea
- **ba:** 636
- **bb:** 636
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
bb909de74598f22f87850097cd81dc6f89b75d9b5e088f8f1b2ad6d0be5c6b63df402d2b6a3c7d037738303d6020664acead493a2b62b3076802e61f8b015219368279d0ef840a410b69ded080b85006
```
Input B (hex):
```
44f9628bc191ac570cae73026ae77a5451e1bc73b2f18d81cf535bb43ce197cc10e04c62d60d4f27ead9d9d8d141582c79aec3827472128b72b5660ec6aaf4af76e0eb21c0fe7db186d9a45add98830f
```

### 113. Keccak Crunchy, width 800, 4 rounds

- **id:** keccak-crunchy-w800-r4-f1a9e48953
- **t:** Keccak Crunchy, width 800, 4 rounds
- **lab:** width 800, 4 rounds
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 800
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[800], first 4 rounds of 22, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 4
- **sr:** 0
- **tot:** 22
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 4
- **who:** ["Stefan Kölbl, Florian Mendel, Martin Schläffer and Tomislav Nad"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** b112361d0b59a194baa637591c8dc6cf67e750a6
- **ba:** 638
- **bb:** 638
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
9281804a7178b0c6f43ce4725da5d8385bb38059244d7041f4b7ae63fa6dde072958235a5929cf2923a62caa89f4bda1bc2cbae7914330e2197fef4f3cb5ff5ecf2f9b8d1c853a7141d9271750c0a80a
```
Input B (hex):
```
5c8c4764f2bb208a28c11fc6a5093ef3675a08906b0d19de1a2ae66730025205215c6f32f5f93e16404b41dc6b78de61f4a3326613e71db7d0d82f84a680a6cd35b600d80a91e0446bb655077888281b
```

### 114. Keccak Crunchy, width 800, 5 rounds

- **id:** keccak-crunchy-w800-r5-9cda2f0586
- **t:** Keccak Crunchy, width 800, 5 rounds
- **lab:** width 800, 5 rounds
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 800
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[800], first 5 rounds of 22, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 5
- **sr:** 0
- **tot:** 22
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 4
- **who:** ["Kexin Qiao, Ling Song, Meicheng Liu and Jian Guo"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** ba5a0bf92d683074628c6685adb0e16635ac52b0
- **ba:** 636
- **bb:** 638
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
3fb77d296db45fceabd5ef63b2db75abe719010273779206a4a645a6f8e3e6686224281583ab3a63fba5c796b5be4c5e964c6192da4796dd4f09b0d46f37684c5137b6d356ab8662527a57de0fea0300
```
Input B (hex):
```
cb0b155bfcf2f3c0a5b50759c36d7322c5f04c91637d478749a675a66fa9be8be38aeb52412d4019c34cfbd930d69f6671fcc9d8548555574af66206c5b5b46456bf127ff0dbea2b107b20f68797fd32
```

### 115. Keccak Crunchy, width 1600, 1 round

- **id:** keccak-crunchy-w1600-r1-01d9c8e7bd
- **t:** Keccak Crunchy, width 1600, 1 round
- **lab:** width 1600, 1 round
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 1600
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[1600], first round of 24, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 1
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 8
- **who:** ["Alexandre Duc (Ecole Polytechnique Federale de Lausanne, Switzerland), Jian Guo (Institute for Infocomm Research, Singapore), Thomas Peyrin and Lei Wei (Nanyang Technological University, Singapore)"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** 0d5af965e55a45a7dbcbfcb8b37c4347a7707662
- **ba:** 2872
- **bb:** 2872
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
dde547b07dc648dd00dd58a202641f49ce16b5b1e4d2129de33714fc93d27970b8c1203587681287456a2947ce48909d5e454e431861e0fb98f5f72bc7719c7f32bcb4b925c6406a3169b2ffb2429c1088eb53a04c349be429930ff004ab70366824ef8deb2ff71c98a91b4aecb85b74a3ae14efe2afd30b42e2fc468e6c7cf6906b837b9a7a973324b37d106bd8840e8798fd6947d0758ab271d040dd4d366db8b9e953348086583303689edcecac6384a9cccb7941552cb2266c8f73a3fd2b5ce67e906604e89a185038e43ce547c08e138c0855e1340707a0977a4394a6a07a2430e029197a3169b315a6985c66266ff22ec4d462ccdb03635646f7fce6712017514930cc7a917f8f3f17eba63d5b986c1f6cceeb48d14e9e18459affb6ba15080445d47edf530e1e6af9c4a754551374c9e25f11b3aeafcbf349caaa04dfa20825868605d99422438ee7eae244fe560de0b61f9364ce5f571829011c08b3242d39aa31123f
```
Input B (hex):
```
dde547b07dc648dd00dd58a202641f49ce16b5b1e4d2129de33714fc93d27970b8c1203587681287456a2947ce48909d5e454e431861e0fb98f5f72bc7719c7f32bcb4b925c6406a3169b2ffb2429c1088eb53a04c349be429930ff004ab70366824ef8deb2ff71c98a91b4aecb85b74a3ae14efe2afd30b42e2fc468e6c7cf6906b837b9a7a973324b37d106bd8840e8798fd6947d0758ab271d040dd4d366db8b9e953348086583303689edcecac6384a9cccb7941552cb2266c8f73a3fd2b5ce67e906604e89a085038e43ce547c08e138c0855e1340707a0977a4394a6a07a2430e029197a3169b315a6985c66266ff22ec4d462ccdb03635646f7fce6712017514930cc7a997f8f3f17eba63d5b986c1f6cceeb48d14e9e18459afeb6ba15080445d47edf530e1e6af9c4a7545d1374c9e25f11b3aeafcbf349caaa04dfb20825868604d99422438ee7eae244fe560de0b61f9364ce5f571829011c08b3242d39aa31123f
```

### 116. Keccak Crunchy, width 1600, 1 round

- **id:** keccak-crunchy-w1600-r1-344d81064f
- **t:** Keccak Crunchy, width 1600, 1 round
- **lab:** width 1600, 1 round
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 1600
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[1600], first round of 24, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 1
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 8
- **who:** ["Paweł Morawiecki (Kielce Univeristy of Commerce, Section of Informatics, Poland)"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** 0002002000000000100000000000000000000000
- **ba:** 1436
- **bb:** 1436
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
010200200000020000000000000001000008000000000800000000400000000000008000000000000102002000000200000000000000000000000000000008000000000000000000000080000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000008000000000000000000000000008001000000000000000000080000000000000000000000000000080000000000000000000000000000000
```
Input B (hex):
```
000200200000000004000000000000800000000000000000000000000000000001000000000000000002002000000000040000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000009000000000000000000000000000000000000000000000000000000000000000000000008002000000
```

### 117. Keccak Crunchy, width 1600, 1 round

- **id:** keccak-crunchy-w1600-r1-684d94bee7
- **t:** Keccak Crunchy, width 1600, 1 round
- **lab:** width 1600, 1 round
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 1600
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[1600], first round of 24, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 1
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 8
- **who:** ["Tim Rademacher (Lexmark International, Inc.)"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** 0f0af7074b6abd486f80dd4af734102b1439ca2b
- **ba:** 384
- **bb:** 384
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
5e1e360f4c02c5773513c59fffd672b76a586273f430250f1839059efe545bd629276b16f0cd9501b51610e3658ef746
```
Input B (hex):
```
da4978d56a0231edc89490f19f180b1795e8a87e38092abbe6fa2fa9ceb36706567f8e10165192dbce20cb22dbfd1db4
```

### 118. Keccak Crunchy, width 1600, 2 rounds

- **id:** keccak-crunchy-w1600-r2-108455a6ea
- **t:** Keccak Crunchy, width 1600, 2 rounds
- **lab:** width 1600, 2 rounds
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 1600
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[1600], first 2 rounds of 24, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 2
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 8
- **who:** ["Paweł Morawiecki (Kielce Univeristy of Commerce, Section of Informatics, Poland)"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** 41e43607a98ebdabe789dd0ae32ad3ebb649a7bc
- **ba:** 1436
- **bb:** 1436
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
438185f9b16225b99b6a0632feee98b1600234e5d5ffe743a755e69fa1e0704c7126f429300a6a813e8e4729d89220a835adb9c0800acb7156e6a58db24338444dc488c4f34b18158b7a54800c0f1414a369b4f2c8b070ac1c2a61baf63569bde36c804fc8948b8fb4770081e1ca7ed7bb828df1a534c8259f432e20f094138dd1ef454821101375d09815010f021cc17ce7cf95a3c926cc1fddaf4419001296d4a7062511907713a340591c019160cf0341800a
```
Input B (hex):
```
ecd63374777f80b53e23f60408aefc00ec6b35934b9bcb59fde80be93cb181d5a066a46675fc550347286483fe8d5b7964b67b8089b6e872141e858f6ab780634f0462428e83dc3e6921b4d7d00cae599ff986eff4b5513a08296ebcb55779c1abb25eae0cbe77b38bde0f368591a712f25cff5762444ab18731b398ca530298bffbe8bf4f961e213a5b7ab4cb462463bc7934e9e9bb63c5193568be95555d827d52dafef8417d60b2ed9ccfa5ba1c45ae4c7001
```

### 119. Keccak Crunchy, width 1600, 2 rounds

- **id:** keccak-crunchy-w1600-r2-18eceb4d89
- **t:** Keccak Crunchy, width 1600, 2 rounds
- **lab:** width 1600, 2 rounds
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 1600
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[1600], first 2 rounds of 24, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 2
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 8
- **who:** ["Alexandre Duc (Ecole Polytechnique Federale de Lausanne, Switzerland), Jian Guo (Institute for Infocomm Research, Singapore), Thomas Peyrin and Lei Wei (Nanyang Technological University, Singapore)"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** ec08e495bbd8d86588f343702ef40c45dc6f0b39
- **ba:** 2872
- **bb:** 2872
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
90a9686330a2231ca504b43e477dc835d98de1b56299c8280c37f0b594bac624632f8793d1aaaf76ae63b4f5e17c2aba090c706ca53894b1708566043f2c28a35baf362c59e6a3084957fd2ad428e5dd345549d98dde8afd63f001a21c294578d87ca43262473aab9f37d6735fbb5093109a6c9d78f69bdbe69c7d03c6c37b9e3f1fd0a1670a4c06422279a1ddc935ed63a18bdb9826b67ec2348188f7fc27361cf7d783022389444602e523cb1a112fbc9c0a54c2c1d284f5540dec503422682bf9ef2d1c7871627a5786467197752d337f81f541547935a88621f8ba4365e63c541359cd85bb47dc418d4dd8027b0b82fc00c2507af8f80019f1bb5d56a199aab4f27739aebf15ef4c63c84fded3d5dad4932b4e8b234ea51409006aaa9b155f8e8c983c4bae2b9811f3e7efc7b8c99b4bf4e9d718377c2c417e97eb19ac4aa738e3e184910f1ca2020391c8bb5a64064f4ddd67855993c6d72ab1f1d6fc980fdf7c93708baf
```
Input B (hex):
```
90a9686330a2231ca504b43e477dc835d98de1b56299c8280c37f0b594bac624632f8793d1aaaf76ae63b4f5e17c2aba090c706ca53894b1708566043f2c28a35baf362c59e6a3084957fd2ad428e5dd345549d98dde8afd63f001a21c294578d87ca43262473aab9f37d6735fbb5093109a6c9d78f69bdbe69c7d03c6c37b9e3f1fd0a1670a4c06422279a1ddc935ed63a18bdb9826b67ec2348188f7fc27361cf7d783022389444602e523cb1a112fbc9c0a54c2c1d284f5540dec5034226c2bf9ef2d1c7871627a5786467197752d337f81f540547935a88621f8ba4365e63c541359cd85bb47dc418d4dd8027b0b82fc00c2507af8f80019f1bb5d56a199aab4f27739aebf15ef4c63c84fded3d1dad4932b4e8b234ea51409026aaa9b155f8e8c983c4bae2b9811f3e7efc7b8c99b4bf4e9d718377c2c417e97eb19ac4aa738e3e384910f1ca2020391c9bb5a64064f4ddd67855993c6d72ab1f1d6fc980fdf7c93708baf
```

### 120. Keccak Crunchy, width 1600, 3 rounds

- **id:** keccak-crunchy-w1600-r3-9b2d1ac722
- **t:** Keccak Crunchy, width 1600, 3 rounds
- **lab:** width 1600, 3 rounds
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 1600
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[1600], first 3 rounds of 24, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 3
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 8
- **who:** ["Itai Dinur, Orr Dunkelman and Adi Shamir"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** 3864a738f596d629ac502017eed97128d7a58a83
- **ba:** 1432
- **bb:** 1432
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
ff4a2526e9c66d01f6b74e6972c56364c0c10c8e4c7152b8e52886e0906779c9dadde455799ae3ca3513a01150a78f66fdb4c3e57768227e4444024736101105958f3f3225539924e1fded81d26a97da68734c49fef1e77d417a12abcfb67723722bcb151411f551e403066f69c01c684710051d516d77288917a1dc19c89c33c35d7b7e958bd638d3d6aa86eb304c11161084c1aca9b0a2475a0fbc927f3e7037c81fd9474e5f514df814bf6780c847332baa
```
Input B (hex):
```
6bf0e3ac5b501758d35d5b8ad96b11d108bce44a8e3f06673c5f053e15f987a8ee211fba2b7fad1d537003bd62a69fca083d157ca6958680c07daf192307aabde0af7547f2ad455d772e3c488761d34bed55c312afdc66fa01d0fcafc87d1c3b3d2a712cc434b2f8375e7c2671f7b984df0139d0b46c38975c1a52059945622cc7938d62a55fb92f7f1d79bbbf4de33136036f66f931e33041f8469031d5d74131884f6031186bf627bc32abdb7430655ca9c3
```

### 121. Keccak Crunchy, width 1600, 4 rounds

- **id:** keccak-crunchy-w1600-r4-9b2d1ac722
- **t:** Keccak Crunchy, width 1600, 4 rounds
- **lab:** width 1600, 4 rounds
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 1600
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[1600], first 4 rounds of 24, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 4
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 8
- **who:** ["Itai Dinur, Orr Dunkelman and Adi Shamir"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** 7f46a674e254f96cfd556561ea2d412cc84088d9
- **ba:** 1432
- **bb:** 1432
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
ff4a2526e9c66d01f6b74e6972c56364c0c10c8e4c7152b8e52886e0906779c9dadde455799ae3ca3513a01150a78f66fdb4c3e57768227e4444024736101105958f3f3225539924e1fded81d26a97da68734c49fef1e77d417a12abcfb67723722bcb151411f551e403066f69c01c684710051d516d77288917a1dc19c89c33c35d7b7e958bd638d3d6aa86eb304c11161084c1aca9b0a2475a0fbc927f3e7037c81fd9474e5f514df814bf6780c847332baa
```
Input B (hex):
```
6bf0e3ac5b501758d35d5b8ad96b11d108bce44a8e3f06673c5f053e15f987a8ee211fba2b7fad1d537003bd62a69fca083d157ca6958680c07daf192307aabde0af7547f2ad455d772e3c488761d34bed55c312afdc66fa01d0fcafc87d1c3b3d2a712cc434b2f8375e7c2671f7b984df0139d0b46c38975c1a52059945622cc7938d62a55fb92f7f1d79bbbf4de33136036f66f931e33041f8469031d5d74131884f6031186bf627bc32abdb7430655ca9c3
```

### 122. Keccak Crunchy, width 1600, 5 rounds

- **id:** keccak-crunchy-w1600-r5-bb0299bbfe
- **t:** Keccak Crunchy, width 1600, 5 rounds
- **lab:** width 1600, 5 rounds
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 1600
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[1600], first 5 rounds of 24, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 5
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 8
- **who:** ["Kexin Qiao, Ling Song, Meicheng Liu and Jian Guo"]
- **src:** https://raw.githubusercontent.com/KeccakTeam/KeccakTools/3473478bf9c10bf95879cd8960c7409fee313162/Sources/KeccakCrunchyContest.cpp
- **d:** a69da1ee0f0f0833c43ff4d41bfa80a8d7e236a1
- **ba:** 1438
- **bb:** 1436
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately.", "The 2016 email prints digest a69da1ee0f0f0833c43ff4d41bfa80a81da0dfac, which differs in its last 32 bits from the recomputed value. The two exact-bit-length messages still collide; Atlas records the recomputed digest, not the conflicting printed string."]
- **ext:** None

Input A (hex):
```
40e797ea27e9338052959a80b9e7e936cc5b37fb6ccdc9ba54e1d6d6e6683b0e315c0dfdb3235afae0766cba0763e4e74c82f0a85c519dd209e0a52e475f6d0dedb843093ffc0c8042edd5f3bb7ae3d203a794565d1e0665371f10f16ff76ee8f8c9934c0a0b18f99c2acb3c949f984cc2a4ae620a1d74d120fff0192a18ee481cef9ad56cea8858726b00a5b399ee41e848704bdcc8d1fc568a72f228b9c403a6d51cd404e35355f9ae7f5c02927f1ddea15823
```
Input B (hex):
```
acfcac2a24ee6d36dd0dca37b72dcdf1517ad569db44e9458bf35521d6bd99ef160dc01e58917eea7d038922b34604346dc0df93aca5ea86db26c9f48b6b68cf405836adeb3f4fe0c348c3b4ca0fa2d27b9930477b47c34d5786d29a97d289f5ac03d911cc4f4639d0ea8bea1c7d45dd5ab9bc6e5764aed5cfe360d9db7be2a07a6cf1ff0b530a5b2f4ddb4c91c1e017dc8859255c519576ccdb30fa629fc3029d68392c23d508bd1e2cdc2d3eefb966c41b310a
```

### 123. Keccak Crunchy, width 1600, 6 rounds

- **id:** keccak-crunchy-w1600-r6-6f1c74a128
- **t:** Keccak Crunchy, width 1600, 6 rounds
- **lab:** width 1600, 6 rounds
- **fl:** Keccak Crunchy
- **g:** kec
- **gl:** Keccak Crunchy
- **sub:** 1600
- **iv:** 0
- **cat:** reduced-round sponge
- **atk:** 
- **scope:** A contest puzzle: Keccak-f[1600], first 6 rounds of 24, capacity 160, 160-bit output. Not SHA-3 and not Keccak-256.
- **r:** 6
- **sr:** 0
- **tot:** 24
- **unit:** rounds
- **full:** False
- **status:** Contest variant
- **statusNote:** Nonstandard Keccak parameters. This does not break SHA-3 or Keccak-256.
- **out:** 160
- **grp:** 8
- **who:** ["Ling Song", "Guohong Liao", "Jian Guo"]
- **src:** https://keccak.team/crunchy_mails/coll-r6-w1600-20170226.txt
- **d:** 89901097dd332160050f4b9125511b61c0962b53
- **ba:** 1438
- **bb:** 1436
- **notes:** ["Capacity 160, output 160: not standard SHA-3 or Keccak-256.", "Source C buffer normalized to its explicit bit length: unused trailing bytes/bits removed, no significant bits changed.", "Digest recomputed by Atlas; cross-check any digest printed in the source separately."]
- **ext:** None

Input A (hex):
```
9d35ecb7e5ab27da6a250ecdb42a8a320e3984a1ecdedb00f445c78164f6433894f5d439ef3bf8dd7ac97202962aba46585518133ecec88c32655462c66c7c2db8f4c75dc2cd8d4d94bf853ff4524257eebd4cb0d6a2cfbd96758a16027a8d209287a6f052c6e7af6f91858d74047c46c3974b3cf6eabff1d47c8835eaaab0c24d43849d3fd2a372610b5990a0d9a5977e32d4db62ece1bbc562e49bcb4b28646a105eb5c8cb43880081c41a6ad93ddd671d1529
```
Input B (hex):
```
1089273007640c5a0b0c7924d7a7c1323aa80464c475ce8b317ece2ee923ce7f85c732f9f908ee1bf9176beb55ba6939a8c6216cb04829e81f2c2022efac42af60fb96bf90bdc1a9da7bb5367ce2980f0fc7883d45262ba0e6c719c94df7c55eddc8a3237a1d393175f2c70aadcdbec090d3c9b2f628fa14178225efea7ef6697871d3ceed7f9b157dca1c29b0c289daae1494989fe7dd7b4b5be192e1cb8830a9ce485c861786137413ade3e57c912a605e4208
```
