# Redis Basic Project

## Overview

This project focuses on using Redis for basic operations and as a simple cache. The goal is to familiarize yourself with Redis commands and how to integrate Redis with Python. 

## Project Timeline

- **Start Date**: June 19, 2024, 6:00 AM
- **End Date**: June 20, 2024, 6:00 AM
- **Checker Release**: June 19, 2024, 12:00 PM
- **Auto Review**: Will be launched at the deadline

## Learning Objectives

- Understand how to use Redis for basic operations
- Learn how to implement Redis as a simple cache

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- Your code should follow the `pycodestyle` style (version 2.5)
- All modules should have documentation
- All classes should have documentation
- All functions and methods should have documentation
- All functions and coroutines must be type-annotated

## Resources

Refer to the following resources for guidance:

- [Redis Crash Course Tutorial](#)
- [Redis commands](#)
- [Redis python client](#)
- [How to Use Redis With Python](#)

## Setup Instructions

### Install Redis on Ubuntu 18.04

1. Install Redis server:
   ```sh
   sudo apt-get -y install redis-server
   ```
2. Install Redis Python client:
   ```sh
   pip3 install redis
   ```
3. Configure Redis to bind to localhost:
   ```sh
   sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
   ```

### Using Redis in a Container

1. Start the Redis server:
   ```sh
   service redis-server start
   ```

## Code Documentation

Ensure all modules, classes, and functions/methods have proper documentation explaining their purpose. Example commands to check documentation:
- For modules:
  ```sh
  python3 -c 'print(__import__("my_module").__doc__)'
  ```
- For classes:
  ```sh
  python3 -c 'print(__import__("my_module").MyClass.__doc__)'
  ```
- For functions:
  ```sh
  python3 -c 'print(__import__("my_module").my_function.__doc__)'
  python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
  ```

## Style and Type Annotations

Ensure your code adheres to `pycodestyle` guidelines and that all functions and coroutines are type-annotated.
