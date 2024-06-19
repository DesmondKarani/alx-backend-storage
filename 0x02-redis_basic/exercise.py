#!/usr/bin/env python3
"""a Cache class. In the __init__ method,
store an instance of the Redis client as a private variable named _redis
(using redis.Redis()) and flush the instance using flushdb"""

import redis
import uuid
from typing import Union, Callable, Optional
import functools


class Cache:
    def __init__(self):
        """Initialize the Cache class with a Redis
        client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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

    def get(
            self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key: The key under which the data is stored.
            fn: Optional; A callable to convert the data.

        Returns:
            The retrieved data, optionally converted.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Retrieve a string from Redis.

        Args:
            key: The key under which the data is stored.

        Returns:
            The retrieved string.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve an integer from Redis.

        Args:
            key: The key under which the data is stored.

        Returns:
            The retrieved integer.
        """
        return self.get(key, int)


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times a method is called.

    Args:
        method: The method to be decorated.

    Returns:
        The wrapped method with call count functionality.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to count calls."""
        key = f"{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper
