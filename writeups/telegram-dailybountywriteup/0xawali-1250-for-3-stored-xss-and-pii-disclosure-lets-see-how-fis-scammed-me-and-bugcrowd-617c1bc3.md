# 1250 $ For 3 Stored XSS AND PII Disclosure , Let’s See How FIS Scammed Me AND Bugcrowd Covered It…

- **Source URL:** https://medium.com/@0xAwali/1250-for-3-stored-xss-and-pii-disclosure-lets-see-how-fis-scammed-me-and-bugcrowd-covered-it-8561d9ce57b5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240612075628/https://medium.com/@0xAwali/1250-for-3-stored-xss-and-pii-disclosure-lets-see-how-fis-scammed-me-and-bugcrowd-covered-it-8561d9ce57b5?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6378 (id 6378)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 1250 $ For 3 Stored XSS AND PII Disclosure , Let’s See How FIS Scammed Me AND Bugcrowd Covered It Up !

Hi In this write-up , I’m going to explain how I got scammed multiple times , providing all the evidence without any kind of drama.

*I might get banned OR removed from bugcrowd platform , but I don’t care because that was 100 % a scam . a bugcrowd senior ASE member confirmed it , but since FIS is a top-tier joint customer , he sided with their customer as always they doing .*


Before discussing the scamming process let’s see bugcrowd’s vulnerability rating taxonomy AND FIS Scope and rewards

Plus let’s see what I found before discussing the scamming process

# **My First Report :**

while doing recon I found misconfigured s3 bucket let me write so I got a stored xss as you can see

Since my finding was in a UAT environment , the severity and payout had to be reduced , so I should receive a maximum bounty of P3 .

While I tried to see the production environment , I was not able to find it for some reasons that I figured out later so this lead us to my second report

# **My Second Report :**

after I figured out some stuff I was able to find the same bug on production environment as you can see

**But my report was marked as a duplicate of my first report .**

This one wasn’t a duplicate , and we will know more later. However a triager member said it’s a duplicate because it’s a mirror and has the same fix.

# **let’s summarize that :**

I found two misconfigured buckets lead to stored xss

*1. Misconfigured buckets lead to stored XSS on UAT environment*

