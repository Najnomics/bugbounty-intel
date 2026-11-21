# Leaks Data via Public API And IDOR

- **Source URL:** https://medium.com/@HBlackGhost/leaks-data-via-public-api-and-idor-1ebab2b37211?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251104053722/https://medium.com/@HBlackGhost/leaks-data-via-public-api-and-idor-1ebab2b37211
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10213 (id 10213)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Leaks Data via Public API And IDOR

بسم الله الرحمن الرحيم , اللهم لك الحمد مالك المنه الفضل علي عباده الفقراء ,اللهم لك الحمد عدد كل شئ , اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كما صليت على إبراهيم، وعلى آل إبراهيم، إنك حميد مجيد، اللَّهُمَّ بَارِكْ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كما باركت على إبراهيم وعلى آل إبراهيم، إنك حميد مجيد , اللهم لك الحمد كما ينبغي لجلال وجهك وعظيم سلطانك االلهم لك الحمد حمداً كثيراً طيباً مباركاً فيه

While I was on a call with my bro , we decided to target another BBP. I sent him a program, and we started diving in to understand it. After spending a few hours analyzing the program, we were ready to hack it easily.

let’s gooo :

This website functions like a virtual school. After exploring it, we discovered an endpoint that allowed us to access all schools information \[ including staff member details and their IDs \] without any authentication. The data exposed depends on your region; for example, if the request originates from Egypt, it reveals information about Egyptian schools.

OMG !!!!!!!!! , i have all schools info

After receiving the response and extracting the school IDs from it, we can use this endpoint to leak detailed information about a specific school.

ohhh, I can retrieve all school data ,That’s sensitive data, right?

let’s do another chain to rise the impact of this bugs , diving and more diving in burp proxy and OMG i can catch a request can leak form it teachers information

OMG, I’m hating the website again!

That’s right — I can access all teachers’ data, including their names, locations, the IDs of their respective schools, and other personally identifiable information (PII) and t their Photos , simply by changing the IDs in the endpoint.

وابلللللللع !! 💥🔥

والسلام عليكم ورحمه الله وبركاته
