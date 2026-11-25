# From Directory Listing to Full Takeover

- **Source URL:** https://medium.com/@andrewdehghan/from-directory-listing-to-full-takeover-78b80b5ad1ea
- **Fetched from:** https://medium.com/@andrewdehghan/from-directory-listing-to-full-takeover-78b80b5ad1ea?source=rss-5ed6bef25c2f------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14914 (id 14914)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Amir Dehghan / Tue, 15 Sep 2026 21:40:08 GMT

I started with a simple check, and right away I noticed that the web application had **Directory Listing** enabled.

I thought, “Well, let’s see what’s inside.”

When I looked through the files, I realized that this wasn’t just a few ordinary files. The application’s **Source Code** was also exposed.

The first thing I did was download the entire available source code.

Then I started going through the files one by one to see if there was anything that shouldn’t have been exposed.

I came across an interesting file.

Inside it, I found that the application was connecting to a **remote MySQL database**, and the database connection credentials were included in the source code.

Things were getting interesting.

The database was hosted on AWS, and using the credentials I found in the source code, I was able to connect to the MySQL database.

Once I confirmed that the connection worked, the next step was obvious:

**Database Dump.**

I took a backup of the database and imported the dump into XAMPP and phpMyAdmin so I could inspect the data more easily.

This made the database much easier to navigate, so I started going through the tables and looking for anything interesting.

After some digging, I found information related to the **Admin** account.

At this point, I had the admin credentials.

But there was a problem.

The password wasn’t stored as a typical hash, and it looked different from what I expected.

So I went back to the source code.

While going through the files, I found one called enc\_dec.php.

After looking at the code, it became clear that the value stored in the database could be converted back to its original value. This wasn’t a typical one-way password hash; the application had its own encryption/decryption mechanism.

Thanks to the enc\_dec.php file, I was able to recover the password and use it for authentication.

Now I had valid credentials.

There was only one thing left:

**Where was the admin panel?**

I tried using Google Dorks and different search queries, but I couldn’t find it.

So I thought, “Let’s just open the IP directly.”

I opened the server IP over HTTP, and interestingly, the server redirected me directly to the **Admin Panel**.

I entered the credentials I had recovered and…

**I was in.**

At this point, the chain looked like this:

Directory Listing → Source Code → MySQL → Database Dump → Password Recovery → Admin Panel

But the story wasn’t over yet.

While reviewing the source code again, I found another file containing **Firebase** credentials.

This time, I checked the credentials and found that they could be used to authenticate to the associated project.

So what started as a simple Directory Listing eventually led me to the source code, the database, the Admin Panel, and finally Firebase.

The interesting part was that none of these steps were planned from the beginning.

Each finding simply led to the next one.

And that’s when I realized:

**The Directory Listing was only the beginning.**
