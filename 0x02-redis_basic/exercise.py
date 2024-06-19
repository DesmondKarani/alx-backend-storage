#!/usr/bin/env python3
"""a Cache class. In the __init__ method,
store an instance of the Redis client as a private variable named _redis
(using redis.Redis()) and flush the instance using flushdb"""

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """Initialize the Cache class with a Redis client and flush
        the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis and return the key.

        Args:
            data: The data to be stored. Can be str, bytes, int, or float.

        Returns:
            The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
