# weak protection against brute-forcing on login api leads to account takeover

- **Source URL:** https://hackerone.com/reports/766875
- **Fetched from:** https://hackerone.com/reports/766875.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/53 (id 53)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# weak protection against brute-forcing on login api leads to account takeover 

- **HackerOne report:** https://hackerone.com/reports/766875
- **State:** Resolved
- **Severity:** critical
- **Weakness:** Improper Restriction of Authentication Attempts
- **Program:** Palo Alto Software (https://hackerone.com/palo_alto_software)
- **Reporter:** zer0code
- **Submitted (UTC):** 2020-01-01T20:49:22.244Z
- **Disclosed (UTC):** 2022-08-29T18:23:08.457Z

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary:
Weak protection against brute-forcing on login API: https://api.outpost.co/api/v1/login leads to account takeover on https://www.teamoutpost.com/
## Steps To Reproduce:
* Sign in on https://www.teamoutpost.com/
███
* redirect to https://app.outpost.co/sign-in to login
█████████
* test any login credentials and review the request to https://api.outpost.co/api/v1/login
███████
* Notice the difference between the wrong user "Username does not exist" and wrong password " Password does not match username" 
████
* first we need to brute-force on username to get some valid usernames 
█████████
* We can grep on "Username does not exist" 
██████
* Here is valid usernames without  "Username does not exist"
██████████
* Notice the API doesn't block me for many requests even I reached more than 33K request and continue 
████
* after we exported a list of valid usernames we can brute-force for password fore every username on the list
██████████
* I imported valid usernames as 1st payload 
██████
* for 2nd payload I can use a passwords list but I tried the simplest password that user can register with " 9 characters long "
███████
* we got some credentials even with ADMIN role
██████████

## Impact

account takeover
