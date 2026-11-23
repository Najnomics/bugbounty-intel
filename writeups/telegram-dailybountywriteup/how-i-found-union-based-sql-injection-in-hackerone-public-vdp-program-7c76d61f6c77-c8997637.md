# how i found union based sql injection in hackerone public vdp program?

- **Source URL:** https://doordiefordream.medium.com/how-i-found-union-based-sql-injection-in-hackerone-public-vdp-program-7c76d61f6c77?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250221172729/https://doordiefordream.medium.com/how-i-found-union-based-sql-injection-in-hackerone-public-vdp-program-7c76d61f6c77
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7409 (id 7409)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# how i found union based sql injection in hackerone public vdp program?

hi everyone , i am back with another writeup.

today i will explain “how i found sql injection on hackerone vdp public program”

lets start,

at first ,consider the name of domain is example.com

like every hacker i was start recon of domain. using waybackurls,

githubrecon and googledorking.

but no use i did not found anything interesting,then start using domain like normal user under burp proxy.

after i opened the urls one by one and checking endpoints for any xss or sql.but nothing i was get.

then i start checking every url for sql with singe quote(‘).even no parameter on urls also checking. some point of time one url get response(500 status code).

“here simple using repeater tab, i was testing every url.”

when i got 500 status, that url has no id parameter.its just url path

its looks like:

[https://www.example.com/used-vehicles/examle--resale-BB005809R](https://www.bharatbenz.com/used-vehicles/BharatBenz--resale-BB005809R)’

next we need to balance the query so i was add ‘ — -’

then final url after:

[https://www.example.com/used-vehicles/example--resale-BB005809R](https://www.bharatbenz.com/used-vehicles/BharatBenz--resale-BB005809R)’ — -

after successfully balance the query ,next we need to find how many columns are there?. so we use order by,
