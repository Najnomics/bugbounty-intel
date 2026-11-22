# privilege escalation allow the app admin to add the user as organization admin (on Microsoft own…

- **Source URL:** https://medium.com/@amitkhandebharad5/privilege-escalation-allow-the-app-admin-to-add-the-user-as-organization-admin-on-microsoft-own-e24352219a24?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260622042625/https://medium.com/@amitkhandebharad5/privilege-escalation-allow-the-app-admin-to-add-the-user-as-organization-admin-on-microsoft-own-e24352219a24
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5966 (id 5966)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# privilege escalation allow the app admin to add the user as organization admin (on Microsoft own asset )

cant wait to disclose how i was able to promote my self as organization admin account using application admin

info: this site allows the users to create the application once we create the account on the site we can add the multiple collaborators to our site

sites has roles like

1: app\_admin

2:member

3: reader

where the app admin has access to all things member are able to edit the app and reader is read only user . so every time when i found this type of functionality i just login into the low level user account and try to access all functionality which i don't have access of

so using reader account i tried to add the user using the cookie of its allowed me to add the user so i just tried to add the user as app\_admin and and i got success and using read user i was able to add the user but after this i think a bit i realized that site are using roles like app\_admin, member and reader . its looking quite suspicious so i thoug what if site uses org\_admin for super admin role (as site using app admin for app then its obvious that site may user org\_admin for superadmin role) so i quickly intercept the request and tried to add the user as org\_admin USING APP ADMIN ACCOUNT but its wont work . so tried to add the user with role name as admin USING APP ADMIN ACCOUNT and its Gaves me 200 ok i just accept the invite using this invited user account and got super admin privilege

#FULL DETAILED POC

STEP: I LOGGED IN INTO THE APP\_ADMIN ACCOUNT

STEP2: INTERCEPTED THE REQUEST WHILE ADDING THE USER

you can see in above screen shot there is role as member

step3: swap the role to admin

//swaped role to admin

step4: send the request and accept the invite from this invited user account

poc: and once i accepted the invite here is all user apps i have full access to there application

and other applications users

i reported got that hall of fame from microsoft
