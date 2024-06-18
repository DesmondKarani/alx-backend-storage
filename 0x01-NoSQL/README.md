# NoSQL and MongoDB Project

## Overview
This project introduces NoSQL databases with a focus on MongoDB. You'll learn about NoSQL principles, how MongoDB differs from SQL databases, and how to perform basic operations using MongoDB with Python.

## Learning Objectives
By the end of this project, you should be able to:
- Define NoSQL and understand its significance.
- Differentiate between SQL and NoSQL databases.
- Explain ACID properties.
- Describe document storage and various types of NoSQL databases.
- List the benefits of using a NoSQL database.
- Perform queries, insertions, updates, and deletions in a NoSQL database.
- Utilize MongoDB for database operations.

## Requirements
### General
- Understanding of NoSQL and its various types.
- Knowledge of MongoDB and how to use it for database operations.

### Technical
- **MongoDB Command File**
  - Files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB 4.2.
  - Each file should end with a new line and start with a comment (`// my comment`).
  - A `README.md` file at the root of the project is mandatory.
  - File lengths will be tested using `wc`.

- **Python Scripts**
  - Scripts will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7 and PyMongo 3.10.
  - Each file should end with a new line and start with the shebang (`#!/usr/bin/env python3`).
  - Code should adhere to the `pycodestyle` style (version 2.5.*).
  - Modules and functions must include documentation.
  - Ensure code is not executed when imported (`if __name__ == "__main__":`).

## Installation
To set up MongoDB 4.2 on Ubuntu 18.04:
```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
$ sudo service mongod start
$ mongo --version
MongoDB shell version v4.2.8
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
```
If you encounter issues with document creation, create the data directory:
```bash
$ sudo mkdir -p /data/db
```

## Usage
To start MongoDB:
```bash
$ service mongod start
```

To list databases:
```bash
$ cat 0-list_databases | mongo
```

## Notes
- Ensure all files follow the required formatting and documentation standards.
- The project will be auto-reviewed at the deadline, so adhere to the guidelines strictly. 

💯💯💯
