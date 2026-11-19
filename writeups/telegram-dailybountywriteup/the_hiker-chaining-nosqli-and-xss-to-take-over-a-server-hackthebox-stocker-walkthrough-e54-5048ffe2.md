# Chaining NOSQLi and XSS to Take Over a Server — HackTheBox Stocker Walkthrough

- **Source URL:** https://medium.com/@The_Hiker/chaining-nosqli-and-xss-to-take-over-a-server-hackthebox-stocker-walkthrough-e549bf3f8bbf?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240905210926/https://medium.com/@The_Hiker/chaining-nosqli-and-xss-to-take-over-a-server-hackthebox-stocker-walkthrough-e549bf3f8bbf
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6292 (id 6292)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Chaining NOSQLi and XSS to Take Over a Server — HackTheBox Stocker Walkthrough

Hello again everyone, today we will take a look at the “Stocker” machine on HTB. Stocker is a fun and easy machine that involved a NoSQLi , XSS, and abusing sudo privileges to gain root access.

You too can hack this box and many more at [https://app.hackthebox.com/](https://app.hackthebox.com/) !

## Initial Scan

As always, we start off with an NMAP scan:

There are just two open ports — SSH on port 22 and HTTP on port 80.

We also see a redirect to “http://stocker.htb” , so we can add that to our /etc/hosts file and take a look at the website.

## Stocker.htb

This website is just static, nothing interesting about it’s functionality.

We do, however, learn the name of the head of the IT department at the bottom of the page:

This could become useful should we ever need to brute-force a login at some point.

## Subdomain Enumeration

Using GoBuster, we can look for hidden subdomains:

We find a subdomain called “dev.stocker.htb” , so we will again add that to our /etc/hosts file and take a look.

## dev.stocker.htb

We are presented with a login page.

Wappalyzer identifies this as a node.js app, using the Express Framework:

This can be validated by taking a look at the server response headers:

I spent some time trying to find hidden directories and files with gobuster, but couldn’t find anything.

This made it pretty clear that the login page is our only attack vector.

Trying some default credentials like “admin:admin” and “admin:password” doesn’t seem to work , so we are left with two choices:

Option 1: SQLi .

Option 2: Brute-forcing the login knowing that the username is likely “angoose” .

I typically like to leave brute-forcing as a last resort , so let’s try some SQLi !

## SQLi or…..NOSQLi ?!

First, let’s take a look at the request and response of a failed login:

Request:

Response:

If we add a single ‘ to the username, nothing changes:

Tried a few more payloads , but didn’t really get anywhere.

Before moving on to the brute-force, I recalled that I learned through previously completed CTFs that Node.js typically accepts POST requests in JSON format as well:

I highlighted in red the parts of the request that I changed. It’s important to change the content-type as well as the payload, so that the request will be a valid JSON POST request.

Response:

Nothing changes, which is actually a good thing in this case! We now know that the login page supports JSON.

This is important, because who said that the database is an SQL database? What if it’s a NOSQL database, like mongodb? Passing NOSQLi payloads in JSON format will allow us to avoid syntax errors more easily.

Let’s try our first payload, which is a query that should return true as long as a user exists:

`{“username”: {“$ne”: null}, “password”: {“$ne”: null} }`
YES! We bypassed the login altogether and are now redirected to /stock !

## Discovering XSS in a PDF generator

There is really not much functionality to this /stock endpoint other than placing orders. Let’s place an order for a few items and follow along the process to get a general understanding of how this website functions.

I added a few items to the basket, and now they are showing up in my cart:

Let’s hit “submit purchase” and see what happens:

We can see another JSON post request, this time to an API endpoint “/api/order” , the items I chose are detailed in this request.

The purchase is successful, and we now get to view our order at the link provided:

This is a PDF file that contains information about our order.

There are two things to note here:

- On the top right corner, we see that the purchaser is “Angoose”, indicating it’s his account we took over.
- The names of the items, the prices and the quantity, which were all passed in our request to the /api/order, are displayed in the file.

This opens up a new potential attack vector : What if we can change these values , and try XSS?

Since the “amount” and “price” values are integers, I’ll focus on the value of “title” , to avoid unnecessary errors.

Let’s try it out:

I Injected my payload, which will try to fetch a file off my kali machine if the attack is successful.

No errors, let’s view the PDF:

And if we check the listener…

It works! Note that the IP that reached back to us is that of the machine and not our own, indicating a successful XSS attack during the rendering of the PDF file.

## From XSS to Local File Disclosure

Normally when we think about XSS we think about stealing cookies.

But, we are already the user “angoose” and we don’t have any indication that there are other users on this website.

What if we try to include a file from the server in the “img” payload?

We can use the payload:

`<img src=file:///etc/passwd >`
Hmm…nothing, there must be another way to include a text file inside. Had to actually read a bit about this, and finally stumbled across a working payload!

`<script>document.write(‘<iframe src=\”file:///etc/passwd\” style=\”width:600px; height:1000px;\”></iframe>’);</script>`
And now, we have the /etc/passwd file in our pdf!

As expected, root and angoose are the only two users on this box.

## Hunting for Sensitive Files

We can read files, but how do we get into the machine?

Maybe we can read a private SSH key?


<script>document.write(‘<iframe src=\”file:///home/angoose/.ssh/id_rsa\” style=\”width:600px; height:1000px;\”></iframe>’);</script>
Nope.

The next logical step is to hunt for passwords within configuration files.

Since we know that there is a database at play here, maybe we can get the password used to connect to the DB and check for password-reuse?

But, where do we begin looking?

First, let’s cause the app to throw an error, as that might give us an indication to the location of this app within the machine.

I’ll add a random ‘,’ into the order request (any location will work — we are trying to get the app to crash):

Great! Looks like the app is located at /var/www/dev/ ! Since this is node.js, we can look for app.js or index.js within this directory!

index.js does the trick, and we find a plain-text password used for the DB connection:

Let’s check if we can SSH into the machine with this password:

We’re in! The first flag can be grabbed from /home/angoose/user.txt !

## Privilege Escalation

Let’s start with low hanging fruits, like sudo -l :

Looks like we can run any .js file using node, as long as it is inside /usr/local/scripts .

We can’t read any of these , and they all seem to be generating reports anyways, which isn’t really all that interesting to us:

So, maybe we can create another .js file here?

Nope. Gotta think harder.

Notice the asterisk ? This is our vector to privilege escalation!

It may look innocent, but this asterisk allows us to traverse our way up the directories and into /tmp, where we will create a malicious .js file!

Our sudo command will look like this:

`sudo node /usr/local/scripts/../../../tmp/root.js`
This command is valid with our current sudo configuration, because the path does indeed begin with /usr/local/scripts/ and ends with .js, it just so happens to be we traverse our way back up in the middle of it!

Let’s create /tmp/root.js:

`require(“child_process”).spawn(“/bin/bash”, {stdio: [0, 1, 2]})`
And we are R00T! The root flag is at /root/root.txt !

Thanks for reading, AND HAPPPY HACKING !
