# How I found an IDOR that led to sensitive information leak?

- **Source URL:** https://medium.com/@tusharsaini484/how-i-found-an-idor-that-led-to-sensitive-information-leak-6055bb121f8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260226041716/https://medium.com/@tusharsaini484/how-i-found-an-idor-that-led-to-sensitive-information-leak-6055bb121f8
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1764 (id 1764)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I found an IDOR that led to sensitive information leak?

Finding your first bug can be a daunting task. It requires a lot of patience, persistence, and dedication. After finding a few P4 bugs, I wanted to hunt for more severe bugs. In this blog post, I’ll be sharing my experience of finding my first major bug, which was an IDOR (Insecure Direct Object Reference) vulnerability.

Before going any further into the blog, let’s under what is an IDOR vulnerability.

Insecure direct object references (IDOR) are a cybersecurity issue that occurs when a web application developer uses an identifier for direct access to an internal implementation object but provides no additional access control and/or authorization checks. It is a type of access control vulnerability that arises when an application uses user-supplied input to access objects directly without validating/checking it.

Now let’s understand how the IDOR happens:

This type of vulnerability can occur when a web server receives user-supplied input to retrieve objects (files, data, documents), too much trust has been placed on the input data, and it is not validated on the server side to confirm the requested object belongs to the user requesting it.

Let’s take an example:

Let’s say that the web application displays transaction details using the following URL: [https://www.example.com/transaction.php?id=8000](https://www.example.com/transaction.php?id=8000)

A malicious hacker could try to substitute the id parameter value 8000 with other similar values, for example, [https://www.example.com/transaction.php?id=8001](https://www.example.com/transaction.php?id=8001)

The 8001 transactions could be valid transaction belonging to another user. The malicious hacker should not be allowed to see it. However, if the developer made an error, the attacker would see this transaction and hence we would have an insecure direct object reference(IDOR) vulnerability.

Now let’s come back to how I explored my hostel’s website and got an IDOR:

I was learning Web App Security, and during that time the most interesting bug I found was the IDOR vulnerability. So I started searching for websites where I could hunt bugs and specifically IDOR.

Then I came across the website, let it be [hostel.com](http://hostel.com) 🙂

I manually explored the website to find parameters for XXS, I found very few but I could not exploit it. Interestingly, I found an id parameter by capturing a specific request in burpsuite. The ID parameter was named Student ID. After I saw the parameter, the first thing after failing XXS, I had in my mind was to test for IDOR.

That student ID was for retrieving the data of the logged-in user. But you could manipulate the parameter by intercepting the request through burpsuite. I did the same. I changed the original number to another random number. And FORWARDED the request.

There we go, I had a blank page with some HTML and Javascript code. Now I went through that code and inside the code, there were all the private details of the student that the ID belonged to. Private details such as name, mobile number, hostel room number, course details, email, permanent address, parent’s name, and occupation.

Then I tried some more random numbers just to make sure that it’s valid for all and not for only a few. And I could access 3500+ students’ data that live at the hostel.

So basically the IDOR lead to Sensitive Information Disclosure of all the students.

The main reason for this IDOR vulnerability.

- The application was using user-supplied input to retrieve data without VALIDATING it at the server side for authorization.

It was not listed on any bug bounty platform OBVIOUSLY, so I did not get any bounty for it. But it was an amazing experience to get an IDOR!

Thank you for reading the blog. If you found it informative, please appreciate on [coffee](https://www.buymeacoffee.com/ryzin) :)

Until the next one comes: **KEEP LEARNING — KEEP IMPROVING.**
