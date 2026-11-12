# Payloads — open-redirect

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. CVE-2022-45402
- Source: `telegram writeups (verbatim excerpts)`

```
Hi,

In Apache Airflow, there is a parameter "next" on the Login page. And after a successful login, we're redirected to this parameter's value. 
I see there are some preventions for the open redirect bug. However, I can bypass these preventions using "/\google.com"

It seems this parameter accepts anything after the slash "/" character. And, browsers parse "/\" as "http://" in the location header.

For reproducing, you can try to login on the http://127.0.0.1:8080/login/?next=/\google.com

I tested this bug in the last version (v2.4.2)

Regards,
Bugra Eskici
```
