# IDOR “Insecure direct object references”, my first P1 in Bugbounty

- **Source URL:** https://medium.com/@jedus0r/idor-insecure-direct-object-references-my-first-p1-in-bugbounty-fb01f50e25df?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221211075800/https://medium.com/@jedus0r/idor-insecure-direct-object-references-my-first-p1-in-bugbounty-fb01f50e25df?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/117 (id 117)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR “*Insecure direct object references”*, my first P1 in Bugbounty

First Whoami : Dris R. A Security Researcher, Penetration Tester from Paris ,France.

## ***France. Summer 2022***

Normally in summer, people chose to go in holiday in their free time, but for my part I was focused in security research, it has now become my playground. I also decided to specialize in web security research to have the maximum skills and therefore have a stronger impact in bug bounty programs or with my clients during web penetration testing.

*In this post i will explain you technically, how i found my first P1 in bugbounty, in-fact in the same program i found 2 IDOR.*

\- The first one as P3 : I was able to delete the CMS of all their customers.

\- The second one as P1 : I was able to delete all the users of the website and in the meantime collect their personal data (Email, Phone, Name..)


*Note : Vulnerabilities are assessed and then categorized between P1 (most severe) to P5 (least severe) which determines how much an organization should reward the researcher who reported it.*

# ***IDOR ? Ok but what is it finally ?***

An IDOR “Insecure direct object references” flaw allows an attacker to gain unauthorized access to resources or perform actions on a web application.


This is accomplished by altering the request parameters supplied to the server while retrieving objects (such as documents, files, and data).

When there is a lack of server-side validation and a request is completed without validating whether the object being requested belongs to the user requesting it, this is possible.

*Non-technical example for understanding :*

You are connected to your bank’s website , and logically you are only autorized to make transfers from accounts that belong to you and therefore use your own money.

But with IDOR vulnerability you can potentialy make transfers from accounts that not belong to you, and therefore use money that is not yours and steal it by changing just a single number in the URL.

# Write UP

While hunting in a program i reported some P4 , and i say to myself i’m bored to report only P4 , let’s search now for critical vulnerability in the same program. As we say in French “On ne sait jamais, sur un malentendu ca peut marcher” which can be translated as nothing ventured, nothing gained.

*I started searching more about the application. I wanted to find one IDOR because the impact is high.*


So I log in again in the application and capture all the requests with my proxy.

*Now the questions that i have in my mind are :*

- *How they identified us ?*
- *What are the sensitive features of the site ?*
- *What are our restrictions ?*

I checked all the HTTP requests that i have in my proxy and found the response for my first question *they identify us with a number ID.*

In my head I map the website (Code, Endpoint, Technologies) and build their backend. I try to think about mistakes that the developers could have made.

They use an API, so i send all API requests which contain my number ID to repeater in my proxy.

The website allow us to create and manage a CMS (*Content Management System)*, so first i will play with this fonctionality, and see if we can access to something that is forbidden.

1. I have this request in front of me , A PUT request with my own test ID 405.

2\. What will happened if we modify the ID to another value like “419” and not 405, are we going to bypass the security of the site and access prohibited data *?*

PUT /api/v1/cms/***419*** HTTP/2


We have received a HTTP 200 OK !!


*So it’s works we can access to others CMS, when normally we are not allowed to do it.*

*But can we go further and increase the impact ?*


3\. Like any hacker I test all HTTP methods,

And when I tried the DELETE method I received a *200 OK.* This means that the CMS is deleted.

4\. So i tried again and send a PUT request to the ressource, and i received this time a 404 not found, it looks like the CMS is removed from the application as we can’t longer access this data.

## POC of cms removal

5\. I go to the url of the CMS to see it with my own eyes and yes the site is no longer accessible..

*Yes we managed to delete CMS that did not belong to us. And this may have a financial impact as the service is no longer available.*


# So the bugbounty plateform accepted the vulnerability as P3

# FROM P3 TO P1

*The delete method was effective and maybe it can affect other resources. Let’s take a look*

1. First my own test account. are we authorized to access the data of other users ?

I send a GET request to the server, with my own test ID 19795.

2\. After I changed the number ID to 19782 (Other user), in the case that we are authorized to do something.

GET /api/v1/users/19782


But no, we are not authorized this time…

3\. We are starting to understand how the application works, so let’s test the DELETE method this time. If it worked once, we never know maybe it may work again.

*I change the method to DELETE, send the request, and i received this time a 200 OK.*

## ***It seems that it worked..***

## 4. POC of user deletion

I just send again the DELETE request, and received a 404 not found so the user no longer exists in the website.

*It’s ok, we have deleted the user, collect personal information, and we can do it for all users of the website, so yes it’s critical.*


# The bugbounty plateform accepted the vulnerability as P1 this time

*I DID IT !! I FOUND MY FIRST P1 WITH MY NEW METHODOLOGY “Jedus0r’s methodology”*

Thanks for reading, and see you soon for a new adventure.


**Contact :**

**Linkedin : https://www.linkedin.com/in/drisr53/**

**Website : https://jedus0r.github.io./**
