#!/usr/bin/env python3
"""a Python function that inserts a new document in a collection based on
kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
    mongo_collection (pymongo.collection.Collection):
    The collection to insert the document into.
    kwargs: The document data.

    Returns:
    ObjectId: The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
