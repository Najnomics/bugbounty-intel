# Sql Injection for Beginners using Sqlmap Part -2

- **Source URL:** https://medium.com/@RajneeshKarya/sql-injection-for-beginners-using-sqlmap-part-2-53e9775b67f5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221016114711/https://medium.com/@RajneeshKarya/sql-injection-for-beginners-using-sqlmap-part-2-53e9775b67f5
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/486 (id 486)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Sql Injection for Beginners using Sqlmap Part -2

Hello friends, I’m Rajneesh Kumar Arya back again with my new blog on SQL Injection. If you haven’t checked out [my first blog](/@RajneeshKarya/sql-injection-for-beginners-using-sqlmap-36e091e8a070) so first take a look at that and then you can continue with this one so without further do let’s power on your system, get some coffee or tea and get jump into it.

In the previous blog, we learn how to enumerate the database of a website having a POST request method with [sqlmap](https://github.com/sqlmapproject/sqlmap) today we are going to do the same thing but with a different method so first of all we need a [sample website.](https://juice-shop.herokuapp.com/#/)

So, our sample website is having a search bar here so let’s try our technique here.

DISCLAIMER: Do not use these techniques to hack anyone try these in your own lab environment.


I put a random string in the search parameter and hit ENTER then it appears in the URL which means it is having GET method to request the server.

As we found our endpoint. So, to test the vulnerability of SQL injection let’s fireup our tool called [bursuite](https://portswigger.net/burp/communitydownload) and intercept the request.

Now press Ctrl + R to send the request to Repeater where we can modify the request.

Now we need to add a ‘test’ in the search parameter and send the request.

Here we got the response of the sever in the response section with a 200 OK response code which means our parameter was sent to the server without any error.

From now the main games start, we need to modify the request and again send it to the server and check its behavior against this request. I’m adding a ‘ in front of our parameter value test and sending it.

And we got an error with the 500 Internal Server Error response code which confirm that here is the vulnerability of SQL Injection.

Hey, do you know the difference between a developer and Hacker? well, the developer hates the error but a hacker loves it so in this case also we got an error which is a good thing for us but not for developers.


We confirmed that our sample website’s search parameter is vulnerable to SQL Injection so now we have to just exploit that vulnerability. To do this we need to call our tool sqlmap.

Now open your terminal or command prompt and type the following command but before that copy the request from the burp suite and paste to any text editor and modify it by adding an [Asterisk](https://en.wikipedia.org/wiki/Asterisk) and save it, we had done the same step in the [previous blog](/@RajneeshKarya/sql-injection-for-beginners-using-sqlmap-36e091e8a070) also, go and check out.

`python3` **sqlmap.py** -r **/home/kairaj5456/Desktop/request.txt** --dbs --level 5
Here, I use ‘— dbs’ for enumerating database and ‘— level’ to increase the aggressiveness of the attack now hit ENTER and take some tea or coffee because it takes time and more than the previous one.

And you can see we got database information and to know what inside database just type this command and take a coffee break.

`python3` **sqlmap.py** -r **/home/kairaj5456/Desktop/request.txt** --tables --threads 10
I use ‘— tables’ to enumerating all the tables present in this database ,‘ — threads’ to increase the speed of enumeration and I got this juicy information.

As you can see I got 20 Tables but I’m only interested in the ‘Users’ table. So, to see what is inside that table you need to just type this command and hit ENTER.

`python3` **sqlmap.py** -r **/home/kairaj5456/Desktop/request.txt**  --threads 10 -T Users --columns I use ‘-T’ to select the table name and ‘ — columns’ to enumerating columns and I got this information.

And again it gave me a lot of data but I’m only interested in ‘email’ and ‘password’ because I wanted to see how many users are there in this website and their password so I can log into it. So, to do so you need type this command and press ENTER.

`python3` **sqlmap.py** -r **/home/kairaj5456/Desktop/request.txt**  --threads 10 -T Users -C email,password --dump
I use ‘-C’ to selecting the columns and ‘ — dump’ to dump all the data from these columns and it takes long time to dump all the emails and password so again a coffee break and you’re good to go.

We got this whole information from the columns but it is useless because you can see passwords are in encrypted form and we cannot use these to gain access to the account. So, what we can do now.

Now, I’ll show you how you can gain access to the accounts with their emails only.

So let’s hack one of the email from our list I choose ‘[hariprakash0902@gmail.com](mailto:hariprakash0902@gmail.com)’ as an email now we have to go to login page of this website.

And enter the email in the email parameter and anything in the password section and you can login to that account. Its seems like a joke that how we can login into someones account by putting anything in the password but the reality is its possible and I’m gonna show how it works.

`'UNION SELECT * FROM Users WHERE email='hariprakash0902@gmail.com'--`
So, copy the above thing and paste into the email parameter and type anything in the password parameter and press Login…….

BOOM! we are in….we hack the username and get access to his account.

This is how you can hack account using SQL Injection and WAIT!!! I have challenge for you hack [this website](http://testfire.net/) and try to login.

Till then keep learning, keep exploring and do HACKING.
