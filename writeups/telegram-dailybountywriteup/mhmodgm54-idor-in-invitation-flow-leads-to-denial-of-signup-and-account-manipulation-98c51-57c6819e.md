# IDOR in Invitation Flow Leads to Denial of Signup and Account Manipulation

- **Source URL:** https://medium.com/@mhmodgm54/idor-in-invitation-flow-leads-to-denial-of-signup-and-account-manipulation-98c51e0dd942?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250927043542/https://medium.com/@mhmodgm54/idor-in-invitation-flow-leads-to-denial-of-signup-and-account-manipulation-98c51e0dd942
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10515 (id 10515)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR in Invitation Flow Leads to Denial of Signup and Account Manipulation

## Introduction

In this write-up, I’ll walk through how I discovered an Insecure Direct Object Reference (IDOR) vulnerability in the invitation flow of a target application.

Initially, the issue was marked as “Not Applicable” (NA) because it seemed to have no practical impact.

However, after further testing, I escalated the scenario to demonstrate a real attack vector with higher impact — preventing invited users from signing up and potentially manipulating account data.Program

## Target Overview

The target (let’s call it `target.com`) is an organization management platform.

It supports multiple roles:

- **Owner**
- **Admin**
- **Developer**
- **Team Member**

The platform allows organization owners and admins to invite new users to join via email links.

## Discovery Steps

first i use the target as normal user with burp work in the background to see request after do some interaction with the target .

now i will explain the flow of signup in the site :

1. User enters their email and password on the signup page
2. They receive an invitation link in their email
3. after use link received can put information like `first_name , last_name , photo ...` your personal info

now after do many interaction and go to burp i found all action use `graphql` expected one request as you expected is the request which get it to put your personal info after signup

`POST /users/{{uuid}}/register`
now when try another uuid as idor it work “it work only with account which new register so it used one time” and without any thinking and after report it classified as NA cause the uuid is not guessable and i can’t get it from any place `until now` and the time to register is very minimum cause if normal one want register it will click on the link received quickly

## Escalating the Impact

I then considered a different angle:

What if I could get the UUID of a newly invited user?

**Normal invite flow for a new user:**

1. Owner sends an invitation.
2. Victim receives an email with the invitation link.
3. Clicking the link triggers the vulnerable `/users/{{uuid}}/register` request.

**Problem:**

As a **low-privilege member**, I could not see other members’ UUIDs — only their email and role. Even backend responses for organization member not include UUIDs

## The Breakthrough

While using an **Owner account**, I noticed that a specific GraphQL request returned:

- Member’s email
- Role
- **UUID**

I tested sending this same GraphQL request **using the JWT token of a low-privilege account** — and it still worked!

This meant that **any member** could enumerate UUIDs for **all other members** (including newly invited ones)

At this point, the attack became possible:

1. Monitor organization members via the GraphQL request
2. Detect when a new invited user appears
3. Immediately send a forged `/users/{{uuid}}/register` request as the attacker, before the victim completes signup

## Automation

To catch new invites instantly, I wrote a Python script that:

- Sends the GraphQL request every 5 minutes
- Compares the response to the previous one
- If a new UUID appears, alerts me immediately

This allowed me to race the victim to the vulnerable step

## Impact

Unlike the initial scenario (which was one-time and low-impact), this version allowed me to:

- **Block the victim from completing signup** — when they attempt to register, the system tells them the UUID is already used.
- **Manipulate the victim’s account data** before they log in (since the password is set **after** the vulnerable step).
- Cause a **persistent denial of access** to the victim.

## End

- Try always to improve impact of your vulnerability not report it without see to it impact in real attack scenario

i wish you benefit from this small and simple write-up

*أن رجلا جاء إلى رسول الله صلى الله عليه وسلم فقال : ( يا رسول الله ! أيُّ الناس أحبُّ إلى الله ؟ فقال : أحبُّ الناس إلى الله أنفعهم للناس…)*