[*https://flex-uat-static.online-banking-services.com*](https://web.archive.org/web/20240612075628/https://flex-uat-static.online-banking-services.com/)

*2. Misconfigured buckets lead to stored XSS on production environment*
[*https://flex-static.online-banking-services.com*](https://web.archive.org/web/20240612075628/https://flex-static.online-banking-services.com/)

So at least one of my two reports should have been accepted as P2. However I was focused on clarifying that both of my findings are not duplicates because there are five pieces of evidence that you can check it yourself right now .

*1. Different S3 buckets name AND configuration 2. Different TLS Certificate 3. Different IPs 4. Different Subdomains 5. Different Content*


The scamming process wasn’t clear here , but please keep this in your mind for later

*1. A triager member said it’s a duplicate because it’s a mirror and has the same fix . 2. FIS Fixed both AND changed the status of my reports to unresolvable , and we will find out why FIS is doing this .*


Anyway , I accepted that but I noticed that both buckets disclose internal information, although it’s not sensitive. I’ve added them to my to-do monitoring list .

# approximately two years later , In 26 Mar 2024

While reading some write-ups related to FIS , some bug bounty hunters found the same bug on two different subdomains. Surprisingly , FIS accepted both. So I revisited my findings and while checking them , I discovered that I could write on the production environment but not on the UAT environment. This verified that both buckets are not mirrors and have different configurations , which leads us to the first scamming

# My Third Report :

So I immediately reported it , but I got a self-duplicate of my first report because the status of my first report is unresolved .

Do you remember when I said we will find out why FIS marked our reports as unresolvable ? Because if someone found a bypass or the same bug , FIS uses this trick to close your report as a duplicate , and that is 100% a scam.

Now it’s obvious to me that there is something wrong , so I tried to explain that it’s not a duplicate .

One of the FIS team members sent a private message to bugcrowd Staff and created a blocker to triage my report

After my report got triaged , I tried to escalate this stored XSS to ATO because I noticed a lot of banks use this bucket based on the listed files. So , I started to see which subdomains use this bucket , and after some time , I found an online bank use this bucket but it was too late to escalate this one to ATO becuase FIS fixed my found

But for some reason after FIS fixed my found , my report was marked as a duplicate of my first report again

But at least the reason changed from it’s a mirror and same fix to we’re already aware of these findings .

So now it’s obvious to me that FIS and the triage member scammed me in 2022 because they closed my report as a duplicate , claiming it was a mirror and had the same fix .

How is that possible when I was able to write on one of them but not both in 2024 ?!

# My Fourth Report :

While digging into both buckets , I found another bucket that was disclose sensitive information in PDF files e.g.

*1. Emails address , usernames , tax-ID of FIS employees 2. Accounts numbers or maybe credit cards 3. Bank transfers*


after two weeks my report closed as N/A after deleting all the files because this is all non-production data intended for testing

so let’s see all non-production data intended for testing e.g. PII of Active/Inactive Since: Past 30 days

So how is this data intended for testing when there is a user registered in 2009 and their last login was in 2024? Imagine that.

This file contained 14 pages , and each page had 10–12 emails , usernames and tax IDs of FIS employees .

So , it was obvious to me that this was a scam again. I immediately created a ticket discussing all the details with the support team, focusing only on my first and second reports .

Actually, I did reach out and tried to contact the FIS team through bugbounty@fisglobal.com in 11 Apr 2024 before escalating this issue with FIS customer support in 11 May 2024 .

Bugcrowd support asked me to allow them five days to investigate, but two weeks passed and nothing happened. So, I reached out to Bugcrowd support again, and they escalated my ticket to the technical customer support manager.

Going back to my RAR, I was discussing why my report is a duplicate. Additionally, if the FIS team insists on marking one of them as valid, the severity and payout should be based on the production environment.

But FIS replied to my RAR after Bugcrowd support escalated my ticket to the technical customer support manager

If you noticed , FIS replied only to why this is a duplicate and skipped my part where I insisted that if they mark one of them as valid, the severity and payout should be based on the production environment

So I immediately got back to my ticket , and Bugcrowd support escalated my ticket to the ASE Appeals team

Jeremy said “ Unfortunately this is not eligible for appeal due to the amount of time that has passed. This should have been raised for appeal two years ago “ AND then he mentioned “ While the original report is still in the Unresolved state we cannot accept new submissions for this as the client has not deemed it completely fixed either ”

So how can you not accept my appeal due to the amount of time that has passed and not accept new submissions for this , especially when the client has not deemed it completely fixed , while the original report has been in an unresolved state since 2022 ?!

But finally , he confirmed that one of my two original reports should have been accepted at a higher priority originally but bugrowd policy prevent him to accept my appeal

Jeremy said, ‘I do wish this could have had a different outcome.’ Since my reports have been unresolved since 2022, I have the right to reopen my first report. so FIS’s trick of keeping reports unresolved to scam can actually help me to reopen my first report.

So I did RAR on my first report, but no one cared. The ASE Appeals team chose Bugcrowd’s policy to cover FIS’s scamming process instead of being ethical and helping me. Therefore, I decided to disclose this.

let’s get back a little with my third report and my ticket and if you noticed FIS team said “ We’ve received multiple reports ”

and ASE Appeals team said that “it wouldn’t be fair to the other researcher who have also since reported this and been duplicated themselves”

But they both forgot that I was able to write on both buckets in 2022. So, if the ASE Appeals team had any intention of helping me, they should have taken my third report as reference and evidence that FIS and a triage member were wrong in 2022 when they closed my report as a duplicate, claiming it was a mirror.

Plus , anyone has knowledge of S3 buckets will confirm that this was a 100 % scam from the beginning because :

*1. Different S3 buckets name AND configuration 2. Different TLS Certificate 3. Different IPs 4. Different Subdomains 5. Different Content*


Because I was frustrated , especially after the ASE Appeals team confirmed that one of my two original reports should have been accepted at a higher priority , I tried to disclose my report. However, Bugcrowd considered my action as a threat and took immediate action against me

# Final Thought :

*1. I know I should have discussed the duplicate issue from the beginning, and if they insist on paying for only one , they should pay based on the production environment. However , I was focused on discussing that both are valid , as I confirmed later .*

*2. The ASE Appeals team can help me if they choose to be ethical , rather than restricting themselves to bugcrowd policy. Plus, if bugcrowd policy prevents the ASE Appeals team from accepting my appeal , since my reports have been unresolved since 2022, I have all rights to reopen my reports .*


# Timeline :

*1. My first Report 04 Oct 2022*

[*https://bugcrowd.com/submissions/756821ad-42cf-42d5-b72a-19295559f61a*](https://web.archive.org/web/20240612075628/https://bugcrowd.com/submissions/756821ad-42cf-42d5-b72a-19295559f61a)

*2. My Second Report 11 Oct 2022*
[*https://bugcrowd.com/submissions/0497a150-9e99-4ad1-b045-a40814da18ed*](https://web.archive.org/web/20240612075628/https://bugcrowd.com/submissions/0497a150-9e99-4ad1-b045-a40814da18ed)
*3. My Third Report 26 Mar 2024*
[*https://bugcrowd.com/submissions/e332b949-3250-4556-8ed2-c5320237d0c9*](https://web.archive.org/web/20240612075628/https://bugcrowd.com/submissions/e332b949-3250-4556-8ed2-c5320237d0c9)
*4. My Fourth Report 08 Apr 2024*
[*https://bugcrowd.com/submissions/ba30fea5-cbc6-42de-a5e5-9ea61e05ac4d*](https://web.archive.org/web/20240612075628/https://bugcrowd.com/submissions/ba30fea5-cbc6-42de-a5e5-9ea61e05ac4d)

I hope I clarified everything

thanks
