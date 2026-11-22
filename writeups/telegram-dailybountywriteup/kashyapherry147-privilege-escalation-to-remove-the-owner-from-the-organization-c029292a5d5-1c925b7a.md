# Privilege Escalation to remove the owner from the organization

- **Source URL:** https://medium.com/@kashyapherry147/privilege-escalation-to-remove-the-owner-from-the-organization-c029292a5d55?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221209213052/https://medium.com/@kashyapherry147/privilege-escalation-to-remove-the-owner-from-the-organization-c029292a5d55
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1046 (id 1046)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege Escalation to remove the owner from the organization

Hi Hackers, Today i am going to tell you about my one of interesting finding. Which is privilege escalation to remove the owner from the organization. And takeover the whole organization.

So, without wasting time. Let’s start

I’m not going to disclose the company name, because of privacy.

Assume [https://organization.redacted](https://organization.redacted.com).com

On November 19 2022, i reported a google map api key issue to the redacted.com, and after two days they triaged my report, and they set medium severity of this report. After saw this, i’m trying to hunt more on redacted.com. And that website handle different roles like owner and an administrator.So, I created two accounts, 1) Owner and 2) Administrator. After analyzing the application i found that, administrator doesn’t have access to change the settings of the organization. And then i fired up my Burpsuite, and played with owner and administrator account. And during the interception of the owner account, I found a json parameter, ”is\_owner”:”true” . Then, i thought can i become an owner using this parameter. And then i intercepted a simple request from the administrator account. And add a request line like this:

org-id: 6386d3e81dcec0115ea89f6d

PUT /v1.2/organization/org-id/qid/\[administrator-email-address\] HTTP/2

And add also this:

{“is\_owner”:true}

and forward the request. And guess what, now i’m also the owner of the application. So, now i thought can i delete the owner. So, now this time i went to owner account, and intercept owner delete request in burpsuite. And the request is like this:

DELETE /v1.2/organization/org-id/user/owner-id HTTP/2

So, now for deleting the owner from the organization i need to know the owner id. So, after analyzing some time i found a request, which is disclosing user-id.

Request is like: 

GET /v1.2/organization/6386d3e81dcec0115ea89f6d/user

Now i have everything, so let’s remove the owner from the organization.

This time again i intercepted one request in burpsuite. and add this request line:

DELETE /v1.2/organization/org-id/user/owner-id

(Use ord-id and owner id here)

And send the request. And Boom, i successfully remove the owner from the organization.

And then, i reported this vulnerability to company, and after 5 days, they said your finding is duplicate. And then i reported 1 privilege and 1 2fa bypass. Both of these reports are also gone duplicate. I was feeling so, sad for this. But if you are a good hunter, then duplicates is a part of your life.

Thanks for reading amazing hackers.

Instagram: [https://www.instagram.com/cyber\_\_hawk/](https://www.instagram.com/cyber__hawk/)

Linkedin: [https://www.linkedin.com/in/hemant-kumar-714564199/](https://www.linkedin.com/in/hemant-kumar-714564199/)

Twitter: [https://twitter.com/Herry51130182](https://twitter.com/Herry51130182)
