# How We Hacked Voice Communication Solutions Company And Found BAC + Info Disclosure + IDOR

- **Source URL:** https://medium.com/@eslam.zayedw/how-we-hacked-voice-communication-solutions-company-and-found-bac-info-disclosure-idor-d-6884037064f0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240604072056/https://medium.com/@eslam.zayedw/how-we-hacked-voice-communication-solutions-company-and-found-bac-info-disclosure-idor-d-6884037064f0?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5976 (id 5976)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How We Hacked Voice Communication Solutions Company And Found BAC + Info Disclosure + IDOR :D

# Let’s Get Straight To The Story

I received a private invitation from a program called target.io

then I started to do my recon and found some nice subdomains.

first, I just wanna say every subdomain has a different API to serve it:-

## login.target.io => api.target.io

## login.dev-02.target.io => api.dev-02.target.io

## login.staging.target.io was using => api.staging.target.io

## Mobile app API (observatory.target.io)

and more like this.

I began to check them one by one and I noticed there was no registration form I found out u need an invitation from a company account on this application

then I went straight to JS Files to find endpoints to see if something was interesting or not I didn’t find anything interesting

so I went back to the login page and sent the login request and started playing with Burp.

I started to play with the login request the first request was sent to endpoint /api/users/login

after changing the endpoint from /api/users/login to /api/users

I got some errors that gave me more required parameters and after crafting the request successfully I got this response The 204 No Content meaning we’ve successfully created our account.

after logging in nothing was interesting just got an Authorization Token (we will use it later)

so I started fuzzing behind [https://api.](https://web.archive.org/web/20240604072056/https://api.exampe.io/)target.io

I found 2 interesting endpoints

/swagger.json => this file got all API endpoints (u can import it to Postman and run it with proxy to burp and begin ur investigation)

/metrics => This one was leaking the entire API requests of all users on the platform

after visiting /metrics endpoint

u can see in the second pic u can notice the endpoints this was leaking the entire UUIDS of all users on the platform ( i mean the role: user) + Request Method used on the endpoints :D

/api/users/\<random-UUID>

/api/users/\<random-UUID>/status

/api/users/\<random-UUID>/profile

And MOOOOORRRRRRE.

from here I went back to Burp and tested this endpoint with all of this UUID’s

there were email and username, group\_id’s, and interesting stuff for all users.

but this one, there was a location with the coordinates of the online user :D

my friend [Abdelrahman Shazly](https://web.archive.org/web/20240604072056/https://medium.com/u/bb9e4e0b1d91?source=post_page-----6884037064f0--------------------------------) started looking in Mobile App API and he found the same stuff :D same information disclosure and IDOR

after finding this stuff I went to the other subdomains and found the same things but one was for admins and one was for developers and one for companies :D

In the end, I got like

5 information Disclosure

5 Broken Access Control

5 IDOR’s users + admins + developers + companies

I started writing my reports after finding all of this nice stuff :D

June 8, 2023:- Reported

6 reports = 1 info disclosure For all URLs + 5 BAC and Idor

June 12, 2023:- All Reports Triaged

August 12, 2023:- 5 reports got duplicated after 2 months of triage and 1 report got resolved, bounty awarded, program quit Hackerone Forever :D

I think the company ran away without paying all the bounties :D
