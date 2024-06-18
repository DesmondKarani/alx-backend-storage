#!/usr/bin/env python3
"""a Python function that changes all topics of a school document based on the
name"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
    mongo_collection (pymongo.collection.Collection):
    The collection to update.
    name (str): The name of the school to update.
    topics (list): The list of topics to update in the document.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
