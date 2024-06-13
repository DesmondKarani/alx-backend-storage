# 0x00. MySQL Advanced

## Overview

This project is focused on advanced SQL concepts using MySQL. It involves creating tables with constraints, optimizing queries, and implementing stored procedures, functions, views, and triggers. The project is designed to enhance your understanding of MySQL and its advanced features.

## Project Details

- **Domain:** Back-end, SQL, MySQL
- **Weight:** 1
- **Start Date:** June 12, 2024, 6:00 AM
- **End Date:** June 14, 2024, 6:00 AM
- **Checker Release:** June 12, 2024, 6:00 PM
- **Auto Review:** At the deadline

## Concepts

For this project, you should review the following concepts:

- Advanced SQL

## Resources

To aid your learning, refer to these materials:

- [MySQL Cheatsheet](#)
- [MySQL Performance: How To Leverage MySQL Database Indexing](#)
- [Stored Procedure](#)
- [Triggers](#)
- [Views](#)
- [Functions and Operators](#)
- [Trigger Syntax and Examples](#)
- [CREATE TABLE Statement](#)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](#)
- [CREATE INDEX Statement](#)
- [CREATE VIEW Statement](#)

## Learning Objectives

By the end of this project, you should be able to explain and implement the following:

1. How to create tables with constraints
2. How to optimize queries by adding indexes
3. What stored procedures and functions are, and how to implement them in MySQL
4. What views are, and how to implement them in MySQL
5. What triggers are, and how to implement them in MySQL

## Requirements

- All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30).
- All your files should end with a new line.
- All your SQL queries should have a comment just before (e.g., syntax above).
- All your files should start with a comment describing the task.
- All SQL keywords should be in uppercase (e.g., SELECT, WHERE).
- A `README.md` file at the root of the project folder is mandatory.
- The length of your files will be tested using `wc`.

## More Information

### Comments for Your SQL File

```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

### Using "Container-on-Demand" to Run MySQL

1. **Request a container**: Ubuntu 18.04 - Python 3.7
2. **Connect via SSH** or **WebTerminal**
3. **Start MySQL** in the container:
    ```bash
    $ service mysql start
    * MySQL Community Server 5.7.30 is started
    ```
4. **Execute SQL scripts**:
    ```bash
    $ cat 0-list_databases.sql | mysql -uroot -p my_database
    Enter password: 
    Database
    information_schema
    mysql
    performance_schema
    sys
    ```

### Importing a SQL Dump

```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
```

### Container Credentials

- **Username:** `root`
- **Password:** `root`
