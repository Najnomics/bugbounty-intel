# SQL Injection

- **Source URL:** https://medium.com/@hamzamabdulrhman/sql-injection-a-beginners-guide-part-1-0bdb41ec8609?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251026065850/https://medium.com/@hamzamabdulrhman/sql-injection-a-beginners-guide-part-1-0bdb41ec8609
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8369 (id 8369)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection: A Beginner’s Guide PART 1

## Introduction

Before diving into what SQL Injection is, how it works, and how to exploit it, we need to understand some basics. These include:

- What is a database?
- Types of databases.
- The difference between databases.
- Database optimization.
- Simple basics of SQL language.

**Let’s get started!**

## What is a Database?

A database is a collection of tables (or sometimes just one table) that stores large amounts of data in an organized way. Sometimes, data can also be stored in files like JSON instead of tables.

## Why do we use databases?

Imagine you have thousands or even millions of records, and you need to find information about a specific product in an inventory. Searching manually through all that data would take forever.

That’s why we use databases. They organize data into tables, and with a simple query, you can find the exact information you’re looking for.

## Types of Databases

There are two main types of databases:

1. **SQL (Relational):**

- Data is stored in structured tables.
- Tables can be linked together.

**2. NoSQL (Non-Relational):**

- Data is stored in files, often in JSON format.
- More flexible but less structured.

## SQL vs. NoSQL:

## SQL Basics

SQL (Structured Query Language) is used to interact with relational databases. You can use SQL commands to add, delete, update, or view data.

## Most Common SQL Commands:

## 1. SELECT

This command is used to view data from a table.

- Syntax:

`SELECT column_name FROM table_name;`
- Examples:
To display all data from a table called`employees`:

`SELECT * FROM employees;`
- To display only phone numbers:

`SELECT phone_number FROM employees;`
## 2. UPDATE

This command updates existing data in a table.

- Syntax:

`UPDATE table_name   SET column1 = value1, column2 = value2   WHERE condition;`
Example:

Change the salary of an employee with ID = 5 to 7000:

`UPDATE employees   SET salary = 7000   WHERE employee_id = 5;`
## 3. DELETE

This command removes data from a table.

- Syntax:

`DELETE FROM table_name WHERE condition;`
- Example:
Delete the record of a product with ID = 101:

`DELETE FROM products   WHERE product_id = 101;`
## 4. INSERT INTO

This command adds new data to a table.

- Syntax:

`INSERT INTO table_name VALUES (value1, value2, value3);`
- Example:
Add a new customer to the`customers` table:

`INSERT INTO customers   VALUES (25, 'John Doe', 'john.doe@example.com');`
## 5. CREATE DATABASE

This command creates a new database.

- Syntax:

`CREATE DATABASE database_name;`
- Example:

`CREATE DATABASE online_store;`
## 6. CREATE TABLE

This command creates a new table in a database.

- Syntax:

`CREATE TABLE table_name (column1 datatype, column2 datatype);`
- Example:

`CREATE TABLE Orders (OrderID int,ProductName varchar(255),Quantity int,Price decimal(10, 2),OrderDate date);`
## 7. ALTER TABLE

The `ALTER TABLE` command is used to add, modify, or delete columns from a table.

### Syntax:

- **To Add a Column:**

`ALTER TABLE table_name ADD column_name datatype;`
- **To Drop a Column:**

`ALTER TABLE table_name   DROP COLUMN column_name;`
- **To Rename a Column:**

`ALTER TABLE table_name   RENAME COLUMN old_name TO new_name;`
### Example:

- Add a column named `PhoneNumber` to the `Employees` table:

`ALTER TABLE Employees   ADD PhoneNumber VARCHAR(20);`
- Remove the column `Age` from the `Employees` table:

`ALTER TABLE Employees   DROP COLUMN Age;`
- Rename the column `FirstName` to `GivenName` in the `Employees` table:

`ALTER TABLE Employees   RENAME COLUMN FirstName TO GivenName;`
## 8. DROP TABLE

The `DROP TABLE` command is used to completely delete a table from the database, including all the data stored in it.

### Syntax:

`DROP TABLE table_name;`
### Example:

- Delete the `Orders` table from the database:

`DROP TABLE Orders;`
## 9. CREATE INDEX

The `CREATE INDEX` command is used to create an index on a table, which helps improve query performance when searching for data.

### Syntax:

```
CREATE INDEX index_name  
ON table_name (column1, column2);
```
### Example:

- Create an index on the `LastName` and `FirstName` columns in the `Customers` table:

`CREATE INDEX idx_name ON Customers (LastName, FirstName);`
## 10. UNION

The `UNION` command is used to combine the results of two SELECT statements into a single result set. Duplicate rows are automatically removed.

### Syntax:

```
SELECT column_name(s) FROM table1  
UNION  
SELECT column_name(s) FROM table2;
```
### Example:

- Combine the cities from the `Customers` and `Suppliers` tables, sorted alphabetically:

`SELECT City FROM Customers   UNION   SELECT City FROM Suppliers   ORDER BY City;`
## 11. DROP INDEX

The `DROP INDEX` command is used to delete an index from a table.

### Syntax:

`DROP INDEX index_name ON table_name;`
### Example:

- Delete the index `idx_name` from the `Customers` table:

`DROP INDEX idx_name ON Customers;`
## What’s Next PART?

- A brief explanation of SQL Injection and how it works.
- How to protect your system from it.

## Conclusion

This was a quick overview of SQL and its most important commands. In the next part, we’ll dive deeper into SQL Injection, how attackers exploit it, and how to secure your applications.
