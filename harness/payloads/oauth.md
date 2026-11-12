# Payloads — oauth

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. iOS OAuth client accepts any protocol in redirect_uri
- Researcher: @xssdoctor
- Post: https://x.com/xssdoctor/status/2105723370125881675
- Sources: `posts/xssdoctor/2026-10-01-2105723370125881675.md`, `writeups/xssdoctor/faav-17-trillion-microsoft-records.md`

```
Register a malicious iOS app for the custom URL scheme accepted as OAuth redirect_uri; start the flow in Safari with callback pointing at the malicious app to capture the code/token
```

## 2. Public OAuth client ID treated as authority — free account R/W production billing catalog ($2,500)
- Researcher: @mdp_sec
- Post: https://x.com/mdp_sec/status/2095462761111388207
- Sources: `posts/mdp_sec/2026-09-03-2095462761111388207.md`

```
Use public OAuth client_id as a free user against production billing catalog endpoints
```

## 3. Account takeover due to insufficient URL validation on RelayState parameter
- Source: `telegram writeups (verbatim excerpts)`

```
GET /2.0/repositories/%7B766210f9-9bec-4010-9f4d-917b06661c0c%7D HTTP/2
Host: api.bitbucket.org
User-Agent: curl/7.79.1
Accept: */*
Authorization: Bearer Txpo3AXXQZHlp....
```
