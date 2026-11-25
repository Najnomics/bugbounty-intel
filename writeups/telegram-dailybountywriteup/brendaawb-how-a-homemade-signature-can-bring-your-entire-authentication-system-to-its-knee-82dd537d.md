# How a “homemade” signature can bring your entire authentication system to its knees. #1

- **Source URL:** https://medium.com/@brendaawb/how-a-homemade-signature-can-bring-your-entire-authentication-system-to-its-knees-1-fac634d85277
- **Fetched from:** https://medium.com/@brendaawb/how-a-homemade-signature-can-bring-your-entire-authentication-system-to-its-knees-1-fac634d85277?source=rss-d5da436c9d46------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14929 (id 14929)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Brenda Wai / Thu, 01 Oct 2026 01:19:50 GMT

Today’s [Bugforge](https://bugforge.io/) challenge is simple to state and brutal to solve: log in as admin on a fictional application, without ever knowing the password. The only hint provided?

JWT.

An instruction that screams classic OWASP territory, but as usual, hides something a little more subtle than it looks.

A JSON Web Token is three blocks separated by dots:

header.payload.signature

Here’s the catch: with HS256, the signature relies on a shared secret, a simple string known only to the server. If that key is weak, predictable, or sitting in a common wordlist... it becomes crackable offline, with no rate limit, no logs, no alerts. An attacker's dream.

Nothing fancy here: I log in with a regular user account, intercept the request, and grab my JWT from the Authorization header or cookies (I use Burp Suite).

A quick trip to [jwt.io](https://jwt.io/) confirms the structure:

No surprise, the algorithm is HS256. Time to crack that secret.

Hashcat has a mode built specifically for HMAC-signed JWTs:

hashcat -a 0 -m 16500 \<JWT\_token> /usr/share/wordlists/rockyou.txt

A few seconds or minutes later, depending on your machine's power and the wordlist used...

...

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwidXNlcm5hbWUiOiJ0ZXN0Iiwicm9sZSI6InVzZXIiLCJpYXQiOjE3OTA4MTI2MDh9

.wDCDyirRMPirVpPxgETXOt1ZuD8Hw2fVkYBd9GdE9cs:secret


Session..........: hashcat

Status...........: Cracked

The secret drops. The secret is revealed. It is secret.Proof that even in 2026, JWT signing keys are still too often hardcoded, never rotated, and far too short to survive a decent wordlist.

Once I have the secret in hand, rebuilding the token by hand is trivial. I edit the payload to impersonate a plausible admin identity:

```
{
  "id": 1,
  "username": "admin",
  "role": "admin",
  "iat": 1790812608
}
```
Then I resign the whole thing on [jwt.io](https://jwt.io/) using the cracked secret secret.

(Tools like jwt\_tool can do the same thing in a single command line).

I swap my original token for the freshly forged one, fire a request at a protected route… and just like that, I’m authenticated as admin, without ever having known a single password.

The server still trusts the signature, and for good reason — it’s *its own key* that just validated my lie.

Then, by searching for the administration endpoints embedded in the application’s local JavaScript file, I found /api/admin/stats. So I loaded it up in BurpSuite and hit send.

And I got the flag!!!

What makes this flaw especially nasty is how silent it is:

One weak secret equals total compromise of the authentication system.

A few simple habits, too often overlooked:

This Bugforge challenge is a great reminder: a JWT’s security doesn’t come from its format, it comes entirely from the strength of its signing key. A solid algorithm (HS256) paired with a weak secret is still… a weak algorithm.

Next time you spot HS256 in a JWT header, ask yourself: *would this secret survive more than ten minutes against hashcat?*

If the answer is no, you already know what to do next.

*Challenge completed as part of the Bugforge daily series. See you in the next write-up!*
