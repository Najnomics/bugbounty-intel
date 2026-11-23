# Idor Is Easy ! You may Don’t know ! The Longest PrivEsc I’ve ever faced on Public BBP

- **Source URL:** https://medium.com/@Ahmex000/idor-is-easy-you-may-dont-know-the-longest-privesc-i-ve-ever-faced-on-public-bbp-1bf67cd699d8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250218222956/https://medium.com/@Ahmex000/idor-is-easy-you-may-dont-know-the-longest-privesc-i-ve-ever-faced-on-public-bbp-1bf67cd699d8
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8162 (id 8162)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Idor Is Easy ! You may Don’t know ! The hardest PrivEsc I’ve ever faced on Public BBP

welocme Volk’s , it’s **Ahmex00** again with my highlighted report in my first year in BugHunting Journay , So let’s start

بِسْمِ اَللَّهِ وَالْحَمْدِ لِلَّهِ الَّذِي عَلَّمَ بِالْقَلَمِ عَلَّمَ الْإِنْسَانَ مَا لَمْ يَعْلَمْ وَالصَّلَاةَ وَالسَّلَامَ عَلَى خَيْرِ مُعَلِّمِي اَلنَّاسِ اَلْخَيْرِ مُحَمَّدْ وَبَعْدٍ

I suggest to you read the previous [writeup](/@Ahmex000/story-of-15-vulnerabilities-in-one-buplic-bbp-561e68213991)

## First, we must Know some simple things about the nature of the site’s work after analyzing the requests used in this vulnerability.

First you should know this : >


1. When you create an account, you get an organization, and its ID is serialized; for example, if your org ID is *1111,* then the next org ID will be *1112,* etc.
2. and you can create groups; also, IDs are serialized: GroupOneID`: 2222` `GroupTwoId: 2223` `GroupThreeId: 2224...` etc
3. Also, in your organization you have three roles; every role has an ID. And guess what! it’s serialized `OrgAdminId: 3333` `AccountAdminId: 3334` `RegularUserId: 3335` *These roles are linked to your organization, and every organization has the same roles but with different IDs.*
4. When you try to invite a new user to your organization, you must first create a new account and you can create group’s , you can invite this user and give him access to `all account groups` , the default value in this option is 0 in all organizations (remember that).

Let’s start with how the journey of the 3 bugz began until I reached P1

First report :

I can create new roles, and I can delete them also, so in my first days while testing this function, I tried to invite a user with my created role and then delete this role to see what happens, I failed in that. The role I created and assigned to the new user: \<I can’t delete it when this user just has this role.

If you give him another role and delete this one, nothing will happen because he has other roles.

If you read the other writeup, you will know that if the user has a separate account and then i invited him to my organization, it will be different in some things. After a while and some tests, I tried it again, but this time it deleted the role, and this user became without a role.

After a lot of experimentation to find out why the role was removed this time, I reached

1. I can only delete the role I gave to a specific user if that user had another account initially.
2. The user must have access to the current organization with access to all groups (group id is 0).

## Now the first report is easy, and the steps are as follows:

1. The victim creates a new role and modifies this role to allow to this role the creation of other roles and invites users to all groups, but with limited permissions.
2. victim invite **attacker-account-one** with this role
3. now **attacker-account-one** can create new roles but WITHOUT important permissions `Assign management permission`
4. The **attacker-account-one** can invite and edit users with (account admin and regular user) roles, and by default can’t invite users with the OrgAdmin role (the biggest role).
5. **attacker-account-one** craete new role - Only with very simple permissionss.
6. **attacker-account-one** invite **attacker-account-two** with created role
7. **attacker-account-one** delete this role
8. now **attacker-account-two** became without role
9. **attacker-account-one** now can give **attacker-account-two** OrgAdmin Role

So, I reported it, but the customer Not much is known about the site, and it is believed that the **attacker-account-one** naturally has the ability to invite users with the OrgAdmin role.

## Ok another quick try: “

By requesting user modification, i manipulated the role parameter and the specified group.

- After many attempts I found out that when I edit a user and that user is in my organization, and I am in that user’s organization and I edit that user (in my organization) and change his role to a different role than the current Group id, that user will become roleless in both groups.

ForEx: My group one ID is 1111, and my role One ID in my org is 2222, and the attacker group one ID is 1112, and he has role One ID 2223, and I invited the attacker to my Group One 1111, then edited this attacker and changed the group One ID to the victim group One ID and changed the role to the victim role ID; the victim became without roles in both organizations.

SO my scenario now is:

1. victim invite attacker to victim organization and give him (view & edit roles)
2. attacker invite victim to attacker organization
3. attcker edit victim in attacker organization and change group One ID and role One id to attacker ID’s
4. now attacker can revoke victim role in vicitm org BUT!

in another side i can try to do same steps with another attacker account , and when this account become without role , i can give him org Admin role As happened in the first report when the account became without a role

i tried It should have worked as intended but when the attacker account two became without a role I couldn’t give it the org admin role

# Now the last attempt (successful One)

After many attempts, I found that I can change the role ID to the victim’s role ID if the user is in my group and is present with the victim but with access to all groups (group ID is 0), but how can I know the victim’s org admin role ID? Regular user role cannot view the roles section.

Do you remember what I told you in the [previous write-up](/@Ahmex000/story-of-15-vulnerabilities-in-one-buplic-bbp-561e68213991)

Roles in organizations are organized, so if I get one role ID, I can simply get the other role IDs. So I simply searched the burp history on the attacker’s role ID in the victim’s organization and found it.

## now The steps have become simple

1. create three account’s (a**ttacker-account-one** , a**ttacker-account-two** , Victim )
2. Victim Invite a**ttacker-account-one** as regular user and access all group’s

Why access all groups? because, as I mentioned above, the (access all groups) option’s default value in all organizations is 0, and an attacker in org one can’t invite users in another’s group, so the backend has validation in this parameter.


3\. Now **attacker-account-one** can just view some data in the victim org.

4\. The attacker created another account, **attacker-account-two**

5\. **attacker-account-two** invites **attacker-account-one** with any role and accesses all groups.

6\. Now **attacker-account-one** is a member of the victim org and **attacker-account-one**.

7\. From **attacker-account-two** , try editing the **attacker-account-one** role and just change the role ID from 

**attacker-account-two** role id list to victim high role id (org admin id in victim org)

8\. **attacker-account-one** One hasn’t had access to view roles in the victim org, BUT he can view his role ID, so it’s easy to gain org admin role ID `attackeroneRoleId+2.`

9\. Now **attacker-account-two** sends an edit user request with all **attacker-account-two** org data and just the victim org admin role ID.

10\. Now **attacker-account-one** becomes org admin in victim organization.

finaly it’s triaged as P1 But customer have another opinion

but thank’s allah accepted as P2 :) …

Olive, 

think out of Th…NO

1. You should not give up. I discovered 3 vulnerabilities after leaving the program and returning to it and doing some simple tests.
2. Working for a long time on one program leads to ideas you might never think of when you quickly switch between different programs.
3. Success from God, try to get as close to God as possible
4. Code is not a human, always try to check with different ideas how the site checks different things and different scenarios
5. and the Big One is Always think about the structure of the code, codes are very sensitive so some simple ideas can make a big difference in the way you deal with penetration testing.

- صلي على النبي بقا وادعي لاخوك
