# Subdomain takeover — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #1474784 Subdomain Takeover of brand.zen.ly — zenly — $750 — None
Source: `hackerone/reports/2022/1474784.md` (https://hackerone.com/reports/1474784)

```
└─$ dig brand.zen.ly
brand.zen.ly.		255	IN	CNAME	brandpad.io.
```

## #1297689 Subdomain takeover of www█████████.affirm.com — affirm — $500 — Business Logic Errors
Source: `hackerone/reports/2021/1297689.md` (https://hackerone.com/reports/1297689)

```
% curl https://www██████████.affirm.com
[...]
<Code>PermanentRedirect</Code>
<Message>The bucket you are attempting to access must be addressed using the specified endpoint. Please send all future requests to this endpoint.</Message>
<Endpoint>s3.amazonaws.com</Endpoint>
<Bucket>affirm-prod-www-cms████</Bucket>
[...]
```

```
% curl https://s3.amazonaws.com/affirm-prod-www-cms████████/index.html
<!-- taken over by hackerone.com/ian bugcrowd.com/iangcarroll ian@lhost.sh -->
```

## #1182864 Subdomain takeover of fr1.vpn.zomans.com — eternal — $350 — Business Logic Errors
Source: `hackerone/reports/2021/1182864.md` (https://hackerone.com/reports/1182864)

```
% dig +short fr1.vpn.zomans.com
52.47.57.107

% curl fr1.vpn.zomans.com
<!-- hackerone.com/ian -->
```

## #1180697 Subdomain takeover of v.zego.com — zego — - — Externally Controlled Reference to a Resource in Another Sphere
Source: `hackerone/reports/2021/1180697.md` (https://hackerone.com/reports/1180697)

```
% dig +short v.zego.com
52.214.138.192

% curl v.zego.com
<!-- hackerone.com/ian -->
```

## #2523654 Subdomain takeover in Gitlab pages — gitlab — - — Misconfiguration
Source: `hackerone/reports/2024/2523654.md` (https://hackerone.com/reports/2523654)

```
docs-dev.gitlab.com.    300     IN      CNAME   gitlab-com.gitlab.io.
gitlab-com.gitlab.io.   300     IN      A       35.185.44.232
```

```
HTTP/1.1 302 Found
content-type: text/html; charset=utf-8
location: https://projects.staging.gitlab.io/auth?domain=http://docs-dev.gitlab.com&state=giZFQTsOOFXvR_0po68zrg==
permissions-policy: interest-cohort=()
set-cookie: gitlab-pages=..._; Path=/auth; Expires=Tue, 28 May 2024 21:07:33 GMT; Max-Age=600; HttpOnly
vary: Origin
date: Tue, 28 May 2024 20:57:33 GMT
gitlab-lb: haproxy-pages-01-lb-gstg
gitlab-sv: pages-us-east1-c

HTTP/2 401 
content-type: text/html; charset=utf-8
permissions-policy: interest-cohort=()
vary: Origin
x-content-type-options: nosniff
content-length: 2872
date: Tue, 28 May 2024 20:57:34 GMT
```

## #1406335 Subdomain takeover of images.crossinstall.com — x — - — Business Logic Errors
Source: `hackerone/reports/2022/1406335.md` (https://hackerone.com/reports/1406335)

```
% dig images.crossinstall.com +short
assets.crossinstall.com.s3.amazonaws.com.
s3-1-w.amazonaws.com.
s3-w.us-east-1.amazonaws.com.
52.217.103.180

% curl images.crossinstall.com/index.html
<!-- hackerone/ian bugcrowd/iangcarroll -->

% whois crossinstall.com | grep Org
Registrant Organization: Twitter, Inc.
Admin Organization: Twitter, Inc.
Tech Organization: Twitter, Inc.
```

## #148770 Subdomain takeover at api.legalrobot.com due to non-used domain in Modulus.io. — legalrobot — - — Violation of Secure Design Principles
Source: `hackerone/reports/2016/148770.md` (https://hackerone.com/reports/148770)

```
NO APPLICATION WAS FOUND FOR
api.legalrobot.com
```

```
$ curl https://api.legalrobot.com
Hello World!<!--FRANS ROSEN-->
```

## #165309 Subdomain Takeover in http://genghis-cdn.shopify.io/ pointing to Fastly  — shopify — - — None
Source: `hackerone/reports/2016/165309.md` (https://hackerone.com/reports/165309)

```
Fastly error: unknown domain: genghis-cdn.shopify.io. Please check that this domain has been added to a service.
```

```
$ host genghis-cdn.shopify.io
genghis-cdn.shopify.io is an alias for shopify-e.map.fastly.net.
shopify-e.map.fastly.net is an alias for prod.shopify-e.map.fastlylb.net.
prod.shopify-e.map.fastlylb.net has address 151.101.60.108
```

## #317005 Subdomain Takeover due to unclaimed domain pointing to AWS — gsa_bbp — - — Off-by-one Error
Source: `hackerone/reports/2019/317005.md` (https://hackerone.com/reports/317005)

```
 nslookup  18f.domains.api.data.gov
Server:         213.186.33.99
Address:        213.186.33.99#53

Non-authoritative answer:
18f.domains.api.data.gov        canonical name = dn9rrjaiux2m0.cloudfront.net.
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.116
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.87
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.105
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.202
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.145
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.21
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.64
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.161
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:d000:3:f914:5e00:93a1
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:6600:3:f914:5e00:93a1
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:6400:3:f914:5e00:93a1
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:5000:3:f914:5e00:93a1
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:be00:3:f914:5e00:93a1
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:c400:3:f914:5e00:93a1
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:4400:3:f914:5e00:93a1
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:7000:3:f914:5e00:93a1
```

## #1179193 Subdomain takeover of www2.growasyouplan.com — palo_alto_software — - — Externally Controlled Reference to a Resource in Another Sphere
Source: `hackerone/reports/2021/1179193.md` (https://hackerone.com/reports/1179193)

```
% whois growasyouplan.com | grep Org
Registrant Organization: Palo Alto Software, Inc.
```

```
% dig +short www2.growasyouplan.com
67.202.62.93

% curl www2.growasyouplan.com
<!-- hackerone.com/ian -->
```

## #794382 Route53 Subdomain Takeover on test-cncf-aws.canary.k8s.io — kubernetes — - — Misconfiguration
Source: `hackerone/reports/2021/794382.md` (https://hackerone.com/reports/794382)

```
test-cncf-aws.canary.k8s.io. 3600 IN    NS      ns-265.awsdns-33.com.
test-cncf-aws.canary.k8s.io. 3600 IN    NS      ns-687.awsdns-21.net.
test-cncf-aws.canary.k8s.io. 3600 IN    NS      ns-1458.awsdns-54.org.
test-cncf-aws.canary.k8s.io. 3600 IN    NS      ns-1825.awsdns-36.co.uk.
```

```
poc.test-cncf-aws.canary.k8s.io
```

