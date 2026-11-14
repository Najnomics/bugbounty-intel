# Access to tomcat-manager with default creds

- **Source URL:** https://hackerone.com/reports/1267174
- **Fetched from:** https://hackerone.com/reports/1267174.json
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1620 (id 1620)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Access to tomcat-manager with default creds

- **HackerOne report:** https://hackerone.com/reports/1267174
- **State:** Resolved
- **Severity:** high
- **Weakness:** Improper Authentication - Generic
- **Program:** JetBlue (https://hackerone.com/jetblue)
- **Reporter:** 0xjackal
- **Submitted (UTC):** 2021-07-17T23:24:05.276Z
- **Disclosed (UTC):** 2023-02-05T12:59:44.752Z

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary:
Hi jetblue Security Team.

I Found that this domain `█████████` using Apache Tomcat/6.0.35 , And i was able to login to https://██████████/manager/html With default credentials `tomcat:tomcat`
See the following Screenshots:-

██████████

███

## Steps To Reproduce:
1. Go To https://███████/manager/html
2. Login with default creds `tomcat:tomcat`

## Supporting Material/References:
- https://book.hacktricks.xyz/pentesting/pentesting-web/tomcat

## Impact

Improper Authentication
Default Credentials lead to access admin manager.

##Fix:-
- Change default creds.
