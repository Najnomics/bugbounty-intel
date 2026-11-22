# Step 21

- **Source URL:** https://medium.com/@R4v3ncl4w/step-21-sql-injection-fundamentals-c54bc69487c9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221006150445/https://medium.com/@R4v3ncl4w/step-21-sql-injection-fundamentals-c54bc69487c9
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/405 (id 405)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Step 21: SQL Injection Fundamentals

SQLi my old friend… honestly I’m hopin to run through this module fairly quickly. I did a Udemy course on SQL databases after struggling with a mysql module. Turns out that this would’ve been the module to start with… maybe. Let’s find out! Work is wild and they’re changing things every day, but got to keep with it!

Fair warning: I’m probably going to skip through a lot of this (aka skim) as I’m feeling pretty good about it.

Also warning: REMEMBER SPOILERS

I’m thinking you’re better off looking at my other SQL stuff if you’re wondering why this is so short.

## Task:

Yeah this easy… this might be a short one people, oops.

Blah blah long story short…

## Task:

## Task:

## Task:

# Intro to SQL Injections

Okay okay, I will slow down now. Starts of a new evening… work is kicking my booty with BS admin stuff from the big guys above who have nothing to do with education but I think we’ll win that fight. The students are incredible though and the teachers and principal I’m working with are fantastic so far! Time to hack…

This module is going to focus on Union based injections.

# Subverting Query Logic

Before we execute entire queries, let’s look at simply altering existing ones by injecting ‘OR’ into tactical places…

## SQLi Discovery

If the request uses GET parameters (the payload is in the URL) you may need the URL encoded version of the payload.

Remember to have an even number of single quotes in a query… I had this problem previously and didn’t realise it.

## Or Injection

This injection gives the output:

There’s a lot more payloads on [Payloadallthethings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection#authentication-bypass) of course there is!

## Task:

Update: it’s been 16 days since I looked at anything. To be honest for a week, I was working and coming home to play Xenoblade Chronicles 3. I’ve sufficiently completed the game now (highly recommend).

Fast forward to this week and four days ago I finally got Covid. LUCKILY my symptoms (thus far) are very mild. I had a moderate fever and sore throat for a day and and my throat is hoarse but not sore anymore but still testing positive. What better thing to do when you can’t go out to do anything? Jump back into things. That damn game consumed me it was BEAUTIFUL, but I’m happy to see the back of it. Just the odd daily game or two of Pokemon Unite now until Scarlet/Violet comes out in November then I’ll probably buy a PS5 and Elden Ring (I know I know, late to the party) and Hogwarts Legacy in February. Honestly it’s been nice to take a break from cybersecurity.

I absolutely love it but I become so obsessed with it I let problems take over my life and it’s all I think about so stepping away for a week or two was nice to focus on other things like a video game and being with the girlfriend (who was also sick just before me).

So who knows when I’ll be back in work. Can’t go back in until I test negative even though I feel fine so study on!

## Using Comments

Remember comments are a useful way to manipulate query logic for our needs. You can use a double dash followed a space or an octothorp (#).

## Task:

Login as the user with id = 5

`‘ or id = 5 ) #`
This goes in your user field, password literally doesn’t matter as in the query it would be commented out”

# Union Clause

UNION is used to combine results from multiple select statements. So far we have only been using OR to alter the logic of an original query.

EDIT: Let’s not talk about my 24 day hiatus. Long story short, work has been wild and I’ve branched out and been a bit more social and been making friends… anyway, UNION BABY

Gonna blast through this as I’ve done a bunch of SQL stuff already…

## Task:

Connect to the above MySQL server with the ‘mysql’ tool, and find the number of records returned when doing a ‘Union’ of all records in the ‘employees’ table and all records in the ‘departments’ table.

`select * from employees UNION select dept_no, dept_name, 3, 4, 5, 6 from departments;`
## UNION Injection

EAAAAZYYYY

## Task:

Use the damn info they give you it’s easy

# Exploitation: Database Enumeration

Easy task… let me just finish this I’m bored haha.

Piece of cake

Great module, but I did so much stuff out of order this was a cake walk.
