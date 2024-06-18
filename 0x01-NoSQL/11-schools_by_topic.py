#!/usr/bin/env python3
"""a Python function that returns the list of school having a specific topic"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    :param mongo_collection: The pymongo collection object
    :param topic: The topic searched
    :return: List of schools having the specific topic
    """
    return list(mongo_collection.find({"topics": topic}))
